---
url: https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/search/
title: gcloud agent-registry agents search \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:56:28.685246+00:00
---

# gcloud agent-registry agents search  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud agent-registry agents search Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud agent-registry agents search - search for agents matching a query 
SYNOPSIS
    

`gcloud agent-registry agents search` `--location`=`LOCATION` [`--page-size`=`PAGE_SIZE`] [`--page-token`=`PAGE_TOKEN`] [`--search-string`=`SEARCH_STRING`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Search across all accessible agents matching specific filter expressions. 
EXAMPLES
     To search agents in location 'us-central1' matching query 'displayName:Gemini Enterprise Core Assistant', run: 
    
    
    gcloud agent-registry agents search --location=us-central1 --search-string="displayName:Gemini Enterprise Core Assistant"

REQUIRED FLAGS
    

Location resource - Parent value for SearchAgentsRequest. Format: `projects/{project}/locations/{location}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


OPTIONAL FLAGS
    

`--page-size`=`PAGE_SIZE`
     The maximum number of agents to return. The service may return fewer than this value. If unspecified, at most 20 agents will be returned. The maximum value is 100; values above 100 will be coerced to 100. 
`--page-token`=`PAGE_TOKEN`
     A page token, received from a previous `SearchAgents` call. 
`--search-string`=`SEARCH_STRING`
     Search criteria used to select the Agents to return. If no search criteria is specified then all accessible Agents will be returned. 

Search expressions can be used to restrict results based upon searchable fields, where the operators can be used along with the suffix wildcard symbol `*`. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details. 

Allowed operators: `=`, `:`, `NOT`, `AND`, `OR`, and `()`. 

Examples: 

  * `agentId="urn:agent:projects-123:projects:123:locations:us-central1:reasoningEngines:1234"` to find the agent with the specified agent ID. 
  * `name:important` to find agents whose name contains `important` as a word. 
  * `displayName:works*` to find agents whose display name contains words that start with `works`. 
  * `skills.tags:test` to find agents whose skills tags contain `test`. 
  * `planner OR booking` to find agents whose metadata contains the words `planner` or `booking`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentregistry/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/agent-registry/overview>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha agent-registry agents search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/agents/search)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
