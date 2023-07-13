# Udacity-data-analyst-4-project-Wrangle-and-Analyze-Data

This project focuses on wrangling the WeRateDogs Twitter data to generate meaningful analyses and visualizations. The Twitter archive provides some basic tweet information, but additional steps are necessary to gather, assess, and clean the data for valuable insights.

![WERATEDOG](IMG_3502.JPG)

The data wrangling process consists of three main parts:

## Data Gathering:

Downloading the WeRateDogs Twitter archive data (twitter_archive_enhanced.csv)
Obtaining the tweet image predictions (image_predictions.tsv) using the Requests library
Querying additional data through the Twitter API (tweet_json.txt) with the Tweepy library
## Data Assessment:

Identifying duplicates, missing values, and invalid entries during the data assessment phase.

## Data Cleaning:

Based on considerations of data completeness, validity, accuracy, and consistency, the following quality and tidiness issues were addressed:

In the 'archive_df' table:

Merging the 'archive_df' and 'tweets' tables based on tweet_id and filtering 'archive_df' to include only rows present in 'tweets'
Removing columns related to retweets and replies in the 'archive_df' table
Extracting dog names from the tweet text in the 'Name' column of 'archive_df'
Verifying if the rating score in the 'text' column matches the combination of 'denominator' and 'numerator' columns in 'archive_df'
Removing the "+0000" from the 'timestamp' column in 'archive_df' and converting it to datetime format
Dropping unnecessary 'expanded_url' columns
Extracting the source of the tweet from the 'source' column
In the 'prediction' table:
8. Removing rows in the 'prediction' table where the tweet_id does not match the merged 'df_clean' table

In the 'archive_df' table:

Creating a categorical column called 'dog stage' to represent the dog's stage using the 'doggo', 'floofer', 'pupper', and 'puppo' columns
Combining the 'rating_numerator' and 'rating_denominator' columns into a single column called 'rating score of the dog' in fractional form.
