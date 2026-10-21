---
url: https://docs.cloud.google.com/load-balancing/docs/https/custom-headers/
title: Create custom headers in backend services \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:21.245736+00:00
---

# Create custom headers in backend services  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/custom-headers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Create custom headers in backend services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure custom headers in backend services used by the classic Application Load Balancer. 

Custom request and response headers let you specify additional headers that the load balancer can add to HTTP(S) requests and responses. Depending on the information detected by the load balancer, these headers can include the following information:

  * Latency to the client
  * Geographic location of the client's IP address
  * Parameters of the TLS connection



Custom _request_ headers are supported for backend services, while custom _response_ headers are supported for backend services and backend buckets.

The load balancer adds certain headers by default to all HTTP(S) requests and responses that it proxies between backends and clients. For more information, see [Target proxies](https://docs.cloud.google.com/load-balancing/docs/https#target-proxies).

## Before you begin

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        

**Note:** Make sure that you're using gcloud CLI version `309.0.0` or later.



## How custom headers work

Custom headers work as follows:

  * When the load balancer forwards a request to the backend, the load balancer adds request headers.

The load balancer adds custom request headers only to the client requests, not to the health check probes. If your backend requires a specific header for authorization that is missing from the health check packet, the health check might fail.

  * The load balancer sets response headers before returning the responses to the client.




To enable custom headers, you specify a list of headers in a property of the backend service or backend bucket.

You specify each header as a `header-name:header-value` string. The header must contain a colon separating the header name and header value.

_Header names_ must fulfill the following requirements:

  * The header name must be a valid HTTP header-field name definition (per [RFC 7230](https://tools.ietf.org/html/rfc7230)). 
  * The header name must not be `X-User-IP` or `CDN-Loop`.
  * The following hop-by-hop headers must not be used: `Keep-Alive`, `Transfer-Encoding`, `TE`, `Connection`, `Trailer`, and `Upgrade`. In accordance with [RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616#page-92), these headers are not stored by caches or propagated by the target proxies.
  * The header name must not begin with `X-Google`, `X-Goog-`, `X-GFE` or `X-Amz-`.
  * A header name must not appear more than once in the list of added headers.



_Header values_ must fulfill the following requirements:

  * The header value must be a valid HTTP header field definition per [RFC 7230](https://tools.ietf.org/html/rfc7230), with obsolete forms disallowed.
  * The header value can be empty.
  * The header value can include one or more variables, enclosed in curly braces, that expand to values that the load balancer provides. For more information, see Variables supported within header values.



The `gcloud` command-line tool has a flag for specifying request headers, which is `--custom-request-header`. Make sure to enclose the header name and header value in straight single quotes (`'`) with this flag.

The general format for the flag is:
    
    
        --custom-request-header='HEADER_NAME:[HEADER_VALUE]'
    

The following is an example of a header value with two variables, `client_region` and `client_city`, enclosed in curly braces.
    
    
        --custom-request-header='X-Client-Geo-Location:{client_region},{client_city}'
    

For clients located in Mountain View, California, the load balancer adds a header as follows:

`X-Client-Geo-Location:US,Mountain View`

To create a backend service with custom headers, see [Configure custom request headers](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers#working-with-request). 

## Variables supported within header values

To inject dynamic, request-specific metadata into your custom headers, you can use the following variables. When these variables are enclosed in curly braces (`{}`) within a header value, the load balancer expands them to their real-time values, such as the client's geographic location, connection parameters, or cache status, before passing the header to your backend or client.

Variable | Description  
---|---  
`cdn_cache_id` | Location code and ID of the cache instance used to serve the request. This is the same value populated in the `jsonPayload.cacheId` field of the Cloud CDN request logs in Logging.   
`cdn_cache_status` | Current cache status. Values can be `hit`, `miss`, `revalidated`, `stale`, `uncacheable`, or `disabled` for any object served by a Cloud CDN-enabled backend.   
`origin_request_header` | Reflects the value of the `Origin` header in the request for Cross-Origin Resource Sharing (CORS) use cases.   
`client_rtt_msec` | Estimated round-trip transmission time between the load balancer and the HTTP(S) client, in milliseconds. This is the smoothed round-trip time (SRTT) parameter measured by the load balancer's TCP stack, per [RFC 2988](https://tools.ietf.org/html/rfc2988). Smoothed RTT is an algorithm that deals with variations and anomalies that may occur in RTT measurements.  
`client_region` | The country (or region) associated with the client's IP address. This is a Unicode CLDR region code, such as `US` or `FR`. (For most countries, these codes correspond directly to [ISO-3166-2 codes](https://wikipedia.org/wiki/ISO_3166-1_alpha-2).)   
`client_region_subdivision` | Subdivision, for example, a province or state, of the country associated with the client's IP address. This is a Unicode CLDR subdivision ID, such as `USCA` or `CAON`. (These Unicode codes are derived from the subdivisions defined by the [ISO-3166-2 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).)   
`client_city` | Name of the city from which the request originated, for example, `Mountain View` for Mountain View, California. There is no canonical list of valid values for this variable. The city names can contain US-ASCII letters, numbers, spaces, and the following characters: `!#$%&'*+-.^_`|~`.   
`client_city_lat_long` | Latitude and Longitude of the city from which the request originated, for example, `37.386051,-122.083851` for a request from Mountain View.   
`client_ip_address` | The client's IP address. This is usually the same as the client IP address that is the next-to-last address in the [`X-Forwarded-For`](https://docs.cloud.google.com/load-balancing/docs/https#x-forwarded-for_header) header, unless the client is using a proxy or the `X-Forwarded-For` header has been tampered with.  
`client_port` | The client's source port.  
`client_encrypted` | `true` if the connection between the client and the load balancer is encrypted (using HTTPS, HTTP/2 or HTTP/3); otherwise, `false`.   
`client_protocol` | The HTTP protocol used for communication between the client and the load balancer. One of `HTTP/1.0`, `HTTP/1.1`, `HTTP/2`, or `HTTP/3`.   
`device_request_type` |  The client's device, derived from `User-Agent` header values.  The following are possible values: `DESKTOP`, `GAME_CONSOLE`, `GAME_CONSOLE`, `MOBILE`, `SET_TOP_BOX`, `SMART_SPEAKER`, `SMART_TV`, `TABLET`, `UNDETERMINED`, `WEARABLE`.   
`server_ip_address` | The IP address of the load balancer that the client connects to. This can be useful when multiple load balancers share common backends. This is the same as the last IP address in the [`X-Forwarded-For`](https://docs.cloud.google.com/load-balancing/docs/https#x-forwarded-for_header) header.   
`server_port` | The destination port number that the client connects to.  
`tls_sni_hostname` | Server name indication (as defined in [RFC 6066](https://tools.ietf.org/html/rfc6066.html)), if provided by the client during the TLS or QUIC handshake. The hostname is converted to lowercase and with any trailing dot removed.   
`tls_version` | TLS version negotiated between client and load balancer during the SSL handshake. Possible values include: `TLSv1`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`. If the client connects using QUIC instead of TLS, the value is `QUIC`.   
`tls_cipher_suite` | Cipher suite negotiated during the TLS handshake. The value is four hex digits defined by the [IANA TLS Cipher Suite Registry](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml), for example, `009C` for TLS_RSA_WITH_AES_128_GCM_SHA256. This value is empty for QUIC and for unencrypted client connections.   
`tls_ja3_fingerprint` | [JA3 TLS/SSL fingerprint](https://github.com/salesforce/ja3) if the client connects using HTTPS, HTTP/2, or HTTP/3.  
`tls_ja4_fingerprint` | [JA4 TLS/SSL fingerprint](https://github.com/FoxIO-LLC/ja4/blob/main/technical_details/JA4.md) if the client connects using HTTPS, HTTP/2, or HTTP/3.  
`user_agent_family` |  The client's browser type, derived from `User-Agent` header values.  The following are possible values: `APPLE`, `APPLEWEBKIT`, `BLACKBERRY`, `DOCOMO`, `GECKO`, `GOOGLE`, `KHTML`, `KOREAN`, `MICROSOFT`, `MSIE`, `NETFRONT`, `NOKIA`, `OBIGO`, `OPERA`, `OPENWAVE`, `OTHER`, `POLARIS`, `SEMC`, `SMIT`, `TELECA`, `USER_DEFINED`.   
`asn` | The Autonomous System Number (ASN) associated with the client's IP address.  
`cloud_trace_id` | The trace ID extracted (or generated) from the HTTP request header.   
`hostname` | The original hostname specified by the client in the `Host` HTTP request header. The value is converted to lowercase with any trailing dot removed.   
  
The load balancer expands variables to empty strings when it cannot determine their values. For example:

  * Geographic location variables when the IP address's location is unknown
  * TLS parameters when TLS is not in use
  * The `{origin_request_header}` when the request does not include an `Origin` header
  * The `{cdn_cache_status}` header when included in a request header



Geographic values (regions, subdivisions, and cities) are estimates based on the client's IP address. From time to time, Google updates the data that provides these values in order to improve accuracy and to reflect geographic and political changes. Even if the original `X-Forwarded-For` header contains valid location information, Google estimates client locations by using the source IP address information contained in packets received by the load balancer.

Headers added by the load balancer overwrite any existing headers that have the same name. Header names are case insensitive. When header names are passed to an HTTP/2 backend, the HTTP/2 protocol encodes header names as lower case.

In header values, leading whitespace and trailing whitespace are insignificant, and are not passed to the backend. To allow for curly braces in header values, the load balancer interprets two opening curly braces (`{{`) as a single opening brace (`{`), and two closing curly braces (`}}`) as a single closing brace (`}`).

## Mutual TLS custom headers

The following additional header variables are available if mutual TLS (mTLS) is configured on the load balancer's TargetHttpsProxy.

Variable | Description  
---|---  
`client_cert_present` | `true` if the client has provided a certificate during the TLS handshake; otherwise, `false`.   
`client_cert_chain_verified` | `true` if the client certificate chain is verified against a configured `TrustStore`; otherwise, `false`.   
`client_cert_error` | Predefined strings representing the error conditions. For more information about the error strings, see [mTLS client validation modes](https://docs.cloud.google.com/load-balancing/docs/mtls#mtls_errors).   
`client_cert_sha256_fingerprint` | Base64-encoded SHA-256 fingerprint of the client certificate.  
`client_cert_serial_number` | The serial number of the client certificate. If the serial number is longer than 50 bytes, the `client_cert_error` is set to `client_cert_serial_number_exceeded_size_limit`, and the serial number is set to an empty string.  
`client_cert_spiffe_id` | The [SPIFFE ID](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/#spiffe-id) from the subject alternative name (SAN) field. If the value is not valid or exceeds 2048 bytes, the SPIFFE ID is set to an empty string. If the SPIFFE ID is longer than 2048 bytes, the `client_cert_error` is set to `client_cert_spiffe_id_exceeded_size_limit`.  
`client_cert_uri_sans` | Comma-separated Base64-encoded list of the SAN extensions of type URI. The SAN extensions are extracted from the client certificate. The SPIFFE ID is not included in the `client_cert_uri_sans` field. If the `client_cert_uri_sans` is longer than 512 bytes, the `client_cert_error` is set to `client_cert_uri_sans_exceeded_size_limit`, and the comma-separated list is set to an empty string.  
`client_cert_dnsname_sans` | Comma-separated Base64-encoded list of the SAN extensions of type DNSName. The SAN extensions are extracted from the client certificate. If the `client_cert_dnsname_sans` is longer than 512 bytes, the `client_cert_error` is set to `client_cert_dnsname_sans_exceeded_size_limit`, and the comma-separated list is set to an empty string.  
`client_cert_valid_not_before` | Timestamp ([RFC 3339](https://www.ietf.org/rfc/rfc3339.html#section-5.6) date string format) before which the client certificate is not valid. For example, `2022-07-01T18:05:09+00:00`.   
`client_cert_valid_not_after` | Timestamp ([RFC 3339](https://www.ietf.org/rfc/rfc3339.html#section-5.6) date string format) after which the client certificate is not valid. For example, `2022-07-01T18:05:09+00:00`.   
`client_cert_issuer_dn` | Base64-encoded DER encoding of the full Issuer field from the certificate. If the `client_cert_issuer_dn` is longer than 512 bytes, the string `client_cert_issuer_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_issuer_dn` is set to an empty string.  
`client_cert_subject_dn` | Base64-encoded DER encoding of the full Subject field from the certificate. If the `client_cert_subject_dn` is longer than 512 bytes, the string `client_cert_subject_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_subject_dn` is set to an empty string.  
`client_cert_leaf` | The client leaf certificate for an established mTLS connection where the certificate passed validation. Certificate encoding is compliant with [RFC 9440](https://datatracker.ietf.org/doc/rfc9440/). This means the binary DER certificate is encoded using Base64 and delimited with colons on either side. If `client_cert_leaf` exceeds 16 KB unencoded, the string `client_cert_validated_leaf_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_leaf` is set to an empty string.  
`client_cert_chain` | The comma-delimited list of certificates, in standard TLS order, of the client certificate chain for an established mTLS connection where the client certificate passed validation, not including the leaf certificate. Certificate encoding is compliant with [RFC 9440](https://datatracker.ietf.org/doc/rfc9440/). If the combined size of `client_cert_leaf` and `client_cert_chain` before Base64 encoding exceeds 16 KB, the string `client_cert_validated_chain_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_chain` is set to an empty string.  
  
## Configure custom request headers

###  Console 

To add custom request headers to an existing backend service:

  1. Go to the load balancing summary page.  
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)
  2. Click **Backends**.
  3. Click the name of a backend service.
  4. Click **Edit** edit.
  5. Click **Advanced configurations (Session affinity, connection draining timeout, security policies)**.
  6. Under **Custom request headers** , click **Add header**.
  7. Enter the **Header name** and **Header value** for the custom request header.
  8. Enter any additional custom request headers.
  9. Click **Save**.



To remove a custom request header from a backend service:

  1. Go to the load balancing summary page.  
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)
  2. Click **Backends**.
  3. Click the name of a backend service.
  4. Click **Edit** edit.
  5. Click **Advanced configurations (Session affinity, connection draining timeout, security policies)**.
  6. Click the **X** next to the name of the custom request header you want to remove.
  7. Click **Save**.



###  gcloud 

To specify custom request headers, use the [`gcloud compute backend-services create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--custom-request-header` flag.

To create a backend service with custom request headers:
    
    
    gcloud compute backend-services create BACKEND_SERVICE_NAME \
        --global-health-checks \
        --global \
        --protocol HTTPS \
        --health-checks https-basic-check \
        --custom-request-header='HEADER_NAME:[HEADER_VALUE]'
    

To add more request headers, specify a unique header name and value by repeating the `--custom-request-header` flag.

To add custom headers to an existing backend service:
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
        --global \
        --custom-request-header='HEADER_1_NAME:[HEADER_1_VALUE]' \
        --custom-request-header='HEADER_2_NAME:[HEADER_2_VALUE]'
    

The previous step replaces any headers already in the backend service with the request headers that you specify in the command.

To remove all headers from a backend service:
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
        --global \
        --no-custom-request-headers
    

###  API 

Make a `PATCH` request to the [`backendServices.patch`](https://docs.cloud.google.com/compute/docs/reference/latest/backendServices/patch) method:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME
    "customRequestHeaders": [
       "client_city:Mountain View"
    ]
    

###  Terraform 

For a Terraform script that creates a load balancer with custom headers, see [Terraform examples for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples#mig-and-custom-headers). 

## Configure custom response headers

###  Console 

To add custom response headers to an existing backend service:

  1. Go to the load balancing summary page.  
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)
  2. Click **Backends**.
  3. Click the name of a backend service.
  4. Click **Edit** edit.
  5. Click **Advanced configurations (Session affinity, connection draining timeout, security policies)**.
  6. Under **Custom response headers** , click **Add header**.
  7. Enter the **Header name** and **Header value** for the custom response header.
  8. Enter any additional custom response headers.
  9. Click **Save**.



To remove a custom response header from a backend service:

  1. Go to the load balancing summary page.  
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)
  2. Click **Backends**.
  3. Click the name of a backend service.
  4. Click **Edit** edit.
  5. Click **Advanced configurations (Session affinity, connection draining timeout, security policies)**.
  6. Click the **X** next to the name of the custom response header you want to remove.
  7. Click **Save**.



### gcloud

For backend services, use the [`gcloud compute backend-services create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--custom-response-header` flag.

For backend buckets, use the [`gcloud compute backend-buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [`gcloud compute backend-buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) command with the `--custom-response-header` flag.
    
    
    gcloud compute backend-services (create | update) BACKEND_SERVICE_NAME
        --custom-response-header='HEADER_NAME:[HEADER_VALUE]'
    
    
    
    gcloud compute backend-buckets (create | update) BACKEND_BUCKET_NAME
        --custom-response-header='HEADER_NAME:[HEADER_VALUE]'
    

Example with `X-Frame-Options` header:
    
    
    gcloud compute backend-buckets update gaming-lab \
        --custom-response-header='X-Frame-Options: DENY'
    

Example with `Strict-Transport-Security` header:

The following example shows you how to add a custom response header to support HTTP Strict Transport Security (HSTS):
    
    
    gcloud compute backend-services update customer-bs-name \
        --global \
        --custom-response-header='Strict-Transport-Security: max-age=63072000'
    

### API

For backend buckets, use the [`Method: backendBuckets.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/insert) or [`Method: backendBuckets.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update) API call.

For backend services, use the [`Method: backendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or [`Method: backendServices.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.

Use one of the following API calls:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET_NAME
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME
    

Add the following snippet to the JSON request body:
    
    
    "customResponseHeaders":HEADER_NAME:[HEADER_VALUE]
    

###  Terraform 

For a Terraform script that creates a load balancer with custom headers, see [Terraform examples for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples#mig-and-custom-headers). 

### Set response headers for Cloud Storage

If you need to set HTTP headers on responses from Cloud Storage—such as Cross-Origin Resource Policy, `X-Frame-Options`, or `X-XSS-Protection` headers—Google Cloud offers the option to use custom headers for Cloud CDN with Cloud Storage. You can do this by configuring custom headers at the load balancer backend bucket level, as described on this page.

Custom response headers configured at the backend bucket level are only added to responses if the client request is sent to the load balancer IP address. Custom headers are not added to responses if the client's request was made directly to the Cloud Storage API.

## Use custom headers with Google Cloud Armor

When you configure a Cloud Armor security policy, you can configure Cloud Armor to insert a custom header and value. If your Cloud Armor security policy is configured to insert the same custom header name as your global external Application Load Balancer or classic Application Load Balancer's custom headers, then the header value specified in your Cloud Armor security policy is overwritten by the value populated by the load balancer. If you don't want the Cloud Armor policy to be overwritten, ensure that you don't use the same name.

## Limitations

The following limitations apply to custom headers used with global load balancers:

  * The total size of all custom request headers (name and value combined, before variable expansion) for each backend service must not exceed 8 KB or 16 request headers.
  * The total size of all custom response headers (name and value combined, before variable expansion) for each backend service must not exceed 8 KB or 16 response headers.



## What's next

  * For an example use case, see [Configuring a load balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-external-backend-internet-neg).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
