---
url: https://docs.cloud.google.com/cpp/docs/reference/kms/latest/classgoogle_1_1cloud_1_1kms__v1_1_1KeyManagementServiceClient/
title: Class KeyManagementServiceClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:21.736633+00:00
---

# Class KeyManagementServiceClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/kms/latest/classgoogle_1_1cloud_1_1kms__v1_1_1KeyManagementServiceClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class KeyManagementServiceClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0  2.10.1 

Google Cloud Key Management Service. 

Manages cryptographic keys and operations using those keys. Implements a REST model with the following objects:

  * [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36)
  * [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)
  * [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)
  * [ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898)



If you are using manual gRPC libraries, see [Using gRPC with Cloud KMS](https://cloud.google.com/kms/docs/grpc).

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### KeyManagementServiceClient(KeyManagementServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeyManagementServiceClient const &`   
  
  
### KeyManagementServiceClient(KeyManagementServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeyManagementServiceClient &&`   
  
  
### KeyManagementServiceClient(std::shared_ptr< KeyManagementServiceConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< KeyManagementServiceConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(KeyManagementServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeyManagementServiceClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`KeyManagementServiceClient &` |   
  
### operator=(KeyManagementServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeyManagementServiceClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`KeyManagementServiceClient &` |   
  
## Functions 

### ListKeyRings(std::string const &, Options)

Lists [KeyRings](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The resource name of the location associated with the [KeyRings](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36), in the format `projects/*/locations/*`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::KeyRing >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListKeyRings(google::cloud::kms::v1::ListKeyRingsRequest, Options)

Lists [KeyRings](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ListKeyRingsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ListKeyRingsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L524). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::KeyRing >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListCryptoKeys(std::string const &, Options)

Lists [CryptoKeys](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The resource name of the [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36) to list, in the format `projects/*/locations/*/keyRings/*`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::CryptoKey >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListCryptoKeys(google::cloud::kms::v1::ListCryptoKeysRequest, Options)

Lists [CryptoKeys](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ListCryptoKeysRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ListCryptoKeysRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L563). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::CryptoKey >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListCryptoKeyVersions(std::string const &, Options)

Lists [CryptoKeyVersions](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The resource name of the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) to list, in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::CryptoKeyVersion >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListCryptoKeyVersions(google::cloud::kms::v1::ListCryptoKeyVersionsRequest, Options)

Lists [CryptoKeyVersions](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ListCryptoKeyVersionsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ListCryptoKeyVersionsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L604). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::CryptoKeyVersion >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListImportJobs(std::string const &, Options)

Lists [ImportJobs](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898). 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The resource name of the [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36) to list, in the format `projects/*/locations/*/keyRings/*`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::ImportJob >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListImportJobs(google::cloud::kms::v1::ListImportJobsRequest, Options)

Lists [ImportJobs](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ListImportJobsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ListImportJobsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L646). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::ImportJob >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListRetiredResources(std::string const &, Options)

Lists the [RetiredResources](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169) which are the records of deleted [CryptoKeys](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

RetiredResources prevent the reuse of these resource names after deletion.

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The project-specific location holding the [RetiredResources](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169), in the format `projects/*/locations/*`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::RetiredResource >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.RetiredResource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListRetiredResources(google::cloud::kms::v1::ListRetiredResourcesRequest, Options)

Lists the [RetiredResources](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169) which are the records of deleted [CryptoKeys](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

RetiredResources prevent the reuse of these resource names after deletion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ListRetiredResourcesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ListRetiredResourcesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L684). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::kms::v1::RetiredResource >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.kms.v1.RetiredResource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetKeyRing(std::string const &, Options)

Returns metadata for a given [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L45) of the [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36) to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::KeyRing >` | the result of the RPC. The response message type ([google.cloud.kms.v1.KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetKeyRing(google::cloud::kms::v1::GetKeyRingRequest const &, Options)

Returns metadata for a given [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::GetKeyRingRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.GetKeyRingRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L809). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::KeyRing >` | the result of the RPC. The response message type ([google.cloud.kms.v1.KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetCryptoKey(std::string const &, Options)

Returns metadata for a given [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59), as well as its [primary](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L133)[CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L118) of the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetCryptoKey(google::cloud::kms::v1::GetCryptoKeyRequest const &, Options)

Returns metadata for a given [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59), as well as its [primary](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L133)[CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::GetCryptoKeyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.GetCryptoKeyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L822). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetCryptoKeyVersion(std::string const &, Options)

Returns metadata for a given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L633) of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetCryptoKeyVersion(google::cloud::kms::v1::GetCryptoKeyVersionRequest const &, Options)

Returns metadata for a given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::GetCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.GetCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L835). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetPublicKey(std::string const &, Options)

Returns the public key for the given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [ASYMMETRIC_SIGN](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L84) or [ASYMMETRIC_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L91).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L633) of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) public key to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::PublicKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.PublicKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L773)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetPublicKey(google::cloud::kms::v1::GetPublicKeyRequest const &, Options)

Returns the public key for the given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [ASYMMETRIC_SIGN](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L84) or [ASYMMETRIC_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L91).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::GetPublicKeyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.GetPublicKeyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L848). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::PublicKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.PublicKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L773)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetImportJob(std::string const &, Options)

Returns metadata for a given [ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898). 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1034) of the [ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898) to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::ImportJob >` | the result of the RPC. The response message type ([google.cloud.kms.v1.ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetImportJob(google::cloud::kms::v1::GetImportJobRequest const &, Options)

Returns metadata for a given [ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::GetImportJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.GetImportJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L871). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::ImportJob >` | the result of the RPC. The response message type ([google.cloud.kms.v1.ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetRetiredResource(std::string const &, Options)

Retrieves a specific [RetiredResource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169) resource, which represents the record of a deleted [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1180) of the [RetiredResource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169) to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::RetiredResource >` | the result of the RPC. The response message type ([google.cloud.kms.v1.RetiredResource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetRetiredResource(google::cloud::kms::v1::GetRetiredResourceRequest const &, Options)

Retrieves a specific [RetiredResource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169) resource, which represents the record of a deleted [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::GetRetiredResourceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.GetRetiredResourceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L896). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::RetiredResource >` | the result of the RPC. The response message type ([google.cloud.kms.v1.RetiredResource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1169)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateKeyRing(std::string const &, std::string const &, google::cloud::kms::v1::KeyRing const &, Options)

Create a new [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36) in a given [Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) and [Location](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Location.html). 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The resource name of the location associated with the [KeyRings](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36), in the format `projects/*/locations/*`.   
`key_ring_id` |  `std::string const &`   
Required. It must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`  
`key_ring` |  `google::cloud::kms::v1::KeyRing const &`   
Required. A [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36) with initial field values.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::KeyRing >` | the result of the RPC. The response message type ([google.cloud.kms.v1.KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateKeyRing(google::cloud::kms::v1::CreateKeyRingRequest const &, Options)

Create a new [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36) in a given [Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) and [Location](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Location.html). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::CreateKeyRingRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.CreateKeyRingRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L909). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::KeyRing >` | the result of the RPC. The response message type ([google.cloud.kms.v1.KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateCryptoKey(std::string const &, std::string const &, google::cloud::kms::v1::CryptoKey const &, Options)

Create a new [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) within a [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

[CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) and [CryptoKey.version_template.algorithm](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L261) are required.

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L45) of the KeyRing associated with the [CryptoKeys](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59).   
`crypto_key_id` |  `std::string const &`   
Required. It must be unique within a KeyRing and match the regular expression `[a-zA-Z0-9_-]{1,63}`  
`crypto_key` |  `google::cloud::kms::v1::CryptoKey const &`   
Required. A [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) with initial field values.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateCryptoKey(google::cloud::kms::v1::CreateCryptoKeyRequest const &, Options)

Create a new [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) within a [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

[CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) and [CryptoKey.version_template.algorithm](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L261) are required.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::CreateCryptoKeyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.CreateCryptoKeyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L931). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateCryptoKeyVersion(std::string const &, google::cloud::kms::v1::CryptoKeyVersion const &, Options)

Create a new [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) in a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

The server will assign the next sequential id. If unset, [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will be set to [ENABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L555).

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L118) of the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) associated with the [CryptoKeyVersions](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322).   
`crypto_key_version` |  `google::cloud::kms::v1::CryptoKeyVersion const &`   
Required. A [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with initial field values.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateCryptoKeyVersion(google::cloud::kms::v1::CreateCryptoKeyVersionRequest const &, Options)

Create a new [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) in a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

The server will assign the next sequential id. If unset, [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will be set to [ENABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L555).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::CreateCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.CreateCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L973). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteCryptoKey(std::string const &, Options)

Permanently deletes the given [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

All child [CryptoKeyVersions](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) must have been previously deleted using [KeyManagementService.DeleteCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L225). The specified crypto key will be immediately and permanently deleted upon calling this method. This action cannot be undone.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L118) of the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::kms::v1::DeleteCryptoKeyMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.kms.v1.DeleteCryptoKeyMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2542) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteCryptoKey(NoAwaitTag, std::string const &, Options)

Permanently deletes the given [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

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
  
### DeleteCryptoKey(google::cloud::kms::v1::DeleteCryptoKeyRequest const &, Options)

Permanently deletes the given [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

All child [CryptoKeyVersions](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) must have been previously deleted using [KeyManagementService.DeleteCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L225). The specified crypto key will be immediately and permanently deleted upon calling this method. This action cannot be undone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::DeleteCryptoKeyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.DeleteCryptoKeyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L992). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::kms::v1::DeleteCryptoKeyMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.kms.v1.DeleteCryptoKeyMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2542) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteCryptoKey(NoAwaitTag, google::cloud::kms::v1::DeleteCryptoKeyRequest const &, Options)

Permanently deletes the given [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::kms::v1::DeleteCryptoKeyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteCryptoKey(google::longrunning::Operation const &, Options)

Permanently deletes the given [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::kms::v1::DeleteCryptoKeyMetadata > >` |   
  
### DeleteCryptoKeyVersion(std::string const &, Options)

Permanently deletes the given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

Only possible if the version has not been previously imported and if its [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) is one of [DESTROYED][CryptoKeyVersionState.DESTROYED], [IMPORT_FAILED][CryptoKeyVersionState.IMPORT_FAILED], or [GENERATION_FAILED][CryptoKeyVersionState.GENERATION_FAILED]. Successfully imported [CryptoKeyVersions](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) cannot be deleted at this time. The specified version will be immediately and permanently deleted upon calling this method. This action cannot be undone.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L633) of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::kms::v1::DeleteCryptoKeyVersionMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.kms.v1.DeleteCryptoKeyVersionMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2558) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteCryptoKeyVersion(NoAwaitTag, std::string const &, Options)

Permanently deletes the given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

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
  
### DeleteCryptoKeyVersion(google::cloud::kms::v1::DeleteCryptoKeyVersionRequest const &, Options)

Permanently deletes the given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

Only possible if the version has not been previously imported and if its [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) is one of [DESTROYED][CryptoKeyVersionState.DESTROYED], [IMPORT_FAILED][CryptoKeyVersionState.IMPORT_FAILED], or [GENERATION_FAILED][CryptoKeyVersionState.GENERATION_FAILED]. Successfully imported [CryptoKeyVersions](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) cannot be deleted at this time. The specified version will be immediately and permanently deleted upon calling this method. This action cannot be undone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::DeleteCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.DeleteCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1005). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::kms::v1::DeleteCryptoKeyVersionMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.kms.v1.DeleteCryptoKeyVersionMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2558) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteCryptoKeyVersion(NoAwaitTag, google::cloud::kms::v1::DeleteCryptoKeyVersionRequest const &, Options)

Permanently deletes the given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::kms::v1::DeleteCryptoKeyVersionRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteCryptoKeyVersion(google::longrunning::Operation const &, Options)

Permanently deletes the given [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::kms::v1::DeleteCryptoKeyVersionMetadata > >` |   
  
### ImportCryptoKeyVersion(google::cloud::kms::v1::ImportCryptoKeyVersionRequest const &, Options)

Import wrapped key material into a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322). 

All requests must specify a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). If a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ImportCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ImportCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1018). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ImportTrustedKeyWrappedCryptoKeyVersion(google::cloud::kms::v1::ImportTrustedKeyWrappedCryptoKeyVersionRequest const &, Options)

Import wrapped key material into a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with a trusted key. 

All requests must specify a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). If a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59).

The [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) will have trusted_wrapping_enabled set to true.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ImportTrustedKeyWrappedCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ImportTrustedKeyWrappedCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1137). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ExportTrustedKeyWrappedCryptoKeyVersion(google::cloud::kms::v1::ExportTrustedKeyWrappedCryptoKeyVersionRequest const &, Options)

Exports a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with a trusted key. 

The [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) must have trusted_wrapping_enabled set to true. The [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) of the [wrapping_key] must have the [AES_WRAPPING](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L112) purpose. The [wrapping_key] must have the [AES_256_KWP](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L538) algorithm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::ExportTrustedKeyWrappedCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1184). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::ExportTrustedKeyWrappedCryptoKeyVersionResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1212)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateImportJob(std::string const &, std::string const &, google::cloud::kms::v1::ImportJob const &, Options)

Create a new [ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898) within a [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

[ImportJob.import_method](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1038) is required.

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L45) of the [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36) associated with the [ImportJobs](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898).   
`import_job_id` |  `std::string const &`   
Required. It must be unique within a KeyRing and match the regular expression `[a-zA-Z0-9_-]{1,63}`  
`import_job` |  `google::cloud::kms::v1::ImportJob const &`   
Required. An [ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898) with initial field values.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::ImportJob >` | the result of the RPC. The response message type ([google.cloud.kms.v1.ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateImportJob(google::cloud::kms::v1::CreateImportJobRequest const &, Options)

Create a new [ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898) within a [KeyRing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L36). 

[ImportJob.import_method](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1038) is required.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::CreateImportJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.CreateImportJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1235). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::ImportJob >` | the result of the RPC. The response message type ([google.cloud.kms.v1.ImportJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L898)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateCryptoKey(google::cloud::kms::v1::CryptoKey const &, google::protobuf::FieldMask const &, Options)

Update a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

**Parameters**  
---  
**Name** | **Description**  
`crypto_key` |  `google::cloud::kms::v1::CryptoKey const &`   
Required. [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) with updated values.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Required. List of fields to be updated in this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateCryptoKey(google::cloud::kms::v1::UpdateCryptoKeyRequest const &, Options)

Update a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::UpdateCryptoKeyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.UpdateCryptoKeyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1257). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateCryptoKeyVersion(google::cloud::kms::v1::CryptoKeyVersion const &, google::protobuf::FieldMask const &, Options)

Update a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)'s metadata. 

[state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) may be changed between [ENABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L555) and [DISABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L561) using this method. See [DestroyCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L372) and [RestoreCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L390) to move between other states.

**Parameters**  
---  
**Name** | **Description**  
`crypto_key_version` |  `google::cloud::kms::v1::CryptoKeyVersion const &`   
Required. [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with updated values.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Required. List of fields to be updated in this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateCryptoKeyVersion(google::cloud::kms::v1::UpdateCryptoKeyVersionRequest const &, Options)

Update a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)'s metadata. 

[state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) may be changed between [ENABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L555) and [DISABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L561) using this method. See [DestroyCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L372) and [RestoreCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L390) to move between other states.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::UpdateCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.UpdateCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1268). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateCryptoKeyPrimaryVersion(std::string const &, std::string const &, Options)

Update the version of a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) that will be used in [Encrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L403). 

Returns an error if called on a key whose purpose is not [ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L77).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) to update.   
`crypto_key_version_id` |  `std::string const &`   
Required. The id of the child [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to use as primary.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateCryptoKeyPrimaryVersion(google::cloud::kms::v1::UpdateCryptoKeyPrimaryVersionRequest const &, Options)

Update the version of a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) that will be used in [Encrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L403). 

Returns an error if called on a key whose purpose is not [ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L77).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::UpdateCryptoKeyPrimaryVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.UpdateCryptoKeyPrimaryVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1281). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKey >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DestroyCryptoKeyVersion(std::string const &, Options)

Schedule a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) for destruction. 

Upon calling this method, [CryptoKeyVersion.state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will be set to [DESTROY_SCHEDULED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L578), and [destroy_time](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L676) will be set to the time [destroy_scheduled_duration](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L199) in the future. At that time, the [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will automatically change to [DESTROYED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L570), and the key material will be irrevocably destroyed.

Before the [destroy_time](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L676) is reached, [RestoreCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L390) may be called to reverse the process.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to destroy.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DestroyCryptoKeyVersion(google::cloud::kms::v1::DestroyCryptoKeyVersionRequest const &, Options)

Schedule a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) for destruction. 

Upon calling this method, [CryptoKeyVersion.state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will be set to [DESTROY_SCHEDULED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L578), and [destroy_time](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L676) will be set to the time [destroy_scheduled_duration](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L199) in the future. At that time, the [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will automatically change to [DESTROYED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L570), and the key material will be irrevocably destroyed.

Before the [destroy_time](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L676) is reached, [RestoreCryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L390) may be called to reverse the process.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::DestroyCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.DestroyCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1298). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RestoreCryptoKeyVersion(std::string const &, Options)

Restore a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) in the [DESTROY_SCHEDULED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L578) state. 

Upon restoration of the CryptoKeyVersion, [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will be set to [DISABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L561), and [destroy_time](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L676) will be cleared.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to restore.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RestoreCryptoKeyVersion(google::cloud::kms::v1::RestoreCryptoKeyVersionRequest const &, Options)

Restore a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) in the [DESTROY_SCHEDULED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L578) state. 

Upon restoration of the CryptoKeyVersion, [state](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L637) will be set to [DISABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L561), and [destroy_time](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L676) will be cleared.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::RestoreCryptoKeyVersionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.RestoreCryptoKeyVersionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1311). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::CryptoKeyVersion >` | the result of the RPC. The response message type ([google.cloud.kms.v1.CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### Encrypt(std::string const &, std::string const &, Options)

Encrypts data, so that it can only be recovered by a call to [Decrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L415). 

The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L77).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) or [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to use for encryption.   
If a [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) is specified, the server will use its [primary version](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L133).   
`plaintext` |  `std::string const &`   
Required. The data to encrypt. Must be no larger than 64KiB.   
The maximum size depends on the key version's [protection_level](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L249). For [SOFTWARE](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1207), [EXTERNAL](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1213), and [EXTERNAL_VPC](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1216) keys, the plaintext must be no larger than 64KiB. For [HSM](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1210) keys, the combined length of the plaintext and additional_authenticated_data fields must be no larger than 8KiB.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::EncryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.EncryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1937)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### Encrypt(google::cloud::kms::v1::EncryptRequest const &, Options)

Encrypts data, so that it can only be recovered by a call to [Decrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L415). 

The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L77).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::EncryptRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.EncryptRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1324). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::EncryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.EncryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1937)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### Decrypt(std::string const &, std::string const &, Options)

Decrypts data that was protected by [Encrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L403). 

The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L77).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L59) to use for decryption. The server will choose the appropriate version.   
`ciphertext` |  `std::string const &`   
Required. The encrypted data originally returned in [EncryptResponse.ciphertext](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1945).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::DecryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.DecryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2002)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### Decrypt(google::cloud::kms::v1::DecryptRequest const &, Options)

Decrypts data that was protected by [Encrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L403). 

The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L77).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::DecryptRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.DecryptRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1413). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::DecryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.DecryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2002)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RawEncrypt(google::cloud::kms::v1::RawEncryptRequest const &, Options)

Encrypts data using portable cryptographic primitives. 

Most users should choose [Encrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L403) and [Decrypt](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L415) rather than their raw counterparts. The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [RAW_ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L98).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::RawEncryptRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.RawEncryptRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1480). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::RawEncryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.RawEncryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2037)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RawDecrypt(google::cloud::kms::v1::RawDecryptRequest const &, Options)

Decrypts data that was originally encrypted using a raw cryptographic mechanism. 

The [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) must be [RAW_ENCRYPT_DECRYPT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L98).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::RawDecryptRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.RawDecryptRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1580). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::RawDecryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.RawDecryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2136)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AsymmetricSign(std::string const &, google::cloud::kms::v1::Digest const &, Options)

Signs data using a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from [GetPublicKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L132). 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to use for signing.   
`digest` |  `google::cloud::kms::v1::Digest const &`   
Optional. The digest of the data to sign. The digest must be produced with the same digest algorithm as specified by the key version's [algorithm](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L649).   
This field may not be supplied if [AsymmetricSignRequest.data](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1709) is supplied.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::AsymmetricSignResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.AsymmetricSignResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2210)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AsymmetricSign(google::cloud::kms::v1::AsymmetricSignRequest const &, Options)

Signs data using a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from [GetPublicKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L132). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::AsymmetricSignRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.AsymmetricSignRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1663). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::AsymmetricSignResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.AsymmetricSignResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2210)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AsymmetricDecrypt(std::string const &, std::string const &, Options)

Decrypts data that was encrypted with a public key retrieved from [GetPublicKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L132) corresponding to a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) ASYMMETRIC_DECRYPT. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to use for decryption.   
`ciphertext` |  `std::string const &`   
Required. The data encrypted with the named [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322)'s public key using OAEP.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::AsymmetricDecryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.AsymmetricDecryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2273)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AsymmetricDecrypt(google::cloud::kms::v1::AsymmetricDecryptRequest const &, Options)

Decrypts data that was encrypted with a public key retrieved from [GetPublicKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L132) corresponding to a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) ASYMMETRIC_DECRYPT. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::AsymmetricDecryptRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.AsymmetricDecryptRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1736). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::AsymmetricDecryptResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.AsymmetricDecryptResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2273)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### MacSign(std::string const &, std::string const &, Options)

Signs data using a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) MAC, producing a tag that can be verified by another source with the same key. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to use for signing.   
`data` |  `std::string const &`   
Required. The data to sign. The MAC tag is computed over this data field based on the specific algorithm.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::MacSignResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.MacSignResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2316)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### MacSign(google::cloud::kms::v1::MacSignRequest const &, Options)

Signs data using a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) MAC, producing a tag that can be verified by another source with the same key. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::MacSignRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.MacSignRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1777). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::MacSignResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.MacSignResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2316)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### MacVerify(std::string const &, std::string const &, std::string const &, Options)

Verifies MAC tag using a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) MAC, and returns a response that indicates whether or not the verification was successful. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) to use for verification.   
`data` |  `std::string const &`   
Required. The data used previously as a [MacSignRequest.data](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1790) to generate the MAC tag.   
`mac` |  `std::string const &`   
Required. The signature to verify.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::MacVerifyResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.MacVerifyResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2363)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### MacVerify(google::cloud::kms::v1::MacVerifyRequest const &, Options)

Verifies MAC tag using a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) MAC, and returns a response that indicates whether or not the verification was successful. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::MacVerifyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.MacVerifyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1815). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::MacVerifyResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.MacVerifyResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2363)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### Decapsulate(google::cloud::kms::v1::DecapsulateRequest const &, Options)

Decapsulates data that was encapsulated with a public key retrieved from [GetPublicKey](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L132) corresponding to a [CryptoKeyVersion](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L322) with [CryptoKey.purpose](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L137) KEY_ENCAPSULATION. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::DecapsulateRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.DecapsulateRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1878). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::DecapsulateResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.DecapsulateResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2422)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GenerateRandomBytes(std::string const &, std::int32_t, google::cloud::kms::v1::ProtectionLevel, Options)

Generate random bytes using the Cloud KMS randomness source in the provided location. 

**Parameters**  
---  
**Name** | **Description**  
`location` |  `std::string const &`   
The project-specific location in which to generate random bytes. For example, "projects/my-project/locations/us-central1".   
`length_bytes` |  `std::int32_t`   
The length in bytes of the amount of randomness to retrieve. Minimum 8 bytes, maximum 1024 bytes.   
`protection_level` |  `google::cloud::kms::v1::ProtectionLevel`   
The [ProtectionLevel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1202) to use when generating the random data. Currently, only [HSM](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/resources.proto#L1210) protection level is supported.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::GenerateRandomBytesResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.GenerateRandomBytesResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2476)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GenerateRandomBytes(google::cloud::kms::v1::GenerateRandomBytesRequest const &, Options)

Generate random bytes using the Cloud KMS randomness source in the provided location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::kms::v1::GenerateRandomBytesRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.kms.v1.GenerateRandomBytesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L1919). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::kms::v1::GenerateRandomBytesResponse >` | the result of the RPC. The response message type ([google.cloud.kms.v1.GenerateRandomBytesResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/kms/v1/service.proto#L2476)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
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
  
### SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &, Options)

Sets the access control policy on the specified resource. 

Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.iam.v1.SetIamPolicyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L100). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | the result of the RPC. The response message type ([google.iam.v1.Policy](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/policy.proto#L102)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &, Options)

Gets the access control policy for a resource. 

Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.iam.v1.GetIamPolicyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L123). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | the result of the RPC. The response message type ([google.iam.v1.Policy](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/policy.proto#L102)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.iam.v1.TestIamPermissionsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L137). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::TestIamPermissionsResponse >` | the result of the RPC. The response message type ([google.iam.v1.TestIamPermissionsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L153)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
