---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id/
title: Connect Microsoft Entra ID \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:08.345890+00:00
---

# Connect Microsoft Entra ID  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect Microsoft Entra ID Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect Microsoft Entra ID to Gemini Enterprise.

After you set up your data source and import data the first time, the data store syncs data from that source at a frequency that you select during setup. **Note:** After you connect Microsoft Entra ID to your app, Google strongly recommends that you enable Knowledge Graph to significantly enhance search quality for your users. For more information, see [Knowledge Graph: Powering intelligent and context-aware search](https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search).

## Supported versions

The Entra ID connector supports all hosted versions of Entra ID through the Microsoft Graph API v1.0.

## Before you begin

Before you set up your data store and import data, you must obtain a client ID and secret for authentication and configure the minimum required permissions for the application. This section provides information about how to complete these tasks.

### Set up access control for Entra ID

To enforce data source access control and secure data in Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider). 

### Obtain a client ID and client secret

  1. Create an Entra ID application:

     1. Sign in to [Microsoft Entra administrator center](https://entra.microsoft.com) as an administrator and click **Application**.
     2. In the **Application** drop-down list, click **App registrations**.
     3. In the **App registrations** page, click **New registration**.
     4. Click **Add new registration** and do the following: 
        * Enter a name for the application.
        * Under **Supported account types** , select **Single tenant only - TENANT_NAME**, where TENANT_NAME is the name of your Microsoft Entra tenant.
        * Under **Redirect URI** , add a web redirect URI pointing to: `https://login.microsoftonline.com/common/oauth2/nativeclient`.
     5. Click **Register**.
  2. Save credentials:

On your registered application window, save the following values for later use:

     1. Use the **Application (client) ID** to set the **Client ID** parameter.
     2. Use the **Directory (tenant) ID** to set the **Azure Tenant** parameter.
  3. Create client secret:

     1. Navigate to **Certificates & secrets**.
     2. Click **New client secret** and specify a duration.
     3. Save the client secret and copy the client secret value for later use.

![save-client-secret-value](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/entraid-images/client-secret-value.png)Save the client secret value 

### Configure the minimum permissions required for the application

  1. On your registered application window, click **API permissions**.
  2. Under **Configured permissions** , select **Microsoft Graph** and configure the following permissions: 

     * `User.Read`
     * `User.Read.All (Application)`

If you want to ingest `profileCardAttributes`, then configure the following permissions: 

     * `People.Read.All (Application)`
     * `PeopleSettings.Read.All (Application)`
     * `PeopleSettings.Read.All (Delegated)`
  3. Grant **admin consent** for all the added permissions. An administrator's consent is required to use client credentials in the authentication flow.




#### Minimum permissions

The following table lists the minimum permissions that you require to create an Entra ID connector:

Permission | Usage reason | Description  
---|---|---  
`User.Read` | Data ingestion | Read organization details during connection establishment.  
`User.Read.All (Application)` | Data ingestion | Read all users in the organization.  
`People.Read.All (Application)` | Data ingestion | Read all the relevant people information, such as contacts, for all users in an organization.  
`PeopleSettings.Read.All (Application)` | Data ingestion | Read user configurations for all the users in the organization, such as profileCardSettings.  
`PeopleSettings.Read.All (Delegated)` | Data ingestion | Read user configurations for all the users in the organization, such as profileCardSettings.  
  
## Create an Entra ID data store

To use the Google Cloud console to sync data from Entra ID to Gemini Enterprise , follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data Stores**.

  3. Click add **Create Data Store**.

  4. On the **Select a data source** page, scroll or search for **Entra ID** to connect your third-party source.

  5. Under **Authentication settings** , enter the client ID and client secret.

  6. Under **Advanced options** :

     * If needed, click **Enable Static IP Addresses**. After creating the connector, you need to add the registered static IPs to your allowlist in order for sync runs to succeed. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).
     * To enable the connector to fetch [extension properties](https://learn.microsoft.com/en-us/graph/api/resources/extensionproperty?view=graph-rest-1.0), which are used to add a custom property to a directory object, select the **Enable Extension Properties** checkbox.
     * If you want to filter ingested user information, provide a custom SQL filter. The filter must be a valid SQL string.

Keys in the filter string must correspond to the following fields:

       * `Id` (the user's object ID in Microsoft Entra ID)
       * `employeeType`
       * `onPremisesSyncEnabled`
       * `accountEnabled`

The following are examples of valid SQL filters:
    
    id = 'abc' AND accountEnabled = true
    
    employeeType='E' AND onPremisesSyncEnabled= true
    

**Note:** For information about finding the `id` (the user's object ID in Microsoft Entra ID), see the [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/partner-center/account-settings/find-ids-and-domain-names#find-the-user-object-id).
     * In the **Azure Tenant** field, enter the Azure tenant ID that you obtained when you created an Entra ID application.

     * To apply a rate limit on the queries that the connector sends to the Entra ID instance, in the **Max QPS** field, specify the maximum queries per second. The default value is 80 QPS.

     * Click **Continue**.

  7. Under **Choose entities you want to sync** :

     * Click **User Profiles**. To filter the data based on `Id` for data ingestion, click **Filter** , and then do the following: 
       * To specify data to be included in the search index, select **Include in the index** and then specify the filter string in the **Id** field.
       * To specify data to be excluded from the search index, select **Exclude from the index** and then specify the filter string in the **Id** field.
     * Select the **Full sync** frequency.
  8. Click **Continue**.

  9. In **Configure your data connector** , select a region for your data store.

  10. Enter a name for your data connector.

  11. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.

  12. If you selected **Enable Static IP Addresses** under **Advanced options** , view the registered static IP addresses for the connector and add them to your allowlist for Entra ID.

     1. Go to the **Data Stores** page and click your connector name to see details about it on its **Data** page.
     2. In the **Static IPs** field, click **View and confirm IPs**.
     3. Copy the static IP addresses for the connector.
     4. In the Microsoft Entra administrator center, add the static IP addresses to a named or trusted location within an existing conditional access policy. For more information, see [Conditional Access: Network assignment](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-assignment-network).



## Check the connector state

  1. To check the status of your ingestion, go to the **Data Stores** page and click your connector name to see details about it on its **Data** page. The **Connector state** changes from **Creating** to **Running** when it begins to synchronize data. When ingestion is complete, the state changes to **Active** to indicate that the connection to your data source is set up and awaiting the next scheduled synchronization.

Depending on the size of your data, ingestion can take several minutes or several hours.

  2. When the connector state changes to **Active** , navigate to the **Entity** tab.

  3. Click the **userprofiles** entity.

  4. Check the number of ingested documents and verify that it matches the number of users in Entra ID.


The following standard user attributes are ingested as part of each user record: Vertex AI schema field name | Entra ID attribute name  
---|---  
`name.displayName` | Display Name  
`name.familyName` | Last Name  
`name.givenName` | First Name  
`name.username` | User Principal Name  
`email.value` | Email  
`employeeId` | Employee Id  
`personId` |   
`employeeType` | Employee type  
`hireDate` | Employee Hire Date  
`department` | Department  
`organizations.jobTitle` | Job title  
`organizations.location` | Office Location  
`Phone` | Business phone  
`managers.email`, `managers.personId` | Not a direct attribute (management chain from immediate manager to top-level manager)  
`directManager.personId` | Not a direct attribute (manager's `personId`)  
`displayphoto.imagebinary.data` | Base64-encoded profile picture  
  
If the Entra ID app has the required permissions to ingest custom attributes, it ingests up to [15 profile card attributes](https://learn.microsoft.com/en-us/graph/add-properties-profilecard#add-a-custom-attribute-to-the-profile-card) per record. By default, the custom attributes are not searchable.

## Configure searchable attributes

To make the custom attributes searchable, do the following:

  1. In the **userprofiles** page, navigate to the **Schema** tab.
  2. Click **Edit**.
  3. Deselect the attributes, such as **address** , from being **retrievable, searchable, and indexable** , then click **Save**.

The **Edit** button remains inactive for a few minutes before reactivating.

  4. When the **Edit** button is in **Active** state, click **Edit**.

  5. Select the **retrievable, searchable, and indexable** boxes for the required custom attributes.

  6. Enable search.

  7. Click **Save**.




## Test the search engine

After configuring your search engine, test its capabilities to verify whether it returns accurate results based on user access.

  1. Enable web app:

     1. Go to the app integration configurations and toggle to **Enable the web app**.
  2. Test web app:

     1. Click **Open** next to the web app link and sign in as a user.

     2. Verify that search results are restricted to items accessible by the user.




## Preview people search results

  1. In the search app, navigate to **Preview** and start searching within the console when using Google IdP.

     * Alternatively, navigate to the provided link and sign in with your IdP to start searching.
     * The search results appear as **people cards** , displaying user details such as **Name, Job title, Email, and Profile picture**.
  2. Click a **people card** to view a detailed profile page, which includes the following:

     * **Name**
     * **Profile picture**
     * **Job title**
     * **Department**
     * **Management chain**
     * **Direct reports**
  3. If custom attributes (profile card properties) are ingested and made indexable, searchable, and retrievable:

     * Searching by a custom attribute value returns only person profiles containing those attributes.
     * Custom attributes appear in search results, but can only be accessed through the API, not the Vertex Search user interface.



## Configure the workforce pool for non-Google IdP without SSO

  1. If your employees use a non-Google IdP, lack SSO with Google, or are not Google Workspace customers, set up a workforce pool as described in [Configure access controls for custom data sources](https://docs.cloud.google.com/gemini/enterprise/docs/identity) to enable the employee search.

The workforce pool lets you to manage and authenticate users from external identity providers, such as Azure or Okta, within Google Cloud console.

  2. To configure your workforce pool and enable the web app for seamless user access, do the following:

     1. Create workforce pool at the organization level in Google Cloud by following the appropriate setup manual:

        1. [Azure OIDC setup](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad#create-oidc-provider)
        2. [Azure SAML setup](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad#create-saml-provider)
        3. [Okta & OIDC setup](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-oidc-provider)
        4. [Okta & SAML setup](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-saml-provider)
     2. Configure the workforce pool in **Gemini Enterprise** > **Settings** for the region where you create your app.




## Recommended rate limits

The following table lists the recommended rate limits based on the number of users. Requests that exceed the limits are throttled. 

Quota group | Requests per second  
---|---  
S (Fewer than 50 users) | 105  
M (50-500 users) | 150  
L (More than 500 users) | 240  
  
## Known limitations

This following are the known limitations for the Entra ID connector:

  * Incremental sync is not supported.
  * Access Control Lists (ACLs) are not supported. All the users are accessible across the organization.
  * If you add a project to a VPC Service Controls perimeter after you create a connection, the connector sync run fails with the following error: `Connector is blocked due to the project being added to the VPC-SC perimeter. Please re-create the data store.` Recreate the data store to allow it to work within the VPC Service Controls perimeter.



## Error messages

The following table lists the error messages that you might get when you use the Entra ID connector:

Error message | Description | Troubleshooting  
---|---|---  
Authorization_RequestDenied Insufficient privileges to complete the operation. | The user account doesn't contain the required scopes to read data. | Provide the required scopes to the user account that is used to create the connection.  
Failed to retrieve OAuth token information | The client credential provided when configuring the connector is invalid. | Verify the following: 

  * The client secret corresponding to the client ID is provided. When you configure the connection, specify the client secret value and not its secret ID.
  * The tenant ID is valid.
  * The client secret hasn't expired. If the client secret has expired, edit the connection and specify the new client secret.

  
Connector is blocked due to the project being added to the VPC-SC perimeter. Please re-create the data store. | The connector was created before the project was added to a VPC Service Controls perimeter. | Recreate the data store to allow it to work within the VPC Service Controls perimeter.  
  
## Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * To preview how your search results appear after your app and data store are set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
