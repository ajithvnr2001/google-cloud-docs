---
url: https://docs.cloud.google.com/location-finder/docs/syntax/
title: Query and filter syntax for Cloud Location Finder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:44.676531+00:00
---

# Query and filter syntax for Cloud Location Finder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/location-finder/docs/syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Cloud Location Finder ](https://docs.cloud.google.com/location-finder/docs)
  * [ Guides ](https://docs.cloud.google.com/location-finder/docs/overview)



Send feedback 

#  Query and filter syntax for Cloud Location Finder Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the query and filter syntax that Cloud Location Finder uses to return cloud locations based on territory, proximity, and [carbon free energy (CFE%)](https://cloud.google.com/sustainability/region-carbon) usage. For more information, see the [REST API reference](https://docs.cloud.google.com/location-finder/docs/reference/rest).

**Note:** Field names in filters require snake case.Field | Supported operators | Description | Example  
---|---|---|---  
carbon_free_energy_percentage | >, < | Matches the carbon free energy percentage as defined by Google.  
CFE% only supported for Google Cloud locations. | `carbon_free_energy_percentage > 75`  
cloud_location_type | =, != | Matches a Cloud location type using an enum. | `cloud_location_type = CLOUD_LOCATION_TYPE_REGION`  
cloud_provider | =, != | Matches a Cloud provider using an enum. | `cloud_provider = CLOUD_PROVIDER_GCP`  
containing_cloud_location | =, != | Matches containing CloudLocation by full resource name. | `containing_cloud_location = "projects/clf-e2e-testing/locations/global/cloudLocations/aws-us-east-1"`  
display_name | =, != | Matches a CloudLocation's display_name by full name. | `display_name = "us-east-1"`  
latency | >, < | Matches the latency criteria using an integer based on RTT measurements with a unit of ms. | `latency < 50`  
territory_code | =, != | Matches a [two-letter ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search/code/) code. Two-letter code must be fully capitalized. | `territory_code = \"US\"`  
  
## Example filter

This example filter illustrates the format to use when including a filter in Cloud Location Finder HTTP or Google Cloud CLI queries.

### HTTP
    
    
    filter=cloud_provider=CLOUD_PROVIDER_GCP%20AND%20cloud_location_type=CLOUD_LOCATION_TYPE_ZONE
    

### gcloud
    
    
    --filter="cloud_provider=CLOUD_PROVIDER_GCP AND cloud_location_type=CLOUD_LOCATION_TYPE_ZONE"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
