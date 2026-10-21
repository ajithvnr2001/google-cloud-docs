---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/execute-sql/
title: gcloud alpha sql instances execute-sql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:04.556796+00:00
---

# gcloud alpha sql instances execute-sql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/execute-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql instances execute-sql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql instances execute-sql - executes a statement on a Cloud SQL instance 
SYNOPSIS
    

`gcloud alpha sql instances execute-sql` `INSTANCE` `--sql`=`SQL` [`--database`=`DATABASE`, `-d` `DATABASE`] [`--partial-result-mode`=`PARTIAL_RESULT_MODE`] [`--password-secret-version`=`PASSWORD_SECRET_VERSION`] [`--row-limit`=`ROW_LIMIT`] [`--user`=`USER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Executes a statement on a Cloud SQL instance. Before executing statements, follow Cloud SQL Data API's instructions to configure your database user and permissions. Note: The requests and responses might transit through intermediate locations between your client and the location of the target instance. 
EXAMPLES
     To execute a statement on a Cloud SQL instance using IAM database authentication, run: 
    
    
    gcloud alpha sql instances execute-sql my-instance-name --sql="ALTER TABLE employees RENAME TO personnel;" --database=my-db

To execute a statement on a Cloud SQL instance using password authentication, run: 
    
    
    gcloud alpha sql instances execute-sql my-instance-name --sql="ALTER TABLE employees RENAME TO personnel;" --database=my-db --user=my-user --password-secret-version=projects/my-project/locations/secret-location/secrets/my-secret/versions/latest

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
REQUIRED FLAGS
    

`--sql`=`SQL`
     SQL statement(s) to execute. It supports multiple statements as well. When it starts with the character '@', the rest should be a filepath to read the SQL statement(s) from. For example, --sql=@my_script.sql. 
OPTIONAL FLAGS
    

`--database`=`DATABASE`, `-d` `DATABASE`
     Database on which the statement is executed. 
`--partial-result-mode`=`PARTIAL_RESULT_MODE`
     Controls how the API responds when the SQL execution result is incomplete due to size limit or other reasons. The default mode is to return an error instead of returning a partial result. `PARTIAL_RESULT_MODE` must be one of: 

`ALLOW_PARTIAL_RESULT`
     If the complete result is unavailable, returns a partial result, marks the field <code>partial_result</code> to <code>true</code>, and doesn't throw an error. 
`FAIL_PARTIAL_RESULT`
     If the complete result is unavailable, returns an error and doesn't return the partial result. 
`PARTIAL_RESULT_MODE_UNSPECIFIED`
     Unspecified mode, effectively the same as <code>FAIL_PARTIAL_RESULT</code>. 
`--password-secret-version`=`PASSWORD_SECRET_VERSION`
     The resource name of the Secret Manager secret holding the password for the database user. The secret should be created using the regional endpoint and stored in the same region as the Cloud SQL instance. The expected resource name format is <code>projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}</code>. Used together with <code>\--user</code>. If not specified, IAM database authentication is used. 
`--row-limit`=`ROW_LIMIT`
     Maximum number of rows to return. The default is unlimited. 
`--user`=`USER`
     The database user to authenticate as. Used together with <code>\--password-secret-version</code>. If not specified, IAM database authentication is used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql instances execute-sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/execute-sql)
    
    
    [gcloud beta sql instances execute-sql](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/execute-sql)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
