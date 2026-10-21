---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors
title: REST Resource: projects.locations.accountConnectors \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:05.382365+00:00
---

# REST Resource: projects.locations.accountConnectors  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.accountConnectors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AccountConnector
    * JSON representation
  * ProviderOAuthConfig
    * JSON representation
  * SystemProvider
  * Methods



## Resource: AccountConnector

AccountConnector encapsulates what a platform administrator needs to configure for users to connect to the service providers, which includes, among other fields, the OAuth client ID, client secret, and authorization and token endpoints.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "annotations": {
        string: string,
        ...
      },
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "oauthStartUri": string,
    
      // Union field account_connector_config can be only one of the following:
      "providerOauthConfig": {
        object ([ProviderOAuthConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors#ProviderOAuthConfig))
      }
      // End of list of possible types for union field account_connector_config.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the accountConnector, in the format `projects/{project}/locations/{location}/accountConnectors/{accountConnectorId}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the accountConnector was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the accountConnector was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotations` |  `map (key: string, value: string)` Optional. Allows users to store small amounts of arbitrary data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`oauthStartUri` |  `string` Output only. Start OAuth flow by clicking on this URL.  
Union field `account_connector_config`. The AccountConnector config. `account_connector_config` can be only one of the following:  
`providerOauthConfig` |  `object (`[ProviderOAuthConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors#ProviderOAuthConfig)`)` Optional. Provider OAuth config.  
  
## ProviderOAuthConfig

ProviderOAuthConfig is the OAuth config for a provider.

JSON representation  
---  
      
    
    {
      "scopes": [
        string
      ],
    
      // Union field oauth_provider_id can be only one of the following:
      "systemProviderId": enum ([SystemProvider](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors#SystemProvider))
      // End of list of possible types for union field oauth_provider_id.
    }  
  
Fields  
---  
`scopes[]` |  `string` Required. User selected scopes to apply to the Oauth config In the event of changing scopes, user records under AccountConnector will be deleted and users will re-auth again.  
Union field `oauth_provider_id`. OAuth Provider ID. It could be Developer Connect owned or providers provided. `oauth_provider_id` can be only one of the following:  
`systemProviderId` |  `enum (`[SystemProvider](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors#SystemProvider)`)` Optional. Immutable. Developer Connect provided OAuth.  
  
## SystemProvider

SystemProvider is a list of providers that are owned by Developer Connect.

Enums  
---  
`SYSTEM_PROVIDER_UNSPECIFIED` | No system provider specified.  
`GITHUB` | GitHub provider. Scopes can be found at <https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes>  
`GITLAB` | GitLab provider. Scopes can be found at <https://docs.gitlab.com/user/profile/personal_access_tokens/#personal-access-token-scopes>  
`GOOGLE` | Google provider. Recommended scopes: "https://www.googleapis.com/auth/drive.readonly", "https://www.googleapis.com/auth/documents.readonly"  
`SENTRY` | Sentry provider. Scopes can be found at <https://docs.sentry.io/api/permissions/>  
`ROVO` | Rovo provider. Must select the "rovo" scope.  
`NEW_RELIC` | New Relic provider. No scopes are allowed.  
`DATASTAX` | Datastax provider. No scopes are allowed.  
`DYNATRACE` | Dynatrace provider.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/create)`

|  Creates a new AccountConnector in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/delete)`

|  Deletes a single AccountConnector.  
  
### `[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/get)`

|  Gets details of a single AccountConnector.  
  
### `[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/list)`

|  Lists AccountConnectors in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/patch)`

|  Updates the parameters of a single AccountConnector.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-06 UTC."],[],[]] 
