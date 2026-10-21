---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/hive/tables/create/
title: gcloud alpha biglake hive tables create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:25:25.510553+00:00
---

# gcloud alpha biglake hive tables create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/hive/tables/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha biglake hive tables create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha biglake hive tables create - create a BigLake Hive table 
SYNOPSIS
    

`gcloud alpha biglake hive tables create` (`TABLE` : `--catalog`=`CATALOG` `--database`=`DATABASE`) `--file`=`FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a BigLake Hive table. 
EXAMPLES
     To create a table `my_table` in parent catalog `my-catalog` and database `my-database` using a creation request from `table_creation.json`, run: 
    
    
    gcloud alpha biglake hive tables create my_table --database=my-database --catalog=my-catalog --file=table_creation.json

The storageDescriptor field is required and must be specified in the file. 

Example `table_creation.json`: 
    
    
    {
      "name": "my_table",
      "storageDescriptor": {
        "locationUri": "gs://my-bucket/my-database/my_table",
        "inputFormat": "org.apache.hadoop.mapred.TextInputFormat",
        "outputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
        "serdeInfo": {
          "name": "my_table",
          "serializationLib": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe"
        },
        "columns": [
          {"name": "id", "type": "int"},
          {"name": "name", "type": "string"}
        ]
      },
      "parameters": {
        "EXTERNAL": "TRUE"
      }
    }

POSITIONAL ARGUMENTS
    

Table resource - The Hive Table to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `table` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TABLE`
     ID of the table or fully qualified identifier for the table. 

To set the `table` attribute: 

  * provide the argument `table` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--catalog`=`CATALOG`
     The Hive Catalog for the resource. 

To set the `catalog` attribute: 

  * provide the argument `table` on the command line with a fully specified name; 
  * provide the argument `--catalog` on the command line. 


`--database`=`DATABASE`
     The Hive Database for the resource. 

To set the `database` attribute: 

  * provide the argument `table` on the command line with a fully specified name; 
  * provide the argument `--database` on the command line. 


REQUIRED FLAGS
    

`--file`=`FILE`
     Path to a JSON or YAML file containing the Hive table definition. The format must follow the Hive Metastore API specification for `HiveTable`. The field `storageDescriptor` must be specified. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud biglake hive tables create](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/hive/tables/create)
    
    
    [gcloud beta biglake hive tables create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake/hive/tables/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
