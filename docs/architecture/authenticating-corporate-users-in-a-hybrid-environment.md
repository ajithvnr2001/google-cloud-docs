---
url: https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment/
title: Authenticate workforce users in a hybrid environment \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:26.785000+00:00
---

# Authenticate workforce users in a hybrid environment  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Authenticate workforce users in a hybrid environment Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

This document is the first part of a multi-part series that discusses how to extend your identity management solution to Google Cloud to enable your workforce to authenticate and consume services in a hybrid computing environment.

The series consists of these parts:

  * Authenticating workforce users in a hybrid environment (this document)
  * [Patterns for authenticating workforce users in a hybrid environment](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment)



## Introduction

Managing user accounts and controlling employee access to applications and computing resources is a key responsibility of enterprise IT departments. To ensure consistency and administrative efficiency, most enterprises consider identity management a central function and use a unified system to manage identities. Most commonly, enterprises rely on Microsoft Active Directory Domain Services (AD DS) for this purpose.

When you extend an IT landscape to Google Cloud as part of a hybrid strategy, you want to maintain a single point where identities are managed. A unified identity management system minimizes administrative effort in managing accounts and access control. This system also helps ensure that users and applications can authenticate securely across a hybrid environment.

This document looks at the ways to integrate Google Cloud with your identity management system. The document helps you choose the approach that best fits your requirements.

Although most of the discussion also applies to [Google Workspace](https://gsuite.google.com/), the document focuses solely on [Cloud Identity](https://docs.cloud.google.com/identity).

## Assess requirements for hybrid identity management

The best way to extend your identity management system to Google Cloud depends on multiple factors:

  * The pools of identities in your organization
  * The identity providers used to provide authentication services for your workforce identities
  * The resources and applications you want your users to be able to access on Google Cloud
  * Your business continuity requirements



The following sections look at each of these factors.

## Identities

The first factor to look at when integrating Google Cloud and your identity management system is how you manage and distinguish between identity types. Most organizations use the following types of identities:

  1. **Workforce identities** are the identities you manage for employees of your organization. These identities are used for signing in to workstations, accessing email, or using corporate applications.
  2. **External identities** are the identities you manage for non-employees such as contractors or partners which need to be given access to corporate resources.
  3. **Guest identities** are identities managed by a different party such as a customer or partner who need access to corporate resources.
  4. **Customer identities** are the identities you manage for users in order to interact with your website or customer-facing applications.
  5. **Workload identities** are the identities you manage to enable applications to interact with other applications or the underlying platform.



Often, workforce identities form a single pool of identities, where each employee has a single identity and all identities managed in the same way, using the same systems. However, this doesn't have to be the case—as a result of a merger or acquisition, for example, you might have multiple pools of workforce identities, each managed differently using different systems. Technically, this means that you might have to integrate multiple LDAP sources, Active Directory forests, or Entra ID tenants with Google Cloud.

Integrating multiple pools adds to the complexity of integrating with Google Cloud. Therefore, you should evaluate:

  * Do all identity pools need access to Google Cloud, or only a select subset?
  * Should all identity pools have access to the same [organization in Google Cloud](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization), or each to a different one?
  * Are there options to reduce the number of pools, for example, by creating cross-forest trusts between Active Directory forests?



External identities are often treated similarly to workforce identities, with these exceptions:

  * Their account might be valid for only a limited time.
  * They might be granted fewer rights by default.
  * They might be managed by a separate LDAP directory, Active Directory forest, or Microsoft Entra ID.



Unlike external identities, guest identities are not managed by you but by a different party. In SaaS applications such as [Google Workspace](https://gsuite.google.com/), guest identities can remove the need for maintaining external identities for customers or partners. You rarely encounter guest identities in on-premises environments.

This document focuses on workforce identities and external identities.

If you have used services such as Google Ads, some of your employees might already have a Google Account that isn't connected to their workforce identity, meaning they have two identities. If so, consider [consolidating these identities](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts).

## Identity providers

The second factor to look at is your identity providers. An _identity provider_ (IdP) is a system that provides authentication services for your workloads and ultimately decides whether to authenticate a user.

In addition to providing authentication services, IdPs often manage the lifecycle of identities. This doesn't have to be the case, though, because identities might also be provisioned from a separate human resources system.

Common identity providers include:

  * Active Directory (AD DS)
  * Microsoft Entra ID (formerly Azure Active Directory)
  * IDaaS providers such as ForgeRock, Okta, or Ping Identity
  * Other LDAP directories, including Active Directory Lightweight Directory Services (AD LDS)



Instead of using only one system, you might be using several systems—to manage different user pools, to handle external accounts, or to provide different authentication services for the same user pools. Examples where multiple IdPs are used to manage the same pools include:

  * Active Directory federated with Entra ID
  * Active Directory federated with an IDaaS provider such as ForgeRock, Okta, or Ping Identity
  * Active Directory with AD LDS replicas



To use your IdP on Google Cloud, you can follow two basic approaches:

  * **Federate your identity provider with Cloud Identity** : By federating with [Cloud Identity](https://docs.cloud.google.com/identity), you enable Google to become an additional IdP that your workforce users can use and that applications deployed on Google Cloud can rely on. Instead of maintaining Google identities for each of your users, you can depend on the federation relationship to maintain identities automatically. This relationship also helps ensure that your IdP remains the source of truth.
  * **Extend your identity provider to Google Cloud** : You can allow applications deployed on Google Cloud to reuse your IdP—by connecting to it directly or by maintaining a replica of your IdP on Google Cloud.



Depending on the other identity management factors, you might need to combine both approaches to support your hybrid usage scenarios.

## Resources

The third factor to look at is which Google Cloud resources you plan to grant your workforce users access to. This factor includes Google Cloud itself—you must allow responsible teams to manage Google Cloud by using the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or APIs.

Additional resources might include:

  * Applications deployed on [App Engine](https://docs.cloud.google.com/appengine), [Compute Engine](https://docs.cloud.google.com/compute), or [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine)
  * Applications protected with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap)
  * Linux VMs, accessed using SSH
  * Windows VMs, accessed using RDP
  * Other Google tools and services such as [Google Workspace](https://gsuite.google.com/), [Data Studio](https://lookerstudio.google.com/), or [Google Ads](https://ads.google.com/home/)



These resources differ in whether they **must** , **could** , or **cannot** use Google as identity provider. The following sections look at these three cases.

### Resources that must use Google as IdP

Resources that must use Google as IdP include the Google Cloud console, the gcloud CLI, applications protected with IAP, and other Google tools and services. To grant your workforce users access to these resources, you must provision a Google identity for each user.

Maintaining separate Google identities runs counter to the idea of unified identity management. So granting users access to any of these resources implies that you must [federate your IdP with Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#patterns_for_federating_an_external_idp_with_gcp).

After you federate your IdP with Google Cloud, consider using Google as IdP for more resources—including applications that might use other means to authenticate users.

### Resources that could use Google as IdP

Resources that could use Google as IdP, but currently don't, include:

  * New applications, aimed at workforce users, that you plan to deploy on Google Cloud.
  * Existing applications, aimed at workforce users, that you plan to [lift and shift](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/adopt#mix_and_match_migration_approaches) or [move and improve](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/adopt#mix_and_match_migration_approaches) to Google Cloud.



Whether these applications can use Google as IdP depends on the protocols you use for authentication and authorization.

#### Web single sign-on protocols

Google supports several industry standard protocols for handling authentication, authorization, and single sign-on. Supported protocols include:

  * [OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), which applies to mobile clients, fat clients, and other non-browser applications.
  * [OpenID Connect 1.0](https://developers.google.com/identity/protocols/OpenIDConnect) (OIDC), which applies to browser-based applications.
  * [SAML 2.0](https://docs.cloud.google.com/identity/solutions/enable-sso), which applies to integrating third-party applications.



For applications that you plan to develop, OAuth 2.0 or OIDC should be your preferred choice. These protocols are widely adopted, and you can take advantage of many well-tested libraries and tools. Also, relying on these protocols implies that you can optionally use Google as IdP while you retain the flexibility of switching identity providers as needed.

If you have applications that use SAML, OAuth 2.0, or OIDC, switching them to using Google as identity provider should be possible with little or no code changes.

#### LDAP

One of the most versatile and relied-on protocols for authentication and authorization is the Lightweight Directory Access Protocol (LDAP). There are multiple ways an application can use LDAP for authentication and authorization. The two most common scenarios are:

  1. **Using LDAP for authentication and querying user information** : In this scenario, an application doesn't use single sign-on. Instead, it shows the user a sign-on form asking for username and password and then uses the provided credentials to attempt an LDAP `bind` operation. If the attempt succeeds, the credentials are considered valid. And further information about the user such as name and group membership might be queried from the directory and used to authorize access.

  2. **Using SAML for authentication and LDAP for querying user information** : In this scenario, the application authenticates the user by using a single sign-on protocol—applications often use SAML for this purpose. After the user has been authenticated, the application uses the LDAP server to query additional information about the user such as name and group memberships.




The critical difference between the two scenarios is that the first scenario requires both the application and the LDAP server to have access to the user's password in order to verify credentials. In the second scenario, the application and the server don't require access to the user's password; the application can perform its LDAP queries by using a dedicated service user.

With [Secure LDAP](https://support.google.com/a/answer/9048516), you can access user and group information in Cloud Identity by using the LDAP protocol. If Google is your primary IdP, Secure LDAP lets you support both scenarios. However, if you integrate Cloud Identity with an external IdP, Cloud Identity doesn't maintain a copy of user passwords. As a result, only the second scenario can be enabled with Secure LDAP.

#### Kerberos and NTLM

If you plan to migrate Windows-based workloads to Google Cloud, some of these applications might rely on [Integrated Windows Authentication (IWA)](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/authentication/windowsauthentication/) instead of using standard protocols. IWA is a common choice for ASP.NET-based applications running on Microsoft IIS. IWA is popular because it allows a seamless single sign-on experience for users who have logged in to their Windows workstation using domain credentials.

IWA relies on [NTLM](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-ntlm) or [Kerberos](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-kerberos). It requires the user's workstation and the server the application is running on to be joined to the same Active Directory domain or to trusting domains.

One consequence of relying on NTLM and Kerberos is that an application using IWA cannot use Google as IdP. However, you might still be able to refactor the application to use OIDC. OIDC doesn't require the user's workstation or the server to be domain-joined. So refactoring might [simplify deployment](https://docs.cloud.google.com/dotnet/docs/deploy-dotnet-applications#security) and help you [pursue alternative deployment options](https://docs.cloud.google.com/dotnet/docs/deploy-dotnet-applications#deployment_options).

Considering the seamless single sign-on experience provided by IWA, using OIDC instead of IWA might seem like a step backward in terms of user experience. However, this doesn't have to be the case if you ensure that users can seamlessly sign on to AD FS or Azure AD:

  * If you [federate Google Cloud with Active Directory and AD FS](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#federating_active_directory_with_cloud_identity_by_using_gcds_and_ad_fs), any authentication methods configured in AD FS apply. If you configure AD FS to allow IWA, users who have logged in to their Windows workstation using domain credentials can be authenticated seamlessly to any application that uses Google as IdP.
  * If you [federate Google Cloud with Entra ID](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#federating_azure_ad_with_cloud_identity), you can enable Azure AD Seamless SSO to the same effect.



The following diagram shows a simplified example of how you can use Cloud Identity, AD FS, and IWA to implement seamless single-sign on for a web application:

![How to use Cloud Identity, AD FS, and IWA to implement seamless single-sign on for a web application](https://docs.cloud.google.com/static/architecture/images/authenticating-corporate-users-sso-app.svg)

  1. The browser requests a protected page using a web browser.
  2. The web application initiates a login using OIDC ([OIDC authentication flow](https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser)). This flow redirects the browser to the Google sign-in endpoint.
  3. The Google sign-in endpoint returns the Google sign-in page to the user, prompting for the email address.
  4. The user enters their email address.
  5. Based on the email address, the Google sign-in endpoint identifies the Cloud Identity account and recognizes that it is configured to use SSO. The sign-in endpoint then initiates a SAML login with AD FS.
  6. AD FS, configured to use IWA, requests the browser to present a Kerberos ticket, which triggers the browser to request the underlying Windows operating system to obtain a suitable ticket.
  7. Unless a suitable ticket has been cached, Windows contacts the Active Directory key distribution center (KDC) and requests a suitable service ticket to be issued based on the ticket granting ticket (TGT) that was obtained when the user signed in to Windows.
  8. The browser presents the newly obtained ticket to AD FS.
  9. AD FS validates the ticket by checking its cryptographic signature, extracts the user identity from the ticket, and issues a SAML token to Google sign-in endpoint.
  10. Using the authentication information from the SAML token, Google sign-in endpoint completes the OIDC login and issues OpenID Connect tokens to the web application.
  11. When the user is authenticated, the protected page can be returned to the user.



#### SSH public-key authentication

When you plan to run Linux virtual machines (VMs) on Google Cloud, you likely need SSH access to these machines. The most common authentication method for SSH is public-key authentication.

Unlike the single sign-on protocols previously discussed, SSH public-key authentication doesn't rely on a centralized IdP to make authentication decisions. Instead, authentication decisions are decentralized—each machine handles authentication based on a local set of authorized public keys.

You can bridge the gap between decentralized SSH public-key authentication and centralized identity management by using [OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin). OS Login ties the lifecycle of SSH keys to the lifecycle of user accounts by:

  * Publishing an SSH public key when a user is created or is attempting to use SSH for the first time.
  * Provisioning the user's public key to machines a user is entitled to access.
  * Deprovisioning the user's public key when the account is revoked access, disabled, or deleted.



Using OS Login effectively makes Cloud Identity the IdP for your Linux instances.

### Resources that cannot use Google as IdP

Some resources cannot directly use Google as IdP. But you can still accommodate these resources on Google Cloud by combining two approaches:

  * [Federate your external IdP with Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#patterns_for_federating_an_external_idp_with_gcp) to allow corporate users to use the Google Cloud console, the gcloud CLI, and other resources that must or could use Google as IdP.
  * [Extend your IdP to Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#patterns_for_extending_an_external_idp_to_gcp) to enable resources that cannot use Google as IdP to be run on Google Cloud.



If a resource relies on protocols that the Google IdP doesn't support, that resource cannot use Google as IdP. Such protocols include:

  * **LDAP for authentication** : Although you can use Secure LDAP to facilitate querying user information from Cloud Identity through LDAP, Cloud Identity does not support using LDAP for authentication when federated with an external IdP.

To allow applications to use LDAP for authentication, you can [expose](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#exposing_an_on-premises_ldap_directory_to_gcp) or [replicate an on-premises LDAP directory](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#replicate_an_on-premises_ldap_directory_to_gcp) or you can [extend your Active Directory to Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#extending_an_on-premises_active_directory_to_gcp).

  * **WS-Trust, WS-Federation** : Especially if you use AD FS, you might still rely on WS-Trust or WS-Federation to handle token-based authentication. Unless you can change affected applications to use SAML or OpenID Connect, it's best to [expose your on-premises AD FS to Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#exposing_an_on-premises_ad_fs_to_gcp) and have the applications use AD FS directly.

  * **OpenID Connect with AD FS-specific claims** : AD FS and Google support OpenID Connect. If you have been using AD FS as an OpenID Connect provider, you might rely on certain AD FS-specific claims that Google doesn't support. If so, consider [exposing your on-premises AD FS to Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#exposing_an_on-premises_ad_fs_to_gcp) and have affected applications directly use AD FS.

  * **Kerberos, NTLM** : If some of your applications use Kerberos or NTLM for authentication, you might be able to modify them to use OpenID Connect or SAML instead. If this isn't possible, you can deploy these applications on domain-joined Windows servers and either [expose](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#exposing_an_on-premises_ldap_directory_to_gcp) or [replicate your on-premises Active Directory to Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#replicate_an_on-premises_ldap_directory_to_gcp).

  * **Windows virtual machines** : If you run Windows workloads on Google Cloud, you must be able to sign in to these VMs through Remote Desktop Protocol (RDP), through a Remote Desktop Gateway, or by other means. If a user has write access to the Google Cloud project where the VM was created, Google Cloud lets the user [create a user and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances), which creates an account in the VM's local Security Account Manager (SAM) database. Crucially, the resulting Windows SAM account isn't connected to the user's Google Account and isn't subject to the same account lifecycle. If you suspend or delete the user's Google Account, the Windows SAM account is unaffected and might continue to provide access to the VM.

If you have a moderate number of Windows VMs and users that must be able to sign in to these machines, then letting users generate Windows user accounts and passwords might be a viable approach. But when managing larger fleets of Windows servers, it can be better to [extend an on-premises Active Directory to Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#extending_an_on-premises_active_directory_to_gcp) and domain-join the respective servers. Domain-joining servers is also a requirement if you rely on Network Level Authentication.




## Availability

The final factor to look at is availability. The ability to authenticate users is likely critical for many of your workloads, and an IdP outage can have far-reaching consequences. The right approach to ensuring suitable availability depends on how you intend to use Google Cloud and how it fits into your hybrid strategy.

### Distributed workloads

To capitalize on the unique capabilities that each computing environment offers, you might use a hybrid multi-cloud approach to [distribute workloads across those environments](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns). These environments might have dependencies on one another that are critical to availability of your workloads. Dependencies might include [VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnels or [interconnects](https://docs.cloud.google.com/network-connectivity/docs/interconnect), applications communicating with one another, or systems accessing data across computing environments.

When federating or extending your external IdP to Google Cloud, ensure that availability of your external IdP and other systems required for authentication meets or exceeds the availability of other critical dependencies. This requirement means that you might need to both redundantly deploy the external IdP and its dependencies _and_ ensure redundant network connectivity.

### Redundant workloads

If you use Google Cloud for ensuring [business continuity](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns), your workloads on Google Cloud are going to mirror some of the workloads you have in your computing environment. The purpose of such a setup is to enable one computing environment to take over the role of the other environment if a failure occurs. So you need to look at every dependency between these environments.

By having Google Cloud rely on an external IdP running on-premises, you create a dependency. That dependency could undermine the intent of having Google Cloud be an independent copy of your computing environment.

Try to replicate your IdP to Google Cloud so that all workloads on Google Cloud are unaffected by an outage of your on-premises computing environment or of connectivity between Google Cloud and your on-premises network.

## What's next

  * Review [common patterns for authenticating workforce users in a hybrid environment](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment).
  * Review the [identity provisioning options for Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
