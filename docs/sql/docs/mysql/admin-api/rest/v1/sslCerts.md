---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/
title: REST Resource: sslCerts \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:58.541781+00:00
---

# REST Resource: sslCerts  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  REST Resource: sslCerts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SslCert
    * JSON representation
  * Methods



## Resource: SslCert

SslCerts Resource

JSON representation  
---  
      
    
    {
      "kind": string,
      "certSerialNumber": string,
      "cert": string,
      "createTime": string,
      "commonName": string,
      "expirationTime": string,
      "sha1Fingerprint": string,
      "instance": string,
      "selfLink": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#sslCert`.  
`certSerialNumber` |  `string` Serial number, as extracted from the certificate.  
`cert` |  `string` PEM representation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commonName` |  `string` User supplied name. Constrained to [a-zA-Z.-_ ]+.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sha1Fingerprint` |  `string` Sha1 Fingerprint.  
`instance` |  `string` Name of the database instance.  
`selfLink` |  `string` The URI of this resource.  
  
## Methods  
  
---  
  
### `[createEphemeral](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/createEphemeral)`

|  Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance.  
  
### `[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/delete)`

|  Deletes the SSL certificate.  
  
### `[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/get)`

|  Retrieves a particular SSL certificate.  
  
### `[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/insert)`

|  Creates an SSL certificate and returns it along with the private key and server certificate authority.  
  
### `[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/list)`

|  Lists all of the current SSL certificates for the instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
