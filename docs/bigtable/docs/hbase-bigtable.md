---
url: https://docs.cloud.google.com/bigtable/docs/hbase-bigtable/
title: Bigtable and the HBase API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:41.029216+00:00
---

# Bigtable and the HBase API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bigtable and the HBase API

One way to communicate with Bigtable is through the Cloud Bigtable HBase client for Java, which is a customized version of the [Apache HBase](https://hbase.apache.org/) client. The Cloud Bigtable HBase client for Java enables you to write Java applications that communicate with Bigtable through the open-source [HBase API](https://hbase.apache.org/apidocs/). The client is compatible with HBase API versions 1.x and 2.x.

The Cloud Bigtable HBase client for Java is for customers who are migrating to Bigtable from HBase and want to continue using the HBase API. In all other cases, Java developers should instead use the [Cloud Bigtable client for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), which calls the Bigtable APIs. 

To learn how to add the HBase client for Java to your application, see [Client Libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).

Source code for the client is available in the GitHub repository [googleapis/java-bigtable-hbase](https://github.com/googleapis/java-bigtable-hbase). Sample code that uses the client is available in the following GitHub repositories:

  * [GoogleCloudPlatform/java-docs-samples](https://github.com/GoogleCloudPlatform/java-docs-samples)
  * [googleapis/java-bigtable-hbase](https://github.com/googleapis/java-bigtable-hbase)



When you use the Cloud Bigtable HBase client for Java, you don't need to run the HBase server. You are simply using a modified version of the HBase client interface. Google runs and maintains the servers for the Bigtable service.

Because HBase and Bigtable are not identical, there are minor differences between the standard HBase API and the HBase API for Cloud Bigtable. See [Differences between the HBase and Bigtable APIs](https://docs.cloud.google.com/bigtable/docs/hbase-differences) for details.

The Cloud Bigtable HBase client for Java works with Hadoop 2.4 and later. It requires a Java 8 runtime environment.

## What's next

  * View a ["hello world" example](https://docs.cloud.google.com/bigtable/docs/samples-java-hello) for the HBase client for Java.
  * Learn how to [connect to Bigtable](https://docs.cloud.google.com/bigtable/docs/hbase-connecting).
  * Find out how to [add the client library to your application](https://docs.cloud.google.com/bigtable/docs/reference/libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
