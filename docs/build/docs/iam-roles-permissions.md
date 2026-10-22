---
url: https://docs.cloud.google.com/build/docs/iam-roles-permissions/
title: IAM roles and permissions \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:59.048668+00:00
---

# IAM roles and permissions  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/iam-roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Access control in Cloud Build is controlled using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam). IAM lets you create and manage permissions for Google Cloud resources. Cloud Build provides a specific set of [predefined IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#role-types) where each role contains a set of permissions. You can use these roles to give more granular access to specific Google Cloud resources and prevent unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

This page describes Cloud Build roles and permissions.

## Predefined Cloud Build roles

With IAM, every API method in Cloud Build API requires that the identity making the API request has the appropriate permissions to use the resource. Permissions are granted by setting policies that grant roles to a principal (user, group, or service account). You can grant multiple roles to a principal on the same resource.

The following table lists the Cloud Build IAM roles and the permissions that they include:

Role | Description | Permissions  
---|---|---  
**Name** : `roles/cloudbuild.builds.viewer`   
**Title** : Cloud Build Viewer  | Can view Cloud Build resources | `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.get` `cloudbuild.locations.list` `cloudbuild.operations.get` `cloudbuild.operations.list` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** : `roles/cloudbuild.builds.editor`   
**Title** : Cloud Build Editor  | Full control of Cloud Build resources | `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** : `roles/cloudbuild.builds.approver`   
**Title** : Cloud Build Approver  | Provide access to approve or reject pending builds | `cloudbuild.builds.approve` `cloudbuild.builds.get` `cloudbuild.builds.list` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** : `roles/cloudbuild.builds.builder`   
**Title** : Cloud Build Legacy Service Account  | When you enable the   
Cloud Build API for a project,   
the Cloud Build legacy service account   
is automatically created in the project   
and is granted this role for the resources   
in the project. The Cloud Build   
legacy service account uses this role only as   
required to perform actions when   
executing your build. |  For a list of permissions   
that this role contains,   
see [Default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account#default_permissions_of_service_account).   
**Name** : `roles/cloudbuild.integrationsViewer`   
**Title** : Cloud Build Integrations Viewer  | Can view Cloud Build  host connections | `cloudbuild.integrations.get` `cloudbuild.integrations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** :`roles/cloudbuild.integrationsEditor`   
**Title** : Cloud Build Integrations Editor  | Edit control of Cloud Build  host connections | `cloudbuild.integrations.get` `cloudbuild.integrations.list` `cloudbuild.integrations.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** :`roles/cloudbuild.integrationsOwner`   
**Title** : Cloud Build Integrations Owner  | Full control of Cloud Build  host connections | `cloudbuild.integrations.create` `cloudbuild.integrations.delete` `cloudbuild.integrations.get` `cloudbuild.integrations.list` `cloudbuild.integrations.update` `compute.firewalls.create` `compute.firewalls.get` `compute.firewalls.list` `compute.networks.get` `compute.networks.updatePolicy` `compute.regions.get` `compute.subnetworks.get` `compute.subnetworks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** :`roles/cloudbuild.connectionViewer`   
**Title** : Cloud Build Connection Viewer  | Can view and list connections  and repositories | `resourcemanager.projects.get` `resourcemanager.projects.list` `cloudbuild.connections.get` `cloudbuild.connections.fetchLinkableRepositories` `cloudbuild.connections.list` `cloudbuild.connections.getIamPolicy` `cloudbuild.repositories.get` `cloudbuild.repositories.list`  
**Name** :`roles/cloudbuild.connectionAdmin`   
**Title** : Cloud Build Connection Admin  | Can manage connections  and repositories | `resourcemanager.projects.get` `resourcemanager.projects.list` `cloudbuild.connections.get` `cloudbuild.connections.fetchLinkableRepositories` `cloudbuild.connections.list` `cloudbuild.connections.create` `cloudbuild.connections.update` `cloudbuild.connections.delete` `cloudbuild.connections.getIamPolicy` `cloudbuild.connections.setIamPolicy` `cloudbuild.repositories.get` `cloudbuild.repositories.list` `cloudbuild.repositories.create` `cloudbuild.repositories.delete`  
**Name** :`roles/cloudbuild.readTokenAccessor`   
**Title** : Cloud Build Read Only Token Accessor  | Can view the connection, its repositories,  and access their read-only token | `cloudbuild.connections.get` `cloudbuild.repositories.get` `cloudbuild.repositories.accessReadToken`  
**Name** :`roles/cloudbuild.tokenAccessor`   
**Title** : Cloud Build Token Accessor  | Can view the connection, its repositories,  and access their read-only and read/write token | `cloudbuild.connections.get` `cloudbuild.repositories.get` `cloudbuild.repositories.accessReadToken` `cloudbuild.repositories.accessReadWriteToken`  
**Name** : `roles/cloudbuild.workerPoolOwner`   
**Title** : Cloud Build WorkerPool Owner  | Full control of the private pool  | `cloudbuild.workerpools.create` `cloudbuild.workerpools.delete` `cloudbuild.workerpools.get` `cloudbuild.workerpools.list` `cloudbuild.workerpools.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** :`roles/cloudbuild.workerPoolEditor`   
**Title** : Cloud Build WorkerPool Editor  | Can update private pools  | `cloudbuild.workerpools.get` `cloudbuild.workerpools.list` `cloudbuild.workerpools.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** : `roles/cloudbuild.workerPoolViewer`   
**Title** : Cloud Build WorkerPool Viewer  | Can view private pools  | `cloudbuild.workerpools.get` `cloudbuild.workerpools.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
**Name** : `roles/cloudbuild.workerPoolUser`   
**Title** : Cloud Build WorkerPool User | Can run builds in the private pool | `cloudbuild.workerpools.use`  
  
In addition to the previous Cloud Build predefined roles, the [basic](https://docs.cloud.google.com/iam/docs/roles-overview#basic) Viewer, Editor, and Owner roles also include permissions related to Cloud Build. However, we recommend that you grant predefined roles where possible to comply with the [security principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

The following table lists the basic roles and the Cloud Build IAM roles that they include.

Role | includes role  
---|---  
`roles/viewer` | `roles/cloudbuild.builds.viewer`, `roles/cloudbuild.integrations.viewer`  
`roles/editor` | `roles/cloudbuild.builds.editor`, `roles/cloudbuild.integrations.editor`  
`roles/owner` | `roles/cloudbuild.integrations.owner`  
**Note:** Owner, Editor, and Viewer include permissions for many other Google Cloud services. The Owner role is automatically granted to the original project creator.

## Permissions

The following table lists the permissions that the caller must have to call each method:

API Method | Required Permission | Role Title  
---|---|---  
[`builds.create()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/create)   
[`triggers.create()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/create)   
[`triggers.patch()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/patch)   
[`triggers.delete()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/delete)   
[`triggers.run()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/run) | `cloudbuild.builds.create` | Cloud Build Editor  
[`builds.cancel()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/cancel) | `cloudbuild.builds.update` | Cloud Build Editor  
[`builds.get()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/get)   
[`triggers.get()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/get) | `cloudbuild.builds.get` | Cloud Build Editor, Cloud Build Viewer  
[`builds.list()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/list)   
[`triggers.list()`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/list) | `cloudbuild.builds.list` | Cloud Build Editor, Cloud Build Viewer  
**Caution:** `cloudbuild.builds.create` permission enables the user to run builds as the [Cloud Build legacy service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account). This permission is included in Cloud Build Editor, Project Owner, and Project Editor roles. Granting a user any of these roles will enable them to run builds as the Cloud Build legacy service account. Depending on the IAM permissions granted to the user and the permissions of the Cloud Build legacy service account, this could enable the user escalated build-time privileges.

## Permissions to view build logs

To view build logs, you require additional permissions depending on whether you're storing your build logs in the default Cloud Storage bucket or in a user-specified Cloud Storage bucket. For more information on permissions required to view build logs, see [Storing and viewing build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-view-build-logs).

## What's next

  * Learn about [the default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).
  * Learn how to [configure access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources).
  * Learn how to [configure access for Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account).
  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
