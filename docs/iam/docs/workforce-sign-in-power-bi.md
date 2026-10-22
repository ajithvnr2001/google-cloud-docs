---
url: https://docs.cloud.google.com/iam/docs/workforce-sign-in-power-bi/
title: Access BigQuery data in Power BI with Workforce Identity Federation and Microsoft Entra \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:55.848013+00:00
---

# Access BigQuery data in Power BI with Workforce Identity Federation and Microsoft Entra  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-sign-in-power-bi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Access BigQuery data in Power BI with Workforce Identity Federation and Microsoft Entra Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to let users that are in Microsoft Entra groups access BigQuery data in Power BI by using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

Microsoft Entra is the identity provider (IdP). Groups claims from Microsoft Entra are mapped to Google Cloud. Groups are granted Identity and Access Management (IAM) permission to access the BigQuery data.

This guide provides instructions for Power BI Desktop or Web.

## Before you begin

  1. Make sure that you have a Google Cloud organization set up.
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. You must have access to Microsoft Entra and Microsoft Graph.
  4. You must have Power BI set up.



## Costs

Workforce Identity Federation is available as a no-cost feature. However, Workforce Identity Federation detailed audit logging uses Cloud Logging. To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs). 

## Required roles

This section describes roles that are required for administrators and resources.

### Roles for administrators

To get the permissions that you need to configure Workforce Identity Federation, ask your administrator to grant you the [IAM Workforce Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) (`roles/iam.workforcePoolAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure identity federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

### Roles for federated identities

Power BI sends the `userProject` parameter during token exchange. Because of this, you must ask your administrator to grant the role Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) to the federated identities on the billing project.

To grant the role to a group of federated identities, run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/serviceusage.serviceUsageConsumer" \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID"
    

Replace the following:

  * `PROJECT_ID`: the billing project ID.
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `GROUP_ID`: the group ID—for example, `admin-group@altostrat.com`. To see a list of common principal identifiers, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).



## Create a workforce identity pool

This section describes how to create the workforce identity pool. You create the workforce identity pool provider later in this guide.

###  gcloud 

To create the workforce identity pool, run the following command:
    
    
    gcloud iam workforce-pools create WORKFORCE_POOL_ID \
        --organization=ORGANIZATION_ID \
        --display-name="DISPLAY_NAME" \
        --description="DESCRIPTION" \
        --session-duration=SESSION_DURATION \
        --location=global
    

Replace the following:

  * `WORKFORCE_POOL_ID`: an ID that you choose to represent your Google Cloud workforce pool. The pool ID must be globally unique across all workforce identity pools in Google Cloud. For information on formatting the ID, see the [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters) section in the API documentation.
  * `ORGANIZATION_ID`: the numeric organization ID of your Google Cloud organization for the workforce identity pool. Workforce identity pools are available across all projects and folders in the organization.
  * `DISPLAY_NAME`: Optional. A display name for your workforce identity pool.
  * `DESCRIPTION`: Optional. A workforce identity pool description.
  * `SESSION_DURATION`: Optional. The session duration, expressed as a number appended with `s`—for example, `3600s`. Session duration determines how long the Google Cloud access tokens, [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated) sign-in sessions, and gcloud CLI sign-in sessions from this workforce pool are valid. Session duration defaults to one hour (3600s). The session duration value must be between 15 minutes (900s) and 12 hours (43200s).

**Tip:** Run `gcloud iam workforce-pools create --help` to find other parameters you can customize for this command.

###  Console 

To create the workforce identity pool, do the following:

  1. In the Google Cloud console, go to the **Workforce Identity Pools** page:

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools?supportedpurview=organizationId)

  2. Select the organization for your workforce identity pool. Workforce identity pools are available across all projects and folders in an organization.

  3. Click **Create pool** and do the following:

     1. In the **Name** field, enter the display name of the pool. The pool ID is automatically derived from the name as you type, and it is displayed under the **Name** field. You can update the pool ID by clicking **Edit** next to the pool ID.

     2. Optional: In **Description** , enter a description of the pool.

     3. To create the workforce identity pool, click **Next**.




The workforce identity pool's session duration defaults to one hour (3600s). The session duration determines how long the Google Cloud access tokens, [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated), and gcloud CLI sign-in sessions from this workforce pool are valid. After you create the pool, you can [update the pool](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-pool) to set a custom session duration. The session duration must be from 15 minutes (900s) to 12 hours (43200s).

## Register a new Microsoft Entra app

This section shows you how to create a Microsoft Entra app using the Microsoft Azure portal.

  1. [Register a new Microsoft Entra application](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application#register-a-new-application).

  2. In the Microsoft Entra application that you registered, [create a new client secret](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application#certificates--secrets). Note the client secret.

  3. Grant API permissions to your Microsoft Entra application so that it can access users and groups information from Active Directory. To grant permissions for Microsoft Graph API, do the following:

     1. In your application, select **API Permissions**.
     2. In **Configured permissions** , click **Add a permission**.
     3. in the **Request API permissions** dialog, select **Microsoft Graph**.
     4. Select **Application permissions**.
     5. In the **Select Permissions** dialog, do the following: 
        1. In the search field, enter `User.ReadBasic.All`.
        2. Click **User.ReadBasic.All**.
        3. Click **Add permissions**.
     6. in the **Request API permissions** dialog, select **Microsoft Graph**.
     7. Select **Application permissions**.
     8. In the **Select Permissions** dialog, do the following: 
        1. In the search field, enter `GroupMember.Read.All`.
        2. Click **GroupMember.Read.All**.
        3. Click **Add permissions**.
     9. In **Configured permissions** , click **Grant admin consent for (domain name)**.
     10. When you are asked to confirm, click **Yes**.
  4. To access the values that you need to configure the workforce pool provider later in this guide, do the following:

     1. Go to the **Overview** page of the Microsoft Entra application.
     2. Click **Endpoints**.
     3. Note the following values:

        * **Client ID:** the ID of the Microsoft Entra app that you registered earlier in this guide.
        * **Client Secret:** the client secret that you generated earlier in this guide.
        * **Tenant ID:** the tenant ID of the Microsoft Entra app that you registered earlier in this guide.
        * **Issuer URI:** the URI of the OpenID Connect metadata document, omitting `/.well-known/openid-configuration`. For example, if the OpenID Connect metadata document URL is `https://login.microsoftonline.com/d41ad248-019e-49e5-b3de-4bdfe1fapple/v2.0/.well-known/openid-configuration`, then the Issuer URI is `https://login.microsoftonline.com/d41ad248-019e-49e5-b3de-4bdfe1fapple/v2.0/`.



## Create a workforce identity pool provider

To create the provider, run the following command:
    
    
    gcloud iam workforce-pools providers create-oidc WORKFORCE_PROVIDER_ID \
        --workforce-pool=WORKFORCE_POOL_ID \
        --location=global \
        --display-name=DISPLAY_NAME \
        --issuer-uri=ISSUER_URI \
        --client-id=https://analysis.windows.net/powerbi/connector/GoogleBigQuery \
        --attribute-mapping=ATTRIBUTE_MAPPING \
        --web-sso-response-type=id-token \
        --web-sso-assertion-claims-behavior=only-id-token-claims \
        --extra-attributes-issuer-uri=APP_ISSUER_URI \
        --extra-attributes-client-id=APP_CLIENT_ID \
        --extra-attributes-client-secret-value=APP_CLIENT_SECRET \
        --extra-attributes-type=EXTRA_GROUPS_TYPE \
        --extra-attributes-filter=EXTRA_FILTER \
        --detailed-audit-logging
    

Replace the following:

  * `WORKFORCE_PROVIDER_ID`: a unique provider ID. The prefix `gcp-` is reserved and can't be used in a provider ID.

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID to connect your IdP to.

  * `DISPLAY_NAME`: an optional user-friendly display name for the provider.

  * `ISSUER_URI`: the value of issuer uri, formatted as, `https://sts.windows.net/TENANT_ID`. Replace `TENANT_ID` with the tenant ID that you noted earlier.

  * `ATTRIBUTE_MAPPING`: a mapping of the group and, optionally, other attributes from the Microsoft Entra claim to Google Cloud attributes—for example: `google.groups=assertion.groups, google.subject=assertion.sub`. The group is granted access on BigQuery data later in this guide.

For more information, see [Attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mapping). 

  * `APP_ISSUER_URI`: the issuer URI of the Microsoft Entra application that you noted earlier.

  * `APP_CLIENT_ID`: the issuer client ID that you noted earlier.

  * `APP_CLIENT_SECRET`: the issuer client secret that you noted earlier.

  * `EXTRA_GROUPS_TYPE`: the type of group identifier, which can be one of the following:

    * `azure-ad-groups-mail`: Group email addresses are retrieved from the IdP—for example: `admin-group@altostrat.com`.

    * `azure-ad-groups-id`: UUIDs that represent the groups are retrieved from the IdP—for example: `abcdefgh-0123-0123-abcdef`.

    * `azure-ad-groups-display-name`: Group display names are retrieved from the IdP—for example: `admin-group-display-name`.

  * `EXTRA_FILTER`: the filter used to request specific assertions to be passed from the IdP. By specifying `--extra-attributes-type=azure-ad-groups-mail`, `--extra-attributes-filter` filters for a user's group claims that are passed from the IdP. By default, all of the groups associated with the user are fetched. The groups that are used must be mail and security enabled. To learn more, see [Use the $search query parameter](https://learn.microsoft.com/en-us/graph/search-query-parameter).

**Important:** A maximum of 999 groups can be fetched.

The following example filters for groups that are associated with user email addresses that start with `gcp`: 
        
        --extra-attributes-filter='"mail:gcp"'

The following example filters groups that are associated with users that have email addresses starting with `gcp` and a **displayName** that contains `example`: 
        
        --extra-attributes-filter='"mail:gcp" AND "displayName:example"'

  * Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, omit the `--detailed-audit-logging` flag when you run `gcloud iam workforce-pools providers create`. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 




## Create allow policies

In this section, you create an allow policy that grants the role BigQuery Data Viewer (`roles/bigquery.dataViewer`) to the mapped group on the project where your BigQuery data is stored. The policy lets all identities that are in the group view data from BigQuery tables and views that are stored in the project.

To create the policy, run the following command:
    
    
    gcloud projects add-iam-policy-binding BIGQUERY_PROJECT_ID \
        --role="roles/bigquery.dataViewer" \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID"
    

Replace the following:

  * `BIGQUERY_PROJECT_ID`: the project ID where your BigQuery data and metadata are stored.
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID
  * `GROUP_ID`: the group identifier, which depends on the value of `--extra-attributes-type` that was used to create the workforce identity pool provider, as follows:

    * `azure-ad-groups-mail`: the group identifier is an email address—for example: `admin-group@altostrat.com`.

    * `azure-ad-groups-id`: the group identifier is a UUID for the group—for example: `abcdefgh-0123-0123-abcdef`.

    * `azure-ad-groups-display-name`: the group identifier is a display name—for example: `admin-group-display-name`.




## Access BigQuery data from Power BI Desktop

To access BigQuery data from Power BI Desktop, do the following:

  1. Open Power BI.
  2. Click **Get Data**.
  3. Click **Database**.
  4. In the list of databases, select **Google BigQuery (Microsoft Entra ID) (Beta)**.
  5. Click **Connect**.
  6. Fill in the following required fields:

     * **Billing project ID:** the billing project ID.
     * **Audience URI:** the Google Cloud URI, formatted as follows:
           
           //iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
           

Replace the following:

       * `WORKFORCE_POOL_ID`: the workforce identity pool ID.

       * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.

  7. Click **Ok**.

  8. Click **Next**.

  9. Click **Select the data**.




If you are asked to sign in, use a Microsoft Entra identity that is a member of the group.

You can now use data from BigQuery in Power BI Desktop.

## Access the BigQuery data from Power BI Web

To access BigQuery data from Power BI Web, do the following:

  1. Go to Power BI Web.

  2. Click **Power query** to add new data source.

  3. Click **Get data**.

  4. In the list, find and select the **Google BigQuery (Microsoft Entra ID) (Beta)**.

  5. Fill in the following required fields:

     * **Billing Project ID:** the Google Cloud billing project

     * **Audience URI:** the audience URI, formatted as follows:
           
           //iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
           

Replace the following:

       * `WORKFORCE_POOL_ID`: the workforce identity pool ID

       * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID

  6. Click **Connection Credentials** > **Authentication kind**.

  7. Select **Organizational account**.

  8. Click **Sign in**.

  9. Click **Next**.

  10. Click **Select the data**.




You can now use data from BigQuery in Power BI Web.

## What's next

  * To delete Workforce Identity Federation users and their data, see [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data)
  * To revoke Workforce Identity Federation user sessions, see [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions)
  * To learn about Google Cloud products' support for Workforce Identity Federation, see [Identity federation: supported products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
