---
url: https://docs.cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate/
title: gcloud notebooks runtimes migrate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:44.661834+00:00
---

# gcloud notebooks runtimes migrate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud notebooks runtimes migrate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud notebooks runtimes migrate - request for migrating runtimes 
SYNOPSIS
    

`gcloud notebooks runtimes migrate` (`RUNTIME` : `--location`=`LOCATION`) [`--async`] [`--post-startup-script-option`=`POST_STARTUP_SCRIPT_OPTION`; default=`"POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED"`] [`--service-account`=`SERVICE_ACCOUNT`] [`--network`=`NETWORK` [`--subnet`=`SUBNET` : `--subnet-region`=`SUBNET_REGION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Request for migrating notebook runtimes. 
EXAMPLES
     To migrate a runtime, run: 
    
    
    gcloud notebooks runtimes migrate example-runtime --location=us-central1

To migrate a runtime with a new custom network, run: 
    
    
    gcloud notebooks runtimes migrate example-runtime --location=us-central1 --network=projects/example-project/global/networks/example-network --subnet=projects/example-project/regions/us-central1/subnetworks/example-subnetwork

To migrate a runtime and reuse the post-startup script, run: 
    
    
    gcloud notebooks runtimes migrate example-runtime --location=us-central1 --post-startup-script-option=POST_STARTUP_SCRIPT_OPTION_RERUN

POSITIONAL ARGUMENTS
    

Runtime resource - User-defined unique name of this runtime. The runtime name must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `runtime` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RUNTIME`
     ID of the runtime or fully qualified identifier for the runtime. 

To set the `runtime` attribute: 

  * provide the argument `runtime` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location of this runtime <https://cloud.google.com/compute/docs/regions-zones/#locations>. 

To set the `location` attribute: 

  * provide the argument `runtime` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `notebooks/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--post-startup-script-option`=`POST_STARTUP_SCRIPT_OPTION`; default=`"POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED"`
     Specifies the behavior of post startup script during migration. `POST_STARTUP_SCRIPT_OPTION` must be one of: `POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED`, `POST_STARTUP_SCRIPT_OPTION_SKIP`, `POST_STARTUP_SCRIPT_OPTION_RERUN`. 
`--service-account`=`SERVICE_ACCOUNT`
     The service account to be included in the Compute Engine instance of the new Workbench Instance when the Runtime uses single user only mode for permission. If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. When the Runtime uses service account mode for permission, it will reuse the same service account, and this field must be empty. 
Network configs. 
Network resource - The name of the VPC that this instance is in. Format: projects/`{project_id}`/global/networks/`{network_id}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--network` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--network`=`NETWORK`
     ID of the network or fully qualified identifier for the network. 

To set the `network` attribute: 

  * provide the argument `--network` on the command line. 


Subnetwork resource - The name of the subnet that this instance is in. Format: projects/`{project_id}`/regions/`{region}`/subnetworks/`{subnetwork_id}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--subnet` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--subnet`=`SUBNET`
     ID of the subnetwork or fully qualified identifier for the subnetwork. 

To set the `subnet` attribute: 

  * provide the argument `--subnet` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--subnet-region`=`SUBNET_REGION`
     Google Cloud region of this subnetwork <https://cloud.google.com/compute/docs/regions-zones/#locations>. 

To set the `subnet-region` attribute: 

  * provide the argument `--subnet` on the command line with a fully specified name; 
  * provide the argument `--subnet-region` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
