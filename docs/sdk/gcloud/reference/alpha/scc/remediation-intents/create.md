---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/remediation-intents/create/
title: gcloud alpha scc remediation-intents create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:25.024926+00:00
---

# gcloud alpha scc remediation-intents create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/remediation-intents/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc remediation-intents create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc remediation-intents create - creates a remediation intent resource 
SYNOPSIS
    

`gcloud alpha scc remediation-intents create` `--parent`=`PARENT` `--workflow-type`=`WORKFLOW_TYPE` [`--async`] [`--finding-name`=`FINDING_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Cloud Security Command Center (SCC) RemediationIntent resource. Created resource is returned as the response of the command. 
EXAMPLES
     Sample usage: Create a manual workflow remediation intent resource: $ {command} scc remediation-intents create \
    
    
    --parent=organizations/123456789/locations/global \
    --finding-name=projects/123456789/sources/123456789/locations/\
    global/findings/123456789 --workflow-type=manual

Create a semi-autonomous workflow remediation intent resource: $ {command} scc remediation-intents create \
    
    
    --parent=organizations/123456789/locations/global \
    --workflow-type=semi-autonomous

REQUIRED FLAGS
    

`--parent`=`PARENT`
     The parent resource to create the remediation intent under. Format: organizations/{org_id}/locations/{loc_id} 
`--workflow-type`=`WORKFLOW_TYPE`
     Type of the workflow to be created. `WORKFLOW_TYPE` must be one of: `semi-autonomous`, `manual`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `False`. 
`--finding-name`=`FINDING_NAME`
     Canonical name of the SCC finding Format: projects/{proj_id}/sources/{src_id}/locations/{loc_id}/findings/{finding_id} 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
