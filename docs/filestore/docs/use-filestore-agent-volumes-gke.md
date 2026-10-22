---
url: https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke/
title: Set up GKE environment for Filestore agent volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:22.891048+00:00
---

# Set up GKE environment for Filestore agent volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Set up GKE environment for Filestore agent volumes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

Filestore agent volumes integrate with Google Kubernetes Engine (GKE) to provide high-density, low-latency persistent file storage for stateful AI agent sandboxes, developer environments, and multi-agent workflows.

This guide walks you through the prerequisites needed to use Filestore agent volumes on GKE.

## Before you begin

  1. Complete the initial setup in [Set up Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites).
  2. Enable the GKE API:
         
         gcloud services enable container.googleapis.com \
             --project=PROJECT_ID
         

  3. Install the required components for `gcloud`:
         
         gcloud components install kubectl gke-gcloud-auth-plugin
         




## Create a GKE cluster

Create a GKE cluster connected to your Private Service Connect.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --network=projects/PROJECT_ID/global/networks/VPC_NETWORK \
        --subnetwork=SUBNET_NAME \
        --num-nodes=3 \
        --workload-pool=PROJECT_ID.svc.id.goog \
        --scopes=cloud-platform \
        --enable-agent-sandbox \
        --addons=GcpFilestoreCsiDriver=DISABLED \
        --cluster-version=1.36.0-gke.3302001
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `REGION`: the region where your volume pool resides, such as `us-central1`.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `VPC_NETWORK`: the name of your PSC-enabled VPC network.
  * `SUBNET_NAME`: the name of the subnet.



## Set up Workload Identity Federation for GKE and IAM

Give the Kubernetes ServiceAccount used by the CSI driver and the Compute Engine default service account permissions to provision Filestore volumes:

  1. Get your project number:
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"
         

Replace `PROJECT_ID` with your project ID.

  2. Grant the Cloud Filestore Editor role (`roles/file.editor`) on the project to the Kubernetes ServiceAccount (`gcp-filestore-csi-controller-sa`) in the `gcp-filestore-csi-driver` namespace:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/gcp-filestore-csi-driver/sa/gcp-filestore-csi-controller-sa" \
             --role="roles/file.editor" \
             --condition=None
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `PROJECT_NUMBER`: your Google Cloud project number.
  3. Grant the Cloud Filestore Editor role (`roles/file.editor`) on the project to the Compute Engine default service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/file.editor" \
             --condition=None
         




## Deploy the Filestore CSI driver

  1. Get cluster credentials:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --region=REGION \
             --project=PROJECT_ID
         

  2. Clone the driver repository and apply the `volumepool` overlay:
         
         git clone https://github.com/kubernetes-sigs/gcp-filestore-csi-driver.git
         cd gcp-filestore-csi-driver
         kubectl apply -k deploy/kubernetes/overlays/volumepool
         

  3. Verify that the CSI driver pods are running:
         
         kubectl get pods -n gcp-filestore-csi-driver
         

The output is similar to the following:
         
         NAME                             READY   STATUS    RESTARTS   AGE
         gcp-filestore-csi-controller-0   5/5     Running   0          2m
         gcp-filestore-csi-node-abcde     3/3     Running   0          2m
         




## Apply the `StorageClass` for your volume pool

To allow your GKE workloads to dynamically provision volumes from your volume pool, apply a Kubernetes `StorageClass` to your cluster.

If you already created the `volume-pool-sc.yaml` manifest in [Set up Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites#sample-storage-class), skip to step 2.

  1. Create a file named `volume-pool-sc.yaml` with the following configuration:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: volume-pool-sc
         provisioner: filestore.csi.storage.gke.io
         parameters:
           volume-pool: "projects/<var>PROJECT_ID</var>/locations/<var>LOCATION</var>/volumePools/<var>VOLUME_POOL_ID</var>"
         mountOptions:
           - vers=3
           - proto=tcp
           - mountproto=tcp
           - port=2049
           - mountport=2050
         volumeBindingMode: Immediate
         reclaimPolicy: Delete
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the region where your volume pool is deployed, such as `us-central1`.
     * `VOLUME_POOL_ID`: the identifier of your volume pool.
  2. Apply the manifest:
         
         kubectl apply -f volume-pool-sc.yaml
         

  3. Verify that the `StorageClass` is available:
         
         kubectl get storageclass volume-pool-sc
         

The output is similar to the following:
         
         NAME             PROVISIONER                    RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
         volume-pool-sc   filestore.csi.storage.gke.io   Delete          Immediate           true                   1m
         




After completing this guide, your GKE environment is ready to support Filestore agent volumes.

## What's next

With your GKE cluster and storage class configured, you can deploy stateful AI agent workloads using any of the following orchestration patterns:

  * Deploy workloads using [GKE Agent Substrate](https://docs.cloud.google.com/filestore/docs/agent-substrate).
  * Deploy workloads using [GKE Agent Sandbox](https://docs.cloud.google.com/filestore/docs/agent-sandbox).
  * Configure dynamic [storage late-binding](https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind).
  * Deploy self-managed [GKE workloads](https://docs.cloud.google.com/filestore/docs/self-managed-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
