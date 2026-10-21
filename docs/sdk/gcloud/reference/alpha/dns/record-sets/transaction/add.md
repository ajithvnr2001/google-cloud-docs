---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/transaction/add/
title: gcloud alpha dns record-sets transaction add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:38.418319+00:00
---

# gcloud alpha dns record-sets transaction add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/transaction/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dns record-sets transaction add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dns record-sets transaction add - append a record-set addition to the transaction 
SYNOPSIS
    

`gcloud alpha dns record-sets transaction add` `RRDATAS` [`RRDATAS` …] `--name`=`NAME` `--ttl`=`TTL` `--type`=`TYPE` `--zone`=`ZONE`, `-z` `ZONE` [`--transaction-file`=`TRANSACTION_FILE`; default="transaction.yaml"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command appends a record-set addition to the transaction. 

For a guide detailing how to manage records, see: <https://cloud.google.com/dns/records/>

EXAMPLES
     To add an A record with an IP address of "1.2.3.4", domain name of "my.domain.", and a managed zone "MANAGED_ZONE", run: 
    
    
    gcloud alpha dns record-sets transaction add "1.2.3.4" --name=my.domain. --ttl=1234 --type=A --zone=MANAGED_ZONE

To add a TXT record with multiple data values while specifying time to live as 14400 seconds, run: 
    
    
    gcloud alpha dns record-sets transaction add "Hello world" "Bye world" --name=my.domain. --ttl=14400 --type=TXT --zone=MANAGED_ZONE

POSITIONAL ARGUMENTS
    

`RRDATAS` [`RRDATAS` …]
     DNS data (Address/CNAME/MX info, etc.) of the record-set to add. This is RDATA; the format of this information varies depending on the type and class of the resource record. 
REQUIRED FLAGS
    

`--name`=`NAME`
     DNS or domain name of the record-set to add. 
`--ttl`=`TTL`
     TTL (time to live) for the record-set to add. 
`--type`=`TYPE`
     DNS record type of the record-set to add. 
`--zone`=`ZONE`, `-z` `ZONE`
     Name of the managed zone whose record sets you want to manage. 
OPTIONAL FLAGS
    

`--transaction-file`=`TRANSACTION_FILE`; default="transaction.yaml"
     Path of the file which contains the transaction. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dns record-sets transaction add](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add)
    
    
    [gcloud beta dns record-sets transaction add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/record-sets/transaction/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
