---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/billing/v1/global-billing-v1/
title: KRM API billing.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:43.711124+00:00
---

# KRM API billing.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/billing/v1/global-billing-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API billing.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## billing.global.gdc.goog/v1

Contains API Schema definitions for Billing Account related APIs.

### BillingAccount

Represents a Billing Account. The identifier of the `BillingAccount` will be the "namespaced name", . It will appear on the Invoices for this Billing Account, and be on the selectors for querying billing data in Dashboards. Limited access: This field might not be available as it may not be accredited for use in your deployment. You can access it when it's approved.

_Appears in:_ \- BillingAccountList

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccount`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BillingAccountSpec_ |   
`status` _BillingAccountStatus_ |   
  
### BillingAccountBinding

Represents the link between a Billing Account and a Project or the Organization. Limited access: This field might not be available as it may not be accredited for use in your deployment. You can access it when it's approved.

_Appears in:_ \- BillingAccountBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccountBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BillingAccountBindingSpec_ |   
`status` _BillingAccountBindingStatus_ |   
  
### BillingAccountBindingList

Contains a list of BillingAccountBinding

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccountBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BillingAccountBinding array_ |   
  
### BillingAccountBindingReplica

Represents a replicated BillingAccountBinding that will be synced to a particular zonal API server.

_Appears in:_ \- BillingAccountBindingReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccountBindingReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BillingAccountBindingSpec_ |   
`status` _BillingAccountBindingStatus_ |   
  
### BillingAccountBindingReplicaList

Contains a list of BillingAccountBindingReplica

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccountBindingReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BillingAccountBindingReplica array_ |   
  
### BillingAccountBindingStatus

Provides the overall status of a BillingAccountBinding.

_Appears in:_ \- BillingAccountBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _BillingAccountBindingZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### BillingAccountBindingZoneStatus

Provides the status of a BillingAccountBinding rolling out to a particular zone.

_Appears in:_ \- BillingAccountBindingStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _BillingAccountBindingStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### BillingAccountList

Contains a list of BillingAccounts

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccountList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BillingAccount array_ |   
  
### BillingAccountReplica

Represents a replicated BillingAccount that will be synced to a particular zonal API server.

_Appears in:_ \- BillingAccountReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccountReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BillingAccountSpec_ |   
`status` _BillingAccountStatus_ |   
  
### BillingAccountReplicaList

Contains a list of BillingAccountReplica

Field | Description  
---|---  
`apiVersion` _string_ | `billing.global.gdc.goog/v1`  
`kind` _string_ | `BillingAccountReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BillingAccountReplica array_ |   
  
### BillingAccountStatus

Provides the overall status of a BillingAccount.

_Appears in:_ \- BillingAccount

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _BillingAccountZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### BillingAccountZoneStatus

Provides the status of a BillingAccount rolling out to a particular zone.

_Appears in:_ \- BillingAccountStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _BillingAccountStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
