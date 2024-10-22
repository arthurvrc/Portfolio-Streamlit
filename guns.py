import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import squarify 
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
import statsmodels.api as sm
from wordcloud import WordCloud
import pycountry



df = pd.read_csv('guns.csv', sep=',', encoding='ISO-8859-1')



# Page title and introduction
st.title("Guns Dataset Analysis")
st.write("""
Welcome to the Guns Dataset Analysis project. This dataset contains a variety of information about firearms, including their type, manufacturer, country of origin, and technical specifications. 
In this project, we will explore various aspects of the dataset through visualizations, aiming to uncover hidden insights and present a comprehensive analysis.
""")

# Sidebar with a short summary of the project and page navigation
st.sidebar.title("Project Overview")
st.sidebar.write("""
In this analysis, we will explore the following sections:
- **General Presentation**: Overview of the dataset, its structure, and key attributes.
- **Temporal Analysis**: Examining trends over time.
- **Technical Characteristics**: Insights into the technical features of the firearms.
- **Correlations**: Relationships between different attributes.
- **Rankings**: Classifying firearms based on specific criteria.
- **Advanced**: In-depth analysis, advanced techniques, and complex visualizations.
""")

# Tab navigation for different sections
tabs = st.tabs(["Introduction", "General Presentation", "Temporal Analysis", 
                "Technical Characteristics", "Correlations", "Rankings", "Advanced"])

# Introduction page
with tabs[0]:
    st.header("Introduction")
    st.write("""



Welcome to the Guns Dataset Analysis project, where we explore the dataset titled **Référentiel Général des Armes**. This dataset, which can be found on the French government's open data platform [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/referentiel-general-des-armes/), contains detailed information about various firearms, including their type, manufacturer, and technical characteristics. It was last updated on October 4, 2024, and includes 23 columns and 59,031 rows of data.

I chose this dataset because of the challenge and fun it presented in terms of data exploration, visualization, and analysis. However, I would like to make it clear that I do not promote the use of firearms in any way and firmly stand against violence. This project is purely for academic purposes and does not intend to glorify or support gun use.

---

### Classes of Data (Columns)

In this project, we will focus on the following key attributes (classes) of the dataset:
- **referenceRGA**: The unique reference number for each firearm in the dataset.
- **famille**: The family or category of the firearm (e.g., shotgun, rifle).
- **typeArme**: The specific type of firearm.
- **marque**: The brand or manufacturer.
- **modele**: The model of the firearm.
- **fabricant**: The name of the manufacturer.
- **paysFabricant**: The country where the firearm was manufactured.
- **modeFonctionnement**: The operating mechanism of the firearm (e.g., semi-automatic).
- **systemeAlimentation**: The feeding system used in the firearm.
- **longueurArme**: The length of the firearm in millimeters.
- **capaciteHorsChambre**: The capacity of the firearm excluding the chamber.
- **capaciteChambre**: The chamber capacity.
- **calibreCanonUn**: The caliber of the first barrel (if applicable).
- **modePercussionCanonUn**: The type of percussion for the first barrel.
- **typeCanonUn**: The type of the first barrel (e.g., rifled).
- **longueurCanonUn**: The length of the first barrel.
- **armeSemiAutoApparenceArmeAuto**: Indicates whether the semi-automatic firearm has an appearance similar to an automatic weapon.
- **classementFrancais**: French classification of the firearm.
- **classementEuropeen**: European classification of the firearm.
- **prototype**: Indicates whether the firearm is a prototype.
- **visible**: Specifies whether the firearm is visible in public records.
- **dateCreaRGA**: The creation date of the firearm's entry in the database.
- **dateMajRGA**: The date of the last update of the firearm's entry.

---

Throughout this analysis, we will explore these attributes to extract meaningful insights, examine trends, and build a comprehensive understanding of the firearms dataset.
    """)



# General Presentation page with visualization
with tabs[1]:
    st.header("General Presentation")

#VISU 1
    st.subheader("Distribution of Firearm Families")
    st.write("""
    This histogram shows the distribution of the different firearm families in the dataset. 
    By visualizing the frequency of each family, we can identify which types of firearms are more common.
    """)

    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(y="famille", data=df, palette="viridis", order=df["famille"].value_counts().index)
    
    # Adding counts to the bars
    for p in ax.patches:
        count = int(p.get_width())  # Get the count
        ax.annotate(f'{count}', (p.get_width() + 100, p.get_y() + p.get_height() / 2), 
                    va='center')  # Annotate the count at the end of each bar

    plt.title('Distribution of Firearm Families')
    plt.xlabel('Count')
    plt.ylabel('Firearm Family')
    st.pyplot(plt)

#VISU 2
 

    # Short description of the visualization
    st.subheader("Distribution of Firearm Types by Family")
    st.write("""
    This bar plot shows the distribution of firearm types within each family. The different colors represent the firearm families, 
    and this allows us to see how types are distributed across families.
    """)

    # Enlarging the figure
    plt.figure(figsize=(16, 10))  # Increased figure size for clarity

    # Plotting the bar plot with increased font sizes
    ax = sns.countplot(y="typeArme", data=df, hue="famille", palette="viridis",
                       order=df["typeArme"].value_counts().index)

    # Adding counts to the bars with increased font size
    for p in ax.patches:
        count = int(p.get_width())  # Get the count
        ax.annotate(f'{count}', (p.get_width() + 50, p.get_y() + p.get_height() / 2),
                    va='center', fontsize=12)  # Increased font size for annotations

    # Move the legend to the bottom right with increased font size
    ax.legend(title="Firearm Family", loc='lower right', bbox_to_anchor=(1, 0), fontsize=12, title_fontsize=14)

    # Adjusting the font sizes for the title, labels, and ticks
    plt.title('Distribution of Firearm Types by Family', fontsize=18)
    plt.xlabel('Count', fontsize=14)
    plt.ylabel('Firearm Type', fontsize=14)

    # Increase tick label font size for better readability
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    # Displaying the plot
    st.pyplot(plt)

    top_families = df['typeArme'].value_counts().nlargest(5)

    # Pie chart
    plt.figure(figsize=(8, 8))  # Increase the figure size for clarity

    # Create the pie chart
    plt.pie(top_families, labels=top_families.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis', 5))

    # Add a title
    plt.title("Top 5 Firearm Families by Occurrence", fontsize=16)

    # Display the pie 
    st.pyplot(plt)


#VISU 3
    st.subheader("Distribution of Firearms by Brand")

    # Short description of the bar chart
    st.write("""
    This bar chart displays the distribution of firearms by brand, 
    highlighting the relative frequency of different brands in the dataset.
    """)

    # Group by brand and get their occurrences
    brand_counts = df['marque'].value_counts()

    # Create a horizontal bar chart
    plt.figure(figsize=(12, 8))  # Set the figure size
    bars = plt.barh(brand_counts.index[:10], brand_counts.values[:10], color='skyblue')  # Show top 10 brands

    # Add a title and labels
    plt.title("Distribution of Firearms by Brand (Top 10)", fontsize=16)
    plt.xlabel("Number of Firearms", fontsize=14)
    plt.ylabel("Brand", fontsize=14)

    # Add counts to the right of the bars
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                 int(bar.get_width()), va='center', fontsize=12)

    # Display the bar chart
    st.pyplot(plt)

#VISU 4
    st.subheader("Distribution of Firearms by Manufacturer")

    # Short description of the pie chart
    st.write("""
    This pie chart illustrates the distribution of firearms by manufacturer, 
    showcasing the proportion of firearms produced by the leading manufacturers in the dataset.
    """)

    # Group by manufacturer and get their occurrences
    manufacturer_counts = df['fabricant'].value_counts()

    # Select the top 5 manufacturers
    top_manufacturers = manufacturer_counts.head(5)

    # Create a pie chart
    plt.figure(figsize=(10, 8))  # Set the figure size
    plt.pie(top_manufacturers, labels=top_manufacturers.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
    
    # Add a title
    plt.title("Distribution of Firearms by Manufacturer", fontsize=16)

    # Display the pie chart
    st.pyplot(plt)


#VISU 5
    st.subheader("Manufacturing Countries Map")

    # Short description of the map
    st.write("""
    This world map displays the manufacturing countries of firearms, 
    highlighting the number of firearms produced in each country.
    """)

    # Group by country and count the number of firearms produced
    country_counts = df['paysFabricant'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Number of Firearms']

    # Create a world map with markers
    fig = px.choropleth(country_counts, 
                        locations='Country',
                        locationmode='country names',
                        color='Number of Firearms',
                        hover_name='Country',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title='Number of Firearms Produced by Country',
                        labels={'Number of Firearms': 'Number of Firearms'},
                        projection='natural earth')

    # Update layout for better appearance
    fig.update_layout(title_font_size=20,
                      geo=dict(showland=True, landcolor='lightgray'))

    # Display the map
    st.plotly_chart(fig)



with tabs[2]:
    st.header("Temporal Analysis")
    

#VISU 6
    st.subheader("Evolution of Firearm Creations Over Time")

    # Short description of the line plot
    st.write("""
    This line plot shows the evolution of firearm creations over the years, 
    illustrating the number of firearms created each year.
    """)

    # Convert 'dateCreaRGA' to datetime and extract the year
    df['dateCreaRGA'] = pd.to_datetime(df['dateCreaRGA'], errors='coerce')
    df['Year'] = df['dateCreaRGA'].dt.year

    # Count the number of firearms created per year
    yearly_counts = df['Year'].value_counts().reset_index()
    yearly_counts.columns = ['Year', 'Number of Firearms']
    yearly_counts = yearly_counts.sort_values('Year')

    # Create a line plot
    fig = px.line(yearly_counts, 
                  x='Year', 
                  y='Number of Firearms', 
                  title='Number of Firearms Created Over Time',
                  labels={'Number of Firearms': 'Number of Firearms'},
                  markers=True)

    # Update layout for better appearance
    fig.update_layout(title_font_size=20,
                      xaxis_title='Year',
                      yaxis_title='Number of Firearms',
                      xaxis=dict(tickmode='linear'))

    # Display the line plot
    st.plotly_chart(fig)


#VISU 7
    st.subheader("Comparison of Creation and Update Dates")

    # Short description of the scatter plot
    st.write("""
    This scatter plot compares the creation dates and the last updated dates of firearms. 
    Each point represents a firearm, showing its creation date on the x-axis and 
    the last updated date on the y-axis.
    """)

    # Convert 'dateCreaRGA' and 'dateMajRGA' to datetime
    df['dateCreaRGA'] = pd.to_datetime(df['dateCreaRGA'], errors='coerce')
    df['dateMajRGA'] = pd.to_datetime(df['dateMajRGA'], errors='coerce')

    # Drop rows with missing values in creation or update dates
    scatter_df = df.dropna(subset=['dateCreaRGA', 'dateMajRGA'])

    # Create a scatter plot
    fig = px.scatter(scatter_df,
                     x='dateCreaRGA', 
                     y='dateMajRGA',
                     title='Comparison of Creation and Update Dates',
                     labels={'dateCreaRGA': 'Creation Date', 'dateMajRGA': 'Update Date'},
                     hover_data=['referenceRGA'])  # Add reference number to hover information

    # Update layout for better appearance
    fig.update_traces(marker=dict(size=5, opacity=0.7))
    fig.update_layout(title_font_size=20,
                      xaxis_title='Creation Date',
                      yaxis_title='Update Date')

    # Display the scatter plot
    st.plotly_chart(fig)


#VISU 8
    st.subheader("Update Rate of Firearms")

    # Short description of the histogram
    st.write("""
    This histogram displays the number of firearms updated each year. 
    It provides insights into the frequency of updates over time.
    """)

    # Convert 'dateMajRGA' to datetime
    df['dateMajRGA'] = pd.to_datetime(df['dateMajRGA'], errors='coerce')

    # Extract year from 'dateMajRGA'
    df['year_updated'] = df['dateMajRGA'].dt.year

    # Count occurrences of updates for each year
    update_counts = df['year_updated'].value_counts().sort_index()

    # Create a histogram
    fig = go.Figure()

    # Add a bar trace
    fig.add_trace(go.Bar(
        x=update_counts.index, 
        y=update_counts.values,
        marker=dict(color='royalblue'),
        text=update_counts.values,  # Text labels for bars
        textposition='outside'       # Positioning of text labels
    ))

    # Update layout for better appearance
    fig.update_layout(
        title='Number of Firearms Updated per Year',
        xaxis_title='Year',
        yaxis_title='Number of Updates',
        title_font_size=20
    )

    # Display the histogram
    st.plotly_chart(fig)


#VISU 9 
    # à trouver 
    





with tabs[3]:

    st.header("Temporal Analysis")

    st.subheader("Density Distribution of Firearm Lengths")

    # Short description of the KDE plot
    st.write("""
    This KDE plot visualizes the density distribution of firearm lengths. 
    """)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create histogram using Seaborn
    sns.histplot(df['longueurArme'], 
                 bins=50,    # Number of bins
                 kde=False,  # Disable KDE line
                 color="lightblue", 
                 ax=ax)

    # Set x-axis limit to 0-2000 cm
    ax.set_xlim(0, 2000)

    # Set titles and labels
    ax.set_title('Firearm Length Distribution', fontsize=16)
    ax.set_xlabel('Firearm Length (cm)', fontsize=12)
    ax.set_ylabel('Number of Firearms', fontsize=12)

    # Show the plot in Streamlit
    st.pyplot(fig)


#VISU 11

    st.subheader("Principal Caliber Analysis")
    st.write("""
    This Bubble Chart presents the most common calibers in the dataset. 
    """)

    caliber_counts = df['calibreCanonUn'].value_counts().reset_index()
    caliber_counts.columns = ['calibre', 'count']

    # Create a bubble chart
    fig_caliber_bubble = px.scatter(
        caliber_counts,
        x='calibre',
        y='count',
        size='count',
        color='calibre',
        title='Analyse du Calibre Principal des Armes',
        labels={'calibre': 'Calibre Principal', 'count': 'Nombre d\'Armes'},
        hover_name='calibre',
        size_max=30,
        template='plotly_white'
    )
    
    fig_caliber_bubble.update_layout(
    width=1500,  
    height=1000   
)

    # Display the bubble chart in Streamlit
    st.plotly_chart(fig_caliber_bubble)
    

#VISU 12
    st.subheader("Types of Cannons VS Percussion Modes")
    st.write("""
    This bar plot shows the Types of Cannon vs. Modes of Percussion
    """)


    bar_data = df.groupby(['typeCanonUn', 'modePercussionCanonUn']).size().reset_index(name='count')

    # Create the grouped bar chart
    fig_cannon_percussion_bar = px.bar(
        bar_data,
        x='typeCanonUn',
        y='count',
        color='modePercussionCanonUn',
        barmode='group',
        title='Types of Cannons VS Percussion Modes',
        labels={'x': 'Type de Canon', 'y': 'Nombre d\'Armes'},
        template='plotly_white'
    )

    # Display the bar chart in Streamlit
    st.plotly_chart(fig_cannon_percussion_bar)



#VISU 12

    st.subheader("Distribution of Amlimentation Systems")

    donut_data = df['systemeAlimentation'].value_counts().reset_index()
    donut_data.columns = ['Système d\'Alimentation', 'Nombre d\'Armes']

    # Create the donut chart
    fig_donut_chart = px.pie(
        donut_data,
        values='Nombre d\'Armes',
        names='Système d\'Alimentation',
        title='Répartition des Systèmes d\'Alimentation',
        hole=0.4,  # This creates the donut effect
        template='plotly_white'
    )

    # Display the donut chart in Streamlit
    st.plotly_chart(fig_donut_chart)



with tabs[4]:
    st.header("Correlations")

#VISU 13
    st.subheader("Length of Firearms by Caliber")
    st.write("""
    This violin plot illustrates the distribution of firearm lengths for each caliber. 
    The width of the violin indicates the density of the lengths at each caliber, providing insights 
    into the variation and common lengths within each caliber.
    """)

    # Violin Plot
    unique_calibers = df['calibreCanonUn'].unique()
    selected_caliber = st.selectbox("Select a Caliber:", sorted(unique_calibers))

    # Filter the dataframe for the selected caliber
    filtered_df = df[df['calibreCanonUn'] == selected_caliber]

    # Violin Plot
    fig_violin_length_caliber = px.violin(filtered_df, x='calibreCanonUn', y='longueurArme', box=True)
    st.plotly_chart(fig_violin_length_caliber)  



#VISU 14
    st.subheader("Correlation between Technical Characteristics")
    st.write("""
    This heatmap illustrates the correlation between various technical characteristics, 
    including length and capacity. It helps to identify relationships among numeric variables, 
    providing insights into how these characteristics interact with one another.
    """)

    numeric_df = df.select_dtypes(include=[np.number])

    # Check if there are any numeric columns
    if numeric_df.empty:
        st.write("No numeric columns available for correlation.")
    else:
        # Correlation Matrix
        corr = numeric_df.corr()

        # Heatmap
        fig_corr = px.imshow(corr, title='Heatmap of Correlation', 
                              labels=dict(x='Variables', y='Variables', color='Correlation'),
                              color_continuous_scale='RdBu', zmin=-1, zmax=1)
        st.plotly_chart(fig_corr)

        st.write("The heatmap reveals the correlations between various weapon characteristics, highlighting potential relationships such as a strong positive correlation between `capaciteHorsChambre` and `capaciteChambre`. Variables like `longueurArme` and `Year` exhibit little to no correlation, indicating that the length of weapons is largely independent of the year of manufacture.")



#VISU 15
    st.subheader("Repartition of Semi Auto Weapons")
    

    semi_auto_counts = df['armeSemiAutoApparenceArmeAuto'].value_counts().reset_index()
    semi_auto_counts.columns = ['Appearance', 'Count'] 

    fig_semi_auto = px.bar(semi_auto_counts, 
                            x='Count', y='Appearance', orientation='h',
                            title='Nombre d\'armes semi-auto')
    st.plotly_chart(fig_semi_auto)

    
with tabs[5]:
    st.header("Rankings")

#VISU 16
    st.subheader("Classement Français vs Européen")
    st.write("Ce graphique compare les classements français et européens des armes.")
    
    # Create a pivot table for visualization
    heatmap_data = df.pivot_table(index='classementFrancais', 
                                   columns='classementEuropeen', 
                                   aggfunc='size', fill_value=0)
    
    # Clustered Bar Chart
    heatmap_data.plot(kind='bar', figsize=(12, 6), cmap='viridis', legend=True)
    plt.title('Comparaison des Classements Français et Européens')
    plt.xlabel('Classement Français')
    plt.ylabel('Nombre d\'Armes')
    st.pyplot(plt)


#VISU 17
    st.subheader("Répartition des Armes par Classement")
    st.write("Ce diagramme en secteurs montre la répartition des armes par classement français.")
    fig_class_rank = px.pie(df, names='classementFrancais', 
                             title='Répartition des armes par classement', 
                             hole=0.3)
    st.plotly_chart(fig_class_rank)



#VISU 18
    country_counts = df['paysFabricant'].value_counts().head(20).reset_index()
    country_counts.columns = ['paysFabricant', 'Nombre d\'armes']

    # Création du graphique à barres
    fig_country_rank = px.bar(
        country_counts,
        x='paysFabricant',
        y='Nombre d\'armes',
        title='Classement des 20 premiers pays fabricants d\'armes',
        labels={'paysFabricant': 'Pays', 'Nombre d\'armes': 'Nombre d\'armes'},
        color='Nombre d\'armes',
        color_continuous_scale='Blues',  # Palette de couleurs
    )

    # Configuration de l'axe y en échelle logarithmique
    fig_country_rank.update_yaxes(type="log")

    # Ajustement de la taille du graphique
    fig_country_rank.update_layout(
        height=600,  # Hauteur
        width=1000,  # Largeur
        xaxis_tickangle=-45  # Inclinaison des légendes pour éviter la superposition
    )

    # Affichage du graphique
    st.plotly_chart(fig_country_rank)

#VISU 19
    manufacturer_counts = df['fabricant'].value_counts().reset_index()
    manufacturer_counts.columns = ['fabricant', 'Nombre d\'armes']

    # Création du graphique à barres
    fig_manufacturer_rank = px.bar(
        manufacturer_counts,
        x='fabricant',
        y='Nombre d\'armes',
        title='Classement des fabricants d\'armes',
        labels={'fabricant': 'Fabricant', 'Nombre d\'armes': 'Nombre d\'armes'},
        color='Nombre d\'armes',
        color_continuous_scale='Reds',  # Palette de couleurs
    )

    # Configuration de l'axe y en échelle logarithmique
    fig_manufacturer_rank.update_yaxes(type="log")

    fig_manufacturer_rank.update_layout(
    height=600,  # Hauteur
    width=1000   # Largeur
)

    # Affichage du graphique
    st.plotly_chart(fig_manufacturer_rank)


with tabs[6]:
    st.header("Advanced Analysis")


#VISU 20
    st.subheader("Word Cloud of Weapon Models")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['modele'].dropna()))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

#VISU 21
    st.subheader("Top 10 Manufacturers by Number of Weapons Produced")
    top_manufacturers = df['fabricant'].value_counts().nlargest(10).reset_index()
    top_manufacturers.columns = ['Manufacturer', 'Number of Weapons']

    fig_top_manufacturers = px.bar(
        top_manufacturers,
        x='Manufacturer',
        y='Number of Weapons',
        title='Top 10 Manufacturers by Number of Weapons Produced',
        labels={'Manufacturer': 'Manufacturer', 'Number of Weapons': 'Number of Weapons'},
        color='Number of Weapons',
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig_top_manufacturers)

#VISU 22

    st.subheader("Types of Weapons and Functioning Mode Heatmap")
    heatmap_data = pd.crosstab(df['typeArme'], df['modeFonctionnement'])
    plt.figure(figsize=(13, 7))
    sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='g')
    plt.title('Heatmap of Types of Weapons and Functioning Mode')
    st.pyplot(plt)



























#https://github.com/aalvaropc/streamlit-portfolio?tab=readme-ov-file