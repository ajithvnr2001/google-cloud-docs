---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import/
title: gcloud dns record-sets import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:49.516985+00:00
---

# gcloud dns record-sets import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dns record-sets import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dns record-sets import - import record-sets into your managed-zone 
SYNOPSIS
    

`gcloud dns record-sets import` `RECORDS_FILE` `--zone`=`ZONE`, `-z` `ZONE` [`--delete-all-existing`] [`--location`=`LOCATION`] [`--replace-origin-ns`] [`--skip-soa-update`] [`--zone-file-format`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command imports record-sets contained within the specified record-sets file into your managed-zone. Note that NS records for the origin of the zone and the SOA NS field are not imported since name-servers are managed by Cloud DNS. By default, record-sets cannot be imported if there are any conflicts. A conflict exists if an existing record-set has the same name and type as a record-set that is being imported. In contrast, if the --delete-all-existing flag is used, the imported record-sets will replace all the records-sets currently in the managed-zone. 
EXAMPLES
     To import record-sets from a yaml record-sets file, run: 
    
    
    gcloud dns record-sets import YAML_RECORDS_FILE --zone=MANAGED_ZONE

To import record-sets from a zone file, run: 
    
    
    gcloud dns record-sets import ZONE_FILE --zone-file-format --zone=MANAGED_ZONE

To replace all the record-sets in your zone with records from a yaml file, run: 
    
    
    gcloud dns record-sets import YAML_RECORDS_FILE --delete-all-existing --zone=MANAGED_ZONE

POSITIONAL ARGUMENTS
    

`RECORDS_FILE`
     File from which record-sets should be imported. For examples of YAML-formatted and BIND zone-formatted records files, refer to <https://cloud.google.com/dns/records#importing_and_exporting_record_sets>
REQUIRED FLAGS
    

`--zone`=`ZONE`, `-z` `ZONE`
     Name of the managed zone whose record sets you want to manage. 
OPTIONAL FLAGS
    

`--delete-all-existing`
     Indicates that all existing record-sets should be deleted before importing the record-sets in the records-file. 
`--location`=`LOCATION`
     Specifies the desired service location the request is sent to. Defaults to Cloud DNS global service. Use --location=global if you want to target the global service. 
`--replace-origin-ns`
     Indicates that NS records for the origin of a zone should be imported if defined 
`--skip-soa-update`
     Skip incrementing the serial number of the SOA record when making changes to the record-sets. 
`--zone-file-format`
     Indicates that the input records-file is in BIND zone format. If omitted, indicates that the records-file is in YAML format. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dns record-sets import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/record-sets/import)
    
    
    [gcloud beta dns record-sets import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/record-sets/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
