---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.prompts.AsyncPrompts
title: Class AsyncPrompts (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:49.277216+00:00
---

# Class AsyncPrompts (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.prompts.AsyncPrompts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncPrompts (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AsyncPrompts(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `AsyncPrompts` class.

## Methods 

### create
    
    
    create(
        *,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreatePromptConfig,
                vertexai._genai.types.common.CreatePromptConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Creates a new prompt in a Vertex Dataset resource.

This method waits for prompt creation to be complete before returning.

Note: This method does not create a versioned resource for your prompt. Call create_version() to create a new prompt resource with a version.

### create_version
    
    
    create_version(
        *,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        prompt_id: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreatePromptVersionConfig,
                vertexai._genai.types.common.CreatePromptVersionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Creates a prompt resource and an initial prompt version.

When creating new prompt and prompt version resources, this waits for the create operation to complete before returning.

Note: This method is recommended instead of create() since it creates a versioned resource for your prompt.

### delete
    
    
    delete(
        *,
        prompt_id: str,
        config: typing.Optional[vertexai._genai.types.common.DeletePromptConfig] = None
    ) -> None

Deletes a prompt resource.

**Exceptions**  
---  
**Type** | **Description**  
`TimeoutError` | If the delete operation does not complete within the timeout.  
`ValueError` | If the delete operation fails.  
  
### delete_version
    
    
    delete_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.DeletePromptConfig] = None
    ) -> None

Deletes a prompt version resource.

**Exceptions**  
---  
**Type** | **Description**  
`TimeoutError` | If the delete operation does not complete within the timeout.  
`ValueError` | If the delete operation fails.  
  
### get
    
    
    get(
        *,
        prompt_id: str,
        config: typing.Optional[vertexai._genai.types.common.GetPromptConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Gets a prompt resource from a Vertex Dataset.

### get_version
    
    
    get_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.GetPromptConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Gets a prompt resource from a Vertex Dataset.

### launch_optimization_job
    
    
    launch_optimization_job(
        method: vertexai._genai.types.common.PromptOptimizerMethod,
        config: typing.Union[
            vertexai._genai.types.common.PromptOptimizerConfig,
            vertexai._genai.types.common.PromptOptimizerConfigDict,
        ],
    ) -> vertexai._genai.types.common.CustomJob

Call async Vertex AI Prompt Optimizer (VAPO).

Note: The `wait_for_completion` parameter in the config will be ignored when using the AsyncClient, as it is not supported.

Example usage: client = [vertexai.Client](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.Client)(project=PROJECT_NAME, location='us-central1') vapo_config = vertexai.types.PromptOptimizerConfig( config_path='gs://you-bucket-name/your-config.json', service_account=service_account, ) job = await client.aio.prompts.launch_optimization_job( method=types.PromptOptimizerMethod.VAPO, config=vapo_config)

### list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListPromptsConfig,
                vertexai._genai.types.common.ListPromptsConfigDict,
            ]
        ] = None
    ) -> typing.AsyncIterator[vertexai._genai.types.common.PromptRef]

Lists prompt resources in a project.

This method retrieves all the prompts from the project provided in the [vertexai.Client](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.Client) constructor and returns a list of prompt references containing the prompt_id and model for the prompt.

To get the full types.Prompt resource for a PromptRef after calling this method, use the get() method with the prompt_id as the prompt_id argument. Example usage:
    
    
    prompt_refs = client.aio.prompt_management.list_prompts()
    async for prompt_ref in prompt_refs:
      await client.prompt_management.get(prompt_id=prompt_ref.prompt_id)
    

### list_versions
    
    
    list_versions(
        *,
        prompt_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListPromptsConfig,
                vertexai._genai.types.common.ListPromptsConfigDict,
            ]
        ] = None
    ) -> typing.AsyncIterator[vertexai._genai.types.common.PromptVersionRef]

Lists prompt version resources for a provided prompt_id.

This method retrieves all the prompt versions for a provided prompt_id.

To get the full types.Prompt resource for a PromptVersionRef after calling this method, use the get() method with the returned prompt_id and version_id. Example usage:
    
    
    prompt_version_refs = await client.prompt_management.list_versions(prompt_id="123")
    async for version_ref in prompt_version_refs:
      await client.aio.prompt_management.get(prompt_id=version_ref.prompt_id, version_id=version_ref.version_id)
    

### optimize
    
    
    optimize(
        *,
        prompt: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.OptimizeConfig,
                vertexai._genai.types.common.OptimizeConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.OptimizeResponse

Makes an async request to the optimizePrompt endpoint and returns an optimized prompt.

Example usage: client = [vertexai.Client](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.Client)(project=PROJECT_NAME, location='us-central1') prompt = "Generate system instructions for analyzing medical articles" response = await client.aio.prompts.optimize(prompt=prompt)

### restore_version
    
    
    restore_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.RestoreVersionConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Restores the provided prompt version to the latest version.

### update
    
    
    update(
        *,
        prompt_id: str,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.UpdatePromptConfig,
                vertexai._genai.types.common.UpdatePromptConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Updates an existing prompt and creates a new version for the prompt associated with the provided prompt_id.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
