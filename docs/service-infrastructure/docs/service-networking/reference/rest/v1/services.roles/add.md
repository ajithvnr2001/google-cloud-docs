---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.roles/add/
title: Method: services.roles.add \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:39.924090+00:00
---

# Method: services.roles.add  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.roles/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.roles.add Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * PolicyBinding
    * JSON representation
  * Try it!



Service producers can use this method to add roles in the shared VPC host project. Each role is bound to the provided member. Each role must be selected from within an allowlisted set of roles. Each role is applied at only the granularity specified in the allowlist.

### HTTP request

`POST https://servicenetworking.googleapis.com/v1/{parent=services/*}/roles:add`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. This is in a form services/{service} where {service} is the name of the private access management service. For example 'service-peering.example.com'. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `servicenetworking.services.addSubnetwork`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "consumerNetwork": string,
      "policyBinding": [
        {
          object ([PolicyBinding](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.roles/add#PolicyBinding))
        }
      ]
    }  
  
Fields  
---  
`consumerNetwork` |  `string` Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is a project number, as in '12345' {network} is a network name.  
`policyBinding[]` |  `object (`[PolicyBinding](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.roles/add#PolicyBinding)`)` Required. List of policy bindings to add to shared VPC host project.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## PolicyBinding

Grouping of IAM role and IAM member.

JSON representation  
---  
      
    
    {
      "role": string,
      "member": string
    }  
  
Fields  
---  
`role` |  `string` Required. Role to apply. Only allowlisted roles can be used at the specified granularity. The role must be one of the following: - 'roles/container.hostServiceAgentUser' applied on the shared VPC host project - 'roles/compute.securityAdmin' applied on the shared VPC host project - 'roles/compute.networkAdmin' applied on the shared VPC host project - 'roles/tpu.xpnAgent' applied on the shared VPC host project - 'roles/dns.admin' applied on the shared VPC host project - 'roles/logging.admin' applied on the shared VPC host project - 'roles/monitoring.viewer' applied on the shared VPC host project - 'roles/servicemanagement.quotaViewer' applied on the shared VPC host project  
`member` |  `string` Required. Member to bind the role with. See [IAM policy bindings](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding) for how to format each member. Eg. - user:[myuser@mydomain.com](mailto:myuser@mydomain.com) \- serviceAccount:[my-service-account@app.gserviceaccount.com](mailto:my-service-account@app.gserviceaccount.com)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
