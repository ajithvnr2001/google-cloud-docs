---
url: https://docs.cloud.google.com/looker/docs/exploring-self-service/
title: Creating self-service Explores \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:34.940930+00:00
---

# Creating self-service Explores  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/exploring-self-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating self-service Explores Stay organized with collections  Save and categorize content based on your preferences. 

Using the **Self-service Explores** feature, you can specify a data source and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control. The following data sources are supported:

  * For Looker connections to BigQuery:

    * Comma-separated files (CSV)
    * Excel files (XLS and XLSX)
    * Google Sheets files
    * BigQuery tables
  * For Looker connections to Snowflake:

    * Comma-separated files (CSV)
    * Excel files (XLS and XLSX)



See the Before you begin and Uploading data to create a self-service Explore sections for details on the requirements and procedures.

After you upload your file, Looker analyzes the data: For each of the fields in the data file, Looker automatically detects the data type and applies the appropriate format for it. Looker also applies a name and a label for each field. Looker creates a LookML model of the data and persists the data by writing it to the BigQuery or Snowflake database that is [specified by your Looker admin](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enable_self-service_explores) or that you specify during the upload process (if your Looker admin has enabled **Advanced connection governance**). When the model is ready, Looker displays the **Edit Self-service Explore** page.

After you upload your data, you can do the following:

  * Open the Explore to create Looker queries that are based on your uploaded data.
  * Add dimensions and measures to your Explore.
  * Manage access to your Explore so that other users can query your Explore.
  * Certify the Explore so that other users know the data is reliable.
  * Remove the data if you no longer need it.



## Before you begin

To use self-service Explores, you must have the following:

  * A Looker instance that meets the following requirements: 
    * Running the minimum Looker version: 
      * To upload data on a BigQuery connection, your instance must be running Looker 25.20 or later. 
      * To upload data on a Snowflake connection, your instance must be running Looker 26.8 or later. 
    * [Configured by a Looker admin to enable self-service Explores](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore).
  * A Looker user account with the [`upload_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#upload_data) permission, which allows a user to upload data files to your instance.



## Uploading data to create a self-service Explore

**Warning:** Before uploading your data, note the following: 

  * Because Looker writes your data to your database connection, your database administrators will be able to view the data that you upload.
  * Self-service Explores may be lost in case of an instance migration or a system backup and recovery.



The following sections provide information on creating self-service Explores from different data sources:

  * Uploading data files from your computer (CSV, XLS, and XLSX files)
  * Uploading data from Google Sheets
  * Using data from a BigQuery table



### Uploading data files from your computer (CSV, XLS, and XLSX files)

You can create a self-service Explore from a file on your computer as long as the file meets the following requirements:

  * The file must be 100 MB or smaller.
  * The file must be a comma-separated values text file (CSV) or an Excel file (XLS or XLSX).
  * For CSV files, the first row of data in the CSV file must contain the column names for the file.

**Note:** For BigQuery connections, if your data file contains only string values in all columns, BigQuery may include the header rows as part of your data and create generic names for each column, such as `string_field_0` and `string_field_1`. In this case, you can edit the self-service Explore and rename the data fields.

To create a self-service Explore from a data file on your computer, follow these steps:

  1. From the [Looker main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu), click the **Create** button.
  2. Select **Data source** from the drop-down menu. This action opens the **Create data source** dialog.
  3. In the **Create data source** dialog, select the **Upload from local** tab.
  4. If your Looker admin has enabled **Advanced connection governance** , select the connection to use for your data upload from the **Connection** drop-down menu. You will only see the connections that you have permission to use for data uploads. After selecting the connection, click **Continue**.
  5. Click the **Choose data** button to navigate to and select your data file. (Alternatively, you can drag a file into the **Create data source** dialog.)
  6. If you selected an Excel file that has more than one worksheet, specify which worksheet to upload from the **Sheet in selected Excel file** drop-down menu. 
  7. Click **Upload**.



When the model is ready, Looker displays the **Edit Self-service Explore** page.

### Uploading data from Google Sheets

Looker supports creating a self-service Explore from a tab in Google Sheets. In addition to the requirements for self-service Explores, the following are required:

  * A Looker instance that your Looker admin has enabled for **Data uploads** and **Google Sheets data import** (see [Admin settings - Self-service Explores](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enable) for information).
  * A BigQuery connection that is enabled by your Looker admin on the **Self-service Explores** admin page.
  * [The required APIs that are enabled by your Looker admin](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enable-apis).
  * A Google Sheets document that you have permission to share, and where the first row of data in the Google Sheets tab contains the column names for the data.



Note the following limitations for uploading data from Google Sheets:

  * Looker (Google Cloud core) instances that use Private Service Connect don't support the OAuth flow for Google Sheets uploads. These instances must use the manual URL flow to upload data from Google Sheets.
  * Looker (Google Cloud core) instances that use VPC Service Controls don't support Google Sheets uploads.
  * If your data contains only string values in all columns, Looker may include the header rows as part of your data and create generic names for each column, such as `string_field_0` and `string_field_1`. In this case, you can edit the self-service Explore and rename the data fields.



The following sections describe the two ways that you can upload a Google Sheets document to create a self-service Explore:

  * Using the Google Drive navigation to select your Google Sheets document: If your Looker admin has enabled the **Data Uploads** toggle, enabled the **Google Sheets data import** toggle, and configured OAuth for your instance (as described in the [Enabling OAuth for Google Sheets uploads](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enabling_oauth_for_uploads) section), you can use Google Drive navigation to select a tab in your Google Sheets document to upload.
  * Manually specifying the URL for your Google Sheets document: If your Looker admin has enabled the **Data Uploads** toggle and the **Google Sheets data import** toggle, but has not configured OAuth for your instance, you can enter the URL for your Google Sheets document and then manually share the Google Sheets document with the Looker service account so that Looker can upload the data.



#### Specifying Google Sheets data using Google Drive navigation

To create a self-service Explore from a Google Sheets file using Google Drive navigation, follow these steps:

  1. From the [Looker main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu), click the **Create** button.
  2. Select **Data source** from the **Create** drop-down menu. This action opens the **Create data source** dialog.
  3. In the **Create data source** dialog, click the **Import from cloud** tab.
  4. If your Looker admin has enabled **Advanced connection governance** , select the connection to use for your data upload from the **Connection** drop-down menu. You will only see BigQuery connections that you have permission to use for data uploads. After selecting the connection, click **Continue**.
  5. Click the **Browse Google Drive** button.
  6. From the **Sign in with Google** dialog, select the Google Account you want to use to navigate to your Google Sheets document.
  7. In the **looker.com wants access to your Google Account** dialog, click **Continue** to allow Looker to access your Google Drive files.
  8. In the **Select a file** dialog, navigate to the Google Sheets document that you want to upload, select the file, and then click **Select**.

**Tip:** If you receive an error that you don't have the ability to grant permission to the Google Sheets document, you can go to Google Drive and make a copy of the Google Sheets document, and then try again by selecting the copy of the Google Sheets document.
  9. If your Google Sheets document contains multiple tabs, the **Create data source** dialog will display a **Sheet** drop-down menu. Select the sheet that you want to upload, and then click **Continue**.




When the model is ready, Looker displays the **Edit Self-service Explore** page.

#### Specifying Google Sheets data using the document URL

To create a self-service Explore from a Google Sheets file using the Google Sheets URL, follow these steps:

  1. In a web browser, navigate to the Google Sheets document that you want to upload to Looker.
  2. In the Google Sheets document, select the tab for the specific Sheet that you want to upload.
  3. In the web browser URL, verify that the URL contains the following elements:

     * The spreadsheet ID: This is located in the URL between the `/d/` and the `/edit` or `/view` suffix.
     * The sheet/tab ID: This is the `gid` parameter that provides the ID of the Sheet.
  4. Copy the URL for the specific tab in Google Sheets that you want to upload, and keep this browser tab open.

  5. In another browser tab, open Looker; then, in the [Looker main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu), click the **Create** button.

  6. Select **Data source** from the **Create** drop-down menu. This action opens the **Create data source** dialog.

  7. In the **Create data source** dialog, click the **Import from cloud** tab.

  8. If your Looker admin has enabled **Advanced connection governance** , select the connection to use for your data upload from the **Connection** drop-down menu. You will only see BigQuery connections that you have permission to use for data uploads. After selecting the connection, click **Continue**.

  9. In the **Google Sheets URL** field, paste the URL for the tab in Google Sheets that you want to upload.

  10. In the **How to grant Google Sheet permission to Looker** section of the **Create data source** dialog, click the **Copy** button to save the Looker service account email to your clipboard. Leave the **Create data source** dialog open.

  11. Go back to the browser tab that contains your Google Sheet. In Google Sheets, click **Share**.

**Tip:** If you don't have permission to share the Google Sheets document, you can make a copy of the Google Sheets document, and then use the copy's URL to upload the data.
  12. In the **Share** dialog, do the following:

     * Paste the Looker service account email into the **Add people, groups, spaces, and calendar events** field.
     * In the drop-down menu next to the input field, select **Viewer**.
     * Clear the **Notify people** checkbox.
     * Click **Share**.
**Tip:** If you want to update the data for this self-service Explore in the future, keep the sharing access to the Looker service account for the Google Sheets document. Otherwise, you will need to re-share the Google Sheets document when you update the data.
  13. Return to the **Create data source** dialog. 

  14. Click **Continue**.




When the model is ready, Looker displays the **Edit Self-service Explore** page.

### Using data from a BigQuery table

Looker supports creating a self-service Explore from a table in a BigQuery database. In addition to the requirements for self-service Explores, the following are required:

  * A Looker instance that is running Looker 26.10 or later.
  * A BigQuery connection that's enabled by your Looker admin on the **Self-service Explores** admin page (see the [Admin settings - Self-service Explores](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enable) documentation page for information).
  * The BigQuery connection must be configured for [authentication with OAuth](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#authentication_with_oauth).
  * A Google Account that has the [`bigquery.jobUser`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) and [`bigquery.dataViewer`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) IAM roles for the BigQuery table you want to upload to Looker.



To create a self-service Explore from a table in your BigQuery database, follow these steps:

  1. From the [Looker main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu), click the **Create** button.
  2. Select **Data source** from the drop-down menu. This action opens the **Create data source** dialog.
  3. In the **Create data source** dialog, select the **Connect to database** tab.
  4. In the **Connect to database** tab, use the **BigQuery connection** drop-down menu to select from the BigQuery connections that you have access to on the Looker instance.
  5. If the dialog displays the **OAuth log in required** banner, click the **Log In** button to select your Google Account to use for OAuth login, and then click **Allow** when prompted.
  6. In the **Connect to database** tab, use the drop-down menus to select the BigQuery **Project** and **Dataset** that contain the table that you want to upload, and then select the **Table** that you want to upload to Looker.
  7. Click **Continue** to upload the table.



When the model is ready, Looker displays the **Edit Self-service Explore** page.

## Opening a self-service Explore

You can open any self-service Explore that you own or that the owner has [shared with you](https://docs.cloud.google.com/looker/docs/exploring-self-service#manage_access):

**Note:** If your Looker admin has enabled **Advanced connection governance** , continued access to a self-service Explore is dependent on your continued access to the underlying database connection. If your access to the connection is revoked, you will no longer be able to query, edit, or share any self-service Explores that use that connection. 

  * If you are the owner of the self-service Explore and you are on its **Edit Self-service Explore** page, you can click the **Explore Data** button to open the Explore.
  * Otherwise, you can select the Explore from the **Self-service Explores** section of the Looker **Explore** menu.



In addition, if you are a Looker admin, you can open any self-service Explore on the instance by using the links in the [**Data uploads**](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#viewing) table on the **Self-service Explores** admin page. For Looker admins, the **Self-service Explores** section of the Looker **Explore** menu doesn't list every self-service Explore on the instance, only those that you own or that the owner has specifically shared with you.

You can use a self-service Explore much in the same way as any other Looker Explore, including performing the following tasks: 

  * [Query your data](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) in the Explore.
  * [Filter and limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) your results to just the data you're interested in.
  * [Merge results from different Explores](https://docs.cloud.google.com/looker/docs/merged-results).
  * [Use table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to create ad hoc Explore metrics.
  * [Use custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) to create ad hoc dimensions and measures.
  * [Create visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations).
  * [Save Explore queries as Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks).
  * [Add Explore queries to dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore).
  * [Share data](https://docs.cloud.google.com/looker/docs/sharing-data) with other users.



In addition, you can prompt Looker to update the data if the information in your data file has changed since you initially uploaded it.

## Editing a self-service Explore

After you upload a data file, you can edit the Explore's data fields and manage user access from the **Edit Self-service Explore** page. 

There are two ways to access the **Edit Self-service Explore** page:

  * When you first upload a data file, Looker will automatically display the **Edit Self-service Explore** page for your data upload.
  * Otherwise, from the Looker **Explore** menu, select the Explore from the **Self-service Explores** section. In the Explore page, click the **Edit data fields** link from the bottom of the field picker panel in the Explore:

![The Edit data fields link on the Explore page.](https://docs.cloud.google.com/static/looker/docs/images/explore-self-service-edit-2520.png)




From the **Edit Self-service Explore** page, you can do the following:

  * Rename the Explore
  * Modify the data fields
  * Add dimensions and measures
  * Manage access to the self-service Explore
  * Open the self-service Explore
  * Remove the data upload from your instance



### Rename the Explore

To rename a self-service Explore, follow these steps:

  1. In the Explore page, click the **Edit data fields** link from the bottom of the field picker panel in the Explore.
  2. In the **Edit Self-service Explore** page, click the name of the data upload and then enter a new name.
  3. Press the **Enter** key to save the name.



The self-service Explore's new name will now be used as the title in the Explore window when you open the Explore, and in the **Self-service Explores** section of the Looker **Explore** menu (you may have to refresh your browser to see the updated name in the **Explore** menu).

### Modify data fields

On the **Edit Self-service Explore** page, the **Data Fields** tab lists the fields that Looker generated from your data file. 

You can't delete a generated field; you can only hide it, either by selecting **Hide** from the field's gear menu in the **Data Fields** table, or by clicking the field's **Edit** edit icon and selecting the **Hide this field from Explores and visualizations** checkbox.

The following sections describe how to edit dimensions and measures:

  * Edit a dimension
  * Edit a measure



#### Edit a dimension

To edit an existing dimension, follow these steps:

  1. From the **Edit Self-service Explore** page, in the **Data Fields** tab, click the **Edit** edit icon in the dimension's row of the **Data Fields** table to open the **Edit dimension** dialog.
  2. In the **Edit dimension** dialog, update any of the following fields (the **Data type** field is read-only): 
     * **Format** : Select a formatting option from the drop-down menu.
     * **Name** : Edit the name that's used to identify the dimension in LookML and expressions.
     * **Label** : Edit the label that appears in Explores and visualizations.
     * **\+ Add description** : Click this option to enter or edit an optional description for the dimension.
     * **Hide this field from Explores and visualizations** : Select or clear this checkbox to hide or display the dimension.
  3. Click **Save**.



#### Edit a measure

To edit an existing measure, follow these steps:

  1. From the **Edit Self-service Explore** page, in the **Data Fields** tab, click the **Edit** edit icon in the measure's row of the **Data Fields** table to open the **Edit measure** dialog.
  2. In the **Edit measure** dialog, update any of the following fields:

**Note:** For count measures, you can edit only **Label** , **Format** , **Description** , and **Hide this field from Explores and visualizations**.
     * **Field to measure** : Select the field that you want to aggregate from the drop-down menu.
     * **Measure type** : Select the aggregation type (such as **Sum** , **Count** , **Average** , **Min** , or **Max**) from the drop-down menu.
     * **Label** : Edit the label that appears in Explores and visualizations.
     * **Filters tab** : Under **Narrow results** , select a field from the **Filter name** drop-down menu and specify a **Filter value**. Use the **+** and **-** buttons to add or remove filter conditions.
     * **Field details tab** : Select a formatting option from the **Format** drop-down menu and enter an optional **Description** (up to 255 characters).
     * **Hide this field from Explores and visualizations** : Select or clear this checkbox to hide or display the measure.
  3. Click **Save**.




### Add dimensions and measures

You can build your own dimensions and measures for your self-service Explore. They are defined based on existing fields in the Explore or from [Looker expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions), and they remain available to all users of your self-service Explore.

The following sections describe how to create custom dimensions and measures:

  * Create a custom dimension
  * Create a custom measure



#### Create a custom dimension

To create a custom dimension by using a Looker expression, follow these steps:

  1. From the **Edit Self-service Explore** page, in the **Data Fields** tab, click the **Add Dimension** button to open the **Create dimension** dialog.
  2. In the expression editor box, enter a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) that defines the dimension, or click **Help me write an expression with Gemini** to generate an expression.
  3. Select a formatting option from the **Format** drop-down menu.
  4. Enter values for **Name** and **Label** for the dimension.
  5. Optionally, click **\+ Add description** to enter or edit a description for the dimension.
  6. Optionally, select the **Hide this field from Explores and visualizations** checkbox to hide the dimension.
  7. Click **Save**.



#### Create a custom measure

To create a custom measure, follow these steps:

  1. From the **Edit Self-service Explore** page, in the **Data Fields** tab, click the **Add Measure** button to open the **Create measure** dialog.
  2. Select the field that you want to aggregate from the **Field to measure** drop-down menu.
  3. In the **Measure type** drop-down, select the type of aggregation that you want to perform on the **Field to measure** field.
  4. Enter a **Label** for the measure.
  5. Configure optional filter conditions or formatting details: 
     * **Filters tab** : Under **Narrow results** , select a field from the **Filter name** drop-down menu and specify a **Filter value**. Use the **+** and **-** buttons to add or remove filter conditions.
     * **Field details tab** : Select a formatting option from the **Format** drop-down menu and enter an optional **Description** (up to 255 characters).
  6. Optionally, select the **Hide this field from Explores and visualizations** checkbox to hide the measure.
  7. Click **Save**.



On the **Edit Self-service Explore** page, your created fields appear under the generated fields in the **Data Fields** table.

### Updating the data for a self-service Explore

When you create a self-service Explore, Looker uploads the data from your file at the time of the upload. Subsequently, if the data in your file changes after you created the self-service Explore, you can update the data by following the steps in this section. 

Note the following for updating the data for a self-service Explore:

  * You can update data only for self-service Explores that you created.
  * If any of the fields have been changed since the self-service Explore was created, Looker will automatically resolve all backwards-compatible changes. 
  * If a field from the originally uploaded file is changed in a significant way, such as if the column is renamed or if the data type is changed, Looker will present a **Review changes** dialog that lists the differences. The **Review changes** dialog will list the old name or data type as "Removed," and the new name or data type as "Added." In the dialog you can apply the changes or cancel the data upload. If you confirm the changes, Looker will permanently delete the removed fields from your self-service Explore.



To update the data for a self-service Explore, follow these steps:

  1. From the **Edit Self-service Explore** page, click the **Update data** button.
  2. In the **Update data** dialog, depending on how you initially created the self-service Explore, do one of the following:

     * If you initially created the self-service Explore by uploading a file from your computer, click **Choose data** to navigate to the file on your computer.
     * If you initially created the self-service Explore by specifying a Google Sheets document, Looker uploads data from the same sheet of the same Google Sheets document.
  3. Click **Continue**. If you initially created the self-service Explore from a Google Sheets document and your Looker admin has configured [OAuth for Google Sheets uploads](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enabling_oauth_for_uploads), Looker prompts you to sign in with your Google Account and authorize access to your Google Sheets document.

  4. If Looker detects that any of the fields from the original file upload are significantly changed in the new file, Looker displays the **Review changes** dialog:

     * To keep the data from the initial file upload, click **Cancel** to cancel the data update.
     * Otherwise, to accept the updates, click **Confirm**. Looker permanently deletes the removed and renamed fields from your self-service Explore.



If your updated file had no significant changes, or if you confirmed the changes, Looker uploads the data from the specified file to your self-service Explore. When the model is ready, Looker displays the **Edit Self-service Explore** page.

### Managing access to the self-service Explore

You can share your self-service Explore with other Looker users and user groups by following these steps:

  1. From the **Edit Self-service Explore** page, click the **User Access** tab and then click the **Share access** button. (You can also click the three-dot menu at the top of the **Edit Self-service Explore** page and select **Share access**.)
  2. In the **Share access** dialog, click the **User or group** field and either select from the drop-down menu or begin typing a username or a group name to filter the menu. 
  3. In the **Access permission** field, leave the value as **View**.
  4. Optionally, click the **Add** button to provide access to another user or group.
  5. Click **Share**.



On the **Edit Self-service Explore** page, the **User Access** tab will show the new user or group to which you provided access. 

**Note:** If your Looker admin has enabled **Advanced connection governance** , you can only share a self-service Explore with users or groups that have the [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) permission on a model that uses the underlying database connection for that Explore. 

If you want to remove a user or group's access to your self-service Explore, you can click the **Delete user** button in the user or group's row of the **User Access** table.

### Certifying a self-service Explore

Self-service Explores are not based on a LookML model, and therefore their data is considered "ungoverned." When you upload data, the self-service Explore's name is displayed with a yellow "uncertified" badge ![](https://docs.cloud.google.com/static/looker/docs/images/uncertified-content-badge-2520.png) in the **Explore** menu and on the Explore page. This badge indicates that data is both uncertified and ungoverned. 

If you have the [`certify_content`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#certify_content) permission, you can add a certification to the Explore so that other users know the data is reliable. 

To add a certification to the self-service Explore, perform the following steps:

  1. From the Looker **Explore** menu, select the Explore from the **Self-service Explores** section.
  2. Click the Explore's gear menu and select **Certify**.
  3. In the **Certify this content?** dialog, enter your notes about the Explore, such as the origins of the data and how you know it's valid data.
  4. Click **Certify**.



When you certify a self-service Explore, Looker displays a certification badge ![](https://docs.cloud.google.com/static/looker/docs/images/certified-content-badge-2520.png) next to the Explore's name in the **Explore** menu and on the Explore page.

See the [Content certification](https://docs.cloud.google.com/looker/docs/content-certification) documentation page for more information.

### Removing a self-service Explore

You can delete your own data upload and its associated self-service Explore by performing the following steps:

  1. From the Looker main **Explore** menu, select the Explore from the **Self-service Explores** section.
  2. Click the **Edit data fields** link from the bottom of the field picker panel in the Explore.

![The Edit data fields link on the Explore page.](https://docs.cloud.google.com/static/looker/docs/images/explore-self-service-edit-2520.png)

  3. On the **Edit Self-service Explore** page, click the three-dot menu.

  4. Select **Remove data**.

  5. Click **Delete** in the confirmation dialog.




In addition, a Looker admin can delete any user's data upload from the **Self-service Explores** admin page by performing the following steps:

  1. From the Looker **Admin** menu, select **Self-service Explores**.
  2. In the **Data uploads** table on the **Self-service Explores** page, find the data upload and click the **Delete** button in its table row.
  3. Click **Delete** in the confirmation dialog.



## Things to consider

If your Looker instance is enabled with [Advanced connection governance](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#agc), note the following limitations:

  * When you create a self-service Explore, you can select from a drop-down list of allowed connections. Looker filters this list so that you see only the connections that are used by the models for which you have the [`upload_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#upload_data) permission. You cannot upload data to any other connection.
  * Continued access to a self-service Explore is dependent on your continued access to the underlying database connection. If your access to the connection is revoked, you will no longer be able to query, edit, or share any self-service Explores that use that connection.
  * You can share a self-service Explore only with users or groups that have the [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) permission on a model that uses the underlying database connection for that Explore.



## What's next

  * Learn more about [creating custom fields](https://docs.cloud.google.com/looker/docs/custom-fields).
  * Learn about [viewing and interacting with Explores in Looker](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
