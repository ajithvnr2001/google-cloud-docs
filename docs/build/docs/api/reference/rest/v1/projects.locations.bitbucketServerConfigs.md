---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs
title: REST Resource: projects.locations.bitbucketServerConfigs \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:18.370537+00:00
---

# REST Resource: projects.locations.bitbucketServerConfigs  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  REST Resource: projects.locations.bitbucketServerConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BitbucketServerConfig
    * JSON representation
    * BitbucketServerSecrets
      * JSON representation
    * BitbucketServerRepositoryId
      * JSON representation
  * Methods



## Resource: BitbucketServerConfig

BitbucketServerConfig represents the configuration for a Bitbucket Server.

JSON representation  
---  
      
    
    {
      "name": string,
      "hostUri": string,
      "secrets": {
        object ([BitbucketServerSecrets](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig.BitbucketServerSecrets))
      },
      "createTime": string,
      "username": string,
      "webhookKey": string,
      "apiKey": string,
      "connectedRepositories": [
        {
          object ([BitbucketServerRepositoryId](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig.BitbucketServerRepositoryId))
        }
      ],
      "peeredNetwork": string,
      "sslCa": string,
      "peeredNetworkIpRange": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name for the config.  
`hostUri` |  `string` Required. Immutable. The URI of the Bitbucket Server host. Once this field has been set, it cannot be changed. If you need to change it, please create another BitbucketServerConfig.  
`secrets` |  `object (`[BitbucketServerSecrets](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig.BitbucketServerSecrets)`)` Required. Secret Manager secrets needed by the config.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when the config was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`username` |  `string` Username of the account Cloud Build will use on Bitbucket Server.  
`webhookKey` |  `string` Output only. UUID included in webhook requests. The UUID is used to look up the corresponding config.  
`apiKey` |  `string` Required. Immutable. API Key that will be attached to webhook. Once this field has been set, it cannot be changed. If you need to change it, please create another BitbucketServerConfig.  
`connectedRepositories[]` |  `object (`[BitbucketServerRepositoryId](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig.BitbucketServerRepositoryId)`)` Output only. Connected Bitbucket Server repositories for this config.  
`peeredNetwork` |  `string` Optional. The network to be used when reaching out to the Bitbucket Server instance. The VPC network must be enabled for private service connection. This should be set if the Bitbucket Server instance is hosted on-premises and not reachable by public internet. If this field is left empty, no network peering will occur and calls to the Bitbucket Server instance will be made over the public internet. Must be in the format `projects/{project}/global/networks/{network}`, where {project} is a project number or id and {network} is the name of a VPC network in the project.  
`sslCa` |  `string` Optional. SSL certificate to use for requests to Bitbucket Server. The format should be PEM format but the extension can be one of .pem, .cer, or .crt.  
`peeredNetworkIpRange` |  `string` Immutable. IP range within the peered network. This is specified in CIDR notation with a slash and the subnet prefix size. You can optionally specify an IP address before the subnet prefix value. e.g. `192.168.0.0/29` would specify an IP range starting at 192.168.0.0 with a 29 bit prefix size. `/16` would specify a prefix size of 16 bits, with an automatically determined IP within the peered VPC. If unspecified, a value of `/24` will be used. The field only has an effect if peeredNetwork is set.  
  
### BitbucketServerSecrets

BitbucketServerSecrets represents the secrets in Secret Manager for a Bitbucket Server.

JSON representation  
---  
      
    
    {
      "adminAccessTokenVersionName": string,
      "readAccessTokenVersionName": string,
      "webhookSecretVersionName": string
    }  
  
Fields  
---  
`adminAccessTokenVersionName` |  `string` Required. The resource name for the admin access token's secret version.  
`readAccessTokenVersionName` |  `string` Required. The resource name for the read access token's secret version.  
`webhookSecretVersionName` |  `string` Required. Immutable. The resource name for the webhook secret's secret version. Once this field has been set, it cannot be changed. If you need to change it, please create another BitbucketServerConfig.  
  
### BitbucketServerRepositoryId

BitbucketServerRepositoryId identifies a specific repository hosted on a Bitbucket Server.

JSON representation  
---  
      
    
    {
      "projectKey": string,
      "repoSlug": string,
      "webhookId": integer
    }  
  
Fields  
---  
`projectKey` |  `string` Required. Identifier for the project storing the repository.  
`repoSlug` |  `string` Required. Identifier for the repository.  
`webhookId` |  `integer` Output only. The ID of the webhook that was created for receiving events from this repo. We only create and manage a single webhook for each repo.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/create)`

|  Creates a new `BitbucketServerConfig`.  
  
### `[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/delete)`

|  Delete a `BitbucketServerConfig`.  
  
### `[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/get)`

|  Retrieve a `BitbucketServerConfig`.  
  
### `[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/list)`

|  List all `BitbucketServerConfigs` for a given project.  
  
### `[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/patch)`

|  Updates an existing `BitbucketServerConfig`.  
  
### `[removeBitbucketServerConnectedRepository](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/removeBitbucketServerConnectedRepository)`

|  Remove a Bitbucket Server repository from a given BitbucketServerConfig's connected repositories.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-22 UTC."],[],[]] 
