---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/volumes/replications/delete/
title: gcloud alpha netapp volumes replications delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:32:55.812980+00:00
---

# gcloud alpha netapp volumes replications delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/volumes/replications/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha netapp volumes replications delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha netapp volumes replications delete - delete a Cloud NetApp Storage Pool 
SYNOPSIS
    

`gcloud alpha netapp volumes replications delete` (`REPLICATION` : `--location`=`LOCATION`) [`--async`] [`--volume`=`VOLUME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Delete a Cloud NetApp Volume Replication. 
EXAMPLES
     The following command deletes a Replication named NAME using the required arguments: 
    
    
    gcloud alpha netapp volumes replications delete NAME --location=us-central1 --volume=vol1

To delete a Replication named NAME asynchronously, run the following command: 
    
    
    gcloud alpha netapp volumes replications delete NAME --location=us-central1 --volume=vol1 --async

POSITIONAL ARGUMENTS
    

Replication resource - The Replication to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `replication` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `volume` attribute: 

  * provide the argument `replication` on the command line with a fully specified name; 
  * provide the argument `--volume` on the command line. 



This must be specified. 

`REPLICATION`
     ID of the replication or fully qualified identifier for the replication. 

To set the `replication` attribute: 

  * provide the argument `replication` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the replication. 

To set the `location` attribute: 

  * provide the argument `replication` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Volume resource - The Volume that the Replication is based on This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--volume` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--volume` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--volume`=`VOLUME`
     ID of the volume or fully qualified identifier for the volume. 

To set the `volume` attribute: 

  * provide the argument `--volume` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud netapp volumes replications delete](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/delete)
    
    
    [gcloud beta netapp volumes replications delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/volumes/replications/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
