---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entry-links/update-aspects/
title: gcloud alpha dataplex entry-links update-aspects \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:42.485650+00:00
---

# gcloud alpha dataplex entry-links update-aspects  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entry-links/update-aspects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex entry-links update-aspects Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex entry-links update-aspects - add or update one aspect for a Dataplex Entry Link 
SYNOPSIS
    

`gcloud alpha dataplex entry-links update-aspects` (`ENTRY_LINK` : `--entry-group`=`ENTRY_GROUP` `--location`=`LOCATION`) `--aspects`=`YAML_OR_JSON_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Add or update one aspect for a Dataplex Entry Link. 
EXAMPLES
     To add or update an aspect for the Dataplex entry link `entrylink1` within the entry group `entry-group1` in location `us-central1` from a YAML/JSON file, run: 
    
    
    gcloud alpha dataplex entry-links update-aspects entrylink1 --project=test-project --location=us-central1 --entry-group entry-group1 --aspects=path-to-a-file-with-aspect.json

POSITIONAL ARGUMENTS
    

Entry link resource - Arguments and flags that define the Dataplex entry link you want to update aspects The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entry_link` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENTRY_LINK`
     ID of the entry link or fully qualified identifier for the entry link. 

To set the `entry-link` attribute: 

  * provide the argument `entry_link` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--entry-group`=`ENTRY_GROUP`
     The name of entry link to use. 

To set the `entry-group` attribute: 

  * provide the argument `entry_link` on the command line with a fully specified name; 
  * provide the argument `--entry-group` on the command line. 


`--location`=`LOCATION`
     The location of the Dataplex resource. 

To set the `location` attribute: 

  * provide the argument `entry_link` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

`--aspects`=`YAML_OR_JSON_FILE`
     Path to a YAML or JSON file containing Aspects to add or update for the EntryLink. 

When this flag is specified, only Aspects referenced in the file are going to be added or updated. This does not remove other Aspects from the EntryLink. 

The file content must be a map where keys are in the format ``ASPECT_TYPE``. Paths are not allowed in the keys for EntryLink aspects. 

Values in the map represent the Aspect's content, which must conform to the template defined for the given ``ASPECT_TYPE``. Each Aspect is fully replaced. 

``ASPECT_TYPE`` must be in the format ``PROJECT_ID.LOCATION.ASPECT_TYPE_ID``. 

Example YAML format: 
    
    
      project-id1.us-central1.my-aspect-type1:
        data:
          aspectField1: someValue
          aspectField2: someOtherValue

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
