---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-bigquery/
title: Run multiple BigQuery query jobs in parallel \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:40.480941+00:00
---

# Run multiple BigQuery query jobs in parallel  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Run multiple BigQuery query jobs in parallel Stay organized with collections  Save and categorize content based on your preferences. 

Runs multiple BigQuery query jobs in parallel, demonstrating an improvement in performance when compared to running the jobs serially, one after the other.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Run multiple BigQuery jobs in parallel](https://docs.cloud.google.com/workflows/docs/tutorials/bigquery-parallel-jobs)



## Code sample

### YAML
    
    
    main:
        steps:
        - init:
            assign:
                - results : {} # result from each iteration keyed by table name
                - tables:
                    - 201201h
                    - 201202h
                    - 201203h
                    - 201204h
                    - 201205h
        - runQueries:
            parallel:
                shared: [results]
                for:
                    value: table
                    in: ${tables}
                    steps:
                    - logTable:
                        call: sys.log
                        args:
                            text: ${"Running query for table " + table}
                    - runQuery:
                        call: googleapis.bigquery.v2.jobs.query
                        args:
                            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                            body:
                                useLegacySql: false
                                useQueryCache: false
                                timeoutMs: 30000
                                # Find top 100 titles with most views on Wikipedia
                                query: ${
                                    "SELECT TITLE, SUM(views)
                                    FROM `bigquery-samples.wikipedia_pageviews." + table + "`
                                    WHERE LENGTH(TITLE) > 10
                                    GROUP BY TITLE
                                    ORDER BY SUM(VIEWS) DESC
                                    LIMIT 100"
                                    }
                        result: queryResult
                    - returnResult:
                        assign:
                            # Return the top title from each table
                            - results[table]: {}
                            - results[table].title: ${queryResult.rows[0].f[0].v}
                            - results[table].views: ${queryResult.rows[0].f[1].v}
        - returnResults:
            return: ${results}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
