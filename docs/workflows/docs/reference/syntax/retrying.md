---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying/
title: Retry steps \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:00.683635+00:00
---

# Retry steps  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Retry steps Stay organized with collections  Save and categorize content based on your preferences. 

You can define a retry policy to retry steps that have returned a specific error code; for example, a particular HTTP status code. The retry syntax described in this document lets you do the following:

  * Define which error codes will be retried
  * Define the maximum number of retry attempts
  * Define a backoff model to increase the likelihood of success



Note that retrying a step counts as an additional step execution for pricing purposes. For more information, see [Pricing](https://cloud.google.com/workflows/pricing).

**Note:** There is a known issue where the placement of `for` directly after `try` causes an error. For details and the workaround, see [Known issues](https://docs.cloud.google.com/workflows/docs/issues).

## Default and custom retry policies

A retry policy consists of a _predicate_ that defines which error codes should be retried, as well as _retry configuration values_ such as the maximum number of retries, and the delay in seconds between retries.

Workflows has default retry policies available for both idempotent and non-idempotent steps. When you use a default retry policy, you don't need to specify a predicate or define the retry configuration values.

Optionally, you can specify a custom retry policy. In the following example, a custom predicate is defined as a subworkflow, and the steps are retried a maximum of eight times. The delays between subsequent attempts are: 1, 2, 4, 8, 16, 32, 60, and 60 (time given in seconds). After eight retry attempts, the step is considered failed, and an exception is raised. Counting the initial execution, the step is executed nine times.

### YAML
    
    
    try:
        steps:
            ...
    retry:
      predicate: ${my_own_predicate}
      max_retries: 8
      backoff:
        initial_delay: 1
        max_delay: 60
        multiplier: 2

### JSON
    
    
    {
      "try": {
        "steps": "..."
      },
      "retry": {
        "predicate": "${my_own_predicate}",
        "max_retries": 8,
        "backoff": {
          "initial_delay": 1,
          "max_delay": 60,
          "multiplier": 2
        }
      }
    }

## Define a retry policy

You can define a retry policy by configuring the `try/retry` structure in one of three ways:

  * Use a default retry policy
  * Use a default retry predicate with custom retry configuration values
  * Use a custom retry policy



### Default retry policy

Workflows has default retry policies available for both idempotent and non-idempotent steps.

Since the default retry policies consist of a default retry predicate and default retry configuration values, you don't need to specify a retry predicate or define the retry configuration values.

### YAML
    
    
    - step_name:
        try:
            steps:
                STEPS_BLOCK
        retry: RETRY_POLICY

### JSON
    
    
    [
      {
        "step_name": {
          "try": {
            "steps": [
              STEPS_BLOCK
            ]
          },
          "retry": "RETRY_POLICY"
        }
      }
    ]

Replace the following:

  * `STEPS_BLOCK`: optional. The `steps` block can contain the following: 
    * [`assign`](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step)
    * [`call`](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
    * [`for`](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#for-in)
    * [`parallel`](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
    * [`raise`](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
    * [`return`](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing#using-return)
    * [`steps`](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps)
    * [`switch`](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
    * [`try`](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
  * `RETRY_POLICY`: the default retry policy to use. One of the following: **Note:** You should use the idempotent retry policy only for idempotent steps (steps that can be safely repeated). You should use the non-idempotent retry policy only for non-idempotent steps (steps that can't be safely repeated).
    * `${http.default_retry}` which has the following default configuration: 
          
          predicate: ${http.default_retry_predicate}
            max_retries: 5
            backoff:
                initial_delay: 1
                max_delay: 60
                multiplier: 1.25

This policy retries HTTP status codes [`429`, `502`, `503`, `504`], connection errors, connection failures, or timeout errors.

    * `${http.default_retry_non_idempotent}` which has the following default configuration: 
          
          predicate: ${http.default_retry_predicate_non_idempotent}
            max_retries: 5
            backoff:
                initial_delay: 1
                max_delay: 60
                multiplier: 1.25

This policy retries HTTP status codes [`429`, `503`] or connection failures.




#### Examples:

### YAML
    
    
    - idempotent_step:
        try:
            call: http.get
            args:
                url: https://example.com/api
        retry: ${http.default_retry}

### JSON
    
    
    [
      {
        "idempotent_step": {
          "try": {
            "call": "http.get",
            "args": {
              "url": "https://example.com/api"
            }
          },
          "retry": "${http.default_retry}"
        }
      }
    ]

### YAML
    
    
    - non_idempotent_step:
        try:
            call: http.get
            args:
                url: https://example.com/api
        retry: ${http.default_retry_non_idempotent}

### JSON
    
    
    [
      {
        "non_idempotent_step": {
          "try": {
            "call": "http.get",
            "args": {
              "url": "https://example.com/api"
            }
          },
          "retry": "${http.default_retry_non_idempotent}"
        }
      }
    ]

### Default retry predicate

You can use a default retry predicate with custom retry configuration values. Select the appropriate predicate for the type of step (idempotent or non-idempotent), then define the retry configuration values.

### YAML
    
    
    - step_name:
        try:
            steps:
                STEPS_BLOCK
        retry:
            predicate: RETRY_PREDICATE
            max_retries: NUMBER_OF_RETRIES
            backoff:
                initial_delay: DELAY_SECONDS
                max_delay: MAX_DELAY_SECONDS
                multiplier: DELAY_MULTIPLIER

### JSON
    
    
    [
      {
        "step_name": {
          "try": {
            "steps": [
              STEPS_BLOCK
            ]
          },
          "retry": {
            "predicate": "RETRY_PREDICATE",
            "max_retries": NUMBER_OF_RETRIES,
            "backoff": {
              "initial_delay": DELAY_SECONDS,
              "max_delay": MAX_DELAY_SECONDS,
              "multiplier": DELAY_MULTIPLIER
            }
          }
        }
      }
    ]

Replace the following:

  * `STEPS_BLOCK`: optional. The `steps` block can contain the following: 
    * [`assign`](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step)
    * [`call`](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
    * [`for`](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#for-in)
    * [`parallel`](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
    * [`raise`](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
    * [`return`](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing#using-return)
    * [`steps`](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps)
    * [`switch`](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
    * [`try`](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
  * `RETRY_PREDICATE`: defines which error codes will be retried. One of the following: 
    * `${http.default_retry_predicate}`—retries HTTP status codes [`429`, `502`, `503`, `504`], connection errors, connection failures, or timeout errors
    * `${http.default_retry_predicate_non_idempotent}`—retries HTTP status codes [`429`, `503`] or connection failures
  * `NUMBER_OF_RETRIES`: maximum number of times a step will be retried, not counting the initial step execution attempt.
  * `DELAY_SECONDS`: delay in seconds between the initial failure and the first retry.
  * `MAX_DELAY_SECONDS`: maximum delay in seconds between retries.
  * `DELAY_MULTIPLIER`: multiplier applied to the previous delay to calculate the delay for the subsequent retry.



#### Example:

### YAML
    
    
    - step_name:
        try:
            steps:
                ...
        retry:
            predicate: ${http.default_retry_predicate_non_idempotent}
            max_retries: 10
            backoff:
                initial_delay: 1
                max_delay: 90
                multiplier: 3

### JSON
    
    
    [
      {
        "step_name": {
          "try": {
            "steps":
            ...
          },
          "retry": {
            "predicate": "${http.default_retry_predicate_non_idempotent}",
            "max_retries": 10,
            "backoff": {
              "initial_delay": 1,
              "max_delay": 90,
              "multiplier": 3
            }
          }
        }
      }
    ]

### Custom retry policy

If the existing default retry policies don't work for your use case, you can use a custom retry policy by creating a [subworkflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows) to define your predicate. Then configure your retry configuration values, including your predicate, in the `retry` block of the main workflow.

### YAML
    
    
    - step_name:
        try:
            steps:
                STEPS_BLOCK
        retry:
            predicate: CUSTOM_PREDICATE
            max_retries: NUMBER_OF_RETRIES
            backoff:
                initial_delay: DELAY_SECONDS
                max_delay: MAX_DELAY_SECONDS
                multiplier: DELAY_MULTIPLIER

### JSON
    
    
    [
      {
        "step_name": {
          "try": {
            "steps": [
              STEPS_BLOCK
            ]
          },
          "retry": {
            "predicate": "CUSTOM_PREDICATE",
            "max_retries": NUMBER_OF_RETRIES,
            "backoff": {
              "initial_delay": DELAY_SECONDS,
              "max_delay": MAX_DELAY_SECONDS,
              "multiplier": DELAY_MULTIPLIER
            }
          }
        }
      }
    ]

Replace the following:

  * `STEPS_BLOCK`: optional. The `steps` block can contain the following: 
    * [`assign`](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step)
    * [`call`](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
    * [`for`](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#for-in)
    * [`parallel`](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
    * [`raise`](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
    * [`return`](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing#using-return)
    * [`steps`](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps)
    * [`switch`](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
    * [`try`](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
  * `CUSTOM_PREDICATE`: a subworkflow which accepts as its single argument a map representing the exception, and which returns `true` to trigger a retry and, otherwise, `false`.
  * `NUMBER_OF_RETRIES`: maximum number of times a step will be retried, not counting the initial step execution attempt.
  * `DELAY_SECONDS`: delay in seconds between the initial failure and the first retry.
  * `MAX_DELAY_SECONDS`: maximum delay in seconds between retries.
  * `DELAY_MULTIPLIER`: multiplier applied to the previous delay to calculate the delay for the subsequent retry.



#### Example:

### YAML
    
    
      main:
          - step_name:
              try:
                  steps:
                      ...
              retry:
                  predicate: ${retry_predicate}
                  max_retries: number_of_retries
                  backoff:
                      initial_delay: delay_seconds
                      max_delay: max_delay_seconds
                      multiplier: delay_multiplier
    
      retry_predicate:
          params: [e]
          steps:
              ...

### JSON
    
    
      {
        "main": [
          {
            "step_name": {
              "try": {
                "steps":
                ...
              },
              "retry": {
                "predicate": "${retry_predicate}",
                "max_retries": "number_of_retries",
                "backoff": {
                  "initial_delay": "delay_seconds",
                  "max_delay": "max_delay_seconds",
                  "multiplier": "delay_multiplier"
                }
              }
            }
          }
        ],
        "retry_predicate": {
          "params": [
            "e"
          ],
          "steps":
          ...
        }
      }

The predicate is checked against any errors that are raised, and determines if the error triggers a retry. To trigger a retry, return `true`; otherwise, return `false`. If an error isn't retried, or the retries are exhausted, the error is propagated, and can cause the execution to fail. You can handle this by using an [`except` block](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors).

Note that when using a custom predicate, errors are only raised for the following HTTP status codes:

  * Client error responses (`400`-`499`)
  * Server error responses (`500`-`599`)



To trigger the predicate for other HTTP status codes, you must explicitly raise an exception. For an example, see Retry steps using a custom retry policy for other HTTP status codes.

## Samples

These samples demonstrate the syntax.

### Retry steps using a default retry policy

This sample uses a default retry policy (`${http.default_retry}`) for HTTP requests.

### YAML
    
    
    - read_item:
        try:
          call: http.get
          args:
            url: https://example.com/someapi
          result: apiResponse
        retry: ${http.default_retry}

### JSON
    
    
    [
      {
        "read_item": {
          "try": {
            "call": "http.get",
            "args": {
              "url": "https://example.com/someapi"
            },
            "result": "apiResponse"
          },
          "retry": "${http.default_retry}"
        }
      }
    ]

### Retry steps using a custom retry policy

This sample implements a custom retry policy that retries HTTP requests that return an HTTP status code `500`.

### YAML
    
    
    main:
      steps:
        - read_item:
            try:
              call: http.get
              args:
                url: https://host.com/api
              result: api_response
            retry:
              predicate: ${custom_predicate}
              max_retries: 5
              backoff:
                initial_delay: 2
                max_delay: 60
                multiplier: 2
        - last_step:
            return: "OK"
    
    custom_predicate:
      params: [e]
      steps:
        - what_to_repeat:
            switch:
              - condition: ${e.code == 500}
                return: true
        - otherwise:
            return: false

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "read_item": {
              "try": {
                "call": "http.get",
                "args": {
                  "url": "https://host.com/api"
                },
                "result": "api_response"
              },
              "retry": {
                "predicate": "${custom_predicate}",
                "max_retries": 5,
                "backoff": {
                  "initial_delay": 2,
                  "max_delay": 60,
                  "multiplier": 2
                }
              }
            }
          },
          {
            "last_step": {
              "return": "OK"
            }
          }
        ]
      },
      "custom_predicate": {
        "params": [
          "e"
        ],
        "steps": [
          {
            "what_to_repeat": {
              "switch": [
                {
                  "condition": "${e.code == 500}",
                  "return": true
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

### Retry steps using a custom retry policy for other HTTP status codes

This sample implements a custom retry policy that retries HTTP requests that return an HTTP status code `202`.

### YAML
    
    
    main:
      steps:
        - read_item:
            try:
              steps:
                - callStep:
                    call: http.get
                    args:
                      url: https://host.com/api
                    result: api_response
                - checkNotOK:
                    switch:
                      - condition: ${api_response.code == 202}
                        raise: ${api_response}
            retry:
              predicate: ${custom_predicate}
              max_retries: 5
              backoff:
                initial_delay: 2
                max_delay: 60
                multiplier: 2
    
    custom_predicate:
      params: [e]
      steps:
        - what_to_repeat:
            switch:
              - condition: ${e.code == 202}
                return: true
        - otherwise:
            return: false

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "read_item": {
              "try": {
                "steps": [
                  {
                    "callStep": {
                      "call": "http.get",
                      "args": {
                        "url": "https://host.com/api"
                      },
                      "result": "api_response"
                    }
                  },
                  {
                    "checkNotOK": {
                      "switch": [
                        {
                          "condition": "${api_response.code == 202}",
                          "raise": "${api_response}"
                        }
                      ]
                    }
                  }
                ]
              },
              "retry": {
                "predicate": "${custom_predicate}",
                "max_retries": 5,
                "backoff": {
                  "initial_delay": 2,
                  "max_delay": 60,
                  "multiplier": 2
                }
              }
            }
          }
        ]
      },
      "custom_predicate": {
        "params": [
          "e"
        ],
        "steps": [
          {
            "what_to_repeat": {
              "switch": [
                {
                  "condition": "${e.code == 202}",
                  "return": true
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

### Retry steps using a custom configuration

This sample implements a default retry predicate (`${http.default_retry_predicate}`) to determine when to perform a retry, and custom retry configuration values.

### YAML
    
    
    - read_item:
        try:
          call: http.get
          args:
            url: https://example.com/someapi
          result: api_response
        retry:
          predicate: ${http.default_retry_predicate}
          max_retries: 5
          backoff:
            initial_delay: 2
            max_delay: 60
            multiplier: 2

### JSON
    
    
    [
      {
        "read_item": {
          "try": {
            "call": "http.get",
            "args": {
              "url": "https://example.com/someapi"
            },
            "result": "api_response"
          },
          "retry": {
            "predicate": "${http.default_retry_predicate}",
            "max_retries": 5,
            "backoff": {
              "initial_delay": 2,
              "max_delay": 60,
              "multiplier": 2
            }
          }
        }
      }
    ]

### Handle errors using a custom predicate

This sample defines a custom error handler, including a custom predicate, and custom backoff parameters. The custom predicate is defined as a subworkflow which accepts as its single argument a map representing the exception, and which returns `true` to trigger a retry and, otherwise, `false`.

### YAML
    
    
    # Define a custom error handler, custom predicate, and custom backoff parameters
    # The `my_own_predicate` subworkflow accepts a map as an argument and defines the
    # exception; it returns true if a retry; false, otherwise
    # Expected outcome: the execution fails and returns an HTTP 404 Not Found error
    main:
      steps:
        - read_item:
            try:
              call: http.get
              args:
                url: https://example.com/someapi
              result: api_response
            retry:
              predicate: ${my_own_predicate}
              max_retries: 5
              backoff:
                initial_delay: 2
                max_delay: 60
                multiplier: 2
        - last_step:
            return: "OK"
    
    my_own_predicate:
      params: [e]
      steps:
        - log_error_tags:
            call: sys.log
            args:
              data: ${e.tags}
              severity: "INFO"
        - log_error_message:
            call: sys.log
            args:
              data: ${e.message}
              severity: "INFO"
        - log_error_code:
            call: sys.log
            args:
              data: ${e.code}
              severity: "INFO"
        - what_to_repeat:
            switch:
              - condition: ${e.code == 202}
                return: true
        - otherwise:
            return: false

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "read_item": {
              "try": {
                "call": "http.get",
                "args": {
                  "url": "https://example.com/someapi"
                },
                "result": "api_response"
              },
              "retry": {
                "predicate": "${my_own_predicate}",
                "max_retries": 5,
                "backoff": {
                  "initial_delay": 2,
                  "max_delay": 60,
                  "multiplier": 2
                }
              }
            }
          },
          {
            "last_step": {
              "return": "OK"
            }
          }
        ]
      },
      "my_own_predicate": {
        "params": [
          "e"
        ],
        "steps": [
              {
                "log_error_tags": {
                  "call": "sys.log",
                  "args": {
                    "data": "${e.tags}",
                    "severity": "INFO"
                  }
                }
              },
              {
                "log_error_message": {
                  "call": "sys.log",
                  "args": {
                    "data": "${e.message}",
                    "severity": "INFO"
                  }
                }
              },
              {
                "log_error_code": {
                  "call": "sys.log",
                  "args": {
                    "data": "${e.code}",
                    "severity": "INFO"
                  }
                }
              },
              {
                "what_to_repeat": {
                  "switch": [
                    {
                      "condition": "${e.code == 202}",
                      "return": true
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
    

When you run the preceding workflow, the execution fails, and returns an HTTP `404 Not Found` error. To demonstrate this, the custom predicate uses the standard library [`sys.log`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/log) function and writes elements from the [error map](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types) to the log. For example, the log output should be similar to the following:
    
    
    {
      "textPayload": "[\"HttpError\"]",
      ...
      "severity": "INFO",
      ...
    }
    {
      "textPayload": "HTTP server responded with error code 404",
      ...
      "severity": "INFO",
      ...
    }
    {
      "textPayload": "404",
      ...
      "severity": "INFO",
      ...
    }

## What's next

  * [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types)
  * [Raise errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
  * [Catch errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
