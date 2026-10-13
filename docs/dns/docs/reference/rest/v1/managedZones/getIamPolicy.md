---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/getIamPolicy/
title: Method: managedZones.getIamPolicy \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:18.427304+00:00
---

# Method: managedZones.getIamPolicy  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/getIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Method: managedZones.getIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

### HTTP request

`POST https://dns.googleapis.com/dns/v1/{resource=projects/*/managedZones/*}:getIamPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. It takes the form `projects/{project}/managedZones/{managedzone}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "options": {
        object ([GetPolicyOptions](https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions))
      }
    }  
  
Fields  
---  
`options` |  `object (`[GetPolicyOptions](https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions)`)` OPTIONAL: A `GetPolicyOptions` object for specifying options to `managedZones.getIamPolicy`.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/Policy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`
  * ` https://www.googleapis.com/auth/ndev.clouddns.readonly`
  * ` https://www.googleapis.com/auth/ndev.clouddns.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `resource` resource:

  * `dns.managedZones.getIamPolicy`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
