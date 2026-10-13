---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/events/create_callback_endpoint/
title: Function: events.create_callback_endpoint \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:01.645461+00:00
---

# Function: events.create_callback_endpoint  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/events/create_callback_endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: events.create_callback_endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Creates a callback endpoint expecting the specified HTTP method.

For more information, see [Wait using callbacks](https://cloud.google.com/workflows/docs/creating-callback-endpoints).

## Arguments

Arguments  
---  
`http_callback_method` |  `string` The HTTP callback method. One of: `POST`(default), `GET`, `HEAD`, `PUT`, `DELETE`, `OPTIONS`, `PATCH`.  
  
## Returns

A map object with a `url` field that stores the URL of the created endpoint.

## Raised exceptions

Exceptions  
---  
`ValueError` | In case of invalid input values.  
`TypeError` | In case of invalid input types.  
  
## Examples
    
    
    # A basic callback workflow
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
