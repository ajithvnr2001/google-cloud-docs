---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/active-directory-integration/
title: Volume replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:44.576050+00:00
---

# Volume replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/active-directory-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)



Send feedback 

#  Volume replication Stay organized with collections  Save and categorize content based on your preferences. 

File sharing protocols like SMB (CIFS), NFSv3 with extended groups, and NFSv4, using security principals, rely on external directory services to provide user identity information. NetApp Volumes relies on Microsoft Active Directory for directory services. Active Directory provides services like LDAP servers for looking up object—such as users, groups, machine accounts—DNS servers to resolve hostnames, and Kerberos servers for authentication.

For more information, see [Best practices for running Active Directory on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices).

Google Cloud's Managed Microsoft Active Directory isn't supported by NetApp Volumes.

## Use cases

NetApp Volumes uses Active Directory for the cases in the following sections.

### SMB domain service

Active Directory is the central domain service for SMB. SMB is used for authentication and identity lookups for users and groups. NetApp Volumes joins the domain as a member and doesn't support SMB in workgroup mode.

### NFSv3 extended group support

For NFSv3 with extended group support, Active Directory provides the LDAP server required for looking up objects such as users, groups, or machine accounts. Specifically, an RFC2307bis-compliant LDAP server is required for user ID and group ID lookups. LDAP support is enabled on storage pools during pool creation.

Extended group support ignores all group IDs sent by the NFS client in an NFS call; instead, it takes the user ID of the request and looks up all group IDs for the given user ID from the LDAP server to do file permission checks.

For more information, see [Manage LDAP RFC2307bis POSIX attributes](https://learn.microsoft.com/en-us/azure/azure-netapp-files/configure-ldap-extended-groups).

### NFSv4.x security principal to user ID and group ID mapping

For NFSv4.x, Active Directory is used to map security principals to user IDs and group IDs. NFSv4 uses a principal-based authentication model. In principal-based authentication, users are identified by security principals which take the form `user@dns_domain` (see https://www.rfc-editor.org/rfc/rfc7530.html#section-19) rather than being identified by user IDs and group IDs. To map security principals to user IDs and group IDs when accessing the volume using an NFSv4.x protocol, NetApp Volumes requires an RFC2307bis-compliant LDAP server. The only LDAP server supported is Active Directory. LDAP support is enabled on storage pools during pool creation.

To use security principals, the NFS client and server must connect to the same LDAP source and the idmapd.conf file must be configured at the client. For more information on configuring the idmapd.conf file, see [Ubuntu Manpage: idmapd.conf - configuration file for libnfsidmap](https://manpages.ubuntu.com/manpages/bionic/man5/idmapd.conf.5.html).

The Active Directory domain name is used for the **dns_domain**. The **user** is the name of Active Directory users. Use these values when you [set your LDAP POSIX attributes](https://docs.google.com/document/d/16YwOyMZE-5xp0zr_l4RWOpmkbAim6ndAepsOLMP6rAo/edit#heading=h.9shy0p65nvwm).

To use NFSv4.1 without setting up ID mapping and only use user IDs and group IDs similar to NFSv3, you can use numeric IDs to ignore security principals. NetApp Volumes supports numeric IDs, and [current NFS clients use numeric IDs by default](https://docs.google.com/document/d/16YwOyMZE-5xp0zr_l4RWOpmkbAim6ndAepsOLMP6rAo/edit#heading=h.yyy4zek4ug9s) if ID mapping isn't configured.

### NFSv4.x with Kerberos

If you use Kerberos, it's mandatory to use [Active Directory as the LDAP server](https://docs.google.com/document/d/16YwOyMZE-5xp0zr_l4RWOpmkbAim6ndAepsOLMP6rAo/edit#heading=h.6fanuiob33o6) for security principal lookups. Kerberos principals are used as security identifiers. Active Directory is also used as the Kerberos Key Distribution Center (KDC). To make this work, you must attach an Active Directory policy containing Kerberos settings to the pool and enable LDAP support on a storage pool during pool creation. 

For more information, see Create a storage pool.

## Active Directory LDAP access

For NFS use cases, Active Directory is used as an LDAP server. NetApp Volumes expects identity data using an RFC2307bis schema. Active Directory already provides this schema, but you need to make sure to populate the required attributes for your users and groups.

NetApp Volumes uses the provided credentials from the Active Directory policy to bind against LDAP using LDAP signing.

If the user or group cannot be found, access is denied.

### Attribute caching

NetApp Volumes caches the results of LDAP queries. The following table describes the time to live (TTL) settings for the LDAP cache. If the cache holds invalid data due to misconfigurations you are trying to fix, you must wait until the cache is refreshed before your changes in Active Directory are detected. Otherwise, the NFS server continues to use the old data to verify access, which likely results in permission denied messages on the client. After the TTL period, entries age out so that stale entries don't linger. Lookup requests that aren't found are retained for a one minute TTL to help avoid performance issues. 

Cache | Default timeout  
---|---  
Group membership list | 24-hour TTL  
Unix groups (GID) | 24-hour TTL, 1-minute negative TTL  
Unix users (UID) | 24-hour TTL, 1-minute negative TTL  
  
### Active Directory domain controller topologies

Once you successfully connect to Active Directory domain controllers, you can use the following file sharing protocols:

  * SMB
  * NFSv3 with extended groups
  * NFSv4



The following sections illustrate various potential topologies. The diagrams show only the domain controller used by NetApp Volumes. Other domain controllers for the same domain are shown only where required.

Microsoft recommends deploying at least two domain controllers (DCs) for redundancy and availability.

### Active Directory domain controller in the same region as NetApp Volumes volumes

The following diagram shows the simplest deployment mode, a domain controller in the same region as the NetApp Volumes volumes.

### Active Directory domain controllers in multiple regions using AD sites

If you are using NetApp Volumes volumes in multiple regions, we recommend that you place at least one domain controller in each region. While the service tries to choose the best DC to use automatically, it is recommended to manage DC selection using AD sites.

### Active Directory domain controller in an on-premises network

Using an on-premises domain controller over VPN is supported, but might negatively affect end user authentication and file access performance. Make sure to not add additional VPC peering hops in your network path.

#### Considerations for on-premise DCs

Connections to on-premise DCs use TCP and IP. These connections often fail due to the following limitations:

  * VPC peering: NetApp Volumes can only reach DCs that are on the storage pool's VPC or connected to it by VPN. NetApp Volumes can't reach DCs in any other VPC, including those that are peered to the VPC that connect to the storage pool. 

  * Firewalls: You must allow NetApp Volumes to contact your DCs. See Firewall rules for Active Directory access.




### Active Directory domain controller in a different VPC network

You can't place the domain controller in a different VPC because Google Cloud VPC peering doesn't allow transitive routing. Alternatively, you can attach NetApp Volumes to a shared VPC network that hosts the Active Directory domain controllers. If you attach NetApp Volumes to a shared VPC network, then, architecturally, this scenario becomes one of the scenarios in the previous sections.

### Manage DC selections using AD sites

To represent the actual data center locations, offices, and network topology as closely as possible, place domain controllers in the same region as your volumes and define an Active Directory site for that region.

When NetApp Volumes is connected to your domain, the service uses DNS-based discovery to find the right domain controllers to communicate with. Using the results of the discovery, the service maintains a list of valid DCs to connect to and uses the one with the lowest latency.

When you specify a site in the Active Directory settings of NetApp Volumes, you can limit the list of DCs to the ones specified in the AD site.

If automatic DC selection fails, using AD sites can help remediate the issue:

  * Deploy at least one domain controller in the NetApp Volumes region and connect them to your existing Active Directory.

  * Create an Active Directory site for your Google Cloud region and place the appropriate domain controllers into that site.

  * Use the Active Directory site when setting up Active Directory connections.




To manually verify the list of potential DCs the service can use, see How to identify Active Directory domain controllers used by NetApp Volumes

For more information, see Active Directory: Design considerations and best practices.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
