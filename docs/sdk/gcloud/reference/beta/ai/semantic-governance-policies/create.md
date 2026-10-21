---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/semantic-governance-policies/create/
title: gcloud beta ai semantic-governance-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:21.016414+00:00
---

# gcloud beta ai semantic-governance-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/semantic-governance-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai semantic-governance-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai semantic-governance-policies create - create a new semantic governance policy 
SYNOPSIS
    

`gcloud beta ai semantic-governance-policies create` (`POLICY` : `--location`=`LOCATION`) `--agent`=`AGENT` `--display-name`=`DISPLAY_NAME` `--natural-language-constraint`=`NATURAL_LANGUAGE_CONSTRAINT` [`--agent-response-denial-message`=`AGENT_RESPONSE_DENIAL_MESSAGE`] [`--async`] [`--description`=`DESCRIPTION`] [`--mcp-tools`=`MCP_TOOLS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new semantic governance policy. 
EXAMPLES
     To create a semantic governance policy `my-policy` in location `us-central1`, run: 
    
    
    gcloud beta ai semantic-governance-policies create my-policy --location=us-central1 --display-name="My Policy" --natural-language-constraint="constraint" --agent="agent-name"

POSITIONAL ARGUMENTS
    

Policy resource - The semantic governance policy to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`POLICY`
     ID of the policy or fully qualified identifier for the policy. 

To set the `policy` attribute: 

  * provide the argument `policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location to create the policy in. 

To set the `location` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--agent`=`AGENT`
     The name of the agent in Agent Registry that is affected by this policy. 
`--display-name`=`DISPLAY_NAME`
     The user-defined name of the semantic governance policy. 
`--natural-language-constraint`=`NATURAL_LANGUAGE_CONSTRAINT`
     The natural language constraint of the semantic governance policy. 
OPTIONAL FLAGS
    

`--agent-response-denial-message`=`AGENT_RESPONSE_DENIAL_MESSAGE`
     Sets `agent_response_customization.denial_message` on the policy: a custom message shown to the end user when the policy denies a request. Max 1000 characters. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description of the semantic governance policy. 
`--mcp-tools`=`MCP_TOOLS`
     The MCP tools that are affected by this policy. Syntax: \--mcp-tools=mcp-server=S1,tools=T1;T2 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `aiplatform/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/vertex-ai/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud ai semantic-governance-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/ai/semantic-governance-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
