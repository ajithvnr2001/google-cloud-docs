---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export/
title: gcloud artifacts sbom export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:14.879276+00:00
---

# gcloud artifacts sbom export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts sbom export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts sbom export - export SBOM files to Google Cloud Storage 
SYNOPSIS
    

`gcloud artifacts sbom export` `--uri`=`URI` [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Export SBOM files to Google Cloud Storage. 
EXAMPLES
     To export an SBOM file for the Artifact Registry image with URI "us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz": 
    
    
    gcloud artifacts sbom export --uri=us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz

REQUIRED FLAGS
    

`--uri`=`URI`
     The URI of the Artifact Registry image the SBOM is exported for. A 'gcr.io' image can also be used if redirection is enabled in Artifact Registry. Make sure 'artifactregistry.projectsettings.get' permission is granted to the current gcloud user to verify the redirection status. 
OPTIONAL FLAGS
    

`--location`=`LOCATION`
     If specified, all requests to Artifact Analysis for occurrences will go to location specified 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
