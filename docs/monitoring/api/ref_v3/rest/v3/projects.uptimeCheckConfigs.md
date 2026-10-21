---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs
title: REST Resource: projects.uptimeCheckConfigs \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:15.243032+00:00
---

# REST Resource: projects.uptimeCheckConfigs  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.uptimeCheckConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: UptimeCheckConfig
    * JSON representation
  * ResourceGroup
    * JSON representation
  * GroupResourceType
  * SyntheticMonitorTarget
    * JSON representation
  * CloudFunctionV2Target
    * JSON representation
  * HttpCheck
    * JSON representation
  * RequestMethod
  * BasicAuthentication
    * JSON representation
  * ContentType
  * ResponseStatusCode
    * JSON representation
  * StatusClass
  * PingConfig
    * JSON representation
  * ServiceAgentAuthentication
    * JSON representation
  * ServiceAgentAuthenticationType
  * TcpCheck
    * JSON representation
  * ContentMatcher
    * JSON representation
  * ContentMatcherOption
  * JsonPathMatcher
    * JSON representation
  * JsonPathMatcherOption
  * CheckerType
  * UptimeCheckRegion
  * InternalChecker
    * JSON representation
  * State
  * Methods



## Resource: UptimeCheckConfig

This message configures which resources and services to monitor for availability.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "period": string,
      "timeout": string,
      "contentMatchers": [
        {
          object ([ContentMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcher))
        }
      ],
      "checkerType": enum ([CheckerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#CheckerType)),
      "disabled": boolean,
      "selectedRegions": [
        enum ([UptimeCheckRegion](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckRegion))
      ],
      "logCheckFailures": boolean,
      "isInternal": boolean,
      "internalCheckers": [
        {
          object ([InternalChecker](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#InternalChecker))
        }
      ],
      "userLabels": {
        string: string,
        ...
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "monitoredResource": {
        object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource))
      },
      "resourceGroup": {
        object ([ResourceGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ResourceGroup))
      },
      "syntheticMonitor": {
        object ([SyntheticMonitorTarget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#SyntheticMonitorTarget))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "httpCheck": {
        object ([HttpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck))
      },
      "tcpCheck": {
        object ([TcpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#TcpCheck))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. A unique resource name for this Uptime check configuration. The format is:
    
    
     projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID]
    

`[PROJECT_ID_OR_NUMBER]` is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response.  
`displayName` |  `string` A human-friendly name for the Uptime check configuration. The display name should be unique within a Cloud Monitoring Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.  
`period` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` How often, in seconds, the Uptime check is performed. Currently, the only supported values are `60s` (1 minute), `300s` (5 minutes), `600s` (10 minutes), and `900s` (15 minutes). Optional, defaults to `60s`.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.  
`contentMatchers[]` |  `object (`[ContentMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcher)`)` The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the `contentMatchers` list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.  
`checkerType` |  `enum (`[CheckerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#CheckerType)`)` The type of checkers to use to execute the Uptime check.  
`disabled` |  `boolean` Whether the check is disabled or not.  
`selectedRegions[]` |  `enum (`[UptimeCheckRegion](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckRegion)`)` The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.  
`logCheckFailures` |  `boolean` To specify whether to log the results of failed probes to Cloud Logging.  
`isInternal  
**(deprecated)**` |  `boolean` This item is deprecated!If this is `true`, then checks are made only from the 'internalCheckers'. If it is `false`, then checks are made only from the 'selectedRegions'. It is an error to provide 'selectedRegions' when isInternal is `true`, or to provide 'internalCheckers' when isInternal is `false`.  
`internalCheckers[]  
**(deprecated)**` |  `object (`[InternalChecker](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#InternalChecker)`)` This item is deprecated!The internal checkers that this check will egress from. If `isInternal` is `true` and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this `UptimeCheckConfig`.  
`userLabels` |  `map (key: string, value: string)` User-supplied key/value data to be used for organizing and identifying the `UptimeCheckConfig` objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.  
The resource the check is checking. Required. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`monitoredResource` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)`)` The [monitored resource](https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: `uptime_url`, `gce_instance`, `gae_app`, `aws_ec2_instance`, `aws_elb_load_balancer` `k8s_service` `servicedirectory_service` `cloud_run_revision`  
`resourceGroup` |  `object (`[ResourceGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ResourceGroup)`)` The group resource associated with the configuration.  
`syntheticMonitor` |  `object (`[SyntheticMonitorTarget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#SyntheticMonitorTarget)`)` Specifies a Synthetic Monitor to invoke.  
End of mutually exclusive fields.  
The type of Uptime check request. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`httpCheck` |  `object (`[HttpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck)`)` Contains information needed to make an HTTP or HTTPS check.  
`tcpCheck` |  `object (`[TcpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#TcpCheck)`)` Contains information needed to make a TCP check.  
End of mutually exclusive fields.  
  
## ResourceGroup

The resource submessage for group checks. It can be used instead of a monitored resource, when multiple resources are being monitored.

JSON representation  
---  
      
    
    {
      "groupId": string,
      "resourceType": enum ([GroupResourceType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#GroupResourceType))
    }  
  
Fields  
---  
`groupId` |  `string` The group of resources being monitored. Should be only the `[GROUP_ID]`, and not the full-path `projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]`.  
`resourceType` |  `enum (`[GroupResourceType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#GroupResourceType)`)` The resource type of the group members.  
  
## GroupResourceType

The supported resource types that can be used as values of `group_resource.resource_type`. `INSTANCE` includes `gce_instance` and `aws_ec2_instance` resource types. The resource types `gae_app` and `uptime_url` are not valid here because group checks on App Engine modules and URLs are not allowed.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Default value (not valid).  
`INSTANCE` | A group of instances from Google Cloud Platform (GCP) or Amazon Web Services (AWS).  
`AWS_ELB_LOAD_BALANCER` | A group of Amazon ELB load balancers.  
  
## SyntheticMonitorTarget

Describes a Synthetic Monitor to be invoked by Uptime.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudFunctionV2": {
        object ([CloudFunctionV2Target](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#CloudFunctionV2Target))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Specifies a Synthetic Monitor's execution stack. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudFunctionV2` |  `object (`[CloudFunctionV2Target](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#CloudFunctionV2Target)`)` Target a Synthetic Monitor GCFv2 instance.  
End of mutually exclusive fields.  
  
## CloudFunctionV2Target

A Synthetic Monitor deployed to a Cloud Functions V2 instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "cloudRunRevision": {
        object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Fully qualified GCFv2 resource name i.e. `projects/{project}/locations/{location}/functions/{function}` Required.  
`cloudRunRevision` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)`)` Output only. The `cloud_run_revision` Monitored Resource associated with the GCFv2. The Synthetic Monitor execution results (metrics, logs, and spans) are reported against this Monitored Resource. This field is output only.  
  
## HttpCheck

Information involved in an HTTP/HTTPS Uptime check request.

JSON representation  
---  
      
    
    {
      "requestMethod": enum ([RequestMethod](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#RequestMethod)),
      "useSsl": boolean,
      "path": string,
      "port": integer,
      "authInfo": {
        object ([BasicAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#BasicAuthentication))
      },
      "maskHeaders": boolean,
      "headers": {
        string: string,
        ...
      },
      "contentType": enum ([ContentType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentType)),
      "customContentType": string,
      "validateSsl": boolean,
      "body": string,
      "acceptedResponseStatusCodes": [
        {
          object ([ResponseStatusCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ResponseStatusCode))
        }
      ],
      "pingConfig": {
        object ([PingConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#PingConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "serviceAgentAuthentication": {
        object ([ServiceAgentAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ServiceAgentAuthentication))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`requestMethod` |  `enum (`[RequestMethod](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#RequestMethod)`)` The HTTP request method to use for the check. If set to `METHOD_UNSPECIFIED` then `requestMethod` defaults to `GET`.  
`useSsl` |  `boolean` If `true`, use HTTPS instead of HTTP to run the check.  
`path` |  `string` Optional (defaults to "/"). The path to the page against which to run the check. Will be combined with the `host` (specified within the `monitoredResource`) and `port` to construct the full URL. If the provided path does not begin with "/", a "/" will be prepended automatically.  
`port` |  `integer` Optional (defaults to 80 when `useSsl` is `false`, and 443 when `useSsl` is `true`). The TCP port on the HTTP server against which to run the check. Will be combined with host (specified within the `monitoredResource`) and `path` to construct the full URL.  
`authInfo` |  `object (`[BasicAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#BasicAuthentication)`)` The authentication information. Optional when creating an HTTP check; defaults to empty. Do not set both `authMethod` and `authInfo`.  
`maskHeaders` |  `boolean` Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if `maskHeaders` is set to `true` then the headers will be obscured with `******.`  
`headers` |  `map (key: string, value: string)` The list of headers to send as part of the Uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at <https://www.w3.org/Protocols/rfc2616/rfc2616.txt> (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentType)`)` The content type header to use for the check. The following configurations result in errors: 1. Content type is specified in both the `headers` field and the `contentType` field. 2. Request method is `GET` and `contentType` is not `TYPE_UNSPECIFIED` 3\. Request method is `POST` and `contentType` is `TYPE_UNSPECIFIED`. 4. Request method is `POST` and a "Content-Type" header is provided via `headers` field. The `contentType` field should be used instead.  
`customContentType` |  `string` A user provided content type header to use for the check. The invalid configurations outlined in the `contentType` field apply to `customContentType`, as well as the following: 1. `contentType` is `URL_ENCODED` and `customContentType` is set. 2. `contentType` is `USER_PROVIDED` and `customContentType` is not set.  
`validateSsl` |  `boolean` Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where `monitoredResource` is set to `uptime_url`. If `useSsl` is `false`, setting `validateSsl` to `true` has no effect.  
`body` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The request body associated with the HTTP POST request. If `contentType` is `URL_ENCODED`, the body passed in must be URL-encoded. Users can provide a `Content-Length` header via the `headers` field or the API will do so. If the `requestMethod` is `GET` and `body` is not empty, the API will return an error. The maximum byte size is 1 megabyte.Note: If client libraries aren't used (which performs the conversion automatically) base64 encode your `body` data since the field is of `bytes` type.A base64-encoded string.  
`acceptedResponseStatusCodes[]` |  `object (`[ResponseStatusCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ResponseStatusCode)`)` If present, the check will only pass if the HTTP response status code is in this set of status codes. If empty, the HTTP status code will only pass if the HTTP status code is 200-299.  
`pingConfig` |  `object (`[PingConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#PingConfig)`)` Contains information needed to add pings to an HTTP check.  
This field is optional and should be set only by users interested in an authenticated uptime check. Do not set both `auth_method` and `auth_info`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`serviceAgentAuthentication` |  `object (`[ServiceAgentAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ServiceAgentAuthentication)`)` If specified, Uptime will generate and attach an OIDC JWT token for the Monitoring service agent service account as an `Authorization` header in the HTTP request when probing.  
End of mutually exclusive fields.  
  
## RequestMethod

The HTTP request method options.

Enums  
---  
`METHOD_UNSPECIFIED` | No request method specified.  
`GET` | GET request.  
`POST` | POST request.  
  
## BasicAuthentication

The authentication parameters to provide to the specified resource or URL that requires a username and password. Currently, only [Basic HTTP authentication](https://tools.ietf.org/html/rfc7617) is supported in Uptime checks.

JSON representation  
---  
      
    
    {
      "username": string,
      "password": string
    }  
  
Fields  
---  
`username` |  `string` The username to use when authenticating with the HTTP server.  
`password` |  `string` The password to use when authenticating with the HTTP server.  
  
## ContentType

Header options corresponding to the content type of a HTTP request body.

Enums  
---  
`TYPE_UNSPECIFIED` | No content type specified.  
`URL_ENCODED` | `body` is in URL-encoded form. Equivalent to setting the `Content-Type` to `application/x-www-form-urlencoded` in the HTTP request.  
`USER_PROVIDED` | `body` is in `customContentType` form. Equivalent to setting the `Content-Type` to the contents of `customContentType` in the HTTP request.  
  
## ResponseStatusCode

A status to accept. Either a status code class like "2xx", or an integer status code like "200".

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "statusValue": integer,
      "statusClass": enum ([StatusClass](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#StatusClass))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Either a specific value or a class of status codes. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`statusValue` |  `integer` A status code to accept.  
`statusClass` |  `enum (`[StatusClass](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#StatusClass)`)` A class of status codes to accept.  
End of mutually exclusive fields.  
  
## StatusClass

An HTTP status code class.

Enums  
---  
`STATUS_CLASS_UNSPECIFIED` | Default value that matches no status codes.  
`STATUS_CLASS_1XX` | The class of status codes between 100 and 199.  
`STATUS_CLASS_2XX` | The class of status codes between 200 and 299.  
`STATUS_CLASS_3XX` | The class of status codes between 300 and 399.  
`STATUS_CLASS_4XX` | The class of status codes between 400 and 499.  
`STATUS_CLASS_5XX` | The class of status codes between 500 and 599.  
`STATUS_CLASS_ANY` | The class of all status codes.  
  
## PingConfig

Information involved in sending ICMP pings alongside public HTTP/TCP checks. For HTTP, the pings are performed for each part of the redirect chain.

JSON representation  
---  
      
    
    {
      "pingsCount": integer
    }  
  
Fields  
---  
`pingsCount` |  `integer` Number of ICMP pings. A maximum of 3 ICMP pings is currently supported.  
  
## ServiceAgentAuthentication

Contains information needed for generating either an [OpenID Connect token](https://developers.google.com/identity/protocols/OpenIDConnect) or [OAuth token](https://developers.google.com/identity/protocols/oauth2). The token will be generated for the Monitoring service agent service account.

JSON representation  
---  
      
    
    {
      "type": enum ([ServiceAgentAuthenticationType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ServiceAgentAuthenticationType))
    }  
  
Fields  
---  
`type` |  `enum (`[ServiceAgentAuthenticationType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ServiceAgentAuthenticationType)`)` Type of authentication.  
  
## ServiceAgentAuthenticationType

Type of authentication.

Enums  
---  
`SERVICE_AGENT_AUTHENTICATION_TYPE_UNSPECIFIED` | Default value, will result in OIDC Authentication.  
`OIDC_TOKEN` | OIDC Authentication  
  
## TcpCheck

Information required for a TCP Uptime check request.

JSON representation  
---  
      
    
    {
      "port": integer,
      "pingConfig": {
        object ([PingConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#PingConfig))
      }
    }  
  
Fields  
---  
`port` |  `integer` The TCP port on the server against which to run the check. Will be combined with host (specified within the `monitoredResource`) to construct the full URL. Required.  
`pingConfig` |  `object (`[PingConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#PingConfig)`)` Contains information needed to add pings to a TCP check.  
  
## ContentMatcher

Optional. Used to perform content matching. This allows matching based on substrings and regular expressions, together with their negations. Only the first 4 MB of an HTTP or HTTPS check's response (and the first 1 MB of a TCP check's response) are examined for purposes of content matching.

JSON representation  
---  
      
    
    {
      "content": string,
      "matcher": enum ([ContentMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcherOption)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "jsonPathMatcher": {
        object ([JsonPathMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#JsonPathMatcher))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`content` |  `string` String, regex or JSON content to match. Maximum 1024 bytes. An empty `content` string indicates no content matching is to be performed.  
`matcher` |  `enum (`[ContentMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcherOption)`)` The type of content matcher that will be applied to the server output, compared to the `content` string when the check is run.  
Certain `ContentMatcherOption` types require additional information. `MATCHES_JSON_PATH` or `NOT_MATCHES_JSON_PATH` require a `JsonPathMatcher`; not used for other options. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`jsonPathMatcher` |  `object (`[JsonPathMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#JsonPathMatcher)`)` Matcher information for `MATCHES_JSON_PATH` and `NOT_MATCHES_JSON_PATH`  
End of mutually exclusive fields.  
  
## ContentMatcherOption

Options to perform content matching.

Enums  
---  
`CONTENT_MATCHER_OPTION_UNSPECIFIED` | No content matcher type specified (maintained for backward compatibility, but deprecated for future use). Treated as `CONTAINS_STRING`.  
`CONTAINS_STRING` | Selects substring matching. The match succeeds if the output contains the `content` string. This is the default value for checks without a `matcher` option, or where the value of `matcher` is `CONTENT_MATCHER_OPTION_UNSPECIFIED`.  
`NOT_CONTAINS_STRING` | Selects negation of substring matching. The match succeeds if the output does _NOT_ contain the `content` string.  
`MATCHES_REGEX` | Selects regular-expression matching. The match succeeds if the output matches the regular expression specified in the `content` string. Regex matching is only supported for HTTP/HTTPS checks.  
`NOT_MATCHES_REGEX` | Selects negation of regular-expression matching. The match succeeds if the output does _NOT_ match the regular expression specified in the `content` string. Regex matching is only supported for HTTP/HTTPS checks.  
`MATCHES_JSON_PATH` | Selects JSONPath matching. See `JsonPathMatcher` for details on when the match succeeds. JSONPath matching is only supported for HTTP/HTTPS checks.  
`NOT_MATCHES_JSON_PATH` | Selects JSONPath matching. See `JsonPathMatcher` for details on when the match succeeds. Succeeds when output does _NOT_ match as specified. JSONPath is only supported for HTTP/HTTPS checks.  
  
## JsonPathMatcher

Information needed to perform a JSONPath content match. Used for `ContentMatcherOption::MATCHES_JSON_PATH` and `ContentMatcherOption::NOT_MATCHES_JSON_PATH`.

JSON representation  
---  
      
    
    {
      "jsonPath": string,
      "jsonMatcher": enum ([JsonPathMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#JsonPathMatcherOption))
    }  
  
Fields  
---  
`jsonPath` |  `string` JSONPath within the response output pointing to the expected `ContentMatcher::content` to match against.  
`jsonMatcher` |  `enum (`[JsonPathMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#JsonPathMatcherOption)`)` The type of JSONPath match that will be applied to the JSON output (`ContentMatcher.content`)  
  
## JsonPathMatcherOption

Options to perform JSONPath content matching.

Enums  
---  
`JSON_PATH_MATCHER_OPTION_UNSPECIFIED` | No JSONPath matcher type specified (not valid).  
`EXACT_MATCH` | Selects 'exact string' matching. The match succeeds if the content at the `jsonPath` within the output is exactly the same as the `content` string.  
`REGEX_MATCH` | Selects regular-expression matching. The match succeeds if the content at the `jsonPath` within the output matches the regular expression specified in the `content` string.  
  
## CheckerType

What kind of checkers are available to be used by the check.

Enums  
---  
`CHECKER_TYPE_UNSPECIFIED` | The default checker type. Currently converted to `STATIC_IP_CHECKERS` on creation, the default conversion behavior may change in the future.  
`STATIC_IP_CHECKERS` | `STATIC_IP_CHECKERS` are used for uptime checks that perform egress across the public internet. `STATIC_IP_CHECKERS` use the static IP addresses returned by `uptimeCheckIps.list`.  
`VPC_CHECKERS` | `VPC_CHECKERS` are used for uptime checks that perform egress using Service Directory and private network access. When using `VPC_CHECKERS`, the monitored resource type must be `servicedirectory_service`.  
  
## UptimeCheckRegion

The regions from which an Uptime check can be run.

Enums  
---  
`REGION_UNSPECIFIED` | Default value if no region is specified. Will result in Uptime checks running from all regions.  
`USA` | Allows checks to run from locations within the United States of America.  
`EUROPE` | Allows checks to run from locations within the continent of Europe.  
`SOUTH_AMERICA` | Allows checks to run from locations within the continent of South America.  
`ASIA_PACIFIC` | Allows checks to run from locations within the Asia Pacific area (ex: Singapore).  
`USA_OREGON` | Allows checks to run from locations within the western United States of America  
`USA_IOWA` | Allows checks to run from locations within the central United States of America  
`USA_VIRGINIA` | Allows checks to run from locations within the eastern United States of America  
  
## InternalChecker

This item is deprecated!

An internal checker allows Uptime checks to run on private/internal GCP resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "network": string,
      "gcpZone": string,
      "peerProjectId": string,
      "state": enum ([State](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#State))
    }  
  
Fields  
---  
`name` |  `string` A unique resource name for this InternalChecker. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/internalCheckers/[INTERNAL_CHECKER_ID]
    

`[PROJECT_ID_OR_NUMBER]` is the Cloud Monitoring Metrics Scope project for the Uptime check config associated with the internal checker.  
`displayName` |  `string` The checker's human-readable name. The display name should be unique within a Cloud Monitoring Metrics Scope in order to make it easier to identify; however, uniqueness is not enforced.  
`network` |  `string` The [GCP VPC network](https://cloud.google.com/vpc/docs/vpc) where the internal resource lives (ex: "default").  
`gcpZone` |  `string` The GCP zone the Uptime check should egress from. Only respected for internal Uptime checks, where internal_network is specified.  
`peerProjectId` |  `string` The GCP project ID where the internal checker lives. Not necessary the same as the Metrics Scope project.  
`state` |  `enum (`[State](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#State)`)` The current operational state of the internal checker.  
  
## State

Operational states for an internal checker.

Enums  
---  
`UNSPECIFIED` | An internal checker should never be in the unspecified state.  
`CREATING` | The checker is being created, provisioned, and configured. A checker in this state can be returned by `ListInternalCheckers` or `GetInternalChecker`, as well as by examining the [long running Operation](https://cloud.google.com/apis/design/design_patterns#long_running_operations) that created it.  
`RUNNING` | The checker is running and available for use. A checker in this state can be returned by `ListInternalCheckers` or `GetInternalChecker` as well as by examining the [long running Operation](https://cloud.google.com/apis/design/design_patterns#long_running_operations) that created it. If a checker is being torn down, it is neither visible nor usable, so there is no "deleting" or "down" state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create)`

|  Creates a new Uptime check configuration.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/delete)`

|  Deletes an Uptime check configuration.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/get)`

|  Gets a single Uptime check configuration.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list)`

|  Lists the existing valid Uptime check configurations for the project (leaving out any invalid configurations).  
  
### `[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/patch)`

|  Updates an Uptime check configuration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
