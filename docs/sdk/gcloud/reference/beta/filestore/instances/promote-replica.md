---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/promote-replica/
title: gcloud beta filestore instances promote-replica \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:33:37.663190+00:00
---

# gcloud beta filestore instances promote-replica  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/promote-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta filestore instances promote-replica Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta filestore instances promote-replica - promote a Filestore standby replication instance 
SYNOPSIS
    

`gcloud beta filestore instances promote-replica` (`INSTANCE` : `--zone`=`ZONE`) [`--async`] [`--location`=`LOCATION`] [`--peer-instance`=`PEER_INSTANCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Promote a Filestore standby replication instance to a regular instance. This command can be called directly on the standby instance or on the active instance with the standby peer instance parameter. When used on the standby instance promotes the standby instance to a regular instance even if the active instance is unavailable. When used on the active instance detaches the standby instance from the active instance even if the standby instance is unavailable. 

This command can fail for the following reasons: 

  * The target instance does not exist. 
  * The instance is not a standby replication member. 
  * The instance is an active instance and the peer instance parameter is missing or invalid. 


EXAMPLES
     To promote a standby instance with the name ``my-replica-instance`` located in ``us-central1``, run: 
    
    
    gcloud beta filestore instances promote-replica my-replica-instance --zone=us-central1

To promote a standby instance with the name ``my-replica-instance`` located in ``us-central1``, attached to the active peer instance ``my-active-instance`` located in ``us-west1``, run: 
    
    
    gcloud beta filestore instances promote-replica my-active-instance --zone=us-west1 --peer-instance=projects/my-project/locations/us-central1/instances/my-replica-instance

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Filestore instance to promote. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     The zone of the Filestore instance. To set the `zone` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * provide the argument `--location` on the command line; 
  * set the property `filestore/zone`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`
     Location of the Filestore instance to promote. 
`--peer-instance`=`PEER_INSTANCE`
     The name of the standby peer instance to promote. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `file/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/filestore/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud filestore instances promote-replica](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
