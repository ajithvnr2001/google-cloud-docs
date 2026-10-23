---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/ephemeral-rayjobs-kueue-concurrent-admission/
title: Start RayJobs faster across multiple compute options \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:46.261573+00:00
---

# Start RayJobs faster across multiple compute options  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/ephemeral-rayjobs-kueue-concurrent-admission/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Start RayJobs faster across multiple compute options Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to configure and deploy ephemeral RayJobs on Google Kubernetes Engine (GKE) using Kueue concurrent admission to place and migrate the job across compute options.

Running an _ephemeral RayJob_ means that you submit a job definition to Kubernetes, where the operator automatically provisions a dedicated Ray cluster, runs your workload to completion, retrieves the results and status, and immediately deletes the cluster to release resources.

[Concurrent admission](https://kueue.sigs.k8s.io/docs/concepts/concurrent_admission/) is a Kueue feature that allows ephemeral RayJobs to start immediately on available resources and fall back across different compute options—such as reservations, Dynamic Workload Scheduler Calendar, Flex-start VMs, on-demand, and Spot VMs—within a single job request. Rather than waiting idly for a specific preferred compute option to become available, a RayJob can start immediately using any available compute option, reducing time-to-start while maximizing overall fleet utilization across your provisioned capacity.

## How concurrent admission works

Concurrent admission is an alpha Kueue feature (available in Kueue v0.18 or later) that changes how jobs are placed across compute options:

  * **Concurrent evaluation:** Rather than evaluating compute options serially, Kueue attempts admission across multiple acceptable compute options (also called [ResourceFlavors](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/)) concurrently. By generating parallel workload variants for each compute option, Kueue schedules and runs the entire job on the first compute option that has available capacity.
  * **Optional migration:** If enabled (`concurrentAdmissionPolicy.migration.mode: TryPreferredFlavors`), Kueue continues attempting admission across more preferred compute options concurrently. If a more preferred compute option becomes available later, Kueue migrates the running job to it. If migration is disabled or omitted, the job remains on its initial compute option to avoid restart disruption.
  * **Workload structure:** Kueue implements concurrent admission by marking the original workload as a _parent_ and creating one _variant_ workload per ResourceFlavor. Each variant attempts admission for a single ResourceFlavor independently. When one is admitted, the parent is admitted, and the remaining variants are deactivated.

**Note:** The order of ResourceFlavors in the ClusterQueue defines preference (the first ResourceFlavor listed is the most preferred). 

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



Make sure you have the following command-line tools installed:

  * The Google Cloud CLI (`gcloud`)
  * `kubectl`



### Requirements and limitations

  * **Kueue version:** Concurrent admission requires Kueue _v0.18 or later_.
  * **Single-compute-option constraint:** Concurrent admission requires all PodSets in a workload—including the Ray head and worker group—to be associated with the same single ResourceFlavor. Decoupled compute option assignment (such as scheduling the Ray head node on a standard CPU compute option while placing worker nodes on GPU or TPU compute options) is not supported under concurrent admission policies.



## Step 1: Create and connect to the GKE cluster

In this step, you define your environment variables, create a Standard cluster with the Ray operator add-on enabled, create a Compute Engine GPU reservation, add the GPU node pools, and connect to your cluster.

  1. Set environment variables for your project, zone, and cluster name:
         
         export PROJECT_ID=PROJECT_ID
         export ZONE=ZONE
         export CLUSTER_NAME=gpu-cluster
         

Replace `PROJECT_ID` with your Google Cloud project ID, and `ZONE` with your target compute zone (for example, `us-central1-a`).

  2. Create a Standard GKE cluster with the Ray operator add-on enabled:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --zone=${ZONE} \
             --machine-type=n2-standard-4 \
             --num-nodes=2 \
             --addons=RayOperator
         

  3. Create a Compute Engine GPU reservation for the GPU node pool to consume. Specify the `--require-specific-reservation` flag to prevent non-GKE VMs from consuming the capacity:
         
         gcloud compute reservations create my-gpu-reservation \
             --project=${PROJECT_ID} \
             --zone=${ZONE} \
             --vm-count=3 \
             --machine-type=n1-standard-4 \
             --accelerator=type=nvidia-tesla-t4,count=1 \
             --require-specific-reservation
         

**Note:** Size the reservation to hold the entire worker group (3 VMs for 3 workers requesting 1 GPU each), because concurrent admission migrates all 3 GPU workers onto the reservation together. 
  4. Create the GPU node pools. In this example, you create a GPU pool of reservations and a GPU pool of Flex-start VMs that use NVIDIA T4 GPUs:

     * **Create the reservation GPU node pool:**
           
           gcloud container node-pools create gpu-pool-reservation \
               --cluster=${CLUSTER_NAME} \
               --project=${PROJECT_ID} \
               --zone=${ZONE} \
               --machine-type=n1-standard-4 \
               --accelerator=type=nvidia-tesla-t4,count=1 \
               --reservation-affinity=specific \
               --reservation=my-gpu-reservation \
               --num-nodes=0 \
               --enable-autoscaling --min-nodes=0 --max-nodes=3
           

     * **Create the GPU node pool of Flex-start VMs:**
           
           gcloud container node-pools create gpu-pool-dws-flex \
               --cluster=${CLUSTER_NAME} \
               --project=${PROJECT_ID} \
               --zone=${ZONE} \
               --machine-type=n1-standard-4 \
               --accelerator=type=nvidia-tesla-t4,count=1 \
               --num-nodes=0 \
               --enable-autoscaling --min-nodes=0 --max-nodes=3 \
               --flex-start \
               --location-policy=ANY \
               --reservation-affinity=none
           

  5. Retrieve cluster credentials to configure `kubectl`:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --zone=${ZONE}
         




## Step 2: Install Kueue

  1. Install the Kueue manifests:
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.18.0/manifests.yaml
         

  2. Enable the `ConcurrentAdmission` feature gate by editing the `kueue-manager-config` ConfigMap in the `kueue-system` namespace:
         
         kubectl edit configmap kueue-manager-config -n kueue-system
         

Add the `featureGates` entry to the `controller_manager_config.yaml` data:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: kueue-manager-config
           namespace: kueue-system
         data:
           controller_manager_config.yaml: |
             apiVersion: config.kueue.x-k8s.io/v1beta2
             kind: Configuration
             featureGates:
               ConcurrentAdmission: true
             # ... keep the rest of the existing configuration ...
         

  3. Restart the Kueue controller manager deployment to apply the configuration:
         
         kubectl rollout restart deployment kueue-controller-manager -n kueue-system
         




## Step 3: Configure Kueue

Create the ResourceFlavor resources (representing capacity from reservations and Flex-start VMs), a ClusterQueue with a concurrent admission policy, and a LocalQueue.

Important considerations for this configuration include the following:

  * The ClusterQueue must use the `queueingStrategy: BestEffortFIFO` key-value pair. The `StrictFIFO` value for this field is not supported with concurrent admission.
  * The ClusterQueue must have exactly one `resourceGroup` containing at most 16 compute options.
  * Compute options are listed in order of preference: the `reservation-flavor` field is listed first, followed by the `dws-flex-flavor` field.
  * The `spec.concurrentAdmissionPolicy` field is immutable after the ClusterQueue is created. To modify the policy, delete and re-create the ClusterQueue.

**Caution:** Concurrent admission requires all PodSets in a workload—including the Ray head and worker group—to be associated with the same single ResourceFlavor. Decoupled compute option assignment (such as scheduling the Ray head node on a standard CPU compute option while placing worker nodes on GPU or TPU compute options) is not supported under concurrent admission policies. If your workloads require scheduling a standalone CPU Ray head under concurrent admission, file a feature request on the [Kueue GitHub repository](https://github.com/kubernetes-sigs/kueue/issues). 

  1. Create a file named `kueue-setup.yaml` with the following:
         
         apiVersion: kueue.x-k8s.io/v1beta2
         kind: ResourceFlavor
         metadata:
           name: reservation-flavor
         spec:
           nodeLabels:
             cloud.google.com/gke-nodepool: gpu-pool-reservation
         ---
         apiVersion: kueue.x-k8s.io/v1beta2
         kind: ResourceFlavor
         metadata:
           name: dws-flex-flavor
         spec:
           nodeLabels:
             cloud.google.com/gke-nodepool: gpu-pool-dws-flex
         ---
         apiVersion: kueue.x-k8s.io/v1beta2
         kind: ClusterQueue
         metadata:
           name: cluster-queue
         spec:
           namespaceSelector: {}
           queueingStrategy: BestEffortFIFO
           # Concurrent admission lets Kueue provision capacity in several flavors at
           # the same time instead of trying them one after another.
           concurrentAdmissionPolicy:
             migration:
               # Move the workload to an earlier (more preferred) flavor if that flavor
               # becomes ready first.
               mode: TryPreferredFlavors
               constraints:
                 # Stop trying additional flavors once this flavor is reached.
                 lastAcceptableFlavorName: reservation-flavor
           resourceGroups:
           - coveredResources: ["nvidia.com/gpu", "cpu", "memory"]
             flavors:
             - name: reservation-flavor
               resources:
               - name: "nvidia.com/gpu"
                 nominalQuota: "3"
               - name: "cpu"
                 nominalQuota: "8"
               - name: "memory"
                 nominalQuota: "32Gi"
             - name: dws-flex-flavor
               resources:
               - name: "nvidia.com/gpu"
                 nominalQuota: "3"
               - name: "cpu"
                 nominalQuota: "8"
               - name: "memory"
                 nominalQuota: "32Gi"
         ---
         apiVersion: kueue.x-k8s.io/v1beta2
         kind: LocalQueue
         metadata:
           name: user-queue
           namespace: default
         spec:
           clusterQueue: cluster-queue

  2. Apply the configuration to your cluster:
         
         kubectl apply -f kueue-setup.yaml
         




## Step 4: Define the ephemeral RayJob

With concurrent admission, each admitted variant associates the entire workload with one flavor, and Kueue injects that flavor's node selector onto the head and worker Pods. You define a single worker group (with three worker replicas) and let Kueue decide and migrate which GPU compute option runs it.

Important settings in this definition include the following:

  * **No compute option node selectors:** Do not associate the worker group with a specific node pool. Kueue automatically adds the node selector based on the admitted compute option.
  * **Head GPU toleration:** Because GKE taints GPU nodes with the `nvidia.com/gpu=present:NoSchedule` taint, the head Pod requires a matching toleration to colocate on a GPU node with a worker.
  * **Ephemeral behavior:** The `shutdownAfterJobFinishes: true` key-value pair instructs KubeRay to delete the Ray cluster when the job finishes.
  * **Disabled autoscaling:** Use fixed replicas (`minReplicas == maxReplicas`). Autoscaling is not recommended for ephemeral jobs.


  1. Create a file named `ephemeral-rayjob.yaml` with the following:
         
         apiVersion: ray.io/v1
         kind: RayJob
         metadata:
           name: ephemeral-gpu-job
           labels:
             # Kueue admits this RayJob through the LocalQueue defined in kueue-setup.yaml.
             kueue.x-k8s.io/queue-name: user-queue
         spec:
           entrypoint: |
             python -c "
             import ray, time, socket
             ray.init()
             print('Cluster resources:', ray.cluster_resources())
             @ray.remote(num_gpus=1)
             def gpu_task(task_id):
                 ip = socket.gethostbyname(socket.gethostname())
                 print(f'Task {task_id} running on node with IP: {ip}')
                 time.sleep(5)
                 return ip
             futures = [gpu_task.remote(i) for i in range(3)]
             results = ray.get(futures)
             print('Tasks successfully executed on nodes:', set(results))
             "
           # Delete the RayCluster after the job finishes, which makes the job ephemeral.
           shutdownAfterJobFinishes: true
           rayClusterSpec:
             rayVersion: '2.58.0'
             headGroupSpec:
               rayStartParams:
                 dashboard-host: '0.0.0.0'
               template:
                 spec:
                   tolerations:
                   - key: nvidia.com/gpu
                     operator: Exists
                     effect: NoSchedule
                   containers:
                   - name: ray-head
                     image: rayproject/ray:2.58.0
                     resources:
                       requests:
                         cpu: "1"
                         memory: "2Gi"
                       limits:
                         cpu: "1"
                         memory: "2Gi"
             workerGroupSpecs:
             - groupName: worker-group
               replicas: 3
               minReplicas: 3
               maxReplicas: 3
               rayStartParams: {}
               template:
                 spec:
                   nodeSelector:
                     cloud.google.com/gke-accelerator: nvidia-tesla-t4
                   containers:
                   - name: ray-worker
                     image: rayproject/ray:2.58.0
                     resources:
                       requests:
                         nvidia.com/gpu: "1"
                         cpu: "2"
                         memory: "8Gi"
                       limits:
                         nvidia.com/gpu: "1"
                         cpu: "2"
                         memory: "8Gi"

  2. Submit the RayJob to the cluster:
         
         kubectl apply -f ephemeral-rayjob.yaml
         




## Step 5: Monitor and verify concurrent admission

  1. Inspect the parent and variant workload objects:
         
         kubectl get workloads
         

To list only the parent workload, run the following command:
         
         kubectl get workloads -l kueue.x-k8s.io/concurrent-admission-parent=true
         

  2. Watch Pod creation and placement:
         
         kubectl get pods -w -o wide
         

The head and worker Pods land on nodes matching the admitted compute option. The head colocates on a GPU node with one of the workers, while the short-lived submitter Pod runs on the default CPU pool.

  3. Check the status of the RayJob:
         
         kubectl get rayjobs
         

  4. View the output logs from the running job:
         
         kubectl logs -l job-name=ephemeral-gpu-job
         

The output is similar to the following:
         
         Cluster resources: {'node:10.52.3.6': 1.0, 'node:__internal_head__': 1.0, 'memory': 27917287424.0, 'object_store_memory': 8194336357.0, 'CPU': 7.0, 'GPU': 3.0, 'node:10.52.3.7': 1.0, 'node:10.52.4.6': 1.0, 'node:10.52.2.6': 1.0}
         (gpu_task pid=277, ip=10.52.4.6) Task 0 running on node with IP: 10.52.4.6
         (gpu_task pid=275, ip=10.52.2.6) Task 2 running on node with IP: 10.52.2.6
         (gpu_task pid=276, ip=10.52.3.7) Task 1 running on node with IP: 10.52.3.7
         Tasks successfully executed on nodes: {'10.52.2.6', '10.52.4.6', '10.52.3.7'}
         Job 'ephemeral-gpu-job' succeeded
         

  5. After the job succeeds, verify that KubeRay automatically removed the Ray cluster Pods:
         
         kubectl get pods
         




## Step 6: (Optional) Start on Flex-start VMs and migrate to a reservation

This scenario demonstrates how a job starts on fallback capacity (Flex-start VMs) and subsequently upgrades to a reservation when quota becomes available.

  1. **Simulate initial condition (reservation occupied):** If the reservation quota is fully occupied by other workloads when the RayJob is submitted, the `reservation-flavor` variant cannot be admitted.
  2. **Job starts on fallback compute option (T1):** Kueue admits `dws-flex-flavor`, and the RayCluster is created on `gpu-pool-dws-flex`:
         
         kubectl get workloads
         

The output shows `dws-flex-flavor` admitted as `True`:
         
         NAME                                                          ADMITTED
         rayjob-ephemeral-gpu-job-[hash]                               True
         rayjob-ephemeral-gpu-job-variant-dws-flex-flavor-[hash]        True
         rayjob-ephemeral-gpu-job-variant-reservation-flavor-[hash]
         

  3. **Reservation capacity frees up (T2):** When capacity on the reservation becomes available, Kueue admits the `reservation-flavor` variant:
         
         kubectl get workloads -w
         
         
         NAME                                                          ADMITTED
         rayjob-ephemeral-gpu-job-[hash]                               True
         rayjob-ephemeral-gpu-job-variant-reservation-flavor-[hash]   True
         rayjob-ephemeral-gpu-job-variant-dws-flex-flavor-[hash]        False
         

  4. **Job migrates to reservation (T3):** Because the `reservation-flavor` compute option has higher priority, Kueue migrates the parent workload. Migration restarts the RayCluster on the new compute option, and the Pods are re-created on the `gpu-pool-reservation` compute option:
         
         kubectl get pods -o wide -w
         

**Note:** Migration restarts the job on the new compute option. Concurrent admission with migration is recommended for workloads that can tolerate restart disruption in exchange for reduced initial wait time. 



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this guide, delete the cluster and reservation:

  1. Delete the GKE cluster:
         
         gcloud container clusters delete ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --zone=${ZONE} \
             --quiet
         

  2. Delete the Compute Engine reservation:
         
         gcloud compute reservations delete my-gpu-reservation \
             --project=${PROJECT_ID} \
             --zone=${ZONE} \
             --quiet
         




## What's next

  * Learn more about [Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).
  * Read about [Kueue concurrent admission](https://kueue.sigs.k8s.io/docs/concepts/concurrent_admission/).
  * Explore [GPU sharing and provisioning strategies on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
