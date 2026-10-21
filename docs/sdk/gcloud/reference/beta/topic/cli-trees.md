---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/cli-trees/
title: gcloud beta topic cli-trees \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:03.273994+00:00
---

# gcloud beta topic cli-trees  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/cli-trees/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta topic cli-trees Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta topic cli-trees - CLI trees supplementary help 
DESCRIPTION
     `(BETA)` CLI trees are static nested dictionaries that describe all of the groups, commands, flags, positionals, help text, and completer module paths for a CLI. A CLI tree is often much faster to load and access than one generated at runtime from an active CLI. It is also a more compact representation. A properly formed CLI tree can be used to reproduce the help documentation for an entire CLI. 
CLI Tree Data Files
     A CLI tree is a dictionary in a JSON file. By convention, the file base name is the corresponding CLI name. For example, the CLI tree file name for `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` is `gcloud.json`. 

CLI trees associated with Google Cloud CLI modules are installed in the `data/cli` subdirectory of the Google Cloud CLI installation root: 
    
    
    $(gcloud info --format="value(installation.sdk_root)")/data/cli

This includes tree data for `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` (core component), `bq`, `gsutil`, and `kubectl`. Note that the tree data is installed with the component. If the component is not installed then neither is its CLI tree. An installed component does not require its CLI tree to run. Only the `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI tree is required by `$ [gcloud alpha interactive](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/interactive)`. 

By default, CLI trees for other commands are JSON files generated on demand from their `man`(1) or `man7.org` man pages. They are cached in the `cli` subdirectory of the global config directory: 
    
    
    $(gcloud info --format="value(config.paths.global_config_dir)")/cli

The gcloud CLI Tree
     The `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI tree is used for static TAB completion, the corpus for `$ [gcloud alpha](https://docs.cloud.google.com/sdk/gcloud/reference/alpha) help-search`, and the data source for `$ [gcloud alpha interactive](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/interactive)` completions and help text generation. 
Other CLI Trees
     `$ [gcloud alpha interactive](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/interactive)` uses CLI tree data files for typeahead, command line completion and active help. A few CLI trees are installed with their respective Google Cloud CLI components: `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` (core component), `bq`, `gsutil`, and `kubectl`. 

The generated trees are a close approximation. You can construct your own, especially for hierarchical CLIs like `git`(1) that are hard to extract from man pages. 

CLI Tree Schema
     TBD (`gcloud interactive` is still in ALPHA). 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud topic cli-trees](https://docs.cloud.google.com/sdk/gcloud/reference/topic/cli-trees)
    
    
    [gcloud alpha topic cli-trees](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/cli-trees)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
