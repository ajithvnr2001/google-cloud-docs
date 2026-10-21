---
url: https://docs.cloud.google.com/workflows/docs/paginate-bigquery-results/
title: Paginate a BigQuery result set \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:10.405115+00:00
---

# Paginate a BigQuery result set  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/paginate-bigquery-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Paginate a BigQuery result set Stay organized with collections  Save and categorize content based on your preferences. 

If you're trying to retrieve the results of a query to a BigQuery dataset that is larger than the Workflows memory limit, you can use a page token to paginate through the results. The page token represents the position in the result set, and is returned when additional results are available. This method lets you loop through a page of results at a time.

BigQuery hosts a number of [public datasets](https://docs.cloud.google.com/bigquery/public-data) that are available to the general public to query. In the following example, you query the [USA Name Data public dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=usa_names&page=dataset) to determine the most common names in the US between 1910 and 2013.

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

### JSON
    
    
    {
      "main": {
        "params": [
          "input"
        ],
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "pageToken": null
                }
              ]
            }
          },
          {
            "startQuery": {
              "call": "googleapis.bigquery.v2.jobs.insert",
              "args": {
                "projectId": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}",
                "body": {
                  "configuration": {
                    "query": {
                      "useLegacySql": false,
                      "query": "SELECT name, SUM(number) AS total FROM `bigquery-public-data.usa_names.usa_1910_2013` GROUP BY name ORDER BY total DESC LIMIT 50"
                    }
                  }
                }
              },
              "result": "query"
            }
          },
          {
            "getPage": {
              "call": "googleapis.bigquery.v2.jobs.getQueryResults",
              "args": {
                "projectId": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}",
                "jobId": "${query.jobReference.jobId}",
                "maxResults": 10,
                "pageToken": "${pageToken}"
              },
              "result": "page"
            }
          },
          {
            "processPage": {
              "for": {
                "value": "row",
                "in": "${page.rows}",
                "steps": [
                  {
                    "processRow": {
                      "call": "sys.log",
                      "args": {
                        "data": "${row}"
                      }
                    }
                  }
                ]
              }
            }
          },
          {
            "checkIfDone": {
              "switch": [
                {
                  "condition": "${\"pageToken\" in page and page.pageToken != \"\"}",
                  "assign": [
                    {
                      "pageToken": "${page.pageToken}"
                    }
                  ],
                  "next": "getPage"
                }
              ]
            }
          }
        ]
      }
    }

## What's next

  * [BigQuery API connector overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/Overview)
  * [Poll for BigQuery job completion](https://docs.cloud.google.com/workflows/docs/poll-bigquery-job)
  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
