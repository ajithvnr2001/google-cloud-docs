---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-iteration/
title: Perform parallel iteration using for loops \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:34.376783+00:00
---

# Perform parallel iteration using for loops  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-iteration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Perform parallel iteration using for loops Stay organized with collections  Save and categorize content based on your preferences. 

Executes loop iterations in parallel to reduce the end-to-end execution time. A shared variable is updated in each iteration.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)



## Code sample

### YAML
    
    
    main:
      params: [args]
      steps:
        - init:
            assign:
              - total: 0
        - countComments:
            parallel:
              shared: [total]    # allows child branch to write to this variable
              for:
                value: postId
                in: ${args.posts}
                steps:
                  - getPostCommentCount:
                      call: http.get
                      args:
                        url: ${"https://example.com/postComments/" + postId}
                      result: numComments
                  - add:
                      assign:
                        - total: ${total + numComments}
        - done:
            return: ${total}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
