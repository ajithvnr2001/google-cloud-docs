---
url: https://docs.cloud.google.com/iam/docs/best-practices-workforce-identity-federation/
title: Best practices for using Workforce Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:04.269012+00:00
---

# Best practices for using Workforce Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/best-practices-workforce-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Best practices for using Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

Workforce Identity Federation federates your Google Cloud organization with an external identity provider (IdP) to enable single sign-on (SSO).

You can apply these best practices to use Workforce Identity Federation effectively and minimize security risks.

## Choose the right architecture

The following sections describe key factors for choosing a federation architecture that matches your requirements.

**Architectural considerations** :

Choose a federation architecture pattern.  
Partition federation usage by service, not by user.  


### Choose a federation architecture pattern

The following four patterns describe common ways to federate a Google Cloud organization with an external IdP:

  * [Cloud Identity federation](https://docs.cloud.google.com/iam/docs/federated-identity-architectures#cloud-identity-fed)
  * [Workforce Identity Federation, sync-less](https://docs.cloud.google.com/iam/docs/federated-identity-architectures#sync-less-fed)
  * [Workforce Identity Federation with System for Cross-domain Identity Management (SCIM)](https://docs.cloud.google.com/iam/docs/federated-identity-architectures#scim-fed)
  * [Hybrid Cloud Identity and Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-architectures#hybrid-fed)



Before federating, consider the advantages and limitations of each pattern and choose the one that matches your requirements. For more information, see the [Architecture patterns for identity federation](https://docs.cloud.google.com/iam/docs/federated-identity-architectures).

**Note:** For best practices about using Cloud Identity or Google Workspace for federation, see the [reference architectures guide](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp) and [federation best practices](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

### Partition federation usage by service

In general, we recommend that you partition federation usage by service, rather than by user. Partitioning usage by service has fewer disadvantages overall.

To reduce complexity, we recommend using either Cloud Identity or Workforce Identity Federation. However, depending on your requirements, you might need both in parallel as described in the [hybrid pattern](https://docs.cloud.google.com/iam/docs/federated-identity-architectures#hybrid-fed).

If you use Cloud Identity federation and Workforce Identity Federation in parallel, you can partition their usage in the following ways:

  * **Partition by user** : Partition your users into two cohorts: one using Workforce Identity Federation and one using Cloud Identity federation.

    * _Advantage_ : Each user has a single identity across Google services and one sign-in method.
    * _Disadvantages_ : Partitioning by users has several disadvantages, including the following:

      * Managing access groups can be complex because IAM allow policies need to contain a combination of principal types and you can't use the same groups for Cloud Identity and Workforce Identity Federation users.

      * Users from different cohorts can't share links with each other because the Google Cloud console, Gemini Enterprise, and other tools use different URLs depending on how users sign in.

      * Users from different cohorts might have access to different feature sets.

  * **Partition by service** : Configure each service, such as Google Cloud or Gemini Enterprise, so that it exclusively grants access to Workforce Identity Federation users or Cloud Identity users, but never both.

    * _Advantage_ : Simplifies administration and ensures a consistent feature set across different users.
    * _Disadvantage_ : Some employees might need to be assigned two identities—one that uses Workforce Identity Federation and one that uses Cloud Identity.



We recommend partitioning by service, specifically separating Gemini Enterprise and Gemini Notebook Enterprise from other services. Gemini Enterprise and the Google Cloud console are separate tools designed for different tasks. Any differences in their sign-in processes should have minimal impact on the overall user experience.

To help enforce this partitioning, use organization policy constraints.

## Strengthen group governance

You should manage access using groups and establish clear processes for governing those groups to use Workforce Identity Federation effectively.

A user's permissions to access resources aren't determined during authentication. Instead, access is evaluated when the user attempts to access the resource based on the policies attached to that specific resource. These policies can include the following:

  * One or more [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies)
  * Zero or more [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview)
  * Zero or more [principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)



Policies define access for individual principals or principal sets:

  * **Principal** : An authenticated user identified by a principal identifier. A workforce principal identifier is similar to the following: `principal://iam.googleapis.com/locations/global/workforcePools/` `POOL_ID/subject/SUBJECT`

The principal identifier contains the following:

    * `POOL_ID`: uniquely identifies a workforce identity pool.
    * `SUBJECT`: uniquely identifies a specific user. The value and format depends on your IdP and attribute mapping.
  * **Principal set** : Users matching specific criteria. Workforce Identity Federation supports three principal sets: group-based (members of a group), attribute-based, and wildcard (all users).




Granting access to individual principals can be useful in specific situations, but it tends to scale poorly because of the following issues:

  * Adding principals one by one causes allow policies to grow and become increasingly difficult to manage.
  * Individual access management requires frequent changes to allow policies.
  * Policies might become increasingly inconsistent over time.



For scalable and effective access management, using group-based principal sets provides these advantages:

  * You can manage access by adding or removing members from groups, using your existing identity tools and processes.
  * Reduce the size and complexity of allow policies.
  * Ensure users with the same role have the same resource access.



To use groups to manage access, you must configure your external IdP in certain ways and be aware of any limitations that the IdP imposes on groups.

The following sections describe best practices for using groups effectively and avoiding IdP limits.

**Best practices** :

Distinguish different types of groups.  
Use access groups to grant access to resources.  
Use enforcement groups to constrain access to resources.  
Don't use organizational and collaboration groups to manage access.  
Use organizational groups and collaboration groups for Gemini Enterprise only.  


### Distinguish different types of groups

The following list describes four types of groups commonly found in organizations:

  * **Access groups** : Used only to grant access to Google services or Google Cloud resources. They represent job functions and simplify the assignment of roles that are required to perform these job functions.
  * **Organizational groups** : These groups represent subsets of an organization's structure, and are typically sourced from human resources data. They might be based on department, reporting structure, geographic location, or other organizational groupings.
  * **Collaboration groups** : These groups represent workgroups, project members, or users that want to collaborate on a project or discuss a specific topic and might be used for email distribution. Collaboration groups are often created on an ad hoc, self-service basis.
  * **Enforcement groups** : Enforcement groups, also called _policy groups_ , are used to restrict access, in contrast to access groups, which are used to grant access. For example, principal access boundaries, deny policies, or enforcing multi-factor authentication. Access groups can allow members to voluntarily leave a group. However, membership of an enforcement group is not voluntary.



The groups you need to federate depend on the following services you use:

  * For Google Cloud, you only need access groups and enforcement groups.
  * For Gemini Enterprise, you need access groups, enforcement groups, and—if using data ingestion-based connectors—certain organizational and collaboration groups.



When configuring Workforce Identity Federation, exclude irrelevant group types to help avoid token limits with your IdP. This approach helps you reduce the risk of exceeding limitations imposed by your IdP and ensure more consistent usage of groups.

###  Grant access to resources by using access groups

To manage access effectively, we recommend using principal sets that map to access groups. [Access groups](https://docs.cloud.google.com/iam/docs/groups-best-practices#types) exist solely to provide access. They represent job functions and simplify assigning the roles required to perform those functions.

Configure access groups by doing the following:

  1. In your IdP, create access groups that represent job functions.
  2. Map the access groups to principal sets to use them in IAM.
  3. Create policy bindings to grant the principal sets access to the resources that are needed for each job function.
  4. In the external IdP, add or remove users from the groups based on their job functions.



Use access groups for policies that grant access, including the following:

  * IAM allow policies
  * VPC Service Controls ingress rules



Ensure that access groups are sufficiently fine-grained. For example, the following groups represent effective access groups:

  * `widget-sales-dashboard-readers`: grants read access to a specific BigQuery dataset and associated dashboard.
  * `dev-ssh-users`: grants OS Login access to Compute Engine VMs in the development environment.

In contrast, the following types of groups aren't generally suitable for use as access groups:

    * Broad administrator groups like `cloud-admins` often lack specificity around which workloads or environments apply.

    * Organizational groups like `australia-fte` represent groups like teams or by location, rather than job function.

    * Communication groups like `security-discuss` are designed for email lists or collaboration, rather than an access group.

To keep access groups fine-grained, create a new set of access groups for each workload or project that you onboard to Google Cloud. This way, you can scale your number of access groups to your number of workloads that you run on Google Cloud.




### Constrain access to resources by using enforcement groups

Enforcement groups are similar to access groups, but typically differ in the following ways:

  * They don't allow members to voluntarily leave the group.
  * They aren't specific to a workload.



Use enforcement groups for policies that reduce access, including the following:

  * IAM deny policies
  * Principal access boundaries
  * Organization policies



Examples of enforcement groups include `users-in-restricted-locations`, `fedramp-low`, and `mfa-users`. The number of enforcement groups is typically small and unlikely to affect a user's total group memberships.

### Don't use organizational and collaboration groups to manage access

To manage access effectively, you can use access groups and enforcement groups instead of organizational or collaboration groups.

Organizational groups represent teams or subsets of an organization's structure and are typically sourced from human resources data. These groups are not suitable for managing access to Google Cloud resources for the following reasons:

  * Team responsibilities and composition might shift over time. For example, a team might hand over a workload to another team, or two teams might merge. Managing access with organizational groups might require a cascade of policy changes during these transitions.
  * Members of an organizational group rarely need identical access to resources. Granting access to an organizational group often gives some members more access than they need.



Collaboration groups are typically self-managed, allowing members to join with approval from another member or without approval. You can use collaboration groups to grant access can lead to over-permissioning and privilege escalation.

To prevent organizational and collaboration groups from being used for access management, configure your IdP to exclude these group memberships in the tokens or assertions used for Workforce Identity Federation.

### Use organizational groups and collaboration groups for Gemini Enterprise only

Although organizational and collaboration groups aren't well-suited for managing access to Google Cloud resources, you might need them for Gemini Enterprise:

  * **ACL evaluation** : When you use data ingestion-based connectors to integrate Gemini Enterprise with Microsoft 365, it might encounter documents with access control lists (ACLs) that refer to organizational and collaboration groups. If Gemini Enterprise lacks access to a user's memberships in these groups, it might not correctly evaluate whether the user is authorized to access those documents.
  * **Notebook sharing** : Gemini Notebook Enterprise lets users share notebooks. Allowing users to share notebooks with collaboration groups is often more convenient than restricting sharing to individual users.



To ensure that organizational and collaboration groups are only available to Gemini Enterprise, you can configure your IdP as follows:

  * Use SCIM to provision organizational and collaboration groups and their memberships.
  * Exclude organizational and collaboration group memberships in the tokens or assertions used for Workforce Identity Federation.



## Manage workforce identity pools

A workforce identity pool defines a namespace for principal identifiers and serves as a container for your federation configuration. Unlike a user directory, a pool doesn't store information about users or groups.

**Best practices** :

Use a single pool per IdP.  
Choose a unique and meaningful pool name.  
Treat pools as highly-privileged resources.  
Consider risks when extending federation to partners.  


### Use a single pool per IdP

Workforce identity pools are an organization-level resource, not a project-level resource. This design reflects that workforce identity pools manage authentication across a Google Cloud organization, rather than an individual project or workload.

For most organizations, the number of workforce identity pools should match the number of IdPs:

  * If your organization uses a single IdP to manage authentication, use a single workforce identity pool.
  * If your organization uses multiple IdPs—for example, because of an acquisition—use one workforce identity pool per IdP.



Limiting the number of workforce identity pools helps you ensure the following:

  * You don't need to create or modify workforce identity pools when onboarding new workloads to Google Cloud.
  * You can use IAM to control which projects and resources within Google Cloud individual users can access.



### Choose a unique and meaningful pool name

To make principal identifiers globally unique, workforce identity encodes the workforce identity pool name into the principal identifier. When choosing a name for a workforce identity pool, consider the following constraints:

  * **Uniqueness** : Choose a name that's unique across Google Cloud and unclaimed by another organization.
  * **Immutability** : You cannot change a workforce identity pool name. Choose a name that remains meaningful over time, avoiding temporary initiative names.
  * **User experience** : Depending on your sign-in configuration, users might need to enter the pool name during sign-in. Choose a short name that's memorable.



### Treat pools as highly-privileged resources

The workforce identity pool and provider determine how users sign in and control how identities and group memberships are derived from the external IdP. Because these components control authentication logic, they are central to the security of your Google Cloud organization. A compromise of these components might enable bad actors to perform spoofing attacks.

To perform a spoofing attack, bad actors might attempt the following actions:

  * **Modifying attribute mappings** : Altering attribute mappings can let a bad actor authenticate as someone else and gain unauthorized privileged access.
  * **Adding a malicious provider** : Adding a provider can let a bad actor bypass your organization's IdP and authenticate using a different IdP that they control.



Workforce identity pools and providers are security-critical resources that require the following protection:

  * **Restrict access to non-federated users** : Limit administrative access to a small number of Cloud Identity or Google Workspace users, including at least one emergency-access user.
  * **Protect administrative users** : Require two-step verification for all administrative and emergency-access users.
  * **Just-in-time access** : Use [Privileged Access Manager (PAM)](https://docs.cloud.google.com/iam/docs/pam-overview) to grant administrative access on a just-in-time basis rather than granting permanent access.



### Consider risks when extending federation to partners

Federating Google Cloud with an external IdP using Workforce Identity Federation establishes a trust relationship. By using federation, you rely on the external IdP to perform the following actions:

  * Perform multi-factor authentication (MFA) that meets your security requirements.
  * Make accurate assertions regarding user identities and group memberships.
  * Follow identity governance processes that ensure users are offboarded promptly and group memberships accurately reflect current roles.



Workforce Identity Federation provides limited mechanisms to validate the assertions made by an external IdP. Specifically, Workforce Identity Federation doesn't support post-SSO MFA [in the same way as Cloud Identity](https://support.google.com/a/answer/6002699).

Before using Workforce Identity Federation to allow external partners or contractors to access your Google Cloud resources, determine whether this level of trust is appropriate. Don't use Workforce Identity Federation for partner access unless you trust the partner and their IdP to consistently meet your security standards.

## Manage workforce identity pool providers

A workforce identity pool provider defines a federation relationship with an external IdP and contains configuration for the following:

  * The IdP to use for single sign-on.
  * The attribute mapping to use for deriving principal identifiers from tokens or assertions provided by the IdP.
  * Optional: the SCIM tenant to use for looking up group membership information.



**Best practices** :

Choose a meaningful provider name.  
Use your IdP's application portal to expose individual services.  
Use a single provider per pool to avoid subject collisions.  
Use the same pool and provider for the Google Cloud console and Gemini Enterprise.  
Use a tenant-specific issuer URI.  
Avoid using the OpenID Connect (OIDC) implicit flow.  


### Choose a meaningful provider name

When creating a workforce identity pool provider, you must assign it a name. Unlike workforce identity pool names, this name doesn't need to be globally unique and isn't encoded into principal identifiers. However, depending on your sign-in configuration, users might need to enter the provider name during sign-in. To improve user experience, choose a meaningful, memorable name—for example, `entra` or `staff`.

Avoid using names like `oidc` or `saml`, because these acronyms might be unfamiliar to users.

### Surface individual services in your IdP application portal

Identity providers such as Microsoft Entra ID and Okta provide an application portal that lets users discover and access their assigned applications. Use the portal to optimize user experience by doing the following:

  * Configure the portal to show relevant Google services individually instead of showing a single Google Cloud link.
  * Configure links to sign in the user automatically.



The following table lists common Google services that support Workforce Identity Federation and the URLs for automatic sign-in:

Application | URL  
---|---  
Google Cloud Workforce Identity Federation console, also known as the console (federated) | `https://auth.cloud.google/signin/locations/global/workforcePools/POOL/providers/PROVIDER?continueUrl=https%3A%2F%2Fconsole.cloud.google`  
Gemini Enterprise | `https://auth.cloud.google/signin/locations/global/workforcePools/POOL/providers/PROVIDER?continueUrl=https%3A%2F%2Fvertexaisearch.cloud.google%2Fhome%2Fcid%2FWEBAPP_ID`  
Gemini Notebook Enterprise | `https://auth.cloud.google/signin/locations/global/workforcePools/POOL/providers/PROVIDER?continueUrl=https%3A%2F%2Fnotebooklm.cloud.google%2Fglobal%2F%3Fproject%3DPROJECT_NUMBER`  
IAP web apps | App URL, such as `https://iap.example.com/`  
  
Replace the following:

  * `POOL`: the workforce identity pool name.
  * `PROVIDER`: the pool provider name.
  * `WEBAPP_ID`: the Gemini Enterprise web app ID.
  * `PROJECT_NUMBER`: the Gemini Notebook Enterprise project number.



### Use a single provider per pool to avoid subject collisions

You can use Workforce Identity Federation to add multiple providers to a workforce pool. Adding a second provider is useful during migrations where you temporarily allow users to authenticate using different IdPs. Beyond temporary situations, avoid using multiple providers for the following reasons:

  * **Subject collisions** : Using multiple providers introduces a risk of subject collisions. In such collisions, the `google.subject` attribute mapping for one provider returns the same value as another provider. This collision maps multiple external identities to the same IAM principal, making them indistinguishable in Cloud Audit Logs.
  * **IAP compatibility** : IAP requires [workforce identity pools to have a single provider](https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation#limitations-when-working-with-workforce-pools) to redirect unauthenticated users to the IdP automatically. If you add an additional provider, IAP cannot authenticate users.



If you need to federate with multiple providers, create multiple workforce pools and configure one provider for each pool.

### Use the same pool and provider for the Google Cloud console and Gemini Enterprise

If you use Workforce Identity Federation for both Gemini Enterprise and Google Cloud, use a single provider to ensure users can access both services simultaneously without signing in again. If you use separate providers with different attribute mappings, users might encounter situations where their access to resources differs depending on which provider they sign in with.

### Use a tenant-specific issuer URI

When configuring a provider, you specify an issuer URI to uniquely identify your IdP. However, depending on your IdP configuration, the issuer URI might not be unique to your organization's tenant. For example, if you use a generic or shared issuer URI such as the Microsoft Entra ID common endpoint (`https://login.microsoftonline.com/common/v2.0`), you might inadvertently allow users from other organizations to authenticate to your Google Cloud organization.

To help prevent unintended cross-tenant access, use a tenant-specific issuer URI. If your IdP doesn't provide a tenant-specific issuer URI, configure an attribute condition to limit access to your specific tenant.

### Avoid using the OpenID Connect (OIDC) implicit flow

When configuring an OIDC provider, prefer the authorization code flow over the implicit flow. The implicit flow is deprecated in version 2.1 of the OAuth specification [because it is vulnerable to token leakage and injection](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-09.html#name-removal-of-the-oauth-20-imp). Using the authorization code flow helps reduce the risk of token interception.

## Manage users

You can manage users using Workforce Identity Federation. Workforce Identity Federation derives a user's principal identifier from the user's token or assertion by performing the following steps:

  1. Determine the subject identifier by applying the attribute mapping for `google.subject`. The subject identifier must uniquely identify a user within a workforce identity pool, but doesn't need to be unique across Google Cloud.
  2. Derive the principal identifier by appending the subject identifier to a prefix that identifies the workforce identity pool. The resulting principal identifier is unique across Google Cloud and has the following format:
         
         principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/\
         subject/SUBJECT
         




When a user who authenticated using Workforce Identity Federation accesses a resource, IAM uses the principal identifier to evaluate role bindings in allow policies and records it in Cloud Audit Logs.

**Best practices** :

Use an immutable subject identifier.  
Don't reuse subject identifiers.  
Microsoft Entra ID: use the UPN as the subject identifier.  


### Use an immutable subject identifier

When a user's subject identifier changes, their principal identifier changes. As a result, Google Cloud no longer recognizes them as the same user:

  * The user cannot access resources they were previously granted access to because their new principal identifier no longer matches the principal identifiers listed in allow policies.
  * Cloud Audit Logs entries only contain the new principal identifier and can no longer be correlated with logs that used the old principal identifier.



To keep a user's principal identifier stable, use an attribute mapping that results in a stable value for `google.subject`.

Many IdPs automatically generate a unique numeric or UUID-formatted identifier for users. These identifiers are unique and stable, making them good candidates for `google.subject`. However, using these identifiers as `google.subject` can result in long, cryptic principal identifiers that might be difficult to work with.

To help you choose an identifier for `google.subject`, consider the following requirements in order of descending priority:

  1. **Uniqueness** : the value uniquely identifies a user in your IdP.
  2. **Usability** : the value is meaningful, or at least readily searchable in your IdP's user directory.
  3. **Immutability** : the value is immutable, or at least mutable only by administrators.



### Don't reuse subject identifiers

Many IdPs enforce uniqueness constraints on certain user identifiers but allow identifiers to be reused. For example, an IdP might not allow you to create two users with the same username `bob`. However, once you delete the user account `bob`, the IdP might allow you to create a new user account and assign it the username `bob` again.

If your provider's attribute mapping for `google.subject` refers to a user identifier that allows reuse, you might encounter subject collisions: Workforce Identity Federation cannot distinguish between an old user and a new user if their `google.subject` is the same. As a result, the new user might gain access to resources intended only for the old user.

To prevent subject collisions, do one or both of the following:

  * Map `google.subject` to a user identifier that your IdP doesn't allow to be reused.
  * When deleting a user in your IdP, use the [`locations.workforcePools.subjects.delete`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects/delete) API to [delete the user's data in Google Cloud](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data) and block the same user identifier from being used for sign-ins until all data has been purged.



### Microsoft Entra ID: use the UPN as the subject identifier

This best practice applies only if you use Microsoft Entra ID as your IdP.

If you use Microsoft Entra ID, the identifiers you can use as the subject identifier include the following:

  * User principal name (`upn`)
  * Object ID (`oid`)
  * Email address (the primary address in `proxyAddresses`)



Among these options, we recommend using the user principal name as the subject identifier for the following reasons:

  * All users have a user principal name.
  * User principal names uniquely identify a user.
  * User principal names tend to be meaningful and straightforward to work with.
  * User principal names embed a domain name, which uniquely identifies the Microsoft Entra ID tenant that the user is associated with.
  * Your organization might have a policy in place that prohibits or governs the reuse of user principal identifiers.



In contrast, a user's Object ID and email address are less suitable for the following reasons:

  * An Object ID (`oid`) is immutable but formatted as a GUID. This format makes them difficult to work with and not meaningful for humans.
  * The email address is not a required attribute, and it might not be populated for all users.



Regardless of which identifier you choose, we recommend that you avoid applying transformations such as forcing identifiers to lowercase.

**Important:** Some Gemini Enterprise connectors, including the data ingestion-based connector for Microsoft SharePoint, work correctly only if you use one of the following attribute mappings: `google.subject=assertion.upn` or `google.subject=assertion.email`.

## Manage groups

Workforce Identity Federation can determine a user's group membership from the following sources:

  * The SAML assertion or ID token provided by the IdP.
  * The Microsoft Graph API, if you use Microsoft Entra ID as your IdP.
  * The SCIM tenant associated with the workforce identity pool provider.



By default, Workforce Identity Federation uses only the SAML assertion or ID token:

Source | Google Cloud | Gemini Enterprise  
---|---|---  
SAML or ID token |  |   
Microsoft Graph API | - | -  
SCIM tenant | - | -  
  
If you use Microsoft Entra ID as your IdP, you can enable the [extra attributes](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups#extra-attributes) feature. Workforce Identity Federation then uses only the Microsoft Graph API as the source for group memberships:

Source | Google Cloud | Gemini Enterprise  
---|---|---  
SAML or ID token | - | -  
Microsoft Graph API |  |   
SCIM tenant | - | -  
  
If you use Gemini Enterprise, you can configure Workforce Identity Federation to use a SCIM tenant, which changes the behavior as follows:

  * Gemini Enterprise uses group memberships from the SCIM tenant and ignores group membership information from the SAML assertion or ID token.
  * Google Cloud uses group membership information from the SAML assertion or ID token and ignores group membership information from the SCIM tenant.

Source | Google Cloud | Gemini Enterprise  
---|---|---  
SAML or ID token |  | -  
Microsoft Graph API | - | -  
SCIM tenant | - |   
  
For each group membership, Workforce Identity Federation derives a principal identifier by performing the following steps:

  1. Determine the group identifier by doing one of the following: 
     * **SAML assertion or ID token** : Apply the attribute mapping for `google.groups`.
     * **SCIM tenant** : Apply the claims mapping for `google.group`.
     * **Microsoft Graph API** : Follow `extra-attributes-type` in the provider configuration.
  2. Derive the principal identifier by appending the group identifier to a prefix that identifies the workforce identity pool. The resulting principal identifier is unique across Google Cloud and has the following format:
         
         principalSet://iam.googleapis.com/locations/global/workforcePools/\
         POOL_ID/group/GROUP_ID
         




When a user that authenticated using Workforce Identity Federation accesses a resource, IAM uses these principal identifiers to evaluate role bindings in allow policies.

**Best practices** :

Use an immutable group identifier.  
Reduce group memberships in assertions or tokens.  
Microsoft Entra ID: use Object ID as the group identifier.  


### Use an immutable group identifier

All IAM policies reference groups by their principal identifier. When you rename a group in your IdP so that its identifier changes, Google Cloud no longer recognizes it as the same group:

  * Existing IAM role bindings continue to refer to the old principal identifier and become ineffective.
  * Members of the renamed group lose access because the group's new principal identifier no longer matches any IAM role bindings.



To prevent these disruptions, configure your attribute and claims mapping to use a stable, immutable value, such as an IdP-generated unique ID. Avoid using display names or email addresses as group identifiers, because these might change during organizational changes.

### Reduce group memberships in assertions or tokens

By default, your IdP might include more group memberships in SAML assertions or ID tokens than you need to manage access to Gemini Enterprise and Google Cloud resources. Including unnecessary group memberships creates multiple risks:

  * **Partial loss of access** : Many IdPs impose limits on the number of group memberships that they can include in a token or assertion. When a user exceeds this limit (group overage), the IdP might drop some group memberships, causing the user to lose access to certain resources.
  * **Sign-in failures** : Workforce Identity Federation [limits the size and number of group memberships](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) that the `google.groups` attribute mapping can produce. Users that exceed one of these limits cannot sign in.
  * **Inconsistent group usage** : If you expose groups to Google Cloud, project owners might decide to use those groups to manage access to resources, even if you never intended certain groups to be used in Google Cloud.



The following approaches can help you mitigate these risks and reduce the number of group memberships in assertions or tokens:

  * **Filter by group type** : Some IdPs, including Microsoft Entra ID, let you configure a filter that determines which groups to include in assertions or tokens. You can configure a filter to exclude group types that are not relevant based on your configuration and the [services that you plan to use](https://docs.cloud.google.com/iam/docs/federated-identity-architectures#service-portfolio).

The following table indicates which types of groups you might need to include in assertions or tokens, depending on the services that you plan to use:

Group Type | Google Cloud | Gemini (Sync-less) | Gemini (SCIM)  
---|---|---|---  
Access groups |  |  | -  
Enforcement groups |  |  | -  
Organizational groups | Not needed | * | -  
Collaboration groups | Not needed | * | -  
  
* Required only if using data-ingestion-based connectors.

    * To manage access to Google Cloud, you must include access groups and enforcement groups.
    * The filter required to manage access to Gemini Enterprise depends on whether you use SCIM. If you use SCIM, Gemini Enterprise ignores group memberships included in assertions or tokens, so you don't need to include any groups specific to Gemini Enterprise. If you don't use SCIM, you must include access groups and enforcement groups needed for Gemini Enterprise. Depending on whether you plan to use [data ingestion-based connectors](https://docs.cloud.google.com/iam/docs/federated-identity-architectures#gemini-m365), you might also need to include certain organizational and collaboration groups.
  * **Assignment** : Some IdPs, including Microsoft Entra ID, let you restrict group memberships in tokens and assertions to assigned groups, which are the groups you explicitly assign to the relying party configuration.

  * **Extra attributes filter** : If you use Microsoft Entra ID and have enabled the [extra attributes](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups#extra-attributes) feature, you can specify a filter using the [`--extra-attributes-filter`](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors) flag. Workforce Identity Federation passes this filter to the Microsoft Graph API when requesting group memberships.




To test or troubleshoot filters, use the [Debug IdP token](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors) tool in the Google Cloud console or enable [detailed audit logging](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#detailed-audit-logging).

### Microsoft Entra ID: use Object ID as the group identifier

This best practice applies only if you use Microsoft Entra ID as your IdP.

If you use Microsoft Entra ID, the identifiers you can use as the group identifier include the following:

  * Object ID (`oid`)
  * Email address
  * Display name



Among these options, we recommend using the Object ID (`oid`) as the group identifier for the following reasons:

  * All groups have an Object ID. In contrast, the email address is an optional field that might be populated only for Microsoft 365 groups.
  * The Object ID is unique and immutable. In contrast, a group's display name can change and might not be unique.



Regardless of which identifier you choose, we recommend that you avoid applying transformations such as forcing identifiers to lowercase.

**Important:** Some Gemini Enterprise connectors, including the data ingestion-based connector for Microsoft SharePoint, work correctly only if you use the Object ID as the group identifier.

## Manage access

Best practices for access limits and just-in-time (JIT) management.

**Best practices** :

Use Cloud Identity users for emergency access.  
Use Cloud Identity for highly-privileged access.  
Use organization policy constraints to govern federation.  
Don't grant access to all members of a pool.  
Limit session length.  
Align session length with JIT access requirements.  


### Use Cloud Identity users for emergency access

To help ensure continuous access to your Google Cloud environments, create emergency-access users for every environment.

Emergency-access users provide access to your Google Cloud environment when services are misconfigured, compromised, or not operating normally. Emergency-access users are highly privileged. Relying on Workforce Identity Federation to authenticate emergency-access users introduces the following risks:

  * A mistake in the workforce identity pool provider configuration can cause you to lock yourself out.
  * A service interruption affecting the external IdP can prevent you from using an emergency-access user when you need it most.
  * A compromise of the external IdP can let bad actors authenticate as an emergency-access user and gain broad access to your Google Cloud resources.



To mitigate these risks, use Cloud Identity or Google Workspace for emergency-access users, even if you use Workforce Identity Federation for other users:

  * Create emergency-access users in Cloud Identity.
  * Exclude these users from single sign-on and let them authenticate using a username and password.
  * Secure these users by enrolling them in two-step verification with a security key.



For more information on emergency-access users, see [Best practices for continuous access to Google Cloud](https://docs.cloud.google.com/docs/security/best-practices-continuous-access-to-google-cloud).

### Use Cloud Identity for highly-privileged access

Highly-privileged users have broad access to your Google Cloud environment. Examples of these users include the following:

  * Users with the Organization Administrator role (`roles/resourcemanager.organizationAdmin`)
  * Users with the Security Admin role (`roles/iam.securityAdmin`) or a similar role that can modify allow policies across significant parts of your Google Cloud resource hierarchy



If you use Workforce Identity Federation for highly-privileged users, any misconfiguration or compromise in your external IdP can impact the security of your Google Cloud resources. In particular, a compromise of the external IdP can let bad actors authenticate as a highly privileged user and gain broad access to your Google Cloud resources.

To mitigate these risks, use Cloud Identity for highly-privileged users:

  * Create highly privileged users in Cloud Identity.
  * Secure these users by enrolling them in two-step verification with a security key.
  * If you have federated Cloud Identity with an external IdP, enable [additional SSO verifications and two-step verification](https://support.google.com/a/answer/6002699#ssochallenges&zippy=Cset-up-post-sso-verification) for these users.



Additional SSO verifications might seem redundant if your IdP already enforces multi-factor authentication, but this setting helps protect users if the IdP is compromised. Additional SSO verifications is a feature supported by Cloud Identity but unavailable for Workforce Identity Federation.

### Use organization policy constraints to govern federation

If you use Cloud Identity for purposes other than emergency or highly- privileged access, partition your Cloud Identity federation and Workforce Identity Federation usage by service. To enforce this practice, use [custom organization policy constraints](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-type-matches-supported-principal-types) to restrict which principal types are allowed in specific projects.

For example, you can limit Workforce Identity Federation to Gemini Enterprise by doing the following:

  * Apply a custom organization policy constraint to your Gemini Enterprise project that uses the [`MemberTypeMatches`](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-type-matches-supported-principal-types) function to limit allowed principal types to `iam.googleapis.com/WorkforcePoolPrincipal` and `iam.googleapis.com/WorkforcePoolPrincipalSet`. These are the principal types used by Workforce Identity Federation.
  * For all other projects, apply a constraint that allows all principal types except `iam.googleapis.com/WorkforcePoolPrincipal` and `iam.googleapis.com/WorkforcePoolPrincipalSet`.



Using custom organization policy constraints helps you ensure consistency and helps prevent accidental use of incorrect principal types.

### Don't grant access to all members of a pool

Workforce Identity Federation supports a wildcard principal identifier that uses the following format:
    
    
    principalSet://iam.googleapis.com/locations/global/workforcePools/
    POOL_ID/*
    

This identifier matches every user your IdP allows to authenticate to Google Cloud.

Don't use this wildcard identifier to grant permissions. As your IdP's user base grows, granting access with the wildcard principal identifier leads to over-permissioning.

Instead, create access groups in your IdP and use these groups to manage access to resources. This approach helps ensure that access is governed by intentional group membership rather than successful authentication, reducing the risk of over-permissioning.

### Limit session length

When a user signs in, Workforce Identity Federation initiates a session. The session permits a user to do the following:

  * Use and navigate between the console (federated), Gemini Enterprise, or other portals that support Workforce Identity Federation.
  * Use IAP-protected web applications.
  * Obtain [federated refresh tokens](https://docs.cloud.google.com/docs/authentication/token-types#federated-refresh-tokens) and [federated access tokens](https://docs.cloud.google.com/docs/authentication/token-types#fed-access-tokens)—for example, by running `gcloud auth login`.



A session remains valid until one of the following occurs:

  * The session length reaches the limit defined by the [workforce identity pool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool:).
  * The session length reaches the limit defined in the `SessionNotOnOrAfter` attribute in the user's SAML assertion, if present.
  * The user signs out. 
  * An administrator [revokes the user's sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions). 



Allowing sessions to stay valid for extended periods increases the risk of token theft and can cause group membership information to become stale:

  * Users might retain access longer than intended if permissions are revoked in the IdP.
  * Users might be unable to exercise newly granted access until they re-authenticate and establish a fresh session.



To mitigate these risks, limit the session length so that users must sign in again at least once per day.

### Align session length with JIT access requirements

To manage privileged access, your IdPs might support just-in-time (JIT) groups that members can activate temporarily. Using just-in-time groups to manage privileged access to Google Cloud or Gemini Enterprise can introduce the following risks:

  * **Delayed activation** : If a user has an active Workforce Identity Federation session while activating their just-in-time group membership, the membership change doesn't take effect until the user signs out and signs in again. Alternatively, if the workforce identity pool provider uses SCIM, the membership change doesn't take effect until the group membership change is provisioned.
  * **Delayed revocation** : If a group membership expires, the user doesn't lose privileged access until they sign out and sign in again or the group membership change is provisioned using SCIM. Depending on your session length, this delay can undermine the purpose of membership expiration.



To mitigate these risks, configure your workforce identity pool session length to be sufficiently short.

## Monitor activity

Whenever you notice suspicious activity affecting a resource in Google Cloud, Cloud Audit Logs provides critical information to determine when the activity occurred and which users were involved.

### Enable data access logs

Workforce Identity Federation can generate logs that let you track sign-in and token exchange activities. The Security Token Service API writes these logs, which include the following [methods](https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-sts):

  * `google.identity.sts.SecurityTokenService.WebSignIn`
  * `google.identity.sts.SecurityTokenService.WebSignOut`
  * `google.identity.sts.v1.SecurityTokenService.ExchangeToken`
  * `google.identity.sts.v1beta.SecurityTokenService.ExchangeToken`



All logs related to sign-in and token exchange activities are classified as data access logs and are disabled by default. To capture these logs, [enable data access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the Security Token Service API across your Google Cloud organization. To increase the verbosity of sign-in logs further, enable [detailed audit logging](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#detailed-audit-logging).

To track other authentication-related activity, we recommend that you enable and use the following logs:

  * [IAM SCIM](https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-iamscim) audit logs
  * [Service Account Credentials](https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-iamcreds) audit logs
  * Cloud Identity and Google Workspace [login audit logs](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/login)



## What's next

  * Review the [Workforce Identity Federation Overview](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).
  * Learn to [Manage pools and providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers). 
  * Learn how to [revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
