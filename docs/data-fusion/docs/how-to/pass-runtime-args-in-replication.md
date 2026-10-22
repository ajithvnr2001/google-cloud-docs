---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/pass-runtime-args-in-replication/
title: Pass a runtime argument to a Replication job \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:10.635866+00:00
---

# Pass a runtime argument to a Replication job  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/pass-runtime-args-in-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Pass a runtime argument to a Replication job Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to pass runtime arguments in Cloud Data Fusion replication jobs.

## Pass a Debezium argument to a replication job

To pass an argument from a Debezium application to a MySQL or SQL Server replication job in Cloud Data Fusion, specify a runtime argument using the prefix, `source.connector`.

### Console

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click menu **Menu > Control Center**.

  3. Locate the **Application** for the replication job and click build **Preferences**. The **Preferences** window opens.

  4. In the **Key** field, specify a runtime argument for the replication job by prefixing it with `source.connector`.

![Go to Preferences and enter source.connector as a prefix to the Key.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/add-runtime-argument.png)

  5. Click **Save & Close**.




### REST API

To set a runtime argument using the REST API, see the [CDAP Preferences Microservices](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561058/Preferences+Microservices) reference.

## Configure JDBC parameters

To pass a JDBC parameter to a MySQL or SQL Server replication job, specify the runtime argument prefixed with `source.connector.database`.

For example, to configure the JDBC parameter `sessionVariables` to `MAX_EXECUTION_TIME=43200000`, [set a runtime argument](https://docs.cloud.google.com/data-fusion/docs/how-to/pass-runtime-args-in-replication#debezium-arguments) with the key `source.connector.database.sessionVariables` and the value `MAX_EXECUTION_TIME=43200000`.

To configure multiple JDBC parameters, set a runtime argument for each parameter. For example, to configure the JDBC parameters `encrypt=true&trustServerCertificate=true`, pass the following arguments:

Key | Value  
---|---  
`source.connector.database.encrypt` | `true`  
`source.connector.database.trustServerCertificate` | `true`  
**Note:** Cloud Data Fusion doesn't support setting JDBC arguments during the setup or assessment of a replication job. If you must set JDBC parameters to resolve assessment issues, bypass the assessment by deploying the replication job through the [Replication API](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref#create-a-replication-job). Then, before you start the job, configure the JDBC arguments as described previously in this section.

## Configure the primary key parameter

The source table that gets replicated must have a primary key. This is a strict requirement only when Oracle is the source database. For SQL Server and MySQL sources, you can specify a custom primary key, even if the source table doesn't have one.

Set the `key` parameter with the following runtime argument:

`source.connector.message.key.columns = SCHEMA.TABLE:KEY_COLUMN`

Replace the following:

  * SCHEMA: The name of the source schema.
  * TABLE: The source table name.
  * KEY_COLUMN: The column that contains the secure key.



You can set the primary key for multiple tables with the `key` property. The following example shows how to set the key for the tables `inventory.customers` and `purchase.orders`:
    
    
    source.connector.message.key.columns = inventory.customers:pk1,pk2;purchase.orders:pk3,pk4
    

![Go to Preferences and set the primary key parameter.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/key-runtime-argument.png)

## Configure isolation mode for a snapshot in SQL Server replication

For more information about the runtime argument for isolation mode, see [Isolation levels in SQL Server replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication-isolation-levels).

## What's next

  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication) in Cloud Data Fusion.
  * Refer to the [Replication API reference](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
