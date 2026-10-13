---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-FrameworkDeployment/
title: Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::FrameworkDeployment (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:53.420752+00:00
---

# Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::FrameworkDeployment (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-FrameworkDeployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::FrameworkDeployment (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Cloud Security Compliance V1 API class Google::Cloud::CloudSecurityCompliance::V1::FrameworkDeployment.

Framework deployments represent the assignment of a framework to a target resource. Supported target resources are organizations, folders, and projects.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cloud_control_deployment_references
    
    
    def cloud_control_deployment_references() -> ::Array<::Google::Cloud::CloudSecurityCompliance::V1::CloudControlDeploymentReference>

**Returns**

  * (::Array<[::Google::Cloud::CloudSecurityCompliance::V1::CloudControlDeploymentReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-CloudControlDeploymentReference)>) — Output only. The references to the cloud control deployments. The reference includes all the cloud control deployments that are in the framework or in a cloud control group.

For example, if a framework deployment deploys two cloud controls, `cc-deployment-1` and `cc-deployment-2`, then the references are:

` { cloud_control_deployment_reference: { cloud_control_deployment: "organizations/\\{organization}/locations/\\{location}/cloudControlDeployments/cc-deployment-1" }, cloud_control_deployment_reference: { cloud_control_deployment: "organizations/\\{organization}/locations/\\{location}/cloudControlDeployments/cc-deployment-2" } `




### #cloud_control_metadata
    
    
    def cloud_control_metadata() -> ::Array<::Google::Cloud::CloudSecurityCompliance::V1::CloudControlMetadata>

**Returns**

  * (::Array<[::Google::Cloud::CloudSecurityCompliance::V1::CloudControlMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-CloudControlMetadata)>) — Required. The deployment mode and parameters for each of the cloud controls in the framework. Every cloud control in the framework includes metadata. 



### #cloud_control_metadata=
    
    
    def cloud_control_metadata=(value) -> ::Array<::Google::Cloud::CloudSecurityCompliance::V1::CloudControlMetadata>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudSecurityCompliance::V1::CloudControlMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-CloudControlMetadata)>) — Required. The deployment mode and parameters for each of the cloud controls in the framework. Every cloud control in the framework includes metadata. 



**Returns**

  * (::Array<[::Google::Cloud::CloudSecurityCompliance::V1::CloudControlMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-CloudControlMetadata)>) — Required. The deployment mode and parameters for each of the cloud controls in the framework. Every cloud control in the framework includes metadata. 



### #computed_target_resource
    
    
    def computed_target_resource() -> ::String

**Returns**

  * (::String) — 

Output only. The target resource to deploy the framework to, in one the following formats:

    * `organizations/{organizationID}`
    * `folders/{folderID}`
    * `projects/{projectID}`



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which the resource was created. 



### #deployment_state
    
    
    def deployment_state() -> ::Google::Cloud::CloudSecurityCompliance::V1::DeploymentState

**Returns**

  * ([::Google::Cloud::CloudSecurityCompliance::V1::DeploymentState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-DeploymentState)) — Output only. The state for the framework deployment. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. A user-provided description of the framework deployment. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A user-provided description of the framework deployment. 



**Returns**

  * (::String) — Optional. A user-provided description of the framework deployment. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. To prevent concurrent updates from overwriting each other, always provide the `etag` when you update a framework deployment. You can also provide the `etag` when you delete a framework deployment, to help ensure that you're deleting the intended version of the framework deployment. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. To prevent concurrent updates from overwriting each other, always provide the `etag` when you update a framework deployment. You can also provide the `etag` when you delete a framework deployment, to help ensure that you're deleting the intended version of the framework deployment. 



**Returns**

  * (::String) — Optional. To prevent concurrent updates from overwriting each other, always provide the `etag` when you update a framework deployment. You can also provide the `etag` when you delete a framework deployment, to help ensure that you're deleting the intended version of the framework deployment. 



### #framework
    
    
    def framework() -> ::Google::Cloud::CloudSecurityCompliance::V1::FrameworkReference

**Returns**

  * ([::Google::Cloud::CloudSecurityCompliance::V1::FrameworkReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-FrameworkReference)) — Required. A reference to the framework that you're deploying. 



### #framework=
    
    
    def framework=(value) -> ::Google::Cloud::CloudSecurityCompliance::V1::FrameworkReference

**Parameter**

  * **value** ([::Google::Cloud::CloudSecurityCompliance::V1::FrameworkReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-FrameworkReference)) — Required. A reference to the framework that you're deploying. 



**Returns**

  * ([::Google::Cloud::CloudSecurityCompliance::V1::FrameworkReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-FrameworkReference)) — Required. A reference to the framework that you're deploying. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The name of the framework deployment, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The name of the framework deployment, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`. 



**Returns**

  * (::String) — Identifier. The name of the framework deployment, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`. 



### #target_resource_config
    
    
    def target_resource_config() -> ::Google::Cloud::CloudSecurityCompliance::V1::TargetResourceConfig

**Returns**

  * ([::Google::Cloud::CloudSecurityCompliance::V1::TargetResourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-TargetResourceConfig)) — Required. The details of the target resource that you want to deploy the framework to. You can specify an existing resource, or create a new one. 



### #target_resource_config=
    
    
    def target_resource_config=(value) -> ::Google::Cloud::CloudSecurityCompliance::V1::TargetResourceConfig

**Parameter**

  * **value** ([::Google::Cloud::CloudSecurityCompliance::V1::TargetResourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-TargetResourceConfig)) — Required. The details of the target resource that you want to deploy the framework to. You can specify an existing resource, or create a new one. 



**Returns**

  * ([::Google::Cloud::CloudSecurityCompliance::V1::TargetResourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-TargetResourceConfig)) — Required. The details of the target resource that you want to deploy the framework to. You can specify an existing resource, or create a new one. 



### #target_resource_display_name
    
    
    def target_resource_display_name() -> ::String

**Returns**

  * (::String) — Output only. The display name of the target resource. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which the resource last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
