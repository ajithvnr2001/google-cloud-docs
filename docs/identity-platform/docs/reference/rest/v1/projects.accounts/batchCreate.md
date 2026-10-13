---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects.accounts/batchCreate/
title: Method: projects.accounts.batchCreate \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:17.936433+00:00
---

# Method: projects.accounts.batchCreate  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects.accounts/batchCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  Method: projects.accounts.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Uploads multiple accounts into the Google Cloud project. If there is a problem uploading one or more of the accounts, the rest will be uploaded, and a list of the errors will be returned. To use this method requires a Google OAuth 2.0 credential with proper [permissions](https://cloud.google.com/identity-platform/docs/access-control).

### HTTP request

`POST https://identitytoolkit.googleapis.com/v1/projects/{targetProjectId}/accounts:batchCreate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`targetProjectId` |  `string` The Project ID of the Identity Platform project which the account belongs to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `targetProjectId`:

  * `firebaseauth.users.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "hashAlgorithm": string,
      "signerKey": string,
      "saltSeparator": string,
      "rounds": integer,
      "memoryCost": integer,
      "users": [
        {
          object ([UserInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/UserInfo))
        }
      ],
      "delegatedProjectNumber": string,
      "sanityCheck": boolean,
      "allowOverwrite": boolean,
      "cpuMemCost": integer,
      "parallelization": integer,
      "blockSize": integer,
      "dkLen": integer,
      "passwordHashOrder": enum ([PasswordHashOrder](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/PasswordHashOrder)),
      "tenantId": string,
      "argon2Parameters": {
        object ([Argon2Parameters](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/Argon2Parameters))
      }
    }  
  
Fields  
---  
`hashAlgorithm` |  `string` Required. The hashing function used to hash the account passwords. Must be one of the following: * HMAC_SHA256 * HMAC_SHA1 * HMAC_MD5 * SCRYPT * PBKDF_SHA1 * MD5 * HMAC_SHA512 * SHA1 * BCRYPT * PBKDF2_SHA256 * SHA256 * SHA512 * STANDARD_SCRYPT * ARGON2  
`signerKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The signer key used to hash the password. Required for the following hashing functions: * SCRYPT, * HMAC_MD5, * HMAC_SHA1, * HMAC_SHA256, * HMAC_SHA512A base64-encoded string.  
`saltSeparator` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` One or more bytes to be inserted between the salt and plain text password. For stronger security, this should be a single non-printable character.A base64-encoded string.  
`rounds` |  `integer` The number of rounds used for hash calculation. Only required for the following hashing functions: * MD5 * SHA1 * SHA256 * SHA512 * PBKDF_SHA1 * PBKDF2_SHA256 * SCRYPT  
`memoryCost` |  `integer` Memory cost for hash calculation. Only required when the hashing function is SCRYPT.  
`users[]` |  `object (`[UserInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/UserInfo)`)` A list of accounts to upload. `localId` is required for each user; everything else is optional.  
`delegatedProjectNumber  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
`sanityCheck` |  `boolean` If true, the service will do the following list of checks before an account is uploaded: * Duplicate emails * Duplicate federated IDs * Federated ID provider validation If the duplication exists within the list of accounts to be uploaded, it will prevent the entire list from being uploaded. If the email or federated ID is a duplicate of a user already within the project/tenant, the account will not be uploaded, but the rest of the accounts will be unaffected. If false, these checks will be skipped.  
`allowOverwrite` |  `boolean` Whether to overwrite an existing account in Identity Platform with a matching `localId` in the request. If true, the existing account will be overwritten. If false, an error will be returned.  
`cpuMemCost` |  `integer` The CPU memory cost parameter to be used by the STANDARD_SCRYPT hashing function. This parameter, along with blockSize and cpuMemCost help tune the resources needed to hash a password, and should be tuned as processor speeds and memory technologies advance.  
`parallelization` |  `integer` The parallelization cost parameter to be used by the STANDARD_SCRYPT hashing function. This parameter, along with blockSize and cpuMemCost help tune the resources needed to hash a password, and should be tuned as processor speeds and memory technologies advance.  
`blockSize` |  `integer` The block size parameter used by the STANDARD_SCRYPT hashing function. This parameter, along with parallelization and cpuMemCost help tune the resources needed to hash a password, and should be tuned as processor speeds and memory technologies advance.  
`dkLen` |  `integer` The desired key length for the STANDARD_SCRYPT hashing function. Must be at least 1.  
`passwordHashOrder` |  `enum (`[PasswordHashOrder](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/PasswordHashOrder)`)`  
`tenantId` |  `string` The ID of the Identity Platform tenant the account belongs to.  
`argon2Parameters` |  `object (`[Argon2Parameters](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/Argon2Parameters)`)` The parameters for Argon2 hashing algorithm.  
  
### Response body

If successful, the response body contains an instance of `[UploadAccountResponse](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/UploadAccountResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/identitytoolkit`
  * ` https://www.googleapis.com/auth/firebase`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
