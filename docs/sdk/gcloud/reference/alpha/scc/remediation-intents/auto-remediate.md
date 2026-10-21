---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/remediation-intents/auto-remediate/
title: gcloud alpha scc remediation-intents auto-remediate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:24.859822+00:00
---

# gcloud alpha scc remediation-intents auto-remediate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/remediation-intents/auto-remediate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc remediation-intents auto-remediate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc remediation-intents auto-remediate - command for semi-automatic remediation of SCC findings 
SYNOPSIS
    

`gcloud alpha scc remediation-intents auto-remediate` `--git-config-path`=`GIT_SETTINGS` `--org-id`=`ORG_ID` [`--root-dir-path`=`ROOT_DIR_PATH`; default="."] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Orchestrates the semi-automatic remediation process for SCC findings by calling the Remediation Intent APIs. 
EXAMPLES
     Sample usage: Remediate a SCC finding for the organization 1234567890, in the terraform repository located at ./terraform-repo. $ {command} scc remediation-intents auto-remediate \
    
    
    --org-id=1234567890 --root-dir-path=./terraform-repo \
    --git-config-path=./git-config.yaml

REQUIRED FLAGS
    

`--git-config-path`=`GIT_SETTINGS`
     Path to the git config file in YAML format to raise the PR. Format: /path/to/file.yaml. Sample Config file: 
    
    
    remote: origin
    main-branch-name: master
    branch-prefix: iac-remediation-
    reviewers: reviewer1,reviewer2

`--org-id`=`ORG_ID`
     The Google Cloud organization ID 
OPTIONAL FLAGS
    

`--root-dir-path`=`ROOT_DIR_PATH`; default="."
     The relative path to the root directory for the terraform repository. If not specified, the default value is assumed to be the current directory. The default is *.`. `
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
