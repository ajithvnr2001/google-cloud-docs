---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-manage-configurations/
title: Manage gdcloud CLI configurations \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:00:03.006903+00:00
---

# Manage gdcloud CLI configurations  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-manage-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage gdcloud CLI configurations Stay organized with collections  Save and categorize content based on your preferences. 

A configuration is a named set of Distributed Cloud CLI properties. These properties are key-value pairs, organized in sections, that govern the behavior of the gdcloud CLI.

**Tip:** If you work with just one project, the default configuration, named `default`, should be sufficient. To learn more about setting properties in a configuration to define per-organization or per-project settings such as the organization console URL or project to use, accessibility preferences, see [Manage properties](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-manage-properties).

Properties that are commonly stored in configurations include the organization console URL and project ID. Configurations allow you to define and enable these and other settings together as a group.

Configurations are stored in your user config directory, typically `~/.config/gdcloud` on Linux, `$HOME/Library/Application Support/gdcloud` on Mac, and `%AppData%\gdcloud` on Windows. Also, note that the config directory must be write-enabled.

If you have multiple configurations, you can choose to switch between them, or run commands using a specific configuration with the `--configuration` flag. For more about switching configurations, refer to the section on Activate a configuration.

To read about configurations from the command-line and a complete list of available properties and the sections they are in, run `gdcloud topic configurations`.

## Default configuration

The gdcloud CLI initially creates a single configuration named `default`. You can set properties in your configuration by running the `gdcloud init` command or by running `gdcloud config set` directly.

## Multiple configurations

The single `default` configuration is suitable for many use cases. However, you can also create additional configurations and switch between them as required using `gdcloud config configurations activate`. The initial `default` configuration is created as a convenience, and is not required to use. You can name this and any additional configurations however you'd like.

Multiple configurations are useful if you want to:

  * **Use multiple projects** : You can create a separate configuration for each project and switch between them as required.
  * **Use multiple organization console URLs**.
  * **Perform generally independent tasks** : For example, you can use one configuration to work on service A in one project and manage an unrelated service B in another project.



## Create a configuration

To create a configuration, run:
    
    
    gdcloud config configurations create NAME
    

You must activate the new configuration after creation to use it.

## Activate a configuration

Only one of your multiple configurations can be active at a given time. The active configuration is the configuration whose properties will govern the behavior of the gdcloud CLI.

To activate a new configuration or switch to a new active configuration, run:
    
    
    gdcloud config configurations activate NAME
    

`gdcloud config list` will always displays you the properties in your active configuration.

To change the active configuration for a single command invocation, apply the `--configuration` flag for any gdcloud CLI command:
    
    
    gdcloud auth print-identity-token --configuration=CONFIGURATION
    

## List configurations

To list the configurations in your gdcloud CLI, run:
    
    
    gdcloud config configurations list
    

The gdcloud CLI lists the configurations and shows which configuration is active:
    
    
    NAME                ISACTIVE   PROPERTIES.CORE.PROJECT PROPERTIES.CORE.ORGANIZATIONCONSOLEURL
    default             False      example-project-default https://console.default-org.example.com
    config-project-1    False      example-project-1       https://console.org-1.example.com
    config-project-2    False      example-project-2       https://console.org-2.example.com
    

## Setting configuration properties

To set and unset the properties in the active configuration, run:
    
    
    gdcloud config set project PROJECT
    

## Viewing configuration properties

To view the properties in a configuration, run:
    
    
    gdcloud config configurations describe NAME
    

The gdcloud CLI prints the configuration properties:
    
    
    is_active: false
    name: default
    properties:
      accessibility:
        screen_reader: "false"
      core:
        organization_console_url: https://console.example.com
        project: example-project
    

To view properties in the active configuration, run:
    
    
    gdcloud config list
    

## Delete a configuration

To delete a configuration, run:
    
    
    gdcloud config configurations delete NAME
    

You can't delete an active configuration. To switch to another configuration before deleting, use `gdcloud config configurations activate` if required.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
