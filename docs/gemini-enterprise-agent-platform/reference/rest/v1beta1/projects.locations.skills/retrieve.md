---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/retrieve/
title: Method: skills.retrieve \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:49:23.010639+00:00
---

# Method: skills.retrieve  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/retrieve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: skills.retrieve Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.skills.retrieve

Retrieves skills.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/skills:retrieve`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The location to retrieve the Skills in. Format: `projects/{project}/locations/{location}`

### Query parameters

| `query` `string` Optional. The query to find matching skills. | `topK` `integer` Optional. The maximum number of skills to return. The service may return fewer than this value. If unspecified, at most 10 skills will be returned. The maximum value is 100.

### Request body

The request body must be empty.

### Response body

Response message for `[SkillRegistryService.RetrieveSkills](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/retrieve#google.cloud.aiplatform.v1beta1.SkillRegistryService.RetrieveSkills)`. If successful, the response body contains data with the following structure: | Fields  
  
`retrievedSkills[]` `object (`[RetrievedSkill](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/retrieve#RetrievedSkill)`)` Skills ranked by similarity if applicable; otherwise, the order is undefined. | JSON representation  
---  
      
    
    {
      "retrievedSkills": [
        {
          object ([RetrievedSkill](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/retrieve#RetrievedSkill))
        }
      ]
    }  
  
## RetrievedSkill

A retrieved skill.

Fields  
  
`skillName` `string` The skill resource name. Format: projects/{project}/locations/{location}/skills/{skill} | `description` `string` The skill description. | JSON representation  
---  
      
    
    {
      "skillName": string,
      "description": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
