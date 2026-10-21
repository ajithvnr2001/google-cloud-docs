---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/packages/delete/
title: gcloud beta container fleet packages delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:58:17.158592+00:00
---

# gcloud beta container fleet packages delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/packages/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container fleet packages delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container fleet packages delete - delete Package Rollouts Fleet Package 
SYNOPSIS
    

`gcloud beta container fleet packages delete` (`FLEET_PACKAGE` : `--location`=`LOCATION`) [`--force`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Delete Package Rollouts Fleet Package. 
EXAMPLES
     To delete Fleet Package `cert-manager-app` in `us-central1`, run: 
    
    
    gcloud beta container fleet packages delete cert-manager-app --location=us-central1

POSITIONAL ARGUMENTS
    

Fleet package resource - The Fleet Package to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `fleet_package` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`FLEET_PACKAGE`
     ID of the fleet-package or fully qualified identifier for the fleet-package. 

To set the `fleet-package` attribute: 

  * provide the argument `fleet_package` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud zone or region for the fleet-package. 

To set the `location` attribute: 

  * provide the argument `fleet_package` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `config_delivery/location`. 


FLAGS
    

`--force`
     If true, force deletion of any child resources. Otherwise, attempting to delete a Fleet Package with children will fail. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container fleet packages delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/packages/delete)
    
    
    [gcloud alpha container fleet packages delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/packages/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
