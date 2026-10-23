---
url: https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints/
title: Wait using callbacks \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:14.430133+00:00
---

# Wait using callbacks  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Wait using callbacks Stay organized with collections  Save and categorize content based on your preferences. 

Callbacks allow workflow executions to wait for another service to make a request to the _callback endpoint_ ; that request resumes the execution of the workflow.

With callbacks, you can signal to your workflow that a specified event has occurred, and wait on that event without polling. For example, you can create a workflow that notifies you when a product is back in stock or when an item has shipped; or that waits to allow human interaction such as reviewing an order or validating a translation.

This page shows you how to create a workflow that supports a callback endpoint, and that waits for HTTP requests from external processes to arrive at that endpoint. You can also [wait for events using callbacks and Eventarc triggers](https://docs.cloud.google.com/workflows/docs/tutorials/create-wait-for-events-callbacks).

**Note:** Callback endpoints can only be waited on in the workflow execution in which they're created. For example, in any subsequent execution of the workflow, you can't receive callbacks from a prior execution.

Callbacks require the use of two standard library built-in functions:

  * `[events.create_callback_endpoint](https://docs.cloud.google.com/workflows/docs/reference/stdlib/events/create_callback_endpoint)`—Creates a callback endpoint expecting the specified HTTP method
  * `[events.await_callback](https://docs.cloud.google.com/workflows/docs/reference/stdlib/events/await_callback)`—Waits for a callback to be received at the given endpoint

**Important** : If your workflow uses callbacks and you last deployed it on or before January 11, 2022, you must redeploy it by July 4, 2022 to continue executing workflows without failures. 

## Create an endpoint that receives a callback request

Create a callback endpoint that can receive HTTP requests to arrive at that endpoint.

  1. Follow the steps to [create](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#creating_a_workflow) a new workflow, or choose an existing workflow to [update](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#updating_a_workflow) but don't deploy it yet.
  2. In the workflow's definition, add a step to create a callback endpoint: 

### YAML
         
         - create_callback:
                 call: events.create_callback_endpoint
                 args:
                     http_callback_method: "METHOD"
                 result: callback_details
             

### JSON
         
         [
               {
                 "create_callback": {
                   "call": "events.create_callback_endpoint",
                   "args": {
                     "http_callback_method": "METHOD"
                   },
                   "result": "callback_details"
                 }
               }
             ]
               

Replace `METHOD` with the expected HTTP method, one of `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `OPTIONS`, or `PATCH`. The default is `POST`.

The result is a map, `callback_details`, with a `url` field that stores the URL of the created endpoint.

The callback endpoint is now ready to receive incoming requests with the specified HTTP method. The URL of the created endpoint can be used to trigger the callback from a process external to the workflow; for example, by passing the URL to a Cloud Run function.

**Note:** You can have multiple callbacks in the same workflow. 
  3. In the workflow's definition, add a step to wait for a callback request: 

### YAML
         
         - await_callback:
                 call: events.await_callback
                 args:
                     callback: ${callback_details}
                     timeout: TIMEOUT
                 result: callback_request
             

### JSON
         
         [
               {
                 "await_callback": {
                   "call": "events.await_callback",
                   "args": {
                     "callback": "${callback_details}",
                     "timeout": TIMEOUT
                   },
                   "result": "callback_request"
                 }
               }
             ]
               

Replace `TIMEOUT` with the maximum number of seconds that the workflow should wait for a request. The default is 43200 (12 hours). If the time elapses before a request is received, a `TimeoutError` is raised. 

Note that there is a maximum execution duration. For more information, see the [request limit](https://docs.cloud.google.com/workflows/quotas#resource_limits). 

The `callback_details` map from the earlier `create_callback` step is passed as an argument.

**Note:** If multiple requests are sent to a callback endpoint before `await_callback` is called, only the first request is accepted and returned. Subsequent requests are rejected with a `RESOURCE_EXHAUSTED` HTTP status code. 
  4. Deploy your workflow to finish creating or updating it. 

When a request is received, all the details of the request are stored in the `callback_request` map. You then have access to the entire HTTP request, including its header, body, and a `query` map for any query parameters. For example:

### YAML
         
         http_request:
               body:
               headers: {...}
               method: GET
               query: {}
               url: "/v1/projects/350446661175/locations/us-central1/workflows/workflow-1/executions/46804f42-dc83-46d6-87e4-93962866ed81/callbacks/49c80102-74d2-49cd-a70e-805a9fded94f_2de9b413-6332-412d-99c3-d7e9b6eeeda2"
             received_time: 2021-06-24 12:49:16.988072651 -0700 PDT m=+742581.005780667
             type: HTTP
             

### JSON
         
         {
                "http_request":{
                   "body":null,
                   "headers":{
                      ...
                   },
                   "method":"GET",
                   "query":{
                   },
                   "url":"/v1/projects/350446661175/locations/us-central1/workflows/workflow-1/executions/46804f42-dc83-46d6-87e4-93962866ed81/callbacks/49c80102-74d2-49cd-a70e-805a9fded94f_2de9b413-6332-412d-99c3-d7e9b6eeeda2"
                },
                "received_time":"2021-06-24 12:49:16.988072651 -0700 PDT m=+742581.005780667",
                "type":"HTTP"
             }
               

If the HTTP body is text or JSON, Workflows will attempt to decode the body; otherwise, raw bytes are returned. 




## Authorize requests to the callback endpoint

To send a request to a callback endpoint, Google Cloud services such as Cloud Run and Cloud Run functions, as well as third-party services, must be authorized to do so by having the appropriate Identity and Access Management (IAM) permissions; specifically, `workflows.callbacks.send` (included in the [Workflows Invoker role](https://docs.cloud.google.com/workflows/docs/access-control#roles)).

**Note:** To learn more about granting roles to service accounts, see [granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Make a direct request

The simplest way to create short-lived credentials for a service account is to make a direct request. Two identities are involved in this flow: the caller, and the service account for whom the credential is created. The call to the basic workflow on this page is an example of a direct request. For more information, see [Use IAM to control access](https://docs.cloud.google.com/workflows/docs/use-iam-for-access) and [Direct request permissions](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-direct).

### Generate an OAuth 2.0 access token

To authorize an application to call the callback endpoint, you can generate an OAuth 2.0 access token for the service account associated with the workflow. Assuming that you have the required permissions (for the `Workflows Editor` or `Workflows Admin`, and `Service Account Token Creator` roles), you can also generate a token yourself by [running the `generateAccessToken` method](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth).

If the `generateAccessToken` request is successful, the returned response body contains an OAuth 2.0 access token and an expiration time. (By default, OAuth 2.0 access tokens are valid for a maximum of 1 hour.) For example: 
    
    
      {
      "accessToken": "eyJ0eXAi...NiJ9",
      "expireTime": "2020-04-07T15:01:23.045123456Z"
      }

The `accessToken` code can then be used in a curl call to the callback endpoint URL as in the following examples: 
    
    
      curl -X GET -H "Authorization: Bearer ACCESS_TOKEN_STRING" CALLBACK_URL
    
    
      curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN_STRING" -d '{"foo" : "bar"}' CALLBACK_URL

### Generate an OAuth token for a Cloud Run function

If you are invoking a callback from a Cloud Run function using the same service account as the workflow and in the same project, you can generate an OAuth access token in the function itself. For example:
    
    
    const {GoogleAuth} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    const auth = new [GoogleAuth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
    const token = await [auth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html).getAccessToken();
    
    try {
      const resp = await fetch(url, {
          method: 'POST',
          headers: {
              'accept': 'application/json',
              'content-type': 'application/json',
              'authorization': `Bearer ${token}`
          },
          body: JSON.stringify({ approved: Boolean(approved) })
      });
      console.log("Response = ", JSON.stringify(resp));
    
      const result = await resp.json();
      console.log("Outcome = ", JSON.stringify(result));

For more context, see the tutorial on [Creating a human-in-the-loop workflow using callbacks](https://docs.cloud.google.com/workflows/docs/tutorials/callbacks-firestore).

### Request offline access

Access tokens periodically expire and become invalid credentials for a related API request. You can refresh an access token without prompting the user for permission if you requested offline access to the scopes associated with the token. Requesting offline access is a requirement for any application that needs to access a Google API when the user is not present. For more information, see [Refreshing an access token (offline access)](https://developers.google.com/identity/protocols/oauth2/web-server#offline).

## Invoke a workflow exactly once using callbacks

Callbacks are fully _idempotent_ which means that you can [retry](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying) a callback if it fails without producing unexpected results or side effects.

After you create a callback endpoint, the URL is ready to receive incoming requests, and is usually returned to a caller before the corresponding call to `await_callback` is made. However, if the callback URL has yet to be received when the `await_callback` step is executed, the workflow execution is blocked until the endpoint is received (or a timeout occurs). Once received, the workflow execution resumes, and the callback is processed.

After you execute the `create_callback_endpoint` step and create a callback endpoint, a single callback slot is available to the workflow. When a callback request is received, this slot is filled with the callback payload until the callback can be processed. When the `await_callback` step is executed, the callback is processed, and the slot is emptied and made available for another callback. You can then reuse the callback endpoint and call `await_callback` again.

If `await_callback` is called only once but a second callback is received, one of the following scenarios occurs and an appropriate HTTP status code is returned:

  * HTTP `429: Too Many Requests` indicates that the first callback was received successfully but hasn't been processed; it remains waiting to be processed. The second callback is rejected by the workflow.

  * HTTP `200: Success` indicates that the first callback was received successfully and a response was returned. The second callback is stored and might never be processed unless `await_callback` is called a second time. If the workflow ends before that happens, the second callback request is never processed and is discarded.

  * HTTP `404: Page Not Found` indicates that the workflow is no longer running. Either the first callback was processed and the workflow has completed, or the workflow has failed. To determine this, you'll need to query the workflow execution state.




### Parallel callbacks

When steps are executed in parallel, and a callback is created by a parent thread and awaited on in child steps, the same pattern as previously described is followed.

In the following example, when the `create_callback_endpoint` step is executed, one callback slot is created. Each subsequent call to `await_callback` opens a new callback slot. Ten callbacks can be made concurrently, if all threads are running and waiting before a callback request is made. Additional callbacks could be made, but would be stored and never processed.

### YAML
    
    
      - createCallbackInParent:
        call: events.create_callback_endpoint
        args:
          http_callback_method: "POST"
        result: callback_details
      - parallelStep:
        parallel:
            for:
                range: [1, 10]
                value: loopValue
                steps:
                  - waitForCallbackInChild:
                      call: events.await_callback
                      args:
                          callback: ${callback_details}

### JSON
    
    
      [
        {
          "createCallbackInParent": {
            "call": "events.create_callback_endpoint",
            "args": {
              "http_callback_method": "POST"
            },
            "result": "callback_details"
          }
        },
        {
          "parallelStep": {
            "parallel": {
              "for": {
                "range": [
                  1,
                  10
                ],
                "value": "loopValue",
                "steps": [
                  {
                    "waitForCallbackInChild": {
                      "call": "events.await_callback",
                      "args": {
                        "callback": "${callback_details}"
                      }
                    }
                  }
                ]
              }
            }
          }
        }
      ]

Note that callbacks are processed in the same order that each call is made by a branch to `await_callback`. However, the execution order of branches is non-deterministic and can arrive at an outcome using various paths. For more information, see [Parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps).

## Try out a basic callback workflow

You can create a basic workflow and then test the call to that workflow's callback endpoint using curl. You must have the necessary `Workflows Editor` or `Workflows Admin` permissions for the project in which the workflow resides.

  1. [ Create and deploy](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#creating_a_workflow) the following workflow and then [execute](https://docs.cloud.google.com/workflows/docs/executing-workflow) it.  


### YAML
         
         - create_callback:
                 call: events.create_callback_endpoint
                 args:
                     http_callback_method: "GET"
                 result: callback_details
             - print_callback_details:
                 call: sys.log
                 args:
                     severity: "INFO"
                     text: ${"Listening for callbacks on " + callback_details.url}
             - await_callback:
                 call: events.await_callback
                 args:
                     callback: ${callback_details}
                     timeout: 3600
                 result: callback_request
             - print_callback_request:
                 call: sys.log
                 args:
                     severity: "INFO"
                     text: ${"Received " + json.encode_to_string(callback_request.http_request)}
             - return_callback_result:
                 return: ${callback_request.http_request}
             

### JSON
         
         [
               {
                 "create_callback": {
                   "call": "events.create_callback_endpoint",
                   "args": {
                     "http_callback_method": "GET"
                   },
                   "result": "callback_details"
                 }
               },
               {
                 "print_callback_details": {
                   "call": "sys.log",
                   "args": {
                     "severity": "INFO",
                     "text": "${\"Listening for callbacks on \" + callback_details.url}"
                   }
                 }
               },
               {
                 "await_callback": {
                   "call": "events.await_callback",
                   "args": {
                     "callback": "${callback_details}",
                     "timeout": 3600
                   },
                   "result": "callback_request"
                 }
               },
               {
                 "print_callback_request": {
                   "call": "sys.log",
                   "args": {
                     "severity": "INFO",
                     "text": "${\\"Received \\" + json.encode_to_string(callback_request.http_request)}"
                   }
                 }
               },
               {
                 "return_callback_result": {
                   "return": "${callback_request.http_request}"
                 }
               }
             ]
               

After executing the workflow, the state of the workflow execution is `ACTIVE` until the callback request is received or the timeout elapses. 

  2. Confirm the execution state and retrieve the callback URL:  


### Console

     1. In the Google Cloud console, go to the **Workflows** page: 

[Go to Workflows ](https://console.cloud.google.com/workflows)
     2. Click the name of the workflow that you just executed. 

The state of the workflow execution is displayed. 

     3. Click the **Logs** tab. 
     4. Look for a log entry similar to the following:
            
            Listening for callbacks on https://workflowexecutions.googleapis.com/v1/projects/...

     5. Copy the callback URL to use in the next command. 

### gcloud

     1. First, retrieve the execution ID: 
            
            gcloud logging read "Listening for callbacks" --freshness=DURATION

Replace `DURATION` with an appropriate amount of time to limit the log entries returned (if you have executed the workflow multiple times). 

For example, `--freshness=t10m` returns log entries that are not older than 10 minutes. For details, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 

The execution ID is returned. Note that the callback URL is also returned in the `textPayload` field. Copy both values to use in the following steps. 

     2. Run the following command: 
            
            gcloud workflows executions describe WORKFLOW_EXECUTION_ID --workflow=WORKFLOW_NAME

The state of the workflow execution is returned. 
  3. You can now call the callback endpoint using a curl command: 
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" CALLBACK_URL

Note that for a `POST` endpoint, you must use a `Content-Type` representation header. For example: 
         
         curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-access-token)" -d '{"foo" : "bar"}' CALLBACK_URL

Replace `CALLBACK_URL` with the URL you copied in the previous step. 

  4. Through the Google Cloud console or using the Google Cloud CLI, confirm that the state of the workflow execution is now `SUCCEEDED`. 
  5. Look for the log entry with the returned `textPayload` that resembles the following: 
         
         Received {"body":null,"headers":...




## Samples

These samples demonstrate the syntax.

### Catch timeout errors

This sample adds to the previous sample by catching any timeout errors, and writing the errors to the system log.

### YAML
    
    
        main:
          steps:
            - create_callback:
                call: events.create_callback_endpoint
                args:
                    http_callback_method: "GET"
                result: callback_details
            - print_callback_details:
                call: sys.log
                args:
                    severity: "INFO"
                    text: ${"Listening for callbacks on " + callback_details.url}
            - await_callback:
                try:
                    call: events.await_callback
                    args:
                        callback: ${callback_details}
                        timeout: 3600
                    result: callback_request
                except:
                    as: e
                    steps:
                        - log_error:
                            call: sys.log
                            args:
                                severity: "ERROR"
                                text: ${"Received error " + e.message}
                            next: end
            - print_callback_result:
                call: sys.log
                args:
                    severity: "INFO"
                    text: ${"Received " + json.encode_to_string(callback_request.http_request)}
        

### JSON
    
    
        {
          "main": {
            "steps": [
              {
                "create_callback": {
                  "call": "events.create_callback_endpoint",
                  "args": {
                    "http_callback_method": "GET"
                  },
                  "result": "callback_details"
                }
              },
              {
                "print_callback_details": {
                  "call": "sys.log",
                  "args": {
                    "severity": "INFO",
                    "text": "${\"Listening for callbacks on \" + callback_details.url}"
                  }
                }
              },
              {
                "await_callback": {
                  "try": {
                    "call": "events.await_callback",
                    "args": {
                      "callback": "${callback_details}",
                      "timeout": 3600
                    },
                    "result": "callback_request"
                  },
                  "except": {
                    "as": "e",
                    "steps": [
                      {
                        "log_error": {
                          "call": "sys.log",
                          "args": {
                            "severity": "ERROR",
                            "text": "${\"Received error \" + e.message}"
                          },
                          "next": "end"
                        }
                      }
                    ]
                  }
                }
              },
              {
                "print_callback_result": {
                  "call": "sys.log",
                  "args": {
                    "severity": "INFO",
                    "text": "${\"Received \" + json.encode_to_string(callback_request.http_request)}"
                  }
                }
              }
            ]
          }
        }
          

### Wait on a callback in a retry loop

This sample modifies the previous sample by implementing [a retry step](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying). Using a custom retry predicate, the workflow logs a warning when a timeout occurs and then retries the wait on the callback endpoint, up to five times. If the retry quota is exhausted before the callback is received, the final timeout error causes the workflow to fail.

### YAML
    
    
        main:
          steps:
            - create_callback:
                call: events.create_callback_endpoint
                args:
                    http_callback_method: "GET"
                result: callback_details
            - print_callback_details:
                call: sys.log
                args:
                    severity: "INFO"
                    text: ${"Listening for callbacks on " + callback_details.url}
            - await_callback:
                try:
                    call: events.await_callback
                    args:
                        callback: ${callback_details}
                        timeout: 60.0
                    result: callback_request
                retry:
                    predicate: ${log_timeout}
                    max_retries: 5
                    backoff:
                        initial_delay: 1
                        max_delay: 10
                        multiplier: 2
            - print_callback_result:
                call: sys.log
                args:
                    severity: "INFO"
                    text: ${"Received " + json.encode_to_string(callback_request.http_request)}
        log_timeout:
            params: [e]
            steps:
              - when_to_repeat:
                  switch:
                    - condition: ${"TimeoutError" in e.tags}
                      steps:
                          - log_error_and_retry:
                              call: sys.log
                              args:
                                  severity: "WARNING"
                                  text: "Timed out waiting for callback, retrying"
                          - exit_predicate:
                              return: true
              - otherwise:
                  return: false
        

### JSON
    
    
        {
          "main": {
            "steps": [
              {
                "create_callback": {
                  "call": "events.create_callback_endpoint",
                  "args": {
                    "http_callback_method": "GET"
                  },
                  "result": "callback_details"
                }
              },
              {
                "print_callback_details": {
                  "call": "sys.log",
                  "args": {
                    "severity": "INFO",
                    "text": "${\"Listening for callbacks on \" + callback_details.url}"
                  }
                }
              },
              {
                "await_callback": {
                  "try": {
                    "call": "events.await_callback",
                    "args": {
                      "callback": "${callback_details}",
                      "timeout": 60
                    },
                    "result": "callback_request"
                  },
                  "retry": {
                    "predicate": "${log_timeout}",
                    "max_retries": 5,
                    "backoff": {
                      "initial_delay": 1,
                      "max_delay": 10,
                      "multiplier": 2
                    }
                  }
                }
              },
              {
                "print_callback_result": {
                  "call": "sys.log",
                  "args": {
                    "severity": "INFO",
                    "text": "${\"Received \" + json.encode_to_string(callback_request.http_request)}"
                  }
                }
              }
            ]
          },
          "log_timeout": {
            "params": [
              "e"
            ],
            "steps": [
              {
                "when_to_repeat": {
                  "switch": [
                    {
                      "condition": "${\"TimeoutError\" in e.tags}",
                      "steps": [
                        {
                          "log_error_and_retry": {
                            "call": "sys.log",
                            "args": {
                              "severity": "WARNING",
                              "text": "Timed out waiting for callback, retrying"
                            }
                          }
                        },
                        {
                          "exit_predicate": {
                            "return": true
                          }
                        }
                      ]
                    }
                  ]
                }
              },
              {
                "otherwise": {
                  "return": false
                }
              }
            ]
          }
        }
          

## What's next

  * [Tutorial: Pause and resume a workflow using callbacks and Google Sheets](https://docs.cloud.google.com/workflows/docs/tutorials/workflow-waits-callback-sheets)

  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
