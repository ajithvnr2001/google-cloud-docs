---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/images/describe/
title: gcloud alpha container images describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:08:24.404346+00:00
---

# gcloud alpha container images describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/images/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container images describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container images describe - lists container analysis data for a given image 
SYNOPSIS
    

`gcloud alpha container images describe` `IMAGE_NAME` [`--metadata-filter`=`METADATA_FILTER`] [`--show-all-metadata`] [`--show-build-details`] [`--show-deployment`] [`--show-image-basis`] [`--show-package-vulnerability`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Lists container analysis data for a valid image. 
EXAMPLES
     Describe the specified image: 
    
    
    gcloud alpha container images describe gcr.io/myproject/myimage@digest
    
    
    Or:
    
    
    gcloud alpha container images describe gcr.io/myproject/myimage:tag

Find the digest for a tag: 
    
    
    gcloud alpha container images describe gcr.io/myproject/myimage:tag --format="value(image_summary.digest)"
    
    
    Or:
    
    
    gcloud alpha container images describe gcr.io/myproject/myimage:tag --format="value(image_summary.fully_qualified_digest)"

See package vulnerabilities found by the Container Analysis API for the specified image: 
    
    
    gcloud alpha container images describe gcr.io/myproject/myimage@digest --show-package-vulnerability

POSITIONAL ARGUMENTS
    

`IMAGE_NAME`
     The fully qualified name(s) of image(s) to describe. The name(s) should be formatted as *.gcr.io/PROJECT_ID/IMAGE_PATH@sha256:DIGEST or *.gcr.io/PROJECT_ID/IMAGE_PATH:TAG. 
FLAGS
    

`--metadata-filter`=`METADATA_FILTER`
     Additional filter to fetch metadata for a given fully qualified image reference. 
`--show-all-metadata`
     Include all metadata in the output. 
`--show-build-details`
     Include build metadata in the output. 
`--show-deployment`
     Include deployment metadata in the output. 
`--show-image-basis`
     Include base image metadata in the output. 
`--show-package-vulnerability`
     Include vulnerability metadata in the output. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container images describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/images/describe)
    
    
    [gcloud beta container images describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/images/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
