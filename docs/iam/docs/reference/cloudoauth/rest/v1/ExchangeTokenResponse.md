---
url: https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest/v1/ExchangeTokenResponse/
title: ExchangeTokenResponse \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:10.401857+00:00
---

# ExchangeTokenResponse  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest/v1/ExchangeTokenResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  ExchangeTokenResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for `[common.token](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest/v1/common/token#google.cloud.identity.oauth.v1.CloudOAuthService.ExchangeToken)`. see [Response](https://www.rfc-editor.org/rfc/rfc6749#section-5.1)

JSON representation  
---  
      
    
    {
      "access_token": string,
      "refresh_token": string,
      "expires_in": integer,
      "token_type": string,
      "scope": string,
      "id_token": string
    }  
  
Fields  
---  
`access_token` |  `string` An OAuth 2.0 security token, issued by Google, in response to the OAuth token exchange request for the authorization code and refresh token flows.The returned [access token](https://www.rfc-editor.org/rfc/rfc6749#section-4.1.4). Tokens can vary in size, depending, in part, on the size of mapped claims, up to a maximum of 12288 bytes (12 KB). Google reserves the right to change the token size and the maximum length at any time.  
`refresh_token` |  `string` A refresh token, issued by Google, in response to the OAuth token exchange request for the refresh token flow.  
`expires_in` |  `integer` The amount of time, in seconds, between the time when the access token was issued and the time when the access token will expire.  
`token_type` |  `string` The type of token. Field reserved for RFC compliance. See [Token Type](https://www.rfc-editor.org/rfc/rfc6749#section-5.1)  
`scope` |  `string` A list of scopes associated with the returned token.  
`id_token` |  `string` Google issued ID token in response to the OAuth token exchange request for ID token flow.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-16 UTC."],[],[]] 
