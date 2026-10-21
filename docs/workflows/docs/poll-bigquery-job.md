---
url: https://docs.cloud.google.com/workflows/docs/poll-bigquery-job/
title: Poll for BigQuery job completion \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:10.025015+00:00
---

# Poll for BigQuery job completion  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/poll-bigquery-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Poll for BigQuery job completion Stay organized with collections  Save and categorize content based on your preferences. 

When initiating a BigQuery job using the [BigQuery connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/Overview), your workflow might not automatically wait for the job's completion. If subsequent steps depend on the job's success, you should implement a polling mechanism.

Many Workflows connectors return a [long-running operation](https://docs.cloud.google.com/workflows/docs/connectors#lro) (LRO) resource that can be polled. While some connectors return a resource of type `Operation` to represent an LRO, BigQuery uses a [`Job`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/Overview#job) resource for this purpose. Other services, such as Cloud Build or Compute Engine, return an actual `Operation` resource. For a list of the LRO resource types, see [Supported connectors](https://docs.cloud.google.com/workflows/docs/reference/googleapis#list_of_supported_connectors).

**Note:** When connectors poll LRO resources, each polling attempt counts as a [billable step](https://docs.cloud.google.com/workflows/pricing).

## Automatic polling

You can automatically poll for the completion of a BigQuery job when using connector methods that return an LRO resource, such as [`googleapis.bigquery.v2.jobs.insert`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/insert).

When you use such a connector method, Workflows blocks the workflow execution until the operation succeeds or fails. The `connector_params` field lets you customize the polling behavior, including the total timeout and the frequency of status checks. For more information, see [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

For example, the following workflow demonstrates starting a BigQuery job using the `jobs.insert` method, and configuring the job's polling with a policy that uses custom settings rather than the default settings:

### YAML
    
    
    # This workflow demonstrates how to automatically poll for the completion of
    # a BigQuery job when using a connector method that return an LRO resource.
    main:
      steps:
        - init:
            assign:
              - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - query: "SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 10"
        - run_bigquery_job:
            call: googleapis.bigquery.v2.jobs.insert
            args:
              projectId: ${project_id}
              body:
                configuration:
                  query:
                    query: ${query}
                    useLegacySql: false
              connector_params:
                timeout: 3600  # Total time in seconds to wait for the job; default is 1800
                polling_policy:
                  initial_delay: 2.0  # Seconds to wait before the first poll; default is 1.0
                  multiplier: 1.5     # Factor by which to increase delay between polls; default is 1.25
                  max_delay: 60.0     # Maximum delay in seconds between polls; default is 60.0
            result: job_status
        - finish:
            return: ${job_status}

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "project_id": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
                },
                {
                  "query": "SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 10"
                }
              ]
            }
          },
          {
            "run_bigquery_job": {
              "call": "googleapis.bigquery.v2.jobs.insert",
              "args": {
                "projectId": "${project_id}",
                "body": {
                  "configuration": {
                    "query": {
                      "query": "${query}",
                      "useLegacySql": false
                    }
                  }
                },
                "connector_params": {
                  "timeout": 3600,
                  "polling_policy": {
                    "initial_delay": 2,
                    "multiplier": 1.5,
                    "max_delay": 60
                  }
                }
              },
              "result": "job_status"
            }
          },
          {
            "finish": {
              "return": "${job_status}"
            }
          }
        ]
      }
    }
    

## Manual polling

Automatic polling only applies to methods that return an LRO resource. Standard synchronous methods like [`googleapis.bigquery.v2.jobs.query`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/query) don't support automatic polling and might require [manual polling](https://docs.cloud.google.com/workflows/docs/sleeping#poll_for_data) if the query takes longer than the internal API timeout.

For example, the following workflow demonstrates how to poll for the completion of a BigQuery job directly within the workflow by using the [`getQueryResults` method](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/getQueryResults):

### YAML
    
    
    # This workflow demonstrates how to manually poll for the completion of
    # a BigQuery job by using the `getQueryResults` method.
    main:
      steps:
        - init:
            assign:
              - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
        - startQuery:
            call: googleapis.bigquery.v2.jobs.query
            args:
              projectId: ${project_id}
              body:
                useLegacySql: false
                query: "SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 10"
            result: queryResponse
        - getJobId:
            assign:
              - jobId: ${queryResponse.jobReference.jobId}
        - pollingLoop:
            steps:
              - checkStatus:
                  call: googleapis.bigquery.v2.jobs.getQueryResults
                  args:
                    projectId: ${project_id}
                    jobId: ${jobId}
                    timeoutMs: 10000  # Default wait time per call
                  result: jobStatus
              - checkIfDone:
                  switch:
                    - condition: ${jobStatus.jobComplete}
                      return: ${jobStatus}  # Job is finished
              - wait:
                  call: sys.sleep
                  args:
                    seconds: 5
                  next: checkStatus  # Repeat check

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "project_id": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
                }
              ]
            }
          },
          {
            "startQuery": {
              "call": "googleapis.bigquery.v2.jobs.query",
              "args": {
                "projectId": "${project_id}",
                "body": {
                  "useLegacySql": false,
                  "query": "SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 10"
                }
              },
              "result": "queryResponse"
            }
          },
          {
            "getJobId": {
              "assign": [
                {
                  "jobId": "${queryResponse.jobReference.jobId}"
                }
              ]
            }
          },
          {
            "pollingLoop": {
              "steps": [
                {
                  "checkStatus": {
                    "call": "googleapis.bigquery.v2.jobs.getQueryResults",
                    "args": {
                      "projectId": "${project_id}",
                      "jobId": "${jobId}",
                      "timeoutMs": 10000
                    },
                    "result": "jobStatus"
                  }
                },
                {
                  "checkIfDone": {
                    "switch": [
                      {
                        "condition": "${jobStatus.jobComplete}",
                        "return": "${jobStatus}"
                      }
                    ]
                  }
                },
                {
                  "wait": {
                    "call": "sys.sleep",
                    "args": {
                      "seconds": 5
                    },
                    "next": "checkStatus"
                  }
                }
              ]
            }
          }
        ]
      }
    }
    

## What's next

  * [BigQuery API connector overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/Overview)
  * [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis)
  * [Workflows syntax overview](https://docs.cloud.google.com/workflows/docs/reference/syntax)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
