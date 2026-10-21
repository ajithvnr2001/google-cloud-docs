---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/
title: gcloud dns record-sets transaction \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:49.866455+00:00
---

# gcloud dns record-sets transaction  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dns record-sets transaction Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dns record-sets transaction - make scriptable and transactional changes to your record-sets 
SYNOPSIS
    

`gcloud dns record-sets transaction` `COMMAND` [`--transaction-file`=`TRANSACTION_FILE`; default="transaction.yaml"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Make scriptable and transactional changes to your record-sets. 
EXAMPLES
     To start a transaction, run: 
    
    
    [gcloud dns record-sets transaction start](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/start) --zone=MANAGED_ZONE

To append a record-set addition to the transaction, run: 
    
    
    [gcloud dns record-sets transaction add](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add) --name RECORD_SET_NAME --ttl TTL --type TYPE DATA --zone=MANAGED_ZONE

To append a record-set removal to the transaction, run: 
    
    
    [gcloud dns record-sets transaction remove](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove) --name RECORD_SET_NAME --ttl TTL --type TYPE DATA

To look at the details of the transaction, run: 
    
    
    [gcloud dns record-sets transaction describe](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe) --zone=MANAGED_ZONE

To delete the transaction, run: 
    
    
    [gcloud dns record-sets transaction abort](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort) --zone=MANAGED_ZONE

To execute the transaction, run: 
    
    
    [gcloud dns record-sets transaction execute](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/execute) --zone=MANAGED_ZONE

FLAGS
    

`--transaction-file`=`TRANSACTION_FILE`; default="transaction.yaml"
     Path of the file which contains the transaction. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[abort](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort)`
     Abort transaction. 
`[add](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add)`
     Append a record-set addition to the transaction. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe)`
     Describe the transaction. 
`[execute](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/execute)`
     Execute the transaction on Cloud DNS. 
`[remove](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove)`
     Append a record-set deletion to the transaction. 
`[start](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/start)`
     Start a transaction. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha dns record-sets transaction](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/transaction)
    
    
    [gcloud beta dns record-sets transaction](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/record-sets/transaction)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
