---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update/
title: gcloud network-connectivity spokes linked-router-appliances update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:52:33.201118+00:00
---

# gcloud network-connectivity spokes linked-router-appliances update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-connectivity spokes linked-router-appliances update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-connectivity spokes linked-router-appliances update - update a Router appliance spoke 
SYNOPSIS
    

`gcloud network-connectivity spokes linked-router-appliances update` (`SPOKE` : `--region`=`REGION`) [`--async`] [`--description`=`DESCRIPTION`] [`--exclude-export-ranges`=[`EXCLUDE_EXPORT_RANGES`,…]] [`--exclude-import-ranges`=[`EXCLUDE_IMPORT_RANGES`,…]] [`--include-export-ranges`=[`INCLUDE_EXPORT_RANGES`,…]] [`--include-import-ranges`=[`INCLUDE_IMPORT_RANGES`,…]] [`--router-appliance`=[`instance`=`INSTANCE`],[`ip`=`IP`]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the details of a Router appliance spoke. 
EXAMPLES
     To update the description of a Router appliance spoke named ``my-spoke``, run: 
    
    
    [gcloud network-connectivity spokes linked-router-appliances](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances) update my-spoke --region=us-central1 --description="new spoke description"

To replace the router appliance instances linked to a spoke with two new instances, run: 
    
    
    [gcloud network-connectivity spokes linked-router-appliances](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances) update my-spoke --region=us-central1 --router-appliance=instance=https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/vm1,ip=10.10.0.1 --router-appliance=instance=https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/vm2,ip=10.10.0.2

POSITIONAL ARGUMENTS
    

Spoke resource - Name of the spoke to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SPOKE`
     ID of the spoke or fully qualified identifier for the spoke. 

To set the `spoke` attribute: 

  * provide the argument `spoke` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The location Id. To set the `region` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     New description of the spoke. 
`--exclude-export-ranges`=[`EXCLUDE_EXPORT_RANGES`,…]
     Dynamic routes overlapped/encompassed by exclude export ranges are excluded during export to hub. 
`--exclude-import-ranges`=[`EXCLUDE_IMPORT_RANGES`,…]
     Hub routes overlapped/encompassed by exclude import ranges are excluded during import from hub. 
`--include-export-ranges`=[`INCLUDE_EXPORT_RANGES`,…]
     Dynamic routes fully encompassed by include export ranges are included during export to hub. If it's empty, the spoke exports all dynamic routes to the hub. 
`--include-import-ranges`=[`INCLUDE_IMPORT_RANGES`,…]
     Hub routes fully encompassed by include import ranges are included during import from hub. If it's empty, the spoke does not import any subnets from the hub. If it's empty and site-to-site-data-transfer is true, the spoke imports all IPv4 site-to-site dynamic routes from the hub. 
`--router-appliance`=[`instance`=`INSTANCE`],[`ip`=`IP`]
     Router appliance instance(s) with which to replace the set of instances already linked to this spoke. Pass this flag multiple times to replace with multiple instances. For example, use `--router-appliance=instance=new_ins_uri,ip=10.10.0.1` for a single router appliance instance, or `--router-appliance=instance=new_ins_uri_1,ip=10.10.0.1 --router-appliance=instance=new_ins_uri_2,ip=10.10.0.2 …` for multiple instances. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    [gcloud network-connectivity spokes linked-router-appliances](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances) update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    [gcloud network-connectivity spokes linked-router-appliances](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances) update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This variant is also available: 
    
    
    [gcloud beta network-connectivity spokes linked-router-appliances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/linked-router-appliances) update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
