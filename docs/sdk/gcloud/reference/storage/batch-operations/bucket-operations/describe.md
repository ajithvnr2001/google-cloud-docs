---
url: https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/bucket-operations/describe/
title: gcloud storage batch-operations bucket-operations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:01.484232+00:00
---

# gcloud storage batch-operations bucket-operations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/bucket-operations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud storage batch-operations bucket-operations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud storage batch-operations bucket-operations describe - describe a bucket operation for a batch operation job 
SYNOPSIS
    

`gcloud storage batch-operations bucket-operations describe` (`BUCKET_OPERATION` : `--job`=`JOB`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a single bucket operation for a batch operation job. 
EXAMPLES
     The following example command describes bucket operation `bo-1` for batch job `my-job`: 
    
    
    gcloud storage batch-operations bucket-operations describe bo-1 --job=my-job

The following example command describes bucket operation `bo-1` using its fully qualified name: 
    
    
    gcloud storage batch-operations bucket-operations describe projects/my-project/locations/global/jobs/my-job/bucketOperations/bo-1

POSITIONAL ARGUMENTS
    

Bucket operation resource - The bucket operation to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `bucket_operation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `bucket_operation` on the command line with a fully specified name; 
  * The default is `global`. 



This must be specified. 

`BUCKET_OPERATION`
     ID of the bucket-operation or fully qualified identifier for the bucket-operation. 

To set the `bucket-operation` attribute: 

  * provide the argument `bucket_operation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--job`=`JOB`
     Batch Job ID for the bucket-operation. 

To set the `job` attribute: 

  * provide the argument `bucket_operation` on the command line with a fully specified name; 
  * provide the argument `--job` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha storage batch-operations bucket-operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/batch-operations/bucket-operations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
