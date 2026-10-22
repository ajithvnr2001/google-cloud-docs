---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/ray-kueue-dws/
title: Optimize AI training on TPUs with DWS and Kueue \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:17.565429+00:00
---

# Optimize AI training on TPUs with DWS and Kueue  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/ray-kueue-dws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Optimize AI training on TPUs with DWS and Kueue Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document teaches you how to configure a GKE cluster to maximize AI training availability on Tensor Processing Units (TPUs). You configure an automated fallback system using an open-source job queueing tool called [Kueue](https://kueue.sigs.k8s.io/), and [Google Cloud's Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) (DWS).

The configuration that you define in this document sets up a primary node pool and a backup pool of nodes:

  * **On-demand (Plan A):** This node pool is your first choice for nodes. The system first attempts to schedule jobs on these on-demand machines. The term _on-demand_ means that once these machines start running, you have reliable, uninterrupted access to them.
  * **DWS flex-start (Plan B):** This is your backup node pool. When Plan A machines aren't available, the Kueue scheduling program automatically assigns your job to this Plan B pool. DWS then searches for the Plan B hardware, but it doesn't guarantee immediate access because that hardware might also be unavailable. DWS doesn't give up though: it holds your request in line for up to 7 days and automatically provides the machines as soon as they're available.



This approach minimizes the time jobs spend waiting in line. It means that you don't have to manually check for available resources or rewrite your script for different machines.

## Overview of configuration steps

To configure the automated fallback system, you must complete several configuration steps. It helps to divide this configuration into two categories:

  * **Cluster Administrator tasks:** One-time infrastructure configuration, such as creating the GKE cluster, provisioning node pools, and installing the Kueue scheduling controller.
  * **AI Developer tasks:** Repetitive, daily workflows, such as defining the training job requirements and submitting the workload.



Even if you perform all of these steps yourself, keeping this distinction in mind helps clarify the overall process.

Before you configure the system, review the configuration steps that you'll perform.

Topic | Task  
---|---  
**Configure the infrastructure (Cluster Administrator)** | 1\. Create a GKE cluster  
2\. Create the node pools  
3\. Verify the status of flex-start in the node pool  
**Install and configure Kueue (Cluster Administrator)** | 1\. Install Kueue  
2\. Define the configuration rules  
**Run a training job (AI Developer)** | 1\. Create the ConfigMap  
2\. Define the RayJob manifest  
3\. Submit the workload  
4\. Connect to the RayJob  
5\. Check the logs  
  
### Key concepts

  * **On-demand (Plan A) node pool:** The primary, high-priority node pool. Your job always tries to use this pool first.
  * **DWS flex-start (Plan B) node pool:** The backup node pool. If machines in the primary pool aren't available, the system automatically uses this pool to search for available hardware.
  * **Kueue:** A scheduling program that manages the job queue. It intercepts your job request and decides which node pool to use (Plan A or Plan B).
  * **Job:** The AI training workload you want to run. In this document, you define it using a RayJob manifest.



## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Google Kubernetes Engine, Cloud TPU API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,tpu.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. Ensure that you have enough preemptible quota to use TPU flex-start VMs. If the default quota isn't enough for your needs, request a higher allocation. For details, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).




## Define environment variables

To simplify the commands that you run in this document, you can set environment variables in [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). These variables store values such as the ID of your Google Cloud project, the names of your node pools, and the location of your GKE cluster.

After you define these variables, you can reuse them in multiple commands by referencing the variable name (for example, `$CLUSTER_NAME`) instead of retyping or replacing values each time. This approach makes the process easier to follow and reduces the risk of errors.

To define the following useful environment variables in Cloud Shell, run the following commands:
    
    
    export PROJECT_ID=$(gcloud config get project)
    export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
    export ZONE="us-east5-b"
    export REGION="us-east5"
    export CLUSTER_NAME="tpu-cluster"
    export GKE_VERSION="1.34"
    export ONDEMAND_NODEPOOL="on-demand-pool"
    export DWS_NODEPOOL="dws-pool"
    

Here's an explanation of these environment variables:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `PROJECT_NUMBER`: The unique identifier number for your project (for example, 123456789012).
  * `ZONE`: The compute zone for your cluster (for example, `us-east5-b`). Select a zone with availability for your chosen accelerator type. See Cloud TPU quotas or GPU quotas for availability info.
  * `REGION`: The region where you create the cluster resources (for example, `us-east5`).
  * `CLUSTER_NAME`: The name you choose for your GKE cluster.
  * `GKE_VERSION`: The GKE version of your cluster. Use version 1.34 or later.
  * `ONDEMAND_NODEPOOL`: The name of your standard on-demand node pool. (This is your Plan A node pool).
  * `DWS_NODEPOOL`: The name of your DWS flex-start node pool. (This is your Plan B node pool).



## Configure the infrastructure (Cluster Administrator)

As the Cluster Administrator, you configure the GKE cluster and node pools to support the fallback mechanism.

### Create a GKE cluster

First, create the GKE cluster. This cluster is the environment in which you install the Kueue controller, configure your node pools, and run your AI training jobs. To create and connect to a cluster, perform these steps:

  1. Create the cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
           --cluster-version=${GKE_VERSION} \
           --machine-type=n2-standard-16 \
           --location=${ZONE} \
           --enable-image-streaming \
           --addons=RayOperator \
           --project=${PROJECT_ID}
         

This command uses the following key flags:

     * `--addons=RayOperator`: Installs the Ray Operator on your cluster. You need this operator to manage the RayJob workload that you submit later in this document.
     * `--enable-image-streaming`: Allows your cluster to pull container images faster. This feature significantly reduces the time it takes for large AI container images to start running.
  2. Retrieve the cluster's credentials so that the kubectl CLI can connect to it. This command updates your Kubernetes config file, which is stored by default in the `~/.kube/config` directory:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
           --location=${ZONE} \
           --project=${PROJECT_ID}
         




### Create the node pools

Create the primary and backup node pools for your environment: the on-demand node pool (**Plan A**) and the DWS flex-start node pool (**Plan B**):

  1. **Create the on-demand node pool** : This pool serves as the primary resource for training jobs:
         
         gcloud container node-pools create ${ONDEMAND_NODEPOOL} \
           --cluster=${CLUSTER_NAME} \
           --location=${ZONE} \
           --machine-type=ct6e-standard-4t \
           --tpu-topology=4x4 \
           --reservation-affinity=none \
           --enable-autoscaling \
           --num-nodes=0 \
           --min-nodes=0 \
           --max-nodes=4
         

In this example, your first choice machines are TPU v6e accelerators. You specify this hardware using the `--machine-type=ct6e-standard-4t` flag. You can change this machine type to match the hardware, such as GPUs or different TPUs, that you want for your AI model.

  2. **Create the DWS flex-start node pool** : In this example, you select the same machine type (`--machine-type=ct6e-standard-4t`) that you chose for the primary on-demand pool. Your Plan B node pool doesn't have to use a different machine type. Because you really want this specific hardware, making it your Plan B choice just means you switch to a different method of acquiring it if it's not immediately available. This alternative method uses DWS, which continuously searches for the available hardware for up to 7 days:
         
         gcloud container node-pools create ${DWS_NODEPOOL} \
           --cluster=${CLUSTER_NAME} \
           --location=${ZONE} \
           --machine-type=ct6e-standard-4t \
           --tpu-topology=4x4 \
           --enable-autoscaling \
           --enable-queued-provisioning \
           --flex-start \
           --num-nodes=0 \
           --min-nodes=0 \
           --max-nodes=4
         

These commands use the following key flags:

     * `--num-nodes=0`, `--min-nodes=0`, `--max-nodes=4`, and `--enable-autoscaling`: This combination allows the node pools to scale up from zero nodes when a job needs them and scale back down when idle, which helps save costs.
     * `--tpu-topology`: Defines the physical arrangement of the TPU chips. You specify this layout because the physical arrangement of the chips affects how fast your distributed training job runs.
     * `--reservation-affinity=none`: (Plan A pool only) This flag prevents the on-demand node pool from consuming your reserved capacity. The DWS flex-start node pool doesn't consume reservations.
     * `--enable-queued-provisioning` and `--flex-start`: (Plan B pool only) These flags enable DWS to provision nodes for your Plan B pool from flexible capacity when it becomes available.



### Verify the status of flex-start in the node pool

Inspect the DWS flex-start node pool and verify that flex-start is enabled:
    
    
    gcloud container node-pools describe ${DWS_NODEPOOL} \
      --cluster=${CLUSTER_NAME} \
      --location=${ZONE} \
      --format="get(config.flexStart)"
    

If flex-start is enabled, the output is `True`.

## Install and configure Kueue (Cluster Administrator)

In this section, you install the Kueue controller on your cluster. Recall that Kueue is a scheduling program that manages the job queue. It intercepts your job request, decides which node pool to use (on-demand or DWS flex-start), and then assigns the job.

### Install Kueue

Run the following command to install Kueue. This command downloads the installation manifests from the official repository and applies them to your cluster:
    
    
    helm install kueue oci://registry.k8s.io/kueue/charts/kueue \
      --namespace kueue-system \
      --create-namespace \
      --set "controllerManager.featureGates[0].name=ElasticJobsViaWorkloadSlices" \
      --set "controllerManager.featureGates[0].enabled=true"
    

### Define the configuration rules

Create a YAML manifest that defines the priority rules. These rules tell Kueue to use the on-demand pool first and the DWS flex-start pool second:

  1. Create a file named `dws-tpu-queue.yaml` with the following content. This file defines two _flavors_ of resources (on-demand and DWS flex-start) and a cluster queue that prioritizes them. This configuration file defines the logic that Kueue uses to handle your jobs:

     * `ResourceFlavor`: At the beginning of this document, you created two node pools and assigned them names using the environment variables `${ONDEMAND_NODEPOOL}` and `${DWS_NODEPOOL}`. When it created those node pools, GKE automatically labeled every node in those pools with the name you chose for those environment variables. The `ResourceFlavor` section tells Kueue to look for nodes with those labels.
     * `ClusterQueue`: This section of the manifest defines the priority rule. It lists the on-demand flavor first, so Kueue tries to provision on-demand machines first. If Kueue can't get those machines, it tries to provision DWS flex-start machines instead.
     * `Quotas`: The file sets a _quota_ , which is a limit on the total resources (such as CPU, memory, and TPU chips) your jobs can use at any given time in the on-demand node pool. When your jobs reach this limit, Kueue automatically tries to provision DWS flex-start machines (your Plan B machines), which you configured in `dws-tpu-queue.yaml` with a much higher quota limit. 
           
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: ResourceFlavor
           metadata:
             name: "default-cpu"
           spec:
             nodeLabels:
               cloud.google.com/gke-nodepool: default-pool
           ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: ResourceFlavor
           metadata:
             name: "on-demand"
           spec:
             nodeLabels:
               cloud.google.com/gke-nodepool: ${ONDEMAND_NODEPOOL}
           ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: ResourceFlavor
           metadata:
             name: "dws"
           spec:
             nodeLabels:
               cloud.google.com/gke-nodepool: ${DWS_NODEPOOL}
           ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: ClusterQueue
           metadata:
             name: "cluster-queue"
           spec:
             namespaceSelector: {}
             resourceGroups:
               - coveredResources: ["cpu", "memory", "google.com/tpu"]
                 flavors:
                   - name: "default-cpu" # Used for Ray Head Pod.
                     resources:
                       - name: "cpu"
                         nominalQuota: 10
                       - name: "memory"
                         nominalQuota: 20Gi
                       - name: "google.com/tpu"
                         nominalQuota: 0
                   - name: "on-demand" # First choice: on-demand node-pool.
                     resources:
                       - name: "cpu"
                         nominalQuota: 40
                       - name: "memory"
                         nominalQuota: 75Gi
                       - name: "google.com/tpu"
                         nominalQuota: 16
                   - name: "dws" # If on-demand is unavailable, fallback to DWS.
                     resources:
                       - name: "cpu"
                         nominalQuota: 1000000000
                       - name: "memory"
                         nominalQuota: 1000000000Gi
                       - name: "google.com/tpu"
                         nominalQuota: 1000000000 # "Infinite" quota
             admissionChecksStrategy:
               admissionChecks:
                 - name: "dws-prov"
                   onFlavors: [dws]
           ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: LocalQueue
           metadata:
             namespace: "default"
             name: "user-queue"
           spec:
             clusterQueue: "cluster-queue"
           ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: AdmissionCheck
           metadata:
             name: dws-prov
           spec:
             controllerName: kueue.x-k8s.io/provisioning-request
             parameters:
               apiGroup: kueue.x-k8s.io
               kind: ProvisioningRequestConfig
               name: dws-config
           ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: ProvisioningRequestConfig
           metadata:
             name: dws-config
           spec:
             provisioningClassName: queued-provisioning.gke.io
             managedResources:
               - google.com/tpu

  2. Apply the configuration to your cluster. The following command uses a command-line tool called `envsubst` to replace placeholder variables that appear in the file `dws-tpu-queue.yaml`. `envsubst` replaces the placeholders with the values of the environment variables that you defined earlier:
         
         envsubst < dws-tpu-queue.yaml | kubectl apply -f -
         




## Run a training job (AI Developer)

As the AI Developer, you define and submit a training workload by creating a RayJob manifest. You specify your resource requirements in this manifest, and the automated fallback system, which the Cluster administrator configured earlier with Kueue and DWS, handles the underlying node pools for you.

In this section, you perform the following steps:

  * Create a Python training script.
  * Store that script in a Kubernetes ConfigMap.
  * Deploy a RayJob that mounts the ConfigMap as a volume so that the training script can be executed on the nodes.



After performing these steps, Ray Train automatically distributes the JAX workload across the nodes, and Kueue handles getting the machines you need.

### The training script

Copy and paste the following Python script into a file called `train.py`:
    
    
    import time
    import ray
    from ray import train
    from ray.train import ScalingConfig
    from ray.train.v2.jax import JaxTrainer
    import jax
    import jax.numpy as jnp
    
    def train_func():
        # JaxTrainer handles JAX distributed setup.
        print(f"Local Devices: {jax.local_devices()}")
    
        # Simple Linear Regression Training Loop.
        key = jax.random.PRNGKey(0)
        x = jax.random.normal(key, (1000, 10))
        w_true = jax.random.normal(key, (10, 1))
        y = jnp.dot(x, w_true)
    
        # Initialize weights
        w = jnp.zeros((10, 1))
        learning_rate = 0.1
    
        @jax.jit
        def update(w, x, y):
            y_pred = jnp.dot(x, w)
            loss = jnp.mean((y_pred - y) ** 2)
            grad = jax.grad(lambda w: jnp.mean((jnp.dot(x, w) - y) ** 2))(w)
            return w - learning_rate * grad, loss
    
        # Training loop
        print("Starting training...")
        for epoch in range(50):
            w, loss = update(w, x, y)
            if epoch % 10 == 0:
                train.report({"loss": loss.item(), "epoch": epoch})
                print(f"Epoch {epoch}: Loss {loss:.4f}")
    
        print("Training Complete!")
        # Allow metrics to sync before closing
        time.sleep(3)
    
    def main():
        scaling_config = ScalingConfig(
            num_workers=4,
            resources_per_worker={"TPU": 4},
            use_tpu=True,
            topology="4x4",
            accelerator_type="TPU-V6E"
        )
    
        trainer = JaxTrainer(
            train_loop_per_worker=train_func,
            scaling_config=scaling_config
        )
    
        result = trainer.fit()
        print(f"Run Result: {result.metrics}")
    
    if __name__ == "__main__":
        main()

The training script uses [JAX](https://github.com/google/jax), a Python library for high-performance numerical computing, to train a linear regression model. This script is a simplified example designed to demonstrate how to use DWS and Kueue for automated fallback, and doesn't perform [data parallelism](https://docs.ray.io/en/latest/train/api/doc/ray.train.data_parallel_trainer.DataParallelTrainer.html) or [model parallelism](https://docs.ray.io/en/latest/data/working-with-llms.html#model-parallelism).

Notice that the `ScalingConfig` section of the training script defines the hardware requirements for the training job. That section requests a 4x4 TPU topology, which matches the physical layout of the node pools you configured earlier.

### Create the ConfigMap

Upload the contents of your `train.py` script into a Kubernetes ConfigMap object. This allows the cluster to store the script and make it available to your RayJob:
    
    
    kubectl create configmap jax-train-script --from-file=train.py
    

The RayJob that you define in the next section mounts this ConfigMap as a volume. This makes the script file appear inside the Ray containers so that the Ray software can find and execute it.

### Apply the RayJob manifest

Create a file named `rayjob-tpu-v6e-dws.yaml` with the following content. This manifest defines your training job and tells the system how to route it:
    
    
    apiVersion: ray.io/v1
    kind: RayJob
    metadata:
      name: rayjob-tpu-v6e-dws-${JOB_ID}
      labels:
        kueue.x-k8s.io/queue-name: user-queue
      annotations:
        kueue.x-k8s.io/elastic-job: "true"
    spec:
      shutdownAfterJobFinishes: true
      entrypoint: python /app/train.py
      runtimeEnvYAML: |
        pip:
          - jax[tpu]==0.8.2
          - pandas==2.3.3
      rayClusterSpec:
        enableInTreeAutoscaling: true
        headGroupSpec:
          rayStartParams: {}
          template:
            spec:
              nodeSelector:
                cloud.google.com/gke-nodepool: default-pool
              containers:
                - name: ray-head
                  image: rayproject/ray:2.53.0-py311
                  ports:
                    - containerPort: 6379
                      name: gcs-server
                    - containerPort: 8265
                      name: dashboard
                    - containerPort: 10001
                      name: client
                  resources:
                    limits:
                      cpu: "2"
                      memory: "4Gi"
                    requests:
                      cpu: "2"
                      memory: "4Gi"
                  volumeMounts:
                    - mountPath: /app
                      name: train-script-volume
              volumes:
                - name: train-script-volume
                  configMap:
                    name: jax-train-script
        workerGroupSpecs:
          - replicas: 1
            minReplicas: 1
            maxReplicas: 2
            numOfHosts: 4
            groupName: tpu-group
            rayStartParams: {}
            template:
              spec:
                tolerations:
                  - key: "google.com/tpu"
                    operator: "Exists"
                    effect: "NoSchedule"
                  - key: "cloud.google.com/gke-queued"
                    operator: "Exists"
                    effect: "NoSchedule"
                containers:
                  - name: ray-worker
                    image: rayproject/ray:2.53.0-py311
                    resources:
                      limits:
                        cpu: "8"
                        google.com/tpu: "4"
                        memory: "16Gi"
                      requests:
                        cpu: "8"
                        google.com/tpu: "4"
                        memory: "16Gi"
                    volumeMounts:
                      - mountPath: /app
                        name: train-script-volume
                volumes:
                  - name: train-script-volume
                    configMap:
                      name: jax-train-script
                nodeSelector:
                  cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                  cloud.google.com/gke-tpu-topology: 4x4

This manifest includes three configurations that make the fallback system work:

  * **Requests specific hardware:** The `nodeSelector` section specifies the hardware that your script requires (in this example, a `tpu-v6e-slice` with a 4x4 topology).
  * **Selects the queue:** The `kueue.x-k8s.io/queue-name` label routes your job directly to Kueue. This enables the automated fallback logic.
  * **Tolerates DWS flex-start nodes:** The `tolerations` section allows the job to run on your Plan B node pool. Because DWS flex-start nodes are specially marked (tainted) by GKE so that normal workloads don't accidentally run on them, your job must explicitly tolerate the `cloud.google.com/gke-queued` taint.



### Submit the workload

To prove that the fallback system works, you need to submit two jobs. The first job consumes the Plan A on-demand capacity, which forces the second job to fall back to the Plan B DWS flex-start capacity.

Run the following command to submit the two jobs. The command uses a `for` loop and `envsubst` to inject a unique job ID into the manifest for each run:
    
    
    for i in 1 2; do
      export JOB_ID=$i
      envsubst < rayjob-tpu-v6e-dws.yaml | kubectl apply -f -
      echo "Submitted Job $i"
      sleep 2
    done
    

After you submit the jobs, the system handles the workload as follows:

  1. **Intercept:** Kueue detects the jobs by using the queue label and temporarily suspends them.
  2. **Decision:** Kueue evaluates resource availability against the administrator's rules. It checks the Plan A pool first.
  3. **Assignment:**
     * Because Plan A resources are available for the first job, Kueue assigns Job 1 there.
     * Because Job 1 consumes the Plan A resources, Kueue automatically assigns Job 2 to the Plan B (DWS flex-start) pool.
  4. **Launch:** Kueue unsuspends the jobs. This action triggers the GKE cluster autoscaler to provision the nodes and start the training scripts.



### Connect to the RayJob

As a final verification step, you can use the `kubectl port-forward` command to connect to the Ray Dashboard and watch your jobs run.

To check the status of your first job, run the following command:
    
    
    kubectl port-forward service/rayjob-tpu-v6e-dws-1-head-svc 8265:8265 &
    

After you run this command, open a web browser and go to `http://localhost:8265`. In the Ray Dashboard, you can view the job status and reported metrics to verify that both jobs complete successfully on their respective node pools.

You can also view the logs for the first job by running the following command:
    
    
    kubectl logs job/rayjob-tpu-v6e-dws-1
    

The truncated output of the training script should resemble the following. You should see the messages `Training Complete!` and `Job 'rayjob-tpu-v6e-dws-1-498t6' succeeded` near the end of the output:
    
    
    (pid=, ip=10.68.3.4) 5] XLA::TPU program HBM usage: 52.5K / 31.25G
    (pid=, ip=10.68.9.4) :2152] XLA::TPU program VMEM usage: 141.0K / 128.00M [repeated 5x across cluster]
    (pid=, ip=10.68.9.4) I0320 03:59:34.722540     855 deepsea_compiler_backend.cc:2163] Total hbm usage >= 260.14M: [repeated 5x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777634     888 deepsea_compiler_backend.cc:2167]     reserved           204B [repeated 19x across cluster]
    (pid=, ip=10.68.9.4) I0320 03:59:34.722542     855 deepsea_compiler_backend.cc:2163]     program           70.0K  [repeated 5x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777626     888 deepsea_compiler_backend.cc:2163]     arguments            0B  [repeated 12x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777627     888 deepsea_compiler_backend.cc:2163] Output size 0B; shares 0B with arguments. [repeated 14x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777625     888 deepsea_compiler_backend.cc:2163] Total host usage >= 0B: [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777626     888 deepsea_compiler_backend.cc:2163]     program         unknown size  [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777634     888 deepsea_compiler_backend.cc:2167] Program sflag requirement 224B: [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777637     888 deepsea_compiler_backend.cc:2167]     scoped              40B [repeated 21x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777636     888 deepsea_compiler_backend.cc:2167] Program vmem requirement 141.0K: [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777637     888 deepsea_compiler_backend.cc:2167] Program smem requirement 40B: [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777637     888 deepsea_compiler_backend.cc:2167] Program host requirement 0B: [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777637     888 deepsea_compiler_backend.cc:2167] Program hbm requirement 70.0K: [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777638     888 deepsea_compiler_backend.cc:2167]     overlays          70.0K [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777638     888 deepsea_compiler_backend.cc:2175] XLA::TPU program SMEM usage: 1.9K / 1.00M (3 parameters) [repeated 7x across cluster]
    (pid=, ip=10.68.6.4) I0320 03:59:34.777636     888 deepsea_compiler_backend.cc:2167]     HLO temp          76.0K (0.0% utilization: Unpadded (0B) Padded (0B), 100.0% fragmentation (76.0K)) [repeated 14x across cluster]
    (RayTrainWorker pid=542, ip=10.68.6.4) Training Complete! [repeated 3x across cluster]
    (RayTrainWorker pid=542, ip=10.68.6.4) Epoch 40: Loss 0.0000 [repeated 3x across cluster]
    2026-03-20 03:59:51,008 SUCC cli.py:65 -- ------------------------------------------
    2026-03-20 03:59:51,008 SUCC cli.py:66 -- Job 'rayjob-tpu-v6e-dws-1-498t6' succeeded
    2026-03-20 03:59:51,008 SUCC cli.py:67 -- ------------------------------------------
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this document, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 


* In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

* In the project list, select the project that you want to delete, and then click **Delete**. 
* In the dialog, type the project ID, and then click **Shut down** to delete the project. 

### Delete the individual resources

If you want to keep the GGoogle Cloud project you used in this document, run the following command to delete the cluster:
    
    
    gcloud container clusters delete ${CLUSTER_NAME} \
        --location=${ZONE} \
        --project=${PROJECT_ID} \
        --quiet
    

## Summary

In this document, you configured and tested a Ray training environment. This environment uses a primary node pool and a backup DWS pool to maximize hardware availability. By automatically falling back to DWS when primary machines are unavailable, you minimized the time your training jobs spend waiting in line.

To get this working, you performed the following steps:

  1. **Created a GKE cluster:** Established the environment to host the node pools and scheduling tools.
  2. **Configured the node pools:** Created an on-demand node pool (Plan A) and a DWS node pool (Plan B).
  3. **Installed and configured Kueue:** Deployed the Kueue controller and applied priority rules instructing the system to try Plan A first and fall back to Plan B.
  4. **Created a ConfigMap:** Deployed a simplified JAX training script to the cluster to serve as the test workload.
  5. **Defined a RayJob manifest:** Configured the job to request specific hardware, route to the Kueue controller, and tolerate DWS nodes.
  6. **Submitted the workload:** Submitted two jobs to force Kueue to automatically route the second job to Plan B when Plan A resources are consumed.
  7. **Verified the results:** Used port forwarding to connect to the Ray Dashboard and confirmed that both jobs ran successfully.



## What's next

  * [Learn how to view logs and metrics for your Ray clusters and jobs](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics).
  * [Learn how to manage larger, distributed TPU workloads that span multiple slices](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
