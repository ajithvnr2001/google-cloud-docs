---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-text-tutorial-query-category/
title: Query label \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:17.110566+00:00
---

# Query label  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-text-tutorial-query-category/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Query label Stay organized with collections  Save and categorize content based on your preferences. 

Find the indexed files that are the most similar to the query label.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Content Classification Tutorial](https://docs.cloud.google.com/natural-language/docs/classify-text-tutorial)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudnaturallanguageapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
