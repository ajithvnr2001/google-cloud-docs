---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/update/
title: Method: responsePolicyRules.update \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:22.853754+00:00
---

# Method: responsePolicyRules.update  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Method: responsePolicyRules.update Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Updates an existing Response Policy Rule.

### HTTP request

`PUT https://dns.googleapis.com/dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Identifies the project addressed by this request.  
`responsePolicy` |  `string` User assigned name of the Response Policy containing the Response Policy Rule.  
`responsePolicyRule` |  `string` User assigned name of the Response Policy Rule addressed by this request.  
  
### Query parameters

Parameters  
---  
`clientOperationId` |  `string` For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.  
  
### Request body

The request body contains an instance of `[ResponsePolicyRule](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules#ResponsePolicyRule)`.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "responsePolicyRule": {
        object ([ResponsePolicyRule](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules#ResponsePolicyRule))
      }
    }  
  
Fields  
---  
`responsePolicyRule` |  `object (`[ResponsePolicyRule](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules#ResponsePolicyRule)`)`  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ndev.clouddns.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `project` resource:

  * `dns.responsePolicyRules.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
