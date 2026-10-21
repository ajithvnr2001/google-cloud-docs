---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/finishOAuthFlow/
title: Method: projects.locations.accountConnectors.users.finishOAuthFlow \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:06.130107+00:00
---

# Method: projects.locations.accountConnectors.users.finishOAuthFlow  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/finishOAuthFlow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.accountConnectors.users.finishOAuthFlow Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * OAuthParams
    * JSON representation
  * GoogleOAuthParams
    * JSON representation
  * Try it!



Finishes OAuth flow for an account connector.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:finishOAuthFlow`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`accountConnector` |  `string` Required. The resource name of the AccountConnector in the format `projects/*/locations/*/accountConnectors/*`.  
  
### Query parameters

Parameters  
---  
Union parameter `params`. The params returned by OAuth flow redirect. `params` can be only one of the following:  
`oauthParams` |  `object (`[OAuthParams](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/finishOAuthFlow#OAuthParams)`)` The params returned by non-Google OAuth 2.0 flow redirect.  
`googleOauthParams` |  `object (`[GoogleOAuthParams](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/finishOAuthFlow#GoogleOAuthParams)`)` The params returned by Google OAuth flow redirects.  
  
### Request body

The request body must be empty.

### Response body

Message for responding to finishing an OAuth flow.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "exchangeError": {
        object ([ExchangeError](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/ExchangeError))
      }
    }  
  
Fields  
---  
`exchangeError` |  `object (`[ExchangeError](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/ExchangeError)`)` The error resulted from exchanging OAuth tokens from the service provider.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `accountConnector` resource:

  * `developerconnect.users.finishOAuth`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## OAuthParams

The params returned by non-Google OAuth 2.0 flow redirect.

JSON representation  
---  
      
    
    {
      "code": string,
      "ticket": string
    }  
  
Fields  
---  
`code` |  `string` Required. The code to be used for getting the token from SCM provider.  
`ticket` |  `string` Required. The ticket to be used for post processing the callback from SCM provider.  
  
## GoogleOAuthParams

The params returned by Google OAuth flow redirects.

JSON representation  
---  
      
    
    {
      "scopes": [
        string
      ],
      "versionInfo": string,
      "ticket": string
    }  
  
Fields  
---  
`scopes[]` |  `string` Required. The scopes returned by Google OAuth flow.  
`versionInfo` |  `string` Optional. The version info returned by Google OAuth flow.  
`ticket` |  `string` Required. The ticket to be used for post processing the callback from Google OAuth flow.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 
