---
url: https://docs.cloud.google.com/apigee/docs/api-platform/errorcatalog/mp-runtime-errorcatalog/
title: Runtime error catalog \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:20.430116+00:00
---

# Runtime error catalog  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/errorcatalog/mp-runtime-errorcatalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Runtime error catalog Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Errors in Apigee

When API requests are made through Apigee, the Apigee components Routers and Message Processors, or the backend servers can return errors to the client applications. 

### Errors from Message Processor

The Message Processor is the core component of Apigee that processes the policies and interacts with the backend servers. It can return errors if it detects any issues such as:

  * Network connectivity issues, TLS handshake failures, unavailability of backend server, lack of response during communication with the backend server
  * Failures during policy execution
  * Invalid HTTP headers, encoding, path, non-adherence to HTTP specifications, exceeding product limits, etc.: 
    * With HTTP request sent by the client applications

OR

    * With HTTP response sent by the backend server
  * And many more



### Sample error from Message Processor

The Message Processor always returns an HTTP status code followed by an error message along with an error code in JSON format as shown below: 

The client application gets a response code like the following example: 
    
    
      HTTP/1.1 504 Gateway Timeout

An error response from the Message Processor appears in the following format: 
    
    
    {
      "fault": {
        "faultstring": "Gateway Timeout",
        "detail": {
          "errorcode": "messaging.adaptors.http.flow.GatewayTimeout"
          "reason": "TARGET_READ_TIMEOUT"
        }
      }
    }

**Note:** The Message Processor always returns the error in the above mentioned JSON format unless it is modified using policies such as RaiseFault or AssignMessage policy in the API proxy. 

**Description of the fields in the error response:**

Field | Description  
---|---  
`faultstring` | Contains the error message describing the possible cause for the error  
`errorcode` | Error code (also referred as **fault code**) associated with the error  
`reason` | Contains a message indicating the possible reason for the error  
  
## Runtime error catalog

This catalog describes the non-policy runtime error codes returned by the Apigee Message Processor component. (For information on the policy-specific runtime errors, see the runtime error sections in the individual policy pages, such as the [ PublishMessage policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#runtime-errors).)

This catalog includes the following information for each of the error codes: 

  * HTTP Status code
  * Error message
  * Reason for the error (not all error messages display a `reason`)
  * Possible causes for the error
  * Any associated HTTP specifications and/or product limits
  * Playbooks and videos that contain instructions to diagnose the cause of the error and effective solutions that you can apply to resolve the error yourself (where available)
  * Fix that you can apply to resolve the error yourself



The following error code categories are covered: 

  * flow.*
  * messaging.adaptors.http.flow.*
  * messaging.runtime.*
  * protocol.http.* - request
  * protocol.http.* - target
  * security.util.*



Use the **Search** box below to filter the table to display the above information for a specific error code. You can search for the status code or any content in any field in the table. 

## searchSearch

Error code | Description | Fix  
---|---|---  
  
## `flow.*`  
  
###  `flow.APITimedOut`

|  | 

  * **HTTP status code:**

| `504 Gateway Timeout`  
---|---  
  
  * **Error message:**

| `API timed out`  
  
  * **Possible cause:**

|  This error occurs if:

  * The backend server doesn't respond back within the timeout period configured by the property [ `api.timeout`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#cloud-timeouts) for the specific API Proxy.
  * A policy takes a long time due to computationally intensive operations, high load, or poor performance.

  
Fix

### Fix

To diagnose and fix the issue, refer to the [504 Gateway timeout - Target read timeout](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/504-target-read-timeout) playbook. Close  
  
###  `flow.SharedFlowNotFound`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `Shared Flow {shared_flow_name} not found`  
  
  * **Possible cause:**

|  This error occurs if the specific shared flow:

  * Does not exist
OR
  * Exists but is not deployed

  
Fix

### Fix

To diagnose and fix the issue, refer to the [FlowCallout policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy#runtime-errors). Close  
  
##  `messaging.adaptors.http.flow`  
  
###  `messaging.adaptors.http.flow.DecompressionFailureAtRequest`

|  | 

  * **HTTP status code:**

| `400 Bad Request`  
---|---  
  
  * **Error message:**

| `Decompression failure at request`  
  
  * **Reason:**

|  `CLIENT_READ_CONTENT_NOT_IN_GZIP_FORMAT` | 

  * **Possible cause:**

|  This error occurs only if:

  * The encoding specified in the HTTP request header `Content-Encoding` is valid and supported by Apigee,
**BUT**
  * The payload format sent by the client as part of the HTTP request does not match the encoding format specified in the `Content-Encoding` header

  
  
###  `messaging.adaptors.http.flow.DecompressionFailureAtResponse`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Decompression failure at response`  
  
  * **Reason:**

|  `TARGET_READ_CONTENT_NOT_IN_GZIP_FORMAT` `TARGET_READ_INCORRECT_HEADER_CHECK`  
  
  * **Possible cause:**

|  This error occurs only if:

  * The encoding specified in the backend/target server's HTTP response header `Content-Encoding` is valid and supported by Apigee,
**BUT**
  * The payload format sent by the backend/target server as part of the HTTP response does not match the encoding format specified in the `Content-Encoding` header

  
**Note:** In certain cases, when using the deflate compression algorithm together with the `Content-Encoding: deflate` header, Apigee may still return a `TARGET_READ_INCORRECT_HEADER_CHECK` error. This situation can occur when the backend's implementation of the deflate compression algorithm does not comply with [ RFC 1950](https://datatracker.ietf.org/doc/html/rfc1950). To address this issue, changing the compression algorithm at the target server from deflate to gzip, along with using the `Content-Encoding: gzip` header in the HTTP response, can be employed as a workaround.   
  
###  `messaging.adaptors.http.flow.ErrorResponseCode`

|  | 

  * **HTTP status code:**

| `500` |   
---|---|---  
  
  * **Error message:**

| Error Message and format can vary depending on the backend server implementation. |   
  
  * **Possible cause:**

| This error occurs if the backend server responds with status code `500` to Apigee. |   
  
  * **HTTP status code:**

| `503` |   
  
  * **Error message:**

| Error Message and format can vary depending on the backend server implementation. |   
  
  * **Possible cause:**

| This error occurs if the backend server responds with status code `503` to Apigee. |   
  
  * **HTTP status code:**

| `504` |   
  
  * **Error message:**

| Error Message and format can vary depending on the backend server implementation. |   
  
  * **Possible cause:**

| This error occurs if the backend server responds with status code `504` to Apigee. |   
**Note:** The error code `messaging.adaptors.http.flow.ErrorResponseCode` is not returned as part of the error message sent to the client applications. This is because this error code is set by Apigee whenever the **backend server** responds with an error and any of the `4XX` or `5XX` status codes. You can view this error code in API Monitoring or analytics database.  
  
###  `messaging.adaptors.http.flow.GatewayTimeout`

|  | 

  * **HTTP status code:**

| `504 Gateway Timeout`  
---|---  
  
  * **Error message:**

| `Gateway Timeout`  
  
  * **Reason:**

| `TARGET_READ_TIMEOUT`  
  
  * **Possible cause:**

| This error occurs if the backend server doesn't respond back to the Apigee Message Processor within the I/O timeout period configured on the Message Processor.  
Fix

### Fix

To diagnose and fix the issue, refer to the [504 Gateway timeout - Target read timeout](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/504-target-read-timeout) playbook. Close  
  
###  `messaging.adaptors.http.flow.InternalServerError`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `Internal server error at backend`  
  
  * **Reason:**

| `SERVER_ERROR`  
  
  * **Possible cause:**

| This error occurs under one of the following scenarios: 

  1. The backend application encountered an unhandled exception or error while processing the request from Apigee. This might stem from issues such as faulty logic, unexpected input, or other runtime problems within the application code.
  2. The backend server might have failed to connect to its database, or a database query might have failed. This can happen due to network connectivity, incorrect database credentials, database server downtime, or issues with the database schema or data.
  3. If your backend server depends on other internal or external services, such as APIs, message queues, or caching systems, a failure in one of these dependencies can cause it to return a `500` error to Apigee. The backend might be unable to communicate with the dependent service or might receive error responses from it.
  4. The backend server might be overloaded due to high traffic, insufficient memory (RAM), excessive CPU utilization, or low disk space. When the server lacks adequate resources, it can't process requests and responds with a `500` error.
  5. Incorrect settings on the backend server can cause unexpected errors during request processing. This includes issues with server configurations, application settings, or deployment configurations.
  6. There might be an underlying bug in the backend application code that is triggered by the specific request from Apigee. These bugs might not be apparent under normal circumstances but are exposed by certain request patterns or data.

  
  
###  `messaging.adaptors.http.flow.LengthRequired`

|  | 

  * **HTTP status code:**

| `411 Length Required`  
---|---  
  
  * **Error message:**

| `'Content-Length' is missing`  
  
  * **Reason:**

| `CLIENT_REQUEST_CONTENT_LENGTH_REQUIRED`  
  
  * **Possible cause:**

|  This error occurs if the `Content-Length` header is not passed by the client application as part of the HTTP `POST` and `PUT` requests sent to Apigee. **Note:** The requests failing with this error cannot be captured in the Trace tool, since the Message Processor performs this validation in a very early phase, much before processing the request and executing any policy in the API Proxy.  
  
  * **HTTP Specification:**

| [ RFC Section 3.3.2: Content-Length](https://datatracker.ietf.org/doc/html/rfc7230#section-3.3.2)  
Fix

### Fix

To address this error, perform the following steps:

  1. Ensure that the client application always passes the header `Content-Length` as part of the HTTP `POST` and `PUT` requests sent to Apigee. For example:
         
         curl -X POST https://HOSTALIAS/PATH -d '{"name": "abc"}' -H "Content-Length: 15"
         

  2. Even if you are passing an empty payload with `POST` and `PUT` requests, ensure that the header `Content-Length: 0` is passed. For example:
         
         curl -X POST https://HOSTALIAS/PATH -H "Content-Length: 0"
         


Close  
  
###  `messaging.adaptors.http.flow.NoActiveTargets`

|  | 

  * **HTTP status code:**

| `503 Service Unavailable` |   
---|---|---  
  
  * **Error message:**

| `The Service is temporarily unavailable` |   
  
  * **Reason:**

|  `TARGET_HEALTHCHECK_CONNECT_TIMEOUT` `TARGET_HEALTHCHECK_CONNECTION_REFUSED` `TARGET_HEALTHCHECK_HTTPS_REQUEST_OVER_HTTP` `TARGET_HEALTHCHECK_UNEXPECTED_EOF` |   
  
  * **Possible cause:**

|  This error occurs under one of the following scenarios, if you are using [ TargetServer](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#sample-targetserver-configuration) in Apigee:

  1. The incorrect DNS resolution of the backend server host by custom authorization server resulted in bad IP addresses leading to connection errors.
  2. Connection timeout errors due to:
     1. Firewall restriction on the backend server prevents Apigee from connecting to backend server.
     2. Network connectivity issues between Apigee and backend server.
  3. The host specified in the TargetServer is incorrect or has unwanted characters (such as a space).

|   
| This error can also occur if the health checks configured to monitor the health check of the target servers fail. |   
  
###  `messaging.adaptors.http.flow.RequestTimeOut`

|  | 

  * **HTTP status code:**

| `408 Request Timeout`  
---|---  
  
  * **Error message:**

| `Request timed out`  
  
  * **Reason:**

| `CLIENT_READ_TIMEOUT`  
  
  * **Possible cause:**

| This error occurs if the Apigee Message Processor doesn't receive the request payload from the client application for the I/O timeout period configured on the Message Processor component.  
Fix

### Fix

Ensure that the client application sends the request payload within the I/O timeout period configured on the Apigee's Message Processor component. Close  
  
###  `messaging.adaptors.http.flow.ServiceUnavailable`

|  | 

  * **HTTP status code:**

| `503 Service Unavailable` |   
---|---|---  
  
  * **Error message:**

| `The Service is temporarily unavailable` |   
  
  * **Reason:**

|  `TARGET_CONNECT_TIMEOUT` `TARGET_WRITE_BROKEN_PIPE` `TARGET_WRITE_CONNECTION_RESET_BY_PEER` `TARGET_CONNECT_CONNECTION_REFUSED` |   
  
  * **Possible cause:**

|  This error occurs under one of the following scenarios:

  1. The incorrect DNS resolution of the backend server host by custom authorization server resulted in bad IP addresses leading to connection errors.
  2. Connection timeout errors due to: 
     1. Firewall restriction on the backend server prevents Apigee from connecting to backend server.
     2. Network connectivity issues between Apigee and backend server.
  3. The target server host specified in the Target Endpoint is incorrect or has unwanted characters (such as space).

|  Fix

### Fix

To diagnose and fix the issue, refer to the [503 Service Unavailable error with TARGET_CONNECT_TIMEOUT playbook](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/vpc-503-target-connect-timeout). Close  
| This error can also occur if the backend server prematurely closes the connection while the Message Processor is still sending the request payload to the backend server. |   
  
###  `messaging.adaptors.http.flow.SslHandshakeFailed`

|  | 

  * **HTTP status code:**

| `503 Service Unavailable`  
---|---  
  
  * **Error message:**

| `SSL Handshake failed {error_message}`  
  
  * **Possible cause:**

|  This error occurs during the SSL handshake process between Apigee's Message Processor and the backend server if:

  1. The truststore of Apigee's Message Processor: 
     * Contains a certificate chain that does not match the backend server's complete certificate chain
OR
     * Does not contain the backend server's complete certificate chain
  2. The certificate chain presented by the backend server: 
     * Contains a Fully Qualified Domain Name (FQDN) that does not match the host name specified in the target endpoint
OR
     * Contains an incorrect/incomplete certificate chain
  3. The backend server rejects the TLS version used by Apigee.  For example, if the backend server accepts only TLS version 1.3, but the target server on the Apigee side has TLS version 1.2 set in its `TLS Protocol` field (or no TLS version is set at all, in which case Apigee will currently **not** use TLS version 1.3 as a default), the connection fails due to a mismatch of protocol versions. 

  
  
###  `messaging.adaptors.http.flow.UnexpectedEOFAtTarget`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Unexpected EOF at target`  
  
  * **Reason:**

| `TARGET_READ_UNEXPECTED_EOF`  
  
  * **Possible cause:**

|  This error occurs under one of the following scenarios:

  1. [ TargetServer](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#sample-targetserver-configuration) is not properly configured to support TLS/SSL connections in Apigee.
  2. The backend server may close the connection abruptly, while Apigee is waiting for a response from the backend server.
  3. Keep alive timeouts configured incorrectly on Apigee and backend server.
  4. The target server expects the value of the Host header to be the target DNS name, not the proxy host name. The solution is to set `use.proxy.host.header.with.target.uri` to `true` at the `HTTPTargetConnection` endpoint property. See [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).

  
  
###  `messaging.adaptors.http.flow.BadGateway`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Bad Gateway`  
  
  * **Possible cause:**

|  This error occurs if the target server sends a malformed HTTP response back to Apigee.  
  
## `messaging.runtime.*`  
  
###  `messaging.runtime.RouteFailed`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `Unable to route the message to a TargetEndpoint`  
  
  * **Possible cause:**

| This error occurs if Apigee cannot route the request to any of the TargetEndpoints because:

  * There is no route rule (`<RouteRule>`) condition that matches the request in a proxy
AND
  * There is no default route rule defined in the ProxyEndpoint (i.e., `<RouteRule>` without any condition)

  
Fix

### Fix

To address this error, follow these instructions:

  1. Review the route rules defined in your ProxyEndpoint and modify to ensure that there is at least one route rule condition that matches your request.
  2. It is a good practice to define a _default_ route rule with no condition when you have multiple RouteRules.
  3. Ensure that the default route rule is always defined last in the list of conditional Routes because rules are evaluated top-down in the ProxyEndpoint.

To learn more about defining `<RouteRule>` conditions in a ProxyEndpoint, see [ Conditional Targets](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes#determiningtheurlofthetargetendpoint-conditionaltargets). Close  
  
## `protocol.http.* - Caused due to bad request`  
  
###  `protocol.http.BadFormData`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `Bad Form Data`  
  
  * **Possible cause:**

|  This error occurs if and only if all of the following conditions are met:

  1. The HTTP request sent by the client to Apigee contains: 
     * ` **Content-Type:** application/x-www-form-urlencoded`, and
     * Form data with the percent sign (%), or the percent sign (%) followed by invalid hexadecimal characters that are not allowed as per [ Forms - Section 17.13.4.1](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.1).
  2. The API proxy in Apigee reads the specific form parameters containing any characters that are not allowed using the ExtractVariables or the AssignMessage policy in the request flow.

  
  
###  `protocol.http.DuplicateHeader`

|  | 

  * **HTTP status code:**

| `400 Bad Request`  
---|---  
  
  * **Error message:**

| `Duplicate Header "{header_name}"`  
  
  * **Possible cause:**

|  This error occurs if a specific HTTP header that is not allowed to have duplicates in Apigee, appears more than once with same or different values as part of the HTTP request sent by the client application to Apigee.   
  
  * **HTTP Specification:**

| [ RFC 7230, section 3.2.2: Field Order](https://tools.ietf.org/html/rfc7230#section-3.2.2)  
  
###  `protocol.http.EmptyHeaderName`

|  | 

  * **HTTP status code:**

| `400 Bad Request`  
---|---  
  
  * **Error message:**

| `Header name cannot be empty`  
  
  * **Possible cause:**

| This error occurs if the header name sent as part of the HTTP request by the client application to Apigee is empty.  
  
  * **HTTP Specification:**

| [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2)  
Fix

### Fix

Ensure that the HTTP request sent by the client application to Apigee always contains a valid header name as per [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2). Close  
  
###  `protocol.http.HeaderNameWithNonAsciiChar`

|  | 

  * **HTTP status code:**

| `400 Bad Request`  
---|---  
  
  * **Error message:**

| `Header {header_name} contains non ascii character {character}`  
  
  * **Possible cause:**

|  This error occurs if the header name sent as part of the HTTP request by the client application to Apigee contains non-ASCII characters.   
  
  * **HTTP Specification:**

| [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2) and [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6)  
Fix

### Fix

Ensure that the client's HTTP request sent to Apigee doesn't contain non-ASCII characters in header names as per [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6). Close  
  
###  `protocol.http.HeaderWithInvalidChar`

|  | 

  * **HTTP status code:**

| `400 Bad Request`  
---|---  
  
  * **Error message:**

| `Header {header_name} contains invalid character {character}`  
  
  * **Possible cause:**

|  This error occurs if the header name sent as part of the HTTP request by the client application to Apigee contains invalid characters such as equal (=), comma (,), semicolon (;), tab, CRLF, and Newline character.   
  
  * **HTTP Specification:**

|  [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2) and [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6)  
Fix

### Fix

Ensure that the HTTP request sent by the client application to Apigee doesn't contain any invalid characters in the header names as per [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6) Close  
  
###  `protocol.http.InvalidPath`

|  | 

  * **HTTP status code:**

| `400 Bad Request`  
---|---  
  
  * **Error message:**

| `Invalid path {path}`  
  
  * **Possible cause:**

|  This error occurs if the path in the HTTP request URL sent by the client application to Apigee contains characters that are not permitted as per the specification RFC 3986, section 3.3: Path.   
  
  * **HTTP Specification:**

| [ RFC 3986, section 3: Syntax Components](https://datatracker.ietf.org/doc/html/rfc3986#section-3) and [ RFC 3986, section 3.3: Path](https://datatracker.ietf.org/doc/html/rfc3986#section-3.3)  
Fix

### Fix

Ensure that the path in the HTTP request URL sent by the client application to Apigee does not contain any characters that are not permitted as [ per RFC 3986, section 3.3: Path](https://datatracker.ietf.org/doc/html/rfc3986#section-3.3). Close  
  
###  `protocol.http.MessageReadError`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Unexpected I/O after message headers have been read.`  
  
  * **Possible cause:**

| This rare error occurs when the MP receives I/O on a channel when it is not expecting it. The MP is reading a request, has read all the headers, and is set to read the request payload. Then it encounters an I/O event that seems to be for the same headers.   
Fix

### Fix

Locate the log message for more information on what is happening. 
    
    
    logger.atSevere().log(
        "Unexpected I/O after message headers have been read. Channel diagnostics=%s."
            + " HeartBeat=%s",
        input.client().getDiagnostic(), message.getHeaders().isHeartBeat());
                    

Close  
  
###  `protocol.http.NoResolvedHost`

|  | 

  * **HTTP status code:**

| `503 Service Unavailable`  
---|---  
  
  * **Error message:**

|  `Unable to resolve host {hostname} ` Where: `{hostname}` is dynamic and its value will change with respect to the host name provided.   
  
  * **Reason:**

| `TARGET_CONNECT_HOST_NOT_REACHABLE`  
  
  * **Possible cause:**

|  This error occurs if the target server host specified is incorrect or has unwanted characters (such as space).   
  
###  `protocol.http.TooBigBody`

|  | 

  * **HTTP status code:**

| `413 Request Entity Too Large`  
---|---  
  
  * **Error message:**

| `Body buffer overflow`  
  
  * **Possible cause:**

|  This error occurs if the payload size sent by the client application as part of HTTP request to Apigee is greater than the allowed limit in Apigee.   
  
  * **Limits:**

| [Apigee Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#system)  
  
###  `protocol.http.TooBigHeaders`

|  | 

  * **HTTP status code:**

| `431 Request Header Fields Too Large`  
---|---  
  
  * **Error message:**

| `request headers size exceeding {limit}`  
  
  * **Possible cause:**

|  The total size of all the request headers sent by the client application as part of the HTTP request to Apigee is greater than the allowed limit in Apigee.   
  
  * **HTTP Specification:**

| [ RFC 6585, section 5: 431 Request Header Fields Too Large](https://datatracker.ietf.org/doc/html/rfc6585#section-5)  
  
  * **Limits:**

| [ Apigee Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#system)  
  
###  `protocol.http.TooBigLine`

|  | 

  * **HTTP status code:**

| `414 Request-URI Too Long`  
---|---  
  
  * **Error message:**

| `request line size exceeding {limit}`  
  
  * **Possible cause:**

|  This error occurs if the size of the request line sent by the client application as part of HTTP request to Apigee is greater than the allowed limit in Apigee.   
  
  * **Limits:**

| [Apigee Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#system)  
  
###  `protocol.http.UnsupportedEncoding`

|  | 

  * **HTTP status code:**

| `415 Unsupported Media`  
---|---  
  
  * **Error message:**

| `Unsupported Encoding "{encoding}"`  
  
  * **Possible cause:**

|  This error occurs if the `Content-Encoding` header sent by the client as part of the HTTP response contains an encoding/payload format that is not supported by Apigee.   
  
  * **HTTP Specification:**

| [ RFC 7231, section 6.5.13: 415 Unsupported Media Type](https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.13)  
  
## `protocol.http.* - Caused by target`  
  
###  `protocol.http.BadPath`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `Invalid request path`  
  
  * **Possible cause:**

|  This error occurs if the request URL of the backend server, represented by the flow variable **target.url** , contains a path that starts with a question mark (?) instead of a forward slash (/), which is **invalid**.   
  
  * **HTTP Specification:**

|  [ RFC 3986, section 3: Syntax Components](https://datatracker.ietf.org/doc/html/rfc3986#section-3) and [ RFC 3986, section 3.3: Path](https://datatracker.ietf.org/doc/html/rfc3986#section-3.3)  
  
###  `protocol.http.DuplicateHeader`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Duplicate Header "{header_name}"`  
  
  * **Possible cause:**

|  This error occurs if the specific HTTP header that is not allowed to have duplicates in Apigee, appears more than once with same or different values as part of the HTTP response sent by the backend server to Apigee.   
  
  * **HTTP Specification:**

| [ RFC 7230, section 3.2.2: Field Order](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.2)  
  
###  `protocol.http.EmptyHeaderName`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Header name cannot be empty`  
  
  * **Possible cause:**

|  This error occurs if the header name sent by the backend server as part of the HTTP response to Apigee is empty.   
  
  * **HTTP Specification:**

| [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2)  
Fix

### Fix

Ensure that the HTTP response sent by the backend server to Apigee always contains a valid header name as per [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2). Close  
  
###  `protocol.http.EmptyPath`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `Request path cannot be empty`  
  
  * **Possible cause:**

|  This error occurs if the HTTP request URL of the backend server, represented by the flow variable **target.url** , contains an empty path.   
  
  * **HTTP Specification:**

|  [ RFC 3986, section 3: Syntax Components](https://datatracker.ietf.org/doc/html/rfc3986#section-3) and [ RFC 3986, section 3.3: Path](https://datatracker.ietf.org/doc/html/rfc3986#section-3.3)  
  
###  `protocol.http.HeaderNameWithNonAsciiChar`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Header {header_name} contains non ascii character {character}`  
  
  * **Possible cause:**

|  This error occurs if the header name sent by the backend server as part of the HTTP response to Apigee Edge contains non-ASCII characters.   
  
  * **HTTP Specification:**

|  [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2) and [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6)  
Fix

### Fix

Ensure that the backend server's HTTP response sent to Apigee doesn't contain non-ASCII characters in header names as per [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6). Close  
  
###  `protocol.http.HeaderWithInvalidChar`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Header {header_name} contains invalid character {character}`  
  
  * **Possible cause:**

|  This error occurs if the header name sent by the backend server as part of the HTTP response, contains invalid characters such as equal (=), comma (,), semicolon (;), tab, CRLF, and Newline character.   
  
  * **HTTP Specification:**

|  [ RFC 7230, section 3.2: Header Fields](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2) and [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6)  
Fix

### Fix

Ensure that the backend server's HTTP response sent to Apigee doesn't contain any invalid characters in the header names as per [ RFC 7230, section 3.2.6: Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6) Close  
  
###  `protocol.http.ProxyTunnelCreationFailed`

|  | 

  * **HTTP status code:**

| `503 Service Unavailable`  
---|---  
  
  * **Error message:**

| `Proxy refused to create tunnel with response status {status code}`  
  
  * **Possible cause:**

|  This error occurs during the creation of the tunnel between Apigee and the backend server by the proxy server due to firewall, ACL (Access Control List), DNS issues, availability of backend server's availability, etc. **Note:** The _status code_ in the error message (`faultstring`) provides the high-level cause of the issue.  
  
###  `protocol.http.Response306Reserved`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Response Status code 306 is reserved, so can't be used.`  
  
  * **Possible cause:**

|  This error occurs if the backend server responded back with `306` status code to Apigee. The `306` status code was defined in a previous version of the HTTP specification. As per the current HTTP specification, this code is reserved and should not be used.  
  
  * **HTTP Specification:**

| [ RFC 7231, section 6.3.5: 306 Reserved](https://datatracker.ietf.org/doc/html/rfc7231#section-6.4.6)  
Fix

### Fix

Since the status code `306` is reserved, ensure that your backend server does not use this status code while sending a response to Apigee. Close  
  
###  `protocol.http.Response405WithoutAllowHeader`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Received 405 Response without Allow Header`  
  
  * **Possible cause:**

|  The backend server responds with `405 Method Not Allowed` status code without the **"Allow"** header.   
  
  * **HTTP Specification:**

|  [ RFC 7231, section 6.5.5: 405 Method Not Allowed](https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.5) and [ RFC 7231, section 7.4.1: Allow](https://datatracker.ietf.org/doc/html/rfc7231#section-7.4.1)  
  
###  `protocol.http.ResponseWithBody`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Received {status_code} Response with message body`  
  
  * **Possible cause:**

|  This error occurs if the HTTP response from the backend server to Apigee is either `204 No Content` or `205 Reset Content` but it contains the response body and/or one or more of the following headers:

  * `Content-Length`
  * `Content-Encoding`
  * `Transfer-Encoding`

  
  
  * **HTTP Specification:**

|  [ RFC 7231, section 6.3.5: 204 No Content](https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.5) and [ RFC 7231, section 6.3.6: 205 Reset Content](https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.6)  
  
###  `protocol.http.TooBigBody`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `Body buffer overflow`  
  
  * **Possible cause:**

|  This error occurs if the payload size sent by the client application as part of HTTP request to Apigee is greater than the allowed limit in Apigee.   
  
  * **Limits:**

| [Apigee Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#system)  
  
###  `protocol.http.TooBigHeaders`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `response headers size exceeding {limit}`  
  
  * **Possible cause:**

|  This error occurs if the total size of all the response headers sent by the backend server as part of the HTTP response to Apigee is greater than the allowed limit in Apigee.   
  
  * **Limits:**

| [ Apigee Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#system)  
  
###  `protocol.http.TooBigLine`

|  | 

  * **HTTP status code:**

| `502 Bad Gateway`  
---|---  
  
  * **Error message:**

| `response line size exceeding {limit}`  
  
  * **Possible cause:**

|  This error occurs if the size of the response line sent by the backend server as part of HTTP response to Apigee is greater than the allowed limit in Apigee Edge.   
  
  * **Limits:**

| [Apigee Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#system)  
  
###  `protocol.http.UnsupportedEncoding`

|  | 

  * **HTTP status code:**

| `415 Unsupported Media`  
---|---  
  
  * **Error message:**

| `Unsupported Encoding "{encoding}"`  
  
  * **Possible cause:**

|  This error occurs if the `Content-Encoding` header sent by the backend server as part of the HTTP response contains the encoding/payload format that is not supported by Apigee.   
  
  * **HTTP Specification:**

| [ RFC 7231, section 6.5.13: 415 Unsupported Media Type](https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.13)  
  
## `security.util.*`  
  
###  `security.util.KeyAliasNotFound`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `KeyAlias {KeyAlias_name} is not found in Keystore {Keystore_Name}`  
  
  * **Possible cause:**

|  This error occurs if the specific KeyAlias referenced in the TargetEndpoint or TargetServer is not found in the specific Keystore.  
Fix

### Fix

Ensure that the KeyAlias specified in the TargetEndpoint or TargetServer exists and is part of the specific Keystore. Close  
  
###  `security.util.TrustStoreWithNoCertificates`

|  | 

  * **HTTP status code:**

| `500 Internal Server Error`  
---|---  
  
  * **Error message:**

| `TrustStore {truststore_name} has no certificates`  
  
  * **Possible cause:**

|  This error occurs if the specific Truststore referenced in the TargetEndpoint or TargetServer doesn't contain any certificates.  
Fix

### Fix

If you would like to validate the backend server's certificate and want to use the Truststore in a TargetEndpoint or TargetServer, then ensure that the Truststore contains the backend server's valid certificates. Close  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
