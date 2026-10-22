---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results/
title: Order healthcare search results \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:04.170918+00:00
---

# Order healthcare search results  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Order healthcare search results Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

By default, when you [search healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data), the search results are returned in reverse chronological order. When you search over the following FHIR resource types that contain unstructured text, you can order your search results according to their relevance to your query:

  * Composition
  * DiagnosticReport
  * DocumentReference



## Example scenario

Suppose that you're searching for the keyword `insulin` for a given patient and you've filtered the results to the resources that contain unstructured text. Among other results, you receive the following documents:

  * Result 1: A DocumentReference resource, dated 24 April, 2024, that contains notes about the patient's "HbA1c" levels.
  * Result 2: A DiagnosticReport resource, dated 11 January, 2024, that contains notes about the "insulin regimen" that the patient must follow.



By default, Result 1 is shown higher in the results because it is a newer document, but when you order by relevance, Result 2 shows up higher in the results. This is because it is more relevant to the search query `insulin`.

## Order your healthcare search results

To order your search results according to relevance, complete the following steps:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the healthcare search app that you want to query.

  3. In the navigation menu, click **Preview**.

  4. In the **Patient ID** field, enter the ID of the patient whose data you want to query. Patient IDs are case-sensitive.

  5. Press **Enter** or click **Preview** to submit the patient ID.

  6. In the **Search here** search bar, enter your query.

If you enabled autocomplete, you see a list of autocomplete suggestions below the search bar as you type.

  7. Press **Enter** to submit the query.

     * The search results are displayed in paginated tables that are categorized based on their FHIR resource type.
     * By default, the search results for all FHIR resource types are displayed in reverse chronological order.
  8. For the Composition, the DocumentReference, and the DiagnosticReport resources, click the **Sort: Reverse Chronological** filter and select **Relevance** from the list. The results for these resources are then ordered according to relevance.




### REST

To order your search results according to relevance, modify your [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) request in the following way:

  * Add the `filter` field to your request to limit the search results to only those FHIR resources that contain unstructured text: Composition, DiagnosticReport, and DocumentReference.
  * Add the `orderBy` field to your search request and set its value to `_RELEVANCE` to get search responses that are sorted according to their relevance.


  1. Send the search request.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://us-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/us/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
         "query": "KEYWORD_QUERY",
         "filter": "patient_id: ANY(\"PATIENT_ID\") AND resource_type: ANY(\"Composition\", \"DiagnosticReport\", \"DocumentReference\")",
         "orderBy": "_RELEVANCE"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `KEYWORD_QUERY`: the keyword that you want to search across the patient clinical data for the filtered patient, such as "diabetes" or "a1c".
     * `PATIENT_ID`: the resource ID of the patient whose data you want to search.

You should receive a JSON response that contains itemized search results listed in the order of their relevance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
