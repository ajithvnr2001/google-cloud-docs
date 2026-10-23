---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility/
title: Setting up intranode visibility \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:27.027031+00:00
---

# Setting up intranode visibility  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Setting up intranode visibility Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows you how to set up _intranode visibility_ on a Google Kubernetes Engine (GKE) cluster.

Intranode visibility configures networking on each node in the cluster so that traffic sent from one Pod to another Pod is processed by the cluster's Virtual Private Cloud (VPC) network, even if the Pods are on the same node.

Intranode visibility is disabled by default on Standard clusters and enabled by default in Autopilot clusters.

## Architecture

Intranode visibility helps ensure that packets sent between Pods are processed by the VPC network. The VPC network then applies firewall rules, routes, flow logs, and packet mirroring configurations to these packets.

When a Pod sends a packet to another Pod on the same node, the packet leaves the node and is processed by the Google Cloud network. Then the packet is immediately sent back to the same node and forwarded to the destination Pod.

Enabling intranode visibility configures network components on each node to manage host network settings:

  * **In GKE Dataplane V2 (GKE version 1.36.0-gke.3302000 or later):** intranode visibility is eBPF-native. Traffic redirection is processed in eBPF, bypassing the host network stack.
  * **In earlier GKE versions or non-GKE Dataplane V2 clusters:** the `netd` DaemonSet manages packet redirection on the node.



## Benefits

Intranode visibility provides the following benefits:

  * See [flow logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) for all traffic between Pods, including traffic between Pods on the same node.
  * Create [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) that apply to all traffic among Pods, including traffic between Pods on the same node.
  * Use [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) to clone traffic, including traffic between Pods on the same node, and forward it for examination.



## Requirements and limitations

Intranode visibility has the following requirements and limitations:

  * Your cluster must be on GKE version 1.15 or later.
  * Intranode visibility is not supported with Windows Server node pools.
  * For clusters configured with [multi-networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods), intranode visibility applies only to traffic on the default network.
  * To prevent connectivity issues, when using `ip-masq-agent` with intranode visibility, your custom `nonMasqueradeCIDRs` list must include the cluster's node and Pod IP address ranges.



## Firewall rules

When you enable intranode visibility, the VPC network processes all packets sent between Pods, including packets sent between Pods on the same node. This means VPC firewall rules and hierarchical firewall policies consistently apply to Pod-to-Pod communication, regardless of Pod location.

If you configure custom firewall rules for communication within the cluster, carefully evaluate your cluster's networking needs to determine the set of egress and ingress allow rules. You can use connectivity tests to ensure that legitimate traffic is not obstructed. For example, Pod-to-Pod communication is required for [network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) to function.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable intranode visibility on a new cluster

You can create a cluster with intranode visibility enabled using the gcloud CLI or the Google Cloud console.

### gcloud

To create a single-node cluster that has intranode visibility enabled, use the `--enable-intra-node-visibility` flag:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-intra-node-visibility
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Console

To create a single-node cluster that has intranode visibility enabled, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_**Create**.

  3. Enter the **Name** for your cluster.

  4. In the **Configure cluster** dialog, next to **GKE Standard** , click **Configure**.

  5. Configure your cluster as needed.

  6. From the navigation pane, under **Cluster** , click **Networking**.

  7. Select the **Enable intranode visibility** checkbox.

  8. Click **Create**.




## Enable intranode visibility on an existing cluster

You can enable intranode visibility on an existing cluster using the gcloud CLI or the Google Cloud console.

When you enable intranode visibility for an existing cluster, GKE restarts components in both the control plane and the worker nodes.

### gcloud

To enable intranode visibility on an existing cluster, use the `--enable-intra-node-visibility` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-intra-node-visibility
    

Replace `CLUSTER_NAME` with the name of your cluster.

### Console

To enable intranode visibility on an existing cluster, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Networking** , click _edit_ **Edit intranode visibility**.

  4. Select the **Enable intranode visibility** checkbox.

  5. Click **Save Changes**.




This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Important:** GKE respects maintenance policies when recreating the nodes for this change using the node upgrade strategy, and depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). To manually apply the changes to the nodes, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running.

## Disable intranode visibility

You can disable intranode visibility on a cluster using the gcloud CLI or the Google Cloud console.

When you disable intranode visibility for an existing cluster, GKE restarts components in both the control plane and the worker nodes.

### gcloud

To disable intranode visibility, use the `--no-enable-intra-node-visibility` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --no-enable-intra-node-visibility
    

Replace `CLUSTER_NAME` with the name of your cluster.

### Console

To disable intranode visibility, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Networking** , click _edit_ **Edit intranode visibility**.

  4. Clear the **Enable intranode visibility** checkbox.

  5. Click **Save Changes**.




This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Important:** GKE respects maintenance policies when recreating the nodes for this change using the node upgrade strategy, and depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). To manually apply the changes to the nodes, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running.

## Exercise: Verify intranode visibility

This exercise shows you the steps required to enable intranode visibility and confirm that it is working for your cluster.

In this exercise, you perform the following steps:

  1. Enable flow logs for the default subnet in the `us-central1` region.
  2. Create a single-node cluster with intranode visibility enabled in the `us-central1-a` zone.
  3. Create two Pods in your cluster.
  4. Send an HTTP request from one Pod to another Pod.
  5. View the flow log entry for the Pod-to-Pod request.



### Enable flow logs

  1. Enable flow logs for the default subnet:
         
         gcloud compute networks subnets update default \
             --region=us-central1 \
             --enable-flow-logs
         

  2. Verify that the default subnet has flow logs enabled:
         
         gcloud compute networks subnets describe default \
             --region=us-central1
         

The output shows that flow logs are enabled, similar to the following:
         
         ...
         enableFlowLogs: true
         ...
         




### Create a cluster

  1. Create a single node cluster with intranode visibility enabled:
         
         gcloud container clusters create flow-log-test \
             --location=us-central1-a \
             --num-nodes=1 \
             --enable-intra-node-visibility
         

  2. Get the credentials for your cluster:
         
         gcloud container clusters get-credentials flow-log-test \
             --location=us-central1-a
         




### Create two Pods

  1. Create a Pod.

Save the following manifest to a file named `pod-1.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: pod-1
         spec:
           containers:
           - name: container-1
             image: google/cloud-sdk:slim
             command:
             - sh
             - -c
             - while true; do sleep 30; done
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f pod-1.yaml
         

  3. Create a second Pod.

Save the following manifest to a file named `pod-2.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: pod-2
         spec:
           containers:
           - name: container-2
             image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0
         

  4. Apply the manifest to your cluster:
         
         kubectl apply -f pod-2.yaml
         

  5. View the Pods:
         
         kubectl get pod pod-1 pod-2 --output wide
         

The output shows the IP addresses of your Pods, similar to the following:
         
         NAME      READY     STATUS    RESTARTS   AGE       IP           ...
         pod-1     1/1       Running   0          1d        10.52.0.13   ...
         pod-2     1/1       Running   0          1d        10.52.0.14   ...
         

Note the IP addresses of `pod-1` and `pod-2`.




### Send a request

  1. Get a shell to the container in `pod-1`:
         
         kubectl exec -it pod-1 -- sh
         

  2. In your shell, send a request to `pod-2`:
         
         curl -s POD_2_IP_ADDRESS:8080
         

Replace `POD_2_IP_ADDRESS` with the IP address of `pod-2`.

The output shows the response from the container running in `pod-2`.
         
         Hello, world!
         Version: 2.0.0
         Hostname: pod-2
         

  3. Type exit to leave the shell and return to your main command-line environment.




### View flow log entries

To view a flow log entry, use the following command:
    
    
    gcloud logging read \
        'logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows" AND jsonPayload.connection.src_ip="POD_1_IP_ADDRESS" AND jsonPayload.connection.dest_ip="POD_2_IP_ADDRESS"'
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POD_1_IP_ADDRESS`: the IP address of `pod-1`.
  * `POD_2_IP_ADDRESS`: the IP address of `pod-2`.



The output shows a flow log entry for a request from `pod-1` to `pod-2`. In this example, `pod-1` has IP address `10.56.0.13`, and `pod-2` has IP address `10.56.0.14`.
    
    
    ...
    jsonPayload:
      bytes_sent: '0'
      connection:
        dest_ip: 10.56.0.14
        dest_port: 8080
        protocol: 6
        src_ip: 10.56.0.13
        src_port: 35414
    ...
    

## Clean up

To avoid incurring unwanted charges on your account, perform the following steps to remove the resources you created:

  1. Delete the cluster:
         
         gcloud container clusters delete -q flow-log-test
         

  2. Disable flow logs for the default subnet:
         
         gcloud compute networks subnets update default --no-enable-flow-logs
         




## What's next

  * Learn how to control the communication between your cluster's Pods and Services by [creating a cluster network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).
  * Learn about the benefits of [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
