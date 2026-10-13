---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs
title: REST Resource: projects.locations.products.authConfigs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:42.578062+00:00
---

# REST Resource: projects.locations.products.authConfigs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  REST Resource: projects.locations.products.authConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AuthConfig
    * JSON representation
  * Methods



## Resource: AuthConfig

The AuthConfig resource use to hold channels and connection config data.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "certificateId": string,
      "credentialType": enum ([CredentialType](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.CredentialType)),
      "creatorEmail": string,
      "createTime": string,
      "lastModifierEmail": string,
      "updateTime": string,
      "visibility": enum ([AuthConfigVisibility](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.AuthConfigVisibility)),
      "state": enum ([State](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.State)),
      "reason": string,
      "expiryNotificationDuration": [
        string
      ],
      "validTime": string,
      "overrideValidTime": string,
    
      // Union field credential can be only one of the following:
      "encryptedCredential": string,
      "decryptedCredential": {
        object ([Credential](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.Credential))
      }
      // End of list of possible types for union field credential.
    }  
  
Fields  
---  
`name` |  `string` Resource name of the SFDC instance projects/{project}/locations/{location}/authConfigs/{authConfig}.  
`displayName` |  `string` The name of the auth config.  
`description` |  `string` A description of the auth config.  
`certificateId` |  `string` Certificate id for client certificate  
`credentialType` |  `enum (`[CredentialType](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.CredentialType)`)` Credential type of the encrypted credential.  
`creatorEmail` |  `string` The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the auth config is created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`lastModifierEmail` |  `string` The last modifier's email address. Generated based on the End User Credentials/LOAS role of the user making the call.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the auth config is modified.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`visibility` |  `enum (`[AuthConfigVisibility](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.AuthConfigVisibility)`)` The visibility of the auth config.  
`state` |  `enum (`[State](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.State)`)` The status of the auth config.  
`reason` |  `string` The reason / details of the current status.  
`expiryNotificationDuration[]` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` User can define the time to receive notification after which the auth config becomes invalid. Support up to 30 days. Support granularity in hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`validTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time until the auth config is valid. Empty or max value is considered the auth config won't expire.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`overrideValidTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` User provided expiry time to override. For the example of Salesforce, username/password credentials can be valid for 6 months depending on the instance settings.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
Union field `credential`.`credential` can be only one of the following:  
`encryptedCredential` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Auth credential encrypted by Cloud KMS. Can be decrypted as Credential with proper KMS key.A base64-encoded string.  
`decryptedCredential` |  `object (`[Credential](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs#AuthConfig.Credential)`)` Raw auth credentials.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs/create)`

|  Creates an auth config record.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs/delete)`

|  Deletes an auth config.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs/get)`

|  Gets a complete auth config.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs/list)`

|  Lists all auth configs that match the filter.  
  
### `[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.authConfigs/patch)`

|  Updates an auth config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
