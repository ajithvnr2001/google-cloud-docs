---
url: https://docs.cloud.google.com/kms/docs/troubleshooting-failed-imports/
title: Troubleshooting failed imports \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:28.512286+00:00
---

# Troubleshooting failed imports  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/troubleshooting-failed-imports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Troubleshooting failed imports Stay organized with collections  Save and categorize content based on your preferences. 

This topic provides information to help you determine why the state of an imported key version is `IMPORT_FAILED`.

Cloud Key Management Service allows you to import user-provided cryptographic keys as new key versions. The initial state for an imported key version is `PENDING_IMPORT`. If the key material is imported successfully, the state of the imported key version is updated to `ENABLED`. If key material isn't imported successfully, the state of the key version is updated to `IMPORT_FAILED`.

## Problems with the key's format

Formatting issues are a common cause of import failures. The following error messages are typically caused by incorrectly formatted keys:

  * `An argument to the import operation was malformed`

  * `The key material in the import request couldn't be unwrapped or wasn't formatted correctly`




Length errors are a specific variety of formatting error that Cloud KMS can detect before it attempts to unwrap your key material. The following length error messages are typically caused by incorrectly formatted keys:

  * `Wrapped ECDSA key has invalid length of (length)`

  * `Wrapped key is too short`

  * `Wrapped key does not consist of 64-bit blocks`

  * `Wrapped key has invalid length`




You can learn more about [formatting keys for import](https://docs.cloud.google.com/kms/docs/formatting-keys-for-import).

## Problems wrapping a key

The following errors indicate a problem when manually wrapping keys for import.

  * `An argument to the import operation was malformed`

  * `The key material in the import request couldn't be unwrapped or wasn't formatted correctly`




Using automatic key wrapping is recommended. If you cannot use automatic key wrapping, verify that you are using the wrapping key from the correct import job and try to [wrap the key](https://docs.cloud.google.com/kms/docs/wrapping-a-key) again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
