---
url: https://docs.cloud.google.com/oracle/compute/quickstart-oracle-toolkit/
title: Quickstart: Use Oracle Toolkit for Google Cloud with Compute Engine \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:33.656063+00:00
---

# Quickstart: Use Oracle Toolkit for Google Cloud with Compute Engine  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/quickstart-oracle-toolkit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Use Oracle Toolkit for Google Cloud with Compute Engine

Learn how to get started with Oracle Toolkit for Google Cloud.

This quickstart shows you how to use Oracle Toolkit to create and run an Oracle database on a Compute Engine virtual machine (VM).

The instructions in this quickstart use Google Cloud CLI.

**Note:** This quickstart is an abridged version of the more comprehensive [Oracle Toolkit for Google Cloud - Compute Engine VM User Guide](https://google.github.io/oracle-toolkit/compute-vm-user-guide.html).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com

  14. [Create an auto mode Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network).
  15. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to host the Oracle software image.
  16. [Create a Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).
  17. Grant the following Identity and Access Management (IAM) role on the Cloud Storage bucket: 
     * [`roles/storage.objectViewer`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectViewer)

To learn how to grant IAM roles and permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 




## Create a Compute Engine VM

Create a Compute Engine VM to host the Oracle database.

Run the following command:
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --image-project=oracle-linux-cloud \
        --image-family=oracle-linux-8 \
        --metadata enable-oslogin=TRUE \
        --boot-disk-size=20GB \
        --create-disk size=DISK_SIZEGB,device-name=oracle-u01 \
        --create-disk size=DISK_SIZEGB,device-name=oracle-asm-data-1 \
        --create-disk size=DISK_SIZEGB,device-name=oracle-asm-reco-1
    

Replace the following:

  * VM_NAME: a name for the VM.
  * ZONE: the zone in which to create the VM.
  * MACHINE_TYPE: the machine type of the VM. See [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).
  * DISK_SIZE: the size, in gigabytes, of the disk. Acceptable sizes range, in 1 GB increments, from 10 GB to 65,536 GB inclusive.

The command creates three disks, namely `oracle-u01`, `oracle-asm-data-1`, and `oracle-asm-reco-1`.




## Download the Oracle Toolkit for Google Cloud

To download the Oracle Toolkit, run the following commands:
    
    
    python3 -m venv oracle-toolkit-venv
    source oracle-toolkit-venv/bin/activate
    pip3 install --upgrade pip
    pip3 install ansible-core==2.16.0 jmespath
    
    
    
    curl -L -o oracle-toolkit-master.zip https://github.com/google/oracle-toolkit/archive/refs/heads/master.zip && 
      unzip ./oracle-toolkit-master.zip && 
      rm ./oracle-toolkit-master.zip && 
      mv oracle-toolkit-master oracle-toolkit
      cd oracle-toolkit
    

## Download the Oracle software

[Download and stage the Oracle software](https://github.com/google/oracle-toolkit/blob/master/docs/user-guide.md#downloading-and-staging-the-oracle-software) that you need in the Cloud Storage bucket. The Oracle Toolkit doesn't contain any Oracle software. You are responsible for procuring the required Oracle software in accordance with the applicable licenses governing such software.

To download and stage the Oracle software, do the following:

  1. Obtain a list of required Oracle software download files. To verify the files for your required Oracle version, add the `--ora-version` argument.
         
         bash ./check-swlib.sh --ora-swlib-bucket gs://BUCKET_NAME --ora-version 19
         

Replace the following:

     * BUCKET_NAME: the name of your Cloud Storage bucket which hosts the Oracle software image.
  2. Download the missing files to your local machine:

     * Download patches (files starting with 'p') from [My Oracle Support](https://support.oracle.com).
     * Download base releases from [Oracle Software Delivery Cloud](https://edelivery.oracle.com) or [Oracle Technology Network](https://www.oracle.com/database/technologies/oracle-database-software-downloads.html).
**Note:** Both **My Oracle Support** and **Oracle Software Delivery Cloud** require Oracle support entitlements.
  3. Transfer the files to the Cloud Storage bucket. Also, in the bucket itself, disable the parallel composite uploads to let MD5 signatures be recorded for file integrity verification.
         
         gcloud storage cp *.zip gs://BUCKET_NAME --property=storage/parallel_composite_upload_enabled=False
         

  4. Verify that the required Oracle software is available in the bucket.
         
         bash ./check-swlib.sh --ora-swlib-bucket BUCKET_NAME
         




## Install the Oracle software and create an Oracle database

To install the Oracle software and create a database, do the following:

  1. Capture the OS login user profile.
         
         OS_LOGIN_USER=$(gcloud os-login describe-profile)
         

  2. Capture the IP address of your VM.
         
         INSTANCE_IP_ADDR=$(gcloud compute instances describe VM_NAME --zone=ZONE --format="value(networkInterfaces[0].networkIP)")
         

Replace the following:

     * VM_NAME: the name of the Compute Engine VM which you created earlier in this guide.
     * ZONE: the zone of the VM.
  3. Run the following command to install the software and create the database through a single command:
         
         bash ./install-oracle.sh \
          --instance-ip-addr $INSTANCE_IP_ADDR \
          --instance-ssh-user $OS_LOGIN_USER \
          --instance-ssh-key "$HOME/.ssh/google_compute_engine" \
          --ora-version 19 \
          --ora-swlib-bucket gs://BUCKET_NAME \
          --ora-swlib-path /u01/oracle_install \
          --ora-data-mounts-json '[{"purpose":"software","blk_device":"/dev/disk/by-id/google-oracle-u01","name":"u01","fstype":"xfs","mount_point":"/u01","mount_opts":"nofail"}]' \
          --ora-asm-disks-json '[{"diskgroup":"DATA","disks":[{"blk_device":"/dev/disk/by-id/google-oracle-asm-data-1","name":"DATA1"}]},{"diskgroup":"RECO","disks":[{"blk_device":"/dev/disk/by-id/google-oracle-asm-reco-1","name":"RECO1"}]}]' \
          --ora-db-name DATABASE_NAME
         

Replace the following:

     * BUCKET_NAME: the name of your Cloud Storage bucket which hosts the Oracle software image.
     * DATABASE_NAME: a name for your database. It must not be more than 8 characters, and must begin with an alphabetic character.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. Delete the Compute Engine VM:
         
         gcloud compute instances delete VM_NAME --zone=ZONE
         

Replace the following:

     * VM_NAME: the name of the Compute Engine VM which you created earlier in this guide.
     * ZONE: the zone of the VM.
  2. Delete the Cloud Storage bucket:

Use the `gcloud storage rm` command with the `--recursive` flag to delete the bucket and anything inside of it:
         
         gcloud storage rm gs://BUCKET_NAME --recursive

Replace the following:

     * BUCKET_NAME: the name of your Cloud Storage bucket.

If successful, the command returns a message similar to:
    
    Removing gs://BUCKET_NAME/...
    




## What's next

  * [User guide for Oracle Toolkit for Google Cloud - Compute Engine VM](https://google.github.io/oracle-toolkit/compute-vm-user-guide.html)
  * [User guide for Oracle Toolkit for Google Cloud](https://google.github.io/oracle-toolkit/user-guide.html)
  * [Oracle Toolkit for Google Cloud - disaster recovery configurations](https://google.github.io/oracle-toolkit/disaster-recovery-configurations.html)
  * [Terraform infrastructure provisioning for Oracle Toolkit for Google Cloud deployments](https://google.github.io/oracle-toolkit/terraform.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
