---
url: https://docs.cloud.google.com/sdk/docs/configurations/
title: Managing gcloud CLI configurations \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:26.517116+00:00
---

# Managing gcloud CLI configurations  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Managing gcloud CLI configurations Stay organized with collections  Save and categorize content based on your preferences. 

A configuration is a named set of Google Cloud CLI [properties](https://docs.cloud.google.com/sdk/docs/properties). These properties are key-value pairs, organized in sections, that govern the behavior of the gcloud CLI.

Tip: Usually, if you're working with just one project, the default configuration, named `default`, should be sufficient. To learn more about setting properties in a configuration to define per-product or per-service settings such as the authorization account to use, prompt preferences, and verbosity levels, see [Managing gcloud CLI properties](https://docs.cloud.google.com/sdk/docs/properties).

Properties that are commonly stored in configurations include default Compute Engine zone, verbosity level, usage reporting, project ID, and an active user or service account. Configurations allow you to define and enable these and other settings together as a group.

Configurations are stored in your user config directory (typically `~/.config/gcloud` on MacOS and Linux, or `%APPDATA%\gcloud` on Windows); you can find the location of your config directory by running `gcloud info --format='value(config.paths.global_config_dir)'`. The config directory can be changed by setting the environment variable `CLOUDSDK_CONFIG`. Also, note that the config directory must be write-enabled. However, if you're using Cloud Shell, your gcloud CLI preferences are stored in a temporary `tmp` folder, set for your current Cloud Shell tab only, and do not persist across sessions.

If you have multiple configurations, you can choose to switch between them or run commands using a specific configuration (with the help of the `--configuration` flag). For more about switching configurations, refer to the section below on Activating configurations.

To read about configurations from the command-line (along with a complete list of available properties and the sections they are in), run [`gcloud topic configurations`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations).

## Default configuration

The gcloud CLI starts you off with a single configuration named `default`. You can set properties in your configuration by running the [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) command or by running [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) directly.

For example, to disable prompting for scripting, run:
    
    
    gcloud config set disable_prompts true
    

## Multiple configurations

The single `default` configuration is suitable for many use cases. However, you can also [create additional configurations](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/create) and switch between them as required using [`gcloud config configurations activate`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/activate). There is nothing special about the initial `default` configuration; it is created as a convenience. You can name this and any additional configurations however you'd like.

Multiple configurations are useful if you want to:

  * **Use multiple projects** : You can create a separate configuration for each project and switch between them as required.
  * **Use multiple authorization accounts**
  * **Perform generally independent tasks** : For example, you can use one configuration to work on a App Engine application in one project and manage an unrelated Compute Engine instances in another project.



## Creating a configuration

To create a configuration, run [`gcloud config configurations create`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/create):
    
    
    gcloud config configurations create [NAME]
    

You must activate the new configuration after creation in order to use it.

## Activating a configuration

Only one of your multiple configurations can be active at a given time. The active configuration is the configuration whose properties will govern the behavior of the gcloud CLI.

To activate a new configuration or switch to a new active configuration, run: [`gcloud config configurations activate`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/activate):
    
    
    gcloud config configurations activate [NAME]
    

[`gcloud config list`](https://docs.cloud.google.com/sdk/gcloud/reference/config/list) will always show you the properties in your active configuration.

To change the active configuration for a single command invocation, you can use the `--configuration` flag on any gcloud CLI command:
    
    
    gcloud auth list --configuration=[CONFIGURATION_NAME]
    

To change the active configuration for all commands in your current terminal, you can set the environment variable `CLOUDSDK_ACTIVE_CONFIG_NAME` to the name of the configuration you'd like to use.

## Automating configuration switching

To help make changing configurations seamless, you can leverage tools such as [direnv](https://direnv.net/) and [ondir](https://swapoff.org/ondir.html) to automatically switch between configurations when you switch working directories. One way to accomplish this is to set the necessary environment variables (like `CLOUDSDK_ACTIVE_CONFIG_NAME`) in the .envrc file in the root directory of your project.

## Listing configurations

To list the configurations in your gcloud CLI installation, run [`gcloud config configurations list`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/list):
    
    
    gcloud config configurations list
    

The gcloud CLI lists the configurations and shows which configuration is active:
    
    
    NAME         IS_ACTIVE     ACCOUNT            PROJECT               DEFAULT_ZONE  DEFAULT_REGION
    default      False         user@gmail.com     example-project-1     us-east1-b    us-east1
    project-1    False         user@gmail.com     example-project-2     us-east1-c    us-east1
    project-2    True          user@gmail.com     example-project-3     us-east1-b    us-east1
    

## Setting configuration properties

To set and unset the properties in the active configuration, run [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) and [`gcloud config unset`](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset):
    
    
    gcloud config set project [PROJECT]
    
    gcloud config unset project
    

Properties can also be set via environment variables named `CLOUDSDK_SECTION_NAME_PROPERTY_NAME`. For example, you can set the `core/project` and `compute/zone` properties as follows:
    
    
    CLOUDSDK_CORE_PROJECT=[YOUR_PROJECT_NAME]
    
    CLOUDSDK_COMPUTE_ZONE=[YOUR_ZONE_NAME]
    

## Viewing configuration properties

To view the properties in a configuration, run: [`gcloud config configurations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/describe):
    
    
    gcloud config configurations describe [NAME]
    

Or, to view properties in the active configuration:
    
    
    gcloud config list
    

The gcloud CLI prints the configuration properties:
    
    
    is_active: false
    name: default
    properties:
      compute:
        region: us-east1
        zone: us-east1-b
      core:
        account: user@google.com
        project: example-project
    

## Deleting a configuration

To delete a configuration, run: [`gcloud config configurations delete`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/delete):
    
    
    gcloud config configurations delete [NAME]
    

You can't delete the active configuration. Use `gcloud config configurations activate` if required to switch to another configuration before deleting.

## What's next

  * Read [gcloud CLI properties](https://docs.cloud.google.com/sdk/docs/properties) to learn more about properties.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
