---
url: https://docs.cloud.google.com/service-extensions/docs/attributes/
title: Supported attributes \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:37.939906+00:00
---

# Supported attributes  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Reference ](https://docs.cloud.google.com/service-extensions/docs/apis)



Send feedback 

#  Supported attributes Stay organized with collections  Save and categorize content based on your preferences. 

When configuring extensions by using plugins or callouts for `ext-proc`-based backend services, you can specify the request and connection attributes to forward to those services. This page describes the supported attributes and specifies which ones are available for each extension type.

By configuring extensions to forward specific attributes, you can achieve the following:

  * Make dynamic routing decisions.
  * Enrich request headers with client information.
  * Implement custom security policies based on client location or TLS parameters.
  * Generate detailed custom logs.



You can specify attributes with the `forwardAttributes` field in the YAML configuration for plugin and callout extensions. For example, for traffic extensions, see [Configure a traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions).

Specifying attributes with `forwardAttributes` is supported for authorization, edge, route, and traffic extensions. You can implement `forwardAttributes` by using either Wasm plugins or callouts (with the [`ext_proc`](https://github.com/envoyproxy/envoy/blob/main/api/envoy/service/ext_proc/v3/external_processor.proto) protocol) on the following products:

  * Regional external Application Load Balancers
  * Regional internal Application Load Balancers
  * Global external Application Load Balancers
  * Cross-region internal Application Load Balancers



The following table lists the supported attributes and the extensions:

Attribute | Description | Extensions  
---|---|---  
`request.origin` | The value of the origin header in a request for Cross-Origin Resource Sharing (CORS) use cases. | traffic  
`request.method` | The HTTP request method, such as `GET` or `POST`. | authorization, edge, route, traffic  
`request.mcp_method` | The HTTP request method, such as `GET` or `POST`. | authorization  
`request.host` | A convenience equivalent to `request.headers['host']`. | authorization, edge, route, traffic  
`request.path` | The requested HTTP URL path. | authorization, edge, route, traffic  
`request.query` | The HTTP URL query, in the format `name1=value&name2=value2`, as it appears in the first line of the HTTP request. No decoding is performed. | authorization, edge, route, traffic  
`request.scheme` | The HTTP URL scheme, such as `HTTP` or `HTTPS`. Values for this attribute are in lowercase. | authorization, edge, route, traffic  
`request.backend_service_name` | The backend service to which the request is forwarded. | authorization, traffic  
`request.backend_service_project_number` | When using Shared VPC, the project number of the backend service to which the request is forwarded. | authorization, traffic  
`request.mcp_param` | The MCP parameter. | authorization  
`request.user_agent_family` | The client's browser type, derived from `User-Agent` header values. These values refer to the raw text string that incoming HTTP clients (such as web browsers, mobile apps, or automated tools) send in the standard HTTP `User-Agent` request header. | edge, traffic (only for global external Application Load Balancers and regional external Application Load Balancers)  
`request.device_request_type` | The device type of the client. The possible values for this attribute can be `APPLE`, `APPLEWEBKIT`, `BLACKBERRY`, `DOCOMO`, `GECKO`, `GOOGLE`, `KHTML`, `KOREAN`, `MICROSOFT`, `MSIE`, `NETFRONT`, `NOKIA`, `OBIGO`, `OPERA`, `OPENWAVE`, `OTHER`, `POLARIS`, `SEMC`, `SMIT`, `TELECA`, or `USER_DEFINED`. | edge, traffic (only for global external Application Load Balancers and regional external Application Load Balancers)  
`request.header_order` | The order of HTTP headers in the client request as a comma-separated string of header names—for example, `host,accept,cookie`. This attribute supports the following headers: `accept`, `accept-charset`, `accept-encoding`, `accept-language`, `connection`, `content-length`, `content-type`, `cookie`, `host`, `if-modified-since`, `ping-from`, `ping-to`, `pragma`, `referer`, `user-agent`, `via`, and `x-forwarded-for`. | traffic (only for global external Application Load Balancers)  
`response.cdn_cache_id` | The location code and ID of the cache instance that's used to serve the request. This is the same value that's populated in the `jsonPayload.cacheId` field of Cloud CDN request logs.  | traffic (only for global external Application Load Balancers)  
`response.cdn_cache_status` | The current status of the cache instance that's used to serve the request. The possible values for this attribute can be `hit`, `miss`, `revalidated`, `stale`, `uncacheable`, or `disabled`. | traffic (only for global external Application Load Balancers)  
`source.ip` | The client's IP address. | edge, route, traffic  
`source.port` | The client's source port. | edge, route, traffic  
`source.client_region` | The country or region associated with the client's IP address. The value is a Unicode CLDR region code, such as `US` or `FR`. For most countries, these codes correspond directly to ISO-3166-2 codes. | edge, traffic (only for global external Application Load Balancers and regional external Application Load Balancers)  
`source.client_region_subdivision` | The subdivision (for example, a province or state) of the country associated with the client's IP address. This is a Unicode CLDR subdivision ID, such as `USCA` or `CAON`. These Unicode codes are derived from the subdivisions defined by the ISO-3166-2 standard. | edge, traffic (only for global external Application Load Balancers)  
`source.client_city` | The name of the city from which the request originated. For example, `Mountain View` for Mountain View, California. There is no canonical list of valid values for this variable. City names can contain US-ASCII letters, numbers, spaces, and the following characters: `!#$%&'*+-.^_`|~`. | edge, traffic (only for global external Application Load Balancers)  
`source.client_city_lat_long` | The latitude and longitude of the city from which the request originated—for example, `37.386051,-122.083851` for a request from Mountain View. | edge, traffic (only for global external Application Load Balancers)  
`connection.client_encrypted` | The value is `true` if the connection between the client and the load balancer is encrypted (by using `HTTPS`, `HTTP/2`, or `HTTP/3`); otherwise, it is `false`. | traffic  
`connection.client_rtt_msec` | The estimated round-trip transmission time between the load balancer and the HTTP(S) client, in milliseconds. This is the smoothed round-trip time (SRTT) parameter (as defined in RFC 2988) that the load balancer's TCP stack measures. | traffic (only for global external Application Load Balancers)  
`connection.client_protocol` | The HTTP protocol used for communication between the client and the load balancer. It can be one of `HTTP/1.0`, `HTTP/1.1`, `HTTP/2`, or `HTTP/3`. | traffic  
`connection.server_ip_address` | The IP address of the load balancer that the client connects to. This value can be useful when multiple load balancers share common backends. This is the same as the last IP address in the `X-Forwarded-For` header. | traffic  
`connection.server_port` | The destination port number that the client connects to. | traffic  
`connection.sni` | Server Name Indication (as defined in RFC 6066), if provided by the client during the TLS or QUIC handshake. The hostname is converted to lowercase and any trailing dot is removed. | authorization, edge, traffic  
`connection.tls_version` | The TLS version negotiated between the client and the load balancer during the SSL handshake. Possible values include: `TLSv1`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`. If the client connects using QUIC instead of TLS, the value is `QUIC`. | edge, traffic  
`connection.sha256_peer_certificate_digest` | The hexadecimal-encoded SHA256 hash of the peer certificate in the downstream TLS connection, if present. | authorization, edge, traffic  
`connection.tls_cipher_suite` | The cipher suite negotiated during the TLS handshake. The value is four hexadecimal digits defined by the IANA TLS Cipher Suite Registry—for example, `009C` for `TLS_RSA_WITH_AES_128_GCM_SHA256`. This value is empty for QUIC and unencrypted client connections. | traffic  
`connection.tls_ja3_fingerprint` | The JA3 TLS/SSL fingerprint if the client connects using `HTTPS`, `HTTP/2`, or `HTTP/3`. | traffic  
`connection.tls_ja4_fingerprint` | The JA4 TLS/SSL fingerprint if the client connects using `HTTPS`, `HTTP/2`, or `HTTP/3`. | edge, traffic  
`connection.client_cert_present` | The value is `true` if the client provided a certificate during the TLS handshake; otherwise, `false`. | authorization, traffic  
`connection.client_cert_chain_verified` | The value is `true` if the client certificate chain is verified against a configured `TrustStore`; otherwise, it is `false`. | authorization, traffic  
`connection.client_cert_error` | Predefined strings representing error conditions. For more information about the error strings, see [mTLS client validation modes](https://docs.cloud.google.com/load-balancing/docs/mtls#mtls_errors). | authorization, traffic  
`connection.client_cert_serial_number` | The serial number of the client certificate. If the serial number is longer than 50 bytes, the `client_cert_error` is set to `client_cert_serial_number_exceeded_size_limit`, and the serial number is set to an empty string. | authorization, traffic  
`connection.client_cert_spiffe_id` | The SPIFFE ID from the Subject Alternative Name (SAN) field. If the value is not valid or exceeds 2048 bytes, the SPIFFE ID is set to an empty string. If the SPIFFE ID is longer than 2048 bytes, the `client_cert_error` is set to `client_cert_spiffe_id_exceeded_size_limit`. | authorization, traffic  
`connection.client_cert_uri_sans` | A comma-separated, Base64-encoded list of the SAN extensions of type `URI`. The SAN extensions are extracted from the client certificate. The SPIFFE ID is not included in the `client_cert_uri_sans` field. If `client_cert_uri_sans` is longer than 512 bytes, the `client_cert_error` is set to `client_cert_uri_sans_exceeded_size_limit`, and the comma-separated list is set to an empty string. | authorization, traffic  
`connection.client_cert_dnsname_sans` | A comma-separated, Base64-encoded list of the SAN extensions of type `DNSName`. The SAN extensions are extracted from the client certificate. If `client_cert_dnsname_sans` is longer than 512 bytes, the `client_cert_error` is set to `client_cert_dnsname_sans_exceeded_size_limit`, and the comma-separated list is set to an empty string. | authorization, traffic  
`connection.client_cert_valid_not_before` | The timestamp (RFC 3339 date string format) before which the client certificate is not valid—for example, `2022-07-01T18:05:09+00:00`.  | authorization, traffic  
`connection.client_cert_valid_not_after` | The timestamp (in the RFC 3339 date string format) after which the client certificate is not valid—for example, `2022-07-01T18:05:09+00:00`.  | authorization, traffic  
`connection.client_cert_issuer_dn` | The Base64-encoded DER encoding of the full `Issuer` field from the certificate. If `client_cert_issuer_dn` is longer than 512 bytes, the string `client_cert_issuer_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_issuer_dn` is set to an empty string. | authorization, traffic  
`connection.client_cert_subject_dn` | The Base64-encoded DER encoding of the full `Subject` field from the certificate. If `client_cert_subject_dn` is longer than 512 bytes, the string `client_cert_subject_dn_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_subject_dn` is set to an empty string. | authorization, traffic  
`connection.client_cert_leaf` | The client leaf certificate for an established mTLS connection where the certificate passed validation. Certificate encoding is compliant with RFC 9440. This means that the binary DER certificate is Base64-encoded and delimited with colons on either side. If `client_cert_leaf` exceeds 16 KB unencoded, the string `client_cert_validated_leaf_exceeded_size_limit` is added to `client_cert_error` and `client_cert_leaf` is set to an empty string. | authorization, traffic  
`connection.client_cert_chain` | The comma-delimited list of certificates, in standard TLS order, of the client certificate chain for an established mTLS connection where the client certificate passed validation, not including the leaf certificate. Certificate encoding is compliant with RFC 9440. If the combined size of `client_cert_leaf` and `client_cert_chain` before Base64 encoding exceeds 16 KB, the string `client_cert_validated_chain_exceeded_size_limit` is added to `client_cert_error`, and `client_cert_chain` is set to an empty string. | authorization, traffic  
  
## Limitations

  * **Attribute availability** : not all attributes are supported for all extension types. For more information, see the table on this page.

  * **Required configuration** : to send attributes to the extension, you must explicitly list the attributes in the `forwardAttributes` field of your extension configuration. If you don't list an attribute in this field, then the load balancer doesn't forward that specific attribute to your extension.

  * **Size limits** : you can configure a maximum of 16 attributes for a single extension.

  * **mTLS attributes** : client certificate attributes (`connection.client_cert_*`) are populated in the data passed to your extension only if you have enabled mTLS and the client presents a certificate.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
