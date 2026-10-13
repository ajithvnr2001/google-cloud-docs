---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider/
title: Configure identity provider \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:07.113362+00:00
---

# Configure identity provider  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure identity provider Stay organized with collections  Save and categorize content based on your preferences. 

To enforce data source access control and secure data in Gemini Enterprise, you must configure an identity provider. This involves setting up the identity provider and managing permissions for your data sources. Google uses your identity provider to identify the end user performing a search and determine if they have access to the documents that are returned as results.

## Choose your identity provider type

The type of the identity provider you choose, depends on the data sources connected to your Gemini Enterprise app. Gemini Enterprise supports the following options:

Identity provider type  |  When to use   
---|---  
**Google Identity** |  Google Identity is the recommended identity provider for Gemini Enterprise.   
  
Google Identity supports: 

  * **All first-party Google data sources** that use data ingestion or data federation. You must use [Google Identity](https://developers.google.com/identity) when connecting to [Google Workspace](https://workspace.google.com/) data sources.
  * **All third-party data sources that use data federation** , where users authenticate directly with the third-party service using OAuth.
  * **All third-party data sources that use data ingestion** , with the exception of Microsoft 365 data sources, such as SharePoint, OneDrive, or Outlook, which require Microsoft Entra ID and Workforce Identity Federation.

**Note:** To use a third-party identity provider with Google Identity, your identity provider must support OIDC or SAML 2.0.  Before configuring Google Identity, determine the unique user attribute that your organization uses, which is typically the user's email. If users have more than one email address, you must [add an email alias](https://support.google.com/a/answer/33327).   
**Third-party identity provider** |  When you connect Gemini Enterprise only to third-party data sources and you already use a third-party identity provider that supports OIDC or SAML 2.0, such as Microsoft Entra ID, Okta, or AD FS, you can use either [Google Identity](https://docs.cloud.google.com/identity/docs/overview) or Workforce Identity Federation. **Note:** Microsoft 365 data sources that connect using data ingestion require Microsoft Entra ID and Workforce Identity Federation.  Google recommends using Google Identity for new setups. Existing customers already using Workforce Identity Federation can choose to remain on Workforce Identity Federation. For more information, see [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).   
  
Before configuring Workforce Identity Federation, determine the unique user attributes that your organization uses and map them to Workforce Identity Federation.   
**Caution:** If you change identity providers, users lose their existing chat history. Because chat history is tied to users' IDs from the original identity provider, switching providers gives users new IDs and effectively a fresh start. Chat history linked to their original IDs can't be retrieved.

## Access control for Google Workspace connectors

When you use enterprise data grounding and search with Google Workspace connectors (such as **People from Google Workspace** or **Google Groups**), Gemini Enterprise strictly respects the source system's access control lists (ACLs) and permissions.

### Core principle: No privilege escalation

A user interacting with Gemini Enterprise can only view and ground responses on information that they are already authorized to access directly in the source Google Workspace application. Gemini Enterprise never bypasses source system access controls or grants additional permissions.

  * **People from Google Workspace (Directory):** User visibility in search and grounding results respects your organization's Directory visibility settings. For example, if a user's visibility in the Google Workspace Directory is limited to their own department or organizational unit, they are only able to find colleagues within that department using Gemini Enterprise. They can't view profiles of employees in restricted departments.

  * **Google Groups:** Content discovery and grounding adhere to group membership and access settings. A user can only search and view content from Google Groups that they are a member of and have permission to view. Non-members can't discover or view discussions from private groups through Gemini Enterprise.




### Where to manage permissions

You don't configure access control and visibility settings in the Gemini Enterprise connector settings in the Google Cloud console. Instead, a Google Workspace administrator configures permission, membership, and visibility settings in the source system:

  * **User profile visibility:** The Google Workspace administrator configures user profile visibility in the Google Admin console. For more information, see [Set up directory sharing](https://support.google.com/a/answer/1628008).

  * **Group access and membership:** The Google Workspace administrator configures group access and membership in Google Groups or the Google Admin console. For more information, see [Set up and manage groups](https://support.google.com/a/answer/167097).




## Workforce Identity Federation for third-party identity providers

This section describes how to configure Workforce Identity Federation for third-party identity providers. Optionally, you can verify if the Workforce Identity Federation set up works as expected.

**Important:** The workforce identity pool admin roles give the administrators powerful permissions. For more information, see [Workforce Identity Federation and pool administrators](https://docs.cloud.google.com/gemini/enterprise/docs/security-overview#pool-admins).

### Configure Workforce Identity Federation

For details on configuring Workforce Identity Federation with your third-party identity connector, see the following resources:

Identity provider | Resources  
---|---  
**Entra ID** |  **Note:** When using data ingestion to connect to Microsoft data sources like SharePoint, OneDrive, or Outlook, you must use Microsoft Entra ID groups to control document access. This requires setting up Workforce Identity Federation with Microsoft Entra ID. This setup is necessary even if you use a different identity provider for single sign-on (SSO) with Microsoft Entra ID. However, this requirement does not apply if you are connecting to a Microsoft data source using data federation. 

  * [Configure Workforce Identity Federation with Microsoft Entra ID and sign in users](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id)
  * [Configure Workforce Identity Federation with Microsoft Entra ID and a large number of groups](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups)
  * [Configure SCIM in Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/configure-scim-ms-entra). SCIM (System for Cross-domain Identity Management) is necessary to fetch a large number of groups from Entra ID for Gemini Enterprise and for autocomplete of user emails and group names when users share agents and notebooks. 

  
**Okta** | 

  * [Configure Workforce Identity Federation with Okta and sign in users](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta)
  * [Configure SCIM in Okta](https://docs.cloud.google.com/iam/docs/configure-scim-okta). SCIM is necessary for autocomplete of user emails and group names when users share agents and notebooks.

  
**OIDC or SAML 2.0** | 

  * [Configure Workforce Identity Federation with an identity provider (IdP) that supports OIDC or SAML 2.0](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation)

  
  
#### Configure attribute mapping

Attribute mapping helps you connect your third-party identity information with Google using Workforce Identity Federation.

When configuring attribute mapping in Workforce Identity Federation, consider the following:

  * The `google.subject` attribute is used for attribute mapping, license assignment, and sharing notebooks. We recommend mapping `google.subject` to the user's email address in lowercase, as license assignment is case sensitive.

  * If your organization has more than one unique identifier, map these unique organizational attributes using the `attribute.as_user_identifier_number between 1 and 50` attribute.

For example, if your organization uses both email and principal name as user identifiers across different applications, and the principal name is set as the `preferred_username` in your third-party identity provider, you can map it to Gemini Enterprise using the Workforce Identity Federation attribute mapping (for example, `attribute.as_user_identifier_1=assertion.preferred_username`).




The following examples show the required attribute mappings for common identity providers. You can add more attribute mappings to support additional unique identifiers, as described previously.

  * [Entra ID with OIDC protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad#create-oidc-provider)   
This example uses the email to uniquely identify users.
        
        google.subject=assertion.email.lowerAscii()
        google.groups=assertion.groups
        google.display_name=assertion.given_name
        

  * [Entra ID with SAML protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad#create-saml-provider)   
This example uses the email to uniquely identify users.
        
        google.subject=assertion.attributes['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress'][0].lowerAscii()
        google.groups=assertion.attributes['http://schemas.microsoft.com/ws/2008/06/identity/claims/groups']
        google.display_name=assertion.attributes['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname'][0]
        

  * [Okta with OIDC protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-oidc-provider)   
This example uses the email to uniquely identify users.
        
        google.subject=assertion.email.lowerAscii()
        google.groups=assertion.groups
        

  * [Okta with SAML protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-saml-provider)   
This example uses the subject assertion of the JWT to uniquely identify users.
        
        google.subject=assertion.subject.lowerAscii()
        google.groups=assertion.attributes['groups']
        




### Optional: Verify Workforce Identity Federation setup

To verify successful sign-ins and correct attribute mapping using the Workforce Identity Federation audit logging feature, do the following:

  1. Enable audit logs for the Data Access activity's Security Token Service API.

     1. In the Google Cloud console, go to the **Audit Logs** page: 

[Go to **Audit Logs**](https://console.cloud.google.com/iam-admin/audit)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. Select an existing Google Cloud project, folder, or organization.
     3. Enable the Data Access audit logs. 
        1. See the Logging documentation for detailed steps on how to [Enable audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable).
        2. For the **Security Token Service API** , select the **Admin Read** audit log type. For more information, see [Example logs for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workforce-identity).
  2. Enable detailed logging in your workforce pool. The Workforce Identity Federation extended groups feature for Microsoft Entra ID doesn't produce detailed audit logging information.

     1. Go to the **Workforce Identity Pools** page:

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools)

     2. In the table, select the pool.

     3. Click the **Enable detailed audit logging** toggle to the on position.

     4. Click **Save Pool**.

  3. In the **Providers** section, click the **Sign in URL** for your provider, and sign in to Google Cloud console as a workforce pool user.

  4. See the audit logs that generated when you signed in.

     1. Go to the **Workforce Identity Pools** page:

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools)

     2. In the table, select the pool you signed into.

     3. Click **View** next to **Logs**.

     4. On the audit log page clear the `protoPayload.resourceName` filter from the query.

     5. Click **Run query**. 

  5. Check the audit logs for an entry with the `google.identity.sts.SecurityTokenService.WebSignIn` method that matches the sign-in timestamp.

  6. Confirm that the `metadata.mapped_attributes` field in the log matches the attribute that you used when configuring Workforce Identity Federation for third-party identity providers.

For example:
         
         "metadata": {
           "mapped_attributes": {
             "attributes.as_user_identifier_1": "alex@admin.altostrat.com"
             "google.subject": "alex@altostrat.com"
             "google.groups": "[123abc-456d, efg-h789-ijk]"
           }
         },
         




## Limitations

When connecting your data sources using a connector to create data stores, the following limitations apply:

  * 3000 readers are allowed per document. Each principal counts as a reader, where a principal can be a group or an individual user.

  * You can select one identity provider type per location supported in Gemini Enterprise.

  * If the identity provider settings are updated by changing the identity provider type or the workforce pool, existing data stores won't automatically update to the new settings. You must delete and recreate these data stores to apply the new identity settings.

  * To set a data source as access-controlled, you must select this setting during data store creation. You can't turn this setting on or off for an existing data store.

  * To preview UI results for search apps that use third-party access control, you must sign in to the federated console or use the web app. See [Preview your app](https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise#preview_your_app).




## Connect to your identity provider

The following section describes how to connect to your identity provider using Google Cloud console.

#### Before you begin

Before connecting the identity provider, do the following:

  * [Grant permissions to admins](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant_permissions_to_admins).

  * If you are connecting a third-party identity provider using Workforce Identity Federation, configure Workforce Identity Federation.




#### Connect identity provider

To specify an identity provider for Gemini Enterprise and turn on data source access control, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/apps)

  2. Click **Settings** > **Authentication**.

  3. Click **Add identity provider** for the location you want to update.

  4. Click **Add identity provider** and select your identity provider type.   
If you select **3rd party identity** , you also need to select the workforce pool that applies for your data sources.

  5. Click **Save changes**.




## Grant permissions to users

Users need the Gemini Enterprise User (`roles/discoveryengine.agentspaceUser`) role to access, manage, and share apps.

Identity provider type  |  Description   
---|---  
**Google Identity** | 

  * If you use Google Identity, Google recommends creating a [Google group](https://groups.google.com) that includes all employees who use the app. 
  * If you're a Google Workspace administrator, you can include all users in an organization to a Google group by following the steps in [Add all your organization's users to a group](https://support.google.com/a/answer/9689259). 
  * Grant the Gemini Enterprise User (`roles/discoveryengine.agentspaceUser`) role to users. For more information on adding the role, see [Grant permissions to your users](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant-role). 

  
**Third-party identity provider** | 

  * Grant the Gemini Enterprise User (`roles/discoveryengine.agentspaceUser`) role to your users and [workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users). For more information on adding the role, see [Grant permissions to your users](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant-role). 
  * Google recommends configuring group claims for your third-party identities. 

  
  
## Impact of identity provider setting changes on ingestion connectors

When you change identity settings, such as the identity provider or Workforce Identity Federation pool, existing data stores that use data ingestion are not automatically updated. To apply the new identity settings, you must delete and recreate the affected data stores.

The following table summarizes which identity setting changes require data store recreation:

Change type | Requires data store recreation  
---|---  
Switching between Google Identity and a third-Party identity provider  | Yes  
Completely changing to a new Workforce Identity Federation pool  | Yes  
Editing attribute mapping within the current identity provider  | No  
Switching to a new provider within the same Workforce Identity Federation pool. For example, using Entra instead of Okta.  | No  
  
## User identity changes

Gemini Enterprise associates a user's chat history, notebooks, and the agents that the user creates with the user's principal identifier. If you use Workforce Identity Federation, the principal identifier includes the value that your attribute mapping assigns to `google.subject`. For example:
    
    
    principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE

### Impact of a subject value change

If the value that's mapped to `google.subject` changes for a user, then Gemini Enterprise treats the user as a new user. For example, this happens when the user's user principal name (UPN) or email address changes in Microsoft Entra ID and your attribute mapping uses that attribute. Principal identifiers are case-sensitive, so a change in letter case is also a change.

After the change, the following applies:

  * The user can't access the chat history, notebooks, or agents that are associated with the previous principal identifier.
  * Gemini Enterprise doesn't migrate data from the previous principal identifier to the new principal identifier.
  * Licenses and IAM roles that are granted to the previous principal identifier don't apply to the new principal identifier.



### Prepare for a subject value change

To reduce the impact of a subject value change, do the following:

  * Before you change a user's UPN or email address in your identity provider, inform the user and ask them to [share any private agents](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents) or notebooks that they want to keep.
  * Assign a Gemini Enterprise license to the new principal identifier, and grant the required roles to it. For more information, see Grant permissions to users.
  * [Transfer ownership of the agents](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents#transfer-ownership) that the user shared with others to the new principal identifier. You can't transfer ownership of agents that aren't shared.



## Troubleshoot authentication errors

If users get HTTP `401` errors that report invalid authentication credentials when they access Gemini Enterprise, check the following.

### Basic checks

  * **Browser state** : Ask the user to clear the browser cache and cookies, or to sign in from an incognito or private browsing window.
  * **Signed-in account** : Make sure that the user signs in with the account that your identity provider configuration expects. If you use Workforce Identity Federation, the user's identity must match your attribute mapping.
  * **Device clock** : Make sure that the device clock is synchronized, for example, by using Network Time Protocol (NTP). Clock drift on the device can cause authentication to fail.



### Network and identity provider policies

  * **Proxies and firewalls** : Proxies, firewalls, or secure web gateways that inspect TLS traffic can remove or change the `Authorization` header. Make sure that these devices don't modify requests to Google domains.
  * **Identity provider access policies** : Check whether access policies in your identity provider, such as Conditional Access policies in Microsoft Entra ID, block sign-in because of device compliance, IP address ranges, or location.
  * **Context-Aware Access** : If your organization uses Context-Aware Access with Google Cloud or Google Workspace, check whether an IP-based access level blocks the requests that Gemini Enterprise makes on the user's behalf. These requests originate from Google's servers, not from the user's network, so they don't match corporate IP ranges. Add an access level that allows the OAuth 2.0 client ID used by Gemini Enterprise, combined with the IP-based access level as an OR condition. Denied requests appear in your organization's audit logs for `contextawareaccess.googleapis.com`.
  * **DNS resolution** : Make sure that your DNS resolvers correctly resolve Google domains, including `*.google.com` and `*.googleapis.com`.



### Collect diagnostic information

If the error persists, capture a HAR (HTTP Archive) file and the browser console logs while you reproduce the error, and then contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs). HAR files can contain sensitive information, such as cookies and tokens. 

## What's next?

  * If you have Cloud Storage or BigQuery data stores and you want to enforce access control on the data, then you must [configure access controls for custom data sources](https://docs.cloud.google.com/gemini/enterprise/docs/identity).

  * If you connect to your own custom data source, learn how you can [set up external identities](https://docs.cloud.google.com/gemini/enterprise/docs/identity-mapping).

  * [Preview your app](https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise#preview_your_app).

  * When you are ready to share the app with your users, you can turn on the app and share the URL with your user. Users need to sign in before they can access the app. For more information, see [View the search web app](https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise#view_the_search_web_app).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
