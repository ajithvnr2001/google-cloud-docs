---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes/
title: Using Shielded GKE Nodes \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:54.960804+00:00
---

# Using Shielded GKE Nodes  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Using Shielded GKE Nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use the _Shielded GKE Nodes_ feature. Shielded GKE Nodes provide strong, verifiable node identity and integrity to increase the security of Google Kubernetes Engine (GKE) nodes.

For GKE Autopilot clusters, the Shielded GKE Nodes feature is enabled by default and cannot be overridden. For GKE Standard clusters, the Shielded GKE Nodes feature is enabled by default but can be overridden.

## About Shielded GKE Nodes

Shielded GKE Nodes are built on top of Compute Engine [Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm). Without Shielded GKE Nodes an attacker can exploit a vulnerability in a Pod to exfiltrate bootstrap credentials and impersonate nodes in your cluster, giving the attackers access to cluster secrets. When Shielded GKE Nodes is enabled, the GKE control plane cryptographically verifies that:

  * Every node in your cluster is a virtual machine running in Google's data center.
  * Every node is part of the [Managed Instance Group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) provisioned for the cluster.
  * The kubelet is being provisioned a certificate for the node on which it is running.



This limits the ability of an attacker to impersonate a node in your cluster even if they are able to exfiltrate bootstrap credentials of the node. The bootstrap credentials, which are contained in node metadata (`TPM_BOOTSTRAP_KEY`) only have the ability to create Certificate Signing Requests. Those certificates won't be automatically approved by the control plane and become working node certificates unless the conditions listed earlier are met and the CSR contains an attestation from the node's [vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm). You can optionally also prevent the `kubelet` on your nodes from creating `Node` objects in the cluster by enabling [control plane node creation](https://docs.cloud.google.com/kubernetes-engine/security/control-plane-node-creation) ([Preview](https://cloud.google.com/products#product-launch-stages)), which limits the impact even if a node is compromised after a CSR is approved.

GKE cluster control plane nodes always use Shielded GKE Nodes, even if you disable the feature on your cluster. Enabling or disabling Shielded GKE Nodes only affects whether the worker nodes that run your workloads use the feature.

## Pricing

There is no additional cost to run Shielded GKE Nodes. However, Shielded GKE Nodes generate about 0.5 KB more logs on startup than standard nodes. See the [Cloud Logging pricing page](https://cloud.google.com/stackdriver/pricing) for details.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enabling Shielded GKE Nodes in a new cluster

You can create a new cluster with Shielded GKE Nodes enabled by using the gcloud CLI or the Google Cloud console.

### gcloud

When creating a new cluster, specify the `--enable-shielded-nodes` option:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-shielded-nodes
    

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the navigation pane, click **Advanced settings**.

  3. In the **Shielded nodes** row, select the **Quick enable** checkbox.

  4. Configure your cluster as desired.

  5. Click **Create**.




See [Creating a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) for more details about creating clusters.

## Enabling Shielded GKE Nodes in an existing cluster

You can enable Shielded GKE Nodes in an existing cluster by using the Google Cloud CLI or the Google Cloud console.

### How GKE enables Shielded GKE Nodes

After you enable Shielded GKE Nodes, the worker nodes are recreated as Shielded VMs. The cluster nodes are recreated in a rolling fashion to minimize downtime.

After you enable Shielded GKE Nodes, GKE updates your cluster with the following steps:

  * GKE immediately recreates the control plane, ignoring [maintenance availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).
  * GKE recreates the worker nodes as Shielded VMs, respecting maintenance availability. GKE uses [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) to update each of the node pools. This depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions).



For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Warning:** If there is no maintenance availability, the control plane might be recreated but the nodes won't yet be recreated. The delay between the two steps might cause [failed node registrations](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-registration) and disruption to your cluster. To manually apply the changes to the nodes to recreate the nodes as Shielded GKE Nodes, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running. Manually draining and deleting individual nodes does not recreate the nodes as Shielded GKE Nodes.

### Enable Shielded GKE Nodes

### gcloud

When updating the cluster, specify the `--enable-shielded-nodes` option:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-shielded-nodes
    

### Console

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. Under **Security** , in the **Shielded GKE Nodes** field, click _edit_ **Edit Shielded GKE Nodes**.

  4. Select the **Enable Shielded GKE Nodes** checkbox.

  5. Click **Save Changes**.




## Verifying that Shielded GKE Nodes are enabled

You verify that your cluster is using Shielded GKE Nodes with the Google Cloud CLI or the Google Cloud console.

### gcloud

Describe the cluster:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

If Shielded GKE Nodes are enabled, the output of the command will include these lines:
    
    
    shieldedNodes:
      enabled: true
    

### Console

To verify that a cluster is using Shielded GKE Nodes:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to inspect.

  3. Under **Security** , in the **Shielded GKE Nodes** field, verify that Shielded GKE Nodes is **Enabled**.




You can also monitor the integrity of your nodes' underlying Shielded VMs. See [Monitoring Integrity on Shielded VM Instances](https://docs.cloud.google.com/compute/docs/instances/integrity-monitoring) for the procedure.

## Disabling Shielded GKE Nodes

You can disable Shielded GKE Nodes with the Google Cloud CLI or the Google Cloud console.

### How GKE disables Shielded GKE Nodes

After you disable Shielded GKE Nodes, GKE updates your cluster with the following steps:

  * GKE immediately recreates the control plane, ignoring [maintenance availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).
  * GKE recreates the worker nodes as unshielded VMs, respecting maintenance availability. GKE uses [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) to update each of the node pools. This depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions).



For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Warning:** If there is no maintenance availability, the control plane might be recreated but the nodes won't yet be recreated. The delay between the two steps might cause [failed node registrations](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-registration) and disruption to your cluster. To manually apply the changes to the nodes to recreate the nodes as unshielded VMs, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running. Manually draining and deleting individual nodes does not recreate the nodes as unshielded VMs.

### Disable Shielded GKE Nodes

### gcloud

When updating the cluster, specify the `--no-enable-shielded-nodes` option:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --no-enable-shielded-nodes
    

### Console

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. Under **Security** , in the **Shielded GKE Nodes** field, click _edit_ **Edit Shielded GKE Nodes**.

  4. Clear the **Enable Shielded GKE Nodes** checkbox.

  5. Click **Save Changes**.




## Node integrity

You can optionally configure node integrity checks on node pools to provide enhanced rootkit and bootkit protection for your nodes. Shielded GKE Nodes, Secure Boot, and Integrity Monitoring are independent features that can each be enabled or disabled individually.

### Secure boot

[Secure boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) is a node pool setting that authenticates the boot components of your node VMs, like the kernel and the bootloader, during the boot process. Secure boot is disabled by default on node pools.

Before you enable secure boot in your node pools, consider the following:

  * Enabling secure boot in Ubuntu nodes blocks unsigned third-party kernel modules from loading in those nodes.
  * Enabling secure boot in Container-Optimized OS nodes has no effect on kernel module loading because Container-Optimized OS node images control the ability to load third-party kernel modules separately from secure boot. If you want to change that setting for Container-Optimized OS nodes, [Configure secure kernel module loading](https://docs.cloud.google.com/kubernetes-engine/security/secure-modules-cos).



To enable secure boot, use the Google Cloud CLI or the Google Cloud console.

### gcloud

To enable secure boot when creating a cluster:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --shielded-secure-boot
    

To enable secure boot when creating a node pool:
    
    
    gcloud container node-pools create POOL_NAME \
        --shielded-secure-boot
    

Secure boot is disabled by default. You can explicitly disable it when creating a cluster or node pool with the `--no-shielded-secure-boot` option.

### Console

To enable secure boot when creating a node pool:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. Click _add_box_ **Add Node Pool**.

  4. From the navigation menu, click **Security**.

  5. Under **Shielded options** , select the **Enable secure boot** checkbox.

  6. Click **Create**.




### Integrity monitoring

[Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) is a node pool setting that's enabled by default on GKE. You can disable integrity monitoring with the Google Cloud CLI or Google Cloud console.

### gcloud

To disable integrity monitoring for system components when creating a node pool:
    
    
    gcloud container node-pools create POOL_NAME \
        --no-shielded-integrity-monitoring
    

Integrity monitoring is enabled by default. You can explicitly enable it when creating a node pool with the `--shielded-integrity-monitoring` option.

### Console

To disable integrity monitoring when creating a node pool:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. Click _add_box_ **Add Node Pool**.

  4. From the navigation pane, click **Security**.

  5. Under **Shielded options** , clear the **Enable integrity monitoring** checkbox.




## What's next

  * [Learn more about Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).
  * [Learn more about node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
