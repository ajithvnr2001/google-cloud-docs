---
url: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup/
title: gcloud datastream objects lookup \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:28:00.953734+00:00
---

# gcloud datastream objects lookup  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud datastream objects lookup Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud datastream objects lookup - lookup a Datastream stream object 
SYNOPSIS
    

`gcloud datastream objects lookup` (`--salesforce-object-name`=`SALESFORCE_OBJECT_NAME` | `--mysql-database`=`MYSQL_DATABASE` `--mysql-table`=`MYSQL_TABLE` | `--oracle-schema`=`ORACLE_SCHEMA` `--oracle-table`=`ORACLE_TABLE` | `--postgresql-schema`=`POSTGRESQL_SCHEMA` `--postgresql-table`=`POSTGRESQL_TABLE` | [`--spanner-table`=`SPANNER_TABLE` : `--spanner-schema`=`SPANNER_SCHEMA`] | `--sqlserver-schema`=`SQLSERVER_SCHEMA` `--sqlserver-table`=`SQLSERVER_TABLE`) (`--stream`=`STREAM` : `--location`=`LOCATION`) [`--endpoint-mode`=`ENDPOINT_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Lookup a stream object by its source object identifier (e.g. schema.table) 
EXAMPLES
     To lookup an existing Mysql stream object: 
    
    
    gcloud datastream objects lookup --stream=my-stream --location=us-central1 --mysql-database=my-db --mysql-table=my-table

To lookup an existing Oracle stream object: 
    
    
    gcloud datastream objects lookup --stream=my-stream --location=us-central1 --oracle-schema=my-schema --oracle-table=my-table

To lookup an existing PostgreSQL stream object: 
    
    
    gcloud datastream objects lookup --stream=my-stream --location=us-central1 --postgresql-schema=my-schema --postgresql-table=my-table

To lookup an existing SQL Server stream object: 
    
    
    gcloud datastream objects lookup --stream=my-stream --location=us-central1 --sqlserver-schema=my-schema --sqlserver-table=my-table

To lookup an existing Salesforce stream object: 
    
    
    gcloud datastream objects lookup --stream=my-stream --location=us-central1 --salesforce-object-name=my-object

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--salesforce-object-name`=`SALESFORCE_OBJECT_NAME`
     Salesforce object name. 
`--mysql-database`=`MYSQL_DATABASE`
     Mysql database for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--mysql-table`=`MYSQL_TABLE`
     Mysql table for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--oracle-schema`=`ORACLE_SCHEMA`
     Oracle schema for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--oracle-table`=`ORACLE_TABLE`
     Oracle table for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--postgresql-schema`=`POSTGRESQL_SCHEMA`
     PostgreSQL schema for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--postgresql-table`=`POSTGRESQL_TABLE`
     PostgreSQL table for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--spanner-table`=`SPANNER_TABLE`
     Spanner table name. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--spanner-schema`=`SPANNER_SCHEMA`
     Spanner schema name. 
`--sqlserver-schema`=`SQLSERVER_SCHEMA`
     SQL Server schema for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--sqlserver-table`=`SQLSERVER_TABLE`
     SQL Server table for the object. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Stream resource - The stream to list objects for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--stream` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--stream`=`STREAM`
     ID of the stream or fully qualified identifier for the stream. 

To set the `stream` attribute: 

  * provide the argument `--stream` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the stream. 

To set the `location` attribute: 

  * provide the argument `--stream` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


OPTIONAL FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
