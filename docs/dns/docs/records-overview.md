---
url: https://docs.cloud.google.com/dns/docs/records-overview/
title: DNS records overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:38.592476+00:00
---

# DNS records overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/records-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  DNS records overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of records and lists DNS record types that Cloud DNS supports, including the Cloud DNS custom record type ALIAS.

A record is a mapping between a DNS resource and a domain name. Each individual DNS record has a type (name and number), an expiration time (time to live), and type-specific data.

To create and manage resource record sets, see [Add, update, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Alias records

An ALIAS record is a Cloud DNS custom record type that behaves like a CNAME record but can only be used at the zone apex and only responds to address record (A or AAAA) queries. Specifically, the ALIAS record type maps an alias domain name to a canonical name and uses the canonical name to look up the answer. This record type is useful when you need CNAME behavior at the apex. You cannot place a CNAME record at the apex because it cannot exist alongside any other record type, including the SOA record that is required at the zone apex.

ALIAS records are specific to Cloud DNS and are never exposed to an external client querying Cloud DNS zones. For a client, an ALIAS record appears as a standard A or AAAA record in the DNS response. ALIAS records are not compatible with DNSSEC, so you cannot enable DNSSEC on a zone with ALIAS records.

You can manage ALIAS records like all other records. To learn how to manage records, see [Manage records](https://docs.cloud.google.com/dns/docs/records).

### Query resolution process

Alias records are only available for Cloud DNS public zones.

For CNAME records, the resolver is responsible for resolving the canonical name. For ALIAS records, the Cloud DNS name server resolves the canonical name and produces synthesized A or AAAA records to return to the resolver. The synthesized A or AAAA records have the ALIAS record's name with the IP addresses found from resolving the ALIAS record's target. The Cloud DNS name servers use Google's available recursive resolvers to resolve alias records.

If the alias target resolves to a resource record set (RRSet) with multiple addresses, Cloud DNS returns all of the records but randomizes their order before returning the synthesized address record. This process is similar to how Cloud DNS treats answers from its nameservers.

Only address records are synthesized during ALIAS record target resolution. Queries for ALIAS records don't return any intermediary CNAME records that are found while resolving the alias record's target. CNAME records that are found through CNAME chasing before reaching the ALIAS record are returned unmodified. If the ALIAS target resolution fails, that is, returns a response code other than `NOERROR`, the Cloud DNS name server returns a `SERVFAIL` response to its client. If the resolution results in a `NODATA` response, which is a `NOERROR` response with no address records, the Cloud DNS name server returns a `NODATA` response.

When resolving ALIAS record targets, Cloud DNS doesn't use client provided [EDNS Client Subnet](https://en.wikipedia.org/wiki/EDNS_Client_Subnet).

#### Time to live (TTL) parameter and caching

The TTL value returned with a synthesized address record is the smallest of the ALIAS record's configured TTL value and the TTL values that are encountered while resolving the ALIAS target. Using this method, the returned TTL could be less than the ALIAS record's configured TTL, but it's never greater than the configured TTL.

The following example demonstrates how TTL is determined for the synthesized address records.

Suppose that the following records are configured in a Cloud DNS managed zone:
    
    
    example.com.    3600    SOA      ns.com.  admin.example.com. (...)
                    86400   NS       ns.com.
                    6000    ALIAS    test-cname.example.com.
    test-cname      3000    CNAME    address.example.com.
    address         5000    A        1.2.3.4
    

A query to this zone for the A record at `example.com` returns a response similar to the following:
    
    
    QUESTION SECTION
    example.com.                  A
    
    ANSWER SECTION
    example.com.        3000      A      1.2.3.4
    

The TTLs encountered during resolution are 6000 (for the ALIAS record), 3000 (for the CNAME record), and 5000 (for the A record). Of these TTLs, 3000 is the smallest, so it's returned in the synthesized address record.

This example shows all records in the same zone for simplicity, but the TTL logic is identical for resolutions that jump through different zones.

#### Authoritative answer bit

The authoritative bit in the DNS response is based on the first name in the chain (the original `qname`), regardless of whether the data associated with that name is found on the server or was retrieved through an ALIAS record resolution.

### Error handling

To resolve `ALIAS` records, Cloud DNS uses third-party authoritative name servers to determine DNS delegations and retrieve externally hosted DNS data. If Cloud DNS can't resolve an `ALIAS` record target (the `ALIAS` target resolution results in an error `RCODE` value, such as `NXDOMAIN` or `REFUSED`), it returns a `SERVFAIL` response. For example, if the `ALIAS` target doesn't exist or its authoritative servers are unreachable, Cloud DNS returns `SERVFAIL`.

Because `SERVFAIL` provides you with limited information about the error, Cloud DNS logging includes the specific `RCODE` value encountered during `ALIAS` record resolution to help you troubleshoot errors. For information about how to use Cloud DNS logging, see [Use logging and monitoring](https://docs.cloud.google.com/dns/docs/monitoring).

If an `ALIAS` target resolution results in a `NODATA` response (an empty response with a `NOERROR` `RCODE`), Cloud DNS returns `NODATA`. `ALIAS` records match both `A` and `AAAA` queries, but the `ALIAS` target can hold only one record type. This is expected behavior and doesn't result in a response with an error `RCODE` value.

### Import and export records

You can import and export records to and from a BIND zone file or a YAML file.

ALIAS records are not supported in BIND files because the ALIAS record type is not a standard DNS record type. While Cloud DNS recognizes these entries, other BIND-compatible DNS software might not.

ALIAS records are exported to YAML files, specific to Cloud DNS, in the following format:
    
    
    kind: dns#resourceRecordSet
    name: DNS Name
    rrdatas: RR Data
    ttl: TTL
    type: ALIAS
    

Cloud DNS can import ALIAS records from a YAML file in the preceding format.

### Security and privacy

Cloud DNS public name servers resolve the ALIAS target on your behalf, but you must ensure that you have configured the ALIAS target correctly; an incorrect ALIAS target could lead to your public records not working as needed or returning undesired IP addresses. 

### Monitor managed zones

Cloud DNS offers logging for all queries to managed zones through Logging. An optional field `alias_query_response_code` is available in the DNS query log to record information about the status of the ALIAS name resolution, since this information is not available from the DNS response.

For details, see [Viewing logs](https://docs.cloud.google.com/dns/docs/monitoring#viewing_logs).

The `alias_query_response_code` is only set if the query is resolved using an ALIAS record. A value of `NoError` means that the ALIAS record was resolved successfully, while any other value represents the error. A `SERVFAIL` value can represent any of the following issues:

  * Unreachable target nameserver
  * Target resolution timed out before finding a response
  * DNSSEC validation failed



The `qtype` field in the log entries does not have an ALIAS option. If an A or AAAA query is answered using an ALIAS record, the `qtype` field remains as A or AAAA. 

## Supported DNS record types

**Note:** Wildcard DNS records are supported for all record types, except for NS records.

Cloud DNS supports the following types of records.

For record type | Enter  
---|---  
`A` |  The host's numeric IP address, in IPv4 dotted decimal format. The `A` record type maps an IPv4 address to a domain name and determines where the requests for the domain name are directed— for example, `192.0.2.91`.   
`AAAA` |  The host's numeric IP address, in IPv6 hexadecimal format. The `AAAA` (quad A) record type maps an IPv6 address to a domain name and determines where the requests for the domain name are directed—for example, `2001:db8::8bd:1002`.   
`ALIAS` ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) |  Alias record (Preview), which maps an alias domain name to a canonical name at the zone apex. An alias record is also called an ANAME record or CNAME flattening.  You can configure alias records by using the gcloud CLI or the Cloud DNS API. You cannot configure alias records by using the Google Cloud console.  An alias record is also called an ANAME record or CNAME flattening.   
`CAA` |  The certificate authorities that are authorized to issue certificates for this domain—for example, `ca.example.net`.  Create a `CAA` record type to ensure that unauthorized CAs don't issue certificates to your domain.  **Note:** We recommend enabling [_Domain Name System Security Extensions (DNSSEC)_](https://docs.cloud.google.com/dns/docs/dnssec) when using this record type in a public zone. DNSSEC is not enabled by default for zones.   
`CNAME` |  The DNS alias for an `A` record—for example, `ftp.example.com` is a DNS alias to `www.example.com`. In this example, `ftp.example.com` is a service present in the same server as `www.example.com`. Links pointing to ` ftp.example.com` receive the `A` record of `www.example.com`.  You can also use the `CNAME` record type to point to an entirely different domain name—for example, `altostrat.com` is a DNS alias to `www.example.com`.  Sometimes, a name server responds with the `CNAME` record and the `A` record referred to by the CNAME value; this behavior is called [_CNAME chasing_](https://docs.cloud.google.com/dns/docs/cnamechasing).  If you encounter issues while creating a CNAME record, see [ CNAME record defined in a private zone not working ](https://docs.cloud.google.com/dns/docs/troubleshooting#cname-in-private-zone-not-working).   
`DNSKEY` |  The DNSSEC public key that the resolvers use to verify the authenticity of records using ZSK and KSK keys.  For example, `7200 IN DNSKEY 256 3 8 AwEAAarQO0FTE/l6LEKFlZllJIwXuLGd3q5d8S8NH+ntOeIMN81A5wAI`. In this example, `7200` is the TTL, `256` is the decimal representation of `DNSKEY` flags, `3` is the protocol indicator for DNSSEC, and `8` is the RSA/SHA-256 cryptographic algorithm used for the key.  You can only add this record type in a public and DNSSEC-enabled zone that is in the `Transfer` state. For more information, see [Manage DNSSEC configuration](https://docs.cloud.google.com/dns/docs/dnssec-config).  **Note:** If you have enabled DNSSEC for this zone, the Zone Signing Key (ZSK) and Key Signing Key (KSK) are automatically generated. For more information about viewing your `DNSKEY`, see [Displaying current DNSKEYs](https://docs.cloud.google.com/dns/docs/dnskeys#display_current_dnskeys).   
`DS` |  The DNSSEC key fingerprint for a secure delegated zone.  For example, `7200 IN DS 31523 5 1 c8761ba5defc26ac7b78e076d7c47fa9f86b9fba`. In this example, `7200` is the TTL, `31523` is the keytag, `5` is the algorithm, and `1` is the digest type.  You can only add this record type in a public zone. This record type does not activate DNSSEC for a delegated zone unless you enable (and activate) DNSSEC for this zone. DNSSEC is not enabled by default for zones.   
`HTTPS` |  HTTPS Service Binding record, which allows an origin to indicate multiple alternative endpoints, each with associated parameters. This record also redirects HTTP to HTTPS.  For example, `1 . alpn=h2, h3` where `1` is the service priority (SvcPriority) which is `0` for aliases and `1-65535` for service descriptions, `.` is the TargetName ("." if same as the owner name), and `alpn=h2, h3` are the service parameters (SvcParams) consisting of key-value pairs describing the target endpoint, separated by spaces.  The HTTPS record type is based on the more general SVCB record type and uses the same value format.   
`IPSECKEY` |  IPsec tunnel gateway data and public keys for IPsec-capable clients to [enable opportunistic encryption](https://docs.cloud.google.com/dns/docs/dnssec-advanced#ipseckey).  For example, `10 1 2 192.0.2.1 AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt==` where `10` is the precedence with lower values having higher priority, `1` is the gateway type, `2` is the algorithm type, and `192.0.2.1` is the gateway.  For more information, see [RFC 4025](https://datatracker.ietf.org/doc/html/rfc4025).   
`MX` |  A preference number and DNS name of a mail exchange server that receives emails on behalf of your domain.  For example: `1 mail.example.com.` where `1` is the preference number.  SMTP servers prefer servers with lower preference numbers with `0` being the lowest preference number you can enter.  The MX record you enter must end with a dot (`.`). You can create multiple records with different priorities to configure backup mail servers or use the same priority to distribute the load across multiple mail servers.  For example, to direct your email to your Google Workspace account, enter the following: `1 SMTP.GOOGLE.COM.`  
`NAPTR` |  The name authority pointer rules used for mapping Uniform Resource Names (URN) by Dynamic Delegation Discovery System (DDDS) applications. The `NAPTR` record type is used by DDDS applications to convert or replace one value with another to find a URN.  In the example, `100 10 "u" "sip+E2U" "!^.*$!sip:information@example.com!i ."` `100` is the Order in which the NAPTR records must be processed, `10` is the Preference that specifies the processing order when records have equal Order values, `"u"` is a Flag that controls aspects of the rewriting and interpretation of the fields in the record, `""sip+E2U` are Services, and `"!^.*$!sip:information@example.com!i"` is the regular expression (RegEx) that contains a substitution expression which is applied to the original string held by the client in order to construct the next domain lookup. Finally, the `.` is the Replacement which is the next domain name to query for depending on the potential values found in the flags field.  For more information, see [RFC 3403](https://datatracker.ietf.org/doc/html/rfc3403).   
`NS` |  The DNS name of the authoritative name server that provides DNS services for your domain or subdomain. Your `NS` records must match the name servers for your zone—for example, `ns-1.example.com`.  **Note:** A wildcard resource record set of type `NS` is not supported.**Note:** Managed private zones don't support custom resource record sets of type `NS`.  
`PTR` |  The Fully Qualified Domain Name (FQDN) or the canonical name of the domain that maps to an IP address—for example, `server-1.example.com`.  The `PTR` record type is typically used for reverse lookups.   
`SOA` |  Start of authority record, which specifies authoritative information about a DNS zone. An `SOA` record is created for you when you create your managed zone. You can modify the record as needed (for example, you can change the serial number to an arbitrary number to support date-based versioning).  For example, `ns-cloud-c1.googledomains.com. cloud-dns-hostmaster.google.com 1 21600 3600 259200 300` where `ns-cloud-c1.googledomains.com.` is the MNAME, `cloud-dns-hostmaster.google.com` is the RNAME, `1` is the SERIAL, `21600` is the REFRESH, `3600` is RETRY, `259200` is EXPIRE, and `300` is the MINIMUM.  For more information, see [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#section-3.3.13).   
`SPF` |  The `SPF` record type is deprecated. Use `TXT` records starting with `v=spf1` instead. `SPF` type records are not used by modern email software.   
`SRV` |  The data which specifies the location (the hostname and port number) of servers for a particular service.  For example, `0 1 587 mail.example.com` where `0` is the priority of the target host, `1` is the weight, and `587` is the port number.  For more information, see [RFC 2782](https://tools.ietf.org/html/rfc2782).   
`SSHFP` |  SSH fingerprint for SSH clients to [validate the public keys of SSH servers](https://docs.cloud.google.com/dns/docs/dnssec-advanced#sshfp).  For example, `2 1 123456789abcdef67890123456789abcdef67890` where `2` is the SSH server algorithm number, `1` is the fingerprint type number, and `123456789abcdef67890123456789abcdef67890` is the fingerprint.   
`SVCB` |  Service Binding record, which allows a logical service to indicate multiple alternative endpoints, each with associated parameters.  For example, `0 alias-target.example.com` where `0` is the service priority (SvcPriority) which is `0` for aliases and `1-65535` for service descriptions.  For HTTPS origins, see the HTTPS record type.   
`TLSA` |  The DNS-based Authentication of Named Entities (DANE) TLSA Certificate Association information. A [TLSA](https://docs.cloud.google.com/dns/docs/dnssec-advanced#tlsa) record contains information used to validate X.509 certificates (such as certificates used by HTTPS) without depending on one of a preconfigured set of certificate authorities (CAs) signing them.  For example, `1 1 2 92003ba34942dc74152e2f2c408d29ec`. In this example, the first `1` is the protocol indicator for DNSSEC, the second `1` is the public key, and `2` is the RSA/SHA-256 cryptographic algorithm used for the key.  Only use this record type if you have enabled DNSSEC for the zone.   
`TXT` |  Text record, which can contain arbitrary text and can also be used to define machine-readable data, such as security or abuse prevention information.  A TXT record may contain one or more text strings; the maximum length of each [ string is 255 characters](https://tools.ietf.org/html/rfc4408#section-3.1.3). If your record data is more than 255 bytes, divide your record into 255-byte strings and enclose each string in quotation marks—for example, `"String one 255 bytes" "String two 255 bytes"`. Mail agents and other software agents concatenate multiple strings. Enclose each string in quotation marks—for example, ` "Hello world" "Bye world"`.  Each TXT record has a 1000-character limit. If you need to increase this limit, contact [Google Cloud support](https://docs.cloud.google.com/support).   
  
## What's next

  * To get started using Cloud DNS, see [Quickstart: Set up DNS records for a domain name with Cloud DNS](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name).

  * To register and set up your domain, see [Tutorial: Set up a domain by using Cloud DNS](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial).

  * To learn about API client libraries, see [Samples and libraries](https://docs.cloud.google.com/dns/docs/reference/libraries).

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
