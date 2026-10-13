---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/log/
title: Function: sys.log \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:22.669896+00:00
---

# Function: sys.log  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/log/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: sys.log Stay organized with collections  Save and categorize content based on your preferences. 

Writes one of `data`, `text`, or `json` to the log at specified severity.

The log is written using the Cloud Logging API, the `workflows.googleapis.com/Workflow` resource, and under the log name `projects/${GOOGLE_CLOUD_PROJECT_ID}/logs/Workflows`.

For more information, see [Send logs to Cloud Logging](https://docs.cloud.google.com/workflows/docs/log-workflow).

## Arguments

Arguments  
---  
`data` |  `integer|float|bool|string|list|dict` The log message. Maps are logged as a JSON payload and stored in the `jsonPayload` field of the log entry. Other accepted types are logged as a text payload and stored in the `textPayload` field of the log entry.  
`severity` |  `string` One of: `DEFAULT`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY` (default: `DEFAULT`).  
`text` |  `integer|float|bool|string|list|dict` The log message. Always logged as a text payload and stored in the `textPayload` field of the log entry.  
`json` |  `dict` The map to be logged as a JSON payload and stored in the `jsonPayload` field of the log entry.  
`timeout` |  `double` The timeout of the log call.  
  
## Raised exceptions

Exceptions  
---  
`TypeError` | 

  * If either `data` or `text` is specified with a type that is not one of `integer`, `float`, `bool`, `string`, `list`, or `dict`.
  * If `json` is specified with a type that is not `dict`.
  * If more than one of `data`, `text`, or `json` are specified.
  * If none of `data`, `text`, or `json` are specified.

  
`TimeoutError` | If the specified timeout is exceeded.  
  
## Examples

### Auto-detect payload
    
    
    - assignStep:
        assign:
          - myVar: "Log my error message"
    - argsMap:
        call: sys.log
        args:
          data: ${myVar}
          severity: "ERROR" # Optional
    - argsList:
        call: sys.log
        args: [${myVar}, "ERROR"]
    
    # Sample output:
    # {
    #   "textPayload": "Log my error message",
    #   ...
    #   "severity": "ERROR",
    #   ...
    # }

### Text payload
    
    
    - assignStep:
        assign:
          - myVar: "Log my error message"
    - argsMap:
        call: sys.log
        args:
          text: ${myVar}
          severity: "ERROR" # Optional
    - argsList:
        call: sys.log
        args: [${null}, "ERROR", ${myVar}]
    
    # Sample output:
    # {
    #     "textPayload": "Log my error message",
    #     ...
    #     "severity": "ERROR",
    #     ...
    # }

### JSON payload
    
    
    - createMap:
        assign:
          - myMap: {"Message1": "Log my error message"}
    - argsMap:
        call: sys.log
        args:
          json: ${myMap}
          severity: "ERROR" # Optional
    - argsList:
        call: sys.log
        args: [${null}, "ERROR", ${null}, ${myMap}]
    
    # Sample output:
    # {
    #     ...
    #     "jsonPayload": {
    #       "Message1": "Log my error message"
    #     },
    #     ...
    #     "severity": "ERROR",
    #     ...
    # }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
