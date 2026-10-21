---
url: https://docs.cloud.google.com/filestore/docs/protocols/
title: About supported file system protocols \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:22.078547+00:00
---

# About supported file system protocols  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/protocols/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  About supported file system protocols Stay organized with collections  Save and categorize content based on your preferences. 

Filestore supports the following file system protocols:

NFSv3

  * Available in all service tiers.
  * Supports bidirectional communication between the client and server. 
    * Uses multiple ports.
    * Creates a trust channel for network traffic and operations.
  * Offers quick setup for standard POSIX access.



NFSv4.1

  * Available in [zonal, regional, and enterprise service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).
  * Supported by Filestore CSI driver to create zonal or enterprise instances and mount them with NFSv4.1 semantics.
  * Compatible with modern firewall configurations and supports network security compliance requirements. 
    * Communication is always initiated by the client and always served through a single server port, `2049`.
    * Supports client and server authentication. 
      * Requires [RPCSEC_GSS Authentication](https://docs.kernel.org/filesystems/nfs/rpc-server-gss.html) which is implemented using [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) and [Kerberos](https://web.mit.edu/kerberos/krb5-latest/doc/), both available in [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview).
      * Supports LDAP and Kerberos for authentication (`krb5`), message integrity checks (`krb5i`), and in-transit data encryption (`krb5p`).
      * Offers NFSv4.1 file ACL support for the client and server.



Each protocol is best suited to specific use cases. The following table compares the specifications of each protocol:

Specification | NFSv3 | NFSv4.1  
---|---|---  
Supported service tiers | All service tiers | Zonal, regional, and enterprise  
Bidirectional communication | Yes | No. Communication is always initiated by the client using server port `2049`.  
Authentication | No | Yes. Requires [RPCSEC_GSS Authentication](https://docs.kernel.org/filesystems/nfs/rpc-server-gss.html), implemented using [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) and [Kerberos](https://web.mit.edu/kerberos/krb5-latest/doc/), both available in [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview).  
Supports file or directory Access Control Lists (ACLs) | No | Yes. Supports up to 50 Access Control Entries (ACEs) per list.  
Groups support | Up to 16 groups | Unlimited groups support when connected to Managed Microsoft AD.  
Security setting | `sys`. Creates a trust channel. | `sys`. Creates a trust channel. `krb5`. Authenticates the client and server. `krb5i`. Provides authentication and message integrity checks.`krb5p`. Provides authentication, message integrity checks, and in-transit data encryption.  
Operations latency | None | Operations latency increases with the security level selected.  
Recovery type | Stateless | Stateful  
File locking type | Network Lock Manager (NLM). The lock is controlled by the client. | Lease-based advisory locking. The lock is controlled by the server.  
Supports client failures | No | Yes  
Supports [private services access](https://docs.cloud.google.com/filestore/docs/network-ip-requirements) | Yes | Yes  
Supports [Private Service Connect](https://docs.cloud.google.com/filestore/docs/configure-psc) [(Restricted GA)](https://docs.cloud.google.com/filestore/docs/getting-support) with IPv4 and IPv6 procotols | Yes | Yes  
  
## NFSv3 benefits

The NFSv3 protocol offers quick setup for standard POSIX access.

## NFSv3 limitations

The following is a list of NFSv3 limitations:

  * Lacks client and server authentication and encryption.
  * Lacks client failure handling.



For NFSv3 instances that use Private Service Connect NFS file locking is subject to the following limitations:

  * Clients waiting on blocking locks won't receive notifications when locks become available. 
  * Locks on rebooted clients are cleared automatically **only** upon detecting subsequent NLM activity from these clients.



## Benefits of NFSv4.1

The NFSv4.1 protocol uses the [RPCSEC_GSS Authentication](https://docs.kernel.org/filesystems/nfs/rpc-server-gss.html) method, which is implemented using [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) and [Kerberos](https://web.mit.edu/kerberos/krb5-latest/doc/) to provide client and server authentication, message integrity checks, and in-transit data encryption.

These security capabilities make the NFSv4.1 protocol compatible with modern network security compliance requirements:

  * Uses a single server port, `2049`, for all communication, helping simplify firewall configurations.

  * Supports NFSv4.1 file access control lists (ACLs).

    * Each ACL supports up to 50 access control entries (ACEs) per file or directory. This includes inheritance records.
  * Unlimited groups support when using Managed Microsoft AD integration.

  * Supports better client failure handling with lease-based advisory locking.

    * The client must verify continued connection with the server. If the client doesn't renew the lease, the server releases the lock and the file becomes available to any other client requesting access through a lock lease. In NFSv3, if a client is deleted while under lock, the file can't be accessed by another client, such as a new GKE node.
  * Supports stateful recovery.

    * Unlike NFSv3, NFSv4.1 is a TCP- and connection-based stateful protocol. The state of the client and server in the previous session can be resumed after recovery.



### Managed Service for Microsoft Active Directory

While [Managed Service for Microsoft Active Directory (Managed Microsoft AD)](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview) is not a strict requirement, it is the only Google Cloud-managed solution to support both LDAP and Kerberos, both of which are requirements for the Filestore NFSv4.1 protocol.

Administrators are strongly encouraged to use [Managed Service for Microsoft Active Directory (Managed Microsoft AD)](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview) to implement and manage LDAP and Kerberos.

As a Google Cloud-managed solution, Managed Microsoft AD provides the following benefits:

  * Offers multiregion deployment, supporting up to five regions on the same domain.

    * Reduces latency by ensuring users and their respective login servers are in closer proximity.
  * Supports [POSIX RFC 2307](https://www.rfc-editor.org/rfc/rfc2307.txt) and [RFC 2307bis](https://datatracker.ietf.org/doc/html/draft-howard-rfc2307bis-01), requirements for NFSv4.1 implementation.

  * Automates unique identifier (UID) and globally unique identifier (GUID) user mapping.

  * Users and groups can be created in or migrated to Managed Microsoft AD.

  * Administrators can create a domain trust with the current on-premises, self-managed, Active Directory (AD) and LDAP domain. With this option, migration is not necessary.

  * Provides an SLA.




### Access control and additional behaviors

  * Filestore NFSv4.1 ACEs are managed on Linux using the following commands:

    * [**`nfs4_setfacl`**](https://linux.die.net/man/1/nfs4_setfacl): Create or edit ACEs on a file or directory.
    * [**`nfs4_getfacl`**](https://linux.die.net/man/1/nfs4_getfacl): List the ACEs on a file or directory.
  * Each ACL supports up to 50 ACEs. Six entries are reserved for autogenerated ACEs created by client `chmod` operations. These ACEs can be modified after creation.

The autogenerated ACE records representing the mode bits are listed in the following order of priority:

    * `DENY and ALLOW ACEs` for the `OWNER@`
    * `DENY and ALLOW ACEs` for the `GROUP@`
    * `DENY and ALLOW ACEs` for `EVERYONE@`

If such ACEs are already present, they will be re-used and modified according to the new applied mode bits.

  * Filestore NFSv4.1 supports checking the required access only in POSIX mode `RWX` (read, write, and execute). It won't differentiate between `write append` and `write` operations that modify the content or `SETATTR` specification. The `nfs4_setfacl` utility also accepts `RWX` as a shortcut and automatically turns on all the appropriate flags.

  * The `nfs4_getfacl` doesn't do any translation of the principal on its own. The `nfs4_getfacl` utility will show the numeric `UID` and `GUID` for the principals. As a result, the special principals of `OWNER@`, `GROUP@`, and `EVERYONE@` will be shown.

  * Regardless of whether using Managed Microsoft AD, when working with `AUTH-SYS` and the `nfs4_setfacl` utility, administrators must specify the numeric `UID` and `GUID`, not user names. This utility isn't able to translate names to these values. If not provided correctly, the Filestore instance will default to the `nobody` ID.

  * When specifying write permissions for a file, or even files affected by an inherited ACE, the ACE must include both the `w` (write) and `a` (append) flags.

  * When checking permissions for `SETATTR`, the returned response is similar to `POSIX` in the following way:

    * The superuser or `ROOT` user can do anything.
    * Only the file owner can set the mode bits, ACLs, and time stamps to a specific time and group, such as one of the `GUID`s it belongs to.
    * Users other than the file owner may view the attributes, including the ACL.
  * A single ACE encompasses both effective and inherit-only permissions. Contrary to other NFSv4.1 implementations, Filestore won't automatically replicate inherited ACES for the purpose of distinguishing between effective and inherit-only ACEs.




### NFSv4.1 limitations

The NFSv4.1 protocol has the following limitations:

  * General limitations

    * When restoring a backup, the new instance must use the same protocol as the source instance.
    * When using any of the authenticated Kerberos security settings, users can expect some operations latency. Latency increases with each increasing security level.
    * The NFSv4.1 protocol doesn't support `AUDIT` and `ALARM` ACEs. 
    * Data access auditing is not supported.
  * GKE limitations

The NFSv4.1 protocol can't be combined with [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares). This feature is only supported with NFSv3. For a comprehensive list of supported GKE versions for each Filestore service tier and protocol, see the compatibility table in [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver#supported-versions).

  * Managed Microsoft AD limitations

    * Once configured, don't delete the Managed Microsoft AD domain or the network peering. Doing so causes the Filestore share to become inaccessible.
    * The only supported authentication mechanism is RPCSEC_GSS, which is implemented using LDAP and Kerberos (both available in Managed Microsoft AD).
    * To have a Filestore instance join Managed Microsoft AD through a Shared VPC, you must use `gcloud` or the Filestore API, not the Google Cloud.
    * The Managed Microsoft AD domain name must not exceed 56 characters.



## What's next

  * [Create a Filestore instance with Private Service Connect](https://docs.cloud.google.com/filestore/docs/configure-psc)
  * [Configure the NFSv4.1 protocol](https://docs.cloud.google.com/filestore/docs/configure-nfsv4)
  * [Create a Filestore instance with Managed Microsoft AD](https://docs.cloud.google.com/filestore/docs/configure-nfsv4-managed-ad)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
