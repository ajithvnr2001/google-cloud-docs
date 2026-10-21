---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/multicast-group-ranges/create/
title: gcloud alpha network-services multicast-group-ranges create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:46:48.238460+00:00
---

# gcloud alpha network-services multicast-group-ranges create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/multicast-group-ranges/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-services multicast-group-ranges create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-services multicast-group-ranges create - create a multicast group range 
SYNOPSIS
    

`gcloud alpha network-services multicast-group-ranges create` (`MULTICAST_GROUP_RANGE` : `--location`=`LOCATION`) `--multicast-domain`=`MULTICAST_DOMAIN` `--reserved-internal-range`=`RESERVED_INTERNAL_RANGE` [`--async`] [`--consumer-accept-list`=[`CONSUMER_ACCEPT_LIST`,…]] [`--description`=`DESCRIPTION`] [`--distribution-scope`=`DISTRIBUTION_SCOPE`] [`--[no-]enable-logging`] [`--labels`=[`KEY`=`VALUE`,…]] [`--require-explicit-accept`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a multicast group range in the specified location of the current project. 
EXAMPLES
     Create a multicast group range with the name 'my-multicast-group-range', reserved-internal-range 'path-to-ir', multicast-domain 'path-to-md', and location 'global'. 
    
    
    gcloud alpha network-services multicast-group-ranges create my-multicast-group-range --reserved-internal-range=path-to-ir --multicast-domain=path-to-md --location=global

POSITIONAL ARGUMENTS
    

Multicast group range resource - Name of the multicast group range to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `multicast_group_range` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MULTICAST_GROUP_RANGE`
     ID of the multicast group range or fully qualified identifier for the multicast group range. 

To set the `multicast_group_range` attribute: 

  * provide the argument `multicast_group_range` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. 

To set the `location` attribute: 

  * provide the argument `multicast_group_range` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--multicast-domain`=`MULTICAST_DOMAIN`
     The multicast domain to be used. 
`--reserved-internal-range`=`RESERVED_INTERNAL_RANGE`
     The reserved internal range to be used. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--consumer-accept-list`=[`CONSUMER_ACCEPT_LIST`,…]
     An optional list of consumer projects that can use this multicast group range. 
`--description`=`DESCRIPTION`
     The description for the multicast group range. 
`--distribution-scope`=`DISTRIBUTION_SCOPE`
     Distribution scope of this multicast group range. `DISTRIBUTION_SCOPE` must be one of: `distribution-scope-unspecified`, `intra-region`, `intra-zone`. 
`--[no-]enable-logging`
     Whether to enable logging for this multicast group range. Use `--enable-logging` to enable and `--no-enable-logging` to disable. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--require-explicit-accept`
     Whether an empty consumer accept list will reject all consumer projects. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud network-services multicast-group-ranges create](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/create)
    
    
    [gcloud beta network-services multicast-group-ranges create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/multicast-group-ranges/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
