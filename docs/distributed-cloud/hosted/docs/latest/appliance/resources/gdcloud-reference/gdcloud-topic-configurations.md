---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-topic-configurations/
title: gdcloud topic configurations \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:04.259555+00:00
---

# gdcloud topic configurations  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-topic-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud topic configurations Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud topic configurations - Supplementary help for named configurations.

## DESCRIPTION

gdcloud CLI properties can be stored in named configurations, which are collections of key-value pairs that influence the behavior of gdcloud CLI. Named configurations are beneficial if you manage more than one project or organization. Properties commonly stored in configurations include the organization console URL and project ID. Configurations let you define and enable these and other settings together as a group. Configuration data is stored in `$HOME/.config/gdcloud/`. Configurations are especially useful if you \+ Work with multiple projects. You can create a separate configuration for each project. \- Use multiple organization console URLs. * Perform generally independent tasks For example, one configuration can be used to work on the Object Storage service in one project and manage an unrelated service in another project. Property information stored in named configurations are readable by all gdcloud CLI commands. To set the properties, use the `gdcloud config set` command.

## Create configurations

Named configurations can be defined by users or built into gdcloud CLI. User-defined configurations have lowercase names, such as `johndoe`, `default`, `jeff-staging`, or `foo2`. These are defined by the following regular expression `^[a-z][-a-z0-9]*$`. To create a new configuration, run 
    
    
    gdcloud init
    

This guides you through setting up your first named configuration, creating a new named configuration, or reinitializing an existing named configuration. Note that reinitializing an existing configuration removes all its existing properties.

To create a new empty configuration, run 
    
    
    gdcloud config configurations create [CONFIG_NAME]
    

## Use configurations

gdcloud CLI should have at most one active configuration which provides property values. Inactive configurations have no effect on gdcloud CLI executions. To activate a configuration, run 
    
    
    gdcloud config configurations activate [CONFIG_NAME]
    

To view and change the properties of your active configuration, run 
    
    
    gdcloud config list
    gdcloud config set
    

Additionally, commands under the `gdcloud config configurations` group let you list, activate, rename, describe, and delete configurations that might or might not be active.

You can activate a configuration for a single gdcloud invocation using flag `--configuration my-config`.

## Available Properties

`accessibility` * `screen_reader` * If set, gdcloud CLI activates the screen reader.

`auth` * `login_config_cert_path` * Path of the file that stores the current login configuration certificate.

`component_manager` * `disable_update_check` * If set, gdcloud CLI does not automatically check for updates.

`core` * `disable_prompts` * If True, the default answer is assumed for all user prompts. However, for any prompts that require user input, an error is raised. * `format` * Set the format for printing command output resources. The default is a command-specific human-friendly output format. If both `core/format` and `--format` are specified, `--format` takes precedence. The supported formats are limited to `csv`, `json`, `table`, `text`, `yaml`. * `organization_console_url` * URL to the current organization UI/console. Note that it should start with `https //console.`. For example, `https //console.org-name.gdch.google.com`. * `project` * Current project name.

`storage` * `s3_access_key_id` * Access key ID of the S3 storage object. It is a unique identifier for users. * `s3_custom_ca_certs_file` * Custom certificates file for the S3 storage object. * `s3_endpoint` * The URL of the S3 object consists of `S3_ENDPOINT/$BUCKET_NAME/$OBJECT_NAME`. The `S3_ENDPOINT` is the location where the S3 storage bucket is located. * `s3_secret_access_key` * Private key of the S3 storage object that is used to sign requests.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
