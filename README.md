## Natural Language Processing

### IBM Watson
Dr Spat also suggested StanfordNLP ([Python](https://github.com/stanfordnlp/stanfordnlp), [Java](https://github.com/stanfordnlp/CoreNLP) - as "CoreNLP") when I first started. I think it's up to you guys but I thought Watson was easier to use.
#### Setting it up and running it
- [IBM Cloud API Docs / Natural Language Understanding](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python) - This helped me understand the options you can turn on/off with NLP features, and how they're nested in the feature method parameters. I think the helpful parts are:
  1. [Choosing text type](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#analyze-text),
  2. [NLP features](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#text-analytics-features), and
  3. [getting the results](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#response-details).
- Importing Watson into your code: [Python](https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/natural_language_understanding_v1.py), [Java](https://github.com/watson-developer-cloud/java-sdk/blob/master/examples/src/main/java/com/ibm/watson/natural_language_classifier/v1/NaturalLanguageClassifierExample.java)
- Software Development Kit: [Python SDK](https://github.com/watson-developer-cloud/python-sdk/blob/master/ibm_watson/natural_language_understanding_v1.py), [Java SDK](https://github.com/watson-developer-cloud/java-sdk/tree/master/natural-language-understanding/src)

### Pandas
