---
url: https://docs.cloud.google.com/compute/docs/oslogin/certificates/
title: Set up OS Login to require SSH certificates for SSH connections \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:38.510736+00:00
---

# Set up OS Login to require SSH certificates for SSH connections  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set up OS Login to require SSH certificates for SSH connections Stay organized with collections  Save and categorize content based on your preferences. 

VMs that support OS Login certificates support connections from SSH keys and SSH certificates. _SSH certificates_ are SSH keys that have been signed by another trusted key, in this case a certificate authority that OS Login manages. This document describes how to set up OS Login VMs to require SSH certificates for SSH connections and block connections from unsigned SSH keys.

When you set up OS Login to require SSH certificates for connections to VMs, only SSH certificates that have been signed by the certificate authority are permitted to connect to VMs; connections from unsigned SSH keys are rejected. SSH certificates have an expiry of five minutes, after which they can no longer be used to connect to VMs and a new certificate must be generated.

We recommend setting up OS Login to require SSH certificates for SSH connections as an added layer of security against malicious users. SSH certificates are short-lived and are only valid for a specific VM, which means that if they are compromised, their attack surface is significantly smaller and their attack window is significantly shorter than that of long-lived SSH keys.

If your organization uses Workforce Identity Federation, see [Use Workforce Identity Federation with OS Login](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#use_workforce_identity_federation_with_os_login) to learn about how to enable SSH certificates for your organization.

## Before you begin

  * [Set up OS Login and assign OS Login IAM roles](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).
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




## Limitations

  * The VM you're connecting to must have OpenSSH version 7.4 or later to use SSH certificates. **Note:** VMs built from SUSE Linux Enterprise Server (SLES) 12 images don't have OpenSSH 7.4 and can't use SSH certificates. 



## Require SSH certificates

You can set up OS Login to require SSH certificates for all SSH connections to OS Login VMs in your project, or for single VMs. After you set up OS Login to require SSH certificates, SSH connections from the Google Cloud console and the gcloud CLI use SSH certificates by default. If you don't want to set up OS Login to require certificates but you want to use certificates to connect to VMs, you must connect using third-party tools, as described in the Connect to a VM using an SSH certificate section.

Warning: When you require SSH certificates, VMs reject connections from SSH keys that you [previously configured to use with OS Login](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). 

### Require SSH certificates for all OS Login-enabled VMs in a project

To require SSH certificates for all connections to all VMs that use OS Login in your project, use the Google Cloud console or the gcloud CLI.

###  Console 

To require SSH certificates for all connections to OS Login-enabled VMs, use the Google Cloud console to set `enable-oslogin` and `enable-oslogin-certificates` to `TRUE` in project metadata:

  1. Go to the **Metadata** page.

[Go to Metadata](https://console.cloud.google.com/compute/metadata)

  2. Click **Edit**.

  3. Click **Add item**.

     1. In the **Key** field, enter `enable-oslogin`.
     2. In the **Value** field, enter `TRUE`.
  4. Click **Add item**.

     1. In the **Key** field, enter `enable-oslogin-certificates`.
     2. In the **Value** field, enter `TRUE`.
  5. Click **Save**.




###  gcloud 

To require SSH certificates for all connections to OS Login-enabled VMs, use the [`gcloud compute project-info add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata) to set `enable-oslogin=TRUE` and `enable-oslogin-certificates=TRUE` in project metadata:
    
    
    gcloud compute project-info add-metadata \
        --metadata enable-oslogin=TRUE,enable-oslogin-certificates=TRUE
    

### Require SSH certificates on a single OS Login-enabled VM

To require certificates for all SSH connections to a single VM that uses OS Login, use the Google Cloud console or the gcloud CLI.

###  Console 

To require SSH certificates for all connections to a single VM, use the Google Cloud console to set `enable-oslogin` and `enable-oslogin-certificates` to `TRUE` in instance metadata:

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM you want to require SSH certificates for.

  3. Click **Edit**.

  4. In the **Metadata** section, click **Add item**.

     1. In the **Key** field, enter `enable-oslogin`.
     2. In the **Value** field, enter `TRUE`.
  5. Click **Add item**.

     1. In the **Key** field, enter `enable-oslogin-certificates`.
     2. In the **Value** field, enter `TRUE`.
  6. Click **Save**.




###  gcloud 

To require SSH certificates for all connections to a single VM, use the [`gcloud compute instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata) to set `enable-oslogin=TRUE` and `enable-oslogin-certificates=TRUE` in instance metadata:
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata enable-oslogin=TRUE,enable-oslogin-certificates=TRUE
    

Replace `VM_NAME` with the name of your VM.

## Connect to a VM using an SSH certificate

After you set up OS Login to require SSH certificates, SSH connections from the Google Cloud console and the gcloud CLI use SSH certificates by default. If you don't want to set up OS Login to require certificates but you want to use certificates to connect to VMs, you must connect using third-party tools.

###  Console 

Connect to VMs using [SSH-in-browser](https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser) from the Google Cloud console, by doing the following:

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)




###  gcloud 

Use the [`gcloud beta compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/ssh) to connect to a VM using a certificate:
    
    
    gcloud beta compute ssh VM_NAME
    

Replace `VM_NAME` with the name of the VM that you want to connect to.

###  Third-party tools 

To use an SSH certificate with a third-party SSH client, do the following:

  1. [Create an SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys) if you don't already have one.

  2. Sign your public SSH key using the [`projects.locations.signSshPublicKey` method](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/projects.locations/signSshPublicKey):
         
         POST https://oslogin.googleapis.com/v1beta/projects/PROJECT_ID/locations/LOCATION:signSshPublicKey
         
         {
          "ssh_public_key": "PUBLIC_KEY"
          "compute_instance": "COMPUTE_INSTANCE",
          "service_account": "SERVICE_ACCOUNT"
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID of the project that contains the VM you want to connect to
     * `LOCATION`: the region where the VM you want to connect to is located
     * `PUBLIC_KEY`: the contents of your SSH public key file
     * `COMPUTE_INSTANCE`: the Compute Engine instance to connect to, in the format of `projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID`.
     * `SERVICE_ACCOUNT`: the service account attached to the instance. Delete this field if the instance doesn't have a service account attached.
  3. Copy the SSH certificate from the output of the `projects.locations.signSshPublicKey` method and save the contents in a new file.

  4. Set permissions on the SSH certificate file, by running the following command:
         
         sudo chmod 600 FILE_NAME
         

Replace `FILE_NAME` with the name of the file.

  5. Connect to the VM using the following command:
         
         ssh -i PATH_TO_PRIVATE_KEY -o CertificateFile=PATH_TO_SSH_CERTIFICATE USERNAME@EXTERNAL_IP
         

Replace the following:

     * `PATH_TO_PRIVATE_KEY`: the path to your private SSH key file.
     * `PATH_TO_SSH_CERTIFICATE`: the path to your SSH certificate file.
     * `USERNAME`: your OS Login username
     * `EXTERNAL_IP`: the external IP address of the VM.



## Troubleshooting

If you can't connect to VMs that you have set up to require SSH certificates, it might be because of the following:

  * Your VM is using an unsupported version of OpenSSH. To workaround this issue, disable certificates in the VM's metadata by setting `enable-oslogin-certificates` to `FALSE` in [instance metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-instance-metadata).



## What's next?

  * Learn more about [OS Login](https://docs.cloud.google.com/compute/docs/oslogin).
  * Learn how to [set up OS Login with 2-step verification](https://docs.cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication).
  * Learn how to [manage OS Login in an organization](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
