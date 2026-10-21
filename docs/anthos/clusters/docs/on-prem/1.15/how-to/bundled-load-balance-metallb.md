---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb/
title: Bundled load balancing with MetalLB \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:51.262732+00:00
---

# Bundled load balancing with MetalLB  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Bundled load balancing with MetalLB Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/bundled-load-balance-metallb)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance-metallb)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to configure Google Distributed Cloud to use bundled load balancing with the [MetalLB load balancer](https://metallb.universe.tf/).

In Google Distributed Cloud, MetalLB runs in [layer-2 mode](https://metallb.universe.tf/concepts/layer2/).

## Example of a MetalLB configuration

Here is an example of a configuration for clusters running the MetalLB load balancer:

[ ![MetalLB load balancer configuration.](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/images/metallb-network.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/images/metallb-network.svg) MetalLB load balancer configuration (Click to enlarge)

The preceding diagram shows a MetalLB deployment. MetalLB runs directly on the cluster nodes. In this example, the admin cluster and user cluster are on two separate VLANs, and each cluster is in a separate subnet:

Cluster | Subnet  
---|---  
Admin cluster | 172.16.20.0/24  
User cluster | 172.16.40.0/24  
  
### admin-cluster.yaml

The following example of an admin cluster configuration file shows the configuration seen in the preceding diagram of:

  * MetalLB load balancer

  * VIPs on MetalLB for Kubernetes API server and add-ons of the admin cluster



    
    
    network:
      hostConfig:
      ...
    
      ipMode:
        type: "static"
        ipBlockFilePath: "config-folder/admin-cluster-ipblock.yaml"
    ...
    
    loadBalancer:
      kind: "MetalLB"
      ...
    
      vips:
        controlPlaneVIP: "172.16.20.100"
        addonsVIP: "172.16.20.101"
    

### admin-cluster-ipblock.yaml

The following example of an IP block file shows the designation of IP addresses for the nodes in the admin cluster. This also includes the address for the control-plane node for the user cluster and an IP address to use during cluster upgrade.
    
    
    blocks:
    - netmask: "255.255.255.0"
      gateway: "17.16.20.1"
      ips:
      - ip: 172.16.20.50
        hostname: admin-vm-1
      - ip: 172.16.20.51
        hostname: admin-vm-2
      - ip: 172.16.20.52
        hostname: admin-vm-3
      - ip: 172.16.20.53
        hostname: admin-vm-4
      - ip: 172.16.20.54
        hostname: admin-vm-5
    

### user-cluster.yaml

The following example of a user cluster configuration file shows the configuration of:

  * Address pools for the MetalLB controller to choose from and assign to Services of type `LoadBalancer`. The ingress VIP is in one of these pools.

  * VIP designated for the Kubernetes API server of the user cluster, and the ingress VIP you have chosen to configure for the ingress proxy. The Kubernetes API server VIP is on the admin cluster subnet because the control plane for a user cluster runs on a node in the admin cluster.

  * A node pool enabled to use MetalLB. MetalLB will be deployed on the nodes in the user cluster that belong to that node pool.



    
    
    network:
      hostConfig:
      ...
    
      ipMode:
        type: "static"
        ipBlockFilePath: "config-folder/user-cluster-ipblock.yaml"
    ...
    
    loadBalancer:
      kind: MetalLB
      metalLB:
        addressPools:
        - name: "address-pool-1"
          addresses:
          - "172.16.40.100/32"
          - "172.16.40.101-172.16.40.112
          avoidBuggyIPs: true
      ...
    
      vips:
        controlPlaneVIP: "172.16.20.102"
        ingressVIP: "172.16.40.102"
    ...
    
    nodePools:
    - name: "node-pool-1"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      enableLoadBalancer: true
    

The configuration in the preceding example specifies a set of addresses available for Services. When an application developer creates a Service of type `LoadBalancer` in the user cluster, the MetalLB controller will choose an IP address from this pool.

### user-cluster-ipblock.yaml

The following example of an IP block file shows the designation of IP addresses for the nodes in the user cluster. This includes an IP address to use during cluster upgrade.
    
    
    blocks:
    - netmask: "255.255.255.0"
      gateway: "17.16.40.1"
      ips:
      - ip: 172.16.40.21
        hostname: user-vm-1
      - ip: 172.16.40.22
        hostname: user-vm-2
      - ip: 172.16.40.23
        hostname: user-vm-3
      - ip: 172.16.40.24
        hostname: user-vm-4
      - ip: 172.16.40.25
        hostname: user-vm-5
    

## Set up MetalLB

### Open firewall ports

MetalLB uses the [Go memberlist library](https://pkg.go.dev/github.com/hashicorp/memberlist) to do leader election. The `memberlist` library uses TCP port 7946 and UDP port 7946 to exchange information. Make sure those ports are accessible for incoming and outgoing traffic on all load-balancer nodes.

### Enable MetalLB for a new admin cluster

In your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#loadbalancerkind), set `loadBalancer.kind` to `"MetalLB"`.
    
    
    loadBalancer:
      kind: "MetalLB"
    

Fill in the rest of your admin cluster configuration file, and create your admin cluster as described in [Create an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-cluster).

### Specify address pools

The MetalLB controller does IP address management for Services. So when an application developer creates a Service of type LoadBalancer in a user cluster, they don't have to manually specify an IP address for the Service. Instead, the MetalLB controller chooses an IP address from an address pool that you specify at cluster creation time.

Think about how many Services of type LoadBalancer are likely to be active in your user cluster at any given time. Then in the [`loadBalancer.metalLB.addressPools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-metallb-section) section of your user cluster configuration file, specify enough IP addresses to accommodate those Services.

The [ingress VIP](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-vips-ingressvip-field) for your user cluster must be among the addresses that you specify in an address pool. This is because the [ingress proxy](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-service-ingress) is exposed by a Service of type LoadBalancer.

If your application developers have no need to create Services of type LoadBalancer, then you don't have to specify any addresses other than the ingress VIP.

Addresses must be in CIDR format or range format. If you want to specify an individual address, use a /32 CIDR. For example:
    
    
    addresses:
      - "192.0.2.0/26"
      - "192.0.2.64-192.0.2.72"
      - "192.0.2.75/32
    

If you need to adjust the addresses in a pool after the cluster is created, you can use `gkectl update cluster`. For more information, see Update MetalLB.

### Enable MetalLB for a new user cluster

In your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-kind-field):

  * Set `loadBalancer.kind` to `"MetalLB"`.
  * Specify one or more address pools for Services. The ingress VIP must be in one of these pools.
  * Set `enableLoadBalancer` to `true` for at least one node pool in your cluster.



Fill in the rest of your user cluster configuration file, and create your user cluster as described in [Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster).

### Manual assignment of Service addresses

If you do not want the MetalLB controller to automatically assign IP addresses from a particular pool to Services, set the `manualAssign` field of the pool to `true`. Then a developer can create a Service of type `LoadBalancer` and manually specify one of the addresses from the pool. For example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-2"
          addresses:
          - "192.0.2.73-192.0.2.80"
          manualAssign: true
    

### Avoiding buggy IP addresses

If you set the `avoidBuggyIPs` field of an address pool to `true`, the MetalLB controller will not use addresses from the pool that end in .0 or .255. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses. For example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
          addresses:
          - "192.0.2.0/24"
          avoidBuggyIPs: true
    

### Create a Service of type LoadBalancer

Here are two manifests: one for a Deployment and one for a Service:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
    spec:
      selector:
        matchLabels:
          greeting: hello
      replicas: 3
      template:
        metadata:
          labels:
            greeting: hello
        spec:
          containers:
          - name: hello
            image: gcr.io/google-samples/hello-app:2.0
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
    spec:
      type: LoadBalancer
      selector:
        greeting: hello
      ports:
      - name: metal-lb-example-port
        protocol: TCP
        port: 60000
        targetPort: 8080
    

Notice that the Service manifest does not specify an external IP address. The MetalLB controller will choose an external IP address from the address pool you specified in the user cluster configuration file.

Save the manifests in a file named `my-dep-svc.yaml`. Then create the Deployment and Service objects:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f my-dep-svc.yaml
    

View the Service:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONIFG get service my-service --output wide
    

The output shows the external IP address that was automatically assigned to the Service. For example:
    
    
    NAME         TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)           AGE   SELECTOR
    my-service   LoadBalancer   10.96.2.166   192.0.2.2   60000:31914/TCP   28s
    

Verify that the assigned external IP address was taken from the address pool you specified in your user cluster configuration file. For example, 192.0.2.2 is in this address pool:
    
    
    metalLB:
      addressPools:
      - name: "address-pool-1"
        addresses:
         - "192.0.2.0/24"
         - "198.51.100.1-198.51.100.3"
    

Call the Service:
    
    
    curl EXTERNAL_IP_ADDRESS:60000
    

The output displays a `Hello, world!` message:
    
    
    Hello, world!
    Version: 2.0.0
    

## Update MetalLB

After you create your cluster, you can update the MetalLB address pools and the `enableLoadBalancer` field in your node pools. Make the desired changes in the user cluster configuration file, and then call `gkectl update cluster`:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONIFG --config USER_CLUSTER_CONFIG
    

## MetalLB Pods and ConfigMap

The MetalLB controller runs as a Deployment, and the MetalLB speaker runs as a DaemonSet on nodes in pools that have `enableLoadBalancer` set to `true`. The MetalLB controller manages the IP addresses assigned to Services. The MetalLB speaker does leader election and announces Service VIPs.

View all MetalLB Pods:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONIFG get pods --namespace kube-system --selector app=metallb
    

You can use the logs from the MetalLB Pods for troubleshooting.

MetalLB configuration is stored in a ConfigMap in a format known by MetalLB. Do not change the ConfigMap directly. Instead, use `gkectl update cluster` as described previously. To view the ConfigMap for troubleshooting:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONIFG get configmap metallb-config --namespace kube-system
    

## Benefits of using MetalLB

  * MetalLB runs directly on your cluster nodes, so it doesn't require extra VMs.

  * The MetalLB controller does IP address management for Services, so you don't have to manually choose an IP address for each Service.

  * Active instances of MetalLB for different Services can run on different nodes.

  * You can [share an IP address](https://metallb.universe.tf/usage/#ip-address-sharing) among different Services.




## MetalLB compared to F5 BIG-IP and Seesaw

  * VIPs must be in the same subnet as the cluster nodes. This is also a requirement for Seesaw, but not for F5 BIG-IP.

  * There are no metrics for traffic.

  * There is no hitless failover; existing connections are reset during failover.

  * External traffic to the Pods of a particular Service passes through a single node running the MetalLB speaker. This means that the client IP address is usually not visible to containers running in the Pod.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
