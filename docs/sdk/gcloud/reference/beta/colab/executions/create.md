---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/colab/executions/create/
title: gcloud beta colab executions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:31.322566+00:00
---

# gcloud beta colab executions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/colab/executions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta colab executions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta colab executions create - create an execution 
SYNOPSIS
    

`gcloud beta colab executions create` (`--display-name`=`DISPLAY_NAME` `--gcs-output-uri`=`GCS_OUTPUT_URI` `--notebook-runtime-template`=`NOTEBOOK_RUNTIME_TEMPLATE` (`--direct-content`=`DIRECT_CONTENT` | [`--dataform-repository-name`=`DATAFORM_REPOSITORY_NAME` : `--commit-sha`=`COMMIT_SHA`] | [`--gcs-notebook-uri`=`GCS_NOTEBOOK_URI` : `--generation`=`GENERATION`]) (`--service-account`=`SERVICE_ACCOUNT` | `--user-email`=`USER_EMAIL`) : `--execution-timeout`=`EXECUTION_TIMEOUT`; default="24h") [`--async`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a notebook execution to be used on a Colab Enterprise runtime. 
EXAMPLES
     To create an execution of a notebook file with Cloud Storage URI `gs://my-bucket/my-notebook.ipynb`, with an execution job display name `my-execution`, compute configured from runtime template `my-runtime-template-id`, running with service account `my-service-account@my-project.iam.gserviceaccount.com`, with results uploaded to Cloud Storage bucket `gs://my-bucket/results`, and in region `us-central1` run: 
    
    
    gcloud beta colab executions create --display-name=my-execution --runtime-template=my-runtime-template-id --gcs-notebook-uri=gs://my-bucket/my-notebook.ipynb --service-account=my-service-account@my-project.iam.gserviceaccount.com --gcs-output-uri=gs://my-bucket/results --region=us-central1

REQUIRED FLAGS
    

Configuration of the execution job. 

This must be specified. 

`--display-name`=`DISPLAY_NAME`
     The display name of the execution. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--gcs-output-uri`=`GCS_OUTPUT_URI`
     The Cloud Storage location to upload notebook execution results to. Format: gs://bucket-name. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Notebook runtime template resource - The runtime template specifying the compute configuration for the notebook execution. The runtime template should be in the same region as the execution. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--notebook-runtime-template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--notebook-runtime-template` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 



This must be specified. 

`--notebook-runtime-template`=`NOTEBOOK_RUNTIME_TEMPLATE`
     ID of the notebook runtime template or fully qualified identifier for the notebook runtime template. 

To set the `name` attribute: 

  * provide the argument `--notebook-runtime-template` on the command line. 


`--execution-timeout`=`EXECUTION_TIMEOUT`; default="24h"
     The max running time of the execution job, as a duration. See '$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)' for details on formatting the input duration. 
Source of the notebook to execute. 

Exactly one of these must be specified: 

`--direct-content`=`DIRECT_CONTENT`
     The direct notebook content as IPYNB. This can be a local filepath to an .ipynb file or can be set to `-` to read content from stdin. 
Or at least one of these can be specified: 

The Dataform repository containing the notebook. Any notebook created from the Colab UI is automatically stored in a Dataform repository. The repository name can be found via the Dataform API by listing repositories in the same project and region as the notebook. 
Dataform repository resource - Unique name of the Dataform repository to source input notebook from. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--dataform-repository-name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--dataform-repository-name` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 



This must be specified. 

`--dataform-repository-name`=`DATAFORM_REPOSITORY_NAME`
     ID of the dataform repository or fully qualified identifier for the dataform repository. 

To set the `name` attribute: 

  * provide the argument `--dataform-repository-name` on the command line. 


`--commit-sha`=`COMMIT_SHA`
     The commit SHA to read from the Dataform repository. If unset, the file will be read from HEAD. 
Or at least one of these can be specified: 

The Cloud Storage notebook source. 
`--gcs-notebook-uri`=`GCS_NOTEBOOK_URI`
     The Cloud Storage uri pointing to the notebook. Format: gs://bucket/notebook_file.ipynb 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--generation`=`GENERATION`
     The version of the Cloud Storage object to read. If unset, the current version of the object will be used. 
Identity to run the execution as. 

Exactly one of these must be specified: 

`--service-account`=`SERVICE_ACCOUNT`
     The service account to run the execution as. 
`--user-email`=`USER_EMAIL`
     The user email to run the execution as. This requires the provided runtime template to have end user credentials enabled. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Region resource - Cloud region to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `colab/region` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud colab executions create](https://docs.cloud.google.com/sdk/gcloud/reference/colab/executions/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
