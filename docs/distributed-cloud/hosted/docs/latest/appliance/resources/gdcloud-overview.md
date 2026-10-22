---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview/
title: gdcloud CLI overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:57.948356+00:00
---

# gdcloud CLI overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  gdcloud CLI overview Stay organized with collections  Save and categorize content based on your preferences. 

This overview document explains the gdcloud CLI, why it's useful, the installation workflow, and the various configuration methods for it to best suit your needs when operating in a Google Distributed Cloud (GDC) air-gapped appliance device.

This document is for all audience groups that work on GDC that must use a dedicated command-line interface tool for their air-gapped hardware and software workflows. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/audiences).

## What is the gdcloud CLI?

The gdcloud CLI is a set of tools to create and manage Google Distributed Cloud (GDC) air-gapped appliance resources. Use these tools to perform common tasks from the command line or through scripts and automation.

The gdcloud CLI allows you to bootstrap infrastructure, manage authentication, and customize local configurations.

## Download and install the gdcloud CLI

To start using gdcloud CLI:

  1. [Download the bundle](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download).
  2. [Install the tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install).
  3. [Initialize the configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#init-default-config).



The current gdcloud CLI version is 1.0. Download and install previous versions of the gdcloud CLI from the [download archive](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download).

## Properties

The gdcloud CLI properties are settings that affect the behavior of the gdcloud CLI tools.

### Enabling accessibility features

For a more streamlined screen reader experience, the gdcloud CLI comes with an `accessibility/screen_reader` property.

To enable the accessibility property, run:
    
    
    gdcloud config set accessibility/screen_reader true
    

For more details about the accessibility features that come with the gdcloud CLI, see the [Enabling accessibility features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-accessibility) guide.

## Configurations

A configuration is a set of gdcloud CLI properties. A configuration works like a _profile_.

When you start using the gdcloud CLI, you work with a single configuration named `default` and you can set properties by running the `gdcloud init` or `gdcloud config set` commands. The `default` configuration is suitable for most use cases.

To work with multiple projects or organizations, you can set up multiple configurations with `gdcloud config configurations create` and switch among the configurations. Within a configuration, you can customize properties. For example, to set your project within an active configuration use the project property:
    
    
    gdcloud config set project PROJECT_ID
    

For a detailed account of these concepts, see [Manage gdcloud CLI configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-configurations).

## What's next

  * [Download the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download)
  * [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install)
  * [Manage gdcloud CLI configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-configurations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
