---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/manual-load-balance/
title: Enabling manual load balancing mode \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:30.386572+00:00
---

# Enabling manual load balancing mode  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/manual-load-balance/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Enabling manual load balancing mode Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Be sure to plan your installation ahead of time. Your clusters' configurations, as declared in the Google Distributed Cloud configuration file, become immutable after you create the clusters. You can't change most aspects of your clusters after they are created, including networking and authentication. The only configurable exceptions are: 

  * [Resizing user clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/resizing-a-user-cluster#resize)
  * [Creating additional user clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/creating-additional-user-clusters#modify_usercluster)
  * [Upgrading clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/upgrading#modify_config)
  * [Creating and managing node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/managing-node-pools)



Google Distributed Cloud clusters can run with one of three load balancing modes: integrated, bundled, or manual. With integrated mode, Google Distributed Cloud cluster uses the F5 BIG-IP load balancer. With bundled mode, Google Distributed Cloud provides and manages the load balancer. You do not have to get a license for a load balancer, and the amount of setup that you have to do is minimal. With manual mode, Google Distributed Cloud uses a different load balancer of your choice. Manual load balancing mode requires that you do more configuration than with integrated mode. This page describes the steps you need to take if you choose to use the manual load balancing mode.

The [Citrix load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/citrix-load-balance) is an example load balancer that you could use with manual load balancing mode.

In this topic, you set aside IP addresses and `nodePort` values for later use. The idea is that you choose the IP addresses and `nodePort` values that you want to use for load balancing and for your cluster nodes. But you don't do anything with the addresses and `nodePort` values at this point. Later, when you are ready to install Google Distributed Cloud, you will need the addresses and `nodePort` values to fill in your cluster configuration file. You will also need the addresses and `nodePort` values when you manually configure your load balancer.

## Setting aside virtual IP addresses

Regardless of whether you use integrated, bundled or manual load balancing mode, you must set aside several virtual IP addresses (VIPs) that you intend to use for load balancing. These VIPs allow external clients to reach your Kubernetes API servers, your ingress services, and your addon services. For detailed instructions on setting aside VIPs, see [Setting aside virtual IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/seesaw-load-balance-quickstart#set_aside_virtual_ip_addresses).

## Setting aside node IP addresses

With manual load balancing mode, you cannot use DHCP. You must specify static IP addresses for your cluster nodes. You need to set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. For details about how many node IP addresses to set aside, see [Configuring static IPs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-static-ips#configuring_static_ips).

## Setting aside `nodePort` values

In Google Distributed Cloud cluster, the Kubernetes API server, the ingress service, and the addon service are implemented as [Kubernetes Services of type `NodePort`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#service_of_type_nodeport). With manual load balancing mode, you must choose your own `nodePort` values for these Services. Choose values in the 30000 - 32767 range. After you choose your `nodePort` values, set them aside for later when you modify your cluster configuration file.

Choose and set aside the following `nodePort` values.

  * For each VIP that you have set aside for a Kubernetes API server, set aside one `nodePort` value.

  * For each VIP that you have set aside for a cluster ingress service, set aside two `nodePort` values: one for HTTP traffic and one for HTTPS traffic. This only applies to user cluster.

  * For each VIP that you have set aside for a cluster addon service, set aside one `nodePort` value. This only applies to admin cluster.




For example, suppose you intend to have two user clusters, and you intend to use addons. You would need to choose and set aside the following `nodePort` values:

  * A `nodePort` value for the Kubernetes API server in the admin cluster.

  * For each of two user clusters, a `nodePort` value for the Kubernetes API server.

  * For each of two user clusters, a `nodePort` value for HTTP traffic to the ingress service.

  * For each of two user clusters, a `nodePort` value for HTTPS traffic to the ingress service.

  * A `nodePort` value for the addon service in the admin cluster.




So in the preceding example, you would need to set aside 8 `nodePort` values.

## Modifying the Google Distributed Cloud configuration file

Prepare a configuration file for each of the cluster: [admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file) and [user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file).

  * Set `loadBalancer.kind` to `ManualLB`.

  * Set `network.ipMode` to `static`

  * Set `network.ipBlockFilePath` to the path of the static IP YAML file for your cluster. This is documented in [Configuring static IPs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-static-ips#static_ips). DHCP is not an option for manual load balancing mode.

  * Update the `loadBalancer.manualLB` field with the `nodePort` values you have chosen for the cluster.




The following example shows a portion of an updated configuration file.
    
    
    network:
      ipMode:
        type: static
        ipBlockFilePath: "ipblock1.yaml"
    loadBalancer:
      kind: ManualLB
      manualLB:
        ingressHTTPNodePort: 30243
        ingressHTTPSNodePort: 30879
        controlPlaneNodePort: 30562:
        addonsnodeport: 31405
    

**Note:** The `ingressHTTPNodePort` and `ingressHTTPSNodePort` fields are only relevant for the user cluster configuration file, so do not include them in the admin cluster configuration file.

## Configure your load balancer

Now that you've updated the configuration file, log in to your load balancer's management console and configure your VIPs:

  * cluster control plane for both admin and user clusters, TCP port 443
  * Add-on manager for the admin cluster if used, TCP port 8443
  * User cluster ingress controller, TCP port 80
  * User cluster ingress controller, TCP port 443



## Load balancing example

A Service has a `ports` field, which is an array of [ServicePort](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceSpec) objects. In a Service of type `NodePort`, each ServicePort object has a `protocol`, a `port`, a `nodePort`, and a `targetPort`. For example, here is part of a manifest for a Service that has two ServicePort objects in its `ports` array:
    
    
    ...
    kind: Service
    ...
    spec:
      ...
      type: NodePort
      ports:
      - protocol: TCP
        port: 80
        nodePort: 32676
        targetPort: 8080
      - protocol: TCP
        port: 443
        nodePort: 32677
        targetPort: 443
    ...
    

Suppose the preceding Service represents the ingress service for one of your user clusters. Also suppose that you have made the following choices:

  * `203.0.113.5` is the VIP for the ingress service of your user cluster.

  * The node addresses for your user cluster are `192.168.0.10`, `192.168.0.11`, and `192.168.0.12`.




After you have configured your load balancer, traffic is routed as follows:

  * A client sends a request to `203.0.113.5` on TCP port 80. The load balancer chooses a user cluster node. For this example, assume the node address is `192.168.0.11`. The load balancer forwards the request to `192.168.0.11` on TCP port 32676. The [iptables](https://linux.die.net/man/8/iptables) rules on the node forward the request to an appropriate Pod on TCP port 8080.

  * A client sends a request to the `203.0.113.5` on TCP port 443. The load balancer chooses a user cluster node. For this example, assume the node address is `192.168.0.10`. The load balancer forwards the request to `192.168.0.10` on TCP port 32677. The iptables rules on the node forward the request to an appropriate Pod on TCP port 443.




## Getting support for manual load balancing

Google does not provide support for load balancers configured using manual load balancing mode. If you encounter issues with the load balancer, reach out to the load balancer's vendor.

## What's next

  * [Load balancing with Citrix](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/citrix-load-balance)



## Troubleshooting

For more information, refer to [Troubleshooting](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
