---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/
title: gcloud alpha container fleet config-management \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:35.603111+00:00
---

# gcloud alpha container fleet config-management  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container fleet config-management Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container fleet config-management - use the Config Management feature 
SYNOPSIS
    

`gcloud alpha container fleet config-management` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync) using the Config Management feature. 

To manage Policy Controller, use `[gcloud container fleet policycontroller](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller)` instead. 

Hierarchy Controller is no longer available to install. If Hierarchy Controller is still configured, Config Sync upgrades are blocked. To upgrade Config Sync, disable Hierarchy Controller following <https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-hierarchy-controller>. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[apply](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/apply)`
     `(ALPHA)` Update a Config Management feature spec. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/delete)`
     `(ALPHA)` `(DEPRECATED)` Remove the Config Management feature spec for the given membership. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/describe)`
     `(ALPHA)` Describe the Config Management feature. 
`[disable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/disable)`
     `(ALPHA)` Disable the Config Management feature. 
`[enable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/enable)`
     `(ALPHA)` Enable the Config Management feature. 
`[fetch-for-apply](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/fetch-for-apply)`
     `(ALPHA)` `(DEPRECATED)` Prints the Config Management configuration applied to the given membership. 
`[status](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/status)`
     `(ALPHA)` Print the status of all clusters with Config Management enabled. 
`[unmanage](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/unmanage)`
     `(ALPHA)` Remove the Config Management feature spec for the given membership. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/update)`
     `(ALPHA)` Update the Config Management feature. 
`[upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/upgrade)`
     `(ALPHA)` Upgrade the version of the Config Management feature. 
`[version](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management/version)`
     `(ALPHA)` Print the version of all clusters with Config Management enabled. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container fleet config-management](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/config-management)
    
    
    [gcloud beta container fleet config-management](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/config-management)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
