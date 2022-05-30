Artist Recommendation System

----------------------
Dataset taken from:
----------------------

https://grouplens.org/datasets/hetrec-2011/
(Last.FM)

--------------------
Datasets Used
--------------------

This project uses 3 of the datasets from the given link above:
user_artists.dat
artists.dat
user_taggedartists-timestamps.dat

--------------------------
Description
--------------------------

At first, we have found the probability of what genres (tags) a user listens to and scaled it for each user on a scale of 0-100.

Then to the same dataframe a column has been added of when the given genre was allotted to the user, also further scaled from 0-100.

This is followed by probability of the genre played by an artist as heard by the users over the entire table, also further scaled from 0-100.

The final recommendation list has been developed as a triple weighted sum/product of the above three criteria following the formula - 
(userGenre + artistGenre) * userTimestamp

The basic idea here has been to use Bayes' Therem of probabilities to find the best artists to be recommended to the user.

----------------------------
Input/Output
----------------------------

The expected input to be taken from the user is an integer which would prove to be the userID of the of the user which achieves to get artist recommendations.

The output will be a list of artists from the dataset which match the genre tastes of the user and thus should be liked by them.

------------------------------
Developed By
------------------------------

Archita Singla
102003575
2CO23











