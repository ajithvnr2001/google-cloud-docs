---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/startOAuthFlow/
title: Method: projects.locations.accountConnectors.users.startOAuthFlow \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:07.057577+00:00
---

# Method: projects.locations.accountConnectors.users.startOAuthFlow  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/startOAuthFlow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.accountConnectors.users.startOAuthFlow Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Starts OAuth flow for an account connector.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:startOAuthFlow`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`accountConnector` |  `string` Required. The resource name of the AccountConnector in the format `projects/*/locations/*/accountConnectors/*`.  
  
### Request body

The request body must be empty.

### Response body

Message for responding to starting an OAuth flow.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ticket": string,
      "codeChallenge": string,
      "codeChallengeMethod": string,
      "clientId": string,
      "scopes": [
        string
      ],
      "authUri": string,
    
      // Union field id can be only one of the following:
      "systemProviderId": enum ([SystemProvider](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors#SystemProvider))
      // End of list of possible types for union field id.
    }  
  
Fields  
---  
`ticket` |  `string` The ticket to be used for post processing the callback from the service provider.  
`codeChallenge` |  `string` Please refer to <https://datatracker.ietf.org/doc/html/rfc7636#section-4.1>  
`codeChallengeMethod` |  `string` Please refer to <https://datatracker.ietf.org/doc/html/rfc7636#section-4.2>  
`clientId` |  `string` The client ID to the OAuth App of the service provider.  
`scopes[]` |  `string` The list of scopes requested by the application.  
`authUri` |  `string` The authorization server URL to the OAuth flow of the service provider.  
Union field `id`. The ID of the service provider. `id` can be only one of the following:  
`systemProviderId` |  `enum (`[SystemProvider](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors#SystemProvider)`)` The ID of the system provider.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `accountConnector` resource:

  * `developerconnect.users.startOAuth`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 
