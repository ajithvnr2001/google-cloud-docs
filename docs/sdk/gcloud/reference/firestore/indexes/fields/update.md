---
url: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update/
title: gcloud firestore indexes fields update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:01:24.718187+00:00
---

# gcloud firestore indexes fields update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud firestore indexes fields update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud firestore indexes fields update - update the index configuration of the given field 
SYNOPSIS
    

`gcloud firestore indexes fields update` (`FIELD` : `--collection-group`=`COLLECTION_GROUP` `--database`=`DATABASE`) (`--clear-exemption` | `--disable-indexes` | `--index`=[`KEY`=`VALUE`,…]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the index configuration of the given field. 

This creates an exemption for the field in question, allowing one to modify the field's index settings and override the defaults. 

EXAMPLES
     The following command creates an exemption for the `timestamp` field in the `Events` collection group, in which all indexes are disabled: 
    
    
    gcloud firestore indexes fields update timestamp --collection-group=Events --disable-indexes
    
    
    gcloud firestore indexes fields update timestamp --database=(default) --collection-group=Events --disable-indexes

The following command creates an exemption for the `timestamp` field in the `Events` collection group, in which the list of indexes is explicitly set to [ASCENDING, DESCENDING]: 
    
    
    gcloud firestore indexes fields update timestamp --collection-group=Events --index=order=ASCENDING --index=order=DESCENDING

The following command clears the exemption on the `timestamp` field in the `Events` collection group, so that the field will return to inheriting its index settings from its ancestors: 
    
    
    gcloud firestore indexes fields update timestamp --collection-group=Events --clear-exemption

POSITIONAL ARGUMENTS
    

Field resource - Field to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `field` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FIELD`
     ID of the field or fully qualified identifier for the field. 

To set the `field` attribute: 

  * provide the argument `field` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--collection-group`=`COLLECTION_GROUP`
     Collection group of the field. To set the `collection-group` attribute: 

  * provide the argument `field` on the command line with a fully specified name; 
  * provide the argument `--collection-group` on the command line. 


`--database`=`DATABASE`
     Database of the field. To set the `database` attribute: 

  * provide the argument `field` on the command line with a fully specified name; 
  * provide the argument `--database` on the command line; 
  * the default value of argument [--database] is `(default)`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--clear-exemption`
     If provided, the field's current index configuration will be reverted to inherit from its ancestor index configurations. 
`--disable-indexes`
     If provided, the field will no longer be indexed at all. 
`--index`=[`KEY`=`VALUE`,…]
     An index for the field. 

This flag can be repeated to provide multiple indexes. Any existing indexes will be overwritten with the ones provided. Any omitted indexes will be deleted if they currently exist. 

The following keys are allowed: 

`order`
     Specifies the order. Valid options are: 'ascending', 'descending'. Exactly one of 'order' or 'array-config' must be specified. 
`array-config`
     Specifies the configuration for an array field. The only valid option is 'contains'. Exactly one of 'order' or 'array-config' must be specified. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `firestore/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/firestore>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha firestore indexes fields update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/indexes/fields/update)
    
    
    [gcloud beta firestore indexes fields update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/indexes/fields/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
