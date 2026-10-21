---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/manual-load-balance/
title: Enabling manual load balancing mode \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:58.972199+00:00
---

# Enabling manual load balancing mode  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/manual-load-balance/

**Version 1.10**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.10 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/overview)



Send feedback 

#  Enabling manual load balancing mode Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.10 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/manual-load-balance)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/manual-load-balance)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud clusters can run with one of three load balancing modes: integrated, bundled, or manual. With integrated mode, Google Distributed Cloud uses the F5 BIG-IP load balancer. With bundled mode, Google Distributed Cloud provides and manages the load balancer. You do not have to get a license for a load balancer, and the amount of setup that you have to do is minimal. With manual mode, Google Distributed Cloud uses a different load balancer of your choice. Manual load balancing mode requires that you do more configuration than with integrated mode. This page describes the steps you need to take if you choose to use the manual load balancing mode.

The [Citrix load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/citrix-load-balance) is an example load balancer that you could use with manual load balancing mode.

In this topic, you set aside IP addresses and `nodePort` values for later use. The idea is that you choose the IP addresses and `nodePort` values that you want to use for load balancing and for your cluster nodes. But you don't do anything with the addresses and `nodePort` values at this point. Later, when you are ready to create your clusters, you will need the addresses and `nodePort` values to fill in your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file) and your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-cluster-configuration-file). You will also need the addresses and `nodePort` values when you manually configure your load balancer.

## Setting aside node IP addresses

With manual load balancing mode, you cannot use DHCP. You must specify static IP addresses for your cluster nodes. You need to set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. For details about how many node IP addresses to set aside, see [Creating an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-cluster#network) and [Creating a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-user-cluster#network).

## Setting aside virtual IP addresses

Regardless of whether you use integrated, bundled or manual load balancing mode, you must set aside several virtual IP addresses (VIPs) that you intend to use for load balancing. These VIPs allow external clients to reach your Kubernetes API servers, your ingress service, and your add-on service for log integration.

Set aside the following VIPs:

  * VIP for the Kubernetes API server of the admin cluster. In the admin cluster configuration file, this is called `controlPlaneVIP`.

  * VIP for add-on service for log aggregation, which runs in the admin cluster. In the admin cluster configuration file, this is called `addonsVIP`.

  * For each user cluster you intend to create, a VIP for the Kubernetes API server of the user cluster. In the user cluster configuration file, this is called `controlPlaneVIP`.

  * For each user cluster you intend to create, a VIP for ingress service in the user cluster. In the user cluster configuration file, this is called `ingressVIP`.




## Setting aside `nodePort` values

In Google Distributed Cloud, the Kubernetes API server, the ingress service, and the add-on service for log aggregation are exposed by [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service). With manual load balancing mode, you must choose your own `nodePort` values for these Services. Choose values in the 30000 - 32767 range. After you choose your `nodePort` values, set them aside for later when you fill in your cluster configuration files.

Choose and set aside the following `nodePort` values.

  * For the VIP that you have set aside for the Kubernetes API server of the admin cluster, set aside one `nodePort` value.

  * For the VIP that you have set aside for the add-on service, set aside one `nodePort` value.

  * For each VIP that you have set aside for Kubernetes API servers of user clusters, set aside one `nodePort` value.

  * For each VIP that you have set aside for the ingress service of a user cluster, set aside two `nodePort` values: one for HTTP traffic and one for HTTPS traffic.




For example, suppose you intend to have an admin cluster and two user clusters. You would need to choose and set aside the following `nodePort` values:

  * A `nodePort` value for the Kubernetes API server of the admin cluster.

  * A `nodePort` value for add-on service in the admin cluster.

  * For each of two user clusters, a `nodePort` value for the Kubernetes API server.

  * For each of two user clusters, a `nodePort` value for HTTP traffic to the ingress service.

  * For each of two user clusters, a `nodePort` value for HTTPS traffic to the ingress service.




So in the preceding example, you would need to set aside eight `nodePort` values.

## Filling in the cluster configuration files

Prepare a configuration file for your admin cluster and a configuration file for each of your user clusters.

In each cluster configuration file:

  * Set `loadBalancer.kind` to `ManualLB`.

  * Set `network.ipMode` to `static`.

  * Set `network.ipBlockFilePath` to the path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/ip-block-file) for the cluster.

  * Update the `loadBalancer.manualLB` section with the `nodePort` values you have chosen for the cluster.




The following example shows a portion of a user cluster configuration file:
    
    
    network:
      ipMode:
        type: static
        ipBlockFilePath: "ipblock1.yaml"
    loadBalancer:
      kind: ManualLB
      manualLB:
        ingressHTTPNodePort: 30243
        ingressHTTPSNodePort: 30879
        konnectivityServerNodePort: 30563
        controlPlaneNodePort: 30562
    

## Configure your load balancer

### Admin cluster

In your admin cluster configuration file, you filled in the following:

  * `loadBalancer.vips.controlPlaneVIP`
  * `loadBalancer.vips.addonsVIP`
  * `loadBalancer.manualLB.controlPlaneNodePort`
  * `loadBalancer.manualLB.addonsNodePort`
  * `network.ipMode.ipBlockFilePath`



In the IP Block file for your admin cluster, you filled in a list of static IP addresses to use for your admin cluster nodes.

Use your load balancer's management console or tools to configure the following mappings in your load balancer. How you do this depends on your load balancer:

  * (`controlPlaneVIP`:443) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)

  * (`addonsVIP`:8443) -> (NODE_IP_ADDRESSES:`addonsNodewPort`)




### User cluster

In your user cluster configuration files, you filled in the following:

  * `loadBalancer.vips.controlPlaneVIP`
  * `loadBalancer.vips.ingressVIP`
  * `loadBalancer.manualLB.controlPlaneNodePort`
  * `loadBalancer.manualLB.konnectivityServerNodePort`
  * `loadBalancer.manualLB.ingressHTTPNodePort`
  * `loadBalancer.manualLB.ingressHTTPSNodePort`
  * `network.ipMode.ipBlockFilePath`



In the IP Block file for your user cluster, you filled in a list of static IP addresses to use for your user cluster nodes.

Use your load balancer's management console or tools to configure the following mappings in your load balancer. How you do this depends on your load balancer:

  * (`controlPlaneVIP`:443) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)

  * (`controlPlaneVIP`:8132) -> (NODE_IP_ADDRESSES:`konnectivityServerNodePort`)

  * (`ingressVIP`:80) -> (NODE_IP_ADDRESSES:`ingressHTTPNodePort`)

  * (`ingressVIP`:443) -> (NODE_IP_ADDRESSES:`ingressHTTPSNodePort`)




### Resetting connections to failed nodes (Recommended)

In addition to the preceding requirements, we recommend you configure the load balancer to reset client connections when it detects a backend node failure. Without this configuration, clients of the Kubernetes API server can stop responding for several minutes when a server instance goes down, which can cause instability in the Kubernetes control plane.

  * With F5 BIG-IP, this setting is called Action On Service Down in the backend pool configuration page.
  * With HAProxy, this setting is called on-marked-down shutdown-sessions in the backend server configuration.
  * If you are using a different load balancer, you should consult the documentation to find the equivalent setting.



## Getting support for manual load balancing

Google does not provide support for load balancers configured using manual load balancing mode. If you encounter issues with the load balancer, reach out to the load balancer's vendor.

## What's next

  * [Load balancing with Citrix](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/citrix-load-balance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
