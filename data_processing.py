import ast
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from data_extraction import extract_and_save_data


def data_processing():
    """
    The purpose of this function is to read the required csv files, preprocess them and return a final merged dataframe
    Input : file_path:text, file_name:list 
    Output : merged_df : dataframe
    """

    #reading all the required csv files and storing in corresponding dataframes
    price_df=pd.read_csv("D:\\Saravanesh Personal\\Guvi\\Capstone Projects\\AirBnB\\Data_Extracted\\price_host.csv")
    address_df=pd.read_csv("D:\\Saravanesh Personal\\Guvi\\Capstone Projects\\AirBnB\\Data_Extracted\\address_availability.csv")
    listings_df=pd.read_csv("D:\\Saravanesh Personal\\Guvi\\Capstone Projects\\AirBnB\\Data_Extracted\\listings.csv")
    reviews_df=pd.read_csv("D:\\Saravanesh Personal\\Guvi\\Capstone Projects\\AirBnB\\Data_Extracted\\reviews.csv")
    review_scores_df=pd.read_csv("D:\\Saravanesh Personal\\Guvi\\Capstone Projects\\AirBnB\\Data_Extracted\\review_scores.csv")
    
    #Add the below lines of code to logging
    print("Length of listings dataframe :",len(listings_df))
    print("Length of price_host_df dataframe :",len(price_df))
    print("Length of address_availability dataframe :",len(address_df))
    print("Length of review_scores dataframe :",len(review_scores_df))
    print("Length of reviews dataframe :",len(reviews_df))

    try:

        ## Step 1 : In address_df - converting the coordinates column to two different columns - latitude & longitude
        ## Apply the conversion function to the 'coordinates' column
        address_df['coordinates'] = address_df['coordinates'].apply(lambda x: ast.literal_eval(x))

        # Split the 'coordinates' column into 'longitude' and 'latitude' columns
        address_df['longitude'] = address_df['coordinates'].apply(lambda x: x[0])
        address_df['latitude'] = address_df['coordinates'].apply(lambda x: x[1])

        # Drop the 'coordinates' column if no longer needed
        address_df.drop(columns=['coordinates'], inplace=True)

        #Merging the listings_df and address_df 
        merged_df=pd.merge(listings_df[['listing_id', "Name", "property_type","amenities"]],
            address_df[['listing_id','market','country','latitude', 'longitude','availability_30', 'availability_60','availability_90','availability_365']], on='listing_id')
        
        # Then, merge the result with price_df
        merged_df = pd.merge(merged_df,
                        price_df[['listing_id', 'price']],
                        on='listing_id')
        
        #Then merge with review scores
        merged_df=pd.merge(merged_df,
                            review_scores_df[['listing_id','review_scores_value']],
                            on='listing_id')
        
        #Merge with reviews 
        merged_review_df=pd.merge(merged_df,
                            reviews_df[['listing_id', 'review_id', 'review_date']],
                            on='listing_id')
        
        return merged_df,merged_review_df
    
    except Exception as e:
        print(f"There is some error in the data processing and the error is :{e}")


if __name__=="__main__":
    data_processing()
