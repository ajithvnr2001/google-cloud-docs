---
url: https://docs.cloud.google.com/python/docs/reference/logging/latest/entries/
title: Log Entries \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:25.487601+00:00
---

# Log Entries  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/logging/latest/entries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Log Entries Stay organized with collections  Save and categorize content based on your preferences. 

3.17.0 (latest)  3.16.3  3.15.0  3.13.0  3.12.1  3.11.3  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.1  3.2.5  3.1.2  3.0.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.2  1.15.3  1.14.0  1.13.0  1.12.1 

Log entries within the Google Cloud Logging API.

### _class_ google.cloud.logging_v2.entries.LogEntry(log_name=None, labels=None, insert_id=None, severity=None, http_request=None, timestamp=None, resource=Resource(type='global', labels={}), trace=None, span_id=None, trace_sampled=None, source_location=None, operation=None, logger=None, payload=None)

Bases: `google.cloud.logging_v2.entries.LogEntry`

Log entry.

  * **Parameters**

    * **log_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str)) – The name of the logger used to post the entry.

    * **labels** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Mapping of labels for the entry

    * **insert_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The ID used to identify an entry uniquely.

    * **severity** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The severity of the event being logged.

    * **http_request** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Info about HTTP request associated with the entry.

    * **timestamp** (_Optional_ _[_[_datetime.datetime_](https://docs.python.org/3/library/datetime.html#datetime.datetime) _]_) – Timestamp for the entry.

    * **resource** (_Optional_ _[_[_google.cloud.logging_v2.resource.Resource_](https://docs.cloud.google.com/python/docs/reference/logging/latest/resource#google.cloud.logging_v2.resource.Resource) _]_) – Monitored resource of the entry.

    * **trace** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Trace ID to apply to the entry.

    * **span_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Span ID within the trace for the log entry. Specify the trace parameter if `span_id` is set.

    * **trace_sampled** (_Optional_ _[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool) _]_) – The sampling decision of the trace associated with the log entry.

    * **source_location** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Location in source code from which the entry was emitted.

    * **operation** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Additional information about a potentially long-running operation associated with the log entry.

    * **logger** ([_logging_v2.logger.Logger_](https://docs.cloud.google.com/python/docs/reference/logging/latest/logger#google.cloud.logging_v2.logger.Logger)) – the logger used to write the entry.




See: <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>

Create new instance of LogEntry(log_name, labels, insert_id, severity, http_request, timestamp, resource, trace, span_id, trace_sampled, source_location, operation, logger, payload)

#### _classmethod_ from_api_repr(resource, client, *, loggers=None)

Construct an entry given its API representation

  * **Parameters**

    * **resource** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict)) – text entry resource representation returned from the API

    * **client** ([_Client_](https://docs.cloud.google.com/python/docs/reference/logging/latest/client#google.cloud.logging_v2.client.Client)) – Client which holds credentials and project configuration.

    * **loggers** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – A mapping of logger fullnames -> loggers. If not passed, the entry will have a newly-created logger if possible, or an empty logger field if not.

  * **Returns**

Log entry parsed from `resource`.

  * **Return type**

google.cloud.logging.entries.LogEntry




#### to_api_repr()

API repr (JSON format) for entry.

### _class_ google.cloud.logging_v2.entries.ProtobufEntry(log_name=None, labels=None, insert_id=None, severity=None, http_request=None, timestamp=None, resource=Resource(type='global', labels={}), trace=None, span_id=None, trace_sampled=None, source_location=None, operation=None, logger=None, payload=None)

Bases: `google.cloud.logging_v2.entries.LogEntry`

Log entry with protobuf message payload.

  * **Parameters**

    * **log_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str)) – The name of the logger used to post the entry.

    * **labels** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Mapping of labels for the entry

    * **insert_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The ID used to identify an entry uniquely.

    * **severity** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The severity of the event being logged.

    * **http_request** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Info about HTTP request associated with the entry.

    * **timestamp** (_Optional_ _[_[_datetime.datetime_](https://docs.python.org/3/library/datetime.html#datetime.datetime) _]_) – Timestamp for the entry.

    * **resource** (_Optional_ _[_[_google.cloud.logging_v2.resource.Resource_](https://docs.cloud.google.com/python/docs/reference/logging/latest/resource#google.cloud.logging_v2.resource.Resource) _]_) – Monitored resource of the entry.

    * **trace** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Trace ID to apply to the entry.

    * **span_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Span ID within the trace for the log entry. Specify the trace parameter if `span_id` is set.

    * **trace_sampled** (_Optional_ _[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool) _]_) – The sampling decision of the trace associated with the log entry.

    * **source_location** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Location in source code from which the entry was emitted.

    * **operation** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Additional information about a potentially long-running operation associated with the log entry.

    * **logger** ([_logging_v2.logger.Logger_](https://docs.cloud.google.com/python/docs/reference/logging/latest/logger#google.cloud.logging_v2.logger.Logger)) – the logger used to write the entry.

    * **payload** (_google.protobuf.Message_) – payload for the log entry.




See: <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>

Create new instance of LogEntry(log_name, labels, insert_id, severity, http_request, timestamp, resource, trace, span_id, trace_sampled, source_location, operation, logger, payload)

#### parse_message(message)

Parse payload into a protobuf message.

Mutates the passed-in `message` in place.

  * **Parameters**

**message** (_google.protobuf.Message_) – the message to be logged




#### to_api_repr()

API repr (JSON format) for entry.

### _class_ google.cloud.logging_v2.entries.StructEntry(log_name=None, labels=None, insert_id=None, severity=None, http_request=None, timestamp=None, resource=Resource(type='global', labels={}), trace=None, span_id=None, trace_sampled=None, source_location=None, operation=None, logger=None, payload=None)

Bases: `google.cloud.logging_v2.entries.LogEntry`

Log entry with JSON payload.

  * **Parameters**

    * **log_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str)) – The name of the logger used to post the entry.

    * **labels** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Mapping of labels for the entry

    * **insert_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The ID used to identify an entry uniquely.

    * **severity** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The severity of the event being logged.

    * **http_request** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Info about HTTP request associated with the entry.

    * **timestamp** (_Optional_ _[_[_datetime.datetime_](https://docs.python.org/3/library/datetime.html#datetime.datetime) _]_) – Timestamp for the entry.

    * **resource** (_Optional_ _[_[_google.cloud.logging_v2.resource.Resource_](https://docs.cloud.google.com/python/docs/reference/logging/latest/resource#google.cloud.logging_v2.resource.Resource) _]_) – Monitored resource of the entry.

    * **trace** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Trace ID to apply to the entry.

    * **span_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Span ID within the trace for the log entry. Specify the trace parameter if `span_id` is set.

    * **trace_sampled** (_Optional_ _[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool) _]_) – The sampling decision of the trace associated with the log entry.

    * **source_location** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Location in source code from which the entry was emitted.

    * **operation** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Additional information about a potentially long-running operation associated with the log entry.

    * **logger** ([_logging_v2.logger.Logger_](https://docs.cloud.google.com/python/docs/reference/logging/latest/logger#google.cloud.logging_v2.logger.Logger)) – the logger used to write the entry.

    * **payload** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict)) – payload for the log entry.




See: <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>

Create new instance of LogEntry(log_name, labels, insert_id, severity, http_request, timestamp, resource, trace, span_id, trace_sampled, source_location, operation, logger, payload)

#### to_api_repr()

API repr (JSON format) for entry.

### _class_ google.cloud.logging_v2.entries.TextEntry(log_name=None, labels=None, insert_id=None, severity=None, http_request=None, timestamp=None, resource=Resource(type='global', labels={}), trace=None, span_id=None, trace_sampled=None, source_location=None, operation=None, logger=None, payload=None)

Bases: `google.cloud.logging_v2.entries.LogEntry`

Log entry with text payload.

  * **Parameters**

    * **log_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str)) – The name of the logger used to post the entry.

    * **labels** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Mapping of labels for the entry

    * **insert_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The ID used to identify an entry uniquely.

    * **severity** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – The severity of the event being logged.

    * **http_request** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Info about HTTP request associated with the entry.

    * **timestamp** (_Optional_ _[_[_datetime.datetime_](https://docs.python.org/3/library/datetime.html#datetime.datetime) _]_) – Timestamp for the entry.

    * **resource** (_Optional_ _[_[_google.cloud.logging_v2.resource.Resource_](https://docs.cloud.google.com/python/docs/reference/logging/latest/resource#google.cloud.logging_v2.resource.Resource) _]_) – Monitored resource of the entry.

    * **trace** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Trace ID to apply to the entry.

    * **span_id** (_Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]_) – Span ID within the trace for the log entry. Specify the trace parameter if `span_id` is set.

    * **trace_sampled** (_Optional_ _[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool) _]_) – The sampling decision of the trace associated with the log entry.

    * **source_location** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Location in source code from which the entry was emitted.

    * **operation** (_Optional_ _[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict) _]_) – Additional information about a potentially long-running operation associated with the log entry.

    * **logger** ([_logging_v2.logger.Logger_](https://docs.cloud.google.com/python/docs/reference/logging/latest/logger#google.cloud.logging_v2.logger.Logger)) – the logger used to write the entry.

    * **payload** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str)) – payload for the log entry.




See: <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>

Create new instance of LogEntry(log_name, labels, insert_id, severity, http_request, timestamp, resource, trace, span_id, trace_sampled, source_location, operation, logger, payload)

#### to_api_repr()

API repr (JSON format) for entry.

### google.cloud.logging_v2.entries.logger_name_from_path(path, project=None)

Validate a logger URI path and get the logger name.

  * **Parameters**

    * **path** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str)) – URI path for a logger API request

    * **project** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str)) – The project the path is expected to belong to

  * **Returns**

Logger name parsed from `path`.

  * **Return type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

  * **Raises**

[**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError) – If the `path` is ill-formed of if the project from `path` does not agree with the `project` passed in.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
