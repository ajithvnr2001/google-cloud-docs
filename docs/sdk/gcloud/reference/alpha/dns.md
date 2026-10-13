---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/
title: gcloud alpha dns \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:54.152766+00:00
---

# gcloud alpha dns  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dns Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dns - manage your Cloud DNS managed-zones and record-sets 
SYNOPSIS
    

`gcloud alpha dns` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The gcloud dns command group lets you create and manage DNS zones and their associated records on Google Cloud DNS. 

Cloud DNS is a scalable, reliable and managed authoritative DNS service running on the same infrastructure as Google. It has low latency, high availability and is a cost-effective way to make your applications and services available to your users. 

More information on Cloud DNS can be found here: <https://cloud.google.com/dns> and detailed documentation can be found here: <https://cloud.google.com/dns/docs/>

EXAMPLES
     To see how to create and maintain managed-zones, run: 
    
    
    [gcloud alpha dns managed-zones](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones) --help

To see how to maintain the record-sets within a managed-zone, run: 
    
    
    [gcloud alpha dns record-sets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets) --help

To display Cloud DNS related information for your project, run: 
    
    
    [gcloud alpha dns project-info describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/project-info/describe) --help

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[active-peering-zones](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/active-peering-zones)`
     `(ALPHA)` Manage your Cloud DNS active-peering-zones. 
`[dns-keys](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/dns-keys)`
     `(ALPHA)` Manage Cloud DNS DNSKEY records. 
`[managed-zones](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones)`
     `(ALPHA)` Manage your Cloud DNS managed-zones. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/operations)`
     `(ALPHA)` Manage your Cloud DNS operations. 
`[outbound-endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/outbound-endpoints)`
     `(ALPHA)` Manage your Cloud DNS outbound endpoints. 
`[policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/policies)`
     `(ALPHA)` Manage your Cloud DNS policies. 
`[project-info](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/project-info)`
     `(ALPHA)` View Cloud DNS related information for a project. 
`[record-sets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets)`
     `(ALPHA)` Manage the record-sets within your managed-zones. 
`[response-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/response-policies)`
     `(ALPHA)` Manage your Cloud DNS response policy. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dns](https://docs.cloud.google.com/sdk/gcloud/reference/dns)
    
    
    [gcloud beta dns](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
