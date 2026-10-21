---
url: https://docs.cloud.google.com/filestore/docs/quickstart-gcloud/
title: Quickstart: Create a Filestore instance by using the gcloud CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:39:55.226518+00:00
---

# Quickstart: Create a Filestore instance by using the gcloud CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/quickstart-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Filestore instance using the gcloud CLI

This quickstart shows you how to get up and running quickly with Filestore using the Google Cloud CLI. In this quickstart, you learn how to:

  * Create a Filestore instance.
  * Mount the file share from that instance on a Compute Engine client VM.
  * Create a file on the mounted file share.
  * Delete the Filestore instance.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Filestore API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable file.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Filestore API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable file.googleapis.com




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * Create and manage Filestore instances: [Cloud Filestore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`) 
  * Create and manage Compute Engine instances: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Create a Compute Engine VM

###  Linux 

  1. Create a Compute Engine instance. Configure the instance as follows: 
     * Name the instance `nfs-client`. 
     * Set the `--zone` flag to `us-central1-c`. 
     * Set the `--image-project` flag to `debian-cloud`. 
     * Set the `--image-family` flag to `debian-11`. 
     * Set the `--tags` flag to `http-server`. 
    
    gcloud compute instances create nfs-client --zone=us-central1-c --image-project=debian-cloud --image-family=debian-11 --tags=http-server




###  Windows 

  1. Create a Compute Engine instance. Configure the instance as follows: 
     * Name the instance `nfs-client`. 
     * Set the `--zone` flag to `us-central1-c`. 
     * Set the `--image-project` flag to `windows-cloud`. 
     * Set the `--image-family` flag to `windows-2012-r2`. 
     * Set the `--tags` flag to `http-server`. 
    
    gcloud compute instances create nfs-client --zone=us-central1-c --image-project=windows-cloud --image-family=windows-2012-r2 --tags=http-server




## Create a Filestore instance

This quickstart shows how to create an instance in the regional service tier with custom performance enabled. For details on creating instances, see [create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances).

  1. Create a Filestore instance. Configure the instance as follows:

     * Name the instance `nfs-server`.
     * Set the `--region` flag to `us-central1`.
     * Set the `--tier` flag to `REGIONAL`.
     * Set the `--performance` flag to `max-iops-per-tb=17000`.

**Note:** After activating custom performance for an instance you can't deactivate it for that instance. Instances with activated custom performance are billed according to purchased IOPS. For details, see [ configure custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance#enable-custom-performance) and [ Filestore pricing](https://docs.cloud.google.com/filestore/pricing).
     * Set the `--file-share` flag to `name="vol1",capacity=1TB`.

     * Set the `--network` flag to `name="default"`.
           
           gcloud filestore instances create nfs-server --region=us-central1 --tier=REGIONAL --performance=max-iops-per-tb=17000 --file-share=name="vol1",capacity=1TB --network=name="default"

  2. Get information about the Filestore instance you created:
         
         gcloud filestore instances describe nfs-server --region=us-central1 

The command returns something like:
         
         createTime: '2025-02-12T09:15:08.163246004Z'
             customPerformanceSupported: true
             fileShares:
              -capacityGb: '1024'
                 name: vol1
             name: projects/yourproject/locations/us-central1/instances/nfs-server
             networks:
             -connectMode: DIRECT_PEERING
               ipAddresses:
                - 10.0.0.2
               network: default
               reservedIpRange: 10.0.0.2/26
             performanceConfig:
               iopsPerTb:
                 maxIopsPerTb: '17000'
             performanceLimits:
               maxIops: '17000'
               maxReadIops: '17000'
               maxReadThroughputBps: '417792000'
               maxWriteIops: '5100'
               maxWriteThroughputBps: '139264000'
             protocol: NFS_V3
             state: READY
             tier: REGIONAL




Copy down the IP address of the instance for use when mounting the file share. For this quickstart, we use the IP address `10.0.0.2`.

## Mount the Filestore file share on the `nfs-client` instance

###  Linux 

  1. Establish an SSH connection to the `nfs-client` instance: 
         
         gcloud compute ssh nfs-client



  1. Install NFS by running the following commands on the terminal window of `nfs-client`:
         
         sudo apt-get -y update &&
         sudo apt-get -y install nfs-common
         

  2. Create a mount directory on the `nfs-client` instance for the Filestore file share:
         
         sudo mkdir /mnt/test
         

  3. Mount the file share to the `nfs-client` instance with the [`mount`](https://linux.die.net/man/8/mount) command by specifying the IP address of the Filestore instance, the name of the file share, and the mount directory to mount to:
         
         sudo mount MOUNT-POINT-DIRECTORY /mnt/test
         

where:

MOUNT-POINT-DIRECTORY is the path to the directory where the Filestore file share is mounted. For example: `10.0.0.2:/vol1`

**Note:** For NFS mount option recommendations, see [Mounting file shares](https://docs.cloud.google.com/filestore/docs/mounting-fileshares#mounting-fileshare-on-vm).
  4. **Optional** : Confirm that the Filestore file share is mounted:

df -h --type=nfs

  5. Make the file share accessible by changing its permissions:
         
         sudo chmod go+rw /mnt/test
         


**Important:** We recommend setting more specific permissions in a production environment. For more information, see [Configuring access on a file share](https://docs.cloud.google.com/filestore/docs/access-control#fileshare-access).

###  Windows 

### Sign in to the `nfs-client` instance and open a Command Prompt as an administrator

  1. Create an account and set an initial password for the `nfs-client` instance:
         
         gcloud compute reset-windows-password nfs-client
         

  2. Configure your instance to enable connecting to serial ports:
         
         gcloud compute instances add-metadata nfs-client --metadata=serial-port-enable=1
         

  3. Enter an interactive session:
         
         gcloud compute connect-to-serial-port nfs-client --port=2
         

  4. At the `SAC>` prompt, create a new channel:
         
         cmd
         

A channel with the name `Cmd0001` is created.

  5. Connect to the channel:
         
         ch -sn Cmd0001
         

  6. Enter the username and password of the `nfs-client` instance and leave the `Domain` field blank. You are connected to the `Command Prompt` interface of the `nfs-client` instance.




### Install NFS client

  1. In the `Command Prompt` of `nfs-client`, switch to `Windows PowerShell`:
         
         powershell
         

  2. Install the `NFS` client:
         
         Install-WindowsFeature -Name NFS-Client
         

  3. Restart the `nfs-client` instance when prompted:
         
         restart-computer
         

  4. At the `SAC>` prompt, wait for the following notification to appear:
         
         EVENT: The CMD command is now available.

Then, run the `cmd` and `ch -sn` commands as previously instructed to sign in and reconnect to the `nfs-client` instance.




### Configure the user ID used by the NFS client

  1. In the Command Prompt, run `powershell` to switch to Windows PowerShell.
  2. In `PowerShell`, run the following commands to create two new registry entries, `AnonymousUid` and `AnonymousGid`:
         
         New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" `
             -Name "AnonymousUid" -Value "0" -PropertyType DWORD
         
         New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" `
             -Name "AnonymousGid" -Value "0" -PropertyType DWORD
         

  3. Restart the NFS client service:
         
         nfsadmin client stop
         
         nfsadmin client start
         




### Map the `vol1` file share to the `nfs-client` instance

  1. Exit `PowerShell`:
         
         exit
         

  2. From `Command Prompt`, mount the file share to the `nfs-client` instance with the [`mount`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mount) command by specifying the IP address of the Filestore instance, the name of the file share, and the drive letter to mount to:
         
         mount -o mtype=hard 10.0.0.2:/vol1 z:
         




## Create a file on the mounted file share

###  Linux 

  1. In the `nfs-client` terminal window, create a file named `testfile` by running the following command:
         
         echo 'This is a test' > /mnt/test/testfile
         

  2. Confirm the file was created by running the following command and verifying that `testfile` is in the directory contents returned:
         
         ls /mnt/test
         




###  Windows 

  1. In the Command Prompt window of the `nfs-client` instance, create a file named `testfile`:
         
         echo 'This is a test' > Z:\testfile
         

  2. Confirm the file was created by running the following command:
         
         dir Z:
         

and verifying that `testfile` is in the directory contents returned.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

### Delete the Google Cloud project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the Filestore instance

Delete the `nfs-server` instance:
    
    
    gcloud filestore instances delete nfs-server --zone=us-central1-c
    

### Delete the Compute Engine instance

Delete the instance: 
    
    
    gcloud compute instances delete nfs-client

## What's next

  * Read the [Filestore Overview](https://docs.cloud.google.com/filestore) to learn more about the basics of Filestore.
  * Set up a Filestore instance on your own by following the instructions at [Creating Instances](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * Read [Access Control](https://docs.cloud.google.com/filestore/docs/access-control) to learn how to control access to Filestore operations and the resources on an instance.
  * See how to [copy data to or from a Filestore instance](https://docs.cloud.google.com/filestore/docs/copying-data).
  * See how to [transfer large datasets from Cloud Storage to Filestore](https://docs.cloud.google.com/filestore/docs/transfer-data-from-gcs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
