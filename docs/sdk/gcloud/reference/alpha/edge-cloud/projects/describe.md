---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/projects/describe/
title: gcloud alpha edge-cloud projects describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:22.079947+00:00
---

# gcloud alpha edge-cloud projects describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/projects/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha edge-cloud projects describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha edge-cloud projects describe - describe a Google Cloud Platform project enabled on Google Distributed Cloud zone 
SYNOPSIS
    

`gcloud alpha edge-cloud projects describe` (`ZONAL_PROJECT` : `--location`=`LOCATION` `--organization`=`ORGANIZATION` `--zone`=`ZONE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe a Google Cloud Platform project enabled on Google Distributed Cloud Connected zone. 
EXAMPLES
     To describe a Google Cloud Platform project `sample-project` in Google Distributed Cloud zone `sample-zone` in organization `sample-org` and location `us-central1`, run: 
    
    
    gcloud alpha edge-cloud projects describe sample-project --location=us-central1 --zone=sample-zone --organization=sample-org

POSITIONAL ARGUMENTS
    

Zonal Project resource - Google Cloud Platform project enabled on Google Distributed Cloud Connected zone. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`ZONAL_PROJECT`
     ID of the Zonal Project or fully qualified identifier for the Zonal Project. 

To set the `zonal_project` attribute: 

  * provide the argument `zonal_project` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `zonal_project` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization name. 

To set the `organization` attribute: 

  * provide the argument `zonal_project` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


`--zone`=`ZONE`
     The name of the Google Distributed Cloud Edge zone. 

To set the `zone` attribute: 

  * provide the argument `zonal_project` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `edgecontainer/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/edge-cloud>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud edge-cloud projects describe](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/projects/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
