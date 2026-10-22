---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/view-maintenance-logs/
title: View maintenance logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:01.822414+00:00
---

# View maintenance logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/view-maintenance-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  View maintenance logs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to find and use [Cloud Logging](https://docs.cloud.google.com/logging/docs) to query and view maintenance logs for an Apigee instance.

## View logs for scheduled maintenance

You can use the Google Cloud console to query and view logs for scheduled maintenance.

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.
  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Apigee captured over the past 30 days.
  4. In the Query builder, add the following lines of code: 
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="ApigeeMaintenanceAdvanced"
             

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for scheduled maintenance.



## View logs for in-progress maintenance

You can use the Google Cloud console to query and view logs for maintenance that's in progress.

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.
  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Apigee captured over the past 30 days.
  4. In the Query builder, add the following lines of code: 
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="ApigeeMaintenanceOngoing"
         labels.is_completed="false"
             

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for maintenance that's in progress.



## View logs for completed maintenance

You can use the Google Cloud console to query and view logs for maintenance that's completed.

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.
  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Apigee captured over the past 30 days.
  4. In the Query builder, add the following lines of code: 
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="ApigeeMaintenanceOngoing"
         labels.is_completed="true"
             

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for maintenance that's completed.



## View logs for canceled maintenance

You can use the Google Cloud console to query and view logs for maintenance that's canceled.

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.
  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Apigee captured over the past 30 days.
  4. In the Query builder, add the following lines of code: 
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="ApigeeMaintenanceCancelled"
             

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for maintenance that's canceled.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
