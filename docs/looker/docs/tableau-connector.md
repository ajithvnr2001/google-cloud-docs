---
url: https://docs.cloud.google.com/looker/docs/tableau-connector/
title: Looker\u2013Tableau BI Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:21.051380+00:00
---

# Looker–Tableau BI Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/tableau-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker–Tableau BI Connector Stay organized with collections  Save and categorize content based on your preferences. 

The Looker–Tableau BI Connector lets you use a Looker Explore as a data source in Tableau Desktop, Tableau Cloud, and Tableau Server. The Looker–Tableau BI Connector is built upon the Looker [Open SQL Interface](https://docs.cloud.google.com/looker/docs/sql-interface), which allows access to LookML models and Explores for applications that use JDBC to connect to data sources.

See the following sections for information about connecting to Looker from these Tableau products:

  * Tableau Desktop
  * Tableau Cloud
  * Tableau Server



## Tableau Desktop

See the following sections for information about connecting to a Looker Explore from Tableau Desktop:

  * Before you begin
  * [Setting up Tableau Desktop to connect to Looker](https://docs.cloud.google.com/looker/docs/setting-up-tableau-desktop-to-connect-to)
  * Connecting to Looker data from Tableau Desktop



### Before you begin

Before you can use Tableau Desktop, you must have the following:

  * Tableau Desktop installed on your computer.
  * A Looker instance that is [set up by your Looker admin for Tableau Desktop](https://docs.cloud.google.com/looker/docs/tableau-admin#desktop).
  * A Looker account with a [user role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#roles) that includes the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission on the LookML model that you want to access from Tableau.
  * A LookML model that uses data from a Google BigQuery connection: 
    * The LookML project must include a model that is configured with at least one Google BigQuery connection in the **Allowed Connections** field. See the [Accessing and editing project information](https://docs.cloud.google.com/looker/docs/manage-projects#adding_and_editing_configurations) documentation page for information about configuring a model and seeing the allowed connections for the model.
    * The LookML project must have a [model file](https://docs.cloud.google.com/looker/docs/lookml-project-files#model_files) that specifies a BigQuery connection in its [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) parameter.



### Setting up Tableau Desktop to connect to Looker

To use Tableau Desktop to connect to Looker data, you must download the `avatica-<release_number>-looker.jar` JDBC driver file from GitHub to a specific directory on your computer by following these steps:

  1. Go to <https://github.com/looker-open-source/calcite-avatica/releases>.
  2. Download the latest version of the `avatica-<release_number>-looker.jar` file.
  3. Save the `avatica-<release_number>-looker.jar` file to each user's computer in the following location:

     * **Windows** : `C:\Program Files\Tableau\Drivers`
     * **MacOS** : `/Library/JDBC` or `~/Library/JDBC`

**Note:** For macOS, manually create the `JDBC` directory if it does not already exist.



### Connecting to Looker data from Tableau Desktop

After you've downloaded and saved the `avatica-<release_number>-looker.jar` file, you can use Tableau Desktop to connect to data from your Looker instance by following these steps:

  1. In Tableau Desktop, from the left-side **Connect** pane, in the **To a Server** section, select the **More...** option.
  2. In the search box, enter **Looker by Google**.
  3. Select the **Looker by Google** option.
  4. In the dialog window, enter these parameters:

     * **Server** : Enter your Looker instance URL without the `https://`. For example: `example.cloud.looker.com`
           
           LOOKER_INSTANCE_URL
           

     * **Port** : `443`

     * **Authentication** : `OAuth`

     * **OAuth Instance Url** : Enter your full Looker instance URL with the `https://`. For example: `https://example.cloud.looker.com`
           
           https://LOOKER_INSTANCE_URL
           

  5. Select **Sign In**. Tableau opens a browser window to connect to your Looker instance and authenticate your account with OAuth.

  6. If prompted, log in to Looker. If you're already logged in, you'll see a message in the browser window that Tableau used the browser window to authenticate with Looker and that you can now close the browser window.

  7. After you have authenticated in to Looker, Tableau opens a **Data Source** page with a connection to your Looker instance.

  8. Use the **Schema** drop-down menu to select a Looker [model](https://docs.cloud.google.com/looker/docs/lookml-project-files#model_files) with the data that you want to view in Tableau Desktop. Tableau populates the **Table** list with the Looker [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) from the Looker model that you selected.

  9. To start exploring the data, select and drag an object from the **Tables** list to the canvas.




See the following sections for more information about using Tableau to connect to Looker data:

  * Identifying Tableau queries in the Looker UI
  * Things to consider



## Tableau Cloud

See the following sections for information about connecting to a Looker Explore from Tableau Cloud:

  * Before you begin
  * Connecting to Looker data from Tableau Cloud



### Before you begin

Before you can use Tableau Cloud to connect to Looker, you must have the following:

  * A Tableau Cloud instance that is [configured by your Tableau admin to connect to Looker](https://docs.cloud.google.com/looker/docs/tableau-admin#cloud).
  * A Tableau Cloud user account with a [Tableau role](https://help.tableau.com/current/online/en-us/permission_license_siterole.htm) that lets you create a data source. If you don't have permission to create a data source, you can access only the Looker Explores that have already been added as data sources on your Tableau Cloud instance.
  * A Looker instance that is running Looker 25.18 or later and is [set up by your Looker admin for Tableau Cloud](https://docs.cloud.google.com/looker/docs/tableau-admin#cloud).
  * A Looker account with a [user role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#roles) that includes the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission on the LookML model that you want to access from Tableau.
  * A LookML model that uses data from a Google BigQuery connection: 
    * The LookML project must include a model that is configured with at least one Google BigQuery connection in the **Allowed Connections** field. See the [Accessing and editing project information](https://docs.cloud.google.com/looker/docs/manage-projects#adding_and_editing_configurations) documentation page for information about configuring a model and seeing the allowed connections for the model.
    * The LookML project must have a [model](https://docs.cloud.google.com/looker/docs/lookml-project-files#model_files) file that specifies a BigQuery connection in its [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) parameter.



### Connecting to Looker data from Tableau Cloud

After you have verified that the prerequisites are satisfied, you can use **Looker by Google** as a data source in Tableau Cloud by following these steps:

  1. Sign in to your Tableau Cloud site, then click the **New** drop-down menu and select **Workbook**.
  2. In the **Connect to Data** dialog, click the **Connectors** tab.
  3. In the **Connectors** tab, click **Looker by Google**.
  4. Select the **Looker by Google** option.
  5. In the dialog window, enter these parameters:

     * **Server** : Enter your Looker instance URL without the `https://`. For example: `example.cloud.looker.com`
           
           LOOKER_INSTANCE_URL
           

     * **Port** : `443`

     * **Authentication** : `OAuth`

     * **OAuth Instance Url** : Enter your full Looker instance URL with the `https://`. For example: `https://example.cloud.looker.com`
           
           https://LOOKER_INSTANCE_URL
           

  6. Select **Sign In**. Tableau opens a browser window to connect to your Looker instance and authenticate your account with OAuth.

  7. If prompted, log in to Looker. If you're already logged in, you'll see a message in the browser window that Tableau used the browser window to authenticate in to Looker and that you can now close the browser window.

  8. After you have authenticated in to Looker, Tableau opens a **Data Source** page with a connection to your Looker instance.

  9. Use the **Schema** drop-down menu to select a Looker [model](https://docs.cloud.google.com/looker/docs/lookml-project-files#model_files) with the data that you want to view in Tableau Desktop. Tableau populates the **Table** list with the Looker [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) from the Looker model that you selected.

  10. To start exploring the data, select and drag an object from the **Tables** list to the canvas.




See the following sections for more information about using Tableau to connect to Looker data:

  * Identifying Tableau queries in the Looker UI
  * Things to consider



## Tableau Server

The Looker–Tableau BI Connector is supported for Tableau Server. Before you can use the Looker–Tableau BI Connector with Tableau Server, you must have the following:

  * A Looker instance that is running Looker 24.14 or later and is configured for OAuth integration by your Looker admin.
  * A Tableau Server instance that is configured by your Tableau admin to connect to Looker.



See the [Administering Tableau to Looker connections](https://docs.cloud.google.com/looker/docs/tableau-admin#server) documentation page for details.

If your admin has set up your Looker instance and your Tableau Server, you can use Looker as a data source for Tableau Desktop and publish the workbook or data source to Tableau Server.

## Identifying Tableau queries in the Looker UI

Queries from Tableau are made through the Open SQL Interface. Looker admins can use the Looker UI to identify which queries originated from the Open SQL Interface, as described in the [Open SQL Interface](https://docs.cloud.google.com/looker/docs/sql-interface#identify_queries) documentation.

Queries from the Looker–Tableau BI Connector have a **Source** value of "sql_interface" or "SQL Interface".

## Things to consider

When you're exploring Looker data with Tableau, note the following considerations:

  * The Looker–Tableau BI Connector is built upon the Looker Open SQL Interface, and it has the same LookML limitations and SQL limitations as the Open SQL Interface. See the [Open SQL Interface](https://docs.cloud.google.com/looker/docs/sql-interface#lookml_limitations) documentation for more details.
  * Tableau automatically queries the database whenever a change is made to the query, including when fields are added and removed using the Looker–Tableau BI Connector. You can turn off automatic updates in Tableau: Refer to the [Tableau documentation](https://help.tableau.com/current/pro/desktop/en-us/queries_autoupdates.htm) for more information.
  * You cannot use Tableau to join two Looker Explores. If you want to join Explores, use Looker to create the joins in your Looker model. See the Looker documentation pages [Working with joins in LookML](https://docs.cloud.google.com/looker/docs/working-with-joins) and [join parameters](https://docs.cloud.google.com/looker/docs/reference/param-join) for information about using joins in Looker.
  * The Looker–Tableau BI Connector is designed to work with a [live connection](https://www.tableau.com/blog/tableau-cloud-tips-extracts-live-connections-cloud-data) in Tableau. Tableau's [data extract mode](https://help.tableau.com/current/pro/desktop/en-us/extracting_data.htm) extracts [Looker measures](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#dimension_and_measure_fields) with a value of "null" and therefore won't produce accurate results. If you want to use extract mode, you can create [aggregate fields](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_aggregate_create.htm) in Tableau directly off the Looker dimension fields instead of using Looker measures.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
