---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/v1/global-kms-v1/
title: KRM API kms.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:28.577428+00:00
---

# KRM API kms.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/v1/global-kms-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API kms.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## kms.global.gdc.goog/v1

### MZAEADKey

MZAEADKey represents the key material that needs to be replicated across multiple zones.

_Appears in:_ \- MZAEADKeyList

Field | Description  
---|---  
`apiVersion` _string_ | `kms.global.gdc.goog/v1`  
`kind` _string_ | `MZAEADKey`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _AEADKeySpec_ |   
`status` _MZAEADKeyStatus_ |   
  
### MZAEADKeyList

MZAEADKeyList contains a list of MZAEADKey

Field | Description  
---|---  
`apiVersion` _string_ | `kms.global.gdc.goog/v1`  
`kind` _string_ | `MZAEADKeyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _MZAEADKey array_ |   
  
### MZAEADKeyStatus

MZAEADKeyStatus defines the observed state of MZAEADKey.

_Appears in:_ \- MZAEADKey

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A report that indicates when an AEADKey creation is complete and ready for use.  
`encryptedKeyMaterial` _integer array_ | Key material encrypted by the KMS root key.  
`rootKeyID` _string_ | Identifier to the root key that wrapped the key material. Follows the format `root-key-namespace/root-key-type/root-key-name/version` Example - `kms-system/ctm/org1-root-key/1` or `kms-system/local/org-1-root-key/1`  
`zones` _MZAEADKeyZoneStatus array_ | Zones represent the status and details of key replication in each zone.  
`primaryZone` _string_ |   
  
### MZAEADKeyZoneStatus

MZAEADKeyZoneStatus represents the replication status of a specific zone.

_Appears in:_ \- MZAEADKeyStatus

Field | Description  
---|---  
`zoneName` _string_ |   
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Indicates whether the zone has successfully completed processing the key material or not.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
