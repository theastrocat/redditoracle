# Reddit Oracle
Reddit front page prediction from titles and subreddit origin.

### Businuess Understanding:
Sentiment analysis is a complex topic, I believe there is a perfect application to see how people react to headlines. Here we can use the reddit's voting engine on what is "popular" to see how people react to headlines.

### Data Understanding:
The data would be headlines, times, web-urls, and subreddits of new and front page posts.

### Data Preparation:
Using standard NLP modeling techniques, TF-IDF, tokenizing, stemming of headlines.

### Modeling:
Using a classification model, or ensemble of classification models with labels as to whether or not they made it to the front page.

### Evaluation:
Accuracy as to whether or not predicted posts make it to the front page.

### Deployment:
Web app with word cloud, and allows users to get a prediction probability on a headline they type in.
