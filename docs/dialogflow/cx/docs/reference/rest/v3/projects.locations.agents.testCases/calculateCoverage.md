---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage/
title: Method: projects.locations.agents.testCases.calculateCoverage \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:19.616032+00:00
---

# Method: projects.locations.agents.testCases.calculateCoverage  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.testCases.calculateCoverage Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * CoverageType
  * IntentCoverage
    * JSON representation
  * Intent
    * JSON representation
  * TransitionCoverage
    * JSON representation
  * Transition
    * JSON representation
  * TransitionNode
    * JSON representation
  * TransitionRouteGroupCoverage
    * JSON representation
  * Coverage
    * JSON representation
  * Transition
    * JSON representation
  * Try it!



Calculates the test coverage for an agent.

### HTTP request

`GET https://{endpoint}/v3/{agent=projects/*/locations/*/agents/*}/testCases:calculateCoverage`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`agent` |  `string` Required. The agent to calculate coverage for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `agent`:

  * `dialogflow.testcases.calculateCoverage`

  
  
### Query parameters

Parameters  
---  
`type` |  `enum (`[CoverageType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#CoverageType)`)` Required. The type of coverage requested.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[TestCases.CalculateCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "agent": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "intentCoverage": {
        object ([IntentCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#IntentCoverage))
      },
      "transitionCoverage": {
        object ([TransitionCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionCoverage))
      },
      "routeGroupCoverage": {
        object ([TransitionRouteGroupCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionRouteGroupCoverage))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`agent` |  `string` The agent to calculate coverage for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
The type of coverage requested. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`intentCoverage` |  `object (`[IntentCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#IntentCoverage)`)` Intent coverage.  
`transitionCoverage` |  `object (`[TransitionCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionCoverage)`)` Transition (excluding transition route groups) coverage.  
`routeGroupCoverage` |  `object (`[TransitionRouteGroupCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionRouteGroupCoverage)`)` Transition route group coverage.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## CoverageType

The type of coverage score requested.

Enums  
---  
`COVERAGE_TYPE_UNSPECIFIED` | Should never be used.  
`INTENT` | Intent coverage.  
`PAGE_TRANSITION` | Page transition coverage.  
`TRANSITION_ROUTE_GROUP` | Transition route group coverage.  
  
## IntentCoverage

Intent coverage represents the percentage of all possible intents in the agent that are triggered in any of a parent's test cases.

JSON representation  
---  
      
    
    {
      "intents": [
        {
          object ([Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Intent))
        }
      ],
      "coverageScore": number
    }  
  
Fields  
---  
`intents[]` |  `object (`[Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Intent)`)` The list of Intents present in the agent  
`coverageScore` |  `number` The percent of intents in the agent that are covered.  
  
## Intent

The agent's intent.

JSON representation  
---  
      
    
    {
      "intent": string,
      "covered": boolean
    }  
  
Fields  
---  
`intent` |  `string` The intent full resource name  
`covered` |  `boolean` Whether the intent is covered by at least one of the agent's test cases.  
  
## TransitionCoverage

Transition coverage represents the percentage of all possible page transitions (page-level transition routes and event handlers, excluding transition route groups) present within any of a parent's test cases.

JSON representation  
---  
      
    
    {
      "transitions": [
        {
          object ([Transition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Transition))
        }
      ],
      "coverageScore": number
    }  
  
Fields  
---  
`transitions[]` |  `object (`[Transition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Transition)`)` The list of Transitions present in the agent.  
`coverageScore` |  `number` The percent of transitions in the agent that are covered.  
  
## Transition

A transition in a page.

JSON representation  
---  
      
    
    {
      "source": {
        object ([TransitionNode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionNode))
      },
      "index": integer,
      "target": {
        object ([TransitionNode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionNode))
      },
      "covered": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "transitionRoute": {
        object ([TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute))
      },
      "eventHandler": {
        object ([EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`source` |  `object (`[TransitionNode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionNode)`)` The start node of a transition.  
`index` |  `integer` The index of a transition in the transition list. Starting from 0.  
`target` |  `object (`[TransitionNode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#TransitionNode)`)` The end node of a transition.  
`covered` |  `boolean` Whether the transition is covered by at least one of the agent's test cases.  
The detailed transition. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`transitionRoute` |  `object (`[TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)`)` Intent route or condition route.  
`eventHandler` |  `object (`[EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler)`)` Event handler.  
End of mutually exclusive fields.  
  
## TransitionNode

The source or target of a transition.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "page": {
        object ([Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page))
      },
      "flow": {
        object ([Flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
A TransitionNode can be either a page or a flow. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`page` |  `object (`[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)`)` Indicates a transition to a `[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)`. Only some fields such as name and displayname will be set.  
`flow` |  `object (`[Flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow)`)` Indicates a transition to a `[Flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow)`. Only some fields such as name and displayname will be set.  
End of mutually exclusive fields.  
  
## TransitionRouteGroupCoverage

Transition route group coverage represents the percentage of all possible transition routes present within any of a parent's test cases. The results are grouped by the transition route group.

JSON representation  
---  
      
    
    {
      "coverages": [
        {
          object ([Coverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Coverage))
        }
      ],
      "coverageScore": number
    }  
  
Fields  
---  
`coverages[]` |  `object (`[Coverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Coverage)`)` Transition route group coverages.  
`coverageScore` |  `number` The percent of transition routes in all the transition route groups that are covered.  
  
## Coverage

Coverage result message for one transition route group.

JSON representation  
---  
      
    
    {
      "routeGroup": {
        object ([TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup))
      },
      "transitions": [
        {
          object ([Transition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Transition_1))
        }
      ],
      "coverageScore": number
    }  
  
Fields  
---  
`routeGroup` |  `object (`[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`)` Transition route group metadata. Only name and displayName will be set.  
`transitions[]` |  `object (`[Transition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage#Transition_1)`)` The list of transition routes and coverage in the transition route group.  
`coverageScore` |  `number` The percent of transition routes in the transition route group that are covered.  
  
## Transition

A transition coverage in a transition route group.

JSON representation  
---  
      
    
    {
      "transitionRoute": {
        object ([TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute))
      },
      "covered": boolean
    }  
  
Fields  
---  
`transitionRoute` |  `object (`[TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)`)` Intent route or condition route.  
`covered` |  `boolean` Whether the transition route is covered by at least one of the agent's test cases.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
