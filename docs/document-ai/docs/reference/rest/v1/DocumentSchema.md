---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema/
title: DocumentSchema \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:16.863855+00:00
---

# DocumentSchema  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  DocumentSchema Stay organized with collections  Save and categorize content based on your preferences. 

The schema defines the output of the processed document by a processor.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "description": string,
      "entityTypes": [
        {
          object ([EntityType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#EntityType))
        }
      ],
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#Metadata))
      },
      "documentPrompt": string
    }  
  
Fields  
---  
`displayName` |  `string` Display name to show users.  
`description` |  `string` Description of the schema.  
`entityTypes[]` |  `object (`[EntityType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#EntityType)`)` Entity types of the schema.  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#Metadata)`)` Metadata of the schema.  
`documentPrompt` |  `string` Optional. Document-level prompt provided by the user. This custom text is injected into the AI model's prompt to provide extra, document-wide guidance for processing.  
  
## EntityType

EntityType is the wrapper of a label of the corresponding model with detailed attributes and limitations for entity-based processors. Multiple types can also compose a dependency tree to represent nested types.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "name": string,
      "baseTypes": [
        string
      ],
      "properties": [
        {
          object ([Property](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#Property))
        }
      ],
    
      // Union field value_source can be only one of the following:
      "enumValues": {
        object ([EnumValues](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#EnumValues))
      }
      // End of list of possible types for union field value_source.
    }  
  
Fields  
---  
`displayName` |  `string` User defined name for the type.  
`name` |  `string` Name of the type. It must be unique within the schema file and cannot be a "Common Type". The following naming conventions are used:

  * Use `snake_casing`.
  * Name matching is case-sensitive.
  * Maximum 64 characters.
  * Must start with a letter.
  * Allowed characters: ASCII letters `[a-z0-9_-]`. (For backward compatibility, internal infrastructure and tooling can handle any ASCII character.)
  * The `/` is sometimes used to denote a property of a type. For example, `line_item/amount`. This convention is deprecated, but will still be honored for backward compatibility.

  
`baseTypes[]` |  `string` The entity type that this type is derived from. For now, one and only one should be set.  
`properties[]` |  `object (`[Property](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#Property)`)` Description the nested structure, or composition of an entity.  
Union field `value_source`.`value_source` can be only one of the following:  
`enumValues` |  `object (`[EnumValues](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#EnumValues)`)` If specified, lists all the possible values for this entity. This should not be more than a handful of values. If the number of values is >10 or could change frequently, use the `EntityType.value_ontology` field and specify a list of all possible values in a value ontology file.  
  
## EnumValues

Defines the a list of enum values.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string` The individual values that this enum values type can include.  
  
## Property

Defines properties that can be part of the entity type.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "valueType": string,
      "occurrenceType": enum ([OccurrenceType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#OccurrenceType)),
      "method": enum ([Method](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#Method))
    }  
  
Fields  
---  
`name` |  `string` The name of the property. Follows the same guidelines as the EntityType name.  
`displayName` |  `string` User defined name for the property.  
`valueType` |  `string` A reference to the value type of the property. This type is subject to the same conventions as the `Entity.base_types` field.  
`occurrenceType` |  `enum (`[OccurrenceType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#OccurrenceType)`)` Occurrence type limits the number of instances an entity type appears in the document.  
`method` |  `enum (`[Method](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#Method)`)` Specifies how the entity's value is obtained.  
  
## OccurrenceType

Types of occurrences of the entity type in the document. This represents the number of instances, not mentions, of an entity. For example, a bank statement might only have one `account_number`, but this account number can be mentioned in several places on the document. In this case, the `account_number` is considered a `REQUIRED_ONCE` entity type. If, on the other hand, it's expected that a bank statement contains the status of multiple different accounts for the customers, the occurrence type is set to `REQUIRED_MULTIPLE`.

Enums  
---  
`OCCURRENCE_TYPE_UNSPECIFIED` | Unspecified occurrence type.  
`OPTIONAL_ONCE` | There will be zero or one instance of this entity type. The same entity instance may be mentioned multiple times.  
`OPTIONAL_MULTIPLE` | The entity type will appear zero or multiple times.  
`REQUIRED_ONCE` | The entity type will only appear exactly once. The same entity instance may be mentioned multiple times.  
`REQUIRED_MULTIPLE` | The entity type will appear once or more times.  
  
## Method

Specifies how the entity's value is obtained from the document.

Enums  
---  
`METHOD_UNSPECIFIED` | Unspecified method. It defaults to `EXTRACT`.  
`EXTRACT` | The entity's value is directly extracted as-is from the document text.  
`DERIVE` | The entity's value is derived through inference and is not necessarily an exact text extraction from the document.  
`RELAXED_EXTRACT` | Attempts to extract the position and value as-is from the document text. If the value cannot be grounded in the text, it falls back to derivation through inference, for both position and value. Note: The inference fallback is currently only supported for boolean entities.  
  
## Metadata

Metadata for global schema behavior.

JSON representation  
---  
      
    
    {
      "documentSplitter": boolean,
      "documentAllowMultipleLabels": boolean,
      "prefixedNamingOnProperties": boolean,
      "skipNamingValidation": boolean
    }  
  
Fields  
---  
`documentSplitter` |  `boolean` If true, a `document` entity type can be applied to subdocument (splitting). Otherwise, it can only be applied to the entire document (classification).  
`documentAllowMultipleLabels` |  `boolean` If true, on a given page, there can be multiple `document` annotations covering it.  
`prefixedNamingOnProperties` |  `boolean` If set, all the nested entities must be prefixed with the parents.  
`skipNamingValidation` |  `boolean` If set, this will skip the naming format validation in the schema. So the string values in `DocumentSchema.EntityType.name` and `DocumentSchema.EntityType.Property.name` will not be checked.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
