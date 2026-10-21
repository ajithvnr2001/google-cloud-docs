---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/manual/
title: gcloud alpha builds triggers create manual \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:13.877966+00:00
---

# gcloud alpha builds triggers create manual  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/manual/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha builds triggers create manual Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha builds triggers create manual - create a build trigger with a manual trigger event 
SYNOPSIS
    

`gcloud alpha builds triggers create manual` (`--trigger-config`=`PATH` | [(`--build-config`=`PATH` | `--inline-config`=`PATH` | [`--dockerfile`=`DOCKERFILE` : `--dockerfile-dir`=`DOCKERFILE_DIR`; default="/" `--dockerfile-image`=`DOCKERFILE_IMAGE`]) : `--description`=`DESCRIPTION` `--name`=`NAME` `--region`=`REGION` `--[no-]require-approval` `--service-account`=`SERVICE_ACCOUNT` `--substitutions`=[`KEY`=`VALUE`,…] `--branch`=`BRANCH` | `--tag`=`TAG` `--repository`=`REPOSITORY` | [`--repo`=`REPO` `--repo-type`=`REPO_TYPE` : `--github-enterprise-config`=`GITHUB_ENTERPRISE_CONFIG`]]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a build trigger with a manual trigger event. 
EXAMPLES
     To create a manual trigger that builds off branch `my-branch` in a GitHub repository named `my-repo`: 
    
    
    gcloud alpha builds triggers create manual --name=my-manual-trigger --build-config=cloudbuild.yaml --repo=https://www.github.com/owner/repo --repo-type=GITHUB --branch=my-branch

To create a manual trigger that builds off branch `my-branch` in a 2nd-gen GitHub repository resource: 
    
    
    gcloud alpha builds triggers create manual --name=my-manual-trigger --build-config=cloudbuild.yaml --repository=projects/my-proj/locations/us-west1/connections/my-conn/repositories/my-repo --branch=my-branch

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--trigger-config`=`PATH`
     Path to Build Trigger config file (JSON or YAML format). For more details, see <https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.triggers#BuildTrigger>
Or at least one of these can be specified: 

Flag based trigger configuration 
`--description`=`DESCRIPTION`
     Build trigger description. 
`--name`=`NAME`
     Build trigger name. 
`--region`=`REGION`
     The region of the Cloud Build Service to use. Must be set to a supported region name (e.g. `us-central1`). If unset, `builds/region`, which is the default region to use when working with Cloud Build resources, is used. If builds/region is unset, region is set to `global`. Note: Region must be specified in 2nd gen repo; `global` is not supported. 
`--[no-]require-approval`
     Require manual approval for triggered builds. Use `--require-approval` to enable and `--no-require-approval` to disable. 
`--service-account`=`SERVICE_ACCOUNT`
     The service account used for all user-controlled operations including UpdateBuildTrigger, RunBuildTrigger, CreateBuild, and CancelBuild. If no service account is set, then the standard Cloud Build service account ([PROJECT_NUM]@system.gserviceaccount.com) is used instead. Format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL}`. 
`--substitutions`=[`KEY`=`VALUE`,…]
     Parameters to be substituted in the build specification. For example: 
    
    
    gcloud alpha builds triggers create manual … --substitutions _FAVORITE_COLOR=blue,_NUM_CANDIES=10

This will result in a build where every occurrence of `${_FAVORITE_COLOR}` in certain fields is replaced by "blue", and similarly for `${_NUM_CANDIES}` and "10". 

Substitutions can be applied to user-defined variables (starting with an underscore) and to the following built-in variables: REPO_NAME, BRANCH_NAME, TAG_NAME, REVISION_ID, COMMIT_SHA, SHORT_SHA. 

For more details, see: <https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values>

Exactly one of these must be specified: 

`--build-config`=`PATH`
     Path to a YAML or JSON file containing the build configuration in the repository. 

For more details, see: <https://cloud.google.com/cloud-build/docs/build-config>

`--inline-config`=`PATH`
     Local path to a YAML or JSON file containing a build configuration. 
Or at least one of these can be specified: 

Dockerfile build configuration flags 
`--dockerfile`=`DOCKERFILE`
     Path of Dockerfile to use for builds in the repository. 

If specified, a build config will be generated to run docker build using the specified file. 

The filename is relative to the Dockerfile directory. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--dockerfile-dir`=`DOCKERFILE_DIR`; default="/"
     Location of the directory containing the Dockerfile in the repository. 

The directory will also be used as the Docker build context. 

`--dockerfile-image`=`DOCKERFILE_IMAGE`
     Docker image name to build. 

If not specified, gcr.io/PROJECT/github.com/REPO_OWNER/REPO_NAME:$COMMIT_SHA will be used. 

Use a build configuration (cloudbuild.yaml) file for building multiple images in a single trigger. 

Flags for repository and branch information 
At most one of these can be specified: 

`--branch`=`BRANCH`
     Branch to build. 
`--tag`=`TAG`
     Tag to build. 
Flags for repository information 

At most one of these can be specified: 

`--repository`=`REPOSITORY`
     Repository resource (2nd gen) to use, in the format "projects/*/locations/*/connections/*/repositories/`". `
Or at least one of these can be specified: 

1st-gen repository settings. 
\--repo`=`REPO``
     URI of the repository (1st gen). Currently only HTTP URIs for GitHub and Cloud Source Repositories are supported. 

This flag argument must be specified if any of the other arguments in this group are specified. 

\--repo-type`=`REPO_TYPE``
     Type of the repository (1st gen). Currently only GitHub and Cloud Source Repository types are supported. 

This flag argument must be specified if any of the other arguments in this group are specified. 

\--github-enterprise-config`=`GITHUB_ENTERPRISE_CONFIG``
     The resource name of the GitHub Enterprise config that should be applied to this source (1st gen). Format: projects/{project}/locations/{location}/githubEnterpriseConfigs/{id} or projects/{project}/githubEnterpriseConfigs/{id} 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud builds triggers create manual](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual)
    
    
    [gcloud beta builds triggers create manual](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/triggers/create/manual)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
