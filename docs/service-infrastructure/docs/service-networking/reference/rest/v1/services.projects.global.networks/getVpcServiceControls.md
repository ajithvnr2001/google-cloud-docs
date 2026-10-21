---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/getVpcServiceControls/
title: Method: services.projects.global.networks.getVpcServiceControls \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:38.743378+00:00
---

# Method: services.projects.global.networks.getVpcServiceControls  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/getVpcServiceControls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.projects.global.networks.getVpcServiceControls Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Consumers can use this method to view whether VPC Service Controls is enabled or disabled for a connection.

### HTTP request

`GET https://servicenetworking.googleapis.com/v1/{name=services/*/projects/*/global/networks/*}/vpcServiceControls`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the VPC Service Controls config to retrieve in the format: `services/{service}/projects/{project}/global/networks/{network}`. {service} is the service that is managing connectivity for the service producer's organization. For Google services that support this functionality, this value is `servicenetworking.googleapis.com`. {project} is a project number e.g. `12345` that contains the service consumer's VPC network. {network} is the name of the service consumer's VPC network. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/roles-permissions/servicenetworking) permission on the specified resource `name`:

  * `servicenetworking.services.getVpcServiceControls`

  
  
### Request body

The request body must be empty.

### Response body

Response for the get VPC Service Controls request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Output only. Indicates whether the VPC Service Controls is enabled or disabled for the connection. If the consumer called the services.enableVpcServiceControls method, then this is true. If the consumer called services.disableVpcServiceControls, then this is false. The default is false.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
