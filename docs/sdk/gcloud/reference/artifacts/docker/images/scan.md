---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan/
title: gcloud artifacts docker images scan \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:09.219692+00:00
---

# gcloud artifacts docker images scan  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts docker images scan Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts docker images scan - perform a vulnerability scan on a container image 
SYNOPSIS
    

`gcloud artifacts docker images scan` `RESOURCE_URI` [`--additional-package-types`=[`ADDITIONAL_PACKAGE_TYPES`,…]] [`--async`] [`--location`=`LOCATION`; default="us"] [`--remote`] [`--skip-package-types`=[`SKIP_PACKAGE_TYPES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     You can scan a container image in a Google Cloud registry (Artifact Registry or Container Registry), or a local container image. 

Reference an image by tag or digest using any of the formats: 
    
    
    Artifact Registry:
      LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE[:tag]
      LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest
    
    
    Container Registry:
      [LOCATION.]gcr.io/PROJECT-ID/REPOSITORY-ID/IMAGE[:tag]
      [LOCATION.]gcr.io/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest
    
    
    Local:
      IMAGE[:tag]

EXAMPLES
     Start a scan of a container image stored in Artifact Registry: 
    
    
    gcloud artifacts docker images scan us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz --remote

Start a scan of a container image stored in the Container Registry, and perform the analysis in Europe: 
    
    
    gcloud artifacts docker images scan eu.gcr.io/my-project/my-repository/my-image:latest --remote --location=europe

Start a scan of a container image stored locally, and perform the analysis in Asia: 
    
    
    gcloud artifacts docker images scan ubuntu:latest --location=asia

POSITIONAL ARGUMENTS
    

`RESOURCE_URI`
     A container image in a Google Cloud registry (Artifact Registry or Container Registry), or a local container image. 
FLAGS
    

`--additional-package-types`=[`ADDITIONAL_PACKAGE_TYPES`,…]
     (DEPRECATED) A comma-separated list of package types to scan in addition to OS packages. 

This flag is deprecated as scanning for all package types is now the default. To skip scanning for specific package types, use --skip-package-types. `ADDITIONAL_PACKAGE_TYPES` must be one of: 

`COMPOSER`
     PHP Composer package. 
`GO`
     Go standard library and third party packages. 
`MAVEN`
     Maven package. 
`NPM`
     NPM package. 
`NUGET`
     NuGet package. 
`PYTHON`
     Python package. 
`RUBYGEMS`
     RubyGems package. 
`RUST`
     Rust package. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`; default="us"
     The API location in which to perform package analysis. Consider choosing a location closest to where you are located. Proximity to the container image does not affect response time. `LOCATION` must be one of: 

`asia`
     Perform analysis in Asia 
`europe`
     Perform analysis in Europe 
`us`
     Perform analysis in the US 
`--remote`
     Whether the container image is located remotely or on your local machine. 
`--skip-package-types`=[`SKIP_PACKAGE_TYPES`,…]
     A comma-separated list of package types to skip when scanning. `SKIP_PACKAGE_TYPES` must be one of: 

`COMPOSER`
     PHP Composer package. 
`GO`
     Go standard library and third party packages. 
`MAVEN`
     Maven package. 
`NPM`
     NPM package. 
`NUGET`
     NuGet package. 
`PYTHON`
     Python package. 
`RUBYGEMS`
     RubyGems package. 
`RUST`
     Rust package. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta artifacts docker images scan](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/images/scan)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
