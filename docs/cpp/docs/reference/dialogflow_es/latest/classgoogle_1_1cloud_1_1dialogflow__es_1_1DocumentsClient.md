---
url: https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1DocumentsClient/
title: Class DocumentsClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:02.621702+00:00
---

# Class DocumentsClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1DocumentsClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class DocumentsClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Service for managing knowledge [Documents](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260). 

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### DocumentsClient(DocumentsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DocumentsClient const &`   
  
  
### DocumentsClient(DocumentsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DocumentsClient &&`   
  
  
### DocumentsClient(std::shared_ptr< DocumentsConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< DocumentsConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(DocumentsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DocumentsClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`DocumentsClient &` |   
  
### operator=(DocumentsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DocumentsClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`DocumentsClient &` |   
  
## Functions 

### ListDocuments(std::string const &, Options)

Returns the list of all documents of the knowledge base. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The knowledge base to list all documents for. Format: `projects/<`[`Project`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html)`ID>/locations/<`[`Location`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Location.html)`ID>/knowledgeBases/<Knowledge Base ID>`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::dialogflow::v2::Document >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListDocuments(google::cloud::dialogflow::v2::ListDocumentsRequest, Options)

Returns the list of all documents of the knowledge base. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::ListDocumentsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.ListDocumentsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L410). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::dialogflow::v2::Document >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetDocument(std::string const &, Options)

Retrieves the specified document. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the document to retrieve. Format `projects/<`[`Project`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html)`ID>/locations/<`[`Location`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Location.html)`ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::dialogflow::v2::Document >` | the result of the RPC. The response message type ([google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetDocument(google::cloud::dialogflow::v2::GetDocumentRequest const &, Options)

Retrieves the specified document. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::GetDocumentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.GetDocumentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L396). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::dialogflow::v2::Document >` | the result of the RPC. The response message type ([google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateDocument(std::string const &, google::cloud::dialogflow::v2::Document const &, Options)

Creates a new document. 

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)



**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The knowledge base to create a document for. Format: `projects/<`[`Project`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html)`ID>/locations/<`[`Location`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Location.html)`ID>/knowledgeBases/<Knowledge Base ID>`.   
`document` |  `google::cloud::dialogflow::v2::Document const &`   
Required. The document to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateDocument(NoAwaitTag, std::string const &, google::cloud::dialogflow::v2::Document const &, Options)

Creates a new document. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`document` |  `google::cloud::dialogflow::v2::Document const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateDocument(google::cloud::dialogflow::v2::CreateDocumentRequest const &, Options)

Creates a new document. 

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)



**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::CreateDocumentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.CreateDocumentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L465). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateDocument(NoAwaitTag, google::cloud::dialogflow::v2::CreateDocumentRequest const &, Options)

Creates a new document. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::CreateDocumentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateDocument(google::longrunning::Operation const &, Options)

Creates a new document. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` |   
  
### ImportDocuments(google::cloud::dialogflow::v2::ImportDocumentsRequest const &, Options)

Creates documents by importing data from external sources. 

Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [ImportDocumentsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L538)



**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::ImportDocumentsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.ImportDocumentsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L482). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::ImportDocumentsResponse > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.ImportDocumentsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L538) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ImportDocuments(NoAwaitTag, google::cloud::dialogflow::v2::ImportDocumentsRequest const &, Options)

Creates documents by importing data from external sources. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::ImportDocumentsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ImportDocuments(google::longrunning::Operation const &, Options)

Creates documents by importing data from external sources. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::ImportDocumentsResponse > >` |   
  
### DeleteDocument(std::string const &, Options)

Deletes the specified document. 

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the document to delete. Format: `projects/<`[`Project`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html)`ID>/locations/<`[`Location`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Location.html)`ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::KnowledgeOperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteDocument(NoAwaitTag, std::string const &, Options)

Deletes the specified document. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteDocument(google::cloud::dialogflow::v2::DeleteDocumentRequest const &, Options)

Deletes the specified document. 

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::DeleteDocumentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.DeleteDocumentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L545). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::KnowledgeOperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteDocument(NoAwaitTag, google::cloud::dialogflow::v2::DeleteDocumentRequest const &, Options)

Deletes the specified document. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::DeleteDocumentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteDocument(google::longrunning::Operation const &, Options)

Deletes the specified document. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::KnowledgeOperationMetadata > >` |   
  
### UpdateDocument(google::cloud::dialogflow::v2::Document const &, google::protobuf::FieldMask const &, Options)

Updates the specified document. 

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)



**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::dialogflow::v2::Document const &`   
Required. The document to update.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Optional. Not specified means `update all`. Currently, only `display_name` can be updated, an InvalidArgument will be returned for attempting to update other fields.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateDocument(NoAwaitTag, google::cloud::dialogflow::v2::Document const &, google::protobuf::FieldMask const &, Options)

Updates the specified document. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`document` |  `google::cloud::dialogflow::v2::Document const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateDocument(google::cloud::dialogflow::v2::UpdateDocumentRequest const &, Options)

Updates the specified document. 

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)



**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::UpdateDocumentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.UpdateDocumentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L559). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateDocument(NoAwaitTag, google::cloud::dialogflow::v2::UpdateDocumentRequest const &, Options)

Updates the specified document. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::UpdateDocumentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateDocument(google::longrunning::Operation const &, Options)

Updates the specified document. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` |   
  
### ReloadDocument(std::string const &, std::string const &, Options)

Reloads the specified document from its specified source, content_uri or content. 

The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)



Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the document to reload. Format: `projects/<`[`Project`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html)`ID>/locations/<`[`Location`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Location.html)`ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`  
`content_uri` |  `std::string const &`   
Optional. The path of gcs source file for reloading document content. For now, only gcs uri is supported.   
For documents stored in Google Cloud Storage, these URIs must have the form `gs://<bucket-name>/<object-name>`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ReloadDocument(NoAwaitTag, std::string const &, std::string const &, Options)

Reloads the specified document from its specified source, content_uri or content. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`content_uri` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ReloadDocument(google::cloud::dialogflow::v2::ReloadDocumentRequest const &, Options)

Reloads the specified document from its specified source, content_uri or content. 

The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)



Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::ReloadDocumentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.ReloadDocumentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L572). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ReloadDocument(NoAwaitTag, google::cloud::dialogflow::v2::ReloadDocumentRequest const &, Options)

Reloads the specified document from its specified source, content_uri or content. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::ReloadDocumentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ReloadDocument(google::longrunning::Operation const &, Options)

Reloads the specified document from its specified source, content_uri or content. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` |   
  
### ExportDocument(google::cloud::dialogflow::v2::ExportDocumentRequest const &, Options)

Exports a smart messaging candidate document into the specified destination. 

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [KnowledgeOperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L645)
  * `response`: [Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260)



**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::ExportDocumentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.dialogflow.v2.ExportDocumentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L612). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.dialogflow.v2.Document](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/dialogflow/v2/document.proto#L260) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ExportDocument(NoAwaitTag, google::cloud::dialogflow::v2::ExportDocumentRequest const &, Options)

Exports a smart messaging candidate document into the specified destination. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::ExportDocumentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ExportDocument(google::longrunning::Operation const &, Options)

Exports a smart messaging candidate document into the specified destination. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::Document > >` |   
  
### ListLocations(google::cloud::location::ListLocationsRequest, Options)

Lists information about the supported locations for this service. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.location.ListLocationsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L58). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.location.Location](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L88), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetLocation(google::cloud::location::GetLocationRequest const &, Options)

Gets information about a location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.location.GetLocationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L82). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` | the result of the RPC. The response message type ([google.cloud.location.Location](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L88)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListOperations(std::string const &, std::string const &, Options)

Lists operations that match the specified filter in the request. 

If the server doesn't support this method, it returns `UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation's parent resource.   
`filter` |  `std::string const &`   
The standard list filter.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListOperations(google::longrunning::ListOperationsRequest, Options)

Lists operations that match the specified filter in the request. 

If the server doesn't support this method, it returns `UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.ListOperationsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L167). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetOperation(std::string const &, Options)

Gets the latest state of a long-running operation. 

Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` | the result of the RPC. The response message type ([google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetOperation(google::longrunning::GetOperationRequest const &, Options)

Gets the latest state of a long-running operation. 

Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.GetOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L160). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` | the result of the RPC. The response message type ([google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CancelOperation(std::string const &, Options)

Starts asynchronous cancellation on a long-running operation. 

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use [Operations.GetOperation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L70) or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L144) value with a [google.rpc.Status.code](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/rpc/status.proto#L37) of `1`, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation resource to be cancelled.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### CancelOperation(google::longrunning::CancelOperationRequest const &, Options)

Starts asynchronous cancellation on a long-running operation. 

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use [Operations.GetOperation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L70) or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L144) value with a [google.rpc.Status.code](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/rpc/status.proto#L37) of `1`, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.CancelOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L212). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
