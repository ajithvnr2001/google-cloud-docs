---
url: https://docs.cloud.google.com/compute/docs/instances/windows/best-practices/
title: Best practices for running Active Directory on Google Cloud \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:42:08.317679+00:00
---

# Best practices for running Active Directory on Google Cloud  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for running Active Directory on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This guide presents best practices for running Active Directory on Google Cloud. The guide focuses on practices that are either specific to Google Cloud or of particular importance when deploying Active Directory on Google Cloud. Consider the guide to be complementary to the general [best practices for securing Active Directory published by Microsoft](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory).

## Architecture

The following sections detail best practices related to architecture.

### Use the architecture pattern that best fits your requirements

To deploy Active Directory on Google Cloud, you first have to decide which domain and forest architecture to use. If you already use Active Directory, you also have to decide whether and how to integrate the two environments.

Which design fits your situation best depends on a number of factors, including the design of your on-premises network, how on-premises and Google Cloud resources are going to interact, as well as your requirements for availability and administrative autonomy. Refer to our [patterns for using Active Directory in a hybrid environment](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment) to see how these factors must determine your design.

![](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-1.svg)

If you want to [maintain a trust boundary](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#trust_boundaries_in_active_directory) between Google Cloud and your on-premises environment, consider implementing the [resource forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#resource_forest) pattern. In this pattern, you deploy a separate forest on Google Cloud and use a one-way forest trust to integrate the Google Cloud forest with your existing on-premises Active Directory forest.

### Separate testing and production

Depending on your use of Active Directory, it might be necessary to perform frequent changes in Active Directory during the development and testing of applications. Developers might need to be able to create and modify [Active Directory accounts](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/service-accounts), change group memberships if applications use groups to handle authorization, or join and remove computers.

To prevent development and testing work from impacting production workloads or hampering the security of your deployment, consider deploying a separate Active Directory domain or forest for development and testing.

![](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-2.svg)

Having a separate development and testing domain or forest also allows you to verify administrative changes before applying them to production. Examples of such changes include experimenting with group policies, testing automation scripts, or potentially risky actions such as raising a forest's functional level.

### Set up Cloud Identity federation in addition to deploying Active Directory on Google Cloud

Deploying Active Directory on Google Cloud allows you to manage Windows VMs on Google Cloud, can enable users to log in to Windows VMs using their existing user accounts, and supports [applications that rely on Kerberos, NTLM, or LDAP](https://docs.cloud.google.com/solutions/authenticating-corporate-users-in-a-hybrid-environment#resources_that_cannot_use_google_as_idp) for authentication.

However, to use the [Google Cloud console](https://docs.cloud.google.com/docs/overview#google-cloud-console), [the `gcloud` command-line tool](https://docs.cloud.google.com/sdk/gcloud), or other Google and Google Cloud tools, you have to authenticate with a Google identity. Deploying Active Directory on Google Cloud is therefore not a replacement for [federating your existing Active Directory with Google Cloud](https://docs.cloud.google.com/solutions/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#patterns_for_federating_an_external_idp_with_gcp) if you are intending to use Active Directory as your leading system for managing users.

For example, if you deploy a separate forest on Google Cloud, then you can set up federation against your on-premises Active Directory as illustrated by the following diagram. Users with accounts in the on-premises Active Directory can then use tools that require a Google identity as well as your applications that rely on Active Directory for authentication.

![A Google Cloud forest federated with an on-premises Active Directory
          domain. The two forests are joined to the domain with a one-way
          forest trust.](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-3.svg)

If you instead decide to [extend your existing forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#extended_forest) or [domain](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#extended_domain) to Google Cloud, then you also have the option to use domain controllers and AD FS servers deployed on Google Cloud to set up the federation.

![An on-premises AD domain that has been extended to a
          Google Cloud Active Directory domain using a
          domain trust.](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-4.svg)

Federation also allows you to enforce a [common lifecycle](https://docs.cloud.google.com/solutions/federating-gcp-with-active-directory-introduction#implementing_federation) for Google accounts and Active Directory Accounts, so that when you disable a user account in your on-premises Active Directory, the corresponding Google user is also suspended.

## Networking

The following section details best practices related to networking.

### Deploy Active Directory into a Shared VPC network

To allow Active Directory to be used across multiple projects, deploy domain controllers into a Shared VPC network. Using a Shared VPC network has multiple advantages:

  * Each application that might require Active Directory access can potentially be deployed into a separate project. Using separate projects helps isolate resources and allows you to manage access individually.

  * You can use a [dedicated project](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#dedicated-dcs) for Active Directory domain controllers, which allows you fine-grained control over which of your users can access related Google Cloud resources.

  * Shared VPC networks allow you to centralize IP address management and firewall configuration, which helps ensuring consistency across multiple projects.




As VPCs are a [global resource](https://docs.cloud.google.com/vpc/docs/vpc#specifications), you can use the same Shared VPC network across multiple regions.

### Do not expose domain controllers externally

To reduce the attack surface of Active Directory, avoid assigning external IP addresses to domain controllers.

Because VM instances without external IP addresses do not have internet access by default, you need to take additional steps to ensure that Windows activation and Windows updates are not impaired on domain controllers.

To support Windows activation, enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet that you plan to deploy domain controllers in, and ensure that the VM instances can access [kms.windows.googlecloud.com](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server). This allows activation to occur without direct internet access.

There are multiple options to support Windows updates:

  * If you have an on-premises [WSUS server](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus), you can configure [hybrid connectivity](https://docs.cloud.google.com/hybrid-connectivity) and configure your domain controllers to use the WSUS server as the source for updates.

  * You can enable internet access via a NAT gateway by deploying [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview).

  * If you have set up hybrid connectivity, you can also route outbound traffic via an on-premises NAT gateway or proxy server.




### Reserve static IP addresses for domain controllers in advance

Because domain controllers serve as DNS servers, they need to be assigned an IP address _that does not change_. To achieve that, [configure static internal IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address) for the domain controller VMs.

When you reserve an IP address, the default behavior is that an unused address is chosen automatically. To ensure that IP addresses of domain controllers are easy to memorize, [reserve an internal static IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

On the domain controllers, set the IP address of the network adapter to the same address. Although this step is optional, it prevents Active Directory from emitting warning messages indicating that the IP address of the machine might still be dynamically assigned.

### Deploy domain controllers across multiple zones

To increase availability, deploy at least two domain controllers and [distribute them over multiple zones](https://docs.cloud.google.com/solutions/deploy-fault-tolerant-active-directory-environment). Because subnets and IP addresses are not tied to a zone, you can deploy all domain controllers into a single subnet.

If you plan to deploy workloads across multiple regions, consider deploying domain controllers in each relevant region. Because [subnets are a regional resource](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets), deploying into an extra region will require an additional subnet.

### Create one site per region

When a [client tries to locate a domain controller](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/enabling-clients-to-locate-the-next-closest-domain-controller), it will first look for a domain controller in the [Active Directory site](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-active-directory-site-topology) that corresponds to the client's IP address. If no domain controller is available in this site, the client will proceed and attempt to locate a domain controller in a different site.

You can take advantage of this behavior by creating a separate site for each region you deploy domain controllers or domain clients in. Clients will then automatically prefer using domain controllers located in the same region, which can help reduce latency and [outbound data transfer cost between regions](https://docs.cloud.google.com/compute/pricing#network).

If you have clients in regions that do not have a domain controller, you can influence which domain controllers these clients choose by adjusting [site link costs](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/determining-the-cost) to reflect geographic closeness of regions and enabling the [Try Next Closest Site](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/enabling-clients-to-locate-the-next-closest-domain-controller) setting.

Using multiple sites influences replication behavior between domain controllers. One downside of using multiple sites can be that replication between sites occurs [less frequently](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/determining-the-interval) than intra-site replication.

However, you can't create Active Directory sites in Managed Microsoft AD because Managed Microsoft AD doesn't support Active Directory Sites and Services feature.

### Use Cloud DNS private forwarding zones

When you create a new VM instance in Compute Engine, the operating system will be preconfigured to use a default DNS server which provides access to [internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns) and public DNS.

Before you can join a machine to an Active Directory domain, you have to ensure that the machine is able to resolve the DNS records managed by Active Directory. The default DNS server that Compute Engine configures for a VM instance provides access to [internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns) and public DNS, but will not be able to resolve DNS names managed by Active Directory.

Create a [private DNS forwarding zone](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones) in Cloud DNS to allow clients to resolve DNS records managed by Active Directory. Configure the zone to forward queries that match your Active Directory domain to your domain controllers.

Using a private DNS forwarding zone has multiple advantages over configuring clients to directly use your Active Directory domain controllers as DNS servers:

  * You do not need to adjust the networking configuration of VM instances. This simplifies the process of creating new VMs.

  * When you promote or demote a domain controller, you only need to update the configuration of the private DNS forwarding zone and do not need to modify any client settings.

  * VM instances still have access to [internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns).

  * Any DNS records that do not match your Active Directory domain will be handled by Cloud DNS, reducing the load on your domain controllers.




If you use multiple domains, create a separate private DNS forwarding zone for each Active Directory domain.

Cloud DNS private forwarding zones are scoped to a single VPC. If you use multiple VPCs connected using [peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), then you can expose the private forwarding zones to other VPCs by configuring [DNS peering](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering-zones).

You still have to manually configure DNS settings on domain controllers. Use `127.0.0.1` as the primary DNS server and, optionally, use the IP address of another domain controller as the secondary DNS server. For more information, see [Recommended DNS settings and alternate options](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/best-practices-for-dns-client-settings).

## Hybrid Connectivity

The following section details best practices related to hybrid connectivity.

### Use DNS inbound forwarding to resolve Google Cloud DNS names from on-premises

Clients in your on-premises network might need to be able to resolve the DNS names of resources deployed on Google Cloud. If you [extend your forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#extended_forest) or deploy a [resource forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#resource_forest) on Google Cloud, then use DNS inbound forwarding to allow on-premises clients to look up DNS records for resources deployed on Google Cloud. To use inbound forwarding, create a [DNS server policy](https://docs.cloud.google.com/dns/docs/server-policies-overview) to allocate an inbound forwarder IP address and make this address accessible to the on-premises network.

If the DNS domain used on Google Cloud (for example, `cloud.example.com`) is a subdomain of the DNS domain used on-premises (for example, `example.com`), then set up DNS delegation. Create an `NS` record in the on-premises domain that points to the inbound forwarder IP address. The `NS` record causes clients attempting to look up a DNS name in the Google Cloud-hosted domain to be redirected to the inbound forwarder IP address.

![](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-5.svg)

If the DNS domains used on Google Cloud and your on-premises Active Directory are different (for example, `cloud.example.com` and `corp.example.com`), then configure conditional DNS forwarding in your on-premises domains and use the inbound forwarder IP address as the target. When requested to resolve a DNS name in the Google Cloud-hosted domain, on-premises domain controllers will forward the quest to the inbound forwarder IP address.

![](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-6.svg)

When using inbound DNS forward, make sure your firewalls are [configured appropriately](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls#resolving_dns_names_from_on-premises).

DNS inbound forwarding is not required if you [extend your existing domain](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#extended_domain) to Active Directory. In this scenario, all DNS records of the domain are automatically replicated across Google Cloud and your on-premises environment and made available for lookup in both environments.

### Use DNS outbound forwarding to resolve on-premises DNS names from Google Cloud

Clients running on Google Cloud might need to be able to resolve the names of resources deployed on-premises. If you [extend your forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#extended_forest) or deploy a [resource forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#resource_forest) on Google Cloud, then create a [private forwarding zone](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones) in Cloud DNS to forward DNS queries for your on-premises domains to your on-premises DNS servers.

![](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-7.svg)

When using outbound DNS forwarding, make sure your firewalls are [configured appropriately](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls#resolving_on-premises_dns_names_from).

DNS outbound forwarding is not required if you [extend your existing domain](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#extended_domain) to Active Directory. In this scenario, all DNS records of the domain are automatically replicated across Google Cloud and your on-premises environment, and made available for lookup in both environments.

### Use VPN tunnels to secure LDAP traffic

Active Directory makes extensive use of the LDAP protocol. Unlike most other protocols used by Active Directory, LDAP is not encrypted by default.

Google Cloud ensures that traffic [between virtual machines](https://docs.cloud.google.com/security/encryption-in-transit#virtual_machine_to_virtual_machine) is encrypted, so using unencrypted LDAP within your VPC is acceptable. If you connect your VPC to an on-premises network, ensure that LDAP traffic is only exchanged over trusted channels.

If you use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) to connect Google Cloud and your on-premises network, then traffic is automatically encrypted using IPSec between Google Cloud and your on-premises VPN endpoint.

[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) and [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) _do not_ provide encryption. To ensure secure communication, establish a VPN tunnel over the Interconnect connection by using a VPN appliance from the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?q=vpn).

### Use selective authentication and AES for forest trusts

When creating a trust relationship between Active Directory forests, [prefer forest trusts over external trusts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/dd560679\(v=ws.10\)#external-trusts-vs-forest-trusts) and take advantage of the following features to improve security:

  * Enable [selective authentication](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/dd560679\(v=ws.10\)#selective-authentication) on outbound trusts in the resource forest. Selective authentication ensures that users from the organizational forest cannot access resources in the resource forest unless explicitly granted permission.

  * Enable [enforcement for forest boundary for Kerberos full delegation](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831747\(v%3Dws.11\)#enforcement-for-forest-boundary-for-kerberos-full-delegation) on inbound trusts in the organizational forest. This feature helps prevent privilege escalation attacks by disallowing resources in the resource forest to request Ticket Granting Tickets (TGTs) from users in the organizational forest.

  * Enable the _The other domain supports Kerberos AES encryption_ option when creating trusts. This option ensures that tickets are used for cross-forest authentication are encrypted using AES instead of the less secure RC4 algorithm.


**Note:** Currently, AES is not automatically applied when creating a trust with Managed Microsoft AD as your resource forest. You are encouraged to manually enable AES on the other domain.

## Security

The following section details best practices related to security.

### Avoid Google Cloud security interfering with Active Directory security

Active Directory gives you fine-grained control over which users are allowed to access which resources. When machines are deployed as VM instances in Compute Engine and users have access to the underlying Google Cloud project, you have to consider additional paths that might allow a user to access a machine:

  * A project member that has been assigned the [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1) role in a Google Cloud project can use the [password reset functionality](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) to create local administrator accounts. Local administrator accounts pose a threat to the security of your Active Directory domain as they can be used to undermine group policies or to install malicious software that might capture domain credentials of other logged on users.

  * By adding a [startup script](https://docs.cloud.google.com/compute/docs/startupscript), a privileged project member can inject malicious code into a VM that is executed as `nt authority\system` the next time the machine is rebooted.

  * By using the [serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console), a privileged project member can also access the Windows Special Administration Console (SAC). Windows considers logons via the SAC as local logons. The SAC can therefore be misused to evade policies which deny logons via RDP, but miss denying local logons.

  * A privileged project member can use the SAC to issue a `crashdump` command, which can cause a memory dump to be written to disk. Such a memory dump might include sensitive information and credentials.

  * By mounting the persistent disk to a different VM or using snapshots, a privileged project member might be able to access disk contents, potentially including memory dumps, from machines the user otherwise would not have the permission to log on to.




When using Managed Microsoft AD, you are better protected against these additional access paths by default. The service does not permit privileged users in your project to reset the Domain Administrator password, run startup scripts, or access the serial console on the AD domain controller VMs.

To further mitigate these risks, make sure that the IAM permissions of projects containing domain-joined VM instances are managed on a least-privilege basis. You can further reduce risk by the user of organization policies, group policies, and shielded VMs:

  * Use an [organizational policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to disable serial port access.

  * Apply a group policy that prevents the creation of local administrator accounts by disabling the [account manager](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#configure-windows-features). Define an **INI Files** preference in your group policy (Computer Configuration > Preferences > Windows Settings > Ini Files) to apply the following setting:

    * Action: Update
    * File Path: `C:\Program Files\Google\Compute Engine\instance_configs.cfg`
    * Section Name: `accountManager`
    * Property Name: `disable`
    * Property Value: `true`
  * Apply a group policy that removes any local administrator accounts from VM instances. Use the **Local Users and Groups** functionality (Computer Configuration > Preferences > Control Panel Settings > Local Users and Groups) to remove group membership from the **Administrators** group and other sensitive groups.

  * Consider using shielded VMs in combination with BitLocker disk encryption to avoid persistent disk or snapshots from being readable by unauthorized users.




### Avoid Active Directory security interfering with Google Cloud security

In an Active Directory domain, machines trust domain controllers to handle authentication and authorization on their behalf. Unless restricted by group policy, a machine's local security policy, or selective authentication, a user that has successfully proven their identity to one of the domain controllers is allowed to log on to any machine in the domain.

The ability for Active Directory users to log on to any machine might enable attackers to perform lateral movements within a domain. Such lateral movements can lead to escalations of privilege if some VM instances are exempted from firewall restrictions or use Google Cloud [service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts): The credentials of a service account are accessible to all processes and users on a VM instance. Any user that can use Active Directory to log on to a machine can therefore access these service account credentials to gain access to any Google Cloud resources that the service account is granted access to.

When setting up Managed Microsoft AD, the service creates a group to make it easy to allow specific users the ability to RDP into domain-joined VMs.

To reduce the risk of lateral movements, [organize users into administrative tiers](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#organize-resources) and use the _Deny access to this computer from the network_ and _Deny logon through Remote Desktop Services_ group policies to restrict access to your VMs based on tier level.

In a [resource forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#resource_forest) topology, take additional advantage of selective authentication to further restrict the set of users from other forests that are allowed to log on to your VMs. You can simplify managing selective authentication permissions by aligning [Google Cloud and Active Directory resource structures](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#align-resources): If Active Directory organizational units map to Google Cloud projects, you can grant users the right to authenticate on a level that matches a Google Cloud project.

In cases where neither selective authentication nor group policies are applicable, create a separate service account, export the [service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys), save them to the VM instance's local disk or a file share, and protect them using an NTFS ACL so that only authorized Active Directory users are able to read and use the keys.

**Note:** When using Managed Microsoft AD, the AD domain controllers are deployed in a dedicated tenant project. This project is not shared with the Managed Microsoft AD domains of other customers.

### Use dedicated projects for domain controllers

Domain controllers player a crucial role in the security of an Active Directory domain and a compromise of a single domain controller can result in the compromise of your entire Active Directory forest.

To limit the risk of unauthorized access, use a separate Google Cloud project to deploy domain controllers and grant access to this project on a least-privilege basis. When creating the project, be aware that some permissions might be inherited from [parent folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). To avoid inadvertently granting access through inheritance, consider creating the project outside of your usual [folder hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

When configuring IAM policies for the project, pay particular attention to restricting access to VM instances, the persistent disks that contain the [ntds.dit](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh994565\(v%3Dws.11\)#adds-database-ntdsdit) database, as well as any storage locations that might contain backups.

In addition to using IAM policies to limit access to the project, [protect the project against accidental deletion](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#protectsharedvpc).

### Use separate VMs and projects for managing Active Directory

To manage Active Directory, you need to be able to use tools such as _Active Directory Users and Computers_ or the _Active Directory Administrative Center_. These tools require you to log on using a privileged domain account, which makes the machine you run these tools on an attractive target for credential theft or keylogging.

To minimize the risk of an attacker obtaining privileged domain credentials, use dedicated VM instances for domain administration and handle such management VMs like [privileged access workstations](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/privileged-access-workstations):

  * Use group policies to ensure that only a select subset of users have the right to log on to management VMs. If you implemented tiered administration, this group of users corresponds to Tier 0.

  * Similar to domain controllers, administrative VMs can be put at risk by project members [creating local administrator accounts](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances), logging on via the [serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console), or tampering with their persistent disks. To limit the risk of unauthorized access, use a separate Google Cloud project for administrative VMs and grant access to this project on a least-privilege basis.




If you plan to access administrative VMs from an on-premises network by using [hybrid connectivity](https://docs.cloud.google.com/hybrid-connectivity), then deploy administrative VMs into a dedicated VPC subnet. A subnet dedicated to management VMs allows you to better distinguish between administrative VMs and other VMs when configuring your on-premises firewalls. If you use a [Shared VPC](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#shared-vpc), use [subnet-level permissions](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) to ensure that only privileged administrators are allowed to deploy VM instances into the management subnet. This practice helps ensure that if on-premises firewalls apply different rules for management VMs than for other VMs, users cannot evade firewall rules by placing non-management VMs into the management subnet.

Additionally, consider restricting the group policy that manages logon restrictions for management VMs to the management subnet. This practice enforces alignment between logon restrictions (based on a group policy) and firewall rules (based on subnet/IP address).

In addition to using IAM policies to limit access to the project, [protect the project against accidental deletion](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#protectsharedvpc).

### Use firewall rules to secure domain controllers and servers

Domain controllers expose a number of services, including LDAP, DNS, Kerberos, and RPC. Depending on your use cases, VMs deployed on Google Cloud, as well as machines running on-premises, might need access to different subsets of these services in order to take advantage of Active Directory.

When using Managed Microsoft AD, the AD domain controllers are deployed in a dedicated tenant project. The network that hosts the AD domain controllers is automatically protected with hardened AD-specific firewall rules.

To reduce the attack surface of domain controllers and your VMs, use firewalls to disallow any network communication that is not strictly required. Refer to our guide on [using Active Directory across firewalls](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls) for details on which firewall configurations are necessary to access Active Directory from within your VPC or from on-premises networks.

### Organize Active Directory resources and users into administrative tiers

Some machines in an Active Directory forest are more critical to the overall security of Active Directory than others. [Domain controllers](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#dedicated-dcs) and [administrative VMs](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#separate-vms) are two examples of machines that are particularly critical and therefore particularly sensitive to potential attacks.

To identify the criticality of each of your machines, use a taxonomy of tiers. While the right number of tiers depends on your specific setup, you can start by distringuishing between three tiers:

  * **Tier 0 (Highly critical)** : This tier includes all machines that are critical to the security of your Active Directory forest. Once a single tier 0 machine is compromised, you must assume your entire forest to be compromised.

  * **Tier 1 (Critical)** : This tier includes the majority of servers in your environment, including application servers and database servers. A compromised tier 1 server might have a substantial business impact, but does not pose an immediate threat to the entire forest.

  * **Tier 2 (Normal)** : This tier includes workstations or other general-purpose machines. A compromise of a tier 2 machine is expected to have limited impact on business and overall security.




Although the immediate impact of a compromised tier 2 machine might seem limited, there is a risk of knock-on effects: When a user who has administrative access to tier 0 or tier 1 machines is lured to log on to a compromised tier 2 machine, they might fall victim to a keylogger or other forms of credential theft. The captured credentials might then be used to attack machines of higher tiers, causing the overall impact to escalate.

To avoid such knock-on effects, make sure to not only categorize machines, but also user accounts, and constrain which set of machines these users have access to:

  * **Tier 0 (Highly critical)** : Users that have access to tier 0 machines.

  * **Tier 1 (Critical)** : Users that have access to tier 1 machines.

  * **Tier 2 (Normal)** : Users that have access to tier 2 machines.




Use the following table as a guideline for which users ought to have access to which resources:

Group  |  Tier  |  Domain access  |  Tier 0 computer access  |  Tier 1 computer access  |  Tier 2 computer access   
---|---|---|---|---|---  
Active Directory administrators  |  0  |  Administrator  |  Limited user  |  Blocked  |  Blocked   
Management server administrators  |  0  |  Limited user  |  Administrator  |  Blocked  |  Blocked   
Server administrators  |  1  |  Limited user  |  Blocked  |  Administrator  |  Blocked   
VDI workstation administrators  |  2  |  Limited user  |  Blocked  |  Blocked  |  Administrator   
VDI workstation users  |  2  |  Limited user  |  Blocked  |  Blocked  |  Limited user   
  
Refer to the [Microsoft documentation](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material) for further details and best practices on implementing an administrative tier model in Active Directory.

When you use the administrative tier model in your Active Directory forest, make sure that the integrity of it is not undermined by forest trust relationships. If the trusted forest also applies a tiered administration model, use selective authentication to ensure that users from the trusted forest are only allowed to access resources within the same tier:

![](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-8.svg)

If the trusted forest does not implement tiered administration, map the trusted forest to a certain tier and use selective authentication to ensure that users from the trusted forest are only allowed to access resources of that particular tier.

![](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-9.svg)

### Using VPC Service Controls and Private Google Access for on-premises hosts

Managed Microsoft AD APIs allow resetting the administrator password and performing other sensitive operations. For critical production deployments, we recommend enabling [VPC Service Controls](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-controls) and using [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) for on-premises hosts to increase security.

## Management

The following section details best practices related to management of Active Directory.

### Align Google Cloud and Active Directory resource structures

When you deploy a new Active Directory domain or forest on Google Cloud, you have to define an organizational unit (OU) structure to organize your resources with your Active Directory domain. Rather than designing an entirely new structure or applying the structure you use in your on-premises environment, create an OU structure that is aligned with your [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy):

  * If you use a tiered administration model, the top-level OUs must reflect your administrative tiers.

  * For each tier, create OUs for users and groups. If you are planning to manage a large number of users and groups, create sub-OUs as appropriate.

  * For each tier, create a `Projects` OU and create sub-OUs for each Google Cloud project that contains Active Directory resources. Use the project-specific sub-OU to manage computer accounts, service accounts, or other Active Directory resources that correspond to Google Cloud resources of the respective project. Make sure that there is a 1:1 mapping between OUs and projects.




The following diagram shows an example hierarchy that follows these principles:

![Hierarchy that mirrors your Google Cloud resource hierarchy. Each
          tier contains a collection of sub-OUs for Users, Groups, and
          Projects.](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/best-practices-10.svg)

If the number of projects that contain Active Directory resources is moderate, then you can create a flat OU structure under the `Projects` OU. If you expect to manage a large number of projects and you have designed your Google Cloud resource hierarchy to use multiple levels of folders, then consider reflecting this folder structure underneath the `Projects` OU.

Aligning your Active Directory OU structure and Google Cloud resource hierarchy has several advantages:

  * When you delegate administrative permissions to a Google Cloud project by using IAM policies, then you might also need to grant project users certain privileges in Active Directory. For example, [Compute Engine administrators](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1) might need to be able to join machines to the domain under a certain OU. Aligning OUs and Google Cloud projects enables you to grant such permissions on the same level of granularity in Active Directory as in Google Cloud.

  * If you plan to use group policy objects (GPOs) to manage computers, then an OU structure that reflects the Google Cloud resource hierarchy helps you ensure that GPOs are applied consistently to all VMs of a given project or folder.

  * If you use a cross-forest trust with conditional authentication, then you can use the OUs that correspond to Google Cloud projects to grant the **Allowed to authenticate** permission on a per-project basis.

  * When you delete a project in Google Cloud, you can simply delete the associated OU, reducing the risk of leaving stale resources in your directory.




If you feel your OU structure needs to deviate from your project structure, then this might be an indication that your project structure is too fine-grained or too coarse-grained.

### Use Google time servers

Kerberos authentication relies on time stamps as part of its protocol. For authentication to succeed, the clocks of the client and server machine must synchronize within a certain margin. By default, Active Directory allows no more than [5 minutes](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/maximum-tolerance-for-computer-clock-synchronization) of difference.

In an on-premises Active Directory environment, the following are the default configuration for synchronizing time:

  * Domain-joined machines synchronize their time with a domain controller.
  * Domain controllers synchronize their time with their domain's [PDC emulator](https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/).
  * PDC emulators of all domains synchronize their time with the PDC emulator of the forest root domain.



In this configuration, the PDC emulator of the forest root domain is the ultimate source of time for Active Directory, and it's common to configure this machine to use an external NTP server as time source.

On Compute Engine, the default configuration for Windows VMs is to use the metadata server (`metadata.google.internal`) as NTP server, which in turn [relies on Google's NTP servers](https://docs.cloud.google.com/blog/products/gcp/making-every-leap-second-count-with-our-new-public-ntp-servers?m=1) to obtain the correct time. Joining a VM to an Active Directory domain doesn't change this default configuration.

Keep the Compute Engine's default configuration unless your forest root domain's PDC emulator is deployed outside of Google Cloud.

If your PDC emulator is deployed outside of Google Cloud, [configure it to use `time.google.com` as NTP source](https://developers.google.com/time/guides). Alternatively, you can restore the default Active Directory behavior of synchronizing time with the PDC emulator by reconfiguring Compute Engine VMs to use the [`DOMHIER` NTP source](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings) and configuring firewall rules to permit inbound NTP traffic (UDP/123) to your domain controllers.

### Consolidate and monitor audit logs

When you deploy Active Directory on Google Cloud, the security of your Active Directory forest and your Google Cloud projects are tied to another: Suspicious activity in Active Directory and Windows might endanger the security of some other resources in the same manner as suspicious activity in Google Cloud might put your Active Directory at risk.

Consistent audit logs are an important tool to identify threats or misconfiguration early and enable you to reconstruct and examine past activity. [Cloud Audit Logging](https://docs.cloud.google.com/logging/docs/audit) allows you to capture and analyze [admin activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) and [data access logs](https://docs.cloud.google.com/logging/docs/audit#data-access). Similarly, you can use [firewall rules logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging) and [VPC flow logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) to analyze networking traffic. These platform services are unaware of any security-related events taking place in Active Directory, however. To establish a consistent audit trail that covers both platform-related audit events and Active Directory-related audit events, install the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent) on domain controllers and domain-joined machines to export Windows security event logs to Cloud Logging.

By default, the Windows security event log might not capture all the events you need for your auditing purposes. Refer to the Microsoft recommendations on configuring [audit policies](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations) and [monitoring Active Directory for signs of compromise](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/monitoring-active-directory-for-signs-of-compromise) to ensure you capture all relevant audit events.

When dealing with a large volume of events, it is easy to miss critical events. To avoid missing critical events, create [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) for events that might be [particularly critical or suspicious](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor) and consider [configuring alerts](https://docs.cloud.google.com/monitoring/alerts) to notify you when the rate of events changes or exceeds acceptable thresholds.

## What's next

  * Find out which [pattern for using Active Directory in a hybrid environment](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment) suits your situation best.

  * Learn how you can [configure Active Directory for VMs to automatically join a domain](https://docs.cloud.google.com/solutions/configuring-active-directory-for-vms-to-automatically-join-the-domain).

  * Try out other Google Cloud features for yourself. See our [tutorials](https://docs.cloud.google.com/docs/tutorials).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
