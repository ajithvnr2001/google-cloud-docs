---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/replication/v1/replication-v1/
title: KRM API replication.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:08.967595+00:00
---

# KRM API replication.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/replication/v1/replication-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API replication.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## replication.gdc.goog/v1

Contains API Schema definitions for the replication.gdc.goog v1 API group.

### VolumeFailover

Defines the Schema for the 'VolumeFailover' API.

_Appears in:_ \- VolumeFailoverList

Field | Description  
---|---  
`apiVersion` _string_ | `storage.gdc.goog/v1`  
`kind` _string_ | `VolumeFailover`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VolumeFailoverSpec_ |   
`status` _VolumeFailoverStatus_ |   
  
### VolumeFailoverList

Contains a list of `VolumeReplicationRelationshipReplica` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `storage.gdc.goog/v1`  
`kind` _string_ | `VolumeFailoverList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VolumeFailover array_ |   
  
### VolumeFailoverSpec

Defines the desired state of `VolumeFailover`.

_Appears in:_ \- VolumeFailover

Field | Description  
---|---  
`volumeReplicationRelationshipRef` _string_ | The unique string referencing a volume replication relationship  
  
### VolumeFailoverState

_Underlying type:_ `string` Defines the state of the volume failover used in the `VolumeFailoverStatus`.

_Appears in:_ \- VolumeFailoverStatus

### VolumeFailoverStatus

Defines the observed state of the `VolumeFailover`.

_Appears in:_ \- VolumeFailover

Field | Description  
---|---  
`state` _VolumeFailoverState_ | The current status of the volume failover.  
`message` _string_ | A human-readable message indicating details about why the volume failover is in this state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
