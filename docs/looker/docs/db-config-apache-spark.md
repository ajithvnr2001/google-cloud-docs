---
url: https://docs.cloud.google.com/looker/docs/db-config-apache-spark/
title: Apache Spark \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:36.787940+00:00
---

# Apache Spark  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-apache-spark/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

This page contains information about connecting Looker to Apache Spark 3.

Looker connects to Apache Spark 3+ through a JDBC connection to the Spark Thrift Server.

**Note:** Looker does not support connections to Apache Spark 1.5 or Apache Spark 2. Queries on connections to Apache Spark 1.5 or Apache Spark 2 will return an error.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : The name of the connection. This is how the connection will be referred to in the LookML model.
  * **Dialect** : Select **Apache Spark 3+**.
  * **Host** : The Thrift server host.
  * **Port** The Thrift server port (10000 by default).
  * **Database** : The default schema or database that will be modeled. When no database is specified for a table, this will be assumed.
  * **Username** : The user that Looker will authenticate as.
  * **Password** : The optional password for Looker user.
  * **Enable PDTs** : Use this toggle to enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). When PDTs are enabled, the **Connection** window reveals additional PDT settings and the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt-overrides) section.
  * **Temp Database** : A temporary schema or database for storing PDTs. It must be created beforehand, with a statement such as `CREATE SCHEMA looker_scratch;`.
  * **Additional JDBC parameters** : Add any additional JDBC parameters. See the Supported JDBC parameters section on this page for a list of supported parameters.
  * **SSL** : Leave this unchecked.
  * **Database Time Zone** : The time zone of data stored in Spark. Usually it can be left blank or set to UTC.
  * **Query Time Zone** : The time zone to display data queried in Looker.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Apache Spark, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `batchsize`
  * `cascadeTruncate`
  * `connectionProvider`
  * `createTableColumnTypes`
  * `createTableOptions`
  * `customSchema`
  * `dbtable`
  * `fetchsize`
  * `isolationLevel`
  * `keytab`
  * `lowerBound`
  * `numPartitions`
  * `oracle.jdbc.mapDateToTimestamp`
  * `partitionColumn`
  * `password`
  * `preferTimestampNTZ`
  * `prepareQuery`
  * `principal`
  * `pushDownAggregate`
  * `pushDownLimit`
  * `pushDownOffset`
  * `pushDownPredicate`
  * `pushDownTableSample`
  * `query`
  * `queryTimeout`
  * `sessionInitStatement`
  * `truncate`
  * `upperBound`
  * `url`
  * `user`



## Feature support

For Looker to support some features, your database dialect must also support them.

### Apache Spark 3+

Apache Spark 3+ supports the following features as of Looker 26.20:

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
  
## Next steps

After you have created the connection, [set authentication options](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
