# Application overview
### Members
- Yaoyu Cheng
- Ruilin Jin
- Winnie Lu
- Yiran Zheng
- Michelle Zhou
 

## Available functionality
- [ ] NCAA Player lookup
      -> enter in NBA or not
		-> in
			-> stat
		-> not in
			-> stat
- [ ] NBA Player lookup
      -> was in NCAA or not
		-> in 
			->stat
		-> not in
			-> stat
- [ ] Annual NCAA statistics review
        > Average height and height range
	> Best school
	> Worst school
	> Top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
	> Top 10 players with highest % of ^^

- [ ] Annual NBA statistics review
        > Average height and height range
	> Best Team
	> Worst Team
	> Top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
	> Top 10 players with highest % of ^^


## Setting up the application

Because one of our datasets was found on Kaggle and wasn't compatible with the format of `retrieve_data.py`, we have hosted some of our datasets in this GitHub repository and linked them in the `datasets.txt` file. The files can be found in the `KaggleDatasets` folder.

Once the datasets have all been downloaded, simply run the following files in the following order:
1. `db_setup.sql`
2. `load_data.py`
3. `application.py`
