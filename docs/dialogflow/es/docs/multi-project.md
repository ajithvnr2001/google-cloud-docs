---
url: https://docs.cloud.google.com/dialogflow/es/docs/multi-project/
title: Using multiple projects \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:25.834569+00:00
---

# Using multiple projects  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/multi-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Using multiple projects Stay organized with collections  Save and categorize content based on your preferences. 

In some cases, you might need to create multiple Google Cloud projects to use Dialogflow CX:

  * You might find it useful to create one project for authentication, quotas, and billing, and additional projects for [agent](https://docs.cloud.google.com/dialogflow/es/docs/agents-overview) data. 
  * Each project can have [at most](https://docs.cloud.google.com/dialogflow/quotas#count_limits) one agent per [region](https://docs.cloud.google.com/dialogflow/es/docs/how/region). If you need multiple agents in the same region, then multiple projects are required. 



## Consumer and resource projects

When you make calls to the API, you typically provide [service account keys for authentication](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup#auth). Each service account is owned by a specific project, but service accounts might be [provided roles to access resources for other projects](https://docs.cloud.google.com/dialogflow/es/docs/access-control#gcp-console). The project associated with the service account you provide for an API call is referred to as the _consumer project_.

When you make calls to the API, your request specifies the agent's project. This project is referred to as the _resource project_.

For example, in the following REST curl request, the project associated with `AGENT_ID` is the resource project, and the project associated with the service account used to generate `TOKEN` is the consumer project:
    
    
    curl -X GET
        -H "Authorization: Bearer TOKEN"
        "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/AGENT_ID"
    

One project can play the role of both consumer and resource project. Agent data, charges, and quotas are associated only with this project.

When consumer and resource projects are two different projects, charges, quota constraints, agent information, and a requirement to enable the API are applicable to either or both projects, as described in the following table.

Description | Consumer project (service account project) | Resource project (agent project) | Notes  
---|---|---|---  
Project that [charges](https://cloud.google.com/products/conversational-agents/pricing) are incurred for | ✔ |  |   
Project that is bound to [quotas](https://docs.cloud.google.com/dialogflow/quotas) | ✔ |  |   
Project that contains the agent that determines the [Trial or Essentials Dialogflow edition](https://docs.cloud.google.com/dialogflow/docs/editions) | ✔ |  | If your consumer project doesn't have an agent, create an empty agent to [upgrade to the Essentials edition](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#change-editions).  
Project that contains all [agent data](https://docs.cloud.google.com/dialogflow/es/docs/agents-overview) and the [Trial or Essentials Dialogflow edition](https://docs.cloud.google.com/dialogflow/docs/editions) |  | ✔ |   
Projects for which you must [enable the Dialogflow API](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup#api) | ✔ | ✔ | The Dialogflow CX API must be enabled for both project types.  
Project that shows API usage on the Cloud console [API dashboard](https://docs.cloud.google.com/apis/docs/monitoring) | ✔ |  |   
  
[ Previous arrow_back  Access control  ](https://docs.cloud.google.com/dialogflow/es/docs/access-control)

[ Next Using VPC Service Controls  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/vpc-service-controls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
