---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entries/remove-aspects/
title: gcloud alpha dataplex entries remove-aspects \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:39.971845+00:00
---

# gcloud alpha dataplex entries remove-aspects  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entries/remove-aspects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex entries remove-aspects Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex entries remove-aspects - remove aspects from a Dataplex Entry 
SYNOPSIS
    

`gcloud alpha dataplex entries remove-aspects` (`ENTRY` : `--entry-group`=`ENTRY_GROUP` `--location`=`LOCATION`) `--keys`=[`ASPECT_TYPE`@`PATH`,…] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Remove aspects from a Dataplex Entry. 
EXAMPLES
     To remove all aspects of type `test-project.us-central1.some-aspect-type` from the entry, run: 
    
    
    gcloud alpha dataplex entries remove-aspects entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --keys='test-project.us-central1.some-aspect-type@*'

To remove all aspects on path `Schema.column1` from the entry, run: 
    
    
    gcloud alpha dataplex entries remove-aspects entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --keys='*@Schema.column1'

To remove exact aspects `test-project.us-central1.some-aspect-type@Schema.column1` and `test-project.us-central1.some-aspect-type2@Schema.column2` from the entry, run: 
    
    
    gcloud alpha dataplex entries remove-aspects entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --keys=test-project.us-central1.some-aspect-type@Schema.column1,test-project.us-central2.some-aspect-type@Schema.column2

POSITIONAL ARGUMENTS
    

Entry resource - Arguments and flags that define the Dataplex Entry you want to reference. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENTRY`
     ID of the entry or fully qualified identifier for the entry. 

To set the `entry` attribute: 

  * provide the argument `entry` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--entry-group`=`ENTRY_GROUP`
     Entry group containing Dataplex Entries. To set the `entry-group` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--entry-group` on the command line. 


`--location`=`LOCATION`
     Location of the Dataplex resource. To set the `location` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

`--keys`=[`ASPECT_TYPE`@`PATH`,…]
     List of Aspect keys, identifying Aspects to remove from the entry. 

Keys are in the format ``ASPECT_TYPE@PATH``, or just ``ASPECT_TYPE``, if the Aspect is attached to an entry itself rather than to a specific column defined in the schema. 

``ASPECT_TYPE`` is expected to be in a format ``PROJECT_ID.LOCATION.ASPECT_TYPE_ID`` or a wildcard `*`, which targets all aspect types. 

``PATH`` can be either empty (which means a 'root' path, such that Aspect is attached to the entry itself), point to a specific column defined in the schema (for example: `Schema.some_column`) or a wildcard `*` (target all paths). 

``ASPECT_TYPE`` and ``PATH`` cannot be both specified as wildcards `*`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex entries remove-aspects](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
