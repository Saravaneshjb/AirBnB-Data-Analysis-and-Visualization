import streamlit as st
from PIL import Image
from visualization import Visualization

# Function to display the Home page
def show_home():
    st.title("Air Bnb Data Analysis and Visualization")
    
    # Creating two columns
    col1, col2 = st.columns([1, 2])
    
    # Personal details on the left
    with col1:
        st.header("Personal Details")
        image = Image.open("C:\\Users\\sarav\\OneDrive\\Desktop\\Saravanesh JB.jpeg")  # Replace with the path to your photo
        st.image(image, width=150)
        st.write("**Name:** Saravanesh JB")
        st.write("**Last held Designation:** Manager-Projects")
        st.write("**Organization:** Ex-Accenture, Ex-Cognizant")
        st.write("**Bio:** Software Engineer with 11+ years of experience working in ETL, Data Analysis and Reporting Projects")
        st.write("**Contact:** Ph: 1234567, [LinkedIn](https://www.linkedin.com/your-profile)")
    
    # Project details in the center
    with col2:
        st.header("Project Details")
        st.write("**Description:** This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.")
        st.write("All the following analysis have been done")
        st.write("1. Price Analysis and Visualization")
        st.write("2. Availability analysis over different years and months")
        st.write("3. Location Based Insights")
        st.write("4. Interactive Visualizations")

# Function to display the Overall Data Analysis page
def show_overall_data_analysis():
    st.title("AirBnB Data Analysis across globe")
    
    # Geospatial representation
    # st.subheader("Geospatial representation of all AirBnB Properties across the globe")
    vs_ob=Visualization()
    fig=vs_ob.geo_spatial_visualization_all()
    #Pie Chart Representation of No. of properties across Globe
    count_by_country,avg_prop_price=vs_ob.price_analysis_visualization_all()
    #Stacked Bar Chart Displaying Total Properties Vs Vacant Properties
    #Line Chart Displaying the trend of the property occupancy over different years/months
    total_vs_avalbl,occupancy_rate_months,occupancy_rate_years=vs_ob.occupancy_visualization_all()
    # Add custom CSS to align the pie chart to the left
    

    # Create three columns for layout
    col1, col2 = st.columns([3,3])

    with col1:
        st.plotly_chart(avg_prop_price,use_container_width=True)
        # st.plotly_chart(fig,use_container_width=True) #Geospatial graph 
        # st.plotly_chart(total_vs_avalbl) # stacked bar chart 
        # st.plotly_chart(occupancy_rate_months) #Line Chart

    with col2:
        st.plotly_chart(count_by_country,use_container_width=True)
        # st.plotly_chart(avg_prop_price)
        # st.plotly_chart(occupancy_rate_years)#Line Chart 
    
    col3, col4=st.columns(2)

    with col3:
        st.plotly_chart(occupancy_rate_years,use_container_width=True)
    
    with col4:
        st.plotly_chart(occupancy_rate_months,use_container_width=True)
    
    st.plotly_chart(total_vs_avalbl,container_width=True)
    st.plotly_chart(fig,use_container_width=True)
    
    # Add custom CSS to style columns
    # Display all graphs in a single row horizontally
    # st.plotly_chart(fig, use_container_width=True) # Geospatial graph 
    # st.plotly_chart(count_by_country, use_container_width=True)
    # st.plotly_chart(avg_prop_price, use_container_width=True)
    # st.plotly_chart(total_vs_avalbl, use_container_width=True) # stacked bar chart
    # st.plotly_chart(occupancy_rate_months, use_container_width=True)
    # st.plotly_chart(occupancy_rate_years, use_container_width=True)


# Function to display the Country Based Analysis page
def show_country_based_analysis():
    
    st.title("Country Based Analysis")
    
    vs_ob = Visualization()
    merged_df = vs_ob.merged_df
    merged_review_df=vs_ob.merged_review_df

    # Create three columns for the select boxes
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Select box for Country
        country_name = merged_df['country'].unique()
        selected_country = st.selectbox("Select Country", country_name)
    
    with col2:
        # Filter cities based on the selected country
        cities = merged_df[merged_df['country'] == selected_country]['market'].unique()
        selected_cities = st.multiselect("Select Cities", cities)
    
    with col3:
        # Filter property types based on the selected cities
        if selected_cities:
            property_types = merged_df[merged_df['market'].isin(selected_cities)]['property_type'].unique()
        else:
            property_types = merged_df['property_type'].unique()
        selected_property_types = st.multiselect("Select Property Types", property_types)
    
    # Filter DataFrame based on selections
    if selected_cities and selected_property_types:
        op_df = merged_df[
            (merged_df['country'] == selected_country) &
            (merged_df['market'].isin(selected_cities)) &
            (merged_df['property_type'].isin(selected_property_types))
        ]
        op1_df = merged_review_df[
            (merged_review_df['country'] == selected_country) &
            (merged_review_df['market'].isin(selected_cities)) &
            (merged_review_df['property_type'].isin(selected_property_types))
        ]
    elif selected_cities:
        op_df = merged_df[
            (merged_df['country'] == selected_country) &
            (merged_df['market'].isin(selected_cities))
        ]
        op1_df = merged_review_df[
            (merged_review_df['country'] == selected_country) &
            (merged_review_df['market'].isin(selected_cities))
        ]
    elif selected_property_types:
        op_df = merged_df[
            (merged_df['country'] == selected_country) &
            (merged_df['property_type'].isin(selected_property_types))
        ]
        op1_df = merged_review_df[
            (merged_review_df['country'] == selected_country) &
            (merged_review_df['property_type'].isin(selected_property_types))
        ]
    else:
        op_df = merged_df[merged_df['country'] == selected_country]
        op1_df = merged_review_df[merged_review_df['country'] == selected_country]
    
    #PieChart the shows various property_type distribution
    # property_type_fig,top10_countries_price_fig,top10_countries_amenities_fig,top10_countries_reviews_fig=vs_ob.price_analysis_visualization_country(selected_country)
    property_type_fig,top10_countries_price_fig,top10_countries_amenities_fig,top10_countries_reviews_fig=vs_ob.test_price_analysis_visualization_country(op_df,selected_country)
    st.plotly_chart(property_type_fig,container_width=True)
    st.plotly_chart(top10_countries_price_fig,container_width=True)
    st.plotly_chart(top10_countries_amenities_fig,container_width=True)
    st.plotly_chart(top10_countries_reviews_fig,container_width=True)

    #Trend Graph Showing the Occupancy based on each country 
    # trend_fig_year,trend_fig_month=vs_ob.occupancy_visualization_country(selected_country)
    trend_fig_year,trend_fig_month=vs_ob.test_occupancy_visualization_country(op1_df,selected_country)
    st.plotly_chart(trend_fig_year,container_width=True)
    st.plotly_chart(trend_fig_month,container_width=True)

    #Geospatial Visaulization Specific to the Country
    # geo_spatial_country=vs_ob.geo_spatial_visualization_country(selected_country)
    geo_spatial_country=vs_ob.test_geo_spatial_visualization_country(op_df,selected_country)
    st.plotly_chart(geo_spatial_country,container_width=True)

    # Display filtered DataFrame
    st.write(op_df)

    #List of plots that needs to be drawn 
    #4. Trend Graph based on Occupancy 
    #5. A Geospatial map showing the listing ids for the country 

    

# Main function to navigate between pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home","Overall Data Analysis", "Country Based Analysis"])
    
    if page == "Home":
        show_home()
    elif page == "Overall Data Analysis":
        show_overall_data_analysis()
    elif page == "Country Based Analysis":
        show_country_based_analysis()


if __name__ == "__main__":
    main()
