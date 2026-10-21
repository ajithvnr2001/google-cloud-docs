---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad/
title: Google Cloud NetApp Volumes Active Directory integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:34.911805+00:00
---

# Google Cloud NetApp Volumes Active Directory integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Google Cloud NetApp Volumes Active Directory integration Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how Google Cloud NetApp Volumes integrates with Active Directory to provide identity and authentication for your Server Message Block (SMB) and Network File System (NFS) volumes. Understanding this integration helps you configure secure access to your file shares.

## About the integration

NetApp Volumes uses Active Directory to manage user identity and authentication for SMB and NFS volumes. Active Directory provides the following directory services for file sharing:

  * **LDAP** : finds users, groups, and computer accounts

  * **DNS** : resolves host names and locates domain controllers

  * **Kerberos** : authenticates clients and services




An Active Directory policy is a configuration template that defines how NetApp Volumes connect to your domain. You attach a policy to a storage pool. The domain join and computer account creation occur subsequently, based on the storage pool service level and the volumes you create. For more information, see [How Active Directory policies join the domain](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#how_active_directory_policies_join_the_domain).

Active Directory policies are specific to each region. You can configure up to five policies per region. For more information, see [Best practices for running Active Directory on Google Cloud](https://docs.cloud.google.com/managed-microsoft-ad/docs/best-practices).

## Use cases for Active Directory

NetApp Volumes uses Active Directory for several use cases:

  * **Provides SMB domain service and authentication** : Active Directory serves as the central domain service for SMB, which NetApp Volumes uses for authentication and identity lookups for users and groups. NetApp Volumes joins your domain as a member but doesn't support SMB in workgroup mode.

  * **Provides extended group support for NFSv3** : for NFSv3 with extended group support, Active Directory provides the LDAP server required to look up objects such as users, groups, or machine accounts.

    * Specifically, user ID and group ID lookups require an `RFC2307bis`-compliant LDAP server.

    * LDAP support is enabled on storage pools during pool creation.

    * Extended group support ignores all group IDs sent by the NFS client in an NFS call. Instead, it takes the user ID of the request and looks up all group IDs for the given user ID from the LDAP server for file permission checks.

For more information, see [Manage LDAP `RFC2307bis` POSIX attributes](https://learn.microsoft.com/en-us/azure/azure-netapp-files/configure-ldap-extended-groups).

  * **Maps security principals to user and group IDs for NFSv4.x** : NetApp Volumes uses Active Directory to map security principals to user IDs and group IDs for NFSv4.x.

    * NFSv4.x uses a principal-based authentication model, where security principals identify users in the format `user@dns_domain`, as described in [RFC 7530 security considerations](https://www.rfc-editor.org/rfc/rfc7530.html#section-19), instead of user IDs and group IDs. To map security principals to user IDs and group IDs when you access the volume with an NFSv4.x protocol, NetApp Volumes requires an `RFC2307bis`-compliant LDAP server. NetApp Volumes only supports Active Directory LDAP servers. LDAP support is enabled on storage pools during pool creation.

    * To use security principals, the following requirements must be met:

      * The NFS client and server must connect to the same LDAP source.

      * You must configure the `idmapd.conf` file on the NFS client. For more information about how to configure the `idmapd.conf` file, see [Ubuntu documentation on how to configure the `idmapd.conf` file for `libnfsidmap`](https://manpages.ubuntu.com/manpages/bionic/man5/idmapd.conf.5.html).

    * The `dns_domain` is the Active Directory domain name, and the `user` is the Active Directory user's name. Use these values when you set your LDAP POSIX attributes.

    * **Using numeric IDs for NFSv4.1** : to use NFSv4.1 without ID mapping and only use user IDs and group IDs similar to NFSv3, use numeric IDs to ignore security principals. NetApp Volumes supports numeric IDs. NFS clients use numeric IDs by default if ID mapping isn't configured.

  * **Provides Kerberos authentication for NFSv4.x** : if you use Kerberos with NFSv4.x, you must use Active Directory as the LDAP server for security principal lookups. [Kerberos principals](https://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html) are used as security identifiers. The Kerberos Key Distribution Center uses Active Directory.

To use Kerberos with NFSv4.x, you must also complete the following steps:

    * Attach an Active Directory policy that contains Kerberos settings to the pool.

    * Enable LDAP support on a storage pool when you create the pool.




## How Active Directory policies join the domain

This section describes when NetApp Volumes joins your Active Directory domain, how it creates computer accounts, and how the service authenticates after joining the domain. For an overview and common use cases, see Google Cloud NetApp Volumes Active Directory integration.

An Active Directory policy is a configuration template. Creating a policy doesn't join a domain or create computer accounts. The policy takes effect only after you attach it to a storage pool and the service joins the domain for that pool.

### Attach an Active Directory policy to a storage pool

You can attach an Active Directory policy in the following situations:

  1. When you create a storage pool.

  2. When you use an existing storage pool that doesn't already have an Active Directory policy.


**Important:** After you assign an Active Directory policy to a storage pool, you can't replace it with another policy. Choose your domain, organizational unit (OU), and Kerberos settings carefully before attaching the policy.

### Determine when the domain join happens

The timing of the domain join depends on the storage pool service level:

  * **Flex Unified, Standard, Premium, and Extreme service levels** : NetApp Volumes joins the domain and creates a computer account when you create the first volume that requires Active Directory. This includes SMB volumes, NFSv3 with extended groups, and NFSv4.x with security principals or Kerberos. For the full list, see Use cases for Active Directory.

  * **Flex File service level** : NetApp Volumes joins the domain when you attach the Active Directory policy to the pool, including during pool creation.




### Computer accounts

NetApp Volumes creates Active Directory computer accounts to enable file servers to authenticate clients and communicate with domain controllers.

  * **Flex Unified and Flex File pools** : create one computer account per storage pool.

  * **Standard, Premium, and Extreme pools** : create multiple computer accounts as needed. For example, it might create separate accounts for NFSv4.1 with Kerberos and for SMB on the same pool.




After NetApp Volumes creates a computer account, it uses that account to communicate with Active Directory. It doesn't continue using the domain join user credentials from the Active Directory policy unless it needs to create a new computer account.

Computer account cleanup depends on whether the domain join user can delete computer accounts:

  * **Delete permission granted** : NetApp Volumes automatically deletes service-created computer accounts when you delete the last volume that uses them.

  * **Delete permission not granted** : computer accounts remain in Active Directory after you delete volumes. A domain administrator must delete unused accounts manually.




For more information about how to delegate permissions for creating and deleting computer accounts, see Required permissions to create Active Directory machine accounts.

### Kerberos encryption types

NetApp Volumes advertises Kerberos encryption types (enctypes) on its Active Directory computer accounts. Kerberos authentication succeeds only if the client, domain controller, and computer account support at least one common encryption type.

By default, NetApp Volumes advertises the following encryption types:

  * DES

  * RC4-HMAC




When you select **Enable AES Encryption for Active Directory authentication** in the Active Directory policy, NetApp Volumes also advertises the following encryption types:

  * AES-128

  * AES-256


**Important:** The Advanced Encryption Standard (AES) is the default in modern Active Directory domains. Select **Enable AES Encryption for Active Directory authentication** when you create or edit an Active Directory policy. For field descriptions, see [Create an Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy).

During Kerberos authentication, the Key Distribution Center (KDC) selects the strongest enctype supported by the client, the domain controller, and the NetApp Volumes computer account. To require specific enctypes on client computers, use Active Directory Group Policy. For more information, see [Configuring encryption types allowed for Kerberos](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos).

For more information about verifying which enctypes clients use, inspecting computer account attributes, or troubleshooting authentication failures related to weak or mismatched ciphers, see [Troubleshoot Kerberos encryption types for Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/troubleshoot-kerberos-encryption-types).

### Test an Active Directory policy connection

The Test Active Directory policy connection feature validates domain join by creating a temporary computer account in your domain.

  * **Delete permission granted** : NetApp Volumes deletes the temporary account immediately after the test.

  * **Delete permission not granted** : The temporary account remains in Active Directory. A domain administrator must delete the account manually. For test prerequisites and steps, see [Test the Active Directory policy connection](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection).




## Required permissions to create Active Directory machine accounts

To use Active Directory, NetApp Volumes must join one or more virtual file servers to your domain as computer accounts. To join the domain, you must provide the credentials of a domain user who has permission to join computers to your domain. By default, only `Domain Admins` group members can join computers to the domain, but Active Directory has the capability to [delegate the required permissions](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/delegating-administration-by-using-ou-objects) to individual users or groups on a full domain or organizational unit (OU) level.

For NetApp Volumes, it's recommended to create a dedicated domain service account. Delegate only the necessary permissions to join new computers to a specific OU. Once a user with `Domain User` or `Domain Guest` group membership is created, use the following instructions to delegate the required permissions.

  1. Sign in to your system as a domain administrator for your Active Directory domain.

  2. Open the **Active Directory Users and Computers** MMC snap-in.

  3. From the menu bar, select **View** and ensure that **Advanced Features** is enabled.

A check mark is displayed if the **Advanced Features** is enabled.

  4. In the task pane, expand the domain node.

  5. Locate the OU you want to modify, right-click, and select **Properties** from the context menu.

  6. In the **OU properties** window, select the **Security** tab.

  7. Under **Security** , click **Advanced** and then click **Add**.

  8. In the **Permission Entry** dialog, complete the following steps:

     1. Click **Select a principal**.

     2. Enter the name of your service account or group, and click **OK**.

     3. For **Applies to:** , select **This object and all descendant objects**.

     4. Make sure the following permissions are selected:

        * **Modify permissions**

        * **Create computer objects**

        * **Delete computer objects**

  9. Select the **Apply** checkbox, and then click **OK**.

  10. Close the **Active Directory Users and Computers** MMC snap-in.




After the service account is delegated, you can provide the username and password as Active Directory policy credentials.

For added security, during the machine account object query and creation, the username and password that are passed to the Active Directory domain use Kerberos encryption.

## Active Directory domain controllers

To connect NetApp Volumes to your domain, the service uses DNS-based discovery to identify a list of available domain controllers to use.

The service runs the following steps to find a domain controller to use:

  1. **Active Directory Site discovery** : NetApp Volumes uses an LDAP ping to the DNS server IP specified in the Active Directory policy to fetch the Active Directory Site subnet information. It returns a list of CIDRs and the Active Directory Sites which are assigned to those CIDRs.

**Note:** You can use the following command to manually fetch this list on a Windows system that's joined to the domain:

`Get-ADReplicationSubnet -Filter * | Select-Object Name,Site`

  2. **Define site names** : if the IP address of the volume matches any of the defined subnets, the associated site name is used. Smaller subnets matches take precedence over larger subnets matches. If the IP address of the volume is unknown, manually [create a temporary volume](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-volume) with the NFS protocol type to determine `/28` CIDR used.

If no site name is defined in the Active Directory, the site name configured in the Active Directory policy is used. If no site name is configured, the Standard, Premium, and Extreme service levels use the `Default-First-Site-Name` site. If the Flex service level tries to use the `Default-First-Site-Name` site, it will fail and the Flex service level instead uses the full domain controller discovery. Note that changes to the Active Directory site parameter are ignored by Flex service level storage pools.

  3. **Domain controller discovery** : with all necessary information acquired, the service identifies potential domain controllers using the following DNS query:

`nslookup -type=srv _ldap._tcp.<site_name>._sites.dc._msdcs.<domain-name> <dns-server>`

For full domain discovery, the service uses the following DNS query:

`nslookup -type=srv _ldap._tcp.dc._msdcs.<domain-name> <dns-server>`

  4. **Domain controller list generation** : a list of domain controllers is generated. NetApp Volumes constantly monitors all of them for availability. Out of the available domain controllers, it selects one for domain join and lookups. If the selected domain controller goes away, another domain controller from the **Available** list is used automatically. Note that the domain controller you choose isn't necessarily the specified DNS server.




You need to provide at least one accessible domain controller for the service to use. We recommend several for better domain controller availability. Make sure there is a routed network path between NetApp Volumes and the domain controllers, and that the [firewall rules on your domain controllers](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#firewall_rules_for_active_directory_access) allow NetApp Volumes to connect.

For more information, see [Active Directory design considerations and best practices](https://social.technet.microsoft.com/wiki/contents/articles/52587.active-directory-design-considerations-and-best-practices.aspx#AD_Site_Layout).

### Active Directory domain controller topologies

Once you successfully connect to Active Directory domain controllers, you can use the following file sharing protocols:

  * SMB

  * NFSv3 with extended groups

  * NFSv4 with security principals and Kerberos




The following scenarios describe potential topologies. These scenarios focus on the domain controller used by NetApp Volumes. Other domain controllers for the same domain are described only where required. We recommend that you deploy at least two domain controllers for redundancy and availability.

Topology | Description  
---|---  
**Active Directory domain controller and volumes in one region** | This scenario is the simplest deployment strategy where a domain controller is in the same region as the volume.  
**Active Directory domain controller and volumes in separate regions** | You can use a domain controller in a different region from a volume. This configuration might negatively affect authentication and file access performance.  
**Active Directory domain controllers in multiple regions using AD sites** | If you use volumes in multiple regions, we recommend that you place at least one domain controller in each region. Although the service automatically selects the domain controller, we recommend that you manage domain controller selection with Active Directory sites.  
**Active Directory domain controller in an on-premises network** | You can use an on-premises domain controller over VPN, but it can negatively affect end user authentication and file access performance. Don't add additional Virtual Private Cloud peering hops in your network path. VPC peering is subject to transitive routing restrictions. Traffic isn't routed beyond the VPC peering hop that NetApp Volumes already consumes.  
**Active Directory domain controller in a different VPC network** | You can't place the domain controller in a different VPC because Google Cloud VPC peering doesn't allow transitive routing. Alternatively, you can connect the VPCs using VPN, attach NetApp Volumes to a shared VPC network that hosts the Active Directory domain controllers; or [connect additional networks](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/connect-additional-networks). If you attach NetApp Volumes to a shared VPC network, then this configuration is similar to one of the preceding scenarios.  
  
## What's next

  * [Create an Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy).

  * [Connect to Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/connect-to-managed-service-for-microsoft-ad).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
