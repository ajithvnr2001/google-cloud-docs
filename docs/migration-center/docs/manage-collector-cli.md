---
url: https://docs.cloud.google.com/migration-center/docs/manage-collector-cli/
title: Manage Migration Center discovery client CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:48.062479+00:00
---

# Manage Migration Center discovery client CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/manage-collector-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Manage Migration Center discovery client CLI Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can manage the Migration Center discovery client CLI.

## Before you begin

  * Complete the steps to [download the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/download-collector-cli).



## Automatic version check

By default, the `mcdc` CLI performs a version check once every 24 hours. When you run the `mcdc` CLI and a new version is available, a message is displayed which indicates that the version of `mcdc` CLI that is available for you to upgrade to. This version check requires an internet connection.

  * When needed, configure a proxy to access the internet:

### Linux
        
        ./mcdc config set proxy PROXY

### Windows
        
        mcdc.exe config set proxy PROXY

Replace PROXY with the IP address of the HTTP or HTTPS proxy. For example, `127.0.0.1:7777` or `socks5://127.0.0.1:1234`.

  * Deactivate the automatic version check by setting the `disable_version_checking` option:

### Linux
        
        ./mcdc config set disable_version_checking true

### Windows
        
        mcdc.exe config set disable_version_checking true




## Manage configurations

You can manage the configuration properties by using the `config` command.

  * Print all configuration properties and their values:

### Linux
        
        ./mcdc config list

### Windows
        
        mcdc.exe config list

  * Print the value of a configuration property:

### Linux
        
        ./mcdc config get PROPERTY_NAME

### Windows
        
        mcdc.exe config get PROPERTY_NAME

Replace PROPERTY_NAME with the name of the property for which you want to print the value.

  * Set a configuration property:

### Linux
        
        ./mcdc config set proxy PROXY

### Windows
        
        mcdc.exe config set proxy PROXY

  * Reset a configuration property to its default value:

### Linux
        
        ./mcdc config unset proxy

### Windows
        
        mcdc.exe config unset proxy




## Manage usage statistics

The `mcdc` CLI sends pseudoanonymized usage information that can help Google to prioritize discovery and assessment features and improvements. These usage statistics are handled in accordance with [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). This section describes how you can change whether usage statistics are sent to Google at any time after you've installed the `mcdc` CLI.

  * Disable sending usage statistics:

### Linux
        
        ./mcdc config set disable_usage_reporting true

### Windows
        
        mcdc.exe config set disable_usage_reporting true

  * Enable sending usage statistics:

### Linux
        
        ./mcdc config set disable_usage_reporting false

### Windows
        
        mcdc.exe config set disable_usage_reporting false




## Delete collected data from host machine

  * After you've collected data and exported it to Migration Center or completed an offline assessment, you can delete the data from the local database:

### Linux
        
        ./mcdc discover purge-db -db DATABASE_NAME

### Windows
        
        mcdc.exe discover purge-db -db DATABASE_NAME

Replace DATABASE_NAME with the path to the database where the collected data is stored. Typically, it is in the same directory where you installed the `mcdc` CLI.




## What's next

  * Learn how to [run an offline assessment](https://docs.cloud.google.com/migration-center/docs/run-offline-assessment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
