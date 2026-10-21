---
url: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/create/
title: gcloud biglake iceberg tables create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:33.977394+00:00
---

# gcloud biglake iceberg tables create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud biglake iceberg tables create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud biglake iceberg tables create - create a BigLake Iceberg table 
SYNOPSIS
    

`gcloud biglake iceberg tables create` `--create-from-file`=`CREATE_FROM_FILE` (`--namespace`=`NAMESPACE` : `--catalog`=`CATALOG`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a BigLake Iceberg table. 
EXAMPLES
     To create a table `my_table` in parent catalog `my-catalog` and namespace `my-namespace` using a creation request from `table_creation.json`, run: 
    
    
    gcloud biglake iceberg tables create --namespace=my-namespace --catalog=my-catalog --create-from-file=table_creation.json

The table name and schema fields are required and must be specified in `table_creation.json`. 

Example `table_creation.json`: 
    
    
    {
      "name": "my_table",
      "location": "gs://my-catalog/my-namespace/my_table",
      "schema": {
        "type": "struct",
        "schema-id": 0,
        "fields": [
          {
            "id": 1,
            "name": "user_id",
            "required": true,
            "type": "long",
            "doc": "Unique identifier for the user"
          },
          {
            "id": 2,
            "name": "username",
            "required": false,
            "type": "string"
          }
        ]
      },
      "partition-spec": {
        "spec-id": 0,
        "fields": [
          {
            "name": "user_id_bucket",
            "transform": "bucket[5]",
            "source-id": 1,
            "partition-id": 1001
          }
        ]
      },
      "write-order": {
        "order-id": 0,
        "fields": [
          {
            "transform": "identity",
            "source-id": 1,
            "direction": "asc",
            "null-order": "nulls-last"
          }
        ]
      },
      "stage-create": false,
      "properties": {
        "owner": "owner",
        "environment": "test",
        "write.format.default": "parquet",
        "comment": "Creating a new table"
      }
    }

REQUIRED FLAGS
    

`--create-from-file`=`CREATE_FROM_FILE`
     Path to a JSON file containing the table creation request. The format must follow the Apache Iceberg REST Catalog Open API specification for `CreateTableRequest`. The fields `name` and `schema` must be specified. 
Namespace resource - The Iceberg Namespace to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--namespace` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--namespace`=`NAMESPACE`
     ID of the namespace or fully qualified identifier for the namespace. 

To set the `namespace` attribute: 

  * provide the argument `--namespace` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--catalog`=`CATALOG`
     The Iceberg Catalog for the resource. 

To set the `catalog` attribute: 

  * provide the argument `--namespace` on the command line with a fully specified name; 
  * provide the argument `--catalog` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha biglake iceberg tables create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/iceberg/tables/create)
    
    
    [gcloud beta biglake iceberg tables create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake/iceberg/tables/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
