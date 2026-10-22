---
url: https://docs.cloud.google.com/architecture/identity/best-practices-for-planning/
title: Best practices for planning accounts and organizations \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:28.618617+00:00
---

# Best practices for planning accounts and organizations  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/best-practices-for-planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Best practices for planning accounts and organizations Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

This document presents best practices for deciding how many [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://workspace.google.com/) accounts, Google Cloud organizations, and billing accounts you need to use. The document provides guidance on identifying a design that satisfies your security and organizational requirements.

In Google Cloud, identity and access management is based on two pillars:

  * Cloud Identity and Google Workspace accounts are containers for users and groups. These accounts are therefore key to authenticating your corporate users and managing access to your Google Cloud resources. A Cloud Identity or Google Workspace account denotes a directory of users, not an individual user account. Individual user accounts are referred to as _users_ or _user accounts_.

  * [Organizations](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) are containers for projects and resources within Google Cloud. Organizations allow resources to be structured hierarchically and are key to centrally and efficiently managing resources.




This document is intended primarily for customers who are setting up enterprise environments.

## Cloud Identity and Google Workspace accounts

Google Workspace is an integrated suite of cloud-native collaboration and productivity apps. It includes tools that let you manage users, groups, and authentication.

Cloud Identity provides a subset of the Google Workspace features. Like Google Workspace, Cloud Identity lets you manage users, groups, and authentication, but it doesn't include all of Google Workspace's collaboration and productivity features.

Cloud Identity and Google Workspace share a common technical platform and use the same set of APIs and administrative tools. The products share the concept of an account as a container for users and groups. This container is identified by a domain name such as `example.com`. For managing users, groups, and authentication, the two products can be considered equivalent.

### Combine Cloud Identity and Google Workspace in a single account

Because Cloud Identity and Google Workspace share a common platform, you can combine access to the products in a single account.

If you already administer a Google Workspace account and want to enable more users to use Google Cloud, you might not want to assign all users a Google Workspace license. In this case, [add Cloud Identity Free to your existing account](https://support.google.com/cloudidentity/answer/7384506). You can then onboard more users without additional charge and decide which users should have access to Google Workspace by [assigning them a Google Workspace license](https://support.google.com/a/answer/1727173).

Similarly, if you already administer a Cloud Identity Free or Premium account, you might want to grant certain users the right to use Google Workspace. Rather than creating separate Google Workspace accounts for those users, you can [add Google Workspace to an existing Cloud Identity account](https://admin.google.com/ac/billing/catalog). After you've assigned the Google Workspace license to those selected users, they can use the productivity and collaboration apps.

### Use as few accounts as possible, but as many as necessary

To let your users collaborate by using Google Workspace, and to minimize administrative overhead, it's best to manage all users through a single Cloud Identity or Google Workspace account and provide a single user account to each individual. This approach helps ensure that settings such as [password policies](https://support.google.com/a/answer/139399), single sign-on, and [two-step verification](https://support.google.com/a/answer/175197) are consistently applied to all users.

Despite these benefits of using a single Cloud Identity or Google Workspace account, you can gain flexibility and administrative autonomy by using multiple accounts. When you are deciding how many Cloud Identity or Google Workspace accounts to use, consider all requirements that suggest using multiple accounts. Then use the smallest number of Cloud Identity or Google Workspace accounts that satisfies your requirements.

### Use separate accounts for staging and production

For most settings that you can configure in Cloud Identity and Google Workspace, you can choose the scope at which each setting should apply—for example, you can specify the [geographic location for your data](https://support.google.com/a/answer/7630496) by user, by group, or by organizational unit. When you plan to apply a new configuration, you can initially choose a small scope (for example, by user) and verify whether the configuration meets your expectations. When you've verified the configuration, you can then apply the same setting to a larger set of groups or organizational units.

Unlike most settings, integrating a Cloud Identity or Google Workspace account with an external identity provider (IdP) has a global impact:

  * [Enabling single sign-on](https://support.google.com/a/answer/60224) is a global setting that applies to all users other than super admins.
  * Depending on your external IdP, setting up user provisioning can also have global impact. An accidental misconfiguration in the external IdP might lead to users inadvertently being modified, suspended, or even deleted.



To mitigate these risks, have separate staging and production Cloud Identity or Google Workspace accounts:

  * Use the staging account to verify any risky configuration changes before applying the same change to your production account.
  * Create a few test users in the staging accounts that you and other administrators can use to verify configuration changes. But don't grant your users access to the staging account.



If you have separate staging and production instances of your external IdP, take these steps:

  * Integrate your staging Cloud Identity or Google Workspace account with your staging IdP instance.
  * Integrate your production Cloud Identity or Google Workspace account with your production IdP instance.



For example, suppose you plan to [set up federation with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory) and have a separate Active Directory forest for testing purposes. In this case, you integrate your staging Cloud Identity or Google Workspace account with the staging forest and the production Cloud Identity or Google Workspace account with your main forest. Apply the same mapping approach for [DNS domains](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction#mapping_dns_domains), [users](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction#mapping_user_accounts), and [groups](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction#mapping_groups) to both forest/account pairs, as shown in the following diagram:

![Active Directory mapping approach for DNS domains, users, and groups.](https://docs.cloud.google.com/static/architecture/identity/images/ad-mapping-dns-domains-users-groups.svg)

Your production and staging Active Directory forests and domains might use DNS domains that don't let you apply the same domain mapping approach for staging and production. In this case, consider registering more User Principal Name (UPN) suffix domains in your staging forest.

Similarly, if you plan to [set up federation with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory), it's best to take the following approach:

  * Integrate the staging Cloud Identity or Google Workspace account with a staging Entra ID tenant.
  * Integrate the production Cloud Identity or Google Workspace account with your main Entra ID tenant.



Apply the same mapping approach for [DNS domains](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_dns_domains), [users](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_user_accounts), and [groups](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_groups) to both tenant/account pairs:

![Entra ID mapping approach for DNS domains, users, and groups.](https://docs.cloud.google.com/static/architecture/identity/images/aad-mapping-dns-domains-users-groups.svg)

Your production and staging Entra ID tenants might use DNS domains that don't let you apply the same domain mapping approach for staging and production. In this case, consider adding an extra domain to your staging tenant.

### Use disjoint DNS domains among Cloud Identity and Google Workspace accounts

When you first add a domain such as `example.com` to your Cloud Identity or Google Workspace account, you need to [verify that you own the domain](https://support.google.com/a/answer/60216). After you have added and verified a domain, you can add subdomains such as `marketing.example.com` and `finance.example.com` without having to verify each subdomain individually.

However, if you add subdomains without verifying each one, conflicts can result if you have another Cloud Identity or Google Workspace account that already uses this subdomain. To avoid these conflicts, prefer using disjoint domains for each account. For example, if you need two Cloud Identity or Google Workspace accounts, try to avoid using two domains where one domain is a subdomain of the other. Instead, use two domains that are not subdomains of another. This practice applies to the primary domain and to [secondary domains](https://support.google.com/a/answer/7502379).

### Don't separate Google Workspace and Google Cloud

If you already use Google Workspace, some users in your Google Workspace account might have been granted [super admin privileges](https://support.google.com/a/answer/2405986) so that they can carry out administrative tasks.

Users with super admin privileges are implicitly granted permission to modify the Identity and Access Management (IAM) policy of the organization node. This permission enables super admins to assign themselves the [organization administrators role](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#adding_an_organization_admin) or any other role in the Google Cloud organization. Having super admin access to a Cloud Identity or Google Workspace account also enables a user to delete the account, its associated Google Cloud organization, and all its resources. You therefore have to assume that super admins have full access to all resources within an organization.

The fact that super admins are also organization administrators might be a security concern if your existing Google Workspace administrators are a different set of users from the users who will be in charge of managing your Google Cloud organization. In this case, you might decide to create a separate Cloud Identity account that is dedicated to Google Cloud in order to limit the access of Google Workspace super admins to Google Cloud resources. Separating Google Workspace and Google Cloud can have several unintended consequences.

For example, you might try creating separate users in the Cloud Identity account and then [restricting access to the Google Cloud organization users to the Cloud Identity account](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains). This would ensure that your Google Cloud deployment and Google Workspace are fully isolated. However, duplicating users negatively affects both user experience and administrative overhead. Additionally, you wouldn't be able to receive any notification emails sent by Google Cloud because the domain used by Cloud Identity must be different from the domain used for Google Workspace and is therefore unsuitable for routing email.

If you instead reference users from the Google Workspace account in your Google Cloud organization, you undermine the isolation between Google Workspace and Google Cloud:

![Referencing users from the Google Workspace account in your Google Cloud organization.](https://docs.cloud.google.com/static/architecture/identity/images/referencing-users-from-g-suite-account.svg)

Google Workspace super admins have the ability to use [domain-wide delegation](https://developers.google.com/admin-sdk/reports/v1/guides/delegation) to impersonate any user in the same Google Workspace account. A rogue super admin could use their elevated privileges to regain access to Google Cloud.

A more effective approach than using separate accounts is to segregate responsibilities between Google Workspace and Google Cloud administrators to reduce the number of super admins:

  * Most administrative duties in Google Workspace don't require super admin privileges. Use [pre-built administrative roles](https://support.google.com/a/answer/2405986) or [custom administrator roles](https://support.google.com/a/answer/2406043) in place of super admin privileges to grant Google Workspace administrators the permissions necessary to conduct their duties.

  * Retain only a minimal number of super-admin users and [discourage everyday usage](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices#discourage_super_admin_account_usage).

  * Take advantage of auditing to detect suspicious activity among administrative users.




### Secure your external IdP when using single sign-on

Cloud Identity and Google Workspace let you [set up single sign-on](https://support.google.com/a/answer/60224) with your external IdP such as Active Directory, Entra ID, or Okta (to name a few). If single sign-on is enabled, Cloud Identity and Google Workspace trust the external IdP to authenticate users on Google's behalf.

Enabling single sign-on offers several advantages:

  * Users can use their existing credentials to sign on to Google services.
  * Users don't need to enter their passwords again if they already have an existing sign-on session.
  * You can apply consistent multi-factor authentication policies across your applications and all Google services.



But enabling single sign-on also exposes you to risks. When single sign-on is enabled and a user needs to be authenticated, Cloud Identity or Google Workspace redirects the user to your external IdP. After authenticating the user, the IdP returns to Google a SAML assertion that states the user's identity. The SAML assertion is signed. Therefore, Google can verify the authenticity of the SAML assertion and verify that the correct identity provider has been used. However, there is no way for Cloud Identity or Google Workspace to verify that the IdP made the right authentication decision and correctly stated the user's identity.

If single sign-on is enabled, the overall security and integrity of your Google deployment hinges on the security and integrity of your IdP. Your Cloud Identity or Google Workspace account and all resources that rely on the users managed by the account are at risk if any of the following are configured insecurely:

  * The IdP itself
  * The machines that the provider is running on
  * The user database that the provider is getting user information from
  * Any other system that the provider depends on



To prevent single sign-on from becoming a weak link in your security posture, ensure that your IdP and all systems it depends on are configured securely:

  * Limit the number of users with administrative access to your IdP or to any of the systems that the provider relies on.
  * Don't grant any user administrative access to these systems to whom you wouldn't also give super admin privileges in Cloud Identity or Google Workspace.
  * Don't use single sign-on if you are unsure about the security controls in place for your external IdP.



### Secure access to your DNS zones

Cloud Identity and Google Workspace accounts are identified by a primary DNS domain name. When you create a new Cloud Identity or Google Workspace account, you must [verify ownership](https://support.google.com/a/answer/60216) of the DNS domain by creating a special DNS record in the corresponding DNS zone.

The importance of DNS and the impact on the overall security of your Google deployment extends beyond the sign-up process:

  * Google Workspace relies on [DNS MX records](https://support.google.com/a/answer/140034) for routing emails. By modifying these MX records, an attacker might be able to route emails to a different server and gain access to sensitive information.

  * If an attacker is able to add records to the DNS zone, they might then be able to reset the password of a super admin user and gain access to the account.




To prevent DNS from becoming a weak link in your security posture, ensure that your DNS server is configured securely:

  * Limit the number of users that have administrative access to the DNS server that manages the primary domain used for Cloud Identity or Google Workspace.

  * Don't grant any user administrative access to your DNS server to whom you wouldn't also give super admin privileges in Cloud Identity or Google Workspace.

  * If you plan to deploy a workload on Google Cloud that has security requirements that aren't met by your existing DNS infrastructure, consider registering for that workload a new DNS domain that uses separate DNS servers or a managed DNS service.




### Export audit logs to BigQuery

Cloud Identity and Google Workspace maintain multiple audit logs to keep track of configuration changes and other activities that might be relevant to the security of your Cloud Identity or Google Workspace account. The following table summarizes these audit logs.

Log | Activities captured  
---|---  
[Admin](https://support.google.com/a/answer/4579579) | Actions performed in your Google Admin Console  
[Login](https://support.google.com/a/answer/4580120) | Successful, unsuccessful, and suspicious sign-in attempts to your domain  
[Token ](https://support.google.com/a/answer/6124308) | Instances of authorizing or revoking access to third-party mobile or web applications  
[Groups](https://support.google.com/a/answer/6270454) | Changes to groups and group memberships  
  
You can access these audit logs either through the [Admin Console](https://admin.google.com/ac/reporting/home) or through the [Reports API](https://developers.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/admin-event-names). For most audit logs, data is [retained for 6 months](https://support.google.com/a/answer/7061566).

If you are operating in a regulated industry, retaining audit data for 6 months might not be sufficient. To retain data for a longer period of time, [configure audit logs to be exported to BigQuery](https://support.google.com/a/answer/9079364).

To limit the risk of unauthorized access to the exported audit logs, use a dedicated Google Cloud project for the BigQuery dataset. To keep the audit data safe from tampering or deletion, grant access to the project and dataset on a least-privilege basis.

**Note:** Super admins are allowed to grant themselves any role within the Google Cloud organization, which means you can't prevent them from being able to modify or delete audit logs.

The Cloud Identity and Google Workspace audit logs are complementary to [Cloud Audit Logs logs](https://docs.cloud.google.com/logging/docs/audit). If you also use BigQuery to collect Cloud Audit Logs logs and other application-specific audit logs, you can correlate login events to activities that a user has performed in Google Cloud or in your applications. Being able to correlate audit data across multiple sources can help you detect and analyze suspicious activity.

[Setting up BigQuery exporting](https://support.google.com/a/answer/9082756) requires a Google Workspace Enterprise license. After you set up the main audit logs, these are exported for all users, including those users without a Google Workspace license. Certain logs such as the Drive and Mobile audit logs are exported for users that have at least a Google Workspace Business license.

If you use Cloud Identity Free for the majority of your users, you can still export to BigQuery by [adding Google Workspace Enterprise to your existing Cloud Identity account](https://admin.google.com/ac/billing/catalog) and purchasing Google Workspace licenses for a selected set of administrators.

## Organizations

Organizations let you organize resources [into a hierarchy of projects and folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail), with the organization node being the root. Organizations are associated with a Cloud Identity or Google Workspace account, and they derive their name from the primary domain name of the associated account. An organization is created automatically when a user from the Cloud Identity or Google Workspace account creates a first project.

Each Cloud Identity or Google Workspace account can have only a single organization. In fact, it's not possible to create an organization without a corresponding account. Despite this dependency, you can [grant users](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) from multiple different accounts access to resources in a single organization:

![Grant users from multiple accounts access to resources.](https://docs.cloud.google.com/static/architecture/identity/images/grant-access-multiple-accounts.svg)

The flexibility to reference users from different Cloud Identity or Google Workspace accounts lets you separate how you treat accounts and organizations. You can separate the decision of how many Cloud Identity or Google Workspace accounts you need in order to manage your users from the decision of how many organizations you need in order to manage your resources.

The number of organizations that you create and their purposes can profoundly impact your security posture, the autonomy of your teams and departments, and the consistency and efficiency of your administration.

The following sections describe best practices for deciding how many organizations to use.

### Use as few organizations as possible, but as many as necessary

The resource hierarchy of an organization lets you reduce the effort of managing IAM policies and organizational policies by taking advantage of inheritance. By configuring policies at the folder or organization level, you ensure that policies are applied consistently across a sub-hierarchy of resources, and you avoid repetitive configuration work. To minimize your administrative overhead, it's [best to use as few organizations as possible](https://docs.cloud.google.com/resource-manager/docs/managing-multiple-orgs#effects_of_using_multiple_organization_nodes).

In contrast, you can gain additional flexibility and administrative autonomy by using multiple organizations. The following sections describe when you might require such additional flexibility or autonomy.

In any case, when you are deciding how many organizations to use, consider all requirements that suggest using multiple organizations. Then use the smallest number of organizations that satisfies your requirements.

### Use organizations to delineate administrative authority

Within a resource hierarchy, you can grant permissions at the resource, project, or folder level. The ultimate level at which you can grant a user permissions is the organization.

A user who has been assigned the Organization Administrator role at the organization level has full control over the organization, its resources, and its IAM policies. An Organization Administrator can take control of any resource within the organization and is free to delegate administrative access to any other user.

However, the capabilities of an Organization Administrator are confined to the organization, making the organization the ultimate scope of administrative authority:

  * An Organization Administrator cannot access any resources in other organizations unless explicitly granted permission.
  * No user outside the organization can take control away from an Organization Administrator of that organization.



The right number of organizations to use depends on the number of independent groups of administrative users in your company:

  * If your company is organized by function, you might have a single department that's in charge of overseeing all Google Cloud deployments.
  * If your company is organized by division or owns a number of autonomously-run subsidiaries, then there might not be a single department that's in charge.



If a single department is in charge of overseeing Google Cloud deployments, it's best to use a single Google Cloud organization node. Within the organization, use folders to structure resources and grant different levels of access to other teams and departments.

If you are dealing with multiple independent departments, trying to centralize administration by using a single organization might cause friction:

  * If you designate a single department to manage the organization, you might face resistance from other departments.
  * If you let multiple teams or departments co-own a single organization, it might be difficult to maintain a consistent resource hierarchy and to ensure that IAM policies and organizational policies are used consistently across your resources.



To prevent this kind of friction, use multiple organizations and create separate folder structures in each organization. By using separate organizations, you establish boundaries between different groups of administrative users, thus delineating their administrative authority.

### Use a separate staging organization

To help ensure consistency and avoid repetitive configuration work, organize your projects into a hierarchy of folders and apply IAM policies and organizational policies at the folder or organization level.

There is a downside of having policies that apply to many projects and resources. Any change to the policy itself or the resource hierarchy the policy applies to might have far-reaching and unintended consequences. To mitigate this risk, it's best to test policy changes before you apply them in your main organization.

We recommend that you create a separate staging organization. This organization helps you test resource hierarchy changes, IAM policies, organizational policies, or other configuration that have potential organization-wide impact such as [access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) and [policies](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy).

To ensure that the results of tests or experiments conducted in the staging organization also apply to the production organization, configure the staging organization to use the same folder structure as your main organization, but with only a small number of projects. At any point, the IAM and organizational policies in the staging organization should either match the policies of your production organization or should reflect the next version of policies that you intend to apply to your production organization.

As the following diagram shows, you use your staging Cloud Identity or Google Workspace account as a basis for the staging organization. You use the staging account (or the external IdP that your staging account is integrated with) to create dedicated test users and a group structure that mirrors the groups you use in your production Cloud Identity or Google Workspace account. You can then use these dedicated test users and groups to test IAM policies without impacting existing users.

![Using your account as a basis for staging.](https://docs.cloud.google.com/static/architecture/identity/images/your-account-as-basis-for-staging.svg)

### Avoid using a separate testing organization

For each production workload that you plan to deploy on Google Cloud, you probably need one or more testing environments, which your development and DevOps teams can use to validate new releases.

From a security perspective, to prevent untested releases from accidentally impacting production workloads, you want to cleanly separate your test environments from your production environments. Similarly, the two types of environments have different requirements for IAM policies. For example, in order for you to grant developers and testers the flexibility they need, the security requirements for your testing environments might be substantially looser than those of your production environments.

As the following diagram shows, from a configuration perspective you want to keep your test environments as similar to your production environments as possible. Any divergence increases the risk that a deployment that worked properly in a test environment fails when deployed to a production environment.

![Keeping test environments similar to production environments.](https://docs.cloud.google.com/static/architecture/identity/images/stage-production-similarity.svg)

To strike a balance between keeping environments isolated and consistent, use folders within the same organization to manage testing and production environments:

  * Apply any IAM policies or organizational policies that are common across environments at the organizational level (or by using a common parent folder).
  * Use the individual folders to manage IAM policies and organization policies that differ between different types of environments.



Don't use your staging organization for managing testing environments. Testing environments are critical to the productivity of development and DevOps teams. Managing such environments in your staging environment would restrict your ability to use the staging organization to experiment with and test policy changes; any such change might disrupt the work of these teams. In short, if you use a staging organization to manage testing environments, you undermine the purpose of your staging organization.

### Use a separate organization for experimenting

To get the most out of Google Cloud, let your development, DevOps, and operations teams familiarize themselves with the platform and expand their experience by running [tutorials](https://docs.cloud.google.com/architecture). Encourage them to experiment with [new features and services](https://cloud.google.com/blog).

Use a separate organization as the sandbox environment to support these types of experimental activities. By using a separate organization, you can keep experiments unencumbered by any policies, configuration, or automation that you use in your production organization.

Avoid using your staging organization for experimenting. Your staging environment should use IAM and organization policies that are similar to your production organization. Therefore, the staging environment is likely to be subject to the same limitations as your production environment. At the same time, relaxing policies in order to allow experiments would undermine the purpose of your staging organization.

To prevent your experimental organization from becoming disorganized, from generating excessive cost, or from becoming a security risk, issue guidelines that define how teams are allowed to use the organization, and who bears responsibility for maintaining the organization. Additionally, consider setting up automation to automatically delete resources, or even entire projects, after a certain number of days.

As the following diagram shows, when you create an organization for experimenting, you first create a dedicated Cloud Identity account. You then use the existing users from your main Cloud Identity or Google Workspace account to grant users access to the experimental organization.

![Experiment organization.](https://docs.cloud.google.com/static/architecture/identity/images/experiment-organization.svg)

To manage the additional Cloud Identity account, you need at least one super admin user account in the Cloud Identity account. For information about how to secure these super-admin user accounts, see [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices).

### Use domain-restricted sharing to enforce trust relationships

IAM policies let you add any valid Google identity as a member. This means that when you edit the IAM policy of a resource, project, folder, or organization, you can add members from different sources, including the following:

  * Users from the Cloud Identity or Google Workspace account that the organization is associated with, as well as service accounts from the same organization
  * Users from other Cloud Identity or Google Workspace accounts
  * Service accounts from other organizations
  * Consumer user accounts, including `gmail.com` users and consumer accounts that use a corporate email address



Being able to reference users from different sources is useful for scenarios and projects where you need to collaborate with affiliates or other companies. In most other cases, it's best to constrain IAM policies to only allow members from trusted sources.

Use [domain-restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) to define a set of trusted Cloud Identity or Google Workspace accounts from which you want to allow members to be added to IAM policies. Define this organizational policy either at the organization level (so that it applies to all projects) or at a folder near the top of the resource hierarchy (to allow certain projects to be exempted).

If you use separate Cloud Identity or Google Workspace accounts and organizations to segregate staging, production, and experimenting environments, use domain-restricted sharing policies to enforce the segregation as listed in the following table:

Organization | Trusted Cloud Identity or Google Workspace account  
---|---  
Staging | Staging  
Production | Production  
Experiments | Production  
  
### Use neutral domain names for organizations

Organizations are identified by a DNS domain name such as `example.com`. The domain name is derived from the primary domain name of the associated Cloud Identity or Google Workspace account.

If there is a canonical DNS domain name that is used throughout your company, use that domain as primary domain in your production Cloud Identity or Google Workspace account. By using the canonical DNS name, you ensure that employees can easily recognize the name of the organization node.

If your company has several subsidiaries or owns a variety of different brands, there might not be a canonical domain name. Rather than arbitrarily picking one of the existing domains, consider registering a new DNS domain that is neutral and dedicated for use by Google Cloud. By using a neutral DNS name, you avoid expressing a preference for a specific brand, subsidiary, or department within your company, which could negatively affect cloud adoption. Add your other, brand-specific domains as [secondary domains](https://support.google.com/a/answer/7502379) so that they can be used in user IDs and for single sign-on.

### Use billing accounts across Google Cloud organizations

Billing accounts define [who pays for a given set of Google Cloud resources](https://docs.cloud.google.com/billing/docs/concepts#overview). Although billing accounts can exist outside of a Google Cloud organization, they are most commonly associated with an organization.

When billing accounts are associated with an organization, they are considered a sub-resource of the organization and are subject to IAM policies defined within the organization. Most importantly, this means that you can use the [Billing IAM roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access) to define which users or groups are allowed to administer or use an account.

A user who has been granted the `Billing Account User` role can link a project to a billing account, causing the resources to be billed to this account. Linking a project to a billing account works within the same organization, but also across organizations.

If you use multiple organizations, you can take advantage of the fact that billing accounts can be used across organizations. This lets you decide how many billing accounts you need independent of how many organizations you need.

The right number of billing accounts depends exclusively on your [commercial or contractual requirements](https://docs.cloud.google.com/billing/docs/concepts#billing_account) such as currency, payment profile, and the number of separate invoices you need. As you did with accounts and organizations, in order to minimize complexity, you want to use the smallest number of billing accounts that satisfies your requirements.

To break down costs accrued across multiple organizations, configure your billing account to [export billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). Each record exported to BigQuery not only contains the project name and ID, but also the ID of the organization the project is associated with (in the `project.ancestry_numbers` field).

## What's next

  * [Create a new Cloud Identity account](https://gsuite.google.com/signup/gcpidentity/welcome)
  * Learn how Google Cloud lets you [authenticate corporate users in a hybrid environment](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment) and [common patterns](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment).
  * Review the [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Find out how to [federate Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction) or [Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
