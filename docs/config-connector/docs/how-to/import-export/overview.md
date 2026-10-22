---
url: https://docs.cloud.google.com/config-connector/docs/how-to/import-export/overview/
title: Install the config-connector CLI tool \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:52.328709+00:00
---

# Install the config-connector CLI tool  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/import-export/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Install the `config-connector` CLI tool

This page explains how to install the `config-connector` CLI tool.

With the `config-connector` CLI tool, you can export existing Google Cloud resources into YAML files, which are required for Config Connector to acquire those resources.

The `config-connector` CLI tool is not installed by default when you install Config Connector.

## Before you begin

[Install Config Connector with a supported installation method](https://docs.cloud.google.com/config-connector/docs/concepts/installation-types).

## Install `config-connector` CLI tool

  1. Download the latest `config-connector` binary tar file:
         
         gcloud storage cp gs://cnrm/latest/cli.tar.gz .
         

  2. Extract the tar file:
         
         tar zxf cli.tar.gz
         

  3. The tar file includes a binary executable for Linux, macOS, and Windows. Choose the appropriate binary for your operating system:

     * Linux: `./linux/amd64/config-connector`
     * macOS: `./darwin/amd64/config-connector`
     * Windows: `./windows/amd64/config-connector`
  4. Copy the binary to a location on your `${PATH}`. For example, on Linux and macOS, you might use `mv` to place it into `/usr/local/bin`.
         
         mv linux/amd64/config-connector /usr/local/bin
         

  5. If you want to use the `config-connector` CLI tool to export directly from Cloud Asset Inventory, enable the Cloud Asset Inventory API on your Google Cloud Identity's project with `gcloud`.
         
         gcloud services enable cloudasset.googleapis.com
         




## Upgrade config-connector

To upgrade the `config-connector` CLI tool to the latest version, repeat the installation steps and overwrite the executable.

## What's next

  * [Perform an export on individual resources](https://docs.cloud.google.com/config-connector/docs/how-to/import-export/export).
  * [Perform a bulk export for all resources in your project, folder, or organization](https://docs.cloud.google.com/config-connector/docs/how-to/import-export/bulk-export).
  * [Learn about the resources that Config Connector supports](https://docs.cloud.google.com/config-connector/docs/reference/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
