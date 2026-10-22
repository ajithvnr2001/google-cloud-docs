---
url: https://docs.cloud.google.com/cortex/docs/v6/overview/
title: Overview \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:30.753112+00:00
---

# Overview  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview

Google Cloud Cortex Framework provides reference architectures, deployable solutions, and packaged implementation services to kickstart your [Data and AI Cloud](https://docs.cloud.google.com/data-cloud) journey. Everything you need to rapidly design, build, and deploy data and AI solutions for your business.

Cortex Framework focuses on solving specific problems and offers pre built solutions for business areas like Marketing, Sales, Supply Chain, Manufacturing, Finance, and Sustainability. For more information, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).

### Google Cloud integration

Cortex Framework builds on top of Google Cloud tools to provide a unified environment for managing your entire data journey. The following diagram describes how Cortex Framework uses various components to provide a unified platform for storing, managing, and analyzing data from diverse data sources:

[ ![Google Cloud Cortex Framework components to provide a unified platform to extract, transform and analyze data](https://docs.cloud.google.com/cortex/docs/images/cortex_architecture.png)](https://docs.cloud.google.com/cortex/docs/images/cortex_architecture.png)

**Figure 1**. Google Cloud Cortex Framework Technical Stack.

Multiple tools are responsible for extracting, transforming, and loading (ETL) data from various sources into the database for later visualization and analysis. Depending on the needs of your business, you can use some of the following:

  * **Data Storage**
    * [Cloud Storage](https://docs.cloud.google.com/storage/docs): for storing data from other data sources.
    * [BigQuery](https://docs.cloud.google.com/bigquery/docs): serverless, managed data warehouse for storing and analyzing large datasets. Cortex Framework uses BigQuery for storing raw, transformed, and reporting data.
    * [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview): secure storage service for sensitive information like passwords, API keys, and certificates. Cortex Framework uses Secret Manager to protect your sensitive data and ensure its responsible use within your data and AI projects.
  * **Data Integration and Processing**
    * [Cloud Build](https://docs.cloud.google.com/build/docs/overview): service that automates building, testing, and deploying your software. Cortex Framework uses Cloud Build for customizing and deploying pre built solutions.
    * [Dataflow](https://docs.cloud.google.com/dataflow/docs): managed service for building and running data pipelines. Cortex Framework uses Dataflow to automate certain data ingestion, transformation, and loading tasks.
    * [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs): managed orchestration service for workflows. Cortex Framework uses Managed Service for Apache Airflow to manage and schedule complex data pipelines.
  * **Data Transformation and Analysis**
    * [BigQuery](https://docs.cloud.google.com/bigquery/docs): serverless environment for building and deploying datasets within BigQuery. Cortex Framework uses BigQuery for data transformations.
    * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs): managed Hadoop and Spark service for large-scale data processing. While less common for Cortex Framework's pre built solutions, Managed Service for Apache Spark could be used for custom data processing needs.
    * [Looker](https://docs.cloud.google.com/looker/docs): business intelligence platform for data exploration and visualization. Cortex Framework integrates with Looker to provide user-friendly dashboards and reports.
  * **ML and AI**
    * [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs): unified platform for building, training, deploying, and managing models. Cortex Framework might use prebuilt Vertex AI components within its solutions.



## Data Foundation

The Cortex Framework Data Foundation defines the structure and organization of the data to ensure consistency and facilitate data analysis across different applications. Cortex Framework simplifies data management, streamlines development, and offers prebuilt solutions for various business domains through its Data Foundation. Data Foundation incorporates tools and services that help ingest, transform, and load data.

Marketing, operations, and sustainability are all business areas that can be benefited from Cortex Framework. It includes predefined workloads that can be used to collect, analyze, and use data. Data can come from various data sources such as Salesforce Marketing Cloud, some Google platforms (like Google Ads and CM360), TikTok, Meta, SAP, and more. For more information, see the [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).

## Deployment

For Cortex Framework deployment instructions, see the following guides:

  * **Demo deployment** : a [quickstart demo](https://docs.cloud.google.com/cortex/docs/v6/quickstart-demo) to test the Cortex Framework set up process with sample data with in just a few clicks.
  * **Deployment steps** : after reading the [prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites) for Cortex Framework Data Foundation deployment, follow the steps for deployment in production environments: 
    1. [Establish workloads](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one).
    2. [Clone repository](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-two).
    3. [Determine integration mechanism](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three).
    4. [Set up components](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-four).
    5. [Configure deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five).
    6. [Execute deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six).



## Support

In case of any requests or issues, you can reach out directly to the Cortex Framework team by creating a new ticket in our support channel:

  1. Go to our [support channel](https://issuetracker.google.com/issues/new?component=1702583) to create a new support case.
  2. _Optional_ : Add the email addresses of people that should also receive updates.
  3. Submit the ticket to our team by clicking **Create**.



For all other questions, contact the [Cortex Framework team](mailto:cortex-support@google.com).

For more information about our support channel, take a look at the available resources:

  * [User's guide](https://developers.google.com/issue-tracker)
  * [FAQ](https://developers.google.com/issue-tracker/references/faq)
  * [Terms of Service](https://developers.google.com/issue-tracker/#terms_of_service)



## What's next?

  * See [Cortex Framework Data Foundation](https://github.com/GoogleCloudPlatform/cortex-data-foundation) repository in GitHub.
  * For information about data sources and workloads available in Cortex Framework, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
