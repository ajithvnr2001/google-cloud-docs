---
url: https://docs.cloud.google.com/filestore/docs/agent-substrate/
title: Use Filestore agent volumes with GKE Agent Substrate \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:48.085532+00:00
---

# Use Filestore agent volumes with GKE Agent Substrate  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/agent-substrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Use Filestore agent volumes with GKE Agent Substrate Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

Google Kubernetes Engine (GKE) Agent Substrate is an infrastructure platform that manages the lifecycle of stateful AI agent sandboxes. Agent Substrate lets platforms suspend idle agent workloads to save compute costs and resume them in under a second when new prompts or tasks arrive.

Filestore agent volumes provide the persistent storage layer for Agent Substrate, preserving workspace files, code repositories, and scratchpad artifacts across sandbox suspend and resume cycles.

## How Agent Substrate uses agent volumes

The following steps describe how Agent Substrate and Filestore agent volumes support an interactive coding agent that helps developers build features, run tests, and debug code:

  1. **Session initialization:** When a developer submits a task, Agent Substrate creates a sandbox environment on GKE and mounts a dedicated Filestore volume. The agent clones the project repository, installs dependencies, and prepares the workspace.
  2. **Cost-efficient idle suspension:** While the developer reviews code diffs or crafts the next prompt, Agent Substrate unmounts the volume and terminates the compute environment. Compute resource utilization drops to zero, while all workspace files, Git history, and build caches remain persisted in the volume.
  3. **Instant resumption:** When the developer sends a new prompt, Agent Substrate claims a pre-warmed sandbox and reattaches the existing volume in under 100 ms. The agent immediately resumes the workload with full file system context intact, avoiding time-consuming repository re-clones or dependency reinstalls.



For more information, see the [Agent Substrate documentation](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate).

To run stateful agent workloads on GKE Agent Substrate with Filestore agent volumes, you install Agent Substrate, configure the Filestore CSI driver integration, and define your agent workloads to use dynamic CSI volumes.

## Install Agent Substrate

To prepare your Google Cloud project and install Agent Substrate on a GKE Standard cluster, follow the instructions in [Install Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate).

## Install and configure the Filestore CSI driver

To use Filestore agent volumes with Agent Substrate, you must select the optional **Filestore CSI driver** step when running the interactive Agent Substrate installer.

The Agent Substrate control plane (`ateapi`) communicates directly with the Filestore CSI driver controller over network gRPC. The CSI driver dynamically provisions, attaches, and detaches per-actor volumes from your Filestore volume pool in synchronization with each actor's lifecycle.

**Note:** If you didn't install the CSI driver with the Agent Substrate installer, you can install it manually using the automated deployment script (`deploy.sh`) or Kustomize manifests in the [GKE Substrate Integration Overlay guide](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver/tree/master/deploy/kubernetes/overlays/substrate).

## Create workloads that use Filestore volumes

In Agent Substrate, you define external Filestore volumes declaratively in an `ActorTemplate` resource rather than creating separate Kubernetes `PersistentVolumeClaim` objects. The following steps walk you through configuring a Filestore `StorageClass` and `CSIDriverConfig`, deploying a `WorkerPool` and `ActorTemplate` that mount an external Filestore volume, and managing the actor lifecycle.

### Create the `StorageClass`

Create a file named `storageclass.yaml` to provision dynamic volumes from your Filestore volume pool:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: substrate-volumepool-sc
    provisioner: filestore.csi.storage.gke.io
    parameters:
      volume-pool: "projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_NAME"
    allowVolumeExpansion: false
    reclaimPolicy: Delete
    volumeBindingMode: Immediate
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region where your volume pool resides, such as `us-central1`.
  * `VOLUME_POOL_NAME`: the name of your Filestore volume pool.



Apply the `StorageClass`:
    
    
    kubectl apply -f storageclass.yaml
    

**Note:** If you deployed the CSI driver using `deploy.sh` with the `--volumepool-location` and `--volumepool-name` flags, the `StorageClass` is created automatically.

### Register the `CSIDriverConfig`

The `CSIDriverConfig` resource bridges the Kubernetes `StorageClass` provisioner (`filestore.csi.storage.gke.io`) to the network gRPC endpoint of the Filestore CSI controller service and the local Unix domain socket path of the CSI node plugin.

Create a file named `csi-driver-config.yaml`:
    
    
    apiVersion: ate.dev/v1alpha1
    kind: CSIDriverConfig
    metadata:
      name: filestore.csi.storage.gke.io
    spec:
      driverName: filestore.csi.storage.gke.io
      controllerEndpoint: tcp://csi-filestore-controller.gcp-filestore-csi-driver.svc:10000
      nodeSocketOverride: unix:///var/lib/kubelet/plugins/filestore.csi.storage.gke.io/csi.sock
      tls:
        enabled: true
        usePodIdentity: true
        serverName: csi-filestore-controller.gcp-filestore-csi-driver.svc
    

Apply the `CSIDriverConfig`:
    
    
    kubectl apply -f csi-driver-config.yaml
    

**Note:** If you installed the CSI driver using the Agent Substrate installer or `deploy.sh`, this `CSIDriverConfig` resource is registered automatically.

### Define the `WorkerPool` and `ActorTemplate`

  1. Create the `ate-demo` atespace and Kubernetes namespace to serve as the isolation boundary for your worker pool, actor template, and actors:
         
         kubectl ate create atespace ate-demo
         kubectl create namespace ate-demo
         

  2. Create a `WorkerPool` resource to maintain physical standby workloads ready to host actor sandboxes. Save the following manifest as `worker-pool.yaml`:
         
         apiVersion: ate.dev/v1alpha1
         kind: WorkerPool
         metadata:
           name: agent-pool
           namespace: ate-demo
           labels:
             workload: stateful-agent
         spec:
           replicas: 5
           workerImage: ko://github.com/agent-substrate/substrate/cmd/ateom-gvisor
         

  3. Apply the `WorkerPool` manifest:
         
         kubectl apply -f worker-pool.yaml
         

  4. Create a file named `actor-template.yaml` defining the `ActorTemplate` that mounts a 5 GiB volume from `substrate-volumepool-sc`:
         
         metadata:
           atespace: ate-demo
           name: stateful-agent-template
         workerSelector:
           matchLabels:
             workload: stateful-agent
         containers:
         - name: agent
           image: CONTAINER_IMAGE
           volumeMounts:
           - name: shared-storage
             mountPath: /mnt/shared
           readyz:
             httpGet:
               path: /readyz
               port: 8080
         sandboxConfig:
           sandboxClass: SANDBOX_CLASS_GVISOR
           configName: gvisor-default
         snapshotsConfig:
           storageLocation: gs://SNAPSHOT_BUCKET/stateful-agent
         volumes:
         - name: shared-storage
           externalVolumeTemplate:
             capacity: 5Gi
             storageClassName: substrate-volumepool-sc
         

Replace the following:

     * `CONTAINER_IMAGE`: the container image for your agent workload, such as `gcr.io/my-project/agent-app@sha256:7f28ab0...`.
     * `SNAPSHOT_BUCKET`: the Cloud Storage bucket used by Agent Substrate to store actor snapshots.

In this manifest, `volumes[].externalVolumeTemplate` specifies the requested volume capacity (`5Gi`) and the `StorageClass` (`substrate-volumepool-sc`) whose provisioner matches your `CSIDriverConfig`, while `containers[].volumeMounts` mounts that volume at `/mnt/shared`. Every volume declared in `volumes` must be mounted by at least one container.

  5. Create the `ActorTemplate` through the Agent Substrate API using the `kubectl ate` CLI:
         
         kubectl ate create actor-template -f actor-template.yaml
         




### Create, suspend, and resume an actor

Once the `ActorTemplate` is created and its golden snapshot is ready, you can create an actor instance and manage its execution state:

  1. Create a new actor from `stateful-agent-template`:
         
         kubectl ate create actor ACTOR_NAME \
             --template=stateful-agent-template \
             -a ate-demo
         

Replace `ACTOR_NAME` with a DNS-1123 label name for your actor, such as `my-agent-1`.

When you create the actor, Agent Substrate dynamically provisions a dedicated Filestore volume from `substrate-volumepool-sc` and mounts it at `/mnt/shared`.

  2. Suspend the actor when it becomes idle:
         
         kubectl ate suspend actor ACTOR_NAME \
             -a ate-demo
         

Suspending the actor checkpoints its memory state to Cloud Storage, unmounts and detaches the Filestore volume while preserving all workspace files on the volume, and releases the workload.

  3. Resume the actor when a new request or task arrives:
         
         kubectl ate resume actor ACTOR_NAME \
             -a ate-demo
         

Resuming the actor assigns it to an available workload, restores its memory snapshot, and reattaches the existing Filestore volume at `/mnt/shared` with all files intact.




## What's next

  * Set up the environment for [GKE](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).
  * Configure pre-warmed sandboxes with [Agent Sandbox](https://docs.cloud.google.com/filestore/docs/agent-sandbox).
  * Explore dynamic storage with [Agent Sandbox late-binding](https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
