---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-dns/
title: Configure DNS lookup using Cloud DNS \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:23.194267+00:00
---

# Configure DNS lookup using Cloud DNS  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Configure DNS lookup using Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how Managed Service for Microsoft Active Directory simplifies DNS configuration with its seamless integration with Cloud DNS.

## Seamless DNS lookup with Managed Microsoft AD

Active Directory depends heavily on DNS for discoverability of the service and for name lookup of domain-joined network resources. But configuring DNS can be a complex and time-consuming process, and you can't use DHCP in Managed Microsoft AD. Managed Microsoft AD removes the need to configure individual clients or [DHCP](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top) for Active Directory domain lookup by seamlessly integrating with [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview). As a result, VMs created on VPC networks for authorized networks are able to discover the Active Directory domain and on-premises VMs, without requiring client-side configuration changes on the individual VMs.

Compute Engine instances are preconfigured to use Cloud DNS for name resolution. Cloud DNS lets you create private DNS zones where you can specify name-to-IP mapping or forward requests for a domain namespace to another DNS server. Cloud DNS can also be configured to point to the DNS setting of another VPC network with DNS peering.

**Note:** We recommend connecting to the domain controller using its domain name rather than its IP address because Managed Microsoft AD does not provide static IP addresses. Using the domain name, the Active Directory DC locator process can find the domain controller for you, even if its IP address has changed.

Managed Microsoft AD uses a private DNS zone and DNS peering to provide seamless integration. When you make a request for instance creation or for adding an authorized network, Managed Microsoft AD creates a private DNS zone in the tenant project hosting the VMs running Active Directory. This private DNS zone is provisioned to forward all requests for the Active Directory domain's fully qualified domain name (FQDN) to DNS servers running in your tenant project.

Then Managed Microsoft AD creates DNS peering between the authorized network and the VPC host AD domain and DNS, forwarding all requests for the AD domain namespace to the private DNS zone in the tenant project.

![DNS](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/seamless-dns1.png)

**Figure 1.** DNS lookup on Google Cloud with Managed Microsoft AD

## Extending DNS resolution to on-premises networks

The integration of Managed Microsoft AD with Cloud DNS also lets on-premises resources discover Google Cloud resources joined to the Managed Microsoft AD. To enable this, [create an inbound DNS policy](https://docs.cloud.google.com/dns/docs/policies#create-in).

![DNS](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/seamless-dns2.png)

**Figure 2.** Extending DNS resolution to on-premises resources

## What's next

  * Learn more about [DNS setup and best practices](https://docs.cloud.google.com/dns/docs/best-practices-dns).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
