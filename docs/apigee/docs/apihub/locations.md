---
url: https://docs.cloud.google.com/apigee/docs/apihub/locations/
title: API hub locations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:24.835874+00:00
---

# API hub locations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API hub locations Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page provides information about data residency and the locations where API hub is available. _Data residency_ describes where your data is stored at rest. To help comply with data residency requirements, Google Cloud gives you the ability to control where that data is stored.

## API hub and data residency

Apigee API hub provides [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-compatibility) to keep your data-at-rest physically within a specified geographical region or location. This ensures that your data is stored and managed within the chosen geographical boundary, helping you meet any regulatory and compliance requirements. 

During the [API hub instance provisioning process](https://docs.cloud.google.com/apigee/docs/apihub/provision), you must specify locations for your instance and search data.

**Important:** Before provisioning API hub in your project, verify if you have an existing Apigee organization in your project. If yes, then ensure the following: 

  * Ensure that the organization does not have the `Google Cloud Platform - Resource Location Restriction` organization policy constraint added.
  * API hub uses Cloud Scheduler for some of its features. Cloud Scheduler is not available in all Google Cloud locations. If you are provisioning API hub in a location where Cloud Scheduler is not available, it will be provisioned in a fallback location. For a list of these locations and their fallbacks, see [API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations). If your organization has a `Resource Location Restriction` policy that prevents resources from being created in the fallback location, provisioning will fail. 



  * **Instance region** : The physical geographic region where your core API hub instance data will be hosted.
  * **Search data multi-region** : If you enable the AI-powered [Semantic search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) feature, this is the multi-region where your search data will be stored. When semantic search is enabled, Vertex AI is automatically provisioned within a Google Cloud region that resides within the selected multi-region. For example, if you choose `US multi-region`, Vertex AI could be provisioned in `us-west1`, `us-central1`, or any other valid region within the `US multi-region`.



## Supported locations

The following table lists the Google Cloud regions where you can provision an API hub instance. 

### Americas

Region description | Region name | Details  
---|---|---  
Columbus |  `us-east5`  
Dallas |  `us-south1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Iowa |  `us-central1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Las Vegas |  `us-west4`  
Los Angeles |  `us-west2`  
Montreal |  `northamerica-northeast1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Northern Virginia |  `us-east4`  
Oregon |  `us-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Salt Lake City |  `us-west3`  
Santiago |  `southamerica-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
São Paulo |  `southamerica-east1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
South Carolina |  `us-east1`  
Toronto |  `northamerica-northeast2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
### Europe

Region description | Region name | Details  
---|---|---  
Belgium |  `europe-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Berlin |  `europe-west10` |   
Finland |  `europe-north1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Frankfurt |  `europe-west3` |   
London |  `europe-west2`  
Madrid |  `europe-southwest1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Milan |  `europe-west8`  
Netherlands |  `europe-west4` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Paris |  `europe-west9` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Turin |  `europe-west12`  
Warsaw |  `europe-central2`  
Zurich |  `europe-west6` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
### Asia-Pacific

Region description | Region name  
---|---  
Delhi |  `asia-south2`  
Hong Kong |  `asia-east2`  
Jakarta |  `asia-southeast2`  
Melbourne |  `australia-southeast2`  
Mumbai |  `asia-south1`  
Osaka |  `asia-northeast2`  
Seoul |  `asia-northeast3`  
Singapore |  `asia-southeast1`  
Sydney |  `australia-southeast1`  
Taiwan |  `asia-east1`  
Tokyo |  `asia-northeast1`  
  
### Middle East

Region description | Region name  
---|---  
Dammam |  `me-central2`  
Doha | `me-central1`  
Tel Aviv |  `me-west1`  
  
### Africa

Region description | Region name  
---|---  
Johannesburg |  `africa-south1`  
  
## Cloud Scheduler location fallbacks

API hub uses [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs) for some of its features. Cloud Scheduler is not available in all Google Cloud locations. If you are provisioning API hub in one of the following locations, Cloud Scheduler will be provisioned in a different location as indicated in the table. 

API hub location | Cloud Scheduler fallback location  
---|---  
Johannesburg (`africa-south1`) | Belgium (`europe-west1`)  
Delhi (`asia-south2`) | Mumbai (`asia-south1`)  
Melbourne (`australia-southeast2`) | Sydney (`australia-southeast1`)  
Finland (`europe-north1`) | Warsaw (`europe-central2`)  
Madrid (`europe-southwest1`) | Belgium (`europe-west1`)  
Netherlands (`europe-west4`) | Belgium (`europe-west1`)  
Milan (`europe-west8`) | Zurich (`europe-west6`)  
Paris (`europe-west9`) | Belgium (`europe-west1`)  
Berlin (`europe-west10`) | Frankfurt (`europe-west3`)  
Turin (`europe-west12`) | Zurich `europe-west6`  
Doha (`me-central1`) | Mumbai (`asia-south1`)  
Dammam (`me-central2`) | Mumbai (`asia-south1`)  
Tel Aviv (`me-west1`) | Frankfurt (`europe-west3`)  
Toronto (`northamerica-northeast2`) | Montreal (`northamerica-northeast1`)  
Santiago (`southamerica-west1`) | São Paulo (`southamerica-east1`)  
Columbus (`us-east5`) | Northern Virginia (`us-east4`)  
Dallas (`us-south1`) | Iowa (`us-central1`)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
