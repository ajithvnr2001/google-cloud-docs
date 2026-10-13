---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-properties/
title: Manage gdcloud CLI properties \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:37.874288+00:00
---

# Manage gdcloud CLI properties  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage gdcloud CLI properties Stay organized with collections  Save and categorize content based on your preferences. 

Properties are settings that govern the behavior of the gdcloud CLI.

Use properties to define settings on an organization and/or a project context such as the organization console URL and project used by the gdcloud CLI for authentication, the information to use when working with Object Storage service, or the option to turn off automatic gdcloud CLI component update checks. For more details about organization and project context, see [View and switch context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-context). Properties can also be used to define gdcloud CLI preferences like accessibility configuration for gdcloud CLI commands.

## Properties and flags

The gdcloud CLI supports command flags that have the same effect as gdcloud CLI properties. Properties allow you to maintain the same settings across command executions while flags affect command behavior on a per-invocation basis. Note that flags override properties when both are set.

## Configurations

A [configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-configurations) is a named set of gdcloud CLI properties. The gdcloud CLI uses a configuration named `default` as the initial active configuration. The `default` configuration is suitable for most use cases. However, you can also create additional configurations and switch between them as required.

## List properties

To list the properties in the active [configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-configurations), run:
    
    
    gdcloud config list
    

## Set properties

To set a property in the active configuration, run `gdcloud config set`. The following example sets the `project` property, where `PROJECT_ID` is the unique ID for your project.
    
    
    gdcloud config set project PROJECT_ID
    

To set properties that are not in the `core` properties section, you must specify the section followed by a forward slash before the property name. The following example sets the `screen_reader` property in the `accessibility` section:
    
    
    gdcloud config set accessibility/screen_reader true
    

## Available properties

The list of all properties can be found by running `gdcloud topic configurations` command and looking for the Available Properties section. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
