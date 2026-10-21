---
url: https://docs.cloud.google.com/natural-language/docs/classify-text-tutorial/
title: Content Classification Tutorial \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:54.761162+00:00
---

# Content Classification Tutorial  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/classify-text-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback 

#  Content Classification Tutorial Stay organized with collections  Save and categorize content based on your preferences. 

## Audience

This tutorial is designed to let you quickly start exploring and developing applications with the Cloud Natural Language API. It is designed for people familiar with basic programming, though even without much programming knowledge, you should be able to follow along. Having walked through this tutorial, you should be able to use the [Reference documentation](https://docs.cloud.google.com/natural-language/docs/reference/rest) to create your own basic applications.

This tutorial steps through a Natural Language application using Python code. The purpose here is not to explain the Python client libraries, but to explain how to make calls to the Natural Language API. Applications in Java and Node.js are essentially similar. Consult the Natural Language API [Samples](https://docs.cloud.google.com/natural-language/docs/sample-apps) for samples in other languages (including the sample in this tutorial).

## Prerequisites

This tutorial has several prerequisites:

  * You've [set up a Cloud Natural Language project](https://docs.cloud.google.com/natural-language/docs/getting-started#set_up_a_project) in the Google Cloud console.
  * You've set up your environment using [Application Default Credentials](https://docs.cloud.google.com/natural-language/docs/common/auth#adc) in the Google Cloud console.
  * You are familiar with [Python](https://www.python.org/) in the Google Cloud console programming.
  * You have set up your Python development environment. It is recommended that you have the latest version of Python, `pip`, and `virtualenv` installed on your system. For instructions, see the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup) for Google Cloud Platform.
  * You've installed the [Google Cloud Client Library for Python](https://docs.cloud.google.com/natural-language/docs/reference/libraries)



## Overview

This tutorial walks you through a basic Natural Language application, using `classifyText` requests, which classifies content into categories along with a confidence score, such as:
    
    
    category: "/Internet & Telecom/Mobile & Wireless/Mobile Apps & Add-Ons"
    confidence: 0.6499999761581421
    

To see the list of all available category labels, see [Categories](https://docs.cloud.google.com/natural-language/docs/categories).

In this tutorial, you will create an application to perform the following tasks:

  * Classify multiple text files and write the result to an index file.
  * Process input query text to find similar text files.
  * Process input query category labels to find similar text files.



The tutorial uses content from Wikipedia. You could create a similar application to process news articles, online comments, and so on.

## Source Files

You can find the tutorial source code in the [Python Client Library Samples](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/language/snippets/classify_text) on GitHub.

This tutorial uses sample source text from Wikipedia. You can find the sample text files in the [resources/texts](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/language/snippets/classify_text/resources/texts) folder of the GitHub project.

## Importing libraries

To use the Cloud Natural Language API, you must to import the `language` module from the `google-cloud-language` library. The `language.types` module contains classes that are required for creating requests. The `language.enums` module is used to specify the type of the input text. This tutorial classifies plain text content (`language.enums.Document.Type.PLAIN_TEXT`).

To calculate the similarity between text based on their resulting content classification, this tutorial uses `numpy` for vector calculations.

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    import json
    import os
    
    from google.cloud import language_v1
    import numpy
    

## Step 1. Classify content

You can use the Python client library to make a request to the Natural Language API to classify content. The Python client library encapsulates the details for requests to and responses from the Natural Language API.

The `classify` function in the tutorial calls the Natural Language API `classifyText` method, by first creating an instance of the `LanguageServiceClient` class, and then calling the `classify_text` method of the `LanguageServiceClient` instance.

The tutorial `classify` function only classifies text content for this example. You can also classify the content of a web page by passing in the source HTML of the web page as the `text` and by setting the `type` parameter to `language.enums.Document.Type.HTML`.

For more information, see [Classifying Content](https://docs.cloud.google.com/natural-language/docs/classifying-text). For details about the structure of requests to the Natural Language API, see the [Natural Language Reference](https://docs.cloud.google.com/natural-language/docs/reference/rest).

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def classify(text, verbose=True):
        """Classify the input text into categories."""
    
        language_client = language_v1.LanguageServiceClient()
    
        document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        response = language_client.classify_text(request={"document": document})
        categories = response.categories
    
        result = {}
    
        for category in categories:
            # Turn the categories into a dictionary of the form:
            # {category.name: category.confidence}, so that they can
            # be treated as a sparse vector.
            result[category.name] = category.confidence
    
        if verbose:
            print(text)
            for category in categories:
                print("=" * 20)
                print("{:<16}: {}".format("category", category.name))
                print("{:<16}: {}".format("confidence", category.confidence))
    
        return result
    
    

The returned result is a dictionary with the category labels as keys, and confidence scores as values, such as:
    
    
    {
        "/Computers & Electronics": 0.800000011920929,
        "/Internet & Telecom/Mobile & Wireless/Mobile Apps & Add-Ons": 0.6499999761581421
    }
    

The tutorial Python script is organized so that it can be run from the command line for quick experiments. For example you can run:
    
    
    python classify_text_tutorial.py classify "Google Home enables users to speak voice commands to interact with services through the Home's intelligent personal assistant called Google Assistant. A large number of services, both in-house and third-party, are integrated, allowing users to listen to music, look at videos or photos, or receive news updates entirely by voice. "

**Note:** The content to be classified must have at least 20 tokens (words) in order for the Natural Language API to return a response.

## Step 2. Index multiple text files

The `index` function in the tutorial script takes, as input, a directory containing multiple text files, and the path to a file where it stores the indexed output (the default file name is `index.json`). The `index` function reads the content of each text file in the input directory, and then passes the text files to the Cloud Natural Language API to be classified into content categories.

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def index(path, index_file):
        """Classify each text file in a directory and write
        the results to the index_file.
        """
    
        result = {}
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
    
            if not os.path.isfile(file_path):
                continue
    
            try:
                with open(file_path) as f:
                    text = f.read()
                    categories = classify(text, verbose=False)
    
                    result[filename] = categories
            except Exception:
                print(f"Failed to process {file_path}")
    
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(result, ensure_ascii=False))
    
        print(f"Texts indexed in file: {index_file}")
        return result
    
    

The results from the Cloud Natural Language API for each file are organized into a single dictionary, serialized as a JSON string, and then written to a file. For example:
    
    
    {
        "android.txt": {
            "/Computers & Electronics": 0.800000011920929,
            "/Internet & Telecom/Mobile & Wireless/Mobile Apps & Add-Ons": 0.6499999761581421
        },
        "google.txt": {
            "/Internet & Telecom": 0.5799999833106995,
            "/Business & Industrial": 0.5400000214576721
        }
    }
    

To index text files from the command line with the default output filename `index.json`, run the following command:
    
    
    python classify_text_tutorial.py index resources/texts

## Step 3. Query the index

### Query with category labels

Once the index file (default file name = `index.json`) has been created, we can make queries to the index to retrieve some of the filenames and their confidence scores.

One way to do this is to use a category label as the query, which the tutorial accomplishes with the `query_category` function. The implementation of the helper functions, such as `similarity`, can be found in the `classify_text_tutorial.py` file. In your applications the similarity scoring and ranking should be carefully designed around specific use cases.

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def query_category(index_file, category_string, n_top=3):
        """Find the indexed files that are the most similar to
        the query label.
    
        The list of all available labels:
        https://cloud.google.com/natural-language/docs/categories
        """
    
        with open(index_file) as f:
            index = json.load(f)
    
        # Make the category_string into a dictionary so that it is
        # of the same format as what we get by calling classify.
        query_categories = {category_string: 1.0}
    
        similarities = []
        for filename, categories in index.items():
            similarities.append((filename, similarity(query_categories, categories)))
    
        similarities = sorted(similarities, key=lambda p: p[1], reverse=True)
    
        print("=" * 20)
        print(f"Query: {category_string}\n")
        print(f"\nMost similar {n_top} indexed texts:")
        for filename, sim in similarities[:n_top]:
            print(f"\tFilename: {filename}")
            print(f"\tSimilarity: {sim}")
            print("\n")
    
        return similarities
    
    

For a list of all of the available categories, see [Categories](https://docs.cloud.google.com/natural-language/docs/categories).

As before, you can call the `query_category` function from the command line:
    
    
    python classify_text_tutorial.py query-category index.json "/Internet & Telecom/Mobile & Wireless"

You should see output similar to the following:
    
    
    Query: /Internet & Telecom/Mobile & Wireless
    
    
    Most similar 3 indexed texts:
      Filename: android.txt
      Similarity: 0.665573579045
    
    
      Filename: google.txt
      Similarity: 0.517527175966
    
    
      Filename: gcp.txt
      Similarity: 0.5
    
    

### Query with text

Alternatively, you can query with text that may not be part of the indexed text. The tutorial `query` function is similar to the `query_category` function, with the added step of making a `classifyText` request for the text input, and using the results to query the index file.

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def query(index_file, text, n_top=3):
        """Find the indexed files that are the most similar to
        the query text.
        """
    
        with open(index_file) as f:
            index = json.load(f)
    
        # Get the categories of the query text.
        query_categories = classify(text, verbose=False)
    
        similarities = []
        for filename, categories in index.items():
            similarities.append((filename, similarity(query_categories, categories)))
    
        similarities = sorted(similarities, key=lambda p: p[1], reverse=True)
    
        print("=" * 20)
        print(f"Query: {text}\n")
        for category, confidence in query_categories.items():
            print(f"\tCategory: {category}, confidence: {confidence}")
        print(f"\nMost similar {n_top} indexed texts:")
        for filename, sim in similarities[:n_top]:
            print(f"\tFilename: {filename}")
            print(f"\tSimilarity: {sim}")
            print("\n")
    
        return similarities
    
    

To do this from the command line, run:
    
    
    python classify_text_tutorial.py query index.json "Google Home enables users to speak voice commands to interact with services through the Home's intelligent personal assistant called Google Assistant. A large number of services, both in-house and third-party, are integrated, allowing users to listen to music, look at videos or photos, or receive news updates entirely by voice. "

This prints something similar to the following:
    
    
    Query: Google Home enables users to speak voice commands to interact with services through the Home's intelligent personal assistant called Google Assistant. A large number of services, both in-house and third-party, are integrated, allowing users to listen to music, look at videos or photos, or receive news updates entirely by voice.
    
      Category: /Internet & Telecom, confidence: 0.509999990463
      Category: /Computers & Electronics/Software, confidence: 0.550000011921
    
    Most similar 3 indexed texts:
      Filename: android.txt
      Similarity: 0.600579500049
    
    
      Filename: google.txt
      Similarity: 0.401314790229
    
    
      Filename: gcp.txt
      Similarity: 0.38772339779
    

## What's next

With the content classification API you can create other applications. For example:

  * Classify every paragraph in an article to see the transition between topics.

  * Classify timestamped content and analyze the trend of topics over time.

  * Compare content categories with content sentiment using the `analyzeSentiment` method.

  * Compare content categories with entities mentioned in the text.




Additionally, other Google Cloud Platform products can be used to streamline your workflow:

  * In the sample application for this tutorial, we processed local text files, but you can modify the code to process text files stored in a Google Cloud Storage bucket by passing a Google Cloud Storage URI to the `classify_text` method.

  * In the sample application for this tutorial, we stored the index file locally, and each query is processed by reading through the whole index file. This means high latency if you have a large amount of indexed data or if you need to process numerous queries. [Datastore](https://docs.cloud.google.com/datastore/docs) is a natural and convenient choice for storing the index data.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
