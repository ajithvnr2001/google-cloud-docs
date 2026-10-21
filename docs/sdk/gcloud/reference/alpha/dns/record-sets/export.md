---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/export/
title: gcloud alpha dns record-sets export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:37.469152+00:00
---

# gcloud alpha dns record-sets export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dns record-sets export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dns record-sets export - export your record-sets into a file 
SYNOPSIS
    

`gcloud alpha dns record-sets export` `RECORDS_FILE` `--zone`=`ZONE`, `-z` `ZONE` [`--location`=`LOCATION`] [`--zone-file-format`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command exports the record-sets contained within the specified managed-zone into a file. The formats you can export to are YAML records format (default) and BIND zone file format. 
EXAMPLES
     To export record-sets into a yaml file, run: 
    
    
    gcloud alpha dns record-sets export records.yaml --zone=examplezonename

To export record-sets into a BIND zone formatted file instead, run: 
    
    
    gcloud alpha dns record-sets export pathto.zonefile --zone=examplezonename --zone-file-format

Similarly, to import record-sets into a BIND zone formatted zone file, run: 
    
    
    [gcloud dns record-sets import](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import) pathto.zonefile --zone-file-format --zone=examplezonename

POSITIONAL ARGUMENTS
    

`RECORDS_FILE`
     File to which record-sets should be exported. 
REQUIRED FLAGS
    

`--zone`=`ZONE`, `-z` `ZONE`
     Name of the managed zone whose record sets you want to manage. 
OPTIONAL FLAGS
    

`--location`=`LOCATION`
     Specifies the desired service location the request is sent to. Defaults to Cloud DNS global service. Use --location=global if you want to target the global service. 
`--zone-file-format`
     Indicates that records-file should be in the zone file format. When using this flag, expect the record-set to be exported to a BIND zone formatted file. If you omit this flag, the record-set is exported into a YAML formatted records file. Note, this format flag determines the format of the output recorded in the records-file; it is different from the global `--format` flag which affects console output alone. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dns record-sets export](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/export)
    
    
    [gcloud beta dns record-sets export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/record-sets/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
