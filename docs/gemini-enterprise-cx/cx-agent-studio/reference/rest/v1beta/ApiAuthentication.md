---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication/
title: ApiAuthentication \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:47.526051+00:00
---

# ApiAuthentication  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  ApiAuthentication Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ApiKeyConfig
    * JSON representation
  * ApiKeyConfig.RequestLocation
  * OAuthConfig
    * JSON representation
  * OAuthConfig.OauthGrantType
  * ServiceAgentIdTokenAuthConfig
  * ServiceAccountAuthConfig
    * JSON representation
  * BearerTokenConfig
    * JSON representation



Authentication information required for API calls.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ApiKeyConfig))
      },
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#OAuthConfig))
      },
      "serviceAgentIdTokenAuthConfig": {
        object ([ServiceAgentIdTokenAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ServiceAgentIdTokenAuthConfig))
      },
      "serviceAccountAuthConfig": {
        object ([ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ServiceAccountAuthConfig))
      },
      "bearerTokenConfig": {
        object ([BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#BearerTokenConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The auth configuration. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`apiKeyConfig` |  `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ApiKeyConfig)`)` Optional. Config for API key auth.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#OAuthConfig)`)` Optional. Config for OAuth.  
`serviceAgentIdTokenAuthConfig` |  `object (`[ServiceAgentIdTokenAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ServiceAgentIdTokenAuthConfig)`)` Optional. Config for ID token auth generated from CES service agent.  
`serviceAccountAuthConfig` |  `object (`[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ServiceAccountAuthConfig)`)` Optional. Config for service account authentication.  
`bearerTokenConfig` |  `object (`[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#BearerTokenConfig)`)` Optional. Config for bearer token auth.  
End of mutually exclusive fields.  
  
## ApiKeyConfig

Configurations for authentication with API key.

JSON representation  
---  
      
    
    {
      "keyName": string,
      "apiKeySecretVersion": string,
      "requestLocation": enum ([ApiKeyConfig.RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ApiKeyConfig.RequestLocation))
    }  
  
Fields  
---  
`keyName` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`apiKeySecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the API key. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`requestLocation` |  `enum (`[ApiKeyConfig.RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#ApiKeyConfig.RequestLocation)`)` Required. Key location in the request.  
  
## ApiKeyConfig.RequestLocation

The location of the API key in the request.

Enums  
---  
`REQUEST_LOCATION_UNSPECIFIED` | Unspecified. This value should not be used.  
`HEADER` | Represents the key in http header.  
`QUERY_STRING` | Represents the key in query string.  
  
## OAuthConfig

Configurations for authentication with OAuth.

JSON representation  
---  
      
    
    {
      "oauthGrantType": enum ([OAuthConfig.OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#OAuthConfig.OauthGrantType)),
      "clientId": string,
      "clientSecretVersion": string,
      "tokenEndpoint": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`oauthGrantType` |  `enum (`[OAuthConfig.OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication#OAuthConfig.OauthGrantType)`)` Required. OAuth grant types.  
`clientId` |  `string` Required. The client ID from the OAuth provider.  
`clientSecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the client secret. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`tokenEndpoint` |  `string` Required. The token endpoint in the OAuth provider to exchange for an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
## OAuthConfig.OauthGrantType

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

Enums  
---  
`OAUTH_GRANT_TYPE_UNSPECIFIED` | Unspecified. Defaults to CLIENT_CREDENTIAL.  
`CLIENT_CREDENTIAL` | Represents the [client credential flow](https://oauth.net/2/grant-types/client-credentials).  
  
## ServiceAgentIdTokenAuthConfig

This type has no fields.

Configurations for authentication with [ID token](https://cloud.google.com/docs/authentication/token-types#id) generated from service agent.

## ServiceAccountAuthConfig

Configurations for authentication using a custom service account.

JSON representation  
---  
      
    
    {
      "serviceAccount": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`serviceAccount` |  `string` Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant. If not specified, the default scope `https://www.googleapis.com/auth/cloud-platform` is used.  
  
## BearerTokenConfig

Configurations for authentication with a bearer token.

JSON representation  
---  
      
    
    {
      "token": string
    }  
  
Fields  
---  
`token` |  `string` Required. The bearer token. Must be in the format `$context.variables.<name_of_variable>`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
