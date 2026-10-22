---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/logging/
title: View pipeline job logs \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:13.272324+00:00
---

# View pipeline job logs  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  View pipeline job logs Stay organized with collections  Save and categorize content based on your preferences. 

After you define, build, and run a pipeline, you can view and query log entries for your pipeline job and pipeline tasks. Learn more about [log entries for the Gemini Enterprise API](https://docs.cloud.google.com/logging/docs/api/platform-logs#vertex_ai_api).

This feature has costs associated with it. [Learn more about Cloud Logging pricing](https://docs.cloud.google.com/logging#pricing).

## View Gemini Enterprise logs for pipeline jobs

Use the following instructions to view logs for your Agent Platform Pipelines jobs in the Google Cloud console or the Google Cloud CLI.

### Console

  1. Enable the Cloud Logging API:

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging)

  2. In the Google Cloud console, go to the **Logs Explorer** :

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  3. Select an existing Gemini Enterprise Agent Platform project at the top of the page.

  4. In the **Query builder** , add the following:

     * **Resource** : Select **Vertex Pipelines Job**. In the dialog, select an Agent Platform Pipelines job.
     * **Log names** : In the Gemini Enterprise Agent Platform section, select `aiplatform.googlapis.com/pipeline_job_events`.
     * **Severity** : Select a log level.
     * **Time range** : Select a preset range or create a custom range.



### gcloud

  1. Run the following command to enable the Cloud Logging API:
         
         gcloud services enable logging.googleapis.com
         

  2. Execute the [gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud logging read "projects/PROJECT_ID/logs/aiplatform.googleapis.com/pipeline_job_events" \
             --limit=LIMIT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud logging read "projects/PROJECT_ID/logs/aiplatform.googleapis.com/pipeline_job_events" `
             --limit=LIMIT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud logging read "projects/PROJECT_ID/logs/aiplatform.googleapis.com/pipeline_job_events" ^
             --limit=LIMIT




## View Gemini Enterprise API logs for pipeline tasks

Use the following instructions to view logs for your Agent Platform Pipelines tasks in the Google Cloud console or the Google Cloud CLI.

### Console

  1. Enable the Cloud Logging API:

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging)

  2. In the Google Cloud console, go to the **Logs Explorer** :

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  3. Select an existing Gemini Enterprise Agent Platform project at the top of the page.

  4. In the **Query builder** , add the following:

     * **Resource** : Select **Vertex Pipelines Job**. In the dialog, select an Agent Platform Pipelines job.
     * **Log names** : In the Gemini Enterprise Agent Platform section, select `aiplatform.googlapis.com/pipeline_job_task_events`.
     * **Severity** : Select a log level.
     * **Time range** : Select a preset range or create a custom range.



### gcloud

  1. Run the following command to enable the Cloud Logging API:
         
         gcloud services enable logging.googleapis.com
         

  2. Execute the [gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud logging read "projects/PROJECT_ID/logs/aiplatform.googleapis.com/pipeline_job_task_events" \
             --limit=LIMIT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud logging read "projects/PROJECT_ID/logs/aiplatform.googleapis.com/pipeline_job_task_events" `
             --limit=LIMIT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud logging read "projects/PROJECT_ID/logs/aiplatform.googleapis.com/pipeline_job_task_events" ^
             --limit=LIMIT




## What's next

  * Learn how to [view pipeline metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/metrics).

  * Learn how to [create custom metrics in the Logs Explorer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/metrics#build-custom-metrics) to monitor the pipeline job failure rate.

  * Learn how to [configure email notifications](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
