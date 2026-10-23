---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation/
title: Rotate your control plane IP \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:39.679929+00:00
---

# Rotate your control plane IP  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Rotate your control plane IP Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to perform an IP rotation for your control plane in Google Kubernetes Engine (GKE) clusters.

Before reading this page, ensure that you're familiar with [credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation). We recommend that you perform a credential rotation, which includes IP rotation. However, you might need to perform a standalone IP rotation if you can't perform a full credential rotation.

This page is for Security specialists who maintain the cluster lifecycle on GKE. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## About credential rotations in GKE

The cluster root Certificate Authority (CA) has a limited lifetime. When the CA expires, any credentials that were signed by the CA are no longer valid, including the cluster client certificate (from the `MasterAuth` API field), the key and certificate for the API server, and the `kubelet` client certificates. Your cluster credential lifetime depends on when you created the cluster or when you last rotated your credentials.

You can revoke and reissue these credentials by performing one of the following types of rotations. In most scenarios, we recommend that you perform a full credential rotation, which is more comprehensive than an IP address rotation.

  * [**Credential rotation**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation):

    * Rotates the IP address that the control plane uses for the Kubernetes API server.
    * Rotates the cluster root CA.
    * Rotates Kubernetes ServiceAccount keys, which are used to sign and verify ServiceAccount credentials.
    * Rotates the [aggregation layer CA](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/).
  * **IP address rotation** :

    * Rotates the IP address that the control plane uses for the Kubernetes API server.
    * Rotates the cluster root CA.



For both of these rotation types, nodes must be re-created before they can use new credentials.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Perform an IP rotation

IP rotation is a multi-step process:

  1. When you initiate an IP rotation, your control plane begins serving on the new IP address in addition to the original IP address.
  2. GKE recreates your node pools to use the new IP address, respecting maintenance availability. You can also recreate your node pools manually by performing a node pool version upgrade to the same GKE version that the nodes already run.
  3. After you initiate a rotation, you must update your cluster's API clients (such as development machines using the `kubectl` command-line interface) to begin communicating with the control plane over the new IP address.
  4. When you complete the rotation, the control plane ceases serving traffic with the previous IP address.



When you start an IP address rotation, GKE recreates your nodes for you, respecting maintenance availability. During major events like Google Cloud Next, GKE might pause automatic node recreations so that you don't experience disruptions. To learn more about how maintenance availability affects IP rotation, and what type of disruption your cluster experiences during the steps of a rotation, see the row for IP rotation in the table of [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies). GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for updating the nodes. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

If you don't complete an IP address rotation within seven days of starting it, GKE attempts to complete the rotation for you. If any nodes in your cluster still use the previous IP address, the automatic completion operation fails, but GKE continues to attempt completion until the nodes are recreated and the operation can complete.

You should plan to manually track and complete IP address rotation after you start the rotation. You can always override maintenance availability and manually trigger specific steps to ensure that credential rotation can complete. Don't rely on automatic completion, which is a best-effort measure.

### Start the rotation

  1. To start an IP rotation, run the following command:
         
         gcloud container clusters update CLUSTER_NAME \
             --start-ip-rotation
         

Replace `CLUSTER_NAME` with the name of the cluster.

The output is similar to the following:
         
         This will start an IP Rotation on cluster CLUSTER_NAME.
         The master will be updated to serve on a new IP address in addition to
         the current IP address. Google Kubernetes Engine will then schedule recreation of all nodes
         to point to the new IP address.  If maintenance window is
         used, nodes are not recreated until a maintenance window occurs. See
         documentation on how to manually update nodes. This operation is
         long-running and will block other operations on the cluster (including
         delete) until it has run to completion.
         Do you want to continue (Y/n)?
         

This command configures the control plane to serve on two IP addresses: the original address and a new address.

**Caution:** In zonal Standard clusters, which have a single-node control plane, this command causes brief downtime for the cluster API server. Autopilot clusters and regional Standard clusters have replicated control plane nodes and don't experience downtime.
  2. Confirm the rotation and leave the shell open for the operation to complete.




#### Restart in-cluster components with long-lived connections

After you start an IP address or credential rotation, the cluster's Certificate Authority (CA) is also rotated. Some in-cluster components that maintain long-lived TLS connections, for example `metrics-server` and `konnectivity-agent`, might not automatically trust the new cluster CA.

This situation can cause those connections to fail when communicating with nodes or other cluster endpoints, and you might see TLS handshake errors in the component logs, such as `x509: certificate signed by unknown authority`.

If you observe these errors after starting a rotation, you might need to manually restart your Pods. A restart forces the Pod to re-initialize its connection and load the new cluster CA certificates. For example, to restart the `metrics-server` and `konnectivity-agent`, run the following commands:
    
    
    kubectl rollout restart deployment metrics-server -n kube-system
    kubectl rollout restart deployment konnectivity-agent -n kube-system
    

### Recreate nodes

After reconfiguring the API server to serve on a new IP address, GKE automatically updates your nodes to use the new IP address. GKE upgrades all of your nodes to the nearest supported node version, which recreates the nodes. For more information, refer to [Node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#node_pool_upgrades).

By default, GKE automatically completes IP address rotations seven days after you start the operation. If an active maintenance window or exclusion in your cluster prevents GKE from recreating some nodes during this seven day period, the IP address rotation initially fails to complete. However, GKE continues to try to recreate the nodes and complete the rotation until maintenance availability lets GKE proceed.

  * If you use maintenance exclusions or maintenance windows that could result in a failed rotation, manually upgrade your cluster to force node recreation:
        
        gcloud container clusters upgrade CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --cluster-version=VERSION
        

Replace `VERSION` with the _same_ GKE version that the cluster already uses.

For more information, see [Automatic maintenance that respects GKE maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#examples_of_automatic_maintenance).




#### Check the progress of node pool recreation

  1. To monitor the rotation operation, run the following command:
         
         gcloud container operations list \
             --filter="operationType=UPGRADE_NODES AND status=RUNNING" \
             --format="value(name)"
         

This command returns the _operation ID_ of the node upgrade operation.

  2. To poll the operation, pass the operation ID to the following command:
         
         gcloud container operations wait OPERATION_ID
         




Node pools are recreated one-by-one, and each has its own operation. If you have multiple node pools, use these instructions to poll each operation.

### Update API clients

After initiating IP rotation, you must update all API clients outside the cluster (such as `kubectl` on developer machines) to point to the new IP address.

To update your API clients, run the following command for each client:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME
    

**Note:** If you are using the Kubernetes Certificates API, you also must [issue new certificates](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/).

### Update hardcoded IP addresses and firewall rules

If you hardcoded the IP address of the control plane in your environment, or if you have firewall rules that target the IP address of the control plane, update the addresses to the new IP address. If you complete the rotation without updating IP addresses in applications and in firewall rules, those resources might experience disruptions when GKE stops serving on the previous control plane IP address.

### Complete the rotation

After updating API clients outside the cluster, complete the rotation to configure the control plane to serve only on the new IP address.

To complete the rotation, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --complete-ip-rotation
    

The output is similar to the following:
    
    
    This will complete the in-progress IP Rotation on cluster CLUSTER_NAME.
    The master will be updated to stop serving on the old IP address and only
    serve on the new IP address. Make sure all API clients have been updated
    to communicate with the new IP address (e.g. by running `gcloud container
    clusters get-credentials --project PROJECT_ID --region COMPUTE_REGION
    CLUSTER_NAME`). This operation is long-running and will
    block other operations on the cluster (including delete) until it has
    run to completion.
    

**Caution:** In zonal Standard clusters, which have a single-node control plane, this command causes brief downtime for the cluster API server. Autopilot clusters and regional Standard clusters have replicated control plane nodes and don't experience downtime.

If the IP address rotation fails to complete and returns an error message similar to the following, refer to [Error 400: Node pool requires recreation](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/4xx-errors#credential-rotation-node-recreate):
    
    
    ERROR: (gcloud.container.clusters.update) ResponseError: code=400, message=Node pool "test-pool-1" requires recreation.
    

If you don't complete an IP address rotation within seven days of starting it, GKE attempts to complete the rotation for you. If any nodes in your cluster still use the previous IP address—potentially due to maintenance availability and [related constraints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#unfinished-node-changes) preventing the nodes from being recreated—the automatic completion fails, but GKE continues to attempt completion until the nodes are recreated and the operation can complete.

## What's next

  * [Learn about Alias IPs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * [Learn about IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).
  * [Learn about configuring authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
