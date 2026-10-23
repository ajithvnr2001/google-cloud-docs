---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ct-lustre-tpu/
title: Provision Managed Lustre on GKE using Cluster Toolkit \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:04.175954+00:00
---

# Provision Managed Lustre on GKE using Cluster Toolkit  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ct-lustre-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Provision Managed Lustre on GKE using Cluster Toolkit Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to integrate Managed Lustre with GKE to create an optimized environment for demanding, data-intensive workloads like artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) by using [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

In this document, you provision a GKE cluster and a Managed Lustre instance declaratively with Cluster Toolkit, automatically configure the Managed Lustre CSI driver and Kubernetes PersistentVolume resources, and run a sample workload on the cluster.

This document is intended for Machine learning (ML) engineers and Data and AI specialists who are interested in exploring Kubernetes container orchestration capabilities backed by [Managed Lustre instances](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre). To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Background

This section describes the key technologies used in this document.

### Cluster Toolkit

Cluster Toolkit is an open-source tool that simplifies deploying and managing AI/ML and HPC environments on Google Cloud. Cluster Toolkit uses modular, declarative blueprints to automate the provisioning of GKE clusters, networks, compute accelerators, and high-performance storage.

For more information, see the [Cluster Toolkit overview](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

### Managed Lustre

Managed Lustre is a high-performance, parallel file system service designed for demanding workloads. The Managed Lustre CSI driver lets you integrate Managed Lustre instances with GKE, by using standard Kubernetes PersistentVolumeClaims (PVCs) and PersistentVolumes (PVs). This driver is particularly beneficial for AI/ML and HPC workloads requiring persistent, scalable, and high-throughput storage.

For more information, see [About the Managed Lustre CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre).

### Accelerator consumption options

[Flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) and Spot VMs let you optimize compute provisioning by paying only for the resources you need. For more information, see [About accelerator consumption options for AI/ML workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Cloud Managed Lustre API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,lustre.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Prepare your environment

  1. [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).

  2. Set your default environment variables and get the IP address of your deployment machine:
         
         gcloud config set project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export REGION=REGION
         export ZONE=ZONE
         export DEPLOYMENT_NAME=DEPLOYMENT_NAME
         export AUTHORIZED_CIDR="$(curl -s ifconfig.me)/32"
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region for your deployment, for example `us-central1`.
     * `ZONE`: a zone supporting Managed Lustre, for example `us-central1-a`.
     * `DEPLOYMENT_NAME`: the name for your deployment.



## Deploy the cluster and storage

  1. Deploy the infrastructure by using the [`examples/gke-managed-lustre.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-managed-lustre.yaml) blueprint from the Cluster Toolkit repository:
         
         gcluster deploy examples/gke-managed-lustre.yaml \
             --vars project_id=${PROJECT_ID},deployment_name=${DEPLOYMENT_NAME},region=${REGION},zone=${ZONE},authorized_cidr=${AUTHORIZED_CIDR}
         

Cluster Toolkit provisions the VPC, creates the Managed Lustre instance, provisions the GKE cluster with the Managed Lustre CSI driver enabled, and creates the Kubernetes PersistentVolume and PersistentVolumeClaim.

  2. Configure `kubectl` to access your new cluster:
         
         gcloud container clusters get-credentials ${DEPLOYMENT_NAME} \
             --zone=${ZONE} \
             --project=${PROJECT_ID}
         




## Run a workload with Managed Lustre

Submit a workload that mounts the Managed Lustre volume by using the `gcluster job submit` command. For more information about job submission options, see the [Cluster Toolkit Job Submission Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md).
    
    
    gcluster job submit \
        --name="test-lustre-$(date +%H%M)" \
        --cluster=${DEPLOYMENT_NAME} \
        --project=${PROJECT_ID} \
        --location=${ZONE} \
        --compute-type=n2-standard-16 \
        --image=ubuntu:latest \
        --command="df -h && echo 'Hello from Managed Lustre on GKE' > /lustre-data/hello.txt && cat /lustre-data/hello.txt" \
        --mount="gke-lustre-instance-pvc;/lustre-data;rw"
    

To inspect workload logs and execution status, use the `gcluster job logs` command:
    
    
    gcluster job logs "test-lustre-$(date +%H%M)" \
        --cluster=${DEPLOYMENT_NAME} \
        --project=${PROJECT_ID} \
        --location=${ZONE}
    

The output is similar to the following:
    
    
    Filesystem                Size  Used Avail Use% Mounted on
    overlay                   193G   11G  183G   6% /
    tmpfs                      64M     0   64M   0% /dev
    10.8.68.5@tcp://lustrefs   35T   22M   35T   1% /lustre-data
    shm                        64M     0   64M   0% /dev/shm
    Hello from Managed Lustre on GKE
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this document, delete the deployment by using Cluster Toolkit:
    
    
    gcluster destroy ${DEPLOYMENT_NAME}
    

## What's next

  * Learn more [about the Managed Lustre CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre).
  * Explore the [Cluster Toolkit blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog).
  * Learn how to [create a GKE storage class](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-storage).
  * Learn how to [create and use a volume backed by Managed Lustre](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/lustre-csi-driver-new-volume).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
