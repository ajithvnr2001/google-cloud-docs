---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-hc-search/
title: Filter healthcare search \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:40:12.275143+00:00
---

# Filter healthcare search  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-hc-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Filter healthcare search Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

**Caution:**

  * Restrictions for healthcare: As a customer, you will not, and will not allow End Users to, use the Generative AI Services for clinical purposes (for clarity, non-clinical research, scheduling, or other administrative tasks is not restricted), as a substitute for professional medical advice, or in any manner that is overseen by or requires clearance or approval from any applicable regulatory authority. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms). 

For clarity, with respect to the use of Agent Search to retrieve and summarize existing medical information, the restriction on the use for clinical purposes means the restriction on the use for direct diagnosis or treatment purposes without review by a licensed professional in compliance with applicable laws and regulations. 

  * The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased (for example, stereotypes or other harmful content) information and should be reviewed. All summaries or answers should be considered draft and not final.
  * This product's intended usage is not to provide information pertaining to the prevention, diagnosis or treatment of illness or disease. Questions regarding diagnosis or treatment recommendations are not intended to be addressed by the product. This product's intended use is to retrieve and summarize existing medical information provided by users.
  * Due to limited test data, this product may or may not be applicable to age group 0-18 and to age group 85 and above. Therefore, when reviewing the generated output, customers must consider the representativeness of subpopulations within their source data.



When you're querying healthcare data, you can use filters to refine your search responses. In a search request, you can provide filters to enforce criteria that include or exclude certain search responses.

For example, when you're [searching over a single patient's data](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data), the search request body must contain the following filter expression that specifies the patient ID:
    
    
    "filter": "patient_id: ANY(\"PATIENT_ID\")"
    

This page shows you how to define filters for healthcare search.

## Before you begin

Before you begin, do the following:

  * Create a healthcare search app and a healthcare search data store, and import FHIR R4 data. For more information, see [Create a healthcare search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-hc) and [Create a healthcare search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc).
  * Review the list of FHIR R4 resources that Agent Search supports as indexable, searchable, and retrievable fields. For more information, see [Healthcare FHIR R4 data schema reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference).
  * Understand the [filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax).



## Define filters

Filters are specified in the `filter` field in the request body of the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.servingConfigs/search) method.

The filter definition follows the [filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax). In the filter expression, the literal can be any indexable field from the response to the search query. For example, if the response contains an Observation resource, the `patient_id` that the Observation resource references can be used as a filter literal.

The following sections show a few examples on how to construct filters.

### Define a `resource_datetime` filter

This example shows you how to specify a filter for a search that includes only those resources that have a `resource_datetime` value later than the specified date and time value.

### REST
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/DATA_STORE_ID/servingConfigs/default_search:search" \
        -d '{
    "query": "QUERY",
    "filter": "patient_id: ANY(\"PATIENT_ID\") AND resource_datetime > \"DATE_TIME_VALUE,
    "contentSearchSpec":{"snippetSpec":{"returnSnippet":true}}
    }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `DATA_STORE_ID`: the ID of the Agent Search data store.
  * `QUERY`: the search query.
  * `PATIENT_ID`: the resource ID of the patient whose data you want to search.
  * `DATE_TIME_VALUE`: the value of the `resource_datetime` field that represents a date and time in the FHIR [dateTime](https://build.fhir.org/datatypes.html#dateTime) format. Some examples of this field are as follows: 
    * To specify a date and time with a time zone separated by a `T` separator: `2022-08-05T01:00:00+00:00`
    * To specify a date: `2022-08-05`
    * To specify a month: `2022-08`
    * To specify a year: `2022`



#### Response

You should receive a JSON response similar to the following truncated response. The response contains itemized search results listed in reverse chronological order with snippets, if snippets are available. The `structData` field contains the structured JSON data for the document.
    
    
    {
        "results": [
        {
            "id": "DOCUMENT_ID",
            "document": {
            "name": "projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID",
            "id": "DOCUMENT_ID",
            "structData": {
                ...
                "resource_type": "FHIR_RESOURCE_TYPE",
                "resource_datetime": "RESOURCE_DATETIME",
                "patient_id": "PATIENT_ID",
                "FHIR_RESOURCE_TYPE": { ... }
            },
            "derivedStructData": {
                "snippets": [
                {
                    "snippet": "SNIPPET_TEXT",
                    "snippet_status": "SUCCESS"
                }
                ]
            }
            }
        }]
    }
    

### Define a resource type filter

The following example shows how to construct a filter that uses an `AND` operator to first filter all Composition resources and then filter those whose date is later than a specified date and time.
    
    
    "filter": "resource_type: ANY("Composition") AND Composition.date > "2022-08-05T01:00:00+00:00""

### Define a FHIR resource filter

You can use a filter to check whether a FHIR resource is present in the Agent Search data store. For example, you can search for a DocumentReference resource that has the ID `6112d1ac-c6bd-4755-d689-bfb71d59afc5` using the following filter.
    
    
    "filter": "DocumentReference.id: ANY(\"6112d1ac-c6bd-4755-d689-bfb71d59afc5\")"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
