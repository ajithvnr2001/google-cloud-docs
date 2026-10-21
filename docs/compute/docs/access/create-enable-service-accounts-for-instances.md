---
url: https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances/
title: Create a VM that uses a user-managed service account \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:53:05.861763+00:00
---

# Create a VM that uses a user-managed service account  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a VM that uses a user-managed service account Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a virtual machine (VM) instance that is configured to use a user-managed service account. A service account is a special kind of account typically used by an application or compute workload to make authorized API calls.

Service accounts are needed for scenarios where a workload, such as a custom application, needs to access Google Cloud resources or perform actions without end-user involvement. For more information about when to use service accounts, see [Best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts). 

If you have applications that need to make calls to Google Cloud APIs, Google recommends that you attach a user-managed service account to the VM on which the application or workload is running. Then, you grant the service account IAM roles, which gives the service account–and, by extension, applications running on the VM–access to Google Cloud resources.

**Note:** When a user connects to a VM, that user can use all of the IAM permissions granted to the service account attached to the VM. 

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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create VMs that use service accounts, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create VMs that use service accounts. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create VMs that use service accounts:

  * To create service accounts: All the permissions in the `iam.serviceAccountCreator` role 
  * To grant permissions to the service account: All the permissions in the `resourcemanager.projectIamAdmin` role 
  * To create VMs: 
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

## Overview

It is recommended that you configure service accounts for your VMs as follows:

  1. Create a new user-managed service account rather than using the Compute Engine default service account, and grant IAM roles to that service account for only the resources and operations that it needs. 
  2. Attach the service account to your VM.
  3. Set the cloud platform (`https://www.googleapis.com/auth/cloud-platform`) scope on your VM. This allows the VM's service account to call the Google Cloud APIs that it has permission to use. 
     * If you specify the service account by using the Google Cloud console, set the service account's access scope to **Allow full access to all Cloud APIs**.
     * If you specify the service account by using the Google Cloud CLI or Compute Engine API, you can use the `scopes` parameter to set the access scope.



## Set up a service account

Create a service account and assign the required IAM roles. Assign as many or as little IAM roles as needed. You can modify the IAM roles on your service account as needed.

Google recommends that you [limit the privileges of service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limiting_service_account_privileges) and regularly check your service account permissions to make sure they are up-to-date.

Use one of the following methods to set up the service account.

###  Console 

Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  1. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
  2. Select your project. 
  3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

  4. Click **Create and continue**. 
  5. Grant the required roles to the service account. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
  6. Click **Continue**. 
  7. In the **Service account users role** field, enter the identifier for the principal that will attach the service account to other resources, such as Compute Engine instances. 

This is typically the email address for a Google Account.

  8. Click **Done** to finish creating the service account. 




###  gcloud 

Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. To provide access to your project and your resources, grant a role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     4. To grant another role to the service account, run the command as you did in the previous step. 
     5. Grant the required role to the principal that will attach the service account to other resources. 
            
            gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `USER_EMAIL`: the email address for a Google Account



###  Terraform 

To create a service account, you can use the [`google_service_account` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account).
    
    
    resource "google_service_account" "default" {
      account_id   = "service-account-id"
      display_name = "Service Account"
    }

Remember to replace the placeholder values for the `account_id` and the `display_name` attributes.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Create a VM and attach the service account

After you create the service account, create a VM and attach the service account that you created in the previous section. Also set the VM's access scope to [`cloud-platform`](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

The access scopes configured on a VM instance define the maximum scopes for OAuth2 access tokens from the metadata server. You can request tokens with fewer scopes than the default. For more information, see [Obtain specific OAuth2 access tokens](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#obtain-oauth-tokens).

If you already have an existing VM and you want to configure that VM to use a different service account, see [Change the attached service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account).

Use one of the following methods to create a VM and attach the service account.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. To attach a service account, do the following:

     1. In the navigation menu, click **Security**.
     2. In the **Service account** list, select the service account that you created.
     3. For **Access scopes** , select **Allow full access to all Cloud APIs**.
  3. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  4. To create and start the instance, click **Create**.




###  gcloud 

To create a new VM instance and configure it to use a custom service account by using the Google Cloud CLI, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and provide the service account email and the `cloud-platform` access scope to the VM instance.
    
    
    gcloud compute instances create VM_NAME \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --scopes=https://www.googleapis.com/auth/cloud-platform
    

Replace the following:

  * `SERVICE_ACCOUNT_EMAIL`: the email address for the service account that you created. For example: `my-sa-123@my-project-123.iam.gserviceaccount.com`. To view the email address, see [Listing service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#listing).
  * `VM_NAME`: the name of the VM instance.



For example:
    
    
    gcloud compute instances create example-vm \
        --service-account 123-my-sa@my-project-123.iam.gserviceaccount.com \
        --scopes=https://www.googleapis.com/auth/cloud-platform
    

You can also specify the scope using the alias: `--scopes=cloud-platform`. These aliases are recognized only by the gcloud CLI. The API and other libraries don't recognize these aliases, so you must specify the full scope URI.

###  Terraform 

To set up a new VM to use a service account, you can use the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance).
    
    
    resource "google_compute_instance" "default" {
      name         = "my-test-vm"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      // Local SSD disk
      scratch_disk {
        interface = "SCSI"
      }
    
      network_interface {
        network = "default"
    
        access_config {
          // Ephemeral public IP
        }
      }
    
      service_account {
        # Google recommends custom service accounts with `cloud-platform` scope with
        # specific permissions granted via IAM Roles.
        # This approach lets you avoid embedding secret keys or user credentials
        # in your instance, image, or app code
        email  = google_service_account.default.email
        scopes = ["cloud-platform"]
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create the VM and specify the service account email and access scope for the VM instance.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "machineType":"zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
       "name":"VM_NAME",
       
       "disks":[
          {
             "initializeParams":{
                "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE"
             },
             "boot":true
          }
       ],
       
       
       "networkInterfaces":[
          {
             "network":"global/networks/NETWORK_NAME"
          }
       ],
       
      "serviceAccounts": [
          {
          "email": "SERVICE_ACCOUNT_EMAIL",
          "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
          }
       ],
       "shieldedInstanceConfig":{
          "enableSecureBoot":"ENABLE_SECURE_BOOT"
       }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project to create the VM in
  * `ZONE`: zone to create the VM in
  * `MACHINE_TYPE_ZONE`: zone containing the machine type to use for the new VM
  * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types), for the new VM
  * `VM_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM
  * `IMAGE_PROJECT`: [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) containing the image  
For example, if you specify `debian-10` as the image family, specify `debian-cloud` as the image project.
  * `IMAGE`: specify one of the following: 
    * `IMAGE`: a specific version of a public image

For example, `"sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20200309"`

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images#image_families)

This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-10"`, Compute Engine creates a VM from the latest version of the OS image in the `Debian 10` image family.

  * `NETWORK_NAME`: the VPC network that you want to use for the VM. You can specify `default` to use your default network.
  * `SERVICE_ACCOUNT_EMAIL`: the email address for the service account that you created. For example: `my-sa-123@my-project-123.iam.gserviceaccount.com`. To view the email address, see [obtain a service account email](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#serviceaccountname). 
  * `ENABLE_SECURE_BOOT`: Optional: If you chose an image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) features, Compute Engine, by default, enables the [virtual trusted platform module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) and [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring). Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default.

If you specify `true` for `enableSecureBoot`, Compute Engine creates a VM with all three Shielded VM features enabled. After Compute Engine starts your VM, to [modify Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm) options, you must stop the VM.




## Access and use other Google Cloud services

After your VM is configured to use the service account, applications can then use the service account to authenticate. The most common method is to authenticate by using [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) and a client library. Some Google Cloud tools such as the gcloud CLI are able to automatically use the service account to access Google Cloud APIs from a VM. For more information, see [Authenticate workloads using service accounts](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads).

If a service account is deleted, applications will no longer have access to Google Cloud resources through that service account. If you delete the default App Engine and Compute Engine service accounts, your VMs will no longer have access to resources in the project. If you're not sure whether a service account is being used, Google recommends [disabling the service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#disabling) before deleting it. Disabled service accounts can be re-enabled if they are still needed.

### Example: Access Cloud Storage resources from your VM

After you have configured your VM to use a service account that has the `storage.admin` role, you can use tools such as the gcloud CLI to manage files that you have stored on Cloud Storage. To access your Cloud Storage resources, complete the following:

  1. Ensure that the service account that is attached to your VM has the `roles/storage.admin` role.

  2. If your VM uses a custom OS image, [install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). By default, the gcloud CLI is installed on most public OS images that are provided by Google Cloud.

  3. Connect to the VM.

  4. From the VM, use the [Google Cloud CLI](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud#create) to manage your Cloud Storage resources.




## What's next?

  * Learn how to [authenticate workloads using service accounts](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads).
  * Learn how to [change the service account attached to a VM](https://docs.cloud.google.com/compute/docs/instances/change-service-account).
  * Learn how to [list and edit service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit).
  * Review the [best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) and mitigate security risks.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
