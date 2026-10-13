---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentOrBuilder
title: Interface DataAgentOrBuilder (0.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:32.073133+00:00
---

# Interface DataAgentOrBuilder (0.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataAgentOrBuilder (0.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.0 (latest)  0.23.0  0.22.0  0.21.0  0.19.0  0.16.0  0.15.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataAgentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels to help users filter related agents. For example, "sales", "business", "etl", and so on. Note labels are used only for filtering and not for policies. See the [labels documentation](https://cloud.google.com/resource-manager/docs/labels-overview) for more details on label usage.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBigqueryAgentAnalyticsEnabled()
    
    
    public abstract boolean getBigqueryAgentAnalyticsEnabled()

Optional. Controls whether BigQuery Agent Analytics trace logging is enabled for the agent.

BigQuery Agent Analytics is in Preview and is delivered to enrolled projects only. In a project that is not enrolled this field is accepted and stored, but no trace rows are written and no error is returned.

Trace logging is additionally suppressed for the entire turn, without error, when any table in the agent's datasource carries row-level security, column-level security or policy tags. It is also suppressed when that determination cannot be made, for example when the caller lacks permission to list a table's row access policies.

Trace rows are written only when this is `true` and `bigquery_agent_analytics_table` is set. On a BigQuery agent, enabling this without a table has no effect: no table is created for the agent and no rows are written. On an agent whose datasource is not BigQuery, `CreateDataAgent` rejects either field with `INVALID_ARGUMENT`.

This setting is independent of the project-level BigQuery Agent Analytics setting configured through `SetAgentOpsObservability`. An agent does not inherit that setting.

` optional bool bigquery_agent_analytics_enabled = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bigqueryAgentAnalyticsEnabled.  
  
### getBigqueryAgentAnalyticsTable()
    
    
    public abstract BigQueryTableReference getBigqueryAgentAnalyticsTable()

Optional. The BigQuery table that BigQuery Agent Analytics trace rows are written to. Has no effect unless `bigquery_agent_analytics_enabled` is `true`. The Preview enrollment described on that field applies here too.

The trace table is validated when it is set on `CreateDataAgent`, or when it is included in the `update_mask` of an `UpdateDataAgent` call. The following are rejected with `INVALID_ARGUMENT`:

  * The table must belong to the same project as the agent.
  * The agent's datasource must be BigQuery. BigQuery Agent Analytics is not supported for Looker, Looker Studio or AlloyDB agents.

These are validated against the agent as sent in the request. An agent that carries no datasource is not validated, and an agent switched to a non-BigQuery datasource is not re-validated; in the latter case no trace rows are written.

The destination dataset must already exist and must grant write access to the project's Gemini Data Analytics service agent, whose address is `service-PROJECT_NUMBER@gcp-sa-geminidataanalytics.iam.gserviceaccount.com` (that grant is not performed on your behalf). Without it the agent answers normally and no trace rows are written.

Changing the table on an existing agent affects subsequent turns only. Rows already written to the previous table are left in place.




` .google.cloud.geminidataanalytics.v1.BigQueryTableReference bigquery_agent_analytics_table = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryTableReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.BigQueryTableReference)` | The bigqueryAgentAnalyticsTable.  
  
### getBigqueryAgentAnalyticsTableOrBuilder()
    
    
    public abstract BigQueryTableReferenceOrBuilder getBigqueryAgentAnalyticsTableOrBuilder()

Optional. The BigQuery table that BigQuery Agent Analytics trace rows are written to. Has no effect unless `bigquery_agent_analytics_enabled` is `true`. The Preview enrollment described on that field applies here too.

The trace table is validated when it is set on `CreateDataAgent`, or when it is included in the `update_mask` of an `UpdateDataAgent` call. The following are rejected with `INVALID_ARGUMENT`:

  * The table must belong to the same project as the agent.
  * The agent's datasource must be BigQuery. BigQuery Agent Analytics is not supported for Looker, Looker Studio or AlloyDB agents.

These are validated against the agent as sent in the request. An agent that carries no datasource is not validated, and an agent switched to a non-BigQuery datasource is not re-validated; in the latter case no trace rows are written.

The destination dataset must already exist and must grant write access to the project's Gemini Data Analytics service agent, whose address is `service-PROJECT_NUMBER@gcp-sa-geminidataanalytics.iam.gserviceaccount.com` (that grant is not performed on your behalf). Without it the agent answers normally and no trace rows are written.

Changing the table on an existing agent affects subsequent turns only. Rows already written to the previous table are left in place.




` .google.cloud.geminidataanalytics.v1.BigQueryTableReference bigquery_agent_analytics_table = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryTableReferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.BigQueryTableReferenceOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the data agent was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the data agent was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDataAnalyticsAgent()
    
    
    public abstract DataAnalyticsAgent getDataAnalyticsAgent()

Data analytics agent.

`.google.cloud.geminidataanalytics.v1.DataAnalyticsAgent data_analytics_agent = 101; `

**Returns**  
---  
**Type** | **Description**  
`[DataAnalyticsAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAnalyticsAgent)` | The dataAnalyticsAgent.  
  
### getDataAnalyticsAgentOrBuilder()
    
    
    public abstract DataAnalyticsAgentOrBuilder getDataAnalyticsAgentOrBuilder()

Data analytics agent.

`.google.cloud.geminidataanalytics.v1.DataAnalyticsAgent data_analytics_agent = 101; `

**Returns**  
---  
**Type** | **Description**  
`[DataAnalyticsAgentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAnalyticsAgentOrBuilder)` |   
  
### getDeleteTime()
    
    
    public abstract Timestamp getDeleteTime()

Output only. [Output only] The time the data agent was soft deleted.

`.google.protobuf.Timestamp delete_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The deleteTime.  
  
### getDeleteTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getDeleteTimeOrBuilder()

Output only. [Output only] The time the data agent was soft deleted.

`.google.protobuf.Timestamp delete_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description of the agent.

  * Must be between 1-1024 characters.



`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description of the agent.

  * Must be between 1-1024 characters.



`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. User friendly display name.

  * Must be between 1-256 characters.



`string display_name = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. User friendly display name.

  * Must be between 1-256 characters.



`string display_name = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getKmsKey()
    
    
    public abstract String getKmsKey()

Optional. Customer managed encryption key (CMEK) to use for encrypting the DataAgent resources. Cloud KMS CryptoKeys must reside in the same location as the DataAgent. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`.

` optional string kms_key = 14 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKey.  
  
### getKmsKeyBytes()
    
    
    public abstract ByteString getKmsKeyBytes()

Optional. Customer managed encryption key (CMEK) to use for encrypting the DataAgent resources. Cloud KMS CryptoKeys must reside in the same location as the DataAgent. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`.

` optional string kms_key = 14 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKey.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentOrBuilder#com_google_cloud_geminidataanalytics_v1_DataAgentOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels to help users filter related agents. For example, "sales", "business", "etl", and so on. Note labels are used only for filtering and not for policies. See the [labels documentation](https://cloud.google.com/resource-manager/docs/labels-overview) for more details on label usage.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels to help users filter related agents. For example, "sales", "business", "etl", and so on. Note labels are used only for filtering and not for policies. See the [labels documentation](https://cloud.google.com/resource-manager/docs/labels-overview) for more details on label usage.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels to help users filter related agents. For example, "sales", "business", "etl", and so on. Note labels are used only for filtering and not for policies. See the [labels documentation](https://cloud.google.com/resource-manager/docs/labels-overview) for more details on label usage.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. Labels to help users filter related agents. For example, "sales", "business", "etl", and so on. Note labels are used only for filtering and not for policies. See the [labels documentation](https://cloud.google.com/resource-manager/docs/labels-overview) for more details on label usage.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Optional. Identifier. The unique resource name of a DataAgent. Format: `projects/{project}/locations/{location}/dataAgents/{data_agent_id}` `{data_agent}` is the resource id and should be 63 characters or less and must match the format described in <https://google.aip.dev/122#resource-id-segments>

Example: `projects/1234567890/locations/global/dataAgents/my-agent`.

It is recommended to skip setting this field during agent creation as it will be inferred automatically and overwritten with the {parent}/dataAgents/{data_agent_id}.

` string name = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Optional. Identifier. The unique resource name of a DataAgent. Format: `projects/{project}/locations/{location}/dataAgents/{data_agent_id}` `{data_agent}` is the resource id and should be 63 characters or less and must match the format described in <https://google.aip.dev/122#resource-id-segments>

Example: `projects/1234567890/locations/global/dataAgents/my-agent`.

It is recommended to skip setting this field during agent creation as it will be inferred automatically and overwritten with the {parent}/dataAgents/{data_agent_id}.

` string name = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPurgeTime()
    
    
    public abstract Timestamp getPurgeTime()

Output only. Timestamp in UTC of when this data agent is considered expired. This is _always_ provided on output, regardless of what was sent on input.

`.google.protobuf.Timestamp purge_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The purgeTime.  
  
### getPurgeTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getPurgeTimeOrBuilder()

Output only. Timestamp in UTC of when this data agent is considered expired. This is _always_ provided on output, regardless of what was sent on input.

`.google.protobuf.Timestamp purge_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getTypeCase()
    
    
    public abstract DataAgent.TypeCase getTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[DataAgent.TypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgent.TypeCase)` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time when the data agent was last updated.

`.google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time when the data agent was last updated.

`.google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasBigqueryAgentAnalyticsEnabled()
    
    
    public abstract boolean hasBigqueryAgentAnalyticsEnabled()

Optional. Controls whether BigQuery Agent Analytics trace logging is enabled for the agent.

BigQuery Agent Analytics is in Preview and is delivered to enrolled projects only. In a project that is not enrolled this field is accepted and stored, but no trace rows are written and no error is returned.

Trace logging is additionally suppressed for the entire turn, without error, when any table in the agent's datasource carries row-level security, column-level security or policy tags. It is also suppressed when that determination cannot be made, for example when the caller lacks permission to list a table's row access policies.

Trace rows are written only when this is `true` and `bigquery_agent_analytics_table` is set. On a BigQuery agent, enabling this without a table has no effect: no table is created for the agent and no rows are written. On an agent whose datasource is not BigQuery, `CreateDataAgent` rejects either field with `INVALID_ARGUMENT`.

This setting is independent of the project-level BigQuery Agent Analytics setting configured through `SetAgentOpsObservability`. An agent does not inherit that setting.

` optional bool bigquery_agent_analytics_enabled = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryAgentAnalyticsEnabled field is set.  
  
### hasBigqueryAgentAnalyticsTable()
    
    
    public abstract boolean hasBigqueryAgentAnalyticsTable()

Optional. The BigQuery table that BigQuery Agent Analytics trace rows are written to. Has no effect unless `bigquery_agent_analytics_enabled` is `true`. The Preview enrollment described on that field applies here too.

The trace table is validated when it is set on `CreateDataAgent`, or when it is included in the `update_mask` of an `UpdateDataAgent` call. The following are rejected with `INVALID_ARGUMENT`:

  * The table must belong to the same project as the agent.
  * The agent's datasource must be BigQuery. BigQuery Agent Analytics is not supported for Looker, Looker Studio or AlloyDB agents.

These are validated against the agent as sent in the request. An agent that carries no datasource is not validated, and an agent switched to a non-BigQuery datasource is not re-validated; in the latter case no trace rows are written.

The destination dataset must already exist and must grant write access to the project's Gemini Data Analytics service agent, whose address is `service-PROJECT_NUMBER@gcp-sa-geminidataanalytics.iam.gserviceaccount.com` (that grant is not performed on your behalf). Without it the agent answers normally and no trace rows are written.

Changing the table on an existing agent affects subsequent turns only. Rows already written to the previous table are left in place.




` .google.cloud.geminidataanalytics.v1.BigQueryTableReference bigquery_agent_analytics_table = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryAgentAnalyticsTable field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the data agent was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDataAnalyticsAgent()
    
    
    public abstract boolean hasDataAnalyticsAgent()

Data analytics agent.

`.google.cloud.geminidataanalytics.v1.DataAnalyticsAgent data_analytics_agent = 101; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataAnalyticsAgent field is set.  
  
### hasDeleteTime()
    
    
    public abstract boolean hasDeleteTime()

Output only. [Output only] The time the data agent was soft deleted.

`.google.protobuf.Timestamp delete_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleteTime field is set.  
  
### hasKmsKey()
    
    
    public abstract boolean hasKmsKey()

Optional. Customer managed encryption key (CMEK) to use for encrypting the DataAgent resources. Cloud KMS CryptoKeys must reside in the same location as the DataAgent. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`.

` optional string kms_key = 14 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kmsKey field is set.  
  
### hasPurgeTime()
    
    
    public abstract boolean hasPurgeTime()

Output only. Timestamp in UTC of when this data agent is considered expired. This is _always_ provided on output, regardless of what was sent on input.

`.google.protobuf.Timestamp purge_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the purgeTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time when the data agent was last updated.

`.google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
