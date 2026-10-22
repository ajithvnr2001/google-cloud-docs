---
url: https://docs.cloud.google.com/healthcare-api/docs/regions/
title: Regions \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:59.089104+00:00
---

# Regions  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Regions Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud uses [regions, subdivided into zones](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), to define the geographic location of physical computing resources.

## Key concepts

You specify a location for storing your Cloud Healthcare API data when you create a dataset. After you create the dataset, the location cannot be changed. Data within the dataset is stored at rest in the chosen location.

The location is tied to the dataset's identity and is a permanent part of the dataset's [resource name](https://docs.cloud.google.com/healthcare-api/docs/concepts/api-structure#resource_names). All data stores within the dataset are assigned to the same region as the dataset.

There are two types of locations:

  * A _regional location_ is a specific geographic place, such as Tokyo. For more information, see [Regional resources](https://docs.cloud.google.com/docs/geography-and-regions#regional_resources) on the Geography and Regions page.

  * A _multi-regional location_ is a large geographic area, such as the United States, that contains at least two regional locations. For more information, see [Multi-regional resources](https://docs.cloud.google.com/docs/geography-and-regions#multiregional_resources) on the Geography and Regions page.




## Available regions

The Cloud Healthcare API supports a subset of the [full list of Google Cloud locations](https://cloud.google.com/about/locations).

The Cloud Healthcare API is available in the following regions:

### Regional locations

| Region name | Region description  
---|---|---  
**Americas** |  |   
| [`northamerica-northeast1`](https://cloud.google.com/about/locations#americas) | Montréal  
| [`northamerica-northeast2`](https://cloud.google.com/about/locations#americas) | Toronto  
| [`us-central1`](https://cloud.google.com/about/locations#americas) | Iowa  
| [`us-east1`](https://cloud.google.com/about/locations#americas) | South Carolina  
| [`us-east4`](https://cloud.google.com/about/locations#americas) | North Virginia  
| [`us-west1`](https://cloud.google.com/about/locations#americas) | Oregon  
| [`us-west2`](https://cloud.google.com/about/locations#americas) | Los Angeles  
| [`us-west3`](https://cloud.google.com/about/locations#americas) | Salt Lake City  
| [`southamerica-east1`](https://cloud.google.com/about/locations#americas) | São Paulo  
**Asia Pacific** |  |   
| [`asia-east1`](https://cloud.google.com/about/locations#asia-pacific) | Taiwan  
| [`asia-east2`](https://cloud.google.com/about/locations#asia-pacific) | Hong Kong  
| [`asia-northeast1`](https://cloud.google.com/about/locations#asia-pacific) | Tokyo  
| [`asia-northeast2`](https://cloud.google.com/about/locations#asia-pacific) | Osaka  
| [`asia-northeast3`](https://cloud.google.com/about/locations#asia-pacific) | Seoul  
| [`asia-south1`](https://cloud.google.com/about/locations#asia-pacific) | Mumbai  
| [`asia-southeast1`](https://cloud.google.com/about/locations#asia-pacific) | Singapore  
| [`asia-southeast2`](https://cloud.google.com/about/locations#asia-pacific) | Jakarta  
| [`australia-southeast1`](https://cloud.google.com/about/locations#asia-pacific) | Sydney  
| [`australia-southeast2`](https://cloud.google.com/about/locations#asia-pacific) | Melbourne  
**Europe** |  |   
| [`europe-north1`](https://cloud.google.com/about/locations#europe) | Finland  
| [`europe-west2`](https://cloud.google.com/about/locations#europe) | London  
| [`europe-west3`](https://cloud.google.com/about/locations#europe) | Frankfurt  
| [`europe-west4`](https://cloud.google.com/about/locations#europe) | Netherlands  
| [`europe-west6`](https://cloud.google.com/about/locations#europe) | Zurich  
**Middle East** |  |   
| [`me-west1`](https://cloud.google.com/about/locations#middle-east) | Tel Aviv  
| [`me-central1`](https://cloud.google.com/about/locations#middle-east) | Doha  
| [`me-central2`](https://cloud.google.com/about/locations#middle-east) | Dammam  
  
### Multi-regional locations

Multi-region name | Multi-region description  
---|---  
[`us`](https://cloud.google.com/about/locations/?region=multi-region#multi-region) | Data centers in the United States  
[`eu`](https://cloud.google.com/about/locations/?region=multi-region#multi-region) | Data centers within member states of the European Union  
  
## Location quota requests

You can request a quota increase for the Cloud Healthcare API in a specific [region](https://docs.cloud.google.com/healthcare-api/docs/regions), or in a [multi-region location](https://docs.cloud.google.com/healthcare-api/docs/regions#multi-regional_locations).

To request a quota increase in a single region: In your quota increase request, specify the region.

To request a quota increase in a multi-region location:

  * For a quota increase in the `us` multi-region, state in your request that the quota is for "US meta region."
  * For a quota increase in the `eu` multi-region, state in your request that the quota is for "EU meta region."



## Location considerations

When you choose a location for your data, you might want to consider factors such as:

  * Regulatory requirements about where to store your data
  * Latency
  * Resiliency
  * Cost
  * Colocation with other Google Cloud services



For example, Google manages [multi-regional locations](https://docs.cloud.google.com/docs/geography-and-regions#multi-regional_resources) to be redundant and distributed within and across regions. These services optimize availability, performance, and resource efficiency. As a result, these services require a trade-off on either latency or the consistency model.

Consider doing the following when choosing a location for your data:

  * **Colocate your dataset and your external data source**.

  * **Colocate your dataset with your Cloud Storage buckets when importing data**.

  * **Colocate your dataset with your Cloud Storage buckets and BigQuery datasets when exporting data**.




## Moving Cloud Healthcare API data between locations

You cannot change the location of a dataset after it is created. Also, you cannot move a dataset from one location to another. If you need to move data from one location to another, complete one of the following processes:

### FHIR data

  1. [Export](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export#exporting_fhir_resources) the data from your FHIR stores to a regional or multi-regional Cloud Storage bucket. When you export the data, the operation only exports the current version of each resource. The operation does not export version history; there is no bulk export operation for version history.

There are [charges](https://cloud.google.com/healthcare-api/pricing#etl_operations) for exporting FHIR data to Cloud Storage. You also incur charges for [storing the exported data](https://cloud.google.com/storage/pricing#storage-pricing) in Cloud Storage.

  2. After you transfer the data to a Cloud Storage bucket, create a new dataset in the new location. Create any FHIR stores in the new dataset that you require for storing your data. Then, [import](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export#importing_fhir_resources) your data from Cloud Storage into the new FHIR stores.




### DICOM data

  1. [Export](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export#exporting_dicom_instances) the data from your DICOM stores to a regional or multi-regional Cloud Storage bucket.

There are [charges](https://cloud.google.com/healthcare-api/pricing#etl_operations) for exporting DICOM data to Cloud Storage. You also incur charges for [storing the exported data](https://cloud.google.com/storage/pricing#storage-pricing) in Cloud Storage.

  2. After you transfer the data to a Cloud Storage bucket, create a new dataset in the new location. Create any DICOM stores in the new dataset that you require for storing your data. Then, [import](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export#importing_dicom_objects) your data from Cloud Storage into the new DICOM stores.




### HL7v2 data

  1. [Export the HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-import-export#exporting_hl7v2_messages) from your HL7v2 store to a regional or multi-regional Cloud Storage bucket.

There are [charges](https://cloud.google.com/healthcare-api/pricing#etl_operations) for exporting HL7v2 messages to Cloud Storage. You also incur charges for [storing the exported data](https://cloud.google.com/storage/pricing#storage-pricing) in Cloud Storage.

  2. After you transfer the data to a Cloud Storage bucket, create a new dataset in the new location. Create any HL7v2 stores in the new dataset that you require for storing your data. Then, [import](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-import-export) your messages from Cloud Storage into the new HL7v2 stores.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
