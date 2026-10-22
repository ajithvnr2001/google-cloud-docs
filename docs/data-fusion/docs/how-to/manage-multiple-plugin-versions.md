---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-multiple-plugin-versions/
title: Manage multiple versions of the same plugin \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:11.562142+00:00
---

# Manage multiple versions of the same plugin  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-multiple-plugin-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage multiple versions of the same plugin Stay organized with collections  Save and categorize content based on your preferences. 

If you have multiple versions of the same plugin in the Cloud Data Fusion Studio, you can select which one you want to use in a data pipeline. If you upgrade a Cloud Data Fusion instance without upgrading the pipelines, there are typically multiple versions of the plugins present.

**Note:** Only one plugin version can be used per pipeline. For example, you cannot have both BigQuery batch source 0.16.2 and BigQuery batch source 0.17.1 in the same pipeline.

To set the default version of a plugin, follow these steps:

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the Cloud Data Fusion Studio interface, click **Studio**.

  3. In the plugins list, hold the pointer over a plugin, such as the BigQuery batch source plugin, and click more_vert **More**.

  4. To change the default version of the plugin, click **Change** next to the current version of the plugin.

**Note:** If you don't see the **Change** option, you have only one version of the plugin in your namespace.
  5. Click the version of the plugin you want to use in the pipeline.This version becomes the default version of the plugin for all pipelines.




## What's next

  * Learn more about [plugin drivers](https://docs.cloud.google.com/data-fusion/docs/how-to/using-jdbc-drivers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
