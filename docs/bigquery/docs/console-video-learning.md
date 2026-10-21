---
url: https://docs.cloud.google.com/bigquery/docs/console-video-learning/
title: BigQuery interactive walkthroughs and videos \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:39:36.013295+00:00
---

# BigQuery interactive walkthroughs and videos  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/console-video-learning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BigQuery interactive walkthroughs and videos

This document lists the interactive walkthroughs and video tutorials available to help you learn about and get started with BigQuery. These resources provide guided, step-by-step instruction for common tasks and visual explanations of concepts and features.

## BigQuery interactive walkthroughs

The following guided walkthroughs lead you through common tasks directly in the Google Cloud console. Click a link to launch a walkthrough.

### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. Enable the BigQuery API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery)

For new projects, the BigQuery API is automatically enabled.

  5. Optional: [Enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project) for the project. If you don't want to enable billing or provide a credit card, the steps in this document still work. BigQuery provides you a sandbox to perform the steps. For more information, see [Enable the BigQuery sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox#setup). **Note:** If your project has a billing account and you want to use the BigQuery sandbox, then [disable billing for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project). 



These walkthroughs are launched in the Google Cloud console. Click the links to launch the interactive tutorial.

Title | Description  
---|---  
**Loading and querying data** |  |   
[Query a public dataset in BigQuery Studio](https://console.cloud.google.com/welcome?walkthrough_id=bigquery--bigquery-quickstart-query-public-dataset) | Use the BigQuery sandbox to query and visualize data in a public dataset.  
[Load and query data using BigQuery Studio](https://console.cloud.google.com/welcome?walkthrough_id=bigquery--bigquery-quickstart-load-data-console) | Use BigQuery Studio to create a dataset, load data, and query the data.  
[Load and query data with the `bq` command-line tool](https://console.cloud.google.com/welcome?walkthrough_id=bigquery--load-data-bq) | Use the BigQuery command-line tool to create a dataset, load data, and query the data.  
[Import data from Cloud Storage to BigQuery](https://console.cloud.google.com/welcome?tutorial=bigquery_import_data_from_cloud_storage) | Use the Google Cloud console to import data from Cloud Storage into BigQuery, and query the data.  
**Workload management** |  |   
[Get started with reservations](https://console.cloud.google.com/welcome?walkthrough_id=bigquery--reservations-get-started) | Use the Google Cloud console to purchase slots, create a reservation, and assign a project to a reservation.  
**AI** |  |   
[Run generative AI in SQL with `AI.GENERATE`](https://console.cloud.google.com/bigquery?walkthrough_id=bigquery--ai-generate-quickstart) | Use Gemini and the `AI.GENERATE` function in BigQuery to summarize text and extract structured insights.  
[Time series forecasting with TimesFM and `AI.FORECAST`](https://console.cloud.google.com/bigquery?walkthrough_id=bigquery--timesfm-quickstart) | Use Google's pre-trained TimesFM foundation model and the `AI.FORECAST` function in BigQuery to forecast time series data without model training.  
[Zero-shot tabular predictions with TabFM and `AI.PREDICT`](https://console.cloud.google.com/bigquery?walkthrough_id=bigquery--tabfm-quickstart) | Use Google's pre-trained TabFM foundation model and the `AI.PREDICT` function in BigQuery to predict tabular outcomes without model training.  
[Classify data with `AI.CLASSIFY`](https://console.cloud.google.com/bigquery?walkthrough_id=bigquery--ai-classify-quickstart) | Use Gemini and the `AI.CLASSIFY` function in BigQuery to categorize unstructured text and data into predefined categories.  
[Write queries with Gemini assistance](https://console.cloud.google.com/bigquery?walkthrough_id=bigquery--write-sql-gemini) | Use Gemini AI-powered assistance in BigQuery to help you query your data using SQL queries and Python code.  
**Client libraries** |  |   
[C# tour](https://console.cloud.google.com/?walkthrough_id=bigquery--csharp-client-library) | Query a public dataset with the BigQuery C# client library.  
[Go tour](https://console.cloud.google.com/?walkthrough_id=bigquery--go-client-library) | Query a public dataset with the BigQuery Go client library.  
[Java tour](https://console.cloud.google.com/?walkthrough_id=bigquery--java-client-library) | Query a public dataset with the BigQuery Java client library.  
[Node.js tour](https://console.cloud.google.com/?walkthrough_id=bigquery--node-client-library) | Query a public dataset with the BigQuery Node.js client library.  
[PHP tour](https://console.cloud.google.com/?walkthrough_id=bigquery--php-client-library) | Query a public dataset with the BigQuery PHP client library.  
[Python tour](https://console.cloud.google.com/?walkthrough_id=bigquery--python-client-library) | Query a public dataset with the BigQuery Python client library.  
[Ruby tour](https://console.cloud.google.com/?walkthrough_id=bigquery--ruby-client-library) | Query a public dataset with the BigQuery Ruby client library.  
  
## BigQuery videos

The following series of video tutorials help you learn more about BigQuery. For more Google Cloud videos, subscribe to the [Google Cloud Tech](https://goo.gle/GoogleCloudTech) YouTube channel.

Title | Description  
---|---  
**Product overviews** |  |   
[ BigQuery in a minute](https://www.youtube.com/watch?v=CFw4peH2UwU) (1:26) | A brief overview of BigQuery, Google's fully-managed data warehouse.  
[BigQuery ML in a minute](https://www.youtube.com/watch?v=0RMT8uEplbM) (1:40) | A brief overview of BigQuery ML. With BigQuery ML, you can train, evaluate, and run inference on models for tasks such as time series forecasting, anomaly detection, classification, regression, clustering, dimensionality reduction, and recommendations.  
**AI** |  |   
[Introduction to Gemini AI and data analytics in BigQuery](https://www.youtube.com/watch?v=-MWIHAH4cbA) (3:42) | An introduction to Gemini in BigQuery, which provides AI and data analytics capabilities that help streamline your workflows across the entire data lifecycle.  
[Use BigQuery & Gemini AI for data analytics ](https://www.youtube.com/watch?v=qrT4g0hZHns) (7:00) | An overview of how Gemini models can help you generate new insights, enrich your datasets, and even analyze multimodal content including images, videos, and text.  
[Introducing BigQuery data engineering agents](https://www.youtube.com/watch?v=SqjGq275d0M) (6:19) | An introduction to BigQuery Data Engineering Agents that help data analysts save time coding, schema mapping, and creating metadata.  
[BigQuery data canvas overview](https://www.youtube.com/watch?v=r_nDZSrWaYk) (6:03) | An overview of AI-powered BigQuery data canvas. This natural language centric tool simplifies the process of finding, querying, and visualizing your data.  
**Querying and visualizing data** |  |   
[Introducing pipe syntax in BigQuery and Cloud Logging](https://www.youtube.com/watch?v=mW2CLYr6w4M) (5:00) | BigQuery's pipe syntax offers a more intuitive way to structure your code. Learn how pipe syntax simplifies both exploratory analysis and complex log analytics tasks, helping you gain insights faster.  
[Visualizing BigQuery geospatial data in Colab](https://www.youtube.com/watch?v=t_q-qLa1lX0) (10:00) | BigQuery lets you store and analyze geospatial data using standard SQL, and bringing that data into a Colab notebook gives you the flexibility to combine BigQuery's power with popular Python visualization libraries.  
[Visualize BigQuery data with Looker](https://www.youtube.com/watch?v=Q2JD3_YBaRc) (3:00) | An overview of how to seamlessly connect to and visualize your BigQuery data using Looker's user-friendly interface and powerful semantic modeling capabilities.  
**BigQuery storage** |  |   
[A tour of BigQuery tables](https://www.youtube.com/watch?v=V2QTtHJXVZY) (6:55) | An overview of the different types of tables in BigQuery, including managed tables, external tables, and virtual tables with logical and materialized views.  
[How does BigQuery store data?](https://www.youtube.com/watch?v=0Hd23GnZ1bE) (8:19) | An introduction to how BigQuery stores data so you can make informed decisions on how to optimize your BigQuery storage. This includes an overview of partitioning and clustering.  
**Monitoring and logging** |  |   
[Monitoring in BigQuery](https://www.youtube.com/watch?v=UY_jy02jBoI) (7:43) | An overview of how monitoring your data warehouse can optimize costs, help you pinpoint which queries need to be optimized, and audit both data sharing and access.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
