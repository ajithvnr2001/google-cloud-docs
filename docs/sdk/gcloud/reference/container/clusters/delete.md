---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete/
title: gcloud container clusters delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:44.628195+00:00
---

# gcloud container clusters delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container clusters delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container clusters delete - delete an existing cluster for running containers 
SYNOPSIS
    

`gcloud container clusters delete` `NAME` [`NAME` …] [`--async`] [`--location`=`LOCATION` | `--region`=`REGION` | `--zone`=`ZONE`, `-z` `ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     When you delete a cluster, the following resources are deleted: 

  * The control plane resources 
  * All of the node instances in the cluster 
  * Any Pods that are running on those instances 
  * Any firewalls and routes created by Kubernetes Engine at the time of cluster creation 
  * Data stored in host hostPath and emptyDir volumes 



GKE will attempt to delete the following resources. Deletion of these resources is not always guaranteed: 

  * External load balancers created by the cluster 
  * Internal load balancers created by the cluster 
  * Persistent disk volumes 


EXAMPLES
     To delete an existing cluster, run: 
    
    
    gcloud container clusters delete sample-cluster

POSITIONAL ARGUMENTS
    

`NAME` [`NAME` …]
     The names of the clusters to delete. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
At most one of these can be specified: 

`--location`=`LOCATION`
     Compute zone or region (e.g. us-central1-a or us-central1) for the cluster. Overrides the default compute/region or compute/zone value for this command invocation. Prefer using this flag over the --region or --zone flags. 
`--region`=`REGION`
     Compute region (e.g. us-central1) for a regional cluster. Overrides the default compute/region property value for this command invocation. 
`--zone`=`ZONE`, `-z` `ZONE`
     Compute zone (e.g. us-central1-a) for a zonal cluster. Overrides the default compute/zone property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters/delete)
    
    
    [gcloud beta container clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
