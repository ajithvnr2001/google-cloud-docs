---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines/
title: Export and import pipelines \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:33.330569+00:00
---

# Export and import pipelines  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Export and import pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export and import pipeline configurations in JSON format. These JSON files are useful in the following scenarios:

  * Moving pipelines from a design environment to an execution environment.
  * Moving pipelines to a new Cloud Data Fusion version or instance.
  * Troubleshooting.



## Export a pipeline

To export your pipeline in JSON Format:

  1. Go to your instance: 
     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **List**.
  3. For the desired pipelines, click settings.
  4. Click **Export**.
  5. Save the JSON files.



## Import a pipeline

In the environment or instance where you want to import your pipeline:

  1. Open the Cloud Data Fusion **Studio** page.
  2. Click **Import**.
  3. Upload the JSON file that you saved when you exported your pipeline.
  4. Optional: You might be prompted to upgrade the version of your plugins. Click **Fix all**. If a particular plugin is not found, follow the prompts to install it from the Hub.
  5. Optional: If you use a custom plugin in your pipeline and you receive a prompt in the upgrade window that the plugin was not found, you must deploy that custom plugin first, and then import the pipeline again.



Your pipeline opens in the **Studio** page. To deploy your pipeline as-is, click **Deploy**.

## Details

A pipeline is exported in JSON format. The file includes information about sources, sinks, and the connections between them.

It doesn't include triggers that you created after the pipeline was deployed. To get details about those triggers, recreate them in a different environment.

## What's next

  * Learn how to [upgrade Cloud Data Fusion instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).
  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
