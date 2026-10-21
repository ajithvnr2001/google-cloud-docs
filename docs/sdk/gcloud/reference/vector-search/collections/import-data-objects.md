---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/import-data-objects/
title: gcloud vector-search collections import-data-objects \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:38.991545+00:00
---

# gcloud vector-search collections import-data-objects  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/import-data-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vector-search collections import-data-objects Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vector-search collections import-data-objects - import data objects into a collection 
SYNOPSIS
    

`gcloud vector-search collections import-data-objects` (`COLLECTION` : `--location`=`LOCATION`) `--gcs-import-contents-uri`=`GCS_IMPORT_CONTENTS_URI` `--gcs-import-error-uri`=`GCS_IMPORT_ERROR_URI` [`--async`] [`--gcs-import-output-uri`=`GCS_IMPORT_OUTPUT_URI`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Import data objects into a collection from Google Cloud Storage. 
EXAMPLES
     To import data objects into a collection `my-collection` in project `my-project` and location `us-central1` from Google Cloud Storage bucket `my-bucket`, run: 
    
    
    gcloud vector-search collections import-data-objects my-collection --location=us-central1 --gcs-import-contents-uri=gs://my-bucket/contents/ --gcs-import-error-uri=gs://my-bucket/errors/ --project=my-project

POSITIONAL ARGUMENTS
    

Collection resource - The resource name of the Collection to import DataObjects into. Format: `projects/{project}/locations/{location}/collections/{collection}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `collection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`COLLECTION`
     ID of the collection or fully qualified identifier for the collection. 

To set the `collection` attribute: 

  * provide the argument `collection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the collection resource. 

To set the `location` attribute: 

  * provide the argument `collection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--gcs-import-contents-uri`=`GCS_IMPORT_CONTENTS_URI`
     URI prefix of the Cloud Storage DataObjects to import. 
`--gcs-import-error-uri`=`GCS_IMPORT_ERROR_URI`
     URI prefix of the Cloud Storage location to write any errors encountered during the import. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--gcs-import-output-uri`=`GCS_IMPORT_OUTPUT_URI`
     URI prefix of the Cloud Storage location to write DataObject `IDs` and `etags` of DataObjects that were successfully imported. The service will write the successfully imported DataObjects to sharded files under this prefix. If this field is empty, no output will be written. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vectorsearch/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview>
NOTES
     This variant is also available: 
    
    
    [gcloud beta vector-search collections import-data-objects](https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/import-data-objects)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
