---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu/
title: Train an LLM using JAX, Ray Train, and TPU Trillium on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:10.394655+00:00
---

# Train an LLM using JAX, Ray Train, and TPU Trillium on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Train an LLM using JAX, Ray Train, and TPU Trillium on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to train the Llama 3 8B large language model (LLM) on Google Kubernetes Engine (GKE) using [MaxText](https://github.com/google/maxtext), [Ray Train](https://docs.ray.io/en/latest/train/train.html), and TPUs.

This tutorial provides a complete, end-to-end walkthrough, from configuring the necessary cloud infrastructure to submitting and successfully running the training workload on multi-host TPUs.

This tutorial is for Platform admins and operators and Data and AI specialists who want to learn how to train large models on a distributed, multi-host TPU slice.

## Background

The combination of GKE, KubeRay, MaxText, and TPUs provides a powerful and scalable platform for large-scale model training. This section describes the key technologies used in this guide:

### JAX

[JAX](https://github.com/jax-ml/jax) is a Python library for accelerator-oriented array computation and program transformation, designed for high-performance numerical computing and large-scale machine learning.

JAX provides an extensible system for transforming numerical functions like `jax.grad`, `jax.jit`, and `jax.vmap`, utilizing the XLA compiler to create highly optimized code that scales efficiently on accelerators like GPUs and TPUs. The core power of JAX lies in its composability, which allows users to combine these transformations to build complex, high-performance numerical programs for distributed execution.

### MaxText

[MaxText](https://github.com/google/maxtext) is a high-performance, open-source large language model (LLM) designed for scalability and customizability. MaxText is built on top of JAX and optimized to run efficiently on Cloud TPU and GPUs.

### TPUs

[Tensor Processing Units](https://cloud.google.com/tpu) (TPUs), are custom-designed accelerators created by Google to optimize machine learning workloads. Unlike general-purpose CPUs or parallel-processing GPUs, TPUs are highly specialized for the massive matrix and tensor computations at the foundation of deep learning, making them efficient at this specific task. The primary advantage of TPUs is performance at scale.

This tutorial uses TPU Trillium, which is the sixth generation of TPUs. For more information, see [Benefits of using TPU Trillium](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#trillium-benefits).

### KubeRay

[KubeRay](https://github.com/ray-project/kuberay) is a Kubernetes operator that provides a unified way to deploy, manage, and monitor Ray applications on Kubernetes. The KubeRay operator is installed and managed through the [Ray on GKE add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview), which is the recommended way to deploy and manage Ray clusters on GKE.

## Objectives

This tutorial shows you how to do the following:

  1. Set up a GKE cluster with a multi-host TPU node pool.
  2. Configure KubeRay to manage the distributed training environment.
  3. Build a custom Docker image that contains MaxText, Ray, and JAX dependencies.
  4. Create a Python training script that uses Ray Train's `JaxTrainer` to orchestrate the MaxText training loop across the TPU slice.
  5. Define a [`RayCluster` custom resource](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/config.html) to provision the head and worker nodes with the necessary TPU resources.
  6. Submit the training Job to the `RayCluster` and monitor its progress.
  7. Use Cloud Storage to store model checkpoints.



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

  3. Create and activate a Python virtual environment:
         
         python3 -m venv ray-env
         source ray-env/bin/activate
         

  4. Install the Ray CLI and other dependencies:
         
         pip install "ray[default]==2.49.1"
         

  5. Set the following environment variables:
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export GS_BUCKET=GS_BUCKET
         export KSA_NAME=KSA_NAME
         export NAMESPACE=default
         export CLUSTER_NAME=CLUSTER_NAME
         export REGION=REGION
         export ZONE=ZONE
         export ARTIFACT_REGISTRY=ARTIFACT_REGISTRY
         

Replace the following:

     * `GS_BUCKET`: the name of the Cloud Storage bucket.
     * `KSA_NAME`: the name of the Kubernetes Service Account.
     * `CLUSTER_NAME`: the name of the new cluster.
     * `REGION`: the region where your TPU Trillium capacity is available.
     * `ZONE`: the zone where your TPU Trillium capacity is available. For more information, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
     * `ARTIFACT_REGISTRY`: the name of the Artifact Registry repository.



## Create a GKE cluster

You can configure KubeRay on TPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

  1. In Cloud Shell, run the following command:
         
         gcloud container clusters create-auto $CLUSTER_NAME \
             --enable-ray-operator \
             --machine-type=n1-standard-16 \
             --location=$REGION
         

  2. To communicate with your cluster, configure `kubectl` :
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=$ZONE
         




### Standard

  1. In Cloud Shell, create a Standard cluster that enables the [Ray operator](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview) add-on by running the following command:
         
         gcloud container clusters create $CLUSTER_NAME \
             --addons=RayOperator \
             --addons GcsFuseCsiDriver \
             --machine-type=n1-standard-16 \
             --workload-pool=$PROJECT_ID.svc.id.goog \
             --location=$ZONE
         

This command also enables the `GcsFuseCsiDriver`, which allows Pods to mount Cloud Storage buckets as local file systems. The cluster creation might take several minutes.

  2. To communicate with your cluster, configure `kubectl`:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=LOCATION
         

  3. Create a [multi-host](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) TPU slice node pool:
         
         gcloud container node-pools create v6e-16 \
             --location=$ZONE \
             --cluster=$CLUSTER_NAME \
             --machine-type=ct6e-standard-4t \
             --threads-per-core=1 \
             --tpu-topology=4x4 \
             --num-nodes=4
         




GKE provisions a node pool consisting of four TPU Trillium (v6e) VMs, which are configured together as a multi-host TPU slice, with a `4x4` topology, that's ready for distributed training workloads.

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

The following script uses Ray Train's `JaxTrainer` to run a distributed MaxText training job. The script configures the training environment for a multi-host TPU slice node pool and runs the MaxText training job on each worker node. The `train_loop_per_worker` function wraps the MaxText main entry point, and uses the Ray's distributed scheduler to execute the MaxText trainer on a multi-host TPU slice.

  1. Save the following Python script as `maxtext_ray_trainer.py`:
         
         import os
         from absl import app
         import logging
         from typing import Sequence
         import ray
         from ray.train.v2.api.config import ScalingConfig, RunConfig
         from ray.train.v2.jax import JaxTrainer
         
         def train_loop_per_worker(config):
             from MaxText.train import main as maxtext_main
         
             argv = config["argv"]
             maxtext_main(argv)
         
         def main(argv: Sequence[str]):
             trainer = JaxTrainer(
                 train_loop_per_worker=train_loop_per_worker,
                 train_loop_config={"argv": argv},
                 scaling_config=ScalingConfig(
                     use_tpu=True,
                     num_workers=4,
                     topology="4x4",
                     accelerator_type="TPU-V6E",
                     resources_per_worker={"TPU": 4},
                     placement_strategy="SPREAD",
                 ),
                 run_config=RunConfig(
                     name="maxtext_jaxtrainer",
                     worker_runtime_env={
                         "env_vars": {
                             "JAX_PLATFORMS": "tpu",
                             "ENABLE_PJRT_COMPATIBILITY": "true",
                             "TPU_SLICE_BUILDER_DUMP_CHIP_FORCE": "true",
                             "TPU_SLICE_BUILDER_DUMP_ICI": "true",
                             "XLA_FLAGS": "--xla_dump_to=/tmp/xla_dump_file --xla_dump_hlo_as_proto",
                         }
                     },
                 ),
             )
             result = trainer.fit()
             logging.info("Training complete!")
             ray.shutdown()
         
         if __name__ == "__main__":
             app.run(main)

  2. To host the custom image, create an Artifact Registry repository:
         
         gcloud artifacts repositories create ${ARTIFACT_REGISTRY} \
             --repository-format=docker --location=${REGION} && \
         gcloud auth configure-docker ${REGION}-docker.pkg.dev
         

  3. To build an image that includes Ray and MaxText dependencies for training, create a `Dockerfile`:
         
         # Start from a Ray base image which includes JaxTrainer API.
         # Maxtext with TPU requires Python 3.12.
         FROM rayproject/ray:2.49.1-py312
         
         USER root
         RUN groupadd -r ray 2>/dev/null || true && usermod -g ray ray
         
         RUN sudo apt-get update -y \
           && sudo apt-get install --no-install-recommends -y git \
           && sudo rm -rf /var/lib/apt/lists/*
         
         WORKDIR /app
         
         # Clone the Maxtext repo and build from source, installing TPU dependencies.
         RUN git clone https://github.com/AI-Hypercomputer/maxtext.git
         
         RUN pip install --no-cache-dir uv
         
         RUN cd maxtext && \
             uv pip install --no-cache --system -e .[tpu] --resolution=lowest && \
             install_maxtext_github_deps
         
         # Copy the Ray Maxtext trainer to run on the remote container.
         COPY maxtext_ray_trainer.py .
         
         RUN chown -R ray:ray .
         ENV PYTHONPATH=/app/maxtext/src:/app/maxtext:/app
         USER ray

**Note:** This tutorial uses a custom image because the dependencies are too large to install them by using the Ray `runtime_env` command.
  4. Build, tag, and push the Docker image to Artifact Registry:
         
         export DOCKER_IMAGE=${REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REGISTRY}/ray-maxtext:latest
         gcloud builds submit --tag ${DOCKER_IMAGE}
         




## Train the model

  1. Save the following sample manifest as `maxtext-tpu-cluster.yaml`:
         
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
                     image: ${DOCKER_IMAGE}
                     imagePullPolicy: IfNotPresent
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
                 - name: gcs-fuse-cache
                   emptyDir:
                     medium: Memory
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: ${GS_BUCKET}
                       mountOptions: "implicit-dirs"
           workerGroupSpecs:
             - replicas: 1
               numOfHosts: 4
               groupName: tpu-group
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
                     - name: ray-worker
                       image: ${DOCKER_IMAGE}
                       imagePullPolicy: IfNotPresent
                       resources:
                         limits:
                           memory: 200G
                           google.com/tpu: "4"
                         requests:
                           cpu: "8"
                           memory: 200G
                           google.com/tpu: "4"
                       env:
                         - name: JAX_PLATFORMS
                           value: tpu
                         - name: ENABLE_PJRT_COMPATIBILITY
                           value: "true"
                       volumeMounts:
                       - name: gcs-fuse-csi-ephemeral
                         mountPath: /data
                       - name: dshm
                         mountPath: /dev/shm
                   volumes:
                   - name: gcs-fuse-cache
                     emptyDir:
                       medium: Memory
                   - name: dshm
                     emptyDir:
                       medium: Memory
                   - name: gcs-fuse-csi-ephemeral
                     csi:
                       driver: gcsfuse.csi.storage.gke.io
                       volumeAttributes:
                         bucketName: ${GS_BUCKET}
                         mountOptions: "implicit-dirs"
                   nodeSelector:
                     cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                     cloud.google.com/gke-tpu-topology: 4x4

The preceding RayCluster spec creates a TPU worker group with four workers (`numOfHosts: 4`) per replica. Each worker requests four TPU chips (`google.com/tpu: "4"`). The workers will be scheduled on a node that runs TPU Trillium (`tpu-v6e-slice`), and that's part of the same colocated multi-host slice. KubeRay scales all four workers atomically, and the required JAX environment variables, as well as Pod Affinities for scheduling, are bootstrapped by GKE through a mutating webhook.

  2. To configure required values in the YAML file, create the RayCluster using `envsubst`:
         
         envsubst < maxtext-tpu-cluster.yaml | kubectl apply -f -
         

  3. Verify the cluster is ready and running:
         
         kubectl get rayclusters maxtext-tpu-cluster
         

The output should be similar to the following:
         
         NAME                  DESIRED WORKERS   AVAILABLE WORKERS   CPUS   MEMORY        GPUS   STATUS   AGE
         maxtext-tpu-cluster   4                 4                   40     798027216Ki   0      ready    11m
         

  4. To access the Ray Dashboard through the Ray head service, establish a port-forwarding session:
         
         kubectl port-forward svc/maxtext-tpu-cluster-head-svc 8265:8265 2>&1 >/dev/null &
         

  5. Verify the RayCluster is reachable from your local environment:
         
         ray list nodes --address http://localhost:8265
         

The output should be similar to the following:
         
         ======== List: 2025-09-13 03:53:16.988269 ========
         Stats:
         ------------------------------
         Total: 5
         Table:
         ------------------------------
             NODE_ID                                                   NODE_IP    IS_HEAD_NODE    STATE    STATE_MESSAGE    NODE_NAME    RESOURCES_TOTAL                  LABELS
         0  92c79d04c34b659c1e3044f7642ad3fd47eb16f290785237149fab56  10.84.0.9
         (...)
         

  6. Submit the JaxTrainer script to the RayCluster and check that the RayJob completes successfully:
         
         ray job submit \
           --address http://localhost:8265 \
           -- python /app/maxtext_ray_trainer.py \
               /app/maxtext/src/MaxText/configs/base.yml \
                base_output_directory=/data/ \
               dataset_type=synthetic \
               per_device_batch_size=1 \
               max_target_length=4096 \
               model_name=llama3-8b \
               steps=100 \
               ici_fsdp_parallelism=4 \
               ici_tensor_parallelism=4 \
               run_name=rayjob-8b-4096-tp4-4x4
         

The preceding command submits the Python script, which calls the JaxTrainer Ray code to the RayCluster. The `ray job submit` command includes some MaxText-specific arguments to pass to the model configuration. 

**Note:** It might take a couple of minutes for the script to complete.

In your terminal, you should see output similar to the following:
         
         (RayTrainWorker pid=21663, ip=10.12.3.6) completed step: 99, seconds: 1.100, TFLOP/s/device: 179.739, Tokens/s/device: 3725.218, total_weights: 65536, loss: 0.000 [repeated 3x across cluster]
         
         ------------------------------------------
         Job 'raysubmit_zCrJcWnuymMQv4C3' succeeded
         ------------------------------------------
         


**Success:** You've completed training by using Ray Train's JaxTrainer and MaxText on distributed multi-host TPU node pools.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

  1. Delete the RayCluster:
         
         kubectl delete raycluster maxtext-tpu-cluster
         

  2. Delete the GKE cluster:
         
         gcloud container clusters delete $CLUSTER_NAME --zone=$ZONE
         

  3. Delete the Cloud Storage bucket:
         
         gsutil rm -r gs://${GS_BUCKET}
         

  4. Delete the Artifact Registry repository:
         
         gcloud artifacts repositories delete ${ARTIFACT_REGISTRY} --location=${REGION} --quiet
         




## What's next

  * Learn about [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html).
  * Learn how to [Serve vLLM on GKE with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu).
  * Learn how to [Serve SDXL on GKE with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-sdxl-tpu).
  * Learn more [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
