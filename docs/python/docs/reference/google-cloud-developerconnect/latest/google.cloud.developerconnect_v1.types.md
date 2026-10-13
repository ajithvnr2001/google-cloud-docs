---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types
title: Package types (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:28.456377+00:00
---

# Package types (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 

API documentation for `developerconnect_v1.types` package.

## Classes 

### [AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector)

AccountConnector encapsulates what a platform administrator needs to configure for users to connect to the service providers, which includes, among other fields, the OAuth client ID, client secret, and authorization and token endpoints.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AppHubService](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AppHubService)

AppHubService represents the App Hub Service.

### [AppHubWorkload](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AppHubWorkload)

AppHubWorkload represents the App Hub Workload.

### [ArtifactConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ArtifactConfig)

The artifact config of the artifact that is deployed.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ArtifactDeployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ArtifactDeployment)

The ArtifactDeployment resource represents the deployment of the artifact within the InsightsConfig resource.

### [BitbucketCloudConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.BitbucketCloudConfig)

Configuration for connections to an instance of Bitbucket Cloud.

### [BitbucketDataCenterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.BitbucketDataCenterConfig)

Configuration for connections to an instance of Bitbucket Data Center.

### [Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection)

Message describing Connection object

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateAccountConnectorRequest)

### [CreateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateConnectionRequest)

Message for creating a Connection

### [CreateGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateGitRepositoryLinkRequest)

Message for creating a GitRepositoryLink

### [CreateInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateInsightsConfigRequest)

Request for creating an InsightsConfig.

### [CryptoKeyConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CryptoKeyConfig)

The crypto key configuration. This field is used by the Customer-managed encryption keys (CMEK) feature.

### [DeleteAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteAccountConnectorRequest)

Message for deleting a AccountConnector

### [DeleteConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteConnectionRequest)

Message for deleting a Connection

### [DeleteGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteGitRepositoryLinkRequest)

Message for deleting a GitRepositoryLink

### [DeleteInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteInsightsConfigRequest)

Request for deleting an InsightsConfig.

### [DeleteSelfRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteSelfRequest)

Message for deleting a User of the user themselves.

### [DeleteUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteUserRequest)

Message for deleting a User

### [DeploymentEvent](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeploymentEvent)

The DeploymentEvent resource represents the deployment of the artifact within the InsightsConfig resource.

### [ExchangeError](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ExchangeError)

Message for representing an error from exchanging OAuth tokens.

### [FetchAccessTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchAccessTokenRequest)

Message for fetching an OAuth access token.

### [FetchAccessTokenResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchAccessTokenResponse)

Message for responding to getting an OAuth access token.

### [FetchGitHubInstallationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitHubInstallationsRequest)

Request for fetching github installations.

### [FetchGitHubInstallationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitHubInstallationsResponse)

Response of fetching github installations.

### [FetchGitRefsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsRequest)

Request for fetching git refs.

### [FetchGitRefsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsResponse)

Response for fetching git refs.

### [FetchLinkableGitRepositoriesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesRequest)

Request message for FetchLinkableGitRepositoriesRequest.

### [FetchLinkableGitRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse)

Response message for FetchLinkableGitRepositories.

### [FetchReadTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadTokenRequest)

Message for fetching SCM read token.

### [FetchReadTokenResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadTokenResponse)

Message for responding to get read token.

### [FetchReadWriteTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadWriteTokenRequest)

Message for fetching SCM read/write token.

### [FetchReadWriteTokenResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadWriteTokenResponse)

Message for responding to get read/write token.

### [FetchSelfRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchSelfRequest)

Message for fetching a User of the user themselves.

### [FinishOAuthRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FinishOAuthRequest)

Message for finishing an OAuth flow.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FinishOAuthResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FinishOAuthResponse)

Message for responding to finishing an OAuth flow.

### [GKEWorkload](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GKEWorkload)

GKEWorkload represents the Google Kubernetes Engine runtime.

### [GenericHTTPEndpointConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig)

Defines the configuration for connections to an HTTP service provider.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetAccountConnectorRequest)

Message for getting a AccountConnector

### [GetConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetConnectionRequest)

Message for getting a Connection

### [GetDeploymentEventRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetDeploymentEventRequest)

Request for getting a DeploymentEvent.

### [GetGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetGitRepositoryLinkRequest)

Message for getting a GitRepositoryLink

### [GetInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetInsightsConfigRequest)

Request for getting an InsightsConfig.

### [GitHubConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitHubConfig)

Configuration for connections to github.com.

### [GitHubEnterpriseConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitHubEnterpriseConfig)

Configuration for connections to an instance of GitHub Enterprise.

### [GitLabConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitLabConfig)

Configuration for connections to gitlab.com.

### [GitLabEnterpriseConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitLabEnterpriseConfig)

Configuration for connections to an instance of GitLab Enterprise.

### [GitProxyConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitProxyConfig)

The git proxy configuration.

### [GitRepositoryLink](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitRepositoryLink)

Message describing the GitRepositoryLink object

### [GoogleArtifactAnalysis](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GoogleArtifactAnalysis)

Google Artifact Analysis configurations.

### [GoogleArtifactRegistry](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GoogleArtifactRegistry)

Google Artifact Registry configurations.

### [GoogleCloudRun](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GoogleCloudRun)

GoogleCloudRun represents the Cloud Run runtime.

### [InsightsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig)

The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstallationState](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InstallationState)

Describes stage and necessary actions to be taken by the user to complete the installation. Used for GitHub and GitHub Enterprise based connections.

### [LinkableGitRepository](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.LinkableGitRepository)

LinkableGitRepository represents a git repository that can be linked to a connection.

### [ListAccountConnectorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsRequest)

Message for requesting list of AccountConnectors

### [ListAccountConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse)

Message for response to listing AccountConnectors

### [ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsRequest)

Message for requesting list of Connections

### [ListConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsResponse)

Message for response to listing Connections

### [ListDeploymentEventsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListDeploymentEventsRequest)

Request for requesting list of DeploymentEvents.

### [ListDeploymentEventsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListDeploymentEventsResponse)

Response to listing DeploymentEvents.

### [ListGitRepositoryLinksRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksRequest)

Message for requesting a list of GitRepositoryLinks

### [ListGitRepositoryLinksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse)

Message for response to listing GitRepositoryLinks

### [ListInsightsConfigsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListInsightsConfigsRequest)

Request for requesting list of InsightsConfigs.

### [ListInsightsConfigsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListInsightsConfigsResponse)

Request for response to listing InsightsConfigs.

### [ListUsersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersRequest)

Message for requesting a list of Users

### [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersResponse)

Message for response to listing Users

### [OAuthCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.OAuthCredential)

Represents an OAuth token of the account that authorized the Connection, and associated metadata.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [Projects](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Projects)

Projects represents the projects to track with the InsightsConfig.

### [ProviderOAuthConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ProviderOAuthConfig)

ProviderOAuthConfig is the OAuth config for a provider.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RuntimeConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.RuntimeConfig)

RuntimeConfig represents the runtimes where the application is deployed.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SecureSourceManagerInstanceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.SecureSourceManagerInstanceConfig)

Configuration for connections to Secure Source Manager instance

### [ServiceDirectoryConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ServiceDirectoryConfig)

ServiceDirectoryConfig represents Service Directory configuration for a connection.

### [StartOAuthRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.StartOAuthRequest)

Message for starting an OAuth flow.

### [StartOAuthResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.StartOAuthResponse)

Message for responding to starting an OAuth flow.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SystemProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.SystemProvider)

SystemProvider is a list of providers that are owned by Developer Connect.
    
    
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/documents.readonly".
    SENTRY (4):
        Sentry provider.
        Scopes can be found at
        https://docs.sentry.io/api/permissions/
    ROVO (5):
        Rovo provider.
        Must select the "rovo" scope.
    NEW_RELIC (6):
        New Relic provider.
        No scopes are allowed.
    DATASTAX (7):
        Datastax provider.
        No scopes are allowed.
    DYNATRACE (8):
        Dynatrace provider.
    

### [UpdateAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateAccountConnectorRequest)

Message for updating a AccountConnector

### [UpdateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateConnectionRequest)

Message for updating a Connection

### [UpdateInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateInsightsConfigRequest)

Request for updating an InsightsConfig.

### [User](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.User)

User represents a user connected to the service providers through a AccountConnector.

### [UserCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UserCredential)

Represents a personal access token that authorized the Connection, and associated metadata.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
