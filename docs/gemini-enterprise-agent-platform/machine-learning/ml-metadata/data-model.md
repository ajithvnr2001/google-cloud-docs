---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/data-model/
title: Data model and resources \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:45.251375+00:00
---

# Data model and resources  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/data-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Data model and resources Stay organized with collections  Save and categorize content based on your preferences. 

Vertex ML Metadata organizes resources hierarchically, where every resource belongs to a MetadataStore. You must first have a MetadataStore before you can create Metadata resources.

## Vertex ML Metadata terminology

The following introduces the data model and terminology that is used to describe Vertex ML Metadata resources and components.

##### **MetadataStore**

  * A MetadataStore is the top-level container for metadata resources. MetadataStore is regionalized and associated with a specific Google Cloud project. Typically, an organization uses one shared MetadataStore for metadata resources within each project. 



##### **artifact**

  * An artifact is a discrete entity or piece of data produced and consumed by a machine learning workflow. Examples of artifacts include datasets, models, input files, and training logs. 



##### **context**

  * A context is used to group artifacts and executions together under a single, queryable, and typed category. Contexts can be used to represent sets of metadata. An example of a Context would be a run of a machine learning pipeline. 

For example, you can use contexts to represent sets of metadata such as: 
  * A Gemini Enterprise Agent Platform Pipelines pipeline run. In this case, the context represents one run and each execution represents a step in the ML pipeline. ![Shows how artifacts, executions, and context combine into
Vertex ML Metadata's graph data model.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/ml-metadata/images/artifact-execution-context-graph.png)

  * An experiment run from a notebook. In this case, the context could represent the notebook and each execution could represent a cell in that notebook. 

##### **event**

    * An event describes the relationship between artifacts and executions. Each artifact can be produced by an execution and consumed by other executions. Events help you to determine the provenance of artifacts in their ML workflows by chaining together artifacts and executions. 

##### **execution**

    * An execution is a record of an individual machine learning workflow step, typically annotated with its runtime parameters. Examples of executions include data ingestion, data validation, model training, model evaluation, and model deployment. 

##### **MetadataSchema**

    * A MetadataSchema describes the schema for particular types of artifacts, executions, or contexts. MetadataSchemas are used to validate the key-value pairs during creation of the corresponding Metadata resources. Schema validation is only performed on matching fields between the resource and the MetadataSchema. Type schemas are represented using OpenAPI Schema Objects, which should be described using YAML. 



#### MetadataSchema example

Type schemas are represented using [OpenAPI Schema Objects](https://swagger.io/specification/#schema-object), which should be described using YAML.

The following is an example of how the predefined `Model` system type is specified in YAML format.
    
    
    title: system.Model
    type: object
    properties:
      framework:
        type: string
        description: "The framework type, for example 'TensorFlow' or 'Scikit-Learn'."
      framework_version:
        type: string
        description: "The framework version, for example '1.15' or '2.1'"
      payload_format:
        type: string
        description: "The format of the Model payload, for example 'SavedModel' or 'TFLite'"
    

**Note:** Resources don't need to include all the fields defined in the corresponding MetadataSchema. They can also include additional fields that aren't defined in the MetadataSchema.

The title of the schema must use the format `<namespace>.<type name>`. Vertex ML Metadata publishes and maintains system-defined schemas for representing common types widely used in ML workflows. These schemas live under the namespace `system`, and can be accessed as MetadataSchema resources in the API. Schemas are always versioned.

To learn more about schemas, see [System schemas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/system-schemas). Additionally, Vertex ML Metadata lets you create user-defined Custom Schemas. To learn more about System Schemas, see [How to register your own custom schemas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/custom-schemas#how_to_register_your_own_custom_schemas).

The Metadata resources exposed closely mirror those of the open source implementation of [ML Metadata (MLMD)](https://github.com/google/ml-metadata).

## What's next

  * [Learn more about predefined system schemas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/system-schemas).
  * [Start tracking with Vertex ML Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/tracking).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
