---
url: https://docs.cloud.google.com/vision-ai/docs/warehouse-searchconfig-and-hypernyms/
title: Overview \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:47.783265+00:00
---

# Overview  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/warehouse-searchconfig-and-hypernyms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

Vision Warehouse allows users to customize their search experience through search config and search hypernym. 

## Search config

Search config can modify the search criteria and search facet behavior. We have the following four use cases for search config.

Availability:

  * Streaming Video Warehouse: All following use cases are enabled.
  * Batch Video Warehouse: Search criteria is enabled, but search facet is not enabled.
  * Image Warehouse: Search config is not available.



### Use case 1: one-to-many criteria

Users can create a customized search criteria that maps to multiple existing data schemas. For example, the following search config creates a customized search criteria, "person". When users search under the criteria "person", like searching "Mike" under criteria "person", our service will expand the "person" criteria to "player", "coach", and "cheerleader", and then search under all these data schemas. In other words, whether "Mike" is annotated as "player", "coach", or "cheerleader", related results will be returned.
    
    
    {
      name: "projects/$PROJECT_NUMBER/locations/$LOCATION_ID/corpora/$CORPUS_ID/searchConfigs/person"
      search_criteria_property {
        mapped_fields: "player"
        mapped_fields: "coach"
        mapped_fields: "cheerleader"
      }
    }
    

### Use case 2: one-to-one facet

Users can enable the search facet for an existing data schema by creating one search config on it. For example, the following search config enables the search facet for location. When users searching under "location," they can now select bucket values under "location," like "Tokyo", "London" to further narrow down search results.

Note that the search config ID, facet_property.mapped_field, and the data schema ID all need to be the same string, in this case, "location".
    
    
    {
      name: "projects/$PROJECT_NUMBER/locations/$LOCATION_ID/corpora/$CORPUS_ID/searchConfigs/location"
      facet_property {
        mapped_fields: "location",
        display_name: "A customized name for UI",
        result_size: 5,
        bucket_type: FACET_BUCKET_TYPE_VALUE
      }
    }
    

### Use case 3: one-to-many criteria and facet

Users can create a customized search criteria and also enable the search facet on it at the same time. For example, the following search config creates a customized search criteria that maps "location" to "city", "state", and "province". Meanwhile, the search facet is enabled. All bucket values from "city", "state", and "province" will be returned together.

Note that, in this case, mapped_fields of search_criteria_property and facet_property need to be identical. And they should be the ID of existing data schema.
    
    
    {
      name: "projects/$PROJECT_NUMBER/locations/$LOCATION_ID/corpora/$CORPUS_ID/searchConfigs/location"
      search_criteria_property {
        mapped_fields: "city"
        mapped_fields: "state"
        mapped_fields: "province"
      }   
      facet_property {
        mapped_fields: "city"    
        mapped_fields: "state"
        mapped_fields: "province"
        display_name: "places"
        result_size: 5,
        bucket_type: FACET_BUCKET_TYPE_VALUE
      }
    }
    

### Use case 4: range-based facet

For use case 2 and 3, we can change the bucket type of a facet to be range-based. Range-based facets are similar to normal facets, but each facet bucket covers some continuous span. Additional setting is needed to configure the continuous span.

Range facets are available for:

  * Integers
  * Dates



There are three types of range facets:

  * Fixed range: each bucket is the same size.
  * Custom range: programmable bucket sizes, for example logarithmic.
  * Date range: fixed bucket granularities of DAY, MONTH, and YEAR (only applicable for date range facets).



The following search config enables the search facet on "inventory-count" search criteria and the facet buckets will be [-inf, 0), [0, 10), [10, 20), [20, 30), [30, inf).
    
    
    {
      name: "projects/$PROJECT_NUMBER/locations/$LOCATION_ID/corpora/$CORPUS_ID/searchConfigs/inventory-count"
      facet_property {
      mapped_fields: "inventory-count"
      display_name: "Inventory Count"
      result_size: 5
      bucket_type:FACET_BUCKET_TYPE_FIXED_RANGE
      fixed_range_bucket_spec {
        bucket_start {
          integer_value: 0
        }
        bucket_granularity {
          integer_value: 10
        }
        bucket_count: 5
        }
      }
    }
    

The following search config enables the search facet on "film-date" search criteria with a DAY granularity.
    
    
    {
      name: "projects/$PROJECT_NUMBER/locations/$LOCATION_ID/corpora/$CORPUS_ID/searchConfigs/film-date"
      facet_property {
        mapped_fields: "film-date"
        display_name: "Film Date"
        result_size: 5
        bucket_type: FACET_BUCKET_TYPE_DATETIME
        datetime_bucket_spec {
          granularity: DAY
        }
      }
    }
    

## Search hypernym

Search hypernym can modify how search queries match with smart search string annotations.

Availability:

  * Streaming Warehouse: Search hypernym is enabled for global search query and smart search criteria string query.
  * VoD Warehouse: Search hypernym is enabled for smart search criteria string query.
  * Image Warehouse: Search hypernym is not available.



A search hypernym maps one hypernym to multiple hyponyms. For example, the following search hypernym maps "vehicle" to "sedan", "truck", and "suv". Searching "vehicle" in a global search query or under smart search string criteria will also match results annotated with "sedan", "truck", and "suv", as well as "vehicle".
    
    
    {
      name: "projects/$PROJECT_NUMBER/locations/$LOCATION_ID/corpora/$CORPUS_ID/searchHypernyms/car-hypernym"
      hypernym: "vehicle"
      hyponyms: "sedan"
      hyponyms: "truck"
      hyponyms: "suv"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
