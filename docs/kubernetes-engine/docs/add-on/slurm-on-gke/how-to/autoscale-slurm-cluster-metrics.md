---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/autoscale-slurm-cluster-metrics/
title: Autoscale a Slurm cluster using metrics \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:12.493820+00:00
---

# Autoscale a Slurm cluster using metrics  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/autoscale-slurm-cluster-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Autoscale a Slurm cluster using metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Slurm Operator add-on for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to configure a metric-based autoscaling approach on your Slurm cluster on Google Kubernetes Engine (GKE). A metric-based approach lets you scale your Slurm workers dynamically to zero during inactivity, and expand the node footprint rapidly to meet sudden high-priority batch workloads.

In this document, you deploy [Kubernetes Event-driven Autoscaling (KEDA)](https://keda.sh/) and configure Google Cloud Managed Service for Prometheus to collect metrics from your model.

This document is for Data administrators, Operators, and Developers who want to enable and configure the Slurm cluster on GKE.

Before reading this document, ensure that you're familiar with the [Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon).

## How metric-based autoscaling works

Metric-based autoscaling coordinates workload-level demands with GKE infrastructure provisioning to ensure that the cluster only allocates resources to handle active and pending jobs.

  * **Application scaling:** Google Cloud Managed Service for Prometheus scrapes queue metrics (such as pending jobs) from the Slurm controller. A KEDA `ScaledObject` monitors these metrics. When a queue backlog builds up, KEDA increases the replica count in the Slurm Operator `NodeSet` custom resource, and the Slurm Operator creates new `slurmd` worker Pods.
  * **Infrastructure scaling:** if these new worker Pods cannot fit on existing nodes, the GKE cluster Autoscaler detects the pending Pods and automatically provisions new machines in your compute node pool. When worker Pods are deleted, the autoscaler removes the empty nodes to save costs.



### Node scale-down safety

To prevent running nodes from being abruptly deprovisioned during downscale operations, the system applies the following safety policies:

  * **Graceful draining:** to prevent running nodes from being interrupted during scale-down events, the Slurm Operator calls the Slurm REST API to set the corresponding worker node to a `DRAIN` state. The operator blocks Pod deletion until Slurm confirms the node finished all running jobs.
  * **Intelligent Pod selection:** when scaling down, the Slurm Operator ranks all active Pods to decide which to delete first. Idle Pods without running workloads lack a workload deadline annotation, so the operator prioritizes them for deletion over busy nodes.



## Prepare your cluster

  1. Create a GKE cluster with autoscaling and the Google Cloud Managed Service for Prometheus add-on enabled:
         
         gcloud container clusters create CLUSTER_NAME \
             --project PROJECT_ID \
             --location CLUSTER_LOCATION \
             --addons=GcpFilestoreCsiDriver,SlurmOperator \
             --cluster-version="GKE_VERSION" \
             --release-channel=rapid \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --enable-managed-prometheus \
             --enable-autoscaling \
             --min-nodes=1 \
             --max-nodes=10
         

Replace the following:

     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `CLUSTER_LOCATION`: the location of your GKE cluster.
     * `GKE_VERSION`: the version of GKE to use, which must be 1.35.2-gke.1842000 or later.
  2. Create a CPU-based node pool with autoscaling enabled:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --zone=NODE_POOL_ZONE \
             --num-nodes=1 \
             --enable-autoscaling \
             --min-nodes=1 \
             --max-nodes=10 \
             --node-taints "slurm-pool=cpu-nodes:NoSchedule" \
             --spot
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your node pool.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `NODE_POOL_ZONE`: the zone of your node pool.
  3. Create a node pool for login nodes only:
         
         gcloud container node-pools create login-pool \
             --cluster=CLUSTER_NAME \
             --zone=NODE_POOL_ZONE \
             --node-taints "login-pool=login-pods:NoSchedule"
         




At this point you should have a Slurm cluster with two node pools, one for login nodes and one for worker nodes.

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
         




At this point you should have a Slurm cluster with two node pools, one for login nodes and one for worker nodes, and a Filestore instance with a PV and PVC.

## Configure OS Login

OS Login simplifies SSH access management by linking your Linux user account to your IAM identity. This configuration lets you manage access to Slurm nodes by using IAM permissions.

**Warning:** OS Login is not supported for node pools that use the GKE metadata server, which includes node pools with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled. If you need both Workload Identity Federation for GKE and OS Login in your Slurm cluster consider creating a separate node pool for the loginset.

  1. Grant necessary IAM roles. Ensure your user account has the necessary IAM roles in the project:

     * `roles/compute.osLogin`: lets you manage your own OS Login profile.
     * `roles/compute.instanceAdmin.v1`: provides permissions to manage compute instances.
     * `roles/iam.serviceAccountUser`: lets users act as a service account, which is often needed for node operations.

For more information about the required roles, see [the guide to set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#assign_os_login_iam_roles).

  2. Add your SSH key to OS Login by uploading your public SSH key:
         
         gcloud compute os-login ssh-keys add --key-file=PATH_TO_PUBLIC_KEY --project=PROJECT_ID
         

Alternatively, you can add a key that's loaded in your `ssh-agent`:
         
         gcloud compute os-login ssh-keys add --key="$(ssh-add -L | grep publickey | head -n 1)" --project=PROJECT_ID
         

  3. Enable OS Login in your project metadata:
         
         gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE --project=PROJECT_ID
         

  4. Get your OS Login username:
         
         gcloud compute os-login describe-profile | grep username
         

The output is similar to the following:
         
         username: OSLOGIN_USERNAME
         

The output includes the `OSLOGIN_USERNAME` value. You use this value later in this document.


**Best practice** : 

For managing OS Login across multiple projects in an organization, consider enforcing OS Login by using an Organization Policy Service constraint (`compute.requireOsLogin`). This is a recommended security best practice. For more information, see [Enable and configure OS Login in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-oslogin).

## Update Helm deployment

In the following section, create the `values.yaml` file to enable the Slurm controller to use Google Cloud Managed Service for Prometheus for monitoring.

  1. Save the following configuration to a new file named `values.yaml`:
         
         imagePullPolicy: IfNotPresent
         
         controller:
           slurmctld:
             image:
               repository: gcr.io/gke-release/slinky/slurmctld
               tag: TAG
           reconfigure:
             image:
               repository: gcr.io/gke-release/slinky/slurmctld
               tag: TAG
           logfile:
             image:
               repository: docker.io/library/alpine
               tag: latest
           persistence:
             enabled: true
             existingClaim: ""
             storageClassName: null
             accessModes:
             - ReadWriteOnce
             resources:
               requests:
                 storage: 4Gi
           extraConf: null
         
           metadata:
             labels:
               app: slurmctld
           extraConfMap:
             SlurmctldDebug: verbose
             MetricsType: metrics/openmetrics
           metrics:
             enabled: true
             serviceMonitor:
               enabled: false
         
         restapi:
           replicas: 1
           slurmrestd:
             image:
               repository: gcr.io/gke-release/slinky/slurmrestd
               tag: TAG
           podSpec:
             nodeSelector:
               kubernetes.io/os: linux
         
         loginsets:
           slinky:
             enabled: true
             replicas: 1
             podSpec:
               tolerations:
                 - key: "login-pool"
                   operator: "Equal"
                   value: "login-pods"
                   effect: "NoSchedule"
               volumes:
                 - name: home-vol
                   persistentVolumeClaim:
                     claimName: PVC_NAME
             login:
               image:
                 repository: gcr.io/gke-release/slinky/login
                 tag: TAG
               volumeMounts:
                 - name: home-vol
                   mountPath: /home
         
         nodesets:
           slinky:
             enabled: false
           cpu-nodes:
             enabled: true
             replicas: 1
             updateStrategy:
               type: RollingUpdate
             slurmd:
               args: [" -N ${POD_NAME#slurm-worker-}"]
               env:
                 - name: POD_NAME
                   valueFrom:
                     fieldRef:
                       fieldPath: metadata.name
               image:
                 repository: gcr.io/gke-release/slinky/slurmd
                 tag: TAG
               imagePullPolicy: IfNotPresent
               volumeMounts:
                 - name: home-vol
                   mountPath: /home
             logfile:
               image:
                 repository: docker.io/library/alpine
                 tag: latest
             partition:
               enabled: true
               useResourceLimits: true
               updateStrategy:
                 type: RollingUpdate
                 rollingUpdate:
                   maxUnavailable: 25%
             podSpec:
               hostNetwork: true
               dnsPolicy: ClusterFirstWithHostNet
               tolerations:
                 - key: "slurm-pool"
                   operator: "Equal"
                   value: "cpu-nodes"
                   effect: "NoSchedule"
               nodeSelector:
                 kubernetes.io/os: linux
               volumes:
                 - name: home-vol
                   persistentVolumeClaim:
                     claimName: PVC_NAME
             taintKubeNodes: false
         
         partitions:
           all:
             enabled: false
           cpu-partition:
             enabled: true
             nodesets:
               - cpu-nodes
             configMap:
               State: UP
               Default: "YES"
               MaxTime: UNLIMITED
         

  2. Install the Slurm Helm chart by using the updated `values.yaml` file:
         
         helm install slurm oci://ghcr.io/slinkyproject/charts/slurm \
             --namespace=slurm --create-namespace --version 1.0.2 -f values.yaml
         




## Install KEDA

To install KEDA on your cluster, deploy the KEDA operator manifests:
    
    
    kubectl apply --server-side -f https://github.com/kedacore/keda/releases/download/v2.15.1/keda-2.15.1.yaml
    

## Configure IAM and Workload Identity Federation for GKE

KEDA needs read access to Google Cloud Managed Service for Prometheus metrics. Grant the [Monitoring Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) on the project to the `keda-operator` Kubernetes ServiceAccount:
    
    
    gcloud projects add-iam-policy-binding projects/PROJECT_ID \
        --role=roles/monitoring.viewer \
        --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/keda/sa/keda-operator \
        --condition=None
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `PROJECT_NUMBER`: your numerical Google Cloud project number.



## Deploy metrics exporter and KEDA config

To determine when to scale up or scale down the cluster, KEDA evaluates a specific metric query. The manifest in the following steps uses a recommended query that calculates the total of pending Jobs and allocated nodes in the partition.

  1. Save the following manifest as `autoscaling-config.yaml`:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: slurm-metrics-exporter
           namespace: slurm
         spec:
           selector:
             matchLabels:
               app: slurmctld
           endpoints:
           - port: 6817
             path: /metrics/partitions
             interval: 5s
         ---
         apiVersion: keda.sh/v1alpha1
         kind: ClusterTriggerAuthentication
         metadata:
           name: google-workload-identity-auth
           namespace: slurm
         spec:
           podIdentity:
             provider: gcp
         ---
         apiVersion: keda.sh/v1alpha1
         kind: ScaledObject
         metadata:
           name: slurm-worker-cpu-nodes-scaler
           namespace: slurm
         spec:
           scaleTargetRef:
             apiVersion: slinky.slurm.net/v1beta1
             kind: NodeSet
             name: slurm-worker-cpu-nodes
           minReplicaCount: 1
           maxReplicaCount: 10
           pollingInterval: 5
           cooldownPeriod: 30
           triggers:
           - type: prometheus
             metadata:
               serverAddress: https://monitoring.googleapis.com/v1/projects/PROJECT_ID/location/global/prometheus
               query: |
                 sum(slurm_partition_jobs_pending{project_id="PROJECT_ID",partition="cpu-partition",cluster="CLUSTER_NAME"})+sum(slurm_partition_nodes_alloc{project_id="PROJECT_ID",partition="cpu-partition",cluster="CLUSTER_NAME"})
               threshold: "1.0"
             authenticationRef:
               kind: ClusterTriggerAuthentication
               name: google-workload-identity-auth
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `CLUSTER_NAME`: the name of your GKE cluster.
**Note:** The preceding sample query works best for single-node Jobs. This sample might not produce correct results for workloads that use multiple nodes. You can customize this query to fit your needs.
  2. Apply the configurations to your cluster:
         
         kubectl apply -f autoscaling-config.yaml
         




At this point, KEDA is monitoring the Slurm metrics and will scale the cluster based on the number of pending Jobs and allocated nodes.

## Verify metrics-based autoscaling

To verify that the metrics-based autoscaling is working as expected, you can submit several batch jobs to the Slurm queue and observe the worker nodes scaling up and down dynamically.

  1. Get the external IP address of the login service:
         
         kubectl get service --namespace slurm slurm-login-slinky
         

  2. Copy the value of the `EXTERNAL-IP` column.

  3. Create a sample batch script:
         
         cat << 'EOF' > sleep-job.sh
         #!/bin/bash
         #SBATCH --job-name=simple_sleep
         #SBATCH --output=sleep_job_%j.out
         #SBATCH --error=sleep_job_%j.err
         #SBATCH --time=00:10:00
         #SBATCH --nodes=1
         #SBATCH --ntasks=1
         #SBATCH --cpus-per-task=1
         
         echo "Starting job at $(date)"
         echo "Sleeping for 5 minutes..."
         sleep 300
         echo "Finished job at $(date)"
         EOF
         

  4. Upload the script to the login node:
         
         scp sleep-job.sh OSLOGIN_USERNAME@EXTERNAL_IP:~/
         

  5. Connect to the login node instance by using SSH:
         
         ssh OSLOGIN_USERNAME@EXTERNAL_IP
         

Replace the following:

     * `EXTERNAL_IP`: the IP address obtained in the previous step.
     * `OSLOGIN_USERNAME`: your OS Login username.
  6. Submit the job script three times to the queue:
         
         sbatch sleep-job.sh
         sbatch sleep-job.sh
         sbatch sleep-job.sh
         

  7. To see how the number of nodes change, in a separate terminal session, run the following command:
         
         kubectl get nodes --watch
         

KEDA detects the pending workloads and scales the `NodeSet`. The GKE Autoscaler provisions new compute nodes to accommodate the worker Pods. You should see new nodes being added to handle the workload.

  8. In the login node, check how the worker nodes are added to the Slurm cluster:
         
         sinfo
         

While the new nodes are transitioning, the output shows their status as `alloc` and `idle`:
         
         PARTITION      AVAIL  TIMELIMIT  NODES  STATE NODELIST
         cpu-nodes         up   infinite      1  alloc cpu-nodes-0
         cpu-nodes         up   infinite      2   idle cpu-nodes-[1-2]
         cpu-partition*    up   infinite      1  alloc cpu-nodes-0
         cpu-partition*    up   infinite      2   idle cpu-nodes-[1-2]
         

  9. After a few minutes, check the node status again. All nodes transition to the allocated state to run the submitted jobs:
         
         PARTITION      AVAIL  TIMELIMIT  NODES  STATE NODELIST
         cpu-nodes         up   infinite      3  alloc cpu-nodes-[0-2]
         cpu-partition*    up   infinite      3  alloc cpu-nodes-[0-2]
         

  10. Verify the state of the running jobs:
         
         squeue
         

The output displays the active jobs running on the nodes:
         
         JOBID PARTITION NAME     USER                             ST      TIME  NODES NODELIST(REASON)
             8 cpu-parti simple_s USERNAME  R       1:28      1 cpu-nodes-1
             9 cpu-parti simple_s USERNAME  R       1:28      1 cpu-nodes-2
             7 cpu-parti simple_s USERNAME  R       2:28      1 cpu-nodes-0
         

  11. Verify the cluster downscale:

When the batch workloads finish running, KEDA waits for the cooldown period before scaling down.

     1. After the jobs finish, verify that the nodes returned to the idle state:
            
            sinfo
            

The output should show three idle nodes:
            
            PARTITION      AVAIL  TIMELIMIT  NODES  STATE NODELIST
            cpu-nodes         up   infinite      3   idle cpu-nodes-[0-2]
            cpu-partition*    up   infinite      3   idle cpu-nodes-[0-2]
            

     2. Wait several minutes for KEDA cooldown and downscale rules to apply, then query `sinfo` again:
            
            sinfo
            

The output shows that the cluster scaled back down to a single node:
            
            PARTITION      AVAIL  TIMELIMIT  NODES  STATE NODELIST
            cpu-nodes         up   infinite      1   idle cpu-nodes-0
            cpu-partition*    up   infinite      1  idle cpu-nodes-0
            

     3. In your local terminal, verify that nodes have been removed:
            
            kubectl get nodes
            

The output should show that GKE removed nodes that are no longer needed.

This confirms that metrics-based autoscaling dynamically manages your Slurm cluster compute resources.


**Success:** You have successfully configured metrics-based autoscaling for your Slurm cluster!

## Clean up

Uninstall KEDA and delete the monitoring configuration resources:
    
    
    kubectl delete -f autoscaling-config.yaml
    kubectl delete -f https://github.com/kedacore/keda/releases/download/v2.15.1/keda-2.15.1.yaml
    

## What's next

  * Explore the [Slurm Project on GitHub](https://github.com/SlinkyProject/slurm-operator).
  * Learn more about [KEDA autoscaling policies](https://keda.sh/docs/).
  * Read about [IAM permissions for Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
