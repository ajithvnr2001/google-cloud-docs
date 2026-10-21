---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update/
title: gcloud vmware private-connections update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:27:57.315279+00:00
---

# gcloud vmware private-connections update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware private-connections update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware private-connections update - update a Google Cloud Private Connection 
SYNOPSIS
    

`gcloud vmware private-connections update` (`PRIVATE_CONNECTION` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--routing-mode`=`ROUTING_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Updates a VMware Engine private connection. Only description and routing-mode can be updated. 
EXAMPLES
     To update a private connection named `my-private-connection` in project `my-project` and region `us-west1` by changing its description to `Updated description for the private connection` and routing-mode to `GLOBAL`, run: 
    
    
    gcloud vmware private-connections update my-private-connection --location=us-west1 --project=my-project --description="Updated description for the private connection" --routing-mode=GLOBAL

Or: 
    
    
    gcloud vmware private-connections update my-private-connection --description="Updated description for the private connection" --routing-mode=GLOBAL

In the second example, the project and location are taken from gcloud properties core/project and compute/regions, respectively. 

POSITIONAL ARGUMENTS
    

Private Connection resource - private_connection. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `private_connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PRIVATE_CONNECTION`
     ID of the Private Connection or fully qualified identifier for the Private Connection. 

To set the `private-connection` attribute: 

  * provide the argument `private_connection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The resource name of the location. 

To set the `location` attribute: 

  * provide the argument `private_connection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Updated description for this Private Connection. 
`--routing-mode`=`ROUTING_MODE`
     Updated routing mode for this Private Connection. `ROUTING_MODE` must be one of: `GLOBAL`, `REGIONAL`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
