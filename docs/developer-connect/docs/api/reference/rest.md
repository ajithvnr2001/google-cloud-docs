---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/
title: Developer Connect API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:12:28.545678+00:00
---

# Developer Connect API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Developer Connect API Stay organized with collections  Save and categorize content based on your preferences. 

Connect third-party source code management to Google

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.accountConnectors
  * REST Resource: v1.projects.locations.accountConnectors.users
  * REST Resource: v1.projects.locations.connections
  * REST Resource: v1.projects.locations.connections.gitRepositoryLinks
  * REST Resource: v1.projects.locations.insightsConfigs
  * REST Resource: v1.projects.locations.insightsConfigs.deploymentEvents
  * REST Resource: v1.projects.locations.operations



## Service: developerconnect.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://developerconnect.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://developerconnect.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.accountConnectors](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors)

Methods  
---  
`[create](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/create)` |  `POST /v1/{parent=projects/*/locations/*}/accountConnectors`   
Creates a new AccountConnector in a given project and location.  
`[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/delete)` |  `DELETE /v1/{name=projects/*/locations/*/accountConnectors/*}`   
Deletes a single AccountConnector.  
`[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/get)` |  `GET /v1/{name=projects/*/locations/*/accountConnectors/*}`   
Gets details of a single AccountConnector.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/list)` |  `GET /v1/{parent=projects/*/locations/*}/accountConnectors`   
Lists AccountConnectors in a given project and location.  
`[patch](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/patch)` |  `PATCH /v1/{accountConnector.name=projects/*/locations/*/accountConnectors/*}`   
Updates the parameters of a single AccountConnector.  
  
## REST Resource: [v1.projects.locations.accountConnectors.users](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users)

Methods  
---  
`[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/delete)` |  `DELETE /v1/{name=projects/*/locations/*/accountConnectors/*/users/*}`   
Deletes a single User.  
`[deleteSelf](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/deleteSelf)` |  `DELETE /v1/{name=projects/*/locations/*/accountConnectors/*}/users:deleteSelf`   
Delete the User based on the user credentials.  
`[fetchAccessToken](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/fetchAccessToken)` |  `POST /v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:fetchAccessToken`   
Fetches OAuth access token based on end user credentials.  
`[fetchSelf](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/fetchSelf)` |  `GET /v1/{name=projects/*/locations/*/accountConnectors/*}/users:fetchSelf`   
Fetch the User based on the user credentials.  
`[finishOAuthFlow](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/finishOAuthFlow)` |  `GET /v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:finishOAuthFlow`   
Finishes OAuth flow for an account connector.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/list)` |  `GET /v1/{parent=projects/*/locations/*/accountConnectors/*}/users`   
Lists Users in a given project, location, and account_connector.  
`[startOAuthFlow](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/startOAuthFlow)` |  `GET /v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:startOAuthFlow`   
Starts OAuth flow for an account connector.  
  
## REST Resource: [v1.projects.locations.connections](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections)

Methods  
---  
`[create](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/create)` |  `POST /v1/{parent=projects/*/locations/*}/connections`   
Creates a new Connection in a given project and location.  
`[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/delete)` |  `DELETE /v1/{name=projects/*/locations/*/connections/*}`   
Deletes a single Connection.  
`[fetchGitHubInstallations](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchGitHubInstallations)` |  `GET /v1/{connection=projects/*/locations/*/connections/*}:fetchGitHubInstallations`   
FetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection.  
`[fetchLinkableGitRepositories](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchLinkableGitRepositories)` |  `GET /v1/{connection=projects/*/locations/*/connections/*}:fetchLinkableGitRepositories`   
FetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection.  
`[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/get)` |  `GET /v1/{name=projects/*/locations/*/connections/*}`   
Gets details of a single Connection.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/list)` |  `GET /v1/{parent=projects/*/locations/*}/connections`   
Lists Connections in a given project and location.  
`[patch](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/patch)` |  `PATCH /v1/{connection.name=projects/*/locations/*/connections/*}`   
Updates the parameters of a single Connection.  
`[processGitHubEnterpriseWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/processGitHubEnterpriseWebhook)` |  `POST /v1/{parent=projects/*/locations/*}/connections:processGitHubEnterpriseWebhook`   
ProcessGitHubEnterpriseWebhook is called by the external GitHub Enterprise instances for notifying events.  
  
## REST Resource: [v1.projects.locations.connections.gitRepositoryLinks](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks)

Methods  
---  
`[create](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/create)` |  `POST /v1/{parent=projects/*/locations/*/connections/*}/gitRepositoryLinks`   
Creates a GitRepositoryLink.  
`[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/delete)` |  `DELETE /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}`   
Deletes a single GitRepositoryLink.  
`[fetchGitRefs](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchGitRefs)` |  `GET /v1/{gitRepositoryLink=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchGitRefs`   
Fetch the list of branches or tags for a given repository.  
`[fetchReadToken](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchReadToken)` |  `POST /v1/{gitRepositoryLink=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchReadToken`   
Fetches read token of a given gitRepositoryLink.  
`[fetchReadWriteToken](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchReadWriteToken)` |  `POST /v1/{gitRepositoryLink=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchReadWriteToken`   
Fetches read/write token of a given gitRepositoryLink.  
`[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/get)` |  `GET /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}`   
Gets details of a single GitRepositoryLink.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/list)` |  `GET /v1/{parent=projects/*/locations/*/connections/*}/gitRepositoryLinks`   
Lists GitRepositoryLinks in a given project, location, and connection.  
`[processBitbucketCloudWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketCloudWebhook)` |  `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processBitbucketCloudWebhook`   
ProcessBitbucketCloudWebhook is called by the external Bitbucket Cloud instances for notifying events.  
`[processBitbucketDataCenterWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketDataCenterWebhook)` |  `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processBitbucketDataCenterWebhook`   
ProcessBitbucketDataCenterWebhook is called by the external Bitbucket Data Center instances for notifying events.  
`[processGitLabEnterpriseWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processGitLabEnterpriseWebhook)` |  `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processGitLabEnterpriseWebhook`   
ProcessGitLabEnterpriseWebhook is called by the external GitLab Enterprise instances for notifying events.  
`[processGitLabWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processGitLabWebhook)` |  `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processGitLabWebhook`   
ProcessGitLabWebhook is called by the GitLab.com for notifying events.  
  
## REST Resource: [v1.projects.locations.insightsConfigs](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*}/insightsConfigs`   
Creates a new InsightsConfig in a given project and location.  
`[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/insightsConfigs/*}`   
Deletes a single Insight.  
`[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/insightsConfigs/*}`   
Gets details of a single Insight.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*}/insightsConfigs`   
Lists InsightsConfigs in a given project and location.  
`[patch](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/patch)` |  `PATCH /v1/{insightsConfig.name=projects/*/locations/*/insightsConfigs/*}`   
Updates the parameters of a single InsightsConfig.  
  
## REST Resource: [v1.projects.locations.insightsConfigs.deploymentEvents](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents)

Methods  
---  
`[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/get)` |  `GET /v1/{name=projects/*/locations/*/insightsConfigs/*/deploymentEvents/*}`   
Gets a single Deployment Event.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/list)` |  `GET /v1/{parent=projects/*/locations/*/insightsConfigs/*}/deploymentEvents`   
Lists Deployment Events in a given insights config.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 
