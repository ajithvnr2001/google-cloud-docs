---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect/
title: About Private Service Connect \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:22.338655+00:00
---

# About Private Service Connect  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of Private Service Connect in Google Kubernetes Engine (GKE) clusters. 

This page assumes that you know about the following:

  * Networking basics, such as IP addressing
  * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)



## Overview

Private Service Connect (PSC) is part of Google Cloud's networking infrastructure that allows your GKE clusters to securely and privately consume services hosted on Google Cloud or on-premises environments, without needing to expose those services publicly. With PSC, Google Cloud assigns an internal IP address to the control plane to forward requests to the GKE cluster management API, allowing you to manage your clusters without traffic ever going over the public internet. PSC provides a consistent framework that helps connect different networks through a service networking approach, and allows service producers and consumers to communicate using internal IP addresses internal to a VPC.

In a GKE cluster using PSC infrastructure, all communication between the cluster control plane and nodes happens privately. You can also isolate your cluster at the control plane and node pool levels without needing to manage complex VPC peering configurations.

## Benefits of clusters enabled with Private Service Connect

**Security** : PSC establishes private connections between your GKE cluster control plane and nodes, keeping traffic entirely within Google's network and away from the public internet. This minimizes the risk of unauthorized access.

**Simplified connectivity** : For PSC clusters, you don't have to manage specific subnets for the control plane endpoint. The PSC endpoint is located entirely within the cluster network, eliminating the need for complex network configurations.

**Scalability** : You can create up to 1000 clusters enabled with PSC to meet high resource requirements. In contrast, you can only create up to 75 clusters per zone or region for clusters using VPC Network Peering.

**Customizable configuration** : PSC lets you independently control the isolation of your cluster control plane, node pools, or workloads, making your clusters more scalable and secure. You can configure a mixture of private and public node pools in your cluster.

**Flexibility** : After creating the cluster, you can change the isolation settings at any time. You can toggle between public and private access to the control plane and change node pool and workload accessibility from the internet without having to create a new cluster.

## Limitations

The control plane has both an internal endpoint and an external endpoint. The internal endpoint of the control plane does not support internal IP addresses in URLs for any webhooks you configure. If you have a webhook with an internal IP address in the URL, you can mitigate this incompatibility by following these steps:

  1. **[Create a headless Service without a selector](https://kubernetes.io/docs/concepts/services-networking/service/#without-selectors)** to manually manage the endpoints to which this Service directs traffic. The following example shows a Service with a webhook listening on port 3000:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: <service-name>
         spec:
           clusterIP: None
           ports:
           - port: 3000
             targetPort: 3000
         

  2. **Create a corresponding endpoint for the required destination.** For example, if your webhook uses the internal IP address `10.0.0.1` in the URL, you can create the following endpoint:
         
         apiVersion: v1
         kind: Endpoints
         metadata:
           name: <service-name>
         subsets:
         - addresses:
           - ip: 10.0.0.1
           ports:
           - port: 3000
         

  3. **Update the webhook configuration** : In your webhook configuration, delete the URL with the internal IP address and add the Service that you created in the first step. For example:
         
         ...
         kind: ValidatingWebhookConfiguration
         ...
         webhooks:
         - name: <webhook-name>
         ...
           clientConfig:
             service:
               name: <service-name>
               namespace: <namespace>
               path: "/validate"
               port: 3000
         

In the preceding example, the webhook has a path of `/validate` and listens on port 3000.

  4. **Verify your webhook** : Confirm that your webhook can continue to receive API server requests and can approve, reject or modify the request based on custom logic. If you get an error verifying the webhook, you may need to [create a new certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) and then update the webhook configuration with the new certificate details. For example:
         
         ...
         kind: ValidatingWebhookConfiguration
         ...
         webhooks:
         - name: <webhook-name>
         ...
           clientConfig:
             ...
             caBundle: <new-certificate>
         ...
         




## Architecture

The following diagram provides an overview of the architecture of a cluster using PSC:

![Architecture of Private Service Connect in GKE.](https://docs.cloud.google.com/static/kubernetes-engine/images/psc-concept.svg)**Figure:** Private Service Connect architecture

The following are the core components of a cluster enabled with PSC:

**Control plane** : Every GKE cluster has a Kubernetes API server that is managed by the control plane. The control plane runs on a virtual machine (VM) that is in a VPC network in a Google-managed project. A regional cluster has multiple replicas of the control plane, each of which runs on its own VM.

The control plane has both an internal endpoint (Private Service Connect endpoint) for internal cluster communication and an external endpoint. You may choose to disable the external endpoint. Traffic between nodes and the control plane is routed entirely using internal IP addresses. To learn about your cluster configuration, see [Verify your control plane configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#verify-control-plane-configuration).

**VPC network** : This is a virtual network in which you create subnets with internal IP address ranges specifically for the cluster's nodes and Pods.

**Private Service Connect endpoint** : This is the internal endpoint in the cluster control plane which lives in your project's VPC network. The PSC endpoint acts as the entry point for accessing the cluster control plane.

**Service attachment** : The service attachment is a resource that establishes a secure and private connection between your VPC network and the producer VPC network. As shown in the preceding diagram, the PSC endpoint accesses the service attachment over a private connection and allows traffic to flow between nodes and the control plane.

## Configuring cluster access

You have several options for configuring control plane access and node access on PSC-enabled clusters. You can change these configurations at any time after cluster creation. To configure your cluster access, see [Customize your network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation).

### Control plane access

  * Access the control plane using DNS-based endpoint only (recommended). You can authorize requests to access the control plane by creating IAM allow policies.

  * Access the control plane using IP-based endpoints only. You may choose to use both the external and internal endpoints of the control plane, or disable the external endpoint to only allow access from Google-reserved IP addresses (for cluster management purposes) and GKE cluster internal IP addresses.

If you are using IP addresses, we recommend you use [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation) to restrict access to your cluster's control plane. With authorized networks, you can also block access to your control plane from Google Cloud VMs, Cloud Run or Cloud Run functions sourced with Google Cloud external IPs.

  * Access the control plane with DNS-based endpoint _and_ IP-based endpoints.




### Cluster node access

With PSC-enabled clusters, you can configure mixed-mode clusters. You can configure your cluster to have nodes with internal or external access. You're also able to change the node network configuration depending on the type of cluster that you use:

  * For Autopilot clusters, you can configure some workloads to run on private nodes, and other workloads to run on public nodes. For example, you may be running a mix of workloads in your cluster in which some require internet access and some don't. You can deploy a workload on a node with external IP addressing to ensure that only such workloads are publicly accessible.

  * For Standard clusters, you can provision some of your nodes with internal IP addresses while other nodes can use external IP addresses.




## Clusters with Private Service Connect

To check if your cluster uses Private Service Connect, run the [gcloud container clusters describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/describe) command. If your cluster uses Private Service Connect, the `privateClusterConfig` resource has the following values:

  * The `peeringName` field is empty or doesn't exist.
  * The `privateEndpoint` field has a value assigned.



To enable your cluster with PSC, create the cluster on version 1.29 or later. Otherwise, for versions 1.28 and earlier, create your cluster without enabling private nodes. You can always update this setting and enable private nodes after cluster creation.

**Warning:** Clusters with Private Service Connect using public nodes created before January 30, 2022 use a Private Service Connect _endpoint_ and _forwarding rule_. Both resources are named `gke-[cluster-name]-[cluster-hash:8]-[uuid:8]-pe` and permit the control plane and nodes to privately connect. GKE creates these resources automatically with no cost. If you remove these resources, cluster network issues including downtime will occur.

## What's next

  * Learn about [customizing network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation) in GKE.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
