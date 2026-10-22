---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring/
title: Proxy Network Load Balancer logging and monitoring \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:37.985360+00:00
---

# Proxy Network Load Balancer logging and monitoring  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Proxy Network Load Balancer logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure and use [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring) for proxy Network Load Balancers.

## Monitoring resources

The following table specifies the resource names for the load balancers.

|  Regional external proxy Network Load Balancer Regional internal proxy Network Load Balancer Cross-region internal proxy Network Load Balancer Global external proxy Network Load Balancer | Classic proxy Network Load Balancer  
---|---|---  
[Logging monitored-resource type](https://docs.cloud.google.com/logging/docs/api/v2/resource-list) | "Proxy Network Load Balancer Rule"  
`l4_proxy_rule` | "Global External Proxy Network Load Balancer Rule"  
`tcp_ssl_proxy_rule`  
[Monitoring monitored-resource type](https://docs.cloud.google.com/logging/docs/api/v2/resource-list) | "Proxy Network Load Balancer Rule"  
`l4_proxy_rule` | "Global External Proxy Network Load Balancer Rule"  
`tcp_ssl_proxy_rule`  
  
## Logging for Proxy Network Load Balancers

Logs provide useful information for troubleshooting and monitoring load balancers. Logs are aggregated for each connection and give you insight into how each connection is routed to the serving backends.

There are no additional charges for using logs. However, based on how you import logs, [standard pricing for Cloud Logging](https://cloud.google.com/stackdriver/pricing#google-clouds-operations-suite-pricing), BigQuery, or Pub/Sub applies. Also, enabling logs does not affect the performance of the load balancer.

### Logs sampling and collection

The connections that leave and enter load balancer backend virtual machine (VM) instances are sampled. These sampled connections are then processed to generate logs. You control the fraction of the connections that are emitted as log entries according to the [logConfig.sampleRate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert#request-body) parameter. When `logConfig.sampleRate` is `1.0` (100%), this means that logs are generated for _all of the connections_ and written to Cloud Logging.

### Enable logging on a new backend service

### gcloud

Use the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create).

For regional external proxy Network Load Balancers and regional internal proxy Network Load Balancers:
    
    
        gcloud compute backend-services create BACKEND_SERVICE \
            --region=REGION \
            --enable-logging \
            --logging-sample-rate=SAMPLE_RATE
        

For global external proxy Network Load Balancers, classic proxy Network Load Balancers, or cross-region internal proxy Network Load Balancers:
    
    
        gcloud compute backend-services create BACKEND_SERVICE \
            --global \
            --enable-logging \
            --logging-sample-rate=SAMPLE_RATE
        

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service.
  * `REGION`: the region of the backend service to create.
  * `SAMPLE_RATE`: this field can only be specified if logging is enabled for this backend service.  


The value of the field must be from `0.0 to 1.0`, where `0.0` means that no logs are reported and `1.0` means that all connections are logged. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.




### API

Make a `POST` request to the [ `regionBackendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert):

For regional internal proxy Network Load Balancers:
    
    
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "INTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For regional external proxy Network Load Balancers:
    
    
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "EXTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For global external proxy Network Load Balancers:

Make a `POST` request to the [ `backendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert):
    
    
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "EXTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For classic proxy Network Load Balancers:

Make a `POST` request to the [ `backendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert):
    
    
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "EXTERNAL",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For cross-region internal proxy Network Load Balancers:

Make a `POST` request to the [ `backendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert):
    
    
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "INTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service.
  * `SAMPLE_RATE`: this field can only be specified if logging is enabled for this backend service.  


The value of the field must be from `0.0 to 1.0`, where `0.0` means that no logs are reported and `1.0` means that all connections are logged. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.




### Enable logging on an existing backend service

### gcloud

Use the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).

For regional external proxy Network Load Balancers and regional internal proxy Network Load Balancers:
    
    
        gcloud compute backend-services update BACKEND_SERVICE \
            --region=REGION \
            --enable-logging \
            --logging-sample-rate=SAMPLE_RATE
        

For global external proxy Network Load Balancers, classic proxy Network Load Balancers, or cross-region internal proxy Network Load Balancers:
    
    
        gcloud compute backend-services update BACKEND_SERVICE \
            --global \
            --enable-logging \
            --logging-sample-rate=SAMPLE_RATE
        

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service.
  * `REGION`: the region of the backend service to create.
  * `SAMPLE_RATE`: this field can only be specified if logging is enabled for this backend service.  


The value of the field must be from `0.0 to 1.0`, where `0.0` means that no logs are reported and `1.0` means that all connections are logged. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.




### API

Make a `PATCH` request to the [`regionBackendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/patch):
    
    
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE
         

For regional internal proxy Network Load Balancers:
    
    
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "INTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For regional external proxy Network Load Balancers:
    
    
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "EXTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For global external proxy Network Load Balancers:

Make a `PATCH` request to the [`backendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch):
    
    
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "EXTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For classic proxy Network Load Balancers:

Make a `PATCH` request to the [`backendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch):
    
    
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "EXTERNAL",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

For cross-region internal proxy Network Load Balancers:

Make a `PATCH` request to the [`backendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch):
    
    
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
        {
        "name": "BACKEND_SERVICE",
        "loadBalancingScheme": "INTERNAL_MANAGED",
        "logConfig": {
           "enable": true,
           "sampleRate": SAMPLE_RATE
          }
        }
        

Replace the following:

  * `PROJECT_ID`: the name of your project.
  * `BACKEND_SERVICE`: the name of the backend service.
  * `SAMPLE_RATE`: this field can only be specified if logging is enabled for this backend service.  


The value of the field must be from `0.0 to 1.0`, where `0.0` means that no logs are reported and `1.0` means that all connections are logged. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.




### Disable logging on an existing backend service

###  gcloud 

Use the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).

For regional external proxy Network Load Balancers and regional internal proxy Network Load Balancers:
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
       --region=REGION \
       --no-enable-logging
    

For global external proxy Network Load Balancers, classic proxy Network Load Balancers, or cross-region internal proxy Network Load Balancers:
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
       --global \
       --no-enable-logging
    

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service.
  * `REGION`: the region of the backend service.



###  API 

For regional external proxy Network Load Balancers and regional internal proxy Network Load Balancers:

Make a `PATCH` request to the [`regionBackendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/patch):
    
    
     PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE
      {
      "logConfig": {
        "enable": false
       }
      }
     

For global external proxy Network Load Balancers, classic proxy Network Load Balancers, or cross-region internal proxy Network Load Balancers:

Make a `PATCH` request to the [`backendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch):
    
    
     PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
      {
      "logConfig": {
        "enable": false
       }
      }
     

Replace the following:

  * `PROJECT_ID`: the name of your project.
  * `REGION`: the region of the backend service.
  * `BACKEND_SERVICE`: the name of the backend service.



### View logs

When logs are ingested into Cloud Logging and not excluded through a [Log Router sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks), you can read logs by using the [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#reading_log_entries).

To view all the logs, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Select the **Proxy Network Load Balancer Rule** resource type. **Note:** For classic proxy Network Load Balancers, select **Global External Proxy Network Load Balancer Rule** resource type. 

  3. Select the **loadbalancing.googleapis.com/connections** log name.




###  Console query 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Show query** toggle.

  3. Paste the following into the query field.
         
         resource.type="LOG_RESOURCE_TYPE"
         logName="projects/PROJECT_ID/logs/loadbalancing.googleapis.com/connections"
         

  4. Click **Run query**.




Replace the following:

  * `LOG_RESOURCE_TYPE`: the logging monitored-resource type set to either `l4_proxy_rule` or `tcp_ssl_proxy_rule`.
  * `PROJECT_ID`: the name of your project.



#### View logs for a specific backend service

To view the logs for a specific backend service, complete the following steps.

###  Console query 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Show query** toggle.

  3. Paste the following into the query field.
         
         resource.type="LOG_RESOURCE_TYPE"
         logName="projects/PROJECT_ID/logs/loadbalancing.googleapis.com/connections"
         resource.labels.backend_service_name="BACKEND_SERVICE_NAME"
         

  4. Click **Run query**.




Replace the following:

  * `LOG_RESOURCE_TYPE`: the logging monitored-resource type set to either `l4_proxy_rule` or `tcp_ssl_proxy_rule`.
  * `PROJECT_ID`: the name of your project.
  * `BACKEND_SERVICE_NAME`: the name of the backend service.



#### View logs for a backend instance group

To view the logs for a specific backend instance group, complete the following steps.

###  Console query 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Show query** toggle.

  3. Paste the following into the query field.
         
         resource.type="LOG_RESOURCE_TYPE"
         logName="projects/PROJECT_ID/logs/loadbalancing.googleapis.com/connections"
         resource.labels.backend_group_name="BACKEND_GROUP_NAME"
         

  4. Click **Run query**.




Replace the following:

  * `LOG_RESOURCE_TYPE`: the logging monitored-resource type set to either `l4_proxy_rule` or `tcp_ssl_proxy_rule`.
  * `PROJECT_ID`: the name of your project.
  * `BACKEND_GROUP_NAME`: the name of the instance group.



### What is logged

Log entries contain information useful for monitoring and debugging your traffic. Log records contain required fields, which are the default fields of every log record.

Field | Field format | Field type: Required or Optional | Description  
---|---|---|---  
**severity**  
**timestamp**  
**receiveTimestamp**  
**insertID**  
**logName** | [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) | Required | The general fields as described in a log entry.  
**resource** | [MonitoredResource](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) | Required | The [MonitoredResource](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) is the resource type associated with a log entry. The [MonitoredResourceDescriptor](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/monitoredResourceDescriptors/list#MonitoredResourceDescriptor) describes the schema of a `MonitoredResource` object by using a type name and a set of labels. For more information, see Resource labels.  
**jsonPayload** | object ([Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf?_ga=#struct) format) | Required | The log entry payload that is expressed as a JSON object. The JSON object contains the following fields: 

  * `statusDetails`
  * [Google Cloud Armor security policy log entries](https://docs.cloud.google.com/armor/docs/request-logging#security_policy_log_entries)
  * `proxyStatus`
  * `backendNetworkName`
  * `routeName`
  * `tlsSniHostname` ([Preview](https://cloud.google.com/products/#product-launch-stages))

  
string | Required | The `proxyStatus` field contains a string that specifies why the global external proxy Network Load Balancer, regional external proxy Network Load Balancer, and internal proxy Network Load Balancer returned an error or info log. This field is not supported for classic proxy Network Load Balancers. The field is not logged if the value is an empty string. This can happen if the proxy returns an error code that is not `0`, `4XX`, or `5XX`. The `proxyStatus` field has two parts:

  * proxyStatus status
  * Optional: proxyStatus details

  
string | Required | The `backendNetworkName` field specifies the VPC network of the backend.  
string | Required | The `routeName` field specifies the name of the TLS route which was used to route the traffic.  
string | Optional | The `tlsSniHostname` field specifies the server name provided by the client in the `ClientHello` message. ([Preview](https://cloud.google.com/products/#product-launch-stages))  
  
### Log fields

Log records contain required fields, which are the default fields of every log record.

Some log fields contain more than one piece of data in a given field—these log fields are in a multi-field format. For example, the `connection` field is of the `IpConnection` format, which contains the source and destination IP address and port, plus the protocol, in a single field. These multi-field log fields are described in the following record format table.

The following table lists all the required log fields for the resource [l4_proxy_rule](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

Field | Field format | Description  
---|---|---  
**connection** | IpConnection | 5-Tuple describing this connection.  
**startTime** | string | Timestamp (RFC 3339 date string format) when the connection from the client was accepted by the load balancer.  
**endTime** | string | Timestamp (RFC 3339 date string format) when the client or the backend terminated the connection.  
**bytesSent** | int64 | Number of bytes sent from the server to the client.  
**bytesReceived** | int64 | Number of bytes received by the server from the client.  
  
#### IpConnection field format

Field | Type | Description  
---|---|---  
**clientIp** | string | Client IP address  
**clientPort** | int32 | Client port. Set for TCP and UDP connections only.  
**serverIp** | string | Server IP address (forwarding rule IP)  
**serverPort** | int32 | Server port. Set for TCP and UDP connections only.  
**protocol** | int32 | [IANA protocol number](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)  
  
### proxyStatus status field

The `proxyStatus` field contains a string that specifies why the load balancer returned an error or an info log. There are two parts in the `proxyStatus` field, `proxyStatus status` and `proxyStatus details`. This section describes the strings that are supported in the `proxyStatus status` field.

The [proxyStatus status](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#log-fields) field is applicable to the following load balancers:

  * Global external proxy Network Load Balancer
  * Regional external proxy Network Load Balancer
  * Cross-region internal proxy Network Load Balancer
  * Regional internal proxy Network Load Balancer



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
`tls_protocol_error` | The load balancer encountered a TLS error during the TLS handshake. | `0`  
`tls_certificate_error` | The load balancer encountered an error at the time of verifying the certificate presented by the server. | `0`  
`tls_alert_received` | The load balancer encountered a fatal TLS alert during the TLS handshake. | `0`  
  
### proxyStatus details field

The `proxyStatus` field contains a string that specifies why the load balancer returned an error or info log. There are two parts in the `proxyStatus` field, `proxyStatus status` and `proxyStatus details`. The `proxyStatus details` field is optional and is shown only when additional information is available. This section describes the strings that are supported in the `proxyStatus details` field.

The [proxyStatus details](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#log-fields) field is applicable to the following load balancers:

  * Global external proxy Network Load Balancer
  * Regional external proxy Network Load Balancer
  * Regional internal proxy Network Load Balancer
  * Cross-region internal proxy Network Load Balancer



Filter this table:  proxyStatus details | Description | Common accompanying response status codes  
---|---|---  
`client_disconnected_before_any_response` | The connection to the client was broken before the load balancer sent any response. | 0  
`client_hello_too_large` | Received ClientHello is unreasonably large. The error results in a closed TLS connection ([Preview](https://cloud.google.com/products#product-launch-stages)). | 0  
`destination_not_found` | The load balancer can't determine the appropriate backend. For example, the indicated SNI hostname did not match (see jsonPayload.tls.sni for the indicated SNI). The error results in a closed TLS connection. ([Preview](https://cloud.google.com/products#product-launch-stages)) | 0  
`invalid_sni_rfc_6066` | The indicated SNI hostname is invalid. SNI must be the fully qualified DNS hostname. The error results in a closed connection. [Preview](https://cloud.google.com/products#product-launch-stages)) | 0  
`client_hello_not_detected` | TLS was not found on the connection. The error results in a closed connection. ([Preview](https://cloud.google.com/products#product-launch-stages)) | 0  
`backend_connection_closed` | The backend unexpectedly closed its connection to the load balancer. This can happen if the load balancer is sending traffic to another entity such as a third-party application that has a TCP timeout shorter than the 10-minute (600-second) timeout of the load balancer. | `502`  
`failed_to_connect_to_backend` | The load balancer failed to connect to the backend. This failure includes timeouts during the connection phase. | `503`  
`failed_to_pick_backend` | The load balancer failed to pick a healthy backend to handle the request. | `502`  
`handled_by_identity_aware_proxy` | This response was generated by [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap) during verifying the identity of the client before allowing access. | `200`, `302`, `400`, `401`, `403`, `500`, `502`  
`request_overall_timeout` | The total request timeout was exceeded. For more information, see [Logged errors for closed connections](https://docs.cloud.google.com/load-balancing/docs/mtls#logged-errors-both-modes). | `408`, `503`, `504`  
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
      

### Resource labels

The following table lists the resource labels for resource type `l4_proxy_rule`.

Field | Type | Description  
---|---|---  
**network_name** | string | The name of the load balancer's VPC network.  
**project_id** | string | The identifier of the Google Cloud project associated with this resource.  
**region** | string | The region where the load balancer is defined.  
**target_proxy_name** | string | The name of the target proxy object referenced by the forwarding rule.   
**forwarding_rule_name** | string | The name of the forwarding rule object.  
**loadbalancing_scheme_name** | string | An attribute on the forwarding rule and the backend service of a load balancer that indicates whether the load balancer can be used for internal or external traffic.  
**backend_target_name** | string | The name of the backend selected to handle the request.  
**backend_target_type** | string | The type of backend target `(BACKEND_SERVICE / UNKNOWN)`.  
**backend_name** | string | The name of the backend instance group or network endpoint group (NEG).  
**backend_type** | string | The type of backend, either an instance group or a NEG, or unknown. Cloud Logging logs requests when the backend_type is `UNKNOWN` even if logging is disabled. For example, if a client closes the connection to the load balancer before the load balancer can pick a backend, the `backend_type` is set to `UNKNOWN` and the request is logged. These logs provide useful debugging information about client requests that were closed because the load balancer couldn't select a backend.  
**backend_scope** | string | The scope of the backend, either a zone name or a region name. Might be `UNKNOWN` whenever `backend_name` is unknown.  
**backend_scope_type** | string | The scope of the backend (`REGION/ZONE`). Might be `UNKNOWN` whenever `backend_name` is unknown.  
  
## Monitoring

The proxy Network Load Balancers export monitoring data to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

Monitoring metrics can be used to do the following:

  * Evaluate a load balancer's configuration, usage, and performance.
  * Troubleshoot problems.
  * Improve resource utilization and user experience.



In addition to the predefined dashboards in Monitoring, you can create custom dashboards, set up alerts, and query metrics by using the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api).

### View Monitoring dashboards

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. If **Resources** appears in the navigation pane, select **Resources** , and then select **Google Cloud Load Balancers**. Otherwise, select **Dashboards** , and then select the dashboard named **Google Cloud Load Balancers**.

  3. Click the name of your load balancer.




In the left pane, you can see various details for this load balancer. In the right pane, you can see timeseries graphs. To see specific breakdowns, click **Breakdowns**.

### Metric reporting frequency and retention

Metrics for the load balancers are batched and exported to Monitoring every one minute. Monitoring data is retained for six weeks.

By default, the dashboard provides data analysis for the past hour (`1h`). You can request analysis for a different time interval either by selecting one of the preconfigured intervals from the menu or by manually entering the time interval you want. For example: `3h` (for 3 hours) or `4d` (for 4 days) or `6w` (for six weeks).

### Metrics for classic proxy Network Load Balancers

The following metrics for classic proxy Network Load Balancers are reported into Monitoring.

Metric | Name | Description  
---|---|---  
Inbound traffic | `tcp_ssl_proxy/ingress_bytes_count` | The number of bytes sent from external endpoints to configured backends through the Google Front End (GFE)—in bytes per second.  
Outbound traffic | `tcp_ssl_proxy/egress_bytes_count` | The number of bytes sent from configured backends to external endpoints through the GFE—in bytes per second.  
Open connections | `tcp_ssl_proxy/open_connections` | The number of connections open at the given sample moment. Samples are taken one minute apart.  
New connections per second | `tcp_ssl_proxy/new_connections` | The number of connections that were created (client successfully connected to backend). The counting granularity is per minute, but graphs are adjusted to show per second values. For more information, see the [Monitoring documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).  
Closed connections per second | `tcp_ssl_proxy/closed_connections` | The number of connections that were closed. The counting granularity is per minute, but graphs are adjusted to show per second values. For more information, see the [Monitoring documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).  
Frontend RTT | `tcp_ssl_proxy/frontend_tcp_rtt` | A distribution of the smoothed round-trip time (RTT) measured for each connection between the client and the GFE (measured by the GFE's TCP stack, each time application layer bytes pass from the GFE to the client). Smoothed RTT is an algorithm that deals with variations and anomalies that might occur in RTT measurements.  
  
### Metrics for other load balancers

The following metrics for regional internal proxy Network Load Balancers, regional external proxy Network Load Balancers, cross-region internal proxy Network Load Balancer, and global external proxy Network Load Balancers are reported into Monitoring.

Metric | Name | Description  
---|---|---  
Inbound traffic | `l4_proxy/ingress_bytes_count` | The number of bytes sent from the client to the backend VM by using the proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds.  
Outbound traffic | `l4_proxy/egress_bytes_count` | The number of bytes sent from the backend VM to the client by using the proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds.  
Closed connections per second | `l4_proxy/tcp/closed_connections_count` | The number of connections that were terminated by using a TCP RST or TCP FIN message. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds.  
  
### Filtering dimensions for metrics

Metrics are aggregated for each load balancer. Metrics can be further broken down by the following dimensions.

Property | Description  
---|---  
BACKEND SCOPE | The scope ([region or zone](https://docs.cloud.google.com/compute/docs/regions-zones)) of the instance group that served the connection.   
BACKEND ZONE | If the instance group was a zonal instance group, the zone of the instance group that served the connection.   
BACKEND REGION | If the instance group was a regional instance group, the region of the instance group that served the connection.   
PROXY CONTINENT | The continent of the GFE that terminated the user TCP/SSL connection—for example, `America`, `Europe`, `Asia`.   
INSTANCE GROUP | The name of the instance group that received the user connection.   
FORWARDING RULE | The name of the forwarding rule used to connect to the GFE.  
CLIENT COUNTRY | The name of the country of the user.  
  
## What's next

  * To learn how SSL policies work, see the [SSL policies overview](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts).
  * To learn how external proxy Network Load Balancers work, see the [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp).
  * To learn how internal proxy Network Load Balancers work, see the [Internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
