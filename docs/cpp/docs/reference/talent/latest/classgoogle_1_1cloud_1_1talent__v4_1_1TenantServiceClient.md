---
url: https://docs.cloud.google.com/cpp/docs/reference/talent/latest/classgoogle_1_1cloud_1_1talent__v4_1_1TenantServiceClient/
title: Class TenantServiceClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:15.113820+00:00
---

# Class TenantServiceClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/talent/latest/classgoogle_1_1cloud_1_1talent__v4_1_1TenantServiceClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class TenantServiceClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

A service that handles tenant management, including CRUD and enumeration. 

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### TenantServiceClient(TenantServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TenantServiceClient const &`   
  
  
### TenantServiceClient(TenantServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TenantServiceClient &&`   
  
  
### TenantServiceClient(std::shared_ptr< TenantServiceConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< TenantServiceConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(TenantServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TenantServiceClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`TenantServiceClient &` |   
  
### operator=(TenantServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TenantServiceClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`TenantServiceClient &` |   
  
## Functions 

### CreateTenant(std::string const &, google::cloud::talent::v4::Tenant const &, Options)

Creates a new tenant entity. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. Resource name of the project under which the tenant is created.   
The format is "projects/{project_id}", for example, "projects/foo".   
`tenant` |  `google::cloud::talent::v4::Tenant const &`   
Required. The tenant to be created.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::talent::v4::Tenant >` | the result of the RPC. The response message type ([google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateTenant(google::cloud::talent::v4::CreateTenantRequest const &, Options)

Creates a new tenant entity. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::talent::v4::CreateTenantRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.talent.v4.CreateTenantRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant_service.proto#L85). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::talent::v4::Tenant >` | the result of the RPC. The response message type ([google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTenant(std::string const &, Options)

Retrieves specified tenant. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the tenant to be retrieved.   
The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::talent::v4::Tenant >` | the result of the RPC. The response message type ([google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTenant(google::cloud::talent::v4::GetTenantRequest const &, Options)

Retrieves specified tenant. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::talent::v4::GetTenantRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.talent.v4.GetTenantRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant_service.proto#L102). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::talent::v4::Tenant >` | the result of the RPC. The response message type ([google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTenant(google::cloud::talent::v4::Tenant const &, google::protobuf::FieldMask const &, Options)

Updates specified tenant. 

**Parameters**  
---  
**Name** | **Description**  
`tenant` |  `google::cloud::talent::v4::Tenant const &`   
Required. The tenant resource to replace the current resource in the system.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Strongly recommended for the best service experience.   
If [update_mask](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant_service.proto#L128) is provided, only the specified fields in [tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant_service.proto#L117) are updated. Otherwise all the fields are updated.   
A field mask to specify the tenant fields to be updated. Only top level fields of [Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32) are supported.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::talent::v4::Tenant >` | the result of the RPC. The response message type ([google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTenant(google::cloud::talent::v4::UpdateTenantRequest const &, Options)

Updates specified tenant. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::talent::v4::UpdateTenantRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.talent.v4.UpdateTenantRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant_service.proto#L114). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::talent::v4::Tenant >` | the result of the RPC. The response message type ([google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteTenant(std::string const &, Options)

Deletes specified tenant. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name of the tenant to be deleted.   
The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteTenant(google::cloud::talent::v4::DeleteTenantRequest const &, Options)

Deletes specified tenant. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::talent::v4::DeleteTenantRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.talent.v4.DeleteTenantRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant_service.proto#L132). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### ListTenants(std::string const &, Options)

Lists all tenants associated with the project. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. Resource name of the project under which the tenant is created.   
The format is "projects/{project_id}", for example, "projects/foo".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::talent::v4::Tenant >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListTenants(google::cloud::talent::v4::ListTenantsRequest, Options)

Lists all tenants associated with the project. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::talent::v4::ListTenantsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.talent.v4.ListTenantsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant_service.proto#L144). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::talent::v4::Tenant >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.talent.v4.Tenant](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/talent/v4/tenant.proto#L32), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
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
