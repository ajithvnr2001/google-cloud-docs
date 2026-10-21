---
url: https://docs.cloud.google.com/architecture/patterns-for-using-active-directory-in-a-hybrid-environment/
title: Patterns for using Active Directory in a hybrid environment \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:21:59.883279+00:00
---

# Patterns for using Active Directory in a hybrid environment  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/patterns-for-using-active-directory-in-a-hybrid-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Patterns for using Active Directory in a hybrid environment Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

This document discusses requirements to consider when you deploy Active Directory to Google Cloud and helps you choose the right architecture.

By federating Active Directory with Cloud Identity or Google Workspace (see [Patterns for authenticating workforce users in a hybrid environment](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#patterns_for_federating_an_external_idp_with_gcp)), you can enable users from your existing Active Directory domains to authenticate and access resources on Google Cloud. You can also deploy Active Directory to Google Cloud if you plan to use Active Directory to manage Windows servers on Google Cloud or if you rely on protocols that are [not supported by Google Cloud](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment#resources_that_cannot_use_google_as_idp).

Before you deploy Active Directory to Google Cloud, you must first decide which domain and forest architecture to use and how to integrate with your existing Active Directory forest.

## Assessing requirements

Active Directory supports a range of domain and forest architectures. In a hybrid environment, one option is to extend a single Active Directory domain across multiple environments. Alternatively, you can use separate domains or forests and connect them using trusts. Which architecture is best depends on your requirements.

To choose the best architecture, look at these factors:

  * Alignment with existing security zones
  * Interaction between on-premises and Google Cloud resources
  * Administrative autonomy
  * Availability



The following sections discuss these factors.

### Alignment with existing security zones

Start by reviewing the design of your on-premises network.

In your on-premises environment, you might have segmented your network into multiple [security zones](https://en.wikipedia.org/wiki/Network_segmentation#Improved_Security)—for example, by using separate VLANs or subnets. In a network that's been segmented into security zones, communication within a security zone is either unrestricted or subject to only lightweight firewall and auditing policies. In contrast, any communication across security zones is subject to strict firewall, auditing, or traffic inspection policies.

The intent of security zones is more far-reaching than just constraining and auditing network communication, however—security zones should implement trust boundaries.

#### Trust boundaries

Each machine in a network runs several processes. These processes might communicate with one another locally by using interprocess communication, and they might communicate across machines by using protocols such as HTTP. In this web of communication, peers don't always trust each other to the same extent. For example, processes might trust processes that are running on the same machine more than processes that are running on other machines. And some machines might be considered more trustworthy than others.

A trust boundary enforces discriminating between communication parties—trusting one set of communication parties more than another set of parties.

Trust boundaries are critical for containing the impact of an attack. Attacks rarely end once a single system has been compromised—whether that system is a single process or an entire machine. Instead, an attacker is likely to try to extend the attack to other systems. Because systems in a trust boundary don't discriminate between each other, spreading an attack inside that trust boundary is easier than attacking systems across a trust boundary.

Once a system in a trust boundary has been compromised, all other systems in that trust boundary must be assumed to be compromised. This assumption can help you identify trust boundaries or validate whether a certain system boundary is a trust boundary, for example:

_Suppose an attacker has achieved the highest level of access to target A (for example, Administrator or root access to a machine or application). If they can leverage these privileges to gain the same level of access to target B, then A and B are, by definition, within the same trust boundary. Otherwise, a trust boundary lies between A and B._

By constraining network communication, security zones can help implement trust boundaries. For a security zone to become a true trust boundary, however, the workloads across each side of the boundary must discriminate between requests that originate from the same security zone and requests that originate from different security zones—and scrutinize the latter more closely.

#### Zero-trust model

The zero-trust model is the preferred networking model on Google Cloud.

Given a single compromised system in a trust boundary, you can assume that all systems in that boundary are compromised. This assumption suggests that smaller trust boundaries are better. The smaller the trust boundary, the fewer systems are compromised and the more boundaries an attacker must clear for an attack to spread.

The zero-trust model takes this idea to its logical conclusion: Each machine in the network is treated as a unique security zone and trust boundary. All communication between machines is subject to the same scrutiny and firewalling, and all network requests are treated as originating from an untrusted source.

On the networking level, you can implement a zero-trust model by using [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) to restrict traffic and [VPC flow logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) and [firewall rules logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging) to analyze traffic. At the application level, you must ensure that all applications consistently and securely handle authentication, authorization, and auditing.

#### Trust boundaries in Active Directory

In an Active Directory domain, machines trust domain controllers to handle authentication and authorization on their behalf. Once a user has proven their identity to one of the domain controllers, they can log on by default to all machines of the same domain. Any access rights that the user is granted by the domain controller (in the form of privileges and group memberships) apply to many machines of the domain.

By using group policies, you can prevent users from accessing certain machines or constrain their rights on certain machines. Once a machine has been compromised, however, an attacker might be able to [steal passwords, password hashes, or Kerberos tokens](https://www.microsoft.com/en-us/download/details.aspx?id=36036) of other domain users signed on to the same machine. The attacker can then leverage these credentials to spread the attack to other domains in the forest.

Given these factors, it's best to assume that all machines in a forest are in a trust security boundary.

Compared to domain boundaries, whose purpose is to control [replication and granting administrative autonomy](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759073\(v=ws.10\)#the-physical-structure-of-active-directory) to different parts of the organization, forest boundaries can provide [stronger isolation](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc773178\(v%3dws.10\)). Forests can [serve as a trust boundary](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321\(v=ws.10\)).

#### Aligning Active Directory forests and security zones

Assuming the forest as the trust boundary influences the design of security zones. If a forest extends across two security zones, it's easier for an attacker to clear the boundary between these security zones. As a result, the two security zones effectively become one and form a single trust boundary.

In a zero-trust model, each machine in a network can be thought of as a separate security zone. Deploying Active Directory in such a network undermines this concept and widens the effective security boundary to include all machines of the Active Directory forest.

For a security zone to serve as a trust boundary, you must ensure that the entire Active Directory forest is in the security zone.

#### Impact on extending Active Directory to Google Cloud

When you plan a deployment to Google Cloud that requires Active Directory, you must decide between two options to align the deployment with your existing security zones:

  * **Extend an existing security zone to Google Cloud**. You can extend one or more of your existing security zones to Google Cloud by provisioning Shared VPC on Google Cloud and connecting it to the existing zone by using Cloud VPN or Cloud Interconnect.

Resources deployed on-premises and on Google Cloud that share a common zone can also share a common Active Directory forest, so there's no need to deploy a separate forest to Google Cloud.

As an example, consider an existing network that has a development [perimeter network](https://en.wikipedia.org/wiki/DMZ_\(computing\)) and production perimeter network as security zones with a separate Active Directory forest in each security zone. If you extend the security zones to Google Cloud, then all deployments on Google Cloud are also part of one of these two security zones, and can use the same Active Directory forests.

![Extending a security zone to Google Cloud](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-1-extend-security-zone.svg)

  * **Introduce new security zones**. Extending a security zone might not be applicable—either because you don't want to further expand a zone, or because the security requirements of your existing security zones don't match the requirements of your Google Cloud deployments. You can treat Google Cloud as additional security zones.

As an example, consider an on-premises environment that has a perimeter network, but doesn't distinguish between development and production workloads. To separate these workloads on Google Cloud, you can create two Shared VPCs and consider them new security zones. You then deploy two additional Active Directory forests to Google Cloud, one per security zone. If necessary, you can establish trust relationships between forests to enable authentication across security zones.

![Separating workloads on Google Cloud by creating two Shared VPCs as new security zones.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-2-new-security-zone.svg)




### Interaction between on-premises and Google Cloud resources

The second factor to consider when you extend your Active Directory to Google Cloud is the interaction of users and resources between on-premises and Google Cloud. Depending on your use case, this interaction might be anywhere from light to heavy.

#### Light interaction

If the sole purpose of using Active Directory on Google Cloud is to manage a fleet of Windows servers and to enable administrators to sign in to these servers, the level of interaction between environments is light:

  * The set of employees interacting with resources on Google Cloud is limited to administrative staff.
  * Applications deployed to Google Cloud might not interact with on-premises applications at all or might do so without relying on Windows authentication facilities such as Kerberos and NTLM.



In a light scenario, consider integrating your on-premises and Google Cloud environments in one of the following two ways:

  * **Two disjoint Active Directory forests** : You can isolate the two environments by using two separate Active Directory forests that don't share a trust relationship. To enable administrators to authenticate, you maintain a separate set of user accounts for them in the Google Cloud forest.

Maintaining a duplicate set of user accounts increases administrative effort and introduces the risk of forgetting to disable accounts when employees leave the company. A better approach is to provision these accounts automatically.

If user accounts in your on-premises Active Directory are provisioned by a Human Resources Information System (HRIS), you might be able to use a similar mechanism to provision and manage user accounts in the Google Cloud forest. Alternatively, you can use tools such as Microsoft Identity Manager to synchronize user accounts between environments.

  * **Two Active Directory forests with cross-forest trust** : By using two Active Directory forests and connecting them with a cross-forest trust, you can avoid having to maintain duplicate accounts. Administrators use the same user account to authenticate to both environments. Although the level of isolation between environments can be considered weaker, using separate forests lets you maintain a trust boundary between your on-premises and Google Cloud environment.




#### Moderate interaction

Your use case might be more complex. For example:

  * Administrators logging in to Windows servers deployed on Google Cloud might need to access file shares hosted on-premises.
  * Applications might use Kerberos or NTLM to authenticate and communicate across environment boundaries.
  * You might want to enable employees to use [Integrated Windows Authentication (IWA)](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/authentication/windowsauthentication/) to authenticate to web applications deployed on Google Cloud.



In a moderate scenario, operating two disjoint Active Directory forests might be too limiting: You cannot use Kerberos to authenticate across the two forests, and using NTLM [pass-through authentication](https://support.microsoft.com/en-us/help/102716/ntlm-user-authentication-in-windows) requires that you keep user accounts and passwords in sync.

In this case, we recommend using two Active Directory forests with a cross-forest trust.

#### Heavy interaction

Certain workloads, including Virtual Desktop Infrastructure (VDI) deployments, might require heavy interaction between on-premises resources and resources deployed on Google Cloud. When resources across environments are closely coupled, trying to maintain a trust boundary between environments might not be practical and using two forests with a cross-forest trust can be too limiting.

In this case, we recommend using a single Active Directory forest and sharing it across environments.

### Administrative autonomy

The third factor to consider when you extend your Active Directory to Google Cloud is administrative autonomy.

If you plan to [distribute workloads across on-premises and Google Cloud](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-architecture-patterns#distributed_deployment_patterns), the workloads you are going to run on Google Cloud might be very different than the workloads you keep on-premises. You might even decide that different teams should manage the two environments.

Separating responsibilities among different teams requires granting each team some administrative autonomy. In Active Directory, you can grant teams the authority to manage resources by using [delegated administration](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/delegating-administration-by-using-ou-objects) or by using separate domains.

Delegated administration is a lightweight way to delegate administrative duties and grant some autonomy to teams. Maintaining a single domain might also help you ensure consistency across environments and teams.

You can't delegate all administrative capabilities, however, and sharing a single domain might increase the administrative overhead of coordinating between teams. In such a case, we recommend using separate domains.

### Availability

The final factor to consider when you extend your Active Directory to Google Cloud is availability. For each domain in an Active Directory forest, the domain controller serves as the identity provider for users in that domain.

When using Kerberos for authentication, a user needs to interact with an Active Directory domain controller at various points:

  * Initial authentication (obtaining a ticket-granting ticket).
  * Periodic reauthentication (refreshing a ticket-granting ticket).
  * Authenticating with a resource (obtaining a service ticket).



Performing the initial authentication and periodic reauthentication requires communicating with a single domain controller only—a domain controller of the domain that the user is a member of.

When authenticating with a resource, it might be necessary to interact with multiple domain controllers, depending on the domain the resource is in:

  * If the resource is located in the same domain as the user, the user can use the same domain controller (or a different domain controller of the same domain) to complete the authentication process.
  * If the resource is located in a different domain, but there is a direct trust relationship with the user's domain, the user needs to interact with at least two domain controllers: One in the resource domain and one in the user's domain.
  * If the resource and user are part of different domains and there is only an indirect trust relationship between these domains, then a successful authentication requires [communicating with domain controllers of every domain in the trust path](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc773178%28v%3dws.10%29#trust-processes-and-interactions).



Locating users and resources in different Active Directory domains or forests can constrain overall availability. Because authenticating requires interacting with multiple domains, an outage of one domain can impact the availability of resources in other domains.

Considering the potential impact of Active Directory topology on [availability](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment#availability), we recommend aligning your Active Directory topology with your hybrid strategy.

#### Distributed workloads

To capitalize on the unique capabilities of each computing environment, you might use a hybrid approach to [distribute workloads across those environments](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-architecture-patterns#distributed_deployment_patterns). In such a setup, the workloads you deploy to Google Cloud are likely to depend on other infrastructure or applications running on-premises, which makes highly available [hybrid connectivity](https://cloud.google.com/hybrid-connectivity/) a critical requirement.

If you deploy a separate Active Directory forest or domain to Google Cloud and use a trust to connect it to your on-premises Active Directory, you add another dependency between Google Cloud and your on-premises environment. This dependency has a minimal effect on availability.

#### Redundant workloads

If you use Google Cloud to ensure business continuity, your workloads on Google Cloud mirror some of the workloads in your on-premises environment. This setup enables one environment to take over the role of the other environment if a failure occurs. So you need to look at every dependency between these environments.

If you deploy a separate Active Directory forest or domain to Google Cloud and use a trust to connect it to your on-premises Active Directory, you might create a dependency that undermines the purpose of the setup. If the on-premises Active Directory becomes unavailable, all workloads deployed on Google Cloud that rely on cross-domain or cross-forest authentication might also become unavailable.

If your goal is to ensure business continuity, you can use separate Active Directory forests in each environment that are not connected to one another. Or you can extend an existing Active Directory domain to Google Cloud. By deploying additional domain controllers to Google Cloud and replicating directory content between environments, you ensure that the environments operate in isolation.

## Integration patterns

After you've assessed your requirements, use the following decision tree to help identify a suitable forest and domain architecture.

![Decision tree to help you choose a forest and domain architecture](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-3-decision-tree.svg)

The following sections describe each pattern.

### Synchronized forests

In the _synchronized forests_ pattern, you deploy a separate Active Directory forest to Google Cloud. You use this forest to manage any resources deployed on Google Cloud as well as the user accounts required to manage these resources.

Instead of creating a trust between the new forest and an existing, on-premises forest, you synchronize accounts. If you use an HRIS as the leading system to manage user accounts, you can configure the HRIS to provision user accounts in the Google Cloud-hosted Active Directory forest. Or you can use tools such as Microsoft Identity Manager to synchronize user accounts between environments.

![Deploying a separate Active Directory forest to Google Cloud](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-4-synchronized-forests.svg)

**Consider using the synchronized forests pattern if one or more of the following applies** :

  * Your intended use of Google Cloud fits one of the [redundant deployment patterns](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-architecture-patterns#redundant_deployment_patterns), and you want to avoid runtime dependencies between your on-premises environment and Google Cloud.
  * You want to maintain a trust boundary between your on-premises Active Directory environment and the Google Cloud-hosted Active Directory environment—either as a [defense-in-depth](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\)) measure or because you trust one environment more than the other.
  * You expect light to no interaction between Active Directory–managed resources on-premises and on Google Cloud.
  * The number of user accounts you need in the Google Cloud-hosted Active Directory environment is small.



**Advantages** :

  * The synchronized forests pattern lets you maintain strong isolation between the two Active Directory environments. An attacker who compromises one environment might gain little advantage in attacking the second environment.
  * You don't need to set up hybrid connectivity between your on-premises and Google Cloud networks to operate Active Directory.
  * The Google Cloud-hosted Active Directory is unaffected by an outage of your on-premises Active Directory. The pattern is well-suited for business-continuity use cases or other scenarios requiring high availability.
  * You can grant a high level of administrative autonomy to teams that manage the Google Cloud-hosted Active Directory forest.
  * This pattern is supported by [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview).



**Best practices:**

  * Don't synchronize user account passwords between the two Active Directory forests. Doing so undermines the isolation between the environments.
  * Don't rely on [pass-through authentication](https://support.microsoft.com/en-us/help/102716/ntlm-user-authentication-in-windows), because it requires synchronizing user account passwords.
  * Make sure that when an employee leaves the company, their accounts in both Active Directory environments are disabled or removed.



### Resource forest

In the _resource forest_ pattern, you deploy a separate Active Directory forest to Google Cloud. You use this forest to manage any resources deployed to Google Cloud as well as a minimal set of administrative user accounts required for managing the forest. By establishing a forest trust to your existing, on-premises Active Directory forest, you enable users from your existing forest to authenticate and access resources managed by the Google Cloud-hosted Active Directory forest.

If necessary, you can evolve this pattern into a hub and spoke topology with your existing Active Directory forest at the center, connected to many resource forests.

![A forest trust to your on-premises Active Directory forest, enabling users
from your existing forest to authenticate and access resources managed by the
Google Cloud-hosted Active Directory forest](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-5-resource-forest.svg)

**Consider using the resource forest pattern if one or more of the following applies** :

  * Your intended use of Google Cloud fits one of the [distributed deployment patterns](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-architecture-patterns#distributed_deployment_patterns), and a dependency between your on-premises environment and Google Cloud is acceptable.
  * You want to maintain a trust boundary between your on-premises Active Directory environment and the Google Cloud-hosted Active Directory environment—either as a defense-in-depth measure or because you consider one environment more trusted than the other.
  * You expect a moderate level of interaction between Active Directory–managed resources on-premises and on Google Cloud.
  * You have a large number of users who need to access resources deployed on Google Cloud—for example, to web applications that use IWA for authentication.



**Advantages** :

  * The resource forest pattern lets you maintain a trust boundary between the two Active Directory environments. Depending on how the trust relationship is configured, an attacker who compromises one environment might gain little to no access to the other environment.
  * This pattern is fully supported by [Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview).
  * You can grant a high level of administrative autonomy to teams that manage the Google Cloud-hosted Active Directory forest.



**Best practices:**

  * Connect the two Active Directory forests using a one-way trust so that the Google Cloud-hosted Active Directory trusts your existing Active Directory, but not the other way around.
  * Use [selective authentication](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/dd560679\(v=ws.10\)#selective-authentication) to limit the resources in the Google Cloud-hosted Active Directory that users from the on-premises Active Directory are allowed to access.
  * Use redundant [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability), [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability), or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies#redundancy-options) connections to ensure highly available network connectivity between your on-premises network and Google Cloud.



### Extended domain

In the _extended domain_ pattern, you extend one or more of your existing Active Directory domains to Google Cloud. For each domain, you deploy one or more domain controllers on Google Cloud, which causes all domain data as well as the global catalog to be replicated and made available on Google Cloud. By using separate [Active Directory sites](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts#BKMK_5) for your on-premises and Google Cloud subnets, you ensure that clients communicate with domain controllers that are closest to them.

![Extending one or more of your existing Active Directory domains to Google Cloud](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-6-extended-domain.svg)

**Consider using the extended domain pattern if one or more of the following applies** :

  * Your intended use of Google Cloud fits one of the redundant deployment patterns, and you want to avoid runtime dependencies between your on-premises environment and Google Cloud.
  * You expect heavy interaction between Active Directory—managed resources on-premises and on Google Cloud.
  * You want to speed up authentication for applications that rely on [LDAP for authentication](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment#ldap).



**Advantages** :

  * The Google Cloud-hosted Active Directory is unaffected by an outage of your on-premises Active Directory. The pattern is well-suited for business-continuity use cases or other scenarios that require high availability.
  * You can limit the communication between your on-premises network and Google Cloud. This can potentially save bandwidth and improve latency.
  * All content of the global catalog is replicated to Active Directory and can be efficiently accessed from Google Cloud-hosted resources.



**Best practices:**

  * If you replicate all domains, the communication between your on-premises network and Google Cloud network are limited to Active Directory replication between domain controllers. If you replicate only a subset of your forest's domains, domain-joined servers running on Google Cloud might still need to communicate with domain controllers of non-replicated domains. Make sure that the firewall rules that apply to communication between on-premises and Google Cloud consider all relevant cases.
  * Be aware that replicating across sites happens at [certain intervals](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/determining-the-interval) only, so updates performed on an on-premises domain controller surface to Google Cloud only after a delay (and vice versa).
  * Consider using [read-only domain controllers](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement) (RODCs) to maintain a read-only copy of domain data on Google Cloud, but be aware that there's a trade-off related to caching of user passwords. If you allow RODCs to cache passwords and prepopulate the password cache, resources deployed on Google Cloud can remain unaffected by an outage of on-premises domain controllers. However, the security benefits of using an RODC over a regular domain controller are limited. If you disable password caching, a compromised RODC might only pose a limited risk to the rest of your Active Directory, but you lose the benefit of Google Cloud remaining unaffected by an outage of on-premises domain controllers.



### Extended forest

In the _extended forest_ pattern, you deploy a new Active Directory domain on Google Cloud, but integrate it into your existing forest. You use the new domain to manage any resources deployed on Google Cloud and to maintain a minimal set of administrative user accounts for managing the domain.

By extending the implicit trust relationships to other domains of the forest, you enable your existing users from other domains to authenticate and access resources managed by the Google Cloud-hosted Active Directory domain.

![Deploying a new Active Directory domain on Google Cloud, but integrating it into your existing forest](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-7-extended-forest.svg)

**Consider using the extended forest pattern if one or more of the following applies** :

  * Your intended use of Google Cloud fits one of the distributed deployment patterns, and a dependency between your on-premises environment and Google Cloud is acceptable.
  * The resources you plan to deploy to Google Cloud require a different domain configuration or structure than your existing domains provide, or you want to grant a high level of administrative autonomy to teams who administer the Google Cloud-hosted domain.
  * You expect moderate to heavy interaction between Active Directory–managed resources on-premises and on Google Cloud.
  * You have many users who need to access resources deployed to Google Cloud—for example, to web applications that use IWA for authentication.



**Advantages** :

  * All content of the global catalog will be replicated to Active Directory and can be efficiently accessed from Google Cloud-hosted resources.
  * Replication traffic between your on-premises network and Google Cloud is limited to global catalog replication. This might help limit your overall bandwidth consumption.
  * You can grant a high level of administrative autonomy to teams that manage the Google Cloud-hosted Active Directory domain.



**Best practices** :

  * Use redundant Dedicated Interconnect, Partner Interconnect, or Cloud VPN connections to ensure highly available network connectivity between your on-premises network and Google Cloud.



### Resource forest with extended domain

The _resource forest with extended domain_ pattern is an extension of the resource forest pattern. The resource forest pattern lets you maintain a trust boundary between environments and providing administrative autonomy. A limitation of the resource forest is that its overall availability hinges on the availability of on-premises domain controllers and reliable network connectivity to your on-premises data center.

You can overcome these limitations by combining the resource forest pattern with the extended domain pattern. By replicating the domain, your user accounts are located in Google Cloud, and you can ensure that users can authenticate to Google Cloud-hosted resources even when on-premises domain controllers are unavailable or network connectivity is lost.

![Combining the resource forest and extended domain patterns](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-8-resource-forest-extended-domain.svg)

**Consider using the resource forest with extended domain pattern if one or more of the following applies** :

  * You want to maintain a trust boundary between your main Active Directory forest and the resource forest.
  * You want to prevent an outage of on-premises domain controllers or loss of network connectivity to your on-premises environment from affecting your Google Cloud-hosted workloads.
  * You expect moderate interaction between Active Directory–managed resources on-premises and on Google Cloud.
  * You have many users from a single Active Directory domain who need to access resources deployed on Google Cloud—for example, to web applications that use IWA for authentication.



**Advantages** :

  * Google Cloud-hosted resources are unaffected by an outage of your on-premises Active Directory. The pattern is well-suited for business-continuity use cases or other scenarios that require high availability.
  * The pattern lets you maintain a trust boundary between the two Active Directory forests. Depending on how the trust relationship is configured, an attacker who compromises one environment might gain little to no access to the other environment.
  * Communication between your on-premises network and Google Cloud network is limited to Active Directory replication between domain controllers. You can implement firewall rules to disallow all other communication, strengthening the isolation between environments
  * You can grant a high level of administrative autonomy to teams that manage the Google Cloud-hosted Active Directory forest.
  * You can use [Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview) for the resource forest.



**Best practices:**

  * Deploy domain controllers for the extended domain into a separate Google Cloud project and [VPC](https://docs.cloud.google.com/vpc) in order to separate these components from the components of the resource forest.
  * Use [VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to connect the VPC to Shared VPC or to the VPC used by the resource forest and [configure firewalls](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls) to restrict communication to Kerberos user authentication and forest trust creation.
  * Connect the two Active Directory forests using a one-way trust so that the Google Cloud-hosted Active Directory trusts your existing Active Directory forest, but not the other way around.
  * Use selective authentication to limit the resources in the resource forest that users from other forests are allowed to access.
  * Be aware that replicating across sites happens at certain intervals only, so updates performed on an on-premises domain controller surface to Google Cloud only after a delay (and vice versa).
  * Consider using RODCs for the extended domain, but be sure to allow caching of passwords to preserve the availability advantages compared to the resource forest pattern.



## What's next

  * Find out more about [Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview).
  * Review best practices for deploying an Active Directory resource forest on Google Cloud.
  * Learn how to [deploy a fault-tolerant Active Directory environment to Google Cloud](https://docs.cloud.google.com/architecture/deploy-fault-tolerant-active-directory-environment).
  * Review our [best practices on VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
