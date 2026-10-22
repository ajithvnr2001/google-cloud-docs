---
url: https://docs.cloud.google.com/gemini/enterprise/docs/cloud-logging/
title: Access Gemini Enterprise connector error logs with Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:38.907906+00:00
---

# Access Gemini Enterprise connector error logs with Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/cloud-logging/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Access Gemini Enterprise connector error logs with Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise provides Cloud Logging for customers to monitor errors and warnings when connecting their data with Gemini Enterprise.

This document describes how to access federated connector error logs and ingestion connector error logs for Gemini Enterprise using Cloud Logging.

## Key concepts

This section introduces key concepts related to observability in Gemini Enterprise.

Concept | Description  
---|---  
Gemini Enterprise connector error logs  |  Gemini Enterprise connector error logs capture errors and failures encountered when integrating Gemini Enterprise with third-party data sources like Jira and Microsoft OneDrive. These logs include connection problems, data transformation issues, and API errors.   
  
## Before you begin

Before accessing the error logs, ensure that you have done the following:

  * To turn on logging, you must have the [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role (`roles/discoveryengine.agentspaceAdmin`).

  * To access Cloud Logging, you must have the [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) IAM role (`roles/logging.viewer`).

  * Created a Gemini Enterprise app. To create one, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * Ensured your data stores are correctly configured and active. For more information on setting up data stores, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store) or [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

  * Turned on the observability settings to see the federated connector error logs. For more information, see [Turn on observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings#turn_on_observability_settings).




## Access federated connector error logs

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.

To view the error logs of your data stores that connect to Gemini Enterprise using data federation, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data Stores**.

  3. Select a data store of your choice.

  4. Click **View Logs**. This opens the **Logs Explorer** page.

  5. To only see Gemini Enterprise connector logs, enter the following query in the query editor field, and click **Run Query** :
         
         logName="projects/PROJECT_ID/logs/discoveryengine.googleapis.com%2Fconnector_activity"
          jsonPayload.logMetadata.name="projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `LOCATION`: the location of your connector. For example, `global`.
     * `COLLECTION_ID`: the ID of the collection that contains your connector, which is also the ID of the data store in the Google Cloud console.
  6. Refine your query scope by using a filter. For example, click **All severities** , and select **Error and higher**. For more information on refining your queries, see [Sample queries](https://docs.cloud.google.com/logging/docs/view/query-library).




## Access ingestion connector error logs

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.

To view the error logs of your data stores that connect to Gemini Enterprise using data ingestion, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data stores**.

  3. Select a data store of your choice.

  4. Click **View Logs**. This opens the **Logs Explorer** page.

  5. By default, the Logs Explorer page searches the resources listed in the default [log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage) for log entries. To filter to Gemini Enterprise logs, do one of the following:

     * Select **All Resources > Consumed API > Discovery Engine API**, and then click **Apply**.
     * Enter the following into the query bar, and click **Run Query** :
           
           resource.type="consumed_api"
           resource.labels.service="discoveryengine.googleapis.com"
           

  6. Refine your query scope by filtering on JSON metadata. For example, to query `ImportDocuments` method logs, do one of the following:

     * Enter the following into the query bar:
           
           jsonPayload.context.reportLocation.functionName=~"ImportDocuments"
           

     * Expand the JSON metadata, and click to filter:

![Filter by clicking on JSON metadata](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/filter-json-metadata.png)**Figure 1.** Filter by clicking on JSON metadata
  7. For most warnings and errors, find details in `jsonPayload.message` and `jsonPayload.status`.

  8. For deeper log analysis, dump the logs to a log sink such as BigQuery. For information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) in the Google Cloud Observability documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
