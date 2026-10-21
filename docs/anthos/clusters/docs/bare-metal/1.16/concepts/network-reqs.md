---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs/
title: Network requirements \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:10.805621+00:00
---

# Network requirements  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Network requirements Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/concepts/network-reqs)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document outlines the networking requirements for installing and operating Google Distributed Cloud.

## External network requirements

Google Distributed Cloud requires an internet connection for operational purposes. Google Distributed Cloud retrieves cluster components from [Container Registry](https://docs.cloud.google.com/container-registry/docs), and the cluster is registered with [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview).

You can connect to Google by using the public internet through HTTPS, a virtual private network (VPN), or a [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) connection.

If the machines you are using for your admin workstation and cluster nodes use a proxy server to access the internet, your proxy server must allow some specific connections. For details, see the prerequisites section of [Install behind a proxy](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/proxy#prerequisites).

## Internal network requirements

Google Distributed Cloud can work with [Layer 2](https://wikipedia.org/wiki/OSI_model#Layer_2:_Data_Link_Layer) or [Layer 3](https://wikipedia.org/wiki/OSI_model#Layer_3:_Network_Layer) connectivity between cluster nodes. The load balancer nodes can be the control plane nodes or a dedicated set of nodes. For more information, see [Choosing and configuring load balancers](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/load-balance).

When you use [Bundled Layer 2 load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb) (`spec.loadBalancer.mode: bundled` and `spec.loadBalancer.type: layer2`), load balancer nodes require Layer 2 adjacency. The Layer 2 adjacency requirement applies whether you run the load balancer on control plane nodes or in a dedicated set of load balancing nodes. [Bundled load balancing with BGP](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp) supports Layer 3 protocol, so strict Layer 2 adjacency isn't required.

The requirements for load balancer machines are as follows:

  * For Bundled Layer 2 load balancing, all load balancers for a given cluster are in the same Layer 2 domain. Control plane nodes must also be in the same Layer 2 domain.
  * For Bundled Layer 2 load balancing, all virtual IP addresses (VIPs) must be in the load balancer machine subnet and routable to the gateway of the subnet.
  * Users are responsible for allowing ingress load balancer traffic.



## Pod networking

Google Distributed Cloud 1.7.0 and later versions allows you to configure up to 250 pods per node. Kubernetes assigns a [Classless Inter-Domain Routing (CIDR) block](https://tools.ietf.org/html/rfc1918) to each node so that each pod can have a unique IP address. The size of the CIDR block corresponds to the maximum number of pods per node. The following table lists the size of the CIDR block that Kubernetes assigns to each node based on the configured maximum pods per node:

Maximum pods per node | CIDR block per node | Number of IP addresses  
---|---|---  
32 | /26 | 64  
33 – 64 | /25 | 128  
65 – 128 | /24 | 256  
129 - 250 | /23 | 512  
  
Running 250 pods per node requires Kubernetes to reserve a `/23` CIDR block for each node. Assuming that your cluster uses the default value of `/16` for the `clusterNetwork.pods.cidrBlocks` field, your cluster has a limit of (2(23-16))=128 nodes. If you intend to grow the cluster beyond this limit, you can either increase the value of `clusterNetwork.pods.cidrBlocks` or decrease the value of `nodeConfig.podDensity.maxPodsPerNode`. This method had a few disadvantages. 

## Single user cluster deployment with high availability

The following diagram illustrates a number of key networking concepts for Distributed Cloud in one possible network configuration.

![Google Distributed Cloud typical network configuration](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/sc-cp-lb-ga.svg)

Consider the following information to meet the network requirements:

  * The control plane nodes run the load balancers, and they all have Layer 2 connectivity, while other connections, including worker nodes, only require Layer 3 connectivity.
  * Configuration files define IP addresses for worker node pools. Configuration files also define VIPs for the following purposes: 
    * Services
    * Ingress
    * Control plane access through the Kubernetes API
  * You require a connection to Google Cloud.



## Port usage

This section shows how UDP and TCP ports are used on cluster and load balancer nodes.

### Control plane nodes

Protocol| Direction| Port range| Purpose| Used by  
---|---|---|---|---  
UDP| Inbound| 6081| GENEVE Encapsulation| Self  
TCP| Inbound| 22| Provisioning and updates of admin cluster nodes| Admin workstation  
TCP| Inbound| 6444| Kubernetes API server| All  
TCP| Inbound| 2379 - 2381| etcd server client API| `kube-apiserver` and `etcd`  
TCP| Inbound| 2382 - 2384| etcd-events server client API| `kube-apiserver` and `etcd-events`  
TCP| Inbound| 10250| `kubelet` API| Self and control plane  
TCP| Inbound| 10251| `kube-scheduler`| Self  
TCP| Inbound| 10252| `kube-controller-manager`| Self  
TCP| Inbound| 10256| Node health check| All  
TCP| Both| 4240| CNI health check| All  
  
### Worker nodes

Protocol| Direction| Port range| Purpose| Used by  
---|---|---|---|---  
TCP| Inbound| 22| Provisioning and updates of user cluster nodes| Admin cluster nodes  
UDP| Inbound| 6081| GENEVE Encapsulation| Self  
TCP| Inbound| 10250| `kubelet` API| Self and control plane  
TCP| Inbound| 10256| Node health check| All  
TCP| Inbound| 30000 - 32767| `NodePort` services| Self  
TCP| Both| 4240| CNI health check| All  
  
### Load balancer nodes

Protocol| Direction| Port range| Purpose| Used by  
---|---|---|---|---  
TCP| Inbound| 22| Provisioning and updates of user cluster nodes| Admin cluster nodes  
UDP| Inbound| 6081| GENEVE Encapsulation| Self  
TCP| Inbound| 443*| Cluster management| All  
TCP| Both| 4240| CNI health check| All  
TCP| Inbound| 7946| Metal LB health check| load balancer nodes  
UDP| Inbound| 7946| Metal LB health check| load balancer nodes  
TCP| Inbound| 10256| Node health check| All  
  
* This port can be configured in the cluster config, using the `controlPlaneLBPort` field.

### Multi-cluster port requirements

In a multi-cluster configuration, added clusters must include the following ports to communicate with the admin cluster.

Protocol| Direction| Port range| Purpose| Used by  
---|---|---|---|---  
TCP| Inbound| 22| Provisioning and updates of cluster nodes| All nodes  
TCP| Inbound| 443*| Kubernetes API server for added cluster| Control plane and load balancer nodes  
  
* This port can be configured in the cluster config, using the `controlPlaneLBPort` field.

## Configure firewalld ports

You are not required to disable firewalld to run Google Distributed Cloud on Red Hat Enterprise Linux (RHEL) or CentOS. To use firewalld, you must open the UDP and TCP ports used by control plane, worker, and load balancer nodes as described in Port usage on this page. The following example configurations show how you can open ports with `firewall-cmd`, the firewalld command-line utility. You should run the commands as the root user.

### Control plane node example configuration

The following block of commands shows an example of how you can open the needed ports on servers running control plane nodes:
    
    
    firewall-cmd --permanent --zone=public --add-port=22/tcp
    firewall-cmd --permanent --zone=public --add-port=4240/tcp
    firewall-cmd --permanent --zone=public --add-port=6444/tcp
    firewall-cmd --permanent --zone=public --add-port=6081/udp
    firewall-cmd --permanent --zone=public --add-port=10250-10252/tcp
    firewall-cmd --permanent --zone=public --add-port=10256/tcp
    firewall-cmd --permanent --zone=public --add-port=2379-2380/tcp
    firewall-cmd --permanent --zone=public --add-port=443/tcp
    firewall-cmd --permanent --zone=public --add-port=30000-32767/tcp
    firewall-cmd --permanent --new-zone=k8s-pods
    firewall-cmd --permanent --zone=k8s-pods --add-source PODS_CIDR
    firewall-cmd --permanent --zone=k8s-pods --set-target=ACCEPT
    firewall-cmd --reload
    

Replace `PODS_CIDR` with the CIDR blocks reserved for your pods configured in the `clusterNetwork.pods.cidrBlocks` field. The default CIDR block for pods is `192.168.0.0/16`.

### Worker node example configuration

The following block of commands shows an example of how you can open the needed ports on servers running worker nodes:
    
    
    firewall-cmd --permanent --zone=public --add-port=22/tcp
    firewall-cmd --permanent --zone=public --add-port=4240/tcp
    firewall-cmd --permanent --zone=public --add-port=6444/tcp
    firewall-cmd --permanent --zone=public --add-port=6081/udp
    firewall-cmd --permanent --zone=public --add-port=10250/tcp
    firewall-cmd --permanent --zone=public --add-port=10256/tcp
    firewall-cmd --permanent --zone=public --add-port=443/tcp
    firewall-cmd --permanent --zone=public --add-port=30000-32767/tcp
    firewall-cmd --permanent --new-zone=k8s-pods
    firewall-cmd --permanent --zone=k8s-pods --add-source PODS_CIDR
    firewall-cmd --permanent --zone=k8s-pods --set-target=ACCEPT
    firewall-cmd --reload
    

Replace `PODS_CIDR` with the CIDR blocks reserved for your pods configured in the `clusterNetwork.pods.cidrBlocks` field. The default CIDR block for pods is `192.168.0.0/16`.

### Load balancer node example configuration

The following block of commands shows an example of how you can open the needed ports on servers running load balancer nodes:
    
    
    firewall-cmd --permanent --zone=public --add-port=22/tcp
    firewall-cmd --permanent --zone=public --add-port=4240/tcp
    firewall-cmd --permanent --zone=public --add-port=6444/tcp
    firewall-cmd --permanent --zone=public --add-port=7946/tcp
    firewall-cmd --permanent --zone=public --add-port=7946/udp
    firewall-cmd --permanent --zone=public --add-port=6081/udp
    firewall-cmd --permanent --zone=public --add-port=10250/tcp
    firewall-cmd --permanent --zone=public --add-port=10256/tcp
    firewall-cmd --permanent --zone=public --add-port=443/tcp
    firewall-cmd --permanent --zone=public --add-port=30000-32767/tcp
    firewall-cmd --permanent --new-zone=k8s-pods
    firewall-cmd --permanent --zone=k8s-pods --add-source PODS_CIDR
    firewall-cmd --permanent --zone=k8s-pods --set-target=ACCEPT
    firewall-cmd --reload
    

Replace `PODS_CIDR` with the CIDR blocks reserved for your pods configured in the `clusterNetwork.pods.cidrBlocks` field. The default CIDR block for pods is `192.168.0.0/16`.

### Confirm your port configuration

To verify your port configuration, use the following steps on control plane, worker, and load balancer nodes:

  1. Run the following Network Mapper command to see what ports are open:
         
         nmap localhost
         

  2. Run the following commands to get your firewalld configuration settings:
         
         firewall-cmd --zone=public --list-all-policies
         firewall-cmd --zone=public --list-ports
         firewall-cmd --zone=public --list-services
         firewall-cmd --zone=k8s-pods --list-all-policies
         firewall-cmd --zone=k8s-pods --list-ports
         firewall-cmd --zone=k8s-pods --list-services
         

  3. If necessary, rerun the commands from the preceding sections to configure your nodes properly. You may need to run the commands as the root user.




### Known issue for firewalld

When running Google Distributed Cloud with `firewalld` enabled on either CentOS or Red Hat Enterprise Linux (RHEL), changes to `firewalld` can remove the Cilium `iptables` chains on the host network. The `iptables` chains are added by the `anetd` Pod when it's started. The loss of the Cilium `iptables` chains causes the Pod on the Node to lose network connectivity outside of the Node.

Changes to `firewalld` that remove the `iptables` chains include, but aren't limited to:

  * Restarting `firewalld`, using `systemctl`

  * Reloading `firewalld` with the command line client (`firewall-cmd --reload`)




To apply `firewalld` changes without removing `iptables` chains, restart `anetd` on the Node:

  1. Locate and delete the `anetd` Pod with the following commands to restart `anetd`:
         
         kubectl get pods -n kube-system kubectl delete pods -n kube-system ANETD_XYZ
         

Replace ANETD_XYZ with the name of the `anetd` Pod.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
