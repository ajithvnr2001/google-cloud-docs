---
url: https://docs.cloud.google.com/oracle/database/docs/view-resource-logs/
title: View resource logs \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:54.698658+00:00
---

# View resource logs  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-resource-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View resource logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view and use the resource logs for your Oracle Database@Google Cloud resources using Cloud Logging.

You can view logs for your Oracle Database@Google Cloud instances, clusters, and databases using Logging in Google Cloud console. These logs capture all Google Cloud console, and Exadata Database and Autonomous AI Database Service events by default.

You can review these logs by looking up the resource name you want to view logs for in Logs Explorer.

## View resource logs

To view resources logs for your Oracle Database@Google Cloud resources:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the Google Cloud project that you want to view logging in at the top of the page.

  3. In the query builder, complete the following:

     1. Click **All resources** to open a drop-down and select **Exadata Infrastructure** , **Cloud VM Cluster** , or **Autonomous Database**. In the dialog, select your instance, cluster, or database, then click **Apply**.

     2. Click **All log names** to open a drop-down, select the log files you want to see, then click **Apply**. The following log files are available:

        * `oracledatabase.googleapis.com/CloudExadataInfrastructure`
        * `oracledatabase.googleapis.com/CloudVmCluster`
        * `oracledatabase.googleapis.com/ContainerDatabase`
        * `oracledatabase.googleapis.com/PluggableDatabase`
        * `oracledatabase.googleapis.com/AutonomousDatabase`
     3. Click **All severities** to open a drop-down and select a log level.

     4. Select a preset time range or create a custom range.




Your selected logs are shown in the results pane.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
