---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate/
title: gcloud artifacts docker upgrade migrate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:09.139239+00:00
---

# gcloud artifacts docker upgrade migrate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts docker upgrade migrate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts docker upgrade migrate - migrate projects from Container Registry to Artifact Registry 
SYNOPSIS
    

`gcloud artifacts docker upgrade migrate` [`--canary-reads`=`PERCENT`] [`--copy-only`] [`--from-gcr`=`GCR_HOST`/`PROJECT_ID`] [`--input-iam-policy-dir`=`DIRECTORY`] [`--last-uploaded-versions`=`N`] [`--max-threads`=`MAX_THREADS`; default=8] [`--output-iam-policy-dir`=`DIRECTORY`] [`--pkg-dev-location`=`PKG_DEV_LOCATION`] [`--projects`=`PROJECTS`] [`--recent-images`=`NUM_DAYS`] [`--skip-iam-update`] [`--skip-pre-copy`] [`--to-pkg-dev`=`PROJECT_ID`/`REPOSITORY_ID`] [`--no-use-analyze-iam`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Migrate projects from Container Registry to Artifact Registry 
EXAMPLES
     To migrate a project `my-project` using gcr.io repositories: 
    
    
    gcloud artifacts docker upgrade migrate --projects=my-project

To migrate several projects using gcr.io repositories: 
    
    
    gcloud artifacts docker upgrade migrate --projects=my-project1,my-project2,my-project3

To migrate a project using pkg.dev repositories: 
    
    
    gcloud artifacts docker upgrade migrate --from-gcr=gcr.io/project1 --to-pkg-dev=project2/repo_name

FLAGS
    

`--canary-reads`=`PERCENT`
     Send only a percent of reads to Artifact Registry. The rest of reads and all writes are sent to Container Registry. 
`--copy-only`
     Only perform image copying 
`--from-gcr`=`GCR_HOST`/`PROJECT_ID`
     Container Registry host + project to copy from. This flag is only used when migrating to pkg.dev repos. Example: gcr.io/my-project 
`--input-iam-policy-dir`=`DIRECTORY`
     During the IAM update step, the tool applies all iam policies in the given directory. 
`--last-uploaded-versions`=`N`
     Only copy the N most recently uploaded versions of each image. More than N images may be copied if new images are uploaded during migration. 
`--max-threads`=`MAX_THREADS`; default=8
     Max number of images to copy simultaneously. Consider quota usage when increasing this 
`--output-iam-policy-dir`=`DIRECTORY`
     Outputs Artifact Registry-equivalent bindings to this directory during IAM update step and then exits the tool. After any neccesary modifications are made, the tool can be rerun with --input-iam-policy-dir to continue migration with the generated bindings. 
`--pkg-dev-location`=`PKG_DEV_LOCATION`
     The location of the pkg-dev repository you are migrating to. If not specified, migration is always done to the same multi-region as GCR. Setting this flag can cause cross-regional copying and lead to billing charges. 
`--projects`=`PROJECTS`
     Comma seperated list of Container Registry projects to migrate to Artifact Registry gcr.io repositories. 
`--recent-images`=`NUM_DAYS`
     Only copy images pulled or pushed in the last NUM_DAYS days. NUM_DAYS must be between 30 and 90 inclusive. 
`--skip-iam-update`
     Migrate without changing iam-policy. Users without Artifact Registry permissions will not have access to migrated images. 
`--skip-pre-copy`
     Skip the initial copy of recent images before enabling redirection. 
`--to-pkg-dev`=`PROJECT_ID`/`REPOSITORY_ID`
     Artifact Registry pkg.dev project ID and repository ID to copy to. Example: my-project/my-repo 
`--use-analyze-iam`
     Use analyzeIAMPolicy to get IAM bindings. If false, tooling iterates through IAM bindings itself, which is slower, but doesn't require anlayzeIAMPolicy quota. Enabled by default, use `--no-use-analyze-iam` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `artifactregistry/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/artifacts/docs/>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
