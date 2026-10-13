---
url: https://docs.cloud.google.com/python/docs/reference/logging/latest/handlers-container-engine/
title: [DEPRECATED] Kubernetes Engine Handler \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:26.875917+00:00
---

# [DEPRECATED] Kubernetes Engine Handler  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/logging/latest/handlers-container-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  [DEPRECATED] Kubernetes Engine Handler Stay organized with collections  Save and categorize content based on your preferences. 

3.17.0 (latest)  3.16.3  3.15.0  3.13.0  3.12.1  3.11.3  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.1  3.2.5  3.1.2  3.0.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.2  1.15.3  1.14.0  1.13.0  1.12.1 

**Deprecated:** Deprecated since version 3.0.0: Use `StructuredLogHandler` instead.

Logging handler for Google Container Engine (GKE).

Formats log messages in a JSON format, so that Kubernetes clusters with the fluentd Google Cloud plugin installed can format their log messages so that metadata such as log level is properly captured.

### _class_ google.cloud.logging_v2.handlers.container_engine.ContainerEngineHandler(*, name=None, stream=None)

Bases: [`logging.StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler)

Handler to format log messages the format expected by GKE fluent.

This handler is written to format messages for the Google Container Engine (GKE) fluentd plugin, so that metadata such as log level are properly set.

DEPRECATED: use StructuredLogHandler to write formatted logs to standard out instead.

  * **Parameters**

    * **name** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The name of the custom log in Cloud Logging.

    * **stream** (_Optional_ _[__IO_ _]_) – Stream to be used by the handler.




#### format(record)

Format the message into JSON expected by fluentd.

  * **Parameters**

**record** ([_logging.LogRecord_](https://docs.python.org/3/library/logging.html#logging.LogRecord)) – The log record.

  * **Returns**

A JSON string formatted for GKE fluentd.

  * **Return type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
