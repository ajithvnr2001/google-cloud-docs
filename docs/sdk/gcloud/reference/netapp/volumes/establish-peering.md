---
url: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/establish-peering/
title: gcloud netapp volumes establish-peering \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:16.115065+00:00
---

# gcloud netapp volumes establish-peering  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/establish-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud netapp volumes establish-peering Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud netapp volumes establish-peering - establish peering for Cache Volumes 
SYNOPSIS
    

`gcloud netapp volumes establish-peering` (`VOLUME` : `--location`=`LOCATION`) `--peer-cluster-name`=`PEER_CLUSTER_NAME` `--peer-svm-name`=`PEER_SVM_NAME` `--peer-volume-name`=`PEER_VOLUME_NAME` [`--async`] [`--peer-ip-addresses`=`PEER_IP_ADDRESS`,[…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Establish peering for Cache Volumes. 
EXAMPLES
     The following command establishes peering for Cache Volume named NAME using the arguments specified: 
    
    
    gcloud netapp volumes establish-peering NAME --location=us-central1 --peer-cluster-name=peer-cluster-name1 --peer-svm-name=peer-svm-name1 --peer-volume-name=peer-volume-name1 --peer-ip-addresses=1.1.1.1,2.2.2.2

POSITIONAL ARGUMENTS
    

Volume resource - The Cache Volume to establish peering for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `volume` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`VOLUME`
     ID of the volume or fully qualified identifier for the volume. 

To set the `volume` attribute: 

  * provide the argument `volume` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the volume. 

To set the `location` attribute: 

  * provide the argument `volume` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

`--peer-cluster-name`=`PEER_CLUSTER_NAME`
     Name of the destination cluster to be peered with the source cluster. 
`--peer-svm-name`=`PEER_SVM_NAME`
     Name of the local source vserver svm to be peered with the destination cluster. 
`--peer-volume-name`=`PEER_VOLUME_NAME`
     Name of the source volume to be peered with the destination volume. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--peer-ip-addresses`=`PEER_IP_ADDRESS`,[…]
     List of ip addresses to be used for peering. This is required for cluster peering, not required for svm peering. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha netapp volumes establish-peering](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/volumes/establish-peering)
    
    
    [gcloud beta netapp volumes establish-peering](https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/volumes/establish-peering)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
