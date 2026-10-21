---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-self-hosted/
title: Introduction to self-hosted data sources \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:14.510802+00:00
---

# Introduction to self-hosted data sources  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-self-hosted/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Introduction to self-hosted data sources Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise can securely connect to customer-managed, self-hosted, third-party data sources. These connections are established through Private Service Connect producer services.

This connectivity model ensures that sensitive data remains in your control and network boundaries, while allowing Gemini Enterprise to access and use the information contained within these data sources. Using Private Service Connect lets you establish a secure and scalable communication channel, bypassing the public internet and minimizing potential security risks associated with traditional network configurations.

![Access patterns for self-hosted data sources.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/self-hosted-access.png)Access patterns for self-hosted data sources

Gemini Enterprise supports the following self-hosted data source patterns:

  * **On-premises or multi-cloud:** Data sources deployed in your data center or in another cloud provider (for example, Amazon Web Services EC2 or EKS, or Microsoft Azure virtual machines), using hybrid network connectivity.

  * **Google Kubernetes Engine:** Data sources hosted within GKE clusters.

  * **Google Cloud Compute Engine:** Data sources deployed on Google Compute Engine VMs.




## Using Private Service Connect with self-hosted services

Private Service Connect is a Google Cloud networking feature that enables private access from a consumer's Virtual Private Cloud network to managed services. It creates a secure, explicit connection between a service consumer and a service producer, eliminating the need for Virtual Private Cloud peering, complex routing, or public IP addresses.

You can set up a Gemini Enterprise Private Service Connect deployment with the following:

  * Gemini Enterprise as the service consumer

  * Your network, containing load balancers that reference on-premises, multi-cloud, or Google Cloud compute resources, as the service producer




For information about specific aspects of using Private Service Connect to connect your self-hosted service to Gemini Enterprise, see the following sections.

### VPC network and subnet configuration

Keep the following in mind:

  * Proxy allocation is at the VPC level, not at the load balancer level. You must create one [proxy-only subnet](https://cloud.google.com/load-balancing/docs/proxy-only-subnets) in each region of a virtual network (VPC) in which you use Envoy-based load balancers. If you deploy multiple load balancers in the same region and same VPC network, they share the same proxy-only subnet for load balancing.

  * [Health check probes](https://cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks) originate from the Envoy proxies located in the [proxy-only subnet](https://cloud.google.com/load-balancing/docs/proxy-only-subnets) within the region. For the health check probes to function correctly, you must create firewall rules in the external environment that allow traffic from the proxy-only subnet to reach your external backends.

  * The proxy-only subnet is the source subnet targeting the cross cloud database. Ensure that this subnet is advertised by a Cloud Router. For more information, see [Advertise specific VPC subnets](https://cloud.google.com/network-connectivity/docs/router/how-to/advertising-subnets).

  * The proxy-only subnet must be on the allowlist for the on-premises or Cross-Cloud firewall.

  * You must create proxy-only subnets regardless of whether your VPC network is auto mode or custom. A proxy-only subnet must provide 64 or more IP addresses. This corresponds to a prefix length of /26 or shorter. The recommended subnet size is /23 (512 proxy-only addresses).




#### Private Service Connect NAT subnet

Packets from the consumer VPC network are translated using source NAT (SNAT), so that their original source IP addresses are converted to source IP addresses from the NAT subnet in the producer's VPC network. Private Service Connect for NAT subnets cannot host workloads.

The minimum subnet size for a Private Service Connect NAT is /29. You can add additional NAT subnets to a service attachment at any time, without interrupting traffic.

You can [monitor published services](https://cloud.google.com/vpc/docs/monitor-private-service-connect-connections) using either predefined dashboards or Google Cloud metrics for Private Service Connect NAT consumption.

### Load balancer configuration

A service producer places its application or service behind a [Google Cloud Internal Load Balancer](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#lb-types). We recommend that you use an Internal TCP Proxy Load Balancer. If using Google Kubernetes Engine, you can use an internal passthrough Network Load Balancer.

**Note:** Each load balancer's forwarding rule can be associated with a single service attachment. You can't associate multiple service attachments with the same forwarding rule.

Because Gemini Enterprise is [not available in all locations](https://cloud.google.com/gemini/enterprise/docs/locations), you must enable global access when creating the internal load balancer forwarding rule. If you don't enable global access, then endpoint creation for Gemini Enterprise (the service consumer) can fail. Ensure that you have enabled global access before you create the Private Service Connect service attachment. For more information about client access for internal load balancers, see [Client access](https://cloud.google.com/load-balancing/docs/internal#client-access).

### Service attachment configuration

To publish a service using Private Service Connect, a service producer [creates a service attachment](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service). This attachment enables service consumers, such as Gemini Enterprise, to connect to the producer's service. For information about publishing a service and creating a service attachment, see [Publish a service](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service).

The service producer has two primary options for controlling consumer connections, managed using the following connection preferences:

  * **Automatically accept all connections** : This allows any consumer to connect, without explicit approval.

  * **Accept connections for selected projects** (explicit approval): This requires you to manually approve each project that requests a connection. With this option, you can choose to accept or reject a project.

If you use explicit project approval, then in order to establish a connection to your service attachment, you must do the following:

    1. Create a data store (for example, a [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc) data store).

    2. In the **Private Service Connect** page of the Google Cloud console, accept the pending connection from the Gemini Enterprise tenant project for your new data store. You can identify the tenant project by its project ID, which ends in `-tp`. For more information, see [Manage requests for access to a published service](https://cloud.google.com/vpc/docs/manage-private-service-connect-services#access).

    3. In the **Gemini Enterprise** page of the Google Cloud console, in **Data stores** , click the name of your new data store to see its status. The data store status is shown on its **Data** page.

You can't see the Gemini Enterprise tenant project ID until you create a data store. The data store status remains as **Creating** until you accept the project connection in Private Service Connect.


**Note:** Gemini Enterprise doesn't support the **Accept connections for selected networks** connection preference.

When creating a service attachment, don't select the [proxy protocol](https://cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol) unless it's supported by the self-hosted service. Doing so results in a SSL/TLS error. You can deselect the proxy protocol by editing the service attachment.

### Firewall configuration

Configure [ingress firewall rules](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#firewall-rules) to allow traffic between the Private Service Connect NAT subnet and the backend VMs in the producer service load balancer. If you're using a hybrid or internet NEG as the backend, firewall rules are not required.

## What's next

  * For more information about how Gemini Enterprise integrates with Private Service Connect, see the following codelabs on Google Developer Codelabs:

    * [Gemini Enterprise to Zonal NEG self-hosted database](https://codelabs.developers.google.com/agentspace-psc-zonal-neg)

    * [Gemini Enterprise Hybrid NEG to Cross Cloud self-hosted database](https://codelabs.developers.google.com/agentspace-psc-hybrid-neg-crosscloud)

    * [Gemini Enterprise Custom Domain](https://codelabs.developers.google.com/agentspace-networking-customdomain)

    * [Gemini Enterprise Custom Domain, WIF Support](https://codelabs.developers.google.com/agentspace-networking-customdomain-wif)

  * For more information on using an internal load balancer across VPC networks on Google Kubernetes Engine, see [Create an internal load balancer across VPC networks](https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
