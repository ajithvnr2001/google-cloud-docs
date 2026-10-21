---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises/
title: Configure on-premises DNS for management appliance access \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:29.188241+00:00
---

# Configure on-premises DNS for management appliance access  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure on-premises DNS for management appliance access

You can access management appliances, such as vCenter Server, NSX Manager, and HCX, on a private cloud from on-premises workstations. To access these appliances by hostname, you must configure DNS so that your on-premises network can resolve their hostnames.

## Configure global address resolution by using Cloud DNS

VMware Engine can use Cloud DNS to provide global DNS resolution for management appliances, even if your private clouds are in different regions. With this approach, you can use a Cloud DNS zone in your project as a single point for DNS resolution across all peered Virtual Private Cloud (VPC) networks.

We recommend using Cloud DNS for address resolution in the following cases:

  * You're using standard VMware Engine networks.
  * You're using legacy VMware Engine networks and have multiple private clouds.



If you use a legacy network with only a single private cloud and don't want to use Cloud DNS, see Configure address resolution without using Cloud DNS.

When you connect a VMware Engine network to your VPC network, Google automatically configures DNS resolution for management appliances from Google Cloud VMs in that VPC network:

  * For standard networks: When you create a private cloud that is linked to a standard VMware Engine network, Google creates an associated management DNS zone and automatically populates it with the management appliance entries.

If this standard VMware Engine network is [Virtual Private Cloud peered](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network) with a VPC network or another VMware Engine network, Google automatically creates a [management DNS zone binding](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-private-cloud-management-dns). This binding ensures resolution of management appliances from your Google Cloud VMs on that network.

You can also manually create a management DNS zone binding if you don't want to use Virtual Private Cloud Network Peering.

  * For legacy networks: When you create a [private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#creating-connection) between your Virtual Private Cloud network and a legacy VMware Engine network, Google automatically creates DNS peering, which ensures resolution from any of your Google Cloud VMs.




To resolve addresses from an on-premises network by using Cloud DNS, do the following:

  1. [Enable inbound DNS forwarding on the Virtual Private Cloud network](https://docs.cloud.google.com/dns/docs/best-practices#use_dns_server_policies_to_allow_queries_from_on-premises).
  2. [Identify the DNS server addresses to use on-premises](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints).
  3. Create a conditional forwarder on your on-premises DNS server to resolve `gve.goog`.



## Configure DNS for management appliances to resolve on-premises domains

If you use services such as HCX, Site Recovery Manager (SRM), Zerto, vSphere Replication, or cross-vCenter vMotion, you might need VMware Engine management appliances to resolve addresses in your on-premises DNS domains.

You must use Cloud DNS to forward DNS queries from management appliances to your on-premises DNS servers. This feature is available only for private clouds that use standard VMware Engine networks.

To configure DNS forwarding to your on-premises network, complete the steps in the following sections.

### Configure a Cloud DNS forwarding zone

  1. If you haven't already, [enable the Cloud DNS API](https://docs.cloud.google.com/dns/docs/set-up-dns-api) in the Google Cloud project that connects to your on-premises network.
  2. Make sure that you have a VPC network in that project with connectivity to your on-premises DNS servers, for example, by using Cloud VPN or Cloud Interconnect.
  3. [Create a Cloud DNS forwarding zone](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones#creating_a_forwarding_zone). When you create the forwarding zone, do the following: 
     * Specify a zone name, such as `forward-to-onprem`.
     * For **DNS name** , enter the DNS domain of your on-premises network, for example, `onprem.example.com`. To forward all DNS queries from management appliances to on-premises DNS servers, enter `.`.
     * Select **Forward queries to another server (outbound forwarding)**.
     * In **Destination DNS servers** , enter the IP addresses of your on-premises DNS servers.
     * In **Networks** , select the VPC network that has connectivity to your on-premises network.



### Configure your on-premises firewall

After you configure a forwarding zone, Cloud DNS sends DNS queries by using IP addresses in the range `35.199.192.0/19`. Configure your on-premises firewall rules to allow UDP and TCP traffic for port 53 from `35.199.192.0/19` to your on-premises DNS servers.

### Create a Cloud DNS peering zone

To enable VMware Engine management appliances to use the forwarding zone, create a Cloud DNS peering zone between the VMware Engine network and the project that contains the forwarding zone:

  1. Grant permission to create the DNS peering. If you're a project owner, run the [`gcloud vmware dns-bind-permission grant`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/grant) command in the project that contains your VMware Engine network:
         
         gcloud vmware dns-bind-permission grant --user=USER_EMAIL
         

Replace `USER_EMAIL` with the email address of the user who creates the peering zone, for example, `username@example.com`.

After you create the peering zone, you can revoke this permission by running the [`gcloud vmware dns-bind-permission revoke`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke) command:
         
         gcloud vmware dns-bind-permission revoke --user=USER_EMAIL
         

  2. Get the `INTRANET` network path of your standard VMware Engine network by running the [`gcloud vmware networks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/networks/describe) command:
         
         gcloud vmware networks describe VMWARE_ENGINE_NETWORK_NAME
         

Replace `VMWARE_ENGINE_NETWORK_NAME` with the name of your VMware Engine network.

The output contains multiple `vpcNetworks` entries. Copy the `network` value from the entry where the `type` field is `INTRANET`, for example, `projects/123456789012-tp/global/networks/intranet-abcde12345`.

  3. Create a Cloud DNS peering zone by running the [`gcloud dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
         
         gcloud dns managed-zones create PEERING_ZONE_NAME \
             --description="PEERING_ZONE_DESCRIPTION" \
             --dns-name="DNS_NAME" \
             --visibility=private \
             --networks="INTRANET_NETWORK_PATH" \
             --peer-network="projects/FORWARDING_PROJECT_ID/global/networks/FORWARDING_VPC_NETWORK"
         

Replace the following:

     * `PEERING_ZONE_NAME`: A name for the peering zone, for example, `gcve-peering-zone`.
     * `PEERING_ZONE_DESCRIPTION`: A description for the zone, for example, `GCVE DNS peering`.
     * `DNS_NAME`: The **DNS name** value that you used for your forwarding zone in the previous section.
     * `INTRANET_NETWORK_PATH`: The `INTRANET` network path that you copied in the previous step.
     * `FORWARDING_PROJECT_ID`: The project ID of the project that contains your forwarding zone.
     * `FORWARDING_VPC_NETWORK`: The name of the VPC network that your forwarding zone uses.



With Cloud DNS forwarding and peering configured, management appliances on your private cloud can now resolve names in your on-premises domains.

## Configure address resolution without using Cloud DNS

If you aren't using Cloud DNS, you can configure on-premises DNS resolution by pointing your on-premises DNS server to the DNS servers of your private cloud.

To configure this resolution, first get the IP addresses of the DNS servers for your private cloud:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click the name of the private cloud to view its details.

  3. On the **Summary** page, copy the **DNS server IP** addresses for your private cloud.




Next, use one of the following options to configure your on-premises DNS server:

  * Create a zone on the DNS server for `gve.goog`
  * Create a conditional forwarder on your on-premises DNS server to resolve `gve.goog`



### Create a zone on the DNS server for `gve.goog`

You can set up a zone as a stub zone and point to the DNS servers on the private cloud for name resolution. This section provides information on using a BIND DNS server or a Microsoft Windows DNS server.

**Note:** This document uses `gve.goog` as a generic reference for a zone. If you have more than one private cloud, specify the distinct zone for your private cloud in the format `GUID.REGION.gve.goog`, such as `ab123456.australia-southeast1.gve.goog`.

#### Create a zone on a BIND DNS server

The file and parameters to configure can vary based on your individual DNS setup.

For example, for the default BIND server configuration, edit the `/etc/named.conf` file on your DNS server and add the following zone information:
    
    
    zone "gve.goog"
    {
        type stub;
        masters { PC_DNS_IP_1; PC_DNS_IP_2; };
        file "gve.goog.db";
    };
    

Replace `PC_DNS_IP_1` and `PC_DNS_IP_2` with the IP addresses of the DNS servers for your private cloud.

#### Create a zone on a Microsoft Windows DNS server

  1. Right-click the DNS server and select **New zone**.
  2. Select **Stub zone** and click **Next**.
  3. Select the appropriate option depending on your environment and click **Next**.
  4. Select **Forward lookup zone** and click **Next**.
  5. Enter the zone name and click **Next**.
  6. Enter the IP addresses of the DNS servers for your private cloud that you obtained from the Google Cloud console.
  7. Click **Next** as needed to complete the setup.



### Create a conditional forwarder

A conditional forwarder sends all DNS name resolution requests to the designated server. This setup forwards any request to `*.gve.goog` to the DNS servers on the private cloud. The following sections show how to set up forwarders on different types of DNS servers.

#### Create a conditional forwarder on a BIND DNS server

The specific file and parameters to configure can vary based on your individual DNS setup.

For example, for the default BIND server configuration, edit the `/etc/named.conf` file on your DNS server and add the following conditional forwarding information:
    
    
    zone "gve.goog" {
        type forward;
        forwarders { PC_DNS_IP_1; PC_DNS_IP_2; };
    };
    

Replace `PC_DNS_IP_1` and `PC_DNS_IP_2` with the IP addresses of the DNS servers for your private cloud.

#### Create a conditional forwarder on a Microsoft Windows DNS server

  1. Open the DNS Manager on the DNS server.
  2. Right-click **Conditional forwarders** and select the option to add a conditional forwarder.
  3. Enter the DNS domain and the IP address of the DNS servers in the private cloud, then click **OK**.



## What's next

  * [Set up DNS bindings for management appliance access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-private-cloud-management-dns)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
