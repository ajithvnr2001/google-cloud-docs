---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-SecurityPosture/
title: Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::SecurityPosture (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:42.918449+00:00
---

# Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::SecurityPosture (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-SecurityPosture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::SecurityPosture (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.2  0.33.0  0.32.0  0.31.1  0.30.0  0.29.1  0.28.0  0.27.0  0.26.0  0.25.1  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1 

Reference documentation and code samples for the Cloud Security Command Center V1 API class Google::Cloud::SecurityCenter::V1::SecurityPosture.

Represents a posture that is deployed on Google Cloud by the Security Command Center Posture Management service. A posture contains one or more policy sets. A policy set is a group of policies that enforce a set of security rules on Google Cloud.

## Inherits

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-Kubernetes-Object)



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #changed_policy
    
    
    def changed_policy() -> ::String

**Returns**

  * (::String) — The name of the updated policy, for example, `projects/{project_id}/policies/{constraint_name}`. 



### #changed_policy=
    
    
    def changed_policy=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the updated policy, for example, `projects/{project_id}/policies/{constraint_name}`. 



**Returns**

  * (::String) — The name of the updated policy, for example, `projects/{project_id}/policies/{constraint_name}`. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of the posture, for example, `CIS-Posture`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the posture, for example, `CIS-Posture`. 



**Returns**

  * (::String) — Name of the posture, for example, `CIS-Posture`. 



### #policy
    
    
    def policy() -> ::String

**Returns**

  * (::String) — The ID of the updated policy, for example, `compute-policy-1`. 



### #policy=
    
    
    def policy=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID of the updated policy, for example, `compute-policy-1`. 



**Returns**

  * (::String) — The ID of the updated policy, for example, `compute-policy-1`. 



### #policy_drift_details
    
    
    def policy_drift_details() -> ::Array<::Google::Cloud::SecurityCenter::V1::SecurityPosture::PolicyDriftDetails>

**Returns**

  * (::Array<[::Google::Cloud::SecurityCenter::V1::SecurityPosture::PolicyDriftDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-SecurityPosture-PolicyDriftDetails)>) — The details about a change in an updated policy that violates the deployed posture. 



### #policy_drift_details=
    
    
    def policy_drift_details=(value) -> ::Array<::Google::Cloud::SecurityCenter::V1::SecurityPosture::PolicyDriftDetails>

**Parameter**

  * **value** (::Array<[::Google::Cloud::SecurityCenter::V1::SecurityPosture::PolicyDriftDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-SecurityPosture-PolicyDriftDetails)>) — The details about a change in an updated policy that violates the deployed posture. 



**Returns**

  * (::Array<[::Google::Cloud::SecurityCenter::V1::SecurityPosture::PolicyDriftDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-SecurityPosture-PolicyDriftDetails)>) — The details about a change in an updated policy that violates the deployed posture. 



### #policy_set
    
    
    def policy_set() -> ::String

**Returns**

  * (::String) — The name of the updated policyset, for example, `cis-policyset`. 



### #policy_set=
    
    
    def policy_set=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the updated policyset, for example, `cis-policyset`. 



**Returns**

  * (::String) — The name of the updated policyset, for example, `cis-policyset`. 



### #posture_deployment
    
    
    def posture_deployment() -> ::String

**Returns**

  * (::String) — The name of the posture deployment, for example, `organizations/{org_id}/posturedeployments/{posture_deployment_id}`. 



### #posture_deployment=
    
    
    def posture_deployment=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the posture deployment, for example, `organizations/{org_id}/posturedeployments/{posture_deployment_id}`. 



**Returns**

  * (::String) — The name of the posture deployment, for example, `organizations/{org_id}/posturedeployments/{posture_deployment_id}`. 



### #posture_deployment_resource
    
    
    def posture_deployment_resource() -> ::String

**Returns**

  * (::String) — The project, folder, or organization on which the posture is deployed, for example, `projects/{project_number}`. 



### #posture_deployment_resource=
    
    
    def posture_deployment_resource=(value) -> ::String

**Parameter**

  * **value** (::String) — The project, folder, or organization on which the posture is deployed, for example, `projects/{project_number}`. 



**Returns**

  * (::String) — The project, folder, or organization on which the posture is deployed, for example, `projects/{project_number}`. 



### #revision_id
    
    
    def revision_id() -> ::String

**Returns**

  * (::String) — The version of the posture, for example, `c7cfa2a8`. 



### #revision_id=
    
    
    def revision_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The version of the posture, for example, `c7cfa2a8`. 



**Returns**

  * (::String) — The version of the posture, for example, `c7cfa2a8`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
