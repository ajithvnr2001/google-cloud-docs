---
url: https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/snapshots/load/
title: gcloud composer environments snapshots load \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:37.845984+00:00
---

# gcloud composer environments snapshots load  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/snapshots/load/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud composer environments snapshots load Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud composer environments snapshots load - load a snapshot into the environment 
SYNOPSIS
    

`gcloud composer environments snapshots load` (`ENVIRONMENT` : `--location`=`LOCATION`) `--snapshot-path`=`SNAPSHOT_PATH` [`--async`] [`--skip-airflow-overrides-setting`] [`--skip-environment-variables-setting`] [`--skip-gcs-data-copying`] [`--skip-pypi-packages-installation`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Load a snapshot into the environment. 
EXAMPLES
     To load a snapshot into the environment named env-1, run: 
    
    
    gcloud composer environments snapshots load env-1 --snapshot-path=gs://my-bucket/path-to-the-specific-snapshot

POSITIONAL ARGUMENTS
    

Environment resource - The environment where to load a snapshot. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `environment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENVIRONMENT`
     ID of the environment or fully qualified identifier for the environment. 

To set the `environment` attribute: 

  * provide the argument `environment` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Region where Composer environment runs or in which to create the environment. 

To set the `location` attribute: 

  * provide the argument `environment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `composer/location`. 


REQUIRED FLAGS
    

`--snapshot-path`=`SNAPSHOT_PATH`
     The Cloud Storage path to load the snapshot from. It must start with prefix gs:// and one needs to specify a single snapshot that should be loaded. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--skip-airflow-overrides-setting`
     When specified, skips setting Airflow overrides from the snapshot. 
`--skip-environment-variables-setting`
     When specified, skips setting environment variables from the snapshot. 
`--skip-gcs-data-copying`
     When specified, skips copying dags, plugins and data folders from the snapshot. 
`--skip-pypi-packages-installation`
     When specified, skips the installation of custom PyPI packages from the snapshot. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha composer environments snapshots load](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load)
    
    
    [gcloud beta composer environments snapshots load](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/snapshots/load)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
