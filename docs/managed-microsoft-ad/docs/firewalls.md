---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls/
title: Configure firewalls for Managed Microsoft AD \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:37.150650+00:00
---

# Configure firewalls for Managed Microsoft AD  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Configure firewalls for Managed Microsoft AD Stay organized with collections  Save and categorize content based on your preferences. 

Domain controllers operated by Managed Service for Microsoft Active Directory expose a number of services, including LDAP, DNS, Kerberos, and RPC. Depending on your use cases, Virtual Machines (VMs) deployed on Google Cloud, as well as machines running on-premises, might need access to these services to take advantage of Active Directory.

To reduce the attack surface of domain controllers and VMs, you should use firewalls to disallow any network communication that is not strictly required. This article describes how to configure firewalls to accommodate common Active Directory use cases while disallowing other network communication.

## Logon versus authentication

While the terms logon and authentication are often used interchangeably, they have different meanings in the context of Windows security. **Logon** describes the process that occurs on the system a user is gaining access to. In contrast, **authentication** is performed by the computer on which the user's account resides.

When you use a local account to log on to a machine, both logon and authentication are handled by the target machine. In an Active Directory environment, it is more common to use a domain user to log on. In that case, the logon is handled by the target machine, while authentication is performed by a domain controller.

To authenticate, a client can use either [Kerberos](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-kerberos) or [NTLM](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-ntlm) . Once a client authenticates, the target machine needs to process the logon. Depending on the [logon type](https://docs.microsoft.com/en-us/windows/win32/api/ntsecapi/ne-ntsecapi-security_logon_type) the client requested, this might require additional interaction with domain controllers using protocols such as Kerberos, NTLM, [LDAP](https://www.ietf.org/rfc/rfc3377.txt) , [RPC](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rpce/290c38b1-92fe-4229-91e6-4fc376610c15) , or [SMB](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-smb/f210069c-7086-4dc2-885e-861d837df688) .

Because authenticating and processing logons require different protocols, it is helpful to distinguish between the two concepts when identifying the right firewall configuration.

## Common use cases

The following sections describe common use cases for accessing Managed Microsoft AD and show which firewall rules you need to configure for each use case.

If you don't plan to integrate Managed Microsoft AD with an on-premises Active Directory, you only need to read the first section of this article,  Accessing Managed Microsoft AD from within your VPC. If you intend to create a trust relationship between Managed Microsoft AD and an on-premises Active Directory, the entire article applies.

**Note:** You should consider the firewall rules described for each use case as a baseline. Depending on your use case, you might need to permit communication over additional protocols and ports. Refer to the Microsoft article [Service overview and network port requirements for Windows](https://support.microsoft.com/en-us/help/832017/service-overview-and-network-port-requirements-for-windows) for further details.

You can use [firewall rule logs](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging) to analyze if additional ports might be required. Because the [implied deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule has logging disabled, you must first create a custom, low-priority firewall rule that denies all ingress traffic, but has firewall logging enabled. With this rule in place, any failed connection attempt causes a log entry to be published to [Stackdriver](https://docs.cloud.google.com/logging). As firewall rules can produce a significant volume of logs, consider disabling firewall logging again once you have completed your analysis.

## Accessing Managed Microsoft AD from within your VPC

When you use the [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) to deploy Managed Microsoft AD, no further configuration is required to enable VMs in the [VPC](https://docs.cloud.google.com/vpc) to access Active Directory.

If you have customized your VPC configuration or firewall rules, you must ensure your firewall configuration still permits communication with Managed Microsoft AD. The following sections describe firewall rules you might need to create.

### Domain name resolution

When a VM attempts to resolve a DNS name, it does not directly query a domain controller. Instead, the DNS query is sent to the metadata server, which is the default DNS server configured for Compute Engine VMs. The metadata server then forwards the query to a Cloud DNS private [DNS forwarding zone](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods) created by Managed Microsoft AD. This forwarding zone then forwards the query to the appropriate domain controller.

![Domain name resolution](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-1.png)

You do not need to configure any firewall rules to enable this use case. Communication to Cloud DNS (1) is always permitted for VMs in a VPC and Managed Microsoft AD allows forwarded DNS requests from Cloud DNS Cloud DNS (2) by default.

### Authenticating to a VM using Kerberos

A user that has logged in to one VM might require access to a service provided by a different VM. For example, a user might attempt to open a RDP connection, access a file share, or access an HTTP resource that requires authentication.

To allow a user to authenticate to the server VM using Kerberos, the client VM has to obtain an appropriate Kerberos ticket from one of the Managed Microsoft AD controllers first.

![Authenticating to a VM using Kerberos](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-2.png)

To enable VMs to authenticate to another by using Kerberos, the following communication needs to be permitted by firewall rules:

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Client VM | Managed Microsoft AD subnet |  Kerberos (UDP/88, TCP/88)  
LDAP (UDP/389, TCP/389)   
2 | Allow | Client VM | Server VM |  Protocol used to access VM, such as HTTP (TCP/80, TCP/443) or RDP (TCP/3389)   
3 | Allow | Server VM | Managed Microsoft AD subnet | See processing logons.  
  
### Authenticating to a VM using NTLM

Although Windows [prefers Kerberos over NTLM](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-negotiate) in most cases, clients might occasionally need to fall back to using NTLM for authentication. NTLM relies on [pass-through authentication](https://support.microsoft.com/en-us/help/102716/ntlm-user-authentication-in-windows) , and therefore requires the server to communicate with one of the Managed Microsoft AD domain controllers to authenticate the user.

![Authenticating to a VM using NTLM](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-3.png)

To enable VMs to authenticate other VMs using NTLM, the following communication needs to be permitted by firewall rules:

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Client VM | Server VM |  Protocol used to access VM, such as HTTP (TCP/80, TCP/443) or RDP (TCP/3389)   
2 | Allow | Client VM | Managed Microsoft AD subnet | See processing logons.  
  
### Domain joining and processing logons

To operate as a domain member and process logons from users, a machine needs to be able to interact with Active Directory. The exact set of protocols used depends on the logon type that individual clients request. To support all common scenarios, you should permit the following combination of protocols.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Server VM | Managed Microsoft AD subnet |  Kerberos (UDP/88, TCP/88)  
NTP (UDP/123)  
RPC (TCP/135, TCP/49152-65535)  
LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)  
LDAP GC (TCP/3268)  
  
  
Additionally, depending on your exact use case, you might also want to permit the following protocols:

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Server VM | Managed Microsoft AD subnet |  Kerberos password change (UDP/464, TCP/464)  
Secure LDAP (TCP/636, TCP/3269)   
  
### Administering Managed Microsoft AD

You must use a [domain-joined VM](https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain) to manage Managed Microsoft AD. To use tools such as Active Directory Administrative Center on this VM, the VM must also be able to access the Active Directory Web Services exposed by Managed Microsoft AD domain controllers.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Admin VM | Managed Microsoft AD subnet |  AD Web Services (TCP/9389)   
  
## Connecting Managed Microsoft AD to an on-premises Active Directory

To connect Managed Microsoft AD to an on-premises Active Directory, you have to create a trust relationship between forests. Additionally, you should enable DNS name resolution between Google Cloud and your on-premises environment.

### Trust creation and verification

In order to create and verify a forest trust, the Managed Microsoft AD domain controllers and the root domain controllers of your on-premises forest must be able to bidirectionally communicate.

![Trust creation and verification](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-4.png)

To enable trust creation and verification, configure your on-premises firewall to permit ingress and egress traffic that matches these characteristics:

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | On-premises AD | Managed Microsoft AD |  DNS (UDP/53, TCP/53)  
Kerberos (UDP/88, TCP/88)  
Kerberos password change (UDP/464, TCP/464)  
RPC (TCP/135, TCP/49152-65535)  
LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)  
  
2 | Allow | Managed Microsoft AD | On-premises AD |  DNS (UDP/53, TCP/53)  
Kerberos (UDP/88, TCP/88)  
Kerberos password change (UDP/464, TCP/464)  
RPC (TCP/135, TCP/49152-65535)  
LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)  
  
  
Managed Microsoft AD is preconfigured to permit traffic matching these characteristics, so you do not need to configure additional firewall rules on Google Cloud.

### Resolving Google Cloud DNS names from on-premises

There are two ways you can allow on-premises machines to resolve DNS names in Managed Microsoft AD: DNS delegation and conditional DNS forwarding.

#### DNS delegation

The DNS domain used by Managed Microsoft AD might be a subdomain of the DNS domain used on-premises. For example, you might use cloud.example.com for Managed Microsoft AD while using example.com on premises. To allow on-premises clients to resolve the DNS names of Google Cloud resources, you can set up DNS delegation.

When using DNS delegation, attempts to resolve the DNS name of a Google Cloud resource first query an on-premises DNS server. The DNS server then redirects the client to Cloud DNS, which in turn forwards the request to one of your Managed Microsoft AD domain controllers.

![DNS delegation](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-5.png)

Exposing Cloud DNS to on-premises networks requires [creating and inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in). This will create an inbound forwarder IP address that is part of your VPC.

To use the forwarder address from on-premises, configure your on-premises firewall to permit egress traffic that matches the characteristics below.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | On-premises AD | Managed Microsoft AD |  DNS (UDP/53, TCP/53)  
Kerberos (UDP/88, TCP/88)  
Kerberos password change (UDP/464, TCP/464)  
RPC (TCP/135, TCP/49152-65535)  
LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)  
  
2 | Allow | Managed Microsoft AD | On-premises AD |  DNS (UDP/53, TCP/53)  
Kerberos (UDP/88, TCP/88)  
Kerberos password change (UDP/464, TCP/464)  
RPC (TCP/135, TCP/49152-65535)  
LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)  
  
  
#### Conditional DNS forwarding

The DNS domain used by Managed Microsoft AD might not be a subdomain of the DNS domain used on premises. For example, you might use`cloud.example.com` for Managed Microsoft AD while using `corp.example.local` on premises.

In scenarios where the DNS domains are unrelated, you can set up conditional DNS forwarding in your on-premises Active Directory DNS. All queries that match the DNS name used by Managed Microsoft AD will then be forwarded to Cloud DNS.

![Conditional DNS forwarding](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-6.png)

To use conditional DNS forwarding, you need to set up a [DNS policy that enables inbound DNS forwarding](https://docs.cloud.google.com/dns/docs/policies#create-in) first. To use the resulting forwarder address from on premises, configure your on-premises firewall to permit egress traffic that matches the characteristics below.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | On-premises AD | DNS forwarding IP address | DNS (UDP/53, TCP/53)  
  
On the Google Cloud side, create a [firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls) to permit ingress traffic matching these criteria.

You do not need to configure any firewall rules to enable communication from the DNS Forwarder to Cloud DNS (2).

### Resolving on-premises DNS names from Google Cloud

Managed Microsoft AD uses conditional DNS forwarding to resolve DNS names in your on-premises forest. To also allow clients running in Google Cloud to resolve DNS names that are managed by an on-premises Active Directory, you can create a [private forwarding zone](https://docs.cloud.google.com/dns/zones#creating-forwarding-zones) in Cloud DNS DNS that forwards queries to on-premises domain controllers.

![Resolving on-premises DNS names](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-7.png)

To enable resolving on-premises DNS names from Google Cloud, configure your on-premises firewall to permit ingress traffic per the following table.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Managed Microsoft AD | On-premises AD | DNS (UDP/53, TCP/53)  
2 | Allow | [Cloud DNS ](https://docs.cloud.google.com/dns/zones#creating-forwarding-zones)(35.199.192.0/19) | On-premises AD | DNS (UDP/53, TCP/53)  
  
Google Cloud allows corresponding egress traffic [by default](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).

## Accessing Managed Microsoft AD resources from on premises

If the Managed Microsoft AD forest is set up to trust your on-premises forest, you might want on-premises users and machines to be able to access resources in the Managed Microsoft AD forest.

### Authenticating to a VM from on-premises using Kerberos

A user that has logged in to an on-premises machine might require access to a service provided by a VM that runs on Google Cloud and is a member of a Managed Microsoft AD forest. For example, a user might attempt to open an RDP connection, access a file share, or access an HTTP resource that requires authentication.

To allow users to authenticate to the server VM using Kerberos, the client machine has to obtain an appropriate Kerberos ticket. This requires communicating with one of the on-premises domain controllers, as well as with one of the Managed Microsoft AD domain controllers.

![Authenticating to a VM from on-premises using Kerberos](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-8.png)

To enable on-premises VMs to authenticate by using Kerberos, configure your on-premises firewall to permit the following egress traffic.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Client machine (on-premises) | Managed Microsoft AD subnet |  LDAP (UDP/389, TCP/389)  
Kerberos (UDP/88, TCP/88)   
2 | Allow | Client machine (on-premises) | Server VM (Google Cloud) | Protocol used by application, such as HTTP (TCP/80, TCP/443) or RDP (TCP/3389)  
3 | Allow | Server VM | Managed Microsoft AD subnet | See processing logons.  
  
On the Google Cloud side, create [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) to permit ingress traffic for (1) and (2). Egress traffic to Managed Microsoft AD (3) is allowed [by default](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).

### Authenticating to a VM from on-premises using NTLM

When using NTLM to authenticate a user from an on-premises Active Directory forest to a server VM joined to a Managed Microsoft AD forest, the Managed Microsoft AD domain controllers need to communicate with the on-premises domain controllers.

![Authenticating to a VM from on-premises using NTLM](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-9.png)

To enable on-premises VMs to authenticate by using NTLM, configure your on-premises firewall to permit ingress and egress traffic as follows.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Client machine (on-premises) | Server VM (Google Cloud) | Protocol used by application, such as HTTP (TCP/80, TCP/443) or RDP (TCP/3389)   
2 | Allow | Server VM | Managed Microsoft AD subnet | See processing logons.  
3 | Allow | Managed Microsoft AD subnet | On-premises AD  |  LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)   
  
On the Google Cloud side, create [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) to permit ingress traffic for (1). Egress traffic for (2) and (3) is allowed [by default](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).

### Processing logons for users of the on-premises forest

To process a logon for a user of the on-premises forest, a VM needs to be able to interact with the on-premises Active Directory. The exact set of protocols used depend on the [logon type](https://docs.microsoft.com/en-us/windows/win32/api/ntsecapi/ne-ntsecapi-security_logon_type) that the client requested. To support all common scenarios, configure your on-premises firewall to permit ingress traffic that matches these characteristics.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Server VM (Google Cloud) | On-premises AD subnet |  Kerberos (UDP/88, TCP/88)  
NTP (UDP/123)   
RPC (TCP/135, TCP/49152-65535)  
LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)  
LDAP GC (TCP/3268)  
  
  
Depending on your exact use case, you might also want to permit the following protocols.

  * Kerberos password change (UDP/464, TCP/464)
  * Secure LDAP (TCP/636, TCP/3269)



On the Managed Microsoft AD side, corresponding egress traffic is allowed [by default](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).

On administrative VMs, you might not plan to allow logons from users of the on-premises forest. One activity that you likely have to perform on administrative VMs however is managing group memberships. Whenever you use the object picker to reference a user or group form your on-premises forest, the object picker will require access to the on-premises domain controllers. For this to work, the administrative VM requires the same access to your on-premises Active Directory domain controllers as it would for processing logons for users of the on-premises forest.

## Accessing on-premises Active Directory resources from Google Cloud

If your on-premises forest is set up to trust the Managed Microsoft AD forest, then you might want users from the Managed Microsoft AD forest to be able to access on-premises resources.

### Authenticating to an on-premises VM using Kerberos

A user that has logged in to a VM running on Google Cloud and that is a member of the Managed Microsoft AD forest might require access to a service provided by an on-premises machine that is a member of your on-premises forest. For example, the user might attempt to open an RDP connection, access a file share, or access an HTTP resource that requires authentication.

To allow the user to authenticate to the on-premises machine using Kerberos, the VM has to obtain an appropriate Kerberos ticket. This requires first communicating with one of the Managed Microsoft AD controllers and then with the on-premises domain controllers.

![Authenticating to an on-premises VM using Kerberos](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-10.png)

To enable on-premises VMs to authenticate by using Kerberos, configure your on-premises firewall to permit ingress traffic that matches the characteristics below.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Client VM (Google Cloud) | Managed Microsoft AD subnet |  Kerberos (UDP/88, TCP/88)  
LDAP (UDP/389, TCP/389)  
Implied by processing logons  
2 | Allow | Client VM (Google Cloud) | On-premises AD|  Kerberos (UDP/88, TCP/88)  
LDAP (UDP/389, TCP/389)   
3 | Allow | Client VM (Google Cloud) | Server machine (on-premises) | Protocol used by application, such as HTTP (TCP/80, TCP/443) or RDP (TCP/3389)  
  
On the Google Cloud side, corresponding egress traffic is allowed [by default](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).

### Authenticating to an on-premises VM using NTLM

When using NTLM to authenticate a user from the Managed Microsoft AD forest to a server machine that is joined to your on-premises forest, the on-premise domain controllers need to be able to communicate with the Managed Microsoft AD domain controllers:

![Authenticating to an on-premises VM using NTLM](https://docs.cloud.google.com/static/managed-microsoft-ad/img/fw-11.png)

To enable on-premises VMs to authenticate by using Kerberos, configure your on-premises firewall to permit ingress and egress traffic that matches these characteristics.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Client VM (Google Cloud) | Server machine (on-premises)  | Protocol used by application, for example HTTP (TCP/80, TCP/443) or RDP (TCP/3389)   
2 | Allow | On-premises AD | Managed Microsoft AD subnet |  LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)   
  
On the Google Cloud side, egress traffic for (1) and ingress traffic for (2) is allowed [by default](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).

### Processing logons for users of the Managed Microsoft AD forest

To process a logon for a user of the Managed Microsoft AD forest, a machine running on-premises needs to be able to interact with Managed Microsoft AD domain controllers. The exact set of protocols used depend on the [logon type](https://docs.microsoft.com/en-us/windows/win32/api/ntsecapi/ne-ntsecapi-security_logon_type) that the client requested. To support all common scenarios, you should permit the following combination of protocols.

| Action | From | To | Protocols  
---|---|---|---|---  
1 | Allow | Server machine (on-premises) | Managed Microsoft AD subnet |  Kerberos (UDP/88, TCP/88)  
NTP (UDP/123)  
RPC (TCP/135, TCP/49152-65535)  
LDAP (UDP/389, TCP/389)  
SMB (UDP/445, TCP/445)  
LDAP GC (TCP/3268)  
  
  
Depending on your exact use case, you might also want to permit the following protocols.

  * Kerberos password change (UDP/464, TCP/464)
  * Secure LDAP (TCP/636, TCP/3269)



Make sure that your on-premises firewalls permit egress traffic that matches these characteristics. You do not need to configure any firewall rules in Google Cloud to enable corresponding ingress traffic to Managed Microsoft AD.

On administrative machines, you might not plan to allow logons from users of the Managed Microsoft AD forest. One activity that you likely have to perform on administrative machines is managing group memberships. Whenever you use the object picker to reference a user or group from the Managed Microsoft AD forest, then the object picker will require access to the Managed Microsoft AD domain controllers. For this to work, the administrative machine requires the same access to the Managed Microsoft AD domain controllers as it would for processing logons for users of the Managed Microsoft AD forest.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
