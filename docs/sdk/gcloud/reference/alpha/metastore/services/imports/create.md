---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/imports/create/
title: gcloud alpha metastore services imports create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:38:36.199728+00:00
---

# gcloud alpha metastore services imports create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/imports/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha metastore services imports create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha metastore services imports create - import metadata into a service 
SYNOPSIS
    

`gcloud alpha metastore services imports create` (`IMPORT` : `--location`=`LOCATION` `--service`=`SERVICE`) `--database-dump`=`DATABASE_DUMP` [`--async`] [`--database-dump-type`=`DATABASE_DUMP_TYPE`; default="MYSQL"] [`--database-type`=`DATABASE_TYPE`; default="MYSQL"] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` This command has been deprecated. Please use `[gcloud metastore services import gcs](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs)` instead. Import metadata with the given name and configurations in to a service. 
EXAMPLES
     To import metadata with the name `my-import` and description `testing description` into service `my-service` from a database dump with uri `gs://database-dump` and database type `mysql`, run: 
    
    
    gcloud alpha metastore services imports create my-import --service=my-service --description='testing description' --database-type=mysql --database-dump=gs://database-dump

POSITIONAL ARGUMENTS
    

Import resource - Arguments and flags that specify the metadata import you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `import` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`IMPORT`
     ID of the import or fully qualified identifier for the import. 

To set the `import` attribute: 

  * provide the argument `import` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataproc Metastore service. 

If not specified, will use `default` metastore/location. To set the `location` attribute: 

  * provide the argument `import` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `metastore/location`. 


`--service`=`SERVICE`
     The identifier of the Dataproc Metastore service 

To set the `service` attribute: 

  * provide the argument `import` on the command line with a fully specified name; 
  * provide the argument `--service` on the command line. 


REQUIRED FLAGS
    

`--database-dump`=`DATABASE_DUMP`
     A Cloud Storage object URI that specifies a database dump from which to import metadata. It must begin with `gs://`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--database-dump-type`=`DATABASE_DUMP_TYPE`; default="MYSQL"
     The type of the database dump. If unspecified, defaults to `MYSQL`. `DATABASE_DUMP_TYPE` must be (only one value is supported): 

`mysql`
     Database dump is a MYSQL dump file. 
`--database-type`=`DATABASE_TYPE`; default="MYSQL"
     (DEPRECATED) The type of the database. If unspecified, defaults to `MYSQL`. 

The --database-type option is deprecated; use --database-dump-type instead. `DATABASE_TYPE` must be (only one value is supported): 

`mysql`
     MySQL Database 
`--description`=`DESCRIPTION`
     The description of this metadata import. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta metastore services imports create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/imports/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
