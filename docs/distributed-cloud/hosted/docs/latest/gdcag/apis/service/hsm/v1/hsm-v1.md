---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/hsm/v1/hsm-v1/
title: KRM API hsm.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:09.642268+00:00
---

# KRM API hsm.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/hsm/v1/hsm-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API hsm.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## hsm.gdc.goog/v1

Contains API Schema definitions for the HSM group.

### CTMKey

Represents a resource on the CipherTrust Manager.

_Appears in:_ \- CTMKeyList

Field | Description  
---|---  
`apiVersion` _string_ | `hsm.gdc.goog/v1`  
`kind` _string_ | `CTMKey`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CTMKeySpec_ |   
`status` _CTMKeyStatus_ |   
  
### CTMKeyDomain

Provides the domain a CTM key resides.

_Appears in:_ \- CTMKeySpec

Field | Description  
---|---  
`name` _string_ |   
`id` _string_ |   
  
### CTMKeyList

Represents a collection of CTM keys.

Field | Description  
---|---  
`apiVersion` _string_ | `hsm.gdc.goog/v1`  
`kind` _string_ | `CTMKeyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CTMKey array_ |   
  
### CTMKeySpec

Provides the specification for a CTM key.

_Appears in:_ \- CTMKey

Field | Description  
---|---  
`domain` _CTMKeyDomain_ | The domain a CTM key resides.  
`details` _KeyResource_ | The details of a CTM key.  
  
### CTMKeyStatus

Provides the status of a CTM key.

_Appears in:_ \- CTMKey

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The status of a CTM key.  
`name` _string_ | The name of a CTM key.  
  
### KeyMeta

_Appears in:_ \- KeyResource

Field | Description  
---|---  
`customAttributes` _object (keys:string, values:string)_ |   
  
### KeyResource

Provides the details of a CTM key.

_Appears in:_ \- CTMKeySpec

Field | Description  
---|---  
`id` _string_ |   
`uri` _string_ |   
`createdAt` _string_ |   
`destroyDate` _string_ |   
`name` _string_ |   
`updatedAt` _string_ |   
`meta` _KeyMeta_ |   
`version` _integer_ |   
`algorithm` _string_ |   
`size` _integer_ |   
`objectType` _string_ |   
`activationDate` _string_ |   
`state` _string_ |   
`uuid` _string_ |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
