---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-text-tutorial-index/
title: Classify text files and write to the index file \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:01.347934+00:00
---

# Classify text files and write to the index file  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-text-tutorial-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Classify text files and write to the index file Stay organized with collections  Save and categorize content based on your preferences. 

Classify each text file in a directory and write the results to the index file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Content Classification Tutorial](https://docs.cloud.google.com/natural-language/docs/classify-text-tutorial)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudnaturallanguageapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
