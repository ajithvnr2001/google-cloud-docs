---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/transaction/remove/
title: gcloud alpha dns record-sets transaction remove \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:57.973439+00:00
---

# gcloud alpha dns record-sets transaction remove  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/transaction/remove/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dns record-sets transaction remove Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dns record-sets transaction remove - append a record-set deletion to the transaction 
SYNOPSIS
    

`gcloud alpha dns record-sets transaction remove` `RRDATAS` [`RRDATAS` …] `--name`=`NAME` `--ttl`=`TTL` `--type`=`TYPE` `--zone`=`ZONE`, `-z` `ZONE` [`--transaction-file`=`TRANSACTION_FILE`; default="transaction.yaml"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command appends a record-set deletion to the transaction. 
EXAMPLES
     To remove an A record, run: 
    
    
    gcloud alpha dns record-sets transaction remove --zone=MANAGED_ZONE --name=my.domain. --ttl=1234 --type=A "1.2.3.4"

To remove a TXT record with multiple data values, run: 
    
    
    gcloud alpha dns record-sets transaction remove --zone=MANAGED_ZONE --name=my.domain. --ttl=2345 --type=TXT "Hello world" "Bye world"

POSITIONAL ARGUMENTS
    

`RRDATAS` [`RRDATAS` …]
     DNS name of the record-set to be removed. 
REQUIRED FLAGS
    

`--name`=`NAME`
     DNS name of the record-set to be removed. 
`--ttl`=`TTL`
     TTL for the record-set to be removed. 
`--type`=`TYPE`
     Type of the record-set to be removed. 
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
    
    
    [gcloud dns record-sets transaction remove](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove)
    
    
    [gcloud beta dns record-sets transaction remove](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/record-sets/transaction/remove)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
