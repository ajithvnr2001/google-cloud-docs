---
url: https://docs.cloud.google.com/bigtable/docs/audit-log-fields/
title: Data Access audit log fields \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:56.806205+00:00
---

# Data Access audit log fields  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/audit-log-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Access audit log fields

The following table lists Bigtable Data API message fields and indicates whether or not they are logged as part of Data Access audit logging. `AUDITED` means the field is included in the audit log entry, `AUDIT_SIZE` means that the size of the repeated field is used to set the number of response items during audit logging, and `Not Audited` means the field is not audited.

  1. Displayed in [Base 64](https://en.wikipedia.org/wiki/Base64). 
  2. Custom audit field added dynamically during audit logging. 

  
---  
**Message** | **Field** | **Logging Status**  
[Cell](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#cell) | timestamp_micros | Not audited  
value | Not audited  
labels[ ] | Not audited  
[CheckAndMutateRowRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#checkandmutaterowrequest) | table_name | **AUDITED**  
app_profile_id | **AUDITED**  
row_key1 | **AUDITED**  
predicate_filter | **AUDITED**  
true_mutations[ ] | **AUDITED**  
false_mutations[ ] | **AUDITED**  
[CheckAndMutateRowResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#checkandmutaterowresponse) | predicate_matched | **AUDITED**  
[Column](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#column) | qualifier | Not audited  
cells[ ] | Not audited  
[ColumnRange](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#columnrange) | family_name | **AUDITED**  
start_qualifier_closed | **AUDITED**  
start_qualifier_open | **AUDITED**  
end_qualifier_closed | **AUDITED**  
end_qualifier_open | **AUDITED**  
[Family](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#family) | name | Not audited  
columns[ ] | Not audited  
[MutateRowRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#mutaterowrequest) | table_name | **AUDITED**  
app_profile_id | **AUDITED**  
row_key1 | **AUDITED**  
mutations[ ] | **AUDITED**  
[MutateRowResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#mutaterowresponse) |  | Not audited  
[MutateRowsRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#mutaterowsrequest) | table_name | **AUDITED**  
app_profile_id | **AUDITED**  
entries[ ] | **AUDITED**  
[Entry](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#entry)   
(A mutation for a given row.) | row_key1 | **AUDITED**  
mutations[ ] | **AUDITED**  
[MutateRowsResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#mutaterowsresponse) | entries[ ] | **AUDITED**  
[Entry](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#entry_1)   
(The result of applying a passed mutation in the original request.) | index | **AUDITED**  
status | **AUDITED**  
[Mutation](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#mutation) | set_cell | **AUDITED**  
delete_from_column | **AUDITED**  
delete_from_family | **AUDITED**  
delete_from_row | **AUDITED**  
[DeleteFromColumn](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#deletefromcolumn) | family_name | **AUDITED**  
column_qualifier | Not audited  
time_range | Not audited  
[DeleteFromFamily](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#deletefromfamily) | family_name | **AUDITED**  
[DeleteFromRow](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#deletefromrow) |  | Not audited  
[SetCell](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#setcell) | family_name | **AUDITED**  
column_qualifier | Not audited  
timestamp_micros | Not audited  
value | Not audited  
[ReadModifyWriteRowRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#readmodifywriterowrequest) | table_name | **AUDITED**  
app_profile_id | **AUDITED**  
row_key1 | **AUDITED**  
rules[ ] | **AUDITED**  
[ReadModifyWriteRowResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#readmodifywriterowresponse) | row | Not audited  
[ReadModifyWriteRule](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#readmodifywriterule) | family_name | **AUDITED**  
column_qualifier | Not audited  
append_value | Not audited  
increment_amount | Not audited  
[ReadRowsRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#readrowsrequest) | table_name | **AUDITED**  
app_profile_id | **AUDITED**  
rows | **AUDITED**  
filter | **AUDITED**  
rows_limit | **AUDITED**  
[ReadRowsResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#readrowsresponse) | chunks[ ] | **AUDIT_SIZE**  
last_scanned_row_key1 | Not audited  
response_stream_bytes2 | **AUDITED**  
[CellChunk](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#cellchunk) | row_key1 | Not audited  
family_name | Not audited  
qualifier | Not audited  
timestamp_micros | Not audited  
labels[ ] | Not audited  
value | Not audited  
value_size | Not audited  
reset_row | Not audited  
commit_row | Not audited  
[Row](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#row) | key | Not audited  
families[ ] | Not audited  
[RowFilter](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#rowfilter) | chain | **AUDITED**  
interleave | **AUDITED**  
condition | **AUDITED**  
sink | **AUDITED**  
pass_all_filter | **AUDITED**  
block_all_filter | **AUDITED**  
row_key_regex_filter | **AUDITED**  
row_sample_filter | **AUDITED**  
family_name_regex_filter | **AUDITED**  
column_qualifier_regex_filter | **AUDITED**  
column_range_filter | **AUDITED**  
timestamp_range_filter | **AUDITED**  
value_regex_filter | **AUDITED**  
value_range_filter | **AUDITED**  
cells_per_row_offset_filter | **AUDITED**  
cells_per_row_limit_filter | **AUDITED**  
cells_per_column_limit_filter | **AUDITED**  
strip_value_transformer | **AUDITED**  
apply_label_transformer | **AUDITED**  
[Chain](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#chain) | filters[ ] | **AUDITED**  
[Condition](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#condition) | predicate_filter | **AUDITED**  
true_filter | **AUDITED**  
false_filter | **AUDITED**  
[Interleave](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#interleave) | filters[ ] | **AUDITED**  
[RowRange](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#rowrange) | start_key_closed | **AUDITED**  
start_key_open | **AUDITED**  
end_key_open | **AUDITED**  
end_key_closed | **AUDITED**  
[RowSet](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#rowset) | row_keys[ ] | **AUDITED**  
row_ranges[ ] | **AUDITED**  
[SampleRowKeysRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#samplerowkeysrequest) | table_name | **AUDITED**  
app_profile_id | **AUDITED**  
[SampleRowKeysResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#samplerowkeysresponse) | row_key1 | Not audited  
offset_bytes | Not audited  
response_stream_bytes2 | **AUDITED**  
[TimestampRange](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#timestamprange) | start_timestamp_micros | **AUDITED**  
end_timestamp_micros | **AUDITED**  
[ValueRange](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#valuerange) | start_value_closed | Not audited  
start_value_open | Not audited  
end_value_closed | Not audited  
end_value_open | Not audited  
  
## What's next

  * [Learn more about Bigtable audit logging.](https://docs.cloud.google.com/bigtable/docs/audit-logging)
  * [View an example of Bigtable Data Access audit log.](https://docs.cloud.google.com/bigtable/docs/audit-log-example)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
