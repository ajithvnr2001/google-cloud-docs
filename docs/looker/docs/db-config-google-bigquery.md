---
url: https://docs.cloud.google.com/looker/docs/db-config-google-bigquery/
title: Google BigQuery \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:07.337960+00:00
---

# Google BigQuery  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-google-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Google BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This page explains how to set up a connection in Looker to [Google BigQuery Standard SQL](https://cloud.google.com/blog/products/gcp/bigquery-111-now-with-standard-sql-iam-and-partitioned-tables) or Google BigQuery Legacy SQL.

The general steps for setting up a Google BigQuery Standard SQL or Google BigQuery Legacy SQL connection are as follows:

  1. On your BigQuery database, configure the authentication method that Looker will use to access your BigQuery database. Looker supports the following authentication options for BigQuery:

     * **Application Default Credentials** : Select this option to use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate into your database.

To enable ADC, you must also set the following environment variables when you start your Looker instance.:

       * `FF_SELF_HOSTED_DIALECT_ADC=true`
       * `GOOGLE_CLOUD_UNIVERSE_DOMAIN="<google_cloud_universe_domain>"`

where `<google_cloud_universe_domain>` is the universe domain of your Google Cloud instance, such as `apis-berlin-build0.goog` or `s3nsapis.fr`.

Set this variable by using the following commands:

`echo 'export FF_SELF_HOSTED_DIALECT_ADC=true' >> lookerstart.cfg`

`echo 'export GOOGLE_CLOUD_UNIVERSE_DOMAIN="<google_cloud_universe_domain>"' >> lookerstart.cfg`

     * **Service account** : See the Authentication with BigQuery service accounts section on this page for information.

     * **OAuth** : See the Authentication with OAuth section on this page for information.

  2. On your BigQuery database, if you want to use [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) on the connection, create a temporary dataset that Looker can use to create PDTs on your database. See the section Creating a temporary dataset for persistent derived tables on this page for the procedure.

**Note:** If you are using OAuth and you want to enable PDTs on the connection, you need to create a BigQuery service account specifically for Looker to use for PDT processes on your BigQuery database. See the section Enabling PDTs for Looker connections to BigQuery with OAuth on this page for the procedure.
  3. In Looker, set up the Looker connection to your BigQuery database. See the section Connecting Looker to BigQuery on this page for the procedure.

  4. In Looker, test the connection between Looker and your BigQuery database. See the section Testing the connection on this page for the procedure.




## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Authentication with BigQuery service accounts

One way that Looker can authenticate into your BigQuery database is with a BigQuery service account. You create the service account on your BigQuery database using the [API Manager in the Google Cloud console](https://console.cloud.google.com/apis/credentials). You must have Google Cloud administrator permissions to create the service account. See the documentation on creating a [service account](https://docs.cloud.google.com/iam/docs/service-accounts).

### Creating a service account and downloading the JSON credentials certificate

To create a BigQuery service account, follow these steps:

  1. Open the credentials page in the [API Manager in the Google Cloud console](https://console.cloud.google.com/apis/credentials) and select your project.

  2. Select **CREATE CREDENTIALS** and choose **Service account**.

  3. Enter a name for the new service account, optionally add a description, and select **CREATE AND CONTINUE**.

  4. Your service account requires two Google BigQuery [predefined roles](https://docs.cloud.google.com/bigquery/access-control#curated_roles_comparison_matrix):

     * **BigQuery > BigQuery Data Editor**
     * **BigQuery > BigQuery Job User**

Select the first role in the **Select a role** field, select **ADD ANOTHER ROLE** , and then select the second role.

![](https://docs.cloud.google.com/static/looker/docs/images/bq-select-roles-2220.png)

After selecting both roles, select **CONTINUE** , and then select **DONE**.

  5. In the **Credentials** page, select your new service account:

![](https://docs.cloud.google.com/static/looker/docs/images/bq-service-account-2220.png)

  6. Select **KEYS** , and then select **ADD KEY** , and then, in the drop-down, select **Create new key** :

![](https://docs.cloud.google.com/static/looker/docs/images/bq-add-key-2220.png)

  7. Select **JSON** under **Key type** , and then select **CREATE** :

![](https://docs.cloud.google.com/static/looker/docs/images/bq-create-private-key-2220.png)

  8. The JSON key will be saved to your computer.

**Caution:** You won't be able to download the key again. Take note of where you save it.

After noting the download location, select **CLOSE** :

![](https://docs.cloud.google.com/static/looker/docs/images/bq-save-private-key-2220.png)

  9. Select **DONE**.

  10. Find the email address that corresponds to the service account. You will need this address to configure the Looker connection to BigQuery:

![](https://docs.cloud.google.com/static/looker/docs/images/bq-account-email-2220.png)

  11. Once you create the service account on your BigQuery database, you will enter this service account information and the certificate file details in the **Service Account Email**, **Service Account JSON/P12 File**, and **Password** fields of Looker's **Connections** window when you set up the Looker connection to BigQuery.




## Authentication with OAuth

**Warning:** Starting on March 1, 2025, Looker requires read-only scope for OAuth configurations on BigQuery connections. See [Restricting OAuth scope to read-only for Google BigQuery connections](https://docs.cloud.google.com/looker/docs/best-practices/oauth-read-only) for more information about switching to the proper configuration and determining which users still need to switch.

Looker supports OAuth for Google BigQuery connections, meaning that each Looker user authenticates in to Google with their own Google OAuth credentials and authorizes Looker to access the database.

OAuth lets database administrators perform the following functions:

  * Audit which Looker users are running queries against the database.
  * Enforce role-based access controls using Google permissions.
  * Use OAuth tokens for all processes and actions that access Google BigQuery, instead of embedding BigQuery IDs and passwords in multiple places.



Note the following for BigQuery connections with OAuth:

  * If a database administrator changes the BigQuery OAuth client credentials, any schedules or alerts that a user owns will be affected. Users must sign in again if their administrator changes the BigQuery OAuth credentials. Users can also go to their Looker **Account** page from their [user profile account page](https://docs.cloud.google.com/looker/docs/user-account#configuring_oauth_connection_credentials) to sign in to Google.
  * Because BigQuery connections that use OAuth are "per user," caching policies are also per user and not just per query. This means that, instead of using cached results whenever the same query is run within the caching period, Looker will use cached results only if the _same user has run the same query_ within the caching period. For further information on caching, see the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page.
  * If you want to use [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) on a BigQuery connection with OAuth, you must create an additional service account for Looker to access your database for PDT processes. See the Persistent derived tables on a BigQuery connection section on this page for information.
  * When a Looker administrator sudos as another user, the administrator uses that user's OAuth access token. When users authorize an OAuth connection in Looker, an **Authorize OAuth Connection** dialog notifies them that privileged Looker users, such as administrators or developers, might have visibility into their data. See the [Users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_users) documentation page for information about using the `sudo` command.
  * Google BigQuery connections that are configured for OAuth authentication don't support [query killing](https://docs.cloud.google.com/looker/docs/admin-panel-database-queries#query_killing).



### Configuring a BigQuery database project for OAuth

The following sections describe how to generate OAuth credentials and how to configure an OAuth consent screen.

In the following cases, you don't need to perform these procedures:

  * If you've already configured an OAuth consent screen for another application in your project, you won't need to create another — you configure only one consent screen for all applications in a project. In this case, you can go right to the procedure for [configuring the Looker (Google Cloud core) connection to your database](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#configuring-the-connection-for-with-oauth).
  * If you're on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance, Looker can use the [OAuth application credentials that your Looker admin used](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) when they created the Looker (Google Cloud core) instance. If you're using the same OAuth application credentials as your Looker (Google Cloud core) instance, you can skip the procedures in this section and the Configuring the Looker connection for BigQuery with OAuth section and instead follow the steps in the [Looker (Google Cloud core) documentation for using OAuth with BigQuery](https://docs.cloud.google.com/looker/docs/looker-core-dialects#oauth-options).

**Note:** See the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#oauth-options) for information about how to configure OAuth using instance credentials for BigQuery connections on Looker (Google Cloud core) instances.



OAuth credentials and the OAuth consent screen must be configured in the [Google Cloud console](https://console.cloud.google.com/). The Google generic description is on [the Google Cloud support](https://support.google.com/cloud/answer/6158849) site and on the [Google Dev console](https://developers.google.com/console/help/) site.

Depending on the type of users who are accessing BigQuery data in Looker and whether your BigQuery data is public or private, OAuth may not be the most appropriate [authentication](https://docs.cloud.google.com/docs/authentication) method. Likewise, the type of data requested from the user and degree of access needed to that user's data when they're authenticating in to Google to use Looker may require [verification by Google](https://support.google.com/cloud/answer/9110914). See more about verification in the Generating Google OAuth credentials section on this page.

#### Generating Google OAuth credentials

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. In the **Select a project** drop-down, navigate to your BigQuery project. This should take you to your project dashboard.

  3. In the left menu, select the **APIs & Services** page. Then select **Credentials**. On the **Credentials** page, select the down arrow in the **Create credentials** button, and select **OAuth client ID** from the drop-down menu:

  4. Google requires that you configure an OAuth consent screen, which lets your users choose how to grant access to their private data, before you can generate your OAuth credentials. To configure your OAuth consent screen, see the Configuring an OAuth consent screen section on this page.

  5. If you've already configured an OAuth consent screen, Google displays the **Create OAuth client ID** page, which lets you create an OAuth client ID and secret to use in your BigQuery connection to Looker. From the **Application type** drop-down, select **Web application**. The page will expand and display additional options:

![](https://docs.cloud.google.com/static/looker/docs/images/bq-create-ouath-client-id-2220.png)

  6. In the **Name** field, enter a name for the app, such as Looker.

  7. In the **Authorized JavaScript origins** section, select **\+ ADD URI** to display the **URIs 1** field. In the **URIs 1** field, enter the URL to your Looker instance, including the `https://`. For example:

     * If Looker hosts your instance: `https://<instancename>.looker.com`
     * If you have a customer-hosted Looker instance: `https://looker.<mycompany>.com`
     * If your Looker instance requires a port number: `https://looker.<mycompany>.com:9999`
  8. In the **Authorized redirect URIs** section, select **\+ ADD URI** to display the **URIs 1** field. In the **URIs 1** field, enter the URL to your Looker instance, followed by `/external_oauth/redirect`. For example: `https://<instancename>.looker.com/external_oauth/redirect` or `https://looker.<mycompany>.com:9999/external_oauth/redirect`.

  9. Select **Create**. Google displays your **Client ID** and your **Client Secret**.

  10. Copy your client ID and your client secret values. You will need them to configure the OAuth for the BigQuery connection in Looker.




#### Configuring an OAuth consent screen

**Note:** If you've already configured an OAuth consent screen for another application in your project, Looker will not display this option. If you've already generated your OAuth credentials, you can proceed to configuring your BigQuery connection for OAuth in Looker.

Google requires that you configure an [OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent), which lets your users choose how to grant access to their private data and provides a link to your organization's terms of service and privacy policy.

In the left menu, select the **OAuth consent screen** page. Before you can configure your OAuth consent screen, you must choose the type of users to whom you're making this app available. Depending on your selection, your app may require [verification by Google](https://support.google.com/cloud/answer/9110914).

![](https://docs.cloud.google.com/static/looker/docs/images/admin-google-consent-user-type-76.png)

Make your selection and select **Create**. Google displays the **OAuth consent screen** page. You can configure this screen for all applications in your project, including both [internal and public](https://support.google.com/cloud/answer/6158849#public-and-internal) applications.

Google will perform a verification for _public_ applications if any of these are true:

  * The application uses Google APIs that use restricted or sensitive scopes.
  * The OAuth consent screen includes an application logo.
  * The project has exceeded the domain threshold.



Do the following to configure your OAuth consent screen:

![](https://docs.cloud.google.com/static/looker/docs/images/bq-oauth-consent-screen-2220.png)

  1. In the **App name** field, enter the name of the application that the user is granting access to — in this case, Looker.

  2. In the **User support email** field, enter the support email that users should contact with login or consent issues.

  3. Select **ADD DOMAIN** to reveal the **Authorized domain 1** field. In this field, enter the domain of the URL to your Looker instance. For example, if Looker hosts your instance at `https://<instance_name>.cloud.looker.com`, the domain is `looker.com`. For customer-hosted Looker deployments, enter the domain on which you host Looker.

  4. In the **Developer contact information** section, enter one or more email addresses that Google can use to contact you about your project.

The remaining fields are optional, but you can use them to further customize your consent screen.

  5. Select **SAVE AND CONTINUE**.

  6. Google displays the **Scopes** page, where you can configure [scopes](https://developers.google.com/identity/protocols/oauth2/scopes). Looker requires only the default scopes, so no additional scope configuration is required. Select **SAVE AND CONTINUE**.

  7. On the **Summary** page, select **BACK TO DASHBOARD**.




You can now continue the procedure for generating your OAuth credentials.

For more information about configuring the Google **OAuth consent screen** , see the Google [support](https://developers.google.com/workspace/guides/configure-oauth-consent) documentation.

### Configuring the Looker connection for BigQuery with OAuth

**Note:** For Looker (Google Cloud core) instances, when you select **OAuth** , Looker defaults to using the OAuth application credentials that your Looker admin used when they created the Looker (Google Cloud core) instance and you don't need to manually enter credentials. See the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#oauth-options) for more information.

To enable OAuth for your BigQuery connection, select the **OAuth** option on the Looker **Connection** page when you are setting up the Looker connection to BigQuery. When you select the **OAuth** option, Looker will display the **OAuth Client ID** and **OAuth Client Secret** fields. Paste in the **Client ID** and **Client Secret** values that you obtained as a step in the Generating Google OAuth credentials procedure on this page.

There are some Google Workspace admin settings that can interrupt BigQuery OAuth:

  * **Session length** : If you have set a session length for BigQuery OAuth, to avoid Looker session timeouts you will need to use the **Exempt Trusted Apps** feature to add Looker to your trusted apps. Refer to the [Set session length for Google Cloud services](https://support.google.com/a/answer/9368756) help article to view the steps for this procedure.
  * **Context-Aware Access settings** : Check the Google Workspace Context-Aware Access settings for anything that might block specific users from completing the OAuth flow. Refer to the [Protect your business with Context-Aware Access](https://support.google.com/a/answer/9275380) help article for information on Context-Aware Access.



### How Looker users authenticate in to BigQuery with OAuth

Once the Looker connection to BigQuery is set up for OAuth, your users with the [BigQuery Job User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) and [BigQuery Data Viewer](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) Identity and Access Management roles can use Looker to perform their initial authentication into your BigQuery database by doing one of the following:

  * Authenticating in to Google from a Looker query that uses the BigQuery connection
  * Authenticating in to Google from the **OAuth Connection Credentials** section on their Looker **Account** page



#### Authenticating in to Google from a query

Once the Looker connection to BigQuery is set up for OAuth, Looker will prompt users to sign in with their Google Account before running queries that use the BigQuery connection. Looker shows this prompt from Explores, dashboards, Looks, and SQL Runner.

The user must perform these steps:

  1. Select **Log In**.
  2. In the **Authorize OAuth Connection** dialog, select **Authorize**. (This dialog notifies the user that the Looker instance will access data on their behalf and that privileged Looker users, such as administrators or developers, might have visibility into their data.)
  3. Use OAuth to authenticate into BigQuery.
  4. Select the **Run** button in the Explore to load the data into the Explore.



#### Authenticating in to Google from the user account page

Once the Looker connection to BigQuery is set up for OAuth, a user can authenticate into their Google Account from the [Looker user account page](https://docs.cloud.google.com/looker/docs/user-account#oauth):

  1. From Looker, select the profile icon and select **Account** from the user menu.
  2. Go to the **OAuth Connection Credentials** section, and select the **Log In** button for the appropriate BigQuery database connection.
  3. In the **Authorize OAuth Connection** dialog, review the notice and select **Authorize** to continue. (Looker stores this consent in your browser's local storage; if you clear local storage, the dialog appears again when you next start an OAuth authorization flow.)
  4. Select the appropriate account from the **Sign in with Google** page.
  5. Select **Allow** on the OAuth consent screen to allow Looker to view and manage your data in Google BigQuery.



Once you authenticate in to Google through Looker, you can log out or reauthorize your credentials at any time through your **Account** page, as described on the [Personalizing your user account](https://docs.cloud.google.com/looker/docs/user-account#oauth) documentation page. Although Google BigQuery tokens don't expire, a user may select **Reauthorize** to sign in with a different Google Account.

### Revoking OAuth tokens

Users can [revoke](https://support.google.com/accounts/answer/3466521#remove-access) access from applications like Looker to the Google Account by visiting their [Google Account settings](https://myaccount.google.com/permissions).

Google BigQuery tokens don't expire; however, if a database admin changes the database connection's OAuth credentials in a way that invalidates the existing credentials, users will have to sign in with their Google Account again before running any queries that use that connection.

**Note:** Some [schedules](https://docs.cloud.google.com/looker/docs/scheduling) or [alerts](https://docs.cloud.google.com/looker/docs/alerts-overview) may be based on models with a BigQuery database connection using OAuth. If a BigQuery database admin changes the existing database connection's OAuth credentials, existing users' credentials may be invalidated. Any schedules or alerts created by that user will fail until the user logs in again through Google OAuth.

## Persistent derived tables on a BigQuery connection

If you want to use [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)) for your BigQuery connection, you may need to do the following, depending on your connection configuration:

  * Use the Google Cloud console to create a temporary dataset in your BigQuery database that Looker can use to write PDTs. See the Creating a temporary dataset for persistent derived tables section on this page for the procedure. This step is required for PDTs, regardless of the other configuration options on the connection.
  * Use the API Manager in the Google Cloud console to create a separate service account for Looker's PDT processes. See the section Creating a service account and downloading the JSON credentials certificate on this page for the procedure. The type of authentication on your connection affects whether a PDT service account is required, and also where you enter the PDT service account information in Looker's **Connections** window when you set up the Looker connection to BigQuery: 
    * If your connection uses OAuth for user authentication, you must create a separate service account for PDT processes. You will enter the service account information and the certificate file details in the **PDT Overrides** section of Looker's **Connections** window. Looker's **Connections** window displays the **PDT Overrides** section automatically when you turn on the **Enable PDTs** toggle for a connection that is also configured with the **OAuth** option in the **Authentication** field. See the Enabling PDTs for Looker connections to BigQuery with OAuth section for more information.
    * If your connection uses service accounts for user authentication, you have the option of creating a separate service account for PDT processes. If you choose to have a separate PDT service account, you will enter the service account information in the **PDT Overrides** section for the **Service Account Email**, **Service Account JSON/P12 File**, and **Password** fields of Looker's **Connections** window. The **PDT Overrides** section appears when you turn on the **Enable PDTs** toggle for a Looker connection to BigQuery using service account authentication.



### Creating a temporary dataset for persistent derived tables

To enable persistent derived tables (PDTs) for your BigQuery connection, turn on the **Enable PDTs** toggle on the Looker **Connection** page when you are setting up the Looker connection to BigQuery. When you enable PDTs, Looker will display the **Temp Project** and **Temp Database** fields. In these fields, you'll enter the project ID and dataset name that Looker can use to create PDTs. You should configure the database or schema in advance with the appropriate write permissions.

**Note:** **Temp Project** is not supported on Looker instances that are enabled for the [**Use Legacy Connections Page**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_connections) legacy feature.**Warning:** If your BigQuery connection is configured for OAuth user authentication, you will need to grant users permissions to the temp datbase in order for the users to query PDTs. Be careful when granting users permissions to the temporary dataset, since PDTs may expose data from underlying tables that the user otherwise wouldn't be able to access. When defining PDTs, LookML developers should be aware that with OAuth connections, permissioning for PDTs is independent of permissioning for users. Developers need to consider data access rules when defining PDTs. 

You can set up a temporary dataset using the Google Cloud console:

  1. Open the [Google Cloud console](https://console.cloud.google.com/bigquery) and select your project.

  2. Select the three-dot menu, and then select **Create dataset**.

![](https://docs.cloud.google.com/static/looker/docs/images/setup-bq-create-new-dataset-2212.png)

  3. Enter a **Dataset ID** (typically `looker_scratch`), and then select your **Data location** (optional), **Default table expiration** , and encryption key management solution. Select **CREATE DATASET** to finish.

**Warning:** If you have multiple Looker instances, such as a production instance and a QA instance, make sure to set different temporary datasets for each instance to avoid PDT management conflicts.

![](https://docs.cloud.google.com/static/looker/docs/images/setup-bq-name-dataset-2212.png)




Now that you have created the dataset, you can specify the project and dataset in the **Temp Project** and **Temp Database** fields of the Looker **Connections** window when you set up the Looker connection to BigQuery.

### Enabling PDTs for Looker connections to BigQuery with OAuth

For BigQuery connections that use OAuth, your users authenticate into Looker with their OAuth credentials. Looker supports PDTs for BigQuery connections with OAuth, but Looker itself cannot use OAuth, so you must set up a BigQuery service account specifically to allow Looker to access your database for PDT processes.

You can set up a PDT service account on your BigQuery database using the Google Cloud API Manager. See the Creating a service account and downloading the JSON credentials certificate section on this page.

Once you create the service account on your BigQuery database, enter the service account information and the certificate file details in the **PDT Overrides** section of Looker's **Connections** window when you set up the Looker connection to BigQuery. See the PDT Overrides section for information about the **PDT Overrides** fields.

### PDT Overrides

For BigQuery connections that use OAuth, and for connections where you want to use different credentials, datasets, or billing projects for your PDTs, you can enable the **PDT Overrides** toggle to enter different information that is specific to PDTs on your connection. (See the [PDT Overrides](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#enable_pdt_overrides) section of the **Connecting Looker to your database** documentation page for more information on why PDT overrides can be helpful.)

If you have turned on the **Enable PDTs** toggle for a connection, the Looker **Connections** window displays the **Enable PDT Overrides** toggle. Turn on the **Enable PDT Overrides** toggle and use the following fields in the **PDT Overrides** section to enter the information for the service account that Looker can use for PDT processes on your database:

  * **PDT Override Billing Project ID** : Specify the project to use for billing for PDT build and maintenance queries (trigger check queries). Queries against the PDT will still use the billing project specified in the **Billing Project ID** field of the general settings. The PDT override billing project is never used for storage, only for billing. If you're going to use this field, the service account must have at minimum the [bigquery.jobUser role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser).

**Note:** **PDT Billing Project ID** is supported only on Looker instances that use the updated connection workflow, which is documented on the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) page. If you are on a Looker (original) instance and your Looker admin has enabled the [Use Legacy Connections Page](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_connections) legacy toggle, the **PDT Billing Project ID** field will not be available.
  * **PDT Override Dataset** : The name of the dataset that you want Looker to use for PDTs on the connection.

**Warning:** Changing the **PDT Override Dataset** field for an existing connection will trigger a rebuild of the PDTs on the connection.
  * **PDT Override Service Account file**: Use the **Upload File** button to upload the certificate file for the BigQuery service account that you want to use for PDT processes on the connection. You can get this file from the Google Cloud API Manager as a step in the Creating a service account and downloading the JSON credentials certificate procedure. The service account that you use for the PDT dataset needs to have read and write access.

  * **Username**: This field applies only if you upload a P12 file in the **PDT Override Service Account file** field of the **PDT Overrides** section. Enter the email address for the BigQuery service account that you want to use for PDT processes on the connection. You can get this email address from the Google Cloud API Manager as a step in the Creating a service account and downloading the JSON credentials certificate procedure.

  * **Password**: This field applies only if you upload a P12 file in the **PDT Override Service Account file** field of the **PDT Overrides** section. Enter the password to the .p12 credentials file for the BigQuery service account that you want to use for PDT processes on the connection.

  * **PDT Override Additional JDBC Parameters**: Add any additional JDBC parameters that should be used for the PDTs on the connection, such as BigQuery labels (see the Job labels and context comments for BigQuery connections section on this page for more information). The following are some of the other supported parameters:

    * `connectTimeout`: Number of milliseconds to wait for a connection. Defaults to 240000.
    * `readTimeout`: Number of milliseconds to wait for a read. Defaults to 240000.
    * `RootURL`: If you have a BigQuery instance in a private network, specify an alternate endpoint to connect to BigQuery other than the default public endpoint.



## Connecting Looker to BigQuery

You create a database connection in Looker on the **Connect your database to Looker** page. There are two options for opening the **Connect your database to Looker** page:

  * Select **Connections** from the **Database** section in the **Admin** panel. On the **Connections** page, click the **Add Connection** button.
  * Click the **Create** button in the [main navigation panel](https://docs.cloud.google.com/looker/docs/finding-content#using_the_left_navigation_panel), and then select the **Connection** menu item.



Fill out the connection details. The majority of these settings are common to most database dialects and are described on the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page. The following settings are mentioned either to highlight them or to clarify how they apply specifically to BigQuery connections:

  * **SQL Dialect** : Select **Google BigQuery Standard SQL** or **Google BigQuery Legacy SQL**.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  * **Project scope** : Select whether the connection should be able to be used with all projects or with only one project. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#project-scope) page for more information.

  * **Enable SSH Server** :  For instances that are deployed on Kubernetes infrastructure and have the ability to add SSH server configuration information, you can turn on the **Enable SSH Server** toggle to configure the **SSH Server** and **SSH Tunnel** fields. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#enable-ssh-server) page for more information.

  * **Billing Project ID** :  The [project ID](https://support.google.com/googleapi/answer/7014113) (unique identifier) of the Google Cloud billing project. The billing project is the Google Cloud project that gets billed, but you can still query datasets in a different Google Cloud project if your LookML developers specify fully scoped table names in the `sql_table_name` parameter of your LookML [views](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name), [Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name), or [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name). For BigQuery, a fully scoped table name uses the format `<project_name>.<dataset_name>.<table_name>`. Without a fully scoped reference, BigQuery looks for the table in the billing project and dataset that you specify in Looker's **Connections** page for the BigQuery connection to Looker. See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/resource-hierarchy) for an explanation of the resource hierarchy in BigQuery.

  * **Storage Project ID** :  The project ID of the storage project, if you separate compute and storage in different projects. You can query datasets in a different Google Cloud project if your LookML developers specify fully scoped table names in the `sql_table_name` parameter of your LookML [views](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name), [Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name), or [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name). For BigQuery, a fully scoped table name uses the format `<project_name>.<dataset_name>.<table_name>`. Without a fully scoped reference, BigQuery looks for the table in the billing project and dataset that you specify in Looker's **Connections** page for the BigQuery connection to Looker. See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/resource-hierarchy) for an explanation of the resource hierarchy in BigQuery.

**Note:** **Storage Project ID** is not supported on Looker instances that are enabled for the [**Use Legacy Connections Page**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_connections) legacy feature.
  * **Primary Dataset** : The name of the dataset that you want Looker to default to when it queries your database. The default dataset must be located within the billing project that is specified for the connection; you cannot enter a value such as `project_name.dataset_name` in the **Database** field to specify a dataset in a different project.

**Warning:** Changing the **Primary Dataset** field for an existing connection will trigger a rebuild of the PDTs on the connection.

Your LookML project can access tables in other datasets (including tables in public datasets) if your LookML developers specify fully scoped table names in the `sql_table_name` parameter of your LookML [views](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name), [Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name), or [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name). For BigQuery, a fully scoped table name uses the format `<project_name>.<dataset_name>.<table_name>`. To query a table in another dataset, the table must be accessible by the service account (for connections that use service account authentication) or by the user running the query (for connections that use OAuth authentication). If your LookML code does not specify fully scoped table names, BigQuery will search for the table in the dataset that you specify in the **Dataset** field of the BiqQuery connection.

If your project doesn't have any datasets (which may be the case if you separate compute and storage in separate projects), you can provide an arbitrary **Dataset** value, but then you must always use fully scoped table names in your LookML.



  * **Authentication**: The type of authentication that Looker will use to access your database. Some of these options are supported only for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances:

    * **Application Default Credentials** : (Looker (Google Cloud core) only) Select this option to use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate into your database (see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#setup_data_from_gcp) for more information).
    * **Service Account**: Select this option to use a BigQuery service account for Looker to authenticate into your database (see the Authentication with BigQuery service accounts for more information). When **Service Account** is selected, you will see the following fields: 
      * **Upload service JSON or P12 File**: Use the **Upload File** button to upload the certificate file for the BigQuery service account. You can get this file from the Google Cloud API Manager as a step in the Creating a service account and downloading the JSON credentials certificate procedure.
      * **Service Account Email**: This field applies only if you upload a P12 file in the **Upload service JSON or P12 File** field. Enter the email address for the BigQuery service account, which you get from the Google Cloud API Manager as a step in the Creating a service account and downloading the JSON credentials certificate procedure.
      * **Password**: The password for the P12 credentials file for the BigQuery service account. The **Password** field applies only if you upload a **P12** file in the **Upload service JSON or P12 File** field.
    * **OAuth**: Select this option to enable each Looker user to authenticate into Google BigQuery and authorize Looker to access the database with the user's BigQuery account. See the Authentication with OAuth section on this page for more information on implementing OAuth for your BigQuery connection. When **OAuth** is selected, you will see the following fields:

      * **OAuth Client ID**: The OAuth client ID. You get this information from the Google Cloud console as a step in the Generating Google OAuth credentials procedure.
      * **OAuth Client Secret**: The OAuth client secret. You get this information from the Google Cloud console as a step in the Generating Google OAuth credentials procedure.
**Note:** For Looker (Google Cloud core) instances, when you select **OAuth** , Looker can automatically use the OAuth application credentials that your Looker admin used when they created the Looker (Google Cloud core) instance. See the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#oauth-options) for more information.


  * **Max connections per node** : The maximum number of connections that Looker can establish with your database. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.
  * **Connection Pool Timeout** : If your users request more connections than the **Max connections per node** setting is configured for, the requests will wait for others to finish before they are executed. The **Connection Pool Timeout** is the maximum amount of time that a request will wait. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#connection-pool-timeout) documentation page for more information.
  * **Max concurrent queries for this connection** : The maximum number of concurrent queries Looker can submit to your database connection at once. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max-queries) documentation page for more information.
  * **Max concurrent queries per user for this connection** : The maximum number of concurrent queries Looker will submit to this database connection at once for each user. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max-queries-per-user) documentation page for more information.
  * **Max Billing Gigabytes**: On BigQuery connections, you are charged for each query based on its size. To help prevent users from accidentally running a query that is too expensive, you can set a maximum number of gigabytes that a user is allowed to pull in a single query. You can leave the **Max Billing Gigabytes** field blank if you aren't limiting query size. See the [BigQuery pricing page](https://cloud.google.com/bigquery/pricing#high-compute) for more information.
  * **Additional JDBC parameters**: Add any additional JDBC parameters, such as BigQuery labels (see the Job labels and context comments for BigQuery connections section on this page for more information). See the Supported JDBC parameters section on this page for the list of parameters that Looker supports. These are some of the supported parameters: 
    * `connectTimeout`: Number of milliseconds to wait for a connection. Defaults to 240000.
    * `readTimeout`: Number of milliseconds to wait for a read. Defaults to 240000.
    * `RootURL`: If you have a BigQuery instance in a private network, specify an alternate endpoint to connect to BigQuery other than the default public endpoint.
  * **Maintenance Schedule** : The `cron` interval for the Looker regenerator. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#maintenance_schedule) documentation page for more information.
  * **Disable Context**: This option disables [context comments](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#context_comments_for_sql_queries) on a BigQuery connection. Context comments on Google BigQuery connections are disabled by default because context comments invalidate Google BigQuery's ability to cache and can negatively impact cache performance. You can enable context comments for a BigQuery connection by turning off the **Disable Context** toggle. See the Job labels and context comments for BigQuery connections section for more information.
  * **SSL** : Enable the toggle to use SSL encryption to protect data as it passes between Looker and your database. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#ssl) documentation page for more information.
  * **Precache tables and columns** : If you want SQL Runner to not preload table information and, instead, to load table information only when a table is selected, clear this option. See the [Precache tables and columns](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#sql_runner_precache) section of the **Connecting Looker to your database** page for more information.
  * **Fetch and cache schema** : If you know that your information schema is slow, you can disable the **Fetch and cache schema** option for your connection. Disabling this feature will prevent some of the Looker SQL optimization for certain features, so you should enable the **Fetch and cache schema** option unless you know that your connection's information schema is particularly slow. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#fetch_information_schema_for_sql_writing) documentation page for more information.

  * **Enable PDTs** : Enable this toggle to allow [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)) on the connection. See the Persistent derived tables on a BigQuery connection section on this page for more information. You will need to specify the temporary dataset on your database that Looker will use to write PDTs. See the Creating a temporary dataset for persistent derived tables section on this page for the procedure. Note: If your connection is configured for **OAuth**, you will need to use the **PDT Overrides** section to specify a service account that Looker can use for PDT processes on your BigQuery connection. See the Enabling PDTs for Looker connections to BigQuery with OAuth section for details.

  * **Temp Project** : The project ID of the project that contains the dataset you want to use to write PDTs. If a **Temp Project** is not specified, then Looker writes PDTs to the project specified in the **Storage Project ID** field of the **Database Settings** section of the connection settings. If a **Storage Project ID** is not specified, then Looker writes PDTs to the project specified in the **Billing Project ID** field of the **Database Settings** section of the connection settings.

**Note:** **Temp Project** is not supported on Looker instances that are enabled for the [**Use Legacy Connections Page**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_connections) legacy feature.**Warning:** Changing the **Temp Project** field for an existing connection will trigger a rebuild of the PDTs on the connection. 
  * **Temp Database** : The BigQuery dataset that you created in the Google Cloud console to allow Looker to write persistent derived tables to your database. See the Creating a temporary dataset for persistent derived tables section for the procedure.

**Warnings:**
    * If you have multiple Looker instances, such as a production and QA instance, make sure to set different temporary datasets for each instance to avoid PDT management conflicts.
    * Changing the **Temp Database** field for an existing connection will trigger a rebuild of the PDTs on the connection.
  * **Max Number of PDT Builder Connections** : The maximum number of concurrent table builds that the Looker regenerator can initiate on your database connection. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_pdt_builder_connections) documentation page for more information.

  * **Retry failed PDT builds** : When the **Retry Failed PDT Builds** toggle is enabled, the Looker regenerator will attempt to rebuild a PDT that failed in the previous regenerator cycle, even if the PDT's trigger condition is not met. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#retry_failed_pdt_builds) documentation page for more information.

  * **PDT API Control** : This toggle determines whether the [`start_pdt_build`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/start_pdt_build), [`check_pdt_build`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/check_pdt_build), and [`stop_pdt_build`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/stop_pdt_build) API calls can be used for this connection. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#enable_pdt_api_control) documentation page for more information.

  * **Enable PDT Overrides** : Enable this toggle to configure separate connection settings that Looker should use for writing PDTs to your database. See the PDT Overrides section on this page for more information on the PDT Overrides fields.

  * **Database Time Zone** : The default time zone for BigQuery is UTC. The time zone setting that you specify here needs to match your BigQuery time zone setting. See the [Database Time Zone](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database_time_zone) section of the **Connecting Looker to your database** page for more information.

  * **Query Time Zone** : See the [Query Time Zone](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#query_time_zone) section of the **Connecting Looker to your database** page for more information.




Once you fill in all the applicable fields for the connection, you can test your connection as needed.

To save these settings, click **Connect**.

## Testing the connection

You can test your connection settings from a couple of places in the Looker UI:

  * Click the **Test** button at the bottom of the **Connections Settings** page, as described on the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#testing_your_connection_settings) documentation page.
  * Click the **Test** button by the connection's listing on the **Connections** admin page, as described on the [Connections](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#testing_connections) documentation page.



For new connections, if Looker displays **Can connect** , then select **Add connection**. Looker will run the rest of the connection tests to verify that the service account was set up correctly and with the proper roles.

![](https://docs.cloud.google.com/static/looker/docs/images/setup-bq-successful-test-520.png)

### Testing a connection that uses OAuth

  1. In Looker, go into [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode).
  2. For an existing BigQuery connection that uses OAuth, [navigate to the project files](https://docs.cloud.google.com/looker/docs/accessing-project-files) for a Looker project that uses your BigQuery connection. For new BigQuery connections that use OAuth, open a [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) and replace the model's [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) value with the name of the your new BigQuery connection, and then save the model file.
  3. Open one of the model's Explores or dashboards and run a query. When you try to run a query, Looker will prompt you to [log in](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#authenticating_into_google_from_a_query) with your Google Account. Follow the Google OAuth login prompts.



## Job labels and context comments for BigQuery connections

For BigQuery connections, Looker sends query context in the form of BigQuery [job labels](https://docs.cloud.google.com/bigquery/docs/viewing-labels#viewing_job_labels). By default, Looker sends the following context label keys for BigQuery connections:

  * **`looker-context-user_id`** : The unique identifier for each user on the Looker instance. You can match this user ID to the user IDs on the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#viewing_and_searching_users) page in the **Admin** menu.
  * **`looker-context-history_slug`** : The unique identifier for each query that is run on the database by the Looker instance.

  * **`looker-context-instance_slug`** : The ID number of the Looker instance that issued the query. Looker support can use this information to help you troubleshoot, if necessary.




You can configure additional job labels for Looker to send with every query on the BigQuery connection by using the **Additional JDBC parameters** text field of the **Connections** page. In the **Additional JDBC parameters** field, add an additional JDBC parameter, `labels`, and provide a comma-separated list of URL-encoded `key=value` pairs. For example, if you include this in the **Additional JDBC parameters** field:
    
    
    labels=this%3Dconnection-label,that%3Danother-connection-label
    

The `%3D` is the URL-encoding for `=`, so this would add the following two labels to every query that Looker sends to the BigQuery database, in addition to the default Looker context labels:

  * `this`: `connection-label`
  * `that`: `another-connection-label`



Note that BigQuery has [restrictions on job labels](https://docs.cloud.google.com/bigquery/docs/labels-intro#requirements):

  * Any connection label that has the same key as a context label will be ignored.
  * If the union of connection labels and context labels exceeds the maximum of 64 total labels, context labels are the first to be dropped, followed by connection labels, until the total number of labels is at most 64.



Looker ensures that context labels conform to all BigQuery's label validity requirements, but does not check connection labels for validity. Configuring invalid connection labels may cause queries to fail.

The BigQuery job labels that Looker sends by default (`looker-context-user_id`, `looker-context-history_id`, and `looker-context-instance_slug`) correspond to the [SQL context comments](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#sql_comments) that Looker attaches to SQL queries for database dialects other than BigQuery. For BigQuery connections, context comments are disabled by default because they invalidate BigQuery's ability to [cache](https://docs.cloud.google.com/bigquery/docs/cached-results), and can negatively impact cache performance. You can enable context comments for a BigQuery connection by turning off the **Disable Context** toggle for the BigQuery connection. We recommend that you keep the default setting for **Disable Context Comment** , so that you are able to use BigQuery's cache. But if you deselect the **Disable Context Comment** option for a BigQuery connection, Looker will send SQL context comments _and_ BigQuery job labels to your database.

SQL context comments and BigQuery job labels convey the same information. For example, Looker might generate the following SQL context comments for a query:
    
    
    -- Looker Query Context
    
    '{"user_id":1,"history_id":4757,"instance_slug":"ec2804ddef74c466f2a43e0afaa3ff6b"}'
    

Then Looker would generate the following BigQuery job labels for the same query:
    
    
    [{"value":"1","key":"looker-context-user_id"},
    
     {"value":"4757","key":"looker-context-history_id"},
    
     {"value":"ec2804ddef74c466f2a43e0afaa3ff6b","key":"looker-context-instance_slug"}]
    

![](https://docs.cloud.google.com/static/looker/docs/images/admin-google-context-comments-2202.png)

## Supported JDBC parameters

For Google BigQuery, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `AdditionalProjects`
  * `connectTimeout`
  * `DefaultDataset`
  * `EnableHighThroughputAPI`
  * `EnableSession`
  * `EndpointOverrides`: For public Looker instances, the value for the `EndpointOverrides` parameter must be the public IP address of the instance.
  * `HighThroughputActivationRatio`
  * `HighThroughputMinTableSize`
  * `HttpConnectTimeout`
  * `HttpReadTimeout`
  * `JobCreationMode`
  * `JobTimeout`
  * `KMSKeyName`
  * `labels`
  * `LargeResultsDatasetExpirationTime`
  * `Location`
  * `MaxResults`
  * `oauthaccesstoken`
  * `ProjectId`
  * `QueryProperties`
  * `readTimeout`
  * `RequestGoogleDriveScope`
  * `RetryInitialDelay`
  * `RetryMaxDelay`
  * `RootURL`: For public Looker instances, the value for the `RootURL` parameter must be the public IP address of the instance.
  * `Timeout`
  * `UnsupportedHTAPIFallback`
  * `UseQueryCache`



## Feature support

For Looker to support some features, your database dialect must also support them.

### Google BigQuery Standard SQL

Google BigQuery Standard SQL supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
### Google BigQuery Legacy SQL

Google BigQuery Legacy SQL supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
## Troubleshooting

### `Dataset not found in location US` error

Scheduled queries or connection tests in Looker (original) may intermittently fail with an error like the following:

`SQL Error Query execution failed: - Not found: Dataset [dataset_name] was not found in location US`

This error can occur even if the dataset exists in a non-US location. In Looker (original) instances that are configured to use Application Default Credentials (ADC) through the legacy connection UI, transient credential validation or metadata lookup failures can cause Google BigQuery to fail to auto-detect the dataset's location. When this auto-detection fails, Google BigQuery defaults to the `US` multi-region, misreporting the transient permission or metadata lookup failure as a location issue.

To resolve or work around this issue, use one of the following methods:

  * **Specify the dataset location** : Explicitly set the dataset's processing region in the connection settings. In the **Additional JDBC parameters** field, add the `Location` parameter set to the actual region code where your data resides (for example, `;Location=northamerica-northeast1`).
  * **Transition to standard authentication** : Transition away from ADC or service account impersonation in Looker (original) to a standard **Service Account** connection that uses a JSON private key, or configure **OAuth**. ADC is no longer supported in Looker (original), and its configuration UI is being deprecated.
  * **Migrate to Looker (Google Cloud core)** : Migrate to a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance, which natively supports [ADC](https://docs.cloud.google.com/looker/docs/looker-core-dialects#setup_data_from_gcp) authentication without requiring exported service account keys.



## Next steps

After you've connected your database to Looker, [configure sign-in options for your users](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
