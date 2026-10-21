---
url: https://docs.cloud.google.com/transcoder/docs/locations/
title: Transcoder API locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:31.384134+00:00
---

# Transcoder API locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Resources ](https://docs.cloud.google.com/transcoder/docs/resources)



Send feedback 

#  Transcoder API locations Stay organized with collections  Save and categorize content based on your preferences. 

The Transcoder API is available in the following regions. For more information about regions, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Regions

The following table lists the regions in the Americas where the Transcoder API is available.

Region description | Region name  
---|---  
Iowa, USA | `us-central1`  
Oregon, USA | `us-west1`  
Los Angeles, USA | `us-west2`  
South Carolina, USA | `us-east1`  
N. Virginia, USA | `us-east4`  
São Paulo, Brazil | `southamerica-east1`  
Montreal, Canada | `northamerica-northeast1`  
  
The following table lists the regions in Asia Pacific where the Transcoder API is available.

Region description | Region name  
---|---  
Taiwan | `asia-east1`  
Tokyo | `asia-northeast1`  
Seoul | `asia-northeast3`  
Mumbai | `asia-south1`  
Singapore | `asia-southeast1`  
  
The following table lists the regions in Australia where the Transcoder API is available.

Region description | Region name  
---|---  
Sydney | `australia-southeast1`  
  
The following table lists the regions in Europe where the Transcoder API is available.

Region description | Region name  
---|---  
Belgium | `europe-west1`  
London | `europe-west2`  
Netherlands | `europe-west4`  
  
The following table lists the regions in Middle East where the Transcoder API is available.

Region description | Region name  
---|---  
Tel Aviv | `me-west1`  
Doha | `me-central1`  
Dammam | `me-central2`  
  
## Location considerations

When you choose a region for use with the Transcoder API, you might want to consider the following:

### Jobs

When you create a job, you specify a region to process it with the Transcoder API. After you create a job, you can't change its region.

### Job templates

Optionally, when you create a job, you can specify a job template to populate the configuration settings for the job. The Transcoder API provides preset job templates in all regions where the API is available. You can also create user-defined job templates for each region where the Transcoder API is available.

To specify a user-defined job template for a job in a region, make sure the template is available in that region. To verify the existence of a template in a region, you can list all the templates in a region or send a request to get the details of a specific template.

### Media assets

To submit media assets for a transcoding job, you first upload them to Cloud Storage. After a job completes, the Transcoder API saves the results back to Cloud Storage. When choosing a region for your jobs and media assets, consider doing the following:

  * When importing data to Cloud Storage, co-locate the bucket for your media assets and your external data source.
  * Co-locate your source media assets in Cloud Storage with the region of Transcoder API jobs.
  * When choosing the output destination for a job, co-locate your output media assets in Cloud Storage and your external clients.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
