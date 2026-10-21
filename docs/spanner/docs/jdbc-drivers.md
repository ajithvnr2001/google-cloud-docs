---
url: https://docs.cloud.google.com/spanner/docs/jdbc-drivers/
title: JDBC drivers \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:20.583707+00:00
---

# JDBC drivers  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/jdbc-drivers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  JDBC drivers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the JDBC drivers that Spanner supports for GoogleSQL-dialect databases and PostgreSQL-dialect databases. You can use these drivers to connect to Spanner from Java applications. Spanner supports the following JDBC drivers:

  * The Spanner JDBC driver, which is an open-source JDBC driver that is written, provided, and supported by Google, similar to the [Cloud Client Libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). This is the recommended JDBC driver for Spanner, especially for the GoogleSQL dialect. You can also use it to connect to PostgreSQL-dialect databases.
  * The PostgreSQL JDBC driver in combination with PGAdapter. This driver only supports PostgreSQL-dialect databases.

| Spanner JDBC driver | PostgreSQL JDBC driver  
---|---|---  
Download | [Maven Central](https://search.maven.org/artifact/com.google.cloud/google-cloud-spanner-jdbc) | [Maven Central](https://search.maven.org/artifact/org.postgresql/postgresql)  
Written by | Google | PostgreSQL  
Support | Google | Google  
Open source | Yes; Apache license | Yes; BSD 2-Clause  
**Note:** Spanner previously supported the Simba JDBC driver. If you already use the Simba driver with Spanner, you can continue to do so.

For information about the Spanner JDBC driver, see [Spanner JDBC driver FAQ](https://docs.cloud.google.com/spanner/docs/open-source-jdbc) and [How to use the Spanner JDBC driver](https://docs.cloud.google.com/spanner/docs/use-oss-jdbc).

For information about the PostgreSQL JDBC driver, see [Connect JDBC to a PostgreSQL-dialect database](https://docs.cloud.google.com/spanner/docs/pg-jdbc-connect).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
