---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/multi-slice-training-ray/
title: Multislice and elastic training on TPUs using Ray Train on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:17.737733+00:00
---

# Multislice and elastic training on TPUs using Ray Train on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/multi-slice-training-ray/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Multislice and elastic training on TPUs using Ray Train on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to train large language models (LLMs) like Llama 3 70B on Google Kubernetes Engine (GKE) using [MaxText](https://github.com/google/maxtext), [Ray Train](https://docs.ray.io/en/latest/train/train.html), and Multislice [Trillium TPUs](https://docs.cloud.google.com/tpu/docs/v6e). This tutorial provides a complete, end-to-end walkthrough, from configuring the necessary secondary data center networking to submitting and successfully running a distributed training workload across 32 physical TPU chips.

This tutorial is for Platform admins, operators, and AI specialists who want to learn how to overcome the memory and networking challenges of training 70-billion parameter models on distributed, multi-host TPU slices.

## Background

The combination of GKE, KubeRay, MaxText, and TPUs provides a powerful and scalable platform for large-scale model training. This section describes the key technologies used in this guide:

### JAX

[JAX](https://github.com/jax-ml/jax) is a Python library for accelerator-oriented array computation and program transformation, utilizing the XLA compiler to create highly optimized code that scales efficiently on accelerators.

### MaxText

[MaxText](https://github.com/google/maxtext) is a high-performance, open-source LLM framework designed for scalability and customizability. MaxText is built on top of JAX and is optimized to run efficiently on Cloud TPUs.

### TPUs

[Tensor Processing Units](https://cloud.google.com/tpu) (TPUs) are custom-designed accelerators created by Google to optimize machine learning workloads. Unlike general-purpose CPUs or parallel-processing GPUs, TPUs are highly specialized for the massive matrix and tensor computations at the foundation of deep learning, making them efficient at this specific task. The primary advantage of TPUs is performance at scale.

This tutorial uses [TPU Trillium](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#trillium-benefits), the sixth generation of TPUs, in a Multislice deployment pattern. Cloud TPU Multislice is where two or more Cloud TPU slices communicate over the data center network (DCN). Multislice enables full-stack, cost-effective, large scale training with near-linear scaling up to tens of thousands of TPU chips. For more information about Multislice, see [Cloud TPU Multislice Overview](https://docs.cloud.google.com/tpu/docs/multislice-introduction).

### KubeRay

[KubeRay](https://github.com/ray-project/kuberay) is a Kubernetes operator that provides a unified way to deploy, manage, and monitor Ray applications on Kubernetes. The KubeRay operator is installed and managed through the [Ray on GKE add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview), which is the recommended way to deploy and manage Ray clusters on GKE.

### GKE Dynamic Resource Allocation Network (DRANET)

[GKE DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra) (Dynamic Resource Allocation Network) is a feature that dynamically attaches high-performance network devices to Pods, bypassing standard Kubernetes networking and enabling high performance over the DCN.

## Objectives

This tutorial shows you how to do the following:

  1. Set up a GKE cluster with two multi-host TPU node pools.
  2. Configure a secondary DCN for cross-slice TPU communication.
  3. Configure KubeRay to manage the distributed training environment.
  4. Deploy a RayCluster custom resource by using Dynamic Resource Allocation (DRA) for network attachments.
  5. Create a Python training script by utilizing Ray Train's JaxTrainer to orchestrate the MaxText training loop across the TPU slices.
  6. Run a baseline Llama 3 8B training job.
  7. Scale up to Llama 3 70B utilizing 2D sharding (Tensor Parallelism and FSDP) over the DCN.



## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
        
        gcloud init

  * [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable container.googleapis.com cloudbuild.googleapis.com

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
        
        gcloud init

  * [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable container.googleapis.com cloudbuild.googleapis.com

  * Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.admin, roles/iam.serviceAccountAdmin, roles/cloudbuild.builds.editor`
        
        gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

    * `PROJECT_ID`: Your project ID.
    * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
    * `ROLE`: The IAM role that you grant to your user account.


  * Because this tutorial utilizes TPU Trillium (v6e), select a region or zone with availability. For more information, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).



## Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell). Cloud Shell comes preinstalled with the `gcloud`, `helm`, and `kubectl` command-line tools that are used in this tutorial.

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. At the top of the Google Cloud console window, click the **Activate Cloud Shell** ![Activate Shell
Button](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png) button.

A Cloud Shell session opens inside a new frame in the Google Cloud console and displays a command-line prompt.

  3. In your terminal, clone the `kubernetes-engine-samples` repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         

  4. Change to the directory containing the sample files:
         
         cd kubernetes-engine-samples/ai-ml/gke-ray/raytrain/maxtext
         

  5. Create and activate a Python virtual environment:
         
         python3 -m venv ray-env
         source ray-env/bin/activate
         

  6. Install the Ray CLI:
         
         pip install "ray[default]==2.55.0"
         

  7. Set the following environment variables:
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export GS_BUCKET=GS_BUCKET
         export KSA_NAME=KSA_NAME
         export NAMESPACE=default
         export CLUSTER_NAME=CLUSTER_NAME
         export REGION=REGION
         export ZONE=ZONE
         export CLUSTER_VERSION=1.35.2-gke.1842000
         

Replace the following:

     * `GS_BUCKET`: the name of the Cloud Storage bucket.
     * `KSA_NAME`: the name of the Kubernetes Service Account.
     * `CLUSTER_NAME`: the name of the new cluster.
     * `REGION`: the region where your TPU Trillium capacity is available.
     * `ZONE`: the zone where your TPU Trillium capacity is available. For more information, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).



## Configure cluster networking for Cloud TPU Multislice

Within a multi-host TPU slice, TPU devices communicate over the high-speed inter-chip interconnects. However, when running Multislice jobs, the TPU slices must communicate with each other over the DCN. Standard Kubernetes Pod networks can bottleneck this traffic. The `ct6e-standard-4t` machine type is backed by multiple physical network interface cards (NICs). To achieve the best performance, you create two additional VPC networks and use GKE DRANET to connect them directly to the Ray Pods.

  1. Create the two additional VPC networks with a large maximum training unit (MTU):
         
         gcloud compute networks create ${CLUSTER_NAME}-net-1 \
           --subnet-mode=custom \
           --mtu=8896
         
         gcloud compute networks create ${CLUSTER_NAME}-net-2 \
           --subnet-mode=custom \
           --mtu=8896
         

  2. Create the dedicated subnets:
         
         gcloud compute networks subnets create tpu-subnet-1 \
           --network=${CLUSTER_NAME}-net-1 \
           --region=${REGION} \
           --range=10.50.0.0/16
         
         gcloud compute networks subnets create tpu-subnet-2 \
           --network=${CLUSTER_NAME}-net-2 \
           --region=${REGION} \
           --range=10.60.0.0/16
         




## Create a GKE cluster

You can configure KubeRay on TPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

To use GKE managed DRANET, your cluster must use version 1.35.2-gke.1842000 or later for Autopilot mode, or 1.34.1-gke.1829001 or later for Standard mode. This tutorial uses version 1.35.2-gke.1842000.

### Autopilot

  1. In Cloud Shell, run the following command:
         
         gcloud container clusters create-auto $CLUSTER_NAME \
             --enable-ray-operator \
             --machine-type=n1-standard-16 \
             --location=$REGION \
             --cluster-version=${CLUSTER_VERSION}
         

  2. To communicate with your cluster, configure `kubectl` :
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=$REGION
         




### Standard

  1. In Cloud Shell, create a Standard cluster that enables the [Ray operator](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview) add-on by running the following command:
         
         gcloud container clusters create $CLUSTER_NAME \
             --addons=RayOperator,GcsFuseCsiDriver \
             --machine-type=n1-standard-16 \
             --enable-dataplane-v2 \
             --workload-pool=$PROJECT_ID.svc.id.goog \
             --location=$ZONE \
             --cluster-version=${CLUSTER_VERSION}
         

This command also enables the `GcsFuseCsiDriver`, which allows Pods to mount Cloud Storage buckets as local file systems. The cluster creation might take several minutes.

  2. To communicate with your cluster, configure `kubectl`:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=$ZONE
         

  3. Create the first [multi-host](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) TPU slice node pool with GKE DRANET enabled:
         
         gcloud container node-pools create v6e-16-0 \
             --location=$ZONE \
             --cluster=$CLUSTER_NAME \
             --machine-type=ct6e-standard-4t \
             --threads-per-core=1 \
             --tpu-topology=4x4 \
             --num-nodes=4 \
             --additional-node-network=network=${CLUSTER_NAME}-net-1,subnetwork=tpu-subnet-1 \
             --additional-node-network=network=${CLUSTER_NAME}-net-2,subnetwork=tpu-subnet-2 \
             --node-labels=cloud.google.com/gke-networking-dra-driver=true \
             --enable-gvnic \
             --scopes=https://www.googleapis.com/auth/cloud-platform
         

  4. Create the second TPU slice node pool:
         
         gcloud container node-pools create v6e-16-1 \
             --location=$ZONE \
             --cluster=$CLUSTER_NAME \
             --machine-type=ct6e-standard-4t \
             --threads-per-core=1 \
             --tpu-topology=4x4 \
             --num-nodes=4 \
             --additional-node-network=network=${CLUSTER_NAME}-net-1,subnetwork=tpu-subnet-1 \
             --additional-node-network=network=${CLUSTER_NAME}-net-2,subnetwork=tpu-subnet-2 \
             --node-labels=cloud.google.com/gke-networking-dra-driver=true \
             --enable-gvnic \
             --scopes=https://www.googleapis.com/auth/cloud-platform
         




GKE provisions a node pool consisting of four TPU Trillium (v6e) VMs, which are configured together as a multi-host TPU slice that has a `4x4` topology. This node pool is ready for distributed training workloads.

The [Ray operator](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview)-enabled GKE cluster automatically installs KubeRay and the [KubeRay TPU webhook](https://github.com/ai-on-gke/kuberay-tpu-webhook) in your cluster.

## Configure a Cloud Storage bucket and a service account

  1. Create a Cloud Storage bucket for shared checkpoints between the multi-host TPU nodes.
         
         gsutil mb -p ${PROJECT_ID} -c STANDARD -l ${REGION} gs://${GS_BUCKET}
         

  2. To enable access to the Cloud Storage bucket, create a Kubernetes Service Account:
         
         kubectl create serviceaccount ${KSA_NAME} --namespace ${NAMESPACE}
         

  3. To enable access to the Cloud Storage bucket, add the required IAM policy bindings to the service account:
         
         gcloud storage buckets add-iam-policy-binding gs://${GS_BUCKET} \
             --member "principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/${NAMESPACE}/sa/${KSA_NAME}" \
             --role "roles/storage.objectUser"
         




## Create the training script

The `maxtext_multi_slice_trainer.py` script uses Ray Train's JaxTrainer to run a distributed MaxText training job across two TPU slices. The script configures the training environment for eight multi-host TPU workers and runs the MaxText training job on each worker node. The `train_loop_per_worker` function wraps the MaxText main entry point, and uses the Ray's distributed scheduler to execute the MaxText trainer on a multi-host TPU slice:
    
    
    import os
    from absl import app
    import logging
    from typing import Sequence
    import ray
    from ray.train.v2.api.config import ScalingConfig, RunConfig
    from ray.train.v2.jax import JaxTrainer
    
    def train_loop_per_worker(config):
        import maxtext
        from maxtext.trainers.pre_train.train import main as maxtext_main
    
        argv = config["argv"]
        maxtext_main(argv)
    
    def main(argv: Sequence[str]):
        # Convert the config file path to an absolute path
        argv = list(argv)
        if len(argv) > 1:
            argv[1] = os.path.abspath(argv[1])
    
        trainer = JaxTrainer(
            train_loop_per_worker=train_loop_per_worker,
            train_loop_config={"argv": argv},
            scaling_config=ScalingConfig(
                use_tpu=True,
                num_workers=8,
                topology="4x4",
                accelerator_type="TPU-V6E",
                resources_per_worker={"TPU": 4},
                placement_strategy="SPREAD",
            ),
            run_config=RunConfig(
                name="maxtext_jaxtrainer",
                worker_runtime_env={
                    "uv": {
                        # maxtext requires some additional deps
                        "packages": ["maxtext[tpu]==0.2.1"],
                        "uv_pip_install_options": ["--resolution=lowest"]
                    },
                },
            ),
        )
        result = trainer.fit()
        logging.info("Training complete!")
        ray.shutdown()
    
    if __name__ == "__main__":
        app.run(main)
    

The preceding script defines a JaxTrainer instance requesting eight workers and a topology of `4x4`. Internally, Ray provisions a [SlicePlacementGroup](https://docs.ray.io/en/latest/ray-core/api/doc/ray.util.tpu.slice_placement_group.html) across the two TPU slices and helps ensure that the Ray Train workers run atomically across both slices, with one worker per host.

## Train the model

  1. The `ray-cluster.tpu-multi-slice.yaml` manifest in the current directory defines the RayCluster custom resource. This manifest includes the DRANET `ResourceClaimTemplate` to provision the network devices for GKE DRANET and Multislice:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: two-netdev
         spec:
           spec:
             devices:
               requests:
               - name: req-netdev
                 exactly:
                   deviceClassName: netdev.google.com
                   allocationMode: ExactCount
                   count: 2
         ---
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: maxtext-tpu-cluster
         spec:
           headGroupSpec:
             rayStartParams: {}
             template:
               metadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
                   gke-gcsfuse/cpu-limit: "0"
                   gke-gcsfuse/memory-limit: "0"
                   gke-gcsfuse/ephemeral-storage-limit: "0"
               spec:
                 serviceAccountName: ${KSA_NAME}
                 containers:
                   - name: ray-head
                     image: rayproject/ray:nightly-py312-tpu
                     imagePullPolicy: Always
                     ports:
                     - containerPort: 6379
                       name: gcs-server
                     - containerPort: 8265
                       name: dashboard
                     - containerPort: 10001
                       name: client
                     resources:
                       limits:
                         memory: "16Gi"
                       requests:
                         cpu: "8"
                         memory: "16Gi"
                     volumeMounts:
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                     - name: dshm
                       mountPath: /dev/shm
                 volumes:
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: ${GS_BUCKET}
                       mountOptions: "implicit-dirs,uid=1000,gid=1000,dir-mode=775,file-mode=664,file-cache:max-size-mb:-1"
                 nodeSelector:
                   iam.gke.io/gke-metadata-server-enabled: "true"
           workerGroupSpecs:
             - replicas: 2
               numOfHosts: 4
               groupName: tpu-group
               rayStartParams: 
                 metrics-export-port: "8082"
               template:
                 metadata:
                   annotations:
                     gke-gcsfuse/volumes: "true"
                     gke-gcsfuse/cpu-limit: "0"
                     gke-gcsfuse/memory-limit: "0"
                     gke-gcsfuse/ephemeral-storage-limit: "0"
                 spec:
                   serviceAccountName: ${KSA_NAME}
                   resourceClaims:
                   - name: netdev
                     resourceClaimTemplateName: two-netdev
                   containers:
                     - name: ray-worker
                       image: rayproject/ray:nightly-py312-tpu
                       imagePullPolicy: Always
                       resources:
                         claims:
                         - name: netdev
                         limits:
                           memory: 200G
                           google.com/tpu: "4"
                         requests:
                           cpu: "8"
                           memory: 200G
                           google.com/tpu: "4"
                       env:
                         - name: MEGASCALE_NUM_SLICES
                           value: "2"
                         - name: MEGASCALE_PORT
                           value: "9915"
                         - name: JAX_PLATFORMS
                           value: tpu,cpu
                         - name: ENABLE_PJRT_COMPATIBILITY
                           value: "true"
                         - name: LIBTPU_INIT_ARGS
                           value: "--xla_tpu_scoped_vmem_limit_kib=122880 --xla_tpu_use_minor_sharding_for_major_trivial_input=true --xla_tpu_relayout_group_size_threshold_for_reduce_scatter=1 --xla_tpu_assign_all_reduce_scatter_layout --xla_tpu_enable_async_collective_fusion_fuse_all_gather=true --xla_tpu_enable_async_collective_fusion_multiple_steps=true --xla_tpu_overlap_compute_collective_tc=true --xla_enable_async_all_gather=true --megascale_grpc_interface_prefixes=eth1,eth2,lo"
                       securityContext:
                         privileged: true
                       volumeMounts:
                       - name: gcs-fuse-csi-ephemeral
                         mountPath: /data
                       - name: dshm
                         mountPath: /dev/shm
                   volumes:
                   - name: dshm
                     emptyDir:
                       medium: Memory
                   - name: gcs-fuse-csi-ephemeral
                     csi:
                       driver: gcsfuse.csi.storage.gke.io
                       volumeAttributes:
                         bucketName: ${GS_BUCKET}
                         mountOptions: "implicit-dirs,uid=1000,gid=1000,dir-mode=775,file-mode=664,file-cache:max-size-mb:-1"
                   nodeSelector:
                     iam.gke.io/gke-metadata-server-enabled: "true"
                     cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                     cloud.google.com/gke-tpu-topology: 4x4
         

The preceding RayCluster spec creates a TPU worker group with eight workers (`numOfHosts: 4`) per replica, with two replicas. Each worker requests four TPU chips (`google.com/tpu: "4"`). The workers are each scheduled on a TPU Trillium node (`tpu-v6e-slice`), which is part of the same colocated multi-host slice. KubeRay scales all four workers in a slice atomically. The required JAX environment variables, as well as Pod Affinities for scheduling, are bootstrapped by GKE through a [mutating webhook](https://github.com/ai-on-gke/kuberay-tpu-webhook).

  2. To create the RayCluster, apply the manifest:
         
         envsubst < ray-cluster.tpu-multi-slice.yaml | kubectl apply -f -
         

  3. Verify that the cluster is ready and running:
         
         kubectl get rayclusters maxtext-tpu-cluster
         

The output should be similar to the following:
         
         NAME                  DESIRED WORKERS   AVAILABLE WORKERS   CPUS   MEMORY         GPUS   STATUS   AGE
         maxtext-tpu-cluster   8                 8                   72     1579277216Ki   0      ready    2m11s
         

  4. To access the Ray Dashboard through the Ray head service, establish a port-forwarding session:
         
         kubectl port-forward svc/maxtext-tpu-cluster-head-svc 8265:8265 2>&1 >/dev/null &
         

  5. Verify that the RayCluster is reachable from your local environment:
         
         ray list nodes --address http://localhost:8265
         

The output should be similar to the following:
         
         ray list nodes --address http://localhost:8265
         2026-04-21 10:20:20,080 - INFO - Note: NumExpr detected 64 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 8.
         2026-04-21 10:20:20,080 - INFO - NumExpr defaulting to 8 threads.
         
         ======== List: 2026-04-21 10:20:20.945431 ========
         Stats:
         ------------------------------
         Total: 9
         
         Table:
         ------------------------------
             NODE_ID                                                   NODE_IP     IS_HEAD_NODE    STATE    STATE_MESSAGE    NODE_NAME    RESOURCES_TOTAL                   LABELS
         0  4f0e4d742de5375047c7688f4d2bc64a42d1e5c77c2d8344b3b375a1  10.68.9.5   False           ALIVE                     10.68.9.5    CPU: 8.0                          ray.io/accelerator-type: TPU-V6E
                                                                                                                                         TPU: 4.0                          ray.io/node-group: tpu-group
                                                                                                                                         accelerator_type:TPU-V6E: 1.0     ray.io/node-id: 4f0e4d742...
                                                                                                                                         memory: 186.265 GiB               ray.io/tpu-pod-type: v6e-16
                                                                                                                                         node:10.68.9.5: 1.0               ray.io/tpu-slice-name: tpu-group-0
                                                                                                                                         object_store_memory: 186.265 GiB  ray.io/tpu-topology: 4x4
                                                                                                                                         tpu-group-0: 1.0                  ray.io/tpu-worker-id: '1'
         ...
         6  ce7056807b95831ce107ba1951dac34b80635e6fdbb312e7f9649938  10.68.2.9   True            ALIVE                     10.68.2.9    CPU: 8.0                          ray.io/node-group: headgroup
                                                                                                                                         memory: 16.000 GiB                ray.io/node-id: ce7056807...
                                                                                                                                         node:10.68.2.9: 1.0
                                                                                                                                         node:__internal_head__: 1.0
                                                                                                                                         object_store_memory: 4.765 GiB
         ...
         

  6. Download the base MaxText configuration file. This file is required by the training script to set the model's default hyperparameters:
         
         curl -O https://raw.githubusercontent.com/google/maxtext/maxtext-v0.2.1/src/maxtext/configs/base.yml
         

  7. Submit the JaxTrainer script to the RayCluster and check that the RayJob completes successfully:




### Llama 3 8B
    
    
    ray job submit \
      --address http://localhost:8265 \
      --working-dir . \
      --runtime-env-json '{"excludes": ["ray-env", ".git"]}' \
      -- python maxtext_multi_slice_trainer.py \
          base.yml \
          base_output_directory=/data/ \
          dataset_type=synthetic \
          per_device_batch_size=4 \
          max_target_length=4096 \
          model_name=llama3-8b \
          steps=100 \
          ici_fsdp_parallelism=4 \
          ici_tensor_parallelism=4 \
          run_name=rayjob-multi-slice
    

### Llama 3 70B
    
    
    ray job submit \
      --address http://localhost:8265 \
      --working-dir . \
      --runtime-env-json '{"excludes": ["ray-env", ".git"]}' \
      -- python maxtext_multi_slice_trainer.py \
          base.yml \
          base_output_directory=/data/ \
          dataset_type=synthetic \
          per_device_batch_size=2 \
          max_target_length=4096 \
          model_name=llama3-70b \
          steps=100 \
          ici_tensor_parallelism=4 \
          ici_fsdp_parallelism=4 \
          dcn_fsdp_parallelism=2 \
          dcn_data_parallelism=1 \
          remat_policy=full \
          run_name=rayjob-multi-slice-70b-fsdp
    

The preceding command submits the Python script, which calls the JaxTrainer Ray code to the RayCluster. The `ray job submit` command includes some MaxText-specific arguments to pass to the model configuration. 

**Note:** It might take a couple of minutes for the script to complete.

In your terminal, you should see output similar to the following for the Llama 3 70B job:
    
    
    [process=5][thread=save_finalize][step=99] CheckpointManager Save Finalize is done on all hosts. [repeated 7x across cluster]
    (RayTrainWorker pid=130520, ip=10.60.7.7) [process=5][thread=TrainingThread(train_fn_with_final_checkpoint_flush)][step=99][wait_until_finished] Done waiting for Save Finalize thread (save_finalize) running at step=99. [repeated 7x across cluster]
    (RayTrainWorker pid=130520, ip=10.60.7.7) [process=5][thread=TrainingThread(train_fn_with_final_checkpoint_flush)][wait_until_finished] No Save Finalize thread to wait for. Returning. [repeated 6x across cluster]
    (RayTrainWorker pid=130520, ip=10.60.7.7) completed step: 99, seconds: 0.693, TFLOP/s/device: 83.171, Tokens/s/device: 11819.175, total_weights: 262144, loss: 0.334 [repeated 6x across cluster]
    
    ------------------------------------------
    Job 'raysubmit_XwUdZMrhsYRKvjqs' succeeded
    ------------------------------------------
    

**Success:** You've completed training using Ray Train's JaxTrainer and MaxText on two multi-host TPU node pools.

## Run Multislice elastic training on Spot VMs

When using highly sought-after accelerators like TPUs, utilizing Spot VMs might significantly reduce costs. However, Spot VMs may be preempted unexpectedly.

Ray Train supports elastic training, which allows your job to dynamically scale the number of participating TPU slices up or down without failing. If a slice is preempted, Ray pauses the training loop, waits for the remaining workers to reorganize, restores from the latest MaxText checkpoint, and resumes training on the smaller footprint.

To enable elastic training, change the `num_workers` parameter in your `ScalingConfig` from a static integer to a tuple representing `(minimum_workers, maximum_workers)`. Additionally, add a `FailureConfig(max_failures=3)` to the `RunConfig`, which instructs Ray Train to retry the training loop up to 3 times instead of failing the job entirely when a worker is preempted.

**Note:** You must ensure your `minimum_workers` count provides enough High Bandwidth Memory (HBM) to physically fit the model you are training. For this example, use the 8B model, which safely fits on a single slice.

### Update the Ray Train script

  1. The `maxtext_elastic_trainer.py` script in the current directory enables elastic training. Notice that it sets `num_workers=(4,8)`, which tells Ray to proceed if at least one 16-chip slice (four workers) is available, but to scale up to two slices (eight workers) if possible. It includes a `FailureConfig` to enable elastic training, define the number of retries, and help ensure the job survives preemptions:
         
         import os
         from absl import app
         import logging
         from typing import Sequence
         import ray
         from ray.train.v2.api.config import ScalingConfig, RunConfig, FailureConfig
         from ray.train.v2.jax import JaxTrainer
         
         def train_loop_per_worker(config):
             import maxtext
             from maxtext.trainers.pre_train.train import main as maxtext_main
         
             argv = config["argv"]
             maxtext_main(argv)
         
         def main(argv: Sequence[str]):
             # Convert the config file path to an absolute path
             argv = list(argv)
             if len(argv) > 1:
                 argv[1] = os.path.abspath(argv[1])
         
             trainer = JaxTrainer(
                 train_loop_per_worker=train_loop_per_worker,
                 train_loop_config={"argv": argv},
                 scaling_config=ScalingConfig(
                     use_tpu=True,
                     # This tells Ray to scale the number of workers between 4 and 8 (i.e. 1 to 2 TPU slices).
                     num_workers=(4,8),
                     topology="4x4",
                     accelerator_type="TPU-V6E",
                     resources_per_worker={"TPU": 4},
                     placement_strategy="SPREAD",
                 ),
                 run_config=RunConfig(
                     name="maxtext_jaxtrainer",
                     # Define a FailureConfig to enable fault tolerance by automatically restarting failed workers.
                     failure_config=FailureConfig(max_failures=3),
                     worker_runtime_env={
                         "uv": {
                             # maxtext requires some additional deps
                             "packages": ["maxtext[tpu]==0.2.1"],
                             "uv_pip_install_options": ["--resolution=lowest"]
                         },
                     },
                 ),
             )
             result = trainer.fit()
             logging.info("Training complete!")
             ray.shutdown()
         
         if __name__ == "__main__":
             app.run(main)
         

  2. Submit the job by using the Ray Job CLI. Be sure to provide a unique `run_name` so the checkpoints don't conflict with previous runs.
         
         ray job submit \
           --address http://localhost:8265 \
           --working-dir . \
           --runtime-env-json '{"excludes": ["ray-env", ".git"]}' \
           -- python maxtext_elastic_trainer.py \
               base.yml \
               base_output_directory=/data/ \
               dataset_type=synthetic \
               per_device_batch_size=4 \
               max_target_length=4096 \
               model_name=llama3-8b \
               steps=100 \
               ici_fsdp_parallelism=4 \
               ici_tensor_parallelism=4 \
               run_name=rayjob-elastic-8b
         

  3. To simulate a node termination or preemption during training, delete a Pod.
         
         kubectl delete pod $(kubectl get pods -l ray.io/node-type=worker -o jsonpath='{.items[0].metadata.name}')
         




The terminal logs a worker failure, but the orchestration controller keeps the job alive and automatically resumes from the `/data/rayjob-elastic-8b/checkpoints` checkpoint after the minimum topology is available.

Because MaxText dynamically recalculates the device mesh upon resumption, you don't need to write any custom logic to handle checkpoint re-sharding when the topology shrinks. JAX's Orbax checkpointer will automatically re-shard the saved weights into the new physical layout before continuing the training loop. The following output shows the Ray Train controller detect newly available TPU resources in the cluster and perform a scaling operation from one slice (four workers) to two slices (eight workers) during training.
    
    
    ...
    (pid=, ip=10.68.9.5) W0421 04:19:07.570048   20579 grpc_transport.cc:1930] GetMultiSliceTopology returned with status: UNAVAILABLE: failed to connect to all addresses; last error: UNKNOWN: ipv4:10.68.8.5:9915: connect endpoint failed (Failed to connect to remote host: Connection refused)
    ...
    (TrainController pid=23150) Detected changes in the cluster resources. Deciding to resize the worker group from 4 -> 8 workers.
    (TrainController pid=23150) Using SlicePlacementGroup utility to reserve 2 slice(s) with topology '4x4'...
    (TrainController pid=23150) Attempting to start training worker group of size 8 with the following resources: [{'TPU': 4, 'accelerator_type:TPU-V6E': 0.001}] * 8
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

  1. Delete the RayCluster:
         
         kubectl delete raycluster maxtext-tpu-cluster
         

  2. Delete the GKE cluster:
         
         gcloud container clusters delete $CLUSTER_NAME --zone=$ZONE
         

  3. Delete the Cloud Storage bucket:
         
         gsutil rm -r gs://${GS_BUCKET}
         




## What's next

  * Learn about [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html).
  * Learn how to [serve vLLM on GKE with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu).
  * Learn more [about TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
