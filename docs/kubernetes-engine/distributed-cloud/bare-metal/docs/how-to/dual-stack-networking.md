---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking/
title: IPv4/IPv6 dual-stack networking \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:50.210044+00:00
---

# IPv4/IPv6 dual-stack networking  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  IPv4/IPv6 dual-stack networking Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud supports [IPv4/IPv6 dual-stack networking](https://kubernetes.io/docs/concepts/services-networking/dual-stack/). This means that a cluster can accept traffic from external devices that use either [Internet Protocol version 4](https://en.wikipedia.org/wiki/IPv4) (IPv4) or [Internet Protocol version 6](https://en.wikipedia.org/wiki/IPv6) (IPv6).

Dual-stack networking assigns both IPv4 and IPv6 addresses to Pods and nodes. A Kubernetes Service can have an IPv4 address, an IPv6 address, or both.

All dual-stack clusters use [flat mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network) for IPv6. By default, a dual-stack cluster uses island mode for IPv4, but you can configure it to use flat mode for IPv4.

To create a dual-stack cluster, your underlying network must be dual-stack enabled. If your underlying network is a single-stack IPv4 or IPv6 network, you can't start a dual-stack cluster.

## Before you begin

If your cluster nodes are running [RedHat Enterprise Linux](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs), and they have [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) enabled, then on each node:

  * In `/etc/firewalld/firewalld.conf`, set `IPv6_rpfilter=no`.

  * Run `systemctl restart firewalld`.




## Overview of creating a dual-stack cluster

You can enable dual-stack networking when you create a new cluster, but you can't enable dual-stack networking for an existing cluster.

Follow the instructions in one of the [cluster creation documents](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

In your configuration file, include manifests for the following:

  * A Namespace resource
  * A Cluster resource
  * One or more NodePool resources
  * One or more `ClusterCIDRConfig` resources



Fill in the Namespace manifest and the NodePool manifests as you would for a single-stack cluster.

In the Cluster manifest, under `clusterNetwork.services.cidrBlocks`, specify both an IPv4 CIDR range and an IPv6 CIDR range. This is the enabling criterion for a dual-stack cluster. That is, if you provide Service CIDR ranges for both IPv4 and IPv6, your cluster will have a dual-stack network.

In the Cluster manifest, under `clusterNetwork.pods.cidrBlocks`, specify an IPv4 CIDR range, but don't specify an IPv6 CIDR range. IPv6 CIDR ranges for Pods are specified in `ClusterCIDRConfig` manifests.

If you are using bundled load balancing, provide both IPv4 and IPv6 addresses in the `loadBalancer.addressPools` section of the Cluster manifest.

The `ClusterCIDRConfig` resources are for specifying IPv4 and IPv6 CIDR ranges for Pods. You can use a single `ClusterCIDRConfig` resource to specify CIDR ranges that are cluster-wide. That is, the IPv4 Pod addresses for all nodes are taken from a single CIDR range, and the IPv6 Pod addresses for all nodes are taken from a single CIDR range. Or you can use several `ClusterCIDRConfig` resources to specify CIDR ranges that apply to a particular node pool or a particular node.

**Note:** Dual-stack clusters cannot be reverted to single-stack. In addition, the `ClusterCIDRConfig` object is immutable; to modify CIDR configurations, create a new `ClusterCIDRConfig` object.

## Reachability for Pod IP addresses

A dual-stack cluster uses flat mode for IPv6 networking. The example given in this document is for a cluster that uses static flat-mode networking for IPv6. That is, the cluster is not configured to use Border Gateway Protocol (BGP).

For a cluster that uses static flat-mode networking, you must specify node and Pod IP addresses that are all part of the same subnet. This configuration makes it possible for clients outside the cluster, but in the same [Layer 2 domain](https://en.wikipedia.org/wiki/Broadcast_domain) as the cluster nodes, to send packets directly to Pod IP addresses.

For example, suppose your cluster nodes and some other machines are all in the same Layer 2 domain. Here's one way you could specify address ranges:

Purpose| Range| Number of addresses  
---|---|---  
Entire Layer 2 domain| `fd12::/108`| 220  
Pods| `fd12::1:0/112`| 216  
Nodes| `fd12::2:0/112`| 216  
Other machines| `fd12::3:0/112`| 216  
VIPs| `fd12::4:0/112`| 216  
  
In the preceding example, these are the key points to understand:

  * All node, Pod, and machine addresses are in the large range: `fd12::/108`.

  * The Pod IP addresses are in a subset of the large range.

  * The node IP addresses are in a different subset of the large range.

  * The IP addresses of other machines are in a different subset of the large range.

  * All the subset ranges are distinct from each other.




In the preceding example, each machine in the Layer 2 domain, including the cluster nodes, must have a forwarding rule for the large range. For example:
    
    
    inet fd12::/108 scope global eth0

## Example: Create a dual-stack cluster

When you create a dual-stack cluster, you have various options. For example, you could have cluster-wide CIDR ranges or you could have CIDR ranges that apply to particular node pools. You could combine an IPv6 flat network with an IPv4 island-mode network. Or both your IPv4 and IPv6 networks could be flat. You could use bundled load balancing or manual load balancing.

This section gives one example of how to create a dual-stack cluster. The cluster in this example has the following characteristics:

  * An IPv4 network in island mode
  * An IPv6 network in flat mode
  * A cluster-wide IPv4 CIDR range for Pods
  * A cluster-wide IPv6 CIDR range for Pods
  * A cluster-wide IPv4 CIDR range for Services
  * A cluster-wide IPv6 CIDR range for Services
  * An IPv4 address pool to be used for Services of type `LoadBalancer`
  * An IPv6 address pool to be used for Services of type `LoadBalancer`
  * Bundled load balancing



For additional configuration examples, see Variations on using ClusterCIDRConfig.

### Fill in a configuration file

Follow the instructions in one of the [cluster creation documents](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

In your configuration file, in the `Cluster` manifest:

  * For `clusterNetwork.pods.cidrBlocks`, provide a single IPv4 CIDR range.

  * For `clusterNetwork.services.cidrBlocks`, provide two CIDR ranges: one for IPv4 and one for IPv6.

  * For `loadBalancer.addressPools`, provide two address ranges: one for IPv4 and one for IPv6. When you create a [Service of type `LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer), the external IP addresses for the Service are chosen from these ranges.




Here is an example that shows the relevant portions of a Cluster manifest:

**Caution:** Don't use this example as-is. Replace the address ranges with values that are appropriate for your network.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: "dual-stack"
      namespace: "cluster-dual-stack"
    
    spec:
      clusterNetwork:
        pods:
          cidrBlocks:
          - "192.168.0.0/16"
        services
          cidrBlocks:
           - "172.16.0.0/20"
           - "fd12::5:0/116"
    ...
      loadBalancer:
        mode: "bundled"
        ...
        addressPools:
        - name: "pool-1"
          addresses:
           - "10.2.0.212-10.2.0.221"
           - "fd12::4:101-fd12::4:110"
    

In the same configuration file, include a manifest for a `ClusterCIDRConfig`.

  * Set `ipv4.cidr` to the same CIDR range that you provided in the `Cluster` manifest. This is a requirement if IPv4 is in island mode.

  * Set `namespace` to the same value that you provided in the `Cluster` manifest.

  * Set `ipv6.cidr` to an IPv6 CIDR range for Pods.

  * For each CIDR range, provide a value for `perNodeMaskSize` to specify how many Pod addresses will be assigned to each node. The number of IPv4 addresses assigned to each node must be the same as the number of IPv6 addresses assigned to each node. You must set your values for `perNodeMaskSize` accordingly. For example, if you want 28 addresses per node, set your `perNodeMaskSize` values as follows:

    * `ipv4.perNodeMaskSize: 24` # (32 - 8 = 24)
    * `ipv6.perNodeMaskSize: 120` # (128 - 8 = 120)



Here's an example of a `ClusterCIDRConfig` manifest:

**Caution:** Don't use this example as-is. Replace the address ranges with values that are appropriate for your network.
    
    
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig
    metadata:
      name: "cluster-wide-ranges"
      namespace: "cluster-dual-stack"  # Must be the same as the Cluster namespace.
    spec:
      ipv4:
        cidr: "192.168.0.0/16"  #  For island mode, must be the same as the Cluster CIDR.
        perNodeMaskSize: 24
      ipv6:
        cidr: "fd12::1:0/112"
        perNodeMaskSize: 120
    

In the preceding example:

  * The IPv4 Pod CIDR range has 2(32-16) = 216 addresses. The per-node mask size is 24, so the number of addresses assigned to each node is 2(32-24) = 28.

  * The IPv6 Pod CIDR range has 2(128-112) = 216 addresses. The per-node mask size is 120, so the number of addresses assigned to each node is 2(128-120) = 28.




#### Example configuration file

Click to see an example of a completed configuration file.

**Caution** : Don't use this example as-is. Replace the address ranges and key paths with values that are appropriate for your network.
    
    
    gcrKeyPath: "bmctl-workspace/.sa-keys/gcr.json"
    sshPrivateKeyPath: "/home/me/.ssh/id_rsa"
    gkeConnectAgentServiceAccountKeyPath: "bmctl-workspace/.sa-keys/bm-connect.json"
    gkeConnectRegisterServiceAccountKeyPath: "bmctl-workspace/.sa-keys/bm-register.json"
    cloudOperationsServiceAccountKeyPath: "bmctl-workspace/.sa-keys/bm-cloud-ops.json"
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: "cluster-dual-stack"
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: "dual-stack"
      namespace: "cluster-dual-stack"
    spec:
      type: "user"
      anthosBareMetalVersion: "1.14.0"
      gkeConnect:
        projectID: "my-project"
      controlPlane:
        nodePoolSpec:
          nodes:
          - address: "10.2.0.4"
      clusterNetwork:
        pods:
          cidrBlocks:
          - "192.168.0.0/16"
        services:
          cidrBlocks:
           - "172.16.0.0/20"
           - "fd12::5:0/116"
      loadBalancer:
        mode: "bundled"
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: "10.2.0.211
          ingressVIP: "10.2.0.212"
        addressPools:
        - name: "pool-1"
          addresses:
          - "10.2.0.212-10.2.0.221"
          - "fd12::4:101-fd12::4:110
      clusterOperations:
        projectID: "my-project"
        location: "us-central1"
      storage:
        lvpNodeMounts:
          path: "/mnt/localpv-disk"
          storageClassName: "node-disk"
        lvpShare:
          numPVUnderSharedPath: 5
          path: "/mnt/localpv-share"
          storageClassName: "local-shared"
      nodeConfig:
        podDensity:
          maxPodsPerNode: 110
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: "pool-1"
      namespace: "cluster-dual-stack"
    spec:
      clusterName: "dual-stack"
      nodes:
      - address: "10.2.0.5"
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig
    metadata:
      name: "cluster-wide-ranges"
      namespace: "cluster-dual-stack"
    spec:
      ipv4:
        cidr: "192.168.0.0/16"
        perNodeMaskSize: 24
      ipv6:
        cidr: "fd12::1:0/112"
        perNodeMaskSize: 120
    

### Finish creating the cluster

Finish creating your cluster as described in your [cluster creation document](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

## View cluster nodes and Pods

List the cluster nodes:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get nodes --output yaml
    

Replace `CLUSTER_KUBECONFIG` with the path of your cluster kubeconfig file.

In the output, you can see the IPv4 and IPv6 addresses of each node. You can also see the IPv4 and IPv6 address ranges for Pods on the node. For example:
    
    
    - apiVersion: v1
      kind: Node
      ...
      spec:
        podCIDR: 192.168.1.0/24
        podCIDRs:
        - 192.168.1.0/24
        - fd12::1:100/120
        providerID: baremetal://10.2.0.5
      status:
        addresses:
        - address: 10.2.0.5
          type: InternalIP
        - address: fd12::2:5
          type: InternalIP
    

List the Pods in the cluster:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get pods --all-namespaces
    

Choose one Pod, and list the details. For example:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get pod gke-metrics-agent-b9qrv \
      --namespace kube-system \
      -- output yaml
    

In the output, you can see the IPv4 and IPv6 addresses of the Pod. For example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      ...
      name: gke-metrics-agent-b9qrv
      namespace: kube-system
    ...
    status:
      ...
      podIPs:
      - ip: 192.168.1.146
      - ip: fd12::1:11a
    

## Variations on using ClusterCIDRConfig

The preceding example used a `ClusterCIDRConfig` object to specify cluster-wide Pod CIDR ranges. That is, a single IPv4 CIDR range is used for all Pods in the cluster. And a single IPv6 CIDR range is used for all Pods in the cluster.

In certain situations, you might not want to use a single CIDR range for all Pods in a cluster. For example, you might want to specify a separate CIDR range for each node pool, or you might want to specify a separate CIDR range for each node. For more information on `ClusterCIDRConfig` and examples on using it, see [Understand the ClusterCIDRConfig custom resource](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-cidr-config).

For example, the following `ClusterCIDRConfig` specifies a CIDR range for a node pool named `"workers"`.

**Caution:** Don't use these examples as they appear here. Replace the address ranges with values that are appropriate for your network.
    
    
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig
    metadata:
      name: "worker-pool-ccc"
      namespace: "cluster-dual-stack"
    spec:
      ipv4:
        cidr: "192.168.0.0/16"
        perNodeMaskSize: 24
      ipv6:
        cidr: "fd12::1:0/112"
        perNodeMaskSize: 120
      nodeSelector:
        matchLabels:
          baremetal.cluster.gke.io/node-pool: "workers"
    

The following `ClusterCIDRConfig` specifies a CIDR range for a single node that has IP address `10.2.0.5`:
    
    
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig
    metadata:
      name: "range-node1"
      namespace: "cluster-dual-stack"
    spec:
      ipv4:
        cidr: "192.168.1.0/24"
        perNodeMaskSize: 24
      ipv6:
        cidr: "fd12::1:0/120"
        perNodeMaskSize: 120
      nodeSelector:
        matchLabels:
          baremetal.cluster.gke.io/k8s-ip: "10.2.0.5"
    

## Create a dual-stack Service of type `ClusterIP`

Here is a manifest for a Deployment:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: "my-deployment"
    spec:
      selector:
        matchLabels:
          app: "try-dual-stack"
      replicas: 3
      template:
        metadata:
          labels:
            app: "try-dual-stack"
        spec:
          containers:
          - name: "hello"
            image: "us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0"
    

Save the manifest in a file named `my-deployment.yaml`, and create the Deployment:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-deployment.yaml
    

Replace `CLUSTER_KUBECONFIG` with the path of your cluster kubeconfig file.

Here is a manifest for a Service of type `ClusterIP`:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: "my-service"
    spec:
      selector:
        app: "try-dual-stack"
      type: "ClusterIP"
      ipFamilyPolicy: "RequireDualStack"
      ipFamilies:
      - "IPv6"
      - "IPv4"
      ports:
      - port: 80
        targetPort: 8080
    

In the context of this exercise, these are the key points to understand about the preceding Service manifest:

  * The `ipFamilyPolicy` field is set to `RequireDualStack` This means both IPv6 and IPv4 `ClusterIP` addresses are allocated for the Service.

  * The `ipFamilies` field specifies the IPv6 family first and the IPv4 family second. This means that `spec.ClusterIP` for the Service will be an IPv6 address chosen from `clusterNetwork.services.cidrBlocks` in the Cluster manifest.




Save the manifest in a file named `my-cip-service.yaml`, and create the Service:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-cip-service.yaml
    

List details about the Service:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get service my-service --output yaml
    

In the output, you can see the cluster IP addresses for the Service. For example:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
      …
    spec:
      clusterIP: fd12::5:9af
      clusterIPs:
      - fd12::5:9af
      - 172.16.12.197
    

On a cluster node, call the Service:
    
    
    curl IPV4_CLUSTER_IP
    curl IPV6_CLUSTER_IP
    

The output displays a "Hello world" message:
    
    
    Hello, world!
    Version: 2.0.0
    Hostname: my-deployment-xxx
    

## Create a dual-stack Service of type `LoadBalancer`

Here is a manifest for a Service of type `LoadBalancer`:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: "my-lb-service"
    spec:
      selector:
        app: "try-dual-stack"
      type: "LoadBalancer"
      ipFamilyPolicy: "RequireDualStack"
      ipFamilies:
      - "IPv6"
      - "IPv4"
      ports:
      - port: 80
        targetPort: 8080
    

Save the manifest in a file named `my-lb-service.yaml`, and create the Service:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-lb-service.yaml
    

Recall that in your Cluster manifest, you specified a range of IPv6 addresses and a range of IPv4 addresses to be used for Services of type `LoadBalancer`:
    
    
      loadBalancer:
        mode: "bundled"
        ...
        addressPools:
        - name: "pool-1"
          addresses:
          - "10.2.0.112-10.2.0.221"
          - "fd12::4:101-fd12::4:110"
    

Your Service will be assigned an external IPv4 address chosen from the IPv4 range and an external IPv6 address chosen from the IPv6 range.

List details for the Service:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get service my-lb-service --output yaml
    

In the output, you can see the external addresses for the Service. For example:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-lb-service
    ...
    status:
      loadBalancer:
        ingress:
        - ip: 10.2.0.213
        - ip: fd12::4:101
    

## Possible values for `ipFamilyPolicy`

When you create a dual-stack Service, you can set `ipFamilyPolicy` to one of these values:

  * `SingleStack`: The controller allocates a cluster IP address for the Service, chosen from the first range specified in the Cluster manifest under `clusterNetwork.services.cidrBlocks`.

  * `PreferDualStack`: The controller allocates IPv4 and IPv6 cluster IP addresses for the Service, chosen from the ranges specified in the Cluster manifest under `clusterNetwork.services.cidrBlocks`. If the cluster is not a dual-stack cluster, the behavior is the same as with `SingleStack`.

  * `RequireDualStack`: The controller allocates IPv4 and IPv6 cluster IP addresses for the Service, chosen from the ranges specified in the Cluster manifest under `clusterNetwork.services.cidrBlocks`. It sets the value of `spec.clusterIP` based on the first address family specified in the Service manifest under `ipFamilies`.




## More information

For more information about how to create dual-stack Services, see [Dual-stack options on new Services](https://kubernetes.io/docs/concepts/services-networking/dual-stack/#dual-stack-options-on-new-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
