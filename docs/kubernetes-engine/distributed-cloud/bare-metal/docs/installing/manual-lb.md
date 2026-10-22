---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/manual-lb/
title: Configure manual load balancing \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:21.226564+00:00
---

# Configure manual load balancing  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/manual-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure manual load balancing Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the load-balancing requirements when using manual load balancing. Unlike [bundled load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/load-balance#bundled_load_balancer_mode) where Google Distributed Cloud deploys load balancers to cluster nodes for control plane and data plane traffic, with manual load balancing you configure your own load-balancing solutions for control plane and data plane traffic.

You must set up an external load balancer for the control plane before creating a bare metal cluster. The external control plane load balancer can also be used for data plane traffic, or you can set up a separate load balancer for the data plane. For example, you can use an in-cluster load balancer like [MetalLB](https://metallb.universe.tf/) for data plane traffic.

In addition to explaining load-balancing requirements, this page describes how to configure manual load balancing using [F5 BIG-IP](https://www.f5.com/products/big-ip-services/local-traffic-manager).

## Prerequisites

The following sections describe the prerequisites for configuring manual load balancing.

### Required IP address

You must plan your VIPs before creating a cluster. All clusters need a VIP for the control plane. All [user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep#user_clusters) need a second VIP for the ingress service.

These VIPs can be in any IPv4 subnet routable from the load balancer. The control plane VIP must be reachable from all cluster nodes and from the admin workstation that you run `bmctl` on.

When you create the cluster, the ingress service is deployed using the VIP you specify in the cluster config file. You can configure load balancing for this IP address after cluster creation.

You must know the IP addresses you will use for the nodes that will be used as control plane nodes.

### External control plane load balancer requirements

The control plane load balancer must be configured before creating the cluster. The control plane load balancer must meet these requirements:

  * A virtual service (frontend) for the control plane VIP. The control plane's default listen port is 443. However, if you specify a different port the `loadBalancer.ports.controlPlaneLBPort` field of the cluster config file use that port for the virtual service.
  * A backend group containing all of the IP addresses of the cluster's control plane nodes. The backend port the control plane listens on is 6444.
  * A health check that monitors the backend nodes. The health check must use HTTPS and check the `/readyz` endpoint on port 6444. The health check must verify that this endpoint returns status code 200 to consider the node healthy.



If the external load balancer is not configured correctly, the cluster bootstrapping is likely to fail. A [preflight check](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight) verifies that the external load balancer is correctly configured, including verifying that the load balancer is health checking the `/readyz` endpoint.

### Reset connections to failed nodes (Recommended)

In addition to the preceding requirements, we recommend you configure the load balancer to reset client connections when it detects a backend node failure. Without this configuration, clients of the Kubernetes API server can stop responding for several minutes when a server instance goes down, which can cause instability in the Kubernetes control plane.

  * With F5 BIG-IP, this setting is called Action On Service Down in the backend pool configuration page.
  * With HAProxy, this setting is called on-marked-down shutdown-sessions in the backend server configuration.
  * If you are using a different load balancer, you should consult the documentation to find the equivalent setting.



## Configure your cluster

Before you create a Google Distributed Cloud cluster, you create a cluster configuration file with `bmctl`. Edit this file to enable manual load balancing in the cluster:

  1. Set the `loadBalancer.mode` field to `manual`.
  2. Set the `loadBalancer.vips.controlPlaneVIP` field to the VIP that you configured on the load balancer.
  3. Remove, or comment out, the `loadBalancer.addressPools` section.



After you have finished editing the config file, including fields not related to load balancing, verify that the control plane VIP is correctly configured on the load balancer by running the preflight checks:
    
    
    bmctl check preflight -c CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of the cluster.

## Support LoadBalancer Services in user clusters

You must configure load balancing to support Kubernetes [LoadBalancer services](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) In manual load-balancing mode, Google Distributed Cloud does not automatically provision load balancers so LoadBalancer services don't work unless you provision and configure load balancers to point the services.

Additionally, Google Distributed Cloud automatically deploys an ingress service in all user clusters using a LoadBalancer service. To be externally accessible, this LoadBalancer service requires a load balancer configured to point to the service.

Your options for supporting LoadBalancer services include:

  * Manually configure the load balancer for every LoadBalancer service in the cluster. See Configuring support for LoadBalancer services for an example using F5 BIG-IP.
  * Install a load balancer controller in the cluster that configures the external load balancer when LoadBalancer services are created.
  * Install an in-cluster load-balancing solution like [MetalLB](https://metallb.universe.tf/).



## Manual load balancing with F5 BIG-IP

This section describes how to configure manual load balancing with F5 BIG-IP as the external load balancer. If you are using a different load balancer, consult the documentation for that load balancer and use these steps as a model.

### Configure the control plane load balancer

You must configure the control plane load balancer before creating a cluster. After performing these steps, you can configure your cluster and create it.

#### Create a partition for your cluster

Each cluster should have its own [partition](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-12-0-0/3.html). Use the BIG-IP Configuration utility to create a partition:

  1. Go to **System > Users > Partition List**.
  2. Click **Create**.
  3. Enter a name for the partition.
  4. Click **Finished**.



In the following steps you create objects in this partition. Make sure this partition is selected in the drop-down menu in the top-right corner of the UI for each of the following tasks so that each object is created in this partition.

#### Create a monitor

Create a [monitor](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-monitors-reference-12-0-0/2.html) to perform health checks on the control plane nodes:

  1. Go to **Local Traffic > Monitors**.
  2. Click **Create**.
  3. Enter a name for the monitor (for example, https_readyz).
  4. Set the **Type** to **HTTPS**.
  5. For **Send String** , enter `GET /readyz HTTP/1.1\r\nHost: \r\nConnection: close`.
  6. For **Receive String** , enter `HTTP/1.1 200`.
  7. Click **Finished**.



#### Create nodes

Create a [node](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-basics-13-0-0/3.html) that points to the control plane nodes. If your cluster has a [high availability (HA) control plane](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep#high_availability) with multiple control plane nodes, create a node object for each control plane node.

  1. Go to **Local Traffic > Nodes > Node List**.
  2. Click **Create**.
  3. Enter a name for the node.
  4. Enter the IP address of the node in the Address field.
  5. Click **Finished**.



#### Create a backend pool

Create a [pool](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-basics-11-6-0/4.html) for the control plane nodes:

  1. Go to Local **Traffic > Pools > Pool List**.
  2. Click **Create**.
  3. Select **Advanced** in the **Configuration** drop-down.
  4. Enter a name for the pool.
  5. Select the health monitor created earlier.
  6. Set **Action On Service Down** to **Reject** (see discussion of this setting in the Resetting connections to failed nodes section).
  7. Add the control plane node to the pool. If your cluster has multiple control plane nodes, repeat these steps for each node: 
     1. In the **New Members** section, click **Node List** and then select the previously created control plane node.
     2. In the **Service Port** field, enter **6444**.
     3. Click **Add**.



#### Create a virtual server

Create a [virtual server](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-basics-11-6-0/2.html) for the control plane:

  1. Go to **Local Traffic > Virtual Servers > Virtual Server List**.
  2. Click **Create**.
  3. Enter a name for the virtual server.
  4. Set **Type** to **Standard**.
  5. Enter **0.0.0.0/0** in the **Source Address** field to allow traffic from any source.
  6. Enter the control plane VIP as the **Destination Address**.
  7. Enter the control plane port as the **Service Port**. By default this is 443, but this is configurable and must match what you configure in your cluster configuration for `loadBalancer.ports.controlPlaneLBPort`.
  8. In the **Source Address Translation** field, select **Auto Map**.
  9. In **Default Pool** , select the pool created earlier in the drop-down.
  10. Click **Finished**.



### Configure support for LoadBalancer services

In manual load-balancing mode, Google Distributed Cloud does not automatically provision load balancers to support [LoadBalancer services](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer). See Supporting LoadBalancer Services in user clusters for more information.

This section shows how to manually configure a F5 BIG-IP load balancer for a LoadBalancer service. Repeat these steps for each LoadBalancer service you want to expose.

#### Prerequisites

In order to configure a LoadBalancer service, you need to know the VIP that you want to expose through the load balancer, the port you want to expose it on, and the NodePort that the LoadBalancer service in Kubernetes is using.

After you have deployed a LoadBalancer service in your cluster, determine the NodePort used for the LoadBalancer service. The following command will show the ports of the service:
    
    
    kubectl --kubeconfig KUBECONFIG get service SERVICE_NAME -oyaml
    

Replace the following:

  * `KUBECONFIG` with the path of the kubeconfig file to use.
  * `SERVICE_NAME` with the name of the LoadBalancer service.



The output of `kubctl get service` includes a `ports` section. Each port entry shows the nodePort exposed for the port on the service, and this nodePort is what you configure the load balancer backend to point to. The following sample output shows the structure of the `ports` section:
    
    
    spec:
      clusterIP: 172.26.232.107
      externalTrafficPolicy: Cluster
      loadBalancerIP: 21.0.101.77
      ports:
      - name: status-port
        nodePort: 30281
        port: 15021
        protocol: TCP
        targetPort: 15021
      - name: http
        nodePort: 30124
        port: 80
        protocol: TCP
        targetPort: 80
      - name: https
        nodePort: 31858
        port: 443
        protocol: TCP
        targetPort: 443
    

There are ports for HTTP and HTTPS traffic. You can expose one or both of these ports through your load balancer.

If you are exposing the ingress service that is automatically deployed in all clusters, the LoadBalancer service is named `istio-ingress` and is in the `gke-system` namespace. Find its ports with this command:
    
    
    kubectl --kubeconfig KUBECONFIG -n gke-system get service istio-ingress -oyaml
    

The ingress service is configured with a loadBalancerIP which is the IP supplied in the `loadBalancer.vips.ingressVIP` field in the initial cluster configuration. You should expose this VIP to expose the ingress service on the external load balancer.

#### Create a backend pool

  1. Go to **Local Traffic > Pools > Pool List**.
  2. Click **Create**.
  3. Enter a name for the pool.
  4. Select **tcp** as the health monitor.
  5. Add worker nodes to the node pool. Repeat these steps for each node. You can add control planes and worker nodes as Kubernetes NodePorts are accessible on any node in the cluster. 
     1. In the **New Members** section, click **Node List** and then select one of the previously created nodes.
     2. In the **Service Port** field, enter the NodePort value for the service.
     3. Click **Add**.



#### Create a virtual server

  1. Go to **Local Traffic > Virtual Servers > Virtual Server List**.
  2. Click **Create**.
  3. Enter a name for the virtual server.
  4. Set **Type** to **Standard**.
  5. Enter **0.0.0.0/0** in the **Source Address** field to allow traffic from any source.
  6. Enter the load balancer service VIP as the **Destination Address**.
  7. Enter the port being exposed for the load balancer service as the **Service Port**.
  8. In the **Source Address Translation** field, select **Auto Map**.
  9. In **Default Pool** , select the pool created earlier in the drop-down.
  10. Click **Finished**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
