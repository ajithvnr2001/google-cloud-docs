---
url: https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic/
title: Assign static IP addresses for outbound traffic \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:13.368932+00:00
---

# Assign static IP addresses for outbound traffic  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Assign static IP addresses for outbound traffic Stay organized with collections  Save and categorize content based on your preferences. 

By default, Secure Web Proxy uses a managed [Cloud NAT](https://docs.cloud.google.com/secure-web-proxy/docs/use-cloud-nat-for-swp) gateway (`swg-autogen-nat`) for outbound web traffic, which typically uses automatically allocated IP addresses. This page describes how to configure the Cloud NAT gateway to use a specific set of static external IPv4 addresses that you own and manage in your Google Cloud project. All outbound traffic from your workloads that's routed through the Secure Web Proxy then originates from one of these predefined static IPs.

**Note:** This setting is an advanced configuration setting for Secure Web Proxy. We recommend that you use the process explained on this page only if it's necessary to implement this specific setting for your workload.

Here are a few key benefits of assigning static IP addresses for your outbound traffic:

  * **Predictable outbound traffic source IPs** : enables external services, partners, and on-premises firewalls to add your specific IP addresses to their authorized lists, ensuring that traffic from your Secure Web Proxy instance is accepted. This is essential for accessing resources that are protected by IP-based access control lists (ACLs).

  * **Dynamic port allocation (DPA)** : efficiently allocates available source ports from the set of static IP addresses that you assign for outbound traffic. DPA lets your workloads manage outbound traffic with a limited number of static IPs, without using up all the available ports. For more information, see [Dynamic port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port).

  * **Enhanced security posture** : provides a smaller, known set of IP addresses to manage and monitor, simplifying security audits and threat analysis.

  * **Improved third-party integration** : facilitates seamless integration with SaaS providers and APIs that require or recommend IP allowlists for enhanced security.

  * **Simplified compliance** : helps you meet compliance requirements for all outbound traffic points and their associated IP addresses.




## Before you begin

  * Complete the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  * Reserve a list of static IPv4 addresses to use for your Secure Web Proxy instance. Before reserving IP addresses in Google Cloud, make sure that you create an address resource by using the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).

  * Verify that you have the Google Cloud CLI version 406.0.0 or later installed:
        
        gcloud version | head -n1
        

If you have an earlier gcloud CLI version installed, update the version:
        
        gcloud components update --version=406.0.0
        




## Configure static IP addresses for Secure Web Proxy

###  Console 

  1. In the Google Cloud console, go to the **Cloud Nat** page.

[Go to Cloud Nat](https://console.cloud.google.com/net-services/nat/list)

  2. Locate the Cloud NAT gateway that your Secure Web Proxy instance uses. Its name would be `swg-autogen-nat`, and it would be associated with a Cloud NAT (with a name in the `swg-autogen-router-YYYY` format) in the appropriate region and Virtual Private Cloud network.

  3. To go to the details page of the Cloud NAT gateway, click the `swg-autogen-nat` gateway name. The **Cloud NAT gateway details** page opens.

  4. Click **Edit**. The **Edit Cloud NAT gateway** page opens.

  5. For **Cloud NAT IP addresses** , change the setting from **Automatic (recommended)** to **Manual**.

  6. For **IP addresses** , select the static IP addresses that you reserved. For more information, see [Configure Cloud NAT IPs for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-cloud-nat-for-swp#enable-cloud-nat-for-swp).

To add multiple IP addresses, click the add_box**Add IP address** button.

  7. Expand the **Advanced configurations** section, and then select the **Enable Dynamic Port Allocation** checkbox.

  8. For **Min ports per VM** , we recommend that you enter `2048`.

  9. For **Max ports per VM** , we recommend that you enter `4096`.

  10. Click **Save**.

  11. After saving your changes, verify the following:

     1. On the Cloud NAT gateway details page, check that the **IP addresses** section now lists your manually selected static IP addresses.

     2. Check that **Dynamic Port Allocation** is enabled for the correct minimum and maximum ports per virtual machine (VM) that you'd configured earlier.




###  Cloud Shell 

  1. To identify the Cloud Router name that was assigned while provisioning your Secure Web Proxy instance, use the [`gcloud compute routers list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list).
         
         gcloud compute routers list \
             --region REGION \
             --filter="network:(NETWORK_NAME) AND name:(swg-autogen-router-*)" \
             --format="get(name)"
         

Replace the following:

     * `REGION`: region where the Cloud Router is deployed for your Secure Web Proxy instance
     * `NETWORK_NAME`: name of your VPC network

The output is similar to the following:
    
    swg-autogen-router-1
    

  2. To list the external automatically provisioned IP addresses that were assigned while provisioning your Secure Web Proxy instance, use the [`gcloud compute routers get-status` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-status).
         
         gcloud compute routers get-status ROUTER_NAME  \
             --region=REGION
         

The output is similar to the following:
         
         kind: compute#routerStatusResponse
         result:
           natStatus:
           - autoAllocatedNatIps:
             - 34.144.80.46
             - 34.144.83.75
             - 34.144.88.111
             - 34.144.94.113
             minExtraNatIpsNeeded: 0
             name: swg-autogen-nat
             numVmEndpointsWithNatMappings: 3
           network: https://www.googleapis.com/compute/projects/PROJECT_NAME/global/networks/NETWORK_NAME
         

This output includes the following values:

     * `PROJECT_NAME`: name of your Google Cloud project
     * `NETWORK_NAME`: name of your VPC network
**Note:** In the preceding output, the `swg-autogen-nat` Cloud NAT gateway has four automatically provisioned IP addresses. The Secure Web Proxy can scale up or scale down automatically provisioned Cloud NAT IP addresses based on your Google Cloud workload.
  3. To update the Cloud NAT gateway to use your predefined IP range, use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).
         
         gcloud compute routers nats update swg-autogen-nat  \
             --router=ROUTER_NAME \
             --nat-external-ip-pool=IPv4_ADDRESSES... \
             --region=REGION
         

Replace `IPv4_ADDRESSES` with the name of the external IPv4 address resource that you intend to use, separated by a comma (`,`).

  4. To verify that your IP range is assigned to the Cloud NAT gateway, use the [`gcloud compute routers nats describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe).
         
         gcloud compute routers nats describe swg-autogen-nat \
             --router=ROUTER_NAME  \
             --region=REGION
         

The output is similar to the following:
         
         enableEndpointIndependentMapping: false
         icmpIdleTimeoutSec: 30
         logConfig:
           enable: false
           filter: ALL
         name: swg-autogen-nat
         natIpAllocateOption: MANUAL_ONLY
         natIps:
         - https://www.googleapis.com/compute/projects/PROJECT_NAME/regions/REGION/addresses/ADDRESS
         sourceSubnetworkIpRangesToNat: ALL_SUBNETWORKS_ALL_IP_RANGES
         

This output includes the following values:

     * `PROJECT_NAME`: name of your Google Cloud project
     * `REGION`: region where the Cloud NAT gateway is deployed
     * `ADDRESS`: name of the static IPv4 address resource
  5. To update the Cloud NAT gateway to use the dynamic port allocation (DPA) mode, use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update). DPA mode enables your Secure Web Proxy instance to use the assigned IP addresses.
         
         gcloud compute routers nats update swg-autogen-nat  \
             --router=ROUTER_NAME \
             --min-ports-per-vm=2048 \
             --max-ports-per-vm=4096 \
             --enable-dynamic-port-allocation \
             --region=REGION
         

For the `--min-ports-per-vm` and `--max-ports-per-vm` flags, we recommend that you set their values to `2048` and `4096`, respectively.

Use [Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-selector#basic-advanced-mode) to monitor metrics data for the following and adjust DPA minimum and maximum values as needed:

     * `Cloud NAT Gateway - Port usage`
     * `Cloud NAT Gateway - New connection count`
     * `Cloud NAT Gateway - Open connections`
  6. To verify that your DPA is enabled and the minimum and maximum port values are set, use the [`gcloud compute routers nats describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe).
         
         gcloud compute routers nats describe swg-autogen-nat \
             --router=ROUTER_NAME \
             --region=REGION
         

Check the output for `natIpAllocateOption: MANUAL_ONLY` to verify that the `natIps` list includes your static IP addresses.

The output is similar to the following:
         
         enableDynamicPortAllocation: true
         enableEndpointIndependentMapping: false
         endpointTypes:
         - ENDPOINT_TYPE_SWG
         logConfig:
           enable: true
           filter: ERRORS_ONLY
         maxPortsPerVm: 4096
         minPortsPerVm: 2048
         name: swg-autogen-nat
         natIpAllocateOption: MANUAL_ONLY
         natIps:
         - https://www.googleapis.com/compute/projects/PROJECT_NAME/regions/REGION/addresses/ADDRESS
         sourceSubnetworkIpRangesToNat: ALL_SUBNETWORKS_ALL_IP_RANGES
         type: PUBLIC
         

This output includes the following values:

     * `PROJECT_NAME`: name of your Google Cloud project
     * `REGION`: region where the Cloud NAT gateway is deployed
     * `ADDRESS`: name of the static IPv4 address resource



## What's next?

  * [Use Cloud NAT for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-cloud-nat-for-swp)
  * [Use tags to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags)
  * [Use URL lists to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
