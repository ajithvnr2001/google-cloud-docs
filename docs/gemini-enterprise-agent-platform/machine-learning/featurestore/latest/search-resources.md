---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/search-resources/
title: Search for Vertex AI Feature Store resources \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:40.782987+00:00
---

# Search for Vertex AI Feature Store resources  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/search-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Search for Vertex AI Feature Store resources Stay organized with collections  Save and categorize content based on your preferences. 

You can use the advanced search in Vertex AI Feature Store to search for online store instances, feature views, and features.

The following resources are included in the search results:

  * Vertex AI Feature Store resources on which you have the read permissions.

  * Feature views that are associated with feature groups and features, and aren't directly associated with the BigQuery data source. The metadata for these feature views aren't managed in Knowledge Catalog and aren't included in the search results.




## Before you begin

Before you use the advanced search in Vertex AI Feature Store, you must complete the following steps:

  1. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  2. Ensure that you have the following IAM permissions in the project:  
`dataplex.projects.search`  
Note that you don't need this permission in all the projects that you want to include within the scope of your search.



## Search for resources

To search for a Vertex AI Feature Store resource, follow these steps:

### Console

  1. Go to the **Advanced search** page.

[Go to Advanced search](https://console.cloud.google.com/vertex-ai/feature-store/advanced-search)

  2. Enter the following search parameters:

     * **Keyword** : Optional. Enter the search keywords to search based on the resource name or metadata.

     * **Resource type** : Click the type of resource to search for. The available options include the following:

       * **All** —Include online stores, feature views, and feature groups in the search results.

       * **Online store** —Include only online store instances in the search results. You can optionally select a **Storage type** to filter the search results based on the type of online serving.

       * **Feature view** —Include only feature views in the search results. You can optionally provide a **Feature name** to filter the search results to include feature views associated with the feature name.

       * **Feature group** —Include only feature groups in the search results. You can optionally provide a **Feature name** to filter the search results based on the names of the features within the feature groups.

     * **Search all projects** : To search for resources in all Google Cloud projects, select this check box. To search for resources only in the project that you have selected, clear the check box.

  3. Click **Search**.

To view the metadata for a resource in Knowledge Catalog, click the resource name in the search results, and then click **View in Dataplex**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
