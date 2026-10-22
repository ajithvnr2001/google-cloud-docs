---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/f5-big-ip-manual/
title: Manually setup F5 BIG-IP virtual servers for manual load balancing \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:20.142513+00:00
---

# Manually setup F5 BIG-IP virtual servers for manual load balancing  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/f5-big-ip-manual/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Manually setup F5 BIG-IP virtual servers for manual load balancing Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to set up the [F5 BIG-IP](https://www.f5.com/products/big-ip-services) when you [integrate with Google Distributed Cloud ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs) using the [manual load-balancing mode on Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

The F5 BIG-IP platform provides various services to help you enhance the security, availability, and performance of your apps. These services include, L7 load balancing, network firewalling, [web application firewalling (WAF)](https://wikipedia.org/wiki/Web_application_firewall), DNS services, and more. For Google Distributed Cloud, BIG-IP provides external access and L3/4 load-balancing services.

### Additional configuration

After the Setup utility completes, you need to [Create an administrative partition](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-12-0-0/3.html) for each user cluster you intend to expose and access.

Initially, you define a partition for the first user cluster. Don't use cluster partitions for anything else. Each of the clusters must have a partition that is for the sole use of that cluster.

### Configuring the BIG-IP for Google Distributed Cloud external endpoints

If you didn't [disable bundled ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress), you must [configure the BIG-IP with the virtual servers](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#cp-v2-user-cluster_4) (VIPs), corresponding to the following Google Distributed Cloud endpoints:

  * **User partition**

    * VIP for user cluster ingress controller (port exposed: `443`)
    * VIP for user cluster ingress controller (port exposed: `80`)

**Note:** Because Google Distributed Cloud blocks creating clusters with [legacy features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features), this document doesn't cover the BIG-IP configuration for legacy features. 

#### Create node object

The cluster node external IP addresses are in turn used to configure node objects on the BIG-IP system. You will create a node object for each Google Distributed Cloud cluster node. The nodes are added to backend pools that are then associated with virtual servers.

**Important:** If you choose [DHCP IP Mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field), you need to update IP addresses for each node object on the BIG-IP system once the Google Distributed Cloud cluster node IP addresses changed. 

  1. To sign in to the BIG-IP management console, go to the IP address. The address is provided during the installation.
  2. Click the **User partition** that you previously created.
  3. Go to **Local Traffic** > **Nodes** > **Node List**.
  4. Click **Create**.
  5. Enter a name and IP address for each cluster host and click **Finished**.

![Configuration of partitions.](https://docs.cloud.google.com/static/architecture/images/partners/installing-f5-big-ip-adc-for-gke-on-prem-using-manual-load-balancing-7-configure-partitions.png)




#### Create backend pools

You create a backend pool for each node Port.

  1. In the BIG-IP management console, click **User partition** for the user partition that you previously created.
  2. Go to **Local Traffic** > **Pools** > **Pool List**.
  3. Click **Create**.
  4. In the **Configuration** drop-down list, click **Advanced**.
  5. In the **Name** field, enter `Istio-80-pool`.
  6. To verify the pool member accessibility, under **Health Monitor** , click **tcp**. Optional: Because this is a manual configuration, you can also take advantage of more [advanced monitors](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-local-traffic-manager-monitors-reference-13-1-0.html) as appropriate for your deployment.
  7. For **Action on Service Down** , click **Reject**.

  8. For this tutorial, in the **Load Balancing Method** drop-down list, click **Round Robin**.

  9. In the **New Members** section, click **Node List** and then select the previously created node.

  10. In the **Service Port** field, enter the appropriate `nodePort` from the [configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#cp-v2-user-cluster_2) or `spec.ports[?].nodePort` in the runtime istio ingress Kubernetes Service (name: `istio-ingress`, namespace: `gke-system`).

  11. Click **Add**.

  12. Repeat steps 8-9 and add each cluster node instance.

![Configuration of cluster node.](https://docs.cloud.google.com/static/architecture/images/partners/installing-f5-big-ip-adc-for-gke-on-prem-using-manual-load-balancing-9-cluster-node.png)

  13. Click **Finished**.

  14. Repeat all of these steps in this section for the remaining [user cluster nodePorts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#cp-v2-user-cluster_4).




#### Create virtual servers

You create a total of two virtual servers on the BIG-IP for the first user cluster. The virtual servers correspond to the "VIP + port" combinations.

  1. In the BIG-IP management console, click the **User partition** that you previously created.
  2. Go to **Local Traffic** > **Virtual Servers** > **Virtual Server List**.
  3. Click **Create**.
  4. In the **Name** field, enter `istio-ingress-80`.
  5. In the **Destination Address/Mask** field, enter the IP address for the VIP. For this tutorial, use the HTTP ingress VIP in the [`configuration file`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#cp-v2-user-cluster_1) or `spec.loadBalancerIP` in the runtime istio ingress Kubernetes Service (name: `istio-ingress`, namespace: `gke-system`).

**Warning:** Don't setup a virtual server for `controlPlaneVIP`.
  6. In the **Service Port** field, enter the appropriate listener port for the VIP. For this tutorial, use port `80` or `spec.ports[?].port` in the runtime istio ingress Kubernetes Service (name: `istio-ingress`, namespace: `gke-system`).

![Configuration of virtual servers.](https://docs.cloud.google.com/static/architecture/images/partners/installing-f5-big-ip-adc-for-gke-on-prem-using-manual-load-balancing-10-virtual-servers.png)

There are several configuration options for enhancing your app's endpoint, such as associating protocol-specific profiles, [certificate profiles](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-13-1-0/6.html#guid-cc146765-9237-474b-9faf-0e18a208cb23), and [WAF policies](https://support.f5.com/csp/article/K85426947).

  7. For **Source Address Translation** click **Auto Map**.

  8. For **Default Pool** select the appropriate pool that you previously created.

  9. Click **Finished**.

  10. [Create and download an archive of the current configuration](https://support.f5.com/csp/article/K4423).




### What's next

  * To further enhance the security and performance of the external-facing VIPs, consider the following:

    * [F5 Advanced WAF](https://www.f5.com/products/security/advanced-waf)
    * [F5 Access Policy Manager (APM)](https://www.f5.com/products/security/access-policy-manager)
    * [Caching & Compression](https://www.f5.com/products/big-ip-services/local-traffic-manager)
    * [Health monitoring](https://techdocs.f5.com/en-us/bigip-15-0-0/big-ip-local-traffic-manager-implementations/implementing-health-and-performance-monitoring.html)
    * [Intelligent application traffic management](https://www.f5.com/products/big-ip-services/local-traffic-manager)
  * Learn more about F5 [BIG-IP Application Services](https://www.f5.com/products/big-ip-services).

  * Learn more about BIG-IP configurations and capabilities:

    * [Certificate profiles](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-13-1-0/6.html#guid-cc146765-9237-474b-9faf-0e18a208cb23)
    * [WAF policies](https://support.f5.com/csp/article/K85426947)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
