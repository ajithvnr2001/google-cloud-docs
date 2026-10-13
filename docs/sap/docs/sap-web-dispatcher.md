---
url: https://docs.cloud.google.com/sap/docs/sap-web-dispatcher/
title: Standalone SAP Web Dispatcher high-availability deployment on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:13.704460+00:00
---

# Standalone SAP Web Dispatcher high-availability deployment on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-web-dispatcher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Standalone SAP Web Dispatcher high-availability deployment on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides you an overview of how you can deploy a standalone SAP Web Dispatcher high-availability (HA) system on Google Cloud using Cloud Load Balancing. 

SAP Web Dispatcher balances the load of the incoming HTTP/HTTPS requests for your SAP NetWeaver application servers, or ABAP or Java systems. For information from SAP about SAP Web Dispatcher, see [SAP Web Dispatcher](https://help.sap.com/doc/saphelp_nw74/7.4.16/en-us/48/8fe37933114e6fe10000000a421937/frameset.htm).

## Deployment architecture

The following diagram shows the recommended deployment architecture for standalone SAP Web Dispatcher HA on Google Cloud:

![Architecture diagram for the deployment of a standalone SAP Web Dispatcher high-availability system on Google Cloud](https://docs.cloud.google.com/static/sap/docs/images/sap-web-dispatcher-standalone-ha.svg)

To provide high availability for SAP Web Dispatcher running on Google Cloud, you must include the following components in your deployment:

  * An active-active setup of two or more SAP Web Dispatcher instances.
  * A Google Cloud Internal Application Load Balancer.



An active-active setup ensures that both instances of SAP Web Dispatcher remain active to receive traffic from the internal Application Load Balancer and forward or redirect that traffic to your backend SAP system. You achieve an active-active setup by deploying at least two instances of SAP Web Dispatcher, with each instance running in separate Compute Engine [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).

The internal Application Load Balancer distributes traffic to the two SAP Web Dispatcher instances. The load balancer distributes traffic that comes from both - clients that are in the same Virtual Private Cloud (VPC) network as the load balancer, and clients like on-premise systems that are connected to the load balancer's VPC network through services such as VPC Network Peering, Cloud VPN, or Cloud Interconnect.

This setup of SAP Web Dispatcher provides zero maintenance downtime, which ensures high availability. Health check rules associated with the internal Application Load Balancer ensure that the incoming traffic is routed to the available SAP Web Dispatcher instance. This also helps you perform maintenance activities, as rolling updates, on those instances. The health checks also help you determine if your SAP Web Dispatcher instances are able to reach your backend SAP system. For more information, see [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal).

## High-level deployment steps

The following are the high-level steps, with some essential details, for deploying standalone SAP Web Dispatcher HA on Google Cloud:

  1. Make sure that you meet the following prerequisites:

     * You have a Google Cloud account and project.
     * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  2. Create at least two unmanaged instance groups, each in a different [zone](https://docs.cloud.google.com/compute/docs/regions-zones).

For instructions, see [Creating groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#create_unmanaged_group) in the Compute Engine documentation.

  3. In each unmanaged instance group, on a VM instance that uses an SAP-supported VM type and an SAP-supported OS image, install SAP Web Dispatcher.

For information about installing SAP Web Dispatcher, see [SAP Web Dispatcher](https://help.sap.com/docs/ABAP_PLATFORM_NEW/683d6a1797a34730a6e005d1e8de6f22/488fe37933114e6fe10000000a421937.html?locale=en-US).

**Note:**
     * Make sure to create ingress `allow` firewall rules so that traffic from your SAP Web Dispatcher instances can connect to your backend SAP system.
     * To verify the configuration of your SAP Web Dispatcher instances, see [Running the Configuration Check](https://help.sap.com/doc/saphelp_nw74/7.4.16/en-us/48/997375ec0973e9e10000000a42189b/frameset.htm).
  4. Create a [regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal#load-balancer-mode) (HTTP/HTTPS) with the following configuration:

     1. In the **Internet facing or internal only** section, select **Only between my VMs or serverless services**.

     2. In the **Region** field, select the region where you have deployed your SAP Web Dispatcher instances.

     3. Select the required VPC network.

     4. Make sure to reserve a proxy-only subnet for this VPC network. For more information, see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).

     5. In the **Backend configuration** section, create a backend service. Example settings for the backend service:

        * **Backend type** : `Instance group`
        * **Protocol** : `HTTP` (default)
        * **Named port** : `http` (default)
        * **Timeout** : 30 seconds (default)
     6. In the **Backend** section, add a backend for each instance group in your SAP Web Dispatcher setup:

        * In the **Instance group** field, select an instance group that you created earlier in this procedure.
        * For the **Port** field, specify the port where your SAP Web Dispatcher instance is running.
     7. For the backend service, create a health check that probes the port where the SAP Web Dispatcher instance is running. Example health check settings:

        * **Protocol** : `TCP`
        * **Port** : specify the port where your SAP Web Dispatcher instance is running
        * **Check interval** : 5 seconds
        * **Timeout** : 5 seconds
        * **Healthy threshold** : 2 seconds
        * **Unhealthy threshold** : 2 seconds
**Note:** For health checks to work, you must create ingress `allow` firewall rules so that traffic from Google Cloud probers can connect to your backend SAP system. For more information, see [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).
     8. In the **Routing rules** section:

        * In the **Mode** field, select **Simple host and path rule**.
        * In the **Host and path rules** section, make sure that there is an entry for the backend service that you created.
     9. In the **Frontend configuration** section:

        * Specify the IP address and port where you want the load balancer to receive traffic.
        * If you want to receive traffic from regions other than the one you specified, then in the **Global access** field, select **Enable**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
