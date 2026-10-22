---
url: https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys/
title: Restrict SSH keys from VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:54.603942+00:00
---

# Restrict SSH keys from VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Restrict SSH keys from VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to prevent users from accessing virtual machine (VM) instances by removing and blocking SSH keys from VMs.

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




## Remove SSH keys

You can remove SSH keys from VMs that use OS Login and VMs that use metadata-based SSH keys. 

### Remove SSH keys from VMs that use OS Login

VMs that use OS Login accept SSH keys that are associated with your Google account. You can remove a public SSH key from your user account using the Google Cloud CLI or the OS Login API. If you're an administrator for your organization, you can remove SSH keys from user accounts using the [Directory API](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#modify-users). Compute Engine automatically removes expired keys from your Google Account.

###  gcloud 

To remove a public SSH key from your account, do the following:

  1. If you don't know which key you want to remove, run the [`gcloud compute os-login describe-profile` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login/describe-profile) to view all keys associated with your account:
         
         gcloud compute os-login describe-profile
         

  2. Copy the `fingerprint` value of the key you want to delete.

  3. Remove the key from your account using the [`gcloud compute os-login ssh-keys remove` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/remove):
         
         gcloud compute os-login ssh-keys remove --key=KEY
         

Replace `KEY` with the public SSH key you want to remove, or the OS Login fingerprint for the key you want to remove.




###  REST 

To remove a public SSH key from your account, do the following:

  1. If you don't know which key you want to remove, use the [`users.getLoginProfile` method](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users/getLoginProfile) to view all keys associated with your account:
         
         GET https://oslogin.googleapis.com/v1/users/ACCOUNT_EMAIL/loginProfile
         

Replace `ACCOUNT_EMAIL` with the email address associated with your account.

  2. Copy the `fingerprint` value of the key you want to delete.

  3. Remove the key from your account using the [`users.sshPublicKeys.delete` method](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKeys/delete):
         
         DELETE https://oslogin.googleapis.com/v1/users/ACCOUNT_EMAIL/sshPublicKeys/FINGERPRINT
         

Replace the following:

     * `ACCOUNT_EMAIL`: the email address associated with your account
     * `FINGERPRINT`: the SHA-256 fingerprint of the key to remove



### Remove SSH keys from VMs that use metadata-based keys

You can remove a public SSH key from project or instance metadata using the Google Cloud console, the gcloud CLI, or the Compute Engine API.

After you remove the last key from metadata for a particular user, or the last key in metadata for a particular user expires, Compute Engine deletes the user's `~/.ssh/authorized_keys` file on the VM.

Caution: If you manage SSH keys in metadata, you might disrupt the ability of your project members to connect to VMs. Additionally, you risk granting users, including users outside of your project, unintended access to VMs. For more information, see [risks of manual key management](https://docs.cloud.google.com/compute/docs/instances/access-overview#risks). 

#### Remove a public key from project metadata

Remove a public SSH key from project metadata to remove access to all VMs in a project.

When you remove a key from metadata using the gcloud CLI and the Compute Engine API, you must retrieve the list of existing keys, edit the list of keys to remove the unwanted keys, and overwrite the old keys with the list of keys you want to keep, as explained in the following section.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.projects.setCommonInstanceMetadata`



###  Console 

To remove a public SSH key from project metadata using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Metadata** page.

[Go to Metadata](https://console.cloud.google.com/compute/metadata/sshKeys)

  2. Click the **SSH keys** tab.

  3. Click edit **Edit** at the top of the page.

  4. Navigate to the SSH key that you want to remove and click the delete delete button next to the SSH key.

Repeat this step for each SSH key that you want to remove.

  5. Click **Save**.




###  gcloud 

To remove a public SSH key from project metadata using the gcloud CLI, do the following:

  1. Run [`gcloud compute project-info describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe) to get the metadata for the project:
         
         gcloud compute project-info describe
         

The output is similar to the following:
         
         ...
         metadata:
           ...
           - key: ssh-keys
             value: |-
               cloudysanfrancisco:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF
               baklavainthebalkans:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQDx3FNVC8 google-ssh {"userName":"baklavainthebalkans","expireOn":"2021-06-14T16:59:03+0000"}
         ...
         

  2. Copy the `ssh-keys` metadata value.

  3. Create and open a new text file on your workstation.

  4. In the file, paste the list of SSH keys that you just copied, then delete any keys you want to remove from project metadata.

  5. Save and close the file.

  6. Run the [`gcloud compute project-info add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata) to set the project-wide `ssh-keys` value:
         
         gcloud compute project-info add-metadata --metadata-from-file=ssh-keys=KEY_FILE
         

Replace `KEY_FILE` with one of the following:

     * the path to the file you created in the previous step, if the project had existing SSH keys
     * the path to your new public SSH key file, if the project didn't have existing SSH keys



###  REST 

To remove a public SSH key from project metadata using the Compute Engine API, do the following:

  1. Use the [`projects.get`](https://docs.cloud.google.com/compute/docs/reference/latest/projects/get) method to get the `fingerprint` and `ssh-keys` values from metadata.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

The response is similar to the following:
         
         ...
         "fingerprint": "utgYE_XWtE8=",
         "items": [
          {
           "key": "ssh-keys",
           "value": "cloudysanfrancisco:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF\nbaklavainthebalkans:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQDx3FNVC8 google-ssh {"userName":"baklavainthebalkans","expireOn":"2021-06-14T16:59:03+0000"}"
          }
         ]
         ...
         

  2. Copy the list of SSH key values and delete the keys you want to remove.

  3. Use the [`projects.setCommonInstanceMetadata`](https://docs.cloud.google.com/compute/docs/reference/latest/projects/setCommonInstanceMetadata) to remove the SSH keys.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/setCommonInstanceMetadata
         
         {
         "items": [
          {
           "key": "ssh-keys",
           "value": "EXISTING_SSH_KEYS"
          }
         ]
         "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `EXISTING_SSH_KEYS`: the list of the SSH keys you want to keep
     * `FINGERPRINT`: the value of the `fingerprint` from the response of the `projects.get` request



#### Remove a public SSH key from instance metadata

Remove a public SSH key from instance metadata to remove access to a single VM.

When you remove a key from metadata using the gcloud CLI and the Compute Engine API, you must retrieve the list of existing keys, edit the list of keys to remove the unwanted keys, and overwrite the old keys with the list of keys you want to keep, as explained in the following section.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.setMetadata`



###  Console 

To remove a public SSH key from instance metadata using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM that you want to remove a key for.

  3. Click **Edit**.

  4. In **SSH Keys** section, click **Show and edit**. The section expands to show all of the instance-level public SSH keys.

  5. Click the delete delete button next to the SSH key that you want to remove.

Repeat this step for each SSH key that you want to remove.

  6. Click **Save**.




###  gcloud 

To remove a public SSH key from instance metadata using the gcloud CLI, do the following:

  1. Run [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) to get the metadata for the VM:
         
         gcloud compute instances describe VM_NAME
         

Replace VM_NAME with the name of the VM for which you need to add or remove public SSH keys.

The output is similar to the following:
         
         ...
         metadata:
         ...
         - key: ssh-keys
          value: |-
            cloudysanfrancisco:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF
            baklavainthebalkans:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQDx3FNVC8 google-ssh {"userName":"baklavainthebalkans","expireOn":"2021-06-14T16:59:03+0000"}
         ...
         

  2. Copy the `ssh-keys` metadata value.

  3. Create and open a new text file on your local workstation.

  4. In the file, paste the list of SSH keys that you just copied, then remove any keys you want to delete.

  5. Save and close the file.

  6. Run the [`gcloud compute project-info add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata) to set the project-wide `ssh-keys` value:
         
         gcloud compute instances add-metadata VM_NAME --metadata-from-file ssh-keys=KEY_FILE
         

Replace the following:

     * `VM_NAME`: the VM you want to remove the SSH key for
     * `KEY_FILE`: the path to the file that contains the list of all project SSH keys



###  REST 

To remove a public SSH key from instance metadata using the Compute Engine API, do the following:

  1. Use the [`instances.get`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/get) method to get the `fingerprint` and `ssh-keys` values from metadata.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone of the VM you're adding an SSH key for
     * `VM_NAME`: the VM you're adding an SSH key for

The response is similar to the following:
    
    ...
    "fingerprint": "utgYE_XWtE8=",
    "items": [
    {
     "key": "ssh-keys",
     "value": "cloudysanfrancisco:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF\nbaklavainthebalkans:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQDx3FNVC8 google-ssh {"userName":"baklavainthebalkans","expireOn":"2021-06-14T16:59:03+0000"}"
    }
    ]
    ...
    

  2. Copy the list of SSH key values and delete the keys you want to remove.

  3. Use the [`instances.setMetadata`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setMetadata) to remove the SSH keys.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
         
         {
         "items": [
          {
           "key": "ssh-keys",
           "value": "EXISTING_SSH_KEYS
          }
         ]
         "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `EXISTING_SSH_KEYS`: the value of the `ssh-keys` key from the response of the `projects.get` request
     * `FINGERPRINT`: the value of the `fingerprint` from the response of the `instances.get` request



## Block project SSH keys from VMs that use metadata-based SSH keys

You can prevent VMs from accepting SSH keys that are stored in project metadata by blocking project SSH keys from VMs. You can block project SSH keys from VMs when you create a VM or after you create a VM.

**Caution:** Users with SSH keys in instance metadata can access VMs that block project SSH keys.

### Block project SSH keys from a VM during VM creation

You can block project SSH keys from VMs during VM creation, using the Google Cloud console, gcloud CLI, or Compute Engine API.

**Caution:** Users with SSH keys in instance metadata can access VMs that block project SSH keys.

###  Console 

To create an instance and block it from accepting SSH keys stored in project metadata using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. To block project SSH keys, do the following:

     1. In the navigation menu, click **Security**.

     2. Expand the **Manage access** section.

     3. To disable OS Login, clear the **Control VM access through IAM permissions** checkbox.

     4. Select the **Block project-wide SSH keys** checkbox.

  3. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  4. To create and start the instance, click **Create**.




###  gcloud 

To create a VM and block it from accepting SSH keys stored in project metadata using the gcloud CLI, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
    
    
    gcloud compute instances create VM_NAME \
        --metadata block-project-ssh-keys=TRUE
    

Replace `VM_NAME` with the name of the new VM.

###  REST 

To create a VM and block it from accepting SSH keys stored in project metadata using the Compute Engine, construct a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `ZONE`: the zone of the VM



In the body of the request, provide usernames and public SSH keys in the `items` property:
    
    
    ...
    {
     "items": [
        {
         "key": "block-project-ssh-keys",
         "value": TRUE
        }
       ]
    }
    ...
    

### Block project SSH keys from a VM after VM creation

You can block project SSH keys from VMs after VM creation using the Google Cloud console, gcloud CLI, or Compute Engine API.

**Caution:** Users with SSH keys in instance metadata can access VMs that block project SSH keys.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.projects.setCommonInstanceMetadata`



###  Console 

To block VMs from accepting connections from SSH keys stored in project metadata using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM that you want to block project SSH keys for.

  3. Click **Edit**.

  4. Under **SSH Keys** , select the **Block project-wide SSH keys** checkbox.

  5. When you have finished editing the connection setting for SSH keys, click **Save**.




###  gcloud 

To block VMs from accepting connections from SSH keys stored in project metadata using the gcloud CLI, do the following:

Run the [`gcloud compute instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata):
    
    
    gcloud compute instances add-metadata VM_NAME --metadata block-project-ssh-keys=TRUE
    

Replace `VM_NAME` with the name of the VM for which you want to block project-wide public SSH keys.

###  REST 

To block VMs from accepting connections from SSH keys stored in project metadata using the Compute Engine API, do the following:

  1. Use the [`instances.get`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/get) method to get the `fingerprint` from metadata.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone of the VM you're adding an SSH key for
     * `VM_NAME`: the VM you're adding an SSH key for

The response is similar to the following:
    
    ...
    "fingerprint": "utgYE_XWtE8="
    ...
    

  2. Use the [`instances.setMetadata` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setMetadata) to set `block-project-ssh-keys` to `TRUE`:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
         
         {
         "items": [
          {
           "key": "block-project-ssh-keys",
           "value": TRUE
          }
         ]
         "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID` is your project ID
     * `ZONE` is the zone where your instance is located
     * `INSTANCE_NAME` is the instance where you want to block project-wide keys.
     * `FINGERPRINT`: the value of the `fingerprint` from the response of the `instances.get` request.



## What's next?

  * Learn about the benefits of using [OS Login](https://docs.cloud.google.com/compute/docs/oslogin) for access management.
  * [Connect to VMs using Google tools](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance), so you don't have to manage your own SSH keys.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
