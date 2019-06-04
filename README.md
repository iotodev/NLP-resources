## Natural Language Processing
Here are some of the links that helped me; I hope they're useful. I'll add to these if I find anything else!

[These](https://github.com/dlabctawg) are the people Dr Spat mentioned, that are doing something similar to your project. We just found them the other day.

### IBM Watson
Dr Spat also suggested StanfordNLP ([Python](https://github.com/stanfordnlp/stanfordnlp), [Java](https://github.com/stanfordnlp/CoreNLP) - as "CoreNLP") when I first started. I think it's up to you guys but I thought Watson was easier to use.
#### Setting it up and running it
- [IBM Cloud API Docs / Natural Language Understanding](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python) - This helped me understand the options you can turn on/off with NLP features, and how they're nested in the feature method parameters. I think the helpful parts are:
  1. [Choosing text type](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#analyze-text),
  2. [NLP features](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#text-analytics-features), and
  3. [getting the results](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#response-details).
- Importing Watson into your code: [Python](https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/natural_language_understanding_v1.py), [Java](https://github.com/watson-developer-cloud/java-sdk/blob/master/examples/src/main/java/com/ibm/watson/natural_language_classifier/v1/NaturalLanguageClassifierExample.java)
  - [API Key](https://www.protectedtext.com/ioto) (Password is your ISSP teacher's name)
- Software Development Kit: [Python SDK](https://github.com/watson-developer-cloud/python-sdk/blob/master/ibm_watson/natural_language_understanding_v1.py), [Java SDK](https://github.com/watson-developer-cloud/java-sdk/tree/master/natural-language-understanding/src)
#### Other stuff
- [NLU on Webpages](https://cloud.ibm.com/docs/services/natural-language-understanding?topic=natural-language-understanding-analyzing-webpages) - using Watson without a web scraper
- [Getting metadata from webpages](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#analyze-text) - found under Reponse > AnalysisResults
- [Categories](https://cloud.ibm.com/docs/services/natural-language-understanding?topic=natural-language-understanding-categories-hierarchy) - all of the categories recognized by the categories NLP feature; there's a category for "law, govt and politics" with subcategories that might be helpful.
- The [curated list](https://github.com/keon/awesome-nlp) I mentioned with a lot of general stuff about NLP. Maybe it's not that useful for the project.

### Word2vec
Puts words into a 3D space (I think it's actually more than 3D), with similar words having closer coordinates (vectors). Like "gun" and "firearm" will have close vectors.

I think it might help if you're looking for mentions of a topic (like guns) and want your program to pick up all words similar enough to "gun" (like firearm or rifle) -  within a certain tolerance level.
- [Good pictures that explain the concept](https://www.tensorflow.org/tutorials/representation/word2vec#the_skip-gram_model)
- [Implementation and output example](https://nbviewer.jupyter.org/github/danielfrg/word2vec/blob/master/examples/word2vec.ipynb#Similarity)
- Github repos: [Python](https://github.com/danielfrg/word2vec), [Java](https://deeplearning4j.org/docs/latest/deeplearning4j-nlp-word2vec)

### Beautiful Soup
HTML Parser (web scraper) for Python.

- Just two links that my Python teacher Chris Thompson gave me, they really helped: [1](https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/) & [2](https://code.datasciencedojo.com/datasciencedojo/tutorials/blob/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py)
- Then my code: https://github.com/brodieheywood/BeautifulSoup-demo/blob/master/web_scraper.py - If you look at the HTML for the webpage it scrapes from, the "paragraph" and "tag" variable definitions make more sense. It might be helpful if you're trying to access elements with a certain ID (or IDs containing a regex) from a specific class.

### Pandas
Pandas is a Python library that can make [data frames](https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm) from data.

The House of Commons gives out all their data as csv files, so I needed a library that could read them into my code. You might not need Pandas for that, but it might be helpful as an alternative to SQL in certain situations. Maybe you could pull from the SQL database, into a Pandas DataFrame, and then do all of your grouping with pandas.groupby (it might be faster? I actually don't know).

I hope that makes sense. I attached some code that you can run to see it working.
- [Tutorial]() - I can't remember which site I used to learn about Pandas! I'm sorry.
- [Grouping data](https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm)
  - Something I did with that: https://github.com/brodieheywood/Pandas-groupby-demo/blob/master/csv_reader.py
- [Converting a Dataframe to a csv File](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) - Part of the Pandas (Python 2) API. Shows optional .to_csv method parameters, like "columns," where you can choose which columns to include in the output csv.
- [DataFrame to SQL](https://github.com/connellblackett/pandas-mssql/blob/master/pandas_mssql/__init__.py) - I think this might be helpful for getting data frames into/out of an SQL database

#### Pandas Troubleshooting
- [Ignoring blank lines when reading from csv](https://github.com/pandas-dev/pandas/pull/7470) - If you're having this problem, you'll probably need more help than that... I might be able to help, but I only solved my problems by iterating through each row and appending only non-blank rows to a list. Awful solution. I think there was an issue with the csv's encoding?
- [Ignoring commas inside cells](https://stackoverflow.com/questions/46081317/reading-csv-with-pandas-and-ignoring-commas#46116006) - by default, Pandas treats commas as column delimiters. Setting a new delimiter gets around this.

### GeoPandas
Python library for interacting with maps (drawing the maps, reading the maps, colouring the maps, associating variables with areas on the map).

- Here's their [GitHub repo](https://github.com/geopandas/geopandas)
- But [the notes from this class](http://darribas.org/gds15) are way more helpful; there are [coding examples](http://darribas.org/gds15/content/labs/lab_03.html) in the labs.

### Graphics
I think you guys have a lot of freedom here, just trying to come up with graphics that get people interested in politics. Some of our ideas were:
- what is the least mentioned topic from news headlines that week (what are politicians trying to avoid talking about)
- where was the biggest change of opinion (like, did Alabama's representatives suddenly go from consistently negative sentiment about carbon tax, to positive?)
- what are the most popular topics, per region

Here's what Allan, who worked in TV, has said:

> Each one should tell a simple story, not resemble reference material. Think TLDR on steroids.
> My overarching concern however is that this is primarily just text and numbers, something that all the networks even with their reduced staffing levels are able to produce to varying degrees. What they consistently struggle with and therefore, something to emphasis and attempt to capitalize on are maps and graphs.


I think you'll talk about it more during the Skype meetings too. 
Here are some of the ideas that Dr Spat has sent me:

- [Choropleth map examples](https://towardsdatascience.com/the-power-of-visualization-in-data-science-1995d56e4208) - how the "political forecast" might be presented, showing the geographical spread of ideas over time
- [DAZN's design](https://drive.google.com/file/d/1vIoa1_C-kesKjiAx-MULkwHaIwa_cEky/view) - Dr Spat mentioned this during the first meeting, just as an example of how sports networks present statistics, and how we might take cues from them.
- [IBM's Tennis Analytics](https://www.ibmbigdatahub.com/tag/605) - IBM is really good at presenting stats/analytics; they do it for pro tennis.
- [Tethne](http://diging.github.io/tethne/api/tutorial.mallet.html#semantic-graph) - maybe?

### Contacts
What I know about them and how they can help us.
