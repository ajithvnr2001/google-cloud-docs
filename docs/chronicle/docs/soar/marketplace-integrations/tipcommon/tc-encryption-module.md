---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-encryption-module/
title: Encryption module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:12.224635+00:00
---

# Encryption module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-encryption-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Encryption module

### TIPCommon.encryption.decrypt

`TIPCommon.encryption.decrypt(enc_data: bytes, key: str)→ str`

Decrypts data with the provided key.

#### Parameters

Parameters  
---  
`enc_data` | `bytes`The data to decrypt.  
`key` | `str`The password used for key generation.  
  
#### Returns

The decrypted message.

#### Return type

`str`

### TIPCommon.encryption.decrypt_email

`TIPCommon.encryption.decrypt_email(smime_email_config: SmimeEmailConfig, logger: ScriptLogger)→ Message`

Checks if an email message is encrypted or signed and decrypts or verifies it.

#### Parameters

Parameters  
---  
`email` | `email.message.Message` An `email.message.Message` object containing email and certificate details.  
`private_key_b64` | `str` A base64-encoded private key.  
`certificate_b64` | `str` A base64-encoded certificate.  
`ca_certificate_b64` | `str` A base64-encoded CA certificate.  
`logger` | `ScriptLogger` A `ScriptLogger` instance.  
  
#### Returns

A Message object with a decrypted or verified message.

#### Return type

`email.message.Message`

### TIPCommon.encryption.encrypt

`TIPCommon.encryption.encrypt(data: str, key: str)→ bytes`

Encrypts data with the provided key.

#### Parameters

Parameters  
---  
`data` | `str`The JSON string to encrypt.  
`key` | `str`The password used for key generation.  
  
#### Returns

The encrypted message.

#### Return type

`bytes`

### TIPCommon.encryption.get_private_key

`TIPCommon.encryption.get_private_key(password: str)→ bytes`

Derives a private key from a password.

#### Parameters

Parameters  
---  
`password` | `str`The password to generate the key from.  
  
#### Returns

A byte string.

#### Return type

`bytes`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
