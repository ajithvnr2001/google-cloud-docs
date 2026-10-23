---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-tiers/
title: Configure external traffic with Network Service Tiers \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:38.692578+00:00
---

# Configure external traffic with Network Service Tiers  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-tiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure external traffic with Network Service Tiers Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to control how external traffic reaches your Services on Google Kubernetes Engine (GKE) clusters by using [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview). Network Service Tiers lets you optimize your network traffic for either performance (Premium Tier) or cost savings (Standard Tier).

Premium Tier delivers traffic on Google's premium backbone network for superior speed and reliability. In contrast, Standard Tier uses regular Internet service provider (ISP) networks that offers a more cost-effective solution.

This page is for Cloud architects and Networking specialists who design and architect their organization's network. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## How Network Service Tiers work in GKE

This section shows you how to manage Network Service Tiers in GKE.

  * **Set a network tier at the project level** : you can set the default network tier for your Google Cloud project to use either Standard Tier or Premium Tier. All new clusters are created with the `network-default` setting, which inherits the project-level tier setting. This setting persists through cluster upgrades. Node pools created within the cluster inherit the network tier from the project-level configuration.

  * **Set a network tier when creating new clusters** : you can configure the network tier when you create a new cluster regardless of the tier setting on your Google Cloud project. New node pools use the cluster-level network tier, and this configuration persists even after you upgrade the node pools.

  * **Set a network tier when updating clusters** : you can configure the network tier when you update an existing cluster. New node pools and new LoadBalancer Services inherit the updated tier configuration, while existing node pools and Services continue to use the original network tier configuration. The updated tier configuration persists after you upgrade your cluster.

  * **Set a network tier when updating LoadBalancer Services** : LoadBalancer Services inherit the network tier of the cluster. However, you can override this setting and update the network tier in the Service manifest.




### Network Service Tiers and load balancing

By default, Regional external passthrough Network Load Balancers use Premium Tier. You can update this configuration so that the LoadBalancer Service uses Standard Tier instead.

If you use Application Load Balancers with Gateway, you can't configure the Network Service Tiers. Network Service Tiers on Gateway are controlled by the GatewayClass resource. For more information, see [Gateway IP address](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities#gateway_ip_address).

GKE Ingress for external Application Load Balancers does not support Standard Tier for traffic routing.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Restrictions

The following restrictions apply:

  * You can configure network tier settings only at the project level or cluster level. You can't configure the network tier of node pools directly.
  * Standard Tier is not supported for global external dual-stack IPv4 or IPv6 addresses. For more information about the types of IP addresses, see [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).



## Create a cluster with Network Service Tiers

To create a cluster and specify the network tier, run the following command:
    
    
     gcloud container clusters create CLUSTER_NAME \
         **--network-tier =NETWORK_TIER** \
         ...
    

Replace the following values:

  * `CLUSTER_NAME`: the name of your cluster.
  * `NETWORK_TIER`: the network tier setting. Use `network-default` for the same tier setting as that on your Google Cloud project, `Standard` for Standard Tier or `Premium` for Premium Tier.



## Migrate an existing cluster to a different tier

Updating the network tier of a cluster does not affect the network tier of existing resources. Existing resources continue to use the IP address associated with the old network tier. To avoid service disruptions, follow these steps when you migrate your cluster to a new network tier:

  1. **Update the cluster** : to update an existing cluster with a network tier, run the following command:
         
         gcloud container clusters update CLUSTER_NAME \
             **--network-tier =NETWORK_TIER** \
             ...
         

Replace the following values:

     * `CLUSTER_NAME`: the name of your cluster.
     * `NETWORK_TIER`: the network tier setting. Use `network-default` for the same tier setting as that on your Google Cloud project, `Standard` for Standard Tier or `Premium` for Premium Tier.
  2. **Create new node pools and Services** : in order for external clients use the new IP addresses associated with the new network tier, you must create new node pools and new LoadBalancer Services. New node pools and new LoadBalancer Services inherit the updated tier configuration, while existing node pools and Services continue to use the original network tier configuration.

  3. **Update DNS records** : change your DNS records to point to the new IP addresses of the new LoadBalancer Services.

  4. **Wait for DNS to propagate** : wait for the DNS Time to Live (TTL) to expire to ensure clients are directed to the new services and to avoid serving stale records.




## Update an external load balancer with Network Service Tiers

For Regional external passthrough Network Load Balancers, GKE defaults to using the network tier that's configured on the cluster for the external forwarding rule and IP address. If the cluster's network tier is set to `network-default`, the load balancer uses Premium Tier. You can override this setting by configuring the `cloud.google.com/network-tier` annotation in the Service manifest. For example:
    
    
        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: store-v1-lb-svc
          **annotations :**
            **cloud.google.com/network-tier: Standard**
        spec:
          type: LoadBalancer
          loadBalancerClass: networking.gke.io/l4-regional-external
          selector:
            app: store
          ports:
          - name: tcp-port
            protocol: TCP
            port: 8080
            targetPort: 8080
        ```
    

For more information about the parameters used for LoadBalancer Services, see [Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#service_parameters).

**Static IP address** : when you create a Service with a [static IP address](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#spd-static-ip), the network tier of the static IP address must match the network tier of the LoadBalancer Service. If there is a mismatch, you see the following error message when you run the `kubectl describe service` command:
    
    
    Error syncing load balancer: failed to ensure load balancer: requested ip "standard-service" is neither static nor assigned to the LB
    

## What's next

  * Read the [overview of Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview).
  * Learn how to [create a backend service-based external load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
