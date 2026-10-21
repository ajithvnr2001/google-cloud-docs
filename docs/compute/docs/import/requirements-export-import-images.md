---
url: https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images/
title: Prerequisites for importing and exporting VM images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:13.232883+00:00
---

# Prerequisites for importing and exporting VM images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Prerequisites for importing and exporting VM images Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

The image import feature on Compute Engine is being moved to Migrate to Virtual Machines. We recommend that you use the new [image import feature on Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import) to import your virtual disks to Google Cloud. 

This document describes the prerequisites for importing and exporting images on Compute Engine.

You can share virtual machine (VM) instances, virtual disk files, and machine images from other cloud environments or from your on-premises environment by importing and exporting images from Cloud Storage. The following checklist summarizes the requirements that you need to meet before you import and export images:

  1. Set up access to a Cloud Storage bucket
  2. Grant required roles to your user account
  3. Grant required roles to the Cloud Build service account
  4. Grant required roles to the Compute Engine service account
  5. Configure VPC Service Controls



## Before you begin

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




## Set up access to a Cloud Storage bucket

You must have access to a Cloud Storage bucket that the import or export tool can use. If you don't have a Cloud Storage bucket, see [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

To set up access to your Cloud Storage bucket, see Grant required roles to your account and Compute Engine service account.

  * If you're exporting an image, the export tool uploads the image to the Cloud Storage bucket.

  * If you're importing an image, you must first upload the image to the Cloud Storage bucket. The import tool downloads the file from the Cloud Storage bucket to Compute Engine, and then the tool creates an image in Compute Engine from that disk file.




## Grant required IAM roles

The VM image import and export tool requires the following accounts to perform the operation on its behalf:

  * **User account.** The account from which you're running the import and export commands.
  * **Cloud Build service account.** A default Cloud Build service account that is created when the import or export tool enables the Cloud Build API.
  * **Compute Engine service account.** A default or custom Compute Engine service account that is required for the import and export workflow.



### Grant required roles to your user account

To import or export images, your user account requires the following roles:

  * Storage Admin role (`roles/storage.admin`) 
  * Viewer role (`roles/viewer`) 
  * Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`) 
  * Cloud Build Editor role (`roles/cloudbuild.builds.editor`) 



###  Console 

  1. Go to the **IAM & Admin** page for the project or organization.

[Go to IAM & Admin](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your account and click edit **Edit**.

  3. In the **Select a role** list, select the following roles:

     * **Cloud Storage** > **Storage Admin**
     * **Project** > **Viewer**
     * **Resource Manager** > **Project IAM Admin**
     * **Cloud Build** > **Cloud Build Editor**
  4. Save your changes.




###  gcloud 

In the following steps, you use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) to grant the required roles at the project level.

  1. Grant the `roles/storage.admin` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='MEMBER' \
           --role='roles/storage.admin'
         

Replace the following:

     * `PROJECT_ID`: the [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for your project
     * `MEMBER`: the account that runs the import and export commands—for example, `user:export-user@gmail.com`
  2. Grant the `roles/viewer` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='MEMBER' \
           --role='roles/viewer'
         

  3. Grant the `roles/resourcemanager.projectIamAdmin` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='MEMBER' \
           --role='roles/resourcemanager.projectIamAdmin'
         

  4. Grant the `roles/cloudbuild.builds.editor` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='MEMBER' \
           --role='roles/cloudbuild.builds.editor'
         




###  REST 

  1. Read the existing policy with the resource's `getIamPolicy` method. For projects, use the [`projects.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy).
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy
         

Replace `PROJECT_ID` with the project ID—for example, `my-project-1`.

  2. To grant the required roles to your account, edit the policy with a text editor.

For example, to grant the required role to your account `user:export-user@gmail.com`, add the following binding to the policy:
         
         {
            {
              "role":"roles/storage.admin",
              "member":[
                "user:export-user@gmail.com"
              ]
            }
            {
              "roles":"roles/viewer",
              "member":[
                "user:export-user@gmail.com"
              ]
            }
            {
              "roles":"roles/resourcemanager.projectIamAdmin",
              "member":[
                "user:export-user@gmail.com"
              ]
            }
            {
              "roles":"roles/cloudbuild.builds.editor",
              "member":[
                "user:export-user@gmail.com"
              ]
            }
         }
         

  3. To write the updated policy, use the `setIamPolicy` method.

For example, to set a policy at the project level, use the [`project.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
         




### Grant required roles to the Cloud Build service account

When you use the Google Cloud console or the gcloud CLI to import or export images for the first time, the tool attempts to enable the Cloud Build API and grant the required roles to the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).

The service account used for Cloud Build depends on whether you used [Cloud Build on the project before May 2024](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). If yes, the legacy Cloud Build service account is used for future builds. Otherwise, the default Compute Engine service account is used.

  * Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`)
  * Service Account User role (`roles/iam.serviceAccountUser`)
  * Compute Admin role (`roles/compute.admin`) 

To avoid granting the Compute Admin role, you can [ create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role) with the following Compute Engine IAM permissions and [grant it to the Cloud Build service account](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access): 

#### Permissions required for the custom role

The Cloud Build service account must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 
    * `compute.disks.create`
    * `compute.disks.delete`
    * `compute.disks.get`
    * `compute.disks.getIamPolicy`
    * `compute.disks.list`
    * `compute.disks.resize`
    * `compute.disks.setLabels`
    * `compute.disks.use`
    * `compute.disks.useReadOnly`
    * `compute.images.create`
    * `compute.images.get`
    * `compute.images.getFromFamily`
    * `compute.images.getIamPolicy`
    * `compute.images.list`
    * `compute.images.useReadOnly`
    * `compute.instances.attachDisk`
    * `compute.instances.create`
    * `compute.instances.delete`
    * `compute.instances.detachDisk`
    * `compute.instances.get`
    * `compute.instances.getSerialPortOutput`
    * `compute.instances.list`
    * `compute.instances.setLabels`
    * `compute.instances.setMetadata`
    * `compute.instances.setServiceAccount`
    * `compute.machineTypes.list`
    * `compute.networks.list`
    * `compute.projects.get`
    * `compute.subnetworks.list`
    * `compute.subnetworks.use`
    * `compute.subnetworks.useExternalIp`
    * `compute.zoneOperations.get`
    * `compute.zones.list`
  * Compute Network User role (`roles/compute.networkUser`) 

This role is required only when you import or export images that use Shared VPC.

In the Shared VPC project, grant the Compute Network User role to the Cloud Build service account that is located in the project where you import or export images. 




However, you can manually grant these roles to ensure that the required permissions are in effect:

###  Console 

  1. After you enable the Cloud Build API, go to the **IAM & Admin** page for the project or organization.

[Go to IAM & Admin](https://console.cloud.google.com/iam-admin/iam)

  2. Locate the Cloud Build service account and click edit **Edit**.

  3. If the required roles are not listed, do the following:

     1. Click add **Add another role**.
     2. In the **Select a role** list, select the required roles that you want to add:

        * **Service Account** > **Service Account Token Creator**
        * **Service Account** > **Service Account User**
        * **Compute Engine** > **Compute Admin**

Alternatively, you can select the **Custom** role. See [Permissions required for the custom role](https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images#expandable-1) earlier in this document.

     3. Click **Save** to save the changes.

  4. Optional: If you're importing or exporting images that use Shared VPC, select the Compute Network User role in the Shared VPC project:

     1. From the project selector at the top of the console, select the Shared VPC host project.
     2. On the **IAM & Admin** page, click person_add **Grant access**.
     3. In the **New principals** field, enter the email address of the Cloud Build service account: 
            
            PROJECT_NUMBER@cloudbuild.gserviceaccount.com'
             

Replace `PROJECT_NUMBER` with the unique number of the project where you import or export images.
     4. In the **Select a role** list, select **Compute Engine** > **Compute Network User** role.
     5. Click **Save** to save the changes.



###  gcloud 

In the following steps, you use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) to grant the required roles at the project level.

  1. Grant the `roles/compute.admin` role to the Cloud Build service account. To avoid granting the `roles/compute.admin` role, you can create a custom role with the required permissions and then grant that role to the Cloud Build service account. See [Permissions required for the custom role](https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images#expandable-1) earlier in this document.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member='serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com' \
            --role='roles/compute.admin'
         

Replace the following:

     * `PROJECT_ID`: the [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for your project
     * `PROJECT_NUMBER`: the [Google Cloud project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for your project
  2. Grant the `roles/iam.serviceAccountUser` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member='serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com' \
            --role='roles/iam.serviceAccountUser'
         

  3. Grant the `roles/iam.serviceAccountTokenCreator` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member='serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com' \
            --role='roles/iam.serviceAccountTokenCreator'
         

  4. Optional: If you're exporting or importing images that use Shared VPC, grant the `roles/compute.networkUser` role:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
            --member='serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com' \
            --role='roles/compute.networkUser'
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the host project where the Shared VPC is located
     * `PROJECT_NUMBER`: the unique number of the project where you import or export images



###  REST 

  1. Read the existing policy with the resource's `getIamPolicy` method. For projects, use the [`projects.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy).
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy
         

Replace `PROJECT_ID` with the project ID—for example, `my-project-1`.

  2. To grant the required roles to your account, edit the policy with a text editor.

For example, to grant the required roles to `serviceAccount:12345@cloudbuild.gserviceaccount.com`, add the following binding to the policy:
         
         {
            {
              "role":"roles/compute.admin",
              "member":[
                "serviceAccount:12345@cloudbuild.gserviceaccount.com"
              ]
            }
            {
              "roles":"roles/iam.serviceAccountUser",
              "member":[
                "serviceAccount:12345@cloudbuild.gserviceaccount.com"
              ]
            }
           {
              "roles":"roles/iam.serviceAccountTokenCreator",
              "member":[
                "serviceAccount:12345@cloudbuild.gserviceaccount.com"
              ]
            }
         }
         

To avoid granting the `roles/compute.admin` role, you can create a custom role with the required permissions and then grant that role to the Cloud Build service account. See [Permissions required for the custom role](https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images#expandable-1) earlier in this document.

  3. Optional: If you're exporting or importing images that use Shared VPC, grant the `roles/compute.networkUser` role in the Shared VPC project.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/HOST_PROJECT_ID:getIamPolicy
         

Replace `HOST_PROJECT_ID` with the ID of the Shared VPC project.

Add the following IAM binding to the Cloud Build service account:
         
         {
            {
              "roles":"roles/compute.networkUser",
              "member":[
                "serviceAccount:12345@cloudbuild.gserviceaccount.com"
              ]
            }
         }
         

  4. To write the updated policy, use the `setIamPolicy` method.

For example, to set a policy at the project level, use the [`project.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
         




For more information on managing access to resources, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console).

**Note:** By default, when the Cloud Build API is enabled, the Cloud Build Service Account role (`roles/cloudbuild.builds.builder`) is granted to the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account). If this role is removed, importing and exporting images might fail.

### Grant required roles to the Compute Engine service account

When you use the Google Cloud console or the gcloud CLI to import or export images for the first time, the tool attempts to grant the required roles to the [default Compute Engine service account](https://docs.cloud.google.com/iam/docs/service-account-types#default).

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Your Compute Engine service account must have the following roles:

  * Compute Storage Admin role (`roles/compute.storageAdmin`): required for both exporting and importing VM images 
  * Storage Object Viewer role (`roles/storage.objectViewer`): required for importing VM images 
  * Storage Object Admin role (`roles/storage.objectAdmin`): required for exporting VM images 
  * Storage Admin role (`roles/storage.admin`): required for exporting VM images 



###  Console 

  1. Go to the **IAM & Admin** page for the project or organization.

[Go to IAM & Admin](https://console.cloud.google.com/iam-admin/iam)

  2. Locate the Compute Engine service account and click edit **Edit**.

  3. In the **Select a role** list, select the following roles:

     * **Compute Engine** > **Compute Storage Admin**
     * **Cloud Storage** > **Storage Object Viewer**
     * **Cloud Storage** > **Storage Object Admin**
  4. Save your changes.




###  gcloud 

In the following steps, you use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) to grant the required roles at the project level.

  1. Grant the `roles/compute.storageAdmin` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com' \
           --role='roles/compute.storageAdmin'
         

  2. If you're importing an image, grant the `roles/storage.objectViewer` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com' \
           --role='roles/storage.objectViewer'
         

  3. If you're exporting an image, grant the `roles/storage.objectAdmin` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com' \
           --role='roles/storage.objectAdmin'
         




###  REST 

  1. Read the existing policy with the resource's `getIamPolicy` method. For projects, use the [`projects.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy).
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy
         

Replace `PROJECT_ID` with the project ID—for example, `my-project-1`.

  2. To grant the required roles to your account, edit the policy with a text editor.

For example, to grant the required roles to `serviceAccount:12345-compute@developer.gserviceaccount.com` for importing an image, add the following binding to the policy:
         
         {
            {
              "role":"roles/compute.storageAdmin",
              "member":[
                "serviceAccount:12345-compute@developer.gserviceaccount.com"
              ]
            }
            {
              "roles":"roles/storage.objectViewer",
              "member":[
                "serviceAccount:12345-compute@developer.gserviceaccount.com"
              ]
            }
         }
         

  3. To write the updated policy, use the `setIamPolicy` method.

For example, to set a policy at the project level, use the [`project.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). In the body of the request, provide the updated IAM policy from the previous step.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy
         




If you don't want to use the default Compute Engine service account, you can specify a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-created) using the `--compute-service-account` flag in the `gcloud` import and export commands. For more information on using custom Compute Engine service account, see the following resources:

  * [Importing virtual disks with custom service accounts](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks#custom-service-account)
  * [Importing virtual appliances with custom service accounts](https://docs.cloud.google.com/compute/docs/import/import-ovf-files#custom-service-account)
  * [Importing machine images from virtual appliances with custom service accounts](https://docs.cloud.google.com/compute/docs/machine-images/import-machine-from-virtual-appliance#custom-service-account)
  * [Exporting custom images with custom service accounts](https://docs.cloud.google.com/compute/docs/images/export-image#custom-service-account)



## Configure VPC Service Controls

If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to protect your projects, you must add an egress rule to the `compute-image-import` (number `71462206840`) project. To follow the principle of least privilege, we recommend that you only allow the `artifactregistry.googleapis.com` service with the following methods: 

  * `artifactregistry.repositories.downloadArtifacts`
  * `artifactregistry.tags.get`
  * `artifactregistry.tags.list`
  * `artifactregistry.versions.get`



For more information, see [VPC Service Controls limitations](https://docs.cloud.google.com/compute/docs/images/export-image#limitations-vpc-sc).

## What's next

  * [Export custom images to Cloud Storage](https://docs.cloud.google.com/compute/docs/images/export-image).
  * [Share your images](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images) across projects.
  * [Choose an import method](https://docs.cloud.google.com/compute/docs/import).
  * [Importing virtual disks](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks)
  * [Importing virtual appliances](https://docs.cloud.google.com/compute/docs/import/import-ovf-files)
  * [Importing machine images from virtual appliances](https://docs.cloud.google.com/compute/docs/machine-images/import-machine-from-virtual-appliance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
