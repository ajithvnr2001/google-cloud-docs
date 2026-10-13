---
url: https://docs.cloud.google.com/sdk/gcloud/
title: gcloud CLI overview \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:18.872559+00:00
---

# gcloud CLI overview  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  gcloud CLI overview Stay organized with collections  Save and categorize content based on your preferences. 

This page contains an overview of the Google Cloud CLI and its common command patterns and capabilities.

## What is the gcloud CLI?

The Google Cloud CLI is a set of tools to create and manage Google Cloud resources. You can use these tools to perform many common platform tasks from the command line or through scripts and other automation.

For example, you can use the gcloud CLI to create and manage the following:

  * Compute Engine virtual machine instances and other resources
  * Cloud SQL instances
  * Google Kubernetes Engine clusters
  * Managed Service for Apache Spark clusters and jobs
  * Cloud DNS managed zones and record sets
  * Cloud Deployment Manager deployments



You can also use the gcloud CLI to deploy App Engine applications, manage authentication, customize local configuration, and perform other tasks.

## Download and install the gcloud CLI

The current gcloud CLI version is 589.0.0.

**Caution:** Make sure that you use the current version of the gcloud CLI, version 589.0.0. This allows you to use the latest features, including authorizing with [`gcloud init`](https://cloud.google.com/sdk/docs/initialize). If you use older versions of the gcloud CLI, you might encounter errors. To find the version number of gcloud CLI that you have installed, enter the following command: `gcloud version`. To learn how to upgrade to the current version of the gcloud CLI, see [Manage an installation](https://docs.cloud.google.com/sdk/docs/install#manage_an_installation).

Although we strongly recommend that you use the current version of gcloud CLI, you can also download and install previous versions from the [download archive](https://console.cloud.google.com/storage/browser/cloud-sdk-release).

If you're using Cloud Shell, the gcloud CLI is available automatically and you don't need to install it. Otherwise, [download and install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) it.

By default, the gcloud CLI installs commands that are at the General Availability level. Additional functionality is available in gcloud CLI [components](https://docs.cloud.google.com/sdk/docs/components) named `alpha`, `beta`, and `preview`. These components allow you to use the gcloud CLI to work with Bigtable, Dataflow, and other parts of the Google Cloud at earlier release levels than General Availability.

## The gcloud CLI cheat sheet

For a quick introduction to the gcloud CLI, a list of commonly used commands, and a look at how these commands are structured, see the [gcloud CLI cheat sheet](https://docs.cloud.google.com/sdk/docs/cheatsheet).

## Release levels

The gcloud CLI commands have the following release levels:

Release level | Label | Description  
---|---|---  
General Availability | None | Commands are considered fully stable and available for production use. For advance notice of changes to commands that break current functionality, see the [release notes](https://docs.cloud.google.com/sdk/docs/release-notes).  
Preview | `preview` | Commands are in the preview release level, used to gather feedback from customers. Preview offerings are often publicly announced, but are not necessarily feature-complete, and no SLAs or technical support commitments are provided for these. Unless stated otherwise by Google, preview offerings are intended for use in test environments only. The average preview stage lasts about six months.  
Beta | `beta` | Commands are functionally complete, but could still have some outstanding issues. Breaking changes to these commands can be made without notice.  
Alpha | `alpha` | Commands are in early release and may change without notice.  
  
The `alpha`, `beta`, and `preview` components are not installed by default when you install the gcloud CLI. You must [install these components](https://docs.cloud.google.com/sdk/docs/components) separately using the `gcloud components install` command. If you try to run an alpha, beta, or preview command and the corresponding component is not installed, the gcloud CLI prompts you to install it.

## Command groups

Within each release level, gcloud CLI commands are organized into a nested hierarchy of command groups, each of which represents a product or feature of Google Cloud or its functional subgroups.

For example:

Command group | Description  
---|---  
`gcloud compute` | Commands related to Compute Engine in general availability  
`gcloud compute instances` | Commands related to Compute Engine instances in general availability  
`gcloud beta compute` | Commands related to Compute Engine in Beta  
`gcloud preview` | Commands related to Google Cloud in Preview  
`gcloud alpha app` | Commands related to managing App Engine deployments in Alpha  
  
## Running gcloud CLI commands

You can run gcloud CLI commands from the command line and from [scripts and other automations](https://docs.cloud.google.com/sdk/docs/scripting-gcloud)—for example, when using Jenkins to automate Google Cloud tasks.

**Note:** gcloud CLI reference documentation and examples use backslashes, `\`, to denote long commands. You can execute these commands as-is (Windows users can use `^` instead of `\`). If you'd like to remove the backslashes, be sure to remove newlines as well to ensure the command is read as a single line.

## Properties

The [gcloud CLI properties](https://docs.cloud.google.com/sdk/docs/properties) are settings that affect the behavior of the gcloud CLI tools. Some of these properties can be set by either global or command options—in which case, the value set by the option takes precedence.

### Enabling accessibility features

For a more streamlined screen reader experience, the gcloud CLI comes with an `accessibility/screen_reader` property.

To enable the accessibility property, run:
    
    
    gcloud config set accessibility/screen_reader true
    

For more details about the accessibility features that come with the gcloud command-line tool, see the [Enabling accessibility features](https://docs.cloud.google.com/sdk/docs/enabling-accessibility-features) guide.

## Configurations

A configuration is a set of gcloud CLI properties. A configuration works like a _profile_.

When you start using the gcloud CLI, you'll work with a single configuration named `default` and you can set properties by running `gcloud init` or `gcloud config set`. This single default configuration is suitable for most use cases.

To work with multiple projects or authorization accounts, you can set up multiple configurations with `gcloud config configurations create` and switch among the configurations. Within a configuration, you can customize properties. For example, to set your project within an active configuration use the `project` property:
    
    
    gcloud config set project <project-id>
    

For a detailed account of these concepts, see the [Configurations guide](https://docs.cloud.google.com/sdk/docs/configurations).

## Global options

The gcloud CLI provides a set of [gcloud CLI options](https://docs.cloud.google.com/sdk/gcloud/reference) that govern the behavior of commands on a per-invocation level. Options override values set in gcloud CLI properties.

## Positional arguments and options

While positional arguments and options affect the output of a gcloud CLI command, there is a subtle difference in their use cases. A positional argument is used to define an entity on which a command operates while an options is required to set a variation in a command's behavior.

## Use of `stdout` and `stderr`

The output of successful gcloud CLI commands is written to `stdout`. All other types of responses—prompts, warnings, and errors—are written to `stderr`. Do not script against responses written to `stderr` because these responses aren't stable.

For guidelines on handling output, refer to the [Scripting guide](https://docs.cloud.google.com/sdk/docs/scripting-gcloud#handling_output).

## Prompting

To protect against unintended destructive actions, the gcloud CLI confirms your intentions before executing commands such as `gcloud projects delete`.

You might be prompted when additional information is needed. For example you will be asked to choose a zone when you create a Compute Engine virtual machine instance using `gcloud compute instances create test-instance`.

To disable prompting, use the `--quiet` option.

Do not script against the wording of prompts because the wording can change.

## Suppressing prompting, writing to the terminal, and logging

The `--quiet` option (also, `-q`) for the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference) disables all interactive prompts when running gcloud CLI commands and is useful for scripting. If input is needed, defaults are used. If there isn't a default, an error is raised.

To suppress printing of command output to standard output and standard error in the terminal, use the `--no-user-output-enabled` option.

To adjust verbosity of logs, specify a verbosity level (debug, info, warning, error, critical, or none) using the [`--verbosity`](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity) option.

## Determining output structure

By default, when a gcloud CLI command returns a list of resources, the resources are pretty-printed to standard output. To produce more meaningful output, the `format`, `filter`, and `projection` options allow you to fine-tune your output.

To define just the format of your output, use the [`--format` option](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats) to produce a tabulated or flattened version of your output (for interactive display) or a machine-readable version of the output (`json`, `csv`, `yaml`, `value`).

To format a list of keys that select resource data values, use [`projections`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/projections). To further refine your output to criteria you define, use [`filter`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

To familiarize yourself with filter and format functionality, you can complete a quick interactive tutorial by clicking **Open in Cloud Shell**. 

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/cloud-shell-tutorials&page=editor&tutorial=cloudsdk/tutorial.md)

## What's next

  * Learn more about gcloud CLI commands in the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
