---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/v1/global-marketplace-v1/
title: KRM API marketplace.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:07.447504+00:00
---

# KRM API marketplace.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/v1/global-marketplace-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API marketplace.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## marketplace.global.gdc.goog/v1

Contains API Schema definitions for the Marketplace API group.

### CatalogOwner

CatalogOwner represents Catalog Owner Information including the Catalog Admin Account and the Catalog Owning Team.

_Appears in:_ \- ServiceCatalogSpec

Field | Description  
---|---  
`admin` _string_ | Catalog Admin Account.  
`team` _string_ | Catalog Owning Team.  
  
### IconType

_Underlying type:_ `string` IconType represents the type of icon asset.

_Appears in:_ \- ServiceDescriptionSpec

### NameSelector

Provides a list of Project Name for Service Catalog Binding to match with.

_Appears in:_ \- ServiceCatalogBindingSelector

Field | Description  
---|---  
`matchNames` _string array_ |   
  
### ServiceCatalog

Represents a single group of Marketplace services.

_Appears in:_ \- ServiceCatalogList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalog`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceCatalogSpec_ |   
`status` _ServiceCatalogStatus_ |   
  
### ServiceCatalogBinding

Represents a ServiceCatalog to Project mapping relations.

_Appears in:_ \- ServiceCatalogBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalogBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceCatalogBindingSpec_ |   
`status` _ServiceCatalogBindingStatus_ |   
  
### ServiceCatalogBindingList

Represents a collection of `ServiceCatalogBinding` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalogBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceCatalogBinding array_ |   
  
### ServiceCatalogBindingReplica

Represents a ServiceCatalog to Project mapping relations.

_Appears in:_ \- ServiceCatalogBindingReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalogBindingReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceCatalogBindingSpec_ |   
`status` _ServiceCatalogBindingReplicaStatus_ |   
  
### ServiceCatalogBindingReplicaList

Represents a collection of `ServiceCatalogBindingReplica` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalogBindingReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceCatalogBindingReplica array_ |   
  
### ServiceCatalogBindingSelector

Provides a set of rules to match Projects. Must choose exactly 0 or 1 of the selectors. 0 selector matches all Projects.

_Appears in:_ \- ServiceCatalogBindingSpec

Field | Description  
---|---  
`nameSelector` _NameSelector_ | NameSelector is used to specify the list of names of Projects.  
`labelSelector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | LabelSelector is used to specify the list of label and values of Projects.  
  
### ServiceCatalogBindingSpec

Provides the specification, or desired state, of a ServiceCatalogBinding resource.

_Appears in:_ \- ServiceCatalogBinding \- ServiceCatalogBindingReplica

Field | Description  
---|---  
`serviceCatalogRef` _NamespacedName_ | ServiceCatalogRef represents the ServiceCatalog in this ServiceCatalogBinding.  
`selector` _ServiceCatalogBindingSelector_ | Selector is used to specify a set of rules to match Projects.  
  
### ServiceCatalogBindingStatus

Provides the overall status of a global service catalog binding.

_Appears in:_ \- ServiceCatalogBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ServiceCatalogBindingZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ServiceCatalogBindingZoneStatus

Provides the status of a Service Catalog rolling out to a particular zone.

_Appears in:_ \- ServiceCatalogBindingStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ServiceCatalogBindingReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### ServiceCatalogList

Represents a collection of `ServiceCatalog` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalogList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceCatalog array_ |   
  
### ServiceCatalogReplica

Represents a single group of Marketplace services.

_Appears in:_ \- ServiceCatalogReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalogReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceCatalogSpec_ |   
`status` _ServiceCatalogReplicaStatus_ |   
  
### ServiceCatalogReplicaList

Represents a collection of `ServiceCatalogReplica` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceCatalogReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceCatalogReplica array_ |   
  
### ServiceCatalogSpec

ServiceCatalogSpec defines catalog owner information and a list of accessible Service Descriptions.

_Appears in:_ \- ServiceCatalog \- ServiceCatalogReplica

Field | Description  
---|---  
`displayName` _string_ | Display name for this ServiceCatalog.  
`owner` _CatalogOwner_ | Catalog Owner Information.  
`serviceDescriptionRef` _NamespacedName array_ | List of Service Descriptions Included in the ServiceCatalog.  
  
### ServiceCatalogStatus

Provides the overall status of a global service catalog.

_Appears in:_ \- ServiceCatalog

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ServiceCatalogZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ServiceCatalogZoneStatus

Provides the status of a Service Catalog rolling out to a particular zone.

_Appears in:_ \- ServiceCatalogStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ServiceCatalogReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### ServiceDescription

ServiceDescription represents a description of a Marketplace service.

_Appears in:_ \- ServiceDescriptionList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceDescription`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceDescriptionSpec_ |   
`status` _ServiceDescriptionStatus_ |   
  
### ServiceDescriptionDetails

ServiceDescriptionDetails defines the fields available for a given section.

_Appears in:_ \- ServiceDescriptionSpec

Field | Description  
---|---  
`details` _string_ | Description details HTML-formatted section.  
`url` _string_ | Description URL, if available.  
  
### ServiceDescriptionList

Represents a collection of `ServiceDescription` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceDescriptionList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceDescription array_ |   
  
### ServiceDescriptionReplica

Represents a description of a Marketplace service.

_Appears in:_ \- ServiceDescriptionReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceDescriptionReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceDescriptionSpec_ |   
`status` _ServiceDescriptionReplicaStatus_ |   
  
### ServiceDescriptionReplicaList

Represents a collection of `ServiceDescriptionReplica` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceDescriptionReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceDescriptionReplica array_ |   
  
### ServiceDescriptionSpec

ServiceDescriptionSpec defines a service description of a Marketplace service.

_Appears in:_ \- ServiceDescription \- ServiceDescriptionReplica

Field | Description  
---|---  
`serviceName` _string_ | Selector value corresponding to "marketplace.gdc.goog/service-name" label.  
`displayName` _string_ | Display name for this service.  
`vendor` _string_ | Vendor for this service.  
`description` _string_ | Short description for this service.  
`serviceType` _string_ | Type of this service for Overview page.  
`iconType` _IconType_ | Type of icon asset.  
`iconSource` _string_ | Source data for the icon asset, e.g. base64-encoded image.  
`overview` _string_ | Service overview HTML-formatted section.  
`pricing` _ServiceDescriptionDetails_ | Service pricing HTML-formatted section.  
`support` _string_ | Service support HTML-formatted section.  
`terms` _ServiceDescriptionDetails_ | Service terms HTML-formatted section.  
`contactInfo` _string_ | Service contact info HTML-formatted section.  
`documentation` _ServiceDescriptionDetails_ | Service documentation details.  
`categories` _string array_ | Additional details for "Categories".  
  
### ServiceDescriptionStatus

Provides the overall status of a global service description.

_Appears in:_ \- ServiceDescription

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ServiceDescriptionZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ServiceDescriptionZoneStatus

Provides the status of a Service Description rolling out to a particular zone.

_Appears in:_ \- ServiceDescriptionStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ServiceDescriptionReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### ServiceVersion

Represents a single version of a Marketplace service.

_Appears in:_ \- ServiceVersionList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceVersion`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceVersionSpec_ |   
`status` _ServiceVersionStatus_ |   
  
### ServiceVersionList

Represents a collection of `ServiceVersion` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceVersionList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceVersion array_ |   
  
### ServiceVersionReplica

Represents a single version of a Marketplace service.

_Appears in:_ \- ServiceVersionReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceVersionReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceVersionSpec_ |   
`status` _ServiceVersionReplicaStatus_ |   
  
### ServiceVersionReplicaList

Represents a collection of `ServiceVersionReplica` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.global.gdc.goog/v1`  
`kind` _string_ | `ServiceVersionReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceVersionReplica array_ |   
  
### ServiceVersionSpec

Defines an available version of a Marketplace service.

_Appears in:_ \- ServiceVersion \- ServiceVersionReplica

Field | Description  
---|---  
`version` _string_ | The version of this service.  
`harborProject` _string_ | The name of the project where service Helm is stored.  
`entrypoint` _string_ | The name of the Helm chart whose lifecycle will be managed.  
`defaultConfiguration` _string_ | The default configuration of the Helm chart values.  
  
### ServiceVersionStatus

Provides the overall status of a global service version.

_Appears in:_ \- ServiceVersion

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ServiceVersionZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ServiceVersionZoneStatus

Provides the status of a Service Version rolling out to a particular zone.

_Appears in:_ \- ServiceVersionStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ServiceVersionReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
