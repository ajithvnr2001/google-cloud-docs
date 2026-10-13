---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/describe/
title: gcloud artifacts docker images describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:08.377765+00:00
---

# gcloud artifacts docker images describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts docker images describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts docker images describe - describe an Artifact Registry container image 
SYNOPSIS
    

`gcloud artifacts docker images describe` `IMAGE` [`--metadata-filter`=`METADATA_FILTER`] [`--show-all-metadata`] [`--show-build-details`] [`--show-deployment`] [`--show-image-basis`] [`--show-package-vulnerability`] [`--show-provenance`] [`--show-sbom-references`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Reference an image by tag or digest using the format: 
    
    
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest

This command can fail for the following reasons: 

  * The repository format is invalid. 
  * The specified image does not exist. 
  * The active account does not have permission to run the command (`roles/artifactregistry.reader`, `roles/containeranalysis.admin` and `roles/serviceusage.serviceUsageViewer`). 


EXAMPLES
     To describe an image digest `abcxyz` under image `busy-box`: 
    
    
    gcloud artifacts docker images describe us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz

To describe an image `busy-box` with tag `my-tag`: 
    
    
    gcloud artifacts docker images describe us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

POSITIONAL ARGUMENTS
    

`IMAGE`
     A container image. 

A valid container image has the format of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE 

A valid container image that can be referenced by tag or digest, has the format of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest 

FLAGS
    

`--metadata-filter`=`METADATA_FILTER`
     Additional filter to fetch metadata for a given qualified image reference. 
`--show-all-metadata`
     Include all metadata in the output. Metadata will be grouped by Grafeas kind, with an additional section for intoto provenance metadata. 
`--show-build-details`
     Include build metadata in the output. 
`--show-deployment`
     Include deployment metadata in the output. 
`--show-image-basis`
     Include base image metadata in the output. 
`--show-package-vulnerability`
     Include vulnerability metadata in the output. 
`--show-provenance`
     Include intoto provenance metadata in the output, in the provenance_summary section. To see all build metadata in the output, use --show-all-metadata or \--show-build-details. 
`--show-sbom-references`
     Include SBOM metadata in the output. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts docker images describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe)
    
    
    [gcloud beta artifacts docker images describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/images/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
