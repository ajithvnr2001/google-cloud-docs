---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete/
title: gcloud container fleet memberships delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:54.398551+00:00
---

# gcloud container fleet memberships delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container fleet memberships delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container fleet memberships delete - delete a membership 
SYNOPSIS
    

`gcloud container fleet memberships delete` (`MEMBERSHIP` : `--location`=`LOCATION`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command deletes the Fleet Membership resource corresponding to the cluster. 

This command is intended to delete stale Fleet Membership resources as doing so on a fully registered cluster will skip uninstalling the Connect Agent and and orphan in-cluster resources and agent connections to Google. To completely unregister the cluster, consider using the command: `[gcloud container fleet memberships unregister](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister)`. 

EXAMPLES
     First retrieve the ID of the membership using the command below. The output of this command lists all the fleet's members, with their unique IDs in the Names column: 
    
    
    [gcloud container fleet memberships list](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/list)

Delete a membership from the active project's fleet: 
    
    
    gcloud container fleet memberships delete MEMBERSHIP_NAME

POSITIONAL ARGUMENTS
    

Membership resource - The cluster membership to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `membership` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MEMBERSHIP`
     ID of the membership or fully qualified identifier for the membership. 

To set the `membership` attribute: 

  * provide the argument `membership` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `membership` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * global is the only supported location. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `gkehub/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha container fleet memberships delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/memberships/delete)
    
    
    [gcloud beta container fleet memberships delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
