---
url: https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation/
title: Best practices for using Workload Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:12.083965+00:00
---

# Best practices for using Workload Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Best practices for using Workload Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

Workload Identity Federation lets applications running outside Google Cloud impersonate a service account by using credentials from an external identity provider.

Using Workload Identity Federation can help you improve security by letting applications use the authentication mechanisms that the external environment provides and can help [replace service account keys](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#using_service_accounts).

To use Workload Identity Federation securely, you must configure it in a way that protects you from the following threats:

  * **Spoofing:** A bad actor might attempt to spoof another user's identity to gain unauthorized access to Google Cloud resources.
  * **Privilege escalation:** A bad actor might take advantage of Workload Identity Federation to gain access to resources they otherwise wouldn't have access to.
  * **Non-repudiation:** A bad actor might conceal their identity and actions by using external credentials that make it difficult to trace actions back to them.
  * **Malicious credential configurations:** A bad actor could provide a malicious credential configuration to circumvent your security defenses.



This guide presents best practices for deciding when to use Workload Identity Federation, and how to configure it in a way that helps you minimize risks.

## When to use Workload Identity Federation

**Best practices** :

Use Workload Identity Federation for applications that have access to ambient credentials.  
Use an additional token exchange to use ambient credentials that aren't supported by Workload Identity Federation.  
Use Workload Identity Federation to reduce the number of credentials that require rotation.  


### Use Workload Identity Federation for applications that have access to ambient credentials

Applications running on cloud providers other than Google Cloud often have access to ambient credentials. These are credentials that the application can obtain without having to perform any additional authentication. Examples include:

  * On AWS, applications deployed on EC2 can use [instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) to assume a role and obtain temporary credentials.
  * On Azure, applications can use [managed identities](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) to obtain access tokens.
  * In GitHub Actions, workflows can [obtain ID tokens](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) that reflect the deployment job's identity.



If the ambient credentials are OpenID Connect (OIDC) tokens, SAML assertions, or AWS credentials, you can [configure Workload Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) to let applications exchange these credentials for short-lived Google access tokens. If the ambient credentials use a different format, you might be able to exchange them for an OIDC token or SAML assertion first, and then use them for Workload Identity Federation.

Use Workload Identity Federation whenever an application needs to access Google Cloud and has access to ambient credentials.

### Use an additional token exchange to use ambient credentials that aren't supported by Workload Identity Federation

In some cases, an application might have access to ambient credentials, but the types of credentials aren't supported by Workload Identity Federation. In these cases, check if an additional token exchange lets you convert the ambient credential into a type of credential that you can use for Workload Identity Federation.

For example, if your application runs in an Active Directory environment, it might have access to Kerberos credentials. If you have an identity provider such as Active Directory Federation Services (AD FS) in your environment that supports [Integrated Windows Authentication](https://en.wikipedia.org/wiki/Integrated_Windows_Authentication), you can use these Kerberos credentials to authenticate to the identity provider and obtain an OAuth access token that uses the JWT format. Using this access token and Workload Identity Federation, you can then let the application perform a second token exchange to obtain short-lived Google credentials.

Chaining token exchanges increases complexity and might introduce additional dependencies, but can free you from having to manage and secure service account keys.

### Use Workload Identity Federation to reduce the number of credentials that require rotation

Applications that integrate with an OpenID or SAML identity provider often use a client secret (or a different form of secret) to authenticate to the identity provider. Typically, this secret is stored as part of the application's configuration. To let such an application access Google Cloud, you must decide between:

  1. Creating a service account key and storing it alongside the other secret.
  2. Using tokens issued by the existing identity provider and exchanging them for Google credentials by using Workload Identity Federation.



The first option requires two secrets, but the second option only requires one. Reducing the number of secrets can help you simplify [secret rotation](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#rotate-keys), which in turn can help improve security.

### Use Workload Identity Federation with regional endpoints to address data residency requirements

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you have data residency requirements and need to control the region in which token exchanges might occur, configure your workloads to use a regional endpoint of the Secure Token Service (STS).

To generate a credential configuration file that uses a regional STS endpoint, use the `gcloud iam workload-identity create-cred-config` command and add the `--sts-location=REGION` argument.

To update an existing credential configuration file, do the following:

  1. Open the credential configuration file.
  2. In the `token_url` field, replace `https://sts.googleapis.com` with `https://sts.REGION.rep.googleapis.com`, or if you use mTLS, replace `https://sts.mtls.googleapis.com` with `https://sts.REGION.rep.mtls.googleapis.com`.



To use regional endpoints over Private Service Connect, see [About accessing regional endpoints through Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).

## Protecting against spoofing threats

A workload identity pool doesn't _contain_ any identities or user accounts, which makes it different from a user directory such as Cloud Identity. Instead, a workload identity pool represents a _view_ that surfaces identities from external identity providers so that they can be used as IAM principals.

Depending on how you configure the workload identity pool and its providers, the same external identity might be represented as multiple different IAM principals, or several external identities could map to the same IAM principal. Such ambiguities might allow bad actors to launch spoofing attacks.

The following section describes best practices that help you avoid ambiguous mappings, and reduce the risk of spoofing threats.

**Best practices** :

Use attribute conditions when federating with GitHub or other multi-tenant identity providers.  
Use a dedicated project to manage workload identity pools and providers.  
Use organizational policy constraints to disable the creation of workload identity pool providers in other projects.  
Use a single provider per workload identity pool to avoid subject collisions.  
Avoid federating with the same identity provider twice.  
Protect the OIDC metadata endpoint of your identity provider.  
Use the URL of the workload identity pool provider as audience.  
Use immutable attributes in attribute mappings.  
Use non-reusable attributes in attribute mappings.  
Don't allow attribute mappings to be modified.  
Don't rely on attributes that aren't stable or authoritative.  
Validate credential configurations from an external source before using them to authenticate to Google APIs. 

### Use attribute conditions when federating with GitHub or other multi-tenant identity providers

Workload Identity Federation doesn't maintain a directory of user accounts; instead, it implements [claims-based identities](https://en.wikipedia.org/wiki/Claims-based_identity): As a result, when two tokens are issued by the same identity provider (IdP) and their claims map to the same `google.subject` value, the two tokens are assumed to identify the same user. To find out which IdP issued a token, Workload Identity Federation inspects and verifies the token's issuer URL.

Some providers, such as GitHub and Terraform Cloud, use a single issuer URL across all of their tenants. For these providers, the issuer URL identifies _all of GitHub or Terraform Cloud_ , not a specific GitHub or Terraform Cloud organization.

When you use these identity providers, it's insufficient to let Workload Identity Federation check a token's issuer URL to ensure that it comes from a trusted source and that its claims can be trusted. We recommend that you configure a Workload Identity Federation attribute condition to check that the token originated from a trusted tenant or, in the case of GitHub or Terraform Cloud, a trusted organization.

To learn more, see [configure an attribute condition](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines#conditions).

### Use a dedicated project to manage workload identity pools and providers

Instead of managing workload identity pools and providers across multiple projects, use a single, dedicated project to manage workload identity pools and providers. Using a dedicated project helps you to:

  * Ensure that only trusted identity providers are used for Workload Identity Federation.
  * Centrally control access to the configuration of workload identity pools and providers.
  * Apply consistent attribute mappings and conditions across all projects and applications.



You can use organizational policy constraints to enforce the discipline of using a dedicated project to manage workload identity pools and providers.

### Use organizational policy constraints to disable the creation of workload identity pool providers in other projects

Users with the permission to create workload identity pool providers can create workload identity pools and providers that might be redundant to the ones you manage in a dedicated project.

You can prevent the creation of new workload identity pool providers by using the `[constraints/iam.workloadIdentityPoolProviders](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers#restrict)` organizational policy constraint with a rule set to **Deny All**.

[Apply these constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints) at the root of your organizational hierarchy to deny the creation of new workload identity pool providers by default. Create exceptions for the projects in which you want to allow the management of workload identity pools and providers by applying a policy constraint that permits certain, trusted AWS accounts or OIDC providers.

### Use a single provider per workload identity pool to avoid subject collisions

Workload Identity Federation lets you create more than one provider per workload identity pool. Using multiple providers can be useful if identities are managed by multiple providers, but you want to hide this complexity from workloads running on Google Cloud.

Using multiple providers introduces a risk of subject collisions, where the attribute mapping for `google.subject` of one provider returns the same value as the attribute mapping for another provider. The result of such a collision is that multiple external identities are mapped to the same IAM principal, making the external identities indistinguishable in Cloud Audit Logs.

To avoid subject collisions, use a single provider per workload identity pool. If you need to federate with multiple providers, create multiple workload identity pools, each using a single workload identity provider.

### Avoid federating with the same identity provider twice

You can create multiple workload identity pool providers that refer to the same identity provider or AWS account. However, if these providers belong to the same workload identity pool, then such a configuration can lead to subject collisions. If the providers belong to different workload identity pools, subject collisions can't occur and the same external identity is instead represented as different IAM principals.

Mapping a single external identity to multiple IAM principals makes it more difficult to analyze which resources a particular external identity has access to. Such an ambiguity can also increase risk when trying to revoke access: An administrator might revoke access for one principal, but might be unaware of the existence of another principal, inadvertently causing the external identity to retain access.

To minimize the risk of ambiguities, avoid federating with the same identity provider more than once. Instead, create a single workload identity pool and provider and use an attribute mapping and condition that ensures that it can be used for all external identities that require access to Google Cloud resources.

### Protect the OIDC metadata endpoint of your identity provider

When you federate with an OpenID Connect provider, Workload Identity Federation periodically downloads the OIDC metadata from your identity provider. Workload Identity Federation uses the IdP's metadata and JSON Web Key Set (JWKS) to validate tokens.

To ensure authenticity, communication with your identity provider is secured by using TLS. If your provider is deployed behind a load balancer or reverse proxy that terminates TLS, then the TLS connection ensures the authenticity of the load balancer or reverse proxy, but not of the actual identity provider.

A bad actor might be able to take advantage of this setup by launching a man-in-the-middle (MITM) attack in which they reconfigure the load balancer to let it pass JWKS requests to a malicious endpoint that serves a different set of keys. Swapping the JWKS lets a bad actor sign tokens that are considered valid by Workload Identity Federation and might allow them to spoof other user's identities.

To protect against JWKS swapping, ensure that your IdP is deployed in a way that protects it against MITM attacks.

### Use the URL of the workload identity pool provider as the audience

When you federate with an OpenID Connect provider, Workload Identity Federation verifies that the audience of tokens (encoded in the `aud` claim) matches the allowed audience setting of the provider. Similarly, when you federate with a SAML provider, Workload Identity Federation checks that the SAML assertion specifies an _audience restriction_ that matches the expected audience.

By default, Workload Identity Federation expects the audience to match the URL `https://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID` that uniquely identifies the workload identity pool provider. Requiring tokens and assertions to use this URL as the audience helps reduce the risk of a [confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem) attack. In such an attack, a bad actor presents a token or SAML assertion to Workload Identity Federation that wasn't intended to be used for Workload Identity Federation, but for some other API.

Requiring the token or assertion to contain the URL of the target workload identity pool provider helps you ensure that clients can only use tokens and assertions that were specifically issued for Workload Identity Federation.

### Use immutable attributes in attribute mappings

To [grant an external identity permission to impersonate a service account](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#impersonate), you create an IAM binding that references the external identity by subject, group, or a custom attribute. The external identity's subject, group, and custom attributes are derived from the attributes that the external identity provider passes to Workload Identity Federation during the token exchange.

Some identity providers permit users to change some of their own attributes. For example, a user might be allowed to modify their email address or aliases. If your IAM bindings refer to attributes that are modifiable, then users might accidentally lose access to certain resources by modifying their user profile. Or worse, bad actors might be able to gain unauthorized access to other resources by deliberately modifying their user attributes to match existing IAM bindings.

To protect against this spoofing threat, limit attribute mappings to attributes that can't be modified by the user, or can't be modified at all.

### Use non-reusable attributes in attribute mappings

When you grant an external identity permission to impersonate a service account and subsequently delete the user in the external identity provider, then the IAM binding of the service account remains in place.

If you later add a new user to your external identity provider, and the user shares certain attributes with the previously deleted user (for example, same email address), then the old and new users will be indistinguishable for Workload Identity Federation. As a result, an IAM binding that was meant to only refer to the old user might apply to the new user too.

To prevent such ambiguities, use attribute mappings that exclusively rely on attributes that can't be reused over time, like a unique user ID.

If your company policy allows the reuse of attributes such as email addresses, then avoid using these attributes in attribute mappings and use a different attribute instead that's guaranteed to be unique over time.

### Don't allow attribute mappings to be modified

Workload Identity Federation uses [attribute mappings](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping) to select which of the attributes provided by the external identity provider should be embedded into an STS token, and how the attribute names should translate. Configuring attribute mappings is a key step to setting up the trust relationship between the external identity provider and Google Cloud.

Attribute mappings are also crucial to the security of using Workload Identity Federation: If you've granted a federated principal or principal set the ability to [impersonate a service account](https://docs.cloud.google.com/iam/docs/workload-identity-federation#impersonation), and you then change the attribute mapping, you might change which users have access to the service account.

Modifying attribute mappings requires the `iam.googleapis.com/workloadIdentityPoolProviders.update` permission. Roles containing this permission include:

  * Owner (`roles/owner`)
  * IAM Workload Identity Pool Admin (`roles/iam.workloadIdentityPoolAdmin`)



If a bad actor has permission to modify attribute mappings, they might be able to change the mapping rules in a way that allows them to spoof their identity and gain access to a service account. To prevent such malicious modifications, make sure only a few administrative users have the permission to modify attribute mappings.

Consider creating a dedicated Google Cloud project for managing workload identity pools, which helps you limit the risk of users inadvertently being granted one of these roles at a higher level in the resource hierarchy.

### Don't rely on attributes that aren't stable or authoritative

An identity provider uses attributes to communicate information about authenticated users. Identity providers typically guarantee that some attributes are authoritative, but others aren't. For example, an external identity provider might embed both a username and a user ID in an OIDC token. Both attributes uniquely identify a user and might seem interchangeable. However, the external identity provider might guarantee that the user ID is stable and authoritative, but allow usernames to be changed.

If your attribute mappings rely on attributes that aren't stable or authoritative, then a bad actor might be able to spoof their identity by modifying their user profile in the external identity provider. For example, they might change their username to that of a user that has been recently deleted in the external identity provider, but still has access to a service account on Google Cloud.

To prevent such spoofing attacks, make sure your attribute mappings only rely on attributes that the external identity provider guarantees to be stable and authoritative.

### Validate credential configurations from an external source before using them to authenticate to Google APIs

Some credential configurations contain URLs and file paths that, if not appropriately validated by a workload, could cause the workload to use malicious endpoints.

When you accept a credential configuration from an external source, you must validate the JSON before using it. If you don't validate the credential configuration, a malicious actor could use the credential configuration to cause your workload to access malicious endpoints.

For more information, see [Security requirements when using credential configurations from an external source](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials).

## Protecting against non-repudiation threats

Whenever you notice suspicious activity affecting one of your resources on Google Cloud, Cloud Audit Logs are an important source of information to find out when the activity happened and which users were involved.

When an application uses Workload Identity Federation, it impersonates a service account. In Cloud Audit Logs, any activity performed by the application is attributed to the impersonated service account. To reconstruct the full chain of events that led to the activity, you must be able to correlate Cloud Audit Logs with the logs of your identity provider so that you can find out which external identity was involved, and why an activity was performed.

This section describes best practices that can help you maintain a non-repudiable audit trail.

**Best practices** :

Enable data access logs for IAM APIs.  
Use a unique subject mapping.  


### Enable data access logs for IAM APIs

To help you identify and understand service account impersonation scenarios, services such as Compute Engine include a `serviceAccountDelegationInfo` section in Cloud Audit Logs. When an application uses Workload Identity Federation, this section [includes the subject](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workload-identity#auth-sa-credentials) of the principal that was used to impersonate the service account.

Not all services include impersonation details in Cloud Audit Logs. To help maintain a non-repudiable audit trail, you must also record all impersonation events by [enabling data access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the **Security Token Service API** and **Identity and Access Management API**. Enable these logs for all Cloud projects that contain workload identity pools or service accounts used for Workload Identity Federation.

By enabling these logs, you make sure that an entry is added to the Cloud Audit Logs whenever an application uses Workload Identity Federation to [exchange an external credential](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workload-identity#exchange-federated) and [impersonates a service account](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workload-identity#create-short-lived-credentials).

### Use a unique subject mapping

The [principal subject used in the serviceAccountDelegationInfo section](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workload-identity#auth-sa-credentials) in Cloud Audit Logs entries is determined by your workload identity pool provider's attribute mapping for `google.subject`.

When you spot suspicious activity and need to find out which external identity was involved, you must be able to look up an external identity by its corresponding `google.subject` value.

Similarly, when an external identity was compromised and you need to find out whether the identity was used to access Google Cloud resources, you must be able to find Cloud Audit Logs entries that correspond to the external identity.

When you [define the attribute mapping ](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation#mappings-and-conditions) for a workload identity pool provider, choose a unique mapping for `google.subject` so that:

  * An external identity maps to exactly one `google.subject` value.
  * A `google.subject` value maps to exactly one external identity.
  * You can look up an external identity by its `google.subject` value.



Using an attribute mapping that satisfies these uniqueness criteria helps you ensure that you can look up external identities by their `google.subject` value, and `google.subject` values by their external identities.

## Protecting against privilege escalation threats

To apply the principle of least privilege when using Workload Identity Federation, you must:

  * limit the number of external identities that can impersonate a service account
  * limit the resources that a service account can access



An overly permissive configuration can lead to a situation where a bad actor can use an external identity to escalate their privileges and access resources they shouldn't have access to.

The following sections provide best practices that can help you protect against privilege escalation threats.

**Best practices** :

Use service accounts that reside in the same project as the resources you need to access.  
Use a dedicated service account for each application.  
Avoid granting access to all members of a pool.  


### Use service accounts that reside in the same project as the resources you need to access

When a client uses Workload Identity Federation [by using client libraries](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#generate-automatic) or [the REST API](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#rest), it follows a three-step process:

  1. Obtain a credential from the trusted identity provider.
  2. Exchange the credential for a token from the Security Token Service.
  3. Use the token from the Security Token Service to impersonate a service account and obtain a short-lived Google access token.



For the last step, use a service account that resides in the same project as the resources you need to access. Using a service account that's managed in the same project helps you apply more restrictive access permissions, and makes it easier to decide when the service account might not be needed anymore.

### Use a dedicated service account for each application

If you have multiple applications that use Workload Identity Federation to access resources in the same project, create a dedicated service account for each application. Using application-specific service accounts helps you avoid over-permissioning by only granting access to resources that each individual application requires.

### Avoid granting access to all members of a pool

Before an external identity can impersonate a service account, you must [grant it the `roles/iam.workloadIdentityUser` role on the service account](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#impersonate). When you grant this role, avoid granting it to all members of the workload identity pool. Instead, grant the role to specific external identities, or to identities that match certain criteria.

Initially, the number of external users that need access to Google Cloud resources might be small. The attribute condition of your workload identity pool and the configuration of your identity provider might therefore only permit a few external identities to use Workload Identity Federation.

When you later onboard new workloads to Google Cloud, you might need to modify your identity provider's configuration or the workload identity pool's attribute condition so that it allows additional external identities.

By only granting the `roles/iam.workloadIdentityUser` role to specific external identities, you can ensure that you can safely grow a workload identity pool without inadvertently granting more external identities impersonation access than necessary.

## What's next

  * Learn about [best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).
  * Read more about [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
