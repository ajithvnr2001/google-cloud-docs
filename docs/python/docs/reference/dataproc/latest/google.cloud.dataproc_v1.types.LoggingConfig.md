---
url: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.LoggingConfig
title: Class LoggingConfig (5.31.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:49.651127+00:00
---

# Class LoggingConfig (5.31.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.LoggingConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LoggingConfig (5.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.31.0 (latest)  5.30.0  5.29.0  5.28.0  5.27.0  5.26.0  5.25.0  5.24.0  5.23.0  5.22.0  5.21.0  5.20.0  5.18.1  5.17.1  5.16.0  5.15.1  5.14.0  5.13.0  5.12.0  5.10.2  5.9.3  5.8.0  5.7.0  5.6.0  5.5.1  5.4.3  5.3.0  5.2.0  5.1.0  5.0.3  4.0.3  3.3.2  3.2.0  3.1.1  3.0.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.0.2  1.1.3  1.0.1  0.8.2  0.7.0  0.6.1  0.5.0 
    
    
    LoggingConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The runtime logging config of the job.

## Attribute  
  
---  
**Name** | **Description**  
`driver_log_levels` |  `MutableMapping[str, [google.cloud.dataproc_v1.types.LoggingConfig.Level](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.LoggingConfig.Level)]`   
The per-package log levels for the driver. This can include "root" package name to configure rootLogger. Examples: \- 'com.google = FATAL' \- 'root = INFO' \- 'org.apache = DEBUG'   
  
## Classes 

### DriverLogLevelsEntry
    
    
    DriverLogLevelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### Level
    
    
    Level(value)

The Log4j level for job execution. When running an `Apache Hive <https://hive.apache.org/>`__ job, Cloud Dataproc configures the Hive client to an equivalent verbosity level.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
