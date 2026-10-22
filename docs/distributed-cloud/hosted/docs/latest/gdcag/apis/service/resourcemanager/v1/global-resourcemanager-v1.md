---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/v1/global-resourcemanager-v1/
title: KRM API resourcemanager.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:13.472690+00:00
---

# KRM API resourcemanager.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/v1/global-resourcemanager-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API resourcemanager.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## resourcemanager.global.gdc.goog/v1

### Project

Represents a namespace that spans across multiple user clusters in an organization in all zones for a customer. It is a namespaced resource, and the controller is expected to watch reconcile `Project` objects in a preconfigured namespace.

_Appears in:_ \- ProjectList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `Project`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectSpec_ |   
`status` _ProjectStatus_ |   
  
### ProjectList

Represents a collection of Projects.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `ProjectList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Project array_ |   
  
### ProjectReplica

Represents a replicated Project resource that will be synced to a particular zonal API server. A Project resource will have a replica for each zone. Upon an update of the Project resource, the replicas will be progressively updated based on the resource's rollout strategy.

_Appears in:_ \- ProjectReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `ProjectReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectSpec_ |   
`status` _ProjectReplicaStatus_ |   
  
### ProjectReplicaList

Represents a collection of projects replicas.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `ProjectReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectReplica array_ |   
  
### ProjectReplicaStatus

Provides the status of a project replica.

_Appears in:_ \- ProjectReplica \- ProjectZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this project's overall state.  
`availableClusters` _integer_ | AvailableClusters represents the amount of available user clusters.  
`errorStatus` _ErrorStatus_ | ErrorStatus contain a list of current errors and the timestamp this field gets updated.  
  
### ProjectServiceAccount

Represents a ServiceAccount associated with Projects in all zones.

_Appears in:_ \- ProjectServiceAccountList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `ProjectServiceAccount`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectServiceAccountSpec_ |   
`status` _ProjectServiceAccountStatus_ |   
  
### ProjectServiceAccountKey

Contains the key component used to verify the JWT signed by the private key for the `ProjectServiceAccount` resource. The JWT is used as part of the authentication flow. Currently, the `ProjectServiceAccountKey` resource only supports user-managed keys. Users can create and delete user-managed key pairs. Users are responsible for rotating these keys periodically to ensure the security of their service accounts. Users retain the private key of these key pairs, and the `ProjectServiceAccountKey` resource retains only the public key.

_Appears in:_ \- ProjectServiceAccountSpec

Field | Description  
---|---  
`algorithm` _ProjectServiceAccountKeyAlgorithm_ | The algorithm of the key. Currently only ES256 keys are supported.  
`id` _string_ | The ID of the key. This is used to determine which key to verify against.  
`key` _string_ | The base64 encoded public key to verify against.  
`validBefore` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The expiration time for the key.  
`validAfter` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The start time when the key becomes valid.  
  
### ProjectServiceAccountList

Represents a collection of ProjectServiceAccounts.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `ProjectServiceAccountList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectServiceAccount array_ |   
  
### ProjectServiceAccountReplica

Represents a replicated ProjectServiceAccount resource that will be synced to a particular zonal API server. A ProjectServiceAccount resource will have a replica for each zone. Upon an update of the ProjectServiceAccount resource, the replicas will be progressively updated based on the resource's rollout strategy.

_Appears in:_ \- ProjectServiceAccountReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `ProjectServiceAccountReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectServiceAccountSpec_ |   
`status` _ProjectServiceAccountReplicaStatus_ |   
  
### ProjectServiceAccountReplicaList

Represents a collection of project service account replicas.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `ProjectServiceAccountReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectServiceAccountReplica array_ |   
  
### ProjectServiceAccountReplicaStatus

Provides the status of a project replica.

_Appears in:_ \- ProjectServiceAccountReplica \- ProjectServiceAccountZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this project's overall state.  
`errorStatus` _ErrorStatus_ | ErrorStatus contain a list of current errors and the timestamp this field gets updated.  
  
### ProjectServiceAccountSpec

Provides the desired state of a project.

_Appears in:_ \- ProjectServiceAccount \- ProjectServiceAccountReplica

Field | Description  
---|---  
`keys` _ProjectServiceAccountKey array_ | The public keys used to verify the signature of the JWTs for the `ProjectServiceAccount` resource.  
  
### ProjectServiceAccountStatus

Provides the overall status of a ProjectServiceAccount.

_Appears in:_ \- ProjectServiceAccount

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ProjectServiceAccountZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ProjectServiceAccountZoneStatus

Provides the status of a ProjectServiceAccount rolling out to a particular zone.

_Appears in:_ \- ProjectServiceAccountStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ProjectServiceAccountReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### ProjectStatus

Provides the overall status of a Project.

_Appears in:_ \- Project

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ProjectZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ProjectZoneStatus

Provides the status of a Project rolling out to a particular zone.

_Appears in:_ \- ProjectStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ProjectReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### TagKey

Represents the key of a tag to separate the control between resource ownership and policy enforcement.

_Appears in:_ \- TagKeyList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagKey`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _TagKeySpec_ |   
`status` _TagKeyStatus_ |   
  
### TagKeyList

Represents a collection of TagKeys.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagKeyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _TagKey array_ |   
  
### TagKeyReplica

Represents a replicated TagKey resource that will be synced to a particular zonal API server. A TagKey resource will have a replica for each zone. Upon an update of the TagKey resource, the replicas will be progressively updated based on the resource's rollout strategy.

_Appears in:_ \- TagKeyReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagKeyReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _TagKeySpec_ |   
`status` _TagKeyReplicaStatus_ |   
  
### TagKeyReplicaList

Represents a collection of tagkey replicas.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagKeyReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _TagKeyReplica array_ |   
  
### TagKeyReplicaStatus

Provides the status of a tagkey replica.

_Appears in:_ \- TagKeyReplica \- TagKeyZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this tagkey's overall state.  
`errorStatus` _ErrorStatus_ | ErrorStatus contain a list of current errors and the timestamp this field gets updated.  
  
### TagKeyStatus

Provides the overall status of a TagKey.

_Appears in:_ \- TagKey

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _TagKeyZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### TagKeyZoneStatus

Provides the status of a TagKey rolling out to a particular zone.

_Appears in:_ \- TagKeyStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _TagKeyReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### TagValue

Represents the value of a tag to separate the control between resource ownership and policy enforcement.

_Appears in:_ \- TagValueList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagValue`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _TagValueSpec_ |   
`status` _TagValueStatus_ |   
  
### TagValueList

Represents a collection of TagValues.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagValueList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _TagValue array_ |   
  
### TagValueReplica

Represents a replicated TagValue resource that will be synced to a particular zonal API server. A TagValue resource will have a replica for each zone. Upon an update of the TagValue resource, the replicas will be progressively updated based on the resource's rollout strategy.

_Appears in:_ \- TagValueReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagValueReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _TagValueSpec_ |   
`status` _TagValueReplicaStatus_ |   
  
### TagValueReplicaList

Represents a collection of tagvalue replicas.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.global.gdc.goog/v1`  
`kind` _string_ | `TagValueReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _TagValueReplica array_ |   
  
### TagValueReplicaStatus

Provides the status of a tagvalue replica.

_Appears in:_ \- TagValueReplica \- TagValueZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this tagvalue's overall state.  
`errorStatus` _ErrorStatus_ | ErrorStatus contain a list of current errors and the timestamp this field gets updated.  
  
### TagValueStatus

Provides the overall status of a TagValue.

_Appears in:_ \- TagValue

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _TagValueZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### TagValueZoneStatus

Provides the status of a TagValue rolling out to a particular zone.

_Appears in:_ \- TagValueStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _TagValueReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
