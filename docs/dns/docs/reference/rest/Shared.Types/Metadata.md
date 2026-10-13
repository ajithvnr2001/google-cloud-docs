---
url: https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/Metadata/
title: Metadata \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:31.875204+00:00
---

# Metadata  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/Metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Metadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UserKey
    * JSON representation



Metadata of a message or a chunk of a message.

JSON representation  
---  
      
    
    {
      "userKey": {
        object ([UserKey](https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/Metadata#UserKey))
      },
      "userAgent": string,
      "clientIp": string,
      "timestampMicros": string,
      "headerOrder": string,
      "deviceIdHash": string,
      "networkId": string,
      "os": string,
      "oauthTokenTimestampMicros": string,
      "source": string
    }  
  
Fields  
---  
`userKey` |  `object (`[UserKey](https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/Metadata#UserKey)`)`  
`userAgent` |  `string`  
`clientIp` |  `string` IP address where the message is created/updated. dot-decimal notation is expected, such as 100.2.3.4.  
`timestampMicros` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The time when the user created the current version of the content. In other words, the last time this content is modified by the user. Note: a client should try its best to fill this field whenever a content is sent to AbuseIAm, both in ClassifyMessage RPC and as a response to RetrieveMessage RPC.  
`headerOrder` |  `string` Header order of the http request from client. The header order is a string where each character in the string is an abbreviation of a field name in the header of the http request, and the ordering of these characters represents the ordering of the fields within the request. With each request the set of fields and their ordering within the request may change. Header order field abbreviations and names: A accept C cookie E accept-encoding F x-forwarded-for H host I if-modified-since K keep-alive L accept-language N connection R referer S accept-charset U user-agent V via Example header order: ARLEUHNKCThis is an optional field that is send to AbuseIAm to help fighting spam. Details about the header order is here: [https://cs.corp.google.com/p#google3/logs/gws/gwslog.proto&q=headerorder&l=1175](https://cs.corp.google.com/p#google3/logs/gws/gwslog.proto&q=headerorder&l=1175)  
`deviceIdHash` |  `string` Mobile Device ID. One way hash is required. The device id is expected to be a hex encoded MD5 hash of the actual device id.  
`networkId` |  `string` Mobile Network ID - Identifies the network the mobile device is operating on.  
`os` |  `string` Contains the operating system of the client. Typically used by mobile clients to specific the mobile OS.  
`oauthTokenTimestampMicros` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Timestamp(in micros) at which the last OAuth Token was issued. This will be used by content that comes from APIs and will typically be used to prevent replay attacks.  
`source` |  `string` Where does the request come from? e.g. gmail, webspam, aol, etc. The source is a unique identifier for a service that calls AbuseIAm.  
  
## UserKey

All users are identified by a user (service, id) tuple. The service field is used to guarantee uniqueness over services. It is essentially the same proto defined in kansas/rpc/client.proto, but proto2 cannot depend on proto1 in proto_library.

For gaia user, the id shall be a hex value. More info is available at: <https://sites.google.com/a/google.com/kansas/Home/kansas-client-documentation/kansas-developers-guide> Note that we prefer hex without prefix padding of 0s, such as f48eaa2, instead of 000000000f48eaa2.

JSON representation  
---  
      
    
    {
      "service": string,
      "id": string
    }  
  
Fields  
---  
`service` |  `string`  
`id` |  `string`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
