---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-sentiment-tutorial/
title: Analyze sentiment app \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:53.689928+00:00
---

# Analyze sentiment app  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-sentiment-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Analyze sentiment app Stay organized with collections  Save and categorize content based on your preferences. 

A basic Natural Language API application that performs sentiment analysis on text.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Sentiment Analysis Tutorial](https://docs.cloud.google.com/natural-language/docs/sentiment-tutorial)



## Code sample

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """Demonstrates how to make a simple call to the Natural Language API."""
    
    import argparse
    
    from google.cloud import language_v1
    
    
    
    def print_result(annotations):
        score = annotations.document_sentiment.score
        magnitude = annotations.document_sentiment.magnitude
    
        for index, sentence in enumerate(annotations.sentences):
            sentence_sentiment = sentence.sentiment.score
            print(f"Sentence {index} has a sentiment score of {sentence_sentiment}")
    
        print(f"Overall Sentiment: score of {score} with magnitude of {magnitude}")
        return 0
    
    
    
    
    def analyze(movie_review_filename):
        """Run a sentiment analysis request on text within a passed filename."""
        client = language_v1.LanguageServiceClient()
    
        with open(movie_review_filename) as review_file:
            # Instantiates a plain text document.
            content = review_file.read()
    
        document = language_v1.Document(
            content=content, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        annotations = client.[analyze_sentiment](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_sentiment)(request={"document": document})
    
        # Print the results
        print_result(annotations)
    
    
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument(
            "movie_review_filename",
            help="The filename of the movie review you'd like to analyze.",
        )
        args = parser.parse_args()
    
        analyze(args.movie_review_filename)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudnaturallanguageapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
