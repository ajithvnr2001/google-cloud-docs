---
url: https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken/
title: Method: projects.serviceAccounts.generateIdToken \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:26.573575+00:00
---

# Method: projects.serviceAccounts.generateIdToken  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.serviceAccounts.generateIdToken Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Generates an OpenID Connect ID token for a service account.

### HTTP request

`POST https://iamcredentials.googleapis.com/v1/{name=projects/*/serviceAccounts/*}:generateIdToken`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the service account for which the credentials are requested, in the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `iam.serviceAccounts.getOpenIdToken`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "delegates": [
        string
      ],
      "audience": string,
      "includeEmail": boolean,
      "organizationNumberIncluded": boolean
    }  
  
Fields  
---  
`delegates[]` |  `string` The sequence of service accounts in a delegation chain. Each service account must be granted the `roles/iam.serviceAccountTokenCreator` role on its next service account in the chain. The last service account in the chain must be granted the `roles/iam.serviceAccountTokenCreator` role on the service account that is specified in the `name` field of the request.The delegates must have the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid.  
`audience` |  `string` Required. The audience for the token, such as the API or account that this token grants access to.  
`includeEmail` |  `boolean` Include the service account email in the token. If set to `true`, the token will contain `email` and `email_verified` claims.  
`organizationNumberIncluded` |  `boolean` Include the organization number of the service account in the token. If set to `true`, the token will contain a `google.organization_number` claim. The value of the claim will be `null` if the service account isn't associated with an organization.  
  
### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "token": string
    }  
  
Fields  
---  
`token` |  `string` The OpenId Connect ID token.The token is a JSON Web Token (JWT) that contains a payload with claims. See the [JSON Web Token spec](https://tools.ietf.org/html/rfc7519) for more information. Here is an example of a decoded JWT payload:
    
    
    {
      "iss": "https://accounts.google.com",
      "iat": 1496953245,
      "exp": 1496953245,
      "aud": "https://www.example.com",
      "sub": "107517467455664443765",
      "azp": "107517467455664443765",
      "email": "my-iam-account@my-project.iam.gserviceaccount.com",
      "email_verified": true,
      "google": {
        "organization_number": 123456
      }
    }
      
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
