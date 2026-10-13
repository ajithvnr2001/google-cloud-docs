---
url: https://docs.cloud.google.com/looker/docs/reference/param-agent/
title: agent \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.662886+00:00
---

# agent  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Usage
    
    
    agent: agent_name {
      advanced_analytics: yes | no
      description: "string"
      instructions: "string"
      is_dashboard_agent: yes | no
      show_debuginfo: yes | no
      show_thinking: yes | no
    }
    

Hierarchy [Model file](https://docs.cloud.google.com/looker/docs/reference/param-model) or LookML file `agent` |  Default value None Accepts

  * `advanced_analytics`: `yes | no` (Defaults to `no`).
  * `description`: A string describing the agent.
  * `instructions`: A string specifying custom prompts and behavior rules. Supports LookML constants (`@{CONSTANT_NAME}`).
  * `is_dashboard_agent`: `yes | no` (Required as `yes` for dashboard agents).
  * `show_debuginfo`: `yes | no` (Defaults to `no`).
  * `show_thinking`: `yes | no` (Defaults to `no`).

  
---|---  
  
## Definition

The `agent` parameter defines a data agent for a [LookML dashboard](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard). Developers can use this parameter and its subparameters to define custom agent instructions, analytical behavior, and display preferences in version-controlled LookML for a single agent that is associated with a single LookML dashboard.

Developers can associate a dashboard agent with a single LookML dashboard by using the [`default_dashboard_agent`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#default_dashboard_agent) parameter.

Data agents for user-defined dashboards or for Explores cannot be defined in LookML.

For detailed information on configuring and using LookML dashboard agents, see the [Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards) documentation page.

## Subparameters

Dashboard agent definitions support the following subparameters:

  * `advanced_analytics`
  * `description`
  * `instructions`
  * `is_dashboard_agent`
  * `show_debuginfo`
  * `show_thinking`



### `advanced_analytics`

The `advanced_analytics` subparameter controls whether the agent can use [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) to generate and run Python code for complex computations and custom visualizations.

Accepts `yes` or `no`. The default value is `no`.

### `description`

The `description` subparameter provides an optional text description of the agent's purpose.
    
    
    agent: sales_agent {
      description: "Executive sales overview dashboard agent"
      is_dashboard_agent: yes
    }
    

### `instructions`

**Note:** [Verified queries](https://docs.cloud.google.com/looker/docs/glossary#verified_query) aren't supported for agents on LookML dashboards.

The `instructions` subparameter accepts a free-form string that provides the agent with business context, preferred fields, filtering rules, or tone of voice when processing conversational questions.
    
    
    agent: sales_agent {
      instructions: "Focus on net revenue and filter by current quarter by default."
      is_dashboard_agent: yes
    }
    

You can reference [LookML constants](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant) within `instructions` by using `@{<var>CONSTANT_NAME</var>}` syntax:
    
    
    agent: sales_agent {
      instructions: "Focus on net revenue. @{FISCAL_YEAR_RULE}"
      is_dashboard_agent: yes
    }
    

If omitted, the agent operates without custom instruction context.

### `is_dashboard_agent`

The `is_dashboard_agent` subparameter specifies whether the agent is configured as a dashboard agent.

Accepts `yes` or `no`. To use the agent with a LookML dashboard, set this parameter to `yes`.

### `show_debuginfo`

The `show_debuginfo` subparameter determines whether the agent displays execution logs and diagnostic information in conversation responses.

Accepts `yes` or `no`. The default value is `no`.

### `show_thinking`

The `show_thinking` subparameter determines whether the agent displays its reasoning steps and intermediate query planning in conversation responses.

Accepts `yes` or `no`. The default value is `no`.

## Examples

### Defining a LookML dashboard agent

The following example defines a LookML dashboard agent with custom instructions, Advanced Analytics enabled, and thinking visibility turned on:
    
    
    agent: customer_insights_agent {
      instructions: "Address the user politely. Prioritize active subscriber metrics and churn analysis."
      description: "Dashboard agent for Customer Insights dashboard."
      is_dashboard_agent: yes
      advanced_analytics: yes
      show_thinking: yes
      show_debuginfo: no
    }
    

To use this agent on a LookML dashboard, map it in the `.dashboard.lookml` file:
    
    
    - dashboard: customer_insights
      title: "Customer Insights"
      layout: newspaper
      enabled_dashboard_agents: true
      default_dashboard_agent: customer_insights_agent
    
      elements:
      - name: active_subscribers
        type: single_value
        model: subscriptions
        explore: customers
        measures: [customers.count]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
