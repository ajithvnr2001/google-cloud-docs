---
url: https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources/
title: Managing access to Compute Engine resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:05.552569+00:00
---

# Managing access to Compute Engine resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Managing access to Compute Engine resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can exercise the principle of least privilege by granting access to specific Compute Engine resources instead of granting access to a parent resource such as a project, folder, or organization.

You grant access to a resource by setting an [Identity and Access Management (IAM) policy](https://docs.cloud.google.com/compute/docs/access#lower-level-policies) on the resource. The policy binds one or more members, such as a user or a service account, to one or more [roles](https://docs.cloud.google.com/compute/docs/access/iam). Each role contains a list of permissions that let the member interact with the resource.

If you grant access to a [parent resource](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control) (for example, to a project), you implicitly grant access to all its child resources (for example, to all VMs in that project). To limit access to resources, set IAM policies on lower-level resources when possible, instead of at the project level or above.

For general information about how to grant, change, and revoke access to resources unrelated to Compute Engine, for example, to grant access to a Google Cloud project, see the IAM documentation for [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Before you begin

  * Review the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).
  * Read the Compute Engine [access control overview](https://docs.cloud.google.com/compute/docs/access).
  * Familiarize yourself with [IAM roles for Compute Engine ](https://docs.cloud.google.com/compute/docs/access/iam).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to manage access to Compute Engine resources, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on the resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage access to Compute Engine resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage access to Compute Engine resources:

  * To grant or revoke access to resources: 
    * `compute.projects.get` on the project
    * `compute.RESOURCE_TYPE.get` on the resource
    * `compute.RESOURCE_TYPE.getIamPolicy` on the resource
    * `compute.RESOURCE_TYPE.setIamPolicy` on the resource
  * To test caller permissions: `compute.RESOURCE_TYPE.getIamPolicy` on the resource 

Replace RESOURCE_TYPE with the resource that you want to manage access to. For example `instances`, `instanceTemplates`, or `images`.




You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Supported resources

To view a list of Compute Engine resources that support resource-level access control, see [Resource types that accept IAM policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies) and filter for **Compute Engine**.

For other Compute Engine resources that don't support resource-level access control, you must manage access to those resources at the project, folder, or organization levels. For information about organizations, folders, or projects, see [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

## Granting access to Compute Engine resources

A _principal_ , such as a user or service account, can access Compute Engine resources. An _identity_ is a property of a principal. A principal's identity is typically represented by an email address associated with the account.

Before you grant an IAM role to a principal for a resource, check which roles are available to grant on a particular resource. For more information, see [Viewing the grantable roles on resources](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles).

To grant permission to access specific Compute Engine resources, set an [IAM policy](https://docs.cloud.google.com/iam/docs/policies) on the resource.

**Note:** When managing access for users in [external identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), replace instances of Google Account principal identifiers—like `user:kiran@example.com`, `group:support@example.com`, and `domain:example.com`—with appropriate [Workforce Identity Federation principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 

###  Console 

  1. In the Google Cloud console, go to the respective resource page for which you want to add permissions. 
     * For instances, go to the [VM instances page](https://console.cloud.google.com/compute/instances).
     * For zonal and regional disks, go to the [Disks page](https://console.cloud.google.com/compute/disks).
     * For snapshots, go to the [Snapshots page](https://console.cloud.google.com/compute/snapshots).
     * For images, go to the [Images page](https://console.cloud.google.com/compute/images).
     * For instance templates, go to the [Instance templates page](https://console.cloud.google.com/compute/instanceTemplates).
     * For machine images, go to the [Machine images page](https://console.cloud.google.com/compute/machineImages).
     * For reservations, go to the [Reservations page](https://console.cloud.google.com/compute/reservations).
     * For sole-tenant nodes, go to the [Sole-tenant nodes page](https://console.cloud.google.com/compute/soleTenancy).
  2. Select the checkboxes next to the resources you want to update.
  3. Complete the following steps based on the resource page. 
     * For VM instances, click person **Permissions**.
     * For all other resources, complete the following: 
       1. Check if the info panel is visible. If it is not visible, click **Show info panel**.
       2. Select the **Permissions** tab.
  4. Click person_add **Add principal**.
  5. Add the identity for the principal and select the required role.
  6. To save your changes, click **Save**.



###  gcloud 

To grant a role to a principal on a resource, use that resource's `add-iam-policy-binding` sub-command with the `--member` and `--role` flags.
    
    
    gcloud compute RESOURCE_TYPE add-iam-policy-binding RESOURCE_NAME \
        --member='PRINCIPAL' \
        --role='ROLE'
    

Replace the following:

  * `RESOURCE_TYPE`: the type of resource. Valid values include: 
    * `disks`
    * `images`
    * `instances`
    * `instance-templates`
    * `machine-images`
    * `reservations`
    * `sole-tenancy node-groups`
    * `sole-tenancy node-templates`
    * `snapshots`
  * `RESOURCE_NAME`: the name of the resource. For example, `my_instance`.
  * `PRINCIPAL`: a valid identity for the principal that you want to grant the role. Must be of the form `user|group|serviceAccount:EMAIL_ADDRESS` or `domain:DOMAIN_ADDRESS`. For example: 
    * `user:test-user@gmail.com`
    * `group:admins@example.com`
    * `serviceAccount:test123@example.domain.com`
    * `domain:example.domain.com`
  * `ROLE`: the role to assign this principal.



If you are granting access to a resource that is in preview, use a `gcloud beta compute` command instead.

###  REST 

To modify an IAM policy through the API, do the following:

  1. Read the existing policy with the resource's respective `getIamPolicy` method. For example, the following HTTP request reads the IAM policy of a VM:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME:getIamPolicy

Replace the following:

     * `PROJECT_ID`: the project ID of the project this VM belongs to.
     * `ZONE`: the zone of the VM. For regional or global resources, replace `zones/ZONE` with `regions/REGION` or `global`.
     * `VM_NAME`: the name of the VM instance.

Compute Engine returns the current policy in the response.

  2. Edit the policy with a text editor to add or remove principals and their associated roles. For example, to grant the `compute.admin` role to email@example.com, add the following new binding to policy:
         
         {
           "members": [
             "user:email@example.com"
           ],
           "role":"roles/compute.admin"
         }
         

  3. Write the updated policy with `setIamPolicy()`:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME:setIamPolicy

Replace the following:

     * `PROJECT_ID`: the project ID of the project this VM belongs to.
     * `ZONE`: the zone of the VM. For regional or global resources, replace `zones/ZONE` with `regions/REGION` or `global`.
     * `VM_NAME`: the name of the VM instance.

In the body of the request, provide the updated IAM policy from the previous step.




## Revoking access to resources

As a best practice, after principals no longer need access to your Compute Engine resources, revoke their access.

###  Console 

  1. In the Google Cloud console, go to the respective resource page for which you want to add permissions. 
     * For instances, go to the [VM instances page](https://console.cloud.google.com/compute/instances).
     * For zonal and regional disks, go to the [Disks page](https://console.cloud.google.com/compute/disks).
     * For snapshots, go to the [Snapshots page](https://console.cloud.google.com/compute/snapshots).
     * For images, go to the [Images page](https://console.cloud.google.com/compute/images).
     * For instance groups, go to the [Instance groups page](https://console.cloud.google.com/compute/instanceGroups).
     * For instance templates, go to the [Instance templates page](https://console.cloud.google.com/compute/instanceTemplates).
     * For machine images, go to the [Machine images page](https://console.cloud.google.com/compute/machineImages).
     * For reservations, go to the [Reservations page](https://console.cloud.google.com/compute/reservations).
     * For sole-tenant nodes, go to the [Sole-tenant nodes page](https://console.cloud.google.com/compute/soleTenancy).
  2. Select the checkboxes next to the resources you want to update.
  3. Complete the following steps based on the resource page. 
     * For VM instances, click person **Permissions**.
     * For all other resources, complete the following: 
       1. Check if the info panel is visible. If it is not visible, click **Show info panel**.
       2. Select the **Permissions** tab.
  4. Click the role card from which you want to remove principals. This expands the card and shows users with that role for that resource.
  5. To remove a principal from that role, click delete **Delete**.



###  gcloud 

To remove a role from a principal for a resource, use the resource's `remove-iam-policy-binding` sub-command with the `--member` and `--role` flags.
    
    
    gcloud compute RESOURCE_TYPE remove-iam-policy-binding RESOURCE_NAME \
        --member='MEMBER' \
        --role='ROLE'
    

Replace the following:

  * `RESOURCE_TYPE`: type of resource. Valid values include: 
    * `disks`
    * `images`
    * `instances`
    * `instance-templates`
    * `machine-images`
    * `reservations`
    * `sole-tenancy node-groups`
    * `sole-tenancy node-templates`
    * `snapshots`
  * `RESOURCE_NAME`: name of the resource. For example, `my_instance`.
  * `PRINCIPAL`: a valid identity for the principal. Must be of the form `user|group|serviceAccount:EMAIL_ADDRESS` or `domain:DOMAIN_ADDRESS`. For example: 
    * `user:test-user@gmail.com`
    * `group:admins@example.com`
    * `serviceAccount:test123@example.domain.com`
    * `domain:example.domain.com`
  * `ROLE`: role from which you want to remove the principal.



If you are revoking access to a resource that is in preview, use a `gcloud beta compute` command instead.

###  REST 

To modify an IAM policy directly through the API, do the following:

  1. Read the existing policy with the resource's respective `getIamPolicy` method. For example, the following HTTP request reads the IAM policy of a VM:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME:getIamPolicy

Replace the following:

     * `PROJECT_ID`: the project ID of the project this VM belongs to.
     * `ZONE`: the zone of the VM. For regional or global resources, replace `zones/ZONE` with `regions/REGION` or `global`.
     * `VM_NAME`: the name of the VM instance.

Compute Engine returns the current policy in the response.

  2. Edit the policy with a text editor to remove members from the associated roles. For example, remove email@example.com from the `compute.admin` role:
         
         {
           "members": [
             "user:owner@example.com"
           ],
           "role":"roles/compute.admin"
         }
         

  3. Write the updated policy with `setIamPolicy()`:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME:setIamPolicy

Replace the following:

     * `PROJECT_ID`: the project ID of the project this VM belongs to.
     * `ZONE`: the zone of the VM. For regional or global resources, replace `zones/ZONE` with `regions/REGION` or `global`.
     * `VM_NAME`: the name of the VM instance.

In the body of the request, provide the updated IAM policy from the previous step.




## Testing whether a caller has permissions

If you don't know what permissions an identity has, use the `testIamPermissions` API method to check which permissions are available to an identity.

The method takes a resource URL and a set of permissions as input parameters, and returns the set of permissions that the caller is allowed. You can use this method on any of the supported resources.

Typically, `testIamPermissions` is intended for integration with your proprietary software, such as a customized graphical user interface. You typically don't call `testIamPermissions` if you're using Google Cloud directly to manage permissions.

For example, if you are building a GUI on top of the Compute Engine API and your GUI has a "start" button that starts an instance, you could call `compute.instances.testIamPermissions()` to determine whether the button should be enabled or disabled.

To test whether a caller has specific permissions on a resource:

  1. Send a request to the resource and include in the request body a list of permissions to check for.

For example, on an instance, you might check for `compute.instances.start`, `compute.instances.stop`, and `compute.instances.delete`.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/testIamPermissions
             {
               "permissions": [
                 "compute.instances.start",
                 "compute.instances.stop",
                 "compute.instances.delete"
                ]
             }

  2. The request returns the permissions that are enabled for the caller.
         
         {
           "permissions": [
             "compute.instances.start",
             "compute.instances.stop"
           ]
         }
         




## Modifying resource access for multiple members

If you want to modify access to Compute Engine resources for multiple members simultaneously, review recommendations on how to [modify an IAM policy programmatically](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#programmatic).

## What's next

  * Learn how to [manage access to custom images](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images) with IAM.
  * Learn more about [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts).
  * Learn more about [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).
  * Learn more about the permissions that are included in [predefined Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam#iam_roles).
  * Learn how to create and manage [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
