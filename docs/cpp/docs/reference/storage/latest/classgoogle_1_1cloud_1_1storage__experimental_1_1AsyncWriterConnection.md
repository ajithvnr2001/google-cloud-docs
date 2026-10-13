---
url: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection/
title: Class AsyncWriterConnection (2.47.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:22.098556+00:00
---

# Class AsyncWriterConnection (2.47.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class AsyncWriterConnection (2.47.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

An interface to asynchronously perform resumable uploads. 

The client library uses the `google.storage.v2.StorageService.BidiWriteObject` RPC to perform asynchronous resumable uploads to Google Cloud Storage. As the name implies, this is a bi-directional RPC. The messages sent via this RPC are `google.storage.v2.BidiWriteObjectRequest` and `google.storage.v2.BidiWriteObjectResponse`.

  * The `BidiWriteObjectRequest` messages upload the object data.
  * The last `BidiWriteObjectRequest` message in an upload must include a `finalize` attribute. These messages result in a `BidiWriteObjectResponse` message, which includes the metadata of the GCS object created by the upload.
  * `BidiWriteObjectRequest` messages may include a `flush` attribute. Such messages result in a `BidiReadObjectResponse` message, which includes how much of the uploaded data has been persisted.
  * `BidiWriteObjectRequest` messages may not include more than `google.storage.v2.ServiceConstants.MAX_WRITE_CHUNK_BYTES` bytes of payload.



In this interface different member functions write messages with different attributes.

The [`Write()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a4dbae17744555ea0929c7180a07c64cf) member function uploads some data, without setting any `finalize` or `flush` attributes. If necessary, the data is broken into multiple `BidiWriteObjectRequest` messages.

The [`Finalize()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1aa8c8027975b9cbdbc363e868e9211a7d) member function uploads some data and sets the `finalize` attribute. If needed, the data is broken into multiple messages to satisfy the `MAX_WRITE_CHUNK_BYTES` limit. Only the last message has the `finalize` attribute. This function also waits for the response message and returns the object metadata (or an error).

The [`Flush()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a769ecdbe14410e2ed0ffb25425828bf1) member function uploads some data and sets the `flush` attribute. As with the other functions the data may need to be broken into multiple messages. Only the last message will have the `flush` attribute set.

This interface can be used to mock the behavior of these bidirectional streaming RPCs. Applications may use these mocks in their own tests.

**Warning:** We expect most applications will use this class in mocks or via the [`AsyncWriter`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriter) wrapper, and do not recommend its use outside mocks. If using this class directly keep in mind the following restrictions: \- Never destroy an [`AsyncWriterConnection`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection) object while any calls to [`Write()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a4dbae17744555ea0929c7180a07c64cf), [`Flush()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a769ecdbe14410e2ed0ffb25425828bf1), [`Query()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a24e6694dec5c55f9bc63a6e336f92ce3), or [`Finalize()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1aa8c8027975b9cbdbc363e868e9211a7d) are pending. \- Have at most one call to [`Write()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a4dbae17744555ea0929c7180a07c64cf) or [`Flush()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a769ecdbe14410e2ed0ffb25425828bf1) pending. \- Do not issue a [`Write()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a4dbae17744555ea0929c7180a07c64cf) call while a [`Flush()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a769ecdbe14410e2ed0ffb25425828bf1) call is pending or vice-versa. \- Do not issue any [`Finalize()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1aa8c8027975b9cbdbc363e868e9211a7d) calls while a [`Write()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a4dbae17744555ea0929c7180a07c64cf), [`Flush()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a769ecdbe14410e2ed0ffb25425828bf1), or [`Query()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a24e6694dec5c55f9bc63a6e336f92ce3) call is pending. \- Only issue one [`Finalize()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1aa8c8027975b9cbdbc363e868e9211a7d) call. \- Issue exactly one [`Query()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a24e6694dec5c55f9bc63a6e336f92ce3) call after a [`Flush()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a769ecdbe14410e2ed0ffb25425828bf1) call completes. 

## Functions 

### Cancel()

Cancels the streaming RPC, terminating any pending operations. 

**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### UploadId() const

Returns the upload id. Used to checkpoint the state and resume uploads. 

**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
### PersistedState() const

Returns the last known state of the upload. 

Updated during initialization and by successful [`Query()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a24e6694dec5c55f9bc63a6e336f92ce3) or [`Finalize()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1aa8c8027975b9cbdbc363e868e9211a7d) requests. 

**Returns**  
---  
**Type** | **Description**  
`absl::variant< std::int64_t, google::storage::v2::Object >` |   
  
### Write(WritePayload)

Uploads some data to the service. 

**Parameter**  
---  
**Name** | **Description**  
`payload` |  `WritePayload`   
  
**Returns**  
---  
**Type** | **Description**  
`future< Status >` |   
  
### Finalize(WritePayload)

Finalizes an upload. 

**Parameter**  
---  
**Name** | **Description**  
`` |  `WritePayload`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::v2::Object > >` |   
  
### Flush(WritePayload)

Uploads some data to the service and flushes the value. 

**Parameter**  
---  
**Name** | **Description**  
`payload` |  `WritePayload`   
  
**Returns**  
---  
**Type** | **Description**  
`future< Status >` |   
  
### Query()

Wait for the result of a [`Flush()`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection#classgoogle_1_1cloud_1_1storage__experimental_1_1AsyncWriterConnection_1a769ecdbe14410e2ed0ffb25425828bf1) call. 

**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< std::int64_t > >` |   
  
### GetRequestMetadata()

Return the request metadata. 

**Returns**  
---  
**Type** | **Description**  
`RpcMetadata` |   
  
### WriteHandle() const

Returns the latest write handle, if any. 

**Returns**  
---  
**Type** | **Description**  
`absl::optional< google::storage::v2::BidiWriteHandle >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
