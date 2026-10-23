---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-for-in-http/
title: Make HTTP requests in a for-in loop \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:32.051630+00:00
---

# Make HTTP requests in a for-in loop  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-for-in-http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Make HTTP requests in a for-in loop Stay organized with collections  Save and categorize content based on your preferences. 

Makes HTTP requests in a for-in loop.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)



## Code sample

### YAML
    
    
    - getUserIDs:
        call: http.get
        args:
          url: https://example.com/getUserIDs
        result: userIds
    - saveUserInfo:
        for:
          value: uid
          in: ${userIds}
          steps:
            - tryStep:
                try:
                  steps:
                    - get:
                        call: http.get
                        args:
                          url: ${"https://example.com/getUserInfo?userId=" + string(uid)}
                        result: userInfo
                    - post:
                        call: http.post
                        args:
                          url: ${"https://example.com/saveUserInfo?userId=" + string(uid)}
                          body: ${userInfo}
                except:
                  as: e
                  steps:
                    - knownErrors:
                        switch:
                          - condition: ${not("HttpError" in e.tags)}
                            return: '${"Connection problem with userID: " + string(uid)}'
                    - unhandledErrors:
                        raise: ${e}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
