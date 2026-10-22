---
url: https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images/
title: Manage access to custom images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:12.683402+00:00
---

# Manage access to custom images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage access to custom images Stay organized with collections  Save and categorize content based on your preferences. 

To let users create, delete, use, or share your custom images, you must grant them the appropriate Identity and Access Management (IAM) roles. This document describes the required IAM permissions for creating and managing custom images and how to give them to users.

For general information about granting access to Compute Engine resources, see [Managing access to Compute Engine resources](https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources). For information about IAM, read the [IAM documentation](https://docs.cloud.google.com/iam/docs).

## Before you begin

  * Read the [IAM](https://docs.cloud.google.com/iam) documentation.
  * Read about [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam#iam_roles), in particular, the Compute Image User role (`roles/compute.imageUser`).
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

To get the permissions that you need to manage access to custom images, ask your administrator to grant you the following IAM roles: 

  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage access to custom images. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage access to custom images:

  * To give users or service accounts the permissions needed to create, share custom images: 
    * `resourcemanager.projects.getIamPolicy` on the project
    * `resourcemanager.projects.setIamPolicy` on the project
  * To give users or service accounts the permissions needed to delete custom images: 
    * `resourcemanager.projects.getIamPolicy` on the project
    * `resourcemanager.projects.setIamPolicy` on the project
    * `compute.images.getIamPolicy`on the image
    * `compute.images.setIamPolicy` on the image
  * To revoke user or service account access to custom images: 
    * `resourcemanager.projects.getIamPolicy` on the project
    * `resourcemanager.projects.setIamPolicy` on the project
  * To create an instance using a shared image: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

On images, you can't grant roles to the special member type [`allUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allusers).

## Give permission to create custom images

You can give users the ability to create [custom images](https://docs.cloud.google.com/compute/docs/images#custom_images) in your organization or project.

Compute Engine offers the predefined [Compute Storage Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.storageAdmin) (`roles/compute.storageAdmin`) that you can assign to users so that they can create, delete, and manage storage-related resources, including images, disks, and snapshots. If you need a role that allows for only image creation, you must create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role). In your custom role, include the following permissions:

  * `compute.images.create` to create new images
  * `compute.images.list` to list images in the project
  * `compute.disks.use` if the image is created from a disk
  * `compute.disks.list` if users need to list all disks in a project



If you give a user the ability to create custom images at the organization level, the user can create custom images for any project within the organization.

###  Console 

  1. In the Google Cloud console, go to the **IAM** page for the project or organization.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. To add a new member, click person_add **Grant access**.

  3. In the **New principals** field, enter the email address of the identity that you want to grant access to.

For example:

     * Google Account email: `test-user@gmail.com`
     * Google group: `admins@googlegroups.com`
     * Identity from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`
     * Service account: `server@example.gserviceaccount.com`
     * Google Workspace domain: `example.com`
  4. In the **Select a role** list, select **Compute Engine > Compute Storage Admin**, or select a custom role if you created one.

  5. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  6. Save your changes.




###  gcloud 

To grant the `roles/compute.storageAdmin` role at an organization level, use the [`gcloud organizations add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding):
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member='MEMBER' \
        --role='roles/compute.storageAdmin'
    

To grant the `roles/compute.storageAdmin` role at a project level, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='MEMBER' \
        --role='roles/compute.storageAdmin'
    

Replace the following:

  * `ORGANIZATION_ID` or `PROJECT_ID`: the organization ID or the project ID—for example, `my-organization-1` or `my-project-1`
  * `MEMBER`: a valid identity to which you want to grant the role

For example:

    * Google Account email: `user:user@gmail.com`
    * Google group: `group:admins@googlegroups.com`
    * Identity from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`
    * Service account: `serviceAccount:server@example.gserviceaccount.com`
    * Google Workspace domain: `domain:example.com`



###  REST 

  1. Read the existing policy with the resource's `getIamPolicy` method. For projects, use the [`projects.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy).
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy
         

Replace `PROJECT_ID` with the project ID—for example, `my-project-1`.

For organizations, use the [`organizations.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/getIamPolicy).
         
         POST https://cloudresourcemanager.googleapis.com/v1/organizations/ORGANIZATION_ID:getIamPolicy
         

Replace `ORGANIZATION_ID` with the organization ID—for example, `123456578920`.

Compute Engine returns the current policy in the response.

  2. To add or remove members and their associated roles, edit the policy with a text editor. Use the following format to add members:

     * `user:test-user@gmail.com`
     * `group:admins@example.com`
     * `serviceAccount:test123@example.domain.com`
     * `domain:example.domain.com`

For example, to grant the `roles/compute.storageAdmin` role to `group:admins@example.com`, add the following binding to the policy:
    
    {
     "members": [
       "group:admins@example.com"
     ],
     "role":"roles/compute.storageAdmin"
    }
    

  3. Write the updated policy by using the `setIamPolicy` method.

For example, to set a policy at the project level, use the [`project.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
         

Replace the `PROJECT_ID` with the project ID.




## Give permissions to delete custom images

Depending on your needs, you can give users permission to do the following:

  * Delete a specific image
  * Delete images owned by a specific project
  * Delete images for any project in an organization



Giving permission at the project level lets users delete all images owned by that project. Giving permission at the organization level lets the user delete any images owned by that organization, regardless of the project.

Compute Engine offers the predefined [Compute Storage Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.storageAdmin) (`roles/compute.storageAdmin`) that you can assign to users so that they can create, delete, and manage storage-related resources, including images, disks, and snapshots. If you need a role that allows for only image deletion, you must create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role). In your custom role, include the following permissions:

  * `compute.images.delete` to delete images
  * `compute.images.list` if users need to list images in the project or organization
  * `compute.images.get` to get the images




###  Console 

To give permission to delete specific images, do the following:

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Select the images that you want to give permissions to.

  3. To expand the permissions column, click **Show info panel**.

  4. To add one or more members, click **Add principal**.

  5. In the **New principals** field, enter the email address of the identity you want to share the image with.

For example:

     * Google Account email: `test-user@gmail.com`
     * Google group: `admins@googlegroups.com`
     * Identity from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`
     * Service account: `server@example.gserviceaccount.com`
     * Google Workspace domain: `example.com`
  6. In the **Role** list, hold the pointer over **Compute Engine** and select **Storage Admin** , or select a custom role from the **Custom** list.

  7. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  8. Save your changes.




To give permission to delete images for a project or organization, do the following:

  1. Go to the **IAM** page for the project or organization.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click person_add **Grant access**.

  3. In the **New principals** field, enter the email address of the identity you want to grant access to. For example:

     * Google Account email: `test-user@gmail.com`
     * Google group: `admins@googlegroups.com`
     * Identity from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`
     * Service account: `server@example.gserviceaccount.com`
     * Google Workspace domain: `example.com`
  4. In the **Role** list, hold the pointer over **Compute Engine** and select **Storage Admin** , or select a custom role from the **Custom** list.

  5. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  6. Save your changes.




###  gcloud 

To give permissions to delete images at the organization level, use the [`gcloud organizations add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding):
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member='MEMBER' \
        --role='ROLE'
    

To give permissions to delete images on a project level, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='MEMBER' \
        --role='ROLE'
    

To give permissions to delete a specific image, use the [`gcloud compute images add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/add-iam-policy-binding):
    
    
    gcloud compute images add-iam-policy-binding IMAGE_NAME \
        --member='MEMBER' \
        --role='ROLE'
    

Replace the following:

  * `ORGANIZATION_ID` or `PROJECT_ID` or `IMAGE_NAME`: the 12-digit numeric organization ID, the project ID, or the image name—for example, `123456578920`, `my-project-1`, or `my-custom-image`
  * `MEMBER`: a valid identity to which you want to grant the role

For example:

    * Google Account email: `user:user@gmail.com`
    * Google Group: `group:admins@googlegroups.com`
    * Identity from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`
    * Service account: `serviceAccount:server@example.gserviceaccount.com`
    * Google Workspace domain: `domain:example.com`
  * `ROLE`: the role to assign to this identity—for example, the `roles/compute.storageAdmin` role, or a custom role such as `roles/customImageDeletionRole`




###  REST 

  1. Read the existing policy with the resource's respective `getIamPolicy` method. For projects, use the [`projects.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy): 
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy
         

Replace `PROJECT_ID` with the project ID.

For organizations, use the [`organizations.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/getIamPolicy):
         
         POST https://cloudresourcemanager.googleapis.com/v1/organizations/ORGANIZATION_ID:getIamPolicy
         

Replace `ORGANIZATION_ID` with the 12-digit numeric organization ID.

For a specific image, use the [`images.getIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getIamPolicy):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:getIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID
     * `IMAGE_NAME`: the name of the image

Compute Engine returns the current policy in the response.

  2. To add or remove members and their associated roles, you can edit the policy with a text editor. Use the following format to add members:

     * `user:test-user@gmail.com`
     * `group:admins@example.com`
     * `serviceAccount:test123@example.domain.com`
     * `domain:example.domain.com`

For example, to grant the `roles/compute.storageAdmin` role to `user:test-email@example.com`, add the following binding to the policy:
    
    {
     "members": [
       "user:test-email@example.com"
     ],
     "role":"roles/compute.storageAdmin"
    }
    

  3. Write the updated policy by using the `setIamPolicy` method.

For example, to set a policy at a project level, use the [`project.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
         

Replace `PROJECT_ID` with the project ID.




## Give permissions to share custom images within an organization

If your project belongs to an organization, the organization can have several other projects with varying levels of access to other projects. When you create custom images, you can share these images with other users from other projects within the organization.

Compute Engine offers the following predefined IAM roles that you can use for image management:

  * Compute Image User (`roles/compute.imageUser`): permission to list, read, and use images in your requests, without having other permissions on the image
  * Compute Storage Admin (`roles/compute.storageAdmin`): permissions to create, modify, and delete disks, images, and snapshots



Alternatively, you can also create your own [custom IAM role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

As a best practice, we recommend that you keep all your custom images in a single project dedicated to host these images. This practice improves the management of those images, and lets you grant specific teams access to only the images that they need. You can also grant teams access to the entire image project, but because team access to the entire image project violates the principle of least privilege, we do not recommend it.

The example below shows how to add a group so that users of that group have access to the image.

###  Console 

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Select the image that you want to share with other users.

  3. To expand the permissions column, click **Show info panel**.

  4. To add one or more members, click **Add principal**.

  5. In the **New principals** field, enter the email address of the identity you want to share the image with.

For example:

     * Google Account email: `test-user@gmail.com`
     * Google group: `admins@googlegroups.com`
     * Identity from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`
     * Service account: `server@example.gserviceaccount.com`
     * Google Workspace domain: `example.com`
  6. In the **Role** list, hold the pointer over **Compute Engine** and select **Image User** or **Storage Admin** , or select a custom role.

  7. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  8. Save your changes.




To let users launch shared custom images from the Google Cloud console, grant users the Viewer IAM role (`roles/viewer`) for the image project. Granting this role helps ensure that the shared images appear in the image selection list.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click person_add **Grant access**.

  3. In the **New principals** field, enter the email address of the identity you want to share the image with. For example:

     * Google Account email: `test-user@gmail.com`
     * Google group: `admins@googlegroups.com`
     * Identity from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`
     * Service account: `server@example.gserviceaccount.com`
     * Google Workspace domain: `example.com`
  4. In the **Role** list, hold the pointer over **Project** and select **Viewer**.

  5. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  6. Save your changes.




###  gcloud 

To update the IAM policy for a specific image, use the [`gcloud compute images add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/add-iam-policy-binding):
    
    
    gcloud compute images add-iam-policy-binding IMAGE_NAME \
        --member='MEMBER' \
        --role='ROLE'
    

Replace the following:

  * `IMAGE_NAME`: the name of the image—for example, `custom-centos-8`
  * `MEMBER`: a valid identity for which you want to grant the role

For example:

    * `user:test-user@gmail.com`
    * `group:admins@example.com`
    * `serviceAccount:test123@example.domain.com`
    * `domain:example.domain.com`
  * `ROLE`: the role to assign this identity to, such as `roles/compute.imageUser`, `roles/compute.storageAdmin`, or a custom role




Optionally, to let users see these shared images in their `images.list` requests, grant users the Viewer IAM role (`roles/viewer`) for the image project by using the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding). If you don't need your users to be able to view the list of shared images, you can skip this step.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='MEMBER' \
        --role='roles/viewer'
    

###  REST 

  1. Read the existing policy with the resource's `getIamPolicy` method. For example, to get the policy on a specific image, use the [`images.getIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getIamPolicy):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:getIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the project this image belongs to
     * `IMAGE_NAME`: the name of the image

Compute Engine returns the current policy in the response.

  2. To add or remove members and their associated roles, edit the policy with a text editor. Use the following format to add members:

     * `user:test-user@gmail.com`
     * `group:admins@example.com`
     * `serviceAccount:test123@example.domain.com`
     * `domain:example.domain.com`

For example, to grant `roles/compute.imageUser` to `test-email@example.com`, add the following binding to the policy:
    
    {
     "members": [
       "user:test-email@example.com"
     ],
     "role":"roles/compute.imageUser"
    }
    

  3. Write the updated policy by using the `setIamPolicy` method. For example, to set policy on a specific image, use the [`project.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:setIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the project this image belongs to
     * `IMAGE_NAME`: the name of the image



Optionally, to let users see these shared images in their `images.list` requests, grant users the Viewer IAM role (`roles/viewer`) for the image project by using the [`projects.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). If you don't need your users to be able to view the list of shared images, you can skip this step.
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
    

## Give permissions to share custom images between organizations

Creating a catalog of custom images can be useful for sharing images with partners, users, or contractors that are outside of your organization. To share your images with users outside of the organization, add them as Image Users to your project:

###  Console 

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Select the image that you want to share with other users.

  3. To expand the permissions column, click **Show info panel**.

  4. To add one or more members, click **Add principal**.

  5. In the **New principals** field, enter the email address of the group you want to share the image with. For example, `admins@example.com`.

  6. In the **Role** list, hold the pointer over **Compute Engine** and select **Compute Image User**.

  7. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  8. Save your changes.




To let users launch shared custom images from the Google Cloud console, grant users the Viewer IAM role (`roles/viewer`) for the image project. Granting this role helps ensure that the shared images appear in the image selection list.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click person_add **Grant access**.

  3. In the **New principals** field, enter the email address of the identity you want to share the image with. For example, `admins@example.com`.

  4. In the **Role** list, hold the pointer over **Project** and select **Viewer**.

  5. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  6. Save your changes.




###  gcloud 

To grant the `roles/compute.imageUser` role to users, use the [`gcloud compute images add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/add-iam-policy-binding):
    
    
    gcloud compute images add-iam-policy-binding IMAGE_NAME \
        --member='MEMBER' \
        --role='roles/compute.imageUser'
    

Replace the following:

  * `IMAGE_NAME`: the name of the image—for example, `custom-centos-8`
  * `MEMBER`: a valid identity for which you want to grant the role—for example, `group:admins@example.com`



Optionally, to let users see these shared images in their `images.list` requests, grant users the Viewer IAM role (`roles/viewer`) for the image project by using the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding). If you don't need your users to be able to view the list of shared images, you can skip this step.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='MEMBER' \
        --role='roles/viewer'
    

###  REST 

  1. Read the existing policy with the resource's `getIamPolicy` method. For example, to get the policy on a specific image, use the [`images.getIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getIamPolicy):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:getIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the project this image belongs to
     * `IMAGE_NAME`: the name of the image

Compute Engine returns the current policy in the response.

  2. To add or remove members and their associated roles, you can edit the policy with a text editor. Use the following format to add members:

     * `user:test-user@gmail.com`
     * `group:admins@example.com`
     * `serviceAccount:test123@example.domain.com`
     * `domain:example.domain.com`

For example, to grant `roles/compute.imageUser` to `test-user@example.com`, add the following binding to the policy:
    
    {
      "members": [
        "user:test-user@example.com"
      ],
      "role":"roles/compute.imageUser"
    }
    

  3. Write the updated policy by using the `setIamPolicy` method. For example, to set a policy on a specific image, use the [`images.setIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:setIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the project this image belongs to
     * `IMAGE_NAME`: the name of the image

Optionally, to let users see these shared images in their `images.list` requests, grant users the Viewer IAM role (`roles/viewer`) for the image project by using the [`projects.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). If you don't need your users to be able to view the list of shared images, you can skip this step.
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
    




## Give permissions to share custom images publicly

You can share your custom images with all authenticated Compute Engine users, regardless of whether they are part of your organization or project.

You can only share resources, such as images, with all authenticated users; you cannot share projects or organizations with all authenticated users. This restriction, and the resource hierarchy, helps prevent an organization from inadvertently sharing their entire project with all authenticated Compute Engine users.

The following example shows how to grant all authenticated Compute Engine users the Compute Image User role (`roles/compute.imageUser`) to a custom image.

**Caution:** Publicly shared images do not appear in the images list for users. Users must know the image name explicitly. Users cannot rely on getting the information by making an `images.list` request.

###  gcloud 

To make images public, use the [`gcloud compute images add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/add-iam-policy-binding):
    
    
    gcloud compute images add-iam-policy-binding IMAGE_NAME \
        --member='allAuthenticatedUsers' \
        --role='roles/compute.imageUser'
    

Replace `IMAGE_NAME` with the name of the resource—for example, `my_image`.

###  REST 

  1. Read the existing policy with the `getIamPolicy` method. For example, to get the policy on a specific image, use the [`images.getIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getIamPolicy):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:getIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the project this image belongs to
     * `IMAGE_NAME`: the name of the image

Compute Engine returns the current policy in the response.

  2. To add or remove members and their associated roles, edit the policy with a text editor:
         
         {
          "members": [
            "allAuthenticatedUsers"
          ],
          "role":"roles/compute.imageUser"
         }
         

  3. Write the updated policy by using the `setIamPolicy` method. For example, to set a policy on a specific image, use the [`images.setIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:setIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the project this image belongs to
     * `IMAGE_NAME`: the name of the image



## Grant a managed instance group access to images

Compute Engine lets you create groups of instances, either as [managed](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) or [unmanaged](https://docs.cloud.google.com/compute/docs/instance-groups#unmanaged_instance_groups) instance groups. If you create a managed instance group (MIG), Compute Engine uses the [Google APIs Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_account) to call the Compute Engine API and perform actions related to the group, such as recreating unhealthy instances and updating instances.

If you want to create a MIG using an image from another project, grant the Compute Image User role (`roles/compute.imageUser`) to the APIs service account belonging to the project that creates the MIG. For example:

  1. Project A wants to create a MIG using images owned by Project B.
  2. Project B grants Project A's service account the Compute Image User role.
  3. Project A can now use images from Project B to create MIGs.



After granting the Compute Image User role, you can access the image from the other projects by using the console or the image's URL when you create the [instance template](https://docs.cloud.google.com/compute/docs/instance-templates#creating_an_instance_template) for the managed group.

### Get the email address of the service account

  1. In the Google Cloud console, go to the **IAM** page of the project whose service account you want to grant access to.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam/)

  2. If prompted, select your project from the list.

  3. Look for the **Google APIs Service Agent** , which has the email address in the following format:
         
         PROJECT_NUMBER@cloudservices.gserviceaccount.com
         

**Note:** This email address requires the project _number_ , not the project ID. To learn how to identify the project number, see [Identifying projects](https://docs.cloud.google.com/compute/docs/projects#projectids).



After retrieving the email address of the service account, you can go to one of the following sections:

  * Grant a MIG access to all images in a project
  * Grant a MIG access to specific images in a project



### Grant a MIG access to all images in a project

Now that you have the email address of a service account, you can add the address to another project and grant it the Compute Image User role (`roles/compute.imageUser`).

###  Console 

  1. In the Google Cloud console, go to the **IAM** page of the image project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. To add a new member, click person_add **Grant access**.

  3. In the **New principals** field, add the service account email address.

  4. In the **Role** list, hold the pointer over **Compute** and select **Compute Image User**.

  5. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  6. Click **Save**.

  7. Switch back to the service account's project.




You can now [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) based on an image from the image project and [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) based on the instance template.

###  gcloud 

Add a service account from image project using the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='serviceAccount:SERVICE_ACCOUNT_EMAIL' --role='roles/compute.imageUser'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project containing images you want to share
  * `SERVICE_ACCOUNT_EMAIL`: the email of the service account



You can now [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) based on an image from the image project and [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) based on the instance template.

###  REST 

  1. Get the IAM policy of the image project, by using the [`projects.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy):
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy
          

Replace `PROJECT_ID` with the project ID of the image project.

  2. To grant the `roles/compute.imageUser` role to the service account, edit the policy with a text editor:
         
         {
           "bindings": [
              {
               "role": "roles/compute.imageUser",
               "members": [
                 "serviceAccount:SERVICE_ACCOUNT_EMAIL"
               ]
             }
           ]
         }
         

Replace the `SERVICE_ACCOUNT_EMAIL` with the service account email.

  3. Write the updated policy by using the [`projects.setIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
         

Replace `PROJECT_ID` with the product ID of the image project.

You can now [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) based on an image from the image project and [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) based on the instance template.




### Grant a MIG access to specific images in a project

Now that you have the email address of a service account, you can add the address to another project and grant the Compute Image User role (`roles/compute.imageUser`) for certain images.

###  Console 

  1. In the Google Cloud console, go to the **Images** page of the image project.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Select the checkboxes next to the images you want to share.

  3. To expand the permissions column, click **Show info panel**.

  4. In the **Permissions** panel, click **Add principal**.

  5. In the **New principals** field, enter the service account email that you want to share the image with. For example, `test123@example.domain.com`.

  6. In the **Role** list, choose **Compute** and select **Compute Image User**.

  7. Optional: To further control user's access to Google Cloud resources, [add conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add).

  8. Click **Save**.

  9. Switch back to the service account's project.




You can now [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) based on an image from the image project and [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) based on the instance template.

###  gcloud 

To grant a service account access to a specific image, use the [`gcloud compute images add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/add-iam-policy-binding):
    
    
    gcloud compute images add-iam-policy-binding IMAGE_NAME \
        --member='serviceAccount:SERVICE_ACCOUNT_EMAIL' \
        --role='roles/compute.imageUser'
    

Replace the following:

  * `IMAGE_NAME`: the image name you want to share
  * `SERVICE_ACCOUNT_EMAIL`: the email of the service account



You can now [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) based on an image from the image project and [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) based on the instance template.

###  REST 

  1. Get the IAM policy of an image by using the [`images.getIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getIamPolicy):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:getIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the image project
     * `IMAGE_NAME`: the name of the image you want to share
  2. To grant the `roles/compute.imageUser` role to the service account, edit the policy with a text editor:
         
         {
           "bindings": [
              {
               "role": "roles/compute.imageUser",
               "members": [
                 "serviceAccount:SERVICE_ACCOUNT_EMAIL"
               ]
             }
           ]
         }
         

Replace the `SERVICE_ACCOUNT_EMAIL` with the service account email.

  3. Write the updated policy by using the [`images.setIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:setIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID of the image project
     * `IMAGE_NAME`: the name of the image you want to share

You can now [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) based on an image from the image project and [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) based on the instance template.




## Control the use of your shared images and snapshots

After sharing your images with other users, you can control where those users employ those resources within your organization. Set the [`constraints/compute.storageResourceUseRestrictions` constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints) to define the projects where users are permitted to use your storage resources.

You must have permission to modify your organization's policies to set these constraints. For example, the [`resourcemanager.organizationAdmin` role](https://docs.cloud.google.com/resource-manager/docs/access-control-org) has permission to set these constraints.

  1. Find the organization ID for your organization by using the [`gcloud organization list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list):
         
         gcloud organizations list
         

  2. Get the existing policy settings for your organization by using the [`gcloud resource-manager org-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe) command:
         
         gcloud resource-manager org-policies describe \
             compute.storageResourceUseRestrictions \
             --organization ORGANIZATION_ID > org-policy.yaml
         

Replace ORGANIZATION_ID with your 12-digit numeric organization ID.

  3. Open the `org-policy.yaml` file in a text editor and modify the `compute.storageResourceUseRestrictions` constraint. Add the restrictions that you need, or remove the restrictions that you no longer require. When you finish editing the file, save your changes. For example, you might set the following constraint entry in your policy file:
         
         constraint: compute.storageResourceUseRestrictions
         listPolicy:
           allowedValues:
             - under:organization/organization-id
         

**Note:** You can also specify a folder ID using the `under:folder/FOLDER_ID` format to organize all projects into a folder.
  4. Apply the `org-policy.yaml` file to your organization by using the [`gcloud resource-manager org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy) command:
         
         gcloud resource-manager org-policies set-policy \
            --organization=ORGANIZATION_ID org-policy.yaml
         

Replace ORGANIZATION_ID with your 12-digit numeric organization ID.




When you finish configuring the constraints in your organization policy, test those constraints to ensure that they create the restrictions that you want.

## Use images from another project

If someone grants you access to one or more images in another project, you can access these images in the project by specifying the image project in your requests.

For example, to create an instance using a shared image from another project, follow the steps listed in [Create an instance from a shared image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-shared-image).

You can also create boot disk volumes from images in another project. For information about creating a boot disk from an image, see [Creating a standalone boot persistent disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks#creatingrootpdalone).

## Revoke access to shared images

After a user no longer needs access to your Compute Engine resources, revoke their access by using the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Images** page of the image project.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Select the checkboxes next to the images you want to update.

  3. To expand the permissions column, click **Show info panel**.

  4. Expand the role for which you want to remove users.

  5. To remove a user from that role, click delete **Delete**.




###  gcloud 

To remove a user from a role on an image, use the [`gcloud compute images remove-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/remove-iam-policy-binding) with the `--member` and `--role` flags:
    
    
    gcloud compute images remove-iam-policy-binding IMAGE_NAME \
        --member='MEMBER' \
        --role='ROLE'
    

Replace the following:

  * `IMAGE_NAME`: the name of the image—for example, `my_image`
  * `MEMBER`: the identity you want to remove

Must be of the form `user|group|serviceAccount:email` or `domain:domain`. For example:

    * `user:test-user@gmail.com`
    * `group:admins@example.com`
    * `serviceAccount:test123@example.domain.com`
    * `domain:example.domain.com`
  * `ROLE`: the role from which you want to remove the identity




If you are revoking access to a resource that is in beta, use a `gcloud beta compute` command instead.

###  REST 

  1. Read the existing policy with the [`images.getIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getIamPolicy):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/IMAGE_NAME:getIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID this image belongs to
     * `IMAGE_NAME`: the name of the image

Compute Engine returns the current policy in the response.

  2. To remove members and their associated roles, edit the policy with a text editor.

  3. Write the updated policy by using the [`images.setIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/global/images/IMAGE_NAME:setIamPolicy
         

Replace the following:

     * `PROJECT_ID`: the project ID this image belongs to
     * `IMAGE_NAME`: the name of the image



## What's next

  * Read about [IAM](https://docs.cloud.google.com/iam).
  * See a list of [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).
  * Learn about [images](https://docs.cloud.google.com/compute/docs/images).
  * Learn how to [create an instance by using a shared image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-shared-image).
  * Learn how to [create a standalone boot persistent disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks#creatingrootpdalone).
  * Learn how to use this role with your [Deployment Manager deployments](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-images-from-other-projects-for-vm-instances).
  * Apply the principle of least privilege by [granting access to specific Compute Engine resources](https://docs.cloud.google.com/compute/docs/access/granting-access-to-resources) instead of to a whole project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
