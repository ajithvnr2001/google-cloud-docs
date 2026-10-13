---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DataAgent
title: Class DataAgent (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:53.100164+00:00
---

# Class DataAgent (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DataAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataAgent (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DataAgent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing a DataAgent object.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`data_analytics_agent` |  `[google.cloud.geminidataanalytics_v1.types.DataAnalyticsAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DataAnalyticsAgent)`   
Data analytics agent. This field is a member of `oneof`_ `type`.   
`name` |  `str`   
Optional. Identifier. The unique resource name of a DataAgent. Format: `projects/{project}/locations/{location}/dataAgents/{data_agent_id}` `{data_agent}` is the resource id and should be 63 characters or less and must match the format described in https://google.aip.dev/122#resource-id-segments Example: `projects/1234567890/locations/global/dataAgents/my-agent`. It is recommended to skip setting this field during agent creation as it will be inferred automatically and overwritten with the {parent}/dataAgents/{data_agent_id}.   
`display_name` |  `str`   
Optional. User friendly display name. \- Must be between 1-256 characters.   
`description` |  `str`   
Optional. Description of the agent. \- Must be between 1-1024 characters.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels to help users filter related agents. For example, "sales", "business", "etl", and so on. Note labels are used only for filtering and not for policies. See the `labels documentation   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the data agent was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the data agent was last updated.   
`delete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] The time the data agent was soft deleted.   
`purge_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp in UTC of when this data agent is considered expired. This is *always* provided on output, regardless of what was sent on input.   
`kms_key` |  `str`   
Optional. Customer managed encryption key (CMEK) to use for encrypting the DataAgent resources. Cloud KMS CryptoKeys must reside in the same location as the DataAgent. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`. This field is a member of `oneof`_ `_kms_key`.   
`bigquery_agent_analytics_enabled` |  `bool`   
Optional. Controls whether BigQuery Agent Analytics trace logging is enabled for the agent. BigQuery Agent Analytics is in Preview and is delivered to enrolled projects only. In a project that is not enrolled this field is accepted and stored, but no trace rows are written and no error is returned. Trace logging is additionally suppressed for the entire turn, without error, when any table in the agent's datasource carries row-level security, column-level security or policy tags. It is also suppressed when that determination cannot be made, for example when the caller lacks permission to list a table's row access policies. Trace rows are written only when this is `true` and `bigquery_agent_analytics_table` is set. On a BigQuery agent, enabling this without a table has no effect: no table is created for the agent and no rows are written. On an agent whose datasource is not BigQuery, `CreateDataAgent` rejects either field with `INVALID_ARGUMENT`. This setting is independent of the project-level BigQuery Agent Analytics setting configured through `SetAgentOpsObservability`. An agent does not inherit that setting. This field is a member of `oneof`_ `_bigquery_agent_analytics_enabled`.   
`bigquery_agent_analytics_table` |  `[google.cloud.geminidataanalytics_v1.types.BigQueryTableReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.BigQueryTableReference)`   
Optional. The BigQuery table that BigQuery Agent Analytics trace rows are written to. Has no effect unless `bigquery_agent_analytics_enabled` is `true`. The Preview enrollment described on that field applies here too. The trace table is validated when it is set on `CreateDataAgent`, or when it is included in the `update_mask` of an `UpdateDataAgent` call. The following are rejected with `INVALID_ARGUMENT`: \- The table must belong to the same project as the agent. \- The agent's datasource must be BigQuery. BigQuery Agent Analytics is not supported for Looker, Looker Studio or AlloyDB agents. These are validated against the agent as sent in the request. An agent that carries no datasource is not validated, and an agent switched to a non-BigQuery datasource is not re-validated; in the latter case no trace rows are written. The destination dataset must already exist and must grant write access to the project's Gemini Data Analytics service agent, whose address is `service-PROJECT_NUMBER@gcp-sa-geminidataanalytics.iam.gserviceaccount.com` (that grant is not performed on your behalf). Without it the agent answers normally and no trace rows are written. Changing the table on an existing agent affects subsequent turns only. Rows already written to the previous table are left in place.   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
