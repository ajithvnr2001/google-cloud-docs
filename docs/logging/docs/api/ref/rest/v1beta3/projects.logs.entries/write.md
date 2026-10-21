---
url: https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write/
title: Method projects.logs.entries.write \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:56:37.296122+00:00
---

# Method projects.logs.entries.write  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)



Send feedback 

#  Method projects.logs.entries.write Stay organized with collections  Save and categorize content based on your preferences. 

**v1 Deprecation**

The Stackdriver Logging API v1 has been deprecated. You must migrate your code to the [v2 API](https://docs.cloud.google.com/logging/docs/api/v2).

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization
  * LogEntry
    * JSON representation
  * LogEntryMetadata
    * JSON representation
  * LogSeverity
  * HttpRequest
    * JSON representation
  * LogEntryOperation
    * JSON representation
  * Try it!



Writes log entries to Stackdriver Logging. Each entry consists of a `LogEntry` object. You must fill in the required fields of the object. You can supply a map, `commonLabels`, that holds default (key, value) data for the `entries[].metadata.labels` map in each entry, saving you the trouble of creating identical copies for each entry.

### HTTP request

`POST https://logging.googleapis.com/v1beta3/{logName=projects/*/logs/*}/entries:write`

(This URI uses [URI Template](https://datatracker.ietf.org/doc/html/rfc6570) syntax.)

### Path parameters

Parameter name | Type | Description  
---|---|---  
`logName` | `string` | The resource name of the log that will receive the log entries.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "commonLabels": {
        string: string,
        ...
      },
      "entries": [
        {
          object([LogEntry](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogEntry))
        }
      ],
      "partialSuccess": boolean,
    }  
  
Field name | Type | Description  
---|---|---  
`commonLabels` | `map (key: string, value: string)` | Metadata labels that apply to all log entries in this request, so that you don't have to repeat them in each log entry's `metadata.labels` field. If any of the log entries contains a (key, value) with the same key that is in `commonLabels`, then the entry's (key, value) overrides the one in `commonLabels`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`entries[]` | `object(`[LogEntry](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogEntry)`)` | Log entries to write.  
`partialSuccess` | `boolean` | Optional. Whether valid entries should be written even if some other entries fail due to INVALID_ARGUMENT or PERMISSION_DENIED errors. If any entry is not written, the response status will be the error associated with one of the failed entries and include error details in the form of WriteLogEntriesPartialErrors.  
  
### Response body

If successful, the response body will be empty.

### Authorization

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/logging.write`
  * ` https://www.googleapis.com/auth/logging.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Auth Guide](https://docs.cloud.google.com/docs/authentication).

## LogEntry

An individual entry in a log.

JSON representation  
---  
      
    
    {
      "metadata": {
        object([LogEntryMetadata](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogEntryMetadata))
      },
      "insertId": string,
      "log": string,
      "httpRequest": {
        object([HttpRequest](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#HttpRequest))
      },
      "operation": {
        object([LogEntryOperation](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogEntryOperation))
      },
      // Union field, only one of the following:
      "protoPayload": {
        "@type": string,
        field1: ...,
        ...
      },
      "textPayload": string,
      "structPayload": {
        object
      },
    }  
  
Field name | Type | Description  
---|---|---  
`metadata` | `object(`[LogEntryMetadata](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogEntryMetadata)`)` | Required. Information about the log entry.  
`insertId` | `string` | A unique ID for the log entry. If you provide this field, the logging service considers other log entries in the same log with the same ID as duplicates which can be removed. If omitted, Stackdriver Logging will generate a unique ID for this log entry.  
`log` | `string` | The log to which this entry belongs. When a log entry is written, the value of this field is set by the logging system.  
`httpRequest` | `object(`[HttpRequest](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#HttpRequest)`)` | Information about the HTTP request associated with this log entry, if applicable.  
`operation` | `object(`[LogEntryOperation](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogEntryOperation)`)` | Optional. Information about an operation associated with the log entry, if applicable.  
Union field, only one of the following:  
`protoPayload` | `object` | The log entry payload, represented as a protocol buffer that is expressed as a JSON object. You can only pass `protoPayload` values that belong to a set of approved types.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`textPayload` | `string` | The log entry payload, represented as a Unicode string (UTF-8).  
`structPayload` | `object` | The log entry payload, represented as a structure that is expressed as a JSON object.  
  
## LogEntryMetadata

Additional data that is associated with a log entry, set by the service creating the log entry.

JSON representation  
---  
      
    
    {
      "timestamp": string,
      "severity": enum([LogSeverity](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogSeverity)),
      "projectId": string,
      "serviceName": string,
      "region": string,
      "zone": string,
      "userId": string,
      "labels": {
        string: string,
        ...
      },
    }  
  
Field name | Type | Description  
---|---|---  
`timestamp` | `string` | The time the event described by the log entry occurred. Timestamps must be later than January 1, 1970. If omitted, Stackdriver Logging will use the time the log entry is received.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`severity` | `enum(`[LogSeverity](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogSeverity)`)` | The severity of the log entry. If omitted, `LogSeverity.DEFAULT` is used.  
`projectId` | `string` | The project ID of the Google Cloud Platform service that created the log entry.  
`serviceName` | `string` | Required. The API name of the Google Cloud Platform service that created the log entry. For example, `"compute.googleapis.com"`.  
`region` | `string` | The region name of the Google Cloud Platform service that created the log entry. For example, `"us-central1"`.  
`zone` | `string` | The zone of the Google Cloud Platform service that created the log entry. For example, `"us-central1-a"`.  
`userId` | `string` | The fully-qualified email address of the authenticated user that performed or requested the action represented by the log entry. If the log entry does not apply to an action taken by an authenticated user, then the field should be empty.  
`labels` | `map (key: string, value: string)` | A set of (key, value) data that provides additional information about the log entry. If the log entry is from one of the Google Cloud Platform sources listed below, the indicated (key, value) information must be provided:Google App Engine, service_name `appengine.googleapis.com`:
    
    
      "appengine.googleapis.com/module_id", <module ID>
      "appengine.googleapis.com/version_id", <version ID>
          and one of:
      "appengine.googleapis.com/replica_index", <instance index>
      "appengine.googleapis.com/clone_id", <instance ID>
    
    or else provide the following Compute Engine labels:
    

Google Compute Engine, service_name `compute.googleapis.com`:
    
    
       "compute.googleapis.com/resource_type", "instance"
       "compute.googleapis.com/resource_id", <instance ID>
    

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## LogSeverity

The severity of the event described in a log entry. These guideline severity levels are ordered, with numerically smaller levels treated as less severe than numerically larger levels. If the source of the log entries uses a different set of severity levels, the client should select the closest corresponding `LogSeverity` value. For example, Java's FINE, FINER, and FINEST levels might all map to `LogSeverity.DEBUG`. If the original severity code must be preserved, it can be stored in the payload.

Enum value | Description  
---|---  
`DEFAULT` | The log entry has no assigned severity level.  
`DEBUG` | Debug or trace information.  
`INFO` | Routine information, such as ongoing status or performance.  
`NOTICE` | Normal but significant events, such as start up, shut down, or configuration.  
`WARNING` | Warning events might cause problems.  
`ERROR` | Error events are likely to cause problems.  
`CRITICAL` | Critical events cause more severe problems or brief outages.  
`ALERT` | A person must take an action immediately.  
`EMERGENCY` | One or more systems are unusable.  
  
## HttpRequest

A common proto for logging HTTP requests.

JSON representation  
---  
      
    
    {
      "requestMethod": string,
      "requestUrl": string,
      "requestSize": string,
      "status": number,
      "responseSize": string,
      "userAgent": string,
      "remoteIp": string,
      "serverIp": string,
      "referer": string,
      "cacheLookup": boolean,
      "cacheHit": boolean,
      "cacheValidatedWithOriginServer": boolean,
      "cacheFillBytes": string,
    }  
  
Field name | Type | Description  
---|---|---  
`requestMethod` | `string` | The request method. Examples: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`.  
`requestUrl` | `string` | The scheme (http, https), the host name, the path and the query portion of the URL that was requested. Example: `"http://example.com/some/info?color=red"`.  
`requestSize` | `string` | The size of the HTTP request message in bytes, including the request headers and the request body.  
`status` | `number` | The response code indicating the status of response. Examples: 200, 404.  
`responseSize` | `string` | The size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body.  
`userAgent` | `string` | The user agent sent by the client. Example: `"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)"`.  
`remoteIp` | `string` | The IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: `"192.168.1.1"`, `"FE80::0202:B3FF:FE1E:8329"`.  
`serverIp` | `string` | The IP address (IPv4 or IPv6) of the origin server that the request was sent to.  
`referer` | `string` | The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).  
`cacheLookup` | `boolean` | Whether or not a cache lookup was attempted.  
`cacheHit` | `boolean` | Whether or not an entity was served from cache (with or without validation).  
`cacheValidatedWithOriginServer` | `boolean` | Whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if `cache_hit` is True.  
`cacheFillBytes` | `string` | The number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted.  
  
## LogEntryOperation

Additional information about a potentially long running operation with which a log entry is associated.

JSON representation  
---  
      
    
    {
      "id": string,
      "producer": string,
      "first": boolean,
      "last": boolean,
    }  
  
Field name | Type | Description  
---|---|---  
`id` | `string` | An opaque identifier. A producer of log entries should ensure that `id` is only reused for entries related to one operation.  
`producer` | `string` | Ensures the operation can be uniquely identified. The combination of `id` and `producer` should be made globally unique by filling `producer` with a value that disambiguates the service that created `id`.  
`first` | `boolean` | True for the first entry associated with `id`.  
`last` | `boolean` | True for the last entry associated with `id`.  
  
## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
