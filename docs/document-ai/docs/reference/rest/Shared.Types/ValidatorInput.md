---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput/
title: ValidatorInput \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:36.859940+00:00
---

# ValidatorInput  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  ValidatorInput Stay organized with collections  Save and categorize content based on your preferences. 

Definition of the validation rules. Those are the input to the validator logic and they are used to validate a document. Next ID: 3

JSON representation  
---  
      
    
    {
      "validationRules": [
        {
          object ([ValidationRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#ValidationRule))
        }
      ]
    }  
  
Fields  
---  
`validationRules[]` |  `object (`[ValidationRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#ValidationRule)`)`  
  
## ValidationRule

Next ID: 9

JSON representation  
---  
      
    
    {
      "ruleId": string,
      "name": string,
      "description": string,
    
      // Union field validation_rule can be only one of the following:
      "fieldOccurrences": {
        object ([FieldOccurrences](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#FieldOccurrences))
      },
      "fieldRegex": {
        object ([FieldRegex](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#FieldRegex))
      },
      "formValidation": {
        object ([FormValidation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#FormValidation))
      },
      "childAlignmentRule": {
        object ([ChildAlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#ChildAlignmentRule))
      },
      "entityAlignmentRule": {
        object ([EntityAlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#EntityAlignmentRule))
      }
      // End of list of possible types for union field validation_rule.
    }  
  
Fields  
---  
`ruleId` |  `string` Unique identifier of the rule. Optional.  
`name` |  `string` Name of the validation rule.  
`description` |  `string` Description of the validation rule. This has no use but for documentation.  
Union field `validation_rule`.`validation_rule` can be only one of the following:  
`fieldOccurrences` |  `object (`[FieldOccurrences](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#FieldOccurrences)`)`  
`fieldRegex` |  `object (`[FieldRegex](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#FieldRegex)`)`  
`formValidation` |  `object (`[FormValidation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#FormValidation)`)`  
`childAlignmentRule` |  `object (`[ChildAlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#ChildAlignmentRule)`)`  
`entityAlignmentRule` |  `object (`[EntityAlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#EntityAlignmentRule)`)`  
  
## FieldOccurrences

JSON representation  
---  
      
    
    {
      "field": {
        object ([Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field))
      },
      "minOccurrences": integer,
      "maxOccurrences": integer
    }  
  
Fields  
---  
`field` |  `object (`[Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field)`)`  
`minOccurrences` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Min and max occurrences of the field. If not set, there is limit set. The defined interval is a closed-closed interval, i.e. [min, max].  
`maxOccurrences` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
  
## Field

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "defaultValue": {
        object ([Constant](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Constant))
      }
    }  
  
Fields  
---  
`fieldName` |  `string` The field name to validate. This can be a simple field name or a nested field one using the ':' (meant as an aggregator) or '*' (meant as foreach) operators.  
`defaultValue` |  `object (`[Constant](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Constant)`)` Default value to use if the field is not present. If the field is missing and the default value is not set, the validation run as if the field is not present in the validation logic.  
  
## Constant

The constant value used in the validation rules.

JSON representation  
---  
      
    
    {
      "floatValue": number
    }  
  
Fields  
---  
`floatValue` |  `number`  
  
## FieldRegex

JSON representation  
---  
      
    
    {
      "field": {
        object ([Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field))
      },
      "pattern": string
    }  
  
Fields  
---  
`field` |  `object (`[Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field)`)`  
`pattern` |  `string` Python regex to validate the field values.  
  
## FormValidation

JSON representation  
---  
      
    
    {
      "leftOperand": {
        object ([Operation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Operation))
      },
      "rightOperand": {
        object ([Operation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Operation))
      },
      "validationOperator": enum ([RelationalOperator](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/RelationalOperator))
    }  
  
Fields  
---  
`leftOperand` |  `object (`[Operation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Operation)`)`  
`rightOperand` |  `object (`[Operation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Operation)`)`  
`validationOperator` |  `enum (`[RelationalOperator](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/RelationalOperator)`)` The relational operator to be applied to the operands.  
  
## Operation

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field))
        }
      ],
      "constants": [
        {
          object ([Constant](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Constant))
        }
      ],
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Operation))
        }
      ],
      "operationType": enum ([OperationType](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/OperationType))
    }  
  
Fields  
---  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field)`)` A list of fields to be used as operands.  
`constants[]` |  `object (`[Constant](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Constant)`)` A list of constants to be used as operands.  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Operation)`)` A list of recursive operations to be used as operands.  
`operationType` |  `enum (`[OperationType](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/OperationType)`)` The operation type to be applied to all the operands.  
  
## ChildAlignmentRule

A rule that aligns specified child fields with a parent field.

JSON representation  
---  
      
    
    {
      "parentField": {
        object ([Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field))
      },
      "childFields": [
        {
          object ([Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field))
        }
      ],
      "alignmentRule": {
        object ([AlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#AlignmentRule))
      }
    }  
  
Fields  
---  
`parentField` |  `object (`[Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field)`)` The full path of the parent field.  
`childFields[]` |  `object (`[Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field)`)` The child fields to be aligned within the parent field.  
`alignmentRule` |  `object (`[AlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#AlignmentRule)`)` The alignment rule to apply to the child fields.  
  
## AlignmentRule

A rule for checking field alignment. Horizontal alignment checks if fields are on the same row by comparing y-coordinates of bounding box centers, while vertical alignment checks if fields are on the same column by comparing x-coordinates of bounding box centers.

JSON representation  
---  
      
    
    {
      "alignmentType": enum ([AlignmentType](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/AlignmentType)),
      "tolerance": number
    }  
  
Fields  
---  
`alignmentType` |  `enum (`[AlignmentType](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/AlignmentType)`)`  
`tolerance` |  `number` The tolerance to use when comparing coordinates.  
  
## EntityAlignmentRule

A rule that aligns specified fields with each other.

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field))
        }
      ],
      "alignmentRule": {
        object ([AlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#AlignmentRule))
      }
    }  
  
Fields  
---  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#Field)`)` The fields to be aligned.  
`alignmentRule` |  `object (`[AlignmentRule](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ValidatorInput#AlignmentRule)`)` The alignment rule to apply to the fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
