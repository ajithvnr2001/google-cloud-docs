---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/objects/compose/
title: gcloud alpha storage objects compose \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:58:18.776898+00:00
---

# gcloud alpha storage objects compose  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/objects/compose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage objects compose Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage objects compose - concatenate a sequence of objects into a new composite object 
SYNOPSIS
    

`gcloud alpha storage objects compose` `SOURCE` [`SOURCE` …] `DESTINATION` [`--additional-headers`=`HEADER`=`VALUE`] [`--delete-source-objects`] [`--clear-custom-contexts` | `--custom-contexts`=[`CUSTOM_CONTEXTS_KEYS_AND_VALUES`,…] | `--custom-contexts-file`=`CUSTOM_CONTEXTS_FILE`] [`--if-generation-match`=`GENERATION` `--if-metageneration-match`=`METAGENERATION`] [`--retain-until`=`DATETIME` `--retention-mode`=`RETENTION_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha storage objects compose creates a new object whose content is the concatenation of a given sequence of source objects in the same bucket. For more information, please see: [composite objects documentation](https://cloud.google.com/storage/docs/composite-objects). 

There is a limit (currently 32) to the number of components that can be composed in a single operation. 

EXAMPLES
     The following command creates a new object `target.txt` by concatenating `a.txt` and `b.txt`: 
    
    
    gcloud alpha storage objects compose gs://bucket/a.txt gs://bucket/b.txt gs://bucket/target.txt

Contexts are merged from source objects on the composed object by default. However, the following command overwrites custom contexts on composed object: 
    
    
    gcloud alpha storage objects compose gs://bucket/a.txt gs://bucket/b.txt gs://bucket/target.txt --custom-contexts=key1=value1,key2=value2

The following command creates a new object `target.txt` by concatenating `a.txt` and `b.txt`, and deletes the source objects after a successful composition: 
    
    
    gcloud alpha storage objects compose gs://bucket/a.txt gs://bucket/b.txt gs://bucket/target.txt --delete-source-objects

POSITIONAL ARGUMENTS
    

`SOURCE` [`SOURCE` …]
     The list of source objects that will be concatenated into a single object. 
`DESTINATION`
     The destination object. 
FLAGS
    

`--additional-headers`=`HEADER`=`VALUE`
     Includes arbitrary headers in storage API calls. Accepts a comma separated list of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides the default `storage/additional_headers` property value for this command invocation. 
`--delete-source-objects`
     If set, the source objects will be deleted after a successful composition. Note that this deletion bypasses the soft delete policy if configured on the bucket. 
OBJECT CONTEXTS FLAGS
    

Group that allow users to handle object contexts. 

At most one of these can be specified: 

`--clear-custom-contexts`
     Clears all custom contexts on objects. 
`--custom-contexts`=[`CUSTOM_CONTEXTS_KEYS_AND_VALUES`,…]
     Sets custom contexts on objects. The existing custom contexts (if any) would be overwritten. 
`--custom-contexts-file`=`CUSTOM_CONTEXTS_FILE`
     Path to a local JSON or YAML file containing custom contexts one wants to set on an object. For example: 

1\. The following JSON document shows two key value pairs, i.e. (key1, value1) and (key2, value2): 
    
    
      {
        "key1": {"value": "value1"},
        "key2": {"value": "value2"}
      }

2\. The following YAML document shows two key value pairs, i.e. (key1, value1) and (key2, value2): 
    
    
      key1:
        value: value1
      key2:
        value: value2

Note: Currently object contexts only supports string format for values. 

PRECONDITION FLAGS
    

`--if-generation-match`=`GENERATION`
     Execute only if the generation matches the generation of the requested object. 
`--if-metageneration-match`=`METAGENERATION`
     Execute only if the metageneration matches the metageneration of the requested object. 
RETENTION FLAGS
    

`--retain-until`=`DATETIME`
     Ensures the destination object is retained until the specified time in RFC 3339 format. 
`--retention-mode`=`RETENTION_MODE`
     Sets the destination object retention mode to either "Locked" or "Unlocked". When retention mode is "Locked", the retain until time can only be increased. `RETENTION_MODE` must be one of: `Locked`, `Unlocked`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage objects compose](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/compose)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
