---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager/
title: Secure Source Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:09:38.053333+00:00
---

# Secure Source Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Secure Source Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Secure Source Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Secure Source Manager roles

Role | Permissions  
---|---  
  
#### Secure Source Manager Admin 

(`roles/securesourcemanager.admin`) Full access to all Secure Source Manager resources.  |  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.*`

  * `securesourcemanager.branchRules.create`
  * `securesourcemanager.branchRules.delete`
  * `securesourcemanager.branchRules.get`
  * `securesourcemanager.branchRules.list`
  * `securesourcemanager.branchRules.update`
  * `securesourcemanager.hooks.create`
  * `securesourcemanager.hooks.delete`
  * `securesourcemanager.hooks.get`
  * `securesourcemanager.hooks.list`
  * `securesourcemanager.hooks.update`
  * `securesourcemanager.instances.access`
  * `securesourcemanager.instances.create`
  * `securesourcemanager.instances.createRepository`
  * `securesourcemanager.instances.delete`
  * `securesourcemanager.instances.get`
  * `securesourcemanager.instances.getIamPolicy`
  * `securesourcemanager.instances.linkDeveloperConnect`
  * `securesourcemanager.instances.list`
  * `securesourcemanager.instances.setIamPolicy`
  * `securesourcemanager.issuecomments.create`
  * `securesourcemanager.issuecomments.delete`
  * `securesourcemanager.issuecomments.get`
  * `securesourcemanager.issuecomments.list`
  * `securesourcemanager.issuecomments.update`
  * `securesourcemanager.issues.close`
  * `securesourcemanager.issues.create`
  * `securesourcemanager.issues.delete`
  * `securesourcemanager.issues.get`
  * `securesourcemanager.issues.list`
  * `securesourcemanager.issues.open`
  * `securesourcemanager.issues.update`
  * `securesourcemanager.locations.get`
  * `securesourcemanager.locations.list`
  * `securesourcemanager.operations.cancel`
  * `securesourcemanager.operations.delete`
  * `securesourcemanager.operations.get`
  * `securesourcemanager.operations.list`
  * `securesourcemanager.prcomments.create`
  * `securesourcemanager.prcomments.delete`
  * `securesourcemanager.prcomments.get`
  * `securesourcemanager.prcomments.list`
  * `securesourcemanager.prcomments.resolve`
  * `securesourcemanager.prcomments.unresolve`
  * `securesourcemanager.prcomments.update`
  * `securesourcemanager.pullRequests.close`
  * `securesourcemanager.pullRequests.create`
  * `securesourcemanager.pullRequests.get`
  * `securesourcemanager.pullRequests.list`
  * `securesourcemanager.pullRequests.listFileDiffs`
  * `securesourcemanager.pullRequests.merge`
  * `securesourcemanager.pullRequests.open`
  * `securesourcemanager.pullRequests.update`
  * `securesourcemanager.repositories.approvePullRequests`
  * `securesourcemanager.repositories.create`
  * `securesourcemanager.repositories.delete`
  * `securesourcemanager.repositories.fetch`
  * `securesourcemanager.repositories.get`
  * `securesourcemanager.repositories.getIamPolicy`
  * `securesourcemanager.repositories.list`
  * `securesourcemanager.repositories.push`
  * `securesourcemanager.repositories.readIssues`
  * `securesourcemanager.repositories.readPullRequests`
  * `securesourcemanager.repositories.setIamPolicy`
  * `securesourcemanager.repositories.update`
  * `securesourcemanager.repositories.writeIssues`
  * `securesourcemanager.repositories.writePullRequests`
  * `securesourcemanager.sshkeys.create`
  * `securesourcemanager.sshkeys.createAny`
  * `securesourcemanager.sshkeys.delete`
  * `securesourcemanager.sshkeys.deleteAny`
  * `securesourcemanager.sshkeys.get`
  * `securesourcemanager.sshkeys.list`
  * `securesourcemanager.sshkeys.listAny`

  
  
#### Secure Source Manager Editor 

(`roles/securesourcemanager.editor`) Editor role for Secure Source Manager  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.branchRules.*`

  * `securesourcemanager.branchRules.create`
  * `securesourcemanager.branchRules.delete`
  * `securesourcemanager.branchRules.get`
  * `securesourcemanager.branchRules.list`
  * `securesourcemanager.branchRules.update`

`securesourcemanager.hooks.*`

  * `securesourcemanager.hooks.create`
  * `securesourcemanager.hooks.delete`
  * `securesourcemanager.hooks.get`
  * `securesourcemanager.hooks.list`
  * `securesourcemanager.hooks.update`

`securesourcemanager.instances.access` `securesourcemanager.instances.create` `securesourcemanager.instances.createRepository` `securesourcemanager.instances.delete` `securesourcemanager.instances.get` `securesourcemanager.instances.getIamPolicy` `securesourcemanager.instances.linkDeveloperConnect` `securesourcemanager.instances.list` `securesourcemanager.issuecomments.*`

  * `securesourcemanager.issuecomments.create`
  * `securesourcemanager.issuecomments.delete`
  * `securesourcemanager.issuecomments.get`
  * `securesourcemanager.issuecomments.list`
  * `securesourcemanager.issuecomments.update`

`securesourcemanager.issues.*`

  * `securesourcemanager.issues.close`
  * `securesourcemanager.issues.create`
  * `securesourcemanager.issues.delete`
  * `securesourcemanager.issues.get`
  * `securesourcemanager.issues.list`
  * `securesourcemanager.issues.open`
  * `securesourcemanager.issues.update`

`securesourcemanager.locations.*`

  * `securesourcemanager.locations.get`
  * `securesourcemanager.locations.list`

`securesourcemanager.operations.*`

  * `securesourcemanager.operations.cancel`
  * `securesourcemanager.operations.delete`
  * `securesourcemanager.operations.get`
  * `securesourcemanager.operations.list`

`securesourcemanager.prcomments.*`

  * `securesourcemanager.prcomments.create`
  * `securesourcemanager.prcomments.delete`
  * `securesourcemanager.prcomments.get`
  * `securesourcemanager.prcomments.list`
  * `securesourcemanager.prcomments.resolve`
  * `securesourcemanager.prcomments.unresolve`
  * `securesourcemanager.prcomments.update`

`securesourcemanager.pullRequests.*`

  * `securesourcemanager.pullRequests.close`
  * `securesourcemanager.pullRequests.create`
  * `securesourcemanager.pullRequests.get`
  * `securesourcemanager.pullRequests.list`
  * `securesourcemanager.pullRequests.listFileDiffs`
  * `securesourcemanager.pullRequests.merge`
  * `securesourcemanager.pullRequests.open`
  * `securesourcemanager.pullRequests.update`

`securesourcemanager.repositories.approvePullRequests` `securesourcemanager.repositories.create` `securesourcemanager.repositories.delete` `securesourcemanager.repositories.fetch` `securesourcemanager.repositories.get` `securesourcemanager.repositories.getIamPolicy` `securesourcemanager.repositories.list` `securesourcemanager.repositories.push` `securesourcemanager.repositories.readIssues` `securesourcemanager.repositories.readPullRequests` `securesourcemanager.repositories.update` `securesourcemanager.repositories.writeIssues` `securesourcemanager.repositories.writePullRequests` `securesourcemanager.sshkeys.*`

  * `securesourcemanager.sshkeys.create`
  * `securesourcemanager.sshkeys.createAny`
  * `securesourcemanager.sshkeys.delete`
  * `securesourcemanager.sshkeys.deleteAny`
  * `securesourcemanager.sshkeys.get`
  * `securesourcemanager.sshkeys.list`
  * `securesourcemanager.sshkeys.listAny`

  
  
#### Secure Source Manager Viewer 

(`roles/securesourcemanager.viewer`) Viewer role for Secure Source Manager  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.branchRules.get` `securesourcemanager.branchRules.list` `securesourcemanager.hooks.get` `securesourcemanager.hooks.list` `securesourcemanager.instances.access` `securesourcemanager.instances.get` `securesourcemanager.instances.getIamPolicy` `securesourcemanager.instances.list` `securesourcemanager.issuecomments.get` `securesourcemanager.issuecomments.list` `securesourcemanager.issues.get` `securesourcemanager.issues.list` `securesourcemanager.locations.*`

  * `securesourcemanager.locations.get`
  * `securesourcemanager.locations.list`

`securesourcemanager.operations.get` `securesourcemanager.operations.list` `securesourcemanager.prcomments.get` `securesourcemanager.prcomments.list` `securesourcemanager.pullRequests.get` `securesourcemanager.pullRequests.list` `securesourcemanager.pullRequests.listFileDiffs` `securesourcemanager.repositories.fetch` `securesourcemanager.repositories.get` `securesourcemanager.repositories.getIamPolicy` `securesourcemanager.repositories.list` `securesourcemanager.repositories.readIssues` `securesourcemanager.repositories.readPullRequests` `securesourcemanager.sshkeys.get` `securesourcemanager.sshkeys.list` `securesourcemanager.sshkeys.listAny`  
  
#### Secure Source Manager Developer Connect Linker 

(`roles/securesourcemanager.developerConnectLinker`) A Developer Connect Linker can link a Secure Source Manager instance to Developer Connect.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.instances.access` `securesourcemanager.instances.linkDeveloperConnect` `securesourcemanager.operations.get` `securesourcemanager.repositories.fetch` `securesourcemanager.repositories.get` `securesourcemanager.repositories.list` `securesourcemanager.repositories.push`  
  
#### Secure Source Manager Instance Accessor 

(`roles/securesourcemanager.instanceAccessor`) An instance accessor can access an instance, but not necessarily create resources in the instance.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.instances.access` `securesourcemanager.sshkeys.create` `securesourcemanager.sshkeys.delete` `securesourcemanager.sshkeys.get` `securesourcemanager.sshkeys.list`  
  
#### Secure Source Manager Instance Manager 

(`roles/securesourcemanager.instanceManager`) Read-write access to all Secure Source Manager resources (full control except for the ability to modify permissions).  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.instances.access` `securesourcemanager.instances.createRepository` `securesourcemanager.instances.delete` `securesourcemanager.instances.get` `securesourcemanager.instances.list` `securesourcemanager.locations.*`

  * `securesourcemanager.locations.get`
  * `securesourcemanager.locations.list`

`securesourcemanager.operations.*`

  * `securesourcemanager.operations.cancel`
  * `securesourcemanager.operations.delete`
  * `securesourcemanager.operations.get`
  * `securesourcemanager.operations.list`

`securesourcemanager.sshkeys.*`

  * `securesourcemanager.sshkeys.create`
  * `securesourcemanager.sshkeys.createAny`
  * `securesourcemanager.sshkeys.delete`
  * `securesourcemanager.sshkeys.deleteAny`
  * `securesourcemanager.sshkeys.get`
  * `securesourcemanager.sshkeys.list`
  * `securesourcemanager.sshkeys.listAny`

  
  
#### Secure Source Manager Instance Owner 

(`roles/securesourcemanager.instanceOwner`) Full control over Secure Source Manager instances, including listing, creating, and deleting them. Also enables instance user management.  |  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.instances.*`

  * `securesourcemanager.instances.access`
  * `securesourcemanager.instances.create`
  * `securesourcemanager.instances.createRepository`
  * `securesourcemanager.instances.delete`
  * `securesourcemanager.instances.get`
  * `securesourcemanager.instances.getIamPolicy`
  * `securesourcemanager.instances.linkDeveloperConnect`
  * `securesourcemanager.instances.list`
  * `securesourcemanager.instances.setIamPolicy`

`securesourcemanager.locations.*`

  * `securesourcemanager.locations.get`
  * `securesourcemanager.locations.list`

`securesourcemanager.operations.*`

  * `securesourcemanager.operations.cancel`
  * `securesourcemanager.operations.delete`
  * `securesourcemanager.operations.get`
  * `securesourcemanager.operations.list`

`securesourcemanager.sshkeys.*`

  * `securesourcemanager.sshkeys.create`
  * `securesourcemanager.sshkeys.createAny`
  * `securesourcemanager.sshkeys.delete`
  * `securesourcemanager.sshkeys.deleteAny`
  * `securesourcemanager.sshkeys.get`
  * `securesourcemanager.sshkeys.list`
  * `securesourcemanager.sshkeys.listAny`

  
  
#### Secure Source Manager Instance Repository Creator 

(`roles/securesourcemanager.instanceRepositoryCreator`) An instance repository creator can connect to a Cloud Git instance via IAP (HTTPS) and create repositories in the instance.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.instances.access` `securesourcemanager.instances.createRepository` `securesourcemanager.sshkeys.create` `securesourcemanager.sshkeys.delete` `securesourcemanager.sshkeys.get` `securesourcemanager.sshkeys.list`  
  
#### Secure Source Manager Repository Admin 

(`roles/securesourcemanager.repoAdmin`) A repoAdmin has the ability to CRUD a repository and its children as well as assign users to a repository. They can also set, get, or check IAM policies on the repository.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.branchRules.*`

  * `securesourcemanager.branchRules.create`
  * `securesourcemanager.branchRules.delete`
  * `securesourcemanager.branchRules.get`
  * `securesourcemanager.branchRules.list`
  * `securesourcemanager.branchRules.update`

`securesourcemanager.hooks.*`

  * `securesourcemanager.hooks.create`
  * `securesourcemanager.hooks.delete`
  * `securesourcemanager.hooks.get`
  * `securesourcemanager.hooks.list`
  * `securesourcemanager.hooks.update`

`securesourcemanager.issuecomments.*`

  * `securesourcemanager.issuecomments.create`
  * `securesourcemanager.issuecomments.delete`
  * `securesourcemanager.issuecomments.get`
  * `securesourcemanager.issuecomments.list`
  * `securesourcemanager.issuecomments.update`

`securesourcemanager.issues.*`

  * `securesourcemanager.issues.close`
  * `securesourcemanager.issues.create`
  * `securesourcemanager.issues.delete`
  * `securesourcemanager.issues.get`
  * `securesourcemanager.issues.list`
  * `securesourcemanager.issues.open`
  * `securesourcemanager.issues.update`

`securesourcemanager.prcomments.*`

  * `securesourcemanager.prcomments.create`
  * `securesourcemanager.prcomments.delete`
  * `securesourcemanager.prcomments.get`
  * `securesourcemanager.prcomments.list`
  * `securesourcemanager.prcomments.resolve`
  * `securesourcemanager.prcomments.unresolve`
  * `securesourcemanager.prcomments.update`

`securesourcemanager.pullRequests.*`

  * `securesourcemanager.pullRequests.close`
  * `securesourcemanager.pullRequests.create`
  * `securesourcemanager.pullRequests.get`
  * `securesourcemanager.pullRequests.list`
  * `securesourcemanager.pullRequests.listFileDiffs`
  * `securesourcemanager.pullRequests.merge`
  * `securesourcemanager.pullRequests.open`
  * `securesourcemanager.pullRequests.update`

`securesourcemanager.repositories.*`

  * `securesourcemanager.repositories.approvePullRequests`
  * `securesourcemanager.repositories.create`
  * `securesourcemanager.repositories.delete`
  * `securesourcemanager.repositories.fetch`
  * `securesourcemanager.repositories.get`
  * `securesourcemanager.repositories.getIamPolicy`
  * `securesourcemanager.repositories.list`
  * `securesourcemanager.repositories.push`
  * `securesourcemanager.repositories.readIssues`
  * `securesourcemanager.repositories.readPullRequests`
  * `securesourcemanager.repositories.setIamPolicy`
  * `securesourcemanager.repositories.update`
  * `securesourcemanager.repositories.writeIssues`
  * `securesourcemanager.repositories.writePullRequests`

  
  
#### Secure Source Manager Repository Creator 

(`roles/securesourcemanager.repoCreator`) A repoCreator has access to create repostiory in a project, the creator will then become the repoAdmin on this repository.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.repositories.create`  
  
#### Secure Source Manager Repository Pull Request Approver 

(`roles/securesourcemanager.repoPullRequestApprover`) A pull request approver can approve pull requests in a repository.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.repositories.approvePullRequests`  
  
#### Secure Source Manager Repository Reader 

(`roles/securesourcemanager.repoReader`) A repoReader has read access to a particular repository, including its child components. They cannot create repositories, and do not manage IAM policies on the repository.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.branchRules.get` `securesourcemanager.branchRules.list` `securesourcemanager.hooks.get` `securesourcemanager.hooks.list` `securesourcemanager.issuecomments.get` `securesourcemanager.issuecomments.list` `securesourcemanager.issues.get` `securesourcemanager.issues.list` `securesourcemanager.prcomments.get` `securesourcemanager.prcomments.list` `securesourcemanager.pullRequests.get` `securesourcemanager.pullRequests.list` `securesourcemanager.pullRequests.listFileDiffs` `securesourcemanager.repositories.fetch` `securesourcemanager.repositories.get` `securesourcemanager.repositories.list` `securesourcemanager.repositories.readIssues` `securesourcemanager.repositories.readPullRequests`  
  
#### Secure Source Manager Repository Writer 

(`roles/securesourcemanager.repoWriter`) A repoWriter has read/write access to a particular repository, including its child components. They cannot create repositories, and do not manage IAM policies on the repository.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.branchRules.get` `securesourcemanager.branchRules.list` `securesourcemanager.hooks.get` `securesourcemanager.hooks.list` `securesourcemanager.issuecomments.*`

  * `securesourcemanager.issuecomments.create`
  * `securesourcemanager.issuecomments.delete`
  * `securesourcemanager.issuecomments.get`
  * `securesourcemanager.issuecomments.list`
  * `securesourcemanager.issuecomments.update`

`securesourcemanager.issues.*`

  * `securesourcemanager.issues.close`
  * `securesourcemanager.issues.create`
  * `securesourcemanager.issues.delete`
  * `securesourcemanager.issues.get`
  * `securesourcemanager.issues.list`
  * `securesourcemanager.issues.open`
  * `securesourcemanager.issues.update`

`securesourcemanager.prcomments.*`

  * `securesourcemanager.prcomments.create`
  * `securesourcemanager.prcomments.delete`
  * `securesourcemanager.prcomments.get`
  * `securesourcemanager.prcomments.list`
  * `securesourcemanager.prcomments.resolve`
  * `securesourcemanager.prcomments.unresolve`
  * `securesourcemanager.prcomments.update`

`securesourcemanager.pullRequests.*`

  * `securesourcemanager.pullRequests.close`
  * `securesourcemanager.pullRequests.create`
  * `securesourcemanager.pullRequests.get`
  * `securesourcemanager.pullRequests.list`
  * `securesourcemanager.pullRequests.listFileDiffs`
  * `securesourcemanager.pullRequests.merge`
  * `securesourcemanager.pullRequests.open`
  * `securesourcemanager.pullRequests.update`

`securesourcemanager.repositories.fetch` `securesourcemanager.repositories.get` `securesourcemanager.repositories.list` `securesourcemanager.repositories.push` `securesourcemanager.repositories.readIssues` `securesourcemanager.repositories.readPullRequests` `securesourcemanager.repositories.writeIssues` `securesourcemanager.repositories.writePullRequests`  
  
#### Secure Source Manager SSH Key User 

(`roles/securesourcemanager.sshKeyUser`) An sshKeyUser can create SSH keys for themselves and list/delete SSH keys they own.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securesourcemanager.sshkeys.create` `securesourcemanager.sshkeys.delete` `securesourcemanager.sshkeys.get` `securesourcemanager.sshkeys.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Secure Source Manager Service Agent 

(`roles/securesourcemanager.serviceAgent`) Gives Secure Source Manager service account access to managed resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.signJwt` `securesourcemanager.instances.access` `serviceusage.services.use`  
  
## Secure Source Manager permissions

Permission | Included in roles  
---|---  
  
#### `securesourcemanager.branchRules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.branchRules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.branchRules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.branchRules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.branchRules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.hooks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.hooks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.hooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.hooks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.hooks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.instances.access`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Developer Connect Linker](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.developerConnectLinker) (`roles/securesourcemanager.developerConnectLinker`)  [Secure Source Manager Instance Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)  [Secure Source Manager Instance Repository Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Secure Source Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.serviceAgent) (`roles/securesourcemanager.serviceAgent`) 

  
  
#### `securesourcemanager.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.instances.createRepository`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)  [Secure Source Manager Instance Repository Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`)   
  
#### `securesourcemanager.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.instances.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.instances.linkDeveloperConnect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Developer Connect Linker](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.developerConnectLinker) (`roles/securesourcemanager.developerConnectLinker`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.instances.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.issuecomments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issuecomments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issuecomments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issuecomments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issuecomments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issues.close`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issues.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issues.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issues.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issues.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issues.open`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.issues.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Developer Connect Linker](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.developerConnectLinker) (`roles/securesourcemanager.developerConnectLinker`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.prcomments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.prcomments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.prcomments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.prcomments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.prcomments.resolve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.prcomments.unresolve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.prcomments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.close`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.listFileDiffs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.merge`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.open`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.pullRequests.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.approvePullRequests`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Pull Request Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoPullRequestApprover) (`roles/securesourcemanager.repoPullRequestApprover`)   
  
#### `securesourcemanager.repositories.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoCreator) (`roles/securesourcemanager.repoCreator`)   
  
#### `securesourcemanager.repositories.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.repositories.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Developer Connect Linker](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.developerConnectLinker) (`roles/securesourcemanager.developerConnectLinker`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Developer Connect Linker](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.developerConnectLinker) (`roles/securesourcemanager.developerConnectLinker`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.repositories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Developer Connect Linker](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.developerConnectLinker) (`roles/securesourcemanager.developerConnectLinker`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.push`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Developer Connect Linker](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.developerConnectLinker) (`roles/securesourcemanager.developerConnectLinker`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.readIssues`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.readPullRequests`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.repositories.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)   
  
#### `securesourcemanager.repositories.writeIssues`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.repositories.writePullRequests`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Repository Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`)  [Secure Source Manager Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`)   
  
#### `securesourcemanager.sshkeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)  [Secure Source Manager Instance Repository Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`)  [Secure Source Manager SSH Key User](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.sshKeyUser) (`roles/securesourcemanager.sshKeyUser`)   
  
#### `securesourcemanager.sshkeys.createAny`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.sshkeys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)  [Secure Source Manager Instance Repository Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`)  [Secure Source Manager SSH Key User](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.sshKeyUser) (`roles/securesourcemanager.sshKeyUser`)   
  
#### `securesourcemanager.sshkeys.deleteAny`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
#### `securesourcemanager.sshkeys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)  [Secure Source Manager Instance Repository Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`)  [Secure Source Manager SSH Key User](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.sshKeyUser) (`roles/securesourcemanager.sshKeyUser`)   
  
#### `securesourcemanager.sshkeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)  [Secure Source Manager Instance Repository Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`)  [Secure Source Manager SSH Key User](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.sshKeyUser) (`roles/securesourcemanager.sshKeyUser`)   
  
#### `securesourcemanager.sshkeys.listAny`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secure Source Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`)  [Secure Source Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.editor) (`roles/securesourcemanager.editor`)  [Secure Source Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.viewer) (`roles/securesourcemanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secure Source Manager Instance Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`)  [Secure Source Manager Instance Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
