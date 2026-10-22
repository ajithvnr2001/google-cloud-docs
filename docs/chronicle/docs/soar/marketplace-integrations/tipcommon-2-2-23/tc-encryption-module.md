---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-encryption-module/
title: encryption module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:48.192749+00:00
---

# encryption module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-encryption-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# `encryption` module

The **`encryption` module** offers a set of high-level functions for data protection and secure communication. It simplifies the process of encrypting and decrypting strings using password-derived keys and provides specialized handling for S/MIME email verification and decryption to ensure message integrity and confidentiality.

### TIPCommon.encryption.decrypt

`TIPCommon.encryption.decrypt(enc_data: bytes, key: str) → str`

Decrypts data using a provided password.

#### Parameters

Parameters  
---  
`enc_data` | `bytes`The encrypted data to decrypt.  
`key` | `str`The password used for key generation during the decryption process.  
  
#### Returns

The decrypted message.

#### Return type

`str`

### TIPCommon.encryption.decrypt_email

`TIPCommon.encryption.decrypt_email(smime_email_config: SmimeEmailConfig, logger: ScriptLogger) → Message`

Checks if an email message is encrypted or signed and performs the necessary decryption or verification.

#### Parameters

Parameters  
---  
`smime_email_config` | `SmimeEmailConfig` A configuration object that contains the email message (`email.message.Message`), the base64-encoded private key, the certificate, and the CA certificate.  
`logger` | `ScriptLogger` An instance of `ScriptLogger` that logs the decryption and verification process.  
  
#### Returns

A message object that contains the decrypted or verified content.

#### Return type

`email.message.Message`

### TIPCommon.encryption.encrypt

`TIPCommon.encryption.encrypt(data: str, key: str) → bytes`

Encrypts a JSON string using a provided key.

#### Parameters

Parameters  
---  
`data` | `str` The JSON string to encrypt.  
`key` | `str` The password used for key generation during the encryption process.  
  
#### Returns

The encrypted message as a byte string.

#### Return type

`bytes`

### TIPCommon.encryption.get_private_key

`TIPCommon.encryption.get_private_key(password: str) → bytes`

Derives a cryptographic key from a provided password.

#### Parameters

Parameters  
---  
`password` | `str` The password string from which the private key is generated.  
  
#### Returns

A byte string that represents the derived private key.

#### Return type

`bytes`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
