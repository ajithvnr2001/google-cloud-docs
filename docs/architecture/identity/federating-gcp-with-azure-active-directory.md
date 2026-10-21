---
url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory/
title: Federate Google Cloud with Microsoft Entra ID (formerly Azure AD) \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:02:26.928268+00:00
---

# Federate Google Cloud with Microsoft Entra ID (formerly Azure AD)  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Federate Google Cloud with Microsoft Entra ID (formerly Azure AD) Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

This document describes how you can configure Cloud Identity or Google Workspace to use [Microsoft Entra ID (formerly Azure AD) as IdP and source for identities](https://docs.cloud.google.com/architecture/identity/reference-architectures#azure_ad_as_idp_with_active_directory_as_authoritative_source).

The document compares the logical structure of Microsoft Entra ID with the structure used by Cloud Identity and Google Workspace and describes how you can map Microsoft Entra ID tenants, domains, users, and groups.

## Implement federation

Google Cloud uses [Google identities](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_identities) for authentication and access management. Manually maintaining Google identities for each employee can add unnecessary management overhead when all employees already have an account in Microsoft Entra ID. By federating user identities between Google Cloud and your existing identity management system, you can automate the maintenance of Google identities and tie their lifecycle to existing users in Microsoft Entra ID.

![Federate Cloud Identity with Microsoft Entra ID.](https://docs.cloud.google.com/static/architecture/identity/images/entra-id-as-idp.svg)

Setting up federation between Microsoft Entra ID and Cloud Identity or Google Workspace entails two pieces:

  * **Provisioning users** : Relevant users and groups are synchronized periodically from Microsoft Entra ID to Cloud Identity or Google Workspace. This process ensures that when you create a new user in Microsoft Entra ID or synchronize a new user from Active Directory to Microsoft Entra ID, it's also made available in Google Cloud so that it can be referenced in Google Cloud even before the associated user has logged in for the first time. This process also ensures that user deletions are being propagated.

Provisioning works one way, which means changes in Microsoft Entra ID are replicated to Google Cloud but not vice versa. Also, provisioning doesn't include passwords.

  * **Single sign-on (SSO)** : Whenever a user needs to authenticate, Google Cloud delegates the authentication to Microsoft Entra ID by using the Security Assertion Markup Language (SAML) protocol. Depending on your Microsoft Entra ID configuration, Microsoft Entra ID might do one of the following:

    * Perform authentication itself.
    * Use pass-through authentication or password hash synchronization.
    * Delegate authentication to an on-premises AD FS server.



Having Cloud Identity or Google Workspace delegate authentication to Microsoft Entra ID not only avoids having to synchronize passwords to Google Cloud, it also ensures that any applicable policies or multi-factor authentication (MFA) mechanisms you have configured in Microsoft Entra ID or AD FS are enforced.

**Note:** This document refers to the [_Google Cloud/G Suite Connector by Microsoft_ gallery app from the Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/aad.googleapps). This app is a Microsoft product and is not maintained or supported by Google.

### Logical structure of Microsoft Entra ID

When you use Azure, you use one or more Microsoft Entra ID tenants (also referred to as _directories_). Microsoft Entra ID tenants are a top-level structure. They are considered administrative boundaries, and serve as containers for users, groups, as well as resources and resource groups.

Each Microsoft Entra ID tenant has at least one DNS domain associated with it. This DNS domain is reflected in usernames (also referred to as _User Principal Names_ or _UPNs_), which take the form of `name@domain`, where `domain` is one of the DNS domains associated with the corresponding tenant.

![Logical structure of Microsoft Entra ID.](https://docs.cloud.google.com/static/architecture/images/federating-gcp-with-entra-id-entra-structure.svg)

An enterprise might maintain multiple Microsoft Entra ID tenants. Common reasons for having multiple tenants include distinguishing between different parts of the organization, separating production resources from development and testing resources, and using separate tenants to integrate multiple forests from an on-premises Active Directory.

### Logical structure of Google Cloud

In Google Cloud, [organizations](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#organization_node) serve as containers for all resources, and they can be further [segmented by using folders and projects](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). However, except for [service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts), organizations aren't used to manage users and groups, making organizations different from Microsoft Entra ID tenants.

For managing users and groups, Google Cloud relies on Cloud Identity or Google Workspace. A [Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#cloud_identity_or_g_suite_account) serves as a private directory for users and groups. As an administrator of the account, you can control the lifecycle and the configuration of users and groups and define how authentication can be performed.

![Logical structure of Google Cloud.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-active-directory-gcp-structure.svg)

When you create a Cloud Identity or Google Workspace account, [a Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) is created automatically for you. The Cloud Identity or Google Workspace account and the Google Cloud organization that's associated with it share the same name and are tied to each other. However, a Google Cloud organization is allowed to reference users and groups from other Cloud Identity or Google Workspace accounts.

### Integrate Microsoft Entra ID and Google Cloud

Despite certain similarities between the logical structure of Microsoft Entra ID and Google Cloud, no single mapping between the two structures works equally well in all scenarios. Instead, the right approach to integrating the two systems and mapping the structure depends on multiple factors:

  * How to map Microsoft Entra ID tenants to Cloud Identity or Google Workspace accounts
  * How to map DNS domains
  * How to map users
  * How to map groups



The following sections look at each of these factors.

Google Cloud interacts only with Microsoft Entra ID, not with your on-premises Active Directory. So the way you've mapped forests and domains of your on-premises Active Directory to Microsoft Entra ID is of minor concern.

## Map Microsoft Entra ID tenants

The following sections describe how to map Microsoft Entra ID tenants for these scenarios:

  * Single tenant
  * Multiple tenants
  * External users



### Single tenant

If you use only a single Microsoft Entra ID tenant, you can map the tenant to a single Cloud Identity or Google Workspace account and set up federation between the two. This Cloud Identity or Google Workspace account then provides the basis for a single Google Cloud organization that you can use to manage all Google Cloud resources.

![Mapping a tenant to a single Cloud Identity account.](https://docs.cloud.google.com/static/architecture/images/federating-gcp-with-entra-single-tenant.svg)

### Multiple tenants

In larger organizations, it's not uncommon to have more than one Microsoft Entra ID tenant. Multiple tenants might be used to differentiate between testing and production environments, or to differentiate between different parts of an organization.

It's possible to map multiple Microsoft Entra ID tenants to a single Cloud Identity or Google Workspace account, and to set up user provisioning and single sign-on accordingly. However, such an N:1 mapping can weaken the isolation between Microsoft Entra ID tenants: If you grant multiple Microsoft Entra ID tenants permission to create and modify users in a single Cloud Identity or Google Workspace account, then these tenants can interfere and tamper with each other's changes.

Typically, a better approach to integrate with multiple Microsoft Entra ID tenants is to create a separate Cloud Identity or Google Workspace account for each tenant and set up federation between each pair.

In Google Cloud, a separate organization is created for each Cloud Identity or Google Workspace account. Because Google Cloud allows resources to be organized using [projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) and [folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) within a single organization, having more than one organization is often impractical. However, you can select one of the organizations and [associate it](https://docs.cloud.google.com/resource-manager/docs/managing-multiple-orgs#using_multiple_organization_nodes) with the other Cloud Identity or Google Workspace accounts, effectively creating an organization that is federated with multiple Active Directory forests. The other organizations remain unused.

![Organization that is federated with multiple Active Directory forests.](https://docs.cloud.google.com/static/architecture/images/federating-gcp-with-entra-multiple-forests.svg)

### External users

With [Microsoft Entra ID B2B](https://docs.microsoft.com/en-us/azure/active-directory/b2b/), you can invite external users as guests to your Microsoft Entra ID tenant. A new user is created for each guest and Microsoft Entra ID automatically assigns a UPN to these guest users. The UPN that Microsoft Entra ID generates uses a prefix derived from the invitee's email address, combined with the tenant's initial domain: `prefix#EXT#@tenant.onmicrosoft.com`.

Provisioning guest users from Microsoft Entra ID to Cloud Identity or Google Workspace is subject to certain limitations:

  * You cannot map the UPN of guest users to email addresses in Cloud Identity or Google Workspace because `onmicrosoft.com` is a domain that cannot be added and verified in Cloud Identity or Google Workspace. You therefore have to map users by using an attribute other than the UPN.
  * If a guest user is suspended in its home tenant, then the corresponding user in Cloud Identity or Google Workspace might remain active and access to Google Cloud resources might not be properly revoked.



A better way to deal with guest users that originate from a different Microsoft Entra ID tenant is to create multiple Cloud Identity or Google Workspace accounts as outlined in the previous section, each federated with a different Microsoft Entra ID tenant. For more information, see [Microsoft Entra ID B2B user provisioning and single sign-on](https://docs.cloud.google.com/architecture/identity/azure-ad-b2b-user-provisioning-and-sso)

To grant an external user access to certain Google Cloud resources, it's not a prerequisite for the user to have a user account in Cloud Identity or Google Workspace. Unless [restricted by policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), you can also [add the external user directly](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access) as a member to the respective projects, folders, or organization, provided that the user has a Google identity.

## Map DNS domains

DNS plays a crucial role, both for Microsoft Entra ID and for Cloud Identity and Google Workspace. The second factor to look at when planning to federate Microsoft Entra ID and Google Cloud is how you can share or map DNS domains between Microsoft Entra ID and Google Cloud.

### Usage of DNS domains in Google Cloud

[Google Sign-In](https://developers.google.com/identity/), which Google Cloud relies on for authentication purposes, uses email addresses to identify users. Using email addresses not only guarantees that they are globally unique, but also enables Google Cloud to send notification messages to the addresses.

Google Sign-In determines the directory or identity provider to use for authenticating a user based on the domain part of the email addresses, which follows the `@`. For an email address that uses the `gmail.com` domain, for example, Google Sign-In uses the directory of Gmail users for authentication.

![Usage of DNS domains in Google Cloud.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-active-directory-dns-domains.svg)

When you sign up for a [Google Workspace](https://gsuite.google.com/) or [Cloud Identity](https://docs.cloud.google.com/identity) account, you're creating a private directory that Sign-In can use for authentication. In the same way that the Gmail directory is associated with the `gmail.com` domain, Google Workspace and Cloud Identity accounts need to be associated with a custom domain. Three different kinds of domains are used:

  * **Primary domain** : This domain identifies the Cloud Identity or Google Workspace account and is used as the name for the organization in Google Cloud. When signing up for Cloud Identity or Google Workspace, you must specify this domain name.
  * **Secondary domain** : Along with the primary domain, you can associate other, secondary domains with a Cloud Identity or Google Workspace account. Each user in the directory is associated with either the primary domain or one of the secondary domains. Two users, `johndoe@example.com` and `johndoe@secondary.example.com`, are considered separate users if `example.com` is the primary domain and `secondary.example.com` is a secondary domain.
  * **Alias domain** : An alias domain is an [alternate name for another domain](https://support.google.com/a/answer/175747#zippy=%2Ccan-i-add-a-user-alias-domain-to-a-secondary-domain%2Cwhat-is-a-user-alias-domain). That is, `johndoe@example.com` and `johndoe@alias.example.com` refer to the same user if `alias.example.com` is set up as an alias domain for `example.com`.



All domains must satisfy the following requirements:

  * They must be valid, global DNS domain names. During setup, you might need administrative access to the respective DNS zones in order to verify domain ownership.
  * A domain, such as `example.com`, can refer only to a single directory. However, you can use different subdomains, such as `subdomain.example.com`, to refer to different directories.
  * Primary and secondary domains should have a valid MX record so that messages sent to email addresses that are formed by using this domain name can be delivered properly.



### Usage of DNS domains in Microsoft Entra ID

The way Cloud Identity and Google Workspace uses DNS is similar to how Microsoft Entra ID relies on DNS to distinguish Microsoft Entra ID tenants and associate usernames with tenants. But be aware of two notable differences:

  1. **Initial domains:** When you create a Microsoft Entra ID tenant, the tenant is associated with an _initial domain_ , which is a subdomain of `onmicrosoft.com`. This domain is different from any [custom domain name](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-custom-domain) that you might register in that you don't own the domain and that you don't have administrative access to the respective DNS zone.

Cloud Identity doesn't have an equivalent of an initial domain and instead requires that you own all domains that you associate with a Cloud Identity account. This requirement means that you cannot register an `onmicrosoft.com` subdomain as a Cloud Identity domain.

  2. **Domains used in user identifiers:** Microsoft Entra ID distinguishes between email addresses MOERAs (Microsoft Online Email Routing Addresses) and UPNs. Both follow an RFC 822 format (`user@domain`), but they serve different purposes: Where UPNs are used to identify users and are used in the sign-on form, only MOERAs are used for delivering email.

The domain suffix used by UPNs is required to match one of the registered domains of your Microsoft Entra ID tenant—the same requirement does not apply to email addresses.

Cloud Identity and Google Workspace doesn't rely on the concept of a UPN and instead use a user's email address as an identifier. Consequently, the domain used by the email address must match one of the registered domains of the Cloud Identity or Google Workspace account.




A Microsoft Entra ID tenant and a Cloud Identity or Google Workspace account can use the same DNS domains. If using the same domains isn't possible, you can configure user provisioning and single sign-on to substitute domain names.

Considering the two differences outlined above, you should base your domain mapping on how you plan to map users between Microsoft Entra ID and Cloud Identity or Google Workspace.

## Map users

The third factor to look at when planning to federate Microsoft Entra ID and Google Cloud is how to map users between Microsoft Entra ID and Cloud Identity or Google Workspace.

Successfully mapping Microsoft Entra ID users to users in Cloud Identity or Google Workspace requires two pieces of information for each user:

  1. A stable, unique ID that you can use during synchronization to track which Microsoft Entra ID user corresponds to which user in Cloud Identity or Google Workspace.
  2. An email address for which the domain part corresponds to a Cloud Identity primary, secondary, or alias domain. Because this email address will be used throughout Google Cloud, the address should be human-readable.



Internally, Microsoft Entra ID identifies users by ObjectId, which is a randomly generated, globally unique ID. While this ID is stable and therefore meets the first requirement, it's meaningless to humans and doesn't follow the format of an email address. To map users, the only practical options are to map by UPN or by email address.

![Mapping users by email address.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-active-directory-google-sign-in.png)

If the user enters an email address that belongs to a Cloud Identity or Google Workspace account that is configured to use single sign-on with Microsoft Entra ID, the user is then redirected to the Microsoft Entra ID sign-on screen.

Microsoft Entra ID uses UPNs, not email addresses, to identify users, so the sign-on screen prompts the user to provide a UPN.

![Sign-on screen that prompts for a UPN.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-active-directory-upn-prompt.png)

If the Microsoft Entra ID tenant is configured to use AD FS for sign-on, another redirect takes the user to the AD FS sign-on screen. AD FS can identify users either by their Active Directory UPN or by their Pre–Windows 2000 logon name (`domain\user`).

![AD FS sign-on screen.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-active-directory-ad-fs.png)

If the email address used for Cloud Identity or Google Workspace, the UPN used by Microsoft Entra ID, and the UPN used by Active Directory all differ, the sequence of sign-on screens can easily become confusing for end users. In contrast, if all three identifiers are the same as in the example screenshots (`johndoe@example.com`), then users aren't exposed to the technical differences between UPNs and email addresses, minimizing potential confusion among your users.

### Map by UPN

From a user-experience perspective, mapping Microsoft Entra ID UPNs to Cloud Identity or Google Workspace email addresses might be considered the best option. Another benefit of relying on UPNs is that Microsoft Entra ID guarantees uniqueness so that you avoid the risk of naming clashes.

However, in order to map Microsoft Entra ID UPNs to Cloud Identity email addresses, you must meet these requirements:

  * The Microsoft Entra ID UPNs should be valid email addresses so that any notification emails sent by Google Cloud are correctly delivered to the user's mailbox. If this isn't the case already, you might be able to configure alias email addresses to ensure that the user receives such email.
  * The UPNs of all relevant users in Microsoft Entra ID must use a custom domain as suffix (`user@custom-domain`). UPNs that use the Microsoft Entra ID initial domain (`user@tenant.onmicrosoft.com`) cannot be mapped to email addresses in Cloud Identity, because the initial domain isn't owned by you, but by Microsoft.
  * All custom domains used by Microsoft Entra ID for UPNs must be registered in Cloud Identity as well. This requirement means that you must have access to the respective DNS zones in order to perform domain validation. To avoid overriding existing `TXT` DNS records you might have created for verifying domain ownership in Microsoft Entra ID, you can use a `CNAME` record to [verify domain ownership](https://support.google.com/a/topic/1409901) in Cloud Identity.



### Map users by email address

If mapping Microsoft Entra ID UPNs to Cloud Identity or Google Workspace email addresses isn't an option, you can map users by email address.

When you specify an email address in Active Directory, it's stored in the `mail` attribute of the respective `user` object and Microsoft Entra ID Connect will synchronize the value to the `Mail` attribute in Microsoft Entra ID. Microsoft Entra ID also makes the attribute available for user provisioning so that you can map it to the email address in Cloud Identity or cloudid_name_short.

Crucially, the Microsoft Entra ID `Mail` attribute currently isn't shown in the Azure portal and can only be viewed and edited through APIs or PowerShell. Although the user interface lets you specify an email address and an alternate email address, neither of these values is stored in the `Mail` attribute, so they can't be used for provisioning to Cloud Identity or cloudid_name_short. As a result, mapping users of an email address is practical only when you do most of your user creation and editing in Active Directory, not in Microsoft Entra ID.

Mapping users by email address requires that you meet the following additional requirements:

  * Email assignments must be complete. All users that are subject to synchronization must be assigned an email address. Especially when users are synchronized from an on-premises Active Directory, this might not be the case because `mail` is an optional user attribute in Active Directory. Users that lack an email address in the Microsoft Entra ID `Mail` attribute are silently ignored during synchronization.
  * Email addresses must be unique across the Microsoft Entra ID tenant. Although Active Directory doesn't check uniqueness on user creation, Microsoft Entra ID Connect detects collisions by default, which might cause the synchronization of affected users to fail.
  * The domains used by email addresses don't need to be registered in Microsoft Entra ID, but they must be registered in Cloud Identity or Google Workspace. This requirement means that you must have access to the respective DNS zones in order to perform domain validation, and it rules out the use of email addresses with domains that you don't own (like `gmail.com`).



### Map the user lifecycle

After you've defined a mapping between Microsoft Entra ID users and users in Cloud Identity or Google Workspace, you must decide which set of users you want to provision. Refer to our [best practices on mapping identity sets](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#mapping_identity_sets) for guidance on making this decision.

If you don't want to provision all users of your Microsoft Entra ID tenant, you can enable provisioning for a subset of users by using [user assignments](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configure_user_assignment) or [scoping filters](https://docs.microsoft.com/en-us/azure/active-directory/app-provisioning/define-conditional-rules-for-provisioning-user-accounts).

The following table summarizes the default behavior of Microsoft Entra ID provisioning, and shows how enabling or disabling provisioning for a user controls which actions Microsoft Entra ID will perform in Cloud Identity or Google Workspace.

Provisioning enabled for Microsoft Entra ID user | User state in Cloud Identity or Google Workspace | Action performed in Microsoft Entra ID | Action performed in Cloud Identity or Google Workspace  
---|---|---|---  
No | (does not exist) | Enable provisioning | Create new user (*)  
No | Exists (active) | Enable provisioning | Update existing user  
No | Exists (suspended) | Enable provisioning | Update existing user, keep suspended  
Yes | Exists | Modify user | Update existing user  
Yes | Exists | Rename UPN/email address | Change primary email address, keep previous address as alias  
Yes | Exists | Disable provisioning | Suspend user  
Yes | Exists | Soft-delete user | Suspend user  
  
_(*) If a consumer account with the same email address exists, the consumer account is[evicted](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts#consumer_accounts)._

## Map groups

The fourth factor to look at when you are planning to federate Microsoft Entra ID and Google Cloud is whether to synchronize groups between Microsoft Entra ID and Google Cloud and how to map them.

In Google Cloud, [groups](https://docs.cloud.google.com/iam/docs/overview#google_group) are commonly used as a way to manage access efficiently across projects. Rather than assigning individual users to IAM roles in each project, you define a set of groups that model common roles in your organization. You then assign those groups to a set of IAM roles. By modifying the membership of the groups, you can control users' access to an entire set of resources.

Mapping groups between Microsoft Entra ID and Google Cloud is optional. Once you've set up user provisioning, you can create and manage groups directly in Cloud Identity or Google Workspace, which means that Active Directory or Microsoft Entra ID remains the central system for identity management but not for Google Cloud access management.

To maintain Active Directory or Microsoft Entra ID as the central system for identity management and access management, we recommend that you synchronize groups from Microsoft Entra ID instead of managing them in Cloud Identity or Google Workspace. With this approach, you can set up IAM so that you can use group memberships in Active Directory or Microsoft Entra ID to control who has access to resources in Google Cloud.

### Groups in Cloud Identity and Google Workspace

In Cloud Identity and Google Workspace, there is only a single type of group. Groups in Cloud Identity and Google Workspace aren't confined to the scope of the Cloud Identity or Google Workspace account where they were defined. Instead, they can include users from different Cloud Identity or Google Workspace accounts, support being referenced and nested in other accounts, and be used across any Google Cloud organization.

As they do with users, Cloud Identity and Google Workspace identify groups by email address. The email address doesn't have to correspond to an actual mailbox, but it must use one of the domains registered for the respective Cloud Identity account.

When working with groups in IAM, you often need to specify groups by email address rather than by name. So it's best for groups to have not only a meaningful name, but a meaningful and recognizable email address.

### Groups in Microsoft Entra ID

Microsoft Entra ID supports [multiple types of groups](https://docs.microsoft.com/en-us/office365/admin/create-groups/compare-groups?view=o365-worldwide), each catering to different use cases. Groups are scoped to a single tenant and identified by an Object ID, which is a randomly generated, globally unique ID. Groups can be nested and can contain either users from the same tenant or users invited from other tenants by using B2B collaboration. Entra ID also supports dynamic groups, whose members are determined automatically based on a query.

In the context of integrating Microsoft Entra ID with Cloud Identity or Google Workspace, two properties of groups are of primary interest—whether a group is mail-enabled and whether it is security-enabled:

  * A **security-enabled** group can be used to manage access to resources in Microsoft Entra ID. Any security-enabled group is therefore potentially relevant in the context of Google Cloud.
  * A **mail-enabled** group has an email address, which is relevant because Cloud Identity and Google Workspace require groups to be identified by an email address.



In Microsoft Entra ID, you can create groups of type Security or Office 365 (sometimes called unified groups). When synchronizing groups from an on-premises Active Directory or when using the Office 365 type, you can also create groups of type Distribution list.

The following table summarizes the differences between these different kinds of groups regarding being mail-enabled or security-enabled, and how they map to Active Directory group types, assuming a default Microsoft Entra ID Connect configuration:

Source | Active Directory group type | Microsoft Entra ID group type | Mail-enabled | Security-enabled  
---|---|---|---|---  
Microsoft Entra ID | - | Office 365 group | Always | Optional  
Microsoft Entra ID | - | Security group | Optional | Always  
on-premises | Security group (with email) | Security group | Yes | Yes  
on-premises | Security group (without email) | Security group | No | Yes  
on-premises | Distribution list (with email) | Distribution list | Yes | No  
on-premises | Distribution list (without email) | _(ignored by Microsoft Entra ID Connect)_ |  |   
  
Unlike for users, Microsoft Entra ID requires that email addresses assigned to groups use a domain that has been registered as a custom domain in Microsoft Entra ID. This requirement results in the following default behavior:

  * If a group in Active Directory uses an email address that uses a domain that has previously been registered in Microsoft Entra ID, then the email address is properly maintained during synchronization to Microsoft Entra ID.
  * If a group in Active Directory uses an email address that has not been registered in Microsoft Entra ID, then Microsoft Entra ID auto-generates a new email address during synchronization. This email address uses the tenant's default domain. If your tenant uses the initial domain as the default domain, the resulting email address will be in the form of `[name]@[tenant].onmicrosoft.com`.
  * If you create an Office 365 group in Microsoft Entra ID, then Microsoft Entra ID also auto-generates an email address that uses the tenant's default domain.



### Map group identities

Successfully mapping Microsoft Entra ID groups to Cloud Identity or Google Workspace groups requires a common identifier, and this identifier must be an email address. On the Microsoft Entra ID side, this requirement leaves you with two options:

  * You can use the email address of a group in Microsoft Entra ID and map it to a Cloud Identity or Google Workspace email address.
  * You can derive an email address from the name of the group in Microsoft Entra ID and map the resulting address to an email address in Cloud Identity or Google Workspace.



#### Map by email address

Mapping groups by email address is the most obvious choice, yet it requires you to meet several requirements:

  * All groups that are subject to synchronization must have an email address. In practice, this means that you can only synchronize mail-enabled groups. Groups that lack an email address are ignored during provisioning.
  * The email addresses must be unique across the tenant. Because Microsoft Entra ID doesn't enforce uniqueness, you might have to implement custom checks or policies.
  * The domains used by email addresses must be registered in both Microsoft Entra ID and Cloud Identity or Google Workspace. Any groups with email addresses that use domains not registered in Cloud Identity or Google Workspace, including the `tenant.onmicrosoft.com` domain, will fail to synchronize.



If all relevant groups meet these criteria, identify the domains that are used by these email addresses and ensure that the list of DNS domains registered in Cloud Identity or Google Workspace covers these domains.

#### Map by name

Meeting the criteria required to map groups by email address can be challenging, particularly if many of the security groups you intend to provision to Cloud Identity or Google Workspace aren't mail-enabled. In this case, it might be better to automatically derive an email address from the group's display name.

Deriving an email address presents two challenges:

  1. An email address derived from a group's name might clash with an email address of a user.
  2. Microsoft Entra ID doesn't enforce uniqueness for group names. If multiple groups in your Microsoft Entra ID tenant share the same name, email addresses derived from this name will clash, causing only one group to synchronize successfully.



You can overcome the first challenge by using a domain for the generated email address that is different than any of the domains used by users. For example, if all your users use email addresses with `example.com` as the domain, then you could use `groups.example.com` for all groups. Registering subdomains in Cloud Identity or Google Workspace doesn't require domain verification, so the DNS zone `groups.example.com` doesn't even have to exist.

You can overcome the second challenge, duplicate group names, only technically by deriving the group email address from the Object ID. Because the resulting group names are rather cryptic and difficult to work with, it's better to identify and rename duplicate group names in Microsoft Entra ID before setting up provisioning to Cloud Identity or Google Workspace.

### Map the group lifecycle

After you've defined a mapping between Microsoft Entra ID groups and groups in Cloud Identity or Google Workspace, you must decide which set of groups you want to provision. Similar to users, you can enable provisioning for a subset of groups by using [group assignments](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configure_user_assignment) or [scoping filters](https://docs.microsoft.com/en-us/azure/active-directory/app-provisioning/define-conditional-rules-for-provisioning-user-accounts).

The following table summarizes the default behavior of Microsoft Entra ID provisioning, and shows how enabling or disabling provisioning for a group controls which actions Microsoft Entra ID will perform in Cloud Identity or Google Workspace.

Provisioning enabled for Microsoft Entra ID group | Group state in Cloud Identity or Google Workspace | Action performed in Microsoft Entra ID | Action performed in Cloud Identity or Google Workspace  
---|---|---|---  
No | (does not exist) | Enable provisioning | Create new group  
No | Exists | Enable provisioning | Add member, retain all existing members   
Yes | Exists | Rename group | Rename group  
Yes | Exists | Modify description | Update description  
Yes | Exists | Add member | Add member, retain all existing members  
Yes | Exists | Remove member | Remove member  
Yes | Exists | Disable provisioning | Group left as-is (incl. members)  
Yes | Exists | Delete group | Group left as-is (incl. members)  
**Note:** When you delete a group in Microsoft Entra ID, Microsoft Entra ID doesn't propagate the deletion to Cloud Identity or Google Workspace. Similarly, if you enable provisioning for a group and later disable provisioning, the group in Cloud Identity or Google Workspace remains active. This behavior can result in users inadvertently retaining access rights in Google Cloud. To prevent this from happening, remove all members from a group first, wait for changes to be propagated, and only then delete the group in Microsoft Entra ID or disable provisioning for the group in Microsoft Entra ID.

## What's next

  * Read about [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Learn how to [configure provisioning and single sign-on between Microsoft Entra ID and Cloud Identity](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on).
  * Learn about [best practices for managing super administrator accounts](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
