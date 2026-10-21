---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources/
title: Configure authentication using Active Directory \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:38.727298+00:00
---

# Configure authentication using Active Directory  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure authentication using Active Directory

You can configure vCenter and NSX in Google Cloud VMware Engine to use your on-premises Active Directory as an LDAP or LDAPS identity source for user authentication. Once setup is complete, you can provide access to vCenter and NSX Manager and assign required roles for managing your private cloud.

**Caution:** Joining your private cloud vCenter to an Active Directory domain is unsupported and unnecessary. Your private cloud vCenter server only supports the **Active Directory over LDAP** identity source type, which doesn't require joining your vCenter to an Active Directory domain. Avoid the **Active Directory (Windows Integrated Authentication)** identity source type.

## Before you begin

The steps in this document assume that you first do the following:

  * [Establish connectivity from your on-premises network to your private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises)
  * Enable DNS name resolution of your on-premises Active Directory: 
    * For _Legacy VMware Engine Networks_ : Enable DNS name resolution of your on-premises Active Directory by creating [DNS forwarding rules](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding) in your private cloud.
    * For _Standard VMware Engine Networks_ : Enable DNS name resolution of your on-premises Active Directory by configuring [DNS bindings](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings) to your VMware Engine network.



The following table lists the information you need when setting up your on-premises Active Directory domain as an SSO identity source on vCenter and NSX. Gather the following information before setting up SSO identity sources:

Information | Description  
---|---  
Base DN for users | The base distinguished name for users.  
Domain name | The FQDN of the domain, for example, `example.com`. Don't provide an IP address in this field.  
Domain alias | The domain NetBIOS name. If you use SSPI authentication, add the NetBIOS name of the Active Directory domain as an alias of the identity source.  
Base DN for groups | The base distinguished name for groups.  
Primary server URL |  The primary domain controller LDAP server for the domain. Use the format `ldap://hostname:port` or `ldaps://hostname:port`. The port is typically 389 for LDAP connections and 636 for LDAPS connections. For Active Directory multi-domain controller deployments, the port is typically 3268 for LDAP and 3269 for LDAPS. A certificate that establishes trust for the LDAPS endpoint of the Active Directory server is required when you use `ldaps://` in the primary or secondary LDAP URL.  
Secondary server URL | The address of a secondary domain controller LDAP server that is used for failover.  
Choose certificate | To use LDAPS with your Active Directory LDAP server or OpenLDAP server identity source, click the **Choose certificate** button that appears after you type `ldaps://` in the URL field. A secondary server URL isn't required.  
Username | The ID of a user in the domain who has a minimum of read-only access to the base DN for users and groups.  
Password | The password of the user who is specified by **Username**.  
  
## Add an identity source on vCenter

The following steps describe how to add your on-premises Active Directory as an LDAP server on vCenter:

  1. Sign in to the vCenter for your private cloud using a [solution user account](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege#solution_user_accounts).
  2. Select **Home > Administration**.
  3. Select **Single Sign On > Configuration**.
  4. Open the **Identity Sources** tab and click **+Add** to add a new identity source.
  5. Select **Active Directory as an LDAP Server** , and click **Next**.
  6. Specify the identity source parameters for your environment, and click **Next**.
  7. Review the settings, and click **Finish**.



## Add an identity source on NSX

These steps describe how to add an identity source in NSX Manager. If you want to automate this configuration, you can use the [NSX-T API](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/nsx-t-public-api).

  1. Sign in to NSX Manager in your private cloud.
  2. Go to **System > Settings > Users and Roles > LDAP**.
  3. Click **Add identity source**.
  4. In the **Name** field, enter a display name for the identity source.
  5. Specify the **Domain Name** and **Base DN** of your identity source.
  6. In the **Type** column, select **Active Directory over LDAP**.
  7. In the **LDAP Servers** column, click **Set** .
  8. In the **Set LDAP Server** window, click **Add LDAP Server**.
  9. Specify the LDAP server parameters and click **Check status** to verify the connection from NSX manager to your LDAP server.
  10. Click **Add** to add the LDAP server.
  11. Click **Apply** and then click **Save**.



## Ports required for using on-premises Active Directory as an identity source

The ports listed in the following table are required to configure your on-premises Active Directory as an identity source on the private cloud vCenter.

Port | Source | Destination | Purpose  
---|---|---|---  
53 (UDP) | Private cloud DNS servers | On-premises DNS servers | Required for forwarding DNS lookup of on-premises Active Directory domain names from a private cloud vCenter server to an on-premises DNS server.  
389 (TCP/UDP) | Private cloud management network | On-premises Active Directory domain controllers | Required for LDAP communication from a private cloud vCenter server to Active Directory domain controllers for user authentication.  
636 (TCP) | Private cloud management network | On-premises Active Directory domain controllers | Required for secure LDAP (LDAPS) communication from a private cloud vCenter server to Active Directory domain controllers for user authentication.  
3268 (TCP) | Private cloud management network | On-premises Active Directory global catalog servers | Required for LDAP communication in multi-domain controller deployments.  
3269 (TCP) | Private cloud management network | On-premises Active Directory global catalog servers | Required for LDAPS communication in multi-domain controller deployments.  
8000 (TCP) | Private cloud management network | On-premises network | Required for vMotion of virtual machines from the private cloud network to the on-premises network.  
  
## What's next

For more information about SSO identity sources, see the following vSphere and NSX Data Center documentation:

  * [Add or Edit a vCenter Single Sign-On Identity Source](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.authentication.doc/GUID-B23B1360-8838-4FF2-B074-71643C4CB040.html).
  * [LDAP Identity Source](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/administration/GUID-664DC51F-3D6B-442F-9C29-2A5304ACCCA4.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
