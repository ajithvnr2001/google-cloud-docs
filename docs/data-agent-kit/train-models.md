---
url: https://docs.cloud.google.com/data-agent-kit/train-models/
title: Train AI and ML models \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:48.466628+00:00
---

# Train AI and ML models  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/train-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Train AI and ML models Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to train AI and ML models in the Google Cloud Data Agent Kit.

In this quickstart, you use a session template and a sample Jupyter notebook to predict New York City taxi tip amounts. Using a remote Jupyter kernel with PySpark, you try out various models like linear regression, random forest, and XGBoost. This process lets you perform distributed training and inference. It demonstrates scalability across multiple machines using Spark ML and the XGBoost library.

Although not covered in this quickstart, there are multiple ways to train AI and ML models using Google Cloud Data Agent Kit:

  * If your training dataset is large or you want the distributed training capabilities that Apache Spark offers, you can use Spark notebooks with remote kernels.
  * If your dataset is in BigQuery and BigQuery ML supports your use case, you can use a BigQuery DataFrames notebook.
  * If your dataset is small and you want to train your model locally, you can use a Python notebook.

**Note:** This quickstart uses the Data Agent Kit extension, but you can accomplish the same tasks with natural language prompts using the Data Agent Kit plugin with a supported coding agent or CLI.

## Before you begin

Before you begin, do the following:

  1. [Install the extension](https://docs.cloud.google.com/data-agent-kit/install).
  2. [Configure extension settings](https://docs.cloud.google.com/data-agent-kit/configure).
  3. Review the guidance at [Find and explore data](https://docs.cloud.google.com/data-agent-kit/find-explore-data).



## Create a Spark runtime template

Serverless Spark Runtime templates let you start an Apache Spark session with a given set of configurations. To create a new Serverless Runtime template, complete the following steps:

  1. In the IDE activity bar, click the **Google Cloud Data Agent Kit** icon.
  2. In the Google Cloud Data Agent Kit menu, expand **Apache Spark**.
  3. Expand **Serverless** and then click **New Runtime**. A Serverless Runtime creation form appears.
  4. In the **Display Name** field, enter `ai-ml-tutorial`.
  5. Go to the **Auto Scaling** section.
  6. Set `spark.dynamicAllocation.enabled` to false in the drop-down list. This setting is needed for XGBoost to work with Apache Spark.
  7. Leave all other fields set to the default.
  8. Click **Submit**.



## Create a new notebook

**Note:** In this quickstart, you use a prebuilt sample notebook. You can also use the agent in your IDE to generate a Spark notebook with a prompt that describes your specific ML use case.

Next, create a new Spark notebook:

  1. Under **Apache Spark** in the Google Cloud Data Agent Kit tab, click **\+ New Spark Notebook**.
  2. Choose **Remote Kernel** for the kernel type.
  3. Click **Start with a sample notebook**.
  4. In the list of samples, select **Data Science with PySpark and Distributed XGBoost**. An untitled Jupyter notebook appears.



## Train your model

  1. In the notebook tab, click **Run All**. The kernel picker asks you to select a kernel to execute the notebook with.
  2. Click **Select Another Kernel**.
  3. Click **Remote Spark Kernels**.
  4. Select the **ai-ml-tutorial on Serverless Spark** , the Runtime template that you created earlier.

**Note:** On Windows, Long Path support must be enabled to work with Spark Notebooks on Remote Kernels.

You see the following notification while the system creates your Serverless Spark session: `Connecting to kernel: ai-ml-tutorial on Serverless Spark`. When the notebook connects to the remote PySpark kernel, execution starts at the first cell. This process takes approximately two to three minutes.

**Key Point:** Managed Service for Apache Spark executes your training code. The system doesn't download any part of your training dataset to your local machine.

## Inspect your Spark session

  1. In the Google Cloud Data Agent Kit tab, under Apache Spark, expand the **ai-ml-tutorial** Runtime template. The IDE displays the list of interactive sessions that you have created with this runtime template.
  2. Locate the session that the system created by executing the notebook at the top of the list. Click the session to see its details. You can review the session configuration and the resources that the system consumed to execute your notebook.



## Clean up

After successfully executing the notebook, perform the following cleanup steps.

  1. In the Google Cloud Data Agent Kit tab, under Apache Spark, right-click **Serverless** and select **List Serverless Runtimes**. The list of Serverless Runtimes appears.
  2. Click the **Action** menu for `ai-ml-tutorial` to list all the Interactive Sessions that the system created from your template.
  3. Click **Delete**.
  4. Go back to the Serverless Runtimes window.
  5. For `ai-ml-tutorial`, click **Delete**.
  6. Click **Confirm** to delete the template that you created for this tutorial.



## What's next

  * [Managed Service for Apache Spark overview](https://docs.cloud.google.com/dataproc/docs/concepts/overview)
  * [Transform data](https://docs.cloud.google.com/data-agent-kit/transform-data)
  * [Codelab: Analytics with the Data Agent Kit and Antigravity](https://codelabs.developers.google.com/dak-analytics-eng-antigravity-ide#0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
