import pandas as pd
import streamlit as st
import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('uber-raw-data-apr14.csv', parse_dates=['Date/Time'])

# Title and introduction
st.title("Uberdata Visualization")
st.write(
    "This dashboard provides insights into Uber taxi trips in New York City, showcasing various visualizations to explore patterns in pickup and dropoff locations, trip durations, and activity trends. "
    "By diving into the dataset, we aim to uncover hidden patterns, identify popular zones, and highlight the dynamics of ride-sharing in one of the world's busiest cities."
)

# Additional introduction content
st.write(
    "Uber has transformed the way we navigate urban environments, and understanding the intricacies of its operations can reveal fascinating trends about urban mobility. "
    "In this dashboard, we analyze the longest and shortest trips, peak activity hours, and density of trips, providing a comprehensive overview of the data. "
    "This visualization tool allows users to interactively explore Uber's trip data, gaining insights into where and when rides are most frequent, and understanding the factors that drive demand in different neighborhoods."
)

# Sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.write(
    "Welcome to the Uberdata Visualization dashboard! In this interactive application, you can explore various visualizations derived from the dataset of Uber trips in New York City. "
    "Each page offers unique insights into different aspects of the data, allowing you to dive deep into the fascinating world of ride-sharing trends. "
    "Select a page from the options below to begin your exploration!"
)
page = st.sidebar.radio("Select a page:", ["Introduction", "Pickups and Dropoffs", "Time", "Zones"])

if page == "Introduction":
    st.write("Let's get started.")
    
elif page == "Pickups and Dropoffs":
    # Calculate the distance for each trip
    data['next_lat'] = data['Lat'].shift(-1)
    data['next_lon'] = data['Lon'].shift(-1)

    # Remove rows with null next_lat or next_lon
    data.dropna(subset=['next_lat', 'next_lon'], inplace=True)

    # Calculate the distance (this can be adapted for real distance calculations)
    data['distance'] = ((data['next_lat'] - data['Lat']) ** 2 + (data['next_lon'] - data['Lon']) ** 2) ** 0.5

    # Find the longest and shortest trips
    longest_trip_index = data['distance'].idxmax()
    shortest_trip_index = data['distance'].idxmin()

    # Ensure the shortest trip is not zero
    if data['distance'].min() == 0:
        shortest_trip_index = data[data['distance'] > 0]['distance'].idxmin()

    longest_trip = data.loc[longest_trip_index]
    shortest_trip = data.loc[shortest_trip_index]

    # Create a DataFrame for the trips
    trips = pd.DataFrame({
        'start_lat': [longest_trip['Lat'], shortest_trip['Lat']],
        'start_lon': [longest_trip['Lon'], shortest_trip['Lon']],
        'end_lat': [longest_trip['next_lat'], shortest_trip['next_lat']],
        'end_lon': [longest_trip['next_lon'], shortest_trip['next_lon']],
        'label': ['Longest Trip', 'Shortest Trip'],
        'line_width': [7, 5],  # Adjusted width
        'color': [[255, 0, 0], [0, 255, 0]]  # Red for longest, green for shortest
    })

    # Visualization 1: Trips
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

    # Display the first visualization
    st.pydeck_chart(deck1)

    # Visualization 3: Pickup and Dropoff Points
    st.subheader("Pickup and Dropoff Points")
    st.write("This map displays pickup points in blue and dropoff points in red randomly selected from the dataset.")

    # Sample 150 random pickups and dropoffs
    pickup_data = data[['Lat', 'Lon']].sample(150, random_state=42).copy()  # Randomly sample pickups
    pickup_data['color'] = 'blue'  # Assign color for pickups
    dropoff_data = data[['next_lat', 'next_lon']].sample(150, random_state=42).copy()  # Randomly sample dropoffs
    dropoff_data.columns = ['Lat', 'Lon']
    dropoff_data['color'] = 'red'  # Assign color for dropoffs

    # Create a combined DataFrame for the points
    pickup_data['type'] = 'Pickup'
    dropoff_data['type'] = 'Dropoff'
    points = pd.concat([pickup_data, dropoff_data], ignore_index=True)

    # Create the map with pickup and dropoff points
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
                get_fill_color='[0, 0, 255]',  # Blue for pickups
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
                get_fill_color='[255, 0, 0]',  # Red for dropoffs
                get_radius=100,
                pickable=True,
                tooltip={
                    "html": "Dropoff Point",
                    "style": {"color": "black"},
                },
            ),
        ],
    )

    # Display the second visualization
    st.pydeck_chart(deck2)

    # Visualization: Trip Lines from Pickup to Dropoff
    st.subheader("Trip Lines from Pickup to Dropoff")
    st.write("This map shows fine lines indicating the trips from pickup to dropoff for 100 random samples.")

    # Sample 100 random rows for trip lines
    sample_trips = data.sample(100, random_state=42)

    # Create a DataFrame for the lines, including next_lat and next_lon
    trip_lines = pd.DataFrame({
        'start_lat': sample_trips['Lat'],
        'start_lon': sample_trips['Lon'],
        'end_lat': sample_trips['next_lat'],
        'end_lon': sample_trips['next_lon'],
    })

    # Create the map with lines for the trips
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
                get_color='[0, 0, 255]',  # Blue color for all lines
                get_width=2,
                pickable=True,
                tooltip={
                    "html": "Trip from Pickup to Dropoff",
                    "style": {"color": "black"},
                },
            ),
        ],
    )

    # Display the third visualization
    st.pydeck_chart(deck3)

elif page == "Time":
    # Visualization 2: Histogram of Trips by Hour
    st.subheader("Histogram of Trips by Hour")
    st.write("This histogram shows the number of trips taken during each hour of the day, revealing peak activity times.")
    data['hour'] = data['Date/Time'].dt.hour
    hourly_trips = data['hour'].value_counts().sort_index()

    # Create the histogram
    st.bar_chart(hourly_trips)

    # Ensure correct datetime format
    data['Dropoff Time'] = data['Date/Time'] + pd.to_timedelta(np.random.randint(5, 60, data.shape[0]), unit='m')

    # Calculate Trip Duration
    data['Trip Duration'] = (data['Dropoff Time'] - data['Date/Time']).dt.total_seconds() / 60  

    # Calculate the average trip duration
    average_trip_duration = data['Trip Duration'].mean()

    # Visualization: Trip Duration Histogram
    st.subheader("Trip Duration Histogram")
    st.write("This histogram shows the distribution of trip durations in minutes.")
    st.write(f"The average trip duration is {average_trip_duration:.2f} minutes.")

    plt.figure(figsize=(10, 6))
    sns.histplot(data['Trip Duration'], bins=30, kde=True)
    plt.title("Distribution of Trip Durations")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")
    st.pyplot(plt)

elif page == "Zones":
    # Ensure to include next_lat and next_lon in the sample
    data['next_lat'] = data['Lat'].shift(-1)
    data['next_lon'] = data['Lon'].shift(-1)

    # Remove rows with null next_lat or next_lon
    data.dropna(subset=['next_lat', 'next_lon'], inplace=True)

    # Visualization 5: Density Heatmap of Trips (using half the dataset)
    st.subheader("Density Heatmap of Trips")
    st.write("This heatmap shows the density of trips, highlighting the busiest areas in New York City.")
    half_data = data.sample(frac=0.4, random_state=42)  # Use 40% of the dataset

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

    # Display the heatmap visualization
    st.pydeck_chart(deck4)

    # Visualization 6: Clusters of Most Popular Pickup and Dropoff Areas
    st.subheader("Clusters of Most Popular Pickup and Dropoff Areas")
    st.write("This visualization clusters the most popular pickup and dropoff areas, allowing users to explore the frequency of trips in different zones.")

    # Sample 1000 points for clustering
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

    # Display the clusters visualization
    st.pydeck_chart(deck5)


    # Visualization 7: Popular Pickup and Dropoff Areas with Hover Information
    st.subheader("Popular Pickup and Dropoff Areas")
    st.write("This map displays clusters of the most popular pickup and dropoff areas in NYC.")

    # Count pickup and dropoff frequencies
    pickup_counts = data.groupby(['Lat', 'Lon']).size().reset_index(name='Frequency')
    dropoff_counts = data.groupby(['next_lat', 'next_lon']).size().reset_index(name='Frequency')

    # Combine pickup and dropoff counts
    pickup_counts['Type'] = 'Pickup'
    dropoff_counts['Type'] = 'Dropoff'
    combined_counts = pd.concat([pickup_counts, dropoff_counts], ignore_index=True)

    # Identify top 5 pickup and dropoff areas
    top_pickups = pickup_counts.nlargest(40, 'Frequency')
    top_dropoffs = dropoff_counts.nlargest(40, 'Frequency')

    # Create a DataFrame for clusters
    cluster_data = pd.concat([top_pickups, top_dropoffs], ignore_index=True)

    # Create clusters on the map
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
                get_fill_color='[255, 255, 255, 25]',  # White color with 90% opacity
                get_radius=600,  # Radius of 600
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
                get_fill_color='[255, 255, 255, 25]',  # White color with 90% opacity
                get_radius=600,  # Radius of 600
                pickable=True,
                tooltip={
                    "html": "<b>Dropoff Area</b><br/>Frequency: {Frequency}",
                    "style": {"color": "black"},
                },
            ),
        ],
    )

    # Display the clusters visualization
    st.pydeck_chart(deck5)

     









