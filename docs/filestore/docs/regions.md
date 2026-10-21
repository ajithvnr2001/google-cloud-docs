---
url: https://docs.cloud.google.com/filestore/docs/regions/
title: Regions and zones \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:14.911375+00:00
---

# Regions and zones  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Regions and zones Stay organized with collections  Save and categorize content based on your preferences. 

Filestore instances live in zones within regions. A region is a specific geographical location where you can run your resources. Each region is subdivided into several zones. For example, the `us-central1` region in the central United States has zones `us-central1-a`, `us-central1-b`, `us-central1-c`, and `us-central1-f`. For more information, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

Some Google Cloud APIs, including the [Filestore API](https://docs.cloud.google.com/filestore/docs/reference/rest), use the concept of locations, which can represent either [regions or zones](https://docs.cloud.google.com/storage/docs/locations#key-concepts). For Filestore instances, locations map to zones.

To decrease network latency, we recommend creating a Filestore instance in a region and zone that is close to where you plan to use it. For example, if you plan to access the instance from Asia, then you should create it in one of the `asia-east1` zones. Similarly, you get the best performance by mounting Filestore file shares on clients in the same region.

## Supported regions

For more information on region specific considerations, see the [Geography & Regions](https://cloud.google.com/about/locations) page.

Filestore is available in the following regions and zones.

###  Africa 

Region Description | Region Name | Zones  
---|---|---  
Johannesburg | `africa-south1` | 

  * `africa-south1-a`
  * `africa-south1-b`
  * `africa-south1-c`

  
  
###  Asia 

Region Description | Region Name | Zones  
---|---|---  
Taiwan | `asia-east1` | 

  * `asia-east1-a`
  * `asia-east1-b`
  * `asia-east1-c`

  
Hong Kong | `asia-east2` | 

  * `asia-east2-a`
  * `asia-east2-b`
  * `asia-east2-c`

  
Tokyo | `asia-northeast1` | 

  * `asia-northeast1-a`
  * `asia-northeast1-b`
  * `asia-northeast1-c`

  
Osaka | `asia-northeast2` | 

  * `asia-northeast2-a`
  * `asia-northeast2-b`
  * `asia-northeast2-c`

  
Seoul | `asia-northeast3` | 

  * `asia-northeast3-a`
  * `asia-northeast3-b`
  * `asia-northeast3-c`

  
Singapore | `asia-southeast1` | 

  * `asia-southeast1-a`
  * `asia-southeast1-b`
  * `asia-southeast1-c`

  
Bangkok | `asia-southeast3` | 

  * `asia-southeast3-a`
  * `asia-southeast3-b`
  * `asia-southeast3-c`

  
  
###  Australia 

Region Description | Region Name | Zones  
---|---|---  
Sydney | `australia-southeast1` | 

  * `australia-southeast1-a`
  * `australia-southeast1-b`
  * `australia-southeast1-c`

  
Melbourne | `australia-southeast2` | 

  * `australia-southeast2-a`
  * `australia-southeast2-b`
  * `australia-southeast2-c`

  
  
###  Europe 

Region Description | Region Name | Zones  
---|---|---  
Warsaw | `europe-central2` | 

  * `europe-central2-a`
  * `europe-central2-b`
  * `europe-central2-c`

  
Finland | `europe-north1` | 

  * `europe-north1-a`
  * `europe-north1-b`
  * `europe-north1-c`

  
Stockholm | `europe-north2` | 

  * `europe-north2-a`
  * `europe-north2-b`
  * `europe-north2-c`

  
Madrid | `europe-southwest1` | 

  * `europe-southwest1-a`
  * `europe-southwest1-b`
  * `europe-southwest1-c`

  
Belgium | `europe-west1` | 

  * `europe-west1-b`
  * `europe-west1-c`
  * `europe-west1-d`

  
London | `europe-west2` | 

  * `europe-west2-a`
  * `europe-west2-b`
  * `europe-west2-c`

  
Frankfurt | `europe-west3` | 

  * `europe-west3-a`
  * `europe-west3-b`
  * `europe-west3-c`

  
Netherlands | `europe-west4` | 

  * `europe-west4-a`
  * `europe-west4-b`
  * `europe-west4-c`

  
Zurich | `europe-west6` | 

  * `europe-west6-a`
  * `europe-west6-b`
  * `europe-west6-c`

  
Milan | `europe-west8` | 

  * `europe-west8-a`
  * `europe-west8-b`
  * `europe-west8-c`

  
Paris | `europe-west9` | 

  * `europe-west9-a`
  * `europe-west9-b`
  * `europe-west9-c`

  
Berlin | `europe-west10` | 

  * `europe-west10-a`
  * `europe-west10-b`
  * `europe-west10-c`

  
Turin | `europe-west12` | 

  * `europe-west12-a`
  * `europe-west12-b`
  * `europe-west12-c`

  
  
###  India 

Region Description | Region Name | Zones  
---|---|---  
Mumbai | `asia-south1` | 

  * `asia-south1-a`
  * `asia-south1-b`
  * `asia-south1-c`

  
Delhi | `asia-south2` | 

  * `asia-south2-a`
  * `asia-south2-b`
  * `asia-south2-c`

  
  
###  Indonesia 

Region Description | Region Name | Zones  
---|---|---  
Jakarta | `asia-southeast2` | 

  * `asia-southeast2-a`
  * `asia-southeast2-b`
  * `asia-southeast2-c`

  
  
###  Middle East

Region Description | Region Name | Zones  
---|---|---  
Doha | `me-central1` | 

  * `me-central1-a`
  * `me-central1-b`
  * `me-central1-c`

  
Dammam | `me-central2` | 

  * `me-central2-a`
  * `me-central2-b`
  * `me-central2-c`

  
Tel Aviv | `me-west1` | 

  * `me-west1-a`
  * `me-west1-b`
  * `me-west1-c`

  
  
###  North America 

Region Description | Region Name | Zones  
---|---|---  
Montréal | `northamerica-northeast1` | 

  * `northamerica-northeast1-a`
  * `northamerica-northeast1-b`
  * `northamerica-northeast1-c`

  
Toronto | `northamerica-northeast2` | 

  * `northamerica-northeast2-a`
  * `northamerica-northeast2-b`
  * `northamerica-northeast2-c`

  
Mexico | `northamerica-south1` | 

  * `northamerica-south1-a`
  * `northamerica-south1-b`
  * `northamerica-south1-c`

  
Iowa | `us-central1` | 

  * `us-central1-a`
  * `us-central1-b`
  * `us-central1-c`
  * `us-central1-f`

  
South Carolina | `us-east1` | 

  * `us-east1-b`
  * `us-east1-c`
  * `us-east1-d`

  
Northern Virginia | `us-east4` | 

  * `us-east4-a`
  * `us-east4-b`
  * `us-east4-c`

  
Columbus | `us-east5` | 

  * `us-east5-a`
  * `us-east5-b`
  * `us-east5-c`

  
Dallas | `us-south1` | 

  * `us-south1-a`
  * `us-south1-b`
  * `us-south1-c`

  
Oregon | `us-west1` | 

  * `us-west1-a`
  * `us-west1-b`
  * `us-west1-c`

  
Los Angeles | `us-west2` | 

  * `us-west2-a`
  * `us-west2-b`
  * `us-west2-c`

  
Salt Lake City | `us-west3` | 

  * `us-west3-a`
  * `us-west3-b`
  * `us-west3-c`

  
Las Vegas | `us-west4` | 

  * `us-west4-a`
  * `us-west4-b`
  * `us-west4-c`

  
  
###  South America 

Region Description | Region Name | Zones  
---|---|---  
São Paulo | `southamerica-east1` | 

  * `southamerica-east1-a`
  * `southamerica-east1-b`
  * `southamerica-east1-c`

  
Santiago | `southamerica-west1` | 

  * `southamerica-west1-a`
  * `southamerica-west1-b`
  * `southamerica-west1-c`

  
  
## Next steps

  * Get started using Filestore by [installing and enabling Filestore components](https://docs.cloud.google.com/filestore/docs/install).
  * Learn more about Filestore's [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers) to decide which service tier is right for you.
  * Learn more about Filestore in the [Technical overview](https://docs.cloud.google.com/filestore/docs/overview).
  * Learn how to better protect your data with features like [dual-region storage](https://docs.cloud.google.com/storage/docs/locations#location-dr) and [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
