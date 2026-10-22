---
url: https://docs.cloud.google.com/docs/security/compromised-credentials/
title: Respond to compromised Google Cloud credentials \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:46.709287+00:00
---

# Respond to compromised Google Cloud credentials  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compromised-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Respond to compromised Google Cloud credentials Stay organized with collections  Save and categorize content based on your preferences. 

If you suspect that any of your credentials have been compromised, you must take immediate action to limit the impact of the compromise on your Google Cloud account.

Google Cloud credentials control access to your resources that are hosted on Google Cloud. Google Cloud includes both long-lived and short-lived credentials. To help keep your data secure and protected from attackers, you must handle your credentials with utmost care and respond quickly to any suspected compromise.

## Google Cloud credentials

The following table describes common Google Cloud credentials.

Credential | Description  
---|---  
[Service account private keys](https://docs.cloud.google.com/iam/docs/keys-create-delete) (JSON and p12 files) |  **Type:** Long-lived service credential **Typical locations:**

  * Developer workstations
  * Application server environments
  * Source code repositories
  * Secret management systems

**Remediation:** Service account keys and tokens  
[Service account tokens](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) (OAuth 2.0 access tokens) |  **Type:** Short-lived credential **Typical locations:**

  * Application runtime memory
  * Production workloads (fetched dynamically from instance metadata servers)
  * Developer workstations or CI/CD pipelines

**Remediation:** Service account keys and tokens  
[API keys](https://docs.cloud.google.com/docs/authentication/api-keys) |  **Type:** Long-lived service credential **Typical locations:**

  * Frontend source code
  * Backend configuration files
  * Secret management systems or environment variables

**Remediation:** API keys  
[OAuth 2.0 client ID secrets](https://developers.google.com/identity/protocols/oauth2) |  **Type:** Long-lived service credential **Typical locations:**

  * Web server backend configuration files
  * Secret management systems

**Remediation:** OAuth 2.0 client ID secrets  
[Google Cloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate) |  **Type:** Long-lived user credential **Typical location:** User's home directory. To list active credentials, run the `gcloud auth list` command. **Remediation:** User credentials and Google Cloud CLI OAuth tokens  
[OAuth access tokens for Google Cloud CLI](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials#overview-gcloud-oauth-tokens) |  **Type:** Short-lived credential **Typical location:** Developer workstations **Remediation:** User credentials and gcloud CLI OAuth tokens  
[Application Default Credentials](https://docs.cloud.google.com/docs/authentication#adc) |  **Type:** Long-lived user credential **Typical location:** Developer workstations **Remediation:** Application Default Credentials  
Browser cookies |  **Type:** Long-lived user credential **Typical location:** Browser-specific, but are typically stored on developer workstations **Remediation:** Browser cookies  
[Security Token Service federated access tokens for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation#access-management) |  **Type:** Short-lived credential **Typical locations:**

  * External workload runtime environments
  * CI/CD deployment pipelines

**Remediation:** Security Token Service federated access tokens  
[Security Token Service federated access tokens for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials) |  **Type:** Short-lived credential **Typical locations:**

  * Developer workstations
  * Third-party client applications and scripts

**Remediation:** Security Token Service federated access tokens  
  
## Protect your Google Cloud resources from a compromised credential

If you suspect a credential is compromised, revoke and reissue it. Proceed carefully to ensure you don't suffer a service outage as a result of revoking credentials.

In general, to reissue credentials, you generate a new credential, deploy it to all services and users that need it, and then revoke the old credential.

The following sections provide specific instructions for each type of credential.

### Service account keys and tokens

Complete the following steps to replace a compromised service account key and block compromised short-lived service account tokens.

[Short-lived service account tokens](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) exist separately from the credential or permission that was used to generate them and can't be revoked. Service account access tokens are bearer tokens and remain valid until their expiration time (by default, up to 60 minutes, or up to 12 hours if an [extended token lifetime policy](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) is configured).

Unlike access tokens that are granted to user identities, access tokens that are granted to service accounts can't be invalidated through the Admin console or commands like [`gcloud auth revoke`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke). Additionally, the session duration that you specify in [Google Cloud session control](https://support.google.com/a/answer/9368756) applies to user accounts in your Cloud Identity or Google Workspace directory, but not to service accounts. Therefore, your incident response for compromised service accounts needs to address both the persistent key files and the short-lived access tokens.

#### Required roles

To get the permissions that you need to respond to compromised service account keys and tokens, ask your administrator to grant you the following IAM roles: 

  * Manage service account keys: [Service Account Key Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) on the project that contains the service account 
  * Disable, enable, or delete service accounts: [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) on the project that contains the service account 
  * Apply deny policies to block active tokens: [Deny Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyAdmin) (`roles/iam.denyAdmin`) on organization 
  * Revoke impersonation roles: Project Identity and Access Management (IAM) Admin (`roles/resourcemanager.projectIamAdmin`), Service Account Admin (`roles/iam.serviceAccountAdmin`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to respond to compromised service account keys and tokens. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to respond to compromised service account keys and tokens:

  * Manage service account keys: 
    * `iam.serviceAccountKeys.create` on the project that contains the service account
    * `iam.serviceAccountKeys.delete` on the project that contains the service account
    * `iam.serviceAccountKeys.list` on the project that contains the service account
  * Disable, enable, or delete service accounts: 
    * `iam.serviceAccounts.disable` on the project that contains the service account
    * `iam.serviceAccounts.enable` on the project that contains the service account
    * `iam.serviceAccounts.delete` on the project that contains the service account
  * Apply deny policies to block active tokens: `iam.denypolicies.create` on the organization 
  * Revoke impersonation roles: 
    * `resourcemanager.projects.setIamPolicy` on the project
    * `iam.serviceAccounts.setIamPolicy` on the project that contains the service account



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Respond to compromised service account keys and tokens

  1. To block a compromised service account token, complete one of the following:

     * [Disable the service account](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#disabling) that the credential represents.

     * Apply an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-access#create-deny-policy) for the service account principal (`principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS`) on your projects or folders. The IAM deny policy denies access to sensitive APIs and permissions for active tokens and workloads so that you can investigate the incident without destroying the service account.

     * [Delete the service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete).

If you disable or delete the service account, any workload that uses the service account immediately loses access to your resources.

  2. To replace a compromised service account key, complete the following steps:

     1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Locate the affected service account.

     3. If required, create a new key for the service account and deploy the new key to all the locations in which the old key was in use.

     4. Disable the old key to verify that the new key works as expected.

     5. Delete the old key.

For more information, see [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).

  3. If unauthorized principals might have permission to generate tokens, revoke the Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) role. For instructions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  4. After the incident is resolved, wait at least 60 minutes after disabling the service account so that the compromised token can expire. If you set an extended lifetime policy using `constraints/iam.allowServiceAccountCredentialLifetimeExtension`, then wait the time that's specified in the constraint before re-enabling the service account.

  5. After the required wait time has passed, re-enable the service account and reset the deny policy.




### User credentials and gcloud CLI OAuth tokens

After an endpoint is compromised, determine how to respond to the primary threat of a compromised endpoint and the secondary threat of compromised tokens. If an attacker has persistent access to the developer workstation, they might copy tokens again after the legitimate user reauthenticates.

#### Required roles

To get the permissions that you need to revoke user access and invalidate gcloud CLI OAuth tokens in the Google Workspace Admin Console, ask your administrator to grant you the following Google Workspace administrator roles:

  * Manage third-party connected apps and session controls: [Security Admin](https://support.google.com/a/answer/2405986#security_admin) or [Super Admin](https://support.google.com/a/answer/2405986#super_admin)
  * Manage user credentials and sign-in sessions: [User Management Admin](https://support.google.com/a/answer/2405986#user_management) or [Super Admin](https://support.google.com/a/answer/2405986#super_admin)
  * Run the Admin SDK directory revocation script: [Super Admin](https://support.google.com/a/answer/2405986#super_admin) or a custom administrator role with Admin API privileges for User Management (`https://www.googleapis.com/auth/admin.directory.user.security`)



For more information about assigning administrator roles in Google Workspace, see [Assign admin roles in the Google Admin console](https://support.google.com/a/answer/172176).

#### Invalidate gcloud CLI tokens for specific user accounts

Complete the following steps to remove a user's access to gcloud CLI and invalidate any compromised tokens:

  1. To remove a user's access to Google Cloud CLI, complete one of the following:

     * As a Google Workspace administrator, remove access to Google Cloud CLI from the user's list of connected apps. For more information, see [View and remove access to third-party applications](https://support.google.com/a/answer/2537800#zippy=%2Cview-and-remove-access-to-third-party-applications).

     * Provide the following instructions to the user:

       1. Open the list of [apps with access to your Google Account](https://myaccount.google.com/permissions).

       2. Remove Google Cloud CLI from the list of connected apps.

When the user accesses Google Cloud CLI again, they are prompted to reauthorize the application.

  2. If you have extracted or intercepted a specific compromised token string (whether a refresh token or an access token), you can invalidate it directly using the Google OAuth 2.0 revocation endpoint:
         
         curl -d "token=TOKEN_STRING" \
           -H "Content-Type: application/x-www-form-urlencoded" \
           -X POST "https://oauth2.googleapis.com/revoke"
         

When you run this command to revoke a refresh token, you revoke both the refresh token and all associated access tokens. When you run this command to revoke an access token, you also invalidate the associated refresh token.

**Note:** Other methods, like suspending the user, resetting the user's password, or resetting sign-in cookies don't invalidate compromised access tokens that an attacker already controls. For example, if you suspend a user during an investigation but don't revoke gcloud CLI tokens, the access tokens might still be valid if the suspended user is restored before the access tokens expire.
  3. If you haven't already enforced [Google Cloud session control](https://support.google.com/a/answer/9368756), immediately enable this with a short reauthentication frequency. This control helps ensure that all refresh tokens expire at the end of the duration that you define, which limits the duration that an attacker can use the compromised tokens.




#### Invalidate gcloud CLI tokens for many user accounts

**Note:** This section applies only to user accounts in Google Workspace or Cloud Identity that have authorized the gcloud CLI. It doesn't invalidate tokens for service accounts or Security Token Service federated workloads.

If you suspect a breach but can't identify which users were affected, consider revoking active sessions for all users in your organization more quickly than the reauthentication policy allows.

This approach can be disruptive to legitimate users and terminate long-running processes that depend on user credentials. If you choose to adopt this approach, prepare a scripted solution for your security operations center (SOC) to run in advance and test it with a few users.

The following sample code uses the Google Workspace Admin SDK to identify all user identities in your Google Workspace or Cloud Identity account who have access to the gcloud CLI. If a user has authorized the gcloud CLI, the script revokes the refresh token and access token and forces the user to reauthenticate with their password or security key. For instructions on how to enable the Admin SDK API and run this code, see the [Google Apps Script quickstart](https://developers.google.com/admin-sdk/directory/v1/quickstart/apps-script).
    
    
    /**
     * Remove access to the Google Cloud CLI for all users in an organization
     * @see https://developers.google.com/admin-sdk/directory/reference/rest/v1/tokens
     * @see https://developers.google.com/admin-sdk/directory/reference/rest/v1/users
     * @see https://developers.google.com/apps-script/guides/services/advanced#enabling_advanced_services
     */
    
    function listUsersAndInvalidate() {
      const users = AdminDirectory.Users.list({
        customer: 'my_customer' // alias to represent your account's customerId
        }).users;
      if (!users || users.length === 0) {
        Logger.log('No users found.');
        return;
      }
      for (const user of users){
        let tokens = AdminDirectory.Tokens.list(user.primaryEmail).items
        if (!tokens || tokens.length === 0) {
          continue;
        }
        for (const token of tokens) {
          if (token.clientId === "32555940559.apps.googleusercontent.com") {
            AdminDirectory.Tokens.remove(user.primaryEmail, token.clientId)
            Logger.log('Invalidated the tokens granted to gcloud for user %s', user.primaryEmail)
          }
        }
      }
    }

### Application Default Credentials

If you suspect that an Application Default Credential is compromised, you can revoke it. This procedure can cause a temporary outage until the credentials file is recreated.

#### Required roles

To get the permissions that you need to remove connected application access in the Google Workspace Admin Console, ask your administrator to grant you the [Security Admin](https://support.google.com/a/answer/2405986#security_admin) or [Super Admin](https://support.google.com/a/answer/2405986#super_admin) role.

Local commands run on developer workstations don't require administrator roles. For more information about assigning administrator roles in Google Workspace, see [Assign admin roles in the Google Admin console](https://support.google.com/a/answer/172176).

#### Revoke Application Default Credentials

Complete one of the following:

  * As a Google Workspace administrator, remove access to the Google Auth Library from the user's list of connected apps. For more information, see [View and remove access to third-party applications](https://support.google.com/a/answer/2537800#zippy=%2Cview-and-remove-access-to-third-party-applications).

  * Instruct the owner of the compromised credential to complete the following:

    1. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk), if you haven't already.

    2. Revoke the credentials:
           
           gcloud auth application-default revoke
           

    3. If you can't run gcloud CLI, complete the following:

       1. Revoke access to Google Auth Library using [myaccount.google.com/permissions](https://myaccount.google.com/permissions) or the [OAuth 2.0 revocation endpoint](https://oauth2.googleapis.com/revoke).

       2. Manually delete the `application_default_credentials.json` file:

          * Linux, macOS: `$HOME/.config/gcloud/application_default_credentials.json`
          * Windows: `%APPDATA%\gcloud\application_default_credentials.json`
    4. Recreate the credentials file with your user identity:
           
           gcloud auth application-default login
           




### API keys

Complete the following steps to regenerate a compromised API key.

#### Required roles

To get the permissions that you need to manage API keys, ask your administrator to grant you the [API Keys Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.apiKeysAdmin) (`roles/serviceusage.apiKeysAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage API keys. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage API keys:

  * `apikeys.keys.create`
  * `apikeys.keys.delete`
  * `apikeys.keys.update`
  * `apikeys.keys.getKeyString`
  * `apikeys.keys.list`
  * `apikeys.keys.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Regenerate an API key

  1. In the Google Cloud console, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click the name of the API key that you want to rotate.

  3. Click **Rotate key**.

  4. Enter a name and confirm restrictions.

  5. Click **Create**.

  6. Update applications to use the new API key.

  7. In **Previous key** , click **Delete the previous key**.




For more information, see [Rotate an API key](https://docs.cloud.google.com/docs/authentication/api-keys#rotate).

### OAuth 2.0 client ID secrets

Changing a client ID secret causes a temporary outage while the secret is rotated.

#### Required roles

To get the permissions that you need to reset OAuth 2.0 client ID secrets, ask your administrator to grant you the [OAuth Config Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to reset OAuth 2.0 client ID secrets. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to reset OAuth 2.0 client ID secrets:

  * `clientauthconfig.clients.createSecret`
  * `clientauthconfig.clients.getWithSecret`
  * `clientauthconfig.clients.update`
  * `clientauthconfig.clients.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Reset an OAuth 2.0 client ID secret

  1. In the Google Cloud console, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Select the compromised OAuth 2.0 client ID and edit it.

  3. Click **Reset Secret**.

  4. Deploy the new secret to your application.




For more information, see [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849) and [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2).

### Security Token Service federated access tokens

When external identity sessions are compromised, you must stop new token exchanges and revoke active federated access tokens. This task applies to access tokens that are issued by Workload Identity Federation or Workforce Identity Federation.

#### Required roles

To get the permissions that you need to manage Workload Identity Federation and Workforce Identity Federation to block federated tokens, ask your administrator to grant you the following IAM roles: 

  * Manage workload identity pools and providers: [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`) on the project that contains the workload identity pool 
  * Manage workforce identity pools and providers: [Workforce Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) (`roles/iam.workforcePoolAdmin`) on the organization that contains the workforce identity pool 
  * Apply deny policies to block active tokens: [Deny Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyAdmin) (`roles/iam.denyAdmin`) on the organization 
  * Manage service account impersonation: [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) on the project that contains the service account 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage Workload Identity Federation and Workforce Identity Federation to block federated tokens. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage Workload Identity Federation and Workforce Identity Federation to block federated tokens:

  * Manage workload identity pools and providers: 
    * `iam.workloadIdentityPools.update` on the project that contains the workload identity pool
    * `iam.workloadIdentityPoolProviders.update` on the project that contains the workload identity pool
  * Manage workforce identity pools and providers: 
    * `iam.workforcePools.update` on the organization that contains the workforce identity pool
    * `iam.workforcePoolProviders.update` on the organization that contains the workforce identity pool
  * Apply deny policies to block active tokens: 
    * `iam.denypolicies.create` on the organization
    * `iam.denypolicies.update` on the project, folder, or organization
  * Manage service account impersonation: `iam.serviceAccounts.setIamPolicy` on the project that contains the service account 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Block federated access tokens

  1. Complete one of the following:

     * To block new token exchanges, disable the [workload identity pool provider](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers#update-provider) or the [workforce identity pool provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider).

     * To block new token exchanges and active tokens across an entire pool, [disable the workload identity pool](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers#update-pool) or [disable the workforce identity pool](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update).

  2. To block immediate access for active bearer tokens (which are valid for up to one hour), complete one of the following:

     * To block direct resource access, revoke the IAM roles for the affected [principal or principalSet](https://docs.cloud.google.com/iam/docs/principal-identifiers), or apply a temporary [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-access#create-deny-policy).

     * If the federated identity impersonates a service account (`roles/iam.workloadIdentityUser`), complete Service account keys and tokens. To avoid future impersonation issues, remove the impersonation role binding.

  3. In your identity provider, rotate the compromised credentials, revoke active sessions, or delete the compromised entity.




### Browser cookies

Complete the following steps to invalidate browser cookies for a user.

#### Required roles

To get the permissions that you need to sign a user out and force a password change in the Google Workspace Admin Console, ask your administrator to grant you the [User Management Admin](https://support.google.com/a/answer/2405986#user_management) or [Super Admin](https://support.google.com/a/answer/2405986#super_admin) role.

For more information about assigning administrator roles in Google Workspace, see [Make a user an admin](https://support.google.com/a/answer/172176).

#### Invalidate browser cookies

If you suspect browser cookies are compromised, complete one of the following:

  * As a Google Workspace administrator, [sign a user out](https://support.google.com/a/answer/178854) of their account and immediately [force a password change](https://support.google.com/a/answer/33319).

  * Instruct the user to sign out of their [Google Account](https://accounts.google.com) and change their password immediately.




These actions invalidate all existing cookies, and the user is asked to sign in again.

## Investigate unauthorized access and resources after revoking credentials

After you revoke compromised credentials and restore your service, review all access to your Google Cloud resources. You can use Cloud Logging or Security Command Center.

### Required roles

To get the permissions that you need to investigate unauthorized access and resources, ask your administrator to grant you the following IAM roles: 

  * View audit logs in Logging: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project, folder, or organization 
  * View Data Access audit logs in Logging: [Private Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`) on the project, folder, or organization 
  * View findings in Security Command Center: [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`) on the project or organization 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to investigate unauthorized access and resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to investigate unauthorized access and resources:

  * View audit logs in Logging: 
    * `logging.logEntries.list` on the project, folder, or organization
    * `logging.views.access` on the project, folder, or organization
  * View Data Access audit logs in Logging: `logging.privateLogEntries.list` on the project, folder, or organization 
  * View findings in Security Command Center: 
    * `securitycenter.findings.list` on the project or organization
    * `securitycenter.findings.get` on the project or organization



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Investigate unauthorized access and resources

In Logging, complete the following:

  1. Examine your [audit logs](https://docs.cloud.google.com/logging/docs/audit) in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Search all potentially affected resources, and make sure that all account activity (especially related to the compromised credentials) is as expected.

For example, complete the following:

     * Search for all API calls that were initiated by the compromised identity during the incident window.
     * If the identity had impersonation privileges, search for actions where `protoPayload.authenticationInfo.serviceAccountDelegationInfo.firstPartyPrincipal.principalEmail` matches the compromised principal.
     * Check if new service account keys, new user accounts, or project-level SSH keys were created during the incident.



In Security Command Center, complete the following:

  1. In the Google Cloud console, go to the Security Command Center **Findings** page. 

[ Go to Findings](https://console.cloud.google.com/security/command-center/findings)

  2. If necessary, select your Google Cloud project or organization.

  3. In the **Quick filters** section, click an appropriate filter to display the finding that you need in the **Findings query results** table. For example, if you select **Event Threat Detection** or **Container Threat Detection** in the **Source display name** subsection, only findings from the selected service appear in the results.

The table is populated with findings for the source you selected.

  4. To view details of a specific finding, click the finding name under **Category**. The finding details pane expands to display a summary of the finding's details.

  5. To display all findings that were caused by the same user's actions:

     1. On the finding details pane, copy the email address next to **Principal email**.
     2. Close the pane.
     3. In **Query editor** , enter the following query:
            
            access.principal_email="USER_EMAIL"
            

Replace USER_EMAIL with the email address that you previously copied.

Security Command Center displays all findings that are associated with actions taken by the user that you specified.




## Delete all unauthorized resources

Make sure that there are no unexpected resources, such as VMs, App Engine apps, service accounts, and Cloud Storage buckets, that the compromised credential could access.

After you identify all unauthorized resources, you can delete these resources immediately. Immediate action is especially important for Compute Engine resources, because attackers can use compromised accounts to exfiltrate data or otherwise compromise your production systems.

To delete unauthorized resources, see the following documentation:

  * [Delete a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)
  * [Delete a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets)
  * [Delete a service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#deleting)



Alternatively, you can try to isolate unauthorized resources to allow your own forensics teams to perform additional analysis.

## Contact Customer Care

For help with finding the Google Cloud logs and tools that you require for your investigation and mitigation steps, contact [Cloud Customer Care](https://docs.cloud.google.com/support) and open a [support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case).

## Handle account lockouts

If you are completely locked out of your account, consider the following options:

  * Use the [Google Workspace Account Recovery Form](https://support.google.com/a/contact/recovery_form), which is available in the Google Workspace Admin Toolbox. For more information, see [Recovering administrator access to your account](https://knowledge.workspace.google.com/admin/users/recovering-administrator-access-to-your-account).

  * If an attacker is creating fraudulent resources while you are completely locked out and you have a support entitlement, complete the following:

    1. In an Incognito window, browse to [Support Contact Troubleshooter](https://support.google.com/cloud/troubleshooter/9664343).

    2. Select **Yes** and click **File a ticket**.

    3. Complete and submit the form with your details.

  * If an attacker is creating fraudulent resources while you are completely locked out and you don't have a support entitlement, complete the following:

    1. In an Incognito window, browse to [Support Contact Troubleshooter](https://support.google.com/cloud/troubleshooter/9664343).

    2. Answer the questions as follows:

Troubleshooter question | Required selection  
---|---  
Do you have a support entitlement? | No  
Are you currently in your free trial period? | No  
Are you the billing administrator of a GCP (Google Cloud) Billing Account? | No  
Are you encountering any of these situations? | I can no longer access my GCP project or billing account and need to regain access.  
    3. Click **File a ticket with our access recovery team**.

    4. Complete and submit the unauthenticated contact form with your details, including any billing account IDs or payment indicators that you can provide to verify your identity.




## What's next

Implement the following best practices to help you avoid compromised credentials:

  * Best practices related to authentication failures in [Mitigate OWASP Top 10:2025 on Google Cloud](https://docs.cloud.google.com/docs/security/owasp-top-ten-mitigation). For example, ensure that you separate credentials from code and use Secret Manager to store and manage secrets.

  * [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

  * [Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
