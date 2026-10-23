---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-shared-storage-filestore/
title: Configure Filestore for Slurm Operator add-on for GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:45.231983+00:00
---

# Configure Filestore for Slurm Operator add-on for GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-shared-storage-filestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Configure Filestore for Slurm Operator add-on for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Slurm Operator add-on for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document show you how to configure Filestore shared storage for Slurm jobs on Google Kubernetes Engine (GKE). Shared storage is essential for Slurm clusters to to help ensure that the Slurm login and worker nodes can access the same configuration files, scripts, and job data.

Before reading this document, ensure that you're familiar with the [Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Cloud Filestore API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,file.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Set up the cluster

To use shared storage with Slurm, you need a GKE cluster with the Slurm Operator add-on for GKE enabled. In this section, you set up a GKE cluster. You also set up OS Login for secure access and consistent user identification across the cluster.

  1. Grant the `roles/file.editor` role to the service account that your cluster uses. If your nodes use the Compute Engine default service account, run the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role roles/file.editor
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `PROJECT_NUMBER`: your project number.
  2. Create a GKE cluster with the Slurm Operator add-on for GKE and OS Login enabled. To create the cluster, complete the steps in [Deploy Slurm on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke).

  3. Enable the Filestore CSI driver on the cluster:
         
         gcloud container clusters update CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --update-addons=GcpFilestoreCsiDriver=ENABLED
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



## Configure Filestore

To use Filestore as shared storage for your Slurm cluster, you must enable the [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/filestore-for-gke) and create a PersistentVolume (PV) and PersistentVolumeClaim (PVC).

  1. Create a Filestore instance:
         
         gcloud filestore instances create INSTANCE_NAME \
             --zone=INSTANCE_ZONE \
             --tier=BASIC_HDD \
             --file-share=name="SHARE_NAME",capacity=1TB \
             --network=name="default"
         

Replace the following:

     * `INSTANCE_NAME`: the name of your new instance.
     * `INSTANCE_ZONE`: the zone of your Filestore instance. If you're using a regional cluster, use a zone in its region. If you're using a zonal cluster, use the same zone as the cluster.
     * `SHARE_NAME`: the name of the file share.
  2. Annotate the values for the `INSTANCE_IP` field that's needed for the manifest:
         
         gcloud filestore instances describe INSTANCE_NAME \
             --zone=INSTANCE_ZONE \
             --format="table(networks[0].ipAddresses[0])"
         

Replace the following:

     * `INSTANCE_NAME`: the name of your Filestore instance.
     * `INSTANCE_ZONE`: the zone of your Filestore instance.

The output includes the `INSTANCE_IP` value. You use this value in the manifest in the following step.

  3. To define the PV and PVC, create a manifest file named `filestore-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: PV_NAME
         spec:
           storageClassName: ""
           capacity:
             storage: 1Ti
           accessModes:
             - ReadWriteMany
           persistentVolumeReclaimPolicy: Retain
           volumeMode: Filesystem
           csi:
             driver: filestore.csi.storage.gke.io
             volumeHandle: "modeInstance/INSTANCE_ZONE/INSTANCE_NAME/SHARE_NAME"
             volumeAttributes:
               ip: INSTANCE_IP
               volume: SHARE_NAME
         ---
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: PVC_NAME
           namespace: slurm
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: ""
           resources:
             requests:
               storage: 1Ti
           volumeName: PV_NAME
         

Replace the following:

     * `PV_NAME`: the name of your PersistentVolume.
     * `PVC_NAME`: the name of your PersistentVolumeClaim.
     * `INSTANCE_ZONE`: the zone of your Filestore instance.
     * `INSTANCE_NAME`: the name of your Filestore instance.
     * `SHARE_NAME`: the name of the file share.
     * `INSTANCE_IP`: the IP address of the Filestore instance that you retrieved earlier.
  4. Create the `slurm` namespace:
         
         kubectl create namespace slurm
         

  5. Apply the manifest:
         
         kubectl apply -f filestore-pvc.yaml
         




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
                 - name: home-vol
                   mountPath: /home
             podSpec:
               nodeSelector:
                 cloud.google.com/gke-nodepool: NODE_POOL_NAME
               tolerations:
                 - key: "slurm-worker"
                   operator: "Equal"
                   value: "true"
                   effect: "NoSchedule"
               volumes:
               - name: home-vol
                 persistentVolumeClaim:
                   claimName: slurm-shared-storage-pvc
         
         loginsets:
           slinky:
             enabled: true
             replicas: 1
             login:
               image:
                 repository: gcr.io/gke-release/slinky/login
                 tag: IMAGE_TAG
               volumeMounts:
                 - name: home-vol
                   mountPath: /home
             podSpec:
               volumes:
               - name: home-vol
                 persistentVolumeClaim:
                   claimName: slurm-shared-storage-pvc
         

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
         
         df -h /home
         

  4. Check the mount paths on the worker nodes:
         
         srun -N 1 df -h /home
         




## Clean up

  1. Clean up Slurm cluster and resources by following the directions in the [Clean up](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke#clean-up) section of Deploy a Slurm cluster on GKE.

  2. Delete the Filestore instance:
         
         gcloud filestore instances delete INSTANCE_NAME --zone=INSTANCE_ZONE --quiet
         

Replace `INSTANCE_NAME` with the name of your Filestore instance and `INSTANCE_ZONE` with its zone.




## What's next

  * Learn more about [Filestore on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
