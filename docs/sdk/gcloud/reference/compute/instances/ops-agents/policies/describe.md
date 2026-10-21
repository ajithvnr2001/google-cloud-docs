---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe/
title: gcloud compute instances ops-agents policies describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:26:33.299460+00:00
---

# gcloud compute instances ops-agents policies describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instances ops-agents policies describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instances ops-agents policies describe - describe a Google Cloud Observability agents policy for the Ops Agent 
SYNOPSIS
    

`gcloud compute instances ops-agents policies describe` `POLICY_ID` `--zone`=`ZONE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute instances ops-agents policies describe` describes a policy that facilitates agent management across Compute Engine instances based on user specified instance filters. This policy installs, specifies versioning, and removes Ops Agents. 

The command returns the content of one policy. For instance: 
    
    
    agentsRule:
      packageState: installed
      version: latest
    instanceFilter:
      inclusionLabels:
      - labels:
          env: prod

If no policies are found, then the command returns a `NOT_FOUND` error. 

EXAMPLES
     To describe an agents policy named `ops-agents-test-policy` in the current project, run: 
    
    
    gcloud compute instances ops-agents policies describe ops-agents-test-policy --zone=ZONE

POSITIONAL ARGUMENTS
    

`POLICY_ID`
     ID of the policy. 

This ID must contain only lowercase letters, numbers, and hyphens, end with a number or a letter, be between 1-63 characters, and be unique within the project. 

REQUIRED FLAGS
    

`--zone`=`ZONE`
     Zone of the agents policy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instances ops-agents policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/describe)
    
    
    [gcloud beta compute instances ops-agents policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies/describe)
    
    
    [gcloud preview compute instances ops-agents policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/ops-agents/policies/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
