# DUE 11/20

# READING (you will be asked questions on this after thanks giving)
_On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜_
https://s10251.pcdn.co/pdf/2021-bender-parrots.pdf

# Assignment: Follow the notebook 
the only steps that remains are:
- do the word cloud for the Sentiment==0 and Sentiment==4 reviews. 

remember to comment on your figures? describe what a word cloud is and how to interpret it and highlight the differences beteeen Sentiment==0 and ==4

- perform the sentiment analysis.

You are using a pretrained model that weights each word independently by its positive/negative weight and sums the weights of all words. 

NOTE: 
This is not an ideal way to do sentiment analysis - the correct way, and the intended use of the data, would be to _train_ the model on this dataset because otherwise the positive/negative connotation of the words is taken out of context and may not be applicable in general (e.g. a model trained for sentiment analysis on twitter, where posts are of limited length, may not perform on a book analysis)

