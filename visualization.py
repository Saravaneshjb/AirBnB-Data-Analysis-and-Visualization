import ast
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from data_processing import data_processing


class Visualization:
    def __init__(self):
        self.merged_df,self.merged_review_df=data_processing()
    
    def geo_spatial_visualization_all(self):
        """
        This method is used to provide the geo visualization with respect to all the listing ids wrt a specific country
        """
        # Your Mapbox token
        mapbox_token = 'pk.eyJ1IjoiamJzYXJhdmFuZXNoIiwiYSI6ImNseDl2dWtscTJxZDgyanM5M3o4MTdoMXgifQ.OGRGr6rVb_ux8K7KeXZBFw'

        # Set Mapbox access token
        px.set_mapbox_access_token(mapbox_token)

        # country_name=self.merged_df['country'].unique()
        ## Ploting the geospatial map for each country
        # for country in country_name:
        # merged_df_country=self.merged_df[self.merged_df['country']==f'{country}']
        # Create the plot
        fig = px.scatter_mapbox(self.merged_df,
                                lat='latitude',
                                lon='longitude',
                                hover_name='Name',
                                hover_data={'property_type': True,
                                            'market': True,
                                            'country': True},
                                color='property_type',
                                size_max=15,
                                zoom=2,
                                height=600)

        # Update layout for better visuals
        fig.update_layout(
            title=f'Geospatial Map of Listings across globe',
            mapbox=dict(
                style='light',  # you can choose 'streets', 'outdoors', 'light', 'dark', 'satellite', 'satellite-streets'
                center=dict(lat=20, lon=0),  # center the map
                zoom=1  # starting zoom level
            )
        )

        # Show the plot
        return fig
    
    def geo_spatial_visualization_country(self,country):
        """
        This method is used to provide the geo visualization with respect to all the listing ids wrt a specific country
        """
        # Your Mapbox token
        mapbox_token = 'pk.eyJ1IjoiamJzYXJhdmFuZXNoIiwiYSI6ImNseDl2dWtscTJxZDgyanM5M3o4MTdoMXgifQ.OGRGr6rVb_ux8K7KeXZBFw'

        # Set Mapbox access token
        px.set_mapbox_access_token(mapbox_token)

        # country_name=self.merged_df['country'].unique()
        ## Ploting the geospatial map for each country
        # for country in country_name:
        merged_df_country=self.merged_df[self.merged_df['country']==f'{country}']
        # Create the plot
        fig = px.scatter_mapbox(merged_df_country,
                                lat='latitude',
                                lon='longitude',
                                hover_name='Name',
                                hover_data={'property_type': True,
                                            'market': True,
                                            'country': True},
                                color='property_type',
                                size_max=15,
                                zoom=2,
                                height=600)

        # Update layout for better visuals
        fig.update_layout(
            title=f'Geospatial Map of Listings in {country}',
            mapbox=dict(
                style='light',  # you can choose 'streets', 'outdoors', 'light', 'dark', 'satellite', 'satellite-streets'
                center=dict(lat=merged_df_country['latitude'].iloc[0], lon=merged_df_country['longitude'].iloc[0]),  # center the map
                zoom=10  # starting zoom level
            )
        )

        # Show the plot
        return fig
    

    def test_geo_spatial_visualization_country(self,df,country):
        """
        This method is used to provide the geo visualization with respect to all the listing ids wrt a specific country
        """
        # Your Mapbox token
        mapbox_token = 'pk.eyJ1IjoiamJzYXJhdmFuZXNoIiwiYSI6ImNseDl2dWtscTJxZDgyanM5M3o4MTdoMXgifQ.OGRGr6rVb_ux8K7KeXZBFw'

        # Set Mapbox access token
        px.set_mapbox_access_token(mapbox_token)

        # country_name=self.merged_df['country'].unique()
        ## Ploting the geospatial map for each country
        # for country in country_name:
        merged_df_country=df
        # Create the plot
        fig = px.scatter_mapbox(merged_df_country,
                                lat='latitude',
                                lon='longitude',
                                hover_name='Name',
                                hover_data={'property_type': True,
                                            'market': True,
                                            'country': True},
                                color='property_type',
                                size_max=15,
                                zoom=2,
                                height=600)

        # Update layout for better visuals
        fig.update_layout(
            title=f'Geospatial Map of Listings in {country}',
            mapbox=dict(
                style='light',  # you can choose 'streets', 'outdoors', 'light', 'dark', 'satellite', 'satellite-streets'
                center=dict(lat=merged_df_country['latitude'].iloc[0], lon=merged_df_country['longitude'].iloc[0]),  # center the map
                zoom=10  # starting zoom level
            )
        )

        # Show the plot
        return fig
    

    def price_analysis_visualization_all(self):
        # Price Analysis based on Location - Country
        price_analysis = self.merged_df.groupby('country')['price'].agg(['mean', 'median', 'min', 'max', 'std','count'])


        # Details about no. of properties in each country 
        price_analysis_sorted_count = price_analysis.sort_values('count', ascending=False)
        price_analysis_sorted = price_analysis.sort_values('mean', ascending=False)

        # Create a pie chart using Plotly Express
        fig1 = px.pie(price_analysis_sorted_count,
                    names=price_analysis_sorted_count.index,  # Use the index column (country names) as labels
                    values='count',  # Use the mean column for values
                    title='count of properties by country')

        # Update the traces to display the average prices on the pie chart
        fig1.update_traces(textposition='inside', 
                        textinfo='value', 
                        #   texttemplate='$%{value:.2f}',
                        hoverinfo='label+value')

        # Customize the layout for better readability
        fig1.update_layout(title_text='count of properties by Country',
                        title_x=0.1)  # Center the title
        
        # Create a pie chart using Plotly Express
        fig2 = px.pie(price_analysis_sorted,
                    names=price_analysis_sorted.index,  # Use the index column (country names) as labels
                    values='mean',  # Use the mean column for values
                    title='Avg Property Price in each country')

        # Update the traces to display the average prices on the pie chart
        fig2.update_traces(textposition='inside', 
                        textinfo='value', 
                        texttemplate='$%{value:.2f}',
                        hoverinfo='label+value')

        # Customize the layout for better readability
        fig2.update_layout(title_text='Average Property Price by Country',
                        title_x=0.1)  # Center the title


        # Show the plot
        return fig1,fig2
    
    def price_analysis_visualization_country(self,country_name):
        #Pie chart displaying a distribution of the Property type based on each country selection
        property_type_count=self.merged_df.groupby(['country','property_type'])['listing_id'].agg(['count'])
        property_type_count=property_type_count.reset_index()
        country_data = property_type_count[property_type_count['country'] == country_name]
        pie_property_type_dist_fig = px.pie(country_data, 
                    names='property_type', 
                    values='count', 
                    title=f'Property Type Distribution in {country_name}',
                    hole=0.5)  # Create a donut chart
        
        #Top 10 Properties in a Country - Based on Price 
        country_df = self.merged_df[self.merged_df['country'] == country_name].sort_values('price', ascending=False)[0:10]
        top10_countries_price_fig =  px.bar(country_df, 
                    x='Name', 
                    y='price', 
                    title=f'Top 10 Properties in {country_name} - Based on Price',
                    color='property_type',
                    category_orders={'Name': country_df['Name'].tolist()},
                    hover_data={'market': True})
        top10_countries_price_fig.update_xaxes(tickangle=45)
        top10_countries_price_fig.update_layout(xaxis_title='Property Name', 
                        yaxis_title='Price', 
                        legend_title='Property Type')

        #Top 10 Properties in a Country - Based on Amenities
        self.merged_df["amenities_count"]=self.merged_df['amenities'].apply(lambda x : len(ast.literal_eval(x)))

        country_df = self.merged_df[self.merged_review_df['country'] == country_name].sort_values('amenities_count', ascending=False)[0:10]
            
        top10_countries_amenities_fig =  px.bar(country_df, 
                    x='Name', 
                    y='amenities_count', 
                    title=f'Top 10 Properties in {country_name} - Based on no. of amenities',
                    color='property_type',
                    category_orders={'Name': country_df['Name'].tolist()},
                    hover_data={'market': True})
        top10_countries_amenities_fig.update_xaxes(tickangle=45)
        top10_countries_amenities_fig.update_layout(xaxis_title='Property Name', 
                        yaxis_title='No. of Amenities', 
                        legend_title='Property Type')
        
        #Top 10 Properties in a Country - Based on Review Scores 

        country_df = self.merged_df[(self.merged_df['country'] == country_name)&(self.merged_df['review_scores_value']!='Data unavailable')]
        # Converting the review_score_values to numeric
        country_df['review_scores_value'] = pd.to_numeric(country_df['review_scores_value'])

        # Sort by review_scores_value in descending order and get the top 10 records
        country_df = country_df.sort_values('review_scores_value', ascending=False).head(10)
        top10_countries_reviews_fig =  px.bar(country_df, 
                    x='Name', 
                    y='review_scores_value', 
                    title=f'Top 10 Properties in {country_name} - Based on Review Score',
                    color='property_type',
                    category_orders={'Name': country_df['Name'].tolist()},
                    hover_data={'market': True})
        top10_countries_reviews_fig.update_xaxes(tickangle=45)
        top10_countries_reviews_fig.update_layout(xaxis_title='Property Name', 
                        yaxis_title='review value', 
                        legend_title='Property Type')
        
        return pie_property_type_dist_fig,top10_countries_price_fig,top10_countries_amenities_fig,top10_countries_reviews_fig

    def test_price_analysis_visualization_country(self,df,country_name):
        #Pie chart displaying a distribution of the Property type based on each country selection
        property_type_count=df.groupby(['country','property_type'])['listing_id'].agg(['count'])
        property_type_count=property_type_count.reset_index()
        country_data = property_type_count
        pie_property_type_dist_fig = px.pie(country_data, 
                    names='property_type', 
                    values='count', 
                    title=f'Property Type Distribution in {country_name}',
                    hole=0.5)  # Create a donut chart
        
        #Top 10 Properties in a Country - Based on Price 
        country_df = df.sort_values('price', ascending=False)[0:10]
        top10_countries_price_fig =  px.bar(country_df, 
                    x='Name', 
                    y='price', 
                    title=f'Top 10 Properties in {country_name} - Based on Price',
                    color='property_type',
                    category_orders={'Name': country_df['Name'].tolist()},
                    hover_data={'market': True})
        top10_countries_price_fig.update_xaxes(tickangle=45)
        top10_countries_price_fig.update_layout(xaxis_title='Property Name', 
                        yaxis_title='Price', 
                        legend_title='Property Type')

        #Top 10 Properties in a Country - Based on Amenities
        df["amenities_count"]=df['amenities'].apply(lambda x : len(ast.literal_eval(x)))

        country_df = df.sort_values('amenities_count', ascending=False)[0:10]
            
        top10_countries_amenities_fig =  px.bar(country_df, 
                    x='Name', 
                    y='amenities_count', 
                    title=f'Top 10 Properties in {country_name} - Based on no. of amenities',
                    color='property_type',
                    category_orders={'Name': country_df['Name'].tolist()},
                    hover_data={'market': True})
        top10_countries_amenities_fig.update_xaxes(tickangle=45)
        top10_countries_amenities_fig.update_layout(xaxis_title='Property Name', 
                        yaxis_title='No. of Amenities', 
                        legend_title='Property Type')
        
        #Top 10 Properties in a Country - Based on Review Scores 

        country_df = df[df['review_scores_value']!='Data unavailable']
        # Converting the review_score_values to numeric
        country_df['review_scores_value'] = pd.to_numeric(country_df['review_scores_value'])

        # Sort by review_scores_value in descending order and get the top 10 records
        country_df = country_df.sort_values('review_scores_value', ascending=False).head(10)
        top10_countries_reviews_fig =  px.bar(country_df, 
                    x='Name', 
                    y='review_scores_value', 
                    title=f'Top 10 Properties in {country_name} - Based on Review Score',
                    color='property_type',
                    category_orders={'Name': country_df['Name'].tolist()},
                    hover_data={'market': True})
        top10_countries_reviews_fig.update_xaxes(tickangle=45)
        top10_countries_reviews_fig.update_layout(xaxis_title='Property Name', 
                        yaxis_title='review value', 
                        legend_title='Property Type')
        
        return pie_property_type_dist_fig,top10_countries_price_fig,top10_countries_amenities_fig,top10_countries_reviews_fig
    
    def occupancy_visualization_all(self):
        #Details of Properties available/vacant w.r.t each country 
        available_properties_df=self.merged_df[(self.merged_df['availability_30']>0)|(self.merged_df['availability_60']>0)|(self.merged_df['availability_90']>0)|(self.merged_df['availability_365']>0)].groupby('country').agg(Available_No_Properties=('country','count'))
        available_properties_df=available_properties_df.reset_index()

        #Total Properties available across globe w.r.t each country 
        total_properties_df=self.merged_df.groupby('country').agg(Total_Properties=('country','count'))
        total_properties_df=total_properties_df.reset_index()
        total_properties_df

        #Creating a new dataframe 
        properties_avlbl_df=pd.merge(total_properties_df[['country', 'Total_Properties']],
                            available_properties_df[['country', 'Available_No_Properties']],
                            on='country')


        # Create the figure - Stacked Bar Chart showing comparison of Properties 
        fig1 = go.Figure()

        # Add total properties bar
        fig1.add_trace(go.Bar(
            x=properties_avlbl_df['country'],
            y=properties_avlbl_df['Total_Properties'],
            name='Total Properties',
            marker_color='blue'
        ))

        # Add available properties bar
        fig1.add_trace(go.Bar(
            x=properties_avlbl_df['country'],
            y=properties_avlbl_df['Available_No_Properties'],
            name='Available Properties',
            marker_color='red'
        ))

        # Update layout for stacked bars
        fig1.update_layout(barmode='group',
                        title='Total and Available Properties by Country',
                        xaxis_title='Country',
                        yaxis_title='Number of Properties',
                        legend_title='Property Type')

        
        # A line chart providing trend of the occupancy over years and different months in a year
        merged_occupancy_df=self.merged_review_df

        # Line Chart Visualizing the trend of Occupancy over months & Years 

        merged_occupancy_df['review_date']=pd.to_datetime(merged_occupancy_df['review_date'])
        merged_occupancy_df['review_year']=merged_occupancy_df['review_date'].dt.year
        merged_occupancy_df['review_month']=merged_occupancy_df['review_date'].dt.strftime('%B')

        # Plot to capture the trend 

        # Define the order of months
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        # Count records for each month and sort by the defined month order
        month_counts = merged_occupancy_df['review_month'].value_counts().reindex(month_order).fillna(0)

        # Convert to DataFrame for Plotly
        month_counts_df = pd.DataFrame({'Month': month_counts.index, 'Count': month_counts.values})

        # Create a bar plot for the count of records in each month
        fig_month = px.line(month_counts_df, 
                        x='Month', 
                        y='Count', 
                        title='Occupancy count over different Months',
                        labels={'Month': 'Month', 'Count': 'Count'},
                        text='Count')
        fig_month.update_layout(xaxis_title='Month', yaxis_title='Count')
        

        # Define the range of years to be displayed
        year_range = list(range(2009, 2020))

        # Count records for each year and reindex to include all years in the range
        year_counts = merged_occupancy_df['review_year'].value_counts().reindex(year_range).fillna(0)

        # Convert to DataFrame for Plotly
        year_counts_df = pd.DataFrame({'Year': year_counts.index, 'Count': year_counts.values})

        # Create a bar plot for the count of records in each year
        fig_year = px.line(year_counts_df, 
                        x='Year', 
                        y='Count', 
                        title='Occupancy count over different Years',
                        labels={'Year': 'Year', 'Count': 'Count'},
                        text='Count')
        fig_year.update_layout(xaxis_title='Year', yaxis_title='Count')
        
        
        # Show the plot
        return fig1,fig_month,fig_year
    

    def occupancy_visualization_country(self,country_name):
        # A line chart providing trend of the occupancy over years and different months in a year
        merged_occupancy_df=self.merged_review_df

        # Line Chart Visualizing the trend of Occupancy over months & Years 

        merged_occupancy_df['review_date']=pd.to_datetime(merged_occupancy_df['review_date'])
        merged_occupancy_df['review_year']=merged_occupancy_df['review_date'].dt.year
        merged_occupancy_df['review_month']=merged_occupancy_df['review_date'].dt.strftime('%B')

        # Define the range of years to be displayed
        year_range = list(range(2009, 2020))

        # Count records for each year and reindex to include all years in the range
        year_counts_df = merged_occupancy_df[merged_occupancy_df['country']==f'{country_name}'].groupby(['country','review_year'])['review_year'].value_counts().reset_index()

        # Create a line plot for the count of records in each year
        fig_year = px.line(year_counts_df, 
                        x='review_year', 
                        y='count', 
                        title=f'Occupancy rate over different Years in {country_name}',
                        labels={'review_year': 'year', 'count': 'count'},
                        text='count')
        fig_year.update_layout(xaxis_title='Year', yaxis_title='count')

        # Define the order of months
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        # Count records for each month and sort by the defined month order
        month_counts_df = merged_occupancy_df[merged_occupancy_df['country']==f'{country_name}'].groupby(['country','review_month'])['review_month'].value_counts().reset_index()

        # Create a bar plot for the count of records in each month
        fig_month = px.line(month_counts_df, 
                        x='review_month', 
                        y='count', 
                        title=f'Occupancy rate over different Months in {country_name}',
                        labels={'review_month': 'Month', 'Count': 'count'},
                        text='count')
        fig_month.update_layout(xaxis_title='Month', yaxis_title='Count')
        
        
        return fig_year,fig_month
    
    
    def test_occupancy_visualization_country(self,df,country_name):
        # A line chart providing trend of the occupancy over years and different months in a year
        merged_occupancy_df=df

        # Line Chart Visualizing the trend of Occupancy over months & Years 

        merged_occupancy_df['review_date']=pd.to_datetime(merged_occupancy_df['review_date'])
        merged_occupancy_df['review_year']=merged_occupancy_df['review_date'].dt.year
        merged_occupancy_df['review_month']=merged_occupancy_df['review_date'].dt.strftime('%B')

        # Define the range of years to be displayed
        year_range = list(range(2009, 2020))

        # Count records for each year and reindex to include all years in the range
        year_counts_df = merged_occupancy_df.groupby(['country','review_year'])['review_year'].value_counts().reset_index()

        # Create a line plot for the count of records in each year
        fig_year = px.line(year_counts_df, 
                        x='review_year', 
                        y='count', 
                        title=f'Occupancy rate over different Years in {country_name}',
                        labels={'review_year': 'year', 'count': 'count'},
                        text='count')
        fig_year.update_layout(xaxis_title='Year', yaxis_title='count')

        # Define the order of months
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        # Count records for each month and sort by the defined month order
        month_counts_df = merged_occupancy_df.groupby(['country','review_month'])['review_month'].value_counts().reset_index()

        # Create a bar plot for the count of records in each month
        fig_month = px.line(month_counts_df, 
                        x='review_month', 
                        y='count', 
                        title=f'Occupancy rate over different Months in {country_name}',
                        labels={'review_month': 'Month', 'Count': 'count'},
                        text='count')
        fig_month.update_layout(xaxis_title='Month', yaxis_title='Count')
        
        
        return fig_year,fig_month