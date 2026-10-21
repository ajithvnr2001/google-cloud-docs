---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/keycloak/v1/global-keycloak-v1/
title: KRM API keycloak.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:28.812473+00:00
---

# KRM API keycloak.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/keycloak/v1/global-keycloak-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API keycloak.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## keycloak.global.gdc.goog/v1

Package v1 contains API Schema definitions for the keycloak.global.gdc.goog v1 API group

### ManagedKeycloak

Represents a managed instance of a Keycloak server.

_Appears in:_ \- ManagedKeycloakList

Field | Description  
---|---  
`apiVersion` _string_ | `keycloak.global.gdc.goog/v1`  
`kind` _string_ | `ManagedKeycloak`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManagedKeycloakSpec_ | The desired state of the ManagedKeycloak instance.  
`status` _ManagedKeycloakStatus_ | The most recently observed status of the ManagedKeycloak instance.  
  
### ManagedKeycloakList

Represents a collection of ManagedKeycloak instances.

Field | Description  
---|---  
`apiVersion` _string_ | `keycloak.global.gdc.goog/v1`  
`kind` _string_ | `ManagedKeycloakList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManagedKeycloak array_ |   
  
### ManagedKeycloakReplica

Represents a managed instance of a Keycloak server.

_Appears in:_ \- ManagedKeycloakReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `keycloak.global.gdc.goog/v1`  
`kind` _string_ | `ManagedKeycloakReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManagedKeycloakSpec_ | The desired state of the ManagedKeycloak instance.  
`status` _ManagedKeycloakReplicaStatus_ | The most recently observed status of the ManagedKeycloak instance.  
  
### ManagedKeycloakReplicaList

Represents a collection of ManagedKeycloakReplica instances.

Field | Description  
---|---  
`apiVersion` _string_ | `keycloak.global.gdc.goog/v1`  
`kind` _string_ | `ManagedKeycloakReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManagedKeycloakReplica array_ |   
  
### ManagedKeycloakReplicaStatus

Provides the status of an `ManagedKeycloak` resource.

_Appears in:_ \- ManagedKeycloakReplica \- ManagedKeycloakZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
### ManagedKeycloakSpec

Represents the specification or the desired state of a ManagedKeycloak instance.

_Appears in:_ \- ManagedKeycloak \- ManagedKeycloakReplica

Field | Description  
---|---  
`adminCredentialSecretName` _string_ | The name of the Kubernetes Secret containing the initial admin credentials. The secret must contain `username` and `password` keys.  
`replicas` _integer_ | Configuration for number of replicas.  
  
### ManagedKeycloakStatus

Represents the specification or the desired state of a ManagedKeycloak instance.

_Appears in:_ \- ManagedKeycloak

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ManagedKeycloakZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ManagedKeycloakZoneStatus

Represents the current status of a ManagedKeycloak instance.

_Appears in:_ \- ManagedKeycloakStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ManagedKeycloakReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
