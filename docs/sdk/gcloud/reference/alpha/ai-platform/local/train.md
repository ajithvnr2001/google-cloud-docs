---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/train/
title: gcloud alpha ai-platform local train \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:49:12.216953+00:00
---

# gcloud alpha ai-platform local train  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/train/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai-platform local train Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai-platform local train - run an AI Platform training job locally 
SYNOPSIS
    

`gcloud alpha ai-platform local train` `--module-name`=`MODULE_NAME` [`--distributed`] [`--evaluator-count`=`EVALUATOR_COUNT`] [`--job-dir`=`JOB_DIR`] [`--package-path`=`PACKAGE_PATH`] [`--parameter-server-count`=`PARAMETER_SERVER_COUNT`] [`--start-port`=`START_PORT`; default=27182] [`--worker-count`=`WORKER_COUNT`] [`GCLOUD_WIDE_FLAG …`] [-- `USER_ARGS` …]
DESCRIPTION
     `(ALPHA)` This command runs the specified module in an environment similar to that of a live AI Platform Training Job. 

This is especially useful in the case of testing distributed models, as it allows you to validate that you are properly interacting with the AI Platform cluster configuration. If your model expects a specific number of parameter servers or workers (i.e. you expect to use the CUSTOM machine type), use the \--parameter-server-count and --worker-count flags to further specify the desired cluster configuration, just as you would in your cloud training job configuration: 
    
    
    gcloud alpha ai-platform local train --module-name trainer.task --package-path /path/to/my/code/trainer --distributed --parameter-server-count 4 --worker-count 8

Unlike submitting a training job, the --package-path parameter can be omitted, and will use your current working directory. 

AI Platform Training sets a TF_CONFIG environment variable on each VM in your training job. You can use TF_CONFIG to access the cluster description and the task description for each VM. 

Learn more about TF_CONFIG: <https://cloud.google.com/ai-platform/training/docs/distributed-training-details>. 

POSITIONAL ARGUMENTS
    

[-- `USER_ARGS` …]
     Additional user arguments to be forwarded to user code. Any relative paths will be relative to the `parent` directory of `--package-path`. The '--' argument must be specified between gcloud specific args on the left and USER_ARGS on the right. 
REQUIRED FLAGS
    

`--module-name`=`MODULE_NAME`
     Name of the module to run. 
OPTIONAL FLAGS
    

`--distributed`
     Runs the provided code in distributed mode by providing cluster configurations as environment variables to subprocesses 
`--evaluator-count`=`EVALUATOR_COUNT`
     Number of evaluators with which to run. Ignored if --distributed is not specified. Default: 0 
`--job-dir`=`JOB_DIR`
     Cloud Storage path or local_directory in which to store training outputs and other data needed for training. 

This path will be passed to your TensorFlow program as the `--job-dir` command-line arg. The benefit of specifying this field is that AI Platform will validate the path for use in training. However, note that your training program will need to parse the provided `--job-dir` argument. 

`--package-path`=`PACKAGE_PATH`
     Path to a Python package to build. This should point to a `local` directory containing the Python source for the job. It will be built using `setuptools` (which must be installed) using its `parent` directory as context. If the parent directory contains a `setup.py` file, the build will use that; otherwise, it will use a simple built-in one. 
`--parameter-server-count`=`PARAMETER_SERVER_COUNT`
     Number of parameter servers with which to run. Ignored if --distributed is not specified. Default: 2 
`--start-port`=`START_PORT`; default=27182
     Start of the range of ports reserved by the local cluster. This command will use a contiguous block of ports equal to parameter-server-count + worker-count + 1. 

If --distributed is not specified, this flag is ignored. 

`--worker-count`=`WORKER_COUNT`
     Number of workers with which to run. Ignored if --distributed is not specified. Default: 2 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ai-platform local train](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/local/train)
    
    
    [gcloud beta ai-platform local train](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/local/train)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
