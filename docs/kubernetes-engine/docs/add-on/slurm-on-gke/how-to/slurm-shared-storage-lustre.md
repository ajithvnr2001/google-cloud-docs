---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-shared-storage-lustre/
title: Configure Managed Lustre shared storage for Slurm Operator add-on for GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:39.452442+00:00
---

# Configure Managed Lustre shared storage for Slurm Operator add-on for GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-shared-storage-lustre/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Configure Managed Lustre shared storage for Slurm Operator add-on for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Slurm Operator add-on for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to configure Google Cloud Managed Lustre shared storage for Slurm jobs on Google Kubernetes Engine (GKE). Shared storage is essential for Slurm clusters to help ensure that the Slurm login and worker nodes can access the same configuration files, scripts, and job data.

Before reading this document, ensure that you're familiar with the [Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Cloud Managed Lustre API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,lustre.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Set up the cluster

To use shared storage with Slurm, you need a GKE cluster with the Slurm Operator add-on for GKE enabled. In this section, you complete the following configuration steps:

  * Create a VPC network.
  * Set up a GKE cluster in the same VPC network as your Managed Lustre instance. You also set up OS Login for secure access and consistent user identification across the cluster, which is useful when sharing the `/home` directory.
  * Enable the Managed Lustre CSI driver on the cluster.



Complete the following steps to set up the cluster:

  1. Configure the VPC network by completing the steps in the [Set up a VPC network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/lustre-csi-driver-new-volume#vpc-setup) section.

  2. Create a GKE cluster with the Slurm Operator add-on for GKE and OS Login enabled. To create the cluster, complete the steps in [Deploy a Slurm cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke) and use the `--network` flag to specify the VPC network you created in the previous step.

  3. Enable the Managed Lustre CSI driver on the cluster:
         
         gcloud container clusters update CLUSTER_NAME \
             --location CONTROL_PLANE_LOCATION \
             --project PROJECT_ID \
             --update-addons=LustreCsiDriver=ENABLED
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
     * `PROJECT_ID`: your Google Cloud project ID.



When the Managed Lustre CSI driver is enabled, GKE automatically creates StorageClasses for provisioning Managed Lustre instances.

## Configure Managed Lustre

In this section, you use the StorageClasses to dynamically provision a volume through a PersistentVolumeClaim (PVC).

  1. Create Slurm namespace:
         
         kubectl create namespace slurm
         

  2. Create a manifest file named `lustre-pvc.yaml` to define the PVC:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: slurm-lustre-pvc
           namespace: slurm
         spec:
           accessModes:
           - ReadWriteMany
           resources:
             requests:
               storage: 72000Gi
           storageClassName: lustre-rwx-125mbps-per-tib
         

  3. Apply the manifest:
         
         kubectl apply -f lustre-pvc.yaml
         




## Use shared storage in Slurm configurations

After creating your PVC, you can configure the Slurm Operator resources to mount the shared storage.

### Configure Slurm login node and worker nodes

  1. Find an available image tag:

     1. In the Google Cloud console, go to the **Artifact Registry repository** page that includes the `slinky/slurmd` package.

[Go to Artifact Registry repository](https://console.cloud.google.com/artifacts/docker/gke-release/us/gcr.io/slinky%2Fslurmd)

     2. Annotate one of the image tag values, for example `25.11-ubuntu24.04-gke.4`. You use this tag in the `IMAGE_TAG` placeholder in the following configuration file.

  2. Save the following configuration to a file named `values.yaml`:
         
         controller:
           slurmctld:
             image:
               repository: gcr.io/gke-release/slinky/slurmctld
               tag: IMAGE_TAG
           reconfigure:
             image:
               repository: gcr.io/gke-release/slinky/slurmctld
               tag: IMAGE_TAG
         
         restapi:
           replicas: 1
           slurmrestd:
             image:
               repository: gcr.io/gke-release/slinky/slurmrestd
               tag: IMAGE_TAG
         
         nodesets:
           slinky:
             replicas: 1
             slurmd:
               image:
                 repository: gcr.io/gke-release/slinky/slurmd
                 tag: IMAGE_TAG
               volumeMounts:
                 - name: data-vol
                   mountPath: /data
             podSpec:
               nodeSelector:
                 cloud.google.com/gke-nodepool: NODE_POOL_NAME
               volumes:
               - name: data-vol
                 persistentVolumeClaim:
                   claimName: slurm-lustre-pvc
         
         loginsets:
           slinky:
             enabled: true
             replicas: 1
             login:
               image:
                 repository: gcr.io/gke-release/slinky/login
                 tag: IMAGE_TAG
               volumeMounts:
                 - name: data-vol
                   mountPath: /data
             podSpec:
               volumes:
               - name: data-vol
                 persistentVolumeClaim:
                   claimName: slurm-lustre-pvc
         

Replace the following:

     * `IMAGE_TAG`: the tag that you annotated in the previous step.
     * `NODE_POOL_NAME`: the name of the node pool where you want to deploy the Slurm worker Pods.
  3. Upgrade the Slurm chart by using the `values.yaml` file:
         
         helm upgrade slurm oci://ghcr.io/slinkyproject/charts/slurm \
           --version 1.0.2 \
           --namespace=slurm \
           -f values.yaml
         




## Verify shared storage

To verify that shared storage is mounted correctly, follow these steps:

  1. Check that the PVCs and PVs are bound:
         
         kubectl get pvc -n slurm
         

The output should show the status of all PVCs as `Bound` to their PVs.

  2. Connect to the Slurm login node by completing the steps in [Configure OS Login](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke#configure-os-login).

  3. On the login node, check the mount paths:
         
         df -h /data
         

  4. Check the mount paths on the worker nodes:
         
         srun -N 1 df -h /data
         




## Clean up

Clean up Slurm cluster and resources by following the directions in the [Clean up](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke#clean-up) section of Deploy a Slurm cluster on GKE.

## What's next

  * Learn more about [Managed Lustre on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
