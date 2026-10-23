---
url: https://docs.cloud.google.com/alloydb/docs/locations/
title: AlloyDB locations \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:55.659616+00:00
---

# AlloyDB locations  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Resources ](https://docs.cloud.google.com/alloydb/docs/resources)



Send feedback 

#  AlloyDB locations Stay organized with collections  Save and categorize content based on your preferences. 

When you [create an AlloyDB cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create), you must choose a _location_ where the cluster's instances will be created. You cannot change the location after you create the cluster.

In AlloyDB, you choose the location by specifying a Google Cloud [_region_](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). For highly available (regional) clusters, AlloyDB automatically manages resources across _zones_ in that region. For zonal instances, you can optionally specify a target Compute Engine zone using the [`gceZone`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances) API parameter (or [`gce_zone`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance#gce_zone) in Terraform). If you don't specify a zone, AlloyDB automatically selects one with available capacity.

To reduce latency and increase availability, store your data close to the users and services that need it. For example, if you frequently write data to AlloyDB from a Cloud Storage bucket in the `us-central1` (Iowa) region, create your AlloyDB cluster in the `us-central1` region.

The following sections list the regions that AlloyDB is available in.

## Americas

Region Name | Region Description | Low CO2  
---|---|---  
`northamerica-northeast1` | Montreal |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-northeast2` | Toronto |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-south1` | Mexico |   
`southamerica-east1` | Brazil |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`southamerica-west1` | Santiago |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1` | Iowa |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-east1` | South Carolina |   
`us-east4` | Northern Virginia |   
`us-east5` | Columbus |   
`us-south1` | Dallas |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west1` | Oregon |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west2` | Los Angeles |   
`us-west3` | Salt Lake City |   
`us-west4` | Las Vegas |   
  
## Europe

Region Name | Region Description | Low CO2  
---|---|---  
`europe-central2` | Warsaw |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-southwest1` | Madrid |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north1` | Finland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north2` | Stockholm |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west1` | Belgium |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west2` | London |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west3` | Frankfurt |   
`europe-west4` | Netherlands |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west6` | Zurich |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west8` | Milan |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west9` | Paris |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west10` | Berlin |   
`europe-west12` | Turin |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
## Asia

Region Name | Region Description | Low CO2  
---|---|---  
`asia-east1` | Taiwan |   
`asia-east2` | Hong Kong |   
`asia-northeast1` | Tokyo |   
`asia-northeast2` | Osaka |   
`asia-northeast3` | Seoul |   
`asia-south1` | Mumbai |   
`asia-south2` | Delhi |   
`asia-southeast1` | Singapore |   
`asia-southeast2` | Jakarta |   
`asia-southeast3` | Bangkok |   
  
## Australia

Region Name | Region Description | Low CO2  
---|---|---  
`australia-southeast1` | Sydney |   
`australia-southeast2` | Melbourne |   
  
## Middle East

Region Name | Region Description | Low CO2  
---|---|---  
`me-central1` | Doha |   
`me-central2` | Dammam |   
`me-west1` | Tel Aviv |   
  
## Africa

Region Name | Region Description | Low CO2  
---|---|---  
`africa-south1` | Johannesburg |   
  
## What's next

  * [Create an AlloyDB cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create).
  * Learn more about Google Cloud [geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).
  * View a [map of Google Cloud locations](https://docs.cloud.google.com/about/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
