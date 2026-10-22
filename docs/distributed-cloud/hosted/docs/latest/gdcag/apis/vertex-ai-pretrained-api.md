---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai-pretrained-api/
title: KRM API aiplatform.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:05.808917+00:00
---

# KRM API aiplatform.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai-pretrained-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API aiplatform.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

The pre-trained APIs are a collection of AI services that include Optical Character Recognition (OCR), Speech-to-Text, and Translation. The services are enabled and disabled using the Kubernetes Resource Model (KRM) API. The KRM API is a management API that is optionally used by the AI Platform Admin.

## aiplatform.gdc.goog/v1

Package v1 contains API Schema definitions for the aiplatform.gdc.goog v1 API group

### Application

Application defines the type of AI Application

_Appears in:_ \- ApplicationStatus \- PackageSpec

Field | Description  
---|---  
`name` _ApplicationName_ |   
`path` _string_ | path of Application helm in harbor  
  
### ApplicationStatus

ApplicationStatus keeps track of each application thats is deployed

_Appears in:_ \- PackageStatus

Field | Description  
---|---  
`application` _Application_ |   
`deployed` _boolean_ | Indicates if application is deployed successfully  
`messages` _string array_ | Hold the messages if any  
  
### Package

Package is the Schema for the packages API

_Appears in:_ \- PackageList

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.gdc.goog/v1`  
`kind` _string_ | `Package`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _PackageSpec_ |   
`status` _PackageStatus_ |   
  
### PackageList

PackageList contains a list of Packages

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.gdc.goog/v1`  
`kind` _string_ | `PackageList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Package array_ |   
  
### PackageSpec

PackageSpec defines the desired state of Package

_Appears in:_ \- Package

Field | Description  
---|---  
`applications` _Application array_ | applications list ex. ocr  
  
### PackageStatus

PackageStatus defines the observed state of Package

_Appears in:_ \- Package

Field | Description  
---|---  
`observedGeneration` _integer_ | The generation observed by the application controller.  
`applicationStatuses` _object (keys:ApplicationName, values:ApplicationStatus)_ | The status of deployed applications  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
