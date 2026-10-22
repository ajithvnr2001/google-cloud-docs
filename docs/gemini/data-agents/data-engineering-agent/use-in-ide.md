---
url: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/use-in-ide/
title: Use the Data Engineering Agent in Visual Studio Code \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:02.295868+00:00
---

# Use the Data Engineering Agent in Visual Studio Code  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/use-in-ide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Use the Data Engineering Agent in Visual Studio Code Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To provide feedback or to ask questions about this preview feature, contact [bigquery-dea-feedback@google.com](mailto:bigquery-dea-feedback@google.com).

The Data Engineering Agent within [Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit) can assist you in creating and building [orchestration pipelines](https://docs.cloud.google.com/orchestration-pipelines/overview) in your integrated development environment (IDE). By leveraging Gemini for Google Cloud, the Data Engineering Agent provides a natural language interface to automate the generation, modification, and management of complex orchestration workflows.

[Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview) is supported in VS Code, IDEs based on VS Code, and supported agentic CLIs.

The Data Engineering Agent supports the following common data engineering tasks:

  * **Create orchestration pipelines** : Generate a new pipeline in an empty workspace or add additional pipelines to existing projects.
  * **Modify pipeline structure** : Use natural language to add, remove, or update individual actions within an orchestration pipeline.
  * **Manage execution metadata** : Change pipeline names and update execution schedules, for example, from manual to daily runs.
  * **Troubleshoot pipeline runs** : Proactively identify the root cause of failed pipeline runs and apply agent-suggested fixes.



## Before you begin

Before you use the Data Engineering Agent in your IDE, perform the steps in this section.

  1. Install the [Data Agent Kit extension](https://docs.cloud.google.com/data-agent-kit/install). The Data Engineering Agent is included in Data Agent Kit.
  2. Enable the Gemini Data Analytics API and Dataform API.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=geminidataanalytics.googleapis.com,dataform.googleapis.com)

  3. [Install version 563.0.0 or later of the Google Cloud SDK](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).

  4. [Install the `gcloud beta` commands.](https://docs.cloud.google.com/sdk/gcloud/reference/components/install)

  5. [Configure an environment in Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/create-environments). Use the [default Managed Service for Apache Airflow environment configuration](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#basic-setup). Then, in the [**Scheduler** settings for Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/configure#set-scheduler), input the name of your Managed Service for Apache Airflow environment, the ID of the Google Cloud project where the environment is hosted, and the region where the environment is located.




### Required roles

To get the permissions that you need to interact with the Data Engineering Agent and its underlying services, ask your administrator to grant you the following IAM roles on project: 

  * [Gemini Data Analytics Stateless Chat User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentStatelessUser) (`roles/geminidataanalytics.dataAgentStatelessUser`)
  * [Dataform Code Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.codeEditor) (`roles/dataform.codeEditor`)
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * To list environments and manage Apache Airflow DAGs: [Composer User ](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.user) (`roles/composer.user`) 
  * To deploy the orchestration pipeline or update the pipeline using a designated Managed Airflow environment service account: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Best practices

  * Understand that the agent follows a multi-step loop. The agent first generates a plan for your approval. Next, the agent performs the act (for example, writing code). Finally, the agent verifies the results using dry runs or tests.
  * The agent's performance depends on the files open in your workspace. Use the `@file` syntax or open relevant SQLX files to give the agent the necessary context to build your orchestration logic.



## Create an orchestration pipeline

To create an orchestration pipeline in an empty workspace or add an additional orchestration pipeline to an existing workspace, do the following:

  1. Open your IDE with the Data Agent Kit extension installed.
  2. Open the **Ask Agent** panel.
  3. Enter a natural language prompt to generate an orchestration pipeline. For example:
         
         Create an orchestration pipeline that unifies my Google Ads and YouTube Ads
          data into a single marketing table.
         

Once you have entered a prompt, click **Send**.

  4. Review the generated pipeline structure and apply the changes.




## Update a pipeline schedule

To change the orchestration pipeline name or update the execution schedule (for example, from manual to daily), do the following:

  1. Open your IDE with the Data Agent Kit extension installed.
  2. Navigate to your existing orchestration pipeline configuration.
  3. Open the **Ask Agent** panel.
  4. Enter a natural language prompt to update the pipeline schedule. For example:
         
         Update the execution schedule for this pipeline to run daily at 2 AM.
         

The agent updates the underlying configuration, for example, the Apache Airflow DAG settings.

  5. Review and save the updated pipeline schedule.




## Modify pipeline actions

To add or delete individual actions in your orchestration pipeline, do the following:

  1. Open your IDE with the Data Agent Kit extension installed.
  2. Identify the pipeline action you want to add or delete.
  3. Open the **Ask Agent** panel.
  4. Enter a natural language prompt to modify the pipeline actions. For example:
         
         Add a new action to the pipeline that runs the daily_sales_aggregation table
         task.
         

  5. Review and save the updated pipeline definition.




## Troubleshoot

If you encounter any errors during orchestration pipeline generation, ensure that you have completed all the prerequisites required to run the Data Engineering Agent. For more information, see Before you begin.

To troubleshoot a failed orchestration or data pipeline run, do the following:

  1. Open your IDE with the Data Agent Kit extension installed.
  2. In your pipeline or development workspace, click the **Executions** tab.
  3. From the executions list, find the failed data pipeline run. You can identify failed runs in the **Status** column of the execution run.
  4. Hover over the failure icon, then click **Investigate**. The Data Engineering Agent analyzes the logs and identifies root causes, such as schema drift or data type mismatches.
  5. In the **Ask Agent** panel, review the suggested fix.
  6. To resolve the issue, enter a prompt such as, `Apply the suggested fix to the pipeline`. Alternatively, you can manually update the SQLX code based on the agent's analysis.



## What's next

  * Learn how to [deploy orchestration pipelines](https://docs.cloud.google.com/orchestration-pipelines/deploy-orchestration-pipelines).
  * Learn how to [create runner environments that execute orchestration pipelines](https://docs.cloud.google.com/orchestration-pipelines/create-runner-environments).
  * Learn about [manually defining and fine-tuning your pipeline and deployment configurations](https://docs.cloud.google.com/orchestration-pipelines/reference/orchestration-pipelines-dsl-reference).
  * Learn how to [build and modify orchestration pipelines using Google Cloud CLI commands](https://docs.cloud.google.com/orchestration-pipelines/manage-orchestration-pipelines).
  * Learn how to [use the Data Engineering Agent to build and modify data pipelines in Google Cloud console](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
