---
url: https://docs.cloud.google.com/code/docs/intellij/connect-sql-database/
title: Connect to a Cloud SQL database \u00a0|\u00a0 Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:37.704068+00:00
---

# Connect to a Cloud SQL database  |  Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/connect-sql-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Connect to a Cloud SQL database Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code supports running [Cloud SQL Auth proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) to connect to a [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) database, viewing Cloud SQL instances, and creating new data sources.

## Before you begin

  * Install [Cloud Code](https://docs.cloud.google.com/code/docs/intellij/install) if you haven't already.

  * To create a new data source, you can use one of the following premium JetBrains IDEs:

    * [IntelliJ Ultimate](https://www.jetbrains.com/idea/download) or another premium JetBrains IDE which contains the [Database Tools and SQL](https://www.jetbrains.com/help/idea/relational-databases.html) plugin (enabled by default).

    * [DataGrip](https://www.jetbrains.com/datagrip/), the standalone database management environment.

  * You can also use other preferred database tools (such as [DBeaver](https://dbeaver.com/download/), [MySQL Workbench](https://www.mysql.com/products/workbench/), and [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)) to connect to the Cloud SQL instances using the local port provided by Cloud Code.




## Connect to Cloud SQL database using Cloud SQL Auth proxy

You can connect to a Cloud SQL database and view a list of Cloud SQL instances in IntelliJ or other [supported JetBrains IDEs](https://docs.cloud.google.com/code/docs/intellij/ides) with Cloud Code.

**Note:** When performing these actions for the first time, Cloud Code installs Cloud SQL dependencies which include Cloud SQL Auth proxy.

To connect to a Cloud SQL database with Cloud Code, perform the following:

  1. In your IDE, click **Google Cloud Databases** in the sidebar or click **View** > **Tool Windows** > **Google Cloud Databases**.

  2. If a Google Cloud project isn't already selected, click **Select a Google Cloud project** and follow the prompts to load your Google Cloud project.

Cloud SQL instances in your Google Cloud project appear under **Cloud SQL**.

![Cloud SQL tools window](https://docs.cloud.google.com/static/code/docs/intellij/images/cloud-sql-view.png)

  3. To connect to a Cloud SQL instance, right-click an instance and select **Connect using Cloud SQL Proxy**. You can also choose to use a private IP by selecting **Connect using Cloud SQL Proxy (Private IP)**.




To learn more about connecting to SQL instances, see [About connection options](https://docs.cloud.google.com/sql/docs/mysql/connect-overview).

## Create a new data source

**Note:** Creating a new data source requires IntelliJ Ultimate or other premium JetBrains IDEs editions with the Database Tools and SQL plugin enabled, the DataGrip IDE, or other preferred database tools like [DBeaver](https://dbeaver.com/download/), [MySQL Workbench](https://www.mysql.com/products/workbench/), and [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)).

After a Cloud SQL Auth proxy connection is established, the **Cloud SQL Instance Connected** dialog appears, giving you the option to create a new data source for the locally available database or view existing data sources.

  1. To create a new data source, select **Create new data source**.

Alternatively, you can right-click an instance and select **Create New Data Source**.

![Data Sources and Drivers dialog](https://docs.cloud.google.com/static/code/docs/intellij/images/data-sources-and-drivers-dialog.png)

  2. In the **Authentication** field, select a method (by default, this is a username and password).

  3. Save the configuration.

Cloud Code creates a new data source connection with a name in the following format:

`gcp-project:location:db-instance-name`.

You can begin working with the database instance via JetBrains' Database Tools and SQL plugin capabilities, or DataGrip.

  4. (Optional) To view the list of data sources in your IDE, click **Database** in the Sidebar or **View** > **Tool Windows** > **Database**. Right-clicking a data source provides you with a list of options, such as viewing schemas, tables, and other database operations.

![Database tools options](https://docs.cloud.google.com/static/code/docs/intellij/images/database-tools-options.png)

To learn more about working with databases in DataGrip, see [Quick start with DataGrip](https://www.jetbrains.com/help/datagrip/quick-start-with-datagrip.html).




## Disconnect Cloud SQL Auth proxy

To stop the proxy process and free up the local database port, in the terminal, press `Ctrl+C`.

## Known issues

This section lists any known issues and their current resolutions.

### Set a different port to connect to several databases

The Cloud SQL Auth proxy doesn't auto-select ports if busy and always depends on one, which limits you to a single connected instance of a certain type of database.

Cloud Code runs Cloud SQL Auth proxy in the terminal, and if it runs into a port conflict, you can set a different port to connect to a database by running the same command in the terminal with a custom `--port` flag. For example:

`--port=PORT_NUMBER`

You can then use this port in your database connection. The command will be auto-generated. For example:

`path_to_proxy/cloud-sql-proxy INSTANCE_CONNECTION_STRING`

## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
