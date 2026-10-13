---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials
title: REST Resource: projects.locations.oauthClients.credentials \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:55.034530+00:00
---

# REST Resource: projects.locations.oauthClients.credentials  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.locations.oauthClients.credentials Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: OauthClientCredential
    * JSON representation
  * Methods



## Resource: OauthClientCredential

Represents an `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`. Used to authenticate an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` while accessing Google Cloud resources on behalf of a user by using OAuth 2.0 Protocol.

JSON representation  
---  
      
    
    {
      "name": string,
      "disabled": boolean,
      "displayName": string,
    
      // Union field credential can be only one of the following:
      "clientSecret": string
      // End of list of possible types for union field credential.
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The resource name of the `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.Format: `projects/{project}/locations/{location}/oauthClients/{oauthClient}/credentials/{credential}`  
`disabled` |  `boolean` Optional. Whether the `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)` is disabled. You cannot use a disabled `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
`displayName` |  `string` Optional. A user-specified display name of the `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.Cannot exceed 32 characters.  
Union field `credential`.`credential` can be only one of the following:  
`clientSecret` |  `string` Output only. The system-generated OAuth client secret.The client secret must be stored securely. If the client secret is leaked, you must delete and re-create the client credential. To learn more, see [OAuth client and credential security risks and mitigations](https://cloud.google.com/iam/docs/workforce-oauth-app#security)  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/create)`

|  Creates a new `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/delete)`

|  Deletes an `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/get)`

|  Gets an individual `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/list)`

|  Lists all `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`s in an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/patch)`

|  Updates an existing `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
