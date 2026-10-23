---
url: https://docs.cloud.google.com/data-studio/connect-to-google-cloud-sql-for-mysql/
title: Connect to Google Cloud SQL for MySQL \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:00.133631+00:00
---

# Connect to Google Cloud SQL for MySQL  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-cloud-sql-for-mysql/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Google Cloud SQL for MySQL Stay organized with collections  Save and categorize content based on your preferences. 

You can connect your Cloud SQL for MySQL databases to Data Studio by using the Cloud SQL for MySQL connector. Use your database tables or custom queries to build interactive reports and dashboards. You can then share these insights with stakeholders or team members who don't have direct database access.

## Supported versions

The Cloud SQL for MySQL connector was tested on the following MySQL versions:

  * 5.6
  * 5.7
  * 8.0



If you experience issues with using a supported version, let us know in the [Data Studio Community](https://discuss.google.dev/c/data-studio/246). You can also add and vote on feature requests [on the issue tracker](https://issuetracker.google.com/issues?q=status:open%20componentid:196095).

## How to connect to Cloud SQL for MySQL

A Data Studio data source can connect to a single Cloud SQL for MySQL database table, or to a custom query that you provide.

To connect to your Cloud SQL for MySQL database, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, click add **Create** , and then select **Data Source**.
  3. Select the **Cloud SQL for MySQL** connector.
  4. Configure access to your database by using one of the connection options.
  5. Click **AUTHENTICATE**. You'll see a list of tables in that database.
  6. Select a table from the list or enter a custom query.
  7. Click **CONNECT**.



You can now access all the columns in the table as fields in your reports.

### Connection options

**Note:** Data Studio can't connect to `localhost`. You must use a public hostname or IP address.

#### Connect by using a hostname or IP address

In the connection panel, select **BASIC**. Enter the connection details:

  * Instance Connection Name
  * Database
  * Username
  * Password



#### Connect by using a JDBC URL

In the connection panel, select **JDBC URL**. Enter the connection details:

  * JDBC URL 
    * **Example** `jdbc:google:mysql://INSTANCE_CONNECTION_NAME/DATABASE`

  * Username
  * Password

**Tip:** If you use the JDBC hostname option, you can make sure it's accessible with public DNS lookup tools such as [Whois](https://www.whois.com.au/whois/dns.html).

To connect by using an IPv6 literal address, enclose the address in square brackets. For example: `jdbc:google:mysql://[2001:db8:1:1:1:1:1:1]/your_db`

### Custom query

Select the **CUSTOM QUERY** option to provide a SQL query instead of connecting to a single table. Data Studio uses this custom SQL as an inner select statement for each generated query to the database.

Custom SQL queries may only have a single statement. For example, the following will **not** work because it has multiple SQL statements:
    
    
    DECLARE cost_per_tb_in_dollar FLOAT64 DEFAULT 4.2;
    
    SELECT total_bytes_billed / (1024 * 1024))* cost_per_tb_in_dollar)/(1024*1024))) FROM billing-table;
    
    

Queries in Data Studio may time out after three to five minutes. If your custom queries time out, try the following approaches to resolve the issue:

  * Simplify the query so that it runs faster.
  * Run the query in your database and store the results in a separate table. Connect the new table in your data source.



## Notes

Review the following sections for details on finding your instance connection name, configuring required permissions, and setting up network connectivity.

### Find your instance connection name

The instance connection name identifies your instance on Google Cloud. You can get it from the Google Cloud console, or by using the command line.

#### Use the console

  1. Navigate to https://console.cloud.google.com/sql/instances.
  2. Click the Instance ID you want to connect to.
  3. On the left, you'll find connection Name in the "Connect to this instance" section.



#### Use the command line

To find the connection name using the Cloud command line interface, use the following command:
    
    
    gcloud sql instances describe [INSTANCE_NAME] | grep connectionName
    

### Permissions

You must have at least `cloudsql.client` permission in the Cloud SQL for MySQL project to create the connection. If you don't have (or can't get) this access, you can use the [MySQL connector](https://docs.cloud.google.com/data-studio/connect-to-mysql) instead.

### Network connectivity

The Cloud SQL for MySQL connector supports connections to Cloud SQL for MySQL instances with public IP connectivity and private IP connectivity.

You must configure [public IP connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) or [private IP connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip) for your Cloud SQL for MySQL instance before using the Cloud SQL for MySQL connector.

To allow Data Studio to access data in Cloud SQL and make queries against this data over a private connection, select the [**Private path for Google Cloud services**](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#private-path) option in your Cloud SQL for MySQL instance settings.

## Supported data types

Data Studio maps your database's built-in data types to a unified set of [data types](https://docs.cloud.google.com/data-studio/data-types). If Data Studio encounters a column in your table or query of an unsupported type, it won't create a field for that column. 

## Firewall and database access

To allow Data Studio to connect to and query databases that are behind a firewall, you will need to open access to one of the following IP addresses. You may also need to configure your database to accept traffic from these addresses. Consult the documentation for your specific database for instructions on how to do this.

### IP addresses

The following addresses are reserved for Data Studio's global infrastructure:

  * `142.251.74.0/23`

  * `2001:4860:4807::/48` (Optional, for platforms that support IPv6)




If you have [enabled data residency](https://docs.cloud.google.com/data-studio/data-residency) for your Data Studio Pro subscription, use the following addresses instead:

  * `142.251.56.0/24`

  * `2001:4860:4815::/48` (Optional, for platforms that support IPv6)




## Limits of the Cloud SQL for MySQL connector

  * Data Studio does not support MySQL Spatial Data Extensions.
  * You can query a maximum of 150 K rows per query using this connector. If you exceed this limit, the data will be truncated.
  * Column headers (field names) must use ASCII characters only. Non-ASCII characters aren't supported.



## Troubleshooting

See the [Data Studio troubleshooting guide](https://docs.cloud.google.com/data-studio/troubleshooting-guide) for a list of common error messages and steps to resolve them.

## Related resources

  * [Add data to a report](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Cloud SQL for MySQL developer documentation](https://docs.cloud.google.com/sql/docs/external)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
