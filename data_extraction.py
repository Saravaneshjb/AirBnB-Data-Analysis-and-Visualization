import os
import shutil
import pandas as pd
import json

class DataExtraction:
    def __init__(self,file_path):
        self.file_path=file_path
    
    def listings(self):
        # Opening the file and retrieving the reviews details 
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # sample_data = data[1:961]
        listings_dict = {
            'listing_id':[],
            'listing_url': [],
            'Name': [],
            'house_rules': [],
            'property_type': [],
            'room_type': [],
            'bed_type': [],
            'minimum_nights':[],
            'maximum_nights':[],
            'cancellation_policy':[],
            'accomodates':[],
            'no_of_bedrooms':[],
            'no_of_beds':[],
            'no_of_reviews':[],
            'no_of_bathrooms':[],
            'amenities':[],
            'thumbnail_url':[],
            'picture_url':[]
        }

        for listings in data:
            listings_dict['listing_id'].append(listings['_id'])
            listings_dict['listing_url'].append(listings.get('listing_url', 'Data unavailable'))
            listings_dict['Name'].append(listings.get('name', 'Data unavailable'))
            listings_dict['house_rules'].append(listings.get('house_rules', 'Data unavailable'))
            listings_dict['property_type'].append(listings.get('property_type', 'Data unavailable'))
            listings_dict['room_type'].append(listings.get('room_type', 'Data unavailable'))
            listings_dict['bed_type'].append(listings.get('bed_type', 'Data unavailable'))
            listings_dict['minimum_nights'].append(listings.get('minimum_nights', 'Data unavailable'))
            listings_dict['maximum_nights'].append(listings.get('maximum_nights', 'Data unavailable'))
            listings_dict['cancellation_policy'].append(listings.get('cancellation_policy', 'Data unavailable'))
            listings_dict['accomodates'].append(listings.get('accommodates', 'Data unavailable'))
            listings_dict['no_of_bedrooms'].append(listings.get('bedrooms', 'Data unavailable'))
            listings_dict['no_of_beds'].append(listings.get('beds', 'Data unavailable'))
            listings_dict['no_of_reviews'].append(listings.get('number_of_reviews', 'Data unavailable'))
            listings_dict['no_of_bathrooms'].append(listings.get('bathrooms', 'Data unavailable'))
            listings_dict['amenities'].append(listings.get('amenities', 'Data unavailable'))
            listings_dict['thumbnail_url'].append(listings['images'].get('thumbnail_url', 'Data unavailable'))
            listings_dict['picture_url'].append(listings['images'].get('picture_url', 'Data unavailable'))
        
        listings_df=pd.DataFrame(listings_dict)

        return listings_df
    
    def price_host_details(self):
        # Opening the file and retrieving the reviews details 
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # sample_data = data[1:961]
        price_host_dict = {
            'listing_id':[],
            'price': [],
            'security_deposit': [],
            'cleaning_fee': [],
            'extra_people': [],
            'guests_included': [],
            'host_id': [],
            'host_url':[],
            'host_name':[],
            'host_location':[],
            'host_about':[],
            'host_response_time':[],
            'host_thumbnail_url':[],
            'host_picture_url':[],
            'host_neighbourhood':[],
            'host_response_rate':[],
            'host_is_superhost':[],
            'host_has_profile_pic':[],
            'host_identity_verified':[],
            'host_verifications':[]
        }

        for listings in data:
            price_host_dict['listing_id'].append(listings['_id'])
            price_host_dict['price'].append(listings.get('price', 'Data unavailable'))
            price_host_dict['security_deposit'].append(listings.get('security_deposit', 'Data unavailable'))
            price_host_dict['cleaning_fee'].append(listings.get('cleaning_fee', 'Data unavailable'))
            price_host_dict['extra_people'].append(listings.get('extra_people', 'Data unavailable'))
            price_host_dict['guests_included'].append(listings.get('guests_included', 'Data unavailable'))
            price_host_dict['host_id'].append(listings['host'].get('host_id', 'Data unavailable'))
            price_host_dict['host_url'].append(listings['host'].get('host_url', 'Data unavailable'))
            price_host_dict['host_name'].append(listings['host'].get('host_name', 'Data unavailable'))
            price_host_dict['host_location'].append(listings['host'].get('host_location', 'Data unavailable'))
            price_host_dict['host_about'].append(listings['host'].get('host_about', 'Data unavailable'))
            price_host_dict['host_response_time'].append(listings['host'].get('host_response_time', 'Data unavailable'))
            price_host_dict['host_thumbnail_url'].append(listings['host'].get('host_thumnail_url', 'Data unavailable'))
            price_host_dict['host_picture_url'].append(listings['host'].get('host_picture_url', 'Data unavailable'))
            price_host_dict['host_neighbourhood'].append(listings['host'].get('host_neighbourhood', 'Data unavailable'))
            price_host_dict['host_response_rate'].append(listings['host'].get('host_response_rate', 'Data unavailable'))
            price_host_dict['host_is_superhost'].append(listings['host'].get('host_is_superhost', 'Data unavailable'))
            price_host_dict['host_has_profile_pic'].append(listings['host'].get('host_has_profile_pic', 'Data unavailable'))
            price_host_dict['host_identity_verified'].append(listings['host'].get('host_identity_verified', 'Data unavailable'))
            price_host_dict['host_verifications'].append(listings['host'].get('host_verifications', 'Data unavailable'))

        price_host_df=pd.DataFrame(price_host_dict)

        return price_host_df
    
    def address_availabilty(self):
        # Opening the file and retrieving the reviews details 
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # sample_data = data[1:961]
        address_availability_dict = {
            'listing_id':[],
            'street': [],
            'suburb': [],
            'government_area': [],
            'market': [],
            'country': [],
            'coordinates': [],
            'is_location_exact':[],
            'availability_30':[],
            'availability_60':[],
            'availability_90':[],
            'availability_365':[]
        }

        for listings in data:
            address_availability_dict['listing_id'].append(listings['_id'])
            address_availability_dict['street'].append(listings['address'].get('street', 'Data unavailable'))
            address_availability_dict['suburb'].append(listings['address'].get('suburb', 'Data unavailable'))
            address_availability_dict['government_area'].append(listings['address'].get('government_area', 'Data unavailable'))
            address_availability_dict['market'].append(listings['address'].get('market', 'Data unavailable'))
            address_availability_dict['country'].append(listings['address'].get('country', 'Data unavailable'))
            address_availability_dict['is_location_exact'].append(listings['address']['location'].get('is_location_exact', 'Data unavailable'))
            address_availability_dict['coordinates'].append(listings['address']['location'].get('coordinates', 'Data unavailable'))
            address_availability_dict['availability_30'].append(listings['availability'].get('availability_30', 'Data unavailable'))
            address_availability_dict['availability_60'].append(listings['availability'].get('availability_60', 'Data unavailable'))
            address_availability_dict['availability_90'].append(listings['availability'].get('availability_90', 'Data unavailable'))
            address_availability_dict['availability_365'].append(listings['availability'].get('availability_365', 'Data unavailable'))
        
        address_availability_df=pd.DataFrame(address_availability_dict)

        return address_availability_df
    
    def review_score_details(self):
        # Opening the file and retrieving the reviews details 
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # sample_data = data[1:961]
        reviews_scores_dict = {
            'listing_id':[],
            'review_scores_accuracy': [],
            'review_scores_cleanliness': [],
            'review_scores_checkin': [],
            'review_scores_communication': [],
            'review_scores_location': [],
            'review_scores_value': [],
            'review_scores_rating':[]
        }

        for listings in data:
            reviews_scores_dict['listing_id'].append(listings['_id'])
            reviews_scores_dict['review_scores_accuracy'].append(listings['review_scores'].get('review_scores_accuracy', 'Data unavailable'))
            reviews_scores_dict['review_scores_cleanliness'].append(listings['review_scores'].get('review_scores_cleanliness', 'Data unavailable'))
            reviews_scores_dict['review_scores_checkin'].append(listings['review_scores'].get('review_scores_checkin', 'Data unavailable'))
            reviews_scores_dict['review_scores_communication'].append(listings['review_scores'].get('review_scores_communication', 'Data unavailable'))
            reviews_scores_dict['review_scores_location'].append(listings['review_scores'].get('review_scores_location', 'Data unavailable'))
            reviews_scores_dict['review_scores_value'].append(listings['review_scores'].get('review_scores_value', 'Data unavailable'))
            reviews_scores_dict['review_scores_rating'].append(listings['review_scores'].get('review_scores_rating', 'Data unavailable'))
        
        review_scores_df=pd.DataFrame(reviews_scores_dict)

        return review_scores_df
    

    def reviews(self):
        # Opening the file and retrieving the reviews details 
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # sample_data = data[1:961]
        reviews_dict = {
            'review_id': [],
            'review_date': [],
            'listing_id': [],
            'reviewer_id': [],
            'reviewer_name': [],
            'comments': []
        }

        for listings in data:
            # print(f"Processing the listing_id : {listings['_id']}")
            for reviews in listings['reviews']:
                reviews_dict['review_id'].append(reviews.get('_id', 'Data unavailable'))
                reviews_dict['review_date'].append(reviews.get('date', 'Data unavailable'))
                reviews_dict['listing_id'].append(reviews.get('listing_id', 'Data unavailable'))
                reviews_dict['reviewer_id'].append(reviews.get('reviewer_id', 'Data unavailable'))
                reviews_dict['reviewer_name'].append(reviews.get('reviewer_name', 'Data unavailable'))
                reviews_dict['comments'].append(reviews.get('comments', 'Data unavailable'))
        
        reviews_df=pd.DataFrame(reviews_dict)

        return reviews_df


def extract_and_save_data():
    file_path = "D:\\Saravanesh Personal\\Guvi\\Capstone Projects\\AirBnB\\Data\\sample_airbnb.json"
    extractor = DataExtraction(file_path)
    
    # Directory for storing extracted data
    output_dir = "Data_Extracted"
    
    # Remove existing directory and its contents, if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # Create a new directory
    os.makedirs(output_dir)
    try:
        # Run extraction methods and save CSVs
        listings_df = extractor.listings()
        listings_df.to_csv(os.path.join(output_dir, 'listings.csv'), index=False)
        
        price_host_df = extractor.price_host_details()
        price_host_df.to_csv(os.path.join(output_dir, 'price_host.csv'), index=False)
        
        address_availability_df = extractor.address_availabilty()
        address_availability_df.to_csv(os.path.join(output_dir, 'address_availability.csv'), index=False)

        review_scores_df = extractor.review_score_details()
        review_scores_df.to_csv(os.path.join(output_dir, 'review_scores.csv'), index=False)

        reviews_df = extractor.reviews()
        reviews_df.to_csv(os.path.join(output_dir, 'reviews.csv'), index=False)

        return listings_df, price_host_df, address_availability_df, review_scores_df, reviews_df
    except Exception as e:
        print(f"An error occured during extraction : {e}")
        return None,None,None,None,None


if __name__ == "__main__":
    listings_df,price_host_df,address_availability_df,review_scores_df,reviews_df=extract_and_save_data()





