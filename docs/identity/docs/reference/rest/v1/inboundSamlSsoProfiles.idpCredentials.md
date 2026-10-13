---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials
title: REST Resource: inboundSamlSsoProfiles.idpCredentials \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:42.007458+00:00
---

# REST Resource: inboundSamlSsoProfiles.idpCredentials  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: inboundSamlSsoProfiles.idpCredentials Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: IdpCredential

Credential for verifying signatures produced by the Identity Provider.

JSON representation  
---  
      
    
    {
      "name": string,
      "updateTime": string,
    
      "rsaKeyInfo": {
        object ([RsaPublicKeyInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#RsaPublicKeyInfo))
      },
      "dsaKeyInfo": {
        object ([DsaPublicKeyInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#DsaPublicKeyInfo))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the credential.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the `IdpCredential` was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `key_info`. Information about the key in the credential, such as its algorithm, key size, etc. `key_info` can be only one of the following:  
`rsaKeyInfo` |  `object (`[RsaPublicKeyInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#RsaPublicKeyInfo)`)` Output only. Information of a RSA public key.  
`dsaKeyInfo` |  `object (`[DsaPublicKeyInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#DsaPublicKeyInfo)`)` Output only. Information of a DSA public key.  
  
## RsaPublicKeyInfo

Information of a RSA public key.

JSON representation  
---  
      
    
    {
      "keySize": integer
    }  
  
Fields  
---  
`keySize` |  `integer` Key size in bits (size of the modulus).  
  
## DsaPublicKeyInfo

Information of a DSA public key.

JSON representation  
---  
      
    
    {
      "keySize": integer
    }  
  
Fields  
---  
`keySize` |  `integer` Key size in bits (size of parameter P).  
  
## Methods  
  
---  
  
### `[add](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/add)`

|  Adds an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/delete)`

|  Deletes an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/get)`

|  Gets an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/list)`

|  Returns a list of `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`s in an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
