---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/datastores/create/
title: gcloud vmware datastores create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:54.386659+00:00
---

# gcloud vmware datastores create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/datastores/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware datastores create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware datastores create - create a datastore 
SYNOPSIS
    

`gcloud vmware datastores create` (`DATASTORE` : `--location`=`LOCATION`) (`--filestore`=`FILESTORE` | `--netapp`=`NETAPP` | `--third-party-nfs-file-share`=`THIRD_PARTY_NFS_FILE_SHARE` `--third-party-nfs-network`=`THIRD_PARTY_NFS_NETWORK` `--third-party-nfs-servers`=`SERVER`,[`SERVER`,…]) [`--async`] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a datastore. Datastore creation is considered finished when the datastore is in ACTIVE state. Check the progress of a datastore using `[gcloud vmware datastores list](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/datastores/list)`. 
EXAMPLES
     To create a datastore named `my-datastore` in `us-west2-a` connected to filestore instance `projects/my-project/locations/us-west2-a/instances/my-filestore-instance`, run: 
    
    
    gcloud vmware datastores create my-datastore --location=us-west2-a --project=my-project --filestore=projects/my-project/locations/us-west2-a/instances/my-filestore-instance

Or: 
    
    
    gcloud vmware datastores create my-datastore --filestore=projects/my-project/locations/us-west2-a/instances/my-filestore-instance

Or: 
    
    
    gcloud vmware datastores create my-datastore --netapp=projects/my-project/locations/us-west2-a/volumes/my-netapp-volume

Or: 
    
    
    gcloud vmware datastores create my-datastore --third-party-nfs-network=my-network --third-party-nfs-file-share=my-fileshare --third-party-nfs-servers=10.0.0.1,10.0.0.2 --location=us-west2-a --project=my-project

In the second example, the project and location are taken from gcloud properties core/project and compute/zone. 

POSITIONAL ARGUMENTS
    

Datastore resource - datastore. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `datastore` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATASTORE`
     ID of the datastore or fully qualified identifier for the datastore. 

To set the `datastore` attribute: 

  * provide the argument `datastore` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the private cloud or cluster. 

To set the `location` attribute: 

  * provide the argument `datastore` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/zone`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--filestore`=`FILESTORE`
     Google Filestore instance to be used as datastore. 
`--netapp`=`NETAPP`
     Google NetApp volume to be used as datastore. 
Or at least one of these can be specified: 

`--third-party-nfs-file-share`=`THIRD_PARTY_NFS_FILE_SHARE`
     Mount folder name of NFS. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--third-party-nfs-network`=`THIRD_PARTY_NFS_NETWORK`
     Network name of NFS's VPC. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--third-party-nfs-servers`=`SERVER`,[`SERVER`,…]
     Comma-separated list of server IP addresses of the NFS file service. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Text describing the datastore. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
