---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/plugin-types/
title: Types of plugins \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:27.437347+00:00
---

# Types of plugins  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/plugin-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Types of plugins Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the types of plugins that are installed by default when you create a Cloud Data Fusion instance. These plugins are available in the default namespace in your instance, and any new namespaces that you create. You can download additional plugins from [Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin).

Plugins have the following categories in Cloud Data Fusion. They appear on the left-hand panel in the Cloud Data Fusion **Studio** page.

## Source

Source plugins connect to databases, files, or real-time streams where your pipeline reads data. You set up sources for a data pipeline using the web interface, so you don't have to use code to configure low-level connections.

## Transform

Transformation plugins change data after it's loaded from a source. For example, you can use these plugins to clone a record, change the file format to JSON, or create a custom transformation using JavaScript.

## Analytics

Analytics plugins perform aggregations, such as joining data from different sources and running analytics and machine learning operations.

## Sink

Sink plugins write data to resources, such as Cloud Storage, BigQuery, Spanner, relational databases, file systems, and mainframes. You can query the data that gets written to the sink using the Cloud Data Fusion web interface or REST API.

## Conditions and actions

Condition and action plugins schedule actions that take place during a workflow, but don't directly manipulate data in the workflow.

Example use cases:

  * Schedule a database command to run at the end of your pipeline by adding the Database action plugin to your pipeline.
  * Trigger an action that moves files within Cloud Storage by adding the File Move plugin to your pipeline.



## Error handlers and alerts

When stages of the pipeline encounter null values, logical errors, or other errors, error handler plugins catch them. Use these plugins to find errors in the output after a transform or analytics plugin in your pipeline. You can write the errors to a database for analysis.

## What's next

  * Learn how to [deploy a plugin from the Cloud Data Fusion Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
