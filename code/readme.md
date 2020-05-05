# Application overview
###Members
- Yaoyu Cheng
- Ruilin Jin
- Zhou Lu
- Yiran Zheng
- Michelle Zhou
 

## Available functionality
- [ ] NCAA Player lookup
- [ ] NBA Player lookup
- [ ] Annual NCAA statistics review
- [ ] Annual NBA statistics review


## Setting up the application

Because one of our datasets was found on Kaggle and wasn't compatible with the format of `retrieve_data.py`, we have hosted some of our datasets in this GitHub repository and linked them in the `datasets.txt` file. The files can be found in the `KaggleDatasets` folder.

Once the datasets have all been downloaded, simply run the following files in the following order:
1. `db_setup.sql`
2. `load_data.py`
3. `application.py`
