---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/v1/resourcemanager-v1/
title: KRM API resourcemanager.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:33.184089+00:00
---

# KRM API resourcemanager.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/v1/resourcemanager-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API resourcemanager.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## resourcemanager.gdc.goog/v1

Contains API Schema definitions for the Resource Manager group.

### ClusterPropagationStatus

Provides the propagation status of a cluster.

_Appears in:_ \- PropagationStatus

Field | Description  
---|---  
`namespace` _string_ |   
`name` _string_ |   
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`propagatedNamespace` _string_ | The namespace of the propagated resource.  
  
### ClusterStatus

Contains the propagation status for a specific cluster.

_Appears in:_ \- ClusterPropagationStatus \- OrganizationRoleBindingStatus \- OrganizationRoleStatus \- ProjectClusterStatus \- ProjectRoleBindingStatus \- ProjectRoleStatus \- ProjectServiceAccountStatus

Field | Description  
---|---  
`namespace` _string_ |   
`name` _string_ |   
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
### NameSelector

Provides a list of Project Name For ProjectBinding to match with.

_Appears in:_ \- ProjectBindingSelector

Field | Description  
---|---  
`matchNames` _string array_ |   
  
### OrganizationRole

Provides a system namespace resource that propagates the `ClusterRole` configuration to all user clusters within the organization.

_Appears in:_ \- OrganizationRoleList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `OrganizationRole`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _OrganizationRoleSpec_ |   
`status` _OrganizationRoleStatus_ |   
  
### OrganizationRoleBinding

Provides a system namespace resource that propagates the `ClusterRoleBinding` configuration to all user clusters within the organization.

_Appears in:_ \- OrganizationRoleBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `OrganizationRoleBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _OrganizationRoleBindingSpec_ |   
`status` _OrganizationRoleBindingStatus_ |   
  
### OrganizationRoleBindingList

Contains a list of `OrganizationRoleBinding` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `OrganizationRoleBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _OrganizationRoleBinding array_ |   
  
### OrganizationRoleBindingSpec

Defines the specification of the `OrganizationRoleBinding` object.

_Appears in:_ \- OrganizationRoleBinding

Field | Description  
---|---  
`subjects` _[Subject](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#subject-v1-rbac) array_ | The subjects of the `ClusterRoleBinding` resource to create in the cluster.  
`roleRef` _[RoleRef](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#roleref-v1-rbac)_ | The `RoleRef` resource of the `ClusterRoleBinding` object to create in the cluster.  
  
### OrganizationRoleBindingStatus

Defines the observed state of the `OrganizationRoleBinding` object.

_Appears in:_ \- OrganizationRoleBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`propagatedName` _string_ | The name of the propagated `ClusterRoleBinding` resource in all user clusters within the organization.  
`clusters` _ClusterStatus array_ | The list of propagation statuses for the clusters. When properly propagated, the list includes all clusters within the organization.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### OrganizationRoleList

Contains a list of `OrganizationRole` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `OrganizationRoleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _OrganizationRole array_ |   
  
### OrganizationRoleSpec

Defines the desired state of the `OrganizationRole` resource.

_Appears in:_ \- OrganizationRole

Field | Description  
---|---  
`rules` _[PolicyRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#policyrule-v1-rbac) array_ | The rules of the `ClusterRole` resource to create in all clusters.  
`aggregationRule` _[AggregationRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#aggregationrule-v1-rbac)_ | An optional field that describes the same aggregation logic as in the Kubernetes `ClusterRole` object.  
  
### OrganizationRoleStatus

Defines the observed state of the `OrganizationRole` object.

_Appears in:_ \- OrganizationRole

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | If the `Ready` condition is `True`, then all `ClusterRole` resources are successfully propagated to all user clusters. If the `Ready` condition is `False`, then some or all `ClusterRole` resources have failed to propagate.  
`propagatedName` _string_ | The name of the propagated `ClusterRole` resource in all user clusters within the organization.  
`clusters` _ClusterStatus array_ | The list of propagation statuses on the clusters.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### Project

Represents a namespace that spans across multiple user clusters in an organization. It is a namespaced resource, and the controller is expected to watch reconcile `Project` objects in a preconfigured namespace.

_Appears in:_ \- ProjectList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `Project`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`status` _ProjectStatus_ |   
  
### ProjectBinding

Represents a cluster resource that maintains the mapping relations between clusters and projects. The namespace of the `ProjectBinding` object corresponds to the cluster.

_Appears in:_ \- ProjectBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectBindingSpec_ |   
  
### ProjectBindingClusterRef

Represents the cluster that projects propagate to.

_Appears in:_ \- ProjectBindingSpec

Field | Description  
---|---  
`name` _string_ | The cluster name.  
  
### ProjectBindingList

Contains a list of `ProjectBinding` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectBinding array_ |   
  
### ProjectBindingSelector

Provides a set of rules to match Projects. Must choose exactly 0 or 1 of the selectors. 0 selector matches all Projects.

_Appears in:_ \- ProjectBindingSpec

Field | Description  
---|---  
`nameSelector` _NameSelector_ |   
`labelSelector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ |   
  
### ProjectBindingSpec

Provides the specification, or desired state, of a `ProjectBinding` resource.

_Appears in:_ \- ProjectBinding

Field | Description  
---|---  
`clusterRef` _ProjectBindingClusterRef_ |   
`selector` _ProjectBindingSelector_ | The Selector is used to specify a set of rules to match Projects.  
  
### ProjectClusterStatus

Contains the propagation status and egress NAT IP address used for a specific cluster.

_Appears in:_ \- ProjectStatus

Field | Description  
---|---  
`namespace` _string_ |   
`name` _string_ |   
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`egressNATIPAddress` _string_ |   
  
### ProjectList

Represents a collection of projects.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Project array_ |   
  
### ProjectRole

Represents a project resource that propagates the `Role` configuration to all user clusters the project spans across. The namespace of the `ProjectRole` resource corresponds to the project.

_Appears in:_ \- ProjectRoleList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectRole`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectRoleSpec_ |   
`status` _ProjectRoleStatus_ |   
  
### ProjectRoleBinding

Represents a project resource that propagates the `RoleBinding` resource configuration to all user clusters the project spans across. The namespace for the `ProjectRoleBinding` resource corresponds to the project.

_Appears in:_ \- ProjectRoleBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectRoleBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectRoleBindingSpec_ |   
`status` _ProjectRoleBindingStatus_ |   
  
### ProjectRoleBindingList

Contains a list of `ProjectRoleBinding` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectRoleBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectRoleBinding array_ |   
  
### ProjectRoleBindingSpec

Defines the specification of the `ProjectRoleBinding` resource. It is the same definition as a native `RoleBinding` definition.

_Appears in:_ \- ProjectRoleBinding

Field | Description  
---|---  
`subjects` _[Subject](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#subject-v1-rbac) array_ | The subjects of the `RoleBinding` resource created in the cluster.  
`roleRef` _[RoleRef](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#roleref-v1-rbac)_ | The `RoleRef` resource of the `RoleBinding` object to create in the cluster.  
  
### ProjectRoleBindingStatus

Defines the observed state of the `ProjectRoleBinding` resource.

_Appears in:_ \- ProjectRoleBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`clusters` _ClusterStatus array_ | The list of propagation statuses for the clusters.  
`propagatedName` _string_ | The name of the propagated `ProjectRole` resource realized in the user clusters.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### ProjectRoleList

Contains a list of `ProjectRole` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectRoleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectRole array_ |   
  
### ProjectRoleSpec

Defines the desired state of a `ProjectRole` resource. It is the same definition as a native Kubernetes `Role`.

_Appears in:_ \- ProjectRole

Field | Description  
---|---  
`rules` _[PolicyRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#policyrule-v1-rbac) array_ |   
  
### ProjectRoleStatus

Defines the observed state of a `ProjectRole` resource.

_Appears in:_ \- ProjectRole

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`clusters` _ClusterStatus array_ | The list of propagation statuses on the clusters.  
`propagatedName` _string_ | The name of the propagated `ProjectRole` resource realized in the user clusters.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### ProjectServiceAccount

Defines a project resource that propagates the service account to all user clusters the project spans across. The namespace of the `ProjectServiceAccount` resource corresponds to the project.

_Appears in:_ \- ProjectServiceAccountList

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
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
`validBefore` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The expiration date for the key.  
`validAfter` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The start date when the key becomes valid.  
  
### ProjectServiceAccountList

Contains a list of `ProjectServiceAccount` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `resourcemanager.gdc.goog/v1`  
`kind` _string_ | `ProjectServiceAccountList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectServiceAccount array_ |   
  
### ProjectServiceAccountSpec

Defines the desired state of the `ProjectServiceAccount` resource.

_Appears in:_ \- ProjectServiceAccount

Field | Description  
---|---  
`keys` _ProjectServiceAccountKey array_ | The public keys used to verify the signature of the JWTs for the `ProjectServiceAccount` resource.  
  
### ProjectServiceAccountStatus

Defines the observed state of the `ProjectServiceAccount` resource.

_Appears in:_ \- ProjectServiceAccount

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | If the `Ready` condition is `True`, all `ServiceAccount` resources are successfully propagated to all clusters of its project. If the `Ready` condition is `False`, some `ServiceAccount` resources have failed to propagate. The `Ready` condition can transition from `True` to `Unknown` if the corresponding `ServiceAccount` resource in a user cluster is modified, which triggers another propagation.  
`propagatedName` _string_ | The name of the propagated `ServiceAccount` resource.  
`clusters` _ClusterStatus array_ | The list of all selected cluster names and the conditions of the propagated resources in the clusters.  
  
### ProjectStatus

Provides the status of a project.

_Appears in:_ \- Project

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`propagatedName` _string_ | The name of the propagated namespace.  
`clusters` _ProjectClusterStatus array_ | The propagation statuses and egress NAT IP addresses of all user clusters this project spans across.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
