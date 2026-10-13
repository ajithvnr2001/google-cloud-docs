---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction/
title: DataProfileAction \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:43.380295+00:00
---

# DataProfileAction  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  DataProfileAction Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Export
    * JSON representation
  * PubSubNotification
    * JSON representation
  * EventType
  * DataProfilePubSubCondition
    * JSON representation
  * PubSubExpressions
    * JSON representation
  * PubSubLogicalOperator
  * PubSubCondition
    * JSON representation
  * ProfileScoreBucket
  * DetailLevel
  * PublishToChronicle
  * PublishToSecurityCommandCenter
  * TagResources
    * JSON representation
  * TagCondition
    * JSON representation
  * TagValue
    * JSON representation
  * ProfileGeneration
  * PublishToDataplexCatalog
    * JSON representation



A task to execute when a data profile has been generated.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "exportData": {
        object ([Export](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#Export))
      },
      "pubSubNotification": {
        object ([PubSubNotification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubNotification))
      },
      "publishToChronicle": {
        object ([PublishToChronicle](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PublishToChronicle))
      },
      "publishToScc": {
        object ([PublishToSecurityCommandCenter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PublishToSecurityCommandCenter))
      },
      "tagResources": {
        object ([TagResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#TagResources))
      },
      "publishToDataplexCatalog": {
        object ([PublishToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PublishToDataplexCatalog))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Type of action to execute when a profile is generated. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`exportData` |  `object (`[Export](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#Export)`)` Export data profiles into a provided location.  
`pubSubNotification` |  `object (`[PubSubNotification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubNotification)`)` Publish a message into the Pub/Sub topic.  
`publishToChronicle` |  `object (`[PublishToChronicle](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PublishToChronicle)`)` Publishes generated data profiles to Google Security Operations. For more information, see [Use Sensitive Data Protection data in context-aware analytics](https://docs.cloud.google.com/chronicle/docs/detection/usecase-dlp-high-risk-user-download).  
`publishToScc` |  `object (`[PublishToSecurityCommandCenter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PublishToSecurityCommandCenter)`)` Publishes findings to Security Command Center for each data profile.  
`tagResources` |  `object (`[TagResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#TagResources)`)` Tags the profiled resources with the specified tag values.  
`publishToDataplexCatalog` |  `object (`[PublishToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PublishToDataplexCatalog)`)` Publishes a portion of each profile to Dataplex Universal Catalog with the aspect type Sensitive Data Protection Profile.  
End of mutually exclusive fields.  
  
## Export

If set, the detailed data profiles will be persisted to the location of your choice whenever updated.

JSON representation  
---  
      
    
    {
      "profileTable": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      },
      "sampleFindingsTable": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      }
    }  
  
Fields  
---  
`profileTable` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` Store all profiles to BigQuery.

  * The system will create a new dataset and table for you if none are are provided. The dataset will be named `sensitive_data_protection_discovery` and table will be named `discovery_profiles`. This table will be placed in the same project as the container project running the scan. After the first profile is generated and the dataset and table are created, the discovery scan configuration will be updated with the dataset and table names.
  * See [Analyze data profiles stored in BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles).
  * See [Sample queries for your BigQuery table](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#sample_sql_queries).
  * Data is inserted using [streaming insert](https://cloud.google.com/blog/products/bigquery/life-of-a-bigquery-streaming-insert) and so data may be in the buffer for a period of time after the profile has finished.
  * The Pub/Sub notification is sent before the streaming buffer is guaranteed to be written, so data may not be instantly visible to queries by the time your topic receives the Pub/Sub notification.
  * The best practice is to use the same table for an entire organization so that you can take advantage of the [provided Data Studio reports](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#use_a_premade_report). If you use VPC Service Controls to define security perimeters, then you must use a separate table for each boundary.

  
`sampleFindingsTable` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` Store sample `[data profile findings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding)` in an existing table or a new table in an existing dataset. Each regeneration will result in new rows in BigQuery. Data is inserted using [streaming insert](https://cloud.google.com/blog/products/bigquery/life-of-a-bigquery-streaming-insert) and so data may be in the buffer for a period of time after the profile has finished.  
  
## PubSubNotification

Send a Pub/Sub message into the given Pub/Sub topic to connect other systems to data profile generation. The message payload data will be the byte serialization of `DataProfilePubSubMessage`.

JSON representation  
---  
      
    
    {
      "topic": string,
      "event": enum ([EventType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#EventType)),
      "pubsubCondition": {
        object ([DataProfilePubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#DataProfilePubSubCondition))
      },
      "detailOfMessage": enum ([DetailLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#DetailLevel))
    }  
  
Fields  
---  
`topic` |  `string` Cloud Pub/Sub topic to send notifications to. Format is projects/{project}/topics/{topic}.  
`event` |  `enum (`[EventType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#EventType)`)` The type of event that triggers a Pub/Sub. At most one `PubSubNotification` per EventType is permitted.  
`pubsubCondition` |  `object (`[DataProfilePubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#DataProfilePubSubCondition)`)` Conditions (e.g., data risk or sensitivity level) for triggering a Pub/Sub.  
`detailOfMessage` |  `enum (`[DetailLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#DetailLevel)`)` How much data to include in the Pub/Sub message. If the user wishes to limit the size of the message, they can use resourceName and fetch the profile fields they wish to. Per table profile (not per column).  
  
## EventType

Types of event that can trigger an action.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | Unused.  
`NEW_PROFILE` | New profile (not a re-profile).  
`CHANGED_PROFILE` | One of the following profile metrics changed: Data risk score, Sensitivity score, Resource visibility, Encryption type, Predicted infoTypes, Other infoTypes  
`SCORE_INCREASED` | Table data risk score or sensitivity score increased.  
`ERROR_CHANGED` | A user (non-internal) error occurred.  
  
## DataProfilePubSubCondition

A condition for determining whether a Pub/Sub should be triggered.

JSON representation  
---  
      
    
    {
      "expressions": {
        object ([PubSubExpressions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubExpressions))
      }
    }  
  
Fields  
---  
`expressions` |  `object (`[PubSubExpressions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubExpressions)`)` An expression.  
  
## PubSubExpressions

An expression, consisting of an operator and conditions.

JSON representation  
---  
      
    
    {
      "logicalOperator": enum ([PubSubLogicalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubLogicalOperator)),
      "conditions": [
        {
          object ([PubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubCondition))
        }
      ]
    }  
  
Fields  
---  
`logicalOperator` |  `enum (`[PubSubLogicalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubLogicalOperator)`)` The operator to apply to the collection of conditions.  
`conditions[]` |  `object (`[PubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#PubSubCondition)`)` Conditions to apply to the expression.  
  
## PubSubLogicalOperator

Logical operators for conditional checks.

Enums  
---  
`LOGICAL_OPERATOR_UNSPECIFIED` | Unused.  
`OR` | Conditional OR.  
`AND` | Conditional AND.  
  
## PubSubCondition

A condition consisting of a value.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "minimumRiskScore": enum ([ProfileScoreBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#ProfileScoreBucket)),
      "minimumSensitivityScore": enum ([ProfileScoreBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#ProfileScoreBucket))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The value for the condition to trigger. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`minimumRiskScore` |  `enum (`[ProfileScoreBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#ProfileScoreBucket)`)` The minimum data risk score that triggers the condition.  
`minimumSensitivityScore` |  `enum (`[ProfileScoreBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#ProfileScoreBucket)`)` The minimum sensitivity level that triggers the condition.  
End of mutually exclusive fields.  
  
## ProfileScoreBucket

Various score levels for resources.

Enums  
---  
`PROFILE_SCORE_BUCKET_UNSPECIFIED` | Unused.  
`HIGH` | High risk/sensitivity detected.  
`MEDIUM_OR_HIGH` | Medium or high risk/sensitivity detected.  
  
## DetailLevel

The levels of detail that can be included in the Pub/Sub message.

Enums  
---  
`DETAIL_LEVEL_UNSPECIFIED` | Unused.  
`TABLE_PROFILE` | The full table data profile.  
`RESOURCE_NAME` | The name of the profiled resource.  
`FILE_STORE_PROFILE` | The full file store data profile.  
  
## PublishToChronicle

This type has no fields.

Message expressing intention to publish to Google Security Operations.

## PublishToSecurityCommandCenter

This type has no fields.

If set, a summary finding will be created or updated in Security Command Center for each profile.

## TagResources

If set, attaches the [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) provided to profiled resources. Tags support [access control](https://docs.cloud.google.com/iam/docs/tags-access-control). You can conditionally grant or deny access to a resource based on whether the resource has a specific tag.

JSON representation  
---  
      
    
    {
      "tagConditions": [
        {
          object ([TagCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#TagCondition))
        }
      ],
      "profileGenerationsToTag": [
        enum ([ProfileGeneration](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#ProfileGeneration))
      ],
      "lowerDataRiskToLow": boolean
    }  
  
Fields  
---  
`tagConditions[]` |  `object (`[TagCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#TagCondition)`)` The tags to associate with different conditions.  
`profileGenerationsToTag[]` |  `enum (`[ProfileGeneration](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#ProfileGeneration)`)` The profile generations for which the tag should be attached to resources. If you attach a tag to only new profiles, then if the sensitivity score of a profile subsequently changes, its tag doesn't change. By default, this field includes only new profiles. To include both new and updated profiles for tagging, this field should explicitly include both `PROFILE_GENERATION_NEW` and `PROFILE_GENERATION_UPDATE`.  
`lowerDataRiskToLow` |  `boolean` Whether applying a tag to a resource should lower the risk of the profile for that resource. For example, in conjunction with an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview), you can deny all principals a permission if a tag value is present, mitigating the risk of the resource. This also lowers the data risk of resources at the lower levels of the resource hierarchy. For example, reducing the data risk of a table data profile also reduces the data risk of the constituent column data profiles.  
  
## TagCondition

The tag to attach to profiles matching the condition. At most one `TagCondition` can be specified per sensitivity level.

JSON representation  
---  
      
    
    {
      "tag": {
        object ([TagValue](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#TagValue))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "sensitivityScore": {
        object ([SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`tag` |  `object (`[TagValue](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction#TagValue)`)` The tag value to attach to resources.  
The type of condition on which attaching the tag will be predicated. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`sensitivityScore` |  `object (`[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore)`)` Conditions attaching the tag to a resource on its profile having this sensitivity score.  
End of mutually exclusive fields.  
  
## TagValue

A value of a tag.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "namespacedValue": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The format of the tag value. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`namespacedValue` |  `string` The namespaced name for the tag value to attach to resources. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`, for example, "123456/environment/prod" for an organization parent, or "my-project/environment/prod" for a project parent.  
End of mutually exclusive fields.  
  
## ProfileGeneration

Whether a profile being created is the first generation or an update.

Enums  
---  
`PROFILE_GENERATION_UNSPECIFIED` | Unused.  
`PROFILE_GENERATION_NEW` | The profile is the first profile for the resource.  
`PROFILE_GENERATION_UPDATE` | The profile is an update to a previous profile.  
  
## PublishToDataplexCatalog

Create Dataplex Universal Catalog aspects for profiled resources with the aspect type Sensitive Data Protection Profile. To learn more about aspects, see <https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects>.

JSON representation  
---  
      
    
    {
      "lowerDataRiskToLow": boolean
    }  
  
Fields  
---  
`lowerDataRiskToLow` |  `boolean` Whether creating a Dataplex Universal Catalog aspect for a profiled resource should lower the risk of the profile for that resource. This also lowers the data risk of resources at the lower levels of the resource hierarchy. For example, reducing the data risk of a table data profile also reduces the data risk of the constituent column data profiles.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
