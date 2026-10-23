---
url: https://docs.cloud.google.com/spanner-omni/client-library-overview/
title: Client library support for Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:46.057308+00:00
---

# Client library support for Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/client-library-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Client library support for Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

You can use existing [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries) to connect to Spanner Omni. However, there are some differences in how to connect, specifically in connection strings and authentication methods. This document describes these differences and provides guidance for accessing Spanner Omni with existing Spanner client libraries and drivers.

Although the Spanner Omni resource model references entities such as projects, outside of Google Cloud, these entities have no significance. Additionally, other common entities, such as instances, might differ based on the deployment method. 

When using Spanner client libraries with Spanner Omni, note the following differences:

  * The `project` and `instance` must be set to `default` when required by client libraries or tools.

  * Multi-tenancy isn't supported within a Spanner Omni deployment. Each deployment provides a single, precreated default instance (named `instances/default`), which you can use to create databases and other resources.




## What's next

  * [Use the Go client library to connect to Spanner Omni](https://docs.cloud.google.com/spanner-omni/go).

  * [Use the Java client library to connect to Spanner Omni](https://docs.cloud.google.com/spanner-omni/java).

  * [Use the Python client library to connect to Spanner Omni](https://docs.cloud.google.com/spanner-omni/python).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
