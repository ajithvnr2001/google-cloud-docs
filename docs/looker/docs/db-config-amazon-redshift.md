---
url: https://docs.cloud.google.com/looker/docs/db-config-amazon-redshift/
title: Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+ \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:07:29.609892+00:00
---

# Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-amazon-redshift/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+ Stay organized with collections  Save and categorize content based on your preferences. 

Looker supports connections with Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+.

  * For Amazon Redshift connections, Looker uses the PostgreSQL JDBC driver.
  * For Amazon Redshift 2.1+ and Amazon Redshift Serverless 2.1+ connections, Looker uses the Redshift JDBC driver.

**Note:** For [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/) deployments, Looker can connect successfully, but it may encounter issues with killing queries because of a difference in the system tables for retrieving query connection IDs. 



Optionally, you can also access data from Amazon Redshift using [Amazon Redshift Spectrum](https://aws.amazon.com/redshift/spectrum/) to access data stored in S3.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

If you're interested in using SSL encryption, see the [Amazon Redshift documentation on configuring security options for connections](http://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html).

If you will use an [SSH tunnel](https://docs.cloud.google.com/looker/docs/using-an-ssh-tunnel) your Redshift client and SSH server must be [set to an MTU of 1500](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network_mtu.html).

## Users and security

First, create your Looker user. Change password to a unique, secure password:
    
    
    CREATE USER looker WITH PASSWORD 'password';
    

See the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html#r_CREATE_USER-parameters) for information about password constraints.

Next, grant the appropriate privileges:
    
    
    GRANT USAGE ON SCHEMA public TO looker;
    GRANT SELECT ON TABLE public.table1 TO looker;
    GRANT SELECT ON TABLE public.table2 TO looker;
    ...
    GRANT SELECT ON TABLE public.tableN TO looker;
    

To give Looker access to the information schema data that it needs to [generate LookML](https://docs.cloud.google.com/looker/docs/generating-a-model) and that it needs for the [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics) side bar, run the following commands:
    
    
    GRANT SELECT ON TABLE information_schema.tables TO looker;
    GRANT SELECT ON TABLE information_schema.columns TO looker;
    

If you want to `GRANT SELECT` on all of your tables to the `looker` user, execute this query:
    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO looker;
    

For acceptable Redshift performance, it is necessary to set the proper distribution and sort keys. See the [Redshift documentation](http://docs.aws.amazon.com/redshift/latest/dg/t_Creating_tables.html) for details.

## Temp schema setup

While logged in to your Redshift database as an admin user, run:
    
    
    CREATE SCHEMA looker_scratch AUTHORIZATION looker;
    

If the `looker_scratch` schema is already created or has bad permissions:
    
    
    ALTER SCHEMA looker_scratch OWNER TO looker;
    

## Setting the search_path

Finally, you should set an appropriate `search_path`, which Looker SQL Runner uses to retrieve certain metadata from your database. Assuming that you have created a user called `looker`, and a temp schema called `looker_scratch`, the command is as follows:
    
    
    ALTER USER looker SET search_path TO '$user',looker_scratch,schema_of_interest,public;
                                                                ^^^^^^^^^^^^^^^^^^
                                                                ^^^^^^^^^^^^^^^^^^
                                                 include a comma-separated list of
                                                all schemas you'll use with Looker
    

## Optionally accessing data in S3 using Amazon Redshift Spectrum

You can take full advantage of Amazon Redshift Spectrum's performance from within Looker.

Spectrum significantly extends the functionality and ease of use for Redshift by letting users access data stored in S3, without having to load it into Redshift first. You can even join S3 data to data stored in Redshift, and the Redshift optimizer will take care of maximizing your query performance, optimizing both the S3 and Redshift portions of your query. For information on setting up access using Amazon Spectrum, see the Community post on [Using Amazon Redshift's new Spectrum Feature](https://www.googlecloudcommunity.com/gc/Modeling/Using-Amazon-Redshift-s-new-Spectrum-Feature/m-p/576711#M5207).

## Creating the Looker connection to your database

After completing the database configuration, you can connect to the database by performing the following steps:

  1. Click the Looker **Main menu** icon menu and select **Admin** , if the **Admin** menu isn't already displayed. (You may have to click the back arrow if the **Explore** or **Develop** menu is displayed.)
  2. In the **Admin** menu, select **Connections** , and then click **Add Connection**.
  3. From the **Dialect** drop-down menu, select **Amazon Redshift** , **Amazon Redshift 2.1+** , or **Amazon Redshift Serverless 2.1+**.
  4. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.
  5. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.
  6. If Looker displays **Can Connect** , press **Connect** to create the connection. 



Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `AccessKeyID`
  * `AllowDBUserOverride`
  * `ApplicationName`
  * `AuthMech`
  * `AutoCreate`
  * `ClusterID`
  * `connectTimeout`
  * `DbGroups`
  * `DbUser`
  * `HOST`: For public Looker instances, the value for the `HOST` parameter must be the public IP address of the instance.
  * `IdP_Host`: For public Looker instances, the value for the `IdP_Host` parameter must be the public IP address of the instance.
  * `IdP_Port`
  * `IdP_Tenant`
  * `loginTimeout`
  * `LogLevel`
  * `password`
  * `PORT`
  * `Preferred_Role`
  * `Profile`
  * `queryGroup`
  * `Region`
  * `SecretAccessKey`
  * `SessionToken`
  * `socketTimeout`
  * `ssl`
  * `sslFactory`
  * `sslmode`
  * `tcpKeepAlive`
  * `User`
  * `UseStaticIdp`



## Feature support

For Looker to support some features, your database dialect must also support them. The following sections show the feature support for Amazon Redshift dialects:

  * Amazon Redshift
  * Amazon Redshift 2.1+
  * Amazon Redshift Serverless 2.1+



### Amazon Redshift

Amazon Redshift supports the following features as of Looker 26.18:

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
  
### Amazon Redshift 2.1+

Amazon Redshift 2.1+ supports the following features as of Looker 26.18:

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
  
### Amazon Redshift Serverless 2.1+

Amazon Redshift Serverless 2.1+ supports the following features as of Looker 26.18:

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
