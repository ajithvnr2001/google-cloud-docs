---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-namespaces/
title: Create and manage namespaces \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:27.593860+00:00
---

# Create and manage namespaces  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-namespaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create and manage namespaces Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage namespaces in the Cloud Data Fusion Studio.

A namespace is a logical grouping of applications, data, and the associated metadata in a Cloud Data Fusion instance. You can think of namespaces as instance partitioning. Any application or data, referred to here as an _entity_ , can exist independently in multiple namespaces. In a single instance, one namespace stores the data and metadata of an entity independently from another namespace.

## Before you begin

When you first create a Cloud Data Fusion instance, you see a namespace called **default**. If you don't need to control access with multiple namespaces, you can work in this default namespace. Namespaces are only a logical partitioning. Scalability or concurrency continues to be maintained only at the instance level.

## Create a namespace

To create a namespace in the Cloud Data Fusion Studio, follow these steps:

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the Cloud Data Fusion Studio, click menu **Menu**.

  3. In the menu, click to expand the **Namespace** arrow_drop_down  options.

  4. Click **Add Namespace**.

  5. Enter a name and description and complete the optional configuration steps.

  6. Click **Finish**.




## Manage a namespace

To manage configurations in namespace, see [Namespace administration](https://docs.cloud.google.com/data-fusion/docs/concepts/manage-studio-administration#namespace-administration).

## What's next

  * Learn more about [Namespace microservices](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
