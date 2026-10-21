---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/tag-templates/create/
title: gcloud beta data-catalog tag-templates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:42.656880+00:00
---

# gcloud beta data-catalog tag-templates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/tag-templates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta data-catalog tag-templates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta data-catalog tag-templates create - create a Data Catalog tag template 
SYNOPSIS
    

`gcloud beta data-catalog tag-templates create` (`TAG_TEMPLATE` : `--location`=`LOCATION`) `--field`=[`id`=`ID`,`type`=`TYPE`,`display-name`=`DISPLAY_NAME`,`required`=`REQUIRED`,…] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex aspect-types](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead. 

Create a Data Catalog tag template. 

EXAMPLES
     Create a string tag template with a required string field: 
    
    
    gcloud beta data-catalog tag-templates create TEMPLATE --field=id=ID,display-name=DISPLAY,type=string,required=TRUE

Create an enum tag template with an optional enum field with values 'A' and 'B': 
    
    
    gcloud beta data-catalog tag-templates create TEMPLATE --field=id=ID,display-name=DISPLAY,type='enum(A|B)'

Create a tag template with a optional string field and a required enum field with values 'A' and 'B': 
    
    
    gcloud beta data-catalog tag-templates create TEMPLATE --field=id=ID1,display-name=DISPLAY1,type=string --field=id=ID2,display-name=DISPLAY2,type='enum(A|B)',required=TRUE

POSITIONAL ARGUMENTS
    

Tag template resource - Tag template to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `tag_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TAG_TEMPLATE`
     ID of the tag template or fully qualified identifier for the tag template. 

To set the `tag_template` attribute: 

  * provide the argument `tag_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the tag template. To set the `location` attribute: 

  * provide the argument `tag_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--field`=[`id`=`ID`,`type`=`TYPE`,`display-name`=`DISPLAY_NAME`,`required`=`REQUIRED`,…]
     Specification for a tag template field. This flag can be repeated to specify multiple fields. The following keys are allowed: 
    
    
    *id*::: (Required) ID of the tag template field.
    
    
    *type*::: (Required) Type of the tag template field. Choices are
        double, string, bool, timestamp, and enum.
    
    
    To specify a string field:
      `type=string`
    
    
    To specify an enum field with values 'A' and 'B':
      `type=enum(A|B)`
    
    
    *display-name*::: Display name of the tag template field.
    
    
    *required*::: Indicates if the tag template field is required.
        Defaults to FALSE.

OPTIONAL FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Human-readable name for the tag template. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud data-catalog tag-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create)
    
    
    [gcloud alpha data-catalog tag-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/tag-templates/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
