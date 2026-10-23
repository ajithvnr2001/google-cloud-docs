---
url: https://docs.cloud.google.com/looker/docs/excel-connector/
title: Looker-Excel Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:33.366040+00:00
---

# Looker-Excel Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/excel-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker-Excel Connector Stay organized with collections  Save and categorize content based on your preferences. 

The Looker-Excel Connector lets you export queries from a Looker Explore to a format that Microsoft Excel recognizes. When the Looker-Excel Connector is enabled, Looker Explores display the **Open in Excel** option in the Explore gear menu. When you select this option, Looker exports the Explore query to an ODC file on your Windows PC. If you have the ODBC driver installed, you can open the ODC file in Microsoft Excel for Windows.

## Before you begin

To use the Looker-Excel Connector, you must have the following:

  * A Windows 64-bit or 32-bit PC.
  * A Looker instance that meets the following requirements: 
    * Running Looker 25.16 or later.
    * Enabled for the **Microsoft Excel** BI connector. A Looker admin must enable the **Microsoft Excel** toggle on the Looker [**BI Connectors**](https://docs.cloud.google.com/looker/docs/bi-connectors) page.
  * A Looker account with a [user role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#roles) that includes the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission on the LookML model that the user wants to access with Looker-Excel Connector.



You must also install the ODBC driver, as described in the following section.

### Installing the ODBC driver

The Looker ODBC driver is a piece of software that must be installed on the local machine of each user of the Looker-Excel Connector. The ODBC driver allows ODBC compatible clients to connect to your Looker instance as if the instance were a SQL database.

To use an ODBC driver, you need to have an ODBC manager program installed. Windows typically comes pre-installed with a program called **ODBC Data Sources** as the management tool. For more information, see the [Microsoft documentation on the ODBC Data Source Administrator](https://learn.microsoft.com/en-us/sql/odbc/admin/odbc-data-source-administrator).

To install the ODBC driver, follow these steps:

  1. Use the following links to download the latest ODBC installer for your Windows system's architecture (64-bit or 32-bit):

     * [64-bit](https://dl.google.com/looker-odbc-driver/windows/64bit/looker-odbc-installer-x64-1.0.6.exe)
     * [32-bit](https://dl.google.com/looker-odbc-driver/windows/32bit/looker-odbc-installer-x86-1.0.6.exe)
  2. Open the ODBC installer file and follow the on-screen instructions.

  3. You may see a Windows dialog that says **Windows protected your PC**. If you see this dialog, click the **More info** link and then click the **Run anyway** button.




The first time you open an ODC file after installing the ODBC driver on your Windows PC, Windows prompts you to create a [Data Source Name (DSN)](https://support.microsoft.com/en-us/topic/what-is-a-dsn-data-source-name-ae9a0c76-22fc-8a30-606e-2436fe26e89f) to enable you to use the ODBC driver with ODBC clients such as Excel. The DSN is a saved configuration that contains your Looker instance information and authentication credentials.

## Using the Looker-Excel Connector

Once the prerequisites are met and the ODBC driver is installed on your computer, you can open Looker data in Microsoft Excel by following these steps:

  1. On your Windows PC, open your Looker instance in a browser.
  2. [Open an Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#explores_are_the_starting_point_for_exploration) and run a query.
  3. Click the Explore gear menu and select the **Open in Excel** option. 
  4. In the **Open in Excel** dialog, select one of the following options for **Number of rows and columns to include** :

     * **Current result table** : Select this option to include all the rows and columns that are in the current result table in the Explore. The number of rows is limited by the **Row Limit** value of the Explore.
     * **All results** : Select this option to include all the results that are returned by the query to your database. The **All results** option is typically disabled for queries that have [Row Totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) enabled, or that retrieve data from a database dialect that [cannot stream results](https://docs.cloud.google.com/looker/docs/downloading#streaming_query_results) [percent of total](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_total), or that contain the following types of measures: [percent of previous](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_previous) or [running totals](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#running_total). Warning: Even when the **All results** option is available, you should still use caution when downloading all results. Some queries are very large, containing thousands or millions of rows, which can overwhelm most spreadsheet programs — or even your Looker instance.
     * **Custom** : Select this option to manually specify the number of rows and columns to include in the ODC file download. 
     * Users who have [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permission can enter a row size up to 100,000 and column size up to 200.
     * Users who have [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) permission can enter a row size up to 5,000 rows and column size up to 200.
     * For users with neither `download_with_limit` or `download_without_limit` permission, the **Open In Excel** option will not be displayed.
  5. In the **Open in Excel** dialog, click **Download**. An ODC file will be downloaded to your computer.

  6. Open the ODC file with Microsoft Excel.

  7. Microsoft Excel presents a security notice about blocked data connections. Click **Enable** to enable the data connection.

  8. Windows presents a dialog for configuring the Google Looker DSN. Configure the DSN by performing the following steps:

     1. In the **Auth Type** drop-down menu, select **OAuth**. Although OAuth is the preferred option, you can instead select **Basic Auth** if required. If you select **Basic Auth** , you will need to input the Looker API credentials. See the Authenticating using basic auth section on this page.
     2. Click **Login**. This will open a web browser that authenticates into your Looker account. After the web browser shows a successful login, close the web browser and go back to the DSN dialog.
     3. Click **OK** in the **DSN** dialog.
     4. If prompted, click **OK** to agree to overwrite the DSN.



Excel runs the query and inserts the data into a new pivot table object. From here, you can use the data in calculations and visualizations. 

If you want to retrieve fresh data, you can do one of the following:

  * To re-run the same query to get the latest data from Looker, click the **Refresh** button in the Excel ribbon.
  * To modify the query, use the Looker Explore UI to update the query and then select the **Open in Explore** Explore option to download a new ODC file (in other words, start over from step 1 of this procedure). By default, Excel will open a new ODC file in a new Excel workbook. If you want to move a pivot table from one workbook to another, you can click-and-drag the sheet between Excel workbooks, or you can copy and paste the pivot table from work workbook to another.



## Limitations

The Looker-Excel Connector is supported only on Windows, not on Mac or Linux computers.

The following Explore query features aren't supported with the Looker-Excel Connector:

  * [Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations)
  * [Pivoted columns](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions)



If you want to open an Explore query in Microsoft Excel, remove the table calculations and pivoted columns before selecting **Open in Excel** from the Explore gear menu.

## Troubleshooting

The following sections provide information on troubleshooting procedures and tools:

  * Manually adding a DSN
  * Installer logs
  * Upgrading the Microsoft Visual C++ Redistributable (MSVC)



### Manually adding a DSN

When you open an ODC file with Excel, Windows will prompt you to create the DSN. If you need to manually create or edit the DSN, you can use the Windows ODBC Driver Data Source Administrator.

**Note:** When using some high resolution display settings, there can be visual issues in the scaling of the data source configuration window inside Excel. If the data source configuration window inside Excel is not sized correctly on your display, you can instead configure the DSN by using the Windows ODBC Data Sources application that is built into Windows, or you can increase the scale factor on your monitor, which will help scale the configuration window inside Excel.

To manually create or edit the DSN, follow these steps:

  1. From the control panel of your Windows PC, open the **ODBC Data Sources** application (before Windows 8, this application was called **ODBC Driver Data Source Administrator**).
  2. Click the **Add** button.
  3. Double-click on **Google Looker ODBC Driver**.
  4. In the **Configure Google Looker DSN** dialog, fill in the following fields: 
     * **Data Source Name ***: (Optional) Enter a name for your data source to help you recognize this DSN in the future.
     * **Host** : Enter the URL for your Looker instance.
     * **Port** : Enter the port to connect to on the Looker instance. The default is **443**.
     * In the **Auth Type** drop-down menu, select **OAuth**. Although OAuth is the preferred option, you can instead select **Basic Auth** if required. If you select **Basic Auth** , you will need to input the Looker API credentials. See the Authenticating using basic auth section on this page.
  5. Click **Login**. This will open a web browser that authenticates into your Looker account. After the web browser shows a successful login, close the web browser and go back to the DSN dialog.
  6. Click **Test** to verify the connection.
  7. Click **OK** in the **DSN** dialog.
  8. If prompted, click **OK** to agree to overwrite the DSN.



#### Authenticating using basic auth

OAuth is the preferred way to authenticate to Looker. Alternatively, if you select **Basic Auth** as the **Auth Type** in the DSN dialog, you can authenticate using the API key **Client ID** and **Client Secret**. See the [Admin settings - Users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) documentation page for information about creating API keys.

**Warning:** The client ID and client secret are stored in plain text, so this method is appropriate only for non-sensitive environments, such as testing.

### Installer logs

If you need to access the installer logs to troubleshoot the Looker-Excel Connector, you can access them in the directory `C:\Users\<username>\lookerODBCLogs`. The installer log names use the following format:
    
    
      Google_Looker_ODBC_<32/64>-bit_Driver_<timestamp>
    

### Upgrading the Microsoft Visual C++ Redistributable (MSVC)

The Microsoft Visual C++ Redistributable (MSVC) Package version 14 is installed automatically if it's not already present.

If the MSVC Package is already installed, the Google Looker ODBC driver installer _won't_ upgrade it. To use the MSVC version that is included with the driver, uninstall the existing MSVC package before running the installer.

After you uninstall the driver, the MSVC package remains installed to support other applications. You can manually uninstall it if you no longer need it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
