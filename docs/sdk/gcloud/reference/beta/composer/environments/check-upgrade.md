---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/check-upgrade/
title: gcloud beta composer environments check-upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:13:01.571528+00:00
---

# gcloud beta composer environments check-upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/check-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta composer environments check-upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta composer environments check-upgrade - check that upgrading a Cloud Composer environment does not result in PyPI module conflicts 
SYNOPSIS
    

`gcloud beta composer environments check-upgrade` (`ENVIRONMENT` : `--location`=`LOCATION`) [`--async`] [`--airflow-version`=`AIRFLOW_VERSION` | `--image-version`=`IMAGE_VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Check that upgrading a Cloud Composer environment does not result in PyPI module conflicts. 
EXAMPLES
     To check that upgrading to the 'composer-1.16.5-airflow-1.10.15' image
    
    
    in a Cloud Composer environment named 'env-1' does not cause
    PyPI package conflicts,
    run:
    
    
    gcloud beta composer environments check-upgrade env-1 --image-version=composer-1.16.5-airflow-1.10.15

POSITIONAL ARGUMENTS
    

Environment resource - The environment to check upgrade for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Group of arguments for performing in-place environment upgrades. 

At most one of these can be specified: 

`--airflow-version`=`AIRFLOW_VERSION`
     Upgrade the environment to a later Apache Airflow version in-place. 

Must be of the form `X[.Y[.Z]]`, where `[]` denotes optional fragments. Examples: `2`, `2.3`, `2.3.4`. 

The Apache Airflow version is a semantic version or an alias in the form of major or major.minor version numbers, resolved to the latest matching Apache Airflow version supported in the current Cloud Composer version. The resolved version is stored in the upgraded environment. 

`--image-version`=`IMAGE_VERSION`
     Upgrade the environment to a later version in-place. 

The image version encapsulates the versions of both Cloud Composer and Apache Airflow. Must be of the form `composer-A[.B.C[-D.E]]-airflow-X[.Y[.Z]]`, where `[]` denotes optional fragments. 

Examples: `composer-2-airflow-2`, `composer-2-airflow-2.2`, `composer-2.1.2-airflow-2.3.4`. 

The Cloud Composer portion of the image version is a semantic version or an alias in the form of major version number or `latest`, resolved to the current Cloud Composer version. The Apache Airflow portion of the image version is a semantic version or an alias in the form of major or major.minor version numbers, resolved to the latest matching Apache Airflow version supported in the given Cloud Composer version. The resolved versions are stored in the upgraded environment. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud composer environments check-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/check-upgrade)
    
    
    [gcloud alpha composer environments check-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/check-upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
