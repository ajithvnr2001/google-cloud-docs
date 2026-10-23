---
url: https://docs.cloud.google.com/workstations/docs/mount-filestore-nfs-instances/
title: Mount Filestore instances in Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:43.823251+00:00
---

# Mount Filestore instances in Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/mount-filestore-nfs-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Mount Filestore instances in Cloud Workstations Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Workstations can mount [Filestore](https://docs.cloud.google.com/filestore/docs/overview) Network File System (NFS) instances that are in the same VPC network. The Filestore instance can be accessed by multiple Cloud Workstations instances at the same time.

For more information about Filestore, see the [Filestore documentation](https://docs.cloud.google.com/filestore/docs).

## Before you begin

Before you begin, create your project and set up required IAM roles.

### Create your project

  1. In your _workstations project_ , make sure that you have enabled the Filestore API and Cloud Workstations APIs.

[Enable Filestore and Cloud Workstations APIs](https://console.cloud.google.com/start/api?id=file.googleapis.com,workstations.googleapis.com)

  2. Make sure that you install and initialize the [`gcloud` CLI](https://docs.cloud.google.com/sdk/docs/install). To [initialize the `gcloud` CLI](https://docs.cloud.google.com/sdk/docs/initialize), run the following command:
         
         gcloud init
         




### Required roles

To get the permissions that you need to create and update workstations, ask your administrator to grant you the following IAM roles on your workstations project: 

  * If you are the _Cloud Workstations Admin_ , ask your administrator to grant you the following role: Cloud Workstations Admin (`roles/workstations.admin`). 
  * If you are the _Filestore Admin_ , ask your administrator to grant you the following role: Filestore Editor (`roles/file.editor`). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Filestore instance

If you have not yet created a Filestore instance, create one using the `gcloud` CLI [`filestore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/create) command that follows. For naming information, see [Naming your Filestore instance](https://docs.cloud.google.com/filestore/docs/creating-instances#naming_your_instance) and [Naming the file share](https://docs.cloud.google.com/filestore/docs/creating-instances#naming_the_file_share).

**Important:** We recommend Filestore ENTERPRISE tier because it provides regional availability that matches with Cloud Workstations availability.
    
    
      gcloud filestore instances create INSTANCE_ID \
        --file-share=name=FILE_SHARE_NAME,capacity=1TiB \
        --tier=ENTERPRISE \
        --network=name=NETWORK_NAME \
        --region=LOCATION \
        --project WORKSTATIONS_PROJECT_ID
    

Replace the following:

  * `INSTANCE_ID`: the ID to uniquely identify your Filestore instance.
  * `FILE_SHARE_NAME`: the name of the directory served from the Filestore instance—for example, `vol1`.
  * `NETWORK_NAME`: the name of the VPC network to which the instance is connected. It should match the network of Cloud Workstations cluster—for example, `default`.
  * `LOCATION`: the region of your Filestore instance. It should match the region of the workstation cluster.
  * `WORKSTATIONS_PROJECT_ID`: the ID of your workstations project.

**Note:** If you want to use a tier other than ENTERPRISE tier, pass `--zone` flag instead of `--region` flag. For example, if your workstation cluster is in `us-central1` region, you can create a Filestore instance in `us-central1-a` zone.

### Get IP address of Filestore instance

After the Filestore instance is created, get its IP address using the [filestore instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/describe) `gcloud` CLI command:
    
    
      gcloud filestore instances describe INSTANCE_ID \
        --region=LOCATION \
        --project WORKSTATIONS_PROJECT_ID
    

Replace the following:

  * `INSTANCE_ID`: the ID to uniquely identify your Filestore instance.
  * `LOCATION`: the region of your Filestore instance. It should match the region of the workstation cluster.
  * `WORKSTATIONS_PROJECT_ID`: the ID of your workstations project.



The command prints the IP address in the following format:
    
    
    ...
    networks:
    - connectMode: DIRECT_PEERING
      ipAddresses:
      - FILESTORE_IP_ADDRESS
    ...
    

Make a note of the `FILESTORE_IP_ADDRESS` because you need this in subsequent steps.

## Create workstation cluster

If you have not yet created a workstation cluster, create one using the `gcloud` CLI [`clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/clusters/create) command:
    
    
    gcloud workstations clusters create \
        WORKSTATIONS_CLUSTER_NAME \
        --network=NETWORK_NAME \
        --region=LOCATION \
        --project=WORKSTATIONS_PROJECT_ID
    

Replace the following:

  * `WORKSTATIONS_CLUSTER_NAME`: the name of the workstation cluster.
  * `NETWORK_NAME`: the name of the VPC network to which the Cloud Workstations instances are connected. It should match the network of the Filestore instance—for example, `default`.
  * `LOCATION`: the region name for your workstation cluster. It should match the region of the Filestore instance.
  * `WORKSTATIONS_PROJECT_ID`: the ID of your workstations project.



## Create a workstation configuration and a workstation

If you have not yet created a Cloud Workstations configuration and a workstation instance, see [Create a workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration) and [Create a workstation](https://docs.cloud.google.com/workstations/docs/create-workstation).

## Mount a Filestore instance in a workstation

After you launch Cloud Workstations instance, go to a terminal window and run the following commands to mount a Filestore instance:
    
    
    sudo rpcbind
    mkdir -p FILE_SHARE_NAME
    sudo mount -o rw,intr FILESTORE_IP_ADDRESS:/FILE_SHARE_NAME FILE_SHARE_NAME
    

Replace the following:

  * `FILE_SHARE_NAME`: the name of the directory served from the Filestore instance—for example, `vol1`.
  * `FILESTORE_IP_ADDRESS`: the IP address of your Filestore instance.



After the `mount` command is successful, you see the Filestore instance contents in the file share path.

For more information about mounting Filestore instances, see [Mounting file shares on Compute Engine clients](https://docs.cloud.google.com/filestore/docs/mounting-fileshares).

## Create a custom container image for Filestore automount

You can use the following Dockerfile to create a custom container image which mounts a Filestore instance in Cloud Workstations automatically on startup.
    
    
    FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest
    
    RUN echo "#!/bin/bash\n\
    sudo rpcbind\n\
    sudo mkdir -p /home/user/FILE_SHARE_NAME\n\
    sudo mount -o rw,intr FILESTORE_IP_ADDRESS:/FILE_SHARE_NAME /home/user/FILE_SHARE_NAME" | sudo tee -a /etc/workstation-startup.d/011_mount-filestore.sh
    
    RUN sudo chmod +x /etc/workstation-startup.d/011_mount-filestore.sh
    

Replace the following:

  * `FILE_SHARE_NAME`: the name of the directory served from the Filestore instance—for example, `vol1`.
  * `FILESTORE_IP_ADDRESS`: the IP address of your Filestore instance.



For more information about creating a custom container image for Cloud Workstations, see [Customize container images](https://docs.cloud.google.com/workstations/docs/customize-container-images).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
