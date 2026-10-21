---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance/
title: Set up and access Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:08.376108+00:00
---

# Set up and access Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Set up and access Mainframe Assessment Tool Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and access Mainframe Assessment Tool. Mainframe Assessment Tool can be deployed either as a virtual machine (VM) instance, or on a Google Kubernetes Engine cluster. You can only upgrade Mainframe Assessment Tool instances deployed as a VM instance.

After you deploy Mainframe Assessment Tool, you can connect to and interact with the web-based graphical user interface to analyze your mainframe applications.

## Before you begin

Complete the steps to [prepare for discovery and assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/prepare-for-assessment).

## Option 1: Set up Mainframe Assessment Tool VM instance

To set up a Mainframe Assessment Tool VM instance, follow these steps:

  1. In the Google Cloud console, click ![Activate Shell Button](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell**.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. To create a Mainframe Assessment Tool VM instance, run the following command:
         
         gcloud compute instances create mainframe-assessment-tool-1-instance \
           --machine-type=MACHINE_TYPE \
           --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  \
           --scopes=cloud-platform --image-project=migrate-modernize-public \
           --image-family=mainframe-assessment-tool --zone=ZONE \
           --boot-disk-size=DISK_SIZE
         

Replace the following:

     * MACHINE_TYPE: the machine type of the VM.
     * SERVICE_ACCOUNT_NAME: the name of the dedicated service account that you created.
     * PROJECT_ID: your Google Cloud project ID.
     * DISK_SIZE: the size of the boot disk.
     * ZONE: the zone where you want to create the VM. All [Google model endpoint locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#google-models) are supported.

Use the following table to determine the values for MACHINE_TYPE and DISK_SIZE based on the expected size of your assessment data.

Assessment zip file size | MACHINE_TYPE | DISK_SIZE  
---|---|---  
**Smaller than 5MB** | e2-standard-4 | 100GB  
**Between 5MB and 50MB** | e2-standard-8 | 100GB  
**Larger than 50MB, or multiple assessments in parallel** | e2-highmem-16 | 300GB  
  
If you've configured the firewall in your project to allow IAP tunnels only for VMs with certain network tags, then you can also add the network tags using the `--tags` flag. For example, `--tags=assessment-iap`.

If your project already has a working [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) setup, add the `--no-address` flag to the `gcloud` command that creates the VM.




### Access Mainframe Assessment Tool VM from your computer

You can access Mainframe Assessment Tool from your Linux, macOS, or Windows-based computer by using Google Cloud CLI through an Identity-Aware Proxy tunnel.

To create an encrypted tunnel to a port of Mainframe Assessment Tool VM instance, run the following command:
    
    
       gcloud compute start-iap-tunnel VM_NAME 4000 --zone=ZONE \
         --local-host-port=localhost:LOCAL_PORT --project=PROJECT_ID
    

Replace the following:

  * VM_NAME: the name of the VM.
  * ZONE: the VM zone.
  * LOCAL_PORT: any port number on your local machine that you want to use for the tunneled connection to the Mainframe Assessment Tool.
  * PROJECT_ID: the project ID of the VM project.



Google Cloud CLI performs a connectivity test with the VM instance, then opens a tunnel and shows a port number as follows:
    
    
       Listening on port 6060.
    

All traffic sent to `localhost:LOCAL_PORT` is forwarded to the Mainframe Assessment Tool VM instance. The port is only accessible by applications running on your local computer.

To access Mainframe Assessment Tool from your local computer, open a web browser and go to `localhost:LOCAL_PORT`.

## Option 2: Deploy Mainframe Assessment Tool on a GKE cluster

To deploy Mainframe Assessment Tool on a GKE cluster, follow these steps:

  1. In the Google Cloud console, click ![Activate Shell Button](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell**.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Enable the [Google Kubernetes Engine API](https://console.cloud.google.com/apis/library/container.googleapis.com) for your Google Cloud project.

  3. If a GKE cluster does not already exist in your project, [create a GKE cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) and make sure that the workload identity pool is configured.

To create a GKE cluster, run the following command:
         
         gcloud container clusters create CLUSTER_NAME \
           --project=PROJECT_ID \
           --zone=ZONE \
           --machine-type=MACHINE_TYPE \
           --enable-ip-alias \
           --release-channel="stable" \
           --workload-pool=PROJECT_ID.svc.id.goog \
           --disk-size=DISK_SIZE
         

Replace the following:

     * CLUSTER_NAME: the name of the new GKE cluster
     * PROJECT_ID: your Google Cloud project ID.
     * MACHINE_TYPE: the machine type of each node.
     * ZONE: the zone where you want to create the cluster. All [Google model endpoint locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#google-models) are supported.
     * DISK_SIZE: the size of the boot disk.

Use the following table to determine the values for MACHINE_TYPE and DISK_SIZE based on the expected size of your assessment data:

Assessment zip file size | MACHINE_TYPE | DISK_SIZE  
---|---|---  
**Smaller than 5MB** | e2-standard-4 | 100GB  
**Between 5MB and 50MB** | e2-standard-8 | 100GB  
**Larger than 50MB, or multiple assessments in parallel** | e2-highmem-16 | 300GB  
  
  4. [Enable Workload Identity Federation for GKE on clusters and node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools).

**Note:** In GKE Autopilot, Workload Identity Federation is always enabled.
  5. In your environment, create a directory for the deployment scripts:
         
         mkdir DESTINATION_DIRECTORY
         

Replace `DESTINATION_DIRECTORY` with a name for the directory.

  6. To download the deployment scripts, run the following command:
         
         gcloud storage cp "gs://mainframe-ai-release/mat/VERSION/kustomize_deployment.zip" DESTINATION_DIRECTORY
         

Replace the following:

     * VERSION: the version of Mainframe Assessment Tool that you want to install, for example, `mainframe-assessment-2-8-0`.
     * DESTINATION_DIRECTORY: the destination directory on your machine where the script is downloaded.
  7. To bind your Google Cloud service account (GSA) to the Kubernetes service account (KSA), run the following command:
         
         gcloud iam service-accounts add-iam-policy-binding \
         SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
         --role="roles/iam.workloadIdentityUser" \
         --member="serviceAccount:PROJECT_ID.svc.id.goog[VERSION/mat-service-account]"
         

Replace the following:

     * PROJECT_ID: your Google Cloud project ID.
     * VERSION: the version of Mainframe Assessment Tool, for example, `mainframe-assessment-2-8-0`.
**Note:** Although granting Identity and Access Management (IAM) roles directly to a Kubernetes ServiceAccount principal (`principal://`) is the recommended best practice for [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), Mainframe Assessment Tool requires IAM service account impersonation because the `deploy.sh` deployment script requires an IAM service account email address and annotates the `mat-service-account` Kubernetes ServiceAccount with `iam.gke.io/gcp-service-account`.
  8. Grant read, write, and execute permissions on the destination directory:
         
         chmod -R u+rwx DESTINATION_DIRECTORY
         

  9. Extract the downloaded scripts:
         
         cd DESTINATION_DIRECTORY && unzip kustomize_deployment.zip
         

Replace DESTINATION_DIRECTORY with the directory where you downloaded the deployment scripts.

  10. To create the containers and deploy Mainframe Assessment Tool, run the following command:
         
         ./deploy.sh PROJECT_ID ZONE \
         CLUSTER_NAME VERSION \
         us-docker.pkg.dev/migrate-modernize-public/mainframe-assessment-prod \
         SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         




The containers should be operational within a few minutes.

The MCP server is disabled by default. For instructions on how to enable the server on this deployment, see [Enable the MCP server on a GKE cluster](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server#enable-mcp-gke).

### Access GKE-deployed Mainframe Assessment Tool from your computer

You can access Mainframe Assessment Tool from your Linux, macOS, or Windows computer by using the `kubectl` command to configure port forwarding.

To create encrypted port forwarding, follow these steps:

  1. To configure access to the cluster, run the following command:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
          --zone ZONE --project PROJECT_ID
         

  2. To configure port forwarding, run the following command:
         
         kubectl port-forward service/assessor-frontend LOCAL_PORT:4000 -n VERSION
         

Replace the following:

     * LOCAL_PORT: a port number on your local machine used for the tunneled connection to Mainframe Assessment Tool. We recommend using `8080`, `8000`, or `3000`. If these ports are unavailable, use any port number higher than 1024, for example, `3001`.
     * VERSION: the version of Mainframe Assessment Tool deployed on the GKE cluster.



## What's next

  * Learn how to [configure settings for Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
