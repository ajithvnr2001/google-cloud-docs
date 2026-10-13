---
url: https://docs.cloud.google.com/cpp/docs/reference/datacatalog/latest/classgoogle_1_1cloud_1_1datacatalog__v1_1_1DataCatalogClient/
title: Class DataCatalogClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:49.432059+00:00
---

# Class DataCatalogClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/datacatalog/latest/classgoogle_1_1cloud_1_1datacatalog__v1_1_1DataCatalogClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class DataCatalogClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Deprecated: Please use Dataplex Catalog instead. 

Data Catalog API service allows you to discover, understand, and manage your data.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### DataCatalogClient(DataCatalogClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataCatalogClient const &`   
  
  
### DataCatalogClient(DataCatalogClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataCatalogClient &&`   
  
  
### DataCatalogClient(std::shared_ptr< DataCatalogConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< DataCatalogConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(DataCatalogClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataCatalogClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`DataCatalogClient &` |   
  
### operator=(DataCatalogClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataCatalogClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`DataCatalogClient &` |   
  
## Functions 

### SearchCatalog(google::cloud::datacatalog::v1::SearchCatalogRequest::Scope const &, std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Searches Data Catalog for multiple resources like entries and tags that match a query.

This is a [Custom Method](about:invalid#zCSafez) that doesn't return all information on a resource, only its ID and high level fields. To get more information, you can subsequently call specific get methods.

Note: Data Catalog search queries don't guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, returned (and not returned) results can vary if you repeat search queries.

For more information, see [Data Catalog search syntax](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`scope` |  `google::cloud::datacatalog::v1::SearchCatalogRequest::Scope const &`   
Required. The scope of this search request.   
The `scope` is invalid if `include_org_ids`, `include_project_ids` are empty AND `include_gcp_public_datasets` is set to `false`. In this case, the request returns an error.   
`query` |  `std::string const &`   
Optional. The query string with a minimum of 3 characters and specific syntax. For more information, see [Data Catalog search syntax](https://cloud.google.com/data-catalog/docs/how-to/search-reference).   
An empty query string returns all data assets (in the specified scope) that you have access to.   
A query string can be a simple `xyz` or qualified by predicates:   


  * `name:x`
  * `column:y`
  * `description:z`

  
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::SearchCatalogResult >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.SearchCatalogResult](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/search.proto#L33), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SearchCatalog(google::cloud::datacatalog::v1::SearchCatalogRequest, Options)

**Deprecated:** This RPC is deprecated. 

Searches Data Catalog for multiple resources like entries and tags that match a query.

This is a [Custom Method](about:invalid#zCSafez) that doesn't return all information on a resource, only its ID and high level fields. To get more information, you can subsequently call specific get methods.

Note: Data Catalog search queries don't guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, returned (and not returned) results can vary if you repeat search queries.

For more information, see [Data Catalog search syntax](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::SearchCatalogRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.SearchCatalogRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L712). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::SearchCatalogResult >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.SearchCatalogResult](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/search.proto#L33), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateEntryGroup(std::string const &, std::string const &, google::cloud::datacatalog::v1::EntryGroup const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates an entry group.

An entry group contains logically related entries together with [Cloud Identity and Access Management](https://docs.cloud.google.com/data-catalog/docs/concepts/iam) policies. These policies specify users who can create, edit, and view entries within entry groups.

Data Catalog automatically creates entry groups with names that start with the `@` symbol for the following resources:

  * BigQuery entries (`@bigquery`)
  * Pub/Sub topics (`@pubsub`)
  * Dataproc Metastore services (`@dataproc_metastore_{SERVICE_NAME_HASH}`)



You can create your own entry groups for Cloud Storage fileset entries and custom entries together with the corresponding IAM policies. User-created entry groups can't contain the `@` symbol, it is reserved for automatically created groups.

Entry groups, like entries, can be searched.

A maximum of 10,000 entry groups may be created per organization across all locations.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The names of the project and location that the new entry group belongs to.   
Note: The entry group itself and its child resources might not be stored in the location specified in its name.   
`entry_group_id` |  `std::string const &`   
Required. The ID of the entry group to create.   
The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and must start with a letter or underscore. The maximum size is 64 bytes when encoded in UTF-8.   
`entry_group` |  `google::cloud::datacatalog::v1::EntryGroup const &`   
The entry group to create. Defaults to empty.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateEntryGroup(google::cloud::datacatalog::v1::CreateEntryGroupRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates an entry group.

An entry group contains logically related entries together with [Cloud Identity and Access Management](https://docs.cloud.google.com/data-catalog/docs/concepts/iam) policies. These policies specify users who can create, edit, and view entries within entry groups.

Data Catalog automatically creates entry groups with names that start with the `@` symbol for the following resources:

  * BigQuery entries (`@bigquery`)
  * Pub/Sub topics (`@pubsub`)
  * Dataproc Metastore services (`@dataproc_metastore_{SERVICE_NAME_HASH}`)



You can create your own entry groups for Cloud Storage fileset entries and custom entries together with the corresponding IAM policies. User-created entry groups can't contain the `@` symbol, it is reserved for automatically created groups.

Entry groups, like entries, can be searched.

A maximum of 10,000 entry groups may be created per organization across all locations.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::CreateEntryGroupRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.CreateEntryGroupRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L847). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetEntryGroup(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets an entry group.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the entry group to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetEntryGroup(std::string const &, google::protobuf::FieldMask const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets an entry group.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the entry group to get.   
`read_mask` |  `google::protobuf::FieldMask const &`   
The fields to return. If empty or omitted, all fields are returned.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetEntryGroup(google::cloud::datacatalog::v1::GetEntryGroupRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets an entry group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::GetEntryGroupRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.GetEntryGroupRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L887). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateEntryGroup(google::cloud::datacatalog::v1::EntryGroup const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an entry group.

You must enable the Data Catalog API in the project identified by the `entry_group.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`entry_group` |  `google::cloud::datacatalog::v1::EntryGroup const &`   
Required. Updates for the entry group. The `name` field must be set.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateEntryGroup(google::cloud::datacatalog::v1::EntryGroup const &, google::protobuf::FieldMask const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an entry group.

You must enable the Data Catalog API in the project identified by the `entry_group.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`entry_group` |  `google::cloud::datacatalog::v1::EntryGroup const &`   
Required. Updates for the entry group. The `name` field must be set.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Names of fields whose values to overwrite on an entry group.   
If this parameter is absent or empty, all modifiable fields are overwritten. If such fields are non-required and omitted in the request body, their values are emptied.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateEntryGroup(google::cloud::datacatalog::v1::UpdateEntryGroupRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an entry group.

You must enable the Data Catalog API in the project identified by the `entry_group.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::UpdateEntryGroupRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.UpdateEntryGroupRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L873). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryGroup >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteEntryGroup(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes an entry group.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the entry group to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteEntryGroup(google::cloud::datacatalog::v1::DeleteEntryGroupRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes an entry group.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::DeleteEntryGroupRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.DeleteEntryGroupRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L902). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### ListEntryGroups(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Lists entry groups.

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The name of the location that contains the entry groups to list.   
Can be provided as a URL.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::EntryGroup >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListEntryGroups(google::cloud::datacatalog::v1::ListEntryGroupsRequest, Options)

**Deprecated:** This RPC is deprecated. 

Lists entry groups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::ListEntryGroupsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.ListEntryGroupsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L917). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::EntryGroup >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateEntry(std::string const &, std::string const &, google::cloud::datacatalog::v1::Entry const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates an entry.

You can create entries only with 'FILESET', 'CLUSTER', 'DATA_STREAM', or custom types. Data Catalog automatically creates entries with other types during metadata ingestion from integrated systems.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

An entry group can have a maximum of 100,000 entries.

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The name of the entry group this entry belongs to.   
Note: The entry itself and its child resources might not be stored in the location specified in its name.   
`entry_id` |  `std::string const &`   
Required. The ID of the entry to create.   
The ID must contain only letters (a-z, A-Z), numbers (0-9), and underscores (_). The maximum size is 64 bytes when encoded in UTF-8.   
`entry` |  `google::cloud::datacatalog::v1::Entry const &`   
Required. The entry to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateEntry(google::cloud::datacatalog::v1::CreateEntryRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates an entry.

You can create entries only with 'FILESET', 'CLUSTER', 'DATA_STREAM', or custom types. Data Catalog automatically creates entries with other types during metadata ingestion from integrated systems.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

An entry group can have a maximum of 100,000 entries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::CreateEntryRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.CreateEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L952). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateEntry(google::cloud::datacatalog::v1::Entry const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an existing entry.

You must enable the Data Catalog API in the project identified by the `entry.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`entry` |  `google::cloud::datacatalog::v1::Entry const &`   
Required. Updates for the entry. The `name` field must be set.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateEntry(google::cloud::datacatalog::v1::Entry const &, google::protobuf::FieldMask const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an existing entry.

You must enable the Data Catalog API in the project identified by the `entry.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`entry` |  `google::cloud::datacatalog::v1::Entry const &`   
Required. Updates for the entry. The `name` field must be set.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Names of fields whose values to overwrite on an entry.   
For more information, see [UpdateEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L977).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateEntry(google::cloud::datacatalog::v1::UpdateEntryRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an existing entry.

You must enable the Data Catalog API in the project identified by the `entry.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::UpdateEntryRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.UpdateEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L977). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteEntry(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes an existing entry.

You can delete only the entries created by the [CreateEntry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L185) method.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the entry to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteEntry(google::cloud::datacatalog::v1::DeleteEntryRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes an existing entry.

You can delete only the entries created by the [CreateEntry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L185) method.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::DeleteEntryRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.DeleteEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1015). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### GetEntry(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets an entry.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the entry to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetEntry(google::cloud::datacatalog::v1::GetEntryRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets an entry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::GetEntryRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.GetEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1027). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### LookupEntry(google::cloud::datacatalog::v1::LookupEntryRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets an entry by its target resource name.

The resource name comes from the source Google Cloud Platform service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::LookupEntryRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.LookupEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1039). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Entry >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListEntries(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Lists entries.

Note: Currently, this method can list only custom entries. To get a list of both custom and automatically created entries, use [SearchCatalog](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L78).

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The name of the entry group that contains the entries to list.   
Can be provided in URL format.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::Entry >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListEntries(google::cloud::datacatalog::v1::ListEntriesRequest, Options)

**Deprecated:** This RPC is deprecated. 

Lists entries.

Note: Currently, this method can list only custom entries. To get a list of both custom and automatically created entries, use [SearchCatalog](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L78).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::ListEntriesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.ListEntriesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2123). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::Entry >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ModifyEntryOverview(google::cloud::datacatalog::v1::ModifyEntryOverviewRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Modifies entry overview, part of the business context of an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109).

To call this method, you must have the `datacatalog.entries.updateOverview` IAM permission on the corresponding project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::ModifyEntryOverviewRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.ModifyEntryOverviewRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2264). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::EntryOverview >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.EntryOverview](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1721)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ModifyEntryContacts(google::cloud::datacatalog::v1::ModifyEntryContactsRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Modifies contacts, part of the business context of an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109).

To call this method, you must have the `datacatalog.entries.updateContacts` IAM permission on the corresponding project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::ModifyEntryContactsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.ModifyEntryContactsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2279). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Contacts >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Contacts](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1733)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateTagTemplate(std::string const &, std::string const &, google::cloud::datacatalog::v1::TagTemplate const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates a tag template.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The name of the project and the template location [region](https://cloud.google.com/data-catalog/docs/concepts/regions).   
`tag_template_id` |  `std::string const &`   
Required. The ID of the tag template to create.   
The ID must contain only lowercase letters (a-z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum size is 64 bytes when encoded in UTF-8.   
`tag_template` |  `google::cloud::datacatalog::v1::TagTemplate const &`   
Required. The tag template to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplate >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplate](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L147)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateTagTemplate(google::cloud::datacatalog::v1::CreateTagTemplateRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates a tag template.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::CreateTagTemplateRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.CreateTagTemplateRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1787). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplate >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplate](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L147)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTagTemplate(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets a tag template.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the tag template to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplate >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplate](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L147)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTagTemplate(google::cloud::datacatalog::v1::GetTagTemplateRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets a tag template.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::GetTagTemplateRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.GetTagTemplateRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1810). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplate >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplate](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L147)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTagTemplate(google::cloud::datacatalog::v1::TagTemplate const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates a tag template.

You can't update template fields with this method. These fields are separate resources with their own create, update, and delete methods.

You must enable the Data Catalog API in the project identified by the `tag_template.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`tag_template` |  `google::cloud::datacatalog::v1::TagTemplate const &`   
Required. The template to update. The `name` field must be set.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplate >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplate](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L147)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTagTemplate(google::cloud::datacatalog::v1::TagTemplate const &, google::protobuf::FieldMask const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates a tag template.

You can't update template fields with this method. These fields are separate resources with their own create, update, and delete methods.

You must enable the Data Catalog API in the project identified by the `tag_template.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`tag_template` |  `google::cloud::datacatalog::v1::TagTemplate const &`   
Required. The template to update. The `name` field must be set.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Names of fields whose values to overwrite on a tag template. Currently, only `display_name` and `is_publicly_readable` can be overwritten.   
If this parameter is absent or empty, all modifiable fields are overwritten. If such fields are non-required and omitted in the request body, their values are emptied.   
Note: Updating the `is_publicly_readable` field may require up to 12 hours to take effect in search results.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplate >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplate](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L147)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTagTemplate(google::cloud::datacatalog::v1::UpdateTagTemplateRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates a tag template.

You can't update template fields with this method. These fields are separate resources with their own create, update, and delete methods.

You must enable the Data Catalog API in the project identified by the `tag_template.name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::UpdateTagTemplateRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.UpdateTagTemplateRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1822). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplate >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplate](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L147)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteTagTemplate(std::string const &, bool, Options)

**Deprecated:** This RPC is deprecated. 

Deletes a tag template and all tags that use it.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the tag template to delete.   
`force` |  `bool`   
Required. If true, deletes all tags that use this template.   
Currently, `true` is the only supported value.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteTagTemplate(google::cloud::datacatalog::v1::DeleteTagTemplateRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes a tag template and all tags that use it.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::DeleteTagTemplateRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.DeleteTagTemplateRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1840). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### CreateTagTemplateField(std::string const &, std::string const &, google::cloud::datacatalog::v1::TagTemplateField const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates a field in a tag template.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The name of the project and the template location [region](https://cloud.google.com/data-catalog/docs/concepts/regions).   
`tag_template_field_id` |  `std::string const &`   
Required. The ID of the tag template field to create.   
Note: Adding a required field to an existing template is _not_ allowed.   
Field IDs can contain letters (both uppercase and lowercase), numbers (0-9), underscores (_) and dashes (-). Field IDs must be at least 1 character long and at most 128 characters long. Field IDs must also be unique within their template.   
`tag_template_field` |  `google::cloud::datacatalog::v1::TagTemplateField const &`   
Required. The tag template field to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateTagTemplateField(google::cloud::datacatalog::v1::CreateTagTemplateFieldRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates a field in a tag template.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::CreateTagTemplateFieldRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.CreateTagTemplateFieldRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1905). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTagTemplateField(std::string const &, google::cloud::datacatalog::v1::TagTemplateField const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates a field in a tag template.

You can't update the field type with this method.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the tag template field.   
`tag_template_field` |  `google::cloud::datacatalog::v1::TagTemplateField const &`   
Required. The template to update.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTagTemplateField(std::string const &, google::cloud::datacatalog::v1::TagTemplateField const &, google::protobuf::FieldMask const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates a field in a tag template.

You can't update the field type with this method.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the tag template field.   
`tag_template_field` |  `google::cloud::datacatalog::v1::TagTemplateField const &`   
Required. The template to update.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Optional. Names of fields whose values to overwrite on an individual field of a tag template. The following fields are modifiable:   


  * `display_name`
  * `type.enum_type`
  * `is_required`  
If this parameter is absent or empty, all modifiable fields are overwritten. If such fields are non-required and omitted in the request body, their values are emptied with one exception: when updating an enum type, the provided values are merged with the existing values. Therefore, enum values can only be added, existing enum values cannot be deleted or renamed.   
Additionally, updating a template field from optional to required is _not_ allowed. 

  
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTagTemplateField(google::cloud::datacatalog::v1::UpdateTagTemplateFieldRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates a field in a tag template.

You can't update the field type with this method.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::UpdateTagTemplateFieldRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.UpdateTagTemplateFieldRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1932). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RenameTagTemplateField(std::string const &, std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Renames a field in a tag template.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the tag template field.   
`new_tag_template_field_id` |  `std::string const &`   
Required. The new ID of this tag template field. For example, `my_new_field`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RenameTagTemplateField(google::cloud::datacatalog::v1::RenameTagTemplateFieldRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Renames a field in a tag template.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](about:invalid#zCSafez).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::RenameTagTemplateFieldRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.RenameTagTemplateFieldRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1967). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RenameTagTemplateFieldEnumValue(std::string const &, std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Renames an enum value in a tag template.

Within a single enum field, enum values must be unique.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the enum field value.   
`new_enum_value_display_name` |  `std::string const &`   
Required. The new display name of the enum value. For example, `my_new_enum_value`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RenameTagTemplateFieldEnumValue(google::cloud::datacatalog::v1::RenameTagTemplateFieldEnumValueRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Renames an enum value in a tag template.

Within a single enum field, enum values must be unique.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::RenameTagTemplateFieldEnumValueRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.RenameTagTemplateFieldEnumValueRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1983). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::TagTemplateField >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.TagTemplateField](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L211)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteTagTemplateField(std::string const &, bool, Options)

**Deprecated:** This RPC is deprecated. 

Deletes a field in a tag template and all uses of this field from the tags based on this template.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the tag template field to delete.   
`force` |  `bool`   
Required. If true, deletes this field from any tags that use it.   
Currently, `true` is the only supported value.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteTagTemplateField(google::cloud::datacatalog::v1::DeleteTagTemplateFieldRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes a field in a tag template and all uses of this field from the tags based on this template.

You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::DeleteTagTemplateFieldRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.DeleteTagTemplateFieldRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2000). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### CreateTag(std::string const &, google::cloud::datacatalog::v1::Tag const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates a tag and assigns it to:

  * An [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109) if the method name is `projects.locations.entryGroups.entries.tags.create`.
  * Or [EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)if the method name is `projects.locations.entryGroups.tags.create`.



Note: The project identified by the `parent` parameter for the [tag](about:invalid#zCSafez) and the [tag template](about:invalid#zCSafez) used to create the tag must be in the same organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The name of the resource to attach this tag to.   
Tags can be attached to entries or entry groups. An entry can have up to 1000 attached tags.   
Note: The tag and its child resources might not be stored in the location specified in its name.   
`tag` |  `google::cloud::datacatalog::v1::Tag const &`   
Required. The tag to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Tag >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Tag](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateTag(google::cloud::datacatalog::v1::CreateTagRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Creates a tag and assigns it to:

  * An [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109) if the method name is `projects.locations.entryGroups.entries.tags.create`.
  * Or [EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752)if the method name is `projects.locations.entryGroups.tags.create`.



Note: The project identified by the `parent` parameter for the [tag](about:invalid#zCSafez) and the [tag template](about:invalid#zCSafez) used to create the tag must be in the same organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::CreateTagRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.CreateTagRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1857). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Tag >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Tag](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTag(google::cloud::datacatalog::v1::Tag const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an existing tag.

**Parameters**  
---  
**Name** | **Description**  
`tag` |  `google::cloud::datacatalog::v1::Tag const &`   
Required. The updated tag. The "name" field must be set.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Tag >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Tag](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTag(google::cloud::datacatalog::v1::Tag const &, google::protobuf::FieldMask const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an existing tag.

**Parameters**  
---  
**Name** | **Description**  
`tag` |  `google::cloud::datacatalog::v1::Tag const &`   
Required. The updated tag. The "name" field must be set.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Names of fields whose values to overwrite on a tag. Currently, a tag has the only modifiable field with the name `fields`.   
In general, if this parameter is absent or empty, all modifiable fields are overwritten. If such fields are non-required and omitted in the request body, their values are emptied.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Tag >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Tag](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTag(google::cloud::datacatalog::v1::UpdateTagRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Updates an existing tag.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::UpdateTagRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.UpdateTagRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1878). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::Tag >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.Tag](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteTag(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the tag to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteTag(google::cloud::datacatalog::v1::DeleteTagRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::DeleteTagRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.DeleteTagRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1893). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### ListTags(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Lists tags assigned to an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109). The [columns](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L72) in the response are lowercased.

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The name of the Data Catalog resource to list the tags of.   
The resource can be an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109) or an [EntryGroup](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1752) (without `/entries/{entries}` at the end).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::Tag >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.Tag](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L36), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListTags(google::cloud::datacatalog::v1::ListTagsRequest, Options)

**Deprecated:** This RPC is deprecated. 

Lists tags assigned to an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109). The [columns](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L72) in the response are lowercased.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::ListTagsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.ListTagsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2017). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::datacatalog::v1::Tag >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.datacatalog.v1.Tag](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/tags.proto#L36), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ReconcileTags(google::cloud::datacatalog::v1::ReconcileTagsRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

`ReconcileTags` creates or updates a list of tags on the entry. If the [ReconcileTagsRequest.force_delete_missing](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2071) parameter is set, the operation deletes tags not included in the input tag list.

`ReconcileTags` returns a [long-running operation] [google.longrunning.Operation] resource that can be queried with [Operations.GetOperation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L70) to return [ReconcileTagsMetadata] [google.cloud.datacatalog.v1.ReconcileTagsMetadata] and a [ReconcileTagsResponse] [google.cloud.datacatalog.v1.ReconcileTagsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2083) message.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::ReconcileTagsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.ReconcileTagsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2051). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::datacatalog::v1::ReconcileTagsResponse > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.datacatalog.v1.ReconcileTagsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ReconcileTags(NoAwaitTag, google::cloud::datacatalog::v1::ReconcileTagsRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::datacatalog::v1::ReconcileTagsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ReconcileTags(google::longrunning::Operation const &, Options)

**Deprecated:** This RPC is deprecated. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::datacatalog::v1::ReconcileTagsResponse > >` |   
  
### StarEntry(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Marks an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109) as starred by the current user. Starring information is private to each user.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the entry to mark as starred.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::StarEntryResponse >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.StarEntryResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2176)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### StarEntry(google::cloud::datacatalog::v1::StarEntryRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Marks an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109) as starred by the current user. Starring information is private to each user.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::StarEntryRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.StarEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2163). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::StarEntryResponse >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.StarEntryResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2176)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UnstarEntry(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Marks an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109) as NOT starred by the current user. Starring information is private to each user.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the entry to mark as **not** starred.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::UnstarEntryResponse >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.UnstarEntryResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2193)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UnstarEntry(google::cloud::datacatalog::v1::UnstarEntryRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Marks an [Entry](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L1109) as NOT starred by the current user. Starring information is private to each user.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::UnstarEntryRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.UnstarEntryRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2180). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::UnstarEntryResponse >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.UnstarEntryResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2193)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### SetIamPolicy(std::string const &, google::iam::v1::Policy const &, Options)

**Deprecated:** This RPC is deprecated. 

Sets an access control policy for a resource. Replaces any existing policy.

Supported resources are:

  * Tag templates
  * Entry groups



Note: This method sets policies only within Data Catalog and can't be used to manage policies in BigQuery, Pub/Sub, Dataproc Metastore, and any external Google Cloud Platform resources synced with the Data Catalog.

To call this method, you must have the following Google IAM permissions:

  * `datacatalog.tagTemplates.setIamPolicy` to set policies on tag templates.
  * `datacatalog.entryGroups.setIamPolicy` to set policies on entry groups.



**Parameters**  
---  
**Name** | **Description**  
`resource` |  `std::string const &`   
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.   
`policy` |  `google::iam::v1::Policy const &`   
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | the result of the RPC. The response message type ([google.iam.v1.Policy](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/policy.proto#L102)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### SetIamPolicy(std::string const &, IamUpdater const &, Options)

Updates the IAM policy for `resource` using an optimistic concurrency control loop. 

The loop fetches the current policy for `resource`, and passes it to `updater`, which should return the new policy. This new policy should use the current etag so that the read-modify-write cycle can detect races and rerun the update when there is a mismatch. If the new policy does not have an etag, the existing policy will be blindly overwritten. If `updater` does not yield a policy, the control loop is terminated and kCancelled is returned.

**Parameters**  
---  
**Name** | **Description**  
`resource` |  `std::string const &`   
Required. The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.   
`updater` |  `IamUpdater const &`   
Required. Functor to map the current policy to a new one.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | google::iam::v1::Policy   
  
### SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Sets an access control policy for a resource. Replaces any existing policy.

Supported resources are:

  * Tag templates
  * Entry groups



Note: This method sets policies only within Data Catalog and can't be used to manage policies in BigQuery, Pub/Sub, Dataproc Metastore, and any external Google Cloud Platform resources synced with the Data Catalog.

To call this method, you must have the following Google IAM permissions:

  * `datacatalog.tagTemplates.setIamPolicy` to set policies on tag templates.
  * `datacatalog.entryGroups.setIamPolicy` to set policies on entry groups.



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
  
### GetIamPolicy(std::string const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets the access control policy for a resource.

May return:

  * A`NOT_FOUND` error if the resource doesn't exist or you don't have the permission to view it.
  * An empty policy if the resource exists but doesn't have a set policy.



Supported resources are:

  * Tag templates
  * Entry groups



Note: This method doesn't get policies from Google Cloud Platform resources ingested into Data Catalog.

To call this method, you must have the following Google IAM permissions:

  * `datacatalog.tagTemplates.getIamPolicy` to get policies on tag templates.
  * `datacatalog.entryGroups.getIamPolicy` to get policies on entry groups.



**Parameters**  
---  
**Name** | **Description**  
`resource` |  `std::string const &`   
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | the result of the RPC. The response message type ([google.iam.v1.Policy](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/policy.proto#L102)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Gets the access control policy for a resource.

May return:

  * A`NOT_FOUND` error if the resource doesn't exist or you don't have the permission to view it.
  * An empty policy if the resource exists but doesn't have a set policy.



Supported resources are:

  * Tag templates
  * Entry groups



Note: This method doesn't get policies from Google Cloud Platform resources ingested into Data Catalog.

To call this method, you must have the following Google IAM permissions:

  * `datacatalog.tagTemplates.getIamPolicy` to get policies on tag templates.
  * `datacatalog.entryGroups.getIamPolicy` to get policies on entry groups.



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

**Deprecated:** This RPC is deprecated. 

Gets your permissions on a resource.

Returns an empty set of permissions if the resource doesn't exist.

Supported resources are:

  * Tag templates
  * Entry groups



Note: This method gets policies only within Data Catalog and can't be used to get policies from BigQuery, Pub/Sub, Dataproc Metastore, and any external Google Cloud Platform resources ingested into Data Catalog.

No Google IAM permissions are required to call this method.

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
  
### ImportEntries(google::cloud::datacatalog::v1::ImportEntriesRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Imports entries from a source, such as data previously dumped into a Cloud Storage bucket, into Data Catalog. Import of entries is a sync operation that reconciles the state of the third-party system with the Data Catalog.

`ImportEntries` accepts source data snapshots of a third-party system. Snapshot should be delivered as a .wire or base65-encoded .txt file containing a sequence of Protocol Buffer messages of [DumpItem][google.cloud.datacatalog.v1.DumpItem] type.

`ImportEntries` returns a [long-running operation] [google.longrunning.Operation] resource that can be queried with [Operations.GetOperation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L70) to return [ImportEntriesMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2233) and an [ImportEntriesResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2221) message.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::ImportEntriesRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.ImportEntriesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2198). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::datacatalog::v1::ImportEntriesResponse > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.datacatalog.v1.ImportEntriesResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2221) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ImportEntries(NoAwaitTag, google::cloud::datacatalog::v1::ImportEntriesRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::datacatalog::v1::ImportEntriesRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ImportEntries(google::longrunning::Operation const &, Options)

**Deprecated:** This RPC is deprecated. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::datacatalog::v1::ImportEntriesResponse > >` |   
  
### SetConfig(google::cloud::datacatalog::v1::SetConfigRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Sets the configuration related to the migration to Dataplex for an organization or project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::SetConfigRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.SetConfigRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2377). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::MigrationConfig >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.MigrationConfig](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2447)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RetrieveConfig(google::cloud::datacatalog::v1::RetrieveConfigRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Retrieves the configuration related to the migration from Data Catalog to Dataplex for a specific organization, including all the projects under it which have a separate configuration set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::RetrieveConfigRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.RetrieveConfigRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2393). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::OrganizationConfig >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.OrganizationConfig](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2435)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### RetrieveEffectiveConfig(google::cloud::datacatalog::v1::RetrieveEffectiveConfigRequest const &, Options)

**Deprecated:** This RPC is deprecated. 

Retrieves the effective configuration related to the migration from Data Catalog to Dataplex for a specific organization or project. If there is no specific configuration set for the resource, the setting is checked hierarchicahlly through the ancestors of the resource, starting from the resource itself.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::datacatalog::v1::RetrieveEffectiveConfigRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.datacatalog.v1.RetrieveEffectiveConfigRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2400). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::datacatalog::v1::MigrationConfig >` | the result of the RPC. The response message type ([google.cloud.datacatalog.v1.MigrationConfig](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/datacatalog/v1/datacatalog.proto#L2447)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
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
  
### DeleteOperation(std::string const &, Options)

Deletes a long-running operation. 

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation resource to be deleted.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteOperation(google::longrunning::DeleteOperationRequest const &, Options)

Deletes a long-running operation. 

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.DeleteOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L219). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
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
