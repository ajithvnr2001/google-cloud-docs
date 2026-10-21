---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manual-load-balance/
title: Enabling manual load balancing mode \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:51.619506+00:00
---

# Enabling manual load balancing mode  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manual-load-balance/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Enabling manual load balancing mode Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/manual-load-balance)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/manual-load-balance)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud clusters can run with one of three load balancing modes: integrated, bundled, or manual.

  * With integrated mode, Google Distributed Cloud uses the F5 BIG-IP load balancer.

  * With bundled mode, Google Distributed Cloud provides and manages the load balancer. You don't have to get a license for a load balancer, and the amount of setup that you have to do is minimal.

  * With manual mode, Google Distributed Cloud uses a load balancer of your choice. Manual load balancing mode requires that you do more configuration than with integrated mode. The [Citrix load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/citrix-load-balance) is an example load balancer that you could use with manual load balancing mode.




Manual load balancing is supported for the following cluster types:

  * User clusters that have Controlplane V2 enabled. With Controlplane V2, the control-plane nodes for a user cluster are in the user cluster itself.

  * User clusters that use kubeception. The term _kubeception_ refers to the case where the control plane for a user cluster runs on one or more nodes in the admin cluster. If Controlplane V2 _isn't_ enabled, a user cluster uses kubeception.

  * High availability (HA) admin clusters and non-HA admin clusters.




This page describes the steps you need to take if you choose to use the manual load balancing mode.

In this topic, you set aside IP addresses for your cluster nodes for later use. You also set aside IP addresses for virtual IPs (VIPs) and decide on `nodePort` values. The idea is that you choose the IP addresses and `nodePort` values that you want to use and then record them in a spreadsheet or some other tool. When you are ready to create your clusters, you will need the IP addresses and `nodePort` values to fill in the configuration files for your [admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file) and your [user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file) and the [IP block files](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) for your clusters.

You will also need the IP addresses and `nodePort` values when you manually configure your load balancer.

## Setting aside node IP addresses

With manual load balancing mode, you cannot use DHCP. You must specify static IP addresses for your cluster nodes. You need to set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. For details about how many node IP addresses to set aside, see [Plan your IP addresses (Controlplane V2)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses) and [Plan your IP addresses (kubeception)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses-kubeception).

### Configure IP addresses

Where you configure the static IP addresses that you have set aside depends on the cluster type and whether Controlplane V2 is enabled on your user clusters.

### HA admin cluster

The following table describes what the IP addresses are for and where you configure them for HA admin clusters.

**Static IPs** | **Configuration**  
---|---  
Control plane nodes | Admin cluster configuration file in the `network.controlPlaneIPBlock.ips` section  
Add-on nodes | [Admin cluster IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file  
  
### Non-HA admin cluster

The following table describes what the IP addresses are for and where you configure them for non-HA admin clusters.

**Static IPs** | **Configuration**  
---|---  
Control plane node | [Admin cluster IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file  
Add-on nodes | Admin cluster IP block file  
  
### CP V2 user cluster

The following table describes what the IP addresses are for and where you configure them for user clusters with Controlplane V2 enabled.

**Static IPs** | **Configuration**  
---|---  
control plane nodes | User cluster configuration file in the `network.controlPlaneIPBlock.ips` section  
Worker nodes | [User cluster IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the user cluster configuration file  
  
### Kubeception user cluster

The following table describes what the IP addresses are for and where you configure them for user clusters that use kubeception.

**Static IPs** | **Configuration**  
---|---  
control plane nodes | [Admin cluster IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file  
Worker nodes | [User cluster IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the user cluster configuration file  
  
## Setting aside IP addresses for VIPs

Regardless of whether you use integrated, bundled or manual load balancing mode, you must set aside several IP addresses that you intend to use for virtual IPs (VIPs) for load balancing. These VIPs allow external clients to reach the Kubernetes API servers and your ingress service on user clusters.

### Configure VIPs

Where you configure VIPs depends on the cluster type.

### HA admin cluster

The following table describes what the VIP is for and where you configure it for HA admin clusters.

**VIP** | **Configuration**  
---|---  
VIP for the Kubernetes API server of the admin cluster | Admin cluster configuration file in the `loadBalancer.vips.controlPlaneVIP` field  
VIP for add-on nodes | Admin cluster configuration file in the `loadBalancer.vips.addonsVIP` field  
  
### Non-HA admin cluster

The following table describes what the VIP is for and where you configure it for non-HA admin clusters.

**VIP** | **Configuration**  
---|---  
VIP for the Kubernetes API server of the admin cluster | Admin cluster configuration file in the `loadBalancer.vips.controlPlaneVIP` field  
VIP for add-on nodes | Admin cluster configuration file in the `loadBalancer.vips.addonsVIP` field  
  
### CP V2 user cluster

The following table describes what the VIPs are for and where you configure them for user clusters with Controlplane V2 enabled.

**VIPs** | **Configuration**  
---|---  
VIP for the Kubernetes API server of the user cluster | User cluster configuration file in the `loadBalancer.vips.controlPlaneVIP` field  
VIP for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.vips.ingressVIP` field  
  
### Kubeception user cluster

The following table describes what the VIPs are for and where you configure them for user clusters that use kubeception.

**VIPs** | **Configuration**  
---|---  
VIP for the Kubernetes API server of the user cluster | User cluster configuration file in the `loadBalancer.vips.controlPlaneVIP` field  
VIP for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.vips.ingressVIP` field  
  
## Setting aside `nodePort` values

In Google Distributed Cloud, the Kubernetes API server and the ingress service are exposed by [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service). With manual load balancing mode, you must choose your own `nodePort` values for these Services. Choose values in the 30000 - 32767 range.

### Configure `nodePort` values

Where you configure `nodePort` values depends on whether the user cluster has ControlPlane V2 enabled.

### HA admin cluster

The following table describes what the `nodePort` is for and where you configure it for HA admin clusters.

**`nodePort`** | **Configuration**  
---|---  
`nodePort` for add-on nodes | Admin cluster configuration file in the `loadBalancer.manualLB.addonsNodePort` field  
  
### Non-HA admin cluster

The following table describes what the `nodePort` values are for and where you configure them for non-HA admin clusters.

**`nodePort`** | **Configuration**  
---|---  
`nodePort` for the Kubernetes API server of the admin cluster | Admin cluster configuration file in the `loadBalancer.vips.controlPlaneNodePort` field  
`nodePort` for add-on nodes | Admin cluster configuration file in the `loadBalancer.manualLB.addonsNodePort` field  
  
### CP V2 user cluster

The following table describes what the `nodePorts` are for and where you configure them for user clusters with Controlplane V2 enabled.

**`nodePorts`** | **Configuration**  
---|---  
HTTP `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPNodePort`  
HTTPS `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPSNodePort`  
  
You don't need to configure a `nodePort` for the control plane VIP because Google Distributed Cloud handles load balancing to the control plane nodes for user clusters with Controlplane V2 enabled.

### Kubeception user cluster

The following table describes what the `nodePort` values are for and where you configure them for user clusters that use kubeception.

**`nodePort`** | **Configuration**  
---|---  
`nodePort` for the Kubernetes API server of the user cluster | User cluster configuration file in the `loadBalancer.manualLB.controlPlaneNodePort` field  
`nodePort` for the Konnectivity server of the user cluster (the Konnectivity server uses the control plane VIP) | User cluster configuration file in the `loadBalancer.manualLB.konnectivityServerNodePort` field  
HTTP `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPNodePort`  
HTTPS `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPSNodePort`  
  
### Example cluster configuration file

The following example shows a portion of an admin and user cluster configuration file:

### HA admin cluster
    
    
    network:
      controlPlaneIPBlock:
        netmask: "255.255.248.0"
        gateway: "21.0.143.254"
        ips:
        - ip: "21.0.140.226"
          hostname: "admin-cp-vm-1"
        - ip: "21.0.141.48"
          hostname: "admin-cp-vm-2"
        - ip: "21.0.141.65"
          hostname: "admin-cp-vm-3"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.21.40"
      kind: ManualLB
      manualLB:
        addonsNodePort: 31405
    

### Non-HA admin cluster
    
    
    network:
      ipMode:
        type: static
        ipBlockFilePath: "ipblock-admin.yaml"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.21.40"
        addonsVIP: "172.16.21.41"
      kind: ManualLB
      manualLB:
        controlPlaneNodePort: 30562
        addonsNodePort: 30563
    

### CP V2 user cluster
    
    
    network:
      ipMode:
        type: static
        ipBlockFilePath: "ipblock1.yaml"
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
        gateway: "172.16.21.1"
        ips:
        - ip: "172.16.21.6"
          hostname: "cp-vm-1"
        - ip: "172.16.21.7"
          hostname: "cp-vm-2"
        - ip: "172.16.21.8"
          hostname: "cp-vm-3"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.21.40"
        ingressVIP: "172.16.21.30"
      kind: ManualLB
      manualLB:
        ingressHTTPNodePort: 30243
        ingressHTTPSNodePort: 30879
    

### Kubeception user cluster
    
    
    network:
      ipMode:
        type: static
        ipBlockFilePath: "ipblock1.yaml"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.21.40"
        ingressVIP: "172.16.21.30"
      kind: ManualLB
      manualLB:
        ingressHTTPNodePort: 30243
        ingressHTTPSNodePort: 30879
        konnectivityServerNodePort: 30563
        controlPlaneNodePort: 30562
    

## Configure your load balancer

Use your load balancer's management console or tools to configure the following mappings in your load balancer. How you do this depends on your load balancer.

### HA admin cluster

#### Control plane traffic

Google Distributed Cloud automatically handles load balancing for HA admin cluster control plane traffic. Although you don't need to configure a mapping in the load balancer, you must specify an IP address in the `loadBalancer.vips.controlPlaneVIP` field.

#### Traffic to services in the add-on nodes

The following shows the mapping to the IP addresses and `nodePort` values for traffic to services in add-on nodes:

  * (`addonsVIP`:8443) -> (NODE_IP_ADDRESSES:`addonsNodePort`)



Add this mapping for all nodes in the admin cluster, both the control plane nodes and the add-on nodes.

### Non-HA admin cluster

#### Control plane traffic

The following shows the mapping to the IP address and `nodePort` value for the control plane node:

  * (`controlPlaneVIP`:443) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)



Add this mapping for all nodes in the admin cluster, both the control plane node and the add-on nodes.

#### Traffic to services in the add-on nodes

The following shows the mapping to the IP addresses and `nodePort` values for services running in add-on nodes:

  * (`addonsVIP`:8443) -> (NODE_IP_ADDRESSES:`addonsNodePort`)



Add this mapping for all nodes in the admin cluster, both the control plane node and the add-on nodes.

### CP V2 user cluster

#### Control plane traffic

Google Distributed Cloud automatically handles load balancing of the control plane traffic for user clusters with Controlplane V2 enabled. Although you don't need to configure a mapping in the load balancer, you must specify an IP address in the `loadBalancer.vips.controlPlaneVIP` field.

#### Data plane traffic

The following shows the mapping to the IP addresses and `nodePort` values for data plane traffic:

  * (`ingressVIP`:`80`) -> (NODE_IP_ADDRESSES:`ingressHTTPNodePort`)
  * (`ingressVIP`:`443`) -> (NODE_IP_ADDRESSES:`ingressHTTPSNodePort`)



Add these mappings for all nodes in the user cluster, both control plane nodes and worker nodes. Because you configured NodePorts on the cluster, Kubernetes opens the NodePorts on all cluster nodes. This lets any node in the cluster handle data plane traffic.

After you configure the mappings, the load balancer listens for traffic on the IP address that you configured for the user cluster's ingress VIP on standard HTTP and HTTPS ports. The load balancer routes requests to any node in the cluster. After a request is routed to one of the cluster nodes, internal Kubernetes networking takes over and routes the request to the destination Pod.

### Kubeception user cluster

#### Control plane traffic

The following shows the mapping to the IP addresses and `nodePort` values for control plane traffic:

  * (`controlPlaneVIP`:`443`) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)
  * (`controlPlaneVIP`:`8132`) -> (NODE_IP_ADDRESSES:`konnectivityServerNodePort`)



Add this mapping for all nodes in the _admin_ cluster, both the admin cluster and the user cluster control plane nodes and add-on nodes.

#### Data plane traffic

The following shows the mapping to the IP addresses and `nodePort` values for data plane traffic:

  * (`ingressVIP`:`80`) -> (NODE_IP_ADDRESSES:`ingressHTTPNodePort`)
  * (`ingressVIP`:`443`) -> (NODE_IP_ADDRESSES:`ingressHTTPSNodePort`)



Add these mappings for all nodes in the user cluster. With user clusters using kubeception, all nodes in the cluster are worker nodes.

**Note:** The healthcheck to `ingressVIP` will fail until you configure at least one ingress.

### Resetting connections to failed nodes (Recommended)

In addition to the preceding requirements, we recommend you configure the load balancer to reset client connections when it detects a backend node failure. Without this configuration, clients of the Kubernetes API server can stop responding for several minutes when a server instance goes down, which can cause instability in the Kubernetes control plane.

  * With F5 BIG-IP, this setting is called Action On Service Down in the backend pool configuration page.
  * With HAProxy, this setting is called on-marked-down shutdown-sessions in the backend server configuration.
  * If you are using a different load balancer, you should consult the documentation to find the equivalent setting.



## Getting support for manual load balancing

Google does not provide support for load balancers configured using manual load balancing mode. If you encounter issues with the load balancer, reach out to the load balancer's vendor.

## What's next

  * [Load balancing with Citrix](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/citrix-load-balance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
