---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people/
title: Sync people data from Google Workspace \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:35.720498+00:00
---

# Sync people data from Google Workspace  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Sync people data from Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

You can set up people search for your work teams by syncing people data from Google Workspace. After the people search data store is set up and the data is ingested into the Gemini Enterprise index, it enables features such as [Knowledge Graph and Natural Language Processing](https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search). This improves search quality, letting you find people in your Google Workspace Directory through the web app.

For information about Google Workspace Directory, see the Google Workspace documentation:

  * [Overview: Set up and manage the Directory](https://support.google.com/a/answer/1628009)
  * [Add information to a user's Directory profile](https://support.google.com/a/answer/6191788)

**Note:** If your people data is not in Google Workspace, you can import it from Cloud Storage or BigQuery. For information, see [Import people data from a custom source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people-custom).

### Before you begin

Before you can set up a people search data store, you must do the following:

  * To enforce data source access control and secure data in Gemini Enterprise, make sure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider). Gemini Enterprise strictly respects the source system's permissions and directory visibility settings. Users can only view directory profiles that they are authorized to access in Google Workspace Directory (no privilege escalation).

  * A Google Workspace administrator must enable people search on Google Workspace data:

    1. Sign in to the [Google Admin console](https://admin.google.com/) with an administrator account.
    2. Go to **Directory** > **Directory settings**.
    3. Turn on **Contact sharing**.
  * Sign in to the Google Cloud console with the same account that you use for Google Workspace.



  * If you use security controls, be aware of their limitations related to data in Google Workspace, as discussed in the following table:

Security control | Note the following  
---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/gemini/enterprise/docs/locations) | Gemini Enterprise only guarantees data residency in Google Cloud. For information about data residency and Google Workspace, see Google Workspace compliance guidance and documentation, including [Data regions for Google Workspace](https://support.google.com/a/answer/9223653). Also review examples like [Choose the region where data is stored](https://support.google.com/a/topic/7631290) and [ Digital sovereignty](https://workspace.google.com/intl/en_in/security/digital-sovereignty/).   
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek) |  Your keys only encrypt data within Google Cloud. Cloud Key Management Service controls don't apply to data stored in Google Workspace.   
[ Access Transparency](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency) |  Access Transparency logs actions taken by Google personnel on the Google Cloud project. You'll also need to review the Access Transparency logs created by Google Workspace. For more information, see [Access Transparency log events](https://support.google.com/a/answer/9230979) in the Google Workspace Admin Help documentation.   



Before creating the people data store, you need to set up a service account and domain-wide delegation.

### Set up the service account

  1. Verify that you have the permissions you need to create a service account. See [Required roles](https://docs.cloud.google.com/iam/docs/service-accounts-create#permissions).

  2. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) in a Google Cloud project within the organization.

  3. Optional: Skip the **Grant this service account access to project (optional)** step.

![Shows the Grant this service account access to project \(optional\) section that needs to be skipped.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/skip-grant-this-service-account-access-to-project.png) Skip the Grant this service account access to project (optional) step. 

  4. Grant the Discovery Engine service account (`service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`) access as a **Service account token creator** (`roles/iam.serviceAccountTokenCreator`), and click **Save**.

![Shows how to configure the Grant users access to this service account section.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/grant-the-discovery-engine-service-account-access.png) Grant the Discovery Engine service account access. 

  5. After the service account is created, click the **Details** tab of the service account, and click **Advanced settings**.

  6. Copy the client ID for domain-wide delegation.

![Shows the client ID in the advaced settings, domain-wide delegation section. ](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/copy-client-id.png) Copy the client ID. 




### Set up domain-wide delegation

  1. Sign in to the [Google Workspace Admin console](https://admin.google.com).
  2. Navigate to **Security** > **Access and data control** > **API controls**.
  3. Click **Manage domain wide delegation**.

![Shows Manage domain wide delegation. ](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/manage-domain-wide-delegation.png) Click Manage domain wide delegation. 

  4. Click **Add new**.

![Highlights the add new link. ](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/add-new.png) Click Add new. 

  5. In the **Add a new client ID** dialog, do the following:

     1. **Client ID** : Enter the client ID.
     2. **OAuth scopes** : Enter `https://www.googleapis.com/auth/directory.readonly`.
     3. Click **Authorize**.

![Configure the domain-wide delegation settings.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/configure-domain-wide-delegation-settings.png) Configure the domain-wide delegation settings. 




### Configure custom attributes

If you have custom people data (also known as custom attributes) and want the custom attribute data to appear in search results, do the following:

  1. Sign in to the [Google Workspace Admin console](https://admin.google.com).

  2. Click **Directory > Users > More options > Manage custom attributes**.

![Manage custom people data attributes.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/people-search-manage-custom-attributes.png) Click Manage custom attributes. 

  3. To make the custom attribute searchable, set **Visibility** for the attribute to **Visible to organization**.

![Set the visibility of the custom attribute to Visible to org
anization.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/people-search-visible-to-organization.png) Set the visibility of the custom attribute to Visible to organization to make it searchable. 




### Connect using OAuth

Connecting with OAuth offers an alternative to domain-wide delegation for authenticating your people search connector. This method requires you to create an OAuth client to authorize the connector to access your organization's directory data. The following steps guide you through creating the client, setting up the connector, and updating the credentials.

  1. Create an OAuth client

     1. Navigate to the Google Cloud console and search for `Credentials`.

     2. Click add **Create Credentials**.

![Click create credentials button.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/create-cred.png)Create credentials.

     3. Select **OAuth client ID** from the drop-down menu.

![Select the OAuth client ID.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/oauth-client-id.png)Select the OAuth client ID.

     4. Select **Web application** from the **Application type** drop-down menu.

![Select the web application option.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/webapp.png)Select the web application option.

     5. Add a name for the OAuth client ID and enter the authorized redirect URI as `https://vertexaisearch.cloud.google.com/oauth-redirect`.

     6. Click **Create** and save the credentials.




### Create a people search data store

To connect your people data to Gemini Enterprise, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data Stores** page.

  3. Click add **Create Data Store**.

  4. On the **Select a data source** page, click **People search**.

![Select the People Search data store.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/source-page.png)Select the People Search data store.

  5. Configure the authentication details:

You can authenticate using either an OAuth 2.0 refresh token or domain-wide delegation.

     * Using an OAuth 2.0 refresh token:

       1. Select **OAuth 2.0 refresh token** and add the client ID and client secret you created in the previous steps.

       2. Click the **Authenticate** button to give consent for the scope `https://www.googleapis.com/auth/directory.readonly`.

       3. Provide a name for the connector and click **Create**.

     * Using domain-wide delegation:

       1. Select **Domain-wide delegation**.

       2. Enter the service account email and the private key that you generated.

       3. Click **Continue**.

  6. Update the connector credentials:

You must update your client credentials if your OAuth refresh token has expired, or if you want to switch credential flows for ingesting documents. This process is necessary when you switch from domain-wide delegation to OAuth, or from OAuth back to domain-wide delegation.

     1. Navigate to the People Search connector.

     2. Click **Re-authenticate**.

![Click the Re-authenticate button.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/reauth.png)Click the Re-authenticate button.

     3. Choose the credential flow that you want to use.

![Click the credential flow.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/oauth-refresh-token.png)Click the credential flow. 

     4. Add the new credentials and click **Authenticate**.

     5. Enter the email address of the account that fetches the people data. If you prefer not to use an administrator account, you can use an alternate account that has access to the organization's directory data.

     6. Enter the service account email you created previously.

     7. Click **Continue**.

![Configure the authentication details.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/people-search-connector-images/configure-authentication-details.png)Configure the authentication details.

  7. Choose a region for your data store.

  8. In the **Your data store name** field, enter a name for your data store.

  9. Click **Create**.

Syncing might take several minutes to hours, depending on data size.




## Error messages

The following table describes error messages that you might encounter when syncing people data by using data indexing. This table includes gRPC error codes and suggested troubleshooting steps. 

Error Code (gRPC) | Error Message | Description | Troubleshooting  
---|---|---|---  
9 (Failed precondition) | Authentication failed: Service account misconfigured. Ensure that the Discovery Engine service account has the service account token creator role and that the domain wide delegation (DWD) service account auth scope is set up correctly on Google Cloud Admin. All documents have been deleted from Gemini Enterprise. | This error occurs when the Discovery Engine service account lacks the service account token creator role, or the domain-wide delegation (DWD) service account lacks the correct auth scope. | Verify that the Discovery Engine service account has the service account token creator role as described in the [Set up the service account](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people#service-account) section and verify that the DWD service account auth scope is set up correctly on Google Cloud Admin as described in the [Set up domain-wide delegation](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people#domain-delegation) section. Regrant the missing service account permissions.  
9 (Failed precondition) | Zero results fetched after full sync. All documents have been deleted from Gemini Enterprise. | This error occurs when contact sharing is disabled in directory settings of the Admin console. | Verify that you turned on contact sharing to enable people search on Google Workspace data as described in the [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people#before-you-begin) section.  
3 (Invalid argument) | Failed to exchange signed JWT for access token. Google Workspace account has been deleted. All documents have been deleted from Gemini Enterprise. | This error occurs when the Google Workspace account is deleted. | Create a new connector with an active Google Workspace account.   
3 (Invalid argument) | GAIA id not found. Authentication failed. | This error occurs when the user account is incorrect. | Verify that the user account exists and enter the correct credentials.   
8 (Resource exhausted) | The quota for the project exceeded. Increase the document quota for the project. | This error occurs when the project quota is exceeded. | Increase the document quota for the project. For more information, see [Quotas](https://docs.cloud.google.com/gemini/enterprise/docs/quotas).  
13 (Internal error) | Internal error encountered. | This error occurs when there is an internal error. | Contact the support team.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
