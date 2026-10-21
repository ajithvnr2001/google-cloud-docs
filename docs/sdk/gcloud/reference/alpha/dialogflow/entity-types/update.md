---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dialogflow/entity-types/update/
title: gcloud alpha dialogflow entity-types update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:07:29.227978+00:00
---

# gcloud alpha dialogflow entity-types update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dialogflow/entity-types/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dialogflow entity-types update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dialogflow entity-types update - update a Dialogflow entity type 
SYNOPSIS
    

`gcloud alpha dialogflow entity-types update` `ENTITY_TYPE` [`--auto-expand`] [`--display-name`=`DISPLAY_NAME`] [`--add-entities`=`ADD_ENTITIES` `--clear-entities` | `--remove-entities`=[`REMOVE_ENTITIES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Dialogflow entity type. 
EXAMPLES
     To update the display name of an entity type: 
    
    
    gcloud alpha dialogflow entity-types update --display-name="color"

POSITIONAL ARGUMENTS
    

EntityType resource - Entity type to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entity_type` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENTITY_TYPE`
     ID of the entityType or fully qualified identifier for the entityType. 

To set the `entity_type` attribute: 

  * provide the argument `entity_type` on the command line. 


FLAGS
    

`--auto-expand`
     Whether or not the entity type can be automatically expanded to idenitify entities not explicitly included. 
`--display-name`=`DISPLAY_NAME`
     A human readable name for the entity type. 
Use these flags for adding and removing entities: 
`--add-entities`=`ADD_ENTITIES`
     Comma separated list of entities, or a map of entities to synonyms, to be added to existing list of entities. 

If specified with `--remove-entities` or `--clear-entities`, entities will be removed in a separate request before entities are added. If an entity with a given value exists, it will be overwritten. 

If a list, the entities can contain references to other entity types (with or without aliases). 

To specify a map, set this flag with `--flags-file` as a map, where each key is the canonical name and each value is a list of synonyms to map to the canonical name. The canonical name must be explicitly included in the list of synonyms. For more information on `--flags-file`, see `gcloud topics flags-file`. 

For example, use `--flags-file=flags.yaml`, where `flags.yaml` contains: 
    
    
    --entities:
      red:
      - red
      - cherry
      - rose
      blue:
      - blue
      - azure
      - cyan

For more information, see <https://cloud.google.com/dialogflow-enterprise/docs/reference/rest/v2/Entity>. 

At most one of these can be specified: 

`--clear-entities`
     If true, remove all existing entities. 

Can be used with `--add-entities` to replace existing entities. 

`--remove-entities`=[`REMOVE_ENTITIES`,…]
     A comma separated list of entities to be removed. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dialogflow/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/dialogflow/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
