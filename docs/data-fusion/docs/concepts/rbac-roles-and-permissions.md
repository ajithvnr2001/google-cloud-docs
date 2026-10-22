---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/rbac-roles-and-permissions/
title: RBAC roles and permissions \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:59.430721+00:00
---

# RBAC roles and permissions  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/rbac-roles-and-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  RBAC roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the roles and permissions used by Cloud Data Fusion instances with [role-based access control](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac) (RBAC) enabled.

For fine-grained access enforcement at the namespace level and lower, use these data plane resources and permissions with RBAC.

## Resource hierarchy

Cloud Data Fusion resources have the following resource hierarchy:

![Cloud Data Fusion project resource hierarchy](https://docs.cloud.google.com/static/data-fusion/docs/images/concepts/data-fusion-resource-hierarchy@1x.png)

This figure shows the resource hierarchy in descending order (broadest to narrowest): Google Cloud project, location, Cloud Data Fusion instance, and namespaces. Below namespaces, in no order, are connections, secure keys, pipelines, artifacts (such as plugins, drivers, and applications), and compute profiles.

The following resources are Cloud Data Fusion [data plane](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#data-fusion-studio) resources that you control with the REST API or in the Cloud Data Fusion Studio: namespaces, connections, secure keys, pipelines, artifacts, and compute profiles.

## Predefined roles for RBAC

Cloud Data Fusion RBAC includes several predefined roles that you can use:

Instance Access role (`datafusion.accessor`)
    Grants the principal access to a Cloud Data Fusion instance, but not to any resources within the instance. Use this role in combination with other namespace-specific roles to provide fine-grained access to namespace.
Viewer role (`datafusion.viewer`)
    Grants access to a principal on a namespace to view pipelines, but not to author or run pipelines.
Operator role (`datafusion.operator`)
    Grants access to a principal on a namespace to access and run pipelines, change the compute profile, create compute profiles, or upload artifacts. Can perform the same actions as a developer, with the exception of previewing pipelines.
Developer role (`datafusion.developer`)
    Grants access to a principal on a namespace to create and modify limited resources, such as pipelines, within the namespace.
Editor role (`datafusion.editor`)
    Grants the principal full access to all Cloud Data Fusion resources under a namespace within a Cloud Data Fusion instance. This role must be granted in addition to the Instance Accessor role to the principal. With this role, the principal can create, delete, and modify resources in the namespace.
Instance Admin role (`datafusion.admin`)
    Grants access to all resources within a Cloud Data Fusion instance. Assigned through IAM. Not assigned at the namespace level through RBAC.
**Note:** A Cloud Data Fusion IAM role contains a number of permissions. They're less granular than RBAC roles. A combination of IAM and RBAC permissions are applied to each principal. IAM roles also have precedence over RBAC rolesOperation | datafusion.accessor | datafusion.viewer | datafusion.operator | datafusion.developer | datafusion.editor | datafusion.admin  
---|---|---|---|---|---|---  
**Instances**  
Access instance |  |  |  |  |  |   
**Namespaces**  
Create namespace |  |  |  |  |  | *  
Access namespace with explicit access granted |  |  |  |  |  |   
Access namespace without explicit access granted |  |  |  |  |  | *  
Edit namespace |  |  |  |  |  |   
Delete namespace |  |  |  |  |  |   
**Namespace service account**  
Add service account |  |  |  |  |  |   
Edit service account |  |  |  |  |  |   
Remove service account |  |  |  |  |  |   
Use service account |  |  |  |  |  |   
**RBAC**  
Grant or revoke permissions for other principals in the namespace |  |  |  |  |  | *  
**Schedules**  
Create schedule |  |  |  |  |  |   
View schedule |  |  |  |  |  |   
Change schedule |  |  |  |  |  |   
**Compute profiles**  
Create compute profiles |  |  |  |  |  |   
View compute profiles |  |  |  |  |  |   
Edit compute profiles |  |  |  |  |  |   
Delete compute profiles |  |  |  |  |  |   
**Connections**  
Create connections |  |  |  |  |  |   
View connections |  |  |  |  |  |   
Edit connections |  |  |  |  |  |   
Delete connections |  |  |  |  |  |   
Use connections |  |  |  |  |  |   
**Wrangler workspaces**  
Create workspaces |  |  |  |  |  |   
View workspaces |  |  |  |  |  |   
Edit workspaces |  |  |  |  |  |   
Delete workspaces |  |  |  |  |  |   
Use workspaces |  |  |  |  |  |   
**Pipelines**  
Create pipelines |  |  |  |  |  |   
View pipelines |  |  |  |  |  |   
Edit pipelines |  |  |  |  |  |   
Delete pipelines |  |  |  |  |  |   
Preview pipelines |  |  |  |  |  |   
Deploy pipelines |  |  |  |  |  |   
Run pipelines |  |  |  |  |  |   
**Secure keys**  
Create secure keys |  |  |  |  |  |   
View secure keys |  |  |  |  |  |   
Delete secure keys |  |  |  |  |  |   
**Tags**  
Create tags |  |  |  |  |  |   
View tags |  |  |  |  |  |   
Delete tags |  |  |  |  |  |   
**Cloud Data Fusion Hub**  
Deploy plugins |  |  |  |  |  |   
**Source Control Management**  
Configure source control repository |  |  |  |  |  |   
Sync pipelines from a namespace |  |  |  |  |  |   
**Lineage**  
View lineage |  |  |  |  |  |   
**Logs**  
View logs |  |  |  |  |  |   
  
* The principal must have the Data Fusion Admin IAM role, not the Instance Admin RBAC role. 

For a complete list of permissions included in Cloud Data Fusion's predefined role, see [Cloud Data Fusion predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion).

## Custom roles for RBAC

Some use cases cannot be implemented using the predefined roles for Cloud Data Fusion. In these cases, create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

### Examples

The following examples describe how to create custom roles for RBAC:

  * To create a custom role that only gives access to the secure keys within a namespace, create a custom role with the `datafusion.namespaces.get` and `datafusion.secureKeys.*` permissions.

  * To create a custom role that gives read-only access to secure keys, create a custom role with the `datafusion.namespaces.get`, `datafusion.secureKeys.getSecret`, and `datafusion.secureKeys.list` permissions.




## Permissions for common actions

A single, predefined permission might not be sufficient to perform the corresponding action. For example, to update namespace properties, you might also need `datafusion.namespaces.get` permission. The following table describes common actions performed within a Cloud Data Fusion instance and the required IAM permissions:

Action | Required Permission  
---|---  
Access an Instance | `datafusion.instances.get`  
Create a Namespace | `datafusion.namespaces.create`  
Get a Namespace | `datafusion.namespaces.get`  
Update Namespace Metadata (such as properties) | 

  * `datafusion.namespaces.get`
  * `datafusion.namespaces.update`

  
Delete Namespace (Only with Unrecoverable Reset Enabled) | 

  * `datafusion.namespaces.get`
  * `datafusion.namespaces.delete`

  
View Permissions on Namespace | `datafusion.namespaces.getIamPolicy`  
Grant Permissions on Namespace | `datafusion.namespaces.setIamPolicy`  
Pull Pipelines from Namespace SCM Configuration | 

  * `datafusion.namespaces.get`
  * `datafusion.namespaces.readRepository`
  * `datafusion.pipelines.create`

  
Push Pipelines to SCM Repository for Namespace | 

  * `datafusion.namespaces.get`
  * `datafusion.namespaces.writeRepository`

  
Get Namespace SCM Configuration | `datafusion.namespaces.get`  
Update Namespace SCM Configuration | `datafusion.namespaces.updateRepositoryMetadata`  
Set a Service Account for a Namespace | 

  * `datafusion.namespaces.get`
  * `datafusion.namespaces.setServiceAccount`

  
Unset a Service Account for a Namespace | 

  * `datafusion.namespaces.get`
  * `datafusion.namespaces.unsetServiceAccount`

  
Provision a Service Account Credential for a Namespace | `datafusion.namespaces.provisionCredential`  
View a Pipeline Draft | `datafusion.namespaces.get`  
Create/Delete a Pipeline Draft | 

  * `datafusion.namespaces.get`
  * `datafusion.namespaces.update`

  
List Compute Profiles | `datafusion.profiles.list`  
Create a Compute Profile | `datafusion.profiles.create`  
View a Compute Profile | `datafusion.profiles.get`  
Edit a Compute Profile | `datafusion.profiles.update`  
Delete a Compute Profile | `datafusion.profiles.delete`  
Create a Connection | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelineConnections.create`

  
View a Connection | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelineConnections.get`

  
Edit a Connection | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelineConnections.update`

  
Delete a Connection | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelineConnections.delete`

  
Browse, Sample, or View Connection Specifications | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelineConnections.use`

  
Create a Wrangler Workspace | 

  * `datafusion.namespaces.get`
  * `datafusion.wranglerWorkspaces.create`

  
View a Wrangler Workspace | 

  * `datafusion.namespaces.get`
  * `datafusion.wranglerWorkspaces.get`

  
Edit or re-sample a Wrangler Workspace | 

  * `datafusion.namespaces.get`
  * `datafusion.wranglerWorkspaces.update`

  
Delete a Wrangler Workspace | 

  * `datafusion.namespaces.get`
  * `datafusion.wranglerWorkspaces.delete`

  
Apply a set of directives on a Wrangler Workspace | 

  * `datafusion.namespaces.get`
  * `datafusion.wranglerWorkspaces.use`

  
List Pipelines | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelines.list`

  
Create Pipeline | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelines.create`

  
View Pipeline | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelines.get`

  
Edit Pipeline | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelines.create`

  
Edit Pipeline Properties | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelines.update`

  
Delete Pipeline | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelines.delete`

  
Preview Pipeline | `datafusion.pipelines.preview`  
Run Pipeline | `datafusion.pipelines.execute`  
Create Schedule | `datafusion.pipelines.execute`  
View Schedule | 

  * `datafusion.namespaces.get`
  * `datafusion.pipelines.get`

  
Change Schedule | `datafusion.pipelines.execute`  
List Secure Keys | 

  * `datafusion.namespaces.get`
  * `datafusion.secureKeys.list`

  
Create Secure Keys | 

  * `datafusion.namespaces.get`
  * `datafusion.secureKeys.update`

  
View Secure Keys | 

  * `datafusion.namespaces.get`
  * `datafusion.secureKeys.getSecret`

  
Delete Secure Keys | 

  * `datafusion.namespaces.get`
  * `datafusion.secureKeys.delete`

  
List Artifacts* | 

  * `datafusion.namespaces.get`
  * `datafusion.artifacts.list`

  
Create an Artifact* | 

  * `datafusion.namespaces.get`
  * `datafusion.artifacts.create`
  * `datafusion.artifacts.update`

  
Get an Artifact* | 

  * `datafusion.namespaces.get`
  * `datafusion.artifacts.get`

  
Delete an Artifact* | 

  * `datafusion.namespaces.get`
  * `datafusion.artifacts.delete`

  
Preferences, Tags, and Metadata | Preferences, tags, and metadata are set at the resource level for the particular resource (`datafusion.RESOURCE.update`).   
Dataset Permissions (Deprecated) | `datafusion.namespaces.update`  
  
* Artifacts, such as plugins and drivers, are items that you upload in Cloud Data Fusion for developing pipelines. 

## What's next

  * Learn more about [RBAC](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac) in Cloud Data Fusion.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
