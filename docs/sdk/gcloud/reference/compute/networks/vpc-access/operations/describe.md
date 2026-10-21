---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/operations/describe/
title: gcloud compute networks vpc-access operations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:02:31.056459+00:00
---

# gcloud compute networks vpc-access operations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/operations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute networks vpc-access operations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute networks vpc-access operations describe - show metadata for a VPC Access Service operation 
SYNOPSIS
    

`gcloud compute networks vpc-access operations describe` (`OPERATION` : `--region`=`REGION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Display all metadata associated with a VPC Access Service operation given a valid operation name. 

This command can fail for the following reasons: 

  * The operation specified does not exist. 
  * The active account does not have permission to access the given operation. 


EXAMPLES
     The following command prints metadata for an operation with the name in region `us-central1`: 
    
    
    gcloud compute networks vpc-access operations describe operation-1564112342235-435a134f8c3f8-81bb4b49-0830c1f8 --region=us-central

POSITIONAL ARGUMENTS
    

Operation resource - The operation to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `operation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`OPERATION`
     ID of the operation or fully qualified identifier for the operation. 

To set the `operation` attribute: 

  * provide the argument `operation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Compute region (e.g. us-central1) for the connector. To set the `region` attribute: 

  * provide the argument `operation` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vpcaccess/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/vpc/docs/configure-serverless-vpc-access>
NOTES
     These variants are also available: 
    
    
    [gcloud beta compute networks vpc-access operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/vpc-access/operations/describe)
    
    
    [gcloud preview compute networks vpc-access operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/networks/vpc-access/operations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
