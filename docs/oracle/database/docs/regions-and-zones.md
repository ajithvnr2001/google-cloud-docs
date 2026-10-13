---
url: https://docs.cloud.google.com/oracle/database/docs/regions-and-zones/
title: Supported regions and zones \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:52.625638+00:00
---

# Supported regions and zones  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/regions-and-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Supported regions and zones Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Oracle Database@Google Cloud regional and zonal resources, and lists supported Google Cloud regions and zones.

Oracle Database@Google Cloud resources are hosted in multiple locations worldwide. These locations are composed of regions and zones. Regions are independent geographic areas that consist of zones. Resources that live in a zone are referred to as zonal resources. Regional resources can be used by any resource in that region, regardless of zone.

The Oracle Database@Google Cloud zones are called _GCP Oracle zones_.

## Regional and zonal resources

Oracle Database@Google Cloud resources are either regional or zonal. The scope of the resource determines where it is provisioned. For example, zonal resources can be placed together in the same location, and regional resources can run in any zone. However, all resources, whether regional or zonal, must be unique within the project. That means every resource in Oracle Database@Google Cloud must be uniquely named across the project.

The following Oracle Database@Google Cloud resources are regional resources:

  * [Autonomous AI Databases](https://docs.cloud.google.com/oracle/database/docs/create-databases)



The following Oracle Database@Google Cloud resources are zonal resources:

  * [Exadata Infrastructures](https://docs.cloud.google.com/oracle/database/docs/create-instances)
  * [Exadata VM Clusters](https://docs.cloud.google.com/oracle/database/docs/create-clusters)
  * [Exascale VM Clusters and Exascale Storage Vaults](https://docs.cloud.google.com/oracle/database/docs/create-exascale-clusters)
  * [ODB Networks and ODB Subnets](https://docs.cloud.google.com/oracle/database/docs/create-odb-network)
  * [DB systems](https://docs.cloud.google.com/oracle/database/docs/create-base-db-system)
  * [Goldengate deployments](https://docs.cloud.google.com/oracle/database/docs/deploy-and-connect)



## Choosing a region and zone

You choose which region or zone hosts your resources, which controls where your data is stored and used. You must create your ODB Network and other zonal resources, including Exadata Infrastructure, Exadata VM Clusters, and DB system in the same region and zone to ensure optimal performance and seamless communication.

## Available regions and zones

Oracle Database@Google Cloud is available in the following regions based on your selected Oracle Cloud Infrastructure (OCI) service type:

  * Exadata Database Service
  * Base Database Service
  * Exadata Database Service on Exascale Infrastructure
  * Autonomous AI Database Service
  * Goldengate



### Exadata Database Service regions and zones

You can create Exadata Database and Exadata VM Clusters resources in the following regions and zones:

| Region Name | Region Description | Zone |   
---|---|---|---|---  
**Asia Pacific** |  |  |  |   
| `asia-northeast1` | Tokyo, Japan | `asia-northeast1-a-r1` |   
| `asia-northeast2` | Osaka, Japan | `asia-northeast2-a-r1` |   
| `australia-southeast1` | Sydney, Australia | `australia-southeast1-b-r1` |   
| `australia-southeast2` | Melbourne, Australia | `australia-southeast2-a-r2`  
`australia-southeast2-b-r1` |   
| `asia-south1` | Mumbai, India | `asia-south1-b-r1` |   
| `asia-south2` | Delhi, India | `asia-south2-b-r1` |   
**North America** |  |  |  |   
| `northamerica-northeast1` | Montréal, Québec, Canada | `northamerica-northeast1-a-r1` |   
| `northamerica-northeast2` | Toronto, Ontario, Canada | `northamerica-northeast2-a-r2` |   
| `us-central1` | Iowa | `us-central1-a-r1` |   
| `us-east4` | Northern Virginia | `us-east4-a-r2`  
`us-east4-b-r1` |   
| `us-west3` | Salt Lake City | `us-west3-a-r1` |   
**South America** |  |  |  |   
| `southamerica-east1` | São Paulo, Brazil, South America | `southamerica-east1-a-r1` |   
**Europe** |  |  |  |   
| `europe-west2` | London , England | `europe-west2-a-r1`  
`europe-west2-c-r2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt, Germany | `europe-west3-a-r2`  
`europe-west3-b-r1` |   
| `europe-west8` | Milan, Italy | `europe-west8-b-r1`  
`europe-west8-a-r1` |   
| `europe-west12` | Turin, Italy | `europe-west12-a-r1` |   
  
### Exadata Database Service on Exascale Infrastructure regions and zones

You can create Exascale VM Clusters and Exascale Storage Vaults in the following regions and zones:

| Region Name | Region Description | Zone |   
---|---|---|---|---  
**Asia Pacific** |  |  |  |   
| `asia-northeast1` | Tokyo, Japan | `asia-northeast1-a-r1` |   
| `asia-northeast2` | Osaka, Japan | `asia-northeast2-a-r1` |   
| `australia-southeast2` | Melbourne, Australia | `australia-southeast2-a-r2` |   
| `asia-south1` | Mumbai, India | `asia-south1-b-r1` |   
| `asia-south2` | Delhi, India | `asia-south2-b-r1` |   
**North America** |  |  |  |   
| `northamerica-northeast1` | Montréal, Québec, Canada | `northamerica-northeast1-a-r1` |   
| `us-central1` | Iowa | `us-central1-a-r1` |   
| `us-east4` | Northern Virginia | `us-east4-a-r2`  
`us-east4-b-r1` |   
| `us-west3` | Salt Lake City | `us-west3-a-r1` |   
**Europe** |  |  |  |   
| `europe-west2` | London, England | `europe-west2-a-r1`  
`europe-west2-c-r2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt, Germany | `europe-west3-a-r2`  
`europe-west3-b-r1` |   
| `europe-west8` | Milan, Italy | `europe-west8-b-r1`  
`europe-west8-a-r1` |   
  
### Base Database Service regions and zones

You can create DB systems resources in the following regions and zones:

| Region Name | Region Description | Zone |   
---|---|---|---|---  
**Asia Pacific** |  |  |  |   
| `asia-northeast1` | Tokyo, Japan | `asia-northeast1-a-r1` |   
| `asia-northeast2` | Osaka, Japan | `asia-northeast2-a-r1` |   
| `australia-southeast2` | Melbourne, Australia | `australia-southeast2-a-r2` |   
| `asia-south1` | Mumbai, India | `asia-south1-b-r1` |   
| `asia-south2` | Delhi, India | `asia-south2-b-r1` |   
**North America** |  |  |  |   
| `northamerica-northeast1` | Montréal, Québec, Canada | `northamerica-northeast1-a-r1` |   
| `us-central1` | Iowa | `us-central1-a-r1` |   
| `us-east4` | Northern Virginia | `us-east4-a-r2`  
`us-east4-b-r1` |   
| `us-west3` | Salt Lake City | `us-west3-a-r1` |   
**Europe** |  |  |  |   
| `europe-west2` | London, England | `europe-west2-a-r1`  
`europe-west2-c-r2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt, Germany | `europe-west3-a-r2`  
`europe-west3-b-r1` |   
| `europe-west8` | Milan, Italy | `europe-west8-b-r1`  
`europe-west8-a-r1` |   
  
### Autonomous AI Database Service regions

You can create Autonomous AI Database resources in the following regions:

| Region Name | Region Description |   
---|---|---|---  
**Asia Pacific** |  |  |   
| `asia-northeast1` | Tokyo, Japan |   
| `asia-northeast2` | Osaka, Japan |   
| `australia-southeast1` | Sydney, Australia |   
| `australia-southeast2` | Melbourne, Australia |   
| `asia-south1` | Mumbai, India |   
| `asia-south2` | Delhi, India |   
**North America** |  |  |   
| `northamerica-northeast1` | Montréal, Québec, Canada |   
| `northamerica-northeast2` | Toronto, Ontario, Canada |   
| `us-central1` | Iowa |   
| `us-east4` | Northern Virginia |   
| `us-west3` | Salt Lake City |   
**South America** |  |  |   
| `southamerica-east1` | São Paulo, Brazil, South America |   
**Europe** |  |  |   
| `europe-west2` | London, England |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt, Germany |   
| `europe-west8` | Milan, Italy |   
  
### Goldengate regions and zones

You can create Goldengate resources in the following regions and zones:

| Region Name | Region Description | Zone |   
---|---|---|---|---  
**Asia Pacific** |  |  |  |   
| `asia-northeast1` | Tokyo, Japan | `asia-northeast1-a-r1` |   
| `asia-northeast2` | Osaka, Japan | `asia-northeast2-a-r1` |   
| `australia-southeast1` | Sydney, Australia | `australia-southeast1-b-r1` |   
| `australia-southeast2` | Melbourne, Australia | `australia-southeast2-a-r2`  
`australia-southeast2-b-r1` |   
| `asia-south1` | Mumbai, India | `asia-south1-b-r1` |   
| `asia-south2` | Delhi, India | `asia-south2-b-r1` |   
**North America** |  |  |  |   
| `northamerica-northeast1` | Montréal, Québec, Canada | `northamerica-northeast1-a-r1` |   
| `northamerica-northeast2` | Toronto, Ontario, Canada | `northamerica-northeast2-a-r2` |   
| `us-central1` | Iowa | `us-central1-a-r1` |   
| `us-east4` | Northern Virginia | `us-east4-a-r2`  
`us-east4-b-r1` |   
| `us-west3` | Salt Lake City | `us-west3-a-r1` |   
**South America** |  |  |  |   
| `southamerica-east1` | São Paulo, Brazil, South America | `southamerica-east1-a-r1` |   
**Europe** |  |  |  |   
| `europe-west2` | London, England | `europe-west2-a-r1`  
`europe-west2-c-r2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt, Germany | `europe-west3-a-r2`  
`europe-west3-b-r1` |   
| `europe-west8` | Milan, Italy | `europe-west8-b-r1`  
`europe-west8-a-r1` |   
  
## What's next?

  * [Place an order for Oracle Database@Google Cloud](https://docs.cloud.google.com/oracle/database/docs/overview#place-an-order)
  * [Create Exadata Infrastructure instances](https://docs.cloud.google.com/oracle/database/docs/create-instances)
  * [Create Exadata VM Clusters](https://docs.cloud.google.com/oracle/database/docs/create-clusters)
  * [Create Exascale VM Clusters](https://docs.cloud.google.com/oracle/database/docs/create-exascale-clusters)
  * [Create Autonomous AI Database resources](https://docs.cloud.google.com/oracle/database/docs/create-databases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
