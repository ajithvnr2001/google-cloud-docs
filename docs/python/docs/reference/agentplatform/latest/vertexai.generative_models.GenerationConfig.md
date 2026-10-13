---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.generative_models.GenerationConfig
title: Class GenerationConfig (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:10.180466+00:00
---

# Class GenerationConfig (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.generative_models.GenerationConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerationConfig (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    GenerationConfig(
        *,
        temperature: typing.Optional[float] = None,
        top_p: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        candidate_count: typing.Optional[int] = None,
        max_output_tokens: typing.Optional[int] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        response_mime_type: typing.Optional[str] = None,
        response_schema: typing.Optional[typing.Dict[str, typing.Any]] = None,
        seed: typing.Optional[int] = None,
        audio_timestamp: typing.Optional[bool] = None,
        routing_config: typing.Optional[RoutingConfig] = None,
        logprobs: typing.Optional[int] = None,
        response_logprobs: typing.Optional[bool] = None,
        response_modalities: typing.Optional[typing.List[GenerationConfig.Modality]] = None,
        model_config: typing.Optional[GenerationConfig.ModelConfig] = None
    )

Parameters for the generation.

## Classes 

### Modality
    
    
    Modality(value)

The modalities of the response.

### ModelConfig
    
    
    ModelConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Config for model selection.

### RoutingConfig
    
    
    RoutingConfig(
        *,
        routing_config: typing.Union[
            vertexai.generative_models._generative_models.GenerationConfig.RoutingConfig.AutoRoutingMode,
            vertexai.generative_models._generative_models.GenerationConfig.RoutingConfig.ManualRoutingMode,
        ]
    )

The configuration for model router requests. Deprecated, please use ModelConfig to set routing preference instead.

The routing config is either one of the two nested classes:

  * AutoRoutingMode: Automated routing.
  * ManualRoutingMode: Manual routing.



Usage:

  * AutoRoutingMode:
        
        routing_config=generative_models.RoutingConfig(
            routing_config=generative_models.RoutingConfig.AutoRoutingMode(
                model_routing_preference=generative_models.RoutingConfig.AutoRoutingMode.ModelRoutingPreference.BALANCED,
            ),
        )
        

  * ManualRoutingMode:
        
        routing_config=generative_models.RoutingConfig(
            routing_config=generative_models.RoutingConfig.ManutalRoutingMode(
                model_name="gemini-1.5-pro-001",
            ),
        )
        




## Methods 

### GenerationConfig
    
    
    GenerationConfig(
        *,
        temperature: typing.Optional[float] = None,
        top_p: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        candidate_count: typing.Optional[int] = None,
        max_output_tokens: typing.Optional[int] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        response_mime_type: typing.Optional[str] = None,
        response_schema: typing.Optional[typing.Dict[str, typing.Any]] = None,
        seed: typing.Optional[int] = None,
        audio_timestamp: typing.Optional[bool] = None,
        routing_config: typing.Optional[RoutingConfig] = None,
        logprobs: typing.Optional[int] = None,
        response_logprobs: typing.Optional[bool] = None,
        response_modalities: typing.Optional[typing.List[GenerationConfig.Modality]] = None,
        model_config: typing.Optional[GenerationConfig.ModelConfig] = None
    )

Constructs a GenerationConfig object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
