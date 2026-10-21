---
url: https://docs.cloud.google.com/secret-manager/docs/locations/
title: Secret Manager locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:23.066292+00:00
---

# Secret Manager locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/secret-manager/docs/resources)



Send feedback 

#  Secret Manager locations Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager resources can be created in one of many locations. For more information about locations within Google Cloud, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

Secret Manager supports multi-region locations, but doesn't support zones or dual-region locations.

## How locations work in Secret Manager

Secrets and secret versions can be accessed globally across Google Cloud. A secret's _replication policy_ determines where the secret and its versions are stored in Google Cloud.

Secrets that use the automatic replication policy are replicated without restriction. Automatic replication is recommended for most users.

If you need more control over the locations where a secret is stored, you can choose the user-managed replication policy. With user-managed replication, you select one or more geographic locations where the secret will be replicated. For specific instructions, see [Creating secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

For more information about availability of Secret Manager resources, refer to the [service-level agreement SLA](https://docs.cloud.google.com/secret-manager/sla).

### Secret Manager regional endpoint locations

If your data is subject to data residency zone (DRZ) regulations or other compliance requirements, create and store your Secret Manager resources in a [Google Cloud location](https://cloud.google.com/about/locations) that supports regional endpoints. Regional endpoints are request endpoints that only allow requests to proceed if the affected resource exists in the location specified by the endpoint. For example, when you use the endpoint `https://secretmanager.me-central2.rep.googleapis.com` in a delete secret request, the request only proceeds if the secret is located in `ME-CENTRAL2`. Regional endpoints ensure that your data at rest and in transit remains in a specific Google Cloud location. To enforce the use of regional endpoints, you can set an organization policy. Learn more in [Restricting endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage). For information about creating regional secrets, see [Create regional secrets](https://docs.cloud.google.com/secret-manager/docs/create-regional-secrets).

### Parameter Manager regional endpoint locations

[Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview) is an extension to the Secret Manager service that lets you create, store, and manage your application parameters. You can create Parameter Manager resources in a [global](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations#location_types) location, a [multi-region](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations#location_types) location, or [in a specific data location with the help of a regional endpoint](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter).

The following table lists the [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) or specific geographical locations where you can access the Secret Manager global service. Additionally, it identifies the locations where the regionalized Secret Manager and Parameter Manager services are available.

## Locations in Asia Pacific

The following table lists the locations in Asia Pacific where regional Secret Manager and Parameter Manager resources can be stored.

Region | Regional Secret Manager | Parameter Manager  
---|---|---  
`asia-south2` (Delhi) | Yes | Yes  
`asia-east2` (Hong Kong) | Yes | Yes  
`asia-southeast2` (Jakarta) | Yes | No  
`australia-southeast2` (Melbourne) | Yes | Yes  
`asia-south1` (Mumbai) | Yes | Yes  
`asia-northeast2` (Osaka) | Yes | Yes  
`asia-northeast3` (Seoul) | Yes | Yes  
`asia-southeast1` (Singapore) | Yes | No  
`australia-southeast1` (Sydney) | Yes | Yes  
`asia-east1` (Taiwan) | Yes | Yes  
`asia-northeast1` (Tokyo) | Yes | Yes  
`asia-southeast3` (Bangkok) | Yes | No  
  
## Locations in Europe

The following table lists the locations in Europe where regional Secret Manager and Parameter Manager resources can be stored.

Region | Regional Secret Manager | Parameter Manager  
---|---|---  
`europe-west1` (Belgium) | Yes | Yes  
`europe-west10` (Berlin) | Yes | No  
`europe-north1` (Finland) | No | No  
`europe-north2` (Stockholm) | Yes | No  
`europe-west3` (Frankfurt) | Yes | Yes  
`europe-west2` (London) | Yes | Yes  
`europe-southwest1` (Madrid) | Yes | Yes  
`europe-west8` (Milan) | Yes | Yes  
`europe-west4` (Netherlands) | Yes | Yes  
`europe-west12` (Turin) | Yes | No  
`europe-west9` (Paris) | Yes | Yes  
`europe-central2` (Warsaw) | Yes | Yes  
`europe-west6` (Zurich) | Yes | Yes  
  
## Locations in North America

The following table lists the locations in North America where regional Secret Manager and Parameter Manager resources can be stored.

Region | Regional Secret Manager | Parameter Manager  
---|---|---  
`us-central1` (Iowa) | Yes | Yes  
`us-west4` (Las Vegas) | Yes | Yes  
`us-west2` (Los Angeles) | Yes | Yes  
`northamerica-south1` (Mexico) | Yes | Yes  
`northamerica-northeast1` (Montréal) | Yes | Yes  
`us-east4` (Northern Virginia) | Yes | Yes  
`us-west1` (Oregon) | Yes | Yes  
`us-west3` (Salt Lake City) | Yes | Yes  
`us-east1` (South Carolina) | Yes | Yes  
`northamerica-northeast2` (Toronto) | Yes | Yes  
`us-east5` (Columbus) | Yes | Yes  
`us-south1` (Dallas) | Yes | Yes  
  
## Locations in South America

The following table lists the locations in South America where regional Secret Manager resources can be stored.

Region | Regional Secret Manager | Parameter Manager  
---|---|---  
`southamerica-east1` (São Paulo) | Yes | Yes  
`southamerica-west1` (Santiago) | Yes | Yes  
  
## Locations in Middle East

The following table lists the locations in the Middle East where regional Secret Manager and Parameter Manager resources can be stored.

Region | Regional Secret Manager | Parameter Manager  
---|---|---  
`me-central2` (Dammam) | Yes | No  
`me-central1` (Doha) | Yes | Yes  
`me-west1` (Tel Aviv) | Yes | Yes  
  
## Locations in Africa

The following table lists the locations in Africa where regional Secret Manager and Parameter Manager resources can be stored.

Region | Regional Secret Manager | Parameter Manager  
---|---|---  
`africa-south1` (Johannesburg) | Yes | Yes  
  
## Available multi-region locations

The following table lists the multi-region locations where regional Secret Manager and Parameter Manager resources can be stored.

Multi-region locations are data centers spread across a general geographical area. For example, a resource created in the `eu` multi-region is stored in multiple data centers within the European Union. You cannot select specific data centers within a multi-region.

Multi-Region Name | Multi-Region Description | Regional Secret Manager | Parameter Manager  
---|---|---|---  
`us` | Data centers in the United States | Yes | Yes  
`eu` | Data centers in the European Union | Yes | Yes  
`ca` | Data centers in the Canada | Yes | Yes  
`in` | Data centers in the India | Yes | Yes  
  
## What's next

  * Learn more about [locations](https://cloud.google.com/about/locations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
