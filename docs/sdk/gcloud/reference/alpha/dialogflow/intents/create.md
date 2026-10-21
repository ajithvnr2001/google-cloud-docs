---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dialogflow/intents/create/
title: gcloud alpha dialogflow intents create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:07:30.165033+00:00
---

# gcloud alpha dialogflow intents create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dialogflow/intents/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dialogflow intents create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dialogflow intents create - create a Dialogflow entity type for the agent of the current project 
SYNOPSIS
    

`gcloud alpha dialogflow intents create` `--display-name`=`DISPLAY_NAME` [`--is-fallback`] [`--no-ml-enabled`] [`--other-properties`=[`KEY`=`VALUE`,…]] [`--priority`=`PRIORITY`] [`--responses`=[`RESPONSES`,…]] [`--training-phrases`=[`TRAINING_PHRASES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Dialogflow intent for the agent of the current project. 
EXAMPLES
     To create an intent with a training phrase and a response: 
    
    
    gcloud alpha dialogflow intents create --display-name="test-intent" --priority=1 --training-phrases="example query" --responses="example response"

REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Human-readable name for the intent. 
OPTIONAL FLAGS
    

`--is-fallback`
     If true, set this intent as a fallback intent. 
`--ml-enabled`
     If true, enable machine learning for the intent. Enabled by default, use `--no-ml-enabled` to disable. 
`--other-properties`=[`KEY`=`VALUE`,…]
     Map containing other properties to set on the intent. 

For more information on available properties, see: <https://cloud.google.com/dialogflow-enterprise/docs/reference/rest/v2/projects.agent.intents>

To set complex types, specify this flag with `--flags-file`. For more information, see `gcloud topics flags-file`. 

Other flags take precedence over properties specified here. 

`--priority`=`PRIORITY`
     Priority of the intent. 

Higher numbers represent higher priorities. Zero or negative numbers mean that the intent is disabled. Default priority is 500000. 

`--responses`=[`RESPONSES`,…]
     Comma separated list of simple text responses to send to the user. 
`--training-phrases`=[`TRAINING_PHRASES`,…]
     List of examples or templates. 

Can be provided as comma separated unannotated examples or as a list training phrase objects. To provide training phrase objects, specify the flag with `--flags-file`. 

For example, use `--flags-file=flags.yaml`, where `flags.yaml` contains: 
    
    
    --training-phrases:
      - type: TEMPLATE
        parts:
        - text: I love the color
        - text: red
          entityType: <entity_type_id>
          alias: color

For more information on training phrases, see: <https://cloud.google.com/dialogflow-enterprise/docs/reference/rest/Shared.Types/Intent#TrainingPhrase>

For more information on `--flags-file`, see `gcloud topics flags-file`. 

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
