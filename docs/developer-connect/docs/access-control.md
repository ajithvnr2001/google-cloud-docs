---
url: https://docs.cloud.google.com/developer-connect/docs/access-control/
title: IAM roles and permissions \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:30.560246+00:00
---

# IAM roles and permissions  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Developer Connect roles and permissions.

Access control in Developer Connect is controlled using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam). IAM lets you create and manage permissions for Google Cloud resources. Developer Connect provides a specific set of [predefined IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#role-types) where each role contains a set of permissions suited to a particular type of access or action. We recommend that you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), and grant only the necessary access to your resources.

## Predefined Developer Connect roles

You assign permissions to accounts through the use of roles. The following table lists the IAM roles available for Developer Connect and the permissions that they include:

The IAM documentation includes a [searchable reference](https://docs.cloud.google.com/iam/docs/roles-permissions) of all predefined roles.

Role | Permissions  
---|---  
  
#### Developer Connect Admin 

(`roles/developerconnect.admin`) Full access to Developer Connect resources.  |  `developerconnect.connections.constructGitHubAppManifest` `developerconnect.connections.create` `developerconnect.connections.delete` `developerconnect.connections.fetchGitHubInstallations` `developerconnect.connections.fetchLinkableGitRepositories` `developerconnect.connections.generateGitHubStateToken` `developerconnect.connections.get` `developerconnect.connections.list` `developerconnect.connections.processGitHubAppCreationCallback` `developerconnect.connections.processGitHubOAuthCallback` `developerconnect.connections.update` `developerconnect.gitRepositoryLinks.create` `developerconnect.gitRepositoryLinks.delete` `developerconnect.gitRepositoryLinks.fetchGitRefs` `developerconnect.gitRepositoryLinks.get` `developerconnect.gitRepositoryLinks.gitProxyRead` `developerconnect.gitRepositoryLinks.gitProxyWrite` `developerconnect.gitRepositoryLinks.list` `developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.*`

  * `developerconnect.operations.cancel`
  * `developerconnect.operations.delete`
  * `developerconnect.operations.get`
  * `developerconnect.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Developer Connect Viewer 

(`roles/developerconnect.viewer`) Read-only access to Developer Connect resources.  |  `developerconnect.connections.get` `developerconnect.connections.list` `developerconnect.gitRepositoryLinks.get` `developerconnect.gitRepositoryLinks.list` `developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.get` `developerconnect.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Developer Connect HTTP Proxy Writer Beta

(`roles/developerconnect.connectionHttpProxyWriter`) Grants read and write access to connections through the HTTP Proxy.  |  `developerconnect.connections.httpProxyRead` `developerconnect.connections.httpProxyWrite`  
  
#### Developer Connect Git Proxy Reader 

(`roles/developerconnect.gitProxyReader`) Grants read-only access to repositories through the Git Proxy.  |  `developerconnect.gitRepositoryLinks.gitProxyRead`  
  
#### Developer Connect Git Proxy User 

(`roles/developerconnect.gitProxyUser`) Grants read and write access to repositories through the Git Proxy.  |  `developerconnect.gitRepositoryLinks.gitProxyRead` `developerconnect.gitRepositoryLinks.gitProxyWrite`  
  
#### Developer Connect Insights Admin 

(`roles/developerconnect.insightsAdmin`) Admin access to Developer Connect Insights resources.  |  `developerconnect.deploymentEvents.*`

  * `developerconnect.deploymentEvents.get`
  * `developerconnect.deploymentEvents.list`

`developerconnect.insightsConfigs.*`

  * `developerconnect.insightsConfigs.create`
  * `developerconnect.insightsConfigs.delete`
  * `developerconnect.insightsConfigs.get`
  * `developerconnect.insightsConfigs.list`
  * `developerconnect.insightsConfigs.update`

`developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.get` `developerconnect.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Developer Connect Insights Config Agent 

(`roles/developerconnect.insightsAgent`) Allow Developer Connect to access SDLC information.  |  `cloudasset.assets.exportResource` `cloudasset.assets.listResource` `cloudasset.assets.searchAllResources` `cloudasset.feeds.create` `cloudasset.feeds.delete` `cloudasset.feeds.get` `cloudasset.feeds.update` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `logging.logEntries.create`  
  
#### Developer Connect Insights Viewer 

(`roles/developerconnect.insightsViewer`) Read-only access to Developer Connect Insights resources.  |  `developerconnect.deploymentEvents.*`

  * `developerconnect.deploymentEvents.get`
  * `developerconnect.deploymentEvents.list`

`developerconnect.insightsConfigs.get` `developerconnect.insightsConfigs.list` `developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.get` `developerconnect.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Developer Connect OAuth Admin Beta

(`roles/developerconnect.oauthAdmin`) Grants read and write access to AccountConnector resources.  |  `developerconnect.accountConnectors.*`

  * `developerconnect.accountConnectors.create`
  * `developerconnect.accountConnectors.delete`
  * `developerconnect.accountConnectors.fetchUserRepositories`
  * `developerconnect.accountConnectors.get`
  * `developerconnect.accountConnectors.gitProxyRead`
  * `developerconnect.accountConnectors.gitProxyWrite`
  * `developerconnect.accountConnectors.httpProxyRead`
  * `developerconnect.accountConnectors.httpProxyWrite`
  * `developerconnect.accountConnectors.list`
  * `developerconnect.accountConnectors.update`

`developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.get` `developerconnect.operations.list` `developerconnect.providers.list` `developerconnect.users.*`

  * `developerconnect.users.delete`
  * `developerconnect.users.deleteSelf`
  * `developerconnect.users.fetchAccessToken`
  * `developerconnect.users.finishOAuth`
  * `developerconnect.users.getSelf`
  * `developerconnect.users.list`
  * `developerconnect.users.startOAuth`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Developer Connect OAuth User Beta

(`roles/developerconnect.oauthUser`) Grants read and write access to User resources, and read access to AccountConnectors.  |  `developerconnect.accountConnectors.fetchUserRepositories` `developerconnect.accountConnectors.get` `developerconnect.accountConnectors.gitProxyRead` `developerconnect.accountConnectors.gitProxyWrite` `developerconnect.accountConnectors.httpProxyRead` `developerconnect.accountConnectors.httpProxyWrite` `developerconnect.accountConnectors.list` `developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.get` `developerconnect.operations.list` `developerconnect.users.deleteSelf` `developerconnect.users.fetchAccessToken` `developerconnect.users.finishOAuth` `developerconnect.users.getSelf` `developerconnect.users.startOAuth` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Developer Connect Read Token Accessor Beta

(`roles/developerconnect.readTokenAccessor`) Grants access to Read-Only tokens (both PAT and short-lived). Also grants access to view the git repository link.  |  `developerconnect.connections.get` `developerconnect.gitRepositoryLinks.fetchReadToken` `developerconnect.gitRepositoryLinks.get`  
  
#### Developer Connect Token Accessor Beta

(`roles/developerconnect.tokenAccessor`) Grants access to Read/Write and Read-Only tokens (both PAT and short-lived). Also grants access to view the git repository link.  |  `developerconnect.connections.get` `developerconnect.gitRepositoryLinks.fetchReadToken` `developerconnect.gitRepositoryLinks.fetchReadWriteToken` `developerconnect.gitRepositoryLinks.get`  
  
#### Developer Connect User 

(`roles/developerconnect.user`) Grants access to view the connection and to the features that interact with the actual repository such as reading content from the repository  |  `developerconnect.connections.fetchGitHubInstallations` `developerconnect.connections.fetchLinkableGitRepositories` `developerconnect.connections.get` `developerconnect.connections.list` `developerconnect.gitRepositoryLinks.fetchGitRefs` `developerconnect.gitRepositoryLinks.get` `developerconnect.gitRepositoryLinks.list` `developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.get` `developerconnect.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Developer Connect Service Agent 

(`roles/developerconnect.serviceAgent`) Gives the Developer Connect API Service Account access to necessary GCP resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `apphub.applications.get` `apphub.services.get` `apphub.services.list` `apphub.workloads.get` `apphub.workloads.list` `developerconnect.connections.get` `developerconnect.connections.httpProxyRead` `developerconnect.connections.httpProxyWrite` `developerconnect.gitRepositoryLinks.get` `developerconnect.operations.get`  
  
## Developer Connect service account

Developer Connect uses a _service agent_ to execute tasks on your behalf when communicating with other services. This service agent is created automatically when you first interact with Developer Connect (create a repository connection or account connector).

The identifier for the Developer Connect service agent is as follows, where PROJECT_NUMBER is your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    service-PROJECT_NUMBER@gcp-sa-devconnect.iam.gserviceaccount.com
    

You use this identifier to grant or modify IAM roles and permissions.

## Configure access to resources

For specific steps on granting roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).
  * [Connect to a GitHub repository](https://docs.cloud.google.com/developer-connect/docs/connect-repo).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
