---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-for-range-http/
title: Use a for-range loop to make HTTP requests \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:47.657176+00:00
---

# Use a for-range loop to make HTTP requests  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-for-range-http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Use a for-range loop to make HTTP requests Stay organized with collections  Save and categorize content based on your preferences. 

Uses range-based iteration to make HTTP requests.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)



## Code sample

### YAML
    
    
    - init:
        assign:
          - minTemp: -14.5
          - maxTemp: 42.8
    - storeNormalBodyTemp:
        for:
          value: temp
          range: ${[minTemp, maxTemp]}
          steps:
            - checkTemp:
                call: http.get
                args:
                  url: ${"https://example.com/isBodyTempNormal?temp=" + string(temp)}
                result: isNormal
            - storeOrBreak:
                switch:
                  - condition: ${isNormal}
                    next: storeTemp
                next: break
            - storeTemp:
                call: http.post
                args:
                  url: ${"https://example.com/storeTemp?temp=" + string(temp)}
                  body: ${temp}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
