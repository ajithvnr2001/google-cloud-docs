---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/
title: gcloud beta container hub config-management \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:31.891786+00:00
---

# gcloud beta container hub config-management  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub config-management Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub config-management - use the Config Management feature 
SYNOPSIS
    

`gcloud beta container hub config-management` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync) using the Config Management feature. 

To manage Policy Controller, use `[gcloud container fleet policycontroller](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller)` instead. 

Hierarchy Controller is no longer available to install. If Hierarchy Controller is still configured, Config Sync upgrades are blocked. To upgrade Config Sync, disable Hierarchy Controller following <https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-hierarchy-controller>. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[apply](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/apply)`
     `(BETA)` Update a Config Management feature spec. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/describe)`
     `(BETA)` Describe the Config Management feature. 
`[disable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/disable)`
     `(BETA)` Disable the Config Management feature. 
`[enable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/enable)`
     `(BETA)` Enable the Config Management feature. 
`[status](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/status)`
     `(BETA)` Print the status of all clusters with Config Management enabled. 
`[unmanage](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/unmanage)`
     `(BETA)` Remove the Config Management feature spec for the given membership. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/update)`
     `(BETA)` Update the Config Management feature. 
`[upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/upgrade)`
     `(BETA)` Upgrade the version of the Config Management feature. 
`[version](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/version)`
     `(BETA)` Print the version of all clusters with Config Management enabled. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub config-management](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/config-management)
    
    
    [gcloud alpha container hub config-management](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/config-management)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
