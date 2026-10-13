---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/v1/marketplace-v1/
title: KRM API marketplace.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:40.665641+00:00
---

# KRM API marketplace.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/v1/marketplace-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API marketplace.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## marketplace.gdc.goog/v1

Contains API Schema definitions for the Marketplace API group.

### IconType

_Underlying type:_ `string` IconType represents the type of icon asset.

_Appears in:_ \- ServiceDescriptionSpec

### ServiceDescription

ServiceDescription represents a description of a Marketplace service.

_Appears in:_ \- ServiceDescriptionList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.gdc.goog/v1`  
`kind` _string_ | `ServiceDescription`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceDescriptionSpec_ |   
  
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
`apiVersion` _string_ | `marketplace.gdc.goog/v1`  
`kind` _string_ | `ServiceDescriptionList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceDescription array_ |   
  
### ServiceDescriptionSpec

ServiceDescriptionSpec defines a service description of a Marketplace service.

_Appears in:_ \- ServiceDescription

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
  
### ServiceInstance

Represents an installed instance of a Marketplace service.

_Appears in:_ \- ServiceInstanceList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.gdc.goog/v1`  
`kind` _string_ | `ServiceInstance`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceInstanceSpec_ |   
`status` _ServiceInstanceStatus_ |   
  
### ServiceInstanceList

Represents a collection of `ServiceInstance` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.gdc.goog/v1`  
`kind` _string_ | `ServiceInstanceList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceInstance array_ |   
  
### ServiceInstanceSpec

Defines an installed instance of a Marketplace service.

_Appears in:_ \- ServiceInstance

Field | Description  
---|---  
`serviceVersionRef` _NamespacedName_ | ServiceVersionRef references the ServiceVersion for this instance.  
`clusterRef` _NamespacedName_ | The name of the cluster to install the service instance.  
`targetNamespace` _string_ | TargetNamespace specifies an optional namespace where the service instance should be installed.  
`parameters` _[JSON](https://pkg.go.dev/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1#JSON)_ | The parameters to configure for the service instance. This can contain arbitrary JSON data.  
  
### ServiceInstanceStatus

Defines the observed state of a Marketplace service instance.

_Appears in:_ \- ServiceInstance

Field | Description  
---|---  
`installedVersion` _string_ | The currently running version. An empty string indicates no version is installed.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The indicator for whether the installation is successful, or if any errors occurred.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with the observed times included.  
  
### ServiceVersion

Represents a single version of a Marketplace service.

_Appears in:_ \- ServiceVersionList

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.gdc.goog/v1`  
`kind` _string_ | `ServiceVersion`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ServiceVersionSpec_ |   
  
### ServiceVersionList

Represents a collection of `ServiceVersion` custom resources.

Field | Description  
---|---  
`apiVersion` _string_ | `marketplace.gdc.goog/v1`  
`kind` _string_ | `ServiceVersionList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ServiceVersion array_ |   
  
### ServiceVersionSpec

Defines an available version of a Marketplace service.

_Appears in:_ \- ServiceVersion

Field | Description  
---|---  
`version` _string_ | The version of this service.  
`harborProject` _string_ | The name of the project where service Helm is stored.  
`entrypoint` _string_ | The name of the Helm chart whose lifecycle will be managed.  
`defaultConfiguration` _string_ | The default configuration of the Helm chart values.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
