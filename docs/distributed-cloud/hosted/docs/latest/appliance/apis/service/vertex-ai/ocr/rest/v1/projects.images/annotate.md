---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.images/annotate/
title: Method: projects.images.annotate \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:06.549123+00:00
---

# Method: projects.images.annotate  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.images/annotate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Method: projects.images.annotate Stay organized with collections  Save and categorize content based on your preferences. 

Run image detection and annotation for a batch of images.

### HTTP request

`POST https://{VISION_GDC_ENDPOINT}/v1/{parent}/images:annotate`

### Path parameters

Parameters  
---  
`parent` |  `string` Optional. Target project and location to make a call.Format: `projects/{project-id}/locations/{location-id}`.If no parent is specified, a region will be chosen automatically.Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.Example: `projects/project-A/locations/eu`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([AnnotateImageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[AnnotateImageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageRequest)`)` Required. Individual image annotation requests for this batch.  
  
### Response body

If successful, the response body contains an instance of `[BatchAnnotateImagesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/BatchAnnotateImagesResponse)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
