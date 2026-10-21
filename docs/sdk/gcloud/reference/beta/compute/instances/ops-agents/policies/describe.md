---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies/describe/
title: gcloud beta compute instances ops-agents policies describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:32:50.913628+00:00
---

# gcloud beta compute instances ops-agents policies describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute instances ops-agents policies describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute instances ops-agents policies describe - describe a Google Cloud's operations suite agents (Ops Agents) policy 
SYNOPSIS
    

`gcloud beta compute instances ops-agents policies describe` `POLICY_ID` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute instances ops-agents policies describe` describes a policy that facilitates agent management across Compute Engine instances based on user specified instance filters. This policy installs, specifies versioning, enables autoupgrade, and removes Ops Agents. 

The command returns the content of one policy. For instance: 
    
    
    agent_rules:
    - enable_autoupgrade: true
      package_state: installed
      type: ops-agent
      version: latest
    assignment:
      group_labels:
      - app: myapp
        env: prod
      os_types:
      - short_name: ubuntu
        version: '18.04'
      zones:
      - us-central1-a
    create_time: '2021-02-02T02:10:25.344Z'
    description: A test policy to install agents
    etag: <ETAG>
    id: projects/<PROJECT_NUMBER>/guestPolicies/ops-agents-test-policy
    update_time: '2021-02-02T02:10:25.344Z'

If no policies are found, it returns a ``NOT_FOUND`` error. 

EXAMPLES
     To describe an Ops Agents policy named ``ops-agents-test-policy`` in the current project, run: 
    
    
    gcloud beta compute instances ops-agents policies describe ops-agents-test-policy

POSITIONAL ARGUMENTS
    

`POLICY_ID`
     ID of the policy. 

This ID must start with ``ops-agents-``, contain only lowercase letters, numbers, and hyphens, end with a number or a letter, be between 1-63 characters, and be unique within the project. The goal of the prefix ``ops-agents-`` is to easily distinguish these Ops Agents specific policies from other generic policies and lower the chance of naming conflicts. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute instances ops-agents policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe)
    
    
    [gcloud alpha compute instances ops-agents policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/describe)
    
    
    [gcloud preview compute instances ops-agents policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/ops-agents/policies/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
