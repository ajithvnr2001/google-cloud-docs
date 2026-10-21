---
url: https://docs.cloud.google.com/sdk/docs/properties/
title: Managing gcloud CLI properties \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:42.351796+00:00
---

# Managing gcloud CLI properties  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Managing gcloud CLI properties Stay organized with collections  Save and categorize content based on your preferences. 

Properties are settings that govern the behavior of the gcloud CLI.

You can use properties to define a per-product or per-service setting such as the account used by the gcloud CLI for authorization, the default region to use when working with Compute Engine resources, or the option to turn off automatic gcloud CLI component update checks. Properties can also be used to define gcloud CLI preferences like verbosity level and prompt configuration for gcloud CLI commands.

## Properties and flags

The gcloud CLI supports some [global flags](https://docs.cloud.google.com/sdk/gcloud/reference) and command flags that have the same effect as gcloud CLI properties. For example, the gcloud CLI supports both the `--project` flag and `project` property. Properties allow you to maintain the same settings across command executions while flags affect command behavior on a per-invocation basis. Note that flags override properties when both are set.

## Configurations

A [configuration](https://docs.cloud.google.com/sdk/docs/configurations) is a named set of gcloud CLI properties. The gcloud CLI uses a configuration named `default` as the initial active configuration. The `default` configuration is suitable for most use cases. However, you can also create additional configurations and switch between them as required.

## Listing properties

To list the properties in the active [configuration](https://docs.cloud.google.com/sdk/docs/configurations), run [`gcloud config list`](https://docs.cloud.google.com/sdk/gcloud/reference/config/list):
    
    
    gcloud config list
    

The gcloud CLI returns the list of properties:
    
    
    [compute]
    region = us-east1
    zone = us-east1-d
    [core]
    account = user@google.com
    disable_usage_reporting = False
    project = example-project
    [metrics]
    command_name = gcloud.config.list
    

## Setting properties

To set a property in the active configuration, run [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). The following example sets the [`project`](https://docs.cloud.google.com/sdk/gcloud/reference#--project) property, where PROJECT_ID is the unique ID for your project.
    
    
    gcloud config set project PROJECT_ID
    

To set properties that are not in the [`core`](https://docs.cloud.google.com/sdk/docs/properties#core) properties section, you must specify the section followed by a forward slash before the property name. The following example sets the zone name to `us-east1-b`.
    
    
    gcloud config set compute/zone us-east1-b
    

## Setting properties using environment variables

You can also set properties using environment variables. Each property has a corresponding environment variable that can be used to set it. The name of the environment variable follows the `CLOUDSDK_SECTION_NAME_PROPERTY_NAME` pattern. For example, you can set the `core/project` and `compute/zone` properties as follows:
    
    
    CLOUDSDK_CORE_PROJECT=PROJECT_NAME
    
    CLOUDSDK_COMPUTE_ZONE=ZONE_NAME
    

**Note:** The environment variable values take precedence over property values set using [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).

## Unsetting properties

To unset a property in the active configuration, use [`gcloud config unset`](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset):
    
    
    gcloud config unset disable_usage_reporting
    

## Available Properties

The list of all properties can be found by running [`gcloud topic configurations`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) or [`gcloud config set --help`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) and looking for the Available Properties section.

## What's next

  * Read [gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/configurations) to learn more about configurations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
