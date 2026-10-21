---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/agent-pools/list/
title: gcloud alpha transfer agent-pools list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:55.490724+00:00
---

# gcloud alpha transfer agent-pools list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/agent-pools/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha transfer agent-pools list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha transfer agent-pools list - list Transfer Service transfer agent pools 
SYNOPSIS
    

`gcloud alpha transfer agent-pools list` [`--limit`=`LIMIT`] [`--names`=[`NAMES`,…]] [`--page-size`=`PAGE_SIZE`; default=256] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List Transfer Service transfer pools in a given project to show their configurations. 
EXAMPLES
     To list all agent pools in your current project, run: 
    
    
    gcloud alpha transfer agent-pools list

To list agent pools named "foo" and "bar" in your project, run: 
    
    
    gcloud alpha transfer agent-pools list --names=foo,bar

To list all information about jobs 'foo' and 'bar' formatted as JSON, run: 
    
    
    gcloud alpha transfer agent-pools list --names=foo,bar --format=json

FLAGS
    

`--limit`=`LIMIT`
     Return the first items from the API up to this limit. 
`--names`=[`NAMES`,…]
     The names of the agent pools you want to list. Separate multiple names with commas (e.g., --name=foo,bar). If not specified, all agent pools in your current project will be listed. 
`--page-size`=`PAGE_SIZE`; default=256
     Retrieve batches of this many items from the API. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud transfer agent-pools list](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
