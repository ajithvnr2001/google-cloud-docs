---
url: https://docs.cloud.google.com/kms/docs/additional-authenticated-data/
title: Additional authenticated data \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:59.023022+00:00
---

# Additional authenticated data  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/additional-authenticated-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Additional authenticated data Stay organized with collections  Save and categorize content based on your preferences. 

Additional authenticated data (AAD) is any string that you pass to Cloud Key Management Service as part of an encrypt or decrypt request. AAD is used as an integrity check and can help protect your data from a [_confused deputy attack_](https://en.wikipedia.org/wiki/Confused_deputy_problem). The AAD string must be no larger than 64 KiB.

Cloud KMS will not decrypt ciphertext unless the same AAD value is used for both encryption and decryption.

AAD is bound to the encrypted data, because you cannot decrypt the ciphertext unless you know the AAD, but it is not stored as part of the ciphertext. AAD also does not increase the cryptographic strength of the ciphertext. Instead it is an additional check by Cloud KMS to authenticate a decryption request.

In Cloud KMS, AAD is always present when you make a call to encrypt or decrypt - if you do not provide a value for AAD, then an empty string is used. If an empty string is used as the AAD for the encryption of plaintext, then only an empty string will allow decryption of the ciphertext.

AAD is not logged by [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

**Warning:** Ensure that you securely store the AAD, or have the ability to reproduce the AAD, because without the AAD you will not be able to decrypt your ciphertext.

## When to use AAD

One example of using AAD is when your application serves as a wrap/unwrap proxy with a single key and an unbounded number of clients, with each client in distinct security boundaries. For example, the application could be a diary application that allows users to maintain a private diary. When a user needs to view a private diary entry, the application can use the unique user name as the AAD in the unwrap (decrypt) request to explicitly authenticate the user. In this scenario you can use a single key to serve multiple (unbounded) users. A primary benefit is you don't need to maintain state for individual users.

Another example is if your application needs to use bearer tokens that contain some private information, such as an email address. Inputs to the bearer token would be the authenticated data used for a bearer token plus the plaintext email address. These inputs would then get encrypted so the bearer token that gets exchanged is in the form of [Additional Encrypted Authenticated Data](https://en.wikipedia.org/wiki/Authenticated_encryption) (AEAD).

## Confused deputy attack example

This example shows how an application could be tricked into decrypting ciphertext on behalf of a malicious user. The application is the confused deputy in this example because the application is unaware the attacker has tricked the application into misusing its authority. The result is the attacker is able to view decrypted data that originally was encrypted for another user. Note in this attack, the attacker does not need to know the encryption key, because it relies on the confused deputy to perform the decryption.

  1. A diary application allows users to maintain a private diary. Each diary entry is encrypted and intended to be decrypted only by the user that created the diary entry.

  2. Alice creates a diary entry. The application encrypts the diary entry and then stores the encrypted diary entry at a location reserved for diary entries that belong to Alice.

  3. Alice sends a request to view her diary entry. Because the encrypted diary entry is at a location reserved for Alice, the application decrypts the data and returns it as the response to Alice's request. This is the intended behaviour of the application.

  4. Mallory copies Alice's diary entry from the location reserved for Alice to the location reserved for Mallory.

  5. Mallory sends a request to view Mallory's copy of Alice's diary entry. Because the copy of Alice's diary entry is at a location reserved for Mallory, the application decrypts the diary entry and returns the plaintext as the response to Mallory's request. Mallory can then view Alice's diary entry, which is not the intended behaviour of the application.




To defend against this type of attack, the application can use a non-empty string as AAD for encryption and decryption. The AAD provides an extra check for decryption requests. When Mallory sends the decryption request to view Mallory's copy of Alice's diary entry, Mallory's request will not succeed unless Mallory can also trick the application into using the correct AAD.

## Storing or reproducing AAD

Before encrypting with AAD, decide whether you will _store_ the AAD side-by-side with the encrypted data, or _reproduce_ the AAD, for subsequent decryption.

A reason to store AAD is to make it straightforward to use the AAD when you need to decrypt ciphertext. For example, a database row could contain both the ciphertext and the AAD used when the plaintext was encrypted. When a decrypt request is received, the application can retrieve both the AAD and the ciphertext from the database. The application can then use the AAD for the ciphertext decryption process.

A reason to reproduce AAD is to verify any non-private data while also avoiding storage of the AAD. For example, if you want to ensure that the filepath and filename of an encrypted file has not changed, you can include the filepath and filename as AAD when you encrypt the file. Then, when a decrypt request is sent for the file, you can reproduce the AAD by examining the filepath and filename.

### Storing AAD

Storing AAD means AAD is saved and then readily available by your application for future use. For example, a database table could contain a column for ciphertext and a column for the AAD used when the ciphertext was created. When it is time to decrypt the ciphertext, the application retrieves the AAD and uses it for the decryption.

**Warning:** If you store AAD, ensure that you keep it secure.

Consider a diary application that is designed to show a diary entry only to the user that created it. When a diary entry is created, it is encrypted and then saved to a database, in column `ENCRYPTED_DIARY_ENTRY`. For each request to view a diary entry, the application authenticates the user and then provides the diary entry to the user.

Suppose no AAD is used (other than the default empty string) and hypothetically Mallory was able to copy Alice's `ENCRYPTED_DIARY_ENTRY` data to Mallory's `ENCRYPTED_DIARY_ENTRY` data. When Mallory sends a decrypt request for Mallory's `ENCRYPTED_DIARY_ENTRY` data (which was copied from Alice's data), the application performs the decryption without realizing it has been tricked. Mallory is able to see Alice's diary entry as plaintext.

Now let's suppose the user email address is used as the AAD when a diary entry is encrypted. When Alice creates a diary entry, the application stores her unencrypted email address in the column `EMAIL`, side-by-side with the `ENCRYPTED_DIARY_ENTRY` data. Let's suppose again that Mallory was able to copy Alice's `ENCRYPTED_DIARY_ENTRY` data to Mallory's `ENCRYPTED_DIARY_ENTRY` data. When Mallory sends a decrypt request, the application retrieves Mallory's email address from the `EMAIL` column to use as the AAD for the decrypt request. Mallory's email address will not succeed as the AAD for decryption, so the application does not let Mallory see Alice's diary entry as plaintext.

### Reproducing AAD

Reproducing AAD means it isn't stored anywhere, but you can reproduce when it is time for decryption.

**Warning:** If you do not store the AAD and you cannot reproduce the AAD, you will not be able to decrypt the ciphertext.

As an example, you can use a filepath and filename as AAD. During the encryption process, suppose the encrypted file was saved to `MY_PATH\MY_FILE1.enc`, so `"MY_PATH\MY_FILE1.enc"` was used as the AAD. This AAD is not stored. When a decrypt request is received, the application reproduces the AAD by examining the filepath and filename of the file to decrypt. If the encrypted file has not been moved to another location, `"MY_PATH\MY_FILE1.enc"` will be used as the AAD during decryption, which is the same as the AAD used during encryption, so the decryption can proceed.

If the encrypted file has been moved, for example to `SOME_OTHER_PATH\MY_FILE1.enc`, then `"SOME_OTHER_PATH\MY_FILE1.enc"` will be used as the AAD for decryption. This AAD value does not match the AAD value used for encryption, so the decryption will fail.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
