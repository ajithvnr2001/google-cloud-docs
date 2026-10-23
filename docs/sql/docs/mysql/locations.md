---
url: https://docs.cloud.google.com/sql/docs/mysql/locations/
title: Manage instance locations \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:20.429189+00:00
---

# Manage instance locations  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Manage instance locations Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/locations "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/locations "View this page for the SQL Server database engine")

This page discusses the options for placing your instances in Google Cloud locations.

When you create a Cloud SQL instance, you choose a [region](https://docs.cloud.google.com/docs/geography-and-regions) where the instance and its data are stored. To reduce latency and increase availability, choose the same region for your data and your Compute Engine instances, standard environment applications, and other services.

There are different location types:

A regional location is a specific geographic place, such as London.

A multi-regional location is a large geographic area, such as the United States, that contains at least two geographic places. Multi-regional locations are only used for backups.

**Note:** Some organizations use an organization policy to restrict resource locations. If this type of policy affects your project, you can only select regions the organization policy allows. In the **Location** drop-down menu in the Console, the locations that are not allowed are unavailable. [ Learn more](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 

You choose a location when you first create the instance. The location can't be changed after the instance is created.

## Regional Locations

Regional locations are specific geographic locations within a multi-region location. Cloud SQL is available in all Google Cloud regions and is offered in upcoming regional launches at the time of launch. You can create a Cloud SQL instance in the following regions:

| Region Name | Region Description |   
---|---|---|---  
**Africa** |  |  |   
| `africa-south1` | Johannesburg |   
**Asia** |  |  |   
| `asia-east1` | Taiwan |   
| `asia-east2` | Hong Kong |   
| `asia-northeast1` | Tokyo |   
| `asia-northeast2` | Osaka |   
| `asia-northeast3` | Seoul |   
| `asia-south1` | Mumbai |   
| `asia-south2` | Delhi |   
| `asia-southeast1` | Singapore |   
| `asia-southeast2` | Jakarta |   
| `asia-southeast3` | Bangkok |   
**Australia** |  |  |   
| `australia-southeast1` | Sydney |   
| `australia-southeast2` | Melbourne |   
**Europe** |  |  |   
| `europe-central2` | Warsaw |   
| `europe-north1` | Finland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-southwest1` | Madrid |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west1` | Belgium |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west2` | London |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt |   
| `europe-west4` | Netherlands |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west6` | Zürich |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west8` | Milan |   
| `europe-west9` | Paris |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west10` | Berlin |   
| `europe-west12` | Turin |   
**Middle East** |  |  |   
| `me-central1` | Doha |   
| `me-central2` | Dammam |   
| `me-west1` | Tel Aviv |   
**North America** |  |  |   
| `northamerica-northeast1` | Montréal |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `northamerica-northeast2` | Toronto |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `northamerica-south1` | Mexico |   
| `us-central1` | Iowa |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-south1` | Dallas |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-east1` | South Carolina |   
| `us-east4` | Northern Virginia |   
| `us-east5` | Columbus |   
| `us-west1` | Oregon |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-west2` | Los Angeles |   
| `us-west3` | Salt Lake City |   
| `us-west4` | Las Vegas |   
**South America** |  |  |   
| `southamerica-east1` | São Paulo |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `southamerica-west1` | Santiago |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
### Multi-regional backup locations

Multi-Region Name | Multi-Region Description  
---|---  
`asia` | Data centers in Asia, excluding Hong Kong and Indonesia  
`eu` | Data centers within [member states](https://europa.eu/european-union/about-eu/countries_en) of the European Union*  
`us` | Data centers in the United States  
  
* Backup data stored in the `eu` multi-region is not stored in the `europe-west2` (London) or `europe-west6` (Zürich) regions.

## Zones

Zones are sub-locations in a region where you can create zonal resources such as Cloud SQL instances. For example, a zone named `us-central1-a` indicates a zone within the `us-central1` region. A zone is independent of other zones in the same region.

You can choose your zone to keep your Cloud SQL instance close to your other Google Cloud services. If you want your instance to be replicated between zones synchronously, then [configure it for high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability).

When you first create the instance, you can add a zone. To modify this zone, you can [edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).

## Preferred Location

You can select your zone. Choose **Any** if you want the system to select and assign a zone for you during instance creation.

For more information about zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## What's next

  * Get more information about [building applications to meet your latency, availability, and durability requirements](https://docs.cloud.google.com/docs/geography-and-regions).
  * View all the [Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
