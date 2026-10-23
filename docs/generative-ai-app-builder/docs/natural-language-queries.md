---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries/
title: Filter with natural-language understanding \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:38.725913+00:00
---

# Filter with natural-language understanding  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Filter with natural-language understanding Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to apply natural-language understanding to automatically make filters for search queries and, therefore, to improve the quality of the results returned.

You can use this feature with search apps that are connected to structured data stores.

## About natural-language query understanding

If you have a custom search app with structured data, your users' natural-language queries can be reformatted as filtered queries. This can lead to better quality search results than searching for words in the query string.

For example, a natural-language query such as `"Find a coffee shop serving banana bread"` might be reformulated as a query and a filter: `"query": "banana bread", "filter": "type": ANY(\"cafe\")`.

Using natural-language query understanding is easier and more flexible than writing your own filter expressions. For information about writing filter expressions, see [Filter custom search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata).

## Hard and soft filters

There are two kinds of filters that you can apply for natural-language query understanding: _hard_ and _soft_.

  * **Hard.** By default, extracted filters are applied as mandatory criteria that a result must satisfy to be returned.

Behavior is similar to the `filter` field in the [search request](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search#request-body).

  * **Soft.** An alternative to the hard filter is to apply a boost to the search results. Boosted results are more likely to be returned but results that don't meet the boost criterion can also be returned.

Behavior is similar to the `boostSpec` field in the [search request](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search#request-body).




You can experiment with both types of filter. If searches are not returning enough results, try the soft filter instead of the hard one.

For details on how to apply a soft filter, see Search with the soft filter below.

## Examples

This feature is best explained through examples:

  * Example: Field extraction from queries (hard filter) shows the field filters extracted from the query.

  * Example: With a geolocation filter (hard filter) includes the special case of the geolocation filter.

  * Example: Field extraction from queries (soft filter) shows the soft filter extracted from a query made to a blended app.




### Example: Field extraction from queries (hard filter)

This natural-language query understanding feature is explained through the example of searching for a hotel.

Take the following query made to a structured data store for a hotel site: _"Find me a family-friendly hotel with at least four stars that costs less than 300 a night, lets me bring my dog, and has free Wi-Fi."_

Without natural-language query understanding, the search app looks for documents that contain the words in the query.

With natural-language query understanding and appropriately structured data, the search is made more effective by replacing some of the natural language in the query with filters. If the structured data has fields for `star_rating` (numbers), `price` (numbers), and `amenities` (strings), then the query can be formulated to include the following filters:
    
    
       {
           "star_rating": >=4,
           "price": <=300,
           "amenities": "Wifi", "Pets Allowed"
       }
    

### Example: With a geolocation filter (hard filter)

This example is similar to the preceding one except that it includes a _geolocation_ filter, which is special kind of extracted filter. Agent Search has the ability to recognize locations in a query and create proximity filters for the locations.

Take the following query made to a state-wide business site: _"Find me a chic and stylish hotel with at least 4 stars that is in San Francisco."_

With natural-language query understanding and the geolocation filter, the search is reformulated to include the following filter for a hotel with at least a 4-star rating and within a 10 km radius of San Francisco:
    
    
       {
           "star_rating": >=4,
           "location": GEO_DISTANCE(\"San Francisco, CA\", 10000)
       }
    

In this example, the `GEO_DISTANCE` is an address, but in other queries, it might be written as a latitude and longitude, even though the original query contained an address.

### Example: Field extraction from queries (soft filter)

This natural-language query understanding feature is explained through the example of searching for a hotel but showing some results that don't meet all criteria.

Take the following query made to a travel site: _"Find me a family-friendly hotel with at least four stars that costs less than 300 a night, and lets me bring my dog."_

With natural-language query understanding and appropriately structured data, the search is made more effective by replacing some of the natural language in the query with soft filters. If the structured data has fields for `star_rating` (numbers), `price` (numbers), and `amenities` (strings), then the query can be rewritten as the following boost:

Boost condition extracted from the natural-language query:
    
    
    {
      "boostSpec": {
        "conditionBoostSpecs": {
          "condition": "(star_rating >= 4.5) AND (price < 200) AND ANY(amenities, \"Pets Allowed\")",
          "boost": 0.7
        }
      }
    }
    

In this case, perhaps some lower rated hotels or non pet-friendly hotels may be returned.

The strength of the boost depends on the number of structured filters that a document matches. If three conditions are extracted and the document matches only one of the conditions, then the document receives a small boost. Alternatively, if the document matches all three conditions, then it is given a strong boost.

## Limitations

The following limitations apply to natural-language query understanding:

  * Natural-language query understanding can't be applied to [blended search apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#blended). You get an error if you try to use natural-language query understanding with a blended search app.

  * Natural-language query understanding works only for custom search apps that use structured data stores.

  * Using natural-language query understanding increases latency, so you might choose not to use it if latency is a problem.

  * For geolocation, the location must be explicitly described. You can't use locations such as "near me" or "home".

  * The radius for geolocation is 10 km and isn't configurable.

  * Boolean fields can't be used in filters. For example, if the query is _"Find me a non-smoking hotel room"_ , then a boolean field like `"non_smoking": true` isn't useful but a string field like `"non_smoking": "YES"` can be part of the filter.




## Before you begin

Before you start using natural-language query understanding, you have to enable it for the structured data stores connected to the apps that you plan to use.

To enable natural-language query understanding, follow these steps:

### REST

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Run the following curl command:
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID?update_mask=natural_language_query_understanding_config.mode" \
         -d '{
               "naturalLanguageQueryUnderstandingConfig": {
                 "mode": "ENABLED"
               }
             }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
**Note:** If you want to disable natural-language query understanding for a data store, run the command above, replacing `ENABLED` with `DISABLED`.

#### Example command and response
    
    curl -X PATCH
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    -H "X-Goog-User-Project: my-project-123"
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store?update_mask=natural_language_query_understanding_config.mode"
    -d '{
           "naturalLanguageQueryUnderstandingConfig": {
             "mode": "ENABLED"
           }
        }'
    
    
    * * *
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store",
      "displayName": "test_data_store",
      "industryVertical": "GENERIC",
      "createTime": "2024-07-10T18:50:01.673414Z",
      "solutionTypes": [
        "SOLUTION_TYPE_SEARCH"
      ],
      "defaultSchemaId": "default_schema",
      "documentProcessingConfig": {
        "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/documentProcessingConfig",
        "defaultParsingConfig": {
          "digitalParsingConfig": {}
        }
      },
      "servingConfigDataStore": {},
      "naturalLanguageQueryUnderstandingConfig": {
        "mode": "ENABLED"
      }
    }
    

  3. Repeat steps 1 and 2 for each data store.

  4. Wait approximately 24 hours.

If you try to use natural-language query understanding before the data store is ready, the response you get is the same as if `filterExtractionCondition` was set to `DISABLED`.




## Search, converting natural-language queries into filters

To search on a query in natural language and get results that are optimized for natural-language queries, do the following:

### REST

  1. Run the following curl command, which calls the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
                 "query": "QUERY",
                 "naturalLanguageQueryUnderstandingSpec": {
                   "filterExtractionCondition": "ENABLED"
                 }
               }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query. The app must be connected to a data store that contains structured data. The app can't be a blended search app.
     * `QUERY`: the query written in natural language.

#### Example command and partial result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    "https://discoveryengine.googleapis.com/v1/projects/123456
    /locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search"
    -d '{
    "query": "Find me a family-friendly hotel with at least four stars that costs less than 300 a night, lets me bring my dog, and has free Wi-Fi.",
    "naturalLanguageQueryUnderstandingSpec": {
      "filterExtractionCondition": "ENABLED"}
    }'
    
    
    * * *
    
    
    {
    "results": [
    {
      "id": "b2617d862",
      "document": {
        "name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/b2617d862",
        ...
      }
    },
    {
      "id": "a51841841",
      "document": {
        "name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/a51841841",
        ...
      }
    }
    ],
    "naturalLanguageQueryUnderstandingInfo": {
    "extractedFilters": "(amenities: ANY(\"Pets Allowed\") AND amenities: ANY(\"Wifi\") AND star_rating: >= 4 AND price: < 300)",
    "extractedFilterStructured": {
      "expression": {
        "andExpr": {
          "expressions": [
            {
              "numberConstraint": {
                "fieldName": "star_rating",
                "value": 4,
                "comparison": "GREATER_THAN_EQUALS",
              }
            },
            {
              "numberConstraint": {
                "fieldName": "price",
                "value": 300,
                "comparison": "LESS_THAN",
              }
            },
            {
              "stringConstraint": {
                "fieldName": "amenities",
                "any": ["Pets Allowed"]
              }
            },
            {
              "stringConstraint": {
                "fieldName": "amenities",
                "any": ["Wifi"]
              }
            },
          ]
        }
    




## Search, converting locations in queries to geolocation filters

To search on a query in natural language and get results that are optimized for natural-language queries including proximity to locations, do the following:

### REST

  1. Run the following curl command, which calls the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
                 "query": "QUERY",
                 "naturalLanguageQueryUnderstandingSpec": {
                   "filterExtractionCondition": "ENABLED",
                   "geoSearchQueryDetectionFieldNames": ["GEO_FIELD_NAME_1", "GEO_FIELD_NAME_N"]"
                 }
               }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query. The app must be connected to a data store that contains structured data. The app can't be a blended search app.
     * `QUERY`: the query written in natural language.
     * `GEO_FIELD_NAME_1, GEO_FIELD_NAME_N`: a list of values of type `geolocation`. If the value type isn't `geolocation`, then this field is ignored.

#### Example command and result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    "https://discoveryengine.googleapis.com/v1/projects/123456
    /locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search"
    -d '{
    "query": "Find me a chic and stylish hotel with at least 4 stars that is in San Francisco.",
    "naturalLanguageQueryUnderstandingSpec": {
      "filterExtractionCondition": "ENABLED",
      "geoSearchQueryDetectionFieldNames": ["location"]}
    }'
    
    
    * * *
    
    
    {
    "results": [
    {
    "id": "b2617d862",
    "document": {
    "name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/b2617d862",
    ...
    }
    },
    {
    "id": "a51841841",
    "document": {
    "name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/a51841841",
    ...
    }
    }
    ],
    "naturalLanguageQueryUnderstandingInfo": {
    "extractedFilters": "(star_rating: >= 4 AND GEO_DISTANCE("location", "San Francisco", 10000))",
    "extractedFilterStructured": {
    "expression": {
    "andExpr": {
      "expressions": [
        {
          "numberConstraint": {
            "fieldName": "star_rating",
            "value": 4,
            "comparison": "GREATER_THAN_EQUALS",
          }
        },
        {
          "geolocationConstraint": {
            "fieldName": "location",
            "address": "San Francisco",
            "radius_in_meters": 10000,
          }
        },
      ]
    }
    




## Search with the soft filter

To apply a soft filter, do the following:

### REST

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl command, which calls the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
                 "query": "QUERY",
                 "naturalLanguageQueryUnderstandingSpec": {
                   "filterExtractionCondition": "ENABLED",
                   "extractedFilterBehavior": "SOFT_BOOST"
                 }
               }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: The ID of your search app. The app must be connected to a data store that contains structured data. The app can't be a blended search app.
     * `QUERY`: Your query in natural language.

#### Example command and partial response
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search" \
      -d '{
            "query": "Find me a family-friendly hotel with at least four stars that costs less than 300 a night, lets me bring my dog, and has free Wi-Fi.",
            "naturalLanguageQueryUnderstandingSpec": {
              "filterExtractionCondition": "ENABLED",
              "extractedFilterBehavior": "SOFT_BOOST"
            }
          }'
    
    
    * * *
    
    
    {
      "results": [
        {
          "id": "4246fcb660e398908bcd3007d9863ef8",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-app/branches/0/documents/4246fcb660e398908bcd3007d9863ef8",
            "id": "4246fcb660e398908bcd3007d9863ef8",
            "structData": {
              "room_types": [
                "Double",
                "Single",
                "Deluxe"
              ],
              "available_date": "2023-11-14",
              "amenities": [
                "Pet Friendly",
                "Pool",
                "Free Wi-Fi",
                "Bar"
              ],
              "location": {
                "zip_code": "23941",
                "country": "USA",
                "city": "South Amber",
                "state": "NH",
                "address": "2304 Nicholas Fort, Moorechester, MI 20090"
              },
              "id": 262,
              "contact": {
                "email": "eric59@example.com",
                "phone": "316-868-8020x2693"
              },
              "price_per_night": 112.48,
              "title": "Houston-Tran",
              "rating": 1.5
            },
            "derivedStructData": {
              "clearbox_escorer_score": 0,
              "is_exact_match_query": 0,
              "can_fetch_raw_content": "true"
            }
          },
          "rankSignals": {
            "keywordSimilarityScore": 0,
            "semanticSimilarityScore": 0.7236669,
            "boostingFactor": 0,
            "defaultRank": 1,
            "customSignals": [
              {
                "name": "c.id",
                "value": 262
              },
              {
                "name": "c.rating",
                "value": 1.5
              },
              {
                "name": "c.price_per_night",
                "value": 112.48
              }
            ]
          }
        },
        {
          "id": "d729812e97b224b7a812e9ad0240ca3e",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-app/branches/0/documents/d729812e97b224b7a812e9ad0240ca3e",
            "id": "d729812e97b224b7a812e9ad0240ca3e",
            "structData": {
              "location": {
                "address": "38107 Mays Extension Apt. 070, Steventon, DC 31453",
                "state": "MA",
                "country": "USA",
                "zip_code": "25856",
                "city": "New Laura"
              },
              "title": "Serrano, Jackson and Carr",
              "available_date": "2024-04-05",
              "room_types": [
                "Single",
                "Deluxe",
                "Single"
              ],
              "price_per_night": 188.87,
              "contact": {
                "email": "knavarro@example.com",
                "phone": "(089)882-8916"
              },
              "id": 66,
              "rating": 4.3,
              "amenities": [
                "Pet Friendly",
                "Gym",
                "Pool",
                "Free Wi-Fi"
              ]
            },
            "derivedStructData": {
              "can_fetch_raw_content": "true",
              "is_exact_match_query": 0,
              "clearbox_escorer_score": 0.76363050937652588
            }
          },
          "rankSignals": {
            "keywordSimilarityScore": 0.7636305,
            "semanticSimilarityScore": 0.7108109,
            "boostingFactor": 0,
            "defaultRank": 2,
            "customSignals": [
              {
                "name": "c.id",
                "value": 66
              },
              {
                "name": "c.rating",
                "value": 4.3
              },
              {
                "name": "c.price_per_night",
                "value": 188.87
              }
            ]
          }
        },
        {
          "id": "67e4484d2e6bf30bd3aa5229058cf3ad",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-app/branches/0/documents/67e4484d2e6bf30bd3aa5229058cf3ad",
            "id": "67e4484d2e6bf30bd3aa5229058cf3ad",
            "structData": {
              "rating": 4.6,
              "room_types": [
                "Double",
                "Single",
                "Deluxe"
              ],
              "title": "Spencer-Small",
              "id": 249,
              "amenities": [
                "Pet Friendly",
                "Free Wi-Fi",
                "Pet Friendly",
                "Restaurant"
              ],
              "price_per_night": 66.38,
              "contact": {
                "phone": "+1-176-057-5439x71337",
                "email": "mike26@example.com"
              },
              "location": {
                "zip_code": "37354",
                "state": "WY",
                "city": "Port James",
                "address": "52979 Linda Orchard, New Ashley, GA 22405",
                "country": "USA"
              },
              "available_date": "2024-04-10"
            },
            "derivedStructData": {
              "can_fetch_raw_content": "true",
              "clearbox_escorer_score": 0,
              "is_exact_match_query": 0
            }
          },
          "rankSignals": {
            "keywordSimilarityScore": 0,
            "semanticSimilarityScore": 0.71184474,
            "boostingFactor": 0,
            "defaultRank": 3,
            "customSignals": [
              {
                "name": "c.id",
                "value": 249
              },
              {
                "name": "c.rating",
                "value": 4.6
              },
              {
                "name": "c.price_per_night",
                "value": 66.38
              }
            ]
          }
        },
        ...
        {
          "id": "53d468f88b0d87b29bff51f8784d91a8",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-app/branches/0/documents/53d468f88b0d87b29bff51f8784d91a8",
            "id": "53d468f88b0d87b29bff51f8784d91a8",
            "structData": {
              "contact": {
                "email": "bradley29@example.com",
                "phone": "404.120.7687x62482"
              },
              "price_per_night": 68.66,
              "rating": 3.3,
              "amenities": [
                "Restaurant",
                "Bar",
                "Pet Friendly",
                "Pool"
              ],
              "id": 25,
              "room_types": [
                "Suite",
                "Suite",
                "Double"
              ],
              "available_date": "2024-05-15",
              "title": "Wilson-Ward",
              "location": {
                "city": "East Sheila",
                "country": "USA",
                "state": "TX",
                "zip_code": "34921",
                "address": "60458 Fleming Freeway, South Holly, ME 64008"
              }
            },
            "derivedStructData": {
              "is_exact_match_query": 0,
              "can_fetch_raw_content": "true",
              "clearbox_escorer_score": 0
            }
          },
          "rankSignals": {
            "keywordSimilarityScore": 0,
            "semanticSimilarityScore": 0.70549995,
            "boostingFactor": 0,
            "defaultRank": 49,
            "customSignals": [
              {
                "name": "c.id",
                "value": 25
              },
              {
                "name": "c.rating",
                "value": 3.3
              },
              {
                "name": "c.price_per_night",
                "value": 68.66
              }
            ]
          }
        },
        {
          "id": "653c16be81e88e23d694db625e474881",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-app/branches/0/documents/653c16be81e88e23d694db625e474881",
            "id": "653c16be81e88e23d694db625e474881",
            "structData": {
              "price_per_night": 443.9,
              "amenities": [
                "Pool",
                "Free Wi-Fi",
                "Parking",
                "Beach Access"
              ],
              "contact": {
                "email": "jamesblackburn@example.com",
                "phone": "155.107.3771"
              },
              "available_date": "2024-02-25",
              "id": 279,
              "room_types": [
                "Deluxe",
                "Penthouse",
                "Single"
              ],
              "title": "Wolf, Williams and Jenkins",
              "rating": 3.1,
              "location": {
                "address": "904 Kimberly Alley, Lake Aprilchester, WI 31242",
                "zip_code": "23652",
                "state": "SD",
                "country": "USA",
                "city": "Cunninghamside"
              }
            },
            "derivedStructData": {
              "can_fetch_raw_content": "true",
              "clearbox_escorer_score": 0.76363050937652588,
              "is_exact_match_query": 0
            }
          },
          "rankSignals": {
            "keywordSimilarityScore": 0.7636305,
            "semanticSimilarityScore": 0.69835776,
            "boostingFactor": 0,
            "defaultRank": 50,
            "customSignals": [
              {
                "name": "c.id",
                "value": 279
              },
              {
                "name": "c.rating",
                "value": 3.1
              },
              {
                "name": "c.price_per_night",
                "value": 443.9
              }
            ]
          }
        }
      ],
      "totalSize": 106,
      "attributionToken": "mAL0FwEKDAiJ_4nIBhDH28e5ARIkNjkwMzk4ODktMDAwMC0yNGQ4LWJmYzEtMTRjMTRlZjFiNjcwIgdHRU5FUklDKkiVksUwjr6dFZ_Wty27kfoxvpH6MbaqojKugJM34-uQN9PaiTeQ97IwwvCeFdSynRXg65A3nNa3Lbe3jC2OkckwuaqiMtDaiTcwAVKMAXByb2plY3RzLzc1NjIwNjYwODQ3OS9sb2NhdGlvbnMvZ2xvYmFsL2NvbGxlY3Rpb25zL2RlZmF1bHRfY29sbGVjdGlvbi9lbmdpbmVzL2hvdGVscy1tYW55LXNlYXJjaF8xNzI0NDUyMzYwMzU2L3NlcnZpbmdDb25maWdzL2RlZmF1bHRfc2VhcmNo",
      "nextPageToken": "AzN2IWMmVGNxMGNx0SMjZmYtgDZ0ITLwADMw0CO4gTOzATO2QiGC8O-7WMEGgcmorICMIBM1IgC",
      "guidedSearchResult": {},
      "summary": {},
      "appliedControls": [
        "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/secondbb"
      ],
      "queryExpansionInfo": {},
      "naturalLanguageQueryUnderstandingInfo": {
        "extractedFilters": "(rating\u003e=4 AND price_per_night\u003c300 AND amenities: ANY(\"Pet Friendly\") AND amenities: ANY(\"Free Wi-Fi\"))",
        "structuredExtractedFilter": {
          "expression": {
            "andExpr": {
              "expressions": [
                {
                  "stringConstraint": {
                    "fieldName": "amenities",
                    "values": [
                      "Pet Friendly"
                    ],
                    "querySegment": "lets me bring my dog"
                  }
                },
                {
                  "stringConstraint": {
                    "fieldName": "amenities",
                    "values": [
                      "Free Wi-Fi"
                    ],
                    "querySegment": "free Wi Fi"
                  }
                },
                {
                  "numberConstraint": {
                    "fieldName": "rating",
                    "comparison": "GREATER_THAN_EQUALS",
                    "value": 4
                  }
                },
                {
                  "numberConstraint": {
                    "fieldName": "price_per_night",
                    "comparison": "LESS_THAN",
                    "value": 300
                  }
                }
              ]
            }
          }
        }
      }
    }
    

This example command sets the filter behavior to `SOFT_BOOST`, overriding the default `HARD_FILTER`.




## Specify fields for natural-language queries

For a field to be used as a filter in natural-language query understanding, it must be marked as indexable in the schema. (For general information about viewing and editing a schema, see [Update a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas).)

Agent Search determines which of the indexable fields in the schema make sense to use in natural-language query understanding filters. But, if fields are included that you don't want, then you need to create an allowlist to specify which fields can be used.

Consider a hotel booking site, where there are fields such as `amenities`, `id`, `price_per_night`, `rating`, and `room_types`. Of these, if the `id` is a string of characters and numbers, Agent Search is likely to exclude it from the fields used for natural-language query understanding.

However, if you observe that Agent Search is returning poor quality query results because it's not excluding fields that it should, then, you need to specify which fields can be used. For example, if the hotel schema has a field for `renovation_status` that isn't useful to customers and might be embarrassing to the hotel chain, then you can exclude it from the list of allowed fields.

Example of a record from the structured data store of hotel data.
    
    
    {
      "title": "Miller-Jones",
      "rating": 1.7,
      "price_per_night": 115.16,
      "id": 2902,
        …
      ],
      "amenities": [
        "Spa",
        "Parking",
        "Restaurant"
        …
      ],
      "renovation_status": "Restaurant and spa renovation planned for 2027"
    }
    

An appropriate allowlist for fields in this example would be `["amenities", "price_per_night", "rating", "title"]`. Missing from the list is `renovation_status`.

**Note:** Including a field in the allowlist doesn't guarantee its use in natural-language query understanding. For example, if you include `id` in the allowlist, it is unlikely to be used.

To specify an allowlist of fields that can be used in a natural-language query understanding in a search, do the following:

### REST

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl command, which calls the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
           -d '{
                 "query": "QUERY",
                 "naturalLanguageQueryUnderstandingSpec": {
                   "allowedFieldNames": ["FIELD_1", "FIELD_2"],
             }
           }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: The ID of your search app. The app must be connected to a data store that contains structured data. The app can't be a blended search app.
     * `QUERY`: Your query in natural language.
     * `FIELD__N_`: An indexable field in the schema that can be used for natural-language query understanding.

#### Example command and partial response
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
      -H "Content-Type: application/json"
      "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search"
      -d '{
            "query": "A hotel with beach access for less than $150 a night.",
            "naturalLanguageQueryUnderstandingSpec": {
              "allowedFieldNames": ["amenities", "price_per_night", "rating"]
            }
      }'
    
    
    * * *
    
    
    {
      "results": [
        {
          "id": "8dbf32e3e8d289c30a7c70bf4ba68bac",
          "document": {
          "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-app/branches/0/documents/8dbf32e3e8d289c30a7c70bf4ba68bac",
            "id": "8dbf32e3e8d289c30a7c70bf4ba68bac",
            "structData": {
              "rating": 3.2,
              "location": {
                "city": "Jessicastad",
                "country": "USA",
                "zip_code": "18285",
                "state": "IA",
                "address": "552 Martin Gateway Apt. 964, Christinebury, OR 41179"
              },
              "contact": {
                "phone": "001-446-555-2265x7190",
                "email": "edwardscameron@example.com"
              },
              "amenities": [
                "Parking",
                "Beach Access",
                "Spa"
              ],
              "room_types": [
                "Double",
                "Deluxe",
                "Single"
              ],
              "id": 59,
              "title": "Williams, Richmond and Williams",
              "price_per_night": 143,
              "available_date": "2025-06-06"
            },
            "derivedStructData": {
              "clearbox_escorer_score": 0.77886492013931274,
              "can_fetch_raw_content": "true",
              "is_exact_match_query": 0
            }
          },
          "rankSignals": {
            "keywordSimilarityScore": 0.7788649,
            "semanticSimilarityScore": 0.71246886,
            "boostingFactor": 0,
            "defaultRank": 1,
            "customSignals": [
              {
                "name": "c.rating",
                "value": 3.2
              },
              {
                "name": "c.id",
                "value": 59
              },
              {
                "name": "c.price_per_night",
                "value": 143
              }
            ]
          }
        },
        ...
        {
          "id": "fd5f0b4125a9c52420510aa1aa52eaff",
          "document": {
          "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-app/branches/0/documents/fd5f0b4125a9c52420510aa1aa52eaff",
            "id": "fd5f0b4125a9c52420510aa1aa52eaff",
            "structData": {
              "amenities": [
                "Beach Access",
                "Spa",
                "Gym",
                "Pet Friendly"
              ],
              "room_types": [
                "Queen",
                "King",
                "Suite"
              ],
              "id": 277,
              "title": "Wyatt, Thomas and Price",
              "available_date": "2023-11-17",
              "contact": {
                "phone": "9745551788",
                "email": "shermandaniel@example.com"
              },
              "rating": 3.3,
              "price_per_night": 139.18,
              "location": {
                "address": "05952 Elaine Freeway, Lake Timothychester, MD 69485",
                "country": "USA",
                "state": "DC",
                "city": "North Marcusmouth",
                "zip_code": "23129"
              }
            },
            "derivedStructData": {
              "can_fetch_raw_content": "true",
              "clearbox_escorer_score": 0.77886492013931274,
              "is_exact_match_query": 0
            }
          },
          "rankSignals": {
            "keywordSimilarityScore": 0.7788649,
            "semanticSimilarityScore": 0.7304497,
            "boostingFactor": 0,
            "defaultRank": 2,
            "customSignals": [
              {
                "name": "c.rating",
                "value": 3.3
              },
              {
                "name": "c.id",
                "value": 277
              },
              {
                "name": "c.price_per_night",
                "value": 139.18
              }
            ]
          }
        }
      ],
      "totalSize": 17,
      "attributionToken": "lwL0FgEKCwj__drHBhCzzZdSEiQ2OTAwYTgzZC0wMDAwLTI5YzYtYjliMi03NDc0NDYzYjVjY2QiB0dFTkVSSUMqSJWSxTCQ97IwwvCeFZ_Wty25qqIy0NqJN9PaiTeugJM31LKdFY6-nRWc1rct4-uQN7e3jC2-kfoxjpHJMLuR-jG2qqIy4OuQNzABUowBcHJvamVjdHMvNzU2MjA2NjA4NDc5L2xvY2F0aW9ucy9nbG9iYWwvY29sbGVjdGlvbnMvZGVmYXVsdF9jb2xsZWN0aW9uL2VuZ2luZXMvaG90ZWxzLW1hbnktc2VhcmNoXzE3MjQ0NTIzNjA3NTYvc2VydmluZ0NvbmZpZ3MvZGVmYXVsdF9zZWFyY2g",
      "nextPageToken": "Q2YjVjYzYDN0cDN30iMiljYtYzY5ITLwADMw0yYzgTYwATO2QiGB0ZxBPIEGcs6m_PCMIBM1IgC",
      "guidedSearchResult": {},
      "summary": {},
      "appliedControls": [
      "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/secondbb"
      ],
      "queryExpansionInfo": {}
    }
    

This example command allows the fields `amenities`, `price_per_night`, and `rating` to be used in natural-language query filters.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
