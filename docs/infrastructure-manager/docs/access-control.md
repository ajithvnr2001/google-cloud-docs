---
url: https://docs.cloud.google.com/infrastructure-manager/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:45.891887+00:00
---

# Access control with IAM  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Infrastructure Manager roles and permissions.

Infra Manager uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) to control access to the service. To grant access to deploy resources with Infra Manager, assign the needed Infra Manager [IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#role-types) to the [service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account) that you use to call Infra Manager. For details about how to grant permissions to service accounts, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

A service account is not required to view Infra Manager deployments, revisions, and IAM policies. To view Infra Manager, grant access to the user, group, or service account.

To deploy or view the Google Cloud resources defined in the Terraform configuration, you need to grant the service account permissions that are specific to these resources. These permissions are in addition to the Infra Manager permissions listed on this page. For a list of all roles and the permissions they contain, see [Identity and Access Management basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Predefined Infra Manager roles

IAM provides [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) that grant access to specific Google Cloud resources and prevent unauthorized access to other resources.

The following table lists the Infra Manager IAM roles and the permissions that they include:

Role | Description | Permissions  
---|---|---  
Infra Manager Admin (`roles/config.admin`) | For a user, full control to Infra Manager resources | `config.deployments.create`  
`config.deployments.delete`  
`config.deployments.deleteState`  
`config.deployments.get`  
`config.deployments.getIamPolicy`  
`config.deployments.getLock`  
`config.deployments.getState`  
`config.deployments.list`  
`config.deployments.lock`  
`config.deployments.setIamPolicy`  
`config.deploymentgroups.create`  
`config.deploymentgroups.update`  
`config.deploymentgroups.delete`  
`config.deploymentgroups.get`  
`config.deploymentgroups.list`  
`config.deploymentgroups.provision`  
`config.deploymentgroups.deprovision`  
`config.deploymentgrouprevisions.get`  
`config.deploymentgrouprevisions.list`  
`config.deployments.unlock`  
`config.deployments.update`  
`config.deployments.updateState`  
`config.automigrationconfig.get`  
`config.automigrationconfig.update`  
`config.previews.create`  
`config.previews.delete`  
`config.previews.get`  
`config.previews.list`  
`config.previews.export`  
`config.previews.upload`  
`config.locations.get`  
`config.locations.list`  
`config.operations.cancel`  
`config.operations.delete`  
`config.operations.get`  
`config.operations.list`  
`config.resources.get`  
`config.resources.list`  
`config.resourcechanges.get`  
`config.resourcechanges.list`  
`config.resourcedrifts.get`  
`config.resourcedrifts.list`  
`config.revisions.get`  
`config.revisions.getState`  
`config.revisions.list`  
`config.artifacts.import`  
`config.terraformversions.get`  
`config.terraformversions.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
Infra Manager Service Agent (`roles/config.agent`) | Provide access to a service account to work with Infra Manager, including deployments, revisions, logging, and Terraform state files. | `storage.buckets.get`  
`storage.buckets.list`  
`storage.buckets.create`  
`storage.buckets.update`  
`storage.buckets.delete`  
`storage.objects.get`  
`storage.objects.list`  
`storage.objects.create`  
`storage.objects.update`  
`storage.objects.delete`  
`logging.logEntries.create`  
`config.deployments.getState`  
`config.deployments.updateState`  
`config.deployments.deleteState`  
`config.deployments.getLock`  
`config.previews.upload`  
`config.artifacts.import`  
`config.revisions.getState`  
`cloudbuild.connections.list`  
`cloudbuild.repositories.accessReadToken`  
`cloudbuild.repositories.list`  
`cloudquotas.quotas.get`  
`monitoring.timeSeries.list`  
Infra Manager Service Account (`roles/cloudconfig.serviceAgent`) | When you enable the Infra Manager API, the Infra Manager service account is automatically created in the project and is granted this role for the resources in the project. The Infra Manager service account uses this role only as required to perform actions when creating, managing, or deleting deployments and revisions. | `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`cloudbuild.builds.create`  
`cloudbuild.builds.update`  
`cloudbuild.workerpools.use`  
`iam.serviceAccounts.actAs`  
`iam.serviceAccounts.getAccessToken`  
`logging.logEntries.create`  
`logging.logEntries.route`  
`serviceusage.services.use`  
`storage.buckets.get`  
`storage.buckets.list`  
`storage.buckets.create`  
`storage.buckets.update`  
`storage.buckets.delete`  
`storage.objects.get`  
`storage.objects.list`  
`storage.objects.create`  
`storage.objects.update`  
`storage.objects.delete`  
Infra Manager Viewer (`roles/config.viewer`) | Read deployments, revisions, and IAM policies. | `config.deployments.get`  
`config.deployments.getIamPolicy`  
`config.deployments.list`  
`config.deploymentgroups.get`  
`config.deploymentgroups.list`  
`config.deploymentgrouprevisions.get`  
`config.deploymentgrouprevisions.list`  
`config.previews.get`  
`config.previews.list`  
`config.locations.get`  
`config.locations.list`  
`config.operations.get`  
`config.operations.list`  
`config.resources.get`  
`config.resources.list`  
`config.revisions.get`  
`config.revisions.list`  
`config.terraformversions.get`  
`config.terraformversions.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
In addition to the Infra Manager predefined roles, the [basic](https://docs.cloud.google.com/iam/docs/roles-overview#basic) Viewer and Owner roles also include permissions related to Infra Manager. However, we recommend that you grant predefined roles where possible to comply with the [security principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

The following table lists the basic roles and the Infra Manager IAM roles that they include.

Role | Includes role  
---|---  
Viewer | `roles/config.viewer`  
Owner | `roles/config.admin`  
  
## Permissions

Permissions that the caller must have to call each method is listed in the [REST API reference](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest).

## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [using conditions in IAM](https://docs.cloud.google.com/deploy/docs/securing/iam#about_iam_conditions)
  * Find out more about [Infra Manager service accounts](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
