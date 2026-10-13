---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys
title: REST Resource: projects.serviceAccounts.keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:08.686068+00:00
---

# REST Resource: projects.serviceAccounts.keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.serviceAccounts.keys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServiceAccountKey
    * JSON representation
  * ServiceAccountPrivateKeyType
  * ServiceAccountKeyAlgorithm
  * ServiceAccountKeyOrigin
  * KeyType
  * ServiceAccountKeyDisableReason
  * ExtendedStatus
    * JSON representation
  * ServiceAccountKeyExtendedStatusKey
  * Methods



## Resource: ServiceAccountKey

Represents a service account key.

A service account has two sets of key-pairs: user-managed and system-managed. System-managed keys are also called _Google-owned and managed keys_.

User-managed key-pairs can be created and deleted by users. Users are responsible for rotating these keys periodically to ensure security of their service accounts. Users retain the private key of these key-pairs, and Google retains ONLY the public key.

System-managed keys that are actively used for signing are rotated regularly according to [security best practices](https://docs.cloud.google.com/iam/docs/key-rotation#timing). The rotation process is probabilistic, and usage of the new key will gradually ramp up and down over the key's lifetime.

If you cache the public key set for a service account, we recommend that you update the cache every 15 minutes. User-managed keys can be added and removed at any time, so it is important to update the cache frequently. For Google-managed keys, Google will publish a key at least 6 hours before it is first used for signing and will keep publishing it for at least 6 hours after it was last used for signing.

Public keys for all service accounts are also published at the OAuth2 Service Account API.

JSON representation  
---  
      
    
    {
      "name": string,
      "privateKeyType": enum ([ServiceAccountPrivateKeyType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountPrivateKeyType)),
      "keyAlgorithm": enum ([ServiceAccountKeyAlgorithm](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)),
      "privateKeyData": string,
      "publicKeyData": string,
      "validAfterTime": string,
      "validBeforeTime": string,
      "keyOrigin": enum ([ServiceAccountKeyOrigin](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyOrigin)),
      "keyType": enum ([KeyType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#KeyType)),
      "disabled": boolean,
      "disableReason": enum ([ServiceAccountKeyDisableReason](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyDisableReason)),
      "extendedStatus": [
        {
          object ([ExtendedStatus](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ExtendedStatus))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the service account key in the following format `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`.  
`privateKeyType` |  `enum (`[ServiceAccountPrivateKeyType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountPrivateKeyType)`)` The output format for the private key. Only provided in `keys.create` responses, not in `keys.get` or `ListServiceAccountKey` responses.Google never exposes system-managed private keys, and never retains user-managed private keys.  
`keyAlgorithm` |  `enum (`[ServiceAccountKeyAlgorithm](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)`)` Specifies the algorithm (and possibly key size) for the key.  
`privateKeyData` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The private key data. Only provided in `keys.create` responses. Make sure to keep the private key data secure because it allows for the assertion of the service account identity. When base64 decoded, the private key data can be used to authenticate with Google API client libraries and with [gcloud auth activate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account).A base64-encoded string.  
`publicKeyData` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The public key data. Only provided in `keys.get` responses.A base64-encoded string.  
`validAfterTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The key can be used after this timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`validBeforeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The key can be used before this timestamp. For system-managed key pairs, this timestamp is the end time for the private key signing operation. The public key could still be used for verification for a few hours after this time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`keyOrigin` |  `enum (`[ServiceAccountKeyOrigin](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyOrigin)`)` The key origin.  
`keyType` |  `enum (`[KeyType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#KeyType)`)` The key type.  
`disabled` |  `boolean` The key status.  
`disableReason` |  `enum (`[ServiceAccountKeyDisableReason](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyDisableReason)`)` Output only. optional. If the key is disabled, it may have a DisableReason describing why it was disabled.  
`extendedStatus[]` |  `object (`[ExtendedStatus](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ExtendedStatus)`)` Output only. Extended Status provides permanent information about a service account key. For example, if this key was detected as exposed or compromised, that information will remain for the lifetime of the key in the extendedStatus.  
  
## ServiceAccountPrivateKeyType

Supported private key output formats.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified. Equivalent to `TYPE_GOOGLE_CREDENTIALS_FILE`.  
`TYPE_PKCS12_FILE` | PKCS12 format. The password for the PKCS12 file is `notasecret`. For more information, see <https://tools.ietf.org/html/rfc7292>.  
`TYPE_GOOGLE_CREDENTIALS_FILE` | Google Credentials File format.  
  
## ServiceAccountKeyAlgorithm

Supported key algorithms.

Enums  
---  
`KEY_ALG_UNSPECIFIED` | An unspecified key algorithm.  
`KEY_ALG_RSA_1024` | 1k RSA Key.  
`KEY_ALG_RSA_2048` | 2k RSA Key.  
  
## ServiceAccountKeyOrigin

Service Account Key Origin.

Enums  
---  
`ORIGIN_UNSPECIFIED` | Unspecified key origin.  
`USER_PROVIDED` | Key is provided by user.  
`GOOGLE_PROVIDED` | Key is provided by Google.  
  
## KeyType

`KeyType` filters to selectively retrieve certain varieties of keys.

Enums  
---  
`KEY_TYPE_UNSPECIFIED` | Unspecified key type. The presence of this in the message will immediately result in an error.  
`USER_MANAGED` | User-managed keys (managed and rotated by the user).  
`SYSTEM_MANAGED` | System-managed keys (managed and rotated by Google).  
  
## ServiceAccountKeyDisableReason

DisableReason is intended to communicate more information about a disabled Service Accounts or Service Account Key.

Enums  
---  
`SERVICE_ACCOUNT_KEY_DISABLE_REASON_UNSPECIFIED` | Unspecified disable reason  
`SERVICE_ACCOUNT_KEY_DISABLE_REASON_USER_INITIATED` | Disabled by the user  
`SERVICE_ACCOUNT_KEY_DISABLE_REASON_EXPOSED` | Google detected this Service Account external key's private key data as exposed, typically in a public repository on GitHub or similar.  
`SERVICE_ACCOUNT_KEY_DISABLE_REASON_COMPROMISE_DETECTED` | This service account external key was detected as compromised and used by an attacker.  
  
## ExtendedStatus

Extended status can store additional metadata. For example, for keys disabled due to their private key data being expoesed we may include a message with more information about the exposure.

JSON representation  
---  
      
    
    {
      "key": enum ([ServiceAccountKeyExtendedStatusKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyExtendedStatusKey)),
      "value": string
    }  
  
Fields  
---  
`key` |  `enum (`[ServiceAccountKeyExtendedStatusKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyExtendedStatusKey)`)` The key for this extended status.  
`value` |  `string` The value for the extended status.  
  
## ServiceAccountKeyExtendedStatusKey

Different categories of extendedStatus messages. For example the accompanying message for SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_EXPOSED may contain information about how the key was exposed.

Enums  
---  
`SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_UNSPECIFIED` | Unspecified extended status, should not be used.  
`SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_EXPOSED` | This key has been detected as exposed. extended_status_value may contain information about the exposure (public GitHub repo, open internet, etc.)  
`SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_COMPROMISE_DETECTED` | This key was implicated in a compromise or other attack. extended_status_value may contain information about the abuse perpetrated.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/create)`

|  Creates a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/delete)`

|  Deletes a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
  
### `[disable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/disable)`

|  Disable a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
  
### `[enable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/enable)`

|  Enable a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/get)`

|  Gets a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/list)`

|  Lists every `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)` for a service account.  
  
### `[upload](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/upload)`

|  Uploads the public key portion of a key pair that you manage, and associates the public key with a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-29 UTC."],[],[]] 
