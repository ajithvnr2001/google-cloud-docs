---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections
title: REST Resource: projects.locations.connections \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:26.401139+00:00
---

# REST Resource: projects.locations.connections  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  REST Resource: projects.locations.connections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Connection
    * JSON representation
  * GitHubConfig
    * JSON representation
  * OAuthCredential
    * JSON representation
  * GitHubEnterpriseConfig
    * JSON representation
  * ServiceDirectoryConfig
    * JSON representation
  * GitLabConfig
    * JSON representation
  * UserCredential
    * JSON representation
  * BitbucketDataCenterConfig
    * JSON representation
  * BitbucketCloudConfig
    * JSON representation
  * InstallationState
    * JSON representation
  * Stage
  * Methods



## Resource: Connection

A connection to a SCM like GitHub, GitHub Enterprise, Bitbucket Data Center, Bitbucket Cloud or GitLab.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "installationState": {
        object ([InstallationState](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#InstallationState))
      },
      "disabled": boolean,
      "reconciling": boolean,
      "annotations": {
        string: string,
        ...
      },
      "etag": string,
    
      // Union field connection_config can be only one of the following:
      "githubConfig": {
        object ([GitHubConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#GitHubConfig))
      },
      "githubEnterpriseConfig": {
        object ([GitHubEnterpriseConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#GitHubEnterpriseConfig))
      },
      "gitlabConfig": {
        object ([GitLabConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#GitLabConfig))
      },
      "bitbucketDataCenterConfig": {
        object ([BitbucketDataCenterConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#BitbucketDataCenterConfig))
      },
      "bitbucketCloudConfig": {
        object ([BitbucketCloudConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#BitbucketCloudConfig))
      }
      // End of list of possible types for union field connection_config.
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connectionId}`.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Server assigned timestamp for when the connection was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Server assigned timestamp for when the connection was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`installationState` |  `object (`[InstallationState](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#InstallationState)`)` Output only. Installation state of the Connection.  
`disabled` |  `boolean` Optional. If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.  
`reconciling` |  `boolean` Output only. Set to true when the connection is being set up or updated in the background.  
`annotations` |  `map (key: string, value: string)` Optional. Allows clients to store small amounts of arbitrary data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
Union field `connection_config`. Configuration for the connection depending on the type of provider. `connection_config` can be only one of the following:  
`githubConfig` |  `object (`[GitHubConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#GitHubConfig)`)` Configuration for connections to github.com.  
`githubEnterpriseConfig` |  `object (`[GitHubEnterpriseConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#GitHubEnterpriseConfig)`)` Configuration for connections to an instance of GitHub Enterprise.  
`gitlabConfig` |  `object (`[GitLabConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#GitLabConfig)`)` Configuration for connections to gitlab.com or an instance of GitLab Enterprise.  
`bitbucketDataCenterConfig` |  `object (`[BitbucketDataCenterConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#BitbucketDataCenterConfig)`)` Configuration for connections to Bitbucket Data Center.  
`bitbucketCloudConfig` |  `object (`[BitbucketCloudConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#BitbucketCloudConfig)`)` Configuration for connections to Bitbucket Cloud.  
  
## GitHubConfig

Configuration for connections to github.com.

JSON representation  
---  
      
    
    {
      "authorizerCredential": {
        object ([OAuthCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#OAuthCredential))
      },
      "appInstallationId": string
    }  
  
Fields  
---  
`authorizerCredential` |  `object (`[OAuthCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#OAuthCredential)`)` Optional. OAuth credential of the account that authorized the Cloud Build GitHub App. It is recommended to use a robot account instead of a human user account. The OAuth token must be tied to the Cloud Build GitHub App.  
`appInstallationId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. GitHub App installation id.  
  
## OAuthCredential

Represents an OAuth token of the account that authorized the Connection, and associated metadata.

JSON representation  
---  
      
    
    {
      "oauthTokenSecretVersion": string,
      "username": string
    }  
  
Fields  
---  
`oauthTokenSecretVersion` |  `string` Optional. A SecretManager resource containing the OAuth token that authorizes the Cloud Build connection. Format: `projects/*/secrets/*/versions/*`.  
`username` |  `string` Output only. The username associated to this token.  
  
## GitHubEnterpriseConfig

Configuration for connections to an instance of GitHub Enterprise.

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "apiKey": string,
      "appId": string,
      "appSlug": string,
      "privateKeySecretVersion": string,
      "webhookSecretSecretVersion": string,
      "appInstallationId": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#ServiceDirectoryConfig))
      },
      "sslCa": string,
      "serverVersion": string
    }  
  
Fields  
---  
`hostUri` |  `string` Required. The URI of the GitHub Enterprise host this connection is for.  
`apiKey` |  `string` Required. API Key used for authentication of webhook events.  
`appId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Id of the GitHub App created from the manifest.  
`appSlug` |  `string` Optional. The URL-friendly name of the GitHub App.  
`privateKeySecretVersion` |  `string` Optional. SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*`.  
`webhookSecretSecretVersion` |  `string` Optional. SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*`.  
`appInstallationId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. ID of the installation of the GitHub App.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#ServiceDirectoryConfig)`)` Optional. Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet.  
`sslCa` |  `string` Optional. SSL certificate to use for requests to GitHub Enterprise.  
`serverVersion` |  `string` Output only. GitHub Enterprise version installed at the hostUri.  
  
## ServiceDirectoryConfig

ServiceDirectoryConfig represents Service Directory configuration for a connection.

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The Service Directory service name. Format: projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}.  
  
## GitLabConfig

Configuration for connections to gitlab.com or an instance of GitLab Enterprise.

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "webhookSecretSecretVersion": string,
      "readAuthorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential))
      },
      "authorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#ServiceDirectoryConfig))
      },
      "sslCa": string,
      "serverVersion": string
    }  
  
Fields  
---  
`hostUri` |  `string` Optional. The URI of the GitLab Enterprise host this connection is for. If not specified, the default value is <https://gitlab.com>.  
`webhookSecretSecretVersion` |  `string` Required. Immutable. SecretManager resource containing the webhook secret of a GitLab Enterprise project, formatted as `projects/*/secrets/*/versions/*`.  
`readAuthorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential)`)` Required. A GitLab personal access token with the minimum `read_api` scope access.  
`authorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential)`)` Required. A GitLab personal access token with the `api` scope access.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#ServiceDirectoryConfig)`)` Optional. Configuration for using Service Directory to privately connect to a GitLab Enterprise server. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet.  
`sslCa` |  `string` Optional. SSL certificate to use for requests to GitLab Enterprise.  
`serverVersion` |  `string` Output only. Version of the GitLab Enterprise server running on the `hostUri`.  
  
## UserCredential

Represents a personal access token that authorized the Connection, and associated metadata.

JSON representation  
---  
      
    
    {
      "userTokenSecretVersion": string,
      "username": string
    }  
  
Fields  
---  
`userTokenSecretVersion` |  `string` Required. A SecretManager resource containing the user token that authorizes the Cloud Build connection. Format: `projects/*/secrets/*/versions/*`.  
`username` |  `string` Output only. The username associated to this token.  
  
## BitbucketDataCenterConfig

Configuration for connections to Bitbucket Data Center.

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "webhookSecretSecretVersion": string,
      "readAuthorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential))
      },
      "authorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#ServiceDirectoryConfig))
      },
      "sslCa": string,
      "serverVersion": string
    }  
  
Fields  
---  
`hostUri` |  `string` Required. The URI of the Bitbucket Data Center instance or cluster this connection is for.  
`webhookSecretSecretVersion` |  `string` Required. Immutable. SecretManager resource containing the webhook secret used to verify webhook events, formatted as `projects/*/secrets/*/versions/*`.  
`readAuthorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential)`)` Required. A http access token with the `REPO_READ` access.  
`authorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential)`)` Required. A http access token with the `REPO_ADMIN` scope access.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#ServiceDirectoryConfig)`)` Optional. Configuration for using Service Directory to privately connect to a Bitbucket Data Center. This should only be set if the Bitbucket Data Center is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the Bitbucket Data Center will be made over the public internet.  
`sslCa` |  `string` Optional. SSL certificate to use for requests to the Bitbucket Data Center.  
`serverVersion` |  `string` Output only. Version of the Bitbucket Data Center running on the `hostUri`.  
  
## BitbucketCloudConfig

Configuration for connections to Bitbucket Cloud.

JSON representation  
---  
      
    
    {
      "workspace": string,
      "webhookSecretSecretVersion": string,
      "readAuthorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential))
      },
      "authorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential))
      }
    }  
  
Fields  
---  
`workspace` |  `string` Required. The Bitbucket Cloud Workspace ID to be connected to Google Cloud Platform.  
`webhookSecretSecretVersion` |  `string` Required. SecretManager resource containing the webhook secret used to verify webhook events, formatted as `projects/*/secrets/*/versions/*`.  
`readAuthorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential)`)` Required. An access token with the `repository` access. It can be either a workspace, project or repository access token. It's recommended to use a system account to generate the credentials.  
`authorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#UserCredential)`)` Required. An access token with the `webhook`, `repository`, `repository:admin` and `pullrequest` scope access. It can be either a workspace, project or repository access token. It's recommended to use a system account to generate these credentials.  
  
## InstallationState

Describes stage and necessary actions to be taken by the user to complete the installation. Used for GitHub and GitHub Enterprise based connections.

JSON representation  
---  
      
    
    {
      "stage": enum ([Stage](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#Stage)),
      "message": string,
      "actionUri": string
    }  
  
Fields  
---  
`stage` |  `enum (`[Stage](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections#Stage)`)` Output only. Current step of the installation process.  
`message` |  `string` Output only. Message of what the user should do next to continue the installation. Empty string if the installation is already complete.  
`actionUri` |  `string` Output only. Link to follow for next action. Empty string if the installation is already complete.  
  
## Stage

Stage of the installation process.

Enums  
---  
`STAGE_UNSPECIFIED` | No stage specified.  
`PENDING_CREATE_APP` | Only for GitHub Enterprise. An App creation has been requested. The user needs to confirm the creation in their GitHub enterprise host.  
`PENDING_USER_OAUTH` | User needs to authorize the GitHub (or Enterprise) App via OAuth.  
`PENDING_INSTALL_APP` | User needs to follow the link to install the GitHub (or Enterprise) App.  
`COMPLETE` | Installation process has been completed.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/create)`

|  Creates a Connection.  
  
### `[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/delete)`

|  Deletes a single connection.  
  
### `[fetchLinkableRepositories](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/fetchLinkableRepositories)`

|  FetchLinkableRepositories get repositories from SCM that are accessible and could be added to the connection.  
  
### `[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/get)`

|  Gets details of a single connection.  
  
### `[getIamPolicy](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/list)`

|  Lists Connections in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/patch)`

|  Updates a single connection.  
  
### `[processWebhook](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/processWebhook)`

|  ProcessWebhook is called by the external SCM for notifying of events.  
  
### `[setIamPolicy](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
