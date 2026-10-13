---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.OutputConfig
title: Google Cloud Datalabeling V1beta1 Client - Class OutputConfig (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:19:57.932190+00:00
---

# Google Cloud Datalabeling V1beta1 Client - Class OutputConfig (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.OutputConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Datalabeling V1beta1 Client - Class OutputConfig (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.2  0.6.3  0.5.7  0.4.2  0.3.1  0.2.0  0.1.14 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Datalabeling V1beta1 Client class OutputConfig.

The configuration of output data.

Generated from protobuf message `google.cloud.datalabeling.v1beta1.OutputConfig`

## Namespace

Google \ Cloud \ DataLabeling \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ gcs_destination` |  `[GcsDestination](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.GcsDestination)`   
Output to a file in Cloud Storage. Should be used for labeling output other than image segmentation.  
`↳ gcs_folder_destination` |  `[GcsFolderDestination](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.GcsFolderDestination)`   
Output to a folder in Cloud Storage. Should be used for image segmentation labeling output.  
  
### getGcsDestination

Output to a file in Cloud Storage. Should be used for labeling output other than image segmentation.

**Returns**  
---  
**Type** | **Description**  
`[GcsDestination](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.GcsDestination)|null` |   
  
### hasGcsDestination

### setGcsDestination

Output to a file in Cloud Storage. Should be used for labeling output other than image segmentation.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[GcsDestination](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.GcsDestination)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGcsFolderDestination

Output to a folder in Cloud Storage. Should be used for image segmentation labeling output.

**Returns**  
---  
**Type** | **Description**  
`[GcsFolderDestination](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.GcsFolderDestination)|null` |   
  
### hasGcsFolderDestination

### setGcsFolderDestination

Output to a folder in Cloud Storage. Should be used for image segmentation labeling output.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[GcsFolderDestination](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.GcsFolderDestination)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDestination

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
