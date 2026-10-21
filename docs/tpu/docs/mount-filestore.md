---
url: https://docs.cloud.google.com/tpu/docs/mount-filestore/
title: Mount a Filestore instance to Cloud TPU VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:23.665889+00:00
---

# Mount a Filestore instance to Cloud TPU VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/mount-filestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mount a Filestore instance to Cloud TPU VMs

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

Filestore is a fully managed network attached storage (NAS) for Compute Engine. Filestore offers native compatibility with existing enterprise applications and supports any NFSv3-compatible client.

## Before you begin

In order to mount a Filestore instance on your Cloud TPU VM, you need to add a Filestore role (Cloud Filestore Editor or Cloud Filestore Viewer) to the service account associated with your Cloud TPU VM. If you don't specify a custom service account when you create a Cloud TPU VM, your Cloud TPU VM uses the default Compute Engine service account. For more information about how to specify a service account when creating a Cloud TPU VM, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#prepare-to-request). For more information about how to create a service account, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

### Add the Filestore Editor role to a service account

The following instructions show you how to add the Cloud Filestore Editor role to the Compute Engine default service account. You can follow these instructions to add the Cloud Filestore Editor role to any service account. You can search and use a custom service account instead of the Compute Engine default service account in step 2.

  1. Open the [IAM console](https://console.cloud.google.com/iam-admin/iam).

  2. Select the **View by principals** tab and type `Name:Compute Engine default service account` in the **Filter** field.

  3. Click edit next to the service account. The IAM console displays a dialog listing the roles assigned to the Compute Engine default service account.

  4. Click add to add another role.

  5. Expand the **Select a role** drop down menu, type `Filestore` in the filter, and select **Cloud Filestore editor**.

  6. Click **Save** to dismiss the dialog. You have added the Filestore Editor role to the Compute Engine default service account.




For more information about service accounts, see [Service Account Overview](https://docs.cloud.google.com/iam/docs/service-account-overview). To learn more about IAM roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).

### Create a Filestore instance

Create a Filestore instance using the instructions found in [Creating Filestore instances](https://docs.cloud.google.com/filestore/docs/creating-instances).

## Mount a Filestore instance on a Cloud TPU VM

The commands you use to mount a Filestore instance on a Cloud TPU depends on whether you are using a single Cloud TPU or a Cloud TPU slice.

### Mount a Filestore instance on a single Cloud TPU VM

  1. Connect to your Cloud TPU VM using SSH. 
         
         gcloud compute tpus tpu-vm ssh your-tpu-name \
                 --zone=your-zone
             

  2. Install the `nfs-common` package. 
         
         (vm)$ sudo apt-get update --allow-releaseinfo-change \
                 && sudo apt-get -y update \
                 && sudo apt-get -y install nfs-common
             

  3. Create a directory in which to mount NFS 
         
         (vm)$ sudo mkdir -p mount-dir \
                 && sudo chmod ugo+rw mount-dir
             

  4. Find the IP address of the Filestore. 
         
         (vm)$ gcloud filestore instances describe filestore-instance-name \
                 --location filestore-region
             

  5. Mount Filestore instance on your Cloud TPU VM onto your mount directory. Replace `filestore-ip`, `file-share-name`, `mount-dir` with your FileStore IP address, file share name, and mount directory. 
         
         (vm)$ sudo mount filestore-ip:file-share-name mount-dir
             




### Mount a Filestore instance on a Cloud TPU slice

Cloud TPU slices are composed of 2 or more Cloud TPU VMs. The following commands use the `gcloud compute tpus tpu-vm ssh` command with the `--worker=all` and `--command` flags to run the commands on all Cloud TPU VMs at one time.

  1. Install the `nfs-common` package on all Cloud TPU VMs in your slice. 
         
         gcloud compute tpus tpu-vm ssh your-tpu-name \
                   --project=your-gcp-project \
                   --zone=your-zone \
                   --worker=all \
                   --command="sudo apt-get update --allow-releaseinfo-change && sudo apt-get -y update && sudo apt-get -y install nfs-common"
               

  2. Create a directory in which to mount the Filestore instance. Replace `mount-dir` with a directory name of your choice. 
         
         gcloud compute tpus tpu-vm ssh your-tpu-name \
                 --project=your-gcp-project \
                   --zone=your-zone \
                   --worker=all \
                   --command="sudo mkdir -p mount-dir && sudo chmod ugo+rw mount-dir"
               

  3. Find the IP address of the Filestore instance. 
         
         gcloud filestore instances describe filestore-instance-name \
                 --location filestore-region
             

  4. Mount Filestore instance on your Cloud TPU slice. Replace `filestore-ip`, `file-share-name`, `mount-dir` with your FileStore IP address, file share name, and mount directory. 
         
         gcloud compute tpus tpu-vm ssh your-tpu-name \
                 --project=your-gcp-project \
                   --zone=your-zone \
                   --worker=all \
                   --command="sudo mount filestore-ip:file-share-name mount-dir"
               




## Writing data to Filestore instance

Make sure you grant Linux read and write permissions on the directory in which you mount the Filestore instance. You can use the directory as you would your local file system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
