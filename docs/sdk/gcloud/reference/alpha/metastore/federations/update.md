---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/federations/update/
title: gcloud alpha metastore federations update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:24:14.485896+00:00
---

# gcloud alpha metastore federations update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/federations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha metastore federations update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha metastore federations update - update a Dataproc Metastore federation 
SYNOPSIS
    

`gcloud alpha metastore federations update` (`FEDERATION` : `--location`=`LOCATION`) (`--update-backends`=`RANK`=`BACKEND` `--clear-backends` | `--remove-backends`=`RANK`) [`--async`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the metadata and/or configuration parameters of a Dataproc Metastore federation. 

If run asynchronously with `--async`, exits after printing one operation name that can be used to poll the status of the update via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To update a Dataproc Metastore federation with the name `my-metastore-federation` in location `us-central` with two backends `dpms1` and `dpms2`, run: 
    
    
    gcloud alpha metastore federations update my-metastore-federation --location=us-central1 --update-backends=1=dpms:dpms1,2=dpms:projects/my-project/locations/us-central1/services/dpms2

POSITIONAL ARGUMENTS
    

Federation resource - Arguments and flags that specify the Dataproc Metastore federation you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `federation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FEDERATION`
     ID of the federation or fully qualified identifier for the federation. 

To set the `federation` attribute: 

  * provide the argument `federation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataproc Metastore service. 

If not specified, will use `default` metastore/location. To set the `location` attribute: 

  * provide the argument `federation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `metastore/location`. 


REQUIRED FLAGS
    

Update the backend metastores by passing key-value pairs in through the flags. At least one of these must be specified: 

`--update-backends`=`RANK`=`BACKEND`
     Comma-separated list of metastore backends specified as a list of `RANK=BACKEND` pairs. For example: `1=dpms:dpms1,2=dpms:projects/my-project/locations/us-central1/services/dpms2`. `RANK` represents the rank of the backend metastore and is used to resolve database name collisions. `BACKEND` is specified as `METASTORE_TYPE:METASTORE_NAME` where `METASTORE_TYPE` is the type of backend metastore and `METASTORE_NAME` is the relative resource name of the metastore. If only the name of the metastore is specified (e.g. `dpms1`), project and location will be inferred from the project and location used to create the federation. 
At most one of these can be specified: 

`--clear-backends`
     Clear existing metastore backends. `--clear-backends` must be used with `--update-backends`. 
`--remove-backends`=`RANK`
     Comma-separated list of metastore backend keys to remove with the form `RANK1,RANK2`. The Key represents the rank of the backend metastore and is used to resolve database name collisions. If a `RANK` does not exist then it is sliently ignored. If `--update-backends` is also specified, then `--remove-backends` is applied first. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud alpha metastore federations update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud alpha metastore federations update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud metastore federations update](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/federations/update)
    
    
    [gcloud beta metastore federations update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/federations/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
