---
url: https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/troubleshoot-kerberos-encryption-types/
title: Troubleshoot Kerberos encryption types for Active Directory \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:58.785152+00:00
---

# Troubleshoot Kerberos encryption types for Active Directory  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/troubleshoot-kerberos-encryption-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Troubleshoot Kerberos encryption types for Active Directory Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to identify the Kerberos encryption type (enctype) that clients use when they access NetApp Volumes over SMB or NFS with Active Directory Kerberos.

SMB and NFS don't negotiate enctypes. The Key Distribution Center (KDC) chooses the enctype when it issues the Kerberos ticket.

  * SMB typically uses the service principal name (SPN) `cifs/<server_fqdn>`

  * NFS with Kerberos typically uses the SPN `nfs/<server_fqdn>`




Authentication succeeds only if the client, the KDC, and the NetApp Volumes computer account share at least one supported enctype. For more information about how NetApp Volumes advertises enctypes and when the domain join occurs, see [How Active Directory policies join the domain](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#how_active_directory_policies_join_the_domain).

## Before you begin

Complete the following prerequisites before you begin.

  1. Confirm that the storage pool has an Active Directory policy attached and that the domain join completed successfully. For more information, see [Test the Active Directory policy connection](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection).

  2. Confirm that clients, domain controllers, and NetApp Volumes can connect to each other over the network. For more information, see [Test connectivity to Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/test-connectivity-netapp-volumes).

  3. Find the NetApp Volumes computer account name in Active Directory:

     * Standard, Premium, and Extreme pools can have more than one account.

     * Flex Unified and Flex File pools use one account per pool.




To learn about account behavior by service level, see [How Active Directory policies join the domain](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#how_active_directory_policies_join_the_domain).

## Look up enctypes on NetApp Volumes computer accounts

Kerberos enctypes for a file server are stored on the server computer account in Active Directory, in the `msDS-SupportedEncryptionTypes` attribute. This attribute indicates the enctypes that the NetApp Volumes computer account advertises to the KDC.

### Query the computer account

To query on a domain-joined machine with the Active Directory module installed:
    
    
     Get-ADComputer -Identity "COMPUTER_ACCOUNT_NAME" -Properties msDS-SupportedEncryptionTypes |
      Select-Object Name, msDS-SupportedEncryptionTypes
    

Replace COMPUTER_ACCOUNT_NAME with the NetApp Volumes computer account name.

To query with LDAP:
    
    
     ([adsisearcher]"(&(objectClass=computer)(name=COMPUTER_ACCOUNT_NAME))").FindOne().
      Properties["msdssupportedencryptiontypes"]
    

### Decode the bitmask

`msDS-SupportedEncryptionTypes` is a bitmask defined in [MS-KILE](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/6cfc7b50-11ed-4b4d-846d-6f08f0812919). The following are the common values:

  * `0x1`: DES-CBC-CRC

  * `0x2`: DES-CBC-MD5

  * `0x4`: RC4-HMAC

  * `0x8`: AES128-CTS-HMAC-SHA1-96

  * `0x10`: AES256-CTS-HMAC-SHA1-96




If the attribute is blank or `0`, the KDC applies its own defaults for that account. For more information, see How enctype selection works.

**Note:** If you enabled **Enable AES Encryption for Active Directory authentication** after the computer account was created, the account doesn't show AES in this attribute. Compare the value with the settings in your Active Directory policy. For more information, see Limit enctypes advertised by Google Cloud NetApp Volumes.

## How enctype selection works

Enctype selection is an intersection of three factors. The KDC selects the strongest common enctype.

  1. **Client** : advertises supported enctypes in the Kerberos `AS-REQ` or `TGS-REQ`.

  2. **KDC** : applies domain controller configuration and operating system defaults.

  3. **Target account** : limits the enctypes that the KDC can use for that service ticket through the `msDS-SupportedEncryptionTypes` attribute on the NetApp Volumes computer account.




The KDC performs the following actions:

  1. Computes the intersection of client, KDC, and target-account enctypes.

  2. Selects the strongest enctype in that set.

  3. Issues a ticket encrypted with that enctype, plus a session key that can use a different, often stronger, enctype.




### When `msDS-SupportedEncryptionTypes` is blank or zero

For accounts without a configured value, the KDC uses `DefaultDomainSupportedEncTypes` on the domain controller. Your domain administrators control that setting. For more information, see [Microsoft documentation on Kerberos encryption type selection](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/6cfc7b50-11ed-4b4d-846d-6f08f0812919).

## Ticket encryption versus session key encryption

You can distinguish two enctypes per ticket:

  * **Ticket encryption** : shown as `KerbTicket Encryption Type` in `klist` output.

  * **Session key encryption** : shown as `Session Key Type` in `klist` output.




A ticket can be RC4-encrypted while the session key is AES, depending on configuration and the AES-SK bit (`0x400`).

If the client, KDC, and NetApp Volumes computer account don't share at least one enctype, authentication fails. Typical indicators include KDC events 16 or 27 and client Security-Kerberos event 4.

## Limit enctypes advertised by NetApp Volumes

NetApp Volumes controls which enctypes it advertises on its Active Directory computer accounts through the Active Directory policy.

By default, NetApp Volumes advertises DES and RC4-HMAC. When you select **Enable AES Encryption for Active Directory authentication** in the Active Directory policy, NetApp Volumes also advertises AES-128 and AES-256. For more information about field descriptions, see [Create an Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy).

To confirm what a pool advertises after domain join, query `msDS-SupportedEncryptionTypes` on the NetApp Volumes computer account. For more information, see Look up enctypes on NetApp Volumes computer accounts.

**Note:** NetApp Volumes doesn't control which enctypes clients or domain controllers offer. The KDC selects from the intersection of all three. To restrict enctypes on clients or in your domain, work with your Active Directory administrators. For more information, see Related resources.

## Look up enctypes on clients

To check which Kerberos encryption types your clients are using, run the command for your client operating system.

### Windows clients

To view the Kerberos encryption types after authentication:
    
    
     klist
    

For an SMB session, find the ticket whose `Server` value is `cifs/<server_fqdn>`. For NFS with Kerberos, look for `nfs/<server_fqdn>`.

The following fields show the encryption types:

  * `KerbTicket Encryption Type`: the ticket enctype

  * `Session Key Type`: the session key enctype




To view a specific logon session:
    
    
     klist tickets -li 0x3e7
    

### Linux or macOS clients

To show cached tickets and their encryption types:
    
    
     klist -e
    

To view keytab contents:
    
    
     klist -kte /path/to/keytab
    

## Look up enctypes in domain controller events

If Kerberos auditing is enabled on your domain controllers, event `4769` (Kerberos service ticket requested) records the enctype that was used for a service ticket. Filter for SMB by the service name `cifs/...` or for NFS by the service name `nfs/...`.

Relevant fields in event `4769` include the following:

  * `Ticket Encryption Type`: `0x12` is AES256, `0x11` is AES128, and `0x17` is RC4-HMAC

  * `SessionKeyEncryptionType`: the encryption type for the session key

  * `ServiceSupportedEncryptionTypes`: the encryption types that the service account advertises

  * `ClientAdvertizedEncryptionTypes`: the encryption types that the client sent

  * `Service Name`: the service name, such as `cifs/...` or `nfs/...`

  * `Client Address`: the client address




Event 4768 (Kerberos authentication service) records enctype usage for ticket-granting tickets.

The following XML filter is an example for RC4 service tickets in the Security log:
    
    
    <QueryList>
      <Query Id="0" Path="Security">
        <Select Path="Security">
          *[EventData[Data[@Name='TicketEncryptionType'] and (Data='0x17')]]
        </Select>
      </Query>
    </QueryList>
    

To summarize enctype usage from domain controller event logs over time, your domain administrators can use [Get-KerbEncryptionUsage.ps1](https://github.com/microsoft/Kerberos-Crypto/blob/main/scripts/Get-KerbEncryptionUsage.ps1).

## Related resources

Your Active Directory administrators configure enctype limits on clients and domain controllers. NetApp Volumes documentation doesn't cover those settings. For more information, see the following resources:

  * [Network security: Configure encryption types allowed for Kerberos](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos) — client Group Policy setting

  * [MS-KILE: Kerberos Protocol Extensions](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/6cfc7b50-11ed-4b4d-846d-6f08f0812919) — `msDS-SupportedEncryptionTypes` bitmask and KDC behavior




## What's next

  * Review [Google Cloud NetApp Volumes Active Directory integration](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad) for use cases and domain controller requirements.

  * [Known issues and limitations](https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/known-limitations) for service-level constraints.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
