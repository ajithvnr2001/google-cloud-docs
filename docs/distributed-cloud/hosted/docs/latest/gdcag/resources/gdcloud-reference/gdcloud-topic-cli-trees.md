---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-topic-cli-trees/
title: gdcloud topic cli-trees \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:34.903996+00:00
---

# gdcloud topic cli-trees  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-topic-cli-trees/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud topic cli-trees Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud topic cli-trees - Supplementary help for CLI trees.

## DESCRIPTION

CLI trees are static nested dictionaries that describe all groups, commands, flags, positionals, help text, and completer module paths for a CLI. A static CLI tree is often much faster to load and access than a CLI tree generated at runtime from an active CLI. It is also a more compact representation. A properly formed CLI tree can be used to reproduce the help documentation for an entire CLI.

## CLI-Trees Data Files

A CLI tree is a dictionary stored in a JSON file. By convention, the file base name is the corresponding CLI name. For example, the CLI tree file name for the gdcloud CLI is `gdcloud.json`. CLI trees associated with gdcloud CLI modules are installed in the `data/cli` subdirectory of the root of the unzipped gdcloud CLI bundle directory.
    
    
    <UNZIPPED_CLI_DIR_PATH>/google-distributed-cloud-hosted-cli/data/cli/gdcloud.json
    

This file contains tree data for the gdcloud CLI. Note that the gdcloud CLI does not require this CLI tree to run.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
