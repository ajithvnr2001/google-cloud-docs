---
url: https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-regional/
title: Create custom headers in URL maps \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:40.985535+00:00
---

# Create custom headers in URL maps  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-regional/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Create custom headers in URL maps Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how custom headers work in URL maps used by regional external Application Load Balancers.

Custom request and response headers let you specify additional headers that the load balancer can add to HTTP(S) requests and responses. Depending on the information that the load balancer detects, these headers can include the following information:

  * Latency to the client
  * Parameters of the TLS connection 

  * Geographic location of the client's IP address 


**Important:** Global external Application Load Balancers support header transformations in the [URL map](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#request-response-headers) as well as in the [backend service](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global). However, the regional external Application Load Balancers only support header transformations in URL maps.

## Before you begin

If necessary, update to the latest version of the Google Cloud CLI:
    
    
    gcloud components update
    

## How custom headers work

Custom headers work as follows:

  * When the load balancer makes a request to the backend, the load balancer adds request headers.

The load balancer adds custom request headers only to the client requests, not to the health check probes. If your backend requires a specific header for authorization that is missing from the health check packet, the health check might fail.

  * The load balancer sets response headers before returning a response to the client.




To enable custom headers for regional external Application Load Balancers, you specify a list of header names and header values in the URL map configuration file.

**Header names** must have the following properties:

  * The header name must be a valid HTTP header-field name definition per [RFC 7230](https://tools.ietf.org/html/rfc7230).
  * The header name must not be `X-User-IP`.
  * The header name must not begin with `X-Google`, `X-Goog-`, `X-GFE`, or `X-Amz-`.
  * The following hop-by-hop headers must not be used: `Keep-Alive`, `Transfer-Encoding`, `TE`, `Connection`, `Trailer`, and `Upgrade`. In accordance with [RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616#page-92), these headers are not stored by caches or propagated by the target proxies.
  * The header name must not be `Host` or `authority`. Both `Host` and `authority` are special keywords reserved by Google Cloud. You can't modify these headers for Envoy-based load balancers. Instead, we recommend that you create other custom headers (for example, `MyHost`) so that you don't interfere with the reserved header names.
  * A header name must not appear more than once in the list of headers.



Header names are case-insensitive. When header names are passed to an HTTP/2 backend, the HTTP/2 protocol encodes header names as lowercase.

**Header values** must have the following properties:

  * The header value must be a valid HTTP header field definition per [RFC 7230](https://tools.ietf.org/html/rfc7230), with obsolete forms disallowed.
  * The header value can't be blank. Blank headers are rejected.
  * The header value can include one or more variables, enclosed by curly braces, that expand to values that the load balancer provides. For a complete list of variables allowed in the header value, see Variables that can appear in the header value.



In header values, leading whitespace and trailing whitespace are insignificant and are not passed to the backend. To allow for curly braces in header values, the load balancer interprets two opening curly braces (`{{`) as a single opening brace (`{`), and two closing curly braces (`}}`) as a single closing brace (`}`).

## Add request or response headers

To add request or response headers, use the gcloud CLI to edit the URL map as follows:

**Note:** If you are using the Google Cloud console to add the request and response headers in the URL map, you need to enter the host address in the **Hosts** field and the path matcher section of the following YAML in the **Path matcher** field.

### Regional
    
    
        gcloud compute url-maps edit URL_MAP_NAME \
            --region=REGION
        

The following is a sample YAML file that shows you how to use variables in custom headers:
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: URL_MAP_NAME
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
                   headerAction:
                     requestHeadersToAdd:
                     - headerName: X-header-1-client-region
                       headerValue: "{client_region}"
                     - headerName: X-header-2-client-ip-port
                       headerValue: "{client_ip_address}, {client_port}"
                       replace: True
                     requestHeadersToRemove:
                     - header-3-name
                     responseHeadersToAdd:
                     - headerName: X-header-4-server-ip-port
                       headerValue: "{server_ip_address}, {server_port}"
                       replace: True
                     responseHeadersToRemove:
                     - header-5-name
                     - header-6-name
        

Note the following behaviors:

  * If a response header with custom variables resolves to an empty string, it is removed.
  * If a request header with custom variables resolves to an empty string, it is retained with an empty string placeholder.
  * If a custom request header includes a custom variable, and an incoming client request also includes the same header, the client request header value will be replaced with the new value provided by the load balancer's custom header.



## Variables that can appear in the header value

The following variables can appear in custom header values.

Variable | Description  
---|---  
`client_region` | The country (or region) associated with the client's IP address. This is a Unicode CLDR region code, such as `US` or `FR`. (For most countries, these codes correspond directly to [ISO-3166-2 codes](https://wikipedia.org/wiki/ISO_3166-1_alpha-2).)   
`client_rtt_msec` | Estimated round-trip transmission time between the load balancer and the HTTP(S) client, in milliseconds. This is the smoothed round-trip time (SRTT) parameter measured by the load balancer's TCP stack, per [RFC 2988](https://tools.ietf.org/html/rfc2988). Smoothed RTT is an algorithm that deals with variations and anomalies that may occur in RTT measurements.  
`client_ip_address` | The client's IP address. This is usually the same as the client IP address that is the next-to-last address in the [`X-Forwarded-For`](https://docs.cloud.google.com/load-balancing/docs/https#x-forwarded-for_header) header, unless the client is using a proxy or the `X-Forwarded-For` header has been tampered with.  
`client_port` | The client's source port.  
`client_encrypted` | `true` if the connection between the client and the load balancer is encrypted (using HTTPS, HTTP/2, or HTTP/3); otherwise, `false`.   
`client_protocol` | The HTTP protocol used for communication between the client and the load balancer. One of `HTTP/1.0`, `HTTP/1.1`, `HTTP/2`, or `HTTP/3`.   
`origin_request_header` | Reflects the value of the `Origin` header in the request for Cross-Origin Resource Sharing (CORS) use cases.   
`server_ip_address` | The IP address of the load balancer that the client connects to. This can be useful when multiple load balancers share common backends. This is the same as the last IP address in the [`X-Forwarded-For`](https://docs.cloud.google.com/load-balancing/docs/https#x-forwarded-for_header) header.   
`server_port` | The destination port number that the client connects to.  
`tls_sni_hostname` | Server name indication (as defined in [RFC 6066](https://tools.ietf.org/html/rfc6066.html)), if provided by the client during the TLS or QUIC handshake. The hostname is converted to lowercase and with any trailing dot removed.   
`tls_version` | TLS version negotiated between client and load balancer during the SSL handshake. Possible values include: `TLSv1`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`. If the client connects using QUIC instead of TLS, the value is `QUIC`.   
`tls_cipher_suite` | Cipher suite negotiated during the TLS handshake. The value is four hex digits defined by the [IANA TLS Cipher Suite Registry](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml), for example, `009C` for TLS_RSA_WITH_AES_128_GCM_SHA256. This value is empty for QUIC and for unencrypted client connections.   
`tls_ja3_fingerprint` | [JA3 TLS/SSL fingerprint](https://github.com/salesforce/ja3) if the client connects using HTTPS, HTTP/2 or HTTP/3.  
`tls_ja4_fingerprint` | [JA4 TLS/SSL fingerprint](https://github.com/FoxIO-LLC/ja4/blob/main/technical_details/JA4.md) if the client connects using HTTPS, HTTP/2 or HTTP/3.  
  
The load balancer expands variables to empty strings when it can't determine their values. For example:

  * TLS parameters when TLS is not in use
  * The `{origin_request_header}` when the request does not include an `Origin` header 

  * Geographic location variables when the IP address's location is unknown 




Geographic values are estimates based on the client's IP address. From time to time, Google updates the data that provides these values in order to improve accuracy and to reflect geographic and political changes. Even if the original `X-Forwarded-For` header contains valid location information, Google estimates client locations by using the source IP address information contained in packets received by the load balancer.

## Mutual TLS custom headers

The following additional header variables are available if mutual TLS (mTLS) is configured on the load balancer's TargetHttpsProxy.

Variable | Description  
---|---  
`client_cert_present` | `true` if the client has provided a certificate during the TLS handshake; otherwise, `false`.   
`client_cert_chain_verified` | `true` if the client certificate chain is verified against a configured `TrustStore`; otherwise, `false`.   
`client_cert_error` | Predefined strings representing the error conditions. For more information about the error strings, see [mTLS client validation modes](https://docs.cloud.google.com/load-balancing/docs/mtls#mtls_errors).   
`client_cert_sha256_fingerprint` | Base64-encoded SHA-256 fingerprint of the client certificate.  
`client_cert_serial_number` | The serial number of the client certificate. If the serial number is longer than 50 bytes, the string `client_cert_serial_number_exceeded_size_limit` is added to `client_cert_error`, and the serial number is set to an empty string.  
`client_cert_spiffe_id` | The [SPIFFE ID](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/#spiffe-id) from the subject alternative name (SAN) field. If the value is not valid or exceeds 2048 bytes, the SPIFFE ID is set to an empty string. If the SPIFFE ID is longer than 2048 bytes, the string `client_cert_spiffe_id_exceeded_size_limit` is added to `client_cert_error`.  
`client_cert_uri_sans` | Comma-separated Base64-encoded list of the SAN extensions of type URI. The SAN extensions are extracted from the client certificate. The SPIFFE ID is not included in the `client_cert_uri_sans` field. If the `client_cert_uri_sans` is longer than 512 bytes, the string `client_cert_uri_sans_exceeded_size_limit` is added to `client_cert_error`, and the comma-separated list is set to an empty string.  
`client_cert_dnsname_sans` | Comma-separated Base64-encoded list of the SAN extensions of type DNSName. The SAN extensions are extracted from the client certificate. If the `client_cert_dnsname_sans` is longer than 512 bytes, the string `client_cert_dnsname_sans_exceeded_size_limit` is added to `client_cert_error`, and the comma-separated list is set to an empty string.  
`client_cert_valid_not_before` | Timestamp ([RFC 3339](https://www.ietf.org/rfc/rfc3339.html#section-5.6) date string format) before which the client certificate is not valid. For example, `2022-07-01T18:05:09+00:00`.   
`client_cert_valid_not_after` | Timestamp ([RFC 3339](https://www.ietf.org/rfc/rfc3339.html#section-5.6) date string format) after which the client certificate is not valid. For example, `2022-07-01T18:05:09+00:00`.   
`client_cert_issuer_dn` | Base64-encoded full Issuer field from the certificate. If the `client_cert_issuer_dn` is longer than 512 bytes, the string `client_cert_issuer_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_issuer_dn` is set to an empty string.  
`client_cert_subject_dn` | Base64-encoded full Subject field from the certificate. If the `client_cert_subject_dn` is longer than 512 bytes, the string `client_cert_subject_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_subject_dn` is set to an empty string.  
`client_cert_leaf` | The client leaf certificate for an established mTLS connection where the certificate passed validation. Certificate encoding is compliant with [RFC 9440](https://datatracker.ietf.org/doc/rfc9440/): the binary DER certificate is encoded using Base64 (without line breaks, spaces, or other characters outside the Base64 alphabet) and delimited with colons on either side. If `client_cert_leaf` exceeds 16 KB unencoded, the string `client_cert_validated_leaf_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_leaf` is set to an empty string.  
`client_cert_chain` | The comma-delimited list of certificates, in standard TLS order, of the client certificate chain for an established mTLS connection where the client certificate passed validation, not including the leaf certificate. Certificate encoding is compliant with [RFC 9440](https://datatracker.ietf.org/doc/rfc9440/). If the combined size of `client_cert_leaf` and `client_cert_chain` before Base64 encoding exceeds 16 KB, the string `client_cert_validated_chain_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_chain` is set to an empty string.  
  
## Limitations

The following limitations apply:

  * You can't configure custom headers on backend services used by regional external Application Load Balancers.


  * The following custom header variables aren't supported with regional external Application Load Balancers:

    * `cdn_cache_id`
    * `cdn_cache_status`
    * `client_region_subdivision`
    * `client_city`
    * `client_city_lat_long`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
