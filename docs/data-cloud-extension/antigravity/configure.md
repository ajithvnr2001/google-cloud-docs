---
url: https://docs.cloud.google.com/data-cloud-extension/antigravity/configure/
title: Set up and configure settings \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:42:08.056823+00:00
---

# Set up and configure settings  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-cloud-extension/antigravity/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Set up and configure settings Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure initial settings after you install the Google Cloud Data Agent Kit IDE extension.

**Note:** If you're using the Data Agent Kit plugin with a supported CLI or coding agent, you can use natural language prompts to configure settings.

## Before you begin

Before you begin, complete the steps on [Install Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/install), including [selecting the services](https://docs.cloud.google.com/data-agent-kit/install#select-services) that you want to use. Sections of the Google Cloud Data Agent Kit menu for services that you haven't selected show **integration is not enabled** until you select them.

**Important:** In your IDE, Google Cloud Data Agent Kit and the Google Cloud CLI must be configured to use the same user account, project, region, and billing account.

## Configure Google Cloud project and region

If you haven't configured your project and region, take the following steps.

  1. To open the Data Cloud Settings editor, click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Select **Common**.
  4. Select your Project ID and Region. The project ID must match the project ID that you specified in the gcloud CLI.
  5. Click **Save**.



## Review required roles

Data Agent Kit checks your Identity and Access Management (IAM) roles when you select the services that you want to use.

  1. To open the Data Cloud Settings editor, click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Click **Service Integrations**.
  4. Select the services that you want to use, and then click **Next**.

If you're missing any required roles or APIs, the **Missing permissions** page opens. It lists the recommended IAM permissions for each selected service and the APIs that must be enabled.

  5. To get any missing permissions that you need to use Data Agent Kit, click **Email list** to send the list to your administrator, or click **Copy list**. Ask your administrator to grant you the corresponding IAM roles on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Configure BigQuery region

  1. To open the Data Cloud Settings editor, click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Select **BigQuery**.
  4. Select a BigQuery region.
  5. Click **Save**.



## View Serverless Runtimes for Apache Spark

  1. To open the Data Cloud Settings editor, click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Select **Apache Spark**. All serverless runtimes for your project are displayed.
  4. To view a serverless runtime configuration, click its name.



## Create a Serverless Runtime for Apache Spark

  1. To open the Data Cloud Settings editor, click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Select **Apache Spark**.
  4. Click **Create**.
  5. Fill in the fields and then click **Save**.



## Delete a Serverless Runtime for Apache Spark

  1. To open the Data Cloud Settings editor, click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Select **Apache Spark**.
  4. For the serverless runtime that you want to delete, click **Delete**.



## Set up Scheduler

  1. To open the Google Cloud Data Agent Kit Settings editor, click the **Google Cloud Data Agent Kit** icon in the activity bar.
  2. Expand **Settings** , and then click **Settings**.
  3. Click **Scheduler**.
  4. Select a project and region. The project and region don't need to match the project and region you selected on the Common tab.
  5. Select a Managed Service for Apache Airflow Environment environment to set up workflows.
  6. Click **Save**.



## Install dependencies

Some Google Cloud Data Agent Kit operations require you to install additional software after you've installed the extension. In some cases, you are prompted to consent to automatic installation. In other cases you must manually install the software.

### Orchestration Pipelines

To work with Orchestration Pipelines in your IDE, install the following:

  * [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation?version=1.12)
  * [Dataform CLI](https://docs.cloud.google.com/dataform/docs/use-dataform-cli)



### Notebooks

Notebooks that Google Cloud Data Agent Kit generates include a commented-out `%pip install --upgrade bigframes` cell. If BigQuery DataFrames isn't installed in your kernel, uncomment and run that cell before you run the rest of the notebook.

To allow the agent to execute code cells in your notebooks, you can enable the `google.datacloud.executeCellToolForNotebookMCP` setting in your IDE settings. This setting enables the `execute_cell` tool for the Notebook Model Context Protocol (MCP).

**Important:** Allowing the agent to execute code cells in your notebooks is a powerful capability and should be enabled with caution. You must restart the IDE after changing this setting.

## Troubleshoot

If you run into issues, try signing out of Google Cloud Data Agent Kit and the gcloud CLI and then signing in again. To find additional methods for diagnosing and resolving configuration errors, see [Troubleshoot Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/troubleshooting).

## Report an issue

To report an issue, do the following:

  1. In the Google Cloud Data Agent Kit menu in the activity bar, click **Report bug**.
  2. In the form that opens, document the issue and click **Submit**.



## What's next

  * [Transform data using Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/transform-data)
  * [Mitigate prompt injection risks](https://docs.cloud.google.com/data-agent-kit/prompt-injection-risk)
  * [Try a codelab that uses Data Agent Kit](https://codelabs.developers.google.com/next26/gen-keynote/raw-data-forecasting#0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
