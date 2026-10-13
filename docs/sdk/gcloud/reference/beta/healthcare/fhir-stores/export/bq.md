---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/fhir-stores/export/bq/
title: gcloud beta healthcare fhir-stores export bq \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:39.956630+00:00
---

# gcloud beta healthcare fhir-stores export bq  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/fhir-stores/export/bq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta healthcare fhir-stores export bq Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta healthcare fhir-stores export bq - export Cloud Healthcare API FHIR resources to BigQuery 
SYNOPSIS
    

`gcloud beta healthcare fhir-stores export bq` (`FHIR_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--bq-dataset`=`BQ_DATASET` `--schema-type`=`SCHEMA_TYPE` [`--async`] [`--recursive-depth`=`RECURSIVE_DEPTH`] [`--resource-type`=`RESOURCE_TYPE`] [`--since`=`SINCE`] [`--write-disposition`=`WRITE_DISPOSITION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Export Cloud Healthcare API FHIR resources to BigQuery. 
EXAMPLES
     To export the fhir-store 'test-fhir-store' to the BigQuery dataset 'bqdataset', run: 
    
    
    gcloud beta healthcare fhir-stores export bq test-fhir-store --bq-dataset=bq://my-project.bqdataset --dataset=test-dataset

To perform the same export, but with the 'ANALYTICS' schema and the recursive structure depth of 3, run: 
    
    
    gcloud beta healthcare fhir-stores export bq test-fhir-store --bq-dataset=bq://my-project.bqdataset --dataset=test-dataset --schema-type=analytics --recursive-depth=3

POSITIONAL ARGUMENTS
    

FhirStore resource - Cloud Healthcare API FHIR store to export resources from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `fhir_store` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FHIR_STORE`
     ID of the fhirStore or fully qualified identifier for the fhirStore. 

To set the `fhir_store` attribute: 

  * provide the argument `fhir_store` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--dataset`=`DATASET`
     Cloud Healthcare dataset. 

To set the `dataset` attribute: 

  * provide the argument `fhir_store` on the command line with a fully specified name; 
  * provide the argument `--dataset` on the command line. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `fhir_store` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `healthcare/location`. 


REQUIRED FLAGS
    

`--bq-dataset`=`BQ_DATASET`
     BigQuery dataset that houses the BigQuery tables. 
`--schema-type`=`SCHEMA_TYPE`
     Specifies the output schema type. If unspecified, the default is `LOSSLESS`. `SCHEMA_TYPE` must be one of: 

`analytics`
     Analytics schema defined by the FHIR community. See <https://github.com/rbrush/sql-on-fhir/blob/master/sql-on-fhir.md>. 
`analytics_v2`
     Analytics V2, similar to schema defined by the FHIR community, with added support for extensions with one or more occurrences and contained resources in stringified JSON. 
`lossless`
     Schema generated from original FHIR data. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--recursive-depth`=`RECURSIVE_DEPTH`
     The depth for all recursive structures in the output analytics schema. For example, concept in the CodeSystem resource is a recursive structure; when the depth is 2, the CodeSystem table will have a column called concept.concept but not concept.concept.concept. If not specified or set to 0, the server will use the default value 2. 
`--resource-type`=`RESOURCE_TYPE`
     String of comma-delimited FHIR resource types. If provided, only resources of the specified resource type(s) are exported. 
`--since`=`SINCE`
     If provided, only resources updated after this time are exported. The time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example, `2015-02-07T13:28:17.239+02:00` or `2017-01-01T00:00:00Z`. The time must be specified to the second and include a time zone. 
`--write-disposition`=`WRITE_DISPOSITION`
     Determines whether existing tables in the destination dataset are overwritten or appended to. `WRITE_DISPOSITION` must be one of: 

`write-append`
     Append data to the existing tables. 
`write-empty`
     Only export data if the destination tables are empty. 
`write-truncate`
     Erase all existing data in the tables before writing the instances. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud healthcare fhir-stores export bq](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq)
    
    
    [gcloud alpha healthcare fhir-stores export bq](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/fhir-stores/export/bq)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
