---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-http-get/
title: Make an external HTTP GET request with headers \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:54.001136+00:00
---

# Make an external HTTP GET request with headers  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-http-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Make an external HTTP GET request with headers Stay organized with collections  Save and categorize content based on your preferences. 

Makes an HTTP GET request with a custom header.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests)



## Code sample

### YAML
    
    
    - get_message:
        call: http.get
        args:
          url: https://www.example.com/endpoint
          headers:
            Content-Type: "text/plain"
          query:
            some_val: "Hello World"
            another_val: 123
        result: the_message
    - return_value:
        return: ${the_message.body}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
