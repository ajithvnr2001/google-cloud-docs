---
url: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter/
title: Class AsyncWriter (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:27.974744+00:00
---

# Class AsyncWriter (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class AsyncWriter (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Perform resumable uploads asynchronously. 

Resumable uploads allow applications to continue uploading data after network disconnects and application restarts. To resume an upload the library first queries the current state of the upload. The upload uses this information to send the remaining data. Applications only need to checkpoint a string, the [`UploadId()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter#classgoogle_1_1cloud_1_1storage_1_1AsyncWriter_1a69494bd391cb29278f3a1ddf76611948), to resume an upload even after the application itself restarts.

Some data sources do not permit rewinding to an arbitrary point. For example: if the application is receiving streaming data from an external source it may be impossible to shutdown the application and recover the data streamed while the application was down.

This API does not support resuming uploading data from streaming data sources. If the upload is interrupted you must be able to start sending data from an arbitrary point. 

## Constructors 

### AsyncWriter(AsyncWriter &&)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `AsyncWriter &&`   
  
  
### AsyncWriter(AsyncWriter const &)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `AsyncWriter const &`   
  
  
### AsyncWriter()

### AsyncWriter(std::unique_ptr< AsyncWriterConnection >)

**Parameter**  
---  
**Name** | **Description**  
`impl` |  `std::unique_ptr< AsyncWriterConnection >`   
  
  
## Operators 

### operator=(AsyncWriter &&)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `AsyncWriter &&`   
  
**Returns**  
---  
**Type** | **Description**  
`AsyncWriter &` |   
  
### operator=(AsyncWriter const &)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `AsyncWriter const &`   
  
**Returns**  
---  
**Type** | **Description**  
`AsyncWriter &` |   
  
## Functions 

### UploadId() const

The upload id. 

Applications that need to resume uploads after a restart should checkpoint this value to persistent storage.

**Note:** Calling this function on a default-constructed or moved-from [`AsyncWriter`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter) results in undefined behavior. 

**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
### PersistedState() const

The state of the current upload. 

This returns the last "known" state of the upload. The values are updated (1) when the [`AsyncWriter`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter) object is created, and (2) on calls to `Query()` and [`Finalize()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter#classgoogle_1_1cloud_1_1storage_1_1AsyncWriter_1aafe4cfa63e434b6eda2431522a66fa7e).

Applications may finalize an upload, and then try to resume the upload. In this case this function returns `google::storage::v2::Object`.

During an upload the service will periodically persist the uploaded data. Applications should not assume that all data "sent" is persisted. The service may buffer the data in ephemeral storage before persisting it.

If the application needs to resume an upload that was interrupted, then it must check [`PersistedState()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter#classgoogle_1_1cloud_1_1storage_1_1AsyncWriter_1addc69904113061f8949478e4cec7a7b4) before sending data. The service will assume that new data starts at the correct offset.

If an upload is resumed after it is finalized, the library will return a variant holding `google::storage::v2::Object` value.

Otherwise the variant returns the size of the persisted data. The application should send the remaining data to upload, starting from this point.

In the case of an appendable object, this variant will be populated with a `google::storage::v2::Object` on the first response.

**Note:** Calling this function on a default-constructed or moved-from [`AsyncWriter`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter) results in undefined behavior. 

**Returns**  
---  
**Type** | **Description**  
`std::variant< std::int64_t, google::storage::v2::Object >` |   
  
### Write(AsyncToken, WritePayload)

Upload `payload` returning a new token to continue the upload. 

**Parameters**  
---  
**Name** | **Description**  
`token` |  `AsyncToken`   
  
`payload` |  `WritePayload`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< AsyncToken > >` |   
  
### Finalize(AsyncToken)

Finalize the upload with the existing data. 

**Parameter**  
---  
**Name** | **Description**  
`token` |  `AsyncToken`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::v2::Object > >` |   
  
### Finalize(AsyncToken, WritePayload)

Upload `payload` and then finalize the upload. 

**Parameters**  
---  
**Name** | **Description**  
`token` |  `AsyncToken`   
  
`payload` |  `WritePayload`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::v2::Object > >` |   
  
### Flush()

Flush any buffered data to the service. 

For buffered uploads, this forces any data in the buffer to be sent to the service. The returned future is satisfied when the service acknowledges the flush. Note that the service may not have persisted the data, it may only be in ephemeral storage. To query the amount of persisted data use [`PersistedState()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter#classgoogle_1_1cloud_1_1storage_1_1AsyncWriter_1addc69904113061f8949478e4cec7a7b4) after the flush completes.

**Note:** This is not a terminal operation. The [`AsyncWriter`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter) can be used for further [`Write()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter#classgoogle_1_1cloud_1_1storage_1_1AsyncWriter_1ac0832f422b66e7c231deb9bdff022967) or [`Finalize()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter#classgoogle_1_1cloud_1_1storage_1_1AsyncWriter_1aafe4cfa63e434b6eda2431522a66fa7e) operations. 

**Returns**  
---  
**Type** | **Description**  
`future< Status >` |   
  
### Close()

Close the upload by flushing the remaining data in buffer. 

**Warning:** This is a terminal operation. The [`AsyncWriter`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1AsyncWriter) object is not usable after this call. 

**Returns**  
---  
**Type** | **Description**  
`future< Status >` |   
  
### GetRequestMetadata() const

The headers (if any) returned by the service. 

For debugging only.

**Warning:** The contents of these headers may change without notice. Unless documented in the API, headers may be removed or added by the service. Furthermore, the headers may change from one version of the library to the next, as we find more (or different) opportunities for optimization. 

**Returns**  
---  
**Type** | **Description**  
`RpcMetadata` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
