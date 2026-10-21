---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/tag-templates/fields/enum-values/rename/
title: gcloud alpha data-catalog tag-templates fields enum-values rename \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:01:43.463683+00:00
---

# gcloud alpha data-catalog tag-templates fields enum-values rename  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/tag-templates/fields/enum-values/rename/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha data-catalog tag-templates fields enum-values rename Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha data-catalog tag-templates fields enum-values rename - rename an enum value in Data Catalog tag template enum field 
SYNOPSIS
    

`gcloud alpha data-catalog tag-templates fields enum-values rename` (`ENUM_VALUE` : `--field`=`FIELD` `--location`=`LOCATION` `--tag-template`=`TAG_TEMPLATE`) `--new-id`=`NEW_ID` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex aspect-types](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead. 

Rename an enum value in Data Catalog tag template enum field. 

EXAMPLES
     Rename an enum value in tag template enum field: 
    
    
    [gcloud alpha data-catalog tag-templates fields enum-values](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/tag-templates/fields/enum-values) rename ENUM_VALUE --new-id="new-id"

POSITIONAL ARGUMENTS
    

Enum value resource - Enum value to rename. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `enum_value` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENUM_VALUE`
     ID of the enum value or fully qualified identifier for the enum value. 

To set the `enum_value` attribute: 

  * provide the argument `enum_value` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--field`=`FIELD`
     Tag template field that contains enum value. To set the `field` attribute: 

  * provide the argument `enum_value` on the command line with a fully specified name; 
  * provide the argument `--field` on the command line. 


`--location`=`LOCATION`
     Location of the enum value. To set the `location` attribute: 

  * provide the argument `enum_value` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--tag-template`=`TAG_TEMPLATE`
     Tag template that contains enum value. To set the `tag-template` attribute: 

  * provide the argument `enum_value` on the command line with a fully specified name; 
  * provide the argument `--tag-template` on the command line. 


REQUIRED FLAGS
    

`--new-id`=`NEW_ID`
     New display name of the enum value. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud data-catalog tag-templates fields enum-values rename](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename)
    
    
    [gcloud beta data-catalog tag-templates fields enum-values rename](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/tag-templates/fields/enum-values/rename)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
