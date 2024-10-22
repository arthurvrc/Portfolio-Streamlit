import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk
import plotly.express as px
import streamlit.components.v1 as components
import numpy as np
import seaborn as sns
import squarify 
import plotly.graph_objects as go
import plotly.figure_factory as ff
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
import statsmodels.api as sm
from wordcloud import WordCloud
import pycountry
from streamlit_option_menu import option_menu
import smtplib
from email.mime.text import MIMEText




st.header("Welcome to this Project, hope you will enjoy it! ")

selected = option_menu("Please select a page :", ["Portfolio", "Uber Data", "RGA Analysis"], icons=['house', 'cloud-upload', 'graph-up-arrow'], default_index=0, styles={"container": {"padding": "5!important", "background-color": "#f8f9fa"}, "icon": {"font-size": "20px"}, "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#f1f1f1"}, "nav-link-selected": {"background-color": "#5dade2"}})





if selected == "Portfolio":


    st.title("Welcome to My Portfolio")


    st.sidebar.title("About Me")

    st.sidebar.write("""
    Hi, I'm Arthur Vercher. I'm a Data Science student who loves using data to find answers and solve problems. I have studied in different places, including Los Angeles, Spain, and Australia, which has helped me learn from many cultures.

    In my studies, I've developed skills in data analysis, machine learning, and visualization. I'm especially interested in how data can help make better decisions in different fields.

    Explore this dashboard to see my projects, skills, and interests. I hope you find the information helpful!
    """)


    tabs = st.tabs(["Introduction", "Projects", "Skills", "Fun Facts", "Contact"])

    with tabs[0]:
        st.header("Introduction")
        st.write("""
        Welcome to my personal dashboard! Here, you'll find information about my background, current projects, and some fun facts about me. 
        Feel free to explore the different sections using the sidebar navigation.
                 
        """)

        st.write(" ")
        st.write(" ")

        col12, col22 = st.columns([1, 2])
        
        

        with col12:
            profile_image = "photo-pro.jpg"  

            st.image(profile_image, width=200, caption="Arthur Vercher", use_column_width=False)

        with col22:
            st.markdown("""
            ## Arthur Vercher  
            **M1 Student in Data Science at EFREI Paris**  
                        
            Email: arthur.vercher@efrei.net
                        
            LinkedIn: [Arthur Vercher](https://www.linkedin.com/in/arthur-vercher)  
            """)
        with open("CV_Arthur_Vercher.pdf", "rb") as file:
                st.download_button(
                    label="📥 Download my CV", 
                    data=file, 
                    file_name="Arthur_Vercher_CV.pdf", 
                    mime="application/pdf",
                    key="download_cv",
                    help="Click to download my CV."
                )

        st.write("<hr style='border: none; height: 2px; background-color: #5dade2;'>", unsafe_allow_html=True)
        st.write(" ")  

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Background")
            st.write("""
            I am currently pursuing a Master's in Data Science at EFREI Paris, with a strong foundation in mathematics and computer science. 
            I've gained diverse experience through various roles, including working as a sales consultant, teaching languages, and assisting in medical services.
            """)

        with col2:
            st.subheader("International Experience")
            st.write("""
            I recently completed a semester abroad at the University of California, Irvine (UCI), where I further developed my skills and knowledge in data science.
            """)

        st.subheader("Where I’ve Studied")
        locations = pd.DataFrame({
            'City': ['Adelaide', 'Los Angeles', 'Valencia', 'Paris'],
            'Country': ['Australia', 'USA', 'Spain', 'France'],
            'Latitude': [-34.9285, 34.0522, 39.4699, 48.8566],
            'Longitude': [138.6007, -118.2437, -0.3763, 2.3522]
        })

        st.pydeck_chart(pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=20,
                longitude=0,
                zoom=2,
                pitch=0,
            ),
            map_style='mapbox://styles/mapbox/light-v10',  
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=locations,
                    get_position=['Longitude', 'Latitude'],
                    auto_highlight=True,
                    get_radius=80000,  
                    get_fill_color=[255, 0, 0, 200],  
                    get_line_color=[0, 0, 0],
                    get_line_width=2,
                    pickable=True,
                    radius_scale=2,  
                )
            ],
            tooltip={
                'text': '{City}, {Country}',
                'style': {
                    'backgroundColor': 'rgba(255, 255, 255, 0.8)',  
                    'color': 'black'
                }
            }
        ))

        st.write("© 2024 Arthur Vercher. All rights reserved.")

        
    with tabs[1]:
        st.header("Projects")
        st.write("""
        Here are some of the projects I've been working on recently:
        """)

        project_data = pd.DataFrame({
            'Project': ['Interactive Map of Lost Luggage', 'Tattoo Artist Social Network', 'Python Video Games', 'Patent Classification Tool', 'This Project','Cocktail Finder'],
            'Progress (%)': [100, 100, 100, 100, 85, 55]
        })

        st.subheader("Project Progress")
        fig, ax = plt.subplots(figsize=(12, 6))  
        bars = ax.bar(project_data['Project'], project_data['Progress (%)'], color='skyblue', width=0.4)  

        ax.set_xlabel("Projects")
        ax.set_ylabel("Progress (%)")
        ax.set_title("Current Project Progress")

        ax.set_xticklabels(project_data['Project'], rotation=45, ha='right')

        st.pyplot(fig)

        st.write("""
        I've successfully completed several academic projects, including:
        - **Interactive Map of Lost Luggage**: A website that maps forgotten luggage on Paris metro lines.
        - **Tattoo Artist Social Network**: A platform for tattoo artists to share unique designs.
        - **Python Video Games**: Developed various video games using Python.
        - **Patent Classification Tool**: Currently developing a tool for patent classification and sorting.
        """)

        st.write("if you are interested, here are more of my projects:")
        if st.button('🌐 Visit my GitHub', key="github_button", help="Click to view my GitHub profile"):
            st.markdown("[GitHub Profile](https://github.com/arthurvrc)", unsafe_allow_html=True)

        st.write("© 2024 Arthur Vercher. All rights reserved.")

    with tabs[2]:
        st.header("Skills")
        st.write("""
        Throughout my academic and professional experiences, I have developed a variety of skills, including:
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Programming Languages")
            st.markdown("""
            - **Python**: Highly proficient, used in various projects and applications.
            - **Java**: Experienced in developing applications and understanding object-oriented programming.
            - **HTML**: Proficient in creating structured web content.
            - **SQL**: Skilled in database management and queries.
            - **CSS**: Knowledgeable in styling web content.
            - **C**: Basic understanding of C programming for low-level operations.
            - **...and many more**
            """)

            st.subheader("Software & Tools")
            st.markdown("""
            - **Microsoft Office Suite**: Advanced proficiency in Excel, Word, and PowerPoint.
            - **PowerBI**: Experience in creating interactive data visualizations.
            - **VS Code**: Comfortable with code editing and debugging.
            - **MySQL**: Knowledgeable in managing and querying databases.
            - **...**
            """)

            skills_data = pd.DataFrame({
                'Skill': ['Python', 'Java', 'SQL', 'PowerBI', 'HTML', 'CSS','C'],
                'Proficiency': [90, 40, 85, 20, 80, 80, 50]
            })

            fig = px.bar(skills_data, x='Skill', y='Proficiency', title='Skills Proficiency',
                        labels={'Proficiency': 'Proficiency (%)'},
                        color='Proficiency', color_continuous_scale=px.colors.sequential.Plasma)
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.subheader("Languages")
            st.markdown("""
            - **French**: C2 (Fluent)
            - **Spanish**: C1-C2 (Advanced-Fluent)
            - **English**: C1 (Advanced)
            """)

            st.subheader("Other Competences")
            st.markdown("""
            - **Double Culture**: French-Spanish heritage.
            - **Sports**: Active in Rugby, Boxing (Podium at French Championship), Judo, Tennis...
            """)

        st.write("© 2024 Arthur Vercher. All rights reserved.")


    with tabs[3]:
        st.header("Fun Facts")
        st.write("""
        Here is a glimpse into the interests that make me who I am!
        """)

        st.subheader("Did You Know?")
        
        st.write("""
        - **Rugby Enthusiast**: I’m passionate about rugby and enjoy the thrill of the game. It’s a fantastic way to stay active and challenge myself.
        
        - **Sports Lover**: From boxing and judo to tennis, I love a wide range of sports. I even reached the podium at the French Championship in boxing!
        
        - **Party Lover**: Whether it’s a lively gathering or a relaxed evening with friends, I believe that celebrating life is essential.
        
        - **Car Enthousiast**: My dream is to own a Porsche one day. 
        
        - **Cultural Fusion**: I have a  multicultural background with roots in both France and Spain. This blend of cultures gives me a unique perspective on life.
        """)

        st.subheader("Hidden Talent")
        st.write("""
        - **Cooking Creations**: I think I just love food.
        """)

        st.subheader("Tech and Geek Interests")
        st.write("""
        - **A bit of a gamer**: I enjoy exploring new video games and challenges. But I don't see myself as a gamer since all the students in the class play a lot mere than me... 
        
        - **DIY Projects**: When I’m not working on data science, I like to dive into DIY electronics and coding projects. It’s a rewarding way to apply my technical skills in a hands-on way.
        """)

        st.write("Feel free to reach out if you share any of these interests or if you just want to chat!")


        st.write("Thanks for visiting my dashboard! Stay tuned for more updates.")
        st.write("© 2024 Arthur Vercher. All rights reserved.")


    with tabs[4]:
        st.header("Contact")
        st.write("""    
        If you'd like to leave a comment, please fill out the form below:
        """)


        def send_email(name, email, message):
            msg = MIMEText(f"Message from {name} ({email}): {message}")
            msg['Subject'] = 'New Contact Form Submission'
            msg['From'] = 'your_email@example.com'  
            msg['To'] = 'your_email@example.com'    

            with smtplib.SMTP('smtp.example.com', 587) as server:  
                server.starttls()
                server.login("your_email@example.com", "your_password")  
                server.send_message(msg)

        with st.form(key='contact_form'):
            name = st.text_input("Name")
            message = st.text_area("Message")
            submit_button = st.form_submit_button("Submit")

            if submit_button:
                st.write(f"Thank you {name}! Your message has been sent.")

        st.subheader("Feedback")
        st.write("How would you rate your experience?")
 

        feedback_response = st.feedback("stars")
        st.write(f"You rated: {feedback_response}")
        st.write("Thank you for your feedback!")
        st.write("© 2024 Arthur Vercher. All rights reserved.")






elif selected == "Uber Data":


    data = pd.read_csv('uber-raw-data-apr14.csv', parse_dates=['Date/Time'])

    st.title("Uberdata Visualization")
    st.write(
        "This dashboard provides insights into Uber taxi trips in New York City, showcasing various visualizations to explore patterns in pickup and dropoff locations, trip durations, and activity trends. "
        "By diving into the dataset, we aim to uncover hidden patterns, identify popular zones, and highlight the dynamics of ride-sharing in one of the world's busiest cities."
    )

    st.write(
        "Uber has transformed the way we navigate urban environments, and understanding the intricacies of its operations can reveal fascinating trends about urban mobility. "
        "In this dashboard, we analyze the longest and shortest trips, peak activity hours, and density of trips, providing a comprehensive overview of the data. "
        "This visualization tool allows users to interactively explore Uber's trip data, gaining insights into where and when rides are most frequent, and understanding the factors that drive demand in different neighborhoods."
    )

    st.sidebar.title("Navigation")
    st.sidebar.write(
        "Welcome to the Uberdata Visualization dashboard! In this interactive application, you can explore various visualizations derived from the dataset of Uber trips in New York City. "
        "Each page offers unique insights into different aspects of the data, allowing you to dive deep into the fascinating world of ride-sharing trends. "
        "Select a page from the options below to begin your exploration!"
    )
    tabs2 = st.tabs(["Pickups and Dropoffs", "Time", "Zones"])

    with tabs2[0]:
        st.write("Let's get started.")
        
    
        data['next_lat'] = data['Lat'].shift(-1)
        data['next_lon'] = data['Lon'].shift(-1)

        data.dropna(subset=['next_lat', 'next_lon'], inplace=True)

        data['distance'] = ((data['next_lat'] - data['Lat']) ** 2 + (data['next_lon'] - data['Lon']) ** 2) ** 0.5

        longest_trip_index = data['distance'].idxmax()
        shortest_trip_index = data['distance'].idxmin()

        if data['distance'].min() == 0:
            shortest_trip_index = data[data['distance'] > 0]['distance'].idxmin()

        longest_trip = data.loc[longest_trip_index]
        shortest_trip = data.loc[shortest_trip_index]

        trips = pd.DataFrame({
            'start_lat': [longest_trip['Lat'], shortest_trip['Lat']],
            'start_lon': [longest_trip['Lon'], shortest_trip['Lon']],
            'end_lat': [longest_trip['next_lat'], shortest_trip['next_lat']],
            'end_lon': [longest_trip['next_lon'], shortest_trip['next_lon']],
            'label': ['Longest Trip', 'Shortest Trip'],
            'line_width': [7, 5],  
            'color': [[255, 0, 0], [0, 255, 0]] 
        })

        st.subheader("Longest and Shortest Trips")
        st.write("This visualization displays the longest trip in red and the shortest trip in green.")
        deck1 = pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=data['Lat'].mean(),
                longitude=data['Lon'].mean(),
                zoom=12,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    'LineLayer',
                    data=trips,
                    get_source_position='[start_lon, start_lat]',
                    get_target_position='[end_lon, end_lat]',
                    get_color='color',
                    get_width='line_width',
                    pickable=True,
                    tooltip={
                        "html": "<b>{label}</b>",
                        "style": {"color": "black"},
                    },
                ),
            ],
        )

        st.pydeck_chart(deck1)

        st.subheader("Pickup and Dropoff Points")
        st.write("This map displays pickup points in blue and dropoff points in red randomly selected from the dataset.")

        pickup_data = data[['Lat', 'Lon']].sample(150, random_state=42).copy()  
        pickup_data['color'] = 'blue'  
        dropoff_data = data[['next_lat', 'next_lon']].sample(150, random_state=42).copy() 
        dropoff_data.columns = ['Lat', 'Lon']
        dropoff_data['color'] = 'red'  

        pickup_data['type'] = 'Pickup'
        dropoff_data['type'] = 'Dropoff'
        points = pd.concat([pickup_data, dropoff_data], ignore_index=True)

        deck2 = pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=data['Lat'].mean(),
                longitude=data['Lon'].mean(),
                zoom=12,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=pickup_data,
                    get_position='[Lon, Lat]',
                    get_fill_color='[0, 0, 255]',  
                    get_radius=100,
                    pickable=True,
                    tooltip={
                        "html": "Pickup Point",
                        "style": {"color": "black"},
                    },
                ),
                pdk.Layer(
                    "ScatterplotLayer",
                    data=dropoff_data,
                    get_position='[Lon, Lat]',
                    get_fill_color='[255, 0, 0]', 
                    get_radius=100,
                    pickable=True,
                    tooltip={
                        "html": "Dropoff Point",
                        "style": {"color": "black"},
                    },
                ),
            ],
        )

        st.pydeck_chart(deck2)

        st.subheader("Trip Lines from Pickup to Dropoff")
        st.write("This map shows fine lines indicating the trips from pickup to dropoff for 100 random samples.")

        sample_trips = data.sample(100, random_state=42)

        trip_lines = pd.DataFrame({
            'start_lat': sample_trips['Lat'],
            'start_lon': sample_trips['Lon'],
            'end_lat': sample_trips['next_lat'],
            'end_lon': sample_trips['next_lon'],
        })

        deck3 = pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=data['Lat'].mean(),
                longitude=data['Lon'].mean(),
                zoom=12,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    'LineLayer',
                    data=trip_lines,
                    get_source_position='[start_lon, start_lat]',
                    get_target_position='[end_lon, end_lat]',
                    get_color='[0, 0, 255]',  
                    get_width=2,
                    pickable=True,
                    tooltip={
                        "html": "Trip from Pickup to Dropoff",
                        "style": {"color": "black"},
                    },
                ),
            ],
        )

        st.pydeck_chart(deck3)

    with tabs2[1]:
        st.subheader("Histogram of Trips by Hour")
        st.write("This histogram shows the number of trips taken during each hour of the day, revealing peak activity times.")
        data['hour'] = data['Date/Time'].dt.hour
        hourly_trips = data['hour'].value_counts().sort_index()

        st.bar_chart(hourly_trips)

        data['Dropoff Time'] = data['Date/Time'] + pd.to_timedelta(np.random.randint(5, 60, data.shape[0]), unit='m')

        data['Trip Duration'] = (data['Dropoff Time'] - data['Date/Time']).dt.total_seconds() / 60  

        average_trip_duration = data['Trip Duration'].mean()

        st.subheader("Trip Duration Histogram")
        st.write("This histogram shows the distribution of trip durations in minutes.")
        st.write(f"The average trip duration is {average_trip_duration:.2f} minutes.")

        plt.figure(figsize=(10, 6))
        sns.histplot(data['Trip Duration'], bins=30, kde=True)
        plt.title("Distribution of Trip Durations")
        plt.xlabel("Duration (minutes)")
        plt.ylabel("Frequency")
        st.pyplot(plt)

    with tabs2[2]:
        data['next_lat'] = data['Lat'].shift(-1)
        data['next_lon'] = data['Lon'].shift(-1)

        data.dropna(subset=['next_lat', 'next_lon'], inplace=True)

        st.subheader("Density Heatmap of Trips")
        st.write("This heatmap shows the density of trips, highlighting the busiest areas in New York City.")
        half_data = data.sample(frac=0.4, random_state=42) 

        deck4 = pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=half_data['Lat'].mean(),
                longitude=half_data['Lon'].mean(),
                zoom=12,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    'HeatmapLayer',
                    data=half_data,
                    get_position='[Lon, Lat]',
                    auto_highlight=True,
                    get_weight='1',
                    radius_pixels=50,
                ),
            ],
        )

        st.pydeck_chart(deck4)

        st.subheader("Clusters of Most Popular Pickup and Dropoff Areas")
        st.write("This visualization clusters the most popular pickup and dropoff areas, allowing users to explore the frequency of trips in different zones.")

        cluster_data = data[['Lat', 'Lon']].sample(1000, random_state=42)

        deck5 = pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=cluster_data['Lat'].mean(),
                longitude=cluster_data['Lon'].mean(),
                zoom=12,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=cluster_data,
                    get_position='[Lon, Lat]',
                    radius=100,
                    opacity=0.6,
                    elevation_range=[0, 1000],
                    elevation_scale=4,
                    pickable=True,
                    extruded=True,
                    tooltip=True,
                ),
            ],
        )

        st.pydeck_chart(deck5)


        st.subheader("Popular Pickup and Dropoff Areas")
        st.write("This map displays clusters of the most popular pickup and dropoff areas in NYC.")

        pickup_counts = data.groupby(['Lat', 'Lon']).size().reset_index(name='Frequency')
        dropoff_counts = data.groupby(['next_lat', 'next_lon']).size().reset_index(name='Frequency')

        pickup_counts['Type'] = 'Pickup'
        dropoff_counts['Type'] = 'Dropoff'
        combined_counts = pd.concat([pickup_counts, dropoff_counts], ignore_index=True)

        top_pickups = pickup_counts.nlargest(40, 'Frequency')
        top_dropoffs = dropoff_counts.nlargest(40, 'Frequency')

        cluster_data = pd.concat([top_pickups, top_dropoffs], ignore_index=True)

        deck5 = pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=data['Lat'].mean(),
                longitude=data['Lon'].mean(),
                zoom=12,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=top_pickups,
                    get_position='[Lon, Lat]',
                    get_fill_color='[255, 255, 255, 25]',  
                    get_radius=600,  
                    pickable=True,
                    tooltip={
                        "html": "<b>Pickup Area</b><br/>Frequency: {Frequency}",
                        "style": {"color": "black"},
                    },
                ),
                pdk.Layer(
                    "ScatterplotLayer",
                    data=top_dropoffs,
                    get_position='[next_lon, next_lat]',
                    get_fill_color='[255, 255, 255, 25]',  
                    get_radius=600,  
                    pickable=True,
                    tooltip={
                        "html": "<b>Dropoff Area</b><br/>Frequency: {Frequency}",
                        "style": {"color": "black"},
                    },
                ),
            ],
        )

        st.pydeck_chart(deck5)




elif selected == "RGA Analysis":




    df = pd.read_csv('guns.csv', sep=',', encoding='ISO-8859-1')



    st.title("Guns Dataset Analysis")
    st.write("""
    Welcome to the Guns Dataset Analysis project. This dataset contains a variety of information about firearms, including their type, manufacturer, country of origin, and technical specifications. 
    In this project, we will explore various aspects of the dataset through visualizations, aiming to uncover hidden insights and present a comprehensive analysis.
    """)

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

    tabs = st.tabs(["Introduction", "General Presentation", "Temporal Analysis", 
                    "Technical Characteristics", "Correlations", "Rankings", "Advanced"])

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



    with tabs[1]:
        st.header("General Presentation")

    #VISU 1
        st.subheader("Distribution of Firearm Families")
        st.write("""
        This histogram shows the distribution of the different firearm families in the dataset. 
        By visualizing the frequency of each family, we can identify which types of firearms are more common.
        """)

        plt.figure(figsize=(10, 6))
        ax = sns.countplot(y="famille", data=df, palette="viridis", order=df["famille"].value_counts().index)
        
        for p in ax.patches:
            count = int(p.get_width())  
            ax.annotate(f'{count}', (p.get_width() + 100, p.get_y() + p.get_height() / 2), 
                        va='center')  

        plt.title('Distribution of Firearm Families')
        plt.xlabel('Count')
        plt.ylabel('Firearm Family')
        st.pyplot(plt)

    #VISU 2
    

        st.subheader("Distribution of Firearm Types by Family")
        st.write("""
        This bar plot shows the distribution of firearm types within each family. The different colors represent the firearm families, 
        and this allows us to see how types are distributed across families.
        """)

        plt.figure(figsize=(16, 10))  

        ax = sns.countplot(y="typeArme", data=df, hue="famille", palette="viridis",
                        order=df["typeArme"].value_counts().index)

        for p in ax.patches:
            count = int(p.get_width())  
            ax.annotate(f'{count}', (p.get_width() + 50, p.get_y() + p.get_height() / 2),
                        va='center', fontsize=12)  

        ax.legend(title="Firearm Family", loc='lower right', bbox_to_anchor=(1, 0), fontsize=12, title_fontsize=14)

        plt.title('Distribution of Firearm Types by Family', fontsize=18)
        plt.xlabel('Count', fontsize=14)
        plt.ylabel('Firearm Type', fontsize=14)

        ax.tick_params(axis='x', labelsize=12)
        ax.tick_params(axis='y', labelsize=12)

        st.pyplot(plt)

        top_families = df['typeArme'].value_counts().nlargest(5)

        plt.figure(figsize=(8, 8))  

        plt.pie(top_families, labels=top_families.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis', 5))

        plt.title("Top 5 Firearm Families by Occurrence", fontsize=16)

        st.pyplot(plt)


    #VISU 3
        st.subheader("Distribution of Firearms by Brand")

        st.write("""
        This bar chart displays the distribution of firearms by brand, 
        highlighting the relative frequency of different brands in the dataset.
        """)

        brand_counts = df['marque'].value_counts()

        plt.figure(figsize=(12, 8))  
        bars = plt.barh(brand_counts.index[:10], brand_counts.values[:10], color='skyblue')  

        plt.title("Distribution of Firearms by Brand (Top 10)", fontsize=16)
        plt.xlabel("Number of Firearms", fontsize=14)
        plt.ylabel("Brand", fontsize=14)

        for bar in bars:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                    int(bar.get_width()), va='center', fontsize=12)

        st.pyplot(plt)

    #VISU 4
        st.subheader("Distribution of Firearms by Manufacturer")

        st.write("""
        This pie chart illustrates the distribution of firearms by manufacturer, 
        showcasing the proportion of firearms produced by the leading manufacturers in the dataset.
        """)

        manufacturer_counts = df['fabricant'].value_counts()

        top_manufacturers = manufacturer_counts.head(5)

        plt.figure(figsize=(10, 8))  
        plt.pie(top_manufacturers, labels=top_manufacturers.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
        
        plt.title("Distribution of Firearms by Manufacturer", fontsize=16)

        st.pyplot(plt)


    #VISU 5
        st.subheader("Manufacturing Countries Map")

        st.write("""
        This world map displays the manufacturing countries of firearms, 
        highlighting the number of firearms produced in each country.
        """)

        country_counts = df['paysFabricant'].value_counts().reset_index()
        country_counts.columns = ['Country', 'Number of Firearms']

        fig = px.choropleth(country_counts, 
                            locations='Country',
                            locationmode='country names',
                            color='Number of Firearms',
                            hover_name='Country',
                            color_continuous_scale=px.colors.sequential.Plasma,
                            title='Number of Firearms Produced by Country',
                            labels={'Number of Firearms': 'Number of Firearms'},
                            projection='natural earth')

        fig.update_layout(title_font_size=20,
                        geo=dict(showland=True, landcolor='lightgray'))

        st.plotly_chart(fig)



    with tabs[2]:
        st.header("Temporal Analysis")
        

    #VISU 6
        st.subheader("Evolution of Firearm Creations Over Time")

        st.write("""
        This line plot shows the evolution of firearm creations over the years, 
        illustrating the number of firearms created each year.
        """)

        df['dateCreaRGA'] = pd.to_datetime(df['dateCreaRGA'], errors='coerce')
        df['Year'] = df['dateCreaRGA'].dt.year

        yearly_counts = df['Year'].value_counts().reset_index()
        yearly_counts.columns = ['Year', 'Number of Firearms']
        yearly_counts = yearly_counts.sort_values('Year')

        fig = px.line(yearly_counts, 
                    x='Year', 
                    y='Number of Firearms', 
                    title='Number of Firearms Created Over Time',
                    labels={'Number of Firearms': 'Number of Firearms'},
                    markers=True)

        fig.update_layout(title_font_size=20,
                        xaxis_title='Year',
                        yaxis_title='Number of Firearms',
                        xaxis=dict(tickmode='linear'))

        st.plotly_chart(fig)


    #VISU 7
        st.subheader("Comparison of Creation and Update Dates")
        df = df[df['dateMajRGA'] >= df['dateCreaRGA']]


        st.write("""
        This scatter plot compares the creation dates and the last updated dates of firearms. 
        Each point represents a firearm, showing its creation date on the x-axis and 
        the last updated date on the y-axis.
        """)

        df['dateCreaRGA'] = pd.to_datetime(df['dateCreaRGA'], errors='coerce')
        df['dateMajRGA'] = pd.to_datetime(df['dateMajRGA'], errors='coerce')

        scatter_df = df.dropna(subset=['dateCreaRGA', 'dateMajRGA'])

        fig = px.scatter(scatter_df,
                        x='dateCreaRGA', 
                        y='dateMajRGA',
                        title='Comparison of Creation and Update Dates',
                        labels={'dateCreaRGA': 'Creation Date', 'dateMajRGA': 'Update Date'},
                        hover_data=['referenceRGA'])  

        fig.update_traces(marker=dict(size=5, opacity=0.7))
        fig.update_layout(title_font_size=20,
                        xaxis_title='Creation Date',
                        yaxis_title='Update Date')

        st.plotly_chart(fig)


    #VISU 8
        st.subheader("Update Rate of Firearms")

        st.write("""
        This histogram displays the number of firearms updated each year. 
        It provides insights into the frequency of updates over time.
        """)

        df['dateMajRGA'] = pd.to_datetime(df['dateMajRGA'], errors='coerce')

        df['year_updated'] = df['dateMajRGA'].dt.year

        update_counts = df['year_updated'].value_counts().sort_index()

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=update_counts.index, 
            y=update_counts.values,
            marker=dict(color='royalblue'),
            text=update_counts.values,  
            textposition='outside'       
        ))

        fig.update_layout(
            title='Number of Firearms Updated per Year',
            xaxis_title='Year',
            yaxis_title='Number of Updates',
            title_font_size=20
        )

        st.plotly_chart(fig)


    with tabs[3]:

        st.header("Technical Characteristics")

        st.subheader("Répartition des Armes par Classement")
        st.write("Ce diagramme en secteurs montre la répartition des armes par classement français.")
        fig_class_rank = px.pie(df, names='classementEuropeen', 
                                title='Répartition des armes par classement', 
                                hole=0.3) 
        st.plotly_chart(fig_class_rank)
        st.write(" Catégories d'armes :")
        st.write("- *Catégorie A* : Armes à feu semi-automatiques et de guerre, généralement interdites aux civils.")
        st.write("- *Catégorie B* : Fusils de chasse et armes de tir sportif, nécessitant un permis.")
        st.write("- *Catégorie C* : Carabines et pistolets à répétition manuelle, avec des formalités moins strictes.")


        st.subheader("Density Distribution of Firearm Lengths")

        st.write("""
        This KDE plot visualizes the density distribution of firearm lengths. 
        """)

        fig, ax = plt.subplots(figsize=(10, 6))

        sns.histplot(df['longueurArme'], 
                    bins=50,    
                    kde=False,  
                    color="lightblue", 
                    ax=ax)

        ax.set_xlim(0, 2000)

        ax.set_title('Firearm Length Distribution', fontsize=16)
        ax.set_xlabel('Firearm Length (cm)', fontsize=12)
        ax.set_ylabel('Number of Firearms', fontsize=12)

        st.pyplot(fig)


    #VISU 11

        st.subheader("Principal Caliber Analysis")
        st.write("""
        This Bubble Chart presents the most common calibers in the dataset. 
        """)

        caliber_counts = df['calibreCanonUn'].value_counts().reset_index()
        caliber_counts.columns = ['calibre', 'count']

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

        st.plotly_chart(fig_caliber_bubble)
        

    #VISU 12
        st.subheader("Types of Cannons VS Percussion Modes")
        st.write("""
        This bar plot shows the Types of Cannon vs. Modes of Percussion
        """)


        bar_data = df.groupby(['typeCanonUn', 'modePercussionCanonUn']).size().reset_index(name='count')

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

        st.plotly_chart(fig_cannon_percussion_bar)



    #VISU 12

        st.subheader("Distribution of Amlimentation Systems")

        donut_data = df['systemeAlimentation'].value_counts().reset_index()
        donut_data.columns = ['Système d\'Alimentation', 'Nombre d\'Armes']

        fig_donut_chart = px.pie(
            donut_data,
            values='Nombre d\'Armes',
            names='Système d\'Alimentation',
            title='Répartition des Systèmes d\'Alimentation',
            hole=0.4,  
            template='plotly_white'
        )

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

        unique_calibers = df['calibreCanonUn'].unique()
        selected_caliber = st.selectbox("Select a Caliber:", sorted(unique_calibers))

        filtered_df = df[df['calibreCanonUn'] == selected_caliber]

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

        if numeric_df.empty:
            st.write("No numeric columns available for correlation.")
        else:
            corr = numeric_df.corr()

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

    #VISU 18
        country_counts = df['paysFabricant'].value_counts().head(20).reset_index()
        country_counts.columns = ['paysFabricant', 'Nombre d\'armes']

        fig_country_rank = px.bar(
            country_counts,
            x='paysFabricant',
            y='Nombre d\'armes',
            title='Classement des 20 premiers pays fabricants d\'armes',
            labels={'paysFabricant': 'Pays', 'Nombre d\'armes': 'Nombre d\'armes'},
            color='Nombre d\'armes',
            color_continuous_scale='Blues',  
        )

        fig_country_rank.update_yaxes(type="log")

        fig_country_rank.update_layout(
            height=600,  
            width=1000,  
            xaxis_tickangle=-45  
        )

        st.plotly_chart(fig_country_rank)


    #VISU 19
        manufacturer_counts = df['fabricant'].value_counts().reset_index()
        manufacturer_counts.columns = ['fabricant', 'Nombre d\'armes']

        fig_manufacturer_rank = px.bar(
            manufacturer_counts,
            x='fabricant',
            y='Nombre d\'armes',
            title='Classement des fabricants d\'armes',
            labels={'fabricant': 'Fabricant', 'Nombre d\'armes': 'Nombre d\'armes'},
            color='Nombre d\'armes',
            color_continuous_scale='Reds',  
        )

        fig_manufacturer_rank.update_yaxes(type="log")

        fig_manufacturer_rank.update_layout(
        height=600,  
        width=1000   
    )

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









