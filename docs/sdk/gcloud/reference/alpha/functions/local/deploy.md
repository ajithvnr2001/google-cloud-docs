---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/local/deploy/
title: gcloud alpha functions local deploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:39.183136+00:00
---

# gcloud alpha functions local deploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/local/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha functions local deploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha functions local deploy - deploy a Google Cloud Function locally 
SYNOPSIS
    

`gcloud alpha functions local deploy` `NAME` [`--builder`=`BUILDER`] [`--entry-point`=`ENTRY_POINT`] [`--ignore-file`=`IGNORE_FILE`] [`--port`=`PORT`; default=8080] [`--runtime`=`RUNTIME`] [`--source`=`SOURCE`] [`--build-env-vars-file`=`FILE_PATH` | `--clear-build-env-vars` | `--set-build-env-vars`=[`KEY`=`VALUE`,…] | `--remove-build-env-vars`=[`KEY`,…] `--update-build-env-vars`=[`KEY`=`VALUE`,…]] [`--clear-env-vars` | `--env-vars-file`=`FILE_PATH` | `--set-env-vars`=[`KEY`=`VALUE`,…] | `--remove-env-vars`=[`KEY`,…] `--update-env-vars`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha functions local deploy` Deploy a Google Cloud Function locally. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the locally deployed Google Cloud function. 
FLAGS
    

`--builder`=`BUILDER`
     Name of the builder to use for pack, e.g. `gcr.io/serverless-runtimes/google-22-full/builder/go`. 
`--entry-point`=`ENTRY_POINT`
     Name of a Google Cloud Function (as defined in source code) that will be executed. Defaults to the resource name suffix (ID of the function), if not specified. 
`--ignore-file`=`IGNORE_FILE`
     Override the .gcloudignore file in the source directory and use the specified file instead. By default, the source directory is your current directory. Note that it could be changed by the --source flag, in which case your .gcloudignore file will be searched in the overridden directory. For example, `--ignore-file=.mygcloudignore` combined with `--source=./mydir` would point to `./mydir/.mygcloudignore`
`--port`=`PORT`; default=8080
     Port for the deployment to run on. The default port is 8080 for new local deployments. 
`--runtime`=`RUNTIME`
     Runtime in which to run the function. 

Required when deploying a new function; optional when updating an existing function. 

For a list of available runtimes, run `[gcloud functions runtimes list](https://docs.cloud.google.com/sdk/gcloud/reference/functions/runtimes/list)`. 

`--source`=`SOURCE`
     Location of source code to deploy. 

Location of the source can be one of the following three options: 

  * Source code in Google Cloud Storage (must be a `.zip` archive), 
  * Reference to source repository or, 
  * Local filesystem path (root directory of function source). 



Note that, depending on your runtime type, Cloud Functions will look for files with specific names for deployable functions. For Node.js, these filenames are `index.js` or `function.js`. For Python, this is `main.py`. 

If you do not specify the `--source` flag: 

  * The current directory will be used for new function deployments. 
  * If the function was previously deployed using a local filesystem path, then the function's source code will be updated using the current directory. 
  * If the function was previously deployed using a Google Cloud Storage location or a source repository, then the function's source code will not be updated. 



The value of the flag will be interpreted as a Cloud Storage location, if it starts with `gs://`. 

The value will be interpreted as a reference to a source repository, if it starts with `https://`. 

Otherwise, it will be interpreted as the local filesystem path. When deploying source from the local filesystem, this command skips files specified in the `.gcloudignore` file (see `[gcloud topic gcloudignore](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore)` for more information). If the `.gcloudignore` file doesn't exist, the command will try to create it. 

The minimal source repository URL is: `https://source.developers.google.com/projects/${PROJECT}/repos/${REPO}`

By using the URL above, sources from the root directory of the repository on the revision tagged `master` will be used. 

If you want to deploy from a revision different from `master`, append one of the following three sources to the URL: 

  * `/revisions/${REVISION}`, 
  * `/moveable-aliases/${MOVEABLE_ALIAS}`, 
  * `/fixed-aliases/${FIXED_ALIAS}`. 



If you'd like to deploy sources from a directory different from the root, you must specify a revision, a moveable alias, or a fixed alias, as above, and append `/paths/${PATH_TO_SOURCES_DIRECTORY}` to the URL. 

Overall, the URL should match the following regular expression: 
    
    
    ^[https://source\.developers\.google\.com/projects/](https://source\\.developers\\.google\\.com/projects/)
    (?<accountId>[^/]+)/repos/(?<repoName>[^/]+)
    (((/revisions/(?<commit>[^/]+))|(/moveable-aliases/(?<branch>[^/]+))|
    (/fixed-aliases/(?<tag>[^/]+)))(/paths/(?<path>.*))?)?$

An example of a validly formatted source repository URL is: 
    
    
    <https://source.developers.google.com/projects/123456789/repos/testrepo/>
    moveable-aliases/alternate-branch/paths/path-to=source

At most one of these can be specified: 

`--build-env-vars-file`=`FILE_PATH`
     Path to a local YAML file with definitions for all build environment variables. All existing build environment variables will be removed before the new build environment variables are added. 
`--clear-build-env-vars`
     Remove all build environment variables. 
`--set-build-env-vars`=[`KEY`=`VALUE`,…]
     List of key-value pairs to set as build environment variables. All existing build environment variables will be removed first. 
Or at least one of these can be specified: 

Only --update-build-env-vars and --remove-build-env-vars can be used together. If both are specified, --remove-build-env-vars will be applied first. 
`--remove-build-env-vars`=[`KEY`,…]
     List of build environment variables to be removed. 
`--update-build-env-vars`=[`KEY`=`VALUE`,…]
     List of key-value pairs to set as build environment variables. 
At most one of these can be specified: 

`--clear-env-vars`
     Remove all environment variables. 
`--env-vars-file`=`FILE_PATH`
     Path to a local YAML file with definitions for all environment variables. All existing environment variables will be removed before the new environment variables are added. 
`--set-env-vars`=[`KEY`=`VALUE`,…]
     List of key-value pairs to set as environment variables. All existing environment variables will be removed first. 
Or at least one of these can be specified: 

Only --update-env-vars and --remove-env-vars can be used together. If both are specified, --remove-env-vars will be applied first. 
`--remove-env-vars`=[`KEY`,…]
     List of environment variables to be removed. 
`--update-env-vars`=[`KEY`=`VALUE`,…]
     List of key-value pairs to set as environment variables. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
