---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.skills.Skills
title: Class Skills (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:52.679200+00:00
---

# Class Skills (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.skills.Skills

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Skills (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    Skills(api_client_: google.genai._api_client.BaseApiClient)

Class for managing Skills in the Skill Registry.

## Properties 

### revisions

Returns the revisions sub-module.

## Methods 

### create
    
    
    create(
        *,
        display_name: str,
        description: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateSkillConfig,
                vertexai._genai.types.common.CreateSkillConfigDict,
            ]
        ] = None
    ) -> typing.Union[
        vertexai._genai.types.common.Skill, vertexai._genai.types.common.SkillOperation
    ]

Creates a new Skill.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The display name of the Skill.  
`description` |  `str`   
Required. The description of the Skill.  
`config` |  `CreateSkillConfigOrDict`   
Optional. The configuration for creating the Skill.  
**Returns**  
---  
**Type** | **Description**  
`Skill` | The created Skill if wait_for_completion is True. SkillOperation: The operation for creating the Skill if wait_for_completion is False.  
  
### delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteSkillConfig,
                vertexai._genai.types.common.DeleteSkillConfigDict,
            ]
        ] = None
    ) -> typing.Optional[vertexai._genai.types.common.DeleteSkillOperation]

Deletes a Skill.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name of the Skill to delete. Format: projects/{project}/locations/{location}/skills/{skill}  
`config` |  `DeleteSkillConfigOrDict`   
Optional. Additional configuration for the delete operation.  
**Returns**  
---  
**Type** | **Description**  
`DeleteSkillOperation` | The pending LRO if wait_for_completion is False, otherwise None (blocks until done).  
  
### get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetSkillConfig,
                vertexai._genai.types.common.GetSkillConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Skill

Gets a Skill.

### list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListSkillsConfig,
                vertexai._genai.types.common.ListSkillsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Skill]

Lists Skills in the Skill Registry.

**Parameter**  
---  
**Name** | **Description**  
`config` |  `ListSkillsConfigOrDict`   
Optional. Additional configuration for listing Skills.  
**Returns**  
---  
**Type** | **Description**  
`Iterator[Skill]` | An iterator (Pager) of Skills.  
  
### retrieve
    
    
    retrieve(
        *,
        query: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveSkillsConfig,
                vertexai._genai.types.common.RetrieveSkillsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RetrieveSkillsResponse

Retrieves skills semantically matched to a query.

### update
    
    
    update(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.UpdateSkillConfig,
                vertexai._genai.types.common.UpdateSkillConfigDict,
            ]
        ] = None
    ) -> typing.Union[
        vertexai._genai.types.common.Skill, vertexai._genai.types.common.SkillOperation
    ]

Updates an existing Skill.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name of the Skill to update. Format: projects/{project}/locations/{location}/skills/{skill}  
`config` |  `UpdateSkillConfigOrDict`   
Optional. The configuration for updating the Skill.  
**Returns**  
---  
**Type** | **Description**  
`Skill` | The updated Skill if wait_for_completion is True. SkillOperation: The operation for updating the Skill if wait_for_completion is False.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
