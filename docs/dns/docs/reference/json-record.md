---
url: https://docs.cloud.google.com/dns/docs/reference/json-record/
title: Records format (JSON) \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:16.829823+00:00
---

# Records format (JSON)  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/json-record/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Records format (JSON) Stay organized with collections  Save and categorize content based on your preferences. 

This page shows the JSON formats for various Cloud DNS record types. To get started using Cloud DNS, see the [Quickstart](https://docs.cloud.google.com/dns/quickstart). To manage your DNS records, use the [ResourceRecordSets API](https://docs.cloud.google.com/dns/docs/reference/v1beta2/resourceRecordSets).

## Supported DNS record types

Cloud DNS supports the following types of records:

Record type | Description  
---|---  
`A` |  Address record, which is used to map a host name to an IPv4 address.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
          "1.2.3.4"
      ],
      "ttl": 86400,
      "type": "A"
    }  
  
`AAAA` |  IPv6 Address record, which is used to map a host name to an IPv6 address.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
          "2607:f8b0:400a:801::1005"
      ],
      "ttl": 86400,
      "type": "AAAA"
    }  
  
`CNAME` |  Canonical name record, which is used to alias names.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "mail.example.com.",
      "rrdatas": [
          "example.com."
      ],
      "ttl": 86400,
      "type": "CNAME"
    }

Note that the hostnames must end with periods or trailing dots (`.`) in the `rrdatas` fields to be fully-qualified DNS names.   
`MX` |  Mail exchange record, which is used in routing requests to mail servers.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
          "10 mail.example.com.",
          "20 mail2.example.com."
      ],
      "ttl": 86400,
      "type": "MX"
    }

Note that the hostnames must end with periods or trailing dots (`.`) in the `rrdatas` fields to be fully-qualified DNS names.   
`NAPTR` |  Naming authority pointer record, defined by [ RFC 3403](http://tools.ietf.org/html/rfc3403).  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "2.1.2.1.5.5.5.0.7.7.1.e164.arpa.",
      "rrdatas": [
          "100 10 \"u\" \"sip+E2U\" \"!^.*$!sip:information@foo.se!i\" .",
          "102 10 \"u\" \"smtp+E2U\" \"!^.*$!mailto:information@foo.se!i\" ."
      ],
      "ttl": 300,
      "type": "NAPTR"
    }

Note that the value in the final `replacement` field of each `rrdatas` must end with a period or trailing dot (`.`) to be a fully-qualified DNS name.  This record type raises several escaping issues. Embedded quotes must be escaped for use in JSON as demonstrated earlier. Also, the `regexp` field frequently contains backslash characters, and these must be double-escaped: once as required by the zone file format and again as required by the JSON format. To demonstrate, the [example from RFC 3403 section 6.1](http://tools.ietf.org/html/rfc3403#section-6.1) would be represented in the JSON API as: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "cid.urn.arpa.",
      "rrdatas": [
          "100 10 \"\" \"\" \"!^urn:cid:.+@([^\\\\.]+\\\\.)(.*)$!\\\\2!i\" ."
      ],
      "ttl": 300,
      "type": "NAPTR"
    }  
  
`NS` |  Name server record, which delegates a DNS zone to an authoritative server.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
          "ns-cloud1.googledomains.com."
      ],
      "ttl": 86400,
      "type": "NS"
    }

Note that the hostnames must end with periods or trailing dots (`.`) in the `rrdatas` fields to be fully-qualified DNS names.   
`PTR` |  Pointer record, which is often used for reverse DNS lookups.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "2.1.0.10.in-addr.arpa.",
      "rrdatas": [
        "server.example.com."
      ],
      "ttl": 60,
      "type": "PTR"
    }

Creates a mapping from the address `10.0.1.2` to the host name `server.example.com`, which could be defined in the [managed zone](https://docs.cloud.google.com/dns/zones) named `0.10.in-addr.arpa`.   
`SOA` |  Start of authority record, which specifies authoritative information about a DNS zone. An `SOA` resource record is created for you when you create your managed zone. You can modify the record as needed.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
        "ns-cloud1.googledomains.com. dns-admin.google.com. 1 21600 3600 1209600 300"
      ],
      "ttl": 21600,
      "type": "SOA"
    }

Note that the hostnames must end with periods or trailing dots (`.`) in the `rrdatas` fields to be fully-qualified DNS names.   
`SPF` |  Sender policy framework record, which is used in email validation systems.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
        "v=spf1 mx:example.com -all"
      ],
      "ttl": 21600,
      "type": "SPF"
    }  
  
`SRV` |  Service locator record, which is used by some voice over IP, instant messaging protocols, and other applications.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "sip.example.com.",
      "rrdatas": [
        "0 5 5060 sip.example.com."
      ],
      "ttl": 21600,
      "type": "SRV"
    }

Note that the hostnames must end with periods or trailing dots (`.`) in the `rrdatas` fields to be fully-qualified DNS names.   
`TXT` |  Text record, which can contain arbitrary text and can also be used to define machine-readable data, such as security or abuse prevention information.  Example of the resource record set representation: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
        "google-site-verification=xxxxxxxxxxxxYYYYYYXXX"
      ],
      "ttl": 21600,
      "type": "TXT"
    }

The `TXT` record consists of a list of character strings ([RFC 1035](http://www.ietf.org/rfc/rfc1035.txt)). In zone file format, you write this as a sequence of white space separated strings. Each string can be quoted or unquoted. If one of your strings contains embedded white space, you must use the quoted form, for example: 
    
    
    {
      "kind": "dns#resourceRecordSet",
      "name": "example.com.",
      "rrdatas": [
        "\"v=spf1 include:_spf.google.com ~all\""
      ],
      "ttl": 21600,
      "type": "TXT"
    }

The preceding resource record set consists of a single `TXT` resource record that contains a single character string with embedded spaces.   
  
## Wildcard DNS records

Wildcard records are supported for all record types, except for `NS` records. For example, you might want to map all subdomains to the IP address `1.2.3.4` with the following `Change` request:
    
    
    {
    "additions": [
        {
          "kind": "dns#resourceRecordSet",
          "name": "*.example.com.",
          "rrdatas": [
            "1.2.3.4"
           ],
           "ttl": 21600,
           "type": "A"
        }
    ]
    }

## What's next

  * To learn how to use these formats, see [Managing records](https://docs.cloud.google.com/dns/docs/records).
  * To see how these formats fit into the overall framework, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
