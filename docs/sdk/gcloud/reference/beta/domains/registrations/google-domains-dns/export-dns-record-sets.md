---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/domains/registrations/google-domains-dns/export-dns-record-sets/
title: gcloud beta domains registrations google-domains-dns export-dns-record-sets \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:26.312775+00:00
---

# gcloud beta domains registrations google-domains-dns export-dns-record-sets  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/domains/registrations/google-domains-dns/export-dns-record-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta domains registrations google-domains-dns export-dns-record-sets Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta domains registrations google-domains-dns export-dns-record-sets - export your registration's Google Domains DNS zone's record-sets into a file 
SYNOPSIS
    

`gcloud beta domains registrations google-domains-dns export-dns-record-sets` `REGISTRATION` `--records-file`=`RECORDS_FILE` [`--zone-file-format`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Export your registration's Google Domains DNS (deprecated) zone's record-sets into a file. The formats you can export to are YAML records format (default) and BIND zone file format. 
EXAMPLES
     To export DNS record-sets of ``example.com`` into a YAML file, run: 
    
    
    [gcloud domains registrations google-domains-dns](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns) export-dns-record-sets example.com --records-file=records.yaml

To export DNS record-sets of ``example.com`` into a BIND zone formatted file, run: 
    
    
    [gcloud domains registrations google-domains-dns](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns) export-dns-record-sets example.com --records-file=records.zonefile --zone-file-format

POSITIONAL ARGUMENTS
    

Registration resource - The domain registration to get the DNS records for. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `registration` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `registration` on the command line with a fully specified name; 
  * location is always global. 



This must be specified. 

`REGISTRATION`
     ID of the registration or fully qualified identifier for the registration. 

To set the `registration` attribute: 

  * provide the argument `registration` on the command line. 


REQUIRED FLAGS
    

`--records-file`=`RECORDS_FILE`
     File to which record-sets should be exported. 
OPTIONAL FLAGS
    

`--zone-file-format`
     Indicates that records-file should be in the zone file format. When using this flag, expect the record-set to be exported to a BIND zone formatted file. If you omit this flag, the record-set is exported into a YAML formatted records file. Note, this format flag determines the format of the output recorded in the records-file; it is different from the global `--format` flag which affects console output alone. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud domains registrations google-domains-dns](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns) export-dns-record-sets
    
    
    [gcloud alpha domains registrations google-domains-dns](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/domains/registrations/google-domains-dns) export-dns-record-sets

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
