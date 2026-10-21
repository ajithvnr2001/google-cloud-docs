---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-bigquery-pagetoken/
title: Paginate a BigQuery result set \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:45.381247+00:00
---

# Paginate a BigQuery result set  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-bigquery-pagetoken/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Paginate a BigQuery result set Stay organized with collections  Save and categorize content based on your preferences. 

Uses a page token to paginate a BigQuery result set and loop through a page of results at a time.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Paginate a BigQuery result set](https://docs.cloud.google.com/workflows/docs/paginate-bigquery-results)



## Code sample

### YAML
    
    
    # Use a page token to loop through a page of results at a time when
    # querying a BigQuery dataset larger than the Workflows memory limit
    # This workflow queries a public dataset to determine the most common
    # names in the US between 1910 and 2013
    main:
      params: [input]
      steps:
        - init:
            assign:
              - pageToken: null
        - startQuery:
            call: googleapis.bigquery.v2.jobs.insert
            args:
              projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              body:
                configuration:
                  query:
                    useLegacySql: false
                    # Remove LIMIT from the query to iterate through all results
                    query: SELECT name, SUM(number) AS total FROM `bigquery-public-data.usa_names.usa_1910_2013` GROUP BY name ORDER BY total DESC LIMIT 50
            result: query
        - getPage:
            call: googleapis.bigquery.v2.jobs.getQueryResults
            args:
              projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              jobId: ${query.jobReference.jobId}
              maxResults: 10
              pageToken: ${pageToken}
            result: page
        - processPage:
            for:
              value: row
              in: ${page.rows}
              steps:
                - processRow:
                    call: sys.log
                    args:
                      data: ${row}
        - checkIfDone:
            switch:
              - condition: ${"pageToken" in page and page.pageToken != ""}
                assign:
                  - pageToken: ${page.pageToken}
                next: getPage

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
