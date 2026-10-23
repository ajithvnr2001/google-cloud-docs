---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/plugins/
title: Plugins overview \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:45.030051+00:00
---

# Plugins overview  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/plugins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Plugins overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Data Fusion plugins let you move and manage data as it flows from source to sink in a data pipeline. Each stage, known as a node, consists of a customizable module that extends your workflow capabilities. In the Cloud Data Fusion web interface, you can access default plugins on the **Studio** page, browse the **Hub** for additional integrations, or explore all [Cloud Data Fusion plugins](https://cloud.google.com/data-fusion/plugins).

![Plugins in the web interface.](https://docs.cloud.google.com/static/data-fusion/docs/images/concepts/plugins-in-the-web-interface.png)

## Plugin types

Plugins are categorized into the following categories:

  * Sources
  * Transformations
  * Analytics
  * Sinks
  * Conditions and actions
  * Error handlers and alerts



### Sources

Source plugins connect to databases, files, or real-time streams from which your pipeline reads data. You set up sources for your data pipeline using the web interface, so you don't have to worry about coding low-level connections.

### Transformations

Transform plugins change data after it's ingested from a source. For example, you can clone a record, change the file format to JSON, or use the Javascript plugin to create a custom transformation.

### Analytics

Analytics plugins perform aggregations, such as joining data from different sources and running analytics and machine learning operations.

### Sinks

Sink plugins write data to resources, such as Cloud Storage, BigQuery, Spanner, relational databases, file systems, and mainframes. You can query the data that gets written to the sink using the Cloud Data Fusion web interface or REST API.

### Conditions and actions

Use condition and action plugins to schedule actions that take place during a workflow that don't directly manipulate data in the workflow. For example:

  * Use the Database plugin to schedule a database command to run at the end of your pipeline.
  * Use the File Move plugin to trigger an action that moves files within Cloud Storage.



### Error handlers and alerts

When stages encounter null values, logical errors, or other sources of errors, you can use an error handler plugin to catch errors. Use these plugins to find errors in the output after a transform or analytics plugin. You can write the errors to a database for analysis.

## What's next

  * [Explore the plugins](https://cloud.google.com/data-fusion/plugins).
  * [Create a data pipeline](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline) with the plugins.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
