---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/using-jdbc-drivers/
title: Plugin drivers \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:28.555081+00:00
---

# Plugin drivers  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/using-jdbc-drivers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Plugin drivers Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Java Database Connectivity (JDBC) drivers with Cloud Data Fusion pipelines.

Some plugins in Cloud Data Fusion require a JDBC driver to be added to the namespace. For example, before you can run a pipeline with a MySQL batch source plugin, you must add the supported MySQL driver to the namespace. You can add JDBC drivers to a namespace from the Cloud Data Fusion Hub, the **Namespace admin** page, or the **Add entity** page. You can also delete unneeded JDBC drivers from the **Namespace admin** page.

## Add a JDBC driver

### Hub

To add a JDBC driver from the Cloud Data Fusion Hub, follow these steps:

  1. In the Cloud Data Fusion Studio, click **Hub** > **Drivers** , and click a driver.
  2. Optional: To get information about where to download the JAR file, click **Download**.
  3. Click **Deploy** , upload the JAR file, and click **Next**.
  4. Verify the class name and version of the driver.
  5. Click **Finish**.



Cloud Data Fusion adds the driver to the namespace.

### Namespace admin page

To add a JDBC driver from the **Namespace administrator** page, follow these steps:

  1. Download a driver. For example, to download the JDBC driver for MySQL, go to `dev.mysql.com` and download the JAR file.
  2. In Cloud Data Fusion, click menu **Menu** > **Namespace Admin**.
  3. On the **Namespace** page, click **Drivers**.
  4. Upload your JAR file and click **Next**.
  5. Enter the name and class of the driver.
  6. Click **Finish**.



The driver is added to the namespace.

### Add entity page

To add a JDBC driver from the **Add entity** page, follow these steps:

  1. Download a driver. For example, to download the JDBC driver for MySQL, go to `dev.mysql.com` and download the JAR file.
  2. On the **Pipeline** page, click the green plus sign.
  3. On the **Add entity** page that appears, go to **Driver** and click **Upload**.
  4. Upload the JAR file and click **Next**.
  5. Enter the name and class of the driver.
  6. Click **Finish**.



The driver is added to the namespace.

## Use a JDBC driver

  1. On the **Pipeline** page in the Cloud Data Fusion Studio, choose a plugin from the **Source** or **Sink** list. The node for the source or sink appears in your pipeline.
  2. Hold the pointer over the node in the pipeline and click **Properties**.
  3. In the **Reference name** field, enter the name you defined for the driver in the preceding Add a JDBC driver step.
  4. Click close **Close**.



## Delete a JDBC driver

To delete a JDBC driver from a namespace, follow these steps:

  1. In Cloud Data Fusion, click menu **Menu** > **Namespace Admin**.
  2. On the **Namespace** page, click **Drivers**.
  3. Choose a driver and click more_vert **More**.
  4. Click **Delete**.



## What's next

  * Learn about [configuring plugins](https://docs.cloud.google.com/data-fusion/docs/concepts/plugins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
