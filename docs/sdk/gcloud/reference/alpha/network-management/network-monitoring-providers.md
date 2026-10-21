---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/
title: gcloud alpha network-management network-monitoring-providers \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:34:53.745762+00:00
---

# gcloud alpha network-management network-monitoring-providers  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-management network-monitoring-providers Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-management network-monitoring-providers - a Network Monitoring Provider manages the enablement state of the Network Insights service 
SYNOPSIS
    

`gcloud alpha network-management network-monitoring-providers` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The service is considered enabled when provider resource is in 'ACTIVE' state. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[monitoring-points](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/monitoring-points)`
     `(ALPHA)` A Monitoring Point is an agent within your network or application infrastructure that sends probes and reports the results to AppNeta. 
`[network-paths](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/network-paths)`
     `(ALPHA)` A Network Path represents the hop-by-hop route and active network delivery quality between a Monitoring Point (source) and a target destination. 
`[web-paths](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/web-paths)`
     `(ALPHA)` A Web Path represents a monitored web application or URL, assessed from a monitoring point to measure performance and availability. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/create)`
     `(ALPHA)` Create a Network Monitoring Provider. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/delete)`
     `(ALPHA)` Delete a Network Monitoring Provider. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/describe)`
     `(ALPHA)` Describe a Network Monitoring Provider. 
`[generate-monitoring-point-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/generate-monitoring-point-config)`
     `(ALPHA)` Generate a monitoring point config. 
`[generate-provider-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/generate-provider-access-token)`
     `(ALPHA)` Generate a provider access token. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/list)`
     `(ALPHA)` List Network Monitoring Providers. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud network-management network-monitoring-providers](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/network-monitoring-providers)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
