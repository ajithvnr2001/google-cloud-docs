---
url: https://docs.cloud.google.com/data-studio/connect-to-amazon-redshift/
title: Connect to Amazon Redshift \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:34.161167+00:00
---

# Connect to Amazon Redshift  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-amazon-redshift/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Amazon Redshift Stay organized with collections  Save and categorize content based on your preferences. 

The Amazon Redshift connector lets you create data sources based on Amazon Redshift. You can then visualize that data in your Data Studio reports and explorations.

## How to connect to Amazon Redshift

A Data Studio data source can connect to a single Amazon Redshift database table or to a custom query that you provide.

### To connect

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.

  3. Select the **Amazon Redshift** connector.

  4. Set up the connection to your database: 

####  Connect with a hostname or IP address 

     1. On the left, select **BASIC**. 
     2. Enter the connection details: 
        1. Hostname or IP address 
        2. Port (Optional) 
        3. Database 
        4. Username 
        5. Password 

####  Connect with a JDBC URL 

     1. On the left, select **JDBC URL**. 
     2. Enter the connection details: 
        1. JDBC URL 

**Example** ` jdbc:redshift://hostname or IP address[:port]/database `

        2. Username
        3. Password

**Note:** Data Studio can't connect to `localhost`. You must use a public hostname or IP address.
  5. Enable SSL: Data Studio supports secure (encrypted) connections to the server using the TLS (Transport Layer Security) protocol (TLS 1.2). TLS is also referred to as SSL (Secure Sockets Layer). To enable a secure connection, select **Enable SSL** , then provide your SSL configuration files.

**Note:** This setting is not required by Data Studio but may be required for your database configuration. Check with your database vendor for details.

Learn more about [Amazon Redshift secure connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html).

  6. Click **AUTHENTICATE.**

  7. Select a table from the list or enter a custom query. 




Select the **CUSTOM QUERY** option to provide a SQL query instead of connecting to a single table. Data Studio uses this custom SQL as an inner select statement for each generated query to the database.

Custom SQL queries may only have a single statement. For example, the following will **not** work because it has multiple SQL statements:
    
    
    DECLARE cost_per_tb_in_dollar FLOAT64 DEFAULT 4.2;
    
    SELECT total_bytes_billed / (1024 * 1024))* cost_per_tb_in_dollar)/(1024*1024))) FROM billing-table;
    
    

Queries in Data Studio may time out after three to five minutes. If your custom queries time out, try the following approaches to resolve the issue:

  * Simplify the query so that it runs faster.
  * Run the query in your database and store the results in a separate table. Connect the new table in your data source.



Finally, click **CONNECT**. In a moment, the data source fields list page appears. Click **CREATE REPORT** to start visualizing your data.

## Notes

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




## Limits of the Amazon Redshift connector

  * You can query a maximum of 150 K rows per query using this connector. If you exceed this limit, the data will be truncated.
  * Column headers (field names) must use ASCII characters only. Non-ASCII characters aren't supported.



## License

The Amazon Redshift connector was developed using the Amazon Redshift JDBC driver, which is distributed under the [Apache 2.0 license](https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/LICENSE).

## Troubleshooting

See the [Data Studio troubleshooting guide](https://docs.cloud.google.com/data-studio/troubleshooting-guide) for a list of common error messages and steps to resolve them.

## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
