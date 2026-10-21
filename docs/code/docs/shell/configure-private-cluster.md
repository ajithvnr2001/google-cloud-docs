---
url: https://docs.cloud.google.com/code/docs/shell/configure-private-cluster/
title: Configure a private cluster in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:46.374660+00:00
---

# Configure a private cluster in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/configure-private-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Configure a private cluster in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

A _private cluster_ is a Virtual Private Cloud (VPC)-native cluster that only depends on [internal IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#internal_ip_addresses). This means that nodes and pods are isolated from the internet by default. This page explains how to use Cloud Code to connect to private clusters with and without public endpoint access and permit private clusters to access resources from outside Google Cloud.

For information about private clusters, see [Private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept). For steps to configure private clusters, see [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters).

## Add a private GKE cluster to your KubeConfig

Adding a private cluster in Cloud Code has the following behavior:

  * For clusters that have the public endpoint enabled, adding the cluster sets the cluster address in the KubeConfig to the external IP.

  * For clusters that have the public endpoint turned off, adding the cluster sets the cluster address in the KubeConfig to be the internal VPC IP of the cluster.




To add an authorized network to an existing cluster, make sure you are connected to an authorized network, as this cluster has [authorized networks enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add).

To learn more about connecting to VMs without external IP addresses, see [Securely connecting to VM instances](https://cloud.google.com/solutions/connecting-securely#external). To manage/delete the instances that you created, see [VM instances](https://console.cloud.google.com/compute/instances).

To successfully connect to the private cluster, Cloud Code must be running on a machine in the cluster's network or be able to access the cluster's network, such as by using a proxy server, Cloud Interconnect, or Cloud VPN.

For steps to create GKE clusters in Cloud Code and add existing GKE clusters to Cloud Code, see [create and configure a GKE cluster](https://docs.cloud.google.com/code/docs/shell/create-configure-gke-cluster). Cloud Code opens the Google Cloud console to create your cluster.

After you create the cluster, [configure Cloud NAT](https://docs.cloud.google.com/nat/docs/gke-example?_ga=2.200274222.-1614030937.1640827593#gcloud) to enable outbound internet connections from your cluster if this was not set up during cluster creation. To manage/delete the networks that you created, see [VPC networks](https://console.cloud.google.com/networking/networks/list).

## Troubleshoot issues connecting to private clusters

If your dev environment isn't configured correctly to access a private cluster, recommendations about how to resolve the issue appear in the following contexts:

  * In the expanded **Kubernetes** Explorer, clusters that Cloud Code can't connect to appear with an error icon next to the cluster name. To view possible workarounds and a longer explanation of the potential issue, click the cluster name.

  * When you try to run operations on a cluster that's inaccessible because of potential issues with the private cluster's configuration, a notification displays an error message with a longer explanation of the potential issue and potential workarounds.




## Configure a proxy server for a cluster

If the [control plane API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) isn't available publicly, such as in a GKE cluster with public endpoint turned off, you can configure Cloud Code to proxy requests to the control plane through a proxy server on the same network or VPC as the cluster:

  1. Configure a proxy server on the same network as your cluster if you haven't already. For steps to set up a Compute Engine VM as a basic proxy server, see [Remotely access a private cluster using a bastion host](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/private-cluster-bastion). For additional details, see [Creating Google Kubernetes Engine private clusters with network proxies for controller access](https://docs.cloud.google.com/architecture/creating-kubernetes-engine-private-clusters-with-net-proxies).
  2. Right-click the name of a cluster you've added to Cloud Code and then click **Set up Kubectl Proxying for cluster**. Follow the prompts to enter the name of your proxy server, which is stored in the cluster's `proxy-url` field. The Kubernetes view reloads to display the connected cluster.



### Cancel Kubernetes proxying

Right-click the name of a cluster you've configured for Kubernetes proxying and then click **Cancel Kubectl Proxying for cluster**. Cloud Code stops proxying requests for the cluster by unsetting the `proxy-url` field in the KubeConfig.

## Access resources outside Google Cloud from clusters

All configurations of GKE private clusters don't provide nodes with internet access. As a result, clusters can't reach APIs on the public internet. Clusters are automatically configured with [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access), which, for example, permits clusters to pull images from Artifact Registry. APIs and image registries outside of Google Cloud are inaccessible without additional configuration to allow outbound internet connections from the nodes. To provide these connections, you can set up [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE) on your VPC from Cloud Code:

  1. Run the **Grant private GKE nodes outbound internet access** command, either by right-clicking a cluster or from the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**).
  2. In the terminal, edit the [`gcloud compute routers create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) and [`gcloud beta compute routers nats create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/nats/create) commands to specify the values for your application.
  3. To run the commands, press `Enter`.
  4. To manage/delete the routers that you created, see [Cloud Routers](https://console.cloud.google.com/hybrid/routers/list).



## What's next

  * Learn about [Shared Virtual Private Cloud networks](https://docs.cloud.google.com/vpc/docs/shared-vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
