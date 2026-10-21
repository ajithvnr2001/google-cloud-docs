---
url: https://docs.cloud.google.com/data-studio/connect-to-postgresql/
title: Connect to PostgreSQL \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:43:42.780270+00:00
---

# Connect to PostgreSQL  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-postgresql/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

You can connect your PostgreSQL databases to Data Studio to visualize and analyze your data. Use the PostgreSQL connector to transform your data into interactive dashboards and reports. You can then share your insights with your team or stakeholders who don't have direct database access.

### Supported versions

We've tested Data Studio on the following PostgreSQL versions:

  * 9.6
  * 10
  * 11
  * 12
  * 13
  * 14



If you experience issues with using a supported version, let us know in the [Data Studio Community](https://discuss.google.dev/c/data-studio/246). You can also add and vote on feature requests [on the issue tracker](https://issuetracker.google.com/issues?q=status:open%20componentid:196095).

## How to connect to PostgreSQL

The PostgreSQL connector uses the PostgreSQL JDBC driver to connect a Data Studio data source to a single PostgreSQL database table, or to a custom query that you provide.

To connect to your PostgreSQL database, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, click add **Create** , and then select **Data Source**.
  3. Select the **PostgreSQL** connector.
  4. If asked, authorize Data Studio to access your data.
  5. Configure access to your database by using one of the connection options.
  6. Click **AUTHENTICATE**. You see a list of tables in that database.
  7. Select a table from the list or enter a custom query.
  8. Click **CONNECT**.



You can now access all the columns in the table as fields in your reports.

### Connection options

#### Connect by using a hostname or IP address

In the connection panel, select **BASIC**. Enter the connection details:

  * Hostname or IP address
  * Port (Optional)
  * Database
  * Username
  * Password



#### Connect by using a JDBC URL

In the connection panel, select **JDBC URL**. Enter the connection details:

  * JDBC URL 
    * **Example** `jdbc:postgresql://HOSTNAME[:PORT]/DATABASE`

    * **For Cloud SQL (Private IP)** `jdbc:google:postgresql://INSTANCE_CONNECTION_NAME/DATABASE`

  * Username
  * Password

**Tip:** If you use the JDBC hostname option, you can make sure it's accessible with public DNS lookup tools such as [Whois](https://www.whois.com.au/whois/dns.html).

To connect by using an IPv6 literal address, enclose the address in square brackets. For example: `jdbc:postgresql://[2001:db8:1:1:1:1:1:1]/your_db`

#### Connect by using SSL

Data Studio supports secure (encrypted) connections to the server using the TLS (Transport Layer Security) protocol (TLS 1.2). TLS is also referred to as SSL (Secure Sockets Layer).

To enable a secure connection, select **Enable SSL** and then provide your SSL configuration files.

#### Connect by using client authentication

When the **Enable client authentication** box is checked, you can upload a client private key and a client certificate if required to access your database.

**Note:** Data Studio expects a [PKCS-8 client key format](https://jdbc.postgresql.org/documentation/ssl/).

Learn more about [PostgreSQL secure connections](https://www.postgresql.org/docs/9.3/static/ssl-tcp.html).

### Custom query

Select the **CUSTOM QUERY** option to provide a SQL query instead of connecting to a single table. Data Studio uses this custom SQL as an inner select statement for each generated query to the database.

Custom SQL queries may only have a single statement. For example, the following will **not** work because it has multiple SQL statements:
    
    
    DECLARE cost_per_tb_in_dollar FLOAT64 DEFAULT 4.2;
    
    SELECT total_bytes_billed / (1024 * 1024))* cost_per_tb_in_dollar)/(1024*1024))) FROM billing-table;
    
    

Queries in Data Studio may time out after three to five minutes. If your custom queries time out, try the following approaches to resolve the issue:

  * Simplify the query so that it runs faster.
  * Run the query in your database and store the results in a separate table. Connect the new table in your data source.



## Supported data types

The PostgreSQL connector supports the following data types:

  * Numeric
  * Character
  * Boolean
  * Date/Time (except Intervals)



When Data Studio encounters a column of a non-supported type, it won't create a field for that column.

Learn more about [PostgreSQL data types](https://www.postgresql.org/docs/9.6/static/datatype.html).

## Public and private connections

Data Studio supports both public and private IP connections to PostgreSQL on Cloud SQL.

To connect using a private IP, you must use the **JDBC URL** connection option with the format `jdbc:google:postgresql://INSTANCE_CONNECTION_NAME/DATABASE`. Additionally, you must select the **Private path for Google Cloud services** option in your Cloud SQL instance settings.

## Firewall and database access

To allow Data Studio to connect to and query databases that are behind a firewall, you will need to open access to one of the following IP addresses. You may also need to configure your database to accept traffic from these addresses. Consult the documentation for your specific database for instructions on how to do this.

### IP addresses

The following addresses are reserved for Data Studio's global infrastructure:

  * `142.251.74.0/23`

  * `2001:4860:4807::/48` (Optional, for platforms that support IPv6)




If you have [enabled data residency](https://docs.cloud.google.com/data-studio/data-residency) for your Data Studio Pro subscription, use the following addresses instead:

  * `142.251.56.0/24`

  * `2001:4860:4815::/48` (Optional, for platforms that support IPv6)




## Limits of the PostgreSQL connector

  * The PostgreSQL connector doesn't use the Cloud SQL proxy when connecting to Cloud SQL PostgreSQL instances. If you're connecting to a Cloud SQL PostgreSQL instance using a public IP, you'll need to add the listed IPs to the authorized networks list. See the [Cloud SQL documentation](https://docs.cloud.google.com/sql/docs/postgres/configure-ip#add).

  * Connecting to AlloyDB data sources over SSL isn't supported, since AlloyDB doesn't support exporting Certificate Authority (CA) certificates.

  * Selecting a table outside of the `public` schema isn't supported. However, you can select the **CUSTOM QUERY** option to write a query that includes tables in any schema.

  * You can query a maximum of 150 K rows per query using this connector. If you exceed this limit, the data will be truncated.

  * Column headers (field names) must use ASCII characters only. Non-ASCII characters aren't supported.




## Troubleshooting

See the [Data Studio troubleshooting guide](https://docs.cloud.google.com/data-studio/troubleshooting-guide) for a list of common error messages and steps to resolve them.

## Related resources

[Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
