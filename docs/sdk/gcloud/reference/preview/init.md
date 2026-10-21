---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/init/
title: gcloud preview init \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:14.327152+00:00
---

# gcloud preview init  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/init/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview init Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview init - initialize or reinitialize gcloud 
SYNOPSIS
    

`gcloud preview init` [`--no-browser`] [`--console-only`, `--no-launch-browser`] [`--skip-diagnostics`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` gcloud preview init launches an interactive Getting Started workflow for the gcloud command-line tool. It performs the following setup steps: 

  * Authorizes gcloud and other SDK tools to access Google Cloud using your user account credentials, or from an account of your choosing whose credentials are already available. 
  * Sets up a new or existing configuration. 
  * Sets properties in that configuration, including the current project and optionally, the default Google Compute Engine region and zone you'd like to use. 



gcloud preview init can be used for initial setup of gcloud and to create new or reinitialize gcloud configurations. More information about configurations can be found by running `[gcloud topic configurations](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations)`. 

Properties set by gcloud preview init are local and persistent, and are not affected by remote changes to the project. For example, the default Compute Engine zone in your configuration remains stable, even if you or another user changes the project-level default zone in the Cloud Platform Console. 

To sync the configuration, re-run `gcloud preview init`. 

EXAMPLES
     To launch an interactive Getting Started workflow, run: 
    
    
    gcloud preview init

To launch an interactive Getting Started workflow without diagnostics, run: 
    
    
    gcloud preview init --skip-diagnostics

FLAGS
    

`--no-browser`
     Prevent the command from launching a browser for authorization. Use this flag if you are on a machine that does not have a browser but you can install the gcloud CLI on another machine with a browser. 
`--console-only`, `--no-launch-browser`
     Prevent the command from launching a browser for authorization. Use this flag if you are on a machine that does not have a browser and you cannot install the gcloud CLI on another machine with a browser. 
`--skip-diagnostics`
     Do not run diagnostics. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init)
    
    
    [gcloud alpha init](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/init)
    
    
    [gcloud beta init](https://docs.cloud.google.com/sdk/gcloud/reference/beta/init)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
