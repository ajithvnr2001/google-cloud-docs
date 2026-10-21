---
url: https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication/
title: Use Google OAuth for Looker (Google Cloud core) user authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:33:37.226899+00:00
---

# Use Google OAuth for Looker (Google Cloud core) user authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Use Google OAuth for Looker (Google Cloud core) user authentication Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To learn how to set up an OAuth client and credentials, see the [Create an OAuth client and credentials for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) documentation page.

Google OAuth is used in conjunction with Identity and Access Management (IAM) to authenticate Looker (Google Cloud core) users.

When using OAuth for authentication, Looker (Google Cloud core) authenticates users through the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol. You can use any OAuth 2.0 client. As an example, this page walks you through the steps to set up authentication for a Looker (Google Cloud core) instance by using the Google Cloud console to create OAuth credentials.

If another method is the primary form of authentication, Google OAuth is by default the backup authentication method.

## Authentication and authorization with OAuth and IAM

When used with OAuth, [Looker (Google Cloud core) IAM roles](https://docs.cloud.google.com/looker/docs/looker-core-access-control) provide the following levels of authentication and authorization for all Looker (Google Cloud core) instances within a given Google Cloud project. [Assign](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#adding-users) one of the following IAM roles to each of your principals, depending on the levels of access that you want them to have:

IAM Role | Authentication | Authorization  
---|---|---  
Looker Instance User (`roles/looker.instanceUser`) | Can sign in to Looker (Google Cloud core) instances | Upon first login to Looker (Google Cloud core), granted the default Looker role set in Roles for new users. Cannot access Looker (Google Cloud core) resources in the Google Cloud console.  
Looker Viewer (`roles/looker.viewer`) | Can sign in to Looker (Google Cloud core) instances | Upon first login to Looker (Google Cloud core), granted the default Looker role set in Roles for new users.  Can view the list of Looker (Google Cloud core) instances and instance details in the Google Cloud console  
Looker Admin (`roles/looker.admin`) | Can sign in to Looker (Google Cloud core) instances | Upon first login to Looker (Google Cloud core), granted the default Looker role set in Roles for new users.Verified on each login to Looker (Google Cloud core) that uses [primary OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) or [backup OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#using_oauth_as_a_backup_authentication_method) and each time the user makes a call to the Looker API, this role (or a custom role that includes the `looker.instances.update` permission) also grants the **Admin via IAM** role within the instance.The **Admin via IAM** role contains all the permissions and capabilities of the [**Admin**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) Looker role. This role cannot be removed or reassigned within the Looker (Google Cloud core) instance. To remove the **Admin via IAM** role, reassign the principal to an IAM role other than Looker Admin (`roles/looker.admin`). Changes to IAM roles are automatically synced to the Looker (Google Cloud core) instance even if the user logs in with a third-party identity provider after the change. For more information, see the Admin Looker role versus Admin via IAM Looker role section.As long as a user's OAuth refresh token is valid, the user's role shows as **Admin via IAM** within Looker (Google Cloud core), even if that user later logs in with a third-party identity provider. If the OAuth refresh token expires or is revoked, the user must use OAuth to log into the instance again to regain the **Admin via IAM** role. Can perform all administrative tasks for Looker (Google Cloud core) within the Google Cloud console  
  
Additionally, user accounts with the [`owner`](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role for a project can log in to and administer any Looker (Google Cloud core) instances within that project. These users will be granted the [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) Looker role.

If the predefined roles don't provide the set of permissions that you want, you can also create your own [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

Looker (Google Cloud core) accounts are created at the time of first login to a Looker (Google Cloud core) instance.

### Admin Looker role versus Admin via IAM Looker role

**Note:** In the Looker documentation, any references to "Looker admin" or "**Admin** Looker role" also apply to users with the **Admin via IAM** role.

There are two roles within a Looker (Google Cloud core) instance that use the [Admin permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets) and confer the same admin privileges within the instance. The following table summarizes the two roles' similarities and differences.

Property | Admin Looker role | Admin via IAM Looker role  
---|---|---  
Authoritative source | Granted by another admin in the Looker (Google Cloud core) instance | Directly linked to the Looker Admin IAM role  
Can be added or removed within a Looker (Google Cloud core) instance? | Yes | No  
Can be added or removed with IAM? | No | Yes  
Permissions within Looker (Google Cloud core) | All permissions | All permissions  
Permissions within the Google Cloud console | None | Full access to all Looker (Google Cloud core) resources  
Role validation | Continually within the Looker (Google Cloud core) instance | Upon every login to the Looker (Google Cloud core) instance and every Looker API call.Changes to a role with IAM may take several minutes to propagate.  
Scope | Individual Looker (Google Cloud core) instance | All Looker (Google Cloud core) instances within a Google Cloud project  
  
A user can have both the **Admin** and the **Admin via IAM** Looker roles. Therefore, if you want to revoke admin privileges, be sure to remove both the IAM role and the **Admin** role within the Looker (Google Cloud core) instance.

**Tip:** If a principal with the [Looker Admin IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) was assigned the Looker Admin IAM role and signed in to an instance prior to Looker 25.4, that principal has both the **Admin** Looker role and the **Admin via IAM** role within the Looker (Google Cloud core) instance upon upgrade to Looker 25.4. We recommend that you remove the **Admin** Looker role for these users so that administrator privileges are managed solely through the Google Cloud console.

## Configuring OAuth within the Looker (Google Cloud core) instance

Within the Looker (Google Cloud core) instance, the **Google Authentication** page in the **Authentication** section of the **Admin** menu lets you configure some Google OAuth settings. You must have the **Admin** Looker role.

### Merge user accounts

In the **Merge Users Using** field, specify the method to be used to merge a first-time OAuth sign-in to an existing user account. When a user signs in for the first time through OAuth, this option will connect the user to their existing account by finding the account with a matching email address. If no account exists for the user, a new user account will be created.

You can merge users from the following systems:

  * **SAML**
  * **OIDC**



If you have more than one system in place, you can specify more than one system to merge by in this field. Looker (Google Cloud core) will look up users from the listed systems _in the order in which the systems are specified_. For example, if you first created some users using OIDC and then later used SAML, when a user attempts to login with OAuth for the first time, Looker (Google Cloud core) first looks for the user using OIDC and then, if it doesn't find a match for the user with OIDC, it would then look for the user using SAML.

If you don't want Looker (Google Cloud core) to merge users, leave this field blank.

### Migrating between OIDC identity providers

When you're migrating from one OIDC identity provider to another (for example, when transitioning from PingFederate to Okta), the account merging option that's described in Merge user accounts doesn't apply. Merging applies only when you're transitioning between _different_ authentication types (such as SAML to OIDC).

Looker (Google Cloud core) uses the `sub` claim from the OIDC payload to populate the `oidc_user_id` user attribute, which uniquely identifies OIDC user accounts. To prevent Looker (Google Cloud core) from generating duplicate user accounts during an OIDC migration, configure your new OIDC identity provider to ensure that the `sub` claim that's sent in the OIDC payload matches the `oidc_user_id` that's established by your previous provider (for example, the `sub` claim should contain the user's email address instead of a newly generated UUID).

If maintaining identical `sub` claims on the new identity provider isn't possible, new user accounts will be created. In this scenario, you can use the Looker API to retrieve favorite content and reassign schedules from the previous user accounts to the new user accounts before you delete the previous accounts.

**Warning:** When the `sub` claim changes during an OIDC migration, Looker (Google Cloud core) creates a new user identity and derives a new personal Git development branch name from the new user's internal ID. This change puts developers at risk of losing uncommitted LookML changes that are stored in their original personal branches. If maintaining identical `sub` claims isn't feasible, instruct developers to commit and push all changes from their old personal branches and merge required changes into the production branch _before_ the OIDC cutover. Following the migration, developers can switch to their new personal branches and pull the latest production code.

### Mirror Google Groups

**Note:** Google OAuth group mirroring isn't supported for Looker (Google Cloud core) instances that are [in FIPS-compliant mode](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode).

If you have managed [Google Groups](https://support.google.com/groups/answer/46601?ref_topic=9216), Looker (Google Cloud core) can create [Looker groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) that mirror the membership of your Google Groups. This means that you don't have to set up users in Looker (Google Cloud core) directly but can manage user access by managing the membership of the Google Groups. Additionally, Looker groups can be used to [assign roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#assigning_roles) to group members, set [content access controls](https://docs.cloud.google.com/looker/docs/organizing-spaces), [control feature and data access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#controlling_feature_and_data_access), and assign [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes).

For group mirroring to function correctly, users must have the `VIEW_MEMBERSHIP` permission, which lets them view the membership of the Google Groups that they belong to. To grant this permission in the Google Groups UI settings, set the **Who can view members** field to **Group members**.

The mirrored Looker groups (and any associated roles and access) are applied to new users at their initial login to the Looker (Google Cloud core) instance. The groups aren't applied to pre-existing users, and the groups aren't reapplied if they are removed from a user's account within Looker (Google Cloud core) after the user's initial login.

The **Admin via IAM** Looker role, which is automatically granted to users who have the [**Looker Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) role in the IAM system, overrides group mirroring. Users with the **Looker Admin** role in the IAM system are automatically assigned the **Admin via IAM** role within Looker (Google Cloud core) regardless of what group memberships they have. In addition, these users will be assigned to mirrored groups and receive roles and access through the standard mirroring process.

We recommend that you enable group mirroring for only the primary authentication method for Looker (Google Cloud core). If you are using OAuth as the [backup authentication method](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#using_oauth_as_a_backup_authentication_method), don't enable group mirroring for OAuth. If you enable group mirroring for both the primary and secondary methods of authentication, the following behaviors will occur:

  * If a user has merged identities, group mirroring will match the primary authentication method regardless of the actual authentication method used to sign in.
  * If a user doesn't have merged identities, group mirroring will match the authentication method used to sign in.



#### Steps to enable mirrored groups

To enable group mirroring, complete the following steps:

  1. In the Google Cloud console, enable the Cloud Identity API in the Google Cloud project that contains your OAuth client. You must have the [Service Usage Admin](https://docs.cloud.google.com/service-usage/docs/access-control#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) IAM role to enable APIs. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

  2. In the Google Cloud console, update the OAuth client's consent screen to add the [`https://www.googleapis.com/auth/cloud-identity.groups.readonly` scope](https://developers.google.com/identity/protocols/oauth2/scopes#cloudidentity). You must have the `clientauthconfig.clients.update` IAM permission to add scopes. Complete the following steps to update the consent screen:

     * Navigate to the OAuth client.
     * Choose the **Data Access** page.
     * Click the **Add or remove scopes** button. This opens an **Update selected scopes** panel.
     * Find the `https://www.googleapis.com/auth/cloud-identity.groups.readonly` scope and select the checkbox next to it.
     * Click the **Update** button to add the scope.
     * Close the panel and click **Save** on the **Data Access** page to save the scope.

**Caution:** If the **User Type** field in your OAuth client is set to **External** , you must complete [restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification) for the OAuth app. Until the OAuth app has been verified by Google, users will be able to sign in, but they will see a warning message during the sign-in process. This is because the Cloud Identity API is a [sensitive scope](https://developers.google.com/workspace/guides/configure-oauth-consent#scope_categories).
  3. In the Looker (Google Cloud core) instance, enable the **Mirror Google Groups** toggle on the **Google Authentication** page. This toggle defaults to disabled. Complete the following fields:

     * In the **Looker Group Name** field, add a name for the Looker group. This is the name that will appear on the [**Groups** page](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#viewing_and_searching_groups) within Looker (Google Cloud core).
     * In the **Google Group ID** field, enter the [name or email](https://support.google.com/groups/answer/2464926#info-new) of the Google Group that you want to mirror.
     * In the **Role** field, enter the [Looker role or roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) that you want to assign to the members of that group.



Looker (Google Cloud core) will make one Looker group for every Google Group that is added to the **Google Authentication** page. You can view those Looker groups on the [**Groups** page](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#viewing_and_searching_groups) of Looker (Google Cloud core).

**Note:** Looker (Google Cloud core) fetches only direct group memberships of the user. Any transitive or hierarchical memberships mapped won't work.

#### Editing mirrored groups

When you make changes to a Google Groups membership, those changes are automatically propagated to the mirrored Looker group's membership and validated at the time of each user's next login.

If you edit the **Custom name** or **Role** fields that are assigned to a group on the **Google Authentication** page, this changes how the mirrored Looker group's name appears in Looker (Google Cloud core)'s **Groups** page or the role(s) assigned to the group, but it doesn't change the group members.

If you change the name or email in **Google Group ID** field on the **Google Authentication** page to a new Google group's ID, that changes the members of the mirrored Looker group to the members of the new Google group, but it would maintain the group name and roles as defined on the **Google Authentication** page.

Any edits that are made to a mirrored group will be applied to users of that group when they next sign in to Looker (Google Cloud core).

#### Disabling mirrored groups

If you want to stop mirroring your Google groups within Looker (Google Cloud core), disable the **Mirror Google Groups** toggle on the **Google Authentication** page of the Looker (Google Cloud core) instance. Disabling the toggle results in the following behavior:

  * Any mirror Google group with no users is deleted immediately.
  * Any mirror Google group that _does_ contain users is marked as orphaned. If no users of this group log in within 31 days, the group is deleted. Users can no longer be added or removed from orphaned Google groups.



#### Advanced role management

If the **Mirror Google Groups** toggle is enabled, the **Google Authentication** page displays the **Advanced Role Management** settings. The options in this section determine how much flexibility Looker admins have when configuring Looker groups and users who have been mirrored from Google.

If you want your Looker group and user configuration to strictly match your Google Groups configuration, turn on all the **Advanced Role Management** options. When all of the options are enabled, Looker admins cannot modify mirrored group memberships and can only assign roles to users through Google Groups.

**Caution:** Turning on more restrictive settings will cause users to lose group membership or assigned roles that were configured in Looker (Google Cloud core) directly. This occurs the next time those users sign in to Looker (Google Cloud core).

If you want to have more flexibility to customize your groups within Looker (Google Cloud core), turn off these options. Your Looker (Google Cloud core) groups will still mirror your Google Groups configuration, but you will be able to perform additional group and user management within Looker (Google Cloud core), such as adding Google users to Looker groups or assigning Looker roles directly to Google users.

For Looker (Google Cloud core) instance, these options are off by default.

The **Advanced Role Management** section contains the following options:

  * **Prevent individual Google users from receiving direct roles** : Turning this option on prevents Looker admins from assigning Looker roles directly to Google users. Google users will receive roles only through their group memberships. If Google users are allowed membership in built-in (not mirrored) Looker groups, they can still inherit their roles both from mirrored Google Groups and from built-in Looker groups. Any Google users who were previously assigned roles directly will have those roles removed when they next log in.

**Note:** The **Admin via IAM** Looker role, which is automatically granted to users who have the [**Looker Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) IAM role, overrides the **Prevent individual Google users from receiving direct roles** option. Users with the **Looker Admin** IAM role retain the **Admin via IAM** Looker role regardless of the state of this option. However, enabling this option prevents Looker admins from directly assigning any roles.

If this option is off, Looker admins can assign Looker roles directly to Google users within the Looker (Google Cloud core) instance.

  * **Prevent direct membership in non-Google groups** : This option prevents Looker admins from adding members of mirrored groups directly to built-in Looker groups that are not part of the mirrored group configuration on the **Google Authentication** page.

If this option is selected, any Google users who were previously assigned to built-in Looker groups will be removed from those groups when they next login.

If this option is cleared, Looker admins can add Google users directly to built-in Looker groups.

  * **Prevent Role Inheritance from non-Google Groups** : This option prevents members of mirrored groups from inheriting roles from built-in Looker groups. If mirrored Google Groups are allowed to be members of built-in Looker groups, Google users may retain membership in any built-in Looker groups. Any Google users who previously inherited roles from a built-in Looker group will lose those roles when they next sign in.

If this option is off, mirrored groups or Google users who are added as members of a built-in Looker group will inherit the roles that are assigned to the built-in Looker group.

  * **Auth Requires Role** : If this option is on, Google users are required to have a Looker role assigned. Any Google users who don't have a role assigned won't be able to sign in to Looker (Google Cloud core) at all.

If this option is off, Google users can authenticate to Looker (Google Cloud core) even if they have no role assigned. A user with no assigned role won't be able to see any data or take any action in Looker (Google Cloud core), but they will be able to sign in to Looker (Google Cloud core).




### Set a default Looker role

**Note:** The default Looker role will be granted upon first login. Changes to the user's IAM role after the first login won't change or remove that Looker role that was assigned by default.

If the **Mirror Google Groups** toggle is disabled, the **Roles for new users** setting appears on the **Google Authentication** page. This setting lets you set the default [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) that will be granted to user accounts with the Looker Instance User (`roles/looker.instanceUser`) IAM role or the Looker Viewer (`roles/looker.viewer`) IAM role upon their first login to a Looker (Google Cloud core) instance. To set a default role, follow these steps:

  1. Navigate to the **Google Authentication** page within the **Authentication** section of the **Admin** menu.
  2. In the **Roles for new users** setting, select the role that you want to grant all new users by default. The setting contains a list of all the [default roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) and [custom roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#assigning_roles) within the Looker (Google Cloud core) instance.



Admin roles can't be default roles. User accounts with a Looker Admin (`roles/looker.admin`) IAM role will be granted the Admin via IAM Looker role upon first login in addition to the role that's selected in the **Roles for new users** setting.

If you enable the **Mirror Google Groups** toggle after customizing the **Roles for new users** setting, the roles that are assigned to users through the **Roles for new users** setting will be removed for users upon their next login and replaced by the roles assigned through the **Mirror Google Groups** setting.

### Test User Authentication

Click the **Test Google Authentication** button to test your settings. Tests will redirect out to Google's OAuth server and will open a browser tab. The tab displays the following information:

  * Whether Looker (Google Cloud core) was able to talk to the server and validate.
  * The user information Looker (Google Cloud core) gets from the server. You need to validate that the server returns the proper results.
  * A trace to show how the info was found. Use the trace to troubleshoot if the information is incorrect. If you need additional information, you can read the raw XML server file.
  * Both decoded and raw versions of the ID token received. These can be used to confirm user details as well as Google configuration.



### Save and apply settings

Once you are done entering your information and the tests are all passing, select the **I have confirmed the configuration above and want to enable applying it globally** checkbox, and click **Submit** to save.

## Adding users to a Looker (Google Cloud core) instance

**Note:** Access to the Looker (Google Cloud core) instance is granted through IAM. However, Looker user accounts are not created until users agree to the OAuth consent screen and sign in to the instance.

Once a Looker (Google Cloud core) instance has been [created](https://docs.cloud.google.com/looker/docs/looker-core-instance-create), users can be added through IAM. To add users, follow these steps:

  1. Be sure that you have the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) role or [another role that lets you manage IAM access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions).
  2. Navigate to the Google Cloud console project that the Looker (Google Cloud core) instance resides in.

**Note:** IAM roles are global within a project. If there is more than one Looker (Google Cloud core) instance in a project, IAM roles that are granted within that project will apply to all Looker (Google Cloud core) instances that reside there.
  3. Navigate to the **IAM & Admin > IAM** section of the Google Cloud console.

  4. Select **Grant Access**.

  5. In the **Add principals** section, add one or more of the following:

     * A Google Account email
     * A Google Group
     * A Google Workspace domain
  6. In the **Assign roles** section, select one of the [predefined Looker (Google Cloud core) IAM roles](https://docs.cloud.google.com/looker/docs/looker-core-access-control#roles) or a custom role that you have added.

  7. Click **Save**.

  8. Communicate to new Looker (Google Cloud core) users that access has been granted and direct them to the URL for the instance. From there they can sign in to the instance, at which point their accounts will be created. No automated communication will be sent.




If you change a user's IAM role, the IAM role propagates to the Looker (Google Cloud core) instance within a few minutes. If there is an existing Looker user account, that user's Looker role remains unchanged.

All users must be provisioned by the IAM steps described previously, with one exception: You can [create Looker API-only service accounts](https://docs.cloud.google.com/looker/docs/looker-core-user-management#creating_an_api-only_service_account) within the Looker (Google Cloud core) instance.

## Logging in to Looker (Google Cloud core) with OAuth

The first time that users sign in, they are asked to [sign in using their Google Account](https://support.google.com/accounts/answer/12629094?sjid=8591543582681818450-NC). Each user should use the same account that the Looker admin listed in the **Add principals** field when granting them access. Users will view the [OAuth consent screen](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#configure_the_user_consent_screen_scopes_and_test_users) that was configured during OAuth client creation. After users agree to the consent screen, their accounts within the Looker (Google Cloud core) instance are created and they are logged in.

After that, users will be automatically logged in to Looker (Google Cloud core) unless their authorization [expires](https://support.google.com/a/answer/7576830) or is [revoked by the user](https://developers.google.com/identity/gsi/web/guides/revoke). In those scenarios, users will again view the OAuth consent screen and be asked to consent to authorization.

Some users may be assigned API credentials for use in retrieving an API access token. If the authorization for those users expires or is revoked, their API credentials stop working. Any current API access tokens will also stop working. To resolve the issue, the user must re-authorize their credentials by logging back in to the Looker (Google Cloud core) UI for each Looker (Google Cloud core) instance that is affected. Alternatively, using [API-only service accounts](https://docs.cloud.google.com/looker/docs/looker-core-user-management#creating_an_api-only_service_account) helps avoid a credential authorization failure for API access tokens.

## Removing OAuth access to Looker (Google Cloud core)

**Important:** It is recommended that access to a Looker (Google Cloud core) instance be removed using IAM rather than from within the instance.

If you have [a role that lets you manage IAM access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions), you can remove access to a Looker (Google Cloud core) instance by [revoking the IAM role](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#revoke-single-role) that granted access. If you remove a user account's IAM role, that change propagates to the Looker (Google Cloud core) instance within a few minutes. The user will no longer be able to authenticate to the instance. However, the user account will still appear active on the **Users** page. To remove the user account from the **Users** page, [delete the user](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#deleting_users) within the Looker (Google Cloud core) instance.

## Using OAuth as a backup authentication method

If you use another authentication method—such as Workforce Identity Federation, SAML, or OpenID Connect (OIDC)—you can configure Google OAuth as a secondary or backup authentication method. This configuration ensures that users and administrators can still authenticate with Google Accounts if they cannot access the primary identity provider.

### Set up OAuth as a backup for SAML or OIDC

OAuth is the backup authentication method when [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml) or [OIDC](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect) is the primary authentication method.

To set up an OAuth as the backup method, [grant](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#adding-users) each Looker (Google Cloud core) user the appropriate [IAM role](https://docs.cloud.google.com/looker/docs/looker-core-access-control#roles) to log in to the instance.

### Set up OAuth as the secondary method for Workforce Identity Federation

OAuth can optionally be set up as the secondary authentication method for Workforce Identity Federation. To set up OAuth as the secondary authentication method, [edit the instance](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity#edit-existing-instance) to enable the **Enable secondary OAuth** setting.

### Logging in with OAuth

Once the backup method is set up, users access it through the following steps:

  1. Select **Authenticate with Google** on the sign-in page.
  2. A dialog appears to confirm Google authentication. Select **Confirm** in the dialog.



Users can then log in using their Google Accounts. When first logging in with OAuth, they will be prompted to accept the [OAuth consent screen](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#configure_the_user_consent_screen_scopes_and_test_users) that was set up during instance creation.

## What's next

  * [Connect Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)
  * [Configure a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
