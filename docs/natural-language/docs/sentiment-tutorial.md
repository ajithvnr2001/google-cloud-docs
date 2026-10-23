---
url: https://docs.cloud.google.com/natural-language/docs/sentiment-tutorial/
title: Sentiment Analysis Tutorial \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:42.696168+00:00
---

# Sentiment Analysis Tutorial  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/sentiment-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback 

#  Sentiment Analysis Tutorial Stay organized with collections  Save and categorize content based on your preferences. 

## Audience

This tutorial is designed to let you quickly start exploring and developing applications with the Google Cloud Natural Language API. It is designed for people familiar with basic programming, though even without much programming knowledge, you should be able to follow along. Having walked through this tutorial, you should be able to use the [Reference documentation](https://docs.cloud.google.com/natural-language/docs/reference/rest) to create your own basic applications.

This tutorial steps through a Natural Language API application using Python code. The purpose here is not to explain the Python client libraries, but to explain how to make calls to the Natural Language API. Applications in Java and Node.js are essentially similar. Consult the Natural Language API [Samples](https://docs.cloud.google.com/natural-language/docs/sample-apps) for samples in other languages (including this sample within the tutorial).

## Prerequisites

This tutorial has several prerequisites:

  * You have a Google Cloud account. If you're new to the platform, [create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads.
  * You've [set up a Cloud Natural Language API project](https://docs.cloud.google.com/natural-language/docs/getting-started#set_up_a_project) in the Google Cloud console.
  * You've set up your environment using [Application Default Credentials](https://docs.cloud.google.com/natural-language/docs/common/auth#adc).
  * You have basic familiarity with [Python](https://www.python.org/) programming.
  * You have set up your Python development environment. It is recommended that you have the latest version of Python, `pip`, and `virtualenv` installed on your system. For instructions, see the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup) for Google Cloud Platform.
  * You've installed the [Google Cloud Client Library for Python](https://docs.cloud.google.com/natural-language/docs/reference/libraries)



## Analyzing document sentiment

This tutorial walks you through a basic Natural Language API application, using an `analyzeSentiment` request, which performs sentiment analysis on text. Sentiment analysis attempts to determine the overall attitude (positive or negative) and is represented by numerical `score` and `magnitude` values. (For more information on these concepts, consult [Natural Language Basics](https://docs.cloud.google.com/natural-language/docs/basics#sentiment-analysis-values).)

We'll show the entire code first. (Note that we have removed most comments from this code in order to show you how brief it is. We'll provide more comments as we walk through the code.)

**Note:** To copy the code to your clipboard, click the copy widget that appears in the top-right of the code snippet when you mouseover the code snippet. Copy this code into a `sentiment_analysis.py` file within your development directory. For more information on installing and using the Google Cloud Natural Language Client Library for Python, see [Natural Language API Client Libraries](https://cloud.google.com/natural-language/docs/reference/libraries). 
    
    
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

This simple application performs the following tasks:

  * Imports the libraries necessary to run the application
  * Takes a text file and passes it to the `main()` function
  * Reads the text file and makes a request to the service
  * Parses the response from the service and displays it to the user



We'll go over these steps in more detail below.

## Importing libraries

For more information on installing and using the Google Cloud Natural Language Client Library for Python, see [Natural Language API Client Libraries](https://cloud.google.com/natural-language/docs/reference/libraries). 
    
    
    import argparse
    
    from google.cloud import language_v1
    

We import `argparse`, a standard library, to allow the application to accept input filenames as arguments.

For using the Cloud Natural Language API, we'll also want to import the `language` module from the `google-cloud-language` library. The `types` module contains classes that are required for creating requests.

## Running your application
    
    
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

Here, we simply parse the passed argument for the text filename and pass it to the `analyze()` function.

## Authenticating to the API

Before communicating with the Natural Language API service, you need to authenticate your service using previously acquired credentials. Within an application, the simplest way to obtain credentials is to use [Application Default Credentials](https://docs.cloud.google.com/natural-language/docs/common/auth#adc) (ADC). By default, ADC will attempt to obtain credentials from the `GOOGLE_APPLICATION_CREDENTIALS` environment file, which should be set to point to your service account's JSON key file. (You should have set up your service account and environment to use ADC in the [Quickstart](https://docs.cloud.google.com/natural-language/docs/getting-started). See [Setting Up a Service Account](https://docs.cloud.google.com/natural-language/docs/common/auth#set_up_a_service_account) for more information.)

The Google Cloud Client Library for Python automatically uses the application default credentials.

## Making the request

Now that our Natural Language API service is ready, we can access the service by calling the `analyze_sentiment` method of the `LanguageServiceClient` instance.

The client library encapsulates the details for requests and responses to the API. See the [Natural Language API Reference](https://docs.cloud.google.com/natural-language/docs/reference/rest) for complete information on the specific structure of such a request.

For more information on installing and using the Google Cloud Natural Language Client Library for Python, see [Natural Language API Client Libraries](https://cloud.google.com/natural-language/docs/reference/libraries). 
    
    
    def analyze(movie_review_filename):
        """Run a sentiment analysis request on text within a passed filename."""
        client = language_v1.LanguageServiceClient()
    
        with open(movie_review_filename) as review_file:
            # Instantiates a plain text document.
            content = review_file.read()
    
        document = language_v1.Document(
            content=content, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        annotations = client.analyze_sentiment(request={"document": document})
    
        # Print the results
        print_result(annotations)
    
    

This code snippet performs the following tasks:

  1. Instantiates a `LanguageServiceClient` instance as the client.
  2. Reads the filename containing the text data into a variable.
  3. Instantiates a `Document` object with the contents of the file.
  4. Calls the client's `analyze_sentiment` method.



## Parsing the response
    
    
    def print_result(annotations):
        score = annotations.document_sentiment.score
        magnitude = annotations.document_sentiment.magnitude
    
        for index, sentence in enumerate(annotations.sentences):
            sentence_sentiment = sentence.sentiment.score
            print(f"Sentence {index} has a sentiment score of {sentence_sentiment}")
    
        print(f"Overall Sentiment: score of {score} with magnitude of {magnitude}")
        return 0
    
    

We walk through the response to extract the sentiment `score` values for each sentence, and the overall `score` and `magnitude` values for the entire review, and display those to the user.

## Run the sample

To run our sample, we'll test it on a set of (fake) movie reviews for the movie "Bladerunner."

  1. Download the samples from Google Cloud Storage:
         
         gcloud storage cp gs://cloud-samples-tests/natural-language/sentiment-samples.tgz .
         

To install the latest version of Google Cloud CLI, refer to [gcloud CLI documentation](https://docs.cloud.google.com/sdk/docs).

  2. Unzip those samples, which will create a "**reviews** " folder:
         
         gunzip sentiment-samples.tgz
         tar -xvf sentiment-samples.tar
         

  3. Run our sentiment analysis on one of the specified files:
         
         python sentiment_analysis.py reviews/bladerunner-pos.txt
         Sentence 0 has a sentiment score of 0.8
         Sentence 1 has a sentiment score of 0.9
         Sentence 2 has a sentiment score of 0.8
         Sentence 3 has a sentiment score of 0.2
         Sentence 4 has a sentiment score of 0.1
         Sentence 5 has a sentiment score of 0.4
         Sentence 6 has a sentiment score of 0.3
         Sentence 7 has a sentiment score of 0.4
         Sentence 8 has a sentiment score of 0.2
         Sentence 9 has a sentiment score of 0.9
         Overall Sentiment: score of 0.5 with magnitude of 5.5
         




The above example would indicate a review that was relatively positive (score of `0.5`), and relatively emotional (magnitude of `5.5`).

Running analysis on the other examples should produce values similar to those shown below:
    
    
    python sentiment_analysis.py reviews/bladerunner-neg.txt
    ...
    Overall Sentiment: score of -0.6 with magnitude of 3.3
    
    python sentiment_analysis.py reviews/bladerunner-mixed.txt
    ...
    Overall Sentiment: score of 0 with magnitude of 4.7
    
    python sentiment_analysis.py reviews/bladerunner-neutral.txt
    ...
    Overall Sentiment: score of -0.1 with magnitude of 1.8
    

Note that the magnitudes are all similar (indicating a relative equal amount of emotionally significant sentiment) except for the "neutral" case, which indicates a review with not very much emotional sentiment, either positive or negative. (For more information on sentiment scores and magnitude, and how to interpret these values, see [Interpreting Sentiment Analysis Values](https://docs.cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values).)

If you wish to explore sentiment analysis with more data, Stanford provides a dataset of [IMDB](http://www.imdb.com) movie reviews. To retrieve these movie reviews:

  1. Download the [Large Movie Review dataset](http://ai.stanford.edu/%7Eamaas/data/sentiment/).
  2. Unzip the file into your working directory. The movie reviews are divided into `pos` and `neg` directories within `train` and `test` data directories, with each text file containing one movie review.
  3. Run the `sentiment_analysis.py` tool on any of the movie review text files.



Congratulations! You've performed your first inference tasks using the Google Cloud Natural Language API!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
