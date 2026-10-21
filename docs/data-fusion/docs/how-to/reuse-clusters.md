---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/reuse-clusters/
title: Reuse clusters \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:55:44.965232+00:00
---

# Reuse clusters  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/reuse-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Reuse clusters Stay organized with collections  Save and categorize content based on your preferences. 

Reusing Managed Service for Apache Spark clusters in Cloud Data Fusion lets you reduce provisioning overhead and speed up pipeline execution across runs. For more information, see [When to reuse clusters](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#reuse-clusters) and [Run a pipeline against an existing Managed Service for Apache Spark cluster](https://docs.cloud.google.com/data-fusion/docs/how-to/running-against-existing-dataproc).

## Before you begin

  * You must have a Cloud Data Fusion instance in version 6.5.0 or later.



## Enable cluster reuse

You can reuse clusters in a new compute profile, or in one that's been used in a deployed pipeline.

### Enable cluster reuse in a new profile

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **System admin > Configuration > System compute profiles**.

  3. Click **Create new profile**.

  4. Choose the **Managed Service for Apache Spark** provisioner.

  5. In the **Create a profile for Managed Service for Apache Spark** window, enter the details about your cluster:

     1. In the **Profile label** and **Profile name** fields, enter a name to identify the profile—for example, `execution_compute-profile`.
     2. In the **Description** field, describe the purpose of the profile—for example, `Profile used for pipeline execution`.
     3. In the **Max idle time** field, enter a value. For more information, see [Set max idle time](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters#set_max_idle_time).
     4. Set the **Skip cluster delete** field to `True`. For more information, see [When to reuse clusters](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#reuse-clusters).
     5. Optional: configure other optional fields.
     6. Click **Create**.



### Enable cluster reuse in a deployed pipeline

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **List**.

  3. Click the **Deployed** tab and click a pipeline name. The deployed pipeline opens on the **Studio** page in the Cloud Data Fusion web interface.

  4. Click **Configure**.

  5. In the **Compute config** window, go to the chosen profile and click **Customize**.

  6. In the window that opens, enter the following values:

     1. In the **Max Idle Time** field, enter a value. For more information, see [Set max idle time](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters#set_max_idle_time).
     2. Set **Skip cluster delete** to `True`. For more information, see [When to reuse clusters](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#reuse-clusters).
  7. Click **Done**.




## What's next

  * Learn more about [configuring clusters](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters).
  * Troubleshoot [deleting clusters](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
