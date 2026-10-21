---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/upsert-datapoints/
title: gcloud beta ai indexes upsert-datapoints \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:51:00.402042+00:00
---

# gcloud beta ai indexes upsert-datapoints  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/upsert-datapoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai indexes upsert-datapoints Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai indexes upsert-datapoints - upsert data points into the specified index 
SYNOPSIS
    

`gcloud beta ai indexes upsert-datapoints` (`INDEX` : `--region`=`REGION`) `--datapoints-from-file`=`DATAPOINTS_FROM_FILE` [`--update-mask`=[`UPDATE_MASK_PATH`,…]] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To upsert datapoints into an index `123`, run: 
    
    
    gcloud beta ai indexes upsert-datapoints 123 --datapoints-from-file=example.json --project=example --region=us-central1

POSITIONAL ARGUMENTS
    

Index resource - Index to upsert data points from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `index` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INDEX`
     ID of the index or fully qualified identifier for the index. 

To set the `name` attribute: 

  * provide the argument `index` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the index. 

To set the `region` attribute: 

  * provide the argument `index` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


REQUIRED FLAGS
    

`--datapoints-from-file`=`DATAPOINTS_FROM_FILE`
     Path to a local JSON file that contains the data points that need to be added to the index. 
OPTIONAL FLAGS
    

`--update-mask`=[`UPDATE_MASK_PATH`,…]
     Update mask is used to specify the fields to be overwritten in the datapoints by the update. The fields specified in the update_mask are relative to each IndexDatapoint inside datapoints, not the full request. 

Updatable fields: 

  * Use --update-mask=`all_restricts` to update both `restricts` and `numeric_restricts`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai indexes upsert-datapoints](https://docs.cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints)
    
    
    [gcloud alpha ai indexes upsert-datapoints](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/upsert-datapoints)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
