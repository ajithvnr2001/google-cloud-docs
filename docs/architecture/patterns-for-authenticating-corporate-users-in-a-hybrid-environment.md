---
url: https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment/
title: Patterns for authenticating workforce users in a hybrid environment \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:31.238569+00:00
---

# Patterns for authenticating workforce users in a hybrid environment  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Patterns for authenticating workforce users in a hybrid environment Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

This document is the second part of a multi-part series that discusses how to extend your identity management solution to Google Cloud to enable your workforce users to authenticate and consume services in a hybrid computing environment.

The series consists of the following documents:

  * [Authenticating workforce users in a hybrid environment](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment)
  * Patterns for authenticating workforce users in a hybrid environment (this document)



## Introduction

When you extend your IT landscape to Google Cloud as part of a hybrid strategy, we recommend that you take [a consistent approach to managing identities across environments](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment). As you design and tailor your architecture to meet these constraints and requirements, you can rely on some common patterns. These patterns fall into two categories:

  * **Patterns for federating an external identity provider (IdP) with Google Cloud**. The aim of these patterns is to enable Google to become an IdP for your workforce users so that Google identities are maintained automatically and your IdP remains the source of truth.
  * **Patterns for extending an IdP to Google Cloud**. In these patterns, you let applications deployed on Google Cloud reuse your IdP—either by connecting to it directly or by maintaining a replica of your IdP on Google Cloud.



## Patterns for federating an external IdP with Google Cloud

To enable access to the Google Cloud console, the Google Cloud CLI, or any other resource that uses Google as IdP, a workforce user must have a Google identity. Maintaining Google identities for each employee would be cumbersome when all employees already have an account in an IdP. By federating user identities between your IdP and Google Cloud, you can automate the maintenance of Google Accounts and tie their lifecycle to accounts that exist. Federation helps ensure the following:

  * Your IdP remains the single source of truth for identity management.
  * For all user accounts that your IdP manages, or a selected subset of those accounts, a Google Account is created automatically.
  * If an account is disabled or deleted in your IdP, the corresponding Google Account is suspended or deleted.
  * To prevent passwords or other credentials from being copied, the act of authenticating a user is delegated to your IdP.



### Federate Active Directory with Cloud Identity by using Google Cloud Directory Sync and AD FS

If you use Active Directory as IdP, you can [federate Active Directory with Cloud Identity](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction) by using [Google Cloud Directory Sync (GCDS)](https://tools.google.com/dlpage/dirsync/) and Active Directory Federation Services (AD FS):

  * GCDS is a free Google-provided tool that implements the synchronization process. GCDS communicates with Identity Platform over Secure Sockets Layer (SSL) and usually runs in the existing computing environment.
  * AD FS is provided by Microsoft as part of Windows Server. With AD FS, you can use Active Directory for federated authentication. AD FS usually runs in the existing computing environment.



For more detailed information about this approach, see [Federate Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).

![Pattern: Federating Active Directory with Cloud Identity by using GCDS and AD FS.](https://docs.cloud.google.com/static/architecture/images/authenticating-corporate-users-federate-ad-with-cloud-identity.svg)

For a variation of this pattern, you can also use Active Directory Lightweight Directory Services (AD LDS) or a different LDAP directory with either AD FS or another SAML-compliant IdP.

#### User experience

  1. When you request the protected resource, you are redirected to the Google sign-on screen, which prompts you for your email address.
  2. If the email address is known to be associated with an account that has been synchronized from Active Directory, you are redirected to AD FS.
  3. Depending on the configuration of AD FS, you might see a sign-on screen prompting for your Active Directory username and password. Or AD FS might attempt to sign you in automatically based on your Windows login (IWA).
  4. When AD FS has authenticated you, you are redirected back to the protected resource.



#### Advantages

  * The approach enables a single sign-on experience across on-premises applications and resources on Google Cloud.
  * If you configured AD FS to require multi-factor authentication, that configuration automatically applies to Google Cloud.
  * You don't need to synchronize passwords or other credentials to Google.
  * Because the Cloud Identity API is publicly accessible, there's no need to set up [hybrid connectivity](https://cloud.google.com/hybrid-connectivity/) between your on-premises network and Google Cloud.



#### Best practices

  * Active Directory and Cloud Identity use a different logical structure. Make sure you understand the differences and assess which way of mapping domains, identities, and groups suits your situation best. Refer to our [guide on federating Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction) for more detailed information.
  * Synchronize groups in addition to users. With this approach, you can set up IAM so that you can use group memberships in Active Directory to control who has access to resources in Google Cloud.
  * Deploy and expose AD FS so that workforce users can access it, but don't expose it more than necessary. Although workforce users must be able to access AD FS, there's no requirement for AD FS to be reachable from Google or from any application deployed on Google Cloud.
  * Consider enabling Integrated Windows Authentication (IWA) in AD FS to allow users to sign in automatically based on their Windows login.
  * If AD FS becomes unavailable, users might not be able to use the Google Cloud console or any other resource that uses Google as IdP. So ensure that AD FS and the domain controllers AD FS relies on are deployed and sized to meet your availability objectives.
  * If you use Google Cloud to help ensure business continuity, relying on an on-premises AD FS might undermine the intent of using Google Cloud as an independent copy of your deployment. In this case, consider deploying replicas of all relevant systems on Google Cloud: 
    * Replicate your Active Directory to Google Cloud and deploy GCDS to run on Google Cloud.
    * Run dedicated AD FS servers on Google Cloud. These servers use the Active Directory domain controllers running on Google Cloud.
    * Configure Cloud Identity to use the AD FS servers deployed on Google Cloud for single sign-on.



### Federate Entra ID with Cloud Identity

If you are a Microsoft Office 365 or Azure customer, you might have connected your on-premises Active Directory to Microsoft Entra ID (formerly Azure AD). If all user accounts that potentially need access to Google Cloud are already being synchronized to Entra ID, you can reuse this integration by federating Cloud Identity with Entra ID, as the following diagram shows.

![Federating Cloud Identity with Entra ID.](https://docs.cloud.google.com/static/architecture/images/authenticating-corporate-users-federating-cloud-identity-with-entra.svg)

For more detailed information about this approach, see [Federate Google Cloud with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).

#### User experience

  1. When you request the protected resource, you are redirected to the Google sign-on screen, which prompts you for your email address.
  2. If the email address is associated with an account that has been synchronized from Entra ID, you are redirected to Entra ID.
  3. Depending on how your on-premises Active Directory is connected to Entra ID, Entra ID might prompt you for a username and password. Or it might redirect you to an on-premises AD FS.
  4. After successfully authenticating with Entra ID, you are redirected back to the protected resource.



#### Advantages

  * You don't need to install any additional software on-premises.
  * The approach enables a single sign-on experience across Office 365, Azure, and resources on Google Cloud.
  * If you configured Entra ID to require multi-factor (MFA) authentication, MFA automatically applies to Google Cloud.
  * If your on-premises Active Directory uses multiple domains or forests and you have set up a custom Entra ID Connect configuration to map this structure to an Entra ID tenant, you can take advantage of this integration work.
  * You don't need to synchronize passwords or other credentials to Google.
  * Because the Cloud Identity API is publicly accessible, there's no need to set up [hybrid connectivity](https://cloud.google.com/hybrid-connectivity/) between your on-premises network and Google Cloud or between Azure and Google Cloud.
  * You can surface the Google Cloud console as a tile in the Office 365 portal.



#### Best practices

  * Because Entra ID and Cloud Identity use a different logical structure, make sure you understand the differences. Assess which way of mapping domains, identities, and groups suits your situation best. For more detailed information, see [federating Google Cloud with Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Synchronize groups in addition to users. With this approach, you can set up IAM so that you can use group memberships in Entra ID to control who has access to resources in Google Cloud.
  * If you use Google Cloud to help ensure business continuity, relying on Entra ID for authentication might undermine the intent of using Google Cloud as an independent copy of your deployment.



## Patterns for extending an external IdP to Google Cloud

Some of the applications you plan to deploy on Google Cloud might require the use of [authentication protocols](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment#resources-that-use-google-as-idp) not offered by Cloud Identity. To support these workloads, you must allow these applications to use your IdP from within Google Cloud.

The following sections describe common patterns for allowing your IdP to be used by workloads deployed on Google Cloud.

### Expose an on-premises AD FS to Google Cloud

If an application requires the use of WS-Trust or WS-Federation, or relies on AD FS-specific features or claims when using OpenID Connect, you can allow the application to directly use AD FS for authentication.

![Application directly using AD FS for authentication.](https://docs.cloud.google.com/static/architecture/images/authenticating-corporate-users-auth-using-ad-fs.svg)

By using AD FS, an application can authenticate a user. However, because authentication is not based on a Google identity, the application won't be able to perform any API calls authenticated [with user credentials](https://docs.cloud.google.com/docs/authentication#user-accounts). Instead, any calls to Google Cloud APIs must be authenticated [using a service account](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).

#### User experience

  1. When you request the protected resource, you are redirected to the ADFS sign-on screen, which prompts you for your email address. If AD FS isn't publicly exposed over the internet, accessing AD FS might require you to be connected to your company network or corporate VPN.
  2. Depending on the configuration of AD FS, you might see a sign-on screen prompting for your Active Directory username and password. Or AD FS might attempt to sign you in automatically based on your Windows login.
  3. When AD FS has authenticated you, you are redirected back to the protected resource.



#### Advantages

  * You can use authentication protocols that aren't supported by Cloud Identity, including WS-Trust and WS-Federation.
  * If the application has been developed and tested against AD FS, you can avoid risks that might arise from switching the application to use Cloud Identity.
  * There's no need to set up [hybrid connectivity](https://cloud.google.com/hybrid-connectivity/) between your on-premises network and Google Cloud.



#### Best practices

  * Deploy and expose AD FS so that workforce users can access it, but don't expose it more than necessary. Although workforce users must be able to access AD FS, there's no requirement for AD FS to be reachable from Google or from any application deployed on Google Cloud.
  * If AD FS becomes unavailable, users might not be able to use the application anymore. Ensure that AD FS and the domain controllers it relies on are deployed and sized to meet your availability objectives.
  * Consider refactoring applications that rely on WS-Trust and WS-Federation to use SAML or OpenID Connect instead.
  * If the application relies on group information being exposed as claims in `IdTokens` issued by AD FS, consider retrieving group information from a different source such as the [Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/members/get). Querying the Directory API is a privileged operation that requires using a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) that is enabled for [Google Workspace domain-wide delegation](https://developers.google.com/admin-sdk/reports/v1/guides/delegation).



### Expose an on-premises LDAP directory to Google Cloud

Some of your applications might require users to provide their username and password and use these credentials to attempt an LDAP bind operation. If you cannot [modify these applications](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment#ldap) to use other means such as SAML to perform authentication, you can grant them access to an on-premises LDAP directory.

![Granting users access to an on-premises LDAP directory.](https://docs.cloud.google.com/static/architecture/images/authenticating-corporate-users-on-prem-ldap.svg)

#### Advantages

  * You don't need to change your application.



#### Best practices

  * Use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) to establish hybrid connectivity between Google Cloud and your on-premises network so that you don't need to expose the LDAP directory over the internet.
  * Verify that the latency introduced by querying an on-premises LDAP directory doesn't negatively impact user experience.
  * Ensure that the communication between the application and the LDAP directory is encrypted. You can achieve this encryption by using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or by using [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) with LDAP/S.
  * If the LDAP directory or the private connectivity between Google Cloud and your on-premises network becomes unavailable, users might not be able to use an LDAP-based application anymore. Therefore, ensure that the respective servers are deployed and sized to meet your availability objectives, and consider using [redundant VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/redundant-vpns) or [interconnects](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview).
  * If you use Google Cloud to ensure business continuity, relying on an on-premises LDAP directory might undermine the intent of using Google Cloud as an independent copy of your existing deployment. In this case, consider replicating the LDAP directory to Google Cloud instead.
  * If you use Active Directory, consider [running a replica on Google Cloud instead](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment#heading=h.ps5qjiahyxoj), particularly if you plan to domain-join Windows machines running on Google Cloud to Active Directory.



### Replicate an on-premises LDAP directory to Google Cloud

Replicating an on-premises LDAP directory to Google Cloud is similar to the pattern of Exposing an on-premises LDAP directory to Google Cloud. For applications that use LDAP to verify usernames and passwords, the intent of this approach is to be able to run those applications on Google Cloud. Instead of allowing such applications to query your on-premises LDAP directory, you can maintain a replica of the on-premises directory on Google Cloud.

![Maintaining a replica of the on-premises directory on Google Cloud.](https://docs.cloud.google.com/static/architecture/images/authenticating-corporate-users-on-prem-replica.svg)

#### Advantages

  * You don't need to change your application.
  * The availability of LDAP-based applications running on Google Cloud doesn't depend on the availability of the on-premises directory or connectivity to the on-premises network. This pattern is well-suited for [business continuity hybrid scenarios](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-architecture-patterns#business_continuity_hybridmulti-cloud).



#### Best practices

  * Use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) to establish hybrid connectivity between Google Cloud and your on-premises network so that you don't need to expose the LDAP directory over the internet.
  * Ensure that the replication between the on-premises LDAP directory is conducted over a secure channel.
  * Deploy multiple LDAP directory replicas across multiple [zones or regions](https://docs.cloud.google.com/compute/docs/regions-zones) to meet your availability objectives. You can use an [internal load balancer](https://docs.cloud.google.com/load-balancing/docs/internal) to distribute LDAP connections among multiple replicas deployed in the same region.
  * Use a separate Google Cloud project with a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) to deploy LDAP replicas and grant access to this project on a least-privilege basis.



### Extend an on-premises Active Directory to Google Cloud

Some of the workloads that you plan to deploy on Google Cloud might depend on Active Directory Domain Services, for example:

  * Windows machines that need to be domain-joined
  * Applications that use Kerberos or NTLM for authentication
  * Applications that use Active Directory as an LDAP directory to verify usernames and passwords



To support such workloads, you can extend your on-premises Active Directory forest to Google Cloud—for example, by deploying a resource forest to Google Cloud and connecting it to your on-premises Active Directory forest, as in the following diagram.

![Connecting a resource forest to your on-premises Active Directory forest.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-active-directory-in-hybrid-4-synchronized-forests.svg)

For more detail about this approach and other ways to deploy Active Directory in a hybrid environment, see [Patterns for using Active Directory in a hybrid environment](https://docs.cloud.google.com/architecture/patterns-for-using-active-directory-in-a-hybrid-environment).

![Extending your on-premises Active Directory forest to Google Cloud by deploying additional domain controllers on Google Cloud.](https://docs.cloud.google.com/static/architecture/images/authenticating-corporate-users-deploy-additional-controllers.svg)

#### Advantages

  * Your workloads can take full advantage of Active Directory, including the ability to join Windows machines to the Active Directory domain.
  * The availability of Active Directory-based applications running on Google Cloud doesn't depend on the availability of on-premises resources or connectivity to the on-premises network. The pattern is well-suited for [business continuity hybrid scenarios](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-architecture-patterns#business_continuity_hybridmulti-cloud).



#### Best practices

  * Use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) to establish hybrid connectivity between Google Cloud and your on-premises network.
  * To minimize communication between Google Cloud and your on-premises network, create a separate Active Directory site for Google Cloud deployments. You can use either a single site per Shared VPC or, to minimize inter-region communication, one site per Shared VPC and region.
  * Create a separate Active Directory domain dedicated to resources deployed on Google Cloud and add the domain to the existing forest. Using a separate domain helps reduce replication overhead and partition sizes.
  * To increase availability, [deploy at least two domain controllers](https://docs.cloud.google.com/architecture/deploy-fault-tolerant-active-directory-environment), spread over multiple zones1. If you use multiple regions, consider deploying domain controllers in each region.
  * Use a separate Google Cloud project with a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) to deploy domain controllers and grant access to this project on a least-privilege basis. By [generating a password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) or accessing the [serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console) of domain controller instances, rogue project members might otherwise be able to compromise the domain.
  * Consider deploying an AD FS server farm and GCDS on Google Cloud. This approach lets you [federate Active Directory with Cloud Identity](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory) without depending on the availability of resources or connectivity to the on-premises network.



## What's next

  * Learn more about [federating Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).
  * Learn more about [patterns for using Active Directory in a hybrid environment](https://docs.cloud.google.com/architecture/patterns-for-using-active-directory-in-a-hybrid-environment).
  * Find out how you can [federate Cloud Identity with Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Design the [resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



* * *

  1. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). ↩




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
