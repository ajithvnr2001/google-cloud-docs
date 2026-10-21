---
url: https://docs.cloud.google.com/compute/docs/gcloud-compute/
title: gcloud compute \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:10.643302+00:00
---

# gcloud compute  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gcloud-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  gcloud compute Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

The Google Cloud CLI lets you manage your Compute Engine resources, using the `gcloud compute` command group. `gcloud compute` is an alternative to using the Compute Engine API.

The gcloud CLI is part of the [Google Cloud CLI](https://docs.cloud.google.com/sdk) and is a unified command-line tool that includes features like statement autocompletion, in-place updating, command-line help, human-readable and machine-parsable output formats, and integration with Google Cloud CLI.

**Note:** Looking for reference pages for `gcloud compute` commands? Try the command-line `--help` function. For example, to get help about instance creation, use `gcloud compute instances create --help`. You can see all command-line documentation at [Google Cloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute).

If you have never used Compute Engine, get started with either the [Linux quickstart](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) or the [Windows quickstart](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance).

## Before you begin

  * If you want to run `gcloud compute` in a command prompt, [install, update, and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).
  * If you don't have a command prompt readily available, try using `gcloud compute` in [Cloud Shell](https://docs.cloud.google.com/shell/docs). Cloud Shell is automatically installed, updated, and initialized with the latest Google Cloud CLI.



## Default properties

When you create a virtual machine instance, Compute Engine configures a VM using default properties from the [metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#default). You can check your VM's default properties by running the following command:
    
    
    gcloud compute project-info describe --project PROJECT_ID
    

Replace `PROJECT_ID` with your project ID.

## Default project

If you set a default project when you setup and initialize the Google Cloud CLI, all `gcloud compute` commands use that project ID by default.

You can override the default project ID by using either of the following methods:

  * Run each `gcloud compute` command with the `--project` flag
  * Set the `CLOUDSDK_CORE_PROJECT` environment variable

###  Linux and macOS 

Use the `export` command to set the project environment variable.
        
        export CLOUDSDK_CORE_PROJECT=PROJECT_ID
        

Replace `PROJECT_ID` with the project ID of the project that you want to use as default.

**Unsetting project environment variables**

If you need to unset your project environment variables, use the following `unset` commands:
        
        unset CLOUDSDK_CORE_PROJECT
        

###  Windows 

Use the `set` command to set the project environment variable.
        
        set CLOUDSDK_CORE_PROJECT=PROJECT_ID
        

Replace `PROJECT_ID` with the project ID of the project that you want to use as default.

**Unsetting project environment variables**

If you need to unset your project environment variables, use the following command:
        
        set CLOUDSDK_CORE_PROJECT=
        




If you do not set a default project or environment variable, you must include a `--project` flag in each `gcloud compute` command that you run.

## Default region and zone

Some `gcloud compute` commands require `--region` or `--zone` flags. Instead of specifying these flags each time you run commands, you can set a default region and zone for your project. If you don't set a default region or zone and you run a region- or zone-dependent command, the Google Cloud CLI might prompt you to provide a `--region` or `--zone` flag, or return an error.

You can set the default region and zone in three ways:

  * **In the metadata server**. The default region and zone set in the metadata server are applied to your local client when you run `gcloud init`.
  * **In your local client**. The default region and zone set in your local client override the default region and zone set in the metadata server.
  * **In environment variables**. The default region and zone set in environment variables override the default region and zone set in your local client and in the metadata server.



You can override the default region and zone in the metadata server, in your local client, or in environment variables, by providing `--region` and `--zone` flags when you run commands.

### View default region and zone

To view your default region and zone, run the following commands:
    
    
    gcloud config get-value compute/region
    
    
    gcloud config get-value compute/zone

If the output is `(unset)`, no default region or zone is set.

#### View available regions and zones

You can view a list of regions and zones by running the following commands:
    
    
    gcloud compute regions list
    
    
    gcloud compute zones list

### Set default region and zone in the metadata server

The default region and zone in the metadata server apply to all configurations in your project. To set the default region and zone in the metadata server, do the following:

  1. Set the default region and zone:
         
         gcloud compute project-info add-metadata \
            --metadata google-compute-default-region=REGION,google-compute-default-zone=ZONE
         

For example:
         
         gcloud compute project-info add-metadata \
            --metadata google-compute-default-region=europe-west1,google-compute-default-zone=europe-west1-b
         

  2. Initialize the change in your local client:
         
         gcloud init




You can override the default region and zone set in the metadata server by setting the default region and zone in your local client, setting the default region and zone in environment variables, or by including the `--zone` or `--region` flag in your commands.

**Note:** There are no restrictions on which zone or regions you can set for your default properties. For example, it is possible to set a default zone outside of the default region.

#### Unset default region and zone in the metadata server

To unset the default region and zone in the metadata server, do the following:

  1. Unset metadata:
         
         gcloud compute project-info remove-metadata \
            --keys=google-compute-default-region,google-compute-default-zone
         

  2. Initialize the change in your local client:
         
         gcloud init




### Set default region and zone in your local client

The default region and zone set in your local client override the default region and zone set in the metadata server.

To set the default region and zone in your local client, run the following commands:
    
    
    gcloud config set compute/region REGION
    
    
    
    gcloud config set compute/zone ZONE
    

#### Unset default region and zone in your local client

To unset the default region or zone in your local client, run the following commands:
    
    
    gcloud config unset compute/zone
    
    
    
    gcloud config unset compute/region
    

You can override the default region and zone set in your local client by setting the default region and zone in environment variables, or by including the `--zone` or `--region` flag in your commands.

### Set default region and zone in environment variables

The default region and zone set in environment variables override the default region and zone set in your local client and in the metadata server.

###  Linux and macOS 

Use the `export` command to set the region and zone variables.
    
    
    export CLOUDSDK_COMPUTE_REGION=REGION
    
    
    
    export CLOUDSDK_COMPUTE_ZONE=ZONE
    

To make these environment variables permanent, include these commands in your `~/.bashrc` file and restart your terminal.

###  Windows 

Use the `set` command to set the region and zone variables.
    
    
    set CLOUDSDK_COMPUTE_REGION=REGION
    
    
    
    set CLOUDSDK_COMPUTE_ZONE=ZONE
    

You can override environment variables by including the `--zone` or `--region` flag in your commands.

#### Unset default region and zone in environment variables

Use the following commands to unset the default region and zone in environment variables.

###  Linux and macOS 

To unset your region and zone environment variables, use the following `unset` commands:
    
    
    unset CLOUDSDK_COMPUTE_REGION
    
    
    
    unset CLOUDSDK_COMPUTE_ZONE
    

###  Windows 

To unset your region and zone environment variables, use the following commands:
    
    
    set CLOUDSDK_COMPUTE_REGION=
    
    
    
    set CLOUDSDK_COMPUTE_ZONE=
    

### Override default zone with flags

Use the `--zone` flag to override the default zone set in the metadata server, your local client, and environment variables.

For example:
    
    
    gcloud compute instances create example-instance \
        --zone=ZONE
    

## Configurations

[`gcloud topic configurations`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) are an advanced feature that you can use to influence the behavior of the gcloud CLI. For most users, using default configurations is sufficient.

Configurations might be useful for users who:

  * Work with multiple projects. You can create a separate configuration for each project.
  * Use multiple accounts. For example, a user account and a service account.
  * Perform a variety of independent tasks (work on an App Engine app in one project, administer a Compute Engine cluster in zone us-central1-a, manage the network configurations for region asia-east1, etc.)



To switch between configurations, run the following command:
    
    
    gcloud config configurations activate CONFIGURATION_NAME
    

For more information about managing configurations, see [`gcloud config configurations`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations).

## What's next?

  * Follow the [Quickstart](https://docs.cloud.google.com/sdk/docs/quickstarts) guide for the Google Cloud CLI.
  * Review `gcloud compute` [usage tips](https://docs.cloud.google.com/compute/docs/gcloud-compute/tips).
  * Discover [common `gcloud compute` commands](https://docs.cloud.google.com/compute/docs/gcloud-compute/common-commands).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
