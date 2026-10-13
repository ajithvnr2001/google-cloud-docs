---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataConnector/acquireAndStoreRefreshToken/
title: Method: projects.locations.collections.dataConnector.acquireAndStoreRefreshToken \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:28.515397+00:00
---

# Method: projects.locations.collections.dataConnector.acquireAndStoreRefreshToken  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataConnector/acquireAndStoreRefreshToken/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataConnector.acquireAndStoreRefreshToken Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AdditionalOAuthResponse
    * JSON representation



Exchanges OAuth authorization credentials for a refresh token and stores the refresh token and the scopes. The stored data will be keyed by the connector name and the user identifier from the EUC.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{name=projects/*/locations/*/collections/*/dataConnector}:acquireAndStoreRefreshToken`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Connector resource.The connector name identifies the 3rd party system to use for authorization. It is also used as a key to store the refresh token.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "scopes": [
        string
      ],
      "fullRedirectUri": string,
      "instanceUri": string
    }  
  
Fields  
---  
`scopes[]` |  `string` The scopes of the authorization code and the refresh token.  
`fullRedirectUri` |  `string` Required. The URI the user is redirected to after authorization, including all parameters. E.g., `https://example.com/redir?code=5`  
`instanceUri` |  `string` Optional. The instance URI for the connector, if provided, supported connectors will use this instance URI to construct the token exchange URL. For example, Shopify instance URI is the shop URL.  
  
### Response body

Response message for `[DataConnectorService.AcquireAndStoreRefreshToken](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataConnector/acquireAndStoreRefreshToken#google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAndStoreRefreshToken)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "additionalOauthResponses": [
        {
          object ([AdditionalOAuthResponse](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataConnector/acquireAndStoreRefreshToken#AdditionalOAuthResponse))
        }
      ]
    }  
  
Fields  
---  
`additionalOauthResponses[]` |  `object (`[AdditionalOAuthResponse](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataConnector/acquireAndStoreRefreshToken#AdditionalOAuthResponse)`)` Optional. Additional OAuth responses from the authorization response. This field is optional and will not always be populated. It depends on the connector's type and the authorization response.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.dataConnectors.acquireAndStoreRefreshToken`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AdditionalOAuthResponse

Additional OAuth responses from the authorization response.

JSON representation  
---  
      
    
    {
      "key": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "stringValue": string,
      "intValue": string,
      "boolValue": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`key` |  `string` The key of the additional OAuth response.  
The value of the additional OAuth response. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`stringValue` |  `string` The string value of the additional OAuth response.  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The integer value of the additional OAuth response.  
`boolValue` |  `boolean` The boolean value of the additional OAuth response.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
