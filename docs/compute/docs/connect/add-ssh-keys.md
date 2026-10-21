---
url: https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys/
title: Add SSH keys to VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:22.555565+00:00
---

# Add SSH keys to VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add SSH keys to VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to add SSH keys to virtual machine (VM) instances that use OS Login and VMs that use metadata-based SSH keys. If you or your organization administrator hasn't enabled OS Login, your VMs use metadata-based SSH keys. **Key Point:** The procedures in this document are optional. If you connect to VMs using the Google Cloud console or the Google Cloud CLI, Compute Engine creates and manages SSH keys on your behalf.

## Before you begin

  * For information about managing access to your Compute Engine VMs, see [Choosing an access method](https://docs.cloud.google.com/compute/docs/instances/access-overview).
  * If you haven't already, [create an SSH key pair](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).
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




## Add keys to VMs that use OS Login

VMs that use OS Login accept SSH keys that are associated with your Google Account. You can associate a public SSH key with your Google Account using the gcloud CLI or using the OS Login API. If you're an administrator for your organization, you can add SSH keys to user accounts using the [Directory API](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#modify-users).

When you add SSH keys to your Google Account, Compute Engine generates a username for you by combining the username and domain from the email associated with your Google Account. For example, if your email address is `cloudysanfrancisco@gmail.com`, your username is `cloudysanfrancisco_gmail_com`. If you add an SSH key in a project that is outside of your organization, your username is prefixed with `ext_`, for example, `ext_cloudysanfrancisco_gmail_com`. Your organization administrator can customize your username using the [Directory API](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#modify-users). If you already have a username configured, Compute Engine uses that username when you add SSH keys.

To view the SSH keys stored in your OS Login profile, run the [`gcloud compute os-login describe-profile` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login/describe-profile).

**Note:** VMs that are configured to [require SSH certificates](https://docs.cloud.google.com/compute/docs/oslogin/certificates) reject connections from unsigned SSH keys.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions in the [ Compute OS Login External User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.osLoginExternalUser), if you add an SSH key in a project outside of your organization.



###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To add a public SSH key to your account, use the [`gcloud compute os-login ssh-keys add` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/add):
         
         gcloud compute os-login ssh-keys add \
            --key-file=KEY_FILE_PATH \
            --project=PROJECT \
            --ttl=EXPIRE_TIME
         

Replace the following:

     * `KEY_FILE_PATH`: the path to the public SSH key on your workstation. The key must use the `public-openssh` format
     * `PROJECT`: Optional: a project where you intend to use your SSH key. Specify this field to use your SSH key in a project outside of your organization, or you are not a member of a Cloud Identity organization
     * `EXPIRE_TIME`: Optional: the expiration time for the SSH key

For example, if you specify `30m` the SSH key expires after 30 minutes.

This flag uses the following units:

       * `s` for seconds
       * `m` for minutes
       * `h` for hours
       * `d` for days



###  Terraform 

To add a public SSH key to your account, use the [`google_client_openid_userinfo`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/client_openid_userinfo) resource along with the [`google_os_login_ssh_public_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/os_login_ssh_public_key) resource.
    
    
    data "google_client_openid_userinfo" "me" {
    }
    
    resource "google_os_login_ssh_public_key" "default" {
      user = data.google_client_openid_userinfo.me.email
      key  = file("id_rsa.pub") # path/to/ssl/id_rsa.pub
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To add a public SSH key to your account, use the OS Login API [`users.importSshPublicKey` method](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users/importSshPublicKey):
    
    
    POST https://oslogin.googleapis.com/v1/users/ACCOUNT_EMAIL:importSshPublicKey
    
    {
     "key": "SSH_KEY",
     "expirationTimeUsec": "EXPIRATION_TIMESTAMP"
    }
    

Replace the following:

  * `ACCOUNT_EMAIL`: the email address associated with your account
  * `SSH_KEY`: the public key that you want to add to the account
  * `EXPIRATION_TIMESTAMP`: the expiration time for the key, in microseconds since epoch (1 second = 106 microseconds)



## Add SSH keys to VMs that use metadata-based SSH keys

**Caution:** If you manage SSH keys in metadata, you might disrupt the ability of your project members to connect to VMs. Additionally, you risk granting users, including users outside of your project, unintended access to VMs. Users and service accounts that have the ability to modify project metadata can add SSH keys for all VMs in the project except for VMs that block project-level SSH keys. For more information, see [risks of manual key management](https://docs.cloud.google.com/compute/docs/instances/access-overview#risks). 

VMs that don't use OS Login store SSH keys in Compute Engine project and instance metadata. If OS Login is enabled for a VM, then the VM's guest agent ignores the keys stored in metadata.

You can use SSH keys stored in project metadata to access all VMs in a project. You can use SSH keys stored in instance metadata to access individual VMs.

Compute Engine doesn't automatically remove expired SSH keys from metadata at expiration time, but expired keys can't be used to establish new connections to VMs. If you want to remove expired keys from metadata, see [Remove SSH keys from VMs that use metadata-based keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#remove-metadata-key).

You can add a public SSH key to project or VM instance metadata using the Google Cloud console, the gcloud CLI, or REST. You can't set zonal metadata values for SSH keys.

**Caution:** Public SSH keys that you add directly to a VM's `~/.ssh/authorized_keys` files might be overwritten by the VM's [guest agent](https://github.com/GoogleCloudPlatform/guest-agent#features). We recommend that you add keys using the supported Google Cloud console, gcloud CLI, or REST methods as described in the following sections.

### Add SSH keys to project metadata

You can add a public SSH key to project metadata to access all VMs in a project, except VMs that block project-wide SSH keys. For more information about blocking project-wide SSH keys, see [Block SSH keys from VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.projects.setCommonInstanceMetadata` on the project.
  * `iam.serviceAccounts.actAs` on the project. For more information about service account permissions, see [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions).



###  Console 

To add a public SSH key to project metadata using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Metadata** page.

[Go to Metadata](https://console.cloud.google.com/compute/metadata/sshKeys)

  2. Click the **SSH keys** tab.

  3. Click **Edit**.

  4. Click **Add item**.

  5. In the **SSH key** field that opens, add your public SSH key. The key must be in one of the following formats:

     * Format for a key without an expiration time:
           
           KEY_VALUE USERNAME

     * Format for a key with an expiration time:
           
           KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

     * `KEY_VALUE`: the public SSH key value
     * `USERNAME`: your username. For example, `cloudysanfrancisco` or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connect to Linux VMs as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

     * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`
  6. Click **Save**.




###  gcloud 

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  1. If there are existing SSH keys in project metadata, you must re-add them to project metadata every time you add a new SSH key using the gcloud CLI. If you don't re-add your existing keys, adding a new key erases the existing keys.

To add a public SSH key to project metadata using the gcloud CLI, do the following:

     1. If your project already has project-wide public SSH keys, get them from metadata and add them to a new file:

        1. Run the [`gcloud compute project-info describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe) to get the SSH keys for the project:
               
               gcloud compute project-info describe \
                --format="value(commonInstanceMetadata[items][ssh-keys])"
               

The output is similar to the following:
               
               username:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF... username:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ...
               

        2. Copy the `ssh-keys` metadata value.

        3. Create and open a new text file on your workstation.

        4. In the file, paste the list of keys that you just copied.

        5. Add your new key at the end of the list, in one of the following formats:

           * Format for a key without an expiration time:
                 
                 USERNAME:KEY_VALUE

           * Format for a key with an expiration time:
                 
                 USERNAME:KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

           * `KEY_VALUE`: the public SSH key value
           * `USERNAME`: your username. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connecting to instances as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

           * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`
        6. Save and close the file.

     2. Run the `gcloud compute project-info add-metadata` command to set the project-wide `ssh-keys` value:
            
            gcloud compute project-info add-metadata --metadata-from-file=ssh-keys=KEY_FILE
            

Replace `KEY_FILE` with one of the following:

        * The path to the file you created in the previous step, if the project had existing SSH keys
        * The path to your new public SSH key file, if the project didn't have existing SSH keys



###  Terraform 

To add a public SSH key to your project metadata, use the [`google_compute_project_metadata`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_metadata) resource.
    
    
    resource "google_compute_project_metadata" "default" {
      metadata = {
        ssh-keys = <<EOF
          dev:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT dev
          test:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT test
        EOF
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

If there are existing SSH keys in project metadata, you must re-add them to project metadata every time you add a new SSH key using the Compute Engine API. If you don't re-add your existing keys, adding a new key erases the existing keys.

To add a public SSH key to project metadata using the Compute Engine API, do the following:

  1. Get the `fingerprint` and `ssh-keys` values from metadata by using the [`projects.get`](https://docs.cloud.google.com/compute/docs/reference/latest/projects/get) method
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

The response is similar to the following:
         
         ...
         "fingerprint": "utgYE_XWtE8=",
         "items": [
         {
          "key": "ssh-keys",
          "value": "cloudysanfrancisco:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF...\nbaklavainthebalkans:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQDx3FNVC8... google-ssh {"userName":"baklavainthebalkans","expireOn":"2021-06-14T16:59:03+0000"}"
         }
         ]
         ...
         

  2. Add the new `ssh-keys` value by using the [`projects.setCommonInstanceMetadata`](https://docs.cloud.google.com/compute/docs/reference/latest/projects/setCommonInstanceMetadata) method.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/setCommonInstanceMetadata
         
         {
         "items": [
          {
           "key": "ssh-keys",
           "value": "EXISTING_SSH_KEYS\nNEW_SSH_KEY"
          }
         ]
         "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `EXISTING_SSH_KEYS`: the value of the `ssh-keys` key from the response of the `projects.get` request
     * `FINGERPRINT`: the value of the `fingerprint` from the response of the `projects.get` request
     * `NEW_SSH_KEY`: the new SSH key, in one of the following formats:

       * Format for a key without an expiration time:
             
             USERNAME:KEY_VALUE

       * Format for a key with an expiration time:
             
             USERNAME:KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

       * `KEY_VALUE`: the public SSH key value
       * `USERNAME`: your username. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connecting to instances as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

       * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`



### Add SSH keys to instance metadata

You can add a public SSH key to instance metadata when you create a VM or after you create a VM.

#### Add SSH keys to instance metadata during VM creation

You can add SSH keys to instance metadata during VM creation, using the Google Cloud console, gcloud CLI, or Compute Engine API.

###  Console 

To create an instance and add a public SSH key to instance metadata at the same time using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. To add a public SSH key to instance metadata, do the following:

     1. In the navigation menu, click **Security**.

     2. Expand the **Manage access** section.

     3. To disable OS Login, clear the **Control VM access through IAM permissions** checkbox.

     4. If you want to allow public SSH keys in project metadata to access the instance, clear the **Block project-wide SSH keys** checkbox.

     5. In the **Add manually generated SSH keys** section, click **Add item**.

     6. Add your public key in the text field. The key must be in one of the following formats:

        * Format for a key without an expiration time:
              
              KEY_VALUE USERNAME

        * Format for a key with an expiration time:
              
              KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

        * `KEY_VALUE`: the public SSH key value
        * `USERNAME`: your username. For example, `cloudysanfrancisco` or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connect to Linux VMs as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

        * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`
  3. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  4. To create and start the instance, click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create a VM and add a public SSH key to instance metadata at the same time using the gcloud CLI, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
         
         gcloud compute instances create VM_NAME \
            --metadata=ssh-keys=PUBLIC_KEY
         

Replace the following:

     * `VM_NAME`: the name of the new VM
     * `PUBLIC_KEY`: your public SSH key, in one of the following formats:

       * Format for a key without an expiration time:
             
             USERNAME:KEY_VALUE

       * Format for a key with an expiration time:
             
             USERNAME:KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

       * `KEY_VALUE`: the public SSH key value
       * `USERNAME`: your username. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connecting to instances as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

       * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`

You can add multiple SSH keys by using the `--metadata-from-file=ssh-keys=FILE_PATH` flag. In the file, add a list of usernames and public SSH keys in one of the preceding formats.




###  Terraform 

To add a public SSH key to your instance metadata, use the [`google_compute_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) resource.
    
    
    resource "google_compute_instance" "default" {
      name         = "my-vm"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "ubuntu-1404-trusty-v20160627"
        }
      }
    
      # Local SSD disk
      scratch_disk {
        interface = "SCSI"
      }
    
      network_interface {
        network = "default"
        access_config {}
      }
      metadata = {
        "ssh-keys" = <<EOT
          dev:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT dev
          test:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT test
         EOT
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a VM and add a public SSH key to instance metadata at the same time using the Compute Engine, construct a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `ZONE`: the zone of the VM



In the body of the request, provide usernames and public SSH keys in the `items` property:
    
    
    ...
    {
     "items": [
        {
         "key": "ssh-keys",
         "value": "PUBLIC_KEY"
        }
       ]
    }
    ...
    

Replace `PUBLIC_KEY` with your public key, in one of the following formats:

  * Format for a key without an expiration time:
        
        USERNAME:KEY_VALUE

  * Format for a key with an expiration time:
        
        USERNAME:KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}




Replace the following:

  * `KEY_VALUE`: the public SSH key value
  * `USERNAME`: your username. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connecting to instances as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

  * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`



You can add multiple SSH keys by adding `\n` between keys.

#### Add SSH keys to instance metadata after VM creation

You can add SSH keys to instance metadata after VM creation, using the Google Cloud console, gcloud CLI, or Compute Engine API.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.setMetadata` on the VM



###  Console 

To add a public SSH key to instance metadata using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM that you want to add an SSH key for.

  3. Click **Edit**.

  4. Under **SSH Keys** , click **Add item**.

  5. Add your public key into the text field. The key must be in one of the following formats:

     * Format for a key without an expiration time:
           
           KEY_VALUE USERNAME

     * Format for a key with an expiration time:
           
           KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

     * `KEY_VALUE`: the public SSH key value
     * `USERNAME`: your username. For example, `cloudysanfrancisco` or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connect to Linux VMs as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

     * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`
  6. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. If there are existing SSH keys in instance metadata, you must re-add them to instance metadata every time you add a new SSH key using the gcloud CLI. If you don't re-add your existing keys, adding a new key erases the existing keys.

To add a public SSH key to instance metadata using the gcloud CLI, do the following:

     1. If your VM already has instance-level public SSH keys, get them from metadata and add them to a new file:

        1. Run the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) to get the metadata for the VM:
               
               gcloud compute instances describe VM_NAME
               

Replace VM_NAME with the name of the VM for which you need to add or remove public SSH keys.

The output is similar to the following:
               
               ...
               metadata:
               ...
               - key: ssh-keys
                value: |-
                  cloudysanfrancisco:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF...
                  baklavainthebalkans:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQDx3FNVC8... google-ssh {"userName":"baklavainthebalkans","expireOn":"2021-06-14T16:59:03+0000"}
               ...
               

        2. Copy the `ssh-keys` metadata value.

        3. Create and open a new text file on your workstation.

        4. In the file, paste the list of keys that you just copied.

        5. Add your new key at the end of the list, in one of the following formats:

        * Format for a key without an expiration time:
              
              USERNAME:KEY_VALUE

        * Format for a key with an expiration time:
              
              USERNAME:KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

        * `KEY_VALUE`: the public SSH key value
        * `USERNAME`: your username. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connecting to instances as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

        * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`
        1. Save and close the file.
     2. Run the `gcloud compute instances add-metadata` command to set the `ssh-keys` value:
            
            gcloud compute instances add-metadata VM_NAME --metadata-from-file ssh-keys=KEY_FILE
            

Replace the following:

        * `VM_NAME`: the VM you want to add the SSH key for
        * `KEY_FILE` with one of the following:
        * The path to the file you created in the previous step, if the VM had existing SSH keys
        * The path to your new public SSH key file, if the VM didn't have existing SSH keys



###  REST 

If there are existing SSH keys in instance metadata, you must re-add them to instance metadata every time you add a new SSH key using the Compute Engine API. If you don't re-add your existing keys, adding a new key erases the existing keys.

To add a public SSH key to instance metadata using the Compute Engine API, do the following:

  1. Get the `fingerprint` and `ssh-keys` values from metadata by using the [`instances.get`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/get) method.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone of the VM to add an SSH key
     * `VM_NAME`: the VM you're adding an SSH key for

The response is similar to the following:
    
    ...
    "fingerprint": "utgYE_XWtE8=",
    "items": [
    {
     "key": "ssh-keys",
      "value": "cloudysanfrancisco:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF...\nbaklavainthebalkans:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQDx3FNVC8... google-ssh {"userName":"baklavainthebalkans","expireOn":"2021-06-14T16:59:03+0000"}"
    }
    ]
    ...
    

  2. Add the new `ssh-keys` value by using the [`instances.setMetadata`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setMetadata) method.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
         
         {
         "items": [
          {
           "key": "ssh-keys",
           "value": "EXISTING_SSH_KEYS\nNEW_SSH_KEY"
          }
         ]
         "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `EXISTING_SSH_KEYS`: the value of the `ssh-keys` key from the response of the `instances.get` request
     * `FINGERPRINT`: the `fingerprint` from the response of the `projects.get` request
     * `NEW_SSH_KEY`: the new SSH key, in one of the following formats:

       * Format for a key without an expiration time:
             
             USERNAME:KEY_VALUE

       * Format for a key with an expiration time:
             
             USERNAME:KEY_VALUE google-ssh {"userName":"USERNAME","expireOn":"EXPIRE_TIME"}

Replace the following:

       * `KEY_VALUE`: the public SSH key value
       * `USERNAME`: your username. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`. 

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connecting to instances as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.

       * `EXPIRE_TIME`: the time the key expires, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example: `2021-12-04T20:12:00+0000`



## What's next?

  * Learn how to [connect to VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).
  * Learn how to [manage access to VMs](https://docs.cloud.google.com/compute/docs/instances/access-overview).
  * Learn how to [transfer files to VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files).
  * Learn how [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh) work on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
