---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/zones/describe/
title: gcloud alpha edge-cloud zones describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:25.533795+00:00
---

# gcloud alpha edge-cloud zones describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/zones/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha edge-cloud zones describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha edge-cloud zones describe - describe a Google Distributed Cloud zone 
SYNOPSIS
    

`gcloud alpha edge-cloud zones describe` `ZONE` `--location`=`LOCATION` (`--organization`=`ORGANIZATION` | `--project`=`PROJECT`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Displays details about a specific Google Distributed Cloud zone. 
EXAMPLES
     To describe a zone named `my-zone` in organization `1234567890` and location `us-central1`, run: 
    
    
    gcloud alpha edge-cloud zones describe my-zone --location=us-central1 --organization=1234567890

To describe a zone named `another-zone` in project `my-sample-project` and location `us-central1`, run: 
    
    
    gcloud alpha edge-cloud zones describe another-zone --location=us-central1 --project=my-sample-project

POSITIONAL ARGUMENTS
    

`ZONE`
     Google Distributed Cloud zone name to describe. 
REQUIRED FLAGS
    

`--location`=`LOCATION`
     Google Cloud Platform location. 
Exactly one of these must be specified: 

`--organization`=`ORGANIZATION`
     Google Distributed Cloud organization number for the zone. 
`--project`=`PROJECT`
     Google Cloud Platform project ID for the zone. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `edgecontainer/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/edge-cloud>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud edge-cloud zones describe](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/zones/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
