---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/order-structured-results/
title: Order results from structured data stores \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:37.530829+00:00
---

# Order results from structured data stores  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/order-structured-results/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Order results from structured data stores Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

Ordering is a type of ranking mechanism that dynamically changes the sequence in which results are returned after an initial ranking that's established during the retrieval process. During retrieval, Agent Search fetches the relevant documents from the data store in the order of thousands (subject to the size of the data store). After this the top results are served according to the condition specified for reordering. For more information, see [About retrieval and ranking](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking-overview).

This page explains how to order the results of a search query made on structured data stores and on unstructured data stores with metadata.

## Supported data types for ordering the results

These are the field types that you can have your search results ordered by:

  * `string`
  * `number`
  * `datetime`
  * `geolocation`



## Before you begin

Make sure that you have an app with a data store that contains structured data or unstructured data with metadata.

## Order your search results

To order the search results for a structured data store or for an unstructured data store with metadata, follow these steps:

### REST

To use the API to order your search results for an app with structured data or unstructured data with metadata, use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:

**Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Make a search query and include the `orderBy` field.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "orderBy": "ORDER_BY"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project..
     * `APP_ID`: the ID of the Agent Search app..
     * `QUERY`: the query text to search.
     * `ORDER_BY`: the order in which the results are arranged. The default sort order is ascending. For example, specifying `date` returns results from the oldest to the newest. To get descending sort order, append `desc` to the `date` value—for example, `date desc`. For more examples, see `orderBy` examples.

#### Example command and result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search" \
    -d '{
        "query": "hotel",
        "orderBy": "rating desc"
       }'
        
    
    * * *
    
    
    {
    "results": [
    {
      "id": "10d480b19c256bb1",
      "document": {
        "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/10d480b19c256bb1",
        "id": "10d480b19c256bb1",
        "structData": {
          "available_date": "2023-11-05",
          "amenities": [
            "Lake Views",
            "Private Beach",
            "Spa",
            "Water Activities"
          ],
          "room_types": [
            "Lakefront Suite",
            "Deluxe Room",
            "Cottage"
          ],
          "location": {
            "address": "988 Serenity Circle, Tranquil Town, NV 89501, USA"
          },
          "rating": 4.6,
          "id": 11,
          "price_per_night": 220.5,
          "title": "Serenity Springs Hotel"
        }
      }
    },
    {
      "id": "9ffae8af37cc8b63",
      "document": {
        "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/9ffae8af37cc8b63",
        "id": "9ffae8af37cc8b63",
        "structData": {
          "title": "Riverfront Plaza Hotel",
          "rating": 4.2,
          "location": {
            "address": "101 Main St, Anytown, CA 94501, USA"
          },
          "price_per_night": 145.8,
          "amenities": [
            "Fitness Center",
            "Conference Rooms",
            "Restaurant",
            "Valet Parking"
          ],
          "id": 3,
          "room_types": [
            "Executive Suite",
            "King Room",
            "Double Queen"
          ],
          "available_date": "2023-11-15"
        }
      }
    },
    {
      "id": "3be9e854d8f3a47f",
      "document": {
        "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/3be9e854d8f3a47f",
        "id": "3be9e854d8f3a47f",
        "structData": {
          "amenities": [
            "Oceanfront Views",
            "Pool",
            "Spa",
            "Beachside Dining"
          ],
          "available_date": "2023-09-18",
          "location": {
            "address": "449 Oceanfront Drive, Seaside Resort, CA 92007, USA"
          },
          "id": 13,
          "title": "Ocean Breeze Hotel",
          "room_types": [
            "Ocean View Suite",
            "Deluxe Room",
            "Family Suite"
          ],
          "rating": 4.1,
          "price_per_night": 180
        }
      }
    }
    ],
    "totalSize": 3,
    "attributionToken": "wAHwvwoMCNDYz7UGEMCklrsCEiQ2NmIzYmU5My0wMDAwLTIxMDUtYmUyNy01ODI0MjljMzdlZTQiB0dFTkVSSUMqgAHd1akt3e2ILebtiC2CspoigLKaIpjeqC-q-LMtjr6dFeqCsS2W3qgvwvCeFaz4sy2jgJcinta3LeiCsS3b7Ygt5O2ILa3Eii3Usp0Vpp-VLZzWty359rMt-_azLaCJsy3dj5oixcvzF6vEii2iibMttreMLd_VqS3bj5oipJ-VLQ",
    "guidedSearchResult": {},
    "summary": {}
    }
        

In this example, the documents that contain the word "hotel" are ordered by rating, from the Serenity Springs Hotel with a 4.6 rating to the Ocean Breeze Hotel with a 4.1 rating. 




## `orderBy` examples

To order on a string field called `title`:

  * `"orderBy": "title"` to return the documents in ascending alphabetic order according to title.

  * `"orderBy": "title desc"` to return the documents sorted in reverse alphabetic order (from Z to A) according to the title.




To order on a number field called `rating`:

  * `"orderBy": "rating"` to order from the lowest to the highest rated documents.

  * `"orderBy": "rating desc"` to order from the highest to the lowest rated documents.




To order on a datetime field called `available_date`:

  * `"orderBy": "available_date"` to order from the soonest available document to the farthest out.

  * `"orderBy": "available_date desc"` to order from the document with the farthest out available date to the one soonest available.




To order according to geolocation on a field called `location`:

  * `"orderBy": "GEO_DISTANCE(location, \"Mountain View, CA\")"` sorts the documents in order from those nearest to Mountain View to those farthest from Mountain View.

  * `"orderBy": "GEO_DISTANCE(location, 37.38, -122.08) desc"` sorts the documents in order from farthest to nearest to the location 37.38°N and 122.08°W.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
