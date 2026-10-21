---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/execute-sql/
title: gcloud alpha spanner databases execute-sql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:33.543297+00:00
---

# gcloud alpha spanner databases execute-sql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/execute-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner databases execute-sql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner databases execute-sql - executes a SQL query against a Cloud Spanner database 
SYNOPSIS
    

`gcloud alpha spanner databases execute-sql` (`DATABASE` : `--instance`=`INSTANCE`) `--sql`=`SQL` [`--database-role`=`DATABASE_ROLE`] [`--enable-partitioned-dml`] [`--priority`=`PRIORITY`] [`--query-mode`=`QUERY_MODE`; default="NORMAL"] [`--timeout`=`TIMEOUT`; default="10m"] [`--read-timestamp`=`TIMESTAMP` | `--strong`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Executes a SQL query against a Cloud Spanner database. 
EXAMPLES
     To execute a SQL SELECT statement against example-database under example-instance, run: 
    
    
    gcloud alpha spanner databases execute-sql example-database --instance=example-instance --sql='SELECT * FROM MyTable WHERE MyKey = 1'

POSITIONAL ARGUMENTS
    

Database resource - The Cloud Spanner database to execute the SQL query against. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `database` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The Cloud Spanner instance for the database. 

To set the `instance` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


REQUIRED FLAGS
    

`--sql`=`SQL`
     The SQL query to issue to the database. Cloud Spanner SQL is described at <https://cloud.google.com/spanner/docs/query-syntax>
OPTIONAL FLAGS
    

`--database-role`=`DATABASE_ROLE`
     Database role user assumes while accessing the database. 
`--enable-partitioned-dml`
     Execute DML statement using Partitioned DML 
`--priority`=`PRIORITY`
     The priority for the execute SQL request. `PRIORITY` must be one of: `high`, `low`, `medium`, `unspecified`. 
`--query-mode`=`QUERY_MODE`; default="NORMAL"
     Mode in which the query must be processed. `QUERY_MODE` must be one of: 

`NORMAL`
     Returns only the query result, without any information about the query plan. 
`PLAN`
     Returns only the query plan, without any result rows or execution statistics information. 
`PROFILE`
     Returns the query plan, overall execution statistics, operator-level execution statistics, along with the result rows. 
`WITH_PLAN_AND_STATS`
     Returns the query plan, overall (but not operator-level) execution statistics, along with the results. 
`WITH_STATS`
     Returns the overall (but not operator-level) execution statistics along with the results. 
`--timeout`=`TIMEOUT`; default="10m"
     Maximum time to wait for the SQL query to complete. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
Read-only query timestamp bound. The default is --strong. See <https://cloud.google.com/spanner/docs/timestamp-bounds>. 

At most one of these can be specified: 

`--read-timestamp`=`TIMESTAMP`
     Perform a query at the given timestamp. 
`--strong`
     Perform a strong query. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud spanner databases execute-sql](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql)
    
    
    [gcloud beta spanner databases execute-sql](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/databases/execute-sql)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
