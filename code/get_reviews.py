# Import the required libraries
import pandas as pd
from google_play_scraper import Sort, reviews, app


def get_reviews():
    app_name = 'com.mufumbo.android.recipe.search'

    # Get reviews
    collected_reviews = []

    review_result, continuation_token = reviews(
                                            app_name,
                                            lang='en',
                                            sort=Sort.NEWEST,
                                            count=200)
    
    collected_reviews.extend(review_result)

    # set the range to be num of posted reviews/count value. 
    # ex: 1400 = 280,000 (the num of posted reviews)/ 200 (count set above)
    for batch_count in range(100):  
        review_result, continuation_token = reviews(app_name, continuation_token=continuation_token)
        collected_reviews.extend(review_result)
        print(f'On Batch {batch_count}')


    print(f'DONE! Collected {len(collected_reviews)} reviews')

    raw_reviews_df = pd.DataFrame(collected_reviews)
    raw_reviews_df.to_csv('../data/cookpad_reviews_raw.csv', index=None, header=True)