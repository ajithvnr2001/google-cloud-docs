---
url: https://docs.cloud.google.com/workflows/docs/execute-parallel-steps/
title: Execute workflow steps in parallel \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:12.219317+00:00
---

# Execute workflow steps in parallel  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/execute-parallel-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Execute workflow steps in parallel Stay organized with collections  Save and categorize content based on your preferences. 

Parallel steps can reduce the total execution time for a workflow by performing multiple [blocking calls](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions#blocking-calls) at the same time.

Blocking calls such as [sleep](https://docs.cloud.google.com/workflows/docs/sleeping), [HTTP calls](https://docs.cloud.google.com/workflows/docs/http-requests), and [callbacks](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) can take time, from milliseconds to days. Parallel steps are intended to assist with such concurrent long-running operations. If a workflow must perform multiple blocking calls that are independent of each other, using parallel branches can reduce the total execution time by starting the calls at the same time, and waiting for all of them to complete.

For example, if your workflow must retrieve customer data from several independent systems before continuing, parallel branches allow for concurrent API requests. If there are five systems and each takes two seconds to respond, performing the steps sequentially in a workflow could take at least 10 seconds; performing them in parallel could take as little as two.

**Note:** Parallel branches provide no performance advantages for non-blocking steps, such as assignments, conditions, or non-blocking calls. Due to system overhead, using parallel branches that do not include blocking calls can increase the total execution time.

## Create a parallel step

Create a `parallel` step to define a part of your workflow where two or more steps can execute concurrently.

### YAML
    
    
      - PARALLEL_STEP_NAME:
          parallel:
            exception_policy: POLICY
            shared: [VARIABLE_A, VARIABLE_B, ...]
            concurrency_limit: CONCURRENCY_LIMIT
            BRANCHES_OR_FOR:
              ...

### JSON
    
    
      [
        {
          "PARALLEL_STEP_NAME": {
            "parallel": {
              "exception_policy": "POLICY",
              "shared": [
                "VARIABLE_A",
                "VARIABLE_B",
                ...
              ],
              "concurrency_limit": "CONCURRENCY_LIMIT",
              "BRANCHES_OR_FOR":
              ...
            }
          }
        }
      ]

Replace the following:

  * `PARALLEL_STEP_NAME`: the name of the parallel step.
  * `POLICY` (optional): determines the action other branches will take when an unhandled exception occurs. The default policy, `continueAll`, results in no further action, and all other branches will attempt to run. Note that `continueAll` is the only policy currently supported.
  * `VARIABLE_A`, `VARIABLE_B`, and so on: a list of writable variables with parent scope that allow assignments within the parallel step. For more information, see [Shared variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#variables).
  * `CONCURRENCY_LIMIT` (optional): the maximum number of branches and iterations that can concurrently execute within a single workflow execution before further branches and iterations are queued to wait. This applies to a single `parallel` step only and does not cascade. Must be a positive integer and can be either a literal value or an expression. For details, see [Concurrency limits](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel/parallel-steps#concurrency).
  * `BRANCHES_OR_FOR`: use either `branches` or `for` to indicate one of the following: 
    * Branches that can run concurrently.
    * A loop where iterations can run concurrently.



Note the following:

  * Parallel branches and iterations can run in any order, and might run in a different order with each execution.
  * Parallel steps can include other, nested parallel steps up to the depth limit. See [Quotas and limits](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel/quotas).
  * For more details, see the syntax reference page for [parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel/parallel-steps).

**Tip:** Cloud Run functions (2nd gen) can [ take advantage of concurrency](https://docs.cloud.google.com/functions/docs/2nd-gen/overview#enhanced_infrastructure) through the underlying Cloud Run service, and give you more control over pricing. When calling Cloud Run functions in a parallel `for` step, you can save costs by setting the concurrency so that multiple items are processed by the same Cloud Run function instance. Learn more about [configuring concurrency in Cloud Run](https://docs.cloud.google.com/run/docs/about-concurrency). 

## Replace experimental function with parallel step

If you are using `experimental.executions.map` to support parallel work, you can migrate your workflow to use parallel steps instead, executing ordinary `for` loops in parallel. For examples, see [Replace experimental function with parallel step](https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel).

## Samples

These samples demonstrate the syntax.

### Perform operations in parallel (using branches)

If your workflow has multiple and different sets of steps that can be executed at the same time, placing them in parallel branches can decrease the total time needed to complete those steps.

In the following example, a user ID is passed as an argument to the workflow and data is retrieved in parallel from two different services. [Shared variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#variables) allow values to be written to in the branches, and read after the branches complete:

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
                  "userProfile": {}
                },
                {
                  "recentItems": []
                }
              ]
            }
          },
          {
            "enrichUserData": {
              "parallel": {
                "shared": [
                  "userProfile",
                  "recentItems"
                ],
                "branches": [
                  {
                    "getUserProfileBranch": {
                      "steps": [
                        {
                          "getUserProfile": {
                            "call": "http.get",
                            "args": {
                              "url": "${\"https://example.com/users/\" + input.userId}"
                            },
                            "result": "userProfile"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "getRecentItemsBranch": {
                      "steps": [
                        {
                          "getRecentItems": {
                            "try": {
                              "call": "http.get",
                              "args": {
                                "url": "${\"https://example.com/items?userId=\" + input.userId}"
                              },
                              "result": "recentItems"
                            },
                            "except": {
                              "as": "e",
                              "steps": [
                                {
                                  "ignoreError": {
                                    "assign": [
                                      {
                                        "recentItems": []
                                      }
                                    ]
                                  }
                                }
                              ]
                            }
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }

### Process items in parallel (using a parallel loop)

If you need to perform the same action for each item in a list, you can complete the execution more quickly by using a parallel loop. A parallel loop allows multiple loop iterations to be performed in parallel. Note that, unlike regular [for loops](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration), iterations can be performed in any order.

In the following example, a set of user notifications are processed in a parallel `for` loop:

### YAML
    
    
    main:
      params: [input]
      steps:
        - sendNotifications:
            parallel:
              for:
                value: notification
                in: ${input.notifications}
                steps:
                  - notify:
                      call: http.post
                      args:
                        url: https://example.com/sendNotification
                        body:
                          notification: ${notification}

### JSON
    
    
    {
      "main": {
        "params": [
          "input"
        ],
        "steps": [
          {
            "sendNotifications": {
              "parallel": {
                "for": {
                  "value": "notification",
                  "in": "${input.notifications}",
                  "steps": [
                    {
                      "notify": {
                        "call": "http.post",
                        "args": {
                          "url": "https://example.com/sendNotification",
                          "body": {
                            "notification": "${notification}"
                          }
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    }

### Aggregate data (using a parallel loop)

You can process a set of items while collecting data from the operations performed on each item. For example, you might want to track the IDs of created items, or maintain a list of items with errors.

In the following example, 10 separate queries to a public BigQuery dataset each return the number of words in a document, or set of documents. A [shared variable](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#variables) allows the count of the words to accumulate and be read after all the iterations complete. After calculating the number of words across all the documents, the workflow returns the total.

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
                  "numWords": 0
                },
                {
                  "corpuses": [
                    "sonnets",
                    "various",
                    "1kinghenryvi",
                    "2kinghenryvi",
                    "3kinghenryvi",
                    "comedyoferrors",
                    "kingrichardiii",
                    "titusandronicus",
                    "tamingoftheshrew",
                    "loveslabourslost"
                  ]
                }
              ]
            }
          },
          {
            "runQueries": {
              "parallel": {
                "shared": [
                  "numWords"
                ],
                "for": {
                  "value": "corpus",
                  "in": "${corpuses}",
                  "steps": [
                    {
                      "runQuery": {
                        "call": "googleapis.bigquery.v2.jobs.query",
                        "args": {
                          "projectId": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}",
                          "body": {
                            "useLegacySql": false,
                            "query": "${\"SELECT COUNT(DISTINCT word) FROM `bigquery-public-data.samples.shakespeare` \" + \" WHERE corpus='\" + corpus + \"' \"}"
                          }
                        },
                        "result": "query"
                      }
                    },
                    {
                      "add": {
                        "assign": [
                          {
                            "numWords": "${numWords + int(query.rows[0].f[0].v)}"
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          },
          {
            "done": {
              "return": "${numWords}"
            }
          }
        ]
      }
    }

## What's next

  * [Syntax reference: Parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
  * [Tutorial: Run a workflow that executes other workflows in parallel](https://docs.cloud.google.com/workflows/docs/tutorials/execute-workflows-from-workflow)
  * [Tutorial: Run multiple BigQuery jobs in parallel](https://docs.cloud.google.com/workflows/docs/tutorials/bigquery-parallel-jobs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
