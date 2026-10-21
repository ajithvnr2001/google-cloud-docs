---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/
title: gcloud dns record-sets \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:56:46.812556+00:00
---

# gcloud dns record-sets  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dns record-sets Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dns record-sets - manage the record-sets within your managed-zones 
SYNOPSIS
    

`gcloud dns record-sets` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage the record-sets within your managed-zones. 
EXAMPLES
     To import record-sets from a BIND zone file, run: 
    
    
    [gcloud dns record-sets import](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import) --zone=MANAGED_ZONE --zone-file-format ZONE_FILE

To export record-sets in yaml format, run: 
    
    
    [gcloud dns record-sets export](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/export) --zone=MANAGED_ZONE

To see how to make scriptable changes to your record-sets through transactions, run: 
    
    
    [gcloud dns record-sets transaction](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction) --help

To list all changes, run: 
    
    
    [gcloud dns record-sets changes list](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/list) --zone=MANAGED_ZONE

To see change details, run: 
    
    
    [gcloud dns record-sets changes describe](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe) CHANGE_ID --zone=MANAGED_ZONE

To see the list of all record-sets, run: 
    
    
    [gcloud dns record-sets list](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/list) --zone=MANAGED_ZONE

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[changes](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes)`
     View details about changes to your Cloud DNS record-sets. 
`[transaction](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction)`
     Make scriptable and transactional changes to your record-sets. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/create)`
     Creates a record-set in a managed-zone. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete)`
     Delete a record-set in a managed-zone. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe)`
     Describe a record-set in a managed-zone. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/export)`
     Export your record-sets into a file. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import)`
     Import record-sets into your managed-zone. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/list)`
     View the list of record-sets in a managed-zone. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/update)`
     Updates a record-set in a managed-zone. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha dns record-sets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets)
    
    
    [gcloud beta dns record-sets](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/record-sets)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
