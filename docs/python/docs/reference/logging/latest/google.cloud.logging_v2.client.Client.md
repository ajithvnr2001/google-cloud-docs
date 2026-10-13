---
url: https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client
title: Class Client (3.17.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:18.644536+00:00
---

# Class Client (3.17.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Client (3.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.17.0 (latest)  3.16.3  3.15.0  3.13.0  3.12.1  3.11.3  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.1  3.2.5  3.1.2  3.0.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.2  1.15.3  1.14.0  1.13.0  1.12.1 
    
    
    Client(
        *,
        project=None,
        credentials=None,
        _http=None,
        _use_grpc=None,
        client_info=None,
        client_options=None
    )

Client to bundle configuration needed for API requests.

## Properties 

### logging_api

Helper for logging-related API calls.

See <https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries> <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.logs>

### metrics_api

Helper for log metric-related API calls.

See <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics>

### sinks_api

Helper for log sink-related API calls.

See <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks>

## Methods 

### Client
    
    
    Client(
        *,
        project=None,
        credentials=None,
        _http=None,
        _use_grpc=None,
        client_info=None,
        client_options=None
    )

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
the project which the client acts on behalf of. If not passed, falls back to the default inferred from the environment.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
Thehe OAuth2 Credentials to use for this client. If not passed (and if no `_http` object is passed), falls back to the default inferred from the environment.  
`_http` |  `Optional[requests.Session]`   
HTTP object to make requests. Can be any object that defines `request()` with the same interface as `requests.Session.request`. If not passed, an `_http` object is created that is bound to the `credentials` for the current object. This parameter should be considered private, and could change in the future.  
`_use_grpc` |  `Optional[bool]`   
Explicitly specifies whether to use the gRPC transport or HTTP. If unset, falls back to the `GOOGLE_CLOUD_DISABLE_GRPC` environment variable This parameter should be considered private, and could change in the future.  
`client_info` |  `Optional[Union[google.api_core.client_info.ClientInfo, google.api_core.gapic_v1.client_info.ClientInfo]]`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own library or partner tool.  
`client_options` |  `Optional[Union[dict, google.api_core.client_options.ClientOptions]]`   
Client options used to set user options on the client. API Endpoint should be set through client_options.  
  
### close
    
    
    close()

Closes the Client and all handlers associated with this Client.

### flush_handlers
    
    
    flush_handlers()

Flushes all Python log handlers associated with this Client.

### get_default_handler
    
    
    get_default_handler(**kw)

Return the default logging handler based on the local environment.

**Parameter**  
---  
**Name** | **Description**  
`kw` |  `dict`   
keyword args passed to handler constructor  
**Returns**  
---  
**Type** | **Description**  
`logging.Handler` | The default log handler based on the environment  
  
### list_entries
    
    
    list_entries(
        *,
        resource_names=None,
        filter_=None,
        order_by=None,
        max_results=None,
        page_size=None,
        page_token=None
    )

Return a generator of log entry resources.

**Parameters**  
---  
**Name** | **Description**  
`resource_names` |  `Sequence[str]`   
Names of one or more parent resources from which to retrieve log entries: :: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" If not passed, defaults to the project bound to the API's client.  
`filter_` |  `str`   
a filter expression. See <https://cloud.google.com/logging/docs/view/advanced_filters>  
`order_by` |  `str`   
or :data:`logging_v2.DESCENDING`.  
`max_results` |  `Optional[int]`   
Optional. The maximum number of entries to return. Non-positive values are treated as 0. If None, uses API defaults.  
`page_size` |  `int`   
number of entries to fetch in each API call. Although requests are paged internally, logs are returned by the generator one at a time. If not passed, defaults to a value set by the API.  
`page_token` |  `str`   
opaque marker for the starting "page" of entries. If not passed, the API will return the first page of entries.  
  
### list_metrics
    
    
    list_metrics(*, max_results=None, page_size=None, page_token=None)

List metrics for the project associated with this client.

See <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/list>

**Parameters**  
---  
**Name** | **Description**  
`max_results` |  `Optional[int]`   
Optional. The maximum number of entries to return. Non-positive values are treated as 0. If None, uses API defaults.  
`page_size` |  `int`   
number of entries to fetch in each API call. Although requests are paged internally, logs are returned by the generator one at a time. If not passed, defaults to a value set by the API.  
`page_token` |  `str`   
opaque marker for the starting "page" of entries. If not passed, the API will return the first page of entries.  
  
### list_sinks
    
    
    list_sinks(*, parent=None, max_results=None, page_size=None, page_token=None)

List sinks for the a parent resource.

See <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/list>

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `Optional[str]`   
The parent resource whose sinks are to be listed: :: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]". If not passed, defaults to the project bound to the API's client.  
`max_results` |  `Optional[int]`   
Optional. The maximum number of entries to return. Non-positive values are treated as 0. If None, uses API defaults.  
`page_size` |  `int`   
number of entries to fetch in each API call. Although requests are paged internally, logs are returned by the generator one at a time. If not passed, defaults to a value set by the API.  
`page_token` |  `str`   
opaque marker for the starting "page" of entries. If not passed, the API will return the first page of entries.  
  
### logger
    
    
    logger(name, *, labels=None, resource=None)

Creates a logger bound to the current client.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
The name of the logger to be constructed.  
`resource` |  `Optional[`logging_v2.Resource`]`   
a monitored resource object representing the resource the code was run on. If not given, will be inferred from the environment.  
`labels` |  `Optional[dict]`   
Mapping of default labels for entries written via this logger.  
**Returns**  
---  
**Type** | **Description**  
``logging_v2.logger.Logger`` | Logger created with the current client.  
  
### metric
    
    
    metric(name, *, filter_=None, description="")

Creates a metric bound to the current client.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
The name of the metric to be constructed.  
`filter_` |  `Optional[str]`   
The advanced logs filter expression defining the entries tracked by the metric. If not passed, the instance should already exist, to be refreshed via `Metric.reload`.  
`description` |  `Optional[str]`   
The description of the metric to be constructed. If not passed, the instance should already exist, to be refreshed via `Metric.reload`.  
**Returns**  
---  
**Type** | **Description**  
``logging_v2.metric.Metric`` | Metric created with the current client.  
  
### setup_logging
    
    
    setup_logging(
        *, log_level=20, excluded_loggers=("google.api_core.bidi", "werkzeug"), **kw
    )

Attach default Cloud Logging handler to the root logger.

This method uses the default log handler, obtained by `get_default_handler`, and attaches it to the root Python logger, so that a call such as `logging.warn`, as well as all child loggers, will report to Cloud Logging.

**Parameters**  
---  
**Name** | **Description**  
`log_level` |  `Optional[int]`   
The logging level threshold of the attached logger, as set by the `logging.Logger.setLevel` method. Defaults to :const:`logging.INFO`.  
`excluded_loggers` |  `Optional[Tuple[str]]`   
The loggers to not attach the handler to. This will always include the loggers in the path of the logging client itself.  
**Returns**  
---  
**Type** | **Description**  
`dict` | keyword args passed to handler constructor  
  
### sink
    
    
    sink(name, *, filter_=None, destination=None)

Creates a sink bound to the current client.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
the name of the sink to be constructed.  
`filter_` |  `Optional[str]`   
the advanced logs filter expression defining the entries exported by the sink. If not passed, the instance should already exist, to be refreshed via `Sink.reload`.  
`destination` |  `str`   
destination URI for the entries exported by the sink. If not passed, the instance should already exist, to be refreshed via `Sink.reload`.  
**Returns**  
---  
**Type** | **Description**  
``logging_v2.sink.Sink`` | Sink created with the current client.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
