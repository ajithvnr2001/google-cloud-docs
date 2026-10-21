---
url: https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore/
title: Admin settings - Self-service Explores \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:48:32.943033+00:00
---

# Admin settings - Self-service Explores  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Self-service Explores Stay organized with collections  Save and categorize content based on your preferences. 

With the [**Self-service Explores**](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, your Looker users can upload CSV, XLS, and XLSX files, import Google Sheets, or connect directly to database tables to query and visualize data in a Looker Explore without needing to configure a LookML model or set up Git version control.

Looker admins can select the **Self-service Explores** option from the Looker **Admin** menu to configure the **Self-service Explores** feature and view self-service data sources on the instance. The **Self-service Explores** admin page contains the following tabs:

  * **Database tables** : Enable the **Allow connecting to database tables** option so users can build data models from database tables by using the [visual modeling canvas](https://docs.cloud.google.com/looker/docs/visual-modeling).
  * **Uploads and imports** : Configure database connections for self-service data uploads, enable **Google Sheets data import** , and set up OAuth credentials for Google Sheets.
  * **Audit history** : View and manage self-service Explores on the instance by using the **Data sources** table.



## Before you begin

To use self-service Explores, your Looker instance must meet the following requirements:

  * Running Looker 25.20 or later for BigQuery connections, Looker 26.8 or later for Snowflake connections, or Looker 26.14 or later for connecting to database tables with the [visual modeling canvas](https://docs.cloud.google.com/looker/docs/visual-modeling).
  * Has a connection to a [BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery) or [Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake) database, and the connection must be configured in the following ways: 
    * The connection must be configured with the **All projects** scope. To verify the connection's scope, see the **Scope** column in the [**Databases** tab](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#databases_tab) of the **Connections** page in the Looker admin menu. The connection's **Project Scope** value cannot be edited once the connection is created.
    * The connection must be enabled for persistent derived tables (PDTs). To verify that PDTs are enabled on the connection, open the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) page, click the **Edit** button for the connection, click to open the **Optional Settings** tab, and then verify that the [**Enable PDTs**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#enable_pdts) toggle is turned on.
    * For BigQuery connections that use [authentication with OAuth](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#authentication_with_oauth), users must have permission to view tables in the scratch schema to see uploaded data. This configuration is the same as the one that's required for users to [use persistent derived tables (PDTs) with an OAuth connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#enabling_pdts_for_connections_to_with_oauth).
  * For Snowflake connections, a database administrator must grant `CREATE STAGE` to the Looker role. For details, see the documentation page for [creating a Looker connection to Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake#ssexplores-grant).
  * For any user who will be creating self-service Explores from uploaded files, their Looker user account must have the [`upload_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#upload_data) permission. For users who are creating self-service Explores from database tables, their user account must have the [`create_self_service_from_table`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_self_service_from_table) permission.



Note the following limitations for uploading data from Google Sheets:

  * [Looker (Google Cloud core) instances that use Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) don't support the OAuth flow for Google Sheets uploads. These instances must use the [manual URL flow](https://docs.cloud.google.com/looker/docs/exploring-self-service#url) to upload data from Google Sheets.
  * [Looker (Google Cloud core) instances that use VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) don't support Google Sheets uploads.



## Enabling self-service Explores

**Important:** To support the [Self-service Explore](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, upon upgrade to Looker 25.20, your Looker instance adds the [`upload_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#upload_data) permission to any [role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) or [permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission-sets) that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission, including custom permission sets. If you enable data uploads on a Looker instance, any user with the `upload_data` permission will be able to upload data to create self-service Explores on your instance. 

### Enabling connections to database tables

To allow users to connect directly to database tables and build models by using the [visual modeling canvas](https://docs.cloud.google.com/looker/docs/visual-modeling), perform the following steps:

  1. From the **General** section of the Looker **Admin** menu, select the **Self-service Explores** admin page.
  2. On the **Self-service Explores** admin page, select the **Database tables** tab.
  3. Turn on the **Allow connecting to database tables** option.



### Enabling file uploads and Google Sheets imports

Before your users can upload files or import Google Sheets to create self-service Explores, a Looker admin must configure the feature on the **Uploads and imports** tab by performing the following steps:

  1. From the **General** section of the Looker **Admin** menu, select the **Self-service Explores** admin page and open the **Uploads and imports** tab.
  2. If you want to enable your users to select from multiple connections for their data uploads, enable the **Advanced connection governance** option. See the Advanced connection governance section for more information.
  3. Configure one or more connections for self-service uploads: 
     * If **Single default connection** is enabled: From the **Default connection** drop-down menu, select the connection to use for storing the data for self-service Explores. Looker will save the data to this database for the self-service Explores on your instance. 
     * If **Advanced connection governance** is enabled: In the **Connections** table, find the connection or connections that you want to use for self-service uploads and enable the toggle for **Data upload enablement** for each connection that you want to support data uploads. When a user [creates a self-service Explore](https://docs.cloud.google.com/looker/docs/exploring-self-service#upload-data), Looker lets the user choose from a list of the enabled connections to which the user has access and save the data to the specified database.
  4. Click the **Test** button to verify the connection configuration:

     * If **Single default connection** is enabled: Click the **Test** button next to the **Data uploads** toggle to verify that the default connection is valid and that the connection is enabled for persistent derived tables (PDTs) (see the Before you begin section for connection requirements). 
     * If **Advanced connection governance** is enabled: Click the **Test** button next to each enabled connection in the **Connections** table.

If the test fails, you cannot enable data uploads for that connection. Go to the [**Connections** admin page](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) to troubleshoot the connection.

  5. If the tests pass, turn on the **Data uploads** toggle to enable the self-service Explores feature.

  6. If you want your Looker instance to support [uploading data from Google Sheets](https://docs.cloud.google.com/looker/docs/exploring-self-service#from-sheets), do the following:

     * Verify that you have configured a BigQuery connection for self-service Explores (Google Sheets uploads are supported only on BigQuery connections).
     * Use the Google Cloud console to enable the required APIs to support Google Sheets uploads.
     * Optionally enable OAuth for Google Sheets uploads if you want to enable your users to use Google Drive navigation to select a Google Sheets file for data upload.
     * Test and enable Google Sheets uploads: 
       * If **Single default connection** is enabled: Click the **Test** button next to the **Google Sheets data import** toggle to test the connection for Google Sheets uploads. If the test passes, enable the **Google Sheets data import** toggle.
       * If **Advanced connection governance** is enabled: Click the **Test** button for **Google Sheets imports** in the **Connections** table for each connection that you want to enable for Google Sheets uploads. If the test for a connection passes, enable the **Google Sheets imports** toggle for the connection. (Both the **Data uploads** toggle and the **Google Sheets imports** toggle must be enabled for a connection to upload data from Google Sheets.)



### Enabling the APIs to support Google Sheets uploads

To enable Looker to support uploading data from Google Sheets for BigQuery connections, the following APIs must be enabled in the Google Cloud console by an IAM user with the IAM [`roles/serviceusage.serviceUsageAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) role:

  * This API must be enabled in the Google Cloud project that houses the BigQuery connection that is specified in the **Default connection** drop-down menu of the **Self-service Explores** admin page (or in the Google Cloud projects that house any BigQuery connections that are enabled for **Google Sheets imports** under Advanced connection governance):

    * BigQuery API: Required for all BigQuery operations
  * These APIs must be enabled in the Google Cloud project that is associated with the service account used to upload data (the service account that is used for [PDT processes on your BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#persistent-derived-tables-on-a-connection), which may or may not be the same as the Google Cloud project that houses the BigQuery connection):

    * BigQuery API: Required for all BigQuery operations
    * Google Drive API: Required for BigQuery to read files from Drive
  * This API must be enabled in either the Google Cloud project that is associated with the service account used to upload data or the Google Cloud project that owns the [OAuth client ID credentials](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enabling_oauth_for_uploads), depending on how your users authenticate to access Google Sheets documents:

    * Google Sheets API: Required for retrieving the names of each sheet in a Google Sheets document



Perform the following steps to enable the APIs:

  1. From the Google Cloud console **Open project picker** , select the project that houses the BigQuery connection that is specified in the **Default connection** drop-down menu of the **Self-service Explores** admin page (or that houses a connection enabled for **Google Sheets imports** under Advanced connection governance).

  2. In the Google Cloud console navigation menu, go to **APIs & Services > Library**, open the BigQuery API, and enable the BigQuery API if it isn't already enabled.

[Go to BigQuery API](https://console.cloud.google.com/apis/library/bigquery.googleapis.com)

  3. Still on the BigQuery API page, from the Google Cloud console **Open project picker** , select the Google Cloud project that is associated with the service account used to upload data (the service account that is used for [PDT processes on your BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#persistent-derived-tables-on-a-connection)). Enable the BigQuery API, if the API isn't already enabled.

  4. In the Google Cloud console navigation menu, go to **APIs & Services > Library**, open the Google Drive API, and enable the Google Drive API if it isn't already enabled.

[Go to Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com)

  5. In the Google Cloud console navigation menu, go to **APIs & Services > Library** and open the Google Sheets API. Enable the Google Sheets API in one or both of the following projects, depending on the upload flows that your implementation supports:

     * If your users upload data from Google Sheets by using [Google Drive navigation with OAuth authentication](https://docs.cloud.google.com/looker/docs/exploring-self-service#oauth), you must enable the Google Sheets API in the Google Cloud project that owns the OAuth client ID credentials, because Google Cloud evaluates API enablement and quota against the OAuth client ID's project.
     * If your users upload data from Google Sheets by using the [manual URL flow with service account authentication](https://docs.cloud.google.com/looker/docs/exploring-self-service#url), you must enable the Google Sheets API in the Google Cloud project that is associated with the service account used to upload data.

**Tip:** In Looker 26.14 and earlier, updating data for a self-service Explore always uses the service account credentials; therefore, if your OAuth client ID credentials are in a separate Google Cloud project from your service account, you must enable the Google Sheets API in both Google Cloud projects.

[Go to Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com)




### Configuration for Private Service Connect instances

If your Looker (Google Cloud core) instance uses [Private Service Connect (PSC)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc), you must perform an extra step to support Google Sheets uploads.

To allow Looker to reach the Google Sheets API, you must publish Google Sheets as a service by using Private Service Connect and then add Google Sheets to the Local FQDN setting in your Looker (Google Cloud core) configuration. When configuring the Local FQDN, use `sheets.googleapis.com` in the **Local FQDN** field and the published service's service attachment URI in the **Target Service Attachment URI** field. For instructions, see the [Connect to published services using Local FQDN](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#local-fqdn) documentation.

### Enabling OAuth for Google Sheets uploads

**Important:** Looker (Google Cloud core) instances that use Private Service Connect don't support the OAuth flow for Google Sheets uploads. These instances must use the [manual URL flow](https://docs.cloud.google.com/looker/docs/exploring-self-service#url) to upload data from Google Sheets. 

After you have enabled self-service Explores, enabled the APIs to support Google Sheets uploads, and enabled the **Google Sheets data import** toggle, you can also enable your users to [use Google Drive navigation to select Google Sheets documents for data uploads](https://docs.cloud.google.com/looker/docs/exploring-self-service#oauth).

To enable Google Drive navigation on your Looker instance, an IAM user with the [required roles](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#required-roles) must create an OAuth client in the Google Cloud console and then enter the OAuth credentials into the **Self-service Explores** admin page on your Looker instance, as described in the procedure in this section.

**Note:** Before you can generate your OAuth credentials, Google requires that you configure an OAuth consent screen, which lets your users choose how to grant access to their private data. If you haven't yet configured an OAuth consent screen for your selected Google Cloud console project, the Google Cloud console will display a notice with a **Configure consent screen** button. Click the button and follow the procedure on the [Configure the OAuth consent screen and choose scopes](https://developers.google.com/workspace/guides/configure-oauth-consent#configure_oauth_consent) Workspace documentation page, and then return to this procedure.

To create the OAuth client and enter the credentials in your Looker instance, follow these steps:

  1. In the Google Cloud console, use the Google Cloud console **Open project picker** to select the Google Cloud project where you want to create the OAuth client. This project can be the same Google Cloud project that is associated with the service account used to upload data (the service account that is used for [PDT processes on your BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#persistent-derived-tables-on-a-connection)) or a separate Google Cloud project. Make sure that the Google Sheets API is enabled in the Google Cloud project that owns the OAuth client.

[ Go to Google Cloud console](https://console.cloud.google.com/)

  2. Use the Google Cloud console main menu to navigate to **APIs & Services > Credentials**.

  3. From the **Credentials** page, click the **Create Credentials** drop-down menu, and then select **OAuth client ID**.

  4. In the **Application type** drop-down, select **Web application**.

  5. In the **Name** field, enter a name for your OAuth client, such as `Looker upload data from Sheets`.

  6. In the **Authorized JavaScript origins** section, click the **Add URI** button. Enter your Looker instance URL:
         
         https://LOOKER_INSTANCE_URL
         

  7. Click **Create**.

  8. After you click **Create** , an **OAuth client created** window appears. This window displays the client ID and client secret that the Google Cloud console created for your OAuth client. Copy and make note of these values.

  9. In your Looker instance, select **Self-service Explores** from the **General** section of the **Admin** panel.

  10. On the **Self-service Explores** page, select the **Uploads and imports** tab, and, in the **Client ID** and **Client secret** fields, paste the values that you copied from the Google Cloud console when you created the OAuth client in the Google Cloud console.

  11. Click **Save**.

  12. Click the **Test** button next to the **Google Sheets data import** toggle to test the OAuth configuration in addition to the Google Sheets upload configuration. (You can also click the **Test** button by the **Data uploads** toggle to verify the connection in addition to the Google Sheets configuration.)




Now, when your users upload data by using the **Import from cloud** option, Looker displays [Google Drive navigation for selecting Google Sheets documents](https://docs.cloud.google.com/looker/docs/exploring-self-service#oauth). 

## Advanced connection governance

By default, self-service Explores are saved to a single default database connection that is specified by a Looker admin. However, if you enable the **Advanced connection governance** option on the **Self-service Explores** admin page, you can configure your instance with multiple database connections for storing self-service Explore data. Under **Advanced connection governance** , only users who have permission on an allowed connection can select that connection to store and query their uploaded data.

### Enabling multiple connections

When **Advanced connection governance** is enabled, the **Self-service Explores** admin page displays a **Connections** table listing all database connections on your instance that meet the requirements for self-service Explores. From this table, a Looker admin can perform the following actions for each connection:

  * Enable or disable specific upload flows by using the toggles in the **Data upload enablement** column (for file uploads) and the **Google Sheets imports** column (for Google Sheets uploads).
  * Test the connection's validity and persistent derived table (PDT) status by clicking the **Test** button in the **Data upload enablement** column, and test the connection for configuration for Google Sheets uploads.



### Connection selection during upload

When a user initiates a data upload by using the [**Upload from local**](https://docs.cloud.google.com/looker/docs/exploring-self-service#files-from-computer) tab or the [**Import from cloud**](https://docs.cloud.google.com/looker/docs/exploring-self-service#oauth) tab in the **Create data source** dialog, the first step is to select a connection. Users can select from a drop-down list of allowed connections. Looker filters this list so that a user sees only the connections that are configured to be used by models for which that user has the [`upload_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#upload_data) permission. The user cannot upload data to any other connection.

### User permissions and connection access

Under **Advanced connection governance** , ongoing access to self-service data uploads is strictly bound to the underlying database connection:

  * **Continued access to existing uploads** : Most user actions on a data upload after creation require continued access to the underlying connection. If a user's access to a database connection is revoked, they can no longer view, query, edit, or have shared with them any self-service Explores that use that connection, even if they originally uploaded the data. The self-service Explore will continue to function for other users who still have access to the connection.
  * **Query access** : Continued query access to a self-service Explore requires the user to have the [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) permission on at least one LookML model that is configured to use the underlying database connection for that upload.
  * **Sharing self-service Explores** : Users can only share a self-service Explore with other users or groups that have the [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) permission on a LookML model that is configured to use the underlying database connection for that upload.



### Admin permissions

Looker admins (users who are designated with the Looker Admin role) are considered to have the [`upload_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#upload_data) permission on all models on the instance. Admins can view what data sources exist on a Looker instance, but to view or edit a self-service Explore, the admin must be [granted a role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#assigning_roles) with [access to that specific self-service model](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets).

### Disabling Advanced connection governance

If you decide to turn off **Advanced connection governance** on an instance where it was previously enabled, be aware of the following implications:

  * **Lenient authorization** : The authorization model becomes more permissive. Because connection-level governance is no longer enforced, self-service data uploads can be shared with any user on the instance.
  * **Query access** : Users will continue to be able to query existing self-service data uploads that they had access to before **Advanced connection governance** was disabled.
  * **Role changes** : Connection governance controls are disabled, meaning any future role or permission changes won't restrict access to existing self-service data uploads.
  * **Default connection requirement** : When **Advanced connection governance** is turned off, users can upload data to only the single connection that's selected in the **Default connection** drop-down menu. If your instance used self-service uploads only while **Advanced connection governance** was enabled, a default connection may not have been selected yet. A Looker admin must select and test a default connection when reverting to keep self-service uploads operational.



## Viewing the data sources on your Looker instance

If self-service Explores are enabled on your instance, a Looker admin can select the **Audit history** tab on the **Self-service Explores** admin page to view the **Data sources** table, which lists the self-service Explores that your users have created on the instance.

The **Data sources** table shows the following information about the self-service data sources on your instance:

  * The name of the self-service Explore, which is also a hyperlink that opens the self-service Explore
  * The owner of the data source
  * The date that the data source was created
  * A **Delete** button that allows Looker admins to delete the data source and its associated self-service Explore



Looker admins can open any self-service Explore on the instance by using the links in the **Data sources** table. However, the **Self-service Explores** section of the Looker **Explore** menu lists only the self-service Explores that you own or that the owner has specifically shared with you. The **Explore** menu doesn't list every self-service Explore on the instance for Looker admins, since that could make the **Explore** menu cumbersome.

## Removing a data source

The owner of a data source can [remove their data source from the **Edit Self-service Explore** page](https://docs.cloud.google.com/looker/docs/exploring-self-service#remove_upload). In addition, a Looker admin can remove a data source from the **Self-service Explores** admin page by following these steps:

  1. From the **General** section of the Looker **Admin** menu, select the **Self-service Explores** admin page.
  2. Select the **Audit history** tab.
  3. In the **Data sources** table, click the **Delete** button for the data source that you want to remove. 
  4. Click **Delete** in the confirmation dialog.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
