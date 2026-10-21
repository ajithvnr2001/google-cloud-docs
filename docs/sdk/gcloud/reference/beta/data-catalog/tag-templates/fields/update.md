---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/tag-templates/fields/update/
title: gcloud beta data-catalog tag-templates fields update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:44.172335+00:00
---

# gcloud beta data-catalog tag-templates fields update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/tag-templates/fields/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta data-catalog tag-templates fields update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta data-catalog tag-templates fields update - update a Data Catalog tag template field 
SYNOPSIS
    

`gcloud beta data-catalog tag-templates fields update` (`FIELD` : `--location`=`LOCATION` `--tag-template`=`TAG_TEMPLATE`) [`--display-name`=`DISPLAY_NAME`] [`--enum-values`=[`ENUM_VALUES`,…]] [`--required`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex aspect-types](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead. 

Update a Data Catalog tag template field. 

EXAMPLES
     Update the display name of a tag template field: 
    
    
    gcloud beta data-catalog tag-templates fields update FIELD --display-name=NAME

Set tag template enum field values to be 'A' and 'B': 
    
    
    gcloud beta data-catalog tag-templates fields update FIELD --enum-values=A,B

Set a tag template field to be optional: 
    
    
    gcloud beta data-catalog tag-templates fields update FIELD --no-required

POSITIONAL ARGUMENTS
    

Tag template field resource - Tag template field to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `field` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FIELD`
     ID of the tag template field or fully qualified identifier for the tag template field. 

To set the `field` attribute: 

  * provide the argument `field` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the tag template field. To set the `location` attribute: 

  * provide the argument `field` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--tag-template`=`TAG_TEMPLATE`
     Tag template of the tag template field. To set the `tag-template` attribute: 

  * provide the argument `field` on the command line with a fully specified name; 
  * provide the argument `--tag-template` on the command line. 


FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name of the tag template field. 
`--enum-values`=[`ENUM_VALUES`,…]
     Comma-separated list of enum values. The list of enum values passed with this flag replaces the existing one in tag template enum field. That means: 

  * the enum values passed to the flag and not present in tag template enum field get created 
  * the enum values present in tag template enum field and missing in the list get removed 
  * the order of the items on the list is preserved 



Enum values can only be removed from optional enum fields for now. 

`--required`
     Indicates if the tag template field is required. Updating from FALSE (optional) to TRUE (required) is NOT allowed. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud data-catalog tag-templates fields update](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update)
    
    
    [gcloud alpha data-catalog tag-templates fields update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/tag-templates/fields/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
