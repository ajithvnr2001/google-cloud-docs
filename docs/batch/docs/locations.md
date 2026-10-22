---
url: https://docs.cloud.google.com/batch/docs/locations/
title: Batch locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:30.083967+00:00
---

# Batch locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Resources ](https://docs.cloud.google.com/batch/docs/resources)



Send feedback 

#  Batch locations Stay organized with collections  Save and categorize content based on your preferences. 

Batch is available in the following regions. For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

Only the following regions can be used for a job's location, which is the region that you are required to specify when creating a job. A job's location is used for storing job metadata and is the default location used for creating the Compute Engine resources that the job runs on. Optionally, if you specify the [allowed locations for a job's Compute Engine resources (`allowedLocations[]` field)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations), then the job is only allowed to run in the specified locations.

**Important:** As announced in the [release note for July 20, 2026](https://docs.cloud.google.com/batch/docs/release-notes#July_20_2026), the `allowedLocations[]` field is changing on the following dates:

  * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
  * For all other projects, the changes are starting on _July 31, 2026_.



The changes to the `allowedLocations[]` field are as follows:

  * Before these dates, the `allowedLocations[]` field can specify [any region or zones that offer the Compute Engine resources](https://docs.cloud.google.com/compute/docs/regions-zones).
  * Starting gradually on these dates, creating a job fails when any region or zones specified in the `allowedLocations[]` field are outside of the region that you specify as the job's location. To avoid these failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location.



To identify an existing job's location and the allowed locations for its VMs, [view the details of a job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-job).

## Regions

The following table lists the regions in the Americas where Batch is available.

Region description | Region name | Details  
---|---|---  
Montréal | `northamerica-northeast1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Toronto | `northamerica-northeast2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
São Paulo | `southamerica-east1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Santiago | `southamerica-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Iowa | `us-central1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
South Carolina | `us-east1` |   
Northern Virginia | `us-east4` |   
Columbus | `us-east5` |   
Dallas | `us-south1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Oregon | `us-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Los Angeles | `us-west2` |   
Salt Lake City | `us-west3` |   
Las Vegas | `us-west4` |   
  
The following table lists the regions in Europe and the Middle East where Batch is available.

Region description | Region name | Details  
---|---|---  
Warsaw | `europe-central2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Finland | `europe-north1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Madrid | `europe-southwest1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Belgium | `europe-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
London | `europe-west2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Frankfurt | `europe-west3` |   
Netherlands | `europe-west4` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Zürich | `europe-west6` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Milan | `europe-west8` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Paris | `europe-west9` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Berlin | `europe-west10` |   
Turin | `europe-west12` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Doha | `me-central1` |   
Dammam | `me-central2` |   
Tel Aviv | `me-west1` |   
  
The following table lists the regions in Asia Pacific where Batch is available.

Region description | Region name | Details  
---|---|---  
Taiwan | `asia-east1` |   
Hong Kong | `asia-east2` |   
Tokyo | `asia-northeast1` |   
Osaka | `asia-northeast2` |   
Seoul | `asia-northeast3` |   
Mumbai | `asia-south1` |   
Delhi | `asia-south2` |   
Singapore | `asia-southeast1` |   
Jakarta | `asia-southeast2` |   
Sydney | `australia-southeast1` |   
Melbourne | `australia-southeast2` |   
  
## Recommended zones to obtain GPUs from Dynamic Workload Scheduler

When you [create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus) and use calendar-mode reservations or Flex-start VMs, which both use Dynamic Workload Scheduler, we recommend that you use the following zones. These recommended zones have dedicated capacity for Dynamic Workload Scheduler, so using them increases the likelihood that your requests for GPU machine type from Dynamic Workload Scheduler are approved.

A4A3 UltraA3 MegaA3 HighGPU machine series | Recommended zones for Dynamic Workload Scheduler capacity | Details  
---|---|---  
A4 | `asia-southeast1-b` (Singapore) |   
`us-central1-b` (Iowa) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-south1-b` (Dallas) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
A3 Ultra | `asia-south1-b` (Mumbai) |   
`asia-south2-c` (Delhi) |   
`europe-west1-b` (Belgium) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west4-a` (Netherlands) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-b` (Iowa) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-east4-b` (Northern Virginia) |   
`us-south1-b` (Dallas) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
A3 Mega | `europe-west1-c` (Belgium) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west4-b` (Netherlands) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west4-c` (Netherlands) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-a` (Iowa) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-b` (Iowa) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-c` (Iowa) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-east4-b` (Northern Virginia) |   
A3 High | `asia-east1-c` (Taiwan) |   
`europe-west1-b` (Belgium) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-a` (Iowa) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-b` (Iowa) |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
