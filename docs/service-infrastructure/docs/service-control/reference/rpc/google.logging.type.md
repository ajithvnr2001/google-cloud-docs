---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.logging.type
title: Package google.logging.type \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:34.670142+00:00
---

# Package google.logging.type  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.logging.type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.logging.type Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[LogSeverity](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.logging.type#google.logging.type.LogSeverity)` (enum)



## LogSeverity

The severity of the event described in a log entry, expressed as one of the standard severity levels listed below. For your reference, the levels are assigned the listed numeric values. The effect of using numeric values other than those listed is undefined.

You can filter for log entries by severity. For example, the following filter expression will match log entries with severities `INFO`, `NOTICE`, and `WARNING`:
    
    
    severity > DEBUG AND severity <= WARNING
    

If you are writing log entries, you should map other severity encodings to one of these standard levels. For example, you might map all of Java's FINE, FINER, and FINEST levels to `LogSeverity.DEBUG`. You can preserve the original severity level in the log entry payload if you wish.

Enums  
---  
`DEFAULT` | (0) The log entry has no assigned severity level.  
`DEBUG` | (100) Debug or trace information.  
`INFO` | (200) Routine information, such as ongoing status or performance.  
`NOTICE` | (300) Normal but significant events, such as start up, shut down, or a configuration change.  
`WARNING` | (400) Warning events might cause problems.  
`ERROR` | (500) Error events are likely to cause problems.  
`CRITICAL` | (600) Critical events cause more severe problems or outages.  
`ALERT` | (700) A person must take an action immediately.  
`EMERGENCY` | (800) One or more systems are unusable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
