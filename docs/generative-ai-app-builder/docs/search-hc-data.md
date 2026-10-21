---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data/
title: Get search results for healthcare data \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:51:26.972807+00:00
---

# Get search results for healthcare data  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Get search results for healthcare data Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

**Caution:**

  * Restrictions for healthcare: As a customer, you will not, and will not allow End Users to, use the Generative AI Services for clinical purposes (for clarity, non-clinical research, scheduling, or other administrative tasks is not restricted), as a substitute for professional medical advice, or in any manner that is overseen by or requires clearance or approval from any applicable regulatory authority. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms). 

For clarity, with respect to the use of Agent Search to retrieve and summarize existing medical information, the restriction on the use for clinical purposes means the restriction on the use for direct diagnosis or treatment purposes without review by a licensed professional in compliance with applicable laws and regulations. 

  * The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased (for example, stereotypes or other harmful content) information and should be reviewed. All summaries or answers should be considered draft and not final.
  * This product's intended usage is not to provide information pertaining to the prevention, diagnosis or treatment of illness or disease. Questions regarding diagnosis or treatment recommendations are not intended to be addressed by the product. This product's intended use is to retrieve and summarize existing medical information provided by users.
  * Due to limited test data, this product may or may not be applicable to age group 0-18 and to age group 85 and above. Therefore, when reviewing the generated output, customers must consider the representativeness of subpopulations within their source data.



After importing FHIR R4 data into your healthcare search app, you can query the imported data to get relevant results. You can search using the following types of queries:

  * Keyword query
  * Natural language query
  * Natural language query with a generative AI answer



Additionally, you can filter your search using date-filtered queries. For more information, see [Define a `resource_datetime` filter](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-hc-search#resource-datetime-filter).

When you search in the Google Cloud console, you must first provide a patient ID and search over a single patient's data at a time. When you search using the REST API, you can search over your entire data store.

This page shows how to search healthcare data using the various types of queries.

## Intended use of Agent Search for searching healthcare data

The intended usage of Agent Search is not to provide information pertaining to the prevention, diagnosis, or treatment of illness or disease. Questions regarding diagnosis or treatment recommendations are not intended to be addressed by the product. The intended use of this product is to retrieve and summarize existing medical information provided by users.

Due to limited test data, this product may or may not be applicable to age groups 0-18, and 85 and above. Therefore, when reviewing the generated output, customers must consider the representativeness of subpopulations within their source data.

The following are a few examples of how this product is intended to be used:

  * Exploratory queries to find a patient's information relevant to a topic:

    * "Summarize the aspirin uses"
    * "blood pressure"
    * "diabetes management?"
  * Navigational queries to find specific resources that could be mapped to a structured query:

    * "Show me the most recent a1c"
  * Extractive questions and answers to answer specific questions where evidence may be spread across resources:

    * "Has this patient ever been treated with a cephalsporin"
    * "Has the patient ever undergone psychiatry evaluation"



The following are examples of how this product is **not** intended to be used:

  * Diagnosis recommendations and treatment recommendations:

    * "What is the differential diagnosis for this patient?"
    * "What drugs should I prescribe to the patient?"



## Query guidelines

The following guidelines can help you frame a query that can give you better search results:

  * **Search for queries with specific intent** : Because the model doesn't know what you're looking for, it's better to provide a targeted query than a vague one. For example, searching for the keyword "hypertension" is better than searching for the keyword "summary". While the query "hypertension" brings up specific results from relevant documents, the query "summary" can bring up results from documents that aren't relevant.

  * **Preserve context** : Because search isn't conversational, it's better to provide the full context for each query. For example, if your initial query is "hypertension" and you want to follow up on the same topic, then "when was **hypertension** diagnosed" is a better second query than "when was **it** diagnosed".

  * **Simplify the query** : Whenever possible, break down complex queries into simpler ones. For example, instead of searching for "creatinine and albumin", create different queries for "creatinine", "albumin", and "creatinine albumin ratio", depending on your objective.

  * **Avoid asking for inferences** : Search provides more precise results when the model can return information verbatim from the documents that it searches from instead of calculating or deducing from the searched information. For example, instead of querying "how much has the patient weight changed", you can query, "list the patient weight in the last 10 visits" and then calculate the weight change separately.




## Match highlighting in results

Match highlighting is a configuration that highlights parts of text in a search result that contextually match the search query.

The results from the following resource types support match highlighting:

  * Composition: Highlights contextual text from the `Composition.section[].text.div` field.
  * DiagnosticReport: Highlights contextual text from the `DiagnosticReport.conclusion` field.
  * DocumentReference: Highlights contextual text from the documents referred in the `DocumentReference.content[0].attachment.url` field. The highlighted text is encased within a bounding box. The bounding box is represented by two sets of normalized coordinates in the search response. The documents that support match highlighting are PDF files and image files with [supported types](https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference#documentreference). The following image shows how text is highlighted in a scanned document from the DocumentReference resource type:

![Query is 'insulin'.](https://docs.cloud.google.com/generative-ai-app-builder/images/match-highlighting.png)**Figure 1.** Match highlighting in a DocumentReference scanned document.



When you search using REST API, you must enable match highlighting in your search request using the [`matchHighlightingCondition`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.evaluations#matchhighlightingcondition) field. The response contains the `match_highlighting` field, which you can use to render the highlighted text in your search application:

  * For Composition and DiagnosticReport documents, the `match_highlighting` field contains the start and end indexes for the token that must be highlighted.
  * For DocumentReference documents, the `match_highlighting` field contains the coordinates of the bounding box that highlights the text. The bounding box is represented by two sets of normalized coordinates with their origin at the top-left corner of the document. This field also nests the `page_number` field, which is set to `0` for images and `1` for the first page of PDF files.



When you preview the search results using the Google Cloud console, match highlighting is enabled by default.

## Before you begin

Before you search, do the following:

  * Create a healthcare search app and a healthcare search data store, and import FHIR R4 data. For more information, see [Create a healthcare search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-hc) and [Create a healthcare search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc).
  * [Configure search results for healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes#display-hc).
  * To get helpful query suggestions when searching, turn on [autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete). This is a Preview feature.
  * Review the list of FHIR R4 resources that Agent Search supports. For more information, see [Healthcare FHIR R4 data schema reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference).



## Search using a keyword

You can search your healthcare data store using a keyword. For example, you can search using keywords such as "a1c", "insulin", or "ulcer" to get relevant FHIR resources.

The following image shows the search results when the keyword is "lipid". This example doesn't include a summary or generative AI answer.

![Query is 'lipid'.](https://docs.cloud.google.com/generative-ai-app-builder/images/keyword-query.png)**Figure 2.** Search using keyword.

To search using a keyword, complete the following steps.

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the healthcare search app that you want to query.

  3. In the navigation menu, click **Preview**.

  4. In the **Patient ID** field, enter the ID of the patient whose data you want to query. Patient IDs are case-sensitive.

  5. Press **Enter** or click **Preview** to submit the patient ID.

  6. In the **Search here** search bar, type a keyword to search.

If you enabled autocomplete, you see a list of autocomplete suggestions below the search bar as you type.

  7. Press **Enter** to submit the query.

     * The search results are displayed in paginated tables that are categorized based on their FHIR resource type.
     * By default, the search results for all FHIR resource types are displayed in reverse chronological order.
  8. Optional. To filter the results, select one or more FHIR resource categories that are under the search bar.

  9. Optional. To order results according to relevance for the Composition, the DocumentReference, and the DiagnosticReport resources, click the **Sort: Reverse Chronological** filter and from the list select **Relevance**. For more information, see [Order healthcare search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results). 




### REST

The following sample shows how to search a single patient's FHIR R4 data in the healthcare search app using a keyword. This sample uses the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/search) method.

By default, the search results are returned in a reverse chronological order. When you search over the Composition, the DiagnosticReport, and the DocumentReference resources, you can order your search results according to relevance. For more information, see [Order healthcare search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results). 

  1. Search using a keyword.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
         "query": "KEYWORD_QUERY",
         "filter": "patientId: ANY(\"PATIENT_ID\")",
         "contentSearchSpec":{"snippetSpec":{"returnSnippet":true}}
         "displaySpec": {
             "matchHighlightingCondition": "MATCH_HIGHLIGHTING_CONDITION"
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `KEYWORD_QUERY`: the keyword that you want to search across the patient clinical data for the filtered patient, such as "diabetes" or "a1c".
     * `PATIENT_ID`: the resource ID of the patient whose data you want to search.
     * `MATCH_HIGHLIGHTING_CONDITION`: a string that can have the following values: 
       * `MATCH_HIGHLIGHTING_DISABLED`: turns off match highlighting on all documents.
       * `MATCH_HIGHLIGHTING_ENABLED`: turns on match highlighting on all documents. When you leave this field empty or don't specify it, match highlighting is set to `MATCH_HIGHLIGHTING_DISABLED` and is turned off on all documents.

#### Response

You should receive a JSON response similar to the following truncated response. The response contains itemized search results listed in reverse chronological order with snippets, if snippets are available. The `structData` field contains the structured JSON data for the document. The `derivedStructData` field contains the snippet text, match highlighting tokens, and bounding box coordinates (for scanned documents).
    
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
              ],
              "match_highlighting":{
                "matched_tokens": [
                  {
                    "end_index": TOKEN_END_INDEX,
                    "start_index": TOKEN_START_INDEX,
                    "token_text": "HIGHLIGHTED TEXT"
                  },
                ]
            }
          }
        },
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
              "DocumentReference": {
                  "content": [
                   {
                     "attachment": {
                       "url": "PATH/TO/STORAGE/FILE.png",
                       "creation": "2018-05-03T11:00:00+00:00",
                       "contentType": "image/png"
                     },
                     "format": {
                       "display": "Scanned",
                       "system": "https://g.co/fhir/harmonized/document_format",
                       "code": "scanned"
                     }
                   }
                 ],
                 }
               },
            "derivedStructData": {
              "total_page_count": 1,
              "match_highlighting": {
                "matched_bounding_boxes": [
                  {
                    "page_number": 0,
                    "page_bounding_boxes": [
                      {
                        "normalized_coordinates": [
                          X_MIN
                          Y_MIN
                          X_MAX
                          Y_MAX
                        ],
                        "token_text": "HIGHLIGHTED TEXT"
                      }
                    ]
                }
        ...
        }
      }
     ]
    }
    




## Search using natural language query

Using Agent Search, you can get results for complex natural language queries. For example, the following image shows the results for the the natural language query: "Lab results related to diabetes".

![Query is 'What are the patient's lipid labs'.](https://docs.cloud.google.com/generative-ai-app-builder/images/nl-query.png)**Figure 4.** Search using natural language query.

To search using natural language query, complete the following steps.

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the healthcare search app that you want to query.

  3. In the navigation menu, click **Preview**.

  4. In the **Patient ID** field, enter the patient ID of the patient whose data you want to query. Patient IDs are case-sensitive.

  5. Press **Enter** or click **Preview** to submit the patient ID.

  6. In the **Search here** search bar, enter a natural language query, such as "Lab results related to diabetes".

If you enabled autocomplete, you see a list of autocomplete suggestions below the search bar as you type.

  7. Press **Enter** to submit the query.

     * The search results are displayed in paginated tables that are categorized based on their FHIR resource type.
     * By default, the search results for all FHIR resource types are displayed in a reverse chronological order.
  8. Optional. Select one or more FHIR resource categories that are under the search bar to filter the results.

  9. Optional. To order results according to relevance for the Composition, the DocumentReference, and the DiagnosticReport resources, click the **Sort: Reverse Chronological** filter and from the list select **Relevance**. For more information, see [Order healthcare search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results). 




### REST

The following sample shows how to search a single patient's FHIR R4 data in the healthcare search app using a natural language query. This sample uses the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/search) method. To search using a natural language query, you must add the `naturalLanguageQueryUnderstandingSpec` field to the request body.

By default, the search results are returned in a reverse chronological order. When you search over the Composition, the DiagnosticReport, and the DocumentReference resources, you can order your search results according to relevance. For more information, see [Order healthcare search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results). 

  1. Post a query in natural language.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
         "query": "NATURAL_LANGUAGE_QUERY",
         "filter": "patientId: ANY(\"PATIENT_ID\")",
         "contentSearchSpec":{"snippetSpec":{"returnSnippet":true}},
         "naturalLanguageQueryUnderstandingSpec":{"filterExtractionCondition":"ENABLED"},
         "displaySpec": {
             "matchHighlightingCondition": "MATCH_HIGHLIGHTING_CONDITION"
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `NATURAL_LANGUAGE_QUERY`: the query in natural language, such as "Lab results related to diabetes" or "Is the patient currently on any medication".
     * `PATIENT_ID`: the resource ID of the patient whose data you want to search.
     * `MATCH_HIGHLIGHTING_CONDITION`: a string that can have the following values: 
       * `MATCH_HIGHLIGHTING_DISABLED`: turns off match highlighting on all documents.
       * `MATCH_HIGHLIGHTING_ENABLED`: turns on match highlighting on all documents. When you leave this field empty or don't specify it, match highlighting is set to `MATCH_HIGHLIGHTING_DISABLED` and is turned off on all documents.

#### Response

You should receive a JSON response similar to the following truncated response. The response contains itemized search results listed in reverse chronological order with snippets, if snippets are available. The `structData` field contains the structured JSON data for the document. The `derivedStructData` field contains the snippet text, match highlighting tokens, and bounding box coordinates (for scanned documents).
    
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
              ],
              "match_highlighting":{
                "matched_tokens": [
                  {
                    "end_index": TOKEN_END_INDEX,
                    "start_index": TOKEN_START_INDEX,
                    "token_text": "HIGHLIGHTED TEXT"
                  },
                ]
            }
          }
        },
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
              "DocumentReference": {
                  "content": [
                   {
                     "attachment": {
                       "url": "PATH/TO/STORAGE/FILE.png",
                       "creation": "2018-05-03T11:00:00+00:00",
                       "contentType": "image/png"
                     },
                     "format": {
                       "display": "Scanned",
                       "system": "https://g.co/fhir/harmonized/document_format",
                       "code": "scanned"
                     }
                   }
                 ],
                 }
               },
            "derivedStructData": {
              "total_page_count": 1,
              "match_highlighting": {
                "matched_bounding_boxes": [
                  {
                    "page_number": 0,
                    "page_bounding_boxes": [
                      {
                        "normalized_coordinates": [
                          X_MIN
                          Y_MIN
                          X_MAX
                          Y_MAX
                        ],
                        "token_text": "HIGHLIGHTED TEXT"
                      }
                    ]
                }
        ...
        }
      ]
    }
    




## Search using natural language query with generative AI answer

When you search a patient's FHIR data using a natural language query, you can choose to get a generative AI answer along with the search results. The answer summarizes the search results and also shows the references that are used to generate the answer.

When using the console, you can select the large language model (LLM) for generative AI answers. For more information, see [Configure search results for healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes#display-hc).

When using the REST API, you can specify the LLM model that you want to use. For a list of supported models, see [Available models](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models#models).

**Tip:** You can also try the MedLM model for medical question answering and summarization. For more information, see [Create MedLM prompts](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/medlm-prompts).

The following image shows an example of a natural language query with generative AI answer. The search summary provides an answer for the query by summarizing the findings from relevant results. You can expand segments that have citations to see the references that are used to generate the selected segment. Not all generated answers have citations.

![Query is 'What are the
patient's lipid labs'. The search results are shown in a tabular
format . The
search results are accompanied by a generative AI generated summary that reads quote The patient has no
known allergies endquote.](https://docs.cloud.google.com/generative-ai-app-builder/images/nl-query-with-genAI-answers.png)**Figure 3.** Search using natural language query with generative AI answer.

To search with generative AI answer, do the following:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the healthcare search app that you want to query.

  3. In the navigation menu, click **Configurations**.

  4. Customize the search widget:

     1. In the **Search type** field, select **Search with an answer**.
     2. Select the model that you want to use to generate the summary. For more information, see [Configure search results for healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes#display-hc)
     3. Save and publish your preferences.
  5. In the navigation menu, click **Preview**.

  6. In the **Patient ID** field, enter the patient ID of the patient whose data you want to query. Patient IDs are case-sensitive.

  7. Press **Enter** or click **Preview** to submit the patient ID.

  8. In the **Search here** search bar, enter a natural language query, such as "nsaids", "What are the patient's lipid labs", or "What is the most recent A1C result".

If you enabled autocomplete, you see a list of autocomplete suggestions below the search bar as you type.

  9. Press **Enter** to submit the query.

     * The generative AI answer is displayed under the search bar.
     * The search results are displayed in paginated tables that are categorized based on their FHIR resource type.
     * By default, the search results for all FHIR resource types are displayed in a reverse chronological order.
  10. Optional. Expand a segment of the answer that has citations to see its references from the search results.

  11. Optional. Select one or more FHIR resource categories that are under the search bar to filter the results.

  12. Optional. To order results according to relevance for the Composition, the DocumentReference, and the DiagnosticReport resources, click the **Sort: Reverse Chronological** filter and from the list select **Relevance**. For more information, see [Order healthcare search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results). 




### REST

The following sample shows how to search a single patient's FHIR R4 data in the healthcare search app using a natural language query with generative AI answers. This sample uses the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/search) method.

  * To search using a natural language query, you must add the `naturalLanguageQueryUnderstandingSpec` field to the request body.
  * To include inline citation indexes, you must add the `includeCitations` field. This is a boolean field with default set to `false`.



By default, the search results are returned in a reverse chronological order. When you search over the Composition, the DiagnosticReport, and the DocumentReference resources, you can order your search results according to relevance. For more information, see [Order healthcare search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results). 

  1. Post a query in natural language.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
                 "query": "QUERY",
                 "filter": "patientId: ANY(\"PATIENT_ID\")",
                 "contentSearchSpec": {
                   "snippetSpec": {
                     "returnSnippet": true
                   },
                   "displaySpec": {
                       "matchHighlightingCondition": "MATCH_HIGHLIGHTING_CONDITION"
                   }
                   "summarySpec": {
                     "summaryResultCount": 1,
                     "includeCitations": true,
                     "modelSpec": {
                       "version": "MODEL_VERSION"
                     }
                   }
                 },
                 "naturalLanguageQueryUnderstandingSpec": {
                   "filterExtractionCondition": "ENABLED"
                 }
           }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `QUERY`: the query in natural language, such as "nsaids", "What are the patients lipid labs", or "What is the most recent A1C result". If the query includes an apostrophe `'`, you must replace it with apostrophe's numeric character reference: `&#39;`.
     * `PATIENT_ID`: the resource ID of the patient whose data you want to search.
     * `MODEL_VERSION`: the model version that you want to use to generate the answer. See [Available models](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models#models).
     * `MATCH_HIGHLIGHTING_CONDITION`: a string that can have the following values: 
       * `MATCH_HIGHLIGHTING_DISABLED`: turns off match highlighting on all documents.
       * `MATCH_HIGHLIGHTING_ENABLED`: turns on match highlighting on all documents. When you leave this field empty or don't specify it, match highlighting is set to `MATCH_HIGHLIGHTING_DISABLED` and is turned off on all documents.

#### Response

You should receive a JSON response similar to the following truncated response. The response contains itemized search results listed in reverse chronological order along with the following fields in the `summary` object:

     * `summaryText`: contains the generated answer summary.
     * `summaryWithMetadata`: contains the generated answer summary, with citations. This field is displayed only if there are citations. Not all generated answers have citations. When `summaryWithMetadata` field is available, Google recommends using the `summaryWithMetadata` field over the `summaryText` field.
     * `citations.sources.referenceIndex`: contains the reference index of the documents cited in the response. This is useful to find the full resource name of the document in the `references` field.

The `structData` field contains the structured JSON data for the document. The `derivedStructData` field contains the snippet text, match highlighting tokens, and bounding box coordinates for scanned documents. 
    
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
              ],
              "match_highlighting":{
                "matched_tokens": [
                  {
                    "end_index": TOKEN_END_INDEX,
                    "start_index": TOKEN_START_INDEX,
                    "token_text": "HIGHLIGHTED TEXT"
                  },
                ]
            }
          }
        },
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
              "DocumentReference": {
                  "content": [
                   {
                     "attachment": {
                       "url": "PATH/TO/STORAGE/FILE.png",
                       "creation": "2018-05-03T11:00:00+00:00",
                       "contentType": "image/png"
                     },
                     "format": {
                       "display": "Scanned",
                       "system": "https://g.co/fhir/harmonized/document_format",
                       "code": "scanned"
                     }
                   }
                 ],
                 }
               },
            "derivedStructData": {
              "total_page_count": 1,
              "match_highlighting": {
                "matched_bounding_boxes": [
                  {
                    "page_number": 0,
                    "page_bounding_boxes": [
                      {
                        "normalized_coordinates": [
                          X_MIN
                          Y_MIN
                          X_MAX
                          Y_MAX
                        ],
                        "token_text": "HIGHLIGHTED TEXT"
                      }
                    ]
                }
        ...
        }
      ]
      "summary": {
        "summaryText": "GENERATE_ANSWER_TEXT",
        "summaryWithMetadata": {
          "summary": "GENERATE_ANSWER_TEXT",
          "citationMetadata": {
            "citations": [
              {
                "sources": [
                  {
                    "id": "DOCUMENT_ID",
                    "referenceIndex": "REFERENCE_INDEX_FROM_SUMMARY_METADATA"
                  }
                ]
              }
           ]
          },
          "references": [
            {
              "document": "projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID"
            },
            ...
          ]
        },
      }
    ...
    }
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
