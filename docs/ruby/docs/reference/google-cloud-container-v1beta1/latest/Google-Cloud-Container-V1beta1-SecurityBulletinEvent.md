---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-SecurityBulletinEvent/
title: Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::SecurityBulletinEvent (v0.57.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:43.808641+00:00
---

# Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::SecurityBulletinEvent (v0.57.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-SecurityBulletinEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::SecurityBulletinEvent (v0.57.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.57.1 (latest)  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.1  0.50.0  0.49.1  0.48.0  0.47.0  0.46.0  0.45.1  0.44.0  0.43.0  0.42.1  0.41.0  0.40.1  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.3  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.3 

Reference documentation and code samples for the Kubernetes Engine V1beta1 API class Google::Cloud::Container::V1beta1::SecurityBulletinEvent.

SecurityBulletinEvent is a notification sent to customers when a security bulletin has been posted that they are vulnerable to.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #affected_supported_minors
    
    
    def affected_supported_minors() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The GKE minor versions affected by this vulnerability. 



### #affected_supported_minors=
    
    
    def affected_supported_minors=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The GKE minor versions affected by this vulnerability. 



**Returns**

  * (::Array<::String>) — The GKE minor versions affected by this vulnerability. 



### #brief_description
    
    
    def brief_description() -> ::String

**Returns**

  * (::String) — A brief description of the bulletin. See the bulletin pointed to by the bulletin_uri field for an expanded description. 



### #brief_description=
    
    
    def brief_description=(value) -> ::String

**Parameter**

  * **value** (::String) — A brief description of the bulletin. See the bulletin pointed to by the bulletin_uri field for an expanded description. 



**Returns**

  * (::String) — A brief description of the bulletin. See the bulletin pointed to by the bulletin_uri field for an expanded description. 



### #bulletin_id
    
    
    def bulletin_id() -> ::String

**Returns**

  * (::String) — The ID of the bulletin corresponding to the vulnerability. 



### #bulletin_id=
    
    
    def bulletin_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID of the bulletin corresponding to the vulnerability. 



**Returns**

  * (::String) — The ID of the bulletin corresponding to the vulnerability. 



### #bulletin_uri
    
    
    def bulletin_uri() -> ::String

**Returns**

  * (::String) — The URI link to the bulletin on the website for more information. 



### #bulletin_uri=
    
    
    def bulletin_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The URI link to the bulletin on the website for more information. 



**Returns**

  * (::String) — The URI link to the bulletin on the website for more information. 



### #cve_ids
    
    
    def cve_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The CVEs associated with this bulletin. 



### #cve_ids=
    
    
    def cve_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The CVEs associated with this bulletin. 



**Returns**

  * (::Array<::String>) — The CVEs associated with this bulletin. 



### #manual_steps_required
    
    
    def manual_steps_required() -> ::Boolean

**Returns**

  * (::Boolean) — If this field is specified, it means there are manual steps that the user must take to make their clusters safe. 



### #manual_steps_required=
    
    
    def manual_steps_required=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If this field is specified, it means there are manual steps that the user must take to make their clusters safe. 



**Returns**

  * (::Boolean) — If this field is specified, it means there are manual steps that the user must take to make their clusters safe. 



### #mitigated_versions
    
    
    def mitigated_versions() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The GKE versions where this vulnerability is mitigated. 



### #mitigated_versions=
    
    
    def mitigated_versions=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The GKE versions where this vulnerability is mitigated. 



**Returns**

  * (::Array<::String>) — The GKE versions where this vulnerability is mitigated. 



### #patched_versions
    
    
    def patched_versions() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The GKE versions where this vulnerability is patched. 



### #patched_versions=
    
    
    def patched_versions=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The GKE versions where this vulnerability is patched. 



**Returns**

  * (::Array<::String>) — The GKE versions where this vulnerability is patched. 



### #resource_type_affected
    
    
    def resource_type_affected() -> ::String

**Returns**

  * (::String) — The resource type (node/control plane) that has the vulnerability. Multiple notifications (1 notification per resource type) will be sent for a vulnerability that affects > 1 resource type. 



### #resource_type_affected=
    
    
    def resource_type_affected=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource type (node/control plane) that has the vulnerability. Multiple notifications (1 notification per resource type) will be sent for a vulnerability that affects > 1 resource type. 



**Returns**

  * (::String) — The resource type (node/control plane) that has the vulnerability. Multiple notifications (1 notification per resource type) will be sent for a vulnerability that affects > 1 resource type. 



### #severity
    
    
    def severity() -> ::String

**Returns**

  * (::String) — The severity of this bulletin as it relates to GKE. 



### #severity=
    
    
    def severity=(value) -> ::String

**Parameter**

  * **value** (::String) — The severity of this bulletin as it relates to GKE. 



**Returns**

  * (::String) — The severity of this bulletin as it relates to GKE. 



### #suggested_upgrade_target
    
    
    def suggested_upgrade_target() -> ::String

**Returns**

  * (::String) — This represents a version selected from the patched_versions field that the cluster receiving this notification should most likely want to upgrade to based on its current version. Note that if this notification is being received by a given cluster, it means that this version is currently available as an upgrade target in that cluster's location. 



### #suggested_upgrade_target=
    
    
    def suggested_upgrade_target=(value) -> ::String

**Parameter**

  * **value** (::String) — This represents a version selected from the patched_versions field that the cluster receiving this notification should most likely want to upgrade to based on its current version. Note that if this notification is being received by a given cluster, it means that this version is currently available as an upgrade target in that cluster's location. 



**Returns**

  * (::String) — This represents a version selected from the patched_versions field that the cluster receiving this notification should most likely want to upgrade to based on its current version. Note that if this notification is being received by a given cluster, it means that this version is currently available as an upgrade target in that cluster's location. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
