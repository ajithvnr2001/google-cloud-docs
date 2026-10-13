---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients
title: REST Resource: projects.locations.oauthClients \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:54.022222+00:00
---

# REST Resource: projects.locations.oauthClients  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.locations.oauthClients Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: OauthClient
    * JSON representation
  * State
  * ClientType
  * GrantType
  * Methods



## Resource: OauthClient

Represents an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`. Used to access Google Cloud resources on behalf of a Workforce Identity Federation user by using OAuth 2.0 Protocol to obtain an access token from Google Cloud.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#State)),
      "disabled": boolean,
      "clientId": string,
      "displayName": string,
      "description": string,
      "clientType": enum ([ClientType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#ClientType)),
      "allowedGrantTypes": [
        enum ([GrantType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#GrantType))
      ],
      "allowedScopes": [
        string
      ],
      "allowedRedirectUris": [
        string
      ],
      "expireTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The resource name of the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.Format:`projects/{project}/locations/{location}/oauthClients/{oauthClient}`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#State)`)` Output only. The state of the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
`disabled` |  `boolean` Optional. Whether the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` is disabled. You cannot use a disabled OAuth client.  
`clientId` |  `string` Output only. The system-generated `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` id.  
`displayName` |  `string` Optional. A user-specified display name of the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.Cannot exceed 32 characters.  
`description` |  `string` Optional. A user-specified description of the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.Cannot exceed 256 characters.  
`clientType` |  `enum (`[ClientType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#ClientType)`)` Immutable. The type of `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`. Either public or private. For private clients, the client secret can be managed using the dedicated `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)` resource.  
`allowedGrantTypes[]` |  `enum (`[GrantType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#GrantType)`)` Required. The list of OAuth grant types is allowed for the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
`allowedScopes[]` |  `string` Required. The list of scopes that the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` is allowed to request during OAuth flows.The following scopes are supported:

  * `https://www.googleapis.com/auth/cloud-platform`: See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account.

  
`allowedRedirectUris[]` |  `string` Required. The list of redirect uris that is allowed to redirect back when authorization process is completed.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time after which the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` will be permanently purged and cannot be recovered.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The current state of the `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`ACTIVE` | The `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` is active.  
`DELETED` | The `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` is soft-deleted. Soft-deleted `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)` is permanently deleted after approximately 30 days unless restored via `oauthClients.undelete`.  
  
## ClientType

The type of `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.

Enums  
---  
`CLIENT_TYPE_UNSPECIFIED` | Should not be used.  
`PUBLIC_CLIENT` | Public client has no secret.  
`CONFIDENTIAL_CLIENT` | Private client.  
  
## GrantType

The OAuth grant type.

Enums  
---  
`GRANT_TYPE_UNSPECIFIED` | Should not be used.  
`AUTHORIZATION_CODE_GRANT` | Authorization code grant.  
`REFRESH_TOKEN_GRANT` | Refresh token grant.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/create)`

|  Creates a new `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/delete)`

|  Deletes an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/get)`

|  Gets an individual `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/list)`

|  Lists all non-deleted `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s in a project.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/patch)`

|  Updates an existing `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/undelete)`

|  Undeletes an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`, as long as it was deleted fewer than 30 days ago.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-24 UTC."],[],[]] 
