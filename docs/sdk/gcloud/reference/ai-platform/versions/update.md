---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/versions/update/
title: gcloud ai-platform versions update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:49:28.848226+00:00
---

# gcloud ai-platform versions update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/versions/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai-platform versions update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai-platform versions update - update an AI Platform version 
SYNOPSIS
    

`gcloud ai-platform versions update` (`VERSION` : `--model`=`MODEL`) [`--config`=`YAML_FILE`] [`--description`=`DESCRIPTION`] [`--region`=`REGION`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an AI Platform version. 
POSITIONAL ARGUMENTS
    

Version resource - The AI Platform model to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `version` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`VERSION`
     ID of the version or fully qualified identifier for the version. 

To set the `version` attribute: 

  * provide the argument `version` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--model`=`MODEL`
     Model for the version. 

To set the `model` attribute: 

  * provide the argument `version` on the command line with a fully specified name; 
  * provide the argument `--model` on the command line. 


FLAGS
    

`--config`=`YAML_FILE`
     Path to a YAML configuration file containing configuration parameters for the [version](https://cloud.google.com/ml/reference/rest/v1/projects.models.versions) to create. 

The file is in YAML format. Note that not all attributes of a version are configurable; available attributes (with example values) are: 
    
    
    description: A free-form description of the version.
    manualScaling:
      nodes: 10  # The number of nodes to allocate for this model.
    autoScaling:
      minNodes: 0  # The minimum number of nodes to allocate for this model.
      maxNodes: 1  # The maxinum number of nodes to allocate for this model.
    requestLoggingconfig:
      bigqueryTableName: someTable  # Fully qualified BigQuery table name.
      samplingPercentage: 0.5  # Percentage of requests to be logged.

The name of the version must always be specified via the required VERSION argument. 

Only one of manualScaling or autoScaling can be specified. If both are specified in same yaml file, an error will be returned. 

Labels cannot currently be set in the config.yaml; please use the command-line flags to alter them. 

If an option is specified both in the configuration file and via command-line arguments, the command-line arguments override the configuration file. 

`--description`=`DESCRIPTION`
     Description of the version. 
`--region`=`REGION`
     Google Cloud region of the regional endpoint to use for this command. For the global endpoint, the region needs to be specified as `global`. 

Learn more about regional endpoints and see a list of available regions: <https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints>

`REGION` must be one of: `global`, `asia-east1`, `asia-northeast1`, `asia-southeast1`, `australia-southeast1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `northamerica-northeast1`, `us-central1`, `us-east1`, `us-east4`, `us-west1`. 

`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud ai-platform versions update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud ai-platform versions update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai-platform versions update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update)
    
    
    [gcloud beta ai-platform versions update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/versions/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
