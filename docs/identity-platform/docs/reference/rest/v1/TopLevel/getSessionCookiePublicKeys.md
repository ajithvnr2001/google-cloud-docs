---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/TopLevel/getSessionCookiePublicKeys/
title: Method: getSessionCookiePublicKeys \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:14.976894+00:00
---

# Method: getSessionCookiePublicKeys  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/TopLevel/getSessionCookiePublicKeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  Method: getSessionCookiePublicKeys Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
  * Response body
    * JSON representation
  * OpenIdConnectKey
    * JSON representation
  * Try it!



Retrieves the set of public keys of the session cookie JSON Web Token (JWT) signer that can be used to validate the session cookie created through [createSessionCookie](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects/createSessionCookie).

### HTTP request

`GET https://identitytoolkit.googleapis.com/v1/sessionCookiePublicKeys`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body must be empty.

### Response body

Response message for v1.getSessionCookiePublicKeys.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "keys": [
        {
          object ([OpenIdConnectKey](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/TopLevel/getSessionCookiePublicKeys#OpenIdConnectKey))
        }
      ]
    }  
  
Fields  
---  
`keys[]` |  `object (`[OpenIdConnectKey](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/TopLevel/getSessionCookiePublicKeys#OpenIdConnectKey)`)` Public keys of the session cookie signer, formatted as [JSON Web Keys (JWK)](https://tools.ietf.org/html/rfc7517).  
  
## OpenIdConnectKey

Represents a public key of the session cookie signer, formatted as a [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517).

JSON representation  
---  
      
    
    {
      "kty": string,
      "alg": string,
      "use": string,
      "kid": string,
      "n": string,
      "e": string
    }  
  
Fields  
---  
`kty` |  `string` Key type.  
`alg` |  `string` Signature algorithm.  
`use` |  `string` Key use.  
`kid` |  `string` Unique string to identify this key.  
`n` |  `string` Modulus for the RSA public key, it is represented as the base64url encoding of the value's big endian representation.  
`e` |  `string` Exponent for the RSA public key, it is represented as the base64url encoding of the value's big endian representation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
