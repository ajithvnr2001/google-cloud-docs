---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-smp-io-module/
title: TIPCommon.smp_io \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:55:23.362620+00:00
---

# TIPCommon.smp_io  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-smp-io-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.smp_io

The **TIPCommon.smp_io** module provides a standardized interface for managing stateful data within connectors. It facilitates the reading and writing of alert IDs and general content to persistent storage, supporting both file-based and database-backed data streams to ensure consistency across connector executions.

## State management

These functions are primarily used by connectors to track processed alerts and maintain execution state. They handle the complexity of JSON serialization, default value assignment, and data repair to prevent regressions.

The following table provides the technical specifications for each I/O utility, organized for quick parameter reference:

Function | Parameters | Description & Returns  
---|---|---  
`read_and_repair_existing_ids()` | 

  * `siemplify`: (SiemplifyConnectorExecution) SDK instance.
  * `default_value_to_return`: (Any) Fallback if new. Defaults to `[]`.
  * `identifier`: (str) Connector identifier.
  * `ids_file_name`: (str) Defaults to `ids.json`.
  * `db_key`: (str) Defaults to `ids`.

| Returns: `list` Reads existing alert IDs and automatically converts them from a dictionary to a list format to avoid legacy regressions.  
`read_content()` | 

  * `siemplify`: (SiemplifyConnectorExecution) SDK instance.
  * `file_name`: (str) File to validate.
  * `db_key`: (str) DB key to validate.
  * `default_value_to_return`: (Any) Fallback if new. Defaults to `{}`.
  * `identifier`: (str) Connector identifier.

| Returns: `dict` Retrieves the general content of a `ConnectorStream` object. Content is automatically parsed using `json.loads` before returning.  
`read_ids()` | 

  * `siemplify`: (SiemplifyConnectorExecution) SDK instance.
  * `default_value_to_return`: (Any) Fallback if new. Defaults to `[]`.
  * `identifier`: (str) Connector identifier.
  * `ids_file_name`: (str) Defaults to `ids.json`.
  * `db_key`: (str) Defaults to `ids`.

| Returns: `list` Reads a list of processed IDs from the state storage. Content is parsed using `json.loads` before returning.  
`read_ids_by_timestamp()` | 

  * `siemplify`: (SiemplifyConnectorExecution) SDK instance.
  * `offset_in_hours`: (int) Time limit. Defaults to `72`.
  * `convert_to_milliseconds`: (bool) Seconds to ms conversion.
  * `cast_keys_to_integers`: (bool) Cast dictionary keys.
  * `offset_is_in_days`: (bool) Toggle for day-based offsets.

| Returns: `list` Retrieves IDs falling within a specific time window, typically used for lookback verification of recently seen alerts.  
`write_content()` | 

  * `siemplify`: (SiemplifyConnectorExecution) SDK instance.
  * `content_to_write`: (dict|list|str) Data to persist.
  * `file_name`: (str) Target filename.
  * `db_key`: (str) Target DB key.
  * `default_value_to_set`: (Any) Initial value for new streams.

| Returns: `None` Persists arbitrary content into a `ConnectorStream` for cross-execution state management.  
`write_ids()` | 

  * `siemplify`: (SiemplifyConnectorExecution) SDK instance.
  * `ids`: (list|str) IDs to persist.
  * `stored_ids_limit`: (int) Max IDs to keep. Defaults to `1,000`.
  * `ids_file_name`: (str) Target filename.
  * `db_key`: (str) Target DB key.

| Returns: `None` Saves a list of IDs while enforcing a limit to prevent the state file from growing indefinitely.  
`write_ids_with_timestamp()` | 

  * `siemplify`: (SiemplifyConnectorExecution) SDK instance.
  * `ids`: (dict|list|str) IDs and timestamps to write.
  * `ids_file_name`: (str) Target filename.
  * `db_key`: (str) Target DB key.

| Returns: `None` Saves IDs along with associated timestamps, enabling time-aware retrieval for lookback logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
