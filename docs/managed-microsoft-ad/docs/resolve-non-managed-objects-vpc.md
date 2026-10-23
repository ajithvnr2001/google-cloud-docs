---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/resolve-non-managed-objects-vpc/
title: Resolve queries for non-Managed Microsoft AD objects \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:36.820960+00:00
---

# Resolve queries for non-Managed Microsoft AD objects  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/resolve-non-managed-objects-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Resolve queries for non-Managed Microsoft AD objects Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to configure DNS forwarding so that queries from a Google Cloud authorized network for Active Directory resources located in another domain succeed.

## Context

When using a Google Cloud VM domain-joined to Managed Microsoft AD, if you try to look up users or objects that are not located on the same VPC network, the search fails. It fails because the default Windows configuration does not forward the query to the Managed Microsoft AD domain. Instead, it uses the DNS server for the VPC where the VM is located. This DNS server does not have information about Managed Microsoft AD users and objects outside the VPC network, so the lookup fails.

DNS forwarding is useful in any case where you need to resolve resources located outside the VPC network from Google Cloud. For example, if the Managed Microsoft AD domain has a trust relationship with the target domain, this configuration is required.

## Before you begin

Before you begin, verify the following configurations.

  * The Google Cloud VM must be domain-joined to the Managed Microsoft AD domain.

  * The forwarding target name server is reachable from within your VPC network. You can test that it is reachable with the following steps:

###  Console 

Before you begin, verify that the [Network Management API](https://console.cloud.google.com/marketplace/product/google/networkmanagement.googleapis.com) is enabled.

    1. Go to the [**Connectivity Tests**](https://console.cloud.google.com/net-intelligence/connectivity/tests) page in the Google Cloud console.   
[Go to the Connectivity Tests page](https://console.cloud.google.com/net-intelligence/connectivity/tests)

    2. Create and run a Connectivity Test with the following values:

       * **Protocol** : TCP
       * **Source** : IP address from your Google Cloud VPC
       * **Destination** : IP address of your on-premises DNS server
       * **Destination port** : 53

Learn more about creating and running [Network Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

###  PowerShell 

In Windows PowerShell, run the following command:
    
    nslookup domain-name dns-server-ip
    

Learn more about [`nslookup`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup).




If your target is an on-premises domain, verify the following firewall configuration.

  * The firewall must be configured to allow users from the Managed Microsoft AD domain to access on-premises resources. Learn about [firewall configurations for accessing on-premises resources](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls#accessing_on-premises_active_directory_resources_from).



If you are using private DNS forwarding, there are a few additional prerequisites.

  * Your on-premises firewall must pass queries from Cloud DNS. To allow this, configure the firewall to allow Cloud DNS queries from the 35.199.192.0/19 IP address range on UDP port 53 or TCP port 53. If you are using multiple Cloud Interconnect connections or VPN tunnels, be sure that the firewall allows traffic for all of them.

  * Your on-premises network must have a route that directs traffic destined to 35.199.192.0/19 back to your VPC network.




## Target domain is not on a VPC network

To configure DNS forwarding from Google Cloud to an on-premises domain that is not on a VPC network, you should use a forwarding zone. Learn about [DNS forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones).

To create a forwarding zone that resolves the on-premises DNS name to the IP addresses of on-premises DNS servers, complete the following steps.

###  Console 

  1. Go to the [**Cloud DNS**](https://console.cloud.google.com/networking/dns/zones/) page in the Google Cloud console.   
[Go to the Cloud DNS page](https://console.cloud.google.com/networking/dns/zones/)

  2. Create a DNS zone with the following values:

     * **Zone type** : **Private**
     * **DNS name** : Target DNS name
     * **Options** : **Forward queries to another server**
     * **Destination DNS servers** : IP addresses of target DNS servers



Learn more about [creating DNS forwarding zones](https://docs.cloud.google.com/dns/zones#creating-forwarding-zones).

###  gcloud 

To create a new managed private forwarding zone, you should use the [dns managed-zones create](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create name \
        --description=description \
        --dns-name=on-premises-dns-name \
        --forwarding-targets=on-premises-dns-ip-addresses \
        --visibility=private
    

Learn more about [creating DNS forwarding zones](https://docs.cloud.google.com/dns/zones#creating-forwarding-zones).

## Target domain is on a VPC network

To configure DNS forwarding from Google Cloud to a self-managed domain that is on a VPC network, [follow the steps for Cloud DNS](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones) that are relevant for your configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
