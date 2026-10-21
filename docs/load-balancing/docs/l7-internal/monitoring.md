---
url: https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring/
title: Internal Application Load Balancer logging and monitoring \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:27.865443+00:00
---

# Internal Application Load Balancer logging and monitoring  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal Application Load Balancer logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This document provides you with the information that you need to understand logging and monitoring metrics for [internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal). The logging and monitoring metrics for both regional internal Application Load Balancers and cross-region internal Application Load Balancers are the same.

## Logging

You can enable logging on a per-backend service basis. A single internal Application Load Balancer's URL map can reference more than one backend service. You might need to enable logging for multiple backend services depending on your configuration.

### Logs sampling and collection

The requests (and corresponding responses) handled by load balancer backend virtual machine (VM) instances are sampled. These sampled requests are then processed to generate logs. You control the fraction of the requests that are emitted as log entries according to the [logConfig.sampleRate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert#request-body) parameter. When `logConfig.sampleRate` is `1.0` (100%), logs are generated for _all of the requests_ and written to Cloud Logging.

Also, even when logging is disabled for a backend service, the load balancer might produce log entries for unsuccessful requests if the load balancer can't associate those requests with a particular backend.

### Optional fields

Log records contain required fields and optional fields. The What is logged section lists which fields are optional and which are required. All required fields are always included. You can customize which optional fields you keep.

  * If you select **include all optional** , all optional fields in the log record format are included in the flow logs. When new optional fields are added to the record format, the flow logs automatically include the new fields.

  * If you select **exclude all optional** , all optional fields are omitted.

  * If you select **custom** , you can specify the optional fields that you want to include, such as `tls.protocol,tls.cipher`.




For instructions about customizing optional fields, see Enable logging on an existing backend service.

### Enabling logging on an existing backend service

For **regional internal Application Load Balancers** , use the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of your load balancer.

  3. Click edit**Edit**.

  4. Click **Backend Configuration**.

  5. Click edit**Edit** next to your backend service.

  6. Click **Advanced configurations (Session affinity, connection draining timeout)**.

  7. Click **Enable logging**.

  8. Set a **Sample rate** fraction. You can set a number from `0.0` through `1.0`, where `0.0` means that no requests are logged and `1.0` means that 100% of the requests are logged. The default value is `1.0`.

  9. Optional: To include all the optional fields in the logs, in the **Optional fields** section, click **Include all optional fields**. 

**Pro tip:** To specify the **CUSTOM** option, use the gcloud CLI and the REST API.

  10. To finish editing the backend service, click **Update**.

  11. To finish editing the load balancer, click **Update**.




###  gcloud 

To update the backend service to enable logging, use the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --enable-logging \
        --logging-sample-rate=RATE \
        **--region= REGION** \
        --logging-optional=LOGGING_OPTIONAL_MODE \
        --logging-optional-fields=OPTIONAL_FIELDS
    

where

  * `--enable-logging` enables logging for that backend service.
  * `--logging-sample-rate` lets you specify a value from `0.0` through `1.0`, where `0.0` means no requests are logged and `1.0` means 100% of requests are logged. Only meaningful with the `--enable-logging` parameter. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.
  * `--logging-optional` lets you specify the optional fields that you want to include in the logs:

    * `INCLUDE_ALL_OPTIONAL` to include all optional fields.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional fields.

    * `CUSTOM` to include a custom list of optional fields that you specify in `OPTIONAL_FIELDS`.

  * `--logging-optional-fields` lets you specify a comma-separated list of optional fields that you want to include in the logs.

For example, `tls.protocol,tls.cipher` can only be set if `LOGGING_OPTIONAL_MODE` is set to `CUSTOM`.

If you use [custom metrics](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics) and want to log elements of the ORCA load report, you set `LOGGING_OPTIONAL_MODE` to `CUSTOM` and specify which elements must be logged in the `OPTIONAL_FIELDS` field. For example, `orcaLoadReport.cpu_utilization,orcaLoadReport.mem_utilization`. 




For **cross-region internal Application Load Balancers** , use the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of your load balancer.

  3. Click edit**Edit**.

  4. Click **Backend Configuration**.

  5. Click edit**Edit** next to your backend service.

  6. Click **Advanced configurations (Session affinity, connection draining timeout)**.

  7. Click **Enable logging**.

  8. Set a **Sample rate** fraction. You can set a number from `0.0` through `1.0`, where `0.0` means that no requests are logged and `1.0` means that 100% of the requests are logged. The default value is `1.0`.

  9. Optional: To include all the optional fields in the logs, in the **Optional fields** section, click **Include all optional fields**. 

**Pro tip:** To specify the **CUSTOM** option, use the gcloud CLI and the REST API.

  10. To finish editing the backend service, click **Update**.

  11. To finish editing the load balancer, click **Update**.




###  gcloud 

To update the backend service to enable logging, use the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --enable-logging \
        --logging-sample-rate=RATE \
        **--global** \
        --logging-optional=LOGGING_OPTIONAL_MODE \
        --logging-optional-fields=OPTIONAL_FIELDS
    

where

  * `--enable-logging` enables logging for that backend service.
  * `--logging-sample-rate` lets you specify a value from `0.0` through `1.0`, where `0.0` means no requests are logged and `1.0` means 100% of requests are logged. Only meaningful with the `--enable-logging` parameter. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.
  * `--logging-optional` lets you specify the optional fields that you want to include in the logs:

    * `INCLUDE_ALL_OPTIONAL` to include all optional fields.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional fields.

    * `CUSTOM` to include a custom list of optional fields that you specify in `OPTIONAL_FIELDS`.

  * `--logging-optional-fields` lets you specify a comma-separated list of optional fields that you want to include in the logs.

For example, `tls.protocol,tls.cipher` can only be set if `LOGGING_OPTIONAL_MODE` is set to `CUSTOM`.

If you use [custom metrics](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics) and want to log elements of the ORCA load report, you set `LOGGING_OPTIONAL_MODE` to `CUSTOM` and specify which elements must be logged in the `OPTIONAL_FIELDS` field. For example, `orcaLoadReport.cpu_utilization,orcaLoadReport.mem_utilization`. 




After you enable logging on the backend service, each HTTP(S) request is logged by using [Cloud Logging](https://docs.cloud.google.com/logging/docs).

### Disabling or modifying logging on an existing backend service

###  Console 

  1. In the Google Cloud console, go to the **Load Balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of your load balancer.

  3. Click edit**Edit**.

  4. Click **Backend Configuration**.

  5. Click edit**Edit** next to your backend service.

  6. To disable logging entirely, in the **Logging** section, clear the **Enable logging** checkbox.

  7. If you leave logging enabled, you can set a different **Sample rate** fraction. You can set a number from `0.0` through `1.0`, where `0.0` means that no requests are logged and `1.0` means that 100% of the requests are logged. The default value is `1.0`. For example, `0.2` means 20% of the sampled requests generate logs.

  8. To finish editing the backend service, click **Update**.

  9. To finish editing the load balancer, click **Update**.




###  gcloud: Cross-region mode 

Disable logging on a backend service with the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).

**Disabling logging entirely**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --global \
        --no-enable-logging
    

where

  * `--global` indicates that the backend service is global. Use this field for backend services used with cross-region internal Application Load Balancers.
  * `--no-enable-logging` disables logging for that backend service.



**Enabling logging optional fields on an existing backend service**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --global \
        --enable-logging \
        --logging-sample-rate=VALUE \
        --logging-optional=LOGGING_OPTIONAL_MODE \
        --logging-optional-fields=OPTIONAL_FIELDS
    

where

  * `--logging-sample-rate` lets you specify a value from `0.0` through `1.0`, where `0.0` means that no requests are logged and `1.0` means that 100% of the requests are logged. Only meaningful with the `--enable-logging` parameter. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.
  * `--logging-optional` lets you specify the optional fields that you want to include in the logs:

    * `INCLUDE_ALL_OPTIONAL` to include all optional fields.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional fields.

    * `CUSTOM` to include a custom list of optional fields that you specify in `OPTIONAL_FIELDS`.

  * `--logging-optional-fields` lets you specify a comma-separated list of optional fields that you want to include in the logs.

For example, `tls.protocol,tls.cipher` can only be set if `LOGGING_OPTIONAL_MODE` is set to `CUSTOM`.

If you use [custom metrics](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics) and want to log elements of the ORCA load report, you set `LOGGING_OPTIONAL_MODE` to `CUSTOM` and specify which elements must be logged in the `OPTIONAL_FIELDS` field. For example, `orcaLoadReport.cpu_utilization,orcaLoadReport.mem_utilization`. 




**Updating logging optional mode from CUSTOM to others**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --global \
        --enable-logging \
        --logging-sample-rate=VALUE \
        --logging-optional=LOGGING_OPTIONAL_MODE \
        --logging-optional-fields=
    

where

  * `--logging-optional` lets you specify the optional fields that you want to include in the logs:

    * `INCLUDE_ALL_OPTIONAL` to include all optional fields.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional fields.

  * `--logging-optional-fields` must be explicitly configured as shown to clear any existing `CUSTOM` fields. The API doesn't let you combine a non-`CUSTOM` mode with `CUSTOM` fields.




**Modifying the logging sample rate**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --global \
        --logging-sample-rate=VALUE
    

###  gcloud: Regional mode 

Disable logging on a backend service with the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).

**Disabling logging entirely**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --region=REGION \
        --no-enable-logging
    

where

  * `--region` indicates that the backend service is regional. Use this field for backend services used with regional internal Application Load Balancers.
  * `--no-enable-logging` disables logging for that backend service.



**Enabling logging optional fields on an existing backend service**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --region=REGION \
        --enable-logging \
        --logging-sample-rate=VALUE \
        --logging-optional=LOGGING_OPTIONAL_MODE \
        --logging-optional-fields=OPTIONAL_FIELDS
    

where

  * `--logging-sample-rate` lets you specify a value from `0.0` through `1.0`, where `0.0` means that no requests are logged and `1.0` means that 100% of the requests are logged. Only meaningful with the `--enable-logging` parameter. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.
  * `--logging-optional` lets you specify the optional fields that you want to include in the logs:

    * `INCLUDE_ALL_OPTIONAL` to include all optional fields.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional fields.

    * `CUSTOM` to include a custom list of optional fields that you specify in `OPTIONAL_FIELDS`.

  * `--logging-optional-fields` lets you specify a comma-separated list of optional fields that you want to include in the logs.

For example, `tls.protocol,tls.cipher` can only be set if `LOGGING_OPTIONAL_MODE` is set to `CUSTOM`.

If you use [custom metrics](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics) and want to log elements of the ORCA load report, you set `LOGGING_OPTIONAL_MODE` to `CUSTOM` and specify which elements must be logged in the `OPTIONAL_FIELDS` field. For example, `orcaLoadReport.cpu_utilization,orcaLoadReport.mem_utilization`. 




**Updating logging optional mode from CUSTOM to others**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --region=REGION \
        --enable-logging \
        --logging-sample-rate=VALUE \
        --logging-optional=LOGGING_OPTIONAL_MODE \
        --logging-optional-fields=
    

where

  * `--logging-optional` lets you specify the optional fields that you want to include in the logs:

    * `INCLUDE_ALL_OPTIONAL` to include all optional fields.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional fields.

  * `--logging-optional-fields` must be explicitly configured as shown to clear any existing `CUSTOM` fields. The API doesn't let you combine a non-`CUSTOM` mode with `CUSTOM` fields.




**Modifying the logging sample rate**
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --region=REGION \
        --logging-sample-rate=VALUE
    

### How to view logs

To view logs, in the Google Cloud console, go to the [Logs Explorer](https://console.cloud.google.com/logs) page.

Internal Application Load Balancer logs are indexed first by network and then by region.

  * To see logs for all internal Application Load Balancers, in the first pull-down menu, select **Internal Application Load Balancer Rule**.
  * To see logs for only one network, select **Internal Application Load Balancer Rule** , and then select the name of a network.
  * To see logs for just one region of the network, select **Internal Application Load Balancer Rule > `NETWORK` > `REGION`**.



Log fields of type _boolean_ typically only appear if they have a value of `true`. If a boolean field has a value of `false`, that field is omitted from the log.

[UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding is enforced for log fields. Characters that are not UTF-8 characters are replaced with question marks.

You can configure export of [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) for resource logs (`resource.type="internal_http_lb_rule"`). The metrics created are based on the "Internal Application Load Balancer Rule" resource, which is available under Cloud Monitoring dashboards:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

### What is logged

Internal Application Load Balancer log entries contain information useful for monitoring and debugging your HTTP(S) traffic. Log records contain required fields, which are the default fields of every log record, and optional fields that add additional information about your HTTP(S) traffic. Optional fields can be omitted to save storage costs. Log entries contain the following types of information:

  * General information shown in most Google Cloud logs, such as severity, project ID, project number, and timestamp as described in the [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).
  * [HttpRequest](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest) log fields.



Some log fields are in a multi-field format, with more than one piece of data in a given field. For example, the `tls` field is of the `TlsDetails` format, which contains the TLS protocol and TLS cipher in a single field. These multi-field fields are described in the following record format table.

Field | Type | Field type: Required or Optional | Description  
---|---|---|---  
`logName` | string | Required | The resource name of the log to which this log entry belongs.  
In the form `"projects/PROJECT_ID/logs/requests"`.  
`timestamp` | string | Required | The time at which the request began.  
`severity` | [LogSeverity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity) format | Required | The severity of the log entry. Defaults to `LogSeverity.DEFAULT`.  
`httpRequest` | [HttpRequest](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest) object | Required | An HttpRequest proto that describes the HTTP(S) request being logged.  
`trace` | string | Required | The resource name of the trace associated with the log entry, if any. If it contains a relative resource name, the name is assumed to be relative to `https://tracing.googleapis.com`. Example: `projects/PROJECT_ID/traces/06796866738c859f2f19b7cfb3214824`.  Internal Application Load Balancers don't support this field.   
`spanId` | string | Required | The span ID within the trace associated with the log entry. For Trace spans, this string has the same format that the Trace API v2 uses: a 16-character hexadecimal encoding of an 8-byte array, such as `000000000000004a`.  Internal Application Load Balancers don't support this field.   
`resource` | [ MonitoredResource](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) object | Required | The monitored resource that produced this log entry. The [`MonitoredResourceDescriptor`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/monitoredResourceDescriptors/list#MonitoredResourceDescriptor) object describes the schema of a `MonitoredResource` object by using a type name and a set of labels. For example, monitored resource descriptors for internal Application Load Balancers have a resource type of `internal_http_lb_rule` and use resource labels to identify the actual resource and its attributes. For a list of resource labels, see the Resource labels for `resource.type="internal_http_lb_rule"`.  
**jsonPayload** | object ([Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf?_ga=#struct) format) | Required | The log entry payload that is expressed as a JSON object. The JSON object contains the following fields: 

  * `tls`
  * `proxyStatus`
  * `backendTargetProjectNumber`
  * `serviceDirectoryService`
  * `cloudFitExperiment`
  * `cloudFitFault`
  * `serviceExtensionInfo`
  * `mtls`
  * `authzPolicyInfo`
  * `backendNetworkName`
  * `orcaLoadReport`

  
string | Required | The `proxyStatus` field holds a string that specifies why the internal Application Load Balancer returned the `HttpRequest.status`. This field is populated only when the proxy returns an error code. The field is not logged if the value is an empty string. This can happen if the proxy or backend doesn't return an error or the error code that is not `0`, `4XX`, or `5XX`. The `proxyStatus` field has two parts:

  * proxyStatus error
  * Optional: proxyStatus details

  
string | Required | The `backendTargetProjectNumber` field holds the project number that identifies the owner of the backend service or backend bucket.   
string | Required | The `serviceDirectoryService` field holds the name of the Service Directory service on which the Cloud FIT fault was configured.  
string | Required | The `cloudFitExperiment` field holds the name of the Cloud FIT experiment.  
string | Required | The `cloudFitFault` field holds the name of the fault injected by a Cloud FIT fault experiment in this request path.  
ServiceExtensionInfo | Required | The `serviceExtensionInfo` field stores information about the gRPC streams from the load balancer to Service Extensions. For more information, see [ what is logged for callout extensions](https://docs.cloud.google.com/service-extensions/docs/view-callout-log-messages#what-is-logged-for-callouts).  
AuthzPolicyInfo | Required | The `authzPolicyInfo` field stores information about the authorization policy result. This information is only available for internal Application Load Balancers that have enabled [ authorization policies](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview). For more information, see [ Authorization policy request logs](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#authz_info).  
TlsInfo | Optional | The `tls` field holds the TlsInfo field that specifies the TLS metadata for the connection between the client and the load balancer. This field is only available if the client is using TLS/SSL encryption. Use the `--logging-optional-fields` parameter to specify which elements must be logged:

  * `tls.protocol`
  * `tls.cipher`

You _can't_ set `--logging-optional-fields` to `tls` to specify all elements.  
MtlsInfo | Optional | The `mtls` field holds the MtlsInfo value that specifies the mTLS metadata for the connection between the client and the internal Application Load Balancer. This field is only available if the load balancer uses frontend mutual TLS (mTLS).   
string | Required | The `backendNetworkName` field specifies the VPC network of the backend, if the backend uses a different VPC than the load balancer's forwarding rule.   
OrcaLoadReport | Optional | The `orcaLoadReport` field contains some or all elements of the ORCA load report returned by the backend. This field is only present if the backend returns an ORCA load report, and you configured the load balancer to log the ORCA load report. Use the `--logging-optional-fields` parameter to specify which of the following elements of the ORCA load report must be logged:

  * `orcaLoadReport.cpu_utilization`
  * `orcaLoadReport.mem_utilization`
  * `orcaLoadReport.request_cost`
  * `orcaLoadReport.utilization`
  * `orcaLoadReport.rps_fractional`
  * `orcaLoadReport.eps`
  * `orcaLoadReport.named_metrics`
  * `orcaLoadReport.application_utilization`

You can also set `--logging-optional-fields` to `orcaLoadReport` to specify that all elements must be logged.  
  
#### TlsInfo field format

Field | Field format | Field type: Required or Optional | Description  
---|---|---|---  
**protocol** | string | Optional | TLS protocol that clients use to establish a connection with the load balancer. Possible values can be TLS `1.0, 1.1, 1.2, 1.3`, or `QUIC`. This value is set to `NULL` if the client is not using TLS/SSL encryption.   
**cipher** | string | Optional | TLS cipher that clients use to establish a connection with the load balancer. This value is set to `NULL` if the client is not using HTTP(S) or the client is not using TLS/SSL encryption.   
  
#### MtlsInfo field format

Field | Field format | Field type: Required or Optional | Description  
---|---|---|---  
**clientCertPresent** | bool | Optional | `true` if the client has provided a certificate during the TLS handshake; otherwise, `false`.  
**clientCertChainVerified** | bool | Optional | `true` if the client certificate chain is verified against a configured `TrustStore`; otherwise, `false`.  
**clientCertError** | string | Optional | Predefined strings representing the error conditions. For more information about the error strings, see [Client validation mode](https://docs.cloud.google.com/load-balancing/docs/mtls#client-validation-mode).  
**clientCertSha256Fingerprint** | string | Optional | Base64-encoded SHA-256 fingerprint of the client certificate.  
**clientCertSerialNumber** | string | Optional | The serial number of the client certificate. If the serial number is longer than 50 bytes, the string `client_cert_serial_number_exceeded_size_limit` is added to `client_cert_error`, and the serial number is set to an empty string.  
**clientCertValidStartTime** | string | Optional | Timestamp ([RFC 3339](https://www.ietf.org/rfc/rfc3339.html#section-5.6) date string format) before which the client certificate isn't valid. For example, `2022-07-01T18:05:09+00:00`.  
**clientCertValidEndTime** | string | Optional | Timestamp ([RFC 3339](https://www.ietf.org/rfc/rfc3339.html#section-5.6) date string format) after which the client certificate isn't valid. For example, `2022-07-01T18:05:09+00:00`.  
**clientCertSpiffeId** | string | Optional | The [SPIFFE ID](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/#spiffe-id) from the subject alternative name (SAN) field. If the value isn't valid or exceeds 2048 bytes, the SPIFFE ID is set to an empty string. If the SPIFFE ID is longer than 2048 bytes, the string `client_cert_spiffe_id_exceeded_size_limit` is added to `client_cert_error`.  
**clientCertUriSans** | string | Optional | Comma-separated Base64-encoded list of the SAN extensions of type URI. The SAN extensions are extracted from the client certificate. The SPIFFE ID is not included in the `client_cert_uri_sans` field. If the `client_cert_uri_sans` field is longer than 512 bytes, the string `client_cert_uri_sans_exceeded_size_limit` is added to `client_cert_error`, and the comma-separated list is set to an empty string.  
**clientCertDnsnameSans** | string | Optional | Comma-separated Base64-encoded list of the SAN extensions of type DNSName. The SAN extensions are extracted from the client certificate. If the `client_cert_dnsname_sans` field is longer than 512 bytes, the string `client_cert_dnsname_sans_exceeded_size_limit` is added to `client_cert_error`, and the comma-separated list is set to an empty string.  
**clientCertIssuerDn** | string | Optional | Base64-encoded full Issuer field from the certificate. If the `client_cert_issuer_dn` field is longer than 512 bytes, the string `client_cert_issuer_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_issuer_dn` is set to an empty string.  
**clientCertSubjectDn** | string | Optional | Base64-encoded full Subject field from the certificate. If the `client_cert_subject_dn` field is longer than 512 bytes, the string `client_cert_subject_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_subject_dn` is set to an empty string.  
**clientCertLeaf** | string | Optional | The client leaf certificate for an established mTLS connection where the certificate passed validation. Certificate encoding is compliant with [RFC 9440](https://datatracker.ietf.org/doc/rfc9440/): the binary DER certificate is encoded using Base64 (without line breaks, spaces, or other characters outside the Base64 alphabet) and delimited with colons on either side. If `client_cert_leaf` exceeds 16 KB unencoded, the string `client_cert_validated_leaf_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_leaf` is set to an empty string.  
**clientCertChain** | string | Optional | The comma-delimited list of certificates, in standard TLS order, of the client certificate chain for an established mTLS connection where the client certificate passed validation, not including the leaf certificate. Certificate encoding is compliant with [RFC 9440](https://datatracker.ietf.org/doc/rfc9440/). If the combined size of `client_cert_leaf` and `client_cert_chain` before Base64 encoding exceeds 16 KB, the string `client_cert_validated_chain_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_chain` is set to an empty string.  
  
### proxyStatus status field

The `proxyStatus` field contains a string that specifies why the load balancer returned an error or an info log. There are two parts in the `proxyStatus` field, `proxyStatus status` and `proxyStatus details`. This section describes the strings that are supported in the `proxyStatus status` field.

The [proxyStatus status](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#log-fields) field is applicable to the following load balancers:

  * Regional external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer



Filter this table:  proxyStatus status | Description | Common accompanying response codes  
---|---|---  
`destination_unavailable` | The load balancer considers the backend to be unavailable. For example, recent attempts to communicate with the backend have failed, or a health check might have resulted in a failure. | `500`, `503`  
`connection_timeout` | The load balancer's attempt to open a connection to the backend has timed out. | `504`  
`connection_terminated` | The load balancer's connection to the backend ended before a complete response is received. This `proxyStatus status` is returned during any of the following scenarios:

  * The load balancer's connection to the backend ended before a complete response is received.
  * The TLS connection failed on the SSL handshake, and the client didn't establish a connection with the load balancer.

| `0`, `502`, `503`  
`connection_refused` | The load balancer's connection to the backend is refused.  | `502`, `503`  
`connection_limit_reached` | The load balancer is configured to limit the number of connections it has to the backend, and that limit has been exceeded. This `proxyStatus status` is returned during any of the following scenarios:

  * If any backend is in maintenance mode, the traffic can't be routed to the backend.
  * If the request is locally rate limited.
  * Envoy is handling error conditions such as running out of memory.

| `502`, `503`  
`destination_not_found` | The load balancer can't determine the appropriate backend to use for this request. For example, the backend might not be configured. | `500`, `404`  
`dns_error` | The load balancer encountered a DNS error when trying to find an IP address for the backend hostname. | `502`, `503`  
`proxy_configuration_error` | The load balancer encountered an internal configuration error. | `500`  
`proxy_internal_error` | The load balancer encountered an internal error. | `0`, `500`, `502`  
`proxy_restart` | The proxy managing the connection is experiencing a scheduled restart. This is an informational log.  | `0`  
`proxy_internal_response` | The load balancer generated the response without attempting to connect to the backend. | Any status code depending on the type of problem. For example, the `410` status code means that the backend is unavailable due to payment delinquency.  
`http_response_timeout` | The load balancer reached a configured backend service timeout limit while waiting for the complete response from the backend. | `504`, `408`  
`http_request_error` | The load balancer encountered an HTTP 4xx error, indicating problems with the client request. | `400`, `403`, `405`, `406`, `408`, `411`, `413`, `414`, `415`, `416`, `417`, or `429`  
`http_protocol_error` | The load balancer encountered an HTTP protocol error while communicating with the backend. | `502`  
`tls_protocol_error` | The load balancer encountered a TLS error during the TLS handshake. | `0`  
`tls_certificate_error` | The load balancer encountered an error at the time of verifying the certificate presented by the server or by the client when mTLS is enabled. | `0`  
`tls_alert_received` | The load balancer encountered a fatal TLS alert during the TLS handshake. | `0`  
`no_sni` | The client did not include an SNI in its `ClientHello` message. | `0`  
`client_hello_not_detected` | The client is not using the TLS protocol. | `0`  
`invalid_sni_rfc_6066` | The SNI hostname provided is not a fully qualified DNS hostname. | `0`  
`client_hello_too_large` | The received `ClientHello` message exceeds the maximum allowed size (16 KiB). | `0`  
  
### proxyStatus details field

The `proxyStatus` field contains a string that specifies why the load balancer returned an error or info log. There are two parts in the `proxyStatus` field, `proxyStatus status` and `proxyStatus details`. The `proxyStatus details` field is optional and is shown only when additional information is available. This section describes the strings that are supported in the `proxyStatus details` field.

The [proxyStatus details](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#log-fields) field is applicable to the following load balancers:

  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer
  * Cross-region internal Application Load Balancer



Filter this table:  proxyStatus details | Description | Common accompanying response status codes  
---|---|---  
`client_disconnected_before_any_response` | The connection to the client was broken before the load balancer sent any response. | 0  
`backend_connection_closed` | The backend unexpectedly closed its connection to the load balancer. This can happen if the load balancer is sending traffic to another entity such as a third-party application that has a TCP timeout shorter than the 10-minute (600-second) timeout of the load balancer. | `502`  
`failed_to_connect_to_backend` | The load balancer failed to connect to the backend. This failure includes timeouts during the connection phase. | `503`  
`failed_to_pick_backend` | The load balancer failed to pick a healthy backend to handle the request. | `502`  
`response_sent_by_backend` | The HTTP request was proxied successfully to the backend, and the response was returned by the backend. | The HTTP status code is set by the software running on the backend.  
`client_timed_out` |  The connection between the load balancer and client exceeded the idle timeout. For more information about regional external Application Load Balancer, see [Client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#http-keepalive-timeout). For more information about internal Application Load Balancer, see [Client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/l7-internal#http-keepalive-timeout). | `0`, `408`  
`backend_timeout` | The backend timed out while generating a response. | `502`  
`http_protocol_error_from_backend_response` | The backend response contains an HTTP protocol error. | `501`, `502`  
`http_protocol_error_from_request` | The client request contains an HTTP protocol error. | `400`, `503`  
`http_version_not_supported` |  The HTTP protocol version isn't supported. Only HTTP 1.1 and 2.0 are supported. | `400`  
`handled_by_identity_aware_proxy` | This response was generated by [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap) during verifying the identity of the client before allowing access. | `200`, `302`, `400`, `401`, `403`, `500`, `502`  
`invalid_request_headers` |  The HTTP request headers received from a client contain at least one character that isn't allowed under an applicable HTTP specification. For example, header field names that include a double quotation mark (`"`) or any characters outside of the standard ASCII range (that is, any byte >= `0x80`) are invalid. For more information, see:

  * [ The "5.5. Field Values" section of RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110#section-5.5)
  * [ The "5. Field Syntax" section of RFC 9112](https://datatracker.ietf.org/doc/html/rfc9112#name-field-syntax)
  * [ The "8.2.1. Field Validity" section of RFC 9113](https://datatracker.ietf.org/doc/html/rfc9113#name-field-validity)

| `400`, `404`  
`ip_detection_failed` | The original IP address couldn't be detected. | Any status code possible depending on the nature of the failure. The value must be from `400` to `599`.  
`request_body_too_large` | The HTTP request body exceeded the maximum length supported by the load balancer. | `413`, `507`  
`request_header_timeout` | The request header timed out because the load balancer didn't receive the complete request within 5 seconds. | `408`, `504`  
`denied_by_authz_policy` | The load balancer denied this request because of an [authorization policy](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview). | `403`  
`denied_by_security_policy` | The load balancer denied this request because of a [Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-concepts). | `403`  
`throttled_by_security_policy` | The request was blocked by a Cloud Armor throttle rule. | `429`  
`client_cert_chain_invalid_eku` | Either the client certificate or its issuer doesn't have [extended key usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) that includes clientAuth. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_chain_max_name_constraints_exceeded` | An intermediate certificate provided for validation had more than 10 name constraints. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_invalid_rsa_key_size` | A client leaf or intermediate certificate had an invalid RSA key size. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_not_provided` | The client didn't provide the requested certificate during the handshake. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_pki_too_large` | The PKI to be used for validation has more than three intermediate certificates that share the same `Subject` and `Subject Public Key Info`. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_unsupported_elliptic_curve_key` | A client or intermediate certificate is using an unsupported elliptic curve. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_unsupported_key_algorithm` | A client or intermediate certificate is using a non-RSA or non-ECDSA algorithm. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_validation_failed` | The client certificate fails validation with the `TrustConfig`. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_validation_not_performed` | You have configured mutual TLS without setting up a `TrustConfig`. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`client_cert_validation_search_limit_exceeded` | The depth or iteration limit is reached while attempting to validate the certificate chain. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | 0  
`client_cert_validation_timed_out` | The time limit exceeded (200 ms) while validating the certificate chain. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `0`  
`tls_version_not_supported` | The TLS protocol version is recognized but not supported. The error results in a closed TLS connection. | `0`  
`unknown_psk_identity` | Servers send this error when PSK key establishment is required, but the client doesn't provide an acceptable PSK identity. The error results in a closed TLS connection. | `0`  
`no_application_protocol` | Sent by servers when a client "application_layer_protocol_negotiation" extension advertises only protocols that the server doesn't support. See [TLS application-layer protocol negotiation extension](https://datatracker.ietf.org/doc/html/rfc7301). The error results in a closed TLS connection. | `0`  
`no_certificate` | No certificate was found. The error results in a closed TLS connection. | `0`  
`bad_certificate` | A certificate is invalid, or it contains signatures that couldn't be verified. The error results in a closed TLS connection. | `0`  
`unsupported_certificate` | A certificate is of an unsupported type. The error results in a closed TLS connection. | `0`  
`certificate_revoked` | A certificate was revoked by its signer. The error results in a closed TLS connection. | `0`  
`certificate_expired` | A certificate has expired or it isn't valid. The error results in a closed TLS connection. | `0`  
`certificate_unknown` | Some unspecified issues arose while processing the certificate, rendering it unacceptable. The error results in a closed TLS connection. | `0`  
`unknown_ca` | A valid certificate chain or partial chain was received, but the certificate can't be accepted because the CA certificate cannot be located or matched with a known trust anchor. The error results in a closed TLS connection. | `0`  
`unexpected_message` | An inappropriate message, such as a wrong handshake message or premature application data was received. The error results in a closed TLS connection. | `0`  
`bad_record_mac` | A record is received that can't be deprotected. The error results in a closed TLS connection. | `0`  
`record_overflow` | A `TLSCiphertext` record was received that has a length more than _2 14+256_ bytes, or a record was decrypted to a `TLSPlaintext` record with more than 214 bytes (or some other negotiated limit). The error results in a closed TLS connection. | `0`  
`handshake_failure` | Unable to negotiate an acceptable set of security parameters given the options available. The error results in a closed TLS connection. | `0`  
`illegal_parameter` | A field in the handshake was incorrect or inconsistent with other fields. The error results in a closed TLS connection. | `0`  
`access_denied` | A valid certificate or PSK was received, but when access control was applied, the client didn't proceed with negotiation. The error results in a closed TLS connection. | `0`  
`decode_error` | A message couldn't be decoded because some fields are out of the specified range, or the length of the message is incorrect. The error results in a closed TLS connection. | `0`  
`decrypt_error` | A handshake (not record layer) cryptographic operation failed, including being unable to correctly verify a signature or validate a finished message or a PSK binder. The error results in a closed TLS connection. | `0`  
`insufficient_security` | A negotiation has failed specifically because the server requires parameters that are more secure than those supported by the client. The error results in a closed TLS connection. | `0`  
`inappropriate_fallback` | Sent by a server in response to an invalid connection retry attempt from a client. The error results in a closed TLS connection. | `0`  
`user_cancelled` | The user canceled the handshake for some reason unrelated to a protocol failure. The error results in a closed TLS connection. | `0`  
`missing_extension` | Sent by endpoints that receive a handshake message not containing an extension that is mandatory to send for the offered TLS version or other negotiated parameters. The error results in a closed TLS connection. | `0`  
`unsupported_extension` | Sent by endpoints that receive any handshake message containing an extension known to be prohibited for inclusion in the given handshake message, or including any extensions in `ServerHello` or `Certificate` that was not first offered in the corresponding `ClientHello` or `CertificateRequest`. The error results in a closed TLS connection. | `0`  
`unrecognized_name` | Sent by servers when no server exists that can be identified by the name provided by the client through the "server_name" extension. See [TLS extension definitions](https://datatracker.ietf.org/doc/html/rfc6066). | `0`  
`bad_certificate_status_response` | Sent by clients when an invalid or unacceptable OCSP response is provided by the server through the "status_request" extension. See [TLS extension definitions](https://datatracker.ietf.org/doc/html/rfc6066). The error results in a closed TLS connection. | `0`  
`load_balancer_configured_resource_limits_reached` | The load balancer has reached the configured resource limits, such as the maximum number of connections. | `0`  
  
#### Failed TLS connection log entries

When the TLS connection between the client and the load balancer fails before any backend is selected, log entries record the errors. You can configure the backend services with different log sample rates. When a TLS connection fails, the failed TLS connection log sample rate is the highest sample rate for any backend service. For example, if you have configured two backend services with logging sample rate as `0.3` and `0.5`, the failed TLS connection log sample rate is `0.5`.

You can identify failed TLS connections by checking for these log entry details:

  * proxyStatus error type is `tls_alert_received`, `tls_certificate_error`, `tls_protocol_error`, or `connection_terminated`.
  * There is no backend information.



The following sample shows a failed TLS log entry with the `proxyStatus error` field:
    
    
       json_payload:    {
       @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
       proxyStatus: "error="tls_alert_received"; details="server_to_client: handshake_failure""
       log_name: "projects/529254013417/logs/mockservice.googleapis.com%20name"
       }
       http_request {
        latency {
          nanos: 12412000
        }
        protocol: "HTTP/1.0"
        remote_ip: "127.0.0.2"
       }
      resource {
        type: "mock_internal_http_lb_rule"
        labels {
          backend_name: ""
          backend_scope: ""
          backend_scope_type: "UNKNOWN"
          backend_target_name: ""
          backend_target_type: "UNKNOWN"
          backend_type: "UNKNOWN"
          forwarding_rule_name: "l7-ilb-https-forwarding-rule-dev"
          matched_url_path_rule: "UNKNOWN"
          network_name: "lb-network"
          region: "REGION"
          target_proxy_name: "l7-ilb-https-proxy-dev"
          url_map_name: ""
        }
      }
      timestamp: "2023-08-15T16:49:30.850785Z"
      

#### Resource labels

The following table lists the resource labels for `resource.type="internal_http_lb_rule"`.

Field | Type | Description  
---|---|---  
`network_name` | string | The name of the load balancer's VPC network.  
`project_id` | string | The identifier of the Google Cloud project associated with this resource.  
`region` | string | The region in which the load balancer is defined.  
`url_map_name` | string | The name of the URL map object configured to select a backend service.  
`forwarding_rule_name` | string | The name of the forwarding rule object.  
`target_proxy_name` | string | The name of the target proxy object referenced by the forwarding rule.  
`matched_url_path_rule` | string |  The URL map path rule or route rule configured as part of the URL map key. Can be `UNMATCHED` or `UNKNOWN` as fallbacks. 

  * `UNMATCHED` refers to a request that matches no URL path rules, so it uses the default path rule. 
  * `UNKNOWN` indicates an internal error.

  
`backend_target_name` | string |  The name of the backend selected to handle the request, based on the URL map path rule or route rule that matches the request.   
`backend_target_type` | string | The type of backend target (`BACKEND_SERVICE` / `UNKNOWN`).  
`backend_name` | string | The name of the backend instance group or NEG.  
`backend_type` | string | The type of backend, either an instance group or a NEG, or unknown. Cloud Logging logs requests when the `backend_type` is `UNKNOWN` even if logging is disabled. For example, if a client closes the connection to the load balancer before the load balancer can pick a backend, the `backend_type` is set to `UNKNOWN` and the request is logged. These logs provide useful debugging information about client requests that were closed because the load balancer couldn't select a backend.  
`backend_scope` | string |  The scope of the backend, either a zone name or a region name. Might be `UNKNOWN` whenever `backend_name` is unknown.   
`backend_scope_type` | string |  The scope of the backend (`REGION`/`ZONE`). Might be `UNKNOWN` whenever `backend_name` is unknown.   
`backend_target_cross_project_id` | String |  The project ID of the backend target service or bucket. This field is only available if the backend target resource is created in a project different from the project in which the `url_map` resource is created.   
  
#### Authorization policy request logs

The `authz_info` object in the Load Balancer Log Entry JSON payload contains information about authorization policies. You can configure log-based metrics for traffic allowed or denied by these policies. Check more [authorization policies log details](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb#understand-authz-policy-logging).

Field | Type | Description  
---|---|---  
`authz_info.policies[]` | object | The list of policies that match the request.  
`authz_info.policies[].name` | string | The name of the authorization policy that matches the request. The name is empty for the following reasons:

  * No `ALLOW` policy matches the request and the request is denied.
  * No `DENY` policy matches the request and the request is allowed.

  
`authz_info.policies[].result` | enum | The result can be `ALLOWED` or `DENIED`.  
`authz_info.policies[].details` | string | The details include the following: 

  * `allowed_as_no_deny_policies_matched_request`
  * `denied_as_no_allow_policies_matched_request`
  * `denied_by_authz_extension`
  * `denied_by_cloud_iap`

  
`authz_info.overall_result` | enum | The result can be `ALLOWED` or `DENIED`.  
  
#### View logs for mTLS client certificate validation

To view the [logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logs-error) during mutual TLS client certificate validation, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Show query** toggle to enable the query editor.

  3. Paste the following into the **Query** field. Replace `FORWARDING_RULE_NAME` with the name of your forwarding rule.
         
         jsonPayload.statusDetails=~"client_cert"
         jsonPayload.@type="type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
         resource.labels.forwarding_rule_name=FORWARDING_RULE_NAME
         

  4. Click **Run query**.




## Monitoring

Internal Application Load Balancers export monitoring data to [Monitoring](https://docs.cloud.google.com/monitoring/docs).

Monitoring metrics can be used for the following purposes:

  * Evaluating a load balancer's configuration, usage, and performance
  * Troubleshooting problems
  * Improving resource utilization and user experience



In addition to the predefined dashboards in Monitoring, you can create custom dashboards, set up alerts, and query the metrics through the [Monitoring API](https://docs.cloud.google.com/monitoring/api).

### Viewing Cloud Monitoring metrics

###  Console 

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Internal Application Load Balancer Rule` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Internal Application Load Balancer Rule**.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



### Defining alerting policies

###  Console 

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Internal Application Load Balancer Rule` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select **Internal Application Load Balancer Rule**.
     3. Select a **Metric category** and a **Metric** , and then select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

### Defining Monitoring custom dashboards

###  Console 

You can create custom Monitoring dashboards over internal Application Load Balancer metrics:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Dashboards > Create Dashboard**.

  3. Click **Add Chart**.

  4. Give the chart a title.

  5. Select metrics and filters. For metrics, the resource type is **Internal HTTP/S Load Balancer**.

  6. Click **Save**.




### Metric reporting frequency and retention

Metrics for the load balancers are batched and exported to Monitoring every one minute. Monitoring data is retained for six weeks.

By default, the dashboard provides data analysis for the past hour (`1h`). You can request analysis for a different time interval either by selecting one of the preconfigured intervals from the menu or by manually entering the time interval you want. For example: `3h` (for 3 hours) or `4d` (for 4 days) or `6w` (for six weeks).

### Monitoring metrics

The following metrics for internal Application Load Balancers are [reported into Monitoring](https://docs.cloud.google.com/monitoring/api/metrics).

Filter this table:  Metric | FQDN | Description  
---|---|---  
Backend configured rate | `network.googleapis.com/loadbalancer/backend/configured_rate` | The maximum rate in requests per second configured per backend group. This is the result of scaling the target capacity by the capacity scaler, if specified.  
Backend configured utilization | `network.googleapis.com/loadbalancer/backend/configured_utilization` | The maximum CPU utilization capacity as a fraction, configured per backend group. This is the result of scaling the target capacity by the capacity scaler, if specified.  
Backend error rate | `network.googleapis.com/loadbalancer/backend/error_rate` | The errors served by each backend group per second.  
Backend fullness | `network.googleapis.com/loadbalancer/backend/fullness` | The current fullness of each backend group as a percentage, based on the load balancer's [balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode).  
Backend latencies | `loadbalancing.googleapis.com/https/internal/backend_latencies` |  A distribution of the backend latency. Backend latency is the time in milliseconds between the last byte of the request sent to the backend and the last byte of the response received by the proxy. It includes the time taken by the backend to process the request and the time taken for the response to be sent back to the proxy.  
Backend load balancing custom metrics | `network.googleapis.com/loadbalancer/backend/lb_custom_metric` | The current utilization by each backend group, based on your defined custom metrics.  
Backend rate | `network.googleapis.com/loadbalancer/backend/rate` | The requests received by each backend group per second.  
Backend utilization | `network.googleapis.com/loadbalancer/backend/utilization` | The aggregate CPU utilization of the VMs in the group as a fraction.  
Configured in-flight request | `network.googleapis.com/loadbalancer/backend/configured_in_flight_requests` | The maximum in-flight requests for each backend group. In-flight requests determine how the load is spread for requests running for multiple seconds.  
In-flight request | `network.googleapis.com/loadbalancer/backend/in_flight_requests` | Number of queries in progress by each backend group.  
Request count | `loadbalancing.googleapis.com/https/internal/request_count` | The number of requests served by the internal Application Load Balancer.  
Request bytes count | `loadbalancing.googleapis.com/https/internal/request_bytes` | The number of bytes sent as requests from clients to the internal Application Load Balancer.  
Response bytes count | `loadbalancing.googleapis.com/https/internal/response_bytes` | The number of bytes sent as responses from the internal HTTP(S) load balancer to the client.  
Total latencies | `loadbalancing.googleapis.com/https/internal/total_latencies` |  A distribution of the total latency. Total latency is the time in milliseconds between the first byte of the request received by the proxy and the last byte of the response sent by the proxy. It includes: the time taken by the proxy to process the request, the time taken for the request to be sent from the proxy to the backend, the time taken by the backend to process the request, the time taken for the response to be sent back to the proxy, and the time taken for the proxy to process the response and send the response to the client. It doesn't include the RTT between the client and the proxy. Additionally, pauses between requests on the same connection that use `Connection: keep-alive` do not affect the measurement. This measurement is typically reduced to the 95th percentile in Cloud Monitoring views.  
  
### Filtering dimensions for metrics

Metrics are aggregated for each internal Application Load Balancer. You can filter aggregated metrics by the following dimensions.

Property | Description  
---|---  
BACKEND_SCOPE | The Google Cloud [zone or region](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones) of the backend group that served the client request, or a special string for cases in which the backend group wasn't assigned. Examples: `us-central1-a`, `europe-west1-b`, `asia-east1`, `UNKNOWN`.   
PROXY_REGION | Region of the internal Application Load Balancer, client, and backend. Examples: `us-central1`, `europe-west1` or `asia-east1`.   
BACKEND | The name of the backend instance group or NEG that served the client request.  
BACKEND_TARGET | The name of the backend service that served the client request.  
MATCHED_URL_RULE | The URL map path rule or route rule that matched the prefix of the client HTTP(S) request (up to 50 characters).   
  
The `Response code class fraction` metric is supported for the entire load balancer. No further granularity is supported.

## What's next

  * Read [conceptual information about internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal).
  * Create an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal).
  * See [Internal load balancing and DNS names](https://docs.cloud.google.com/load-balancing/docs/dns-names) for available DNS name options your load balancer can use. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
