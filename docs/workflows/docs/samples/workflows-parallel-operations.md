---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-operations/
title: Perform operations in parallel using branches \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:40.427020+00:00
---

# Perform operations in parallel using branches  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Perform operations in parallel using branches Stay organized with collections  Save and categorize content based on your preferences. 

Executes a workflow that has multiple and different sets of steps at the same time by placing them in parallel branches.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps)



## Code sample

### YAML
    
    
    main:
      params: [input]
      steps:
        - init:
            assign:
              - userProfile: {}
              - recentItems: []
        - enrichUserData:
            parallel:
              shared: [userProfile, recentItems]  # userProfile and recentItems are shared to make them writable in the branches
              branches:
                - getUserProfileBranch:
                    steps:
                      - getUserProfile:
                          call: http.get
                          args:
                            url: '${"https://example.com/users/" + input.userId}'
                          result: userProfile
                - getRecentItemsBranch:
                    steps:
                      - getRecentItems:
                          try:
                            call: http.get
                            args:
                              url: '${"https://example.com/items?userId=" + input.userId}'
                            result: recentItems
                          except:
                            as: e
                            steps:
                              - ignoreError:
                                  assign:  # continue with an empty list if this call fails
                                    - recentItems: []

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
