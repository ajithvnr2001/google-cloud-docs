---
url: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq/
title: gcloud healthcare dicom-stores export bq \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:23.506788+00:00
---

# gcloud healthcare dicom-stores export bq  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud healthcare dicom-stores export bq Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud healthcare dicom-stores export bq - export a Cloud Healthcare API API DICOM store to BigQuery 
SYNOPSIS
    

`gcloud healthcare dicom-stores export bq` (`DICOM_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--bq-table`=`BQ_TABLE` [`--async`] [`--overwrite-table`] [`--write-disposition`=`WRITE_DISPOSITION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Export a Cloud Healthcare API API DICOM store to BigQuery. 
EXAMPLES
     To export the dicom-store ``test-dicom-store`` to the BigQuery table ``testtable`` in the dataset ``testdataset``, overwriting any existing table, run: 
    
    
    gcloud healthcare dicom-stores export bq test-dicom-store --bq-table=bq://my-project.testdataset.testtable --dataset=test-dataset --write-disposition=write-truncate

To export the dicom-store ``test-dicom-store`` to the BigQuery table ``testtable`` in the dataset ``testdataset``, appending any existing table, run: 
    
    
    gcloud healthcare dicom-stores export bq test-dicom-store --bq-table=bq://my-project.testdataset.testtable --dataset=test-dataset --write-disposition=write-append

POSITIONAL ARGUMENTS
    

DicomStore resource - Cloud Healthcare API DICOM store to export. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `dicom_store` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DICOM_STORE`
     ID of the dicomStore or fully qualified identifier for the dicomStore. 

To set the `dicom_store` attribute: 

  * provide the argument `dicom_store` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--dataset`=`DATASET`
     Cloud Healthcare dataset. 

To set the `dataset` attribute: 

  * provide the argument `dicom_store` on the command line with a fully specified name; 
  * provide the argument `--dataset` on the command line. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `dicom_store` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `healthcare/location`. 


REQUIRED FLAGS
    

`--bq-table`=`BQ_TABLE`
     The BigQuery table where the DICOM store should be written. If this table does not exist, a new table with the given name will be created. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--overwrite-table`
     If the destination table already exists and this flag is `TRUE`, the table will be overwritten by the contents of the DICOM store. If the flag is not set and the destination table already exists, the export call returns an error. 
`--write-disposition`=`WRITE_DISPOSITION`
     Determines whether the existing table in the destination is to be overwritten or appended to. `WRITE_DISPOSITION` must be one of: 

`write-append`
     Append data to the existing table. 
`write-empty`
     Only export data if the destination table is empty. 
`write-truncate`
     Erase all existing data in a table before writing the instances. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha healthcare dicom-stores export bq](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/dicom-stores/export/bq)
    
    
    [gcloud beta healthcare dicom-stores export bq](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/dicom-stores/export/bq)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
