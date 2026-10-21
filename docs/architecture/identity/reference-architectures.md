---
url: https://docs.cloud.google.com/architecture/identity/reference-architectures/
title: Reference architectures \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:12.624684+00:00
---

# Reference architectures  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/reference-architectures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Reference architectures Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

This document presents typical architectures that you can use as a reference for managing corporate identities. Two core tenets of corporate identity management are the following:

  * An **authoritative source for identities** that is the sole system that you use to create, manage, and delete identities for your employees. The identities managed in the authoritative source system might be propagated to other systems.

  * A central **identity provider (IdP)** that is the sole system for authentication and that provides a single sign-on experience for your employees that spans applications.




When you use Google Cloud or other Google services, you must decide which system to use as your identity provider and which system to use as your authoritative source.

## Use Google as an IdP

By using [Cloud Identity Premium](https://docs.cloud.google.com/identity) or [Google Workspace](https://workspace.google.com/), you can make Google your primary IdP. Google provides a [large selection of ready-to-use integrations](https://workspace.google.com/marketplace) for popular third-party applications, and you can use standard protocols such as [SAML](https://support.google.com/a/answer/6087519), [OAuth](https://support.google.com/googleapi/answer/6158849), and [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect) to integrate your custom applications.

### Google as IdP and authoritative source

You can use Cloud Identity Premium or Google Workspace as both IdP and as authoritative source, as in the following diagram.

![Google as IdP and authoritative source.](https://docs.cloud.google.com/static/architecture/identity/images/google-as-idp.svg)

  * You use Cloud Identity Premium or Google Workspace to manage users and groups.
  * All Google services use Cloud Identity Premium or Google Workspace as the IdP.
  * You configure corporate applications and other SaaS services to use Google as the IdP.



#### User experience

In this configuration, to an employee, the sign-on user experience looks like this:

  1. Upon requesting a protected resource or access to a corporate application, the employee is redirected to the Google Sign-In screen, which prompts you for your email address and your password.
  2. If [2-step verification](https://www.google.com/landing/2step/) is enabled, the employee is prompted to provide a second factor such as a USB key or code.
  3. When the employee is authenticated, they are redirected back to the protected resource.



#### Advantages

Using Google as your IdP and authoritative source has the following advantages:

  * You can take full advantage of Google's [multi-factor authentication](https://docs.cloud.google.com/identity) and [mobile device management](https://docs.cloud.google.com/identity/mdm) features.
  * You don't need an additional IdP, which might save you money.



#### When to use this architecture

Consider using Google as IdP and authoritative source in the following scenarios:

  * You already use Google Workspace as your collaboration and productivity solution.
  * There is no existing on-premises infrastructure or IdP that you have to integrate with or you would like to keep it separate from all of your resources on Google (in Google Cloud, in Google Ads, and so on).
  * You don't require integration with a human resources information system (HRIS) to manage identities.



### Google as IdP with an HRIS as authoritative source

If you use a human resources information system (HRIS) to manage the onboarding and offboarding process for your employees, you can still use Google as your IdP. Cloud Identity and Google Workspace provide APIs that let HRIS and other systems take control of managing users and groups, as shown in the following diagram.

![Google as IdP with an HRIS as authoritative source.](https://docs.cloud.google.com/static/architecture/identity/images/google-as-idp-with-hris.svg)

  * You use your existing HRIS to manage users and optionally groups. The HRIS remains the single source of truth for identity management and automatically provisions users for Cloud Identity or Google Workspace.
  * All Google services use Cloud Identity Premium or Google Workspace as the IdP.
  * You configure corporate applications and other SaaS services to use Google as the IdP.



#### User experience

To an employee, the sign-on user experience is equivalent to using Google as IdP and authoritative source.

#### Advantages

Using Google as the IdP and authoritative source has the following advantages:

  * You can minimize administrative overhead by reusing your existing HRIS workflows.
  * You can take full advantage of Google's [multi-factor authentication](https://docs.cloud.google.com/identity) and [mobile device management](https://docs.cloud.google.com/identity/mdm) features.
  * You don't need an additional IdP, which might save you money.



#### When to use this architecture

Consider using Google as your IdP with an HRIS as authoritative source in the following scenarios:

  * You have an existing HRIS or other system that serves as the authoritative source for identities.
  * You already use Google Workspace as your collaboration and productivity solution.
  * There is no existing on-premises infrastructure or IdP that you have to integrate with or that you would like to keep separate from your Google estate.



## Use an external IdP

If your organization already uses an IdP such as Active Directory, Microsoft Entra ID (formerly Azure AD), ForgeRock, Okta, or Ping Identity, then you can integrate Google Cloud with this external IdP by using federation.

By [federating a Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_identities) with an external IdP, you can let employees use their existing identity and credentials to sign in to Google services such as Google Cloud, Google Marketing Platform, and Google Ads.

### External IDaaS as IdP and authoritative source

If you use an identity as a service (IDaaS) provider such as ForgeRock, Okta, or Ping Identity, then you can set up federation as illustrated in the following diagram.

![External IDaaS as IdP and authoritative source.](https://docs.cloud.google.com/static/architecture/identity/images/external-idaas-as-idp.svg)

  * Cloud Identity or Google Workspace uses your IDaaS as the IdP for single sign-on.
  * The IDaaS automatically provisions users and groups for Cloud Identity or Google Workspace.
  * Existing corporate applications and other SaaS services can continue to your IDaaS as an IdP.



To learn more about federating Cloud Identity or Google Workspace with Okta, see [Okta user provisioning and single sign-on](https://docs.cloud.google.com/architecture/identity/okta-provisioning-and-single-sign-on).

**User experience**

To an employee, the sign-on user experience looks like this:

  1. Upon requesting a protected resource, the employee is redirected to the Google Sign-In screen, which prompts them for their email address.
  2. Google Sign-In redirects you to the sign-in page of your IDaaS.
  3. You authenticate with your IDaaS. Depending on your IDaaS, this might require you to provide a second factor such as a code.
  4. After you are authenticated, you are redirected back to the protected resource.



**Advantages**

Using an external IDaaS as IdP and authoritative source has the following advantages:

  * You enable a single sign-on experience for your employees that extends across Google services and other applications that are integrated with your IDaaS.
  * If you configured your IDaaS to require multi-factor authentication, that configuration automatically applies to Google Cloud.
  * You don't need to synchronize passwords or other credentials with Google.
  * You can use the free version of Cloud Identity.



**When to use this architecture**

Consider using an external IDaaS as IdP and authoritative source in the following scenarios:

  * You already use an IDaaS provider such as ForgeRock, Okta, or Ping Identity as your IdP.



**Best practices**

See our [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

### Active Directory as IdP and authoritative source

If you use Active Directory as the source of truth for identity management, then you can set up federation as illustrated in the following diagram.

![Active Directory as IdP and authoritative source.](https://docs.cloud.google.com/static/architecture/identity/images/active-directory-as-idp.svg)

  * You use [Google Cloud Directory Sync (GCDS)](https://tools.google.com/dlpage/dirsync/) to automatically provision users and groups from Active Directory for Cloud Identity or Google Workspace. Google Cloud Directory Sync is a free Google-provided tool that implements the synchronization process and can be run either on Google Cloud or in your on-premises environment. Synchronization is one-way so that Active Directory remains the source of truth.
  * Cloud Identity or Google Workspace uses Active Directory Federation Services (AD FS) for single sign-on.
  * Existing corporate applications and other SaaS services can continue to use your AD FS as an IdP.



For a variation of this pattern, you can also use Active Directory Lightweight Directory Services (AD LDS) or a different LDAP directory with either AD FS or another SAML-compliant IdP.

For more information about this approach, see [Federate Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).

#### User experience

  1. Upon requesting the protected resource, the employee is redirected to the Google Sign-in screen, which prompts them for their email address.
  2. Google Sign-In redirects the employee to the sign-in page of AD FS.
  3. Depending on the configuration of AD FS, the employee might see a sign-on screen prompting for their Active Directory username and password. Alternatively, AD FS might attempt to sign the employee in automatically based on their Windows login.
  4. After AD FS has authenticated the employee, they are redirected back to the protected resource.



#### Advantages

Using Active Directory as IdP and authoritative source has the following advantages:

  * You enable a single sign-on experience for your employees that extends across Google services and your on-premises environment.
  * If you configured AD FS to require multi-factor authentication, that configuration automatically applies to Google Cloud.
  * You don't need to synchronize passwords or other credentials to Google.
  * You can use the free version of Cloud Identity.
  * Because the APIs that GCDS uses are publicly accessible, there's no need to set up [hybrid connectivity](https://cloud.google.com/hybrid-connectivity/) between your on-premises network and Google Cloud.



#### When to use this architecture

Consider using Active Directory as the IdP and authoritative source in the following scenarios:

  * You have an existing Active Directory infrastructure.
  * You want to provide a seamless sign-in experience for Windows users.



#### Best practices

Consider these best practices:

  * Active Directory and Cloud Identity use a different logical structure. Make sure you understand the differences and assess which method of mapping domains, identities, and groups best suits your situation. For more information, see our [guide on federating Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).
  * Synchronize groups in addition to users. With this approach, you can set up IAM so that you can use group memberships in Active Directory to control who has access to which resources in Google Cloud.
  * Deploy and expose AD FS so that corporate users can access it, but don't expose it more than necessary. Although corporate users must be able to access AD FS, there's no requirement for AD FS to be reachable from Cloud Identity or Google Workspace, or from any application deployed on Google Cloud.
  * Consider enabling Integrated Windows Authentication (IWA) in AD FS to allow users to sign in automatically based on their Windows login.
  * If AD FS becomes unavailable, users might not be able to use the Google Cloud console or any other resource that uses Google as IdP. So ensure that AD FS and the domain controllers AD FS relies on are deployed and sized to meet your availability objectives.
  * If you use Google Cloud to help ensure business continuity, relying on an on-premises AD FS might undermine the intent of using Google Cloud as an independent copy of your deployment. In this case, consider deploying replicas of all relevant systems on Google Cloud in one of the following ways:

    * [Extend your existing Active Directory domain](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#extended_domain) to Google Cloud and deploy GCDS to run on Google Cloud.
    * Run dedicated AD FS servers on Google Cloud. These servers use the Active Directory domain controllers that are running on Google Cloud.
    * Configure Cloud Identity to use the AD FS servers deployed on Google Cloud for single sign-on.



To learn more, see [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

### Entra ID as IdP with Active Directory as authoritative source

If you are a Microsoft 365 or Azure customer, you might have connected your on-premises Active Directory to Entra ID. If all user accounts that potentially need access to Google Cloud are already being synchronized to Entra ID, you can reuse this integration by federating Cloud Identity with Entra ID, as shown in the following diagram.

![Entra ID as IdP with Active Directory as authoritative source.](https://docs.cloud.google.com/static/architecture/identity/images/entra-id-as-idp.svg)

  * You use Entra ID to automatically provision users and groups to Cloud Identity or Google Workspace. Entra ID itself might be integrated with an on-premises Active Directory.
  * Cloud Identity or Google Workspace use Entra ID for single sign-on.
  * Existing corporate applications and other SaaS services can continue to use Entra ID as an IdP.



For more detailed information about this approach, see [Federate Google Cloud with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).

#### User experience

  1. Upon requesting the protected resource, the employee is redirected to the Google Sign-In screen, which prompts them for their email address.
  2. Google Sign-In redirects them to the sign-in page of AD FS.
  3. Depending on how their on-premises Active Directory is connected to Entra ID, Entra ID might prompt them for a username and password, or it might redirect them to an on-premises AD FS.
  4. After the employee is authenticated with Entra ID, they are redirected back to the protected resource.



**Advantages**

Using Entra ID as your IdP with Active Directory as authoritative source has several advantages:

  * You enable a single sign-on experience for your employees that extends across Google services, Entra, and your on-premises environment.
  * If you configured Entra ID to require multi-factor authentication, that configuration automatically applies to Google Cloud.
  * You don't need to install any additional software on-premises.
  * If your on-premises Active Directory uses multiple domains or forests and you have set up a custom Entra ID Connect configuration to map this structure to an Entra ID tenant, you can take advantage of this integration work.
  * You don't need to synchronize passwords or other credentials to Google.
  * You can use the free version of Cloud Identity.
  * You can surface the Google Cloud console as a tile in the Office 365 portal.
  * Because the APIs that Entra ID uses are publicly accessible, there's no need to set up [hybrid connectivity](https://cloud.google.com/hybrid-connectivity/) between Entra and Google Cloud.



#### When to use this architecture

Consider using Entra ID as IdP with Active Directory as authoritative source in the following scenarios:

  * You already use Entra ID and have integrated it with an existing Active Directory infrastructure.
  * You want to provide a seamless sign-in experience for users across Entra and Google Cloud.



#### Best practices

Follow these best practices:

  * Because Entra ID and Cloud Identity use a different logical structure, make sure you understand the differences. Assess which method of mapping domains, identities, and groups best suits your situation. For more detailed information, see [Federate Google Cloud with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Synchronize groups in addition to users. With this approach, you can set up IAM so that you can use group memberships in Entra ID to control who has access to which resources in Google Cloud.
  * If you use Google Cloud to help ensure business continuity, relying on Entra ID for authentication might undermine the intent of using Google Cloud as an independent copy of your deployment.



To learn more, see [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

## What's next

  * Learn more about [federating with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Find out how to [set up federation with Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Review our [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and for [federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
