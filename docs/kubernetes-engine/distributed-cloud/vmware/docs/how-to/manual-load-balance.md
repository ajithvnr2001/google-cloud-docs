---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance/
title: Enabling manual load balancing mode \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:45.157764+00:00
---

# Enabling manual load balancing mode  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Enabling manual load balancing mode Stay organized with collections  Save and categorize content based on your preferences. 

We recommend that you configure one of the following load balancing modes:

  * With bundled mode, Google Distributed Cloud provides and manages the load balancer. You don't have to get a license for a load balancer, and the amount of setup that you have to do is minimal.

  * With manual mode, Google Distributed Cloud uses a load balancer of your choice, such as F5 BIG-IP or Citrix. Manual load balancing mode requires that you do more configuration than with bundled mode.




Manual load balancing is supported for the following cluster types:

  * User clusters that have Controlplane V2 enabled. With Controlplane V2, the control-plane nodes for a user cluster are in the user cluster itself.

  * User clusters that use kubeception. The term _kubeception_ refers to the case where the control plane for a user cluster runs on one or more nodes in the admin cluster. If Controlplane V2 _isn't_ enabled, a user cluster uses kubeception.




This document describes the steps you need to take if you choose to use the manual load balancing mode.

In this document, you set aside IP addresses for control-plane nodes and worker nodes for later use. You also set aside IP addresses for virtual IPs (VIPs) and decide on NodePort values. The idea is that you choose the IP addresses and NodePort values that you want to use and then record them in a spreadsheet or some other tool. When you are ready to create your clusters, you will need the IP addresses and NodePort values to fill in the configuration files for your [admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest) and your [user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest) and the [IP block files](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for your clusters.

You will also need the IP addresses and NodePort values when you manually configure your load balancer for user clusters.

## Configure a different kind of load balancer for the control plane

In version 1.32 and higher when [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) is enabled, you can optionally configure a different kind of load balancer for the control plane when you create a new cluster. For more information, see the following:

  * Admin clusters: [`adminMaster.controlPlaneLoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-control-plane-load-balancer-section)
  * User clusters: [`masterNode.controlPlaneLoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-control-plane-load-balancer-section)



## Setting aside node IP addresses

With manual load balancing mode, you cannot use DHCP. You must specify static IP addresses for your cluster nodes. You need to set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. For details about how many node IP addresses to set aside, see [Plan your IP addresses (Controlplane V2)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses) and [Plan your IP addresses (kubeception)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses-kubeception).

### Configure IP addresses

Where you configure the static IP addresses that you have set aside depends on the cluster type and whether Controlplane V2 is enabled on your user clusters.

### HA admin cluster

The following table describes what the IP addresses are for and where you configure them for HA admin clusters.

**Static IPs** | **Configuration**  
---|---  
Control-plane nodes | If [ the cluster uses topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field), add the IP addresses in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for the admin cluster, and add the path in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file. If the cluster doesn't use topology domains, add the IP addresses in the admin cluster configuration file in the `network.controlPlaneIPBlock.ips` section.  
1.16 and lower: Add-on nodes | [Admin cluster IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file  
  
In version 1.28 and higher, new HA admin clusters don't have add-on nodes, so you don't need to set aside IP addresses for add-on nodes as in previous versions.

### Non-HA admin cluster

The following table describes what the IP addresses are for and where you configure them for non-HA admin clusters.

**Static IPs** | **Configuration**  
---|---  
Control-plane node | [Admin cluster IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file  
Add-on nodes | Admin cluster IP block file  
  
In version 1.28 and higher, all new admin clusters must be high-availability (HA) clusters with 3 control-plane nodes.

### CP V2 user cluster

The following table describes what the IP addresses are for and where you configure them for user clusters with Controlplane V2 enabled.

**Static IPs** | **Configuration**  
---|---  
Control-plane nodes | If [ the cluster uses topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field), add the IP addresses in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for the user cluster, and add the path in the `network.ipMode.ipBlockFilePath` field in the user cluster configuration file If the cluster doesn't use topology domains, add the IP addresses in the user cluster configuration file in the `network.controlPlaneIPBlock.ips` section.  
Worker nodes | [User cluster IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the user cluster configuration file  
  
### Kubeception user cluster

The following table describes what the IP addresses are for and where you configure them for user clusters that use kubeception.

**Static IPs** | **Configuration**  
---|---  
Control-plane nodes | [Admin cluster IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file  
Worker nodes | [User cluster IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) and add the path in the `network.ipMode.ipBlockFilePath` field in the user cluster configuration file  
  
In version 1.30 and higher, Controlplane V2 is required for new user clusters.

## Setting aside IP addresses for VIPs

Regardless of whether you use integrated, bundled or manual load balancing mode, you must set aside several IP addresses that you intend to use for virtual IPs (VIPs) for load balancing. These VIPs allow external clients to reach the Kubernetes API servers and your ingress service on user clusters.

### Configure VIPs

Where you configure VIPs depends on the cluster type.

### HA admin cluster

The following table describes what the VIP is for and where you configure it for HA admin clusters.

**VIP** | **Configuration**  
---|---  
VIP for the Kubernetes API server of the admin cluster | Admin cluster configuration file in the `loadBalancer.vips.controlPlaneVIP` field  
1.15 and lower: Add-ons VIP | Admin cluster configuration file in the `loadBalancer.vips.addonsVIP` field  
  
Note the following differences in versions:

  * In 1.16 and higher, you don't need to configure an add-ons VIP for HA admin clusters.

  * In 1.28 and higher, new HA admin clusters don't have add-on nodes.




### Non-HA admin cluster

The following table describes what the VIP is for and where you configure it for non-HA admin clusters.

**VIP** | **Configuration**  
---|---  
VIP for the Kubernetes API server of the admin cluster | Admin cluster configuration file in the `loadBalancer.vips.controlPlaneVIP` field  
1.15 and lower: Add-ons VIP | Admin cluster configuration file in the `loadBalancer.vips.addonsVIP` field  
  
Note the following differences in versions:

In 1.16 and higher, you don't need to configure an add-ons VIP for non-HA admin clusters.

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
  
## Setting aside NodePort values

In Google Distributed Cloud, the Kubernetes API server and the ingress service are exposed by [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service). With manual load balancing mode, you must choose your own NodePort values for these Services. Choose values in the 30000 - 32767 range.

### Configure NodePort values

Where you configure NodePort values depends on whether the user cluster has ControlPlane V2 enabled.

### HA admin cluster

The following table describes what the NodePort is for and where you configure it for HA admin clusters.

**`nodePort`** | **Configuration**  
---|---  
1.15 and lower: `nodePort` for add-on nodes | Admin cluster configuration file in the `loadBalancer.manualLB.addonsNodePort` field  
  
In version 1.16 and higher, you don't need to configure a NodePort for add-on nodes for HA admin clusters.

### Non-HA admin cluster

The following table describes what the NodePort values are for and where you configure them for non-HA admin clusters.

**`nodePort`** | **Configuration**  
---|---  
1.16 and earlier: `nodePort` for the Kubernetes API server of the admin cluster | 1.15 and earlier: Admin cluster configuration file in the `loadBalancer.vips.controlPlaneNodePort` field  
1.15 and earlier: `nodePort` for add-on nodes | Admin cluster configuration file in the `loadBalancer.manualLB.addonsNodePort` field  
  
In version 1.16 and higher, you don't need to configure a NodePort for add-on nodes for non-HA admin clusters.

### CP V2 user cluster

The following table describes what the NodePorts are for and where you configure them for user clusters with Controlplane V2 enabled. In version 1.30 and higher, you don't need to configure values for the ingress NodePorts.

**`nodePorts`** | **Configuration**  
---|---  
HTTP `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPNodePort`  
HTTPS `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPSNodePort`  
  
### Kubeception user cluster

The following table describes what the NodePort values are for and where you configure them for user clusters that use kubeception.

**`nodePort`** | **Configuration**  
---|---  
`nodePort` for the Kubernetes API server of the user cluster | User cluster configuration file in the `loadBalancer.manualLB.controlPlaneNodePort` field  
`nodePort` for the Konnectivity server of the user cluster (the Konnectivity server uses the control-plane VIP) | User cluster configuration file in the `loadBalancer.manualLB.konnectivityServerNodePort` field  
HTTP `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPNodePort`  
HTTPS `nodePort` for the ingress service in the user cluster | User cluster configuration file in the `loadBalancer.manualLB.ingressHTTPSNodePort`  
  
### Example cluster configuration file

The following example shows a portion of an admin and user cluster configuration file:

### HA admin cluster

  * Version 1.16 and higher:
        
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
        

  * Version 1.15 and earlier require a VIP and NodePort for add-on nodes.
        
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
            addonsVIP: "203.0.113.4"
          kind: ManualLB
          manualLB:
            addonsNodePort: 31405
        




### Non-HA admin cluster

  * Version 1.16 and higher:
        
        network:
          ipMode:
            type: static
            ipBlockFilePath: "ipblock-admin.yaml"
        loadBalancer:
          vips:
            controlPlaneVIP: "172.16.21.40"
          kind: ManualLB
          manualLB:
            controlPlaneNodePort: 30562
        

  * Version 1.15 and lower require a VIP and NodePort for add-on nodes.
        
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

#### Traffic to control-plane nodes

The mapping that you need to configure depends on whether you will [enabled advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) when you create the admin cluster.

  * If advanced clusters isn't enabled: Google Distributed Cloud automatically handles load balancing of the control plane traffic for HA admin clusters. Although you don't need to configure a mapping in the load balancer, you must specify an IP address in the `loadBalancer.vips.controlPlaneVIP` field.

  * If advanced clusters is enabled, you need to configure your load balancer as follows:

    1. Specify an IP address in the `loadBalancer.vips.controlPlaneVIP` field.

    2. Configure the following mapping:

       * (`controlPlaneVIP`:`443`) -> (CONTROL_PLANE_NODE_IP_ADDRESSES:`6433`)
    3. Ensure the backend health check is correctly configured. The health check must use HTTPS and check the `/readyz` endpoint on port `6443`. The health check must verify that this endpoint returns status code `200` to consider the node healthy.




#### Traffic to services in the add-on nodes

1.15 and earlier: The following shows the mapping to the IP addresses and NodePort values for traffic to services in add-on nodes:

  * (`addonsVIP`:8443) -> (NODE_IP_ADDRESSES:`addonsNodePort`)



Add this mapping for all nodes in the admin cluster, both the control-plane nodes and the add-on nodes.

In version 1.16 and higher, you don't need to configure this mapping for add-on nodes for HA admin clusters.

### Non-HA admin cluster

#### Control-plane traffic

The following shows the mapping to the IP address and NodePort value for the control-plane node:

  * (`controlPlaneVIP`:443) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)



Add this mapping for all nodes in the admin cluster, both the control-plane node and the add-on nodes.

#### Traffic to services in the add-on nodes

1.15 and earlier: The following shows the mapping to the IP addresses and NodePort values for services running in add-on nodes:

  * (`addonsVIP`:8443) -> (NODE_IP_ADDRESSES:`addonsNodePort`)



Add this mapping for all nodes in the admin cluster, both the control-plane node and the add-on nodes.

In version 1.16 and higher, you don't need to configure this mapping for add-on nodes for non-HA admin clusters.

### CP V2 user cluster

#### Control-plane traffic

The mapping that you need to configure depends on whether you will [enable advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) when you create the user cluster.

  * If advanced clusters isn't enabled: Google Distributed Cloud automatically handles load balancing of the control plane traffic for user clusters. Although you don't need to configure a mapping in the load balancer, you must specify an IP address in the `loadBalancer.vips.controlPlaneVIP` field.

  * If advanced clusters is enabled, you need to configure your load balancer as follows:

    1. Specify an IP address in the `loadBalancer.vips.controlPlaneVIP` field.

    2. Configure the following mapping:

       * (`controlPlaneVIP`:`443`) -> (CONTROL_PLANE_NODE_IP_ADDRESSES:`6433`)
    3. Ensure the backend health check is correctly configured. The health check must use HTTPS and check the `/readyz` endpoint on port `6443`. The health check must verify that this endpoint returns status code `200` to consider the node healthy.




#### Data plane traffic

The mapping that you need to configure depends on whether you will enable advanced clusters when you create the user cluster.

  * If advanced clusters isn't enabled, do the following steps before the cluster is created:

    1. In your user cluster configuration file, configure `loadBalancer.vips.ingressVIP`, `loadBalancer.manualLB.ingressHTTPNodePort`, and `loadBalancer.manualLB.ingressHTTPSNodePort`.

    2. In your load balancer, configure the IP address to port mappings for each ingress NodePort:

       * (`ingressVIP`:`80`) -> (NODE_IP_ADDRESSES:`ingressHTTPNodePort`)
       * (`ingressVIP`:`443`) -> (NODE_IP_ADDRESSES:`ingressHTTPSNodePort`)
  * If advanced clusters is enabled, do the following steps:

    1. Before the cluster is created, configure `loadBalancer.vips.ingressVIP` in your user cluster configuration file. You don't need to configure values for each ingress NodePort because they have no effect when advanced clusters is enabled.

    2. After the cluster is created, retrieve the values for each ingress NodePort:
           
           kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n gke-system get service istio-ingress -oyaml
           

Look for HTTP and HTTPS from the ports section in the Service spec and write down the NodePort values.

    3. In your load balancer, configure the IP address to port mappings for each ingress NodePort:

       * (`ingressVIP`:`80`) -> (NODE_IP_ADDRESSES:`ingressHTTPNodePort`)
       * (`ingressVIP`:`443`) -> (NODE_IP_ADDRESSES:`ingressHTTPSNodePort`)

In both cases, add these mappings for all control-plane nodes and worker nodes in the user cluster. Because you configured NodePorts on the cluster, Kubernetes opens the NodePorts on all cluster nodes. This configuration lets any node in the cluster handle data plane traffic.

After you configure the mappings, the load balancer listens for traffic on the IP address that you configured for the user cluster's ingress VIP on standard HTTP and HTTPS ports. The load balancer routes requests to any node in the cluster. After a request is routed to one of the cluster nodes, internal Kubernetes networking takes over and routes the request to the destination Pod.




### Kubeception user cluster

#### Control-plane traffic

The following shows the mapping to the IP addresses and NodePort values for control-plane traffic:

  * (`controlPlaneVIP`:`443`) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)
  * (`controlPlaneVIP`:`8132`) -> (NODE_IP_ADDRESSES:`konnectivityServerNodePort`)



Add this mapping for all nodes in the _admin_ cluster, both the admin cluster and the user cluster control-plane nodes.

#### Data plane traffic

The following shows the mapping to the IP addresses and NodePort values for data plane traffic:

  * (`ingressVIP`:`80`) -> (NODE_IP_ADDRESSES:`ingressHTTPNodePort`)
  * (`ingressVIP`:`443`) -> (NODE_IP_ADDRESSES:`ingressHTTPSNodePort`)



Add these mappings for all nodes in the user cluster. With user clusters using kubeception, all nodes in the cluster are worker nodes.

**Note:** If your environment doesn't run on a [supported IaaS platform](https://metallb.io/), your MetalLB LoadBalancer service might display as `pending` on your monitoring dashboard, even when traffic distributes correctly.**Note:** The healthcheck to `ingressVIP` will fail until you configure at least one ingress.

### Resetting connections to failed nodes (Recommended)

In addition to the preceding requirements, we recommend you configure the load balancer to reset client connections when it detects a backend node failure. Without this configuration, clients of the Kubernetes API server can stop responding for several minutes when a server instance goes down, which can cause instability in the Kubernetes control plane.

  * With F5 BIG-IP, this setting is called Action On Service Down in the backend pool configuration page.
  * With HAProxy, this setting is called on-marked-down shutdown-sessions in the backend server configuration.
  * If you are using a different load balancer, you should consult the documentation to find the equivalent setting.



## Getting support for manual load balancing

Google does not provide support for load balancers configured using manual load balancing mode. If you encounter issues with the load balancer, reach out to the load balancer's vendor.

## What's next

  * [Load balancing with Citrix](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/citrix-load-balance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
