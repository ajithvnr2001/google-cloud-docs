---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deploy/delivery-pipelines/export/
title: gcloud beta deploy delivery-pipelines export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:57:16.051809+00:00
---

# gcloud beta deploy delivery-pipelines export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deploy/delivery-pipelines/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta deploy delivery-pipelines export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta deploy delivery-pipelines export - returns the .yaml definition of the specified delivery pipeline 
SYNOPSIS
    

`gcloud beta deploy delivery-pipelines export` [[`DELIVERY_PIPELINE`] `--region`=`REGION`] [`--destination`=`DESTINATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` The exported yaml definition can be applied by 'deploy apply' command. 
EXAMPLES
     To return the .yaml definition of the delivery pipeline 'test-pipeline', in region 'us-central1', run: 
    
    
    gcloud beta deploy delivery-pipelines export test-pipeline --region=us-central1

POSITIONAL ARGUMENTS
    

Delivery pipeline resource - The name of the Delivery Pipeline. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `delivery_pipeline` on the command line with a fully specified name; 
  * set the property `deploy/delivery_pipeline` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


[`DELIVERY_PIPELINE`]
     ID of the delivery_pipeline or fully qualified identifier for the delivery_pipeline. 

To set the `delivery-pipeline` attribute: 

  * provide the argument `delivery_pipeline` on the command line; 
  * set the property `deploy/delivery_pipeline`. 


`--region`=`REGION`
     The Cloud region for the delivery_pipeline. Alternatively, set the property [deploy/region]. 

To set the `region` attribute: 

  * provide the argument `delivery_pipeline` on the command line with a fully specified name; 
  * set the property `deploy/delivery_pipeline` with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `deploy/region`. 


FLAGS
    

`--destination`=`DESTINATION`
     Path to a YAML file where the configuration will be exported. Alternatively, you may omit this flag to write to standard output. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud deploy delivery-pipelines export](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/export)
    
    
    [gcloud alpha deploy delivery-pipelines export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deploy/delivery-pipelines/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
