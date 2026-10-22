---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/ingest-user-events-overview/
title: User events ingestion starter guide \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:18.289098+00:00
---

# User events ingestion starter guide  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/ingest-user-events-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  User events ingestion starter guide Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance and general best practices for ingesting user events. View the tutorials to get started.

## Before you begin

  * Verify that the data is completely imported from Google Analytics 4 to BigQuery.
  * [Check the import status in the console](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#view), and refer to [Set up an alert for user event recording reduction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor#alert-user-events) for troubleshooting.
  * Before importing historical user event data, review [Best practices for recording user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events#bps) and the [Before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#byb) section on this page.
  * Importing [historical catalog data](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#historical-catalog-data) can further enhance user events and improve model accuracy.

**Caution:** Use a secure form of a unique identifier to keep users anonymous to AI Commerce Search and protect your users' privacy. You are responsible for redacting PII (personally identifiable information), such as email or home addresses, from your data. 

## Tutorials

These tutorials show you how to import user events from various sources.

### Import events from Cloud Storage

This tutorial shows how to import user events from Cloud Storage.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_user_events_gcs_select_language&show=ide&environment_deployment=ide)

* * *

### Import events from BigQuery

This tutorial shows how to import user events from BigQuery.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_user_events_big_query_table_select_language&show=ide&environment_deployment=ide)

* * *

### Import events inline

This tutorial shows how to import user events data inline.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_user_events_inline_source_select_language&show=ide&environment_deployment=ide)

* * *

AI Commerce Search's data ingestion pipeline encompasses both product catalog and user event data. This data stream provides the foundation for model training and continuous evaluation through feedback mechanisms. Accurate and complete data ingestion is an ongoing process for maintaining the adaptability of the underlying models, directly influencing search result quality and relevance.

## User event ingestion general best practices

Consider these data ingestion best practices when architecting your search solution to maximize efficiency and effectiveness.

**Note:** The following content is not referring to [historic events ingestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events).

### Ingest user events in AI Commerce Search

Mirroring the catalog ingestion process, AI Commerce Search offers dual mechanisms for user event data. Bulk import and real-time streaming provide flexibility for diverse customer backend architectures. Unlike the catalog, though, where a hybrid approach is feasible, a dedicated ingestion strategy is better for user events. Of the two options, real-time streaming is standard in practical implementations.

Both yield comparable outcomes in model training, KPI measurement, and revenue optimization, but subtle trade-offs exist. Bulk import, for example, might be more efficient for processing volumes of historical data, while streaming is more responsive to users.

The choice depends on your retail environment requirements, such as: 

  * The latency target for incorporating user events into model training. 
  * The volume of events being generated.



### Scale user event ingestion in AI Commerce Search

Prepare for traffic surges and ensure data integrity by proactively planning for scaling scenarios. High-traffic special events like weekend sales can trigger a 10 to 20 times surge in user activity. Sufficient quotas and the scalability of your ingestion system to handle such spikes is crucial. 

These events often manifest as sudden bursts of traffic, not gradual increases. Missing events during these peak periods can hamper model training, degrade search performance, and skew KPI measurements. Debugging issues can be challenging, because events form the basis for KPI tracking and general troubleshooting. Implementing robust alerting can notify you of deteriorating data quality, which is often a consequence of missing or erroneous event data.

By anticipating these scenarios and taking action, you maintain the reliability and accuracy of your user event data, even under extreme load conditions. Accurate data lays the groundwork for your AI Commerce Search system to deliver optimized performance, accurate analytics, and a user-centered experience during peak traffic.

## Reference architecture for batch events ingestion

![Reference architecture for batch events ingestion](https://d2yds90mtvelsl.cloudfront.net/original/3X/b/4/b4ffc762bb2ef942c155e172ca23d908a9e3640e.png)![](https://d2yds90mtvelsl.cloudfront.net/original/3X/b/4/b4ffc762bb2ef942c155e172ca23d908a9e3640e.png)

Batch ingestion requires a scalable architecture designed for the efficient ingestion of user events into AI Commerce Search. The architecture is composed of Google Cloud services, including Pub/Sub, Dataflow, BigQuery, Workflows, and Cloud Storage, to manage the ingestion process in a staged, controlled manner.

### Architectural overview

Batch events ingestion architecture employs a multi-stage approach to ensure the reliable and accurate transfer of user event data into AI Commerce Search.

Key components include:

  * **Pub/Sub** : Acts as the initial entry point for user events, providing a scalable and durable messaging system.
  * **Dataflow (streaming events)** : Continuously reads raw user events from Pub/Sub and writes them into BigQuery raw event tables, also capturing any failed events for debugging.
  * **BigQuery** : Serves as the primary data warehousing solution, storing raw events, transformed events, and various metadata related to the ingestion process.
  * **Workflows** : Orchestrates the hourly batch processing of raw events, ensuring data integrity and facilitating error handling.
  * **Cloud Storage** : Provides temporary storage for Dataflow during processing and for archiving failed event logs.
  * **AI Commerce Search** : The final destination for user event data, enabling advanced search and recommendation capabilities.



### Step-by-step data flow

This is the step-by-step data flow for bulk events ingestion.

  1. Event streaming and raw data persistence:

     * User events are published to Pub/Sub topics from the customer source system.
     * A Dataflow streaming pipeline (streaming events) continuously reads events from Pub/Sub.
     * Successful raw events are written into BigQuery raw event tables.
     * Any failures during this initial ingestion are captured and stored in separate BigQuery raw failed tables for analysis and troubleshooting.
  2. Hourly batch processing and transformation:

     * Workflows triggers an hourly scheduled Dataflow pipeline (Incr Batch Events).
     * This pipeline reads raw events from BigQuery tables.
     * Events are transformed into the required AI Commerce Search format.
     * Transformed events are written into BigQuery curated event tables.
     * Any transformation failures are captured in BigQuery curated failed event tables.
  3. Data validation and preparation:

     * Workflows executes a BigQuery stored procedure to create or update a view (Incr Update Event View) that reflects the latest transformed event data from the last hour.
     * The workflow then performs a validation check on this view, ensuring that the number of transformed events falls within predefined thresholds.
  4. AI Commerce Search import:

     * If the validation is successful, Workflows invokes the AI Commerce Search import event API, pointing it to the BigQuery view containing the transformed events.
     * AI Commerce Search then imports these events for further processing and indexing.



### Additional considerations for batch events ingestion

Additional aspects to consider when ingesting batch events are:

  * **Security** : Appropriate security measures, such as access controls and encryption, should be implemented to protect sensitive user event data.
  * **Monitoring and logging** : Comprehensive monitoring and logging should be set up to track the performance of the system and identify potential issues proactively.
  * **Cost optimization** : Resource utilization should be monitored to optimize costs and ensure efficient use of Google Cloud services.



This architecture provides a foundation for ingesting user events into AI Commerce Search. Using various Google Cloud services and incorporating best practices for data processing and error handling, it enables organizations to build scalable, maintainable solutions for advanced search and recommendation experiences.

## What's next

  * To understand how user events generally work, refer to [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events).

  * For more in-depth instructions for each ingestion method, refer to the pages on [bulk import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events) and [real-time events streaming](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
