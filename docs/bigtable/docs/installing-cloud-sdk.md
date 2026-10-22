---
url: https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk/
title: Install the gcloud CLI \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:48.147090+00:00
---

# Install the gcloud CLI  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Install the gcloud CLI

As an alternative to the [Google Cloud console](https://console.cloud.google.com/), you can use the [Google Cloud CLI](https://docs.cloud.google.com/sdk) and the [ `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/cbt-overview) to manage your Bigtable instances from the command line.

## Install

To install the command-line interfaces:

  1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs).

If you've already installed the gcloud CLI, run the following command to make sure it's up to date:
         
         gcloud components update
         

  2. Install or update the `beta` component of the gcloud CLI, along with the `cbt` CLI :
         
         gcloud components install beta cbt
         

  3. Set a default project for the gcloud CLI, replacing `PROJECT_ID` with the project where your Bigtable instances are located:
         
         gcloud config set project PROJECT_ID
         




You can now use the gcloud CLI and the `cbt` CLI for Bigtable.

## Get help

For the gcloud CLI, each command for working with Bigtable begins with `gcloud bigtable` or `gcloud beta bigtable`. To get help for each command, see the [reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable) or [beta reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable), or use the gcloud CLI itself to get help:
    
    
    gcloud bigtable clusters --help  # help for all commands
    gcloud bigtable clusters create --help  # help for the `create` command
    

For the `cbt` CLI , get help from the [reference documentation](https://docs.cloud.google.com/bigtable/docs/cbt-reference), or use the `cbt` CLI itself to get help:
    
    
    cbt help  # view a list of commands and help for all commands
    cbt help createtable  # help for the `createtable` command
    

## What's next

  * Learn how to [create a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).
  * Find out how to [view and update existing Bigtable instances](https://docs.cloud.google.com/bigtable/docs/modifying-instance).
  * Learn how to [delete a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/deleting-instance).
  * See [other maintenance tasks you can perform with the `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/cbt-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
