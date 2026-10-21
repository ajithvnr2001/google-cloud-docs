---
url: https://docs.cloud.google.com/monitoring/mql/
title: Monitoring Query Language overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:37.095531+00:00
---

# Monitoring Query Language overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/mql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Monitoring Query Language overview Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available in the Google Cloud console when you create charts, dashboards, and alerting policies. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API. For more information, see the [deprecation notice for MQL](https://docs.cloud.google.com/stackdriver/docs/deprecations/mql). 

Monitoring Query Language (MQL) provides an expressive, text-based interface to Cloud Monitoring time-series data. By using MQL, you can retrieve, filter, and manipulate time-series data.

## Why use MQL?

With MQL, you can manipulate time series to create charts that you can't create any other way. For example, you can do the following:

  * Compute the ratio of requests resulting in a particular class of response codes
  * Compute the ratio of current values to past values
  * Select by arbitrary, rather than predefined, percentile values
  * Select a random sample of time series
  * Evaluate arbitrary arithmetic expressions over values from time series of multiple metric types.
  * Create new labels to aggregate data by, using arbitrary string manipulations including regular expression sub-field capture.
  * Control the time range and period of output data.



MQL uses a set of operations and functions. Operations are linked together using the common pipe mechanism, where the output of one operation becomes the input to the next. Linking operations makes it possible to build up complex queries incrementally.

Additionally, the code editor provides syntactic help in the form of error messages. For more information, see [Use the code editor for MQL](https://docs.cloud.google.com/monitoring/mql/query-editor).

## What's next?

You can create and submit MQL queries by using the code editor or the Monitoring API.

  * For information about the code editor, see [Use the code editor for MQL](https://docs.cloud.google.com/monitoring/mql/query-editor).
  * For information about using MQL queries with the Monitoring API, see [Using the API](https://docs.cloud.google.com/monitoring/mql/qn-from-api).



You can also create alerting policies with MQL by using the Monitoring API. For more information, see [Creating conditions for alerting policies](https://docs.cloud.google.com/monitoring/mql/qn-from-api#ql-alert-condition).

For a series of examples of MQL queries, see [Examples](https://docs.cloud.google.com/monitoring/mql/examples).

For some general information about MQL, see [About the MQL language](https://docs.cloud.google.com/monitoring/mql/query-language).

For a comprehensive reference, see [The Monitoring Query Language reference](https://docs.cloud.google.com/monitoring/mql/reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
