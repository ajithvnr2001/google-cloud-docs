---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license/
title: gcloud compute commitments create-license \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:05.293802+00:00
---

# gcloud compute commitments create-license  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute commitments create-license Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute commitments create-license - create Compute Engine license-based commitments 
SYNOPSIS
    

`gcloud compute commitments create-license` `COMMITMENT` `--amount`=`AMOUNT` `--license`=`LICENSE` `--plan`=`PLAN` [`--cores-per-license`=`CORES_PER_LICENSE`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create Compute Engine license-based commitments. 
EXAMPLES
     To create a commitment called ``commitment-1`` in the ``us-central1`` region with 36-month plan, sles-sap-12 license, 1-2 cores, run: 
    
    
    gcloud compute commitments create-license commitment-1 --plan=36-month --license=https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-12 --region=us-central1 --amount=1 --cores-per-license=1-2

POSITIONAL ARGUMENTS
    

`COMMITMENT`
     Name of the commitment to create. 
REQUIRED FLAGS
    

`--amount`=`AMOUNT`
     Number of licenses purchased. 
`--license`=`LICENSE`
     Applicable license URI. For example: `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-12`
`--plan`=`PLAN`
     Duration of the commitment. `PLAN` must be one of: `12-month`, `36-month`. 
OPTIONAL FLAGS
    

`--cores-per-license`=`CORES_PER_LICENSE`
     Core range of the instance. Must be one of: `1-2`, `3-4`, `5+`. Required for SAP licenses. 
`--region`=`REGION`
     Region of the commitment to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute commitments create-license](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/create-license)
    
    
    [gcloud beta compute commitments create-license](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/commitments/create-license)
    
    
    [gcloud preview compute commitments create-license](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/commitments/create-license)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
