---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/calls/
title: Calls \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:46.860655+00:00
---

# Calls  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/calls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Calls Stay organized with collections  Save and categorize content based on your preferences. 

A common type of workflow step uses the `call` field to run a function and return a result:

### YAML
    
    
      - STEP_NAME:
          call: FUNCTION_NAME
          args:
              ARG_1: VALUE_1
              ARG_2: VALUE_2
              ...
          result: OUTPUT_VARIABLE

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "call": "FUNCTION_NAME",
            "args": {
              "ARG_1": "VALUE_1",
              "ARG_2": "VALUE_2"
            },
            "result": "OUTPUT_VARIABLE"
          }
        }
      ]

Replace the following:

  * `FUNCTION_NAME`: the name of the function you are calling
  * `ARG_1`,`ARG_2` (optional): if the function accepts parameters, the arguments you are passing and their values (`VALUE_1`, `VALUE_2`)
  * `OUTPUT_VARIABLE` (optional): if the function returns anything, the [variable](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#store-result) to store the returned data in



Calls are often HTTP requests but can be made to any function including a connector, a standard library function, or a subworkflow (user-defined function):

  * [Connectors](https://docs.cloud.google.com/workflows/docs/reference/googleapis) can be used to connect to other Google Cloud APIs within a workflow, and to integrate your workflows with those products, allowing you to perform operations from other Google Cloud services.
  * [Standard library functions](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview) include modules and frequently used functions, such as for data type and format conversions, as well as functions that make HTTP calls like [http.get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/get) and [http.post](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/post). To access HTTP response data saved in a variable, see [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).
  * [Subworkflows](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows) let you define a piece of logic that can be called from the main workflow, similar to a routine or function in a programming language.



## Samples

The following samples demonstrate the syntax. For more samples, see [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).

### Assign the response from an API call

This sample makes a call to a [sample API](https://github.com/GoogleCloudPlatform/workflows-samples/tree/main/functions/datetime). The returned day of the week is passed to the [Wikipedia API](https://wikipedia.org/w/api.php). Relevant articles on Wikipedia about the current day of the week are returned.

### YAML
    
    
    main:
      params: [input]
      steps:
        - checkSearchTermInInput:
            switch:
              - condition: '${"searchTerm" in input}'
                assign:
                  - searchTerm: '${input.searchTerm}'
                next: readWikipedia
        - getLocation:
            call: sys.get_env
            args:
              name: GOOGLE_CLOUD_LOCATION
            result: location
        - setFromCallResult:
            assign:
              - searchTerm: '${text.split(location, "-")[0]}'
        - readWikipedia:
            call: http.get
            args:
              url: 'https://en.wikipedia.org/w/api.php'
              query:
                action: opensearch
                search: '${searchTerm}'
            result: wikiResult
        - returnOutput:
            return: '${wikiResult.body[1]}'

### JSON
    
    
    {
      "main": {
        "params": [
          "input"
        ],
        "steps": [
          {
            "checkSearchTermInInput": {
              "switch": [
                {
                  "condition": "${\"searchTerm\" in input}",
                  "assign": [
                    {
                      "searchTerm": "${input.searchTerm}"
                    }
                  ],
                  "next": "readWikipedia"
                }
              ]
            }
          },
          {
            "getLocation": {
              "call": "sys.get_env",
              "args": {
                "name": "GOOGLE_CLOUD_LOCATION"
              },
              "result": "location"
            }
          },
          {
            "setFromCallResult": {
              "assign": [
                {
                  "searchTerm": "${text.split(location, \"-\")[0]}"
                }
              ]
            }
          },
          {
            "readWikipedia": {
              "call": "http.get",
              "args": {
                "url": "https://en.wikipedia.org/w/api.php",
                "query": {
                  "action": "opensearch",
                  "search": "${searchTerm}"
                }
              },
              "result": "wikiResult"
            }
          },
          {
            "returnOutput": {
              "return": "${wikiResult.body[1]}"
            }
          }
        ]
      }
    }
    

### Make an external HTTP POST request

This sample makes a POST request to an external HTTP endpoint.

### YAML
    
    
    - send_message:
        call: http.post
        args:
          url: https://www.example.com/endpoint
          body:
            some_val: "Hello World"
            another_val: 123
        result: the_message
    - return_value:
        return: ${the_message.body}

### JSON
    
    
    [
      {
        "send_message": {
          "call": "http.post",
          "args": {
            "url": "https://www.example.com/endpoint",
            "body": {
              "some_val": "Hello World",
              "another_val": 123
            }
          },
          "result": "the_message"
        }
      },
      {
        "return_value": {
          "return": "${the_message.body}"
        }
      }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
