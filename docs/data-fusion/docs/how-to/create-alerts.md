---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/create-alerts/
title: Create pipeline alerts \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:55:44.867606+00:00
---

# Create pipeline alerts  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/create-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create pipeline alerts Stay organized with collections  Save and categorize content based on your preferences. 

Pipeline alerts in Cloud Data Fusion let you track execution status and monitor workflow health. These notifications help you detect pipeline failures immediately.

You can configure alerts using two different services depending on your deployment stage. Cloud Data Fusion alerts are set up during batch pipeline design and can't be added or edited after deployment. In contrast, you can create log-based alerts through Cloud Monitoring in the Google Cloud console at any time—either before or after you deploy the pipeline.

## Before you begin

You need a Cloud Data Fusion instance. For more information, see [Create a public instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).

## Add an alert in Cloud Data Fusion

**Note:** You cannot add or edit alerts on deployed pipelines in Cloud Data Fusion.

  1. Open your instance.

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Go to the **Studio** page where you're designing your pipeline.

  3. Click **Configure** > **Pipeline alerts** > add **Add**.

  4. Select and configure the alert. For more information about configuring alerts, see [Batch pipeline alerts](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/705265700/Batch+Pipeline+Alerts).

**Note:** For email alerts, if your pipeline doesn't have a long-running Managed Service for Apache Spark cluster with Simple Mail Transfer Protocol (SMTP) server, enter the mail server or service's information, such as its host and port requirements.
  5. After you configure the alert, click **Validate** to check for errors, and then click **Confirm**.




## Create an alert in Monitoring

  1. [Enable Cloud Logging](https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs#enabling-stackdriver) in your Cloud Data Fusion instance.

  2. [Create a log-based alert](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

     1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

This page lets you store, query, update, and delete data.

     2. Enter the following query:
            
            resource.type="cloud_dataproc_cluster"
            logName="projects/PROJECT_ID/logs/datafusion-pipeline-logs"
            resource.labels.project_id="PROJECT_ID"
            severity=ERROR
            jsonPayload.message=~"Pipeline '.*' failed."
            

Replace `PROJECT_ID` with your project's ID.

     3. Click **Create alert** and configure the alert.




An alert is only generated when the pipeline runs on a Managed Service for Apache Spark cluster and fails. For Managed Service for Apache Spark cluster creation failures, the alert is not generated.

## What's next

  * Refer to the CDAP OS [Batch Pipeline Alerts](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/705265700/Batch+Pipeline+Alerts) reference pages.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
