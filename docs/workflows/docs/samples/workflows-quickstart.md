---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-quickstart/
title: Input a search term and pass it to an API \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:11.591633+00:00
---

# Input a search term and pass it to an API  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Input a search term and pass it to an API Stay organized with collections  Save and categorize content based on your preferences. 

Uses your Google Cloud location to construct a search term or you can input your own search term to pass to the Wikipedia API. A list of related Wikipedia articles is returned.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Calls](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
  * [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests)
  * [Quickstart: Create a workflow by using the gcloud CLI](https://docs.cloud.google.com/workflows/docs/create-workflow-gcloud)
  * [Quickstart: Create a workflow by using the Google Cloud console](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



## Code sample

### YAML
    
    
    main:
      params: [input]
      steps:
        - checkSearchTermInInput:
            switch:
              - condition: '${"searchTerm" in input}'
                assign:
                  - searchTerm: '${input.searchTerm}'
                next: readWikipedia
        - getLocation:
            call: sys.get_env
            args:
              name: GOOGLE_CLOUD_LOCATION
            result: location
        - setFromCallResult:
            assign:
              - searchTerm: '${text.split(location, "-")[0]}'
        - readWikipedia:
            call: http.get
            args:
              url: 'https://en.wikipedia.org/w/api.php'
              query:
                action: opensearch
                search: '${searchTerm}'
            result: wikiResult
        - returnOutput:
            return: '${wikiResult.body[1]}'

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
