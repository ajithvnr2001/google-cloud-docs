---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/global-identity-v1/
title: KRM API iam.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:26.131899+00:00
---

# KRM API iam.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/global-identity-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API iam.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## iam.global.gdc.goog/v1

Package v1 contains API Schema definitions for the iam.global.gdc.goog v1 API group

### CustomRole

Represents a template for a global CustomRole Custom roles provide fine-grained control over user permissions, unlike predefined roles. This allows organizations to tailor access rights to their specific needs, balancing operational efficiency with security. By adhering to the principle of least privilege, custom roles significantly enhance security and protect sensitive data.

_Appears in:_ \- CustomRoleList \- CustomRoleReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `CustomRole`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CustomRoleSpec_ |   
`status` _CustomRoleStatus_ |   
  
### CustomRoleList

Contains a list of `CustomRole` resource

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `CustomRoleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CustomRole array_ |   
  
### CustomRoleMetadata

Represents the data necessary to create a Custom Role

_Appears in:_ \- CustomRoleSpec

Field | Description  
---|---  
`scope` _CustomRoleScopeType_ | scope of the custom role created which can either be organization or project  
`roleNamespaces` _string array_ | namespace of the role (optional) only required for role deployment if: case 1: when scope is project then it denotes the project namespaces case 2: when scope is project and roleNamespaces contain ['*'] then it denotes all project namespaces case 3: when scope is organization and deployment roleType is role not clusterRole then it denotes literal namespaces  
`title` _string_ | title is a friendly title for the role, such as "My Company Admin".  
`description` _string_ | description is a short description of the role, such as "My custom role description".  
`id` _string_ | id is the name of the role, such as "my-company-admin".  
`stage` _StageType_ | stage indicates the stage of a role in the launch lifecycle which can either be [ALPHA, BETA, GA, DISABLED]  
  
### CustomRoleReplica

Represents a template for a zonal CustomRole replica

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `CustomRoleReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CustomRoleSpec_ |   
`status` _CustomRoleReplicaStatus_ |   
  
### CustomRoleReplicaList

Contains a list of zonal CustomRole replica resources

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `CustomRoleReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CustomRole array_ |   
  
### CustomRoleReplicaStatus

Provides a status of zonal CustomRole replica

_Appears in:_ \- CustomRoleReplica \- CustomRoleZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this Custom role overall state  
`propagatedCustomRoleName` _string_ | Propagated custom role name for all the replicas  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### CustomRoleScopeType

_Underlying type:_ `string`

_Appears in:_ \- CustomRoleMetadata

### CustomRoleSpec

Defines the CustomRole data in the `ClusterRoleTemplate` resource

_Appears in:_ \- CustomRole \- CustomRoleReplica

Field | Description  
---|---  
`metadata` _CustomRoleMetadata_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`zonalRules` _[PolicyRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#policyrule-v1-rbac) array_ |   
`globalRules` _[PolicyRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#policyrule-v1-rbac) array_ |   
  
### CustomRoleStatus

Provides the status of an `CustomRoleStatus` resource

_Appears in:_ \- CustomRole

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _CustomRoleZoneStatus array_ | The list of zone statuses where the resource is rolled out to  
`propagationInfo` _PropagationInfo_ | propagation information of converted template for global role template conversion  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### CustomRoleZoneStatus

CustomRoleZoneStatus provides the status of a CustomRole rolling out to a particular zone

_Appears in:_ \- CustomRoleStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _CustomRoleReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date  
  
### IAMRole

IAMRole references a predefined role in the global and/or zonal APIServer.

_Appears in:_ \- IAMRoleList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IAMRole`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _IAMRoleSpec_ |   
`status` _IAMRoleStatus_ |   
  
### IAMRoleBinding

IAMRoleBinding references a global IAMRole and adds who information via Subject.

_Appears in:_ \- IAMRoleBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IAMRoleBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _IAMRoleBindingSpec_ |   
`status` _IAMRoleBindingStatus_ |   
  
### IAMRoleBindingList

Contains a list of IAMRoleBinding resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IAMRoleBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _IAMRoleBinding array_ |   
  
### IAMRoleBindingSpec

Provides the specification of the IAMRoleBindingSpec.

_Appears in:_ \- IAMRoleBinding

Field | Description  
---|---  
`roleRef` _[RoleRef](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#roleref-v1-rbac)_ | RoleRef contains information that points to the IAMRole being used.  
`subjects` _[Subject](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#subject-v1-rbac) array_ | The subjects of the global IAMRoleBinding resource.  
  
### IAMRoleBindingStatus

Provides the status of the IAMRoleBinding.

_Appears in:_ \- IAMRoleBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### IAMRoleList

Contains a list of IAMRole resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IAMRoleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _IAMRole array_ |   
  
### IAMRoleSpec

Provides the specification for IAMRole.

_Appears in:_ \- IAMRole

Field | Description  
---|---  
`roleRef` _[RoleRef](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#roleref-v1-rbac)_ | RoleRef contains information that points to the role in the global APIServer being used.  
`zonalRoleRef` _[RoleRef](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#roleref-v1-rbac)_ | ZonalRoleRef contains information that points to the zonal role being used.  
  
### IAMRoleStatus

Provides the status of the IAMRole.

_Appears in:_ \- IAMRole

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### IdentityProviderConfig

Represents a configuration for an identity provider that supports OIDC or SAML.

_Appears in:_ \- IdentityProviderConfigList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfig`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _IdentityProviderConfigSpec_ |   
`status` _IdentityProviderConfigStatus_ |   
  
### IdentityProviderConfigList

Contains a list of `IdentityProviderConfig` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfigList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _IdentityProviderConfig array_ |   
  
### IdentityProviderConfigReplica

Represents a configuration for an identity provider that supports OIDC or SAML.

_Appears in:_ \- IdentityProviderConfigReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfigReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _IdentityProviderConfigSpec_ |   
`status` _IdentityProviderConfigReplicaStatus_ |   
  
### IdentityProviderConfigReplicaList

Contains a list of `IdentityProviderConfigReplica` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfigReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _IdentityProviderConfigReplica array_ |   
  
### IdentityProviderConfigReplicaStatus

Provides the status of an `IdentityProviderConfig` resource.

_Appears in:_ \- IdentityProviderConfigReplica \- IdentityProviderConfigZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### IdentityProviderConfigSpec

Provides the specification, or desired state, of an `IdentityProviderConfig` resource. Either OIDCConfig or SAMLConfig has to be provided but not both.

_Appears in:_ \- IdentityProviderConfig \- IdentityProviderConfigReplica

Field | Description  
---|---  
`oidc` _OIDCProviderConfig_ | OIDC specific configuration.  
`saml` _SAMLProviderConfig_ | SAML specific configuration.  
  
### IdentityProviderConfigStatus

Provides the status of an `IdentityProviderConfig` resource.

_Appears in:_ \- IdentityProviderConfig

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _IdentityProviderConfigZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### IdentityProviderConfigZoneStatus

IdentityProviderConfigZoneStatus provides the status of a IdentityProviderConfig rolling out to a particular zone.

_Appears in:_ \- IdentityProviderConfigStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _IdentityProviderConfigReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### PropagationInfo

Provides the information of converted role template

_Appears in:_ \- CustomRoleStatus

Field | Description  
---|---  
`roleName` _string_ | name of the role  
`roleType` _RoleType_ | type of the role, it can be [role, clusterRole, projectRole, organizationRole]  
`namespaces` _string array_ | namespaces of the role where role deployment will occur  
  
### RoleType

_Underlying type:_ `string`

_Appears in:_ \- PropagationInfo

### StageType

_Underlying type:_ `string`

_Appears in:_ \- CustomRoleMetadata

### ZonalRoleBinding

ZonalRoleBinding references a zonal Role and adds who information via Subject.

_Appears in:_ \- ZonalRoleBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `ZonalRoleBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ZonalRoleBindingSpec_ |   
`status` _ZonalRoleBindingStatus_ |   
  
### ZonalRoleBindingList

Contains a list of ZonalRoleBinding resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `ZonalRoleBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ZonalRoleBinding array_ |   
  
### ZonalRoleBindingReplica

Represents a replicated ZonalRoleBinding resource that will be synced to a particular zonal API server.

_Appears in:_ \- ZonalRoleBindingReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `ZonalRoleBindingReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ZonalRoleBindingSpec_ |   
`status` _ZonalRoleBindingReplicaStatus_ |   
  
### ZonalRoleBindingReplicaList

Contains a list of ZonalRoleBindingReplica resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.global.gdc.goog/v1`  
`kind` _string_ | `ZonalRoleBindingReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ZonalRoleBindingReplica array_ |   
  
### ZonalRoleBindingReplicaStatus

Provides the status of the ZonalRoleBindingReplica.

_Appears in:_ \- ZonalRoleBindingReplica \- ZonalRoleBindingZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`propagatedName` _string_ | PropagatedName of the ZonalRoleBinding that requires propagation in the user clusters within the organization.  
`clusters` _ClusterStatus array_ | The list of propagation statuses for the clusters for ZonalRoleBinding that requires propagation in the user clusters within the organization.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### ZonalRoleBindingSpec

Provides the specification of the ZonalRoleBinding.

_Appears in:_ \- ZonalRoleBinding \- ZonalRoleBindingReplica

Field | Description  
---|---  
`roleRef` _[RoleRef](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#roleref-v1-rbac)_ | RoleRef contains information that points to the zonal role being used.  
`subjects` _[Subject](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#subject-v1-rbac) array_ | The subjects of the global ZonalRoleBinding resource.  
  
### ZonalRoleBindingStatus

Provides the status of the ZonalRoleBinding resource.

_Appears in:_ \- ZonalRoleBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ZonalRoleBindingZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### ZonalRoleBindingZoneStatus

ZonalRoleBindingZoneStatus provides the status of a ZonalRoleBinding rolling out to a particular zone.

_Appears in:_ \- ZonalRoleBindingStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ZonalRoleBindingReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
