---
url: https://docs.cloud.google.com/infrastructure-manager/docs/locations/
title: Infrastructure Manager locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:01.899485+00:00
---

# Infrastructure Manager locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/infrastructure-manager/docs/resources)



Send feedback 

#  Infrastructure Manager locations Stay organized with collections  Save and categorize content based on your preferences. 

Infrastructure Manager can deploy Google Cloud resources to any [region or zone](https://docs.cloud.google.com/docs/geography-and-regions) where those resources are available. For example, see [Cloud Run locations](https://docs.cloud.google.com/run/docs/locations) for the list of locations where Cloud Run is available. 

The resource's deployment location is specified when you [create a deployment using Google Cloud console](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources#console), in the [Terraform configuration](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform) directly, or as a variable that can be set as part of the [gcloud CLI create a deployment command](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources#storage-bucket).

If you use a storage bucket to store the Terraform configuration, this storage bucket can be in any bucket location. For more details see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).

The Infra Manager service is available in the following regions and multi-regions. These locations are where Infra Manager runs the Cloud Build jobs and where it creates a storage bucket and stores generated artifacts and logs.

**Note:** Depending on usage, projects can be restricted to [certain regions](https://docs.cloud.google.com/build/docs/locations#restricted_regions_for_some_projects) for [Cloud Build](https://docs.cloud.google.com/build/docs). Due to Infra Manager dependencies on Cloud Build, regions restricted for Cloud Build are also restricted for Infra Manager.

For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Types of locations for Infra Manager

You can create Infra Manager resources in different types of locations depending on your availability and latency requirements:

  * **Regional locations** : A regional location consists of data centers in a specific geographic place (for example, `us-central1`). Deployments created in a single region run Cloud Build jobs and store state files and artifacts exclusively in that region. Regional deployments are typically faster and less expensive because data replication isn't required across regions.
  * **Multi-regional locations** : A multi-regional location is a large geographic area (such as `us`) that contains multiple discrete regions. Deployments created in a multi-region replicate deployment metadata and Terraform state files across multiple data centers for higher availability and redundancy. Incoming requests are actively load balanced across healthy instances within the multi-region.



Deployments created in a multi-region location are logically distinct from deployments created in individual regions.

## Multi-regions

Infra Manager is available in the following multi-regions:

Multi-region name | Description | Included regions  
---|---|---  
`us` | Data centers in the United States | `us-central1`, `us-east4`  
  
### Use Cloud Build worker pools in multi-regions

Because [Cloud Build private worker pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) are strictly single-region resources, using a private worker pool with a multi-region deployment (such as `us`) requires the following setup:

  1. **Create identical regional worker pools** in all member regions of the multi-region. For the `us` multi-region, create a private worker pool with the exact same ID and configuration in both `us-central1` and `us-east4`: 
     * `projects/PROJECT_ID/locations/us-central1/workerPools/WORKER_POOL_ID`
     * `projects/PROJECT_ID/locations/us-east4/workerPools/WORKER_POOL_ID`
  2. **Specify the multi-region location** in your Infra Manager request by referencing `locations/us`: `text projects/PROJECT_ID/locations/us/workerPools/WORKER_POOL_ID` When your deployment executes, Infra Manager automatically directs the build job to the matching regional worker pool in the region handling the request.



## Regions

Infra Manager is available in the following regions. For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

### Asia Pacific

The following table lists the available regions in Asia Pacific.

Region description | Region name  
---|---  
Tokyo, Japan | `asia-northeast1`  
Osaka, Japan | `asia-northeast2`  
Seoul, South Korea | `asia-northeast3`  
Taiwan | `asia-east1`  
Hong Kong | `asia-east2`  
Mumbai, India | `asia-south1`  
Delhi, India | `asia-south2`  
Singapore | `asia-southeast1`  
Jakarta, Indonesia | `asia-southeast2`  
Bangkok, Thailand | `asia-southeast3`  
Sydney, Australia | `australia-southeast1`  
Melbourne, Australia | `australia-southeast2`  
  
### Europe

The following table lists the available regions in Europe.

Region description | Region name  
---|---  
Hamina, Finland | `europe-north1`  
Stockholm, Sweden | `europe-north2`  
Warsaw, Poland | `europe-central2`  
St. Ghislain, Belgium | `europe-west1`  
London, England | `europe-west2`  
Frankfurt, Germany | `europe-west3`  
Milan, Italy | `europe-west8`  
Paris, France | `europe-west9`  
Berlin, Germany | `europe-west10`  
Turin, Italy | `europe-west12`  
Eemshaven, Netherlands | `europe-west4`  
Zurich, Switzerland | `europe-west6`  
Madrid, Spain | `europe-southwest1`  
  
### Americas

The following table lists the available regions in the Americas.

Region description | Region name  
---|---  
Moncks Corner, South Carolina | `us-east1`  
Columbus, Ohio | `us-east5`  
Ashburn, Virginia | `us-east4`  
The Dalles, Oregon | `us-west1`  
Los Angeles, California | `us-west2`  
Salt Lake City, Utah | `us-west3`  
Las Vegas, Nevada | `us-west4`  
Council Bluffs, Iowa | `us-central1`  
Dallas, Texas | `us-south1`  
Montréal, Canada | `northamerica-northeast1`  
Toronto, Canada | `northamerica-northeast2`  
Queretaro, Mexico | `northamerica-south1`  
São Paulo, Brazil | `southamerica-east1`  
Santiago, Chile | `southamerica-west1`  
  
### Middle-East and Africa

The following table lists the available regions in the Middle-East and Africa.

Region description | Region name  
---|---  
Johannesburg, South Africa | `africa-south1`  
Doha, Qatar | `me-central1`  
Dammam, Saudi Arabia | `me-central2`  
Tel Aviv, Israel | `me-west1`  
  
## What's next

  * Learn more about [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) in Google Cloud.
  * See the full list of [Cloud locations](https://cloud.google.com/about/locations/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
