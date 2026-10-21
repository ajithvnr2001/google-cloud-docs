---
url: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/federations/create/
title: gcloud metastore federations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:38:21.232395+00:00
---

# gcloud metastore federations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/federations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud metastore federations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud metastore federations create - create a Dataproc Metastore federation 
SYNOPSIS
    

`gcloud metastore federations create` (`FEDERATION` : `--location`=`LOCATION`) `--backends`=`RANK`=`BACKEND` [`--async`] [`--hive-metastore-version`=`HIVE_METASTORE_VERSION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--tags`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Dataproc Metastore federation with the given name and configurations. 

If run asynchronously with `--async`, exits after printing one operation name that can be used to poll the status of the creation via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To create a Dataproc Metastore federation with the name `my-metastore-federation` in location `us-central` with two backends `dpms1` and `dpms2`, run: 
    
    
    gcloud metastore federations create my-metastore-federation --location=us-central1 --backends=1=dpms:dpms1,2=dpms:projects/my-project/locations/us-central1/services/dpms2

POSITIONAL ARGUMENTS
    

Federation resource - Arguments and flags that specify the Dataproc Metastore federation you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--backends`=`RANK`=`BACKEND`
     Backends from which the federation service serves metadata at query time. The backends are specified as a comma-separated list of `RANK=BACKEND` pairs. For example: `1=dpms:dpms1,2=dpms:projects/my-project/locations/us-central1/services/dpms2`. `RANK` represents the rank of the backend metastore and is used to resolve database name collisions. `BACKEND` is specified as `METASTORE_TYPE:METASTORE_NAME` where `METASTORE_TYPE` is the type of backend metastore and `METASTORE_NAME` is the relative resource name of the metastore. If only the name of the metastore is specified (e.g. `dpms1`), project and location will be inferred from the project and location used to create the federation. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--hive-metastore-version`=`HIVE_METASTORE_VERSION`
     Hive metastore schema version of the Metastore federation. `HIVE_METASTORE_VERSION` must be one of: `2.3.6`, `3.1.2`. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--tags`=[`KEY`=`VALUE`,…]
     List of tag KEY=VALUE pairs to add. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha metastore federations create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/federations/create)
    
    
    [gcloud beta metastore federations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/federations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
