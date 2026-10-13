---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors/
title: Catch errors \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:50.081740+00:00
---

# Catch errors  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Catch errors Stay organized with collections  Save and categorize content based on your preferences. 

When a workflow throws an error during execution, it can be caught and handled.

**Note:** There is a known issue where the placement of `for` directly after `try` causes an error. For details and the workaround, see [Known issues](https://docs.cloud.google.com/workflows/docs/issues).

## Use a `try/except` structure

You can use a `try/except` structure for error handling. For example:

### YAML
    
    
      - STEP_NAME:
         try:
             call: http.get
             ...
         except:
             as: ERROR_MAP
             steps:
                 ...

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "try": {
              "call": "http.get"
              ...
            },
            "except": {
              "as": "ERROR_MAP",
              "steps":
                  ...
            }
          }
        }
      ]

Replace `ERROR_MAP` with the name of a map variable that contains the error message.

For example, the map for an `HttpError` error (with an HTTP status code >= `400`) has the following attributes:

  * `tags`: `HttpError` string
  * `message`: human-readable error message
  * `code`: HTTP status code
  * `headers`: response headers
  * `body`: response body



For other error tags, see [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types).

Note that the `steps` block is optional. It can contain the following:

  * [`assign`](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step)
  * [`call`](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
  * [`for`](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#for-in)
  * [`parallel`](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
  * [`raise`](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
  * [`return`](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing#using-return)
  * [`steps`](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps)
  * [`switch`](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
  * [`try`](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)



### Variable scope

A variable created inside an `except` block belongs to the _local scope_ of that block, and is accessible only in that scope. For details, see [Variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#variable-scope).

If you are assigning a variable inside an `except` block and want to access the variable outside of the block, assign the variable _before_ the block to place it in the surrounding scope. For details, see [Share a variable before an `except` block](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-outer-scope).

### Example of `try/except` structure

For example, Workflows considers any HTTP request that returns status code `400` or greater failed. This makes the workflow execution fail unless the workflow catches and handles the error:

### YAML
    
    
      - read_item:
          try:
              call: http.get
              args:
                  url: https://host.com/api
              result: api_response
          except:
              as: e
              steps:
                  - known_errors:
                      switch:
                      - condition: ${not("HttpError" in e.tags)}
                        return: "Connection problem."
                      - condition: ${e.code == 404}
                        return: "Sorry, URL wasn't found."
                      - condition: ${e.code == 403}
                        return: "Authentication error."
                  - unhandled_exception:
                      raise: ${e}
      - url_found:
          return: ${api_response.body}

### JSON
    
    
      [
        {
          "read_item": {
            "try": {
              "call": "http.get",
              "args": {
                "url": "https://host.com/api"
              },
              "result": "api_response"
            },
            "except": {
              "as": "e",
              "steps": [
                {
                  "known_errors": {
                    "switch": [
                      {
                        "condition": "${not(\"HttpError\" in e.tags)}",
                        "return": "Connection problem."
                      },
                      {
                        "condition": "${e.code == 404}",
                        "return": "Sorry, URL wasn't found."
                      },
                      {
                        "condition": "${e.code == 403}",
                        "return": "Authentication error."
                      }
                    ]
                  }
                },
                {
                  "unhandled_exception": {
                    "raise": "${e}"
                  }
                }
              ]
            }
          }
        },
        {
          "url_found": {
            "return": "${api_response.body}"
          }
        }
      ]

The `try` block can contain multiple steps, allowing them to share the same `except` block for error handling:

### YAML
    
    
      - read_item:
          try:
              steps:
                  - step_a:
                      call: http.get
                      args:
                          url: https://host.com/api
                      result: api_response1
                  - step_b:
                      call: http.get
                      args:
                          url: https://host.com/api2
                      result: api_response2
                      ...
          except:
              as: e
              steps:
                  - KnownErrors:
                  ...

### JSON
    
    
      [
        {
          "read_item": {
            "try": {
              "steps": [
                {
                  "step_a": {
                    "call": "http.get",
                    "args": {
                      "url": "https://host.com/api"
                    },
                    "result": "api_response1"
                  }
                },
                {
                  "step_b": {
                    "call": "http.get",
                    "args": {
                      "url": "https://host.com/api2"
                    },
                    "result": "api_response2"
                    ...
                  }
                }
              ]
            },
            "except": {
              "as": "e",
              "steps": [
                {
                  "KnownErrors": null
                }
                ...
              ]
            }
          }
        }
      ]

## Use a `try/retry/except` structure

You can also use a `try/retry/except` structure for error handling. For example:

### YAML
    
    
      - step_name:
          try:
              steps:
                  - step_a:
                      call: http.get
                      args:
                          url: https://httpstat.us/404
          retry: ${http.default_retry_non_idempotent}
          except:
              as: e
              steps:
                  - checkForTimeout:
                      switch:
                      - condition: ${e.code == 404}
                        return: "notfound_404"
                      - condition: ${e.code == 408}
                        return: "timeout_408"
                  - raiseError:
                      raise: ${e}
      - returnSuccess:
          return: "Success"

### JSON
    
    
      [
        {
          "step_name": {
            "try": {
              "steps": [
                {
                  "step_a": {
                    "call": "http.get",
                    "args": {
                      "url": "https://httpstat.us/404"
                    }
                  }
                }
              ]
            },
            "retry": "${http.default_retry_non_idempotent}",
            "except": {
              "as": "e",
              "steps": [
                {
                  "checkForTimeout": {
                    "switch": [
                      {
                        "condition": "${e.code == 404}",
                        "return": "notfound_404"
                      },
                      {
                        "condition": "${e.code == 408}",
                        "return": "timeout_408"
                      }
                    ]
                  }
                },
                {
                  "raiseError": {
                    "raise": "${e}"
                  }
                }
              ]
            }
          }
        },
        {
          "returnSuccess": {
            "return": "Success"
          }
        }
      ]

For more information, see [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying).

## Catch and handle HTTP request errors

This sample implements a custom exception handler based on the HTTP status code returned by the GET request. The workflow catches a potential exception and returns a predefined error message. If an exception is not recognized, the workflow execution fails and throws the exception as returned by the GET request.

The same pattern could be used to catch exceptions raised by Cloud Run or Cloud Run functions workloads.

### YAML
    
    
    # Use a custom exception handler to catch exceptions and return predefined
    # error messages; if the exception isn't recognized, the workflow
    # execution fails and throws the exception returned by the GET request
    - read_item:
        try:
          call: http.get
          args:
            url: https://example.com/someapi
            auth:
              type: OIDC
          result: API_response
        except:
          as: e
          steps:
            - known_errors:
                switch:
                  - condition: ${not("HttpError" in e.tags)}
                    next: connection_problem
                  - condition: ${e.code == 404}
                    next: url_not_found
                  - condition: ${e.code == 403}
                    next: auth_problem
            - unhandled_exception:
                raise: ${e}
    - url_found:
        return: ${API_response.body}
    - connection_problem:
        return: "Connection problem; check URL"
    - url_not_found:
        return: "Sorry, URL wasn't found"
    - auth_problem:
        return: "Authentication error"

### JSON
    
    
    [
      {
        "read_item": {
          "try": {
            "call": "http.get",
            "args": {
              "url": "https://example.com/someapi",
              "auth": {
                "type": "OIDC"
              }
            },
            "result": "API_response"
          },
          "except": {
            "as": "e",
            "steps": [
              {
                "known_errors": {
                  "switch": [
                    {
                      "condition": "${not(\"HttpError\" in e.tags)}",
                      "next": "connection_problem"
                    },
                    {
                      "condition": "${e.code == 404}",
                      "next": "url_not_found"
                    },
                    {
                      "condition": "${e.code == 403}",
                      "next": "auth_problem"
                    }
                  ]
                }
              },
              {
                "unhandled_exception": {
                  "raise": "${e}"
                }
              }
            ]
          }
        }
      },
      {
        "url_found": {
          "return": "${API_response.body}"
        }
      },
      {
        "connection_problem": {
          "return": "Connection problem; check URL"
        }
      },
      {
        "url_not_found": {
          "return": "Sorry, URL wasn't found"
        }
      },
      {
        "auth_problem": {
          "return": "Authentication error"
        }
      }
    ]

## What's next

  * [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types)
  * [Raise errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
  * [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
