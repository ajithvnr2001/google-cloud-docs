---
url: https://docs.cloud.google.com/kms/docs/formatting-keys-for-import/
title: Formatting keys for import \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:37.243113+00:00
---

# Formatting keys for import  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/formatting-keys-for-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Formatting keys for import Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to format your keys so that they can be imported by Cloud KMS as new key versions.

The correct format for your key material varies based on whether the key material is being imported into a symmetric key, or into an asymmetric key. For more information about the difference between symmetric and asymmetric keys, see [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).

## Supported key formats

  * **Symmetric keys for encryption** : Imported symmetric keys must be 16 bytes (for [raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption) only) or 32 bytes of binary data, and must _not_ be encoded. If your key is hex-encoded or base64-encoded, then you must decode it before attempting to import it.
  * **Symmetric keys for signing (MAC keys)** : Imported HMAC signing keys must have a length equal to the output length of the cryptographic hash function being used (for example, HMAC-SHA256 keys must have a length of 32 bytes), and must _not_ be encoded. If your key is hex-encoded or base64-encoded, then you must decode it before attempting to import it.
  * **Asymmetric keys for encryption or signing** : Imported asymmetric keys must be in PKCS #8 format and must be DER-encoded. PCKS #8 format is defined in [RFC 5208](https://tools.ietf.org/html/rfc5208). DER encoding is defined in [International Telecommunications Union X.680](https://www.itu.int/rec/T-REC-X.680/en). Asymmetric keys must use one of the [length and algorithm combinations](https://docs.cloud.google.com/kms/docs/algorithms) supported by Cloud KMS.

**Important:** An RSA key's public exponent must be 65,537 or higher. This is a Digital Signature Standard (DSS) requirement noted in the Criteria for IFC Key Pairs section of [FIPS PUB 186-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf), Section B.3.1

Some aspects of a key, such as the key's length, cannot be changed after the key is created. In these cases, the key cannot be imported into Cloud KMS.

## Checking a symmetric key

Use the `wc` command to check a symmetric key's length.
    
    
    wc -c /path/to/unwrapped-key
    

  * You cannot import a symmetric encryption key with a length other than 32.

  * Symmetric signing keys (MAC keys) must have a length equal to the output length of the cryptographic hash function being used (e.g. HMAC-SHA256 keys must have a length of 32 bytes).




Use the `file` command to check a key's format.
    
    
    file /path/to/unwrapped-key
    

  * If the output is `data`, the key is in the correct format to be imported.

  * If the output is `ASCII text`, use the `cat` command to display the contents of the file.

    * If it is a string of letters and numbers ending in an `=` sign, it might be base64-encoded. Use the `base64` command (`Base64.exe` on Windows) to decode it. The following is an example of a base64-encoded key:
          
          THzArjassB+giKeNeT1Zr74OgV24t+Ep+37Ec6ojB3Y=
          

    * If it contains one or more lines of hexadecimal numbers, it might be hex-encoded. Use the `xxd` command (or the [`Format-Hex` PowerShell command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/format-hex) on Windows) to decode it. The following is an example of a hex-encoded key:
          
          00000000: 4c7c c0ae 36ac b01f a088 a78d 793d 59af  L|..6.......y=Y.
          00000010: be0e 815d b8b7 e129 fb7e c473 aa23 0776  ...]...).~.s.#.v
          

    * If it contains any other text, it may not be a valid symmetric key.




## Formatting asymmetric keys

Asymmetric keys using any of the supported [algorithms](https://docs.cloud.google.com/kms/docs/algorithms) can be imported. In practice, it is difficult to retroactively determine the algorithm used to create an asymmetric key. For that reason, we recommend that you run the following commands on each asymmetric key before attempting to import it into Cloud KMS.

  1. Use the `file` command to check a key's format.
         
         file /path/to/unwrapped-key
         

     * If the output is `PEM`, the key is in PEM format. If it is `ASCII text`, it is probably in PEM format. In either case, run the following command to convert it to PCKS#8 DER format:
           
           openssl pkcs8 -topk8 -nocrypt -inform PEM -outform DER \
               -in /path/to/asymmetric-key-pem \
               -out /path/to/formatted-key
           

     * If the output is `data`, the key is likely to be in DER format, but it may not be in PKCS #8 format. Run the following command to ensure that the key is in the correct format. The command has no effect if the key is already in the correct format. In that case, you can use the `diff` command to verify that the input and output file are identical.
           
           openssl pkcs8 -topk8 -nocrypt -inform DER -outform DER \
               -in /path/to/asymmetric-key-der \
               -out /path/to/formatted-key
           




## Troubleshooting

If you run the commands above and you believe the key is in an appropriate format, but the import still fails, check for errors in Google Cloud console, and then see [Troubleshooting failed imports](https://docs.cloud.google.com/kms/docs/troubleshooting-failed-imports).

## What's next

  * Continue to [Import a key version](https://docs.cloud.google.com/kms/docs/importing-a-key)
  * Learn about [key import](https://docs.cloud.google.com/kms/docs/key-import)



[ Next Configure OpenSSL for manual key wrapping  arrow_forward  ](https://docs.cloud.google.com/kms/docs/configuring-openssl-for-manual-key-wrapping)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
