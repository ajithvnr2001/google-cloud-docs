---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/hubs/create/
title: gcloud beta network-connectivity hubs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:16.552243+00:00
---

# gcloud beta network-connectivity hubs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/hubs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-connectivity hubs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-connectivity hubs create - create a new hub 
SYNOPSIS
    

`gcloud beta network-connectivity hubs create` `HUB` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--policy-mode`=`POLICY_MODE`] [`--preset-topology`=`PRESET_TOPOLOGY`] [`--export-psc` | `--export-psc-global-google-apis` `--export-psc-published-services-and-regional-google-apis`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new hub with the given name. 
EXAMPLES
     To create a hub with the name ``my-hub`` and the description ``optional description``, run: 
    
    
    gcloud beta network-connectivity hubs create my-hub --description="optional description"

POSITIONAL ARGUMENTS
    

Hub resource - Name of the hub to be created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `hub` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`HUB`
     ID of the hub or fully qualified identifier for the hub. 

To set the `hub` attribute: 

  * provide the argument `hub` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the hub. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--policy-mode`=`POLICY_MODE`
     Policy mode of the hub. `POLICY_MODE` must be one of: `policy-mode-unspecified`, `preset`. 
`--preset-topology`=`PRESET_TOPOLOGY`
     Topology of the hub. Only applicable when ``\--policy-mode=PRESET``. `PRESET_TOPOLOGY` must be one of: `hybrid-inspection`, `mesh`, `preset-topology-unspecified`, `star`. 
At most one of these can be specified: 

`--export-psc`
     This boolean controls whether Private Service Connect transitivity is enabled for the hub. 
Or at least one of these can be specified: 

`--export-psc-global-google-apis`
     This boolean controls whether Private Service Connect endpoints for global Google APIs should be propagated. 
`--export-psc-published-services-and-regional-google-apis`
     This boolean control whether Private Service Connect endpoints for regional ILBs and regional Google APIs should be propagated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-connectivity hubs create](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create)
    
    
    [gcloud alpha network-connectivity hubs create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-connectivity/hubs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
