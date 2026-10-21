---
url: https://docs.cloud.google.com/looker/docs/db-config-amazon-athena/
title: Amazon Athena \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:12.260682+00:00
---

# Amazon Athena  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-amazon-athena/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Amazon Athena Stay organized with collections  Save and categorize content based on your preferences. 

Looker supports connections to [Amazon Athena](https://aws.amazon.com/athena/), an interactive query service that lets you analyze data in Amazon S3 using standard SQL. Amazon Athena is serverless, so there is no infrastructure to manage. You are charged only for the queries that are run.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Configuring an Amazon Athena connection

This page describes how to connect Looker to an Amazon Athena instance.

  1. Ensure that you have the following:

     * A pair of Amazon AWS access keys.
     * The S3 bucket containing the data you want to query in Looker with Amazon Athena. The Amazon AWS access keys must have read-write access to this bucket.

> Amazon Athena must have access to this S3 bucket by either a role or a permission set, as well as by firewall rules. Don't add security rules to the S3 bucket for the Looker IP, since this can inadvertently block Amazon Athena's access to the S3 bucket. (For other dialects besides Amazon Athena, users may want to limit access to the data from the network layer with an IP allowlist, as described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.)

     * Knowledge of where your Amazon Athena instance data is located. The region name can be found in the upper right-hand portion of the Amazon Console.

  2. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

  3. Fill out the connection details:

**Note:** The [Simba Athena JDBC Driver with SQL Connector Installation and Configuration Guide](https://s3.amazonaws.com/athena-downloads/drivers/JDBC/SimbaAthenaJDBC_2.0.2/docs/Simba+Athena+JDBC+Driver+Install+and+Configuration+Guide.pdf) provides more details about custom JDBC configurations and other configuration information.
     * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
     * **Dialect** : Select **Amazon Athena**.
     * **Host** and **Port** : Specify the name of the host and port as described in the [Athena documentation on the JDBC URL format](http://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html#jdbc-url-format). The host should be a valid Amazon endpoint (like `athena.eu-west-1.amazonaws.com`), and the port should stay at `443`. An up-to-date list of endpoints that support Athena can be found on this [AWS General Reference](http://docs.aws.amazon.com/general/latest/gr/rande.html#athena) page.
     * **Database** : Specify the default database that you would like modeled. Other databases can be accessed, but Looker treats this database as the default database.
     * **Username** : Specify the AWS access key ID.
     * **Password** : Specify the AWS secret access key.
     * **Enable PDTs** : Use this toggle to enable [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). Enabling PDTs reveals additional PDT fields and the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt-overrides) section for the connection.
     * **Temp Database**: Specify the name of the output directory in your S3 bucket where you want Looker to write your PDTs. The full path to your output directory must be specified in the **Additional JDBC parameters** field; see the Specifying your S3 bucket for query results output and PDTs section on this page.
     * **Max number of PDT builder connections** : Specify the number of possible concurrent PDT builds on this connection. Setting this value too high could negatively impact query times. For more information, see the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_pdt_builder_connections) documentation page.
     * **Additional JDBC parameters**: Specify additional parameters for the connection: 
       * The `s3_staging_dir` parameter is the S3 bucket that Looker should use for query results output and PDTs; see the Specifying your S3 bucket for query results output and PDTs section on this page.
       * Flag for streaming results. If you have the [`athena:GetQueryResultsStream` policy](https://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html#migration-from-previous-jdbc-driver) attached to your Athena user, you can add `;UseResultsetStreaming=1` to the end of your additional JDBC parameters to significantly improve the performance of large result set extraction. This parameter is set to `0` by default.
       * Optional additional parameters to add to the JDBC connection string. See the Supported JDBC parameters section on this page for the list of parameters that Looker supports.
     * **SSL** : Ignore; by default, all connections to the AWS API will be encrypted.
     * **Max connections per node** : By default, this is set to 5. You can increase this up to 20 if Looker is the main query engine running against Athena. See [the Athena service limits documentation](http://docs.aws.amazon.com/athena/latest/ug/service-limits.html) for more details about the service limits. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.
     * **Connection Pool Timeout** : Specify the connection pool timeout. By default, the timeout is set to 120 seconds. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#connection_pool_timeout) documentation page for more information.
     * **SQL Runner Precache** : Unselect this option if you prefer SQL Runner to load table information only when a table is selected. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#sql_runner_precache) documentation page for more information.
     * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you don't want time zone conversion. See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Specifying your S3 bucket for query results output and PDTs

Use the **Additional JDBC parameters** field of the **Connections** page to configure the path to the S3 bucket that Looker will use for storing query results output, and to specify the name of the output directory in the S3 bucket where you want Looker to write PDTs. Specify this information using the `s3_staging_dir` parameter.

The `s3_staging_dir` JDBC parameter is an alternative way to configure the Amazon Athena `S3OutputLocation` property, which is required for Athena JDBC connections. See [the Athena documentation on JDBC Driver Options](http://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html#jdbc-options) for more information and a list of all available JDBC driver options.

In the **Additional JDBC parameters** field, specify the `s3_staging_dir` parameter using the following format:
    
    
    `s3_staging_dir=s3://<s3-bucket>/<output-path>`
    

Where:

  * `<s3-bucket>` is the name of the S3 bucket.
  * `<output-path>` is the path where Looker will write query results output.



> The AWS access key pair must have write permissions to the `<s3-bucket>` directory.

To configure the directory where Looker will write PDTs, enter the _path of the directory in the S3 bucket_ in the **Temp Database** field. For example, if you want Looker to write PDTs into `s3://<s3-bucket>/looker_scratch`, then enter this in the **Temp Database** field:
    
    
    `looker_scratch`
    

Only enter the _path of the directory_. Looker gets the S3 bucket name from the `s3_staging_dir` parameter that you enter in the **Additional JDBC Parameters** field.

### S3 bucket considerations

It is recommended that you configure [Amazon S3 object lifecycles](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-config-overview-what) to periodically clean out unneeded files in your specified S3 bucket. There are reasons for this:

  * Athena stores query results for every query in an S3 bucket. See [Athena Querying](https://docs.aws.amazon.com/athena/latest/ug/querying.html#querying-identifying-output-files).
  * If you have PDTs enabled, when a PDT is built, metadata about the created table is stored in the S3 bucket.



## Resources

  * [Amazon Athena documentation](http://docs.aws.amazon.com/athena/latest/ug/what-is.html)
  * [Amazon Web Services Console for Athena](https://console.aws.amazon.com/athena/home) (requires an AWS login)
  * [Amazon Athena SQL and HiveQL reference](https://docs.aws.amazon.com/athena/latest/ug/ddl-sql-reference.html)



## Supported JDBC parameters

For Amazon Athena, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `ApplicationName`
  * `AwsCredentialsProviderArguments`
  * `AwsCredentialsProviderClass`
  * `AwsRegion`
  * `Catalog`
  * `Database`
  * `EnableResultReuseByAge`
  * `EndPointOverride`
  * `LogLevel`
  * `MaxQueryExecutionPollingInterval`
  * `maxResultReuseAgeInMinutes`
  * `MetadataRetrievalMethod`
  * `MinQueryExecutionPollingInterval`
  * `OutputLocation`
  * `password`
  * `ProxyHost`: For public Looker instances, the value for the `ProxyHost` parameter must be the public IP address of the instance.
  * `ProxyPort`
  * `ProxyPWD`
  * `ProxyUID`
  * `QueryExecutionPollingIntervalMultiplier`
  * `Region`
  * `ResultFetcher`
  * `ResultReuseByAgeConfiguration`
  * `s3_staging_dir`
  * `S3OutputEncOption`
  * `S3OutputLocation`
  * `Schema`
  * `user`
  * `UseResultsetStreaming`
  * `WorkGroup`



## Feature support

For Looker to support some features, your database dialect must also support them.

Amazon Athena supports the following features as of Looker 26.20:

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

After you have completed the database connection, [configure authentication options](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
