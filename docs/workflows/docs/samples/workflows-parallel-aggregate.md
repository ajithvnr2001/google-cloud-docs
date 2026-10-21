---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-aggregate/
title: Aggregate data using a parallel loop \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:15.626068+00:00
---

# Aggregate data using a parallel loop  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-aggregate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Aggregate data using a parallel loop Stay organized with collections  Save and categorize content based on your preferences. 

Separate queries to a public BigQuery dataset each return the number of words in a document, or set of documents. A shared variable allows the count of the words to accumulate and be read after all the iterations complete.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps)



## Code sample

### YAML
    
    
    # Use a parallel loop to make ten queries to a public BigQuery dataset and
    # use a shared variable to accumulate a count of words; after all iterations
    # complete, return the total number of words across all documents
    main:
      params: [input]
      steps:
        - init:
            assign:
              - numWords: 0
              - corpuses:
                  - sonnets
                  - various
                  - 1kinghenryvi
                  - 2kinghenryvi
                  - 3kinghenryvi
                  - comedyoferrors
                  - kingrichardiii
                  - titusandronicus
                  - tamingoftheshrew
                  - loveslabourslost
        - runQueries:
            parallel:  # 'numWords' is shared so it can be written within the parallel loop
              shared: [numWords]
              for:
                value: corpus
                in: ${corpuses}
                steps:
                  - runQuery:
                      call: googleapis.bigquery.v2.jobs.query
                      args:
                        projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                        body:
                          useLegacySql: false
                          query: ${"SELECT COUNT(DISTINCT word) FROM `bigquery-public-data.samples.shakespeare` " + " WHERE corpus='" + corpus + "' "}
                      result: query
                  - add:
                      assign:
                        - numWords: ${numWords + int(query.rows[0].f[0].v)}  # first result is the count
        - done:
            return: ${numWords}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
