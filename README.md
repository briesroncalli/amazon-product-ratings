# amazon-product-reviews

### avgRatings.py
Basic spark application computing the total number of Amazon reviews and the average rating of each product & sorts by product ID.
Data from https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Electronics_v1_00.tsv.gz

### similarRatings.py
MapReduce application that finds pairs of users who gave a rating of at least 4 to at least 3 common products, sorted by the first 
customer_id in the pairs of users.
