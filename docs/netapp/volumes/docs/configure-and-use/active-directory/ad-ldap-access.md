---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/ad-ldap-access/
title: Use Active Directory as LDAP server for NFS \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:56.792576+00:00
---

# Use Active Directory as LDAP server for NFS  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/ad-ldap-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Use Active Directory as LDAP server for NFS Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad) as an LDAP server for NFS.

NetApp Volumes uses LDAP servers for the following use cases:

  * Mapping Windows and UNIX identities on multi-protocol volumes that offer parallel access through NFS and SMB.

  * Supporting NFS extended groups by retrieving up to 1,024 GIDs for a given UID.

  * Mapping NFSv4 security identifiers to UIDs and GIDs.

  * Mapping Kerberos principals to UIDs and GIDs.




For more information, see [Use cases for using Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#use_cases_for_active_directory).

Flex Unified ONTAP-mode provides flexible options to configure the pool's LDAP client to connect to many popular LDAP servers. For more information, see [Create LDAP client configurations for ONTAP NFS access](https://docs.netapp.com/us-en/ontap/nfs-config/create-ldap-client-config-task.html) and [How to configure LDAP in ONTAP](https://www.netapp.com/pdf.html?item=/media/19423-tr-4835.pdf).

For all other service levels, the service supports only Active Directory as an LDAP server.

NetApp Volumes uses LDAP queries for the following purposes:

  * Map a UNIX username to a UID and primary GID.

  * If LDAP is enabled on the storage pool, look up all of the GIDs for a given UID.

  * Map UIDs to UNIX usernames.

  * Map GIDs back to group names.

  * Map UNIX usernames to alternative Windows usernames.




LDAP servers use LDAP schemas to define the attributes that store relevant information. Active Directory and NetApp Volumes use the RFC2307bis schema to fetch this information. Only ONTAP-mode lets you use or define a different schema. Active Directory already provides this schema, but you must populate the required attributes for your users and groups.

You must populate the following attributes with values for successful lookups:

UNIX attribute | RFC2307bis attribute name  
---|---  
UNIX username | `uid`  
UNIX user numeric ID | `uidNumber`  
UNIX group name | `cn`  
UNIX group numeric ID | `gidNumber`  
UNIX user object class | `objectClass`  
UNIX group object class | `objectClass`  
  
The `objectClass` must include `user` for UNIX users and `group` for UNIX groups.

Although Active Directory provides these attribute fields, the `uid`, `uidNumber`, `cn`, and `gidNumber` fields are empty by default, and a domain administrator must populate them. If the fields are empty, a lookup fails, and the system defaults to an anonymous user named `pcuser` with `UID=65534` and `GID=65534`. This user typically doesn't have permission to access files on UNIX volumes, which can result in `access denied` errors.

For multi-protocol access, the Windows username must match the UNIX username so the system can map UNIX UIDs to Windows SIDs. If usernames don't match, see [How to configure LDAP in ONTAP](https://www.netapp.com/pdf.html?item=/media/19423-tr-4835.pdf) for information about using a combination of the attributes `uid` and `sAMAccountName` to configure asymmetric name mapping.

NetApp Volumes caches LDAP query results. Each cache has a defined time to live (TTL), after which entries expire to prevent stale data. NetApp Volumes also uses a negative TTL to temporarily cache failed lookups, which helps prevent repeated queries for objects that don't exist.

The following table describes the time to live (TTL) settings for the LDAP cache:

Cache | Default timeout  
---|---  
Group membership list | 24-hour time to live  
UNIX groups (GID) | 24-hour time to live, 1-minute negative time to live  
UNIX users (UID) | 24-hour time to live, 1-minute negative time to live  
  
## What's next

[Manage customer-managed encryption key policies](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/cmek-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
