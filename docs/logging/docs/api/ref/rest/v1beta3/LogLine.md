---
url: https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/LogLine/
title: LogLine \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:26:49.465513+00:00
---

# LogLine  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/LogLine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)



Send feedback 

#  LogLine Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SourceLocation
    * JSON representation



Application log line emitted while processing a request.

JSON representation  
---  
      
    
    {
      "time": string,
      "severity": enum([LogSeverity](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogSeverity)),
      "logMessage": string,
      "sourceLocation": {
        object([SourceLocation](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/LogLine#SourceLocation))
      },
    }  
  
Field name | Type | Description  
---|---|---  
`time` | `string` | Approximate time when this log entry was made.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`severity` | `enum(`[LogSeverity](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogSeverity)`)` | Severity of this log entry.  
`logMessage` | `string` | App-provided log message.  
`sourceLocation` | `object(`[SourceLocation](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/LogLine#SourceLocation)`)` | Where in the source code this log message was written.  
  
## SourceLocation

Specifies a location in a source code file.

JSON representation  
---  
      
    
    {
      "file": string,
      "line": string,
      "functionName": string,
    }  
  
Field name | Type | Description  
---|---|---  
`file` | `string` | Source file name. Depending on the runtime environment, this might be a simple name or a fully-qualified name.  
`line` | `string` | Line within the source file.  
`functionName` | `string` | Human-readable name of the function or method being invoked, with optional context such as the class or package name. This information is used in contexts such as the logs viewer, where a file and line number are less meaningful. The format can vary by language. For example: `qual.if.ied.Class.method` (Java), `dir/package.func` (Go), `function` (Python).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
