---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/alter-table-properties/
title: gcloud alpha metastore services alter-table-properties \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:24:16.204410+00:00
---

# gcloud alpha metastore services alter-table-properties  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/alter-table-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha metastore services alter-table-properties Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha metastore services alter-table-properties - alter metadata table properties 
SYNOPSIS
    

`gcloud alpha metastore services alter-table-properties` (`SERVICE` : `--location`=`LOCATION`) `--properties`=[`KEY`=`VALUE`,…] `--table-name`=`TABLE_NAME` `--update-mask`=`UPDATE_MASK` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Alter metadata table properties from a Dataproc Metastore service's underlying metadata store. 

If run asynchronously with `--async`, exits after printing one operation name that can be used to poll the status of the creation via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To alter metadata table properties a and b on table-name `databases/{database_id}/tables/{table_id}` , use the update-mask `properties.a,properties.b` , and run: 
    
    
    gcloud alpha metastore services alter-table-properties my-metastore-service --location=us-central1 --table-name=databases/my-database/tables/my-table --update-mask=properties.a,properties.b --properties=a=1,b=2

POSITIONAL ARGUMENTS
    

Service resource - Arguments and flags that specify the table you want to alter. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataproc Metastore service. 

If not specified, will use `default` metastore/location. To set the `location` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `metastore/location`. 


REQUIRED FLAGS
    

`--properties`=[`KEY`=`VALUE`,…]
     A string where field names are separated by a comma. Describes the desired values to mutate. If update-mask is empty, the properties will not update. Otherwise, the properties only alter the values whose associated paths exist in the update mask. 

For example, the desired key-value pairs. 

a=2,b=3,c=4 

`--table-name`=`TABLE_NAME`
     The name of the table containing the properties you're altering in the following format. 

`databases/{database_id}/tables/{table_id}`

`--update-mask`=`UPDATE_MASK`
     A string where field names are separated by a comma. Specifies the metadata table properties fields that are overwritten by the update. Fields specified in the `update-mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask. 

For example, given the target properties: 
    
    
    properties {
      a: 1
      b: 2
    }

And an update properties: 
    
    
    properties {
      a: 2
      b: 3
      c: 4
    }

then if the field mask is: 

`properties.b,properties.c`

then the updated result will be: 
    
    
    properties {
      a: 1
      b: 3
      c: 4
    }

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud metastore services alter-table-properties](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties)
    
    
    [gcloud beta metastore services alter-table-properties](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/alter-table-properties)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
