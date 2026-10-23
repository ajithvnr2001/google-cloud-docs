---
url: https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity/
title: Use Workforce Identity Federation for Looker (Google Cloud core) user authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:00.399364+00:00
---

# Use Workforce Identity Federation for Looker (Google Cloud core) user authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Use Workforce Identity Federation for Looker (Google Cloud core) user authentication Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Provide feedback or report issues with this preview feature by sending a detailed email to [workforceidentityfederation_lookercore_feedback@google.com](mailto:workforceidentityfederation_lookercore_feedback@google.com).

[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) lets you use an external identity provider (IdP) to authenticate users and groups of users into a Looker (Google Cloud core) instance. By using Workforce Identity Federation, users in your organization can use single sign-on (SSO) to access Looker (Google Cloud core) without requiring you to provision or synchronize Google Accounts (Cloud Identity or Google Workspace accounts) for every user.

Workforce Identity Federation supports external IdPs that use [OpenID Connect (OIDC)](https://openid.net/connect/) or [SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html), such as Microsoft Entra ID (formerly Azure AD), Okta, PingIdentity, and others.

During the feature preview, only Looker (Google Cloud core) instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) are supported.

## How Workforce Identity Federation works with Looker (Google Cloud core)

When you configure Workforce Identity Federation for a Looker (Google Cloud core) instance, the following process occurs:

  1. **Authentication:** A user navigates to your Looker (Google Cloud core) instance URL. If the **Bypass login page** setting is enabled, the user is automatically redirected to the Google Cloud sign-in portal (`https://auth.cloud.google/authorize`), which redirects the user to your external IdP for authentication.
  2. **Token exchange:** After the user authenticates with your IdP, your IdP returns an authentication assertion to Google Cloud Security Token Service (STS). STS exchanges the assertion for a federated access token and ID token.
  3. **Authorization:** Looker (Google Cloud core) verifies that the federated principal has the required Identity and Access Management (IAM) permission (`looker.instances.login`) on the instance.
  4. **Provisioning and role assignment:** Looker (Google Cloud core) creates the user account on first login (Just-In-Time provisioning) and applies group-to-role mappings and user attributes that are based on the claims that it receives from your IdP.



## Before you begin

Before you configure Workforce Identity Federation for Looker (Google Cloud core), ensure that you have the following roles and configurations:

### Required IAM roles

To configure Workforce Identity Federation and create Looker (Google Cloud core) instances, you need the following roles:

  * [**IAM Workforce Pool Admin** (`roles/iam.workforcePoolAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin): Required on the Google Cloud organization to create and manage workforce pools and providers.
  * [**Looker Admin** (`roles/looker.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin): Required on the Google Cloud project to create and manage Looker (Google Cloud core) instances.
  * [**Project IAM Admin** (`roles/resourcemanager.projectIamAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin): Required on the Google Cloud project to grant IAM roles to workforce principals.



### Required APIs

Enable the following APIs in your Google Cloud project:

  * Identity and Access Management API (`iam.googleapis.com`)

[Enable the Identity and Access Management API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com)

  * Security Token Service API (`sts.googleapis.com`)

[Enable the Security Token Service API](https://console.cloud.google.com/apis/enableflow?apiid=sts.googleapis.com)

  * Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`)

[Enable the Cloud Resource Manager API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com)

  * Looker (Google Cloud core) API (`looker.googleapis.com`)

[Enable the Looker (Google Cloud core) API](https://console.cloud.google.com/apis/enableflow?apiid=looker.googleapis.com)


**Note:** During the feature preview, the integration between Looker (Google Cloud core) and Workforce Identity Federation is supported only for Looker (Google Cloud core) instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections).

## Step 1: Set up a workforce identity pool and provider

Workforce identity pools and providers are created at the Google Cloud organization level, not the project level.

Complete the following steps to set up a workforce identity pool and provider:

  1. Create a workforce identity pool by following the instructions on the [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#create-workforce-pool) documentation page.
  2. Create a workforce identity pool provider for your OIDC or SAML 2.0 IdP: 
     * For OIDC providers, see [Configure OIDC workforce identity federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#create-oidc-provider).
     * For SAML providers, see [Configure SAML 2.0 workforce identity federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#create-saml-provider).
     * Define the following attribute mappings immediately during provider creation: 
       * **Email:** Map your IdP's email claim to `google.email`. This mapping is **required** for user identification; authentication will fail if this mapping is missing.
       * **First name and last name:** Map your IdP's given name and family name claims to `attribute.given_name` (first name) and `attribute.family_name` (last name). These mappings are **required** to populate Looker user profiles; authentication will fail if these mappings are missing.
  3. Optionally, configure the following attribute mappings as well:

     * **Groups:** Map your IdP's group claim (for example, `assertion.groups`) to `google.groups`. This mapping is required if you plan to enable group mirroring and to map IdP groups to [Looker roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles). For OIDC providers, ensure that your provider configuration also requests the `groups` scope if your IdP requires it (see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#create-oidc-provider) for IdP-specific requirements).
     * **Custom attributes:** Map [custom IdP claims](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) to `attribute.<attribute_name>`. You can use these mapped attributes in Looker (Google Cloud core) to parameterize database connections and apply row-level data access filters.
**Tip:** To ensure a seamless setup and avoid the need to re-edit your provider configuration later, we recommend that you define attribute mappings immediately during provider creation.



### Configure extended session length and background synchronization

**Note:** If you are evaluating Workforce Identity Federation in a test environment or only testing basic user sign-in, you can skip this section. You only need to configure extended session length and background synchronization before onboarding production users or to support uninterrupted browser sessions, scheduled deliveries, and alerts.

To support uninterrupted browser sessions, long-running scheduled deliveries, user API key access, and connector integrations, complete the following steps:

  1. Configure background attribute synchronization on your workforce pool provider so Google Cloud can periodically refresh user attributes and group memberships in the background: 
     * **For OIDC providers:** Configure either the OIDC Authorization Code flow with the `offline_access` scope (which uses refresh tokens to periodically refresh user attributes and group memberships) or [SCIM 2.0 provisioning](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim). If users belong to a large number of groups that exceed OIDC token size limits, configure SCIM 2.0 provisioning to synchronize group memberships to Google Cloud.
     * **For SAML providers:** Configure [SCIM 2.0 provisioning](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim) on your workforce pool provider. Because SAML assertions don't provide refresh tokens natively, SCIM 2.0 is required to enable offline scheduled deliveries and alerts.
  2. Configure an [extended session length policy](https://docs.cloud.google.com/access-context-manager/docs/extended-session-length-for-workforce-identity-federation) for your workforce pool using Access Context Manager cloud bindings, and set the policy to 90 days (7,776,000 seconds).

This policy sets the maximum session duration and refresh token validity to 90 days. If an extended session length policy is not configured or is set to a shorter duration, the workforce pool refresh token validity takes precedence over Looker's [session duration settings](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions#session_duration), causing browser sessions, offline schedules, user API keys, and connected applications to require re-authentication when the refresh token expires.




## Step 2: Grant IAM permissions to workforce principals

To let workforce users sign in to your Looker (Google Cloud core) instance, grant the Looker Instance User (`roles/looker.instanceUser`) or Looker Admin (`roles/looker.admin`) IAM role to your workforce principals or groups.

You can grant roles to [individual users, entire groups, or all principals in a workforce pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-principal-identifiers) by using the following principal identifiers:

  * **Single workforce user:**
        
        principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/SUBJECT_ID
        

  * **Workforce group:**
        
        principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID
        

  * **All principals in a workforce pool:**
        
        principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/*
        




For more information about assigning IAM roles, see the [ Looker (Google Cloud core) access control with IAM](https://docs.cloud.google.com/looker/docs/looker-core-access-control) documentation page.

## Step 3: Select Workforce Identity Federation as your primary authentication method

You can select Workforce Identity Federation as the primary authentication method when creating a new Looker (Google Cloud core) instance or by editing an existing instance.

### During instance creation

When creating a new Looker (Google Cloud core) instance, you can select Workforce Identity Federation as the primary authentication method:

### console

  1. In the Google Cloud console, go to the **Looker (Google Cloud core)** page. 

[Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker)

  2. Click **CREATE INSTANCE**.
  3. Complete the instance name, region, and edition configuration as described in the documentation for creating instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-instance-create), [Private Service Connect connections](https://docs.cloud.google.com/looker/docs/looker-core-create-psc), or [private services access connections](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip).
  4. In the **Authentication** section, select **Workforce Identity Federation (SAML/OIDC)** as the primary authentication method.
  5. Click **Create**.



To set OAuth as a secondary authentication method, edit the instance configuration after the instance is created.

### When editing an existing instance

If you have an existing Looker (Google Cloud core) instance, you can edit the instance configuration to select Workforce Identity Federation as the primary authentication method or to set OAuth as the secondary authentication method:

### console

  1. In the Google Cloud console, go to the **Looker (Google Cloud core)** page. 

[Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker)

  2. Click the name of the instance that you want to edit.
  3. On the instance **Details** tab, click **Edit**.
  4. In the **Authentication** section, select **Workforce Identity Federation (SAML/OIDC)** as the primary authentication method.
  5. (Optional) To allow [OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) as a secondary authentication method, enable the **Enable Secondary OAuth** toggle.
  6. Click **Save**.



## Step 4: Configure Workforce Identity settings in Looker

After your Looker (Google Cloud core) instance is created, an administrator can configure user attribute mappings, group mirroring, and login options within the **Workforce authentication** page of the Looker Admin panel.

  1. Sign in to your Looker (Google Cloud core) instance with an account that has the **Admin** Looker role.
  2. In the left navigation menu, select **Admin > Authentication > Workforce Identity**.
  3. Configure the settings that are described in the following sections.



See the [**Workforce authentication** page documentation](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-workforce-identity) for more information about the following settings.

### Merge user accounts

In the **Merge Users Using** field, select the authentication systems from which existing user accounts should be merged when a user signs in for the first time with Workforce Identity Federation.

Supported systems for merging include the following:

  * **Google**
  * **SAML**
  * **OIDC**



### Bypass login page

The **Bypass login page** option controls whether unauthenticated users are automatically redirected to your enterprise SSO portal:

  * **Enabled (default):** When users navigate to your instance URL, they are automatically redirected to your IdP sign-in screen without seeing the Looker login page.
  * **Disabled:** Users see the Looker login page and can choose between available authentication options.



Click **Save Configuration** to apply your settings.

### User attribute mapping

Map claims from your IdP assertion to Looker [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes). User attributes can be used for many things, such as to parameterize database connections and apply row-level security filters.

  * In the **Attribute Mapping** section, map Google workforce attributes to corresponding Looker user attributes (for example, mapping `attribute.department` to a `department` user attribute in Looker).



### Groups and roles

You can manage user roles through group mirroring or default role assignments:

  * **Mirror groups from IdP:** When this setting is enabled, Looker (Google Cloud core) creates Looker groups that mirror groups that are passed in the IdP token assertion. 
    * In the **Group Mapping** table, map external IdP group names to Looker groups and assign appropriate Looker roles (such as Viewer, User, or Developer).
  * **Default new user role:** If group mirroring is not used or doesn't match a user, specify the default role to be granted to new users upon first login.
  * **Default new user group:** If group mirroring is not used or doesn't match a user, specify the default group to be assigned to new users.



## Session management and token validity

User sessions and tokens in Looker (Google Cloud core) are governed by the session duration and refresh token validity that are configured in your workforce identity pool policy (such as an extended session length policy):

  * **Browser sessions:** Looker [session duration settings](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions#session_duration) support sessions of up to 30 days when using persistent sessions. However, the workforce identity pool's refresh token validity takes precedence if its validity is less than the session duration configured in Looker. When the refresh token expires, the user must sign in again. We recommend that you set a 90-day refresh token validity in your extended session length policy.
  * **Scheduled deliveries and alerts (offline jobs):** Background jobs run as long as the schedule owner has an active IdP token. If a schedule or alert creator doesn't sign in to the instance for more than 90 days (or the duration that's configured in your workforce pool session policy), their offline session expires, and scheduled deliveries or alerts that are owned by that user are paused. To resume paused schedules or alerts, the owner must sign in to the instance, or an administrator must assign schedule ownership.
  * **Looker OAuth server and connectors:** Integrations that use the Looker OAuth server (such as Data Studio, Connected Sheets, and third-party connectors) use a 30-day refresh token (or a non-expiring refresh token in Data Studio). If the workforce pool session duration is set to less than 90 days, users might need to re-authenticate with Looker when the session duration expires.
  * **User API keys:** API access tokens that are generated by user API keys are valid for 1 hour and require an active user IdP session. If the user's IdP session expires (every 90 days or based on the workforce pool session duration), the user must sign in to the instance again to continue using their API keys.
  * **Service account API keys:** Service account API access tokens are unaffected by workforce pool session policies.



## What's next

  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)
  * [Looker (Google Cloud core) access control with IAM](https://docs.cloud.google.com/looker/docs/looker-core-access-control)
  * [Manage maintenance policies for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-maintenance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
