---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update/
title: gcloud network-connectivity spokes linked-producer-vpc-network update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:52:32.747429+00:00
---

# gcloud network-connectivity spokes linked-producer-vpc-network update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-connectivity spokes linked-producer-vpc-network update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-connectivity spokes linked-producer-vpc-network update - update a Producer VPC spoke 
SYNOPSIS
    

`gcloud network-connectivity spokes linked-producer-vpc-network update` `SPOKE` [`--async`] [`--description`=`DESCRIPTION`] [`--exclude-export-ranges`=[`CIDR_RANGE`,…]] [`--global`] [`--include-export-ranges`=[`CIDR_RANGE`,…]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the details of a Producer VPC spoke. 
EXAMPLES
     To update the description of a Producer VPC spoke named ``my-spoke``, run: 
    
    
    [gcloud network-connectivity spokes linked-producer-vpc-network](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network) update myspoke --global --description="new spoke description"

POSITIONAL ARGUMENTS
    

Spoke resource - Name of the spoke to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--global` on the command line. 



This must be specified. 

`SPOKE`
     ID of the spoke or fully qualified identifier for the spoke. 

To set the `spoke` attribute: 

  * provide the argument `spoke` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     New description of the spoke. 
`--exclude-export-ranges`=[`CIDR_RANGE`,…]
     New exclude export ranges of the spoke. 
`--global`
     Indicates that the spoke is global. 
`--include-export-ranges`=[`CIDR_RANGE`,…]
     New include export ranges of the spoke. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    [gcloud network-connectivity spokes linked-producer-vpc-network](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network) update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    [gcloud network-connectivity spokes linked-producer-vpc-network](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network) update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the networkconnectivity/v1 API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This variant is also available: 
    
    
    [gcloud beta network-connectivity spokes](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes) linked-producer-vpc-network update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
