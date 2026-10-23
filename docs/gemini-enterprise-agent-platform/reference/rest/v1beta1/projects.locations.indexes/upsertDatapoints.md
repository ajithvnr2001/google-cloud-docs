---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints/
title: Method: indexes.upsertDatapoints \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:24.361824+00:00
---

# Method: indexes.upsertDatapoints  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: indexes.upsertDatapoints Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.indexes.upsertDatapoints

Add/update Datapoints into an Index.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{index}:upsertDatapoints`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`index` `string` Required. The name of the Index resource to be updated. Format: `projects/{project}/locations/{location}/indexes/{index}`

### Request body

The request body contains data with the following structure: | Fields  
  
`datapoints[]` `object (`[IndexDatapoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#IndexDatapoint)`)` A list of datapoints to be created/updated. | `updateMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Update mask is used to specify the fields to be overwritten in the datapoints by the update. The fields specified in the updateMask are relative to each IndexDatapoint inside datapoints, not the full request.Updatable fields:

  * Use `all_restricts` to update both restricts and numericRestricts.

This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.

### Response body

If successful, the response body is empty.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `index` resource:

  * `aiplatform.indexes.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## IndexDatapoint

A datapoint of Index. | Fields  
  
`datapointId` `string` Required. Unique identifier of the datapoint. | `featureVector[]` `number` Required. feature embedding vector for dense index. An array of numbers with the length of [NearestNeighborSearchConfig.dimensions]. | `sparseEmbedding` `object (`[SparseEmbedding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#SparseEmbedding)`)` Optional. feature embedding vector for sparse index. | `restricts[]` `object (`[Restriction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#Restriction)`)` Optional. List of Restrict of the datapoint, used to perform "restricted searches" where boolean rule are used to filter the subset of the database eligible for matching. This uses categorical tokens. See: <https://cloud.google.com/vertex-ai/docs/matching-engine/filtering> | `numericRestricts[]` `object (`[NumericRestriction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#NumericRestriction)`)` Optional. List of Restrict of the datapoint, used to perform "restricted searches" where boolean rule are used to filter the subset of the database eligible for matching. This uses numeric comparisons. | `crowdingTag` `object (`[CrowdingTag](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#CrowdingTag)`)` Optional. CrowdingTag of the datapoint, the number of neighbors to return in each crowding can be configured during query. | `embeddingMetadata` `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The key-value map of additional metadata for the datapoint. | JSON representation  
---  
      
    
    {
      "datapointId": string,
      "featureVector": [
        number
      ],
      "sparseEmbedding": {
        object ([SparseEmbedding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#SparseEmbedding))
      },
      "restricts": [
        {
          object ([Restriction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#Restriction))
        }
      ],
      "numericRestricts": [
        {
          object ([NumericRestriction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#NumericRestriction))
        }
      ],
      "crowdingTag": {
        object ([CrowdingTag](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#CrowdingTag))
      },
      "embeddingMetadata": {
        object
      }
    }  
  
## SparseEmbedding

feature embedding vector for sparse index. An array of numbers whose values are located in the specified dimensions.

Fields  
  
`values[]` `number` Required. The list of embedding values of the sparse vector. | `dimensions[]` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The list of indexes for the embedding values of the sparse vector. | JSON representation  
---  
      
    
    {
      "values": [
        number
      ],
      "dimensions": [
        string
      ]
    }  
  
## Restriction

Restriction of a datapoint which describe its attributes(tokens) from each of several attribute categories(namespaces).

Fields  
  
`namespace` `string` The namespace of this restriction. e.g.: color. | `allowList[]` `string` The attributes to allow in this namespace. e.g.: 'red' | `denyList[]` `string` The attributes to deny in this namespace. e.g.: 'blue' | JSON representation  
---  
      
    
    {
      "namespace": string,
      "allowList": [
        string
      ],
      "denyList": [
        string
      ]
    }  
  
## NumericRestriction

This field allows restricts to be based on numeric comparisons rather than categorical tokens.

Fields  
  
`namespace` `string` The namespace of this restriction. e.g.: cost. | `op` `enum (`[Operator](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#Operator)`)` This MUST be specified for queries and must NOT be specified for datapoints. | `Value` `Union type`  
  
The type of Value must be consistent for all datapoints with a given namespace name. This is verified at runtime. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`valueInt` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents 64 bit integer. | `valueFloat` `number` Represents 32 bit float. | `valueDouble` `number` Represents 64 bit float. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "namespace": string,
      "op": enum ([Operator](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.indexes/upsertDatapoints#Operator)),
    
      // Value
      "valueInt": string,
      "valueFloat": number,
      "valueDouble": number
      // Union type
    }  
  
## Operator

Which comparison operator to use. Should be specified for queries only; specifying this for a datapoint is an error.

Datapoints for which Operator is true relative to the query's value field will be allowlisted.

Enums  
---  
`OPERATOR_UNSPECIFIED` | Default value of the enum.  
`LESS` | Datapoints are eligible iff their value is < the query's.  
`LESS_EQUAL` | Datapoints are eligible iff their value is <= the query's.  
`EQUAL` | Datapoints are eligible iff their value is == the query's.  
`GREATER_EQUAL` | Datapoints are eligible iff their value is >= the query's.  
`GREATER` | Datapoints are eligible iff their value is > the query's.  
`NOT_EQUAL` | Datapoints are eligible iff their value is != the query's.  
  
## CrowdingTag

Crowding tag is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than some value k' of the k neighbors returned have the same value of crowdingAttribute.

Fields  
  
`crowdingAttribute` `string` The attribute value used for crowding. The maximum number of neighbors to return per crowding attribute value (perCrowdingAttributeNumNeighbors) is configured per-query. This field is ignored if perCrowdingAttributeNumNeighbors is larger than the total number of neighbors to return for a given query. | JSON representation  
---  
      
    
    {
      "crowdingAttribute": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
