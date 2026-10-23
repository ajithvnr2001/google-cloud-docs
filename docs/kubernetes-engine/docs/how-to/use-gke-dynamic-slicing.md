---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-gke-dynamic-slicing/
title: Schedule dynamic slices with Kueue and TAS \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:40.703151+00:00
---

# Schedule dynamic slices with Kueue and TAS  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-gke-dynamic-slicing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Schedule dynamic slices with Kueue and TAS Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to provision TPU node pools and schedule dynamic slices in Google Kubernetes Engine (GKE) by using [Kueue](https://kueue.sigs.k8s.io/docs/overview/) and [Topology Aware Scheduling (TAS)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas#what-is-tas).

You can also use dynamic slicing by directly interacting with [Slice custom resources](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice). For more information, see [Use dynamic slicing with a custom scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-dynamic-slices).

Before following these instructions, ensure that you understand the [concepts of dynamic slicing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing).

## Requirements

To use dynamic slicing in GKE, you must meet the following requirements:

  * Use a Standard cluster in the Rapid channel in one of the following versions: 
    * For dynamic super-slicing configuration (topologies equal to or larger than `4x4x4`), use version 1.35.2-gke.1842000 or later.
    * For dynamic sub-slicing configuration (topologies smaller than `4x4x4`), use version 1.36.0-gke.3712000 or later.
  * Use Ironwood (TPU7x) version.
  * Use the Container-Optimized OS image for your nodes.
  * To use incremental provisioning, use [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview#all_capacity_mode) reservations. All Capacity mode is a feature enabled by TPU Cluster Director.
  * For dynamic sub-slicing, ensure that your nodes have a pending maintenance events. [Monitor your instances for pending maintenance events](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#monitor-notification). If any of your nodes have a pending maintenance event with an end time between September 18, 2026 and September 30, 2026, you must manually [trigger the host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) on those nodes before you can use sub-slicing.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster in version 1.35.2-gke.1842000 or later, in the Rapid channel. To create a new cluster, see [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
  * Ensure you have sufficient quota for Ironwood (TPU7x) in your region.
  * If you plan to run multislice workloads, [install JobSet](https://jobset.sigs.k8s.io/docs/installation/) v0.10.1 or later
  * [Request TPU capacity in All Capacity mode](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation#confirm_your_capacity_reservation_draft).



## Use dynamic slicing in GKE with Kueue

This section describes the workflow for using dynamic slicing in GKE.

  1. [View the topology and health status of All Capacity mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus).
  2. Enable the slice controller in your cluster.
  3. Install Kueue, JobSet, and LWS.
  4. Create TPU node pools.
  5. Configure Kueue to create a Slice custom resource.
  6. Run workloads on dynamic slicing with Kueue.
  7. Clean up.



## Enable the slice controller

To use dynamic slicing, enable the slice controller in your cluster.

  1. Update your cluster:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             **--enable-slice-controller**
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the region with your [available TPU capacity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  2. Get credentials so that you can communicate with your cluster with `kubectl` commands:
         
         gcloud config set container/cluster CLUSTER_NAME
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=LOCATION
         

  3. In the output of the following command, verify that the `slices.accelerator.gke.io` value is present:
         
         kubectl get crd slices.accelerator.gke.io
         

The output is similar to the following:
         
         slices.accelerator.gke.io                2026-01-09T23:58:02Z
         




## Install Kueue, JobSet, and LWS

If you have already installed Kueue, JobSet, and LWS, you can skip this section.

### Install Kueue

Follow instructions from the [Kueue documentation](https://kueue.sigs.k8s.io/docs/installation/) or run the following command:
    
    
    kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/KUEUE_VERSION/manifests.yaml
    

Replace `KUEUE_VERSION` with the required Kueue version based on your topology requirements. For dynamic sub-slicing, use Kueue v0.18.2 or later. For dynamic super-slicing, use Kueue v0.16.6 or later.

### Install JobSet

Follow instructions from the [JobSet documentation](https://jobset.sigs.k8s.io/docs/installation/) or run the following command:
    
    
    kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/JOBSET_VERSION/manifests.yaml
    

Replace `JOBSET_VERSION` with the required JobSet version based on your topology requirements. For dynamic sub-slicing, use JobSet v0.12.0 or later. For dynamic super-slicing, use JobSet v0.11.1 or later.

### Install LWS

LeaderWorkerSet (LWS) is required only for dynamic sub-slicing.

Follow instructions from the [LWS documentation](https://lws.sigs.k8s.io/docs/installation/) or run the following command:
    
    
    kubectl apply --server-side -f https://github.com/kubernetes-sigs/lws/releases/download/LWS_VERSION/manifests.yaml
    

Replace `LWS_VERSION` with the required LWS version. Use LWS v0.8.0 or later.

## Create node pools with incremental provisioning

This section describes how to create the TPU node pools with incremental provisioning. GKE converts all your TPU capacity into node pools comprising 16-node groups of Ironwood (TPU7x) VMs, or sub-blocks. GKE provisions these node pools even when it can't find all of the healthy VMs by placing nodes on healthy parts of the host machine and incrementally provisioning unhealthy machines while they are repaired.

You can target your node pool to belong to any of the following:

  * A specific block of TPUs, which is exposed in All Capacity mode reservations. Block targeting allows GKE to create the node pool in any available sub-block within the specified block.
  * A specific sub-block, or a specific 16-node group of Ironwood (TPU7x) VMs, of TPUs for more granular control.



### Create a workload policy

To create a TPU slice node pool with Ironwood (TPU7x), you must first create a workload policy with the `accelerator-topology-mode` field set to `provision_only`. This setting triggers the incremental provisioning process.

Create a workload policy:
    
    
    gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --project=PROJECT_ID \
            --region=REGION  \
            --type=HIGH_THROUGHPUT \
            --accelerator-topology=4x4x4 \
            --accelerator-topology-mode=provision_only
    

Replace the following:

  * `WORKLOAD_POLICY_NAME`: a name for your workload policy.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the region for the workload policy.



In this command, do the following::

  * Always set the `accelerator-topology` field to `4x4x4` to match the total number of chips within a single sub-block.
  * Always set the `accelerator-topology-mode` field to `provision_only` to ensure the incremental provisioning process is triggered. When the `provision_only` field is set, the node pool provisions TPU nodes without forming ICI or OCS links.

**Note:** You don't need to create a new workload policy for every node pool. A workload policy is unique per project, per region, and per topology. You can reuse the same workload policy for multiple node pools that share these characteristics. To see the list of workload policies, use the `gcloud compute resource-policies list --filter="region:REGION"` command.

### Target your node pool to belong to a block or a sub-block

You can target specific sub-blocks or blocks within your All Capacity mode reservation.

  * **Target a block:** each node pool uses capacity from a specified block. GKE places the node pool within an available sub-block in that block. You must create as many node pools as there are sub-blocks in the block you want to use.
  * **Target a sub-block:** each node pool maps to a specific and available sub-block. When using sub-block targeting, GKE creates the node pool if at least one VM is healthy. Incremental provisioning helps ensure that all nodes are placed within the specified sub-block.




### Block

  1. To retrieve the name of the block in a reservation and the count of available sub-blocks in the block, complete the following steps in the [View the topology and health status of All Capacity Mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus) document:

     1. Identify the name of the block by [listing all reservation blocks](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#list_all_reservation_blocks) and copying the value in the `name:` field. This value is the name of the block or `BLOCK_NAME` in this document.

     2. Determine how many node pools to create by [describing a reservation block](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#describe_a_reservation_block) and identifying the value in the `reservationSubBlockCount` field. This value is the number of sub-blocks available. For example, the `reservationSubBlockCount: 4` value indicates that the block has four sub-blocks available, and you need to create four separate node pools.

  2. Set the reservation path:
         
         export RESERVATION_PATH="projects/PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME"
         

Replace the following:

     * `RESERVATION_NAME`: the name of your TPU reservation.
     * `BLOCK_NAME`: the name of the block.
  3. Create a node pool for each sub-block identified in the preceding step. For example, if the count is `4`, run this command four times. Use a unique name for each node pool.
         
         gcloud container node-pools create NODE_POOL_NAME \
               --cluster=CLUSTER_NAME \
               --node-locations=ZONE \
               --machine-type=tpu7x-standard-4t \
               --num-nodes=16 \
               --placement-policy=WORKLOAD_POLICY_NAME \
               --reservation-affinity=specific \
               --reservation=${RESERVATION_PATH}
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your new node pool.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `WORKLOAD_POLICY_NAME`: the name of the workload policy you created.
     * `ZONE`: the zone for the node pool, for example, `us-central1-a`.



### Sub-block

  1. To retrieve the name of the block and the IDs of the available sub-blocks, complete the following steps in the [View the topology and health status of All Capacity Mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus) document:

     1. To identify the name of the block, [list all reservation blocks](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#list_all_reservation_blocks) and copy the value in the `name:` field. This value is the name of the block or `BLOCK_NAME` on this document.

     2. To identify the name of the sub-blocks, [list all sub-blocks of a block](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#list_all_sub-blocks_of_a_block) and copy the value in the `name:` field for each entry under `reservationSubBlocks`. This value is the name of the sub-block or `SUBBLOCK_NAME` in this document.

  2. Set the reservation path:
         
         export RESERVATION_PATH="projects/PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUBBLOCK_NAME"
         

Replace the following:

     * `RESERVATION_NAME`: the name of your TPU reservation.
     * `BLOCK_NAME`: the name of the block.
     * `SUBBLOCK_NAME`: the name of the sub-block.
  3. Create the node pool:
         
         gcloud container node-pools create NODE_POOL_NAME \
                 --project=PROJECT_ID \
                 --cluster=CLUSTER_NAME \
                 --node-locations=ZONE \
                 --machine-type=tpu7x-standard-4t \
                 --num-nodes=16 \
                 --placement-policy=WORKLOAD_POLICY_NAME \
                 --reservation-affinity=specific \
                 --reservation=${RESERVATION_PATH}
         

Replace the following:

     * `NODE_POOL_NAME`: a unique name for your new node pool, for example, `sub-block-pool-1`.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `ZONE`: the zone for the node pool, for example, `us-central2-b`.
     * `WORKLOAD_POLICY_NAME`: the name of the workload policy you created.



At this stage, the nodes are created, but their Inter-Chip Interconnect (ICI) links are not yet active. Therefore, you can't run workloads on these node pools directly.

To enable all the necessary ICI links to form the slice and allow workloads to be scheduled, create a dynamic slice by using one of the following methods:

  * Create a [Slice custom resource](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice). Instead of Pods, you use a Slice custom resource to define the specified topology, which the slice controller activates.
  * Schedule GKE workloads with [Kueue](https://kueue.sigs.k8s.io/docs/overview/) and [TAS](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/). Kueue automatically handles the creation and deletion of Slice custom resources. Avoid manually modifying Slice custom resources created by Kueue.



## Create a dynamic slice with Kueue and TAS

In this section, you schedule GKE workloads with Kueue and TAS.

### Install Kueue slice controller

  1. To install the Kueue slice controller, save the following manifest as `slice-controller.yaml`:
         
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: v1
         kind: Namespace
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-system
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-controller-manager
           namespace: slice-controller-system
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-leader-election-role
           namespace: slice-controller-system
         rules:
         - apiGroups:
           - ""
           resources:
           - configmaps
           verbs:
           - get
           - list
           - watch
           - create
           - update
           - patch
           - delete
         - apiGroups:
           - coordination.k8s.io
           resources:
           - leases
           verbs:
           - get
           - list
           - watch
           - create
           - update
           - patch
           - delete
         - apiGroups:
           - ""
           resources:
           - events
           verbs:
           - create
           - patch
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-webhook-secrets-role
           namespace: slice-controller-system
         rules:
         - apiGroups:
           - ""
           resources:
           - secrets
           verbs:
           - get
           - list
           - watch
           - update
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           labels:
             control-plane: controller-manager
           name: slice-controller-manager-role
         rules:
         - apiGroups:
           - ""
           resources:
           - nodes
           - pods
           verbs:
           - get
           - list
           - watch
         - apiGroups:
           - accelerator.gke.io
           resources:
           - slices
           verbs:
           - create
           - delete
           - get
           - list
           - patch
           - update
           - watch
         - apiGroups:
           - accelerator.gke.io
           resources:
           - slices/finalizers
           verbs:
           - update
         - apiGroups:
           - accelerator.gke.io
           resources:
           - slices/status
           verbs:
           - get
           - patch
           - update
         - apiGroups:
           - admissionregistration.k8s.io
           resources:
           - mutatingwebhookconfigurations
           verbs:
           - get
           - list
           - update
           - watch
         - apiGroups:
           - batch
           resources:
           - jobs
           verbs:
           - get
           - list
           - patch
           - update
           - watch
         - apiGroups:
           - events.k8s.io
           resources:
           - events
           verbs:
           - create
           - patch
           - update
           - watch
         - apiGroups:
           - jobset.x-k8s.io
           resources:
           - jobsets
           verbs:
           - get
           - list
           - patch
           - update
           - watch
         - apiGroups:
           - kueue.x-k8s.io
           resources:
           - admissionchecks
           verbs:
           - get
           - list
           - watch
         - apiGroups:
           - kueue.x-k8s.io
           resources:
           - admissionchecks/status
           - workloads/status
           verbs:
           - get
           - patch
           - update
         - apiGroups:
           - kueue.x-k8s.io
           resources:
           - workloads
           verbs:
           - create
           - get
           - list
           - patch
           - update
           - watch
         - apiGroups:
           - leaderworkerset.x-k8s.io
           resources:
           - leaderworkersets
           verbs:
           - get
           - list
           - patch
           - update
           - watch
         - apiGroups:
           - ray.io
           resources:
           - rayclusters
           - rayjobs
           verbs:
           - get
           - list
           - patch
           - update
           - watch
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           labels:
             control-plane: controller-manager
           name: slice-controller-metrics-auth-role
         rules:
         - apiGroups:
           - authentication.k8s.io
           resources:
           - tokenreviews
           verbs:
           - create
         - apiGroups:
           - authorization.k8s.io
           resources:
           - subjectaccessreviews
           verbs:
           - create
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           labels:
             control-plane: controller-manager
           name: slice-controller-metrics-reader
         rules:
         - nonResourceURLs:
           - /metrics
           verbs:
           - get
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-leader-election-rolebinding
           namespace: slice-controller-system
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: Role
           name: slice-controller-leader-election-role
         subjects:
         - kind: ServiceAccount
           name: slice-controller-controller-manager
           namespace: slice-controller-system
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-webhook-secrets-rolebinding
           namespace: slice-controller-system
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: Role
           name: slice-controller-webhook-secrets-role
         subjects:
         - kind: ServiceAccount
           name: slice-controller-controller-manager
           namespace: slice-controller-system
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-manager-rolebinding
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: slice-controller-manager-role
         subjects:
         - kind: ServiceAccount
           name: slice-controller-controller-manager
           namespace: slice-controller-system
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           labels:
             control-plane: controller-manager
           name: slice-controller-metrics-auth-rolebinding
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: slice-controller-metrics-auth-role
         subjects:
         - kind: ServiceAccount
           name: slice-controller-controller-manager
           namespace: slice-controller-system
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           labels:
             control-plane: controller-manager
           name: slice-controller-webhook-server-cert
           namespace: slice-controller-system
         ---
         apiVersion: v1
         kind: Service
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-controller-manager-metrics-service
           namespace: slice-controller-system
         spec:
           ports:
           - name: https
             port: 8443
             protocol: TCP
             targetPort: 8443
           selector:
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
         ---
         apiVersion: v1
         kind: Service
         metadata:
           labels:
             control-plane: controller-manager
           name: slice-controller-webhook-service
           namespace: slice-controller-system
         spec:
           ports:
           - port: 443
             protocol: TCP
             targetPort: 9443
           selector:
             control-plane: controller-manager
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             app.kubernetes.io/managed-by: kustomize
             app.kubernetes.io/name: slice-controller
             control-plane: controller-manager
           name: slice-controller-controller-manager
           namespace: slice-controller-system
         spec:
           replicas: 1
           selector:
             matchLabels:
               app.kubernetes.io/name: slice-controller
               control-plane: controller-manager
           template:
             metadata:
               annotations:
                 kubectl.kubernetes.io/default-container: manager
               labels:
                 app.kubernetes.io/name: slice-controller
                 control-plane: controller-manager
             spec:
               containers:
               - args:
                 - --metrics-bind-address=:8443
                 - --leader-elect
                 - --health-probe-bind-address=:8081
                 - --zap-log-level=3
                 - --feature-gates=UseRetryMechanismForSliceCreation=true
                 - --activation-timeout=60m
                 - --kube-api-qps=100
                 - --kube-api-burst=200
                 - --default-slice-health-node-affinity=HEALTHY_AND_DEGRADED
                 - --reuse-slices=true
                 - --add-preferred-node-affinity=true
                 command:
                 - /manager
                 image: tpuongke/kueue-slice-controller:v0.10
                 livenessProbe:
                   httpGet:
                     path: /healthz
                     port: 8081
                   initialDelaySeconds: 15
                   periodSeconds: 20
                 name: manager
                 ports:
                 - containerPort: 9443
                   name: webhook-server
                   protocol: TCP
                 readinessProbe:
                   httpGet:
                     path: /readyz
                     port: 8081
                   initialDelaySeconds: 5
                   periodSeconds: 10
                 resources:
                   limits:
                     cpu: 12
                     memory: 32Gi
                   requests:
                     cpu: 8
                     memory: 16Gi
                 securityContext:
                   allowPrivilegeEscalation: false
                   capabilities:
                     drop:
                     - ALL
                 volumeMounts:
                 - mountPath: /tmp/k8s-webhook-server/serving-certs
                   name: cert
                   readOnly: true
               securityContext:
                 runAsNonRoot: true
                 seccompProfile:
                   type: RuntimeDefault
               serviceAccountName: slice-controller-controller-manager
               terminationGracePeriodSeconds: 10
               volumes:
               - name: cert
                 secret:
                   defaultMode: 420
                   secretName: slice-controller-webhook-server-cert
         ---
         apiVersion: admissionregistration.k8s.io/v1
         kind: MutatingWebhookConfiguration
         metadata:
           labels:
             control-plane: controller-manager
           name: slice-controller-mutating-webhook-configuration
         webhooks:
         - admissionReviewVersions:
           - v1
           clientConfig:
             service:
               name: slice-controller-webhook-service
               namespace: slice-controller-system
               path: /mutate-batch-v1-job
           failurePolicy: Fail
           name: mjob.kb.io
           rules:
           - apiGroups:
             - batch
             apiVersions:
             - v1
             operations:
             - CREATE
             resources:
             - jobs
           sideEffects: None
         - admissionReviewVersions:
           - v1
           clientConfig:
             service:
               name: slice-controller-webhook-service
               namespace: slice-controller-system
               path: /mutate-jobset-x-k8s-io-v1alpha2-jobset
           failurePolicy: Fail
           name: mjobset.kb.io
           rules:
           - apiGroups:
             - jobset.x-k8s.io
             apiVersions:
             - v1alpha2
             operations:
             - CREATE
             resources:
             - jobsets
           sideEffects: None
         - admissionReviewVersions:
           - v1
           clientConfig:
             service:
               name: slice-controller-webhook-service
               namespace: slice-controller-system
               path: /mutate-leaderworkerset-x-k8s-io-v1-leaderworkerset
           failurePolicy: Fail
           name: mleaderworkerset.kb.io
           rules:
           - apiGroups:
             - leaderworkerset.x-k8s.io
             apiVersions:
             - v1
             operations:
             - CREATE
             resources:
             - leaderworkersets
           sideEffects: None
         - admissionReviewVersions:
           - v1
           clientConfig:
             service:
               name: slice-controller-webhook-service
               namespace: slice-controller-system
               path: /mutate-ray-io-v1-raycluster
           failurePolicy: Fail
           name: mraycluster.kb.io
           rules:
           - apiGroups:
             - ray.io
             apiVersions:
             - v1
             operations:
             - CREATE
             resources:
             - rayclusters
           sideEffects: None
         - admissionReviewVersions:
           - v1
           clientConfig:
             service:
               name: slice-controller-webhook-service
               namespace: slice-controller-system
               path: /mutate-ray-io-v1-rayjob
           failurePolicy: Fail
           name: mrayjob.kb.io
           rules:
           - apiGroups:
             - ray.io
             apiVersions:
             - v1
             operations:
             - CREATE
             resources:
             - rayjobs
           sideEffects: None
         

  2. Apply the `slice-controller.yaml` manifest:
         
         kubectl apply -f slice-controller.yaml
         

  3. To configure Kueue for dynamic slicing, save the following manifest as `dynamic-slice-topology.yaml`:
         
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: Topology
         metadata:
           name: superslice-topology
         spec:
           levels:
           # Label to identify the physical block a sub-block belongs to.
           # Only sub-blocks from the same block can form a slice.
           - nodeLabel: cloud.google.com/gce-topology-block
           # Label to identify individual TPU sub-blocks (4x4x4 topology).
           - nodeLabel: cloud.google.com/gke-tpu-partition-4x4x4-id
           # Standard Kubernetes label for individual nodes.
           # Required to assign Pods to specific VMs.
           - nodeLabel: kubernetes.io/hostname
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ResourceFlavor
         metadata:
           name: superslice-rf
         spec:
           nodeLabels:
             cloud.google.com/gke-tpu-accelerator: tpu7x
           topologyName: superslice-topology
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: AdmissionCheck
         metadata:
           name: superslice-ac
         spec:
           controllerName: accelerator.gke.io/slice
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ClusterQueue
         metadata:
           name: cq
         spec:
           namespaceSelector: {}
           admissionChecks:
           - superslice-ac
           resourceGroups:
           - coveredResources:
             - google.com/tpu
             flavors:
             - name: superslice-rf
               resources:
               - name: google.com/tpu
                 nominalQuota: "999999"  # modeling unlimited quota
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: LocalQueue
         metadata:
           name: lq
           namespace: default
         spec:
           clusterQueue: cq
         

  4. Apply the `dynamic-slice-topology.yaml` manifest:
         
         kubectl apply -f dynamic-slice-topology.yaml
         

In this manifest, you configure Kueue for dynamic slicing by defining the following resources:

     * **Ironwood (TPU7x) dynamic slice topology (`superslice-topology`)**: the topology defines the levels Kueue considers when it schedules dynamic slicing workloads. These levels are the following: 
       * `cloud.google.com/gce-topology-block` label: this level is required to understand which sub-blocks belong to which blocks, because only sub-blocks from the same block can form a slice.
       * `cloud.google.com/gke-tpu-partition-4x4x4-id` label: this level represents individual Ironwood (TPU7x) sub-blocks (`4x4x4` topology).
       * `kubernetes.io/hostname` label: this level is required to assign Pods to specific VMs and to observe their labels and taints.
     * **Ironwood (TPU7x) SuperSlice ResourceFlavor (`superslice-rf`)**: the resource flavor for Ironwood (TPU7x) sub-blocks includes the `cloud.google.com/gke-tpu-accelerator: tpu7x` label to match nodes with Ironwood (TPU7x) machines.
     * **SuperSlice AdmissionCheck (`superslice-ac`)**: this admission check tells Kueue not to schedule a workload until the GKE slice controller confirms that the slice has become active. The admission check is first defined and then added to the `ClusterQueue` that handles dynamic slicing workloads.
     * **ClusterQueue (`cq`) and LocalQueue (`lq`)**: these fields manage `google.com/tpu` resources. The `cq` ClusterQueue includes the `superslice-ac` admission check. The `nominalQuota` field for `google.com/tpu` can be configured in two ways: 
       * **Specific quota** : set the `nominalQuota` field to match existing capacity for fair-sharing and quota management.
       * **Unlimited quota** : set the `nominalQuota` field to a very high value such as `"999999"`, to model unlimited quota. To focus on TAS and dynamic slicing, this configuration bypasses Kueue's quota management functionality.



### Define the partition health selection

Beyond standard node health and readiness, GKE exposes the specific state of each partition shape by using the `cloud.google.com/gke-tpu-partition-[shape]-state` label (where `[shape]` matches the partition ID shape, such as `2x2x1`, `2x2x2`, `2x2x4`, `2x4x4`, or `4x4x4`). This label lets GKE account for factors that influence slice formation, such as the state of TPU links. Dynamic sub-slicing configuration (topologies smaller than `4x4x4`) requires GKE version 1.36.0-gke.3712000 or later.

You can define the value of the partition state label as follows:

  * `HEALTHY`: the partition is healthy and fully functional.
  * `DEGRADED`: the partition's infrastructure is in a degraded state, for example, because of OCS link degradation. The partition can still form a slice, but overall performance might be lower compared to healthy partitions. This state applies only to the top-level `4x4x4` topology. Smaller topologies don't have a degraded state.
  * `UNHEALTHY`: the partition is unhealthy and can't form a slice.
  * `UNSET`: state is undefined due to unsuccessful GKE slice controller initialization.
  * `INCOMPLETE`: not all nodes within the partition are provisioned.



The Kueue Slice Controller webhook validates if a workload includes a specific partition health requirement. If no preference is indicated, the webhook injects a default node affinity.

The behavior is as follows:

  * If a `nodeSelector` or `nodeAffinity` that targets the `cloud.google.com/gke-tpu-partition-[shape]-state` label is present, it remains unchanged.
  * If no such label configuration exists, the webhook injects the following default node affinity to ensure only available partitions are used:
        
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: cloud.google.com/gke-tpu-partition-4x4x4-state
                operator: In
                values:
                - "HEALTHY"
                - "DEGRADED"
        




The following section includes examples where the `cloud.google.com/gke-tpu-partition-4x4x4-state` label is configured to specify the different sub-block health configurations.

## Run test workloads on dynamic slicing with Kueue

This section describes how to deploy workloads on dynamic slicing with Kueue and TAS. It includes examples that show how to create a dynamic slice workload and a workload consisting of multiple slices. The workloads are submitted as JobSets.

### Example 1: Single workload uses a single dynamic slice

The following example describes how to create a workload using a slice with a `4x12x16` topology, which is composed of 12 sub-blocks. The number of Pods was calculated as: (4 * 12 * 16) / 4 chips per node = 192 Pods.

  1. Save the following manifest as `big-super-slice.yaml`:
         
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: big-super-slice
           labels:
             kueue.x-k8s.io/queue-name: lq
         spec:
           replicatedJobs:
             - name: job-jax
               replicas: 1
               template:
                 spec:
                   parallelism: 192  # pods per slice calculation: 4*12*16 / 4 = 192
                   completions: 192
                   backoffLimit: 10
                   template:
                     metadata:
                       annotations:
                         cloud.google.com/gke-tpu-slice-topology: 4x12x16
                     spec:
                       tolerations:
                         - key: "google.com/tpu"
                           operator: "Equal"
                           value: "present"
                           effect: "NoSchedule"
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu7x
                       containers:
                         - name: jax
                           image: python:latest
                           command:
                             - bash
                             - -c
                             - |
                               printenv
                               pip install "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                               python -c 'import jax; print("Global device count:", jax.device_count(), "Local device count:", jax.local_device_count())'
                           resources:
                             limits:
                               google.com/tpu: 4
                       restartPolicy: Never
         

In this manifest, the following annotations tell Kueue the slice characteristics and topology to configure the following:

     * `cloud.google.com/gke-tpu-slice-topology`: specifies `"4x12x16"` as the dynamic slice topology. Requirements for the `tpu7x` accelerator topology include the following rules: 
       * **For dynamic sub-slicing:** you can specify topologies smaller than `4x4x4`, such as `2x2x1`, `2x2x2`, `2x2x4`, or `2x4x4`. These smaller topologies require GKE version 1.36.0-gke.3712000 or later.
       * **For dynamic super-slicing:** you can specify topologies that are equal to or greater than `4x4x4`. For dynamic super-slicing configuration, each dimension of the requested topology must be a multiple of four, for example `4A x 4B x 4C`.
       * The topology must be a three-dimensional string in the format `AxBxC`, for example `4x8x8`.
       * The dimensions must be sorted in non-decreasing order: A <= B <= C. For example, `4x8x4` is invalid; it should be `4x4x8`.
       * The product of the dimensions (A _B_ C) must not exceed 9,216.
       * The largest supported slice topologies can include up to 32 sub-blocks. For example, `8x16x16` with 32 sub-blocks,`8x12x20` with 30 sub-blocks, or `12x12x12` with 27 sub-blocks are within the accepted limits.
     * `cloud.google.com/gke-tpu-accelerator: tpu7x`: schedules Pods on on VMs that run Ironwood (TPU7x).
     * `kueue.x-k8s.io/queue-name`: assigns the JobSet to a Kueue LocalQueue.
     * The webhook injects the default node affinity to ensure `HEALTHY` and `DEGRADED` nodes are used.
  2. Apply the `big-super-slice.yaml` manifest:
         
         kubectl apply -f big-super-slice.yaml
         

After you apply the manifest, Kueue creates a `JobSet` named `big-super-slice`. Kueue then attempts to form a single dynamic slice with a `4x12x16` topology. After the slice is active, Kueue admits the workload, and the 192 Pods are scheduled on the nodes to form the dynamic slice that runs your workloads.




### Example 2: Workload with more than one replica

The following example demonstrates how to create a workload that uses two dynamic slices, each composed of four sub-blocks targeting only `HEALTHY` nodes.

  1. Save the following manifest as `two-super-slices.yaml`:
         
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: two-super-slices
           labels:
             kueue.x-k8s.io/queue-name: lq
         spec:
           replicatedJobs:
             - name: job-jax
               replicas: 2
               template:
                 spec:
                   parallelism: 64  # Pods per slice calculation: (4*8*8) / 4 = 64
                   completions: 64
                   backoffLimit: 10
                   template:
                     metadata:
                       annotations:
                         cloud.google.com/gke-tpu-slice-topology: 4x8x8
                     spec:
                       tolerations:
                         - key: "google.com/tpu"
                           operator: "Equal"
                           value: "present"
                           effect: "NoSchedule"
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu7x
                         cloud.google.com/gke-tpu-partition-4x4x4-state: "HEALTHY"
                       containers:
                         - name: jax
                           image: python:latest
                           command:
                             - bash
                             - -c
                             - |
                               printenv
                               pip install "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                               python -c 'import jax; print("Global device count:", jax.device_count(), "Local device count:", jax.local_device_count())'
                           resources:
                             limits:
                               google.com/tpu: 4
                       restartPolicy: Never
         

  2. Apply the `two-super-slices.yaml` manifest:
         
         kubectl apply -f two-super-slices.yaml
         




In this manifest, you set the `replicas` field to `2` in the `replicatedJobs` section. After you apply the manifest, Kueue attempts to form two separate slices with a `4x8x8` topology. Kueue creates a dynamic slice for each replica defined in `jobset.spec.replicatedJobs[].replicas`. If `n` replicas are specified, Kueue creates `n` dynamic slices for the workload and waits for all slices to become active before admitting the workload.

## Optimize workload scheduling with slice reuse

By default, Kueue instructs the slice controller to provision a new TPU slice for each workload execution and delete it when the workload completes. This behavior can lead to churn and overhead on the underlying infrastructure.

With slice reuse, new workloads can reuse existing, idle TPU slices that have identical topology and hardware limits. When you enable slice reuse, Kueue marks the slice as idle at the end of a job instead of deleting it. A new job requesting the same partition instantly claims and reuses the slice, which bypasses the hardware provisioning delay.

**Note:** The events API group used by the controller has changed. If you have custom integrations, you must use `events.k8s.io/v1` instead of `core/v1`. Enhanced slice reuse efficiency requires Kueue v0.19.0 or later.

### Enable Slice reuse

To fully optimize slice reuse, you must configure both the Slice controller and Kueue to work together.

  1. **Configure the slice controller:** update the Kueue slice controller deployment arguments to include the `--reuse-slices=true` flag. To help ensure workloads are optimally scheduled on existing slices, also add the `--add-preferred-node-affinity=true` flag.

**Note:** Reusable slices are named dynamically with an `s-<topology>` prefix, decoupling them from specific workload names.
  2. **Configure Kueue (Recommended):** to allow Kueue to use the controller's preferred node affinity suggestions, you must enable the `TASRespectNodeAffinityPreferred` feature gate in your Kueue configuration.

For example, edit the `kueue-manager-config` ConfigMap to add the feature gate:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: kueue-manager-config
           namespace: kueue-system
         data:
           controller_manager_config.yaml: |
             apiVersion: config.kueue.x-k8s.io/v1beta1
             kind: Configuration
             featureGates:
               TASRespectNodeAffinityPreferred: true
             # ...
         

After changing the ConfigMap, restart the `kueue-controller-manager` deployment to enforce the change:
         
         kubectl rollout restart deploy kueue-controller-manager -n kueue-system
         

**Note:** Slice reuse works on older Kueue versions, but preferred node affinity enhancement is only compatible with Kueue v0.18 or later.



### Enforce slice deletion per workload

To make a specific workload clean up its slices and prevent slice reuse, complete the following steps:

  1. Apply the following label to your Job or JobSet definition:
         
         kueue.gke.io/tpu-enforce-slice-deletion: "true"
         

After you apply this label, the workload can still be scheduled on an existing idle slice. However, after the workload completes, the slice will be permanently deleted rather than returned to the reusable pool.

  2. Configure Kueue to pass this label down from the framework Job to the Kueue Workload object by adding the label to the `labelKeysToCopy` list in your Kueue configuration:
         
         labelKeysToCopy:
         - "kueue.gke.io/tpu-enforce-slice-deletion"
         




## Monitor the slice

You can see the status of the slice and monitor the slice metrics with [GKE system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

### Monitor the status of the slice

When a slice is created or actively used by a workload, the slice controller attaches labels to identify the workload using it. Because Slice names are generated dynamically (and are decoupled from the workload name when reuse is enabled), you should use these labels to find the slice assigned to your workload.

  1. To find the slices assigned to a workload, run the following command:
         
         kubectl get slice -l kueue.gke.io/tpu-slice-used-by-namespace=NAMESPACE,kueue.gke.io/tpu-slice-used-by-workload=WORKLOAD_NAME
         

Replace the following:

     * `NAMESPACE`: the namespace of your workload.
     * `WORKLOAD_NAME`: the name of the Kueue Workload, which is usually the same as the name of your Job or JobSet.
**Note:** If `WORKLOAD_NAME` is longer than 63 characters, it is automatically trimmed for the label.
  2. Copy the slice name from the output of the previous command.

  3. Use the slice name to check the detailed status of your dynamic slice:
         
         kubectl describe slice SLICE_NAME
         

Replace `SLICE_NAME` with the name of your slice.




The output is similar to the following:
    
    
    Name:         s-4x4x4-74d3fb0b
    Namespace:
    Labels:       <none>
    Annotations:  <none>
    API Version:  accelerator.gke.io/v1beta1
    Kind:         Slice
    Metadata:
      Creation Timestamp:  2026-02-12T23:44:28Z
      Finalizers:
        accelerator.gke.io/slice-finalizer
      Generation:        1
      Resource Version:  1770939905695871008
      UID:               6dbbfe14-4486-4462-864d-e078d0ca8b5b
    Spec:
      Partition Ids:
        5eae6a4f59d59cf30a9bf49de618eb2b
      Topology:  4x4x4
      Type:      tpu7x
    Status:
      Conditions:
        Last Transition Time:  2026-02-12T23:45:05Z
        Message:
        Reason:                ACTIVE
        Status:                True
        Type:                  Ready
        Last Transition Time:  2026-02-12T23:45:05Z
        Message:               NodeLabelingCompleted
        Reason:                NodeLabelIsAdded
        Status:                True
        Type:                  NodeLabeled
    Events:                    <none>
    

### Monitor the metrics of the slice

You can monitor the following GKE system metrics that expose the condition of a slice:

  * `kubernetes.io/accelerator/slice/state`
  * `kubernetes.io/accelerator/partition/state`
  * `kubernetes.io/accelerator/slice/deformation_durations`
  * `kubernetes.io/accelerator/slice/formation_durations`



For more information about the metrics, see [GKE system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes).

#### Kueue Slice controller metrics

You can also monitor the following Prometheus metrics exposed by the Kueue Slice Controller to observe slice lifecycle, reuse, and admission checks:

**Slice lifecycle metrics**

Slice lifecycle metrics track the creation and deletion of slices:

  * `tpu_ac_slice_create_time`: Histogram measuring how long slice creation took.
  * `tpu_ac_slices_created`: Counter tracking created slices (includes an `is_reusable` label).
  * `tpu_ac_slices_status`: Gauge tracking the current number of slices by status, including `is_reusable` and `in_use` labels.
  * `tpu_ac_slice_delete_time`: Histogram measuring how long slice deletion took.
  * `tpu_ac_slices_deleted`: Counter tracking deleted slices.
  * `tpu_ac_slices_gc`: Counter tracking automatically cleaned up slices.



**Slice reuse metrics**

Slice reuse metrics track the successful reuse and conflicts of TPU slices:

  * `tpu_ac_slices_reused`: Counter tracking successfully reused slices.
  * `tpu_ac_slices_conflict`: Counter tracking slices deleted due to topology or shape mismatches.



**Workload and admission metrics**

Workload and admission metrics track the duration and outcomes of admission checks:

  * `tpu_ac_admission_time`: Histogram measuring the admission check process duration. Note: This measures the duration of the slice controller's admission check and does not include the overall Kueue workload admission time.
  * `tpu_ac_workload_processed`: Counter of admission check decisions, containing a `target_state` label.



**General metrics**

General metrics track operational problems and errors:

  * `tpu_ac_problem`: A counter that tracks operational problems or errors. This metric includes a `problem` label that indicates the specific error type.

**Note:** Because of concurrent reconciliation, you might see occasional API server errors (labeled `API_SERVER_ERROR`). These errors can occur, for example, when the system modifies a stale resource. They don't necessarily indicate a system failure.



## Clean up

To avoid unexpected charges, delete your slices before deleting node pools.

  1. Delete the JobSet. This action triggers Kueue to delete the associated Slice custom resources.
         
         kubectl delete jobset JOBSET_NAME
         

Replace `JOBSET_NAME` with the name of your JobSet, for example, `big-super-slice`.

**Note:** Active Slice custom resources block node pool deletion to ensure resources are cleaned up properly. Deleting the JobSet ensures that Kueue cleans up the Slice custom resources before you proceed with node pool deletion.
  2. Delete the TPU node pool:
         
         gcloud container node-pools delete NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION
         




## (Optional) Use dynamic slicing with your own scheduler

This document focuses on using Kueue and TAS. However, you can also manage dynamic slicing with your own custom scheduler. If you choose to use a different scheduler, follow the [Slice custom resource](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice) reference information.

## What's next

  * Learn more about [TPU Cluster Director](https://docs.cloud.google.com/tpu/docs/all-capacity-overview).
  * Learn how to [Manage maintenance events with TPUs in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events).
  * Learn how to [deploy Cloud TPU workloads with dynamic slicing in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-tpu-dynamic-slicing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
