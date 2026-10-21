---
url: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/objects/lookup/
title: gcloud database-migration objects lookup \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:52.815737+00:00
---

# gcloud database-migration objects lookup  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/objects/lookup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud database-migration objects lookup Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud database-migration objects lookup - lookup a DMS migration job object 
SYNOPSIS
    

`gcloud database-migration objects lookup` (`--database`=`DATABASE` `--schema`=`SCHEMA` `--table`=`TABLE`) (`--migration-job`=`MIGRATION_JOB` : `--region`=`REGION`) [`--endpoint-mode`=`ENDPOINT_MODE`] [`--type`=`TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Lookup a migration job object by its source object identifier (e.g. database) 
EXAMPLES
     To lookup an existing migration job object: 
    
    
    gcloud database-migration objects lookup --migration-job=my-job --location=us-central1 --database=my-database

REQUIRED FLAGS
    

The source object identifier. 

At least one of these must be specified: 

`--database`=`DATABASE`
     The name of the database to lookup. 
`--schema`=`SCHEMA`
     The name of the schema to lookup. 
`--table`=`TABLE`
     The name of the table to lookup. 
Migration job resource - The migration job to list migration job objects. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--migration-job` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--migration-job`=`MIGRATION_JOB`
     ID of the migration_job or fully qualified identifier for the migration_job. 

To set the `migration_job` attribute: 

  * provide the argument `--migration-job` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the migration_job. 

To set the `region` attribute: 

  * provide the argument `--migration-job` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


OPTIONAL FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--type`=`TYPE`
     The type of the object to lookup. If not provided, the default is DATABASE. `TYPE` must be one of: `DATABASE`, `SCHEMA`, `TABLE`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
