---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain/
title: Connect to a Managed Microsoft AD domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:07.990071+00:00
---

# Connect to a Managed Microsoft AD domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Connect to a Managed Microsoft AD domain Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the various options for connecting to a Managed Service for Microsoft Active Directory domain.

## Connecting to a domain-joined Windows VM with RDP

You can connect to your domain with Remote Desktop Protocol (RDP). For security reasons, you cannot use RDP to connect directly to a domain controller. Instead, you can use RDP to connect to a Compute Engine instance, and then use the standard AD manageability tools to work remotely with your AD domain.

After [domain-joining your Windows VM](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows), you can [use RDP in the Google Cloud console to connect to your domain-joined Windows VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and [manage your Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects).

### Troubleshooting RDP connections

If you have difficulty connecting to your Windows instance with RDP, see [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp) for tips and approaches to troubleshoot and resolve common RDP issues.

#### Resolving Kerberos issues

If you try to use Kerberos for your RDP connection, but it falls back to NTLM, your configuration may not meet the necessary requirements.

To RDP to a Managed Microsoft AD-joined VM using Kerberos, the RDP client needs a ticket issued for the target server. To get this ticket, the client must be able to do the following tasks:

  * Determine the service principal name (SPN) of the server. For RDP, the SPN is derived from the server's DNS name.
  * Contact the domain controller of the domain the client's workstation is joined to and request a ticket for that SPN.



To ensure that the client can determine the SPN, add an IP-based SPN to the server's computer object in AD.

To ensure that the client can find the right domain controller to contact, you must do one of the following tasks:

  * Create a trust relationship with your on-premises AD domain. Learn more about [creating and managing trusts](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-manage-trusts).
  * Connect from a domain-joined workstation using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).



## Connecting to a domain-joined Linux VM

This section lists some of the open source options for managing Active Directory interoperation with Linux. Learn [how to join a Linux VM to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-linux).

#### System Security Services Daemon (SSSD) joined directly to Active Directory

You can use System Security Services Daemon (SSSD) to manage Active Directory interoperation. Note that SSSD does not support cross-forest trusts. Learn about [SSSD](https://docs.pagure.org/SSSD.sssd/).

#### Winbind

You can use Winbind to manage Active Directory interoperation. It uses Microsoft Remote Procedure Calls (MSRPCs) to interact with Active Directory, which is similar to a Windows client. Winbind supports cross-forest trusts. Learn about [Winbind](https://www.samba.org/samba/docs/old/Samba3-HOWTO/winbind.html).

#### OpenLDAP

OpenLDAP is a suite of LDAP applications. Some third-party providers have developed proprietary Active Directory interoperation tools based on OpenLDAP. Learn about [OpenLDAP](https://en.wikipedia.org/wiki/OpenLDAP).

## Connecting to a domain using trust

If you create a trust between your on-premises domain and your Managed Microsoft AD domain, you can access your AD resources in Google Cloud as if they are in your on-premises domain. Learn how to [create and manage trusts in Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-manage-trusts).

## Connecting to a domain with Hybrid Connectivity products

You can connect to your Managed Microsoft AD domain with Google Cloud Hybrid Connectivity products, like Cloud VPN or Cloud Interconnect. You can configure the connection from your on-premises or other network to an authorized network of Managed Microsoft AD domain.

### Before you begin

  * [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-create-domain).

  * [Join your Windows VM](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows) or [your Linux VM](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-linux) to the Managed Microsoft AD domain.




### Connecting using domain name

We recommend connecting to a domain controller using its domain name rather than its IP address because Managed Microsoft AD does not provide static IP addresses. Using the domain name, the Active Directory DC locator process can find the domain controller for you, even if its IP address has changed.

### Using IP address for DNS resolution

If you use the IP address to connect to a domain, you can create an inbound DNS policy on your VPC network so that it can use the same name resolution services that Managed Microsoft AD uses. Managed Microsoft AD uses Cloud DNS to provide name resolution to Managed Microsoft AD domain using Cloud DNS peering.

To use the inbound DNS policy, you must configure your on-premises systems or name servers to forward DNS queries to the proxy IP address located in the same region as the Cloud VPN tunnel or VLAN attachment that connects your on-premises network to your VPC network. Learn about [creating an inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in).

## Using peerings

Managed Microsoft AD does not support nested peering, so only networks that are directly authorized for Active Directory can access the domain. Peers of the authorized network cannot reach the Managed Microsoft AD domain.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
