---
url: https://docs.cloud.google.com/looker/docs/admin-panel-authentication-workforce-identity/
title: Admin settings - Workforce authentication \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:55.871049+00:00
---

# Admin settings - Workforce authentication  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-authentication-workforce-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Workforce authentication Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Provide feedback or report issues with this preview feature by sending a detailed email to [workforceidentityfederation_lookercore_feedback@google.com](mailto:workforceidentityfederation_lookercore_feedback@google.com).

The **Workforce Authentication** page in the **Authentication** section of the **Admin** menu lets you configure Looker (Google Cloud core) to authenticate users by using Workforce Identity Federation. To set up authentication, you will configure user attribute mappings, link workforce groups to Looker roles, and manage login options.

During the feature preview, only Looker (Google Cloud core) instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) are supported.

## Before you begin

Before you configure Workforce Identity settings in the Looker Admin panel, make sure you complete the following setup steps in Google Cloud, as described on the [Use Workforce Identity Federation for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity) documentation page:

  * [Set up a workforce identity pool and provider](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity#set-up-pool-provider) in your Google Cloud organization.
  * [Grant Identity and Access Management (IAM) permissions to workforce principals](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity#grant-permissions) to allow users to sign in.
  * [Select Workforce Identity Federation as your primary authentication method](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity#select-primary-auth-method) during instance creation or by editing an existing instance.



### Required roles

Looker displays the **Workforce Authentication** page in the **Authentication** section of the **Admin** menu only if the following conditions are met:

  * You have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles).
  * Your [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance is configured to use [Workforce Identity Federation as its primary authentication method](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity#select-primary-auth-method).



## Merge Workforce Identity Federation users to a Looker (Google Cloud core) account

In the **Merge Users Using** field, specify the method to be used to merge a first-time Workforce Identity Federation login to an existing user account. It is possible to merge users from the following systems:

  * Google
  * SAML
  * OIDC



For new instances, Google is the standard merge option. If your instance was previously configured with SAML or OIDC, Looker (Google Cloud core) automatically includes those existing configurations as merge sources to ensure that users are correctly linked to their existing Looker (Google Cloud core) profiles.

When a user logs in for the first time through Workforce Identity Federation, **Merge Users Using** connects the user to their existing account by finding the account that has a matching email address. If there is no existing account for the user, a new user account will be created.

### Multiple merge sources

If you have more than one authentication system in place, you can specify more than one system to merge by in the **Merge Users Using** field. Looker (Google Cloud core) will look up users from the listed systems _in the order that they are specified_. For example, assume that you created some users by using Google OAuth and then enabled OIDC, and now you want to use SAML. Looker would merge by Google OAuth first and then by OIDC.

## User login behavior

The **Bypass Login Page** setting controls whether unauthenticated users see the Looker login page or are automatically redirected to your identity provider (IdP) for authentication.

  * **Enabled (default):** When unauthenticated users navigate to your Looker (Google Cloud core) instance URL, they bypass the Looker **Log In** page and are redirected immediately to your enterprise IdP sign-in portal for authentication. Once authenticated, they return to the requested Looker page.
  * **Disabled:** When unauthenticated users navigate to your instance URL, they see the Looker **Log In** page. Users must select the authentication option to initiate sign-in with their IdP. This option is useful if you have configured secondary Google OAuth and want users to choose their sign-in method.



To change this setting, enable or disable the **Bypass Login Page** switch under **Login Behavior**.

**Tip:** To learn how Workforce Identity Federation affects user session length, persistent sessions, and offline background jobs, see [Session duration and identity provider policies in Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions#core_sessions) and [Session management and token validity](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity#session-management-token-validity).

## User attribute settings

You can pair claims and attributes that are passed from your workforce IdP with Looker [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) to automatically populate user values upon login (for example, to [make database connections user-specific](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#connections)).

### Pair Workforce Identity Federation attributes with Looker user attributes

To pair workforce identity attributes with Looker user attributes, complete the following steps:

  1. On the **Workforce Authentication** page, in the **User Attribute Settings** section, click **Manage Pairings**.
  2. In the **Claim** field, enter the attribute or claim name that's configured in your workforce identity pool (such as `google.display_name` or a custom `attribute.NAME` mapping). You can enter each claim name only once.
  3. In the **Looker User Attributes** field, select one or more Looker user attributes to associate with the claim.
  4. Optional: Select **Required** if a value for this claim is required for a user to log in.
  5. Click **Add Pairing** to add more attribute pairs.
  6. To remove an attribute pairing, click the delete **Delete** icon next to the pairing row.
  7. Click the close **Close** icon to exit the side panel,
  8. Pairings won't be saved or updated until you complete verification, submit from the main page, and click **Save** to apply your changes.



## Groups and roles

You can assign Looker [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) and [roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) to workforce users upon login, either by specifying defaults or by mirroring groups that are defined in your IdP.

### Default groups and roles

When group mirroring is disabled, which is the default setting, you can set default groups and roles for new workforce users when they first log in:

  * **New User Groups:** Enter the Looker groups to assign to new users when they first log in.
  * **New User Roles:** Enter the Looker roles to assign to new users when they first log in.



These default groups and roles apply to new users at their initial login and are not reapplied if removed later.

### Mirrored groups

A **mirrored group** is a Looker group (managed on the [**Groups** page](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups)) that Looker automatically creates and synchronizes with an external workforce group from your IdP.

To automatically create and synchronize Looker groups based on your workforce identity provider's groups, turn on **Mirror Workforce Groups**. By default, this option is disabled.

To configure mirrored groups, complete the following steps:

  1. Turn on **Mirror Workforce Groups**.
  2. Click **Manage Groups** to open the side panel.
  3. Click **Add Mapping** and configure the following: 
     * **Looker Group Name:** Enter the display name for the mirrored group on Looker (Google Cloud core)'s **Groups** page.
     * **Workforce Group ID:** Enter the group identifier as passed in the workforce token (for example, the group name or security identifier from your IdP).
     * **Roles:** Select one or more Looker roles to assign to members of this group.
  4. To remove a group mapping, click the delete **Delete** icon next to the mapping row.
  5. Click the close **Close** icon and click **Save**.



Adding or modifying group mappings doesn't apply them to existing users. Group mappings are evaluated only during the login process.

#### When OAuth is the secondary authentication method

**Important:** We recommend that you enable group mirroring for only the primary authentication method and don't enable group mirroring for backup OAuth authentication.

If you have enabled [backup Google OAuth authentication](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#using_oauth_as_a_backup_authentication_method), enable group mirroring for only your primary authentication method. If you enable group mirroring for both the primary and secondary methods of authentication, the following behaviors will occur: 

  * If a user has merged identities, group mirroring will match the primary authentication method regardless of the actual authentication method that's used to sign in.
  * If a user doesn't have merged identities, group mirroring will match the authentication method that's used to sign in.



### Editing mirrored groups

If you edit a mirrored group mapping, the configuration of the group changes, but the Looker group itself remains intact. For example:

  * Changing the **Looker Group Name** changes the display name of the group on the Looker (Google Cloud core) **Groups** page, without altering assigned roles or members.
  * Changing the **Workforce Group ID** changes which external workforce group maps to that Looker group. Members of the Looker group are reassigned on next login based on membership in the new external workforce group.



Any edits that are made to a mirrored group mapping will be applied to users when they next log in to Looker (Google Cloud core).

### Advanced role management

When **Mirror Workforce Groups** is enabled, you can configure the following options to control role and group assignments:

  * **Prevent individual Workforce users from Receiving Direct Roles:** When this option is enabled, workforce users can only receive roles through group memberships. Any directly assigned roles are removed on next login.
  * **Prevent direct membership in non-Workforce groups:** When this option is enabled, workforce users cannot be manually added to built-in (non-mirrored) Looker groups. Any users who were previously assigned to built-in groups will be removed from those groups on next login. If mirrored groups are allowed to be members of built-in Looker groups, workforce users may retain membership in any parent Looker groups.
  * **Prevent role inheritance from non-Workforce groups:** When this option is enabled, members of mirrored groups don't inherit roles from parent built-in groups. Any users who previously inherited roles from a parent built-in group will lose those roles when they next sign in.
  * **Auth Requires Role:** When this option is enabled, users must have at least one assigned role to sign in. If this option is disabled, users without roles can sign in but cannot view content or perform actions.

**Caution:** Turning on more restrictive settings will cause users to lose group membership or assigned roles that were configured in Looker (Google Cloud core) directly. The loss of group membership or assigned roles will occur the next time those users log in to Looker (Google Cloud core).

### Disabling mirrored groups

If you turn off **Mirror Workforce Groups** , the following behaviors will occur:

  * Mirrored Looker groups with no users are deleted immediately from your instance.
  * Mirrored Looker groups with users are marked as orphaned and will be deleted after 31 days if no members log in.
  * External workforce groups in your IdP remain unaffected.



## Test user authentication

Click the **Test** button to test your settings. Tests will redirect out to the server and will open a browser tab. The tab displays the following information:

  * Whether Looker was able to talk to the server and validate.
  * The names that Looker gets from the server. You need to validate that the server returns the proper results.
  * A trace to show how the information was found. Use the trace to troubleshoot if the information is incorrect. If you need additional details, you can read the raw XML server file.

**Note:** Read the results of the test carefully, as some parts of the test can succeed even if others fail.

**Tips** :

  * You can run this test any time, even if Workforce Identity Federation is partially configured. Running a test can be helpful during configuration to see which parameters need configuration.
  * The test uses the settings that are entered on the **Workforce Identity** page, even if those settings haven't been saved. The test won't affect or change any of the settings on that page.
  * During the test, Looker passes information to the IdP by using the Workforce Identity Federation `RelayState` parameter. The IdP should return this `RelayState` value to Looker unmodified.

**Note:** Be sure to verify that _all_ tests are passing before you click **Update Settings**. Saving incorrect Workforce Identity Federation configuration information could lock you and others out of Looker.

## Save and apply settings

Once you are done entering your information and the tests are all passing, select **I have verified the Workforce configuration** and click **Update Settings** to save.

## What's next

  * [Prepare a Looker (Google Cloud core) instance for users](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
