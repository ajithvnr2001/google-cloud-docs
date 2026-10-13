---
url: https://docs.cloud.google.com/python/docs/reference/appenginelogging/latest/google.cloud.appengine_logging_v1.types.LogLine
title: Class LogLine (1.11.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:36.898462+00:00
---

# Class LogLine (1.11.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/appenginelogging/latest/google.cloud.appengine_logging_v1.types.LogLine

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LogLine (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.2  1.5.0  1.4.5  1.3.2  1.2.0  1.1.6  1.0.0  0.2.0  0.1.5 
    
    
    LogLine(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Application log line emitted while processing a request.

## Attributes  
  
---  
**Name** | **Description**  
`time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Approximate time when this log entry was made.   
`severity` |  `google.logging.type.log_severity_pb2.LogSeverity`   
Severity of this log entry.   
`log_message` |  `str`   
App-provided log message.   
`source_location` |  `[google.cloud.appengine_logging_v1.types.SourceLocation](https://docs.cloud.google.com/python/docs/reference/appenginelogging/latest/google.cloud.appengine_logging_v1.types.SourceLocation)`   
Where in the source code this log message was written.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
