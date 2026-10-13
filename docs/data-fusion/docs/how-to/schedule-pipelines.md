---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/schedule-pipelines/
title: Schedule pipelines \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:34.023972+00:00
---

# Schedule pipelines  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/schedule-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Schedule pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a [schedule](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#scheduling) for your pipeline runs. For example, you can schedule a pipeline to run daily at 1:00 AM UTC.

## Before you begin

To create the schedule, you need to have a deployed pipeline in Cloud Data Fusion. If you don't have one, you can create a pipeline by following the [Quickstart](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline).

To create, edit, or suspend a schedule, open your pipeline in Cloud Data Fusion:

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Go to the Cloud Data Fusion **List** page.

  3. In the **Deployed** tab, choose a pipeline.

The **Pipeline** page opens, where you can create, edit, or suspend a schedule for your pipeline.




## Create the schedule

From the **Pipeline** page in the Cloud Data Fusion Studio, click **Schedule**.

You can use either the **Basic** or **Advanced** tab to define your schedule.

### Basic

  1. On the **Basic** tab, enter the following information about your schedule:

     * Frequency, such as `Every 5 minutes` and `Repeats every 30 days`.
     * Start time, in UTC.
     * Maximum concurrent runs: Choose up to ten runs. If there are already ten pipelines running, the scheduled run that you're creating won't run.
     * Compute Engine profile: Choose a compute profile. The default is the Managed Service for Apache Spark compute profile.
  2. Click **Save and start schedule** (or **Save schedule** , if you want to start it later).




### Advanced

  1. On the **Advanced** tab, define your schedule in cron syntax.
  2. In the **Maximum concurrent runs** field, choose up to ten runs. If there are already ten pipelines running, the scheduled run that you're creating won't run.
  3. Click **Save and start schedule** (or **Save schedule** , if you want to start it later).

**Note:** When setting the cron syntax and entering values in the **Days of the week** field, consider '1' as `Sunday`. For example, if you want to schedule the pipeline for weekdays and skip the weekend, enter `2,3,4,5,6`.

## Change or suspend the schedule

  * You can change, start, or suspend a pipeline schedule from the **Pipeline** page in the Cloud Data Fusion Studio.

  * To suspend the schedule, click **Unschedule**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
