---
url: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/projects.locations.gatewaySecurityPolicies.rules/list/
title: Method: projects.locations.gatewaySecurityPolicies.rules.list \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:59.086882+00:00
---

# Method: projects.locations.gatewaySecurityPolicies.rules.list  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/projects.locations.gatewaySecurityPolicies.rules/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Reference ](https://docs.cloud.google.com/secure-web-proxy/docs/apis)



Send feedback 

#  Method: projects.locations.gatewaySecurityPolicies.rules.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists GatewaySecurityPolicyRules in a given project and location.

### HTTP request

`GET https://networksecurity.googleapis.com/v1alpha1/{parent=projects/*/locations/*/gatewaySecurityPolicies/*}/rules`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project, location and GatewaySecurityPolicy from which the GatewaySecurityPolicyRules should be listed, specified in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networksecurity.gatewaySecurityPolicyRules.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of GatewaySecurityPolicyRules to return per call.  
`pageToken` |  `string` The value returned by the last 'ListGatewaySecurityPolicyRulesResponse' Indicates that this is a continuation of a prior 'rules.list' call, and that the system should return the next page of data.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response returned by the rules.list method.

JSON representation  
---  
      
    
    {
      "gatewaySecurityPolicyRules": [
        {
          object ([GatewaySecurityPolicyRule](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/projects.locations.gatewaySecurityPolicies.rules#GatewaySecurityPolicyRule))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`gatewaySecurityPolicyRules[]` |  `object (`[GatewaySecurityPolicyRule](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/projects.locations.gatewaySecurityPolicies.rules#GatewaySecurityPolicyRule)`)` List of GatewaySecurityPolicyRule resources.  
`nextPageToken` |  `string` If there might be more results than those appearing in this response, then 'nextPageToken' is included. To get the next set of results, call this method again using the value of 'nextPageToken' as 'pageToken'.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
