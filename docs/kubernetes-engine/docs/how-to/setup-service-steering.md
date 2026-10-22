---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-service-steering/
title: Set up Service Steering \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:27.352914+00:00
---

# Set up Service Steering  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-service-steering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Set up Service Steering Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to set up Service Steering for your Pods.

To understand how Service Steering works, see [How Service Steering works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-service-steering#how-service-steering-works).

## Requirements

  * GKE version 1.30 or later.



## Limitations

  * A `ServiceFunctionChain` can have at most one Service Function.
  * We recommend a maximum of 100 nodes plus 10 `ServiceFunctionChain` and `TrafficSelector` pairs.
  * GKE Service Steering is only available with nodes running the Container-Optimized OS node image.
  * GKE Service Steering supports only egress and destination IP addresses.
  * Service Steering doesn't handle conflicts that arise when multiple Traffic Selectors with identical prefix lengths are applied to the same subject. To avoid conflicts, proactively design your Traffic Selectors with non-overlapping IP address ranges and clearly defined selection criteria.



## Implement Service Steering

GKE Service Steering lets you customize and control the flow of network traffic within a cluster. This section demonstrates how to implement Service Steering using a web Gateway example.

Consider a use case where you want to create a web Gateway that secures traffic from end-user client devices to the internet. A VPN terminator draws traffic into the managed Gateway using a secure tunnel. End-user traffic is redirected to the firewall and then the proxy. The proxy performs Source Network Address Translation (SNAT) on the traffic, masks the original source address, and sends it out to the internet.

To implement GKE Service Steering, do the following:

  1. Create a VPC with MTU of 8896.
  2. Create a GKE cluster.
  3. Create the Service Function Pods and Service.
  4. Create the `ServiceFunctionChain`.
  5. Create the `TrafficSelector` resource referencing the `ServiceFunctionChain`.



### Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Review the requirements and limitations.



### Prepare a VPC

Prepare a [VPC](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). Service Steering uses encapsulation to redirect traffic to the appropriate Service Functions. Encapsulation involves adding extra headers to each packet, which increases the packet size. Service Steering doesn't require special configuration in VPCs. While preparing VPC, we recommend that while deciding the [MTU](https://docs.cloud.google.com/vpc/docs/mtu) size, you account for the encapsulation overhead. For more information, see [VPC network with a specified MTU](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).

The following command sets the mtu size in your VPC:
    
    
    gcloud compute networks create VPC_NETWORK_NAME --mtu=8896
    

Replace `VPC_NETWORK_NAME` with the name of the VPC network that contains the subnet.

### Create a GKE cluster

To enable the advanced network routing and IP address management capabilities necessary for implementing Service Steering on GKE, [create](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-a-gke-cluster) a GKE Dataplane V2 enabled GKE cluster as follows:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --network VPC_NAME \
        --release-channel RELEASE_CHANNEL \
        --cluster-version CLUSTER_VERSION \
        --enable-dataplane-v2 \
        --enable-ip-alias
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `VPC_NAME`: the name of the VPC with which you want to associate the cluster.
  * `RELEASE_CHANNEL`: the name of the release channel.
  * `VERSION`: the GKE version, which must be 1.30 or later. You can also use the `--release-channel` flag to select a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). The release channel must have a default version of 1.30 or later.

**Note:** To apply Service Steering over multiple Network Interface Cards (NICs), use the `--enable-multi-networking` flag.

### Create `ServiceFunction` Pods

To establish your Service Chain, deploy the VPN terminator Pod and the necessary Service Function Pods within your cluster. Pods encapsulate the containerized applications that perform your network functions.

The VPN terminator Pod is often the first Service Function in the chain, which terminates the traffic entering the cluster through the VPN. It then directs the other Service Functions such as firewalls and load balancing for further processing before reaching the final destination.

The following example configuration file defines the following three components essential for network traffic management within a cluster:

  * **VPN Pod:** establishes a Virtual Private Network (VPN) endpoint within your cluster, which enables secure and encrypted communication between your cluster and external networks.
  * **Firewall deployment:** Deploys multiple replicas of a firewall Pod, which provide security and load balancing.
  * **Proxy DaemonSet:** Deploys a proxy Pod on every node of your cluster, which helps ensure that network traffic can be processed locally before being forwarded to other services such as firewall.



Save the following sample manifest as `service_function.yaml`:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: vpn
      namespace: vpn
      labels:
        app: vpn
    spec:
      containers:
      - name: vpn
        image: openvpn
        ports:
        - containerPort: 51820
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: firewall
      namespace: firewall
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: firewall
      template:
        metadata:
          labels:
            app: firewall
        spec:
          containers:
          - name: firewall
            image: firewall
    ---
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: proxy
      namespace: proxy
    spec:
      selector:
        matchLabels:
          app: proxy
      template:
        metadata:
          labels:
            app: proxy
        spec:
          containers:
          - name: proxy
            image: proxy
    

Apply the manifest:
    
    
    kubectl apply -f service_function.yaml
    

### Create `ServiceFunctionChains`

To define a sequence of network functions for traffic to traverse, create a pipeline where each function such as firewall, proxy, and load balancer performs its specific task before passing traffic to the next.

Save the following sample manifest as `ServiceFunctionChain.yaml`:
    
    
    apiVersion: networking.gke.io/v1
    kind: ServiceFunctionChain
    metadata:
      name: firewall
    spec:
      sessionAffinity:
        clientIPNoDestination:
          timeoutSeconds: 3600
      serviceFunctions:
      - name: firewall
        namespace: firewall
        podSelector:
          matchLabels:
            app: firewall
    ---
    apiVersion: networking.gke.io/v1
    kind: ServiceFunctionChain
    metadata:
      name: proxy
    spec:
      sessionAffinity:
        clientIPNoDestination: {}
      serviceFunctions:
      - name: proxy
        namespace: proxy
        podSelector:
          matchLabels:
            app: proxy
    

Apply the manifest:
    
    
    kubectl apply -f ServiceFunctionChain.yaml
    

The Service Functions are defined inline within the `ServiceFunctionChain` using the `serviceFunctions` field. A Service Function is an endpoint selector.

### Create the `TrafficSelector` resource

To define where and which traffic is selected for Service Steering, create the `TrafficSelector` resource referencing the `ServiceFunctionChains` to apply to the chosen traffic.

Save the following sample manifest as `TrafficSelector.yaml`:
    
    
    apiVersion: networking.gke.io/v1
    kind: TrafficSelector
    metadata:
      name: vpn-to-firewall
    spec:
      serviceFunctionChain: firewall
      subject:
        pods:
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: vpn
          podSelector:
            matchLabels:
              app: vpn
      egress:
        to:
          ipBlock:
            cidr: 0.0.0.0/0
        ports:
        - allPorts:
            protocol: UDP
        - allPorts:
            protocol: TCP
    ---
    apiVersion: networking.gke.io/v1
    kind: TrafficSelector
    metadata:
      name: firewall-to-proxy
    spec:
      serviceFunctionChain: proxy
      subject:
        pods:
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: firewall
          podSelector:
            matchLabels:
              app: firewall
      egress:
        to:
          ipBlock:
            cidr: 0.0.0.0/0
        ports:
        - allPorts:
            protocol: UDP
        - allPorts:
            protocol: TCP
    

Apply the manifest:
    
    
    kubectl apply -f TrafficSelector.yaml
    

## Troubleshoot Service Steering

This section shows you how to resolve issues related to GKE Service Steering.

### Network traffic not flowing

You can take the following actions to debug the issue:

**Step 1: Verify`servicePathId` is set on `ServiceFunctionChain`**

Verify `servicePathId` is set on `ServiceFunctionChain`. Every `ServiceFunctionChain` object is assigned a unique `servicePathId` as shown in the following example:
    
    
    apiVersion: networking.gke.io/v1
    kind: ServiceFunctionChain
    metadata:
      name: firewall
    spec:
      serviceFunctions:
      - name: firewall
        namespace: firewall
        podSelector:
          matchLabels:
            app: firewal
    status:
      servicePathId: 1
    

**Step 2: Verify a Kubernetes Service is created per Service Function**

A ClusterIP Service is created for each Service Function automatically. You can view the list of services by using `kubectl`:
    
    
    kubectl get svc -A -l networking.gke.io/managed-by=service-steering-controller.gke.io
    

**Step 3: Verify that for each Service Function, a bpf map entry is created on each node to store the Service IP address**

For each Service Function, a bpf map entry is created on each node to store the Service IP address.

Get the name of the `anetd` Pod:
    
    
    kubectl get pods -n kube-system -o wide -l k8s-app=cilium
    

Record the name of the Pod similar to `anetd`.

Run the following command:
    
    
    kubectl -n kube-system exec -it ANETD-POD-NAME -- cilium bpf sfcpath list
    

Replace `ANETD-POD-NAME` with the name of the `anetd` Pod.

The output is similar to the following:
    
    
    PATH     SERVICE FUNCTION ADDRESS
    (1, 1)   10.4.10.124
    

**Step 4: Verify that bpf map entries are created in`sfcselect` map**

On a node, if there are Pods selected by a `TrafficSelector`, bpf map entries are created in `sfcselect` map. The following example shows that TCP/UDP traffic from any port of endpoint (Pod) 3783 to destination IP address 10.0.2.12 is steered to a `ServiceFunctionChain`.

Run the following command:
    
    
    kubectl -n kube-system exec -it ANETD-POD-NAME -- cilium bpf sfcselect list
    

Replace `ANETD-POD-NAME` with the actual name of the anetd Pod in your cluster.

The output is similar to the following:
    
    
    SELECTOR                            PATH
    3783, egress, 0/TCP, 10.0.2.12/32   /32 (1, 1)
    3783, egress, 0/UDP, 10.0.2.12/32   /32 (1, 1)
    

**Step 5: Use tcpdump on port 7081 to capture and analyze network traffic**

Service Steering does [Geneve encapsulation](https://en.wikipedia.org/wiki/Generic_Network_Virtualization_Encapsulation) at UDP port 7081. You can use tcpdump on the relevant nodes to analyze the traffic flow and pinpoint where the issue might be occurring.

## What's next

  * Read [About multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods)
  * Read [About Service Steering](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-service-steering)
  * Read [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
