---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys/
title: REST Resource: dnsKeys \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:17.231550+00:00
---

# REST Resource: dnsKeys  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: dnsKeys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DnsKey
    * JSON representation
    * Digest
      * JSON representation
    * DigestType
  * Methods



## Resource: DnsKey

A DNSSEC key pair.

JSON representation  
---  
      
    
    {
      "id": string,
      "algorithm": enum ([Algorithm](https://docs.cloud.google.com/dns/docs/reference/rest/v1/Algorithm)),
      "keyLength": integer,
      "publicKey": string,
      "creationTime": string,
      "isActive": boolean,
      "type": enum ([KeyType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/KeyType)),
      "keyTag": integer,
      "digests": [
        {
          object ([Digest](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys#DnsKey.Digest))
        }
      ],
      "description": string,
      "kind": string
    }  
  
Fields  
---  
`id` |  `string` Unique identifier for the resource; defined by the server (output only).  
`algorithm` |  `enum (`[Algorithm](https://docs.cloud.google.com/dns/docs/reference/rest/v1/Algorithm)`)` String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time.  
`keyLength` |  `integer` Length of the key in bits. Specified at creation time, and then immutable.  
`publicKey` |  `string` Base64 encoded public half of this key. Output only.  
`creationTime` |  `string` The time that this resource was created in the control plane. This is in RFC3339 text format. Output only.  
`isActive` |  `boolean` Active keys are used to sign subsequent changes to the ManagedZone. Inactive keys are still present as DNSKEY Resource Records for the use of resolvers validating existing signatures.  
`type` |  `enum (`[KeyType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/KeyType)`)` One of "KEY_SIGNING" or "ZONE_SIGNING". Keys of type KEY_SIGNING have the Secure Entry Point flag set and, when active, are used to sign only resource record sets of type DNSKEY. Otherwise, the Secure Entry Point flag is cleared, and this key is used to sign only resource record sets of other types. Immutable after creation time.  
`keyTag` |  `integer` The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B. Output only.  
`digests[]` |  `object (`[Digest](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys#DnsKey.Digest)`)` Cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Output only.  
`description` |  `string` A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the resource's function.  
`kind` |  `string`  
  
### Digest

JSON representation  
---  
      
    
    {
      "type": enum ([DigestType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys#DnsKey.DigestType)),
      "digest": string
    }  
  
Fields  
---  
`type` |  `enum (`[DigestType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys#DnsKey.DigestType)`)` Specifies the algorithm used to calculate this digest.  
`digest` |  `string` The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.  
  
### DigestType

Enums  
---  
`sha1` |   
`sha256` |   
`sha384` |   
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys/get)`

|  Fetches the representation of an existing DnsKey.  
  
### `[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys/list)`

|  Enumerates DnsKeys to a ResourceRecordSet collection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
