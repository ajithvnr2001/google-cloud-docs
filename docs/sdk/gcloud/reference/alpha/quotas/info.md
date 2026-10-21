---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas/info/
title: gcloud alpha quotas info \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:01:35.288539+00:00
---

# gcloud alpha quotas info  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas/info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha quotas info Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha quotas info - manage Cloud Quotas QuotaInfo 
SYNOPSIS
    

`gcloud alpha quotas info` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` QuotaInfo is a read-only resource that provides metadata and quota value information about a particular quota for a given project, folder or organization. The QuotaInfo resource contains: 

  * Metadata such as name and dimension. 
  * Quota values for different quota dimensions. 



Cloud Quotas obtains information from the quotas defined by Google Cloud services and any fulfilled quota adjustments that you initiate. 

Note: Because QuotaInfo is constructed by incorporating information from different sources, a default quota configuration exists even if you have not created a QuotaPreference resource. Until you express a preferred state through quotaPreference.create or quotaPreference.update, QuotaInfo relies on the default quota information available to determine what quota value to enforce. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas/info/describe)`
     `(ALPHA)` Retrieve the QuotaInfo of a quota for a project, folder or organization. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas/info/list)`
     `(ALPHA)` List QuotaInfos of all quotas for a given project, folder or organization. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud quotas info](https://docs.cloud.google.com/sdk/gcloud/reference/quotas/info)
    
    
    [gcloud beta quotas info](https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/info)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
