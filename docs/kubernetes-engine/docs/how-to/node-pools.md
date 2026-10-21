---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools/
title: Add and manage node pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:51.893545+00:00
---

# Add and manage node pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Add and manage node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to add, manage, scale, upgrade, and delete node pools that run in your Google Kubernetes Engine (GKE) Standard [clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture), in order to optimize your GKE Standard clusters for performance and scalability. The node pools in a Standard cluster include Standard node pools, and [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools). Aside from the section about how to Upgrade a node pool, the information in this document applies specifically to Standard node pools. You also learn how to deploy Pods to specific Standard node pools, and about the implications of node pool upgrades on running workloads.

This page is for Operators, Cloud architects, and Developers, who need to create and configure clusters, and deploy workloads on GKE. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing [Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).

**Note:** OS Login is supported in GKE clusters using VPC Network Peering, in clusters using Private Service Connect, and in clusters that run node pool versions 1.20.5 or later. OS Login is explicitly disabled on GKE nodes, even if it is enabled on the Google Cloud project.

## Set up IAM service accounts for GKE

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

**Best practice:** Instead of using the Compute Engine default service account, create a _custom service account_ for your nodes to use and give it only the permissions that GKE needs to run system tasks. For more information, see [Configure a custom node service account](https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts#configure-custom-account). 

To grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account, complete the following steps:

### Console

  1. Go to the **Welcome** page: 

[Go to Welcome](https://console.cloud.google.com/welcome)

  2. In the **Project number** field, click content_copy **Copy to clipboard**.
  3. Go to the **IAM** page: 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. Click person_add **Grant access**.
  5. In the **New principals** field, specify the following value: 
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with the project number that you copied. 
  6. In the **Select a role** menu, select the **Kubernetes Engine Default Node Service Account** role.
  7. Click **Save**.



### gcloud

  1. Find your Google Cloud project number: 
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"

Replace `PROJECT_ID` with your project ID.

The output is similar to the following:
         
         12345678901
         

  2. Grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/container.defaultNodeServiceAccount"

Replace `PROJECT_NUMBER` with the project number from the previous step.




## Add a node pool to a Standard cluster

You can add a new node pool to a GKE Standard cluster using the gcloud CLI, the Google Cloud console, or Terraform. GKE also supports [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable), which automatically manages the node pools in your cluster based on scaling requirements.

**Best practice** : 

Create and use a minimally-privileged Identity and Access Management (IAM) service account for your node pools to use instead of the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). For instructions to create a minimally-privileged service account, refer to [ Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

### gcloud

To create a node pool, run the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) command:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --service-account SERVICE_ACCOUNT
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of your existing cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `SERVICE_ACCOUNT`: the name of the IAM service account for your nodes to use. 

We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
        
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.




For a full list of optional flags you can specify, refer to the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) documentation.

The output is similar to the following:
    
    
    Creating node pool POOL_NAME...done.
    Created [https://container.googleapis.com/v1/projects/PROJECT_ID/zones/us-central1/clusters/CLUSTER_NAME/nodePools/POOL_NAME].
    NAME: POOL_NAME
    MACHINE_TYPE: e2-medium
    DISK_SIZE_GB: 100
    NODE_VERSION: 1.21.5-gke.1302
    

In this output, you see details about the node pool, such as the machine type and GKE version running on the nodes.

Occasionally, the node pool is created successfully but the `gcloud` command times out instead of reporting the status from the server. To check the status of all node pools, including those not yet fully provisioned, use the following command:
    
    
    gcloud container node-pools list --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

### Console

To add a node pool to an existing Standard cluster, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the Standard cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Configure your node pool.

  6. In the navigation menu, click **Security**. 

  7. Optionally, specify a custom IAM service account for your nodes: 
     1. In the **Advanced settings** page, expand the **Security** section.
     2. In the **Service account** menu, select your preferred service account.

We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

  8. Click **Create** to add the node pool.




### Terraform

Use one of the following examples:

  * Add a node pool that uses the Compute Engine default IAM service account:


    
    
    resource "google_container_node_pool" "default" {
      name    = "gke-standard-regional-node-pool"
      cluster = google_container_cluster.default.name
    
      node_config {
        service_account = google_service_account.default.email
      }
    }

  * Add a node pool that uses a custom IAM service account:


  1. Create an IAM service account and grant it the `roles/container.defaultNodeServiceAccount` role on the project:
         
         resource "google_service_account" "default" {
           account_id   = "service-account-id"
           display_name = "Service Account"
         }
         
         data "google_project" "project" {
         }
         
         resource "google_project_iam_member" "default" {
           project = data.google_project.project.project_id
           role    = "roles/container.defaultNodeServiceAccount"
           member  = "serviceAccount:${google_service_account.default.email}"
         }

  2. Create a node pool that uses the new service account:
         
         resource "google_container_node_pool" "default" {
           name    = "gke-standard-regional-node-pool"
           cluster = google_container_cluster.default.name
         
           node_config {
             service_account = google_service_account.default.email
           }
         }




To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## View node pools in a Standard cluster

### gcloud

To list all the node pools of a Standard cluster, run the [`gcloud container node-pools list`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list) command:
    
    
    gcloud container node-pools list --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

To view details about a specific node pool, run the [`gcloud container node-pools describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/describe) command:
    
    
    gcloud container node-pools describe POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `POOL_NAME`: the name of the node pool to view.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Console

To view node pools for a Standard cluster, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the Standard cluster.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to view.




## Scale a node pool

You can scale your node pools up or down to optimize for performance and cost. With GKE Standard node pools, you can scale a node pool horizontally by changing the number of nodes in the node pool, or scale a node pool vertically by changing the machine attribute configuration of the nodes.

### Horizontally scale by changing the node count

### gcloud

To resize a cluster's node pools, run the [`gcloud container clusters resize`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/resize) command:
    
    
    gcloud container clusters resize CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --node-pool POOL_NAME \
        --num-nodes NUM_NODES
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to resize.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `POOL_NAME`: the name of the node pool to resize.
  * `NUM_NODES`: the number of nodes in the pool in a zonal cluster. If you use multi-zonal or regional clusters, NUM_NODES is the number of nodes for each zone the node pool is in.



Repeat this command for each node pool. If your cluster has only one node pool, omit the `--node-pool` flag.

### Console

To resize a cluster's node pools, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the Standard cluster you want to modify.

  3. Click the **Nodes** tab.

  4. In the **Node Pools** section, click the name of the node pool that you want to resize.

  5. Click _edit_ **Resize**.

  6. In the **Number of nodes** field, enter how many nodes that you want in the node pool, and then click **Resize**.

  7. Repeat for each node pool as needed.




### Vertically scale by changing the node machine attributes

You can modify the node pool's configured machine type, disk type, and disk size.

When you edit one or more of these machine attributes, GKE updates the nodes to the new configuration using the [upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-surge-upgrades-are-used) configured for the node pool. If you configure the [blue-green upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) you can migrate the workloads from the original nodes to the new nodes while being able to roll back the original nodes if the migration fails. [Inspect the upgrade settings of the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#inspect-upgrade-settings) to ensure that the configured strategy is how you want your nodes to be updated.

Update at least one of the highlighted machine attributes in the following command:
    
    
    gcloud container node-pools update POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --machine-type MACHINE_TYPE \
        --disk-type DISK_TYPE \
        --disk-size DISK_SIZE
    

Omit any flags for machine attributes that you don't want to change. However, you must use at least one machine attribute flag, as the command otherwise fails.

Replace the following:

  * `POOL_NAME`: the name of the node pool to resize.
  * `CLUSTER_NAME`: the name of the cluster to resize.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `MACHINE_TYPE`: the type of machine to use for nodes. To learn more, see [gcloud container node-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--machine-type).
  * `DISK_TYPE`: the type of the node VM boot disk, can be either `pd-standard`, `pd-ssd`, `pd-balanced`, or `hyperdisk-balanced`, depending on the machine series. You can't use `hyperdisk-extreme` or `hyperdisk-throughput` as boot disks. For more information about the disks that machine series support, see the [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) table.
  * `DISK_SIZE`: the size for node VM boot disks in GB. Defaults to 100GB.



This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

## Upgrade a node pool

By default, Standard node pools have [auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#node_pool_upgrades) enabled, and all Autopilot-managed node pools in Standard clusters always have auto-upgrade enabled. Node auto-upgrades help ensure that your cluster's control plane and node version remain in sync and in compliance with the [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/), which helps ensure that control planes are compatible with nodes up to two minor versions earlier than the control plane. For example, Kubernetes 1.34 control planes are compatible with Kubernetes 1.32 nodes. By default, GKE automatically upgrades only one node pool at a time. To automatically upgrade multiple node pools simultaneously, you can [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades) ([Preview](https://cloud.google.com/products#product-launch-stages)).

**Best practice** : 

Avoid disabling [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable) with Standard node pools so that your cluster benefits from the upgrades listed in the preceding paragraph.

With GKE Standard node pool upgrades, you can choose between three configurable upgrade strategies, including [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge), [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy), and [autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). Autopilot-managed node pools in Standard clusters always use surge upgrades.

For Standard node pools, [choose a strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) and [use the parameters to tune the strategy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies) to best fit your cluster environment's needs.

### How node upgrades work

While a node is being upgraded, GKE stops scheduling new Pods onto it, and attempts to schedule its running Pods onto other nodes. This is similar to other events that re-create the node, such as enabling or disabling a feature on the node pool.

During automatic or manual node upgrades, [PodDisruptionBudgets (PDBs)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and [Pod termination grace period](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) are respected for a maximum of 1 hour. If Pods running on the node can't be scheduled onto new nodes after one hour, GKE initiates the upgrade anyway. This behavior applies even if you configure your PDBs to always have all of your replicas available by setting the `maxUnavailable` field to `0` or `0%` or by setting the `minAvailable` field to `100%` or to the number of replicas. In all of these scenarios, GKE deletes the Pods after one hour so that the node deletion can happen.

**Best practice** : 

If a workload running in a Standard node pool requires more flexibility with graceful termination, use [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) which provide settings for additional soak time to extend PDB checks beyond the one hour default.

To learn more about what to expect during node termination in general, see the topic about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates).

The upgrade is only complete when all nodes have been recreated and the cluster is in the new state. When a newly-upgraded node registers with the control plane, GKE marks the node as schedulable.

New node instances run the new Kubernetes version as well as the following:

  * The [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images)
  * [`kubelet`](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
  * [`kube-proxy`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)



For a node pool upgrade to be considered complete, all nodes in the node pool must be recreated. If an upgrade started but then didn't complete and is in a partially upgraded state, the node pool version might not reflect the version of all of the nodes. To learn more, see [Some node versions don't match the node pool version after an incomplete node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#inconsistent-node-versions). To determine that the node pool upgrade finished, [check the node pool upgrade status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#check-status). If the upgrade operation is beyond the retention period, then check that each individual node version matches the node pool version.

### Save your data to persistent disks before upgrading

Before upgrading a node pool, you must ensure that any data you need to keep is stored in a Pod by using [persistent volumes], which use [persistent disks]. Persistent disks are unmounted, rather than erased, during upgrades, and their data is transferred between Pods.

The following restrictions pertain to persistent disks:

  * The nodes on which Pods are running must be Compute Engine VMs.
  * Those VMs need to be in the same Compute Engine project and zone as the persistent disk.



To learn how to add a persistent disk to an existing node instance, see [Adding or resizing zonal persistent disks](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk) in the Compute Engine documentation.

### Manually upgrade a node pool

**Important:** Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

You can manually upgrade the version of a Standard node pool or Autopilot-managed node pool **in a Standard cluster**. You can match the version of the control plane or, use a previous version that is still available and is compatible with the control plane. You can manually upgrade multiple node pools in parallel, similarly to how GKE can upgrade multiple node pools in parallel if you [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades).

When GKE upgrades a node pool, either manually or automatically, GKE removes any [labels you added to individual nodes using `kubectl`](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node). Any other [types of changes to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#types-of-changes) which recreate the nodes also remove the labels. To avoid losing labels, [apply labels to node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools#updating_node_labels) instead.

Before you manually upgrade your node pool, consider the following conditions:

  * Upgrading a node pool may disrupt workloads running in that node pool. To avoid this, you can create a new node pool with the required version and migrate the workload. After migration, you can delete the old node pool.
  * If you upgrade a node pool with an Ingress in an errored state, the instance group does not sync. To work around this issue, first check the status using the `kubectl get ing` command. If the instance group is not synced, you can work around the problem by re-applying the manifest used to create the ingress.



You can manually upgrade your node pools to a version compatible with the control plane:

  * For Standard node pools, you can use the Google Cloud console or the Google Cloud CLI.
  * For [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools), you can only use the Google Cloud CLI.




### Console

To upgrade a Standard node pool using the Google Cloud console, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster.

  3. On the **Cluster details** page, click the **Nodes** tab.

  4. In the **Node Pools** section, click the name of the node pool that you want to upgrade.

  5. Click _edit_ **Edit**.

  6. Click **Change** under **Node version**.

  7. Select the required version from the **Node version** drop-down list, then click **Change**.




It may take several minutes for the node version to change.

### gcloud

The following variables are used in the commands in this section:

  * `CLUSTER_NAME`: the name of the cluster of the node pool to be upgraded.
  * `NODE_POOL_NAME`: the name of the node pool to be upgraded.
  * `CONTROL_PLANE_LOCATION`: the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.
  * `VERSION`: the Kubernetes version to which the nodes are upgraded. For example, `--cluster-version=1.34.1-gke.1293000` or `cluster-version=latest`.



Upgrade a node pool:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
      --node-pool=NODE_POOL_NAME \
      --location=CONTROL_PLANE_LOCATION
    

To specify a different version of GKE on nodes, use the optional `--cluster-version` flag:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
      --node-pool=NODE_POOL_NAME \
      --location=CONTROL_PLANE_LOCATION \
      --cluster-version VERSION
    

For more information about specifying versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/versioning).

For more information, refer to the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) documentation.

## Deploy a Pod to a specific node pool

You can explicitly deploy a Pod to a specific node pool by using a `nodeSelector` in your Pod manifest. `nodeSelector` schedules Pods onto nodes with a matching label.

All GKE node pools have labels with the following format: `cloud.google.com/gke-nodepool: POOL_NAME`. Add this label to the `nodeSelector` field in your Pod as shown in the following example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
        env: test
    spec:
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
      **nodeSelector :
        cloud.google.com/gke-nodepool: POOL_NAME**
    

For more information, see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/).

As an alternative to node selector, you can use node affinity. Use node affinity if you want a "soft" rule where the Pod attempts to meet the constraint, but is still scheduled even if the constraint can't be satisfied. For more information, see [Node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity). You can also [specify resource requests for the containers](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/).

## Downgrade a node pool

You can downgrade a node pool if GKE completed the node pool upgrade. GKE can't downgrade—and can only roll back—a partially upgraded node pool. If you attempt to trigger a downgrade of a partially upgraded node pool, GKE doesn't update any of the nodes in the node pool with that operation. To check if node pool isn't completely upgraded and can only be rolled back, first [check the node pool upgrade status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#check-status). If the upgrade was cancelled or failed, you can check that the node pool upgrade never completed by checking the nodes in the node pool to see if there are still nodes running the previous version.

If a node pool upgrade didn't complete and you want to roll back upgraded nodes to their previous version, follow the instructions to [roll back a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#rollback). If a node pool upgrade is complete and you want to reverse it because it caused issues for your workloads, you can downgrade the node pool to an earlier version by following the instructions in this section. Review the [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading-limitations) before downgrading a node pool.

**Best practice** : 

Use the [blue-green node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) if you need to optimize for risk mitigation for node pool upgrades impacting your workloads. With this strategy, you can [roll back](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#rollback-a-blue-green-upgrade) an in-progress upgrade to the original nodes if the upgrade is unsuccessful.

  1. Set a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) for the cluster to prevent the node pool from being automatically upgraded by GKE after being downgraded.
  2. To downgrade to an earlier version, follow the steps to [manually upgrade a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) and specify an earlier version.



## Delete a node pool

Deleting a node pool deletes the nodes and all running workloads. By default, GKE doesn't respect [`PodDisruptionBudget`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) settings when deleting node pools. To learn how to change this setting, see Update a node pool to respect PDBs during node pool deletion.

For more information about how deleting a node pool affects your workloads, including interactions with node selectors, see [Deleting node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#drain).

You can only delete Standard node pools. You can't delete the [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools) which run in Standard clusters, GKE automatically cleans these up when they're no longer needed.

Delete a node pool using the gcloud CLI or the Google Cloud console:

### gcloud

To delete a node pool, run the [`gcloud container node-pools delete`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete) command:
    
    
    gcloud container node-pools delete POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `POOL_NAME`: the name of the node pool to delete.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Console

To delete a node pool, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the Standard cluster you want to modify.

  3. Click the **Nodes** tab.

  4. In the **Node Pools** section, click _delete_ next to the node pool you want to delete.

  5. When prompted to confirm, click **Delete**.




### Update a node pool to respect PDBs during node pool deletion

By default, GKE doesn't respect [`PodDisruptionBudget`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) settings when deleting node pools. However, you can update the configuration of the node pool to have GKE respect PDBs during node pool deletion, for up to one hour. Respecting PDBs gives workloads the opportunity to move to other nodes in the cluster. This setting doesn't affect node pool deletion during cluster deletion.

To update the setting for your node pool, run the following gcloud CLI command:
    
    
    gcloud container node-pools update POOL_NAME
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --respect-pdb-during-node-pool-deletion
    

Replace the following:

  * `POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



You can also use the `--respect-pdb-during-node-pool-deletion` flag when you add a node pool.

To remove this configuration and use the default setting of not respecting PDBs during node pool deletion, see the next section.

### Update a node pool to not respect PDBs during node pool deletion

You can update a node pool to revert to the default setting of not respecting PDBs during node pool deletion.

To update the setting, run the following gcloud CLI command:
    
    
    gcloud container node-pools update POOL_NAME
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --no-respect-pdb-during-node-pool-deletion
    

Replace the following:

  * `POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



## Migrate nodes to a different machine type

To learn about different approaches for moving workloads between machine types, for example, to migrate to a newer machine type, see [Migrate nodes to a different machine type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-nodes).

## Migrate workloads between node pools

To migrate workloads from one node pool to another node pool, see [Migrate workloads between node pools](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-pools#migrate-node-pools). For example, you can use these instructions if you're replacing an existing node pool with a new node pool and you want to ensure that the workloads move to the new nodes from the existing nodes.

## Troubleshoot

For troubleshooting information, see [Troubleshoot Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-node-pools) and [Troubleshoot node registration](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-node-registration).

## What's next

  * [Learn about auto-provisioning node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * [Learn how GKE can automatically repair unhealthy nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair).
  * [Learn how to configure `kubelet` and `sysctl` using Node System Configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
