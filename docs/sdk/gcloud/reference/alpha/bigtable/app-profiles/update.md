---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update/
title: gcloud alpha bigtable app-profiles update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:57.189088+00:00
---

# gcloud alpha bigtable app-profiles update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bigtable app-profiles update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bigtable app-profiles update - update a Bigtable app profile 
SYNOPSIS
    

`gcloud alpha bigtable app-profiles update` (`APP_PROFILE` : `--instance`=`INSTANCE`) [`--async`] [`--description`=`DESCRIPTION`] [`--force`] [`--data-boost` `--data-boost-compute-billing-owner`=`DATA_BOOST_COMPUTE_BILLING_OWNER` | `--priority`=`PRIORITY` `--standard` `--use-memory-layer`] [[`--route-any` : `--restrict-to`=[`RESTRICT_TO`,…] `--row-affinity`] | [`--route-to`=`ROUTE_TO` : `--transactional-writes`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Bigtable app profile. 
EXAMPLES
     To update an app profile to use a multi-cluster routing policy, run: 
    
    
    gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --route-any

To update an app profile to use a single-cluster routing policy that routes all requests to `my-cluster-id` and allows transactional writes, run: 
    
    
    gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --route-to=my-cluster-id --transactional-writes

To update the description for an app profile, run: 
    
    
    gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --description="New description"

To update the request priority for an app profile to PRIORITY_LOW, run: 
    
    
    gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --priority=PRIORITY_LOW

To update an app profile to enable Data Boost which bills usage to the host project, run: 
    
    
    gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --data-boost --data-boost-compute-billing-owner=HOST_PAYS

To update an app profile to enable row-affinity routing, run: 
    
    
    gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --route-any --row-affinity

To update an app profile to use the memory layer, run: 
    
    
    gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --use-memory-layer

POSITIONAL ARGUMENTS
    

App profile resource - The app profile to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `app_profile` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APP_PROFILE`
     ID of the app profile or fully qualified identifier for the app profile. 

To set the `name` attribute: 

  * provide the argument `app_profile` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     Bigtable instance for the app profile. 

To set the `instance` attribute: 

  * provide the argument `app_profile` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Friendly name of the app profile. 
`--force`
     Ignore warnings and force update. 
At most one of these can be specified: 

Data Boost Read-only Isolation 
`--data-boost`
     Use Data Boost serverless compute option, rather than standard provisioned node compute. If specified, --data-boost-compute-billing-owner is required. Specifying Data Boost compute on an app profile that uses standard provisioned node compute may cause unexpected behavior for running applications. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--data-boost-compute-billing-owner`=`DATA_BOOST_COMPUTE_BILLING_OWNER`
     Specify the Data Boost compute billing owner, required if --data-boost is passed. `DATA_BOOST_COMPUTE_BILLING_OWNER` must be (only one value is supported): 

`HOST_PAYS`
     Compute billing should be accounted towards the host Cloud project (containing the targeted Bigtable instance / table). 
This flag argument must be specified if any of the other arguments in this group are specified. 
Standard Isolation 
`--priority`=`PRIORITY`
     Specify the request priority under standard provisioned node compute capabilities. Passing this option implies standard provisioned node compute, e.g. the `--standard` option. If not specified, the app profile uses standard provisioned node compute with PRIORITY_HIGH by default. Specifying request priority on an app profile that has Data Boost serverless compute enabled changes the compute option to standard and uses the specified priority, which might cause unexpected behavior for running applications. `PRIORITY` must be one of: 

`PRIORITY_HIGH`
     Requests are treated with high priority. 
`PRIORITY_LOW`
     Requests are treated with low priority. 
`PRIORITY_MEDIUM`
     Requests are treated with medium priority. 
`--standard`
     Use standard provisioned node compute option, rather than Data Boost compute option. If specified, `--priority` or `--use-memory-layer` is required. 
`--use-memory-layer`
     Enables the in-memory layer for standard provisioned node compute. This option sets the compute option to `--standard` with the in-memory layer enabled. Use `--no-use-memory-layer` to disable the in-memory layer. 
At most one of these can be specified: 

Multi Cluster Routing Policy 
`--route-any`
     Use Multi Cluster Routing policy. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--restrict-to`=[`RESTRICT_TO`,…]
     Cluster IDs to route to using the Multi Cluster Routing Policy. If unset, all clusters in the instance are eligible. 
`--row-affinity`
     Use row-affinity routing for this app profile. 
Single Cluster Routing Policy 
`--route-to`=`ROUTE_TO`
     Cluster ID to route to using Single Cluster Routing policy. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--transactional-writes`
     Allow transactional writes with a Single Cluster Routing policy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud bigtable app-profiles update](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/update)
    
    
    [gcloud beta bigtable app-profiles update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/app-profiles/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
