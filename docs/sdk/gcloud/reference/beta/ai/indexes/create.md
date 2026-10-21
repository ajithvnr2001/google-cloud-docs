---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create/
title: gcloud beta ai indexes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:16.942673+00:00
---

# gcloud beta ai indexes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai indexes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai indexes create - create a new Vertex AI index 
SYNOPSIS
    

`gcloud beta ai indexes create` `--display-name`=`DISPLAY_NAME` `--metadata-file`=`METADATA_FILE` [`--description`=`DESCRIPTION`] [`--encryption-kms-key-name`=`ENCRYPTION_KMS_KEY_NAME`] [`--index-update-method`=`INDEX_UPDATE_METHOD`] [`--labels`=[`KEY`=`VALUE`,…]] [`--metadata-schema-uri`=`METADATA_SCHEMA_URI`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create an index under project `example` in region `us-central1`, encrypted with KMS key `kms-key-name`, run: 
    
    
    gcloud beta ai indexes create --display-name=index --description=test --metadata-file=path/to/your/metadata.json --project=example --region=us-central1 --encryption-kms-key-name=kms-key-name

REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name of the index. 
`--metadata-file`=`METADATA_FILE`
     Path to a local JSON file that contains the additional metadata information about the index. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of the index. 
`--encryption-kms-key-name`=`ENCRYPTION_KMS_KEY_NAME`
     The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key. 

The key needs to be in the same region as where the compute resource is created. 

`--index-update-method`=`INDEX_UPDATE_METHOD`
     The update method to use with this index. Choose `stream-update` or `batch-update` (case insensitive). If not set, batch update will be used by default. `INDEX_UPDATE_METHOD` must be one of: 

`batch-update`
     can update index with `[gcloud ai indexes update](https://docs.cloud.google.com/sdk/gcloud/reference/ai/indexes/update)` usingdatapoints files on Cloud Storage. 
`stream-update`
     can update datapoints with `upsert-datapoints` and`delete-datapoints` and will be applied nearly real-time. `
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. `

`--metadata-schema-uri`=`METADATA_SCHEMA_URI`
     Points to a YAML file stored on Google Cloud Storage describing additional information about index. 
Region resource - Cloud region to create index. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the project` attribute: 

  * provide the argument 

`\--region` on the command line with a fully specified name; 
* set the property 
`ai/region` with a fully specified name; 
* choose one from the prompted list of available regions with a fully specified name; 
* provide the argument 
`\--project` on the command line; 
* set the property 
`core/project`. `

`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the region` attribute: 

  * provide the argument 

`\--region` on the command line; 
* set the property 
`ai/region`; 
* choose one from the prompted list of available regions. 
`

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai indexes create](https://docs.cloud.google.com/sdk/gcloud/reference/ai/indexes/create)
    
    
    [gcloud alpha ai indexes create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
