---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance/
title: Bundled load balancing with Seesaw \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:58.846754+00:00
---

# Bundled load balancing with Seesaw  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance/

**Version 1.10**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.10 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/overview)



Send feedback 

#  Bundled load balancing with Seesaw Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.10 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/bundled-load-balance)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud can run in one of three load balancing modes: _integrated_ , _manual_ , or _bundled_. This document shows how to configure Google Distributed Cloud to run the [Seesaw load balancer](https://github.com/google/seesaw). in bundled mode.

The instructions here are complete. For a shorter introduction to using the Seesaw load balancer, see [Seesaw load balancer (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/seesaw-load-balance-quickstart).

In bundled load balancing mode, Google Distributed Cloud provides and manages the load balancer. You do not have to get a license for a load balancer, and the amount of setup that you have to do is minimal.

This document shows how to configure the Seesaw load balancer for an admin cluster and one associated user cluster. You can run the Seesaw load balancer on a single VM, or you can run the load balancer in high-availability (HA) mode, which uses two VMs. In HA mode, the Seesaw load balancer uses the [Virtual Router Redundancy Protocol (VRRP)](https://datatracker.ietf.org/doc/html/rfc5798). The two VMs are called the [Master and the Backup](https://datatracker.ietf.org/doc/html/rfc5798#section-1). Each Seesaw VM is given a [virtual router identifier (VRID)](https://datatracker.ietf.org/doc/html/rfc5798#section-3) of your choice. 

## Example of a Seesaw configuration

Here is an example of a configuration for clusters running the Seesaw load balancer in HA mode:

[ ![Seesaw load balancer configuration in HA mode.](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.10/images/seesaw-network.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.10/images/seesaw-network.svg) Seesaw load balancer configuration in HA mode (Click to enlarge)

The preceding diagram shows two Seesaw VMs each for the admin cluster and the user cluster. In this example, the admin cluster and user cluster are on two separate VLANs, and each cluster is in a separate subnet:

Cluster | Subnet  
---|---  
Admin cluster | 172.16.20.0/24  
User cluster | 172.16.40.0/24  
  
### admin-cluster.yaml

The following example of an admin cluster configuration file shows the configuration seen in the preceding diagram of:

  * The master IP address for the pair of Seesaw VMs servicing the admin cluster.

  * VIPs designated for the Kubernetes API server and add-ons of the admin cluster.



    
    
    network:
      hostConfig: 
      ...
    
      ipMode:
        type: "static"
        ipBlockFilePath: "config-folder/admin-cluster-ipblock.yaml"
    ...
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/admin-seesaw-ipblock.yaml"
        masterIP: 172.16.20.57
      ...
    
      vips:
        controlPlaneVIP: "172.16.20.70"
        addonsVIP: "172.16.20.71"
    

### admin-cluster-ipblock.yaml

The following example of an IP block file shows the designation of IP addresses for the nodes in the admin cluster. This also includes the address for the user cluster control-plane node and an IP address to use during cluster upgrade.
    
    
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
    

### admin-seesaw-ipblock.yaml

The following example of another IP block file specifies two IP addresses for Seesaw VMs servicing the admin cluster. Note that this is a separate IP block file for load-balancer VMs, not cluster nodes.
    
    
    blocks:
      - netmask: "255.255.255.0"
        gateway: "172.16.20.1"
        ips:
        - ip: "172.16.20.60"
          hostname: "admin-seesaw-vm-1"
        - ip: "172.16.20.61"
          hostname: "admin-seesaw-vm-2"
    

### user-cluster.yaml

The following example of a user cluster configuration file shows the configuration of:

  * The master IP address for the pair of Seesaw VMs servicing the user cluster.

  * VIPs designated for the Kubernetes API server and ingress service in the user cluster. The Kubernetes API server VIP is on the admin cluster subnet because the control plane for a user cluster runs on a node in the admin cluster.



    
    
    network:
      hostConfig: 
      ...
    
      ipMode:
        type: "static"
        ipBlockFilePath: "config-folder/user-cluster-ipblock.yaml"
    ...
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/user-seesaw-ipblock.yaml"
        masterIP: 172.16.40.31
      ...
    
      vips:
        controlPlaneVIP: "172.16.20.72"
        ingressVIP: "172.16.40.100"
    

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
    

### user-seesaw-ipblock.yaml

The following example of another IP block file specifies two IP addresses for Seesaw VMs servicing the user cluster.
    
    
    blocks:
      - netmask: "255.255.255.0"
        gateway: "172.16.40.1"
        ips:
        - ip: "172.16.40.29"
          hostname: "user-seesaw-vm-1"
        - ip: "172.16.40.30"
          hostname: "user-seesaw-vm-2"
    

### Port groups

The following table describes the configuration of network interfaces for each of the Seesaw VMs, and their connected port groups as seen in the preceding diagram.

Seesaw VMs | Network interface | Network interface configuration | Connected Port Group  
---|---|---|---  
Master | network-interface-1 | VIPs | load-balancer  
network-interface-2 | IP address taken from IP block file for Seesaw VMs | cluster-node  
Backup | network-interface-1 | No configuration | load-balancer  
network-interface-2 | IP address taken from IP block file for Seesaw VMs | cluster-node  
  
The cluster nodes are also connected to the cluster-node port group.

As the preceding table shows, each of the Seesaw VMs for the admin and user clusters has two network interfaces. For each Seesaw VM, the two network interfaces are connected to two separate port groups:

  * load-balancer port group

  * cluster-node port group




The two port groups for a cluster are on the same VLAN for that cluster.

## Set up Seesaw load balancer

### Recommended versions

The preceding diagram shows the recommended network configuration for Seesaw load balancing. When planning your own configuration, we strongly recommend that you use vSphere 6.7 or later, and Virtual Distributed Switch (VDS) 6.6 or later, for bundled load balancing mode.

If you prefer, you can use earlier versions, but your installation will be less secure. The remaining sections in this topic give more detail about the security advantages of using vSphere 6.7+ and VDS 6.6+.

### Plan your VLANs

With bundled load balancing mode, we strongly recommend that you have your clusters on separate VLANs.

If your admin cluster is on its own VLAN, control plane traffic is separate from the data plane traffic. This separation protects the admin cluster and the user cluster control planes from inadvertent configuration mistakes. Such mistakes can lead, for example, to issues like a broadcast storm due to layer 2 loops in the same VLAN, or a conflicting IP address that eliminates the desired separation between the data plane and the control plane.

### Provision VM resources

For the VMs that run your Seesaw load balancer, provision CPU and memory resources according to the network traffic you expect to encounter.

The Seesaw load balancer is not memory-intensive, and can run in VMs with 1GB of memory. However, the CPU requirement increases as the network packet rate increases.

The following table shows storage, CPU, and memory guidelines for provisioning Seesaw VMs. Because packet rate is not a typical measure of network performance, the table also shows guidelines for the maximum number of active network connections. The guidelines assume an environment where VMs have a 10 Gbps link and CPUs run at less than 70% capacity.

When the Seesaw load balancer runs in HA mode, it uses a [(Master, Backup) pair](https://datatracker.ietf.org/doc/html/rfc5798#section-3).), so all traffic flows through a single VM. Because actual use cases vary, these guidelines need to be modified based on your actual traffic. [Monitor your CPU and packet rate metrics](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance#viewing-seesaw-metrics) to determine the necessary changes.

If you need to change CPU and memory for your Seesaw VMs, see [Upgrading a load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance#upgrade-load-balancer). Note that you can keep the same version of the load balancer, and change the number of CPUs and the memory allocation.

For small admin clusters, we recommend 2 CPUs, and for large admin clusters we recommend 4 CPUs.

Storage | CPU | Memory | Packet rate (pps) | Maximum active connections  
---|---|---|---|---  
20 GB | 1 (non-production) | 1 GB | 250k | 100  
20 GB | 2 | 3 GB | 450k | 300  
20 GB | 4 | 3 GB | 850k | 6,000  
20 GB | 6 | 3 GB | 1,000k | 10,000  
  
### Set aside VIPs and IP addresses

#### VIPs

Regardless of your choice of load balancing mode, you must set aside several virtual IP addresses (VIPs) that you intend to use for load balancing. These VIPs allow external clients to reach your Kubernetes API servers, your ingress services, and your add-on services.

Also think about how many Services of type `LoadBalancer` are likely to be active in your user cluster at any given time, and set aside enough VIPs for these Services. As you create Services of type `LoadBalancer` later on, Anthos clusters on VMware automatically configures the Service VIPs on the load balancer.

#### Node IP addresses

With bundled load balancing mode, you can specify static IP addresses for your cluster nodes, or your cluster nodes can get their IP addresses from a DHCP server.

If you want your cluster nodes to have static IP addresses, set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. Also set aside an additional IP address for each cluster to use during cluster upgrade. For details about how many node IP addresses to set aside, see [Creating an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-cluster).

#### IP addresses for Seesaw VMs

Next, for each cluster, admin and user, set aside IP addresses for the VMs that will run your Seesaw load balancers. The number of addresses you set aside depends on whether you want to create HA Seesaw load balancers or non-HA Seesaw load balancers.

#### Master IP addresses

In addition to the IP addresses for the Seesaw VMs, also set aside a single master IP address for the pair of Seesaw VMs for each cluster.

#### Non-HA configuration

If your set up is a non-HA configuration:

  * For the admin cluster, set aside one IP address for a Seesaw VM, and a master IP address for the Seesaw load balancer. Both of these addresses must be on the same VLAN as your admin cluster nodes.

  * For your user cluster, set aside one IP address for a Seesaw VM, and a master IP address for the Seesaw load balancer. Both of these addresses must be on the same VLAN as the user cluster nodes.




### Plan your port groups

The preceding diagram described the [two port groups](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance#port-groups) used in an HA configuration, and how they are connected to the network interfaces on the Seesaw VMs. For an individual Seesaw VM, decide whether you want the two network interfaces to be connected to the same vSphere port group, or connected to separate port groups. If the port groups are separate, they must be on the same VLAN. We strongly recommend that you have two separate port groups.

### Create IP block files

For each cluster, admin and user, specify the addresses you have chosen for your Seesaw VMs in an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/ip-block-file). If you intend to use static IP addresses for your cluster nodes, you must create a separate IP block files for those addresses.

### Fill in your configuration files

Prepare a configuration file for your [admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file) and another configuration file for your [user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-cluster-configuration-file).

In your configuration file for a given cluster, set `loadBalancer.kind` to `"Seesaw"`.

Under `loadBalancer`, fill in the `seesaw` section:
    
    
    loadBalancer:
      kind: Seesaw
      seesaw:
    

For information on how to fill in the `seesaw` section of a cluster configuration file, refer to [loadbalancer.seesaw (admin cluster)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#loadbalancer-seesaw-section) or [loadbalancer.seesaw (user cluster)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-cluster-configuration-file#loadbalancer-seesaw-section).

In the admin cluster configuration file, designate the following:

  * VIP for the Kubernetes API server of the admin cluster 
  * VIPs for the admin cluster add-ons
  * Master IP address for the pair of Seesaw VMs servicing the admin cluster.



These VIPs must be on the admin cluster subnet.

In the user cluster configuration file, designate:

  * VIP for the Kubernetes API server of the user cluster (this must be on the admin cluster subnet)
  * Ingress VIP in the user cluster
  * Master IP address for the pair of Seesaw VMs servicing the user cluster.



The last two addresses in the preceding list must be on the user cluster subnet.

### Enable MAC learning or promiscuous mode (HA only)

If you are setting up a non-HA Seesaw load balancer, you can skip this section.

If you have set `loadBalancer.seesaw.disableVRRPMAC` to true, you can skip this section.

If you are setting up an HA Seesaw load balancer and you have set `loadBalancer.seesaw.disableVRRPMAC` to `false`, you must enable some combination of MAC learning, forged transmits, and promiscuous mode on your load-balancer port group.

How you enable these features varies according to the type of switch you have:

Switch type| Enabling features| Security impact  
---|---|---  
vSphere 7.0 [VDS](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-B15C6A13-797E-4BCB-B9D9-5CBC5A60C3A6.html) |  For vSphere 7.0 with HA, you are required to set `loadBalancer.seesaw.disableVRRPMAC` to `true`. MAC learning is not supported.  |   
vSphere 6.7 with [VDS](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.networking.doc/GUID-B15C6A13-797E-4BCB-B9D9-5CBC5A60C3A6.html) 6.6 |  Enable MAC learning and [forged transmits](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-7DC6486F-5400-44DF-8A62-6273798A2F80.html) for your load balancer by running this command: `gkectl prepare network --config [CONFIG_FILE]`, where `[CONFIG_FILE]` is the path of your cluster configuration file. You need [dvPort group.Modify](https://www.google.com/url?q=https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-70947484-AFE7-476B-BDC5-3370E755C313.html&sa=D&usg=AFQjCNE0ks8GCuWs5Wl_TdhBuJxDw7-Ymw) permission to do this.  | Minimal. If your load-balancer port group is connected only to your Seesaw VMs, then you can limit MAC learning to your trusted Seesaw VMs.  
vSphere 6.5 or vSphere 6.7 with a version of VDS lower than 6.6 | Enable [promiscuous mode](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-92F3AB1F-B4C5-4F25-A010-8820D7250350.html) and forged transmits for your load-balancer port group. Use the vSphere user interface on the port group page in **Networking** tab: **Edit Settings - > Security**. | All VMs on your load-balancer port group are in promiscuous mode. So any VM on your load-balancer port group can see all traffic. If your load-balancer port group is connected only to your Seesaw VMs, then it is only those VMs that can see all traffic.  
[NSX-T logical switch](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/2.3/com.vmware.nsxt.admin.doc/GUID-F89C1C1F-A270-4FC9-A1CF-CB90545FB636.html) | [Enable MAC learning](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/2.5/administration/GUID-C5752084-A582-4AEA-BD5D-03FE5DBC746E.html) on the logical switch. | vSphere does not support creating two logical switches in the same layer-2 domain. So the Seesaw VMs and the cluster nodes must be on the same logical switch. This means that MAC learning is enabled for all cluster nodes. An attacker might be able to achieve a MAC spoof by running privileged Pods in the cluster.  
[vSphere Standard Switch](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.networking.doc/GUID-350344DE-483A-42ED-B0E2-C811EE927D59.html) | Enable [promiscuous mode](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-92F3AB1F-B4C5-4F25-A010-8820D7250350.html) and forged transmits for your load-balancer port group. Use the vSphere user interface on each ESXI host: **Configure - > Virtual switches -> Standard Switch -> Edit Setting on the port group -> Security**. | All VMs on your load-balancer port group are in promiscuous mode. So any VM on your load-balancer port group can see all traffic. If your load balancer-port group is connected only to your Seesaw VMs, then it is only those VMs that can see all traffic.  
  
### Finish filling in your admin cluster configuration file

Follow the instructions in [Create an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-cluster#filling_in_your_configuration_file) to finish filling in your admin cluster configuration file.

### Run preflight checks

Run preflight checks on your admin cluster configuration file:
    
    
    gkectl check-config --config ADMIN_CLUSTER_CONFIG
    

Replace ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.

### Upload OS images

Upload OS images to your vSphere environment:
    
    
    gkectl prepare --config ADMIN_CLUSTER_CONFIG
    

### Create a load balancer for your admin cluster
    
    
    gkectl create loadbalancer --config [ADMIN_CLUSTER_CONFIG]
    

### Create your admin cluster

Follow the instructions in [Create an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-cluster) to create your admin cluster.

### Finish filling in your user cluster configuration files

Follow the instructions in [Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-user-cluster#filling_in_your_configuration_file) to finish filling in your user cluster configuration file.

### Run preflight checks

Run preflight checks on your user cluster configuration file:
    
    
    gkectl check-config --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTERE_KUBECONFIG: the path of your admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




### Upload OS images

Upload OS images to your vSphere environment:
    
    
    gkectl prepare --config USER_CLUSTER_CONFIG
    

### Create a load balancer for your user cluster

Create a load balancer for your user cluster:
    
    
    gkectl create loadbalancer --config USER_CLUSTER_CONFIG
    

### Create your user cluster

Follow the instructions in [Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-user-cluster) to create your user cluster.

## Performance and load testing

The download throughput of your application scales linearly with the number of backends. This is because the backends send responses directly to the clients, bypassing the load balancer, using Direct Server Return.

In contrast, the upload throughput of your application is limited by the capacity of the one Seesaw VM that performs the load balancing.

Applications vary in the amount of CPU and memory that they require, so it is critically important that you do a load test before you start serving a large number of clients.

Testing indicates that a single Seesaw VM with 6 CPUs and 3 GB of memory can handle 10 GB/s (line rate) uploading traffic with 10 K concurrent TCP connections. However, it is important that you run your own load test if you plan to support a large number of concurrent TCP connections.

## Scaling limits

With bundled load balancing, there are limits to how much your cluster can scale. There is a limit on the number of nodes in your cluster, and there is a limit on the number of Services that can be configured on your load balancer. There is also a limit on health checks. The number of health checks depends on both the number of nodes and the number of Services.

Starting with version 1.3.1, the number of health checks depends on the number of nodes and the number of traffic local Services. A traffic local Service is a Service that has its [`externalTrafficPolicy`](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip) set to `"Local"`.

| Version 1.3.0| Version 1.3.1 and later  
---|---|---  
Max Services (S)| 100| 500  
Max nodes (N)| 100| 100  
Max health checks|  S * N <= 10K| N + L * N <= 10K, where L is number of traffic local services  
  
Example: In version 1.3.1, suppose you have 100 nodes and 99 traffic local Services. Then the number of health checks is 100 + 99 * 100 = 10,000, which is within the 10K limit.

## Upgrade the load balancer for a cluster

When you [upgrade a cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/upgrading), the load balancer is automatically upgraded. You don't need to run a separate command to upgrade the load balancer.

If you like, you can update the CPUs or memory of your Seesaw VMs without doing a full upgrade. First edit the `cpus` and `memoryMB` values in your cluster configuration file. For example:
    
    
    apiVersion: v1
    bundlePath:
    loadBalancer:
      kind: Seesaw
      seesaw:
        cpus: 3
        memoryMB: 3072
    

Then, to update the load balancer for an admin cluster:
    
    
    gkectl upgrade loadbalancer --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config ADMIN_CLUSTER_CONFIG --admin-cluster

To update the load balancer for a user cluster: 
    
    
    gkectl upgrade loadbalancer --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path your admin cluster kubeconfig file

  * ADMIN_CLUSTER_CONFIG: the path of your admin cluster configuration file

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## View Seesaw logs

The Seesaw bundled load balancer stores log files on the Seesaw VMs in `/var/log/seesaw/`. The most important log file is `seesaw_engine.INFO`.

Starting with v1.6, if Stackdriver is enabled, logs are uploaded to Cloud as well. You can view them under resource "anthos_l4lb". To disable log uploading, you can ssh to the VM and run:
    
    
    sudo systemctl disable --now docker.fluent-bit.service
    

## View information about your Seesaw VMs

You can get information about your Seesaw VMs for a cluster from the SeesawGroup custom resource.

View the SeesawGroup custom resource for a cluster:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get seesawgroups -n kube-system -o yaml
    

Replace CLUSTER_KUBECONFIG with the path of the cluster kubeconfig file.

The output has an `isReady` field that shows whether the VMs are ready to handle traffic. The output also shows the names and IP addresses of the Seesaw VMs, and which VM is the primary VM:
    
    
    apiVersion: seesaw.gke.io/v1alpha1
    kind: SeesawGroup
    metadata:
      ...
      name: seesaw-for-cluster-1
      namespace: kube-system
      ...
    spec: {}
    status:
      machines:
      - hostname: cluster-1-seesaw-1
        ip: 172.16.20.18
        isReady: true
        lastCheckTime: "2020-02-25T00:47:37Z"
        role: Master
      - hostname: cluster-1-seesaw-2
        ip: 172.16.20.19
        isReady: true
        lastCheckTime: "2020-02-25T00:47:37Z"
        role: Backup
    

## View Seesaw metrics

The Seesaw bundled load balancer provides the following metrics:

  * Throughput per Service or node
  * Packet rate per Service or node
  * Active connections per Service or node
  * CPU and memory usage
  * Number of healthy backend Pods per Service
  * Which VM is the primary and which is the backup
  * Uptime



Starting with v1.6, those metrics are uploaded to Cloud with Stackdriver. You can view them under monitoring resource of "anthos_l4lb".

You can also use any monitoring and dashboarding solutions of your choice, as long as they support the Prometheus format.

## Delete a load balancer

If you delete a cluster that uses bundled load balancing, you should then delete the Seesaw VMs for that cluster. You can do this by deleting the Seesaw VMs in the vSphere user interface.

As an alternative, you can run `gkectl delete loadbalancer`.

For an admin cluster:
    
    
    gkectl delete loadbalancer --config ADMIN_CLUSTER_CONFIG --seesaw-group-file GROUP_FILE
    

For a user cluster:
    
    
    gkectl delete loadbalancer  --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG \
        --seesaw-group-file GROUP_FILE

Replace the following:

  * ADMIN_CLUSTER_CONFIG: the path of the admin cluster configuration file

  * USER_CLUSTER_CONFIG: the path of the user cluster configuration file

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * GROUP_FILE: the path of the Seesaw group file. The name of the group file has this form  
`seesaw-for-CLUSTER_NAME-IDENTIFIER.yaml`.   
For example: `seesaw-for-gke-admin-12345.yaml`.




## Configuring stateless NSX-T distributed firewall policies for use with Seesaw load balancer

If your configuration uses the stateful NSX-T distributed firewall, and you also want to use Seesaw load balancer, you have several options. Choose which one best suits your environment.

**Note:** The instructions provided here refer to NSX-T 3.1. If you are running an older version of NSX, the menu options may be slightly different.**Note:** Regardless of not having distributed firewall policies enabled, as long as the distributed firewall isn't explicitly disabled, you will have to follow one of the following configuration options.

### NSX configuration checklist

Before you implement one of the remedial options described, verify that you have the following NSX DFW configuration in place:

  * Stateful NSX DFW sections are the default configuration. This is likely what you have in your environment. See [Firewall Sections and Firewall Rules](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/administration/GUID-7897D447-3C0D-43EF-AF89-1563F24EB2D4.html).

  * Service insertion is sometimes used with the NSX DFW to provide service chaining and L7 inspection as part of partner integration. Service insertion policies are also stateful by default. To confirm this integration is enabled in your environment, review the [following information](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/administration/GUID-F6685367-7AA1-4771-927E-ED77727CFDA3.html).




### Option 1--Create a stateless distributed firewall policy for the Seesaw load balancers

With this option, you can keep the distributed firewall enabled in the environment, while mapping the Anthos infrastructure, specifically the Seesaw load balancers, to a stateless Policy. Be sure to consider the differences between stateless and stateful firewalls, to make sure you choose the type best suited to your environment. See [Add a Firewall Rule Section in Manager Mode--Procedure--Step 6](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/administration/GUID-DE76177B-F97C-476D-9A58-EEF94309CC78.html#procedure-1) of the VMware documentation.

To create a stateless firewall policy:

  1. Navigate to **Inventory > Tags**. Create a tag named `seesaw`.

  2. Navigate to **Inventory > Groups**. Create a group named `Seesaw`.

  3. Configure the Seesaw set members.

     * Click **Set Members**. Configure set members with **Membership Criteria** based on the `seesaw` tag that you created. Although using NSX tags is generally considered a best practice by VMware, this methodology requires automation to set them every time the environment changes, such as when you upgrade or resize the Anthos clusters in your environment. In that case, a policy based on some other membership criteria might work better. You can use other dynamic membership options, such as VM Names (including regular expressions), segments, and segment ports. For more information on group membership criteria, refer to [Add a Group](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/administration/GUID-9DFF6EE2-2E00-4097-A412-B72472596E4D.html).
  4. Navigate to **Security > Distributed Firewall**. Create a section called `Anthos`.

  5. Click the top right gear icon and toggle the **Stateful** switch to **No**.

**Note:** A stateless policy cannot be changed to stateful after it is created.
  6. Add rules to the section. It's recommended that you add at least two symmetrical rules, such as the following: 
         
         Source: Seesaw Group, Destination: Any, Applied to: Seesaw Group
         Source: Any, Destination: Seesaw Group, Applied to: Seesaw Group
         

  7. Publish the changes and verify operations.




The stateless section must be placed in the NSX DFW table so that it takes precedence over other sections that might allow the same traffic in a stateful manner, thus masking the stateless rules. Make sure the stateless section is the most specific, and that it precedes other policies that could potentially create an overlap.

Although not mandatory, you can create a group that includes all Anthos VMs, using a coarse-grained membership criteria like Segment Tag, which means all VMs connected to a specific NSX network are included in the group. You can then use this group in your stateless policy.

**Warning:** If you are using NSX service insertion, your redirection rules likely sit inside a stateful policy. If so, you must create a new stateless policy and ensure redirection for the Anthos Seesaw load balancers there.

### Option 2--Add the Seesaw VMs to the distributed firewall exclusion list

With this option, you can exclude VMs from distributed firewall inspection entirely without disabling the NSX DFW. See [Manage a Firewall Exclusion List](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/administration/GUID-3B3C278D-4E35-4CE9-A4E2-ED6B1F25ABCE.html).

  1. Navigate to **Security > Distributed Firewall**. Select **Actions > Exclusion List**.

  2. Pick the Seesaw Group, or the group that includes all Anthos VMs.




## Troubleshooting

### Get an SSH connection to a Seesaw VM

Occasionally you might want to SSH into a Seesaw VM for troubleshooting or debugging.

#### Get the SSH key

If you have already created your cluster, use the following steps to get the SSH key:

  1. Get the `seesaw-ssh` Secret from the cluster. Get the SSH key from the Secret and base64 decode it. Save the decoded key in a temporary file:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get -n  kube-system secret seesaw-ssh -o \
         jsonpath='{@.data.seesaw_ssh}' | base64 -d | base64 -d > /tmp/seesaw-ssh-key
         

Replace CLUSTER_KUBECONFIG with the path of the cluster kubeconfig file.

  2. Set the appropriate permissions for the key file:
         
         chmod 0600 /tmp/seesaw-ssh-key

If you have not already created your cluster, use the following steps to get the SSH key:

  3. Locate the file named `seesaw-for-CLUSTER_NAME-IDENTIFIER.yaml`.

The file is called the _group file_ and is located next to `config.yaml`.

Also, `gkectl create loadbalancer` prints the location of the group file.

  4. In the file, get the value of `credentials.ssh.privateKey`, and base64 decode it. Save the decoded key in a temporary file:
         
         cat seesaw-for-CLUSTER_NAME-IDENTIFIER.yaml  | grep privatekey | sed 's/    privatekey: //g' \
         | base64 -d > /tmp/seesaw-ssh-key
         

  5. Set the appropriate permissions for the key file:
         
         chmod 0600 /tmp/seesaw-ssh-key
         




Now you can SSH into the Seesaw VM:
    
    
    ssh -i /tmp/seesaw-ssh-key ubuntu@SEESAW_IP

Replace SEESAW_IP with the IP address of the Seesaw VM.

### Get snapshots

You can capture snapshots for Seesaw VMs by using the [`gkectl diagnose snapshot`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/diagnose#diagnose_snapshot) command along with the `--scenario` flag.

If you set `--scenario` to `all` or `all-with-logs`, the output includes Seesaw snapshots along with other snapshots.

If you set `--scenario` to `seesaw`, the output includes only Seesaw snapshots.

Examples:
    
    
    gkectl diagnose snapshot --kubeconfig ADMIN_CLUSTER_KUBECONFIG --scenario seesaw
    
    gkectl diagnose snapshot --kubeconfig ADMIN_CLUSTER_KUBECONFIG --cluster-name CLUSTER_NAME --scenario seesaw
    
    gkectl diagnose snapshot --seesaw-group-file GROUP_FILE --scenario seesaw
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * GROUP_FILE: the path of the group file for the cluster.




### Recreate Seesaw VM from broken state

If a Seesaw VM is accidentally deleted, you can recreate the VM by using the [`gkectl upgrade loadbalancer`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-%0Abalance#upgrade-load-balancer) command with the `--no-diff` and `--force` flags. This recreates all Seesaw VMs in your cluster regardless of existence or health status. If your load balancer is in HA mode, and only one out of two VMs is deleted, running this command will recreate both VMs.

For example, to recreate the Seesaw load balancer in the admin cluster, run the following command:
    
    
    gkectl upgrade loadbalancer --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config ADMIN_CLUSTER_CONFIG --admin-cluster --no-diff --force
    

To recreate the Seesaw load balancer in the user cluster, run the following command:
    
    
    gkectl upgrade loadbalancer --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG --no-diff --force
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path your admin cluster kubeconfig file

  * ADMIN_CLUSTER_CONFIG: the path of your admin cluster configuration file

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## Known issues

### Cisco ACI doesn't work with Direct Server Return (DSR)

Seesaw runs in DSR mode and by default it doesn't work in Cisco ACI because of data-plane IP learning. Possible workaround using Application Endpoint Group can be found [here](https://kb.vmware.com/s/article/58485).

### Citrix Netscaler doesn't work with Direct Server Return (DSR)

If you run Netscaler load balancer in front of Seesaw, MAC-Based Forwarding (MBF) must be turned off. Refer to the [Citrix documentation](https://docs.citrix.com/en-us/citrix-adc/current-release/networking/interfaces/configuring-mac-based-forwarding.html#mac-based-forwarding-for-a-load-balancing-setup).

### Upgrading the Seesaw load balancer does not work in some cases

If you attempt to upgrade a cluster from 1.8.0, or use `gkectl upgrade loadbalancer` to update some parameters of your Seesaw load balancer at version 1.8.0, this will not work in either DHCP or IPAM mode. Wait for an announced fix in an upcoming version before you upgrade.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
