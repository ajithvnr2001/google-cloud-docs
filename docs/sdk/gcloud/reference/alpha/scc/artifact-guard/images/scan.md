---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/artifact-guard/images/scan/
title: gcloud alpha scc artifact-guard images scan \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:10.265037+00:00
---

# gcloud alpha scc artifact-guard images scan  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/artifact-guard/images/scan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc artifact-guard images scan Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc artifact-guard images scan - scan an image with Artifact Guard 
SYNOPSIS
    

`gcloud alpha scc artifact-guard images scan` `RESOURCE_URI` `--parent`=`PARENT` `--scan-type`=`SCAN_TYPE` [`--async`] [`--connector-id`=`CONNECTOR_ID`] [`--remote`] [[`--cloud-build-id`=`CLOUD_BUILD_ID` `--cloud-build-project-id`=`CLOUD_BUILD_PROJECT_ID` : `--cloud-build-trigger-id`=`CLOUD_BUILD_TRIGGER_ID`] | [`--github-run-id`=`GITHUB_RUN_ID` : `--github-repository`=`GITHUB_REPOSITORY` `--github-workflow`=`GITHUB_WORKFLOW`] | `--jenkins-build-id`=`JENKINS_BUILD_ID` `--jenkins-build-tag`=`JENKINS_BUILD_TAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Scan a container image with Artifact Guard. 
EXAMPLES
     To scan an image: 
    
    
    gcloud alpha scc artifact-guard images scan my-image:tag --parent=organizations/123/locations/global --scan-type=pipeline --connector-id=my-connector --jenkins-build-tag=t --jenkins-build-id=i

POSITIONAL ARGUMENTS
    

`RESOURCE_URI`
     URI of the image to scan (e.g., `my-image:tag` or `my-image@digest`). 
REQUIRED FLAGS
    

`--parent`=`PARENT`
     Parent resource for artifact guard, e.g., `organizations/123/locations/global`. 
`--scan-type`=`SCAN_TYPE`
     Type of scan to perform. `SCAN_TYPE` must be (only one value is supported): `pipeline`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--connector-id`=`CONNECTOR_ID`
     The ID of the pipeline connector. Required for pipeline scans. 
`--remote`
     If true, treat resource_uri as a remote image. If false, treats it as a local tarball or daemon image. 
CI/CD pipeline context. Required for pipeline scans. 

At most one of these can be specified: 

Google Cloud Build context flags. 
`--cloud-build-id`=`CLOUD_BUILD_ID`
     Cloud Build ID. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--cloud-build-project-id`=`CLOUD_BUILD_PROJECT_ID`
     Cloud Build project ID. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--cloud-build-trigger-id`=`CLOUD_BUILD_TRIGGER_ID`
     Cloud Build trigger ID. 
GitHub Actions workflow context flags. 
`--github-run-id`=`GITHUB_RUN_ID`
     GitHub run ID. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--github-repository`=`GITHUB_REPOSITORY`
     GitHub repository. 
`--github-workflow`=`GITHUB_WORKFLOW`
     GitHub workflow. 
Jenkins CI Pipeline context flags. 
`--jenkins-build-id`=`JENKINS_BUILD_ID`
     Jenkins build ID. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--jenkins-build-tag`=`JENKINS_BUILD_TAG`
     Jenkins build tag. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
