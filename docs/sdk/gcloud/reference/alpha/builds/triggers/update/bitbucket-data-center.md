---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/bitbucket-data-center/
title: gcloud alpha builds triggers update bitbucket-data-center \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:15.488402+00:00
---

# gcloud alpha builds triggers update bitbucket-data-center  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/bitbucket-data-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha builds triggers update bitbucket-data-center Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha builds triggers update bitbucket-data-center - updates Bitbucket Data Center trigger used by Cloud Build 
SYNOPSIS
    

`gcloud alpha builds triggers update bitbucket-data-center` (`TRIGGER` : `--region`=`REGION`) (`--trigger-config`=`PATH` | `--description`=`DESCRIPTION` `--ignored-files`=[`GLOB`,…] `--included-files`=[`GLOB`,…] `--repository`=`REPOSITORY` `--[no-]require-approval` `--service-account`=`SERVICE_ACCOUNT` `--branch-pattern`=`REGEX` | `--tag-pattern`=`REGEX` | `--comment-control`=`COMMENT_CONTROL` `--pull-request-pattern`=`REGEX` `--build-config`=`PATH` | `--inline-config`=`PATH` | [`--dockerfile`=`DOCKERFILE` `--dockerfile-image`=`DOCKERFILE_IMAGE` : `--dockerfile-dir`=`DOCKERFILE_DIR`] `--clear-substitutions` | `--remove-substitutions`=[`KEY`,…] | `--update-substitutions`=[`KEY`=`VALUE`,…]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Updates Bitbucket Data Center trigger used by Cloud Build. 
EXAMPLES
     To update the branch pattern of the trigger: 
    
    
    gcloud alpha builds triggers update bitbucket-data-center my-trigger --branch-pattern=".*"

To update the build config of the trigger: 
    
    
    gcloud alpha builds triggers update bitbucket-data-center my-trigger --build-config="cloudbuild.yaml"

To update the substitutions of the trigger: 
    
    
    gcloud alpha builds triggers update bitbucket-data-center my-trigger --update-substitutions=_REPO_NAME=my-repo,_BRANCH_NAME=master

To update the 2nd-gen repository resource of the trigger: 
    
    
    gcloud alpha builds triggers update bitbucket-data-center my-trigger --repository=projects/my-project/locations/us-west1/connections/my-conn/repositories/my-repo

POSITIONAL ARGUMENTS
    

Trigger resource - Build Trigger. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `TRIGGER` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TRIGGER`
     ID of the trigger or fully qualified identifier for the trigger. 

To set the `trigger` attribute: 

  * provide the argument `TRIGGER` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud location for the trigger. 

To set the `region` attribute: 

  * provide the argument `TRIGGER` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `builds/region`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--trigger-config`=`PATH`
     Path to Build Trigger config file (JSON or YAML format). For more details, see <https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.triggers#BuildTrigger>
Or at least one of these can be specified: 

Flag based trigger configuration 
`--description`=`DESCRIPTION`
     Build trigger description. 
`--ignored-files`=[`GLOB`,…]
     Glob filter. Changes only affecting ignored files won't trigger builds. 
`--included-files`=[`GLOB`,…]
     Glob filter. Changes affecting at least one included file will trigger builds. 
`--repository`=`REPOSITORY`
     Repository resource (2nd gen) to use, in the format "projects/*/locations/*/connections/*/repositories/`". `
\--[no-]require-approval``
     Require manual approval for triggered builds. Use \--require-approval` to enable and `\--no-require-approval` to disable. `
\--service-account`=`SERVICE_ACCOUNT``
     The service account used for all user-controlled operations including UpdateBuildTrigger, RunBuildTrigger, CreateBuild, and CancelBuild. If no service account is set, then the standard Cloud Build service account ([PROJECT_NUM]@system.gserviceaccount.com) is used instead. Format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL}`. 
At most one of these can be specified: 

\--branch-pattern`=`REGEX``
     A regular expression specifying which git branches to match. 

This pattern is used as a regular expression search for any incoming pushes. For example, --branch-pattern=foo will match "foo", "foobar", and "barfoo". Events on a branch that does not match will be ignored. 

The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>. 

\--tag-pattern`=`REGEX``
     A regular expression specifying which git tags to match. 

This pattern is used as a regular expression search for any incoming pushes. For example, --tag-pattern=foo will match "foo", "foobar", and "barfoo". Events on a tag that does not match will be ignored. 

The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>. 

Or at least one of these can be specified: 

Pull Request settings 
\--comment-control`=`COMMENT_CONTROL``
     Require a repository collaborator or owner to comment '/gcbrun' on a pull request before running the build. `COMMENT_CONTROL` must be one of: 

COMMENTS_DISABLED``
     Do not require comments on Pull Requests before builds are triggered. 
COMMENTS_ENABLED``
     Enforce that repository owners or collaborators must comment on Pull Requests before builds are triggered. 
COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY``
     Enforce that repository owners or collaborators must comment on external contributors' Pull Requests before builds are triggered. 
\--pull-request-pattern`=`REGEX``
     A regular expression specifying which base git branch to match for pull request events. 

This pattern is used as a regular expression search for the base branch (the branch you are trying to merge into) for pull request updates. For example, \--pull-request-pattern=foo will match "foo", "foobar", and "barfoo". 

The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>. 

At most one of these can be specified: 

\--build-config`=`PATH``
     Path to a YAML or JSON file containing the build configuration in the repository. 

For more details, see: <https://cloud.google.com/cloud-build/docs/build-config>

\--inline-config`=`PATH``
     Local path to a YAML or JSON file containing a build configuration. 
Or at least one of these can be specified: 

Dockerfile build configuration flags 
\--dockerfile`=`DOCKERFILE``
     Path of Dockerfile to use for builds in the repository. 

If specified, a build config will be generated to run docker build using the specified file. 

The filename is relative to the Dockerfile directory. 

This flag argument must be specified if any of the other arguments in this group are specified. 

\--dockerfile-image`=`DOCKERFILE_IMAGE``
     Docker image name to build. 

This flag argument must be specified if any of the other arguments in this group are specified. 

\--dockerfile-dir`=`DOCKERFILE_DIR``
     Location of the directory containing the Dockerfile in the repository. 

The directory will also be used as the Docker build context. 

At most one of these can be specified: 

\--clear-substitutions``
     Clear existing substitutions. 
\--remove-substitutions`=[`KEY`,…]`
     Remove existing substitutions if present. 
\--update-substitutions`=[`KEY`=`VALUE`,…]`
     Update or add to existing substitutions. Substitutions are parameters to be substituted or add in the build specification. 

For example (using some nonsensical substitution keys; all keys must begin with an underscore): 
    
    
    [gcloud builds triggers update](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/update) …
        --update-substitutions _FAVORITE_COLOR=blue,_NUM_CANDIES=10

This will add the provided substitutions to the existing substitutions and results in a build where every occurrence of `${_FAVORITE_COLOR}` in certain fields is replaced by "blue", and similarly for `${_NUM_CANDIES}` and "10". 

Only the following built-in variables can be specified with the `--substitutions` flag: REPO_NAME, BRANCH_NAME, TAG_NAME, REVISION_ID, COMMIT_SHA, SHORT_SHA. 

For more details, see: <https://cloud.google.com/build/docs/build-config-file-schema#substitutions>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud builds triggers update bitbucket-data-center](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center)
    
    
    [gcloud beta builds triggers update bitbucket-data-center](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/triggers/update/bitbucket-data-center)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
