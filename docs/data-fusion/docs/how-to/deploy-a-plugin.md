---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin/
title: Deploy a plugin from the Cloud Data Fusion Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:27.545032+00:00
---

# Deploy a plugin from the Cloud Data Fusion Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Deploy a plugin from the Cloud Data Fusion Hub Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy [plugins](https://docs.cloud.google.com/data-fusion/docs/concepts/plugins) from the Hub in Cloud Data Fusion.

Cloud Data Fusion has a set of plugins that are installed by default when you create a Cloud Data Fusion instance. These plugins are available for the default namespace and any new namespace that you create.

You can deploy additional plugins from the Hub. For example, if you want to read or write to Teradata, but don't see any Teradata sources or sinks in your namespace, go to the Hub, find the Teradata plugin, and deploy it. When you deploy a plugin from the Hub, it appears in the plugin palette on the **Studio** page in the namespace where you initiated the download. It's not available to other namespaces (you would have to deploy the plugin again for the namespace).

Besides plugins, the Hub also contains drivers and sample pipelines that can be deployed in a namespace.

## Add a plugin to an instance

### Console

  1. Go to the instance details: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. Click **Instances** , and then click the instance's name to go to the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Upgrade the instance to a version that supports the plugin.

  3. Open the instance in the Cloud Data Fusion web interface and click **Hub**.

  4. Choose a plugin. For configuration details for each plugin, see the [Plugin overview](https://docs.cloud.google.com/data-fusion/docs/concepts/plugins).

  5. Click **Deploy**.




The plugin appears in the plugins list on the Cloud Data Fusion **Studio** page, based on the type of plugin it is.

## Add an SAP plugin to an instance

### Console

  1. Go to the instance details: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. Click **Instances** , and then click the instance's name to go to the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Upgrade the instance to a version that supports the plugin.

  3. Open the instance in Cloud Data Fusion.

  4. In the Cloud Data Fusion web interface, click **Hub** , and then click the **SAP** tab.

  5. Click the name of the SAP plugin—for example, **SAP ODP**.

  6. Optional: To configure your SAP system for an SAP plugin, you get the required SAP code and configurations through SAP transport files, which are archived in a zip file. To get those files, click **Download**. For more information, see [Install plugin components in SAP using the SAP transport file](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-sap-erp#install).

  7. Click **Deploy**.




The plugin appears in the **Source** drop-down menu on the **Studio** page of the Cloud Data Fusion web interface. Click it to add the plugin to your pipeline.

## What's next

  * Learn how to [manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections) in Cloud Data Fusion.
  * Learn more about [plugin types](https://docs.cloud.google.com/data-fusion/docs/concepts/plugin-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
