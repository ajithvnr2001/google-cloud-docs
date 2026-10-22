---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-field-settings/
title: Configure field settings \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:36.816500+00:00
---

# Configure field settings  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-field-settings/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure field settings Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure the fields to set up an app for structured data or for unstructured data with metadata.

Field settings help determine how Gemini Enterprise uses fields in its results. You can use the **Schema** tab in the Google Cloud console to configure field settings for structured data and unstructured data with metadata.

Configuring field settings is available only for apps with data stores that have either structured data or unstructured data with metadata.

The following field settings are available:

Field setting | Definition | Use case  
---|---|---  
Indexable | If a field is set to **Indexable** , Gemini Enterprise can filter, order, and facet using this field. Setting boolean and object fields to indexable is not supported. | Search  
Searchable | If a field is set to **Searchable** , recall for that field in Gemini Enterprise queries is improved. Only fields with text values can be set to **Searchable**.  
| Search  
Dynamic facetable | If a field is set to **Dynamic Facetable** , Gemini Enterprise can use that field as a dynamic facet. Dynamic facets can be automatically added to a search based on previous user behavior such as facet clicks and views. This setting is applicable only to fields that are indexable. | Search  
Retrievable | If a field is set to **Retrievable** , Gemini Enterprise returns the field in search results. | Search  
Completable | If a field is set to **Completable** , Gemini Enterprise uses the field's contents as search query suggestions. For more information, see [Configure autocomplete](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete). | Search  
  
## Limitations

Field settings have the following limitations:

  * You can configure up to 50 fields as indexable, searchable, retrievable, or dynamic facetable.
  * To configure a field as dynamic facetable, it must first be configured as indexable.
  * Changing the indexable setting requires re-indexing the data, which can take hours, especially for large data stores.



## Update field settings

To update field settings:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click the name of the app that you want to edit.

  3. Click **Data**.

  4. Click the **Schema** tab. This tab shows current field settings.

  5. Click **Edit**.

  6. Select or clear field settings that you need to update. Some field settings are not supported. For example, numerical fields cannot be set to **Searchable**.

  7. Click **Save** to apply your changes.




## What's next

  * [Update a schema for structured data](https://docs.cloud.google.com/gemini/enterprise/docs/update-schemas)
  * [Configure results for the UI](https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-results)
  * [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
