---
url: https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist/
title: Analyze your stored data with Gemini Cloud Assist \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:57.967707+00:00
---

# Analyze your stored data with Gemini Cloud Assist  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Analyze your stored data with Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use AI-powered assistance through Gemini to help you better understand your data storage landscape in Cloud Storage. When you use Gemini Cloud Assist, you can enter prompts about how Cloud Storage works in general, and when you enable a Storage Intelligence subscription, you can enter prompts about specific buckets and objects.

You can then use the information provided by Gemini Cloud Assist to do the following:

  * Analyze data usage patterns and trends

  * Identify opportunities to save on storage costs

  * Optimize your data for security and compliance

  * Make informed decisions on managing your data




Gemini doesn't use your prompts or its responses as data to train its models without your express permission. For more information about how Google uses your data, see [How Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This page is intended for developers, data analysts or data engineers, platform admins, finance operators, and compliance officers. It assumes that you know how to use Cloud Storage and query [linked datasets](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets).

## What prompts can Gemini answer?

To understand your data storage, you can provide Gemini Cloud Assist with a _prompt_ , which is a natural language statement or question.

When you use Gemini Cloud Assist alone without a Storage Intelligence subscription, you can ask prompts about how Cloud Storage generally works, such as the following:

  * "How do I transition objects from one storage class to another?"

  * "How do I enable soft delete on a bucket?"




When you enable a [Storage Intelligence subscription](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview), you can also ask prompts related to cost saving opportunities, security and compliance, and data discovery. Gemini Cloud Assist can use the metadata contained in [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) to generate _insights_ , which are responses to prompts about your bucket and object metadata and usage. You can ask prompts such as the following:

  * Prompts related to usage and cost savings:

    * "5 largest buckets without Object Lifecycle Management"

    * "5 largest buckets without Autoclass enabled"

  * Prompts related to security and compliance:

    * "5 largest buckets without object versioning enabled"

    * "5 largest objects with a retention expiration date within the next 30 days"

  * Prompts related to data discovery:

    * "Buckets with a high volume of small files (each under 1 MB)"

    * "Objects in Standard storage class smaller than 50 MB"




## Before you begin

In order to use Gemini Cloud Assist for general prompts related to Cloud Storage, you must first set up Gemini Cloud Assist, including getting required roles.

### Set up Gemini Cloud Assist

Ensure that [Gemini Cloud Assist is set up for your Google Cloud project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

If you want to enter prompts related to specific buckets and objects, you must also complete the following prerequisite steps:

  1. Enable Storage Intelligence, which gives you access to using Storage Insights datasets.

  2. Create a Storage Insights dataset, which Gemini Cloud Assist will analyze to provide information about specific buckets and objects.

Alternatively, if there's an existing dataset you want to use, you can get the required IAM roles for accessing the existing dataset.

  3. Ensure that the Storage Insights service agent has access to the dataset Gemini Cloud Assist will analyze. This enables the dataset to be read and analyzed.




### Enable Storage Intelligence

Ensure that [Storage Intelligence is enabled](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence) on the project, folder, or organization that contains or will contain the datasets that Gemini Cloud Assist will use to answer prompts.

### Create a dataset

**Note:** If you plan to use an existing dataset, you can skip this step. 

[Create a dataset](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#create) and [link the dataset to BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#link-dataset).

### Grant required roles for accessing datasets

**Note:** If you plan to use an existing dataset, you can skip this step. 

When a user first creates a dataset configuration, an Storage Insights service agent is created. The service agent follows the naming format `service-PROJECT_NUMBER@gcp-sa-storageinsights.iam.gserviceaccount.com` and appears on the [IAM page of the Google Cloud console](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId) when you select the **Include Google-provided role grants** checkbox.

In order to use Gemini Cloud Assist for prompts related to bucket or object metadata, you need to enable the Storage Insights service agent to read datasets. Ask your administrator to grant the service agent the BigQuery Data Viewer role (`roles/bigquery.dataViewer`) on the organization, folder, or project that contains the dataset you want to analyze.

For instructions on granting roles to service agents, see [create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).

### Get required roles for accessing datasets

**Note:** If you created a dataset from scratch, you most likely already have the required permissions and can skip this step. 

To get the permissions that you need to get insights on bucket and object metadata, ask your administrator to grant you the following IAM roles on the project, folder, or organization that contains the datasets you want to analyze: 

  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)
  * [Storage Insights Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storageinsights#storageinsights.viewer) (`roles/storageinsights.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Analyze your data storage by using natural language prompts

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

**Note:** To improve the quality of responses, include `Cloud Storage` in the prompt. For example: `5 largest Cloud Storage buckets without object versioning enabled`.

To enter prompts to Gemini Cloud Assist, follow these steps:

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. In the toolbar, click spark (**Gemini**) to open the **Cloud Assist** chat panel.

The **Cloud Assist** chat panel appears.

  3. In the **Cloud Assist** chat panel, enter a natural language prompt about your data storage. For example, you might enter the following:
         
         Which is my largest bucket

  4. Click play_arrow (**Generate**).

  5. If prompted to, enter the name of the dataset that Gemini will analyze to generate the response, then click play_arrow (**Generate**).

If successful, Gemini Cloud Assist generates a response similar to the following:
         
         Here's what I found by analyzing the data in EXAMPLE_DATASET:
         

Bucket name | Size  
---|---  
my-bucket | 39.1 TB  
  
The underlying SQL query that Gemini Cloud Assist uses is also returned. The generated SQL query is similar to the following:
         
         SELECT bucket_id, bucket_size
         FROM buckets
         WHERE project_id = 'example-project'
         ORDER BY bucket_size DESC
         LIMIT 1;
         




Optionally, you can enter suggested prompts:

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. In the auto_awesome **Suggested prompts** section, select a suggested prompt. For example, a suggested prompt might say: `Storage size broken down by object content type`.

  3. If successful, Gemini Cloud Assist generates a response similar to the following:
         
         Here's what I found by analyzing the data in EXAMPLE_DATASET:
         

Content type | Size  
---|---  
MP4 | 483.2 GB  
MOV | 239.1 GB  
MP3 | 125.8 GB  
  
The underlying SQL query that Gemini Cloud Assist uses is also returned. The generated SQL query is similar to the following:
         
         SELECT
         oa.contentType, ROUND(sum(oa.size) / (1024 * 1024 * 1024), 2) AS total_size_gb
         FROM object_attributes_latest AS oa
         GROUP BY oa.contentType
         ORDER BY sum(oa.size) DESC;




## Data processing quotas

When you run a prompt using Gemini Cloud Assist to get information about your data in Cloud Storage, Gemini Cloud Assist processes your datasets to provide answers to your prompts. If a prompt requires processing less than 800 GB of data to answer, Gemini Cloud Assist returns the underlying SQL query for the prompt and executes the query, returning the response in SQL. If a prompt requires processing 800 GB of data or more to answer, Gemini Cloud Assist only returns the underlying SQL query and doesn't execute the query. You can [run the query by yourself using BigQuery](https://docs.cloud.google.com/bigquery/docs/running-queries).

Gemini Cloud Assist can process up to 50 TiB of data per month, per organization. If your organization surpasses this limit, Gemini Cloud Assist will return the underlying SQL queries for any additional prompts you run but won't execute the queries. Running additional prompts results in a **Monthly Quota Exceeded** response message.

## Limitations

  * When using prompts to analyze Cloud Storage resources, you can specify up to five resources in the prompt. For example: `5 largest buckets without Autoclass enabled`. Even if you include more than five resources in the prompt, Gemini Cloud Assist can only return results for the top five resources that match the prompt's criteria.

  * Gemini Cloud Assist uses the bucket and object metadata contained in Storage Insights datasets to respond to prompts about your data storage.

The following data is not available in Storage Insights datasets, meaning that Gemini Cloud Assist lacks the proper context to respond to prompts relating to that data:

    * Specific cost data, for example: "how much does my bucket cost per month".

    * Activity data, for example: "what is the last access time of my object".

    * Data about the configuration of certain features, such as soft delete. For example: "which buckets don't have soft delete enabled".

Gemini Cloud Assist also lacks the proper context to respond to prompts related to time series information. For example: "how much did my bucket grow in the last 3 weeks". This is because Gemini Cloud Assist only reads a dataset's latest snapshot.




## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/duet-ai/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/gemini/docs/cloud-assist-pane).
  * Read [Use Gemini for AI assistance and development](https://docs.cloud.google.com/duet-ai/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/duet-ai/docs/discover/data-governance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
