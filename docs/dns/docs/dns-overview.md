---
url: https://docs.cloud.google.com/dns/docs/dns-overview/
title: General DNS overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:34.261138+00:00
---

# General DNS overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/dns-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  General DNS overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Domain Name System (DNS).

For an overview of Cloud DNS, see the [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview). For key terms related to Cloud DNS, see [Key terms](https://docs.cloud.google.com/dns/docs/key-terms).

DNS is a hierarchical distributed database that stores IP addresses and other data and allows queries by name.

In other words, DNS is a directory of readable domain names that translate to numeric IP addresses used by computers to communicate with each other. For example, when you type a URL into a browser, DNS converts the URL into an IP address of a web server associated with that name. The DNS directories are stored and distributed around the world on domain name servers that are updated regularly.

The following concepts are useful when working with DNS.

## DNS server types

A DNS server stores a database of domain names, and then processes domain names based on DNS queries that come from a client in a network.

### Authoritative server

An _authoritative server_ is a server that holds the DNS name records, including A, AAAA, and CNAME.

A _non-authoritative server_ constructs a cache file based on previous queries for domains. It does not hold original name records.

### Recursive resolver

A _recursive resolver_ is the server that sends a query to the authoritative or non-authoritative server for resolution. A recursive resolver is so-called because it performs each query for a given name and returns the final result.

This is in contrast to an _iterative resolver_ , which only returns a referral to the next DNS servers that might have the answer.

For example, when resolving the name `google.com.`, the recursive resolver must determine who is authoritative for `.` (the root zone of DNS). Then it asks those name servers who is authoritative for `.com.`. Finally, it asks those name servers who is authoritative for `google.com.`, and the rdata for the A record is returned to the client.

Following is an example of a recursive resolver in action; if you run `dig +trace google.com`, the recursive resolver performs the following action (8.8.8.8/Google Public DNS is one such resolver):
    
    
     dig +trace google.com
    
    
    
    ; <<>> DiG 9.11.5-P4-5.1-Debian <<>> +trace google.com
    ;; global options: +cmd
    .           168383  IN  NS  a.root-servers.net.
    .           168383  IN  NS  b.root-servers.net.
    .           168383  IN  NS  c.root-servers.net.
    .           168383  IN  NS  d.root-servers.net.
    .           168383  IN  NS  e.root-servers.net.
    .           168383  IN  NS  f.root-servers.net.
    .           168383  IN  NS  g.root-servers.net.
    .           168383  IN  NS  h.root-servers.net.
    .           168383  IN  NS  i.root-servers.net.
    .           168383  IN  NS  j.root-servers.net.
    .           168383  IN  NS  k.root-servers.net.
    .           168383  IN  NS  l.root-servers.net.
    .           168383  IN  NS  m.root-servers.net.
    .           168383  IN  RRSIG   NS 8 0 518400 20190810170000 20190728160000 59944 .
        ITqCp5bSKwoG1P76GpNfDanh4fXxOtHuld5SJzEm9ez0U/K7kpmBm4TE
        cw82zuqtZlqiGOuq+90KHJEhD1fdX3FujgDqe3kaY/41LgFIo76RBeMP
        CorYg29lKQOBf7pLPiJWewFmnLsRXsvENzxNXl9mynX80EQSS2YlCWpr
        47i2j5SFpGDzmxls7LinB4VvwVLhy0FPwBaVc5NVqQoFS5ZkfKXCUz8x
        urExPT2OtPJeDiGzrQGmT6vDbYZtJRWWGK5tPIKZQyF/08YSJlrjebNa
        1nKZVN8SsO8s7elz6JGmdoM6D/1ByLNFQmKvU55ikaVSnXylqixLbJQI 7LyQoA==
    ;; Received 525 bytes from 127.0.0.1#53(127.0.0.1) in 22 ms
    
    com.            172800  IN  NS  a.gtld-servers.net.
    com.            172800  IN  NS  b.gtld-servers.net.
    com.            172800  IN  NS  c.gtld-servers.net.
    com.            172800  IN  NS  d.gtld-servers.net.
    com.            172800  IN  NS  e.gtld-servers.net.
    com.            172800  IN  NS  f.gtld-servers.net.
    com.            172800  IN  NS  g.gtld-servers.net.
    com.            172800  IN  NS  h.gtld-servers.net.
    com.            172800  IN  NS  i.gtld-servers.net.
    com.            172800  IN  NS  j.gtld-servers.net.
    com.            172800  IN  NS  k.gtld-servers.net.
    com.            172800  IN  NS  l.gtld-servers.net.
    com.            172800  IN  NS  m.gtld-servers.net.
    com.            86400   IN  DS  30909 8 2
        E2D3C916F6DEEAC73294E8268FB5885044A833FC5459588F4A9184CF C41A5766
    com.            86400   IN  RRSIG   DS 8 1 86400 20190811170000 20190729160000 59944 .
        KXPRdZspxd6hZYRFx3cj7Yp3d6HDzOG5CmoK46ZrrlKnZkCYMPKzyFQ2
        15pA+jZ37MbQbhe6+S+C4AHWqv95DDsue85ha3ZmWGhnJxcLnDaL5Twp
        Z/W/a+1cTHhhbMZua1riw74mqvzRAF1kVerj7jrvWnOAOZCh69Dr4AFJ
        gRN4MAn+wCZDmPQCtkcGVJ9vyNV7Xra45B4ISqEo0xi8CXewp9cc+aW5
        TSjFRhj1RM9d3k+3Mrq6AAV8dVgWofYTg6Ihph/SfoIx4TrTrEbgfdsv
        MvuLPXvK6Y7oSh5WknbFduw7HQdo1jH3/QR54FORswBJT8VmYD7Zii88 tAjbRQ==
    ;; Received 1170 bytes from 192.58.128.30#53(j.root-servers.net) in 2 ms
    
    google.com.     172800  IN  NS  ns2.google.com.
    google.com.     172800  IN  NS  ns1.google.com.
    google.com.     172800  IN  NS  ns3.google.com.
    google.com.     172800  IN  NS  ns4.google.com.
        CK0POJMG874LJREF7EFN8430QVIT8BSM.com. 86400 IN NSEC3 1 1 0 -
        CK0Q1GIN43N1ARRC9OSM6QPQR81H5M9A NS SOA RRSIG DNSKEY NSEC3PARAM
        CK0POJMG874LJREF7EFN8430QVIT8BSM.com. 86400 IN RRSIG NSEC3 8 2
        86400 20190803044434 20190727033434 17708 com.
        rMmiNL7bYvJpB3Bc+WnqS2iiczm2PwxBvJcl7SL/vcTj88GsxM1ycTSV
        PsHZHxfrv1dv2C5BCSZ+mzeVBu8upLoeraQy+UVf3VXyt3i3rNGzcXYV
        8HSrHcXrRoAJopFim3Ge1xdZ+uERg3cTIcN2tJxxkCeqt/EcUTqtQl8t EAc=
        S84BDVKNH5AGDSI7F5J0O3NPRHU0G7JQ.com. 86400 IN NSEC3 1 1 0 -
        S84CFH3A62N0FJPC5D9IJ2VJR71OGLV5 NS DS RRSIG
        S84BDVKNH5AGDSI7F5J0O3NPRHU0G7JQ.com. 86400 IN RRSIG NSEC3
        8 2 86400 20190804045723 20190728034723 17708 com.
        jypPsaWVop9rzuf70CFYyiK0hliiJ+YYtkjgb3HVj9ICc57kLmv9DkvG
        DddF5GBQpqNEakzyJtya179MAdDT7RhJB4XfmY6fu5I5QTeIjchfP5wt
        7gU1AL7cqTmBAo2RWu62vtUytV09+O3KGFq5O+Cwr11dSTfq1yYyw6YW cMI=
    ;; Received 772 bytes from 192.41.162.30#53(l.gtld-servers.net) in 2 ms
    
    google.com.     300 IN  A   172.217.7.14
    ;; Received 55 bytes from 216.239.32.10#53(ns1.google.com) in 13 ms
    

Each DNS client queries a name server. A recursive resolver queries other name servers, all the way up to a top-level name server, if necessary. The [NS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for a zone on an upper-level name server directs the resolver _down_ to another name server, eventually reaching either a name server that cached the zone or the authoritative server for the zone.

## Zones

### Public zone

A public zone is visible to the internet. You can create DNS records in a public zone to publish your service on the internet. For example, you might create an A record in a public zone called `example.com.` (note the trailing dot) for your public website `www.example.com.`.

### Private zone

A private zone is any zone that cannot be queried over the public internet.

### Delegated subzone

DNS allows the owner of a zone to use NS records to delegate a subdomain to a different name server. Resolvers follow these records and send queries for the subdomain to the target name server specified in the delegation.

For example, you can create separate zones for both `example.com` and `subdomain.example.com`, each with its own authoritative name server. Because `subdomain.example.com` is a child domain of `example.com`, the method to enable the authoritative name server for the subdomain to be located from the parent domain's zone is called delegation. Delegation is essentially a pointer to the authoritative name server for a subdomain. To enable delegation in Cloud DNS, you can add NS records for the subdomains in the zone of the parent domain.

### Split horizon DNS

Split horizon is a term used to describe an instance when two zones, one to be used by the internal network and the other to be used by the external network (usually the internet), are created for the same domain. Split-horizon DNS lets you serve different answers (different resource record sets) for the same name depending on who is asking.

For example, you can provide the development or staging version of your application if the query comes from the development network, and the production or public version of your app if the query comes from the public internet.

## Records

A record is a mapping between a DNS resource and a domain name. Each individual DNS record has a type (name and number), an expiration time (time to live), and type-specific data.

Some of the commonly used record types are:

  * **A:** Address record, which maps host names to their IPv4 address.
  * **AAAA:** IPv6 Address record, which maps host names to their IPv6 address.
  * **CNAME:** Canonical name record, which specifies alias names.
  * **MX:** Mail exchange record, which is used in routing requests to mail servers.
  * **NS:** Name server record, which delegates a DNS zone to an authoritative server.
  * **PTR:** Pointer record, which defines a name associated with an IP address.
  * **SOA:** Start of authority, used to designate the primary name server and administrator responsible for a zone. Each zone hosted on a DNS server must have an SOA (start of authority) record. You can modify the record as needed (for example, you can change the serial number to an arbitrary number to support date-based versioning).



### Record sets

Records with the same name and of the same type but with different data values are called record sets. When you create a record, if a set with the same name and type exists, the record is added to this matching set. If there's no matching set, a new set is created and appended to the list of record sets.

This is an example of a record set with more than one record having the same name and type:

DNS name | Type | TTL (seconds) | Data  
---|---|---|---  
`db-01.dev.gcp.example.com` | A | 50 | `10.128.1.35`  
`db-01.dev.gcp.example.com` | A | 50 | `10.128.1.10`  
  
For a list of supported record types in Cloud DNS, see [Supported DNS record types](https://docs.cloud.google.com/dns/docs/records-overview#supported_dns_record_types).

## Delegation of subdomains

When creating records, make sure that the NS and SOA records match each other. Conflicting NS and SOA records can cause some resolvers to reject the delegation as invalid and refuse to cache `NO DATA` responses to queries. This can result in a large unexpected number of queries against your public managed zones by third-party recursive resolvers when resolvers query your public managed zones for records that don't exist.

For example, suppose that there are two subdomains, `example.com` and `subdomain.example.com` in Cloud DNS. The NS and SOA records for `subdomain.example.com` don't match. Neither of the zones contains any AAAA records. When some third-party recursive resolvers query `subdomain.example.com` for an AAAA record and receive a `NO DATA` response, if the resolvers detect the invalid delegation of `subdomain.example.com`, they refuse to cache the non-existence of AAAA records in that zone. This results in retrying the queries. They query all the Cloud DNS name servers, in turn, for this information.

## Registrar

A domain name registrar is an organization that manages the reservation of internet domain names for public zones. A registrar must be accredited by a generic top-level domain (gTLD) registry or a country code top-level domain (ccTLD) registry. This is how _upper-level_ name servers agree on SOA and update NS records for the zone to direct requests to caching or authoritative name servers.

## SOA serial number

The SOA serial number is a version number for a DNS zone. For all name servers to be current with the version of a zone, they must have the same SOA serial number. The serial numbers of SOA records created in DNS managed zones [monotonically](https://wikipedia.org/wiki/Monotonic_function) increase with each transactional change to a zone's record sets.

However, you can change the serial number of an SOA record to an arbitrary number, including an ISO 8601-formatted date, as recommended in [RFC 1912](https://tools.ietf.org/html/rfc1912).

## DNSSEC

The Domain Name System Security Extension (DNSSEC) addresses vulnerabilities to DNS data. DNSSEC is a suite of IETF specifications that provides authentication of DNS data, authenticated denial of existence, and data integrity to DNS clients (resolvers). In short, DNSSEC provides a way for software to verify the origin of DNS data and validate that it has not been modified in transit.

For more details about DNSSEC, see [RFC 4033](https://tools.ietf.org/html/rfc4033).

For a list of general DNS terminology, see [RFC 7719](https://tools.ietf.org/html/rfc7719).

## What's next

  * To get started using Cloud DNS, see [Quickstart: Set up DNS records for a domain name with Cloud DNS](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name).
  * To add, delete, or update records, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).
  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
