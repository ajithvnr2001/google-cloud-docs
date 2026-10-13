---
url: https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient/
title: Class EventarcClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:00.592500+00:00
---

# Class EventarcClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class EventarcClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Eventarc allows users to subscribe to various events that are provided by Google Cloud services and forward them to supported destinations. 

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### EventarcClient(EventarcClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `EventarcClient const &`   
  
  
### EventarcClient(EventarcClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `EventarcClient &&`   
  
  
### EventarcClient(std::shared_ptr< EventarcConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< EventarcConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(EventarcClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `EventarcClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`EventarcClient &` |   
  
### operator=(EventarcClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `EventarcClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`EventarcClient &` |   
  
## Functions 

### GetTrigger(std::string const &, Options)

Get a single trigger. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the trigger to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Trigger >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTrigger(google::cloud::eventarc::v1::GetTriggerRequest const &, Options)

Get a single trigger. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetTriggerRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetTriggerRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L491). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Trigger >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListTriggers(std::string const &, Options)

List triggers. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection to list triggers on.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Trigger >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListTriggers(google::cloud::eventarc::v1::ListTriggersRequest, Options)

List triggers. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListTriggersRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListTriggersRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L502). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Trigger >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateTrigger(std::string const &, google::cloud::eventarc::v1::Trigger const &, std::string const &, Options)

Create a new trigger in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection in which to add this trigger.   
`trigger` |  `google::cloud::eventarc::v1::Trigger const &`   
Required. The trigger to create.   
`trigger_id` |  `std::string const &`   
Required. The user-provided ID to be assigned to the trigger.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateTrigger(NoAwaitTag, std::string const &, google::cloud::eventarc::v1::Trigger const &, std::string const &, Options)

Create a new trigger in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`trigger` |  `google::cloud::eventarc::v1::Trigger const &`   
  
`trigger_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateTrigger(google::cloud::eventarc::v1::CreateTriggerRequest const &, Options)

Create a new trigger in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateTriggerRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.CreateTriggerRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L549). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateTrigger(NoAwaitTag, google::cloud::eventarc::v1::CreateTriggerRequest const &, Options)

Create a new trigger in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateTriggerRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateTrigger(google::longrunning::Operation const &, Options)

Create a new trigger in a particular project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### UpdateTrigger(google::cloud::eventarc::v1::Trigger const &, google::protobuf::FieldMask const &, bool, Options)

Update a single trigger. 

**Parameters**  
---  
**Name** | **Description**  
`trigger` |  `google::cloud::eventarc::v1::Trigger const &`   
The trigger to be updated.   
`update_mask` |  `google::protobuf::FieldMask const &`   
The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*".   
`allow_missing` |  `bool`   
If set to true, and the trigger is not found, a new trigger will be created. In this situation, `update_mask` is ignored.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateTrigger(NoAwaitTag, google::cloud::eventarc::v1::Trigger const &, google::protobuf::FieldMask const &, bool, Options)

Update a single trigger. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`trigger` |  `google::cloud::eventarc::v1::Trigger const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`allow_missing` |  `bool`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateTrigger(google::cloud::eventarc::v1::UpdateTriggerRequest const &, Options)

Update a single trigger. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateTriggerRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.UpdateTriggerRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L570). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateTrigger(NoAwaitTag, google::cloud::eventarc::v1::UpdateTriggerRequest const &, Options)

Update a single trigger. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateTriggerRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateTrigger(google::longrunning::Operation const &, Options)

Update a single trigger. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### DeleteTrigger(std::string const &, bool, Options)

Delete a single trigger. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the trigger to be deleted.   
`allow_missing` |  `bool`   
If set to true, and the trigger is not found, the request will succeed but no action will be taken on the server.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteTrigger(NoAwaitTag, std::string const &, bool, Options)

Delete a single trigger. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`allow_missing` |  `bool`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteTrigger(google::cloud::eventarc::v1::DeleteTriggerRequest const &, Options)

Delete a single trigger. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteTriggerRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.DeleteTriggerRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L589). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Trigger](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/trigger.proto#L55) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteTrigger(NoAwaitTag, google::cloud::eventarc::v1::DeleteTriggerRequest const &, Options)

Delete a single trigger. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteTriggerRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteTrigger(google::longrunning::Operation const &, Options)

Delete a single trigger. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### GetChannel(std::string const &, Options)

Get a single Channel. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the channel to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Channel >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetChannel(google::cloud::eventarc::v1::GetChannelRequest const &, Options)

Get a single Channel. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetChannelRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetChannelRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L612). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Channel >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListChannels(std::string const &, Options)

List channels. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection to list channels on.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Channel >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListChannels(google::cloud::eventarc::v1::ListChannelsRequest, Options)

List channels. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListChannelsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListChannelsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L623). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Channel >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateChannel(std::string const &, google::cloud::eventarc::v1::Channel const &, std::string const &, Options)

Create a new channel in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection in which to add this channel.   
`channel` |  `google::cloud::eventarc::v1::Channel const &`   
Required. The channel to create.   
`channel_id` |  `std::string const &`   
Required. The user-provided ID to be assigned to the channel.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateChannel(NoAwaitTag, std::string const &, google::cloud::eventarc::v1::Channel const &, std::string const &, Options)

Create a new channel in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`channel` |  `google::cloud::eventarc::v1::Channel const &`   
  
`channel_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateChannel(google::cloud::eventarc::v1::CreateChannelRequest const &, Options)

Create a new channel in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateChannelRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.CreateChannelRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L665). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateChannel(NoAwaitTag, google::cloud::eventarc::v1::CreateChannelRequest const &, Options)

Create a new channel in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateChannelRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateChannel(google::longrunning::Operation const &, Options)

Create a new channel in a particular project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### UpdateChannel(google::cloud::eventarc::v1::Channel const &, google::protobuf::FieldMask const &, Options)

Update a single channel. 

**Parameters**  
---  
**Name** | **Description**  
`channel` |  `google::cloud::eventarc::v1::Channel const &`   
The channel to be updated.   
`update_mask` |  `google::protobuf::FieldMask const &`   
The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateChannel(NoAwaitTag, google::cloud::eventarc::v1::Channel const &, google::protobuf::FieldMask const &, Options)

Update a single channel. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`channel` |  `google::cloud::eventarc::v1::Channel const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateChannel(google::cloud::eventarc::v1::UpdateChannelRequest const &, Options)

Update a single channel. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateChannelRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.UpdateChannelRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L686). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateChannel(NoAwaitTag, google::cloud::eventarc::v1::UpdateChannelRequest const &, Options)

Update a single channel. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateChannelRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateChannel(google::longrunning::Operation const &, Options)

Update a single channel. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### DeleteChannel(std::string const &, Options)

Delete a single channel. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the channel to be deleted.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteChannel(NoAwaitTag, std::string const &, Options)

Delete a single channel. 

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
  
### DeleteChannel(google::cloud::eventarc::v1::DeleteChannelRequest const &, Options)

Delete a single channel. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteChannelRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.DeleteChannelRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L701). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Channel](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteChannel(NoAwaitTag, google::cloud::eventarc::v1::DeleteChannelRequest const &, Options)

Delete a single channel. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteChannelRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteChannel(google::longrunning::Operation const &, Options)

Delete a single channel. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### GetProvider(std::string const &, Options)

Get a single Provider. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the provider to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Provider >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Provider](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/discovery.proto#L28)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetProvider(google::cloud::eventarc::v1::GetProviderRequest const &, Options)

Get a single Provider. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetProviderRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetProviderRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L716). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Provider >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Provider](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/discovery.proto#L28)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListProviders(std::string const &, Options)

List providers. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent of the provider to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Provider >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Provider](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/discovery.proto#L28), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListProviders(google::cloud::eventarc::v1::ListProvidersRequest, Options)

List providers. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListProvidersRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListProvidersRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L727). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Provider >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Provider](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/discovery.proto#L28), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetChannelConnection(std::string const &, Options)

Get a single ChannelConnection. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the channel connection to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::ChannelConnection >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetChannelConnection(google::cloud::eventarc::v1::GetChannelConnectionRequest const &, Options)

Get a single ChannelConnection. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetChannelConnectionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetChannelConnectionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L770). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::ChannelConnection >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListChannelConnections(std::string const &, Options)

List channel connections. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection from which to list channel connections.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::ChannelConnection >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListChannelConnections(google::cloud::eventarc::v1::ListChannelConnectionsRequest, Options)

List channel connections. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListChannelConnectionsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListChannelConnectionsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L781). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::ChannelConnection >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateChannelConnection(std::string const &, google::cloud::eventarc::v1::ChannelConnection const &, std::string const &, Options)

Create a new ChannelConnection in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection in which to add this channel connection.   
`channel_connection` |  `google::cloud::eventarc::v1::ChannelConnection const &`   
Required. Channel connection to create.   
`channel_connection_id` |  `std::string const &`   
Required. The user-provided ID to be assigned to the channel connection.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateChannelConnection(NoAwaitTag, std::string const &, google::cloud::eventarc::v1::ChannelConnection const &, std::string const &, Options)

Create a new ChannelConnection in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`channel_connection` |  `google::cloud::eventarc::v1::ChannelConnection const &`   
  
`channel_connection_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateChannelConnection(google::cloud::eventarc::v1::CreateChannelConnectionRequest const &, Options)

Create a new ChannelConnection in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateChannelConnectionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.CreateChannelConnectionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L819). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateChannelConnection(NoAwaitTag, google::cloud::eventarc::v1::CreateChannelConnectionRequest const &, Options)

Create a new ChannelConnection in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateChannelConnectionRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateChannelConnection(google::longrunning::Operation const &, Options)

Create a new ChannelConnection in a particular project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` |   
  
### DeleteChannelConnection(std::string const &, Options)

Delete a single ChannelConnection. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the channel connection to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteChannelConnection(NoAwaitTag, std::string const &, Options)

Delete a single ChannelConnection. 

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
  
### DeleteChannelConnection(google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &, Options)

Delete a single ChannelConnection. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.DeleteChannelConnectionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L837). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.ChannelConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/channel_connection.proto#L35) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteChannelConnection(NoAwaitTag, google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &, Options)

Delete a single ChannelConnection. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteChannelConnection(google::longrunning::Operation const &, Options)

Delete a single ChannelConnection. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` |   
  
### GetGoogleChannelConfig(std::string const &, Options)

Get a GoogleChannelConfig. 

The name of the GoogleChannelConfig in the response is ALWAYS coded with projectID.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the config to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleChannelConfig >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.GoogleChannelConfig](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_channel_config.proto#L40)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetGoogleChannelConfig(google::cloud::eventarc::v1::GetGoogleChannelConfigRequest const &, Options)

Get a GoogleChannelConfig. 

The name of the GoogleChannelConfig in the response is ALWAYS coded with projectID.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetGoogleChannelConfigRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetGoogleChannelConfigRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L860). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleChannelConfig >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.GoogleChannelConfig](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_channel_config.proto#L40)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateGoogleChannelConfig(google::cloud::eventarc::v1::GoogleChannelConfig const &, google::protobuf::FieldMask const &, Options)

Update a single GoogleChannelConfig. 

**Parameters**  
---  
**Name** | **Description**  
`google_channel_config` |  `google::cloud::eventarc::v1::GoogleChannelConfig const &`   
Required. The config to be updated.   
`update_mask` |  `google::protobuf::FieldMask const &`   
The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleChannelConfig >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.GoogleChannelConfig](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_channel_config.proto#L40)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateGoogleChannelConfig(google::cloud::eventarc::v1::UpdateGoogleChannelConfigRequest const &, Options)

Update a single GoogleChannelConfig. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateGoogleChannelConfigRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.UpdateGoogleChannelConfigRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L848). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleChannelConfig >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.GoogleChannelConfig](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_channel_config.proto#L40)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetMessageBus(std::string const &, Options)

Get a single MessageBus. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the message bus to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::MessageBus >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetMessageBus(google::cloud::eventarc::v1::GetMessageBusRequest const &, Options)

Get a single MessageBus. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetMessageBusRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetMessageBusRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L871). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::MessageBus >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListMessageBuses(std::string const &, Options)

List message buses. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection to list message buses on.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::MessageBus >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListMessageBuses(google::cloud::eventarc::v1::ListMessageBusesRequest, Options)

List message buses. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListMessageBusesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListMessageBusesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L882). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::MessageBus >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListMessageBusEnrollments(std::string const &, Options)

List message bus enrollments. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent message bus to list enrollments on.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::ListMessageBusEnrollmentsResponse >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L951)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListMessageBusEnrollments(google::cloud::eventarc::v1::ListMessageBusEnrollmentsRequest const &, Options)

List message bus enrollments. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListMessageBusEnrollmentsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListMessageBusEnrollmentsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L928). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::ListMessageBusEnrollmentsResponse >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L951)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateMessageBus(std::string const &, google::cloud::eventarc::v1::MessageBus const &, std::string const &, Options)

Create a new MessageBus in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection in which to add this message bus.   
`message_bus` |  `google::cloud::eventarc::v1::MessageBus const &`   
Required. The message bus to create.   
`message_bus_id` |  `std::string const &`   
Required. The user-provided ID to be assigned to the MessageBus. It should match the format `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateMessageBus(NoAwaitTag, std::string const &, google::cloud::eventarc::v1::MessageBus const &, std::string const &, Options)

Create a new MessageBus in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`message_bus` |  `google::cloud::eventarc::v1::MessageBus const &`   
  
`message_bus_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateMessageBus(google::cloud::eventarc::v1::CreateMessageBusRequest const &, Options)

Create a new MessageBus in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateMessageBusRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.CreateMessageBusRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L964). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateMessageBus(NoAwaitTag, google::cloud::eventarc::v1::CreateMessageBusRequest const &, Options)

Create a new MessageBus in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateMessageBusRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateMessageBus(google::longrunning::Operation const &, Options)

Create a new MessageBus in a particular project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### UpdateMessageBus(google::cloud::eventarc::v1::MessageBus const &, google::protobuf::FieldMask const &, Options)

Update a single message bus. 

**Parameters**  
---  
**Name** | **Description**  
`message_bus` |  `google::cloud::eventarc::v1::MessageBus const &`   
Required. The MessageBus to be updated.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Optional. The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateMessageBus(NoAwaitTag, google::cloud::eventarc::v1::MessageBus const &, google::protobuf::FieldMask const &, Options)

Update a single message bus. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`message_bus` |  `google::cloud::eventarc::v1::MessageBus const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateMessageBus(google::cloud::eventarc::v1::UpdateMessageBusRequest const &, Options)

Update a single message bus. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateMessageBusRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.UpdateMessageBusRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L986). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateMessageBus(NoAwaitTag, google::cloud::eventarc::v1::UpdateMessageBusRequest const &, Options)

Update a single message bus. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateMessageBusRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateMessageBus(google::longrunning::Operation const &, Options)

Update a single message bus. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### DeleteMessageBus(std::string const &, std::string const &, Options)

Delete a single message bus. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the MessageBus to be deleted.   
`etag` |  `std::string const &`   
Optional. If provided, the MessageBus will only be deleted if the etag matches the current etag on the resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteMessageBus(NoAwaitTag, std::string const &, std::string const &, Options)

Delete a single message bus. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`etag` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteMessageBus(google::cloud::eventarc::v1::DeleteMessageBusRequest const &, Options)

Delete a single message bus. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteMessageBusRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.DeleteMessageBusRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1006). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.MessageBus](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/message_bus.proto#L36) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteMessageBus(NoAwaitTag, google::cloud::eventarc::v1::DeleteMessageBusRequest const &, Options)

Delete a single message bus. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteMessageBusRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteMessageBus(google::longrunning::Operation const &, Options)

Delete a single message bus. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### GetEnrollment(std::string const &, Options)

Get a single Enrollment. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the Enrollment to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Enrollment >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetEnrollment(google::cloud::eventarc::v1::GetEnrollmentRequest const &, Options)

Get a single Enrollment. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetEnrollmentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetEnrollmentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1029). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Enrollment >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListEnrollments(std::string const &, Options)

List Enrollments. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection to list triggers on.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Enrollment >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListEnrollments(google::cloud::eventarc::v1::ListEnrollmentsRequest, Options)

List Enrollments. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListEnrollmentsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListEnrollmentsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1040). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Enrollment >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateEnrollment(std::string const &, google::cloud::eventarc::v1::Enrollment const &, std::string const &, Options)

Create a new Enrollment in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection in which to add this enrollment.   
`enrollment` |  `google::cloud::eventarc::v1::Enrollment const &`   
Required. The enrollment to create.   
`enrollment_id` |  `std::string const &`   
Required. The user-provided ID to be assigned to the Enrollment. It should match the format `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateEnrollment(NoAwaitTag, std::string const &, google::cloud::eventarc::v1::Enrollment const &, std::string const &, Options)

Create a new Enrollment in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`enrollment` |  `google::cloud::eventarc::v1::Enrollment const &`   
  
`enrollment_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateEnrollment(google::cloud::eventarc::v1::CreateEnrollmentRequest const &, Options)

Create a new Enrollment in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateEnrollmentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.CreateEnrollmentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1086). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateEnrollment(NoAwaitTag, google::cloud::eventarc::v1::CreateEnrollmentRequest const &, Options)

Create a new Enrollment in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateEnrollmentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateEnrollment(google::longrunning::Operation const &, Options)

Create a new Enrollment in a particular project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### UpdateEnrollment(google::cloud::eventarc::v1::Enrollment const &, google::protobuf::FieldMask const &, Options)

Update a single Enrollment. 

**Parameters**  
---  
**Name** | **Description**  
`enrollment` |  `google::cloud::eventarc::v1::Enrollment const &`   
Required. The Enrollment to be updated.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Optional. The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateEnrollment(NoAwaitTag, google::cloud::eventarc::v1::Enrollment const &, google::protobuf::FieldMask const &, Options)

Update a single Enrollment. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`enrollment` |  `google::cloud::eventarc::v1::Enrollment const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateEnrollment(google::cloud::eventarc::v1::UpdateEnrollmentRequest const &, Options)

Update a single Enrollment. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateEnrollmentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.UpdateEnrollmentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1108). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateEnrollment(NoAwaitTag, google::cloud::eventarc::v1::UpdateEnrollmentRequest const &, Options)

Update a single Enrollment. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateEnrollmentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateEnrollment(google::longrunning::Operation const &, Options)

Update a single Enrollment. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### DeleteEnrollment(std::string const &, std::string const &, Options)

Delete a single Enrollment. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the Enrollment to be deleted.   
`etag` |  `std::string const &`   
Optional. If provided, the Enrollment will only be deleted if the etag matches the current etag on the resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteEnrollment(NoAwaitTag, std::string const &, std::string const &, Options)

Delete a single Enrollment. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`etag` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteEnrollment(google::cloud::eventarc::v1::DeleteEnrollmentRequest const &, Options)

Delete a single Enrollment. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteEnrollmentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.DeleteEnrollmentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1128). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Enrollment](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/enrollment.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteEnrollment(NoAwaitTag, google::cloud::eventarc::v1::DeleteEnrollmentRequest const &, Options)

Delete a single Enrollment. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteEnrollmentRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteEnrollment(google::longrunning::Operation const &, Options)

Delete a single Enrollment. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### GetPipeline(std::string const &, Options)

Get a single Pipeline. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the pipeline to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Pipeline >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetPipeline(google::cloud::eventarc::v1::GetPipelineRequest const &, Options)

Get a single Pipeline. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetPipelineRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetPipelineRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1151). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Pipeline >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListPipelines(std::string const &, Options)

List pipelines. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection to list pipelines on.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Pipeline >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListPipelines(google::cloud::eventarc::v1::ListPipelinesRequest, Options)

List pipelines. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListPipelinesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListPipelinesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1162). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Pipeline >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreatePipeline(std::string const &, google::cloud::eventarc::v1::Pipeline const &, std::string const &, Options)

Create a new Pipeline in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection in which to add this pipeline.   
`pipeline` |  `google::cloud::eventarc::v1::Pipeline const &`   
Required. The pipeline to create.   
`pipeline_id` |  `std::string const &`   
Required. The user-provided ID to be assigned to the Pipeline. It should match the format `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreatePipeline(NoAwaitTag, std::string const &, google::cloud::eventarc::v1::Pipeline const &, std::string const &, Options)

Create a new Pipeline in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`pipeline` |  `google::cloud::eventarc::v1::Pipeline const &`   
  
`pipeline_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreatePipeline(google::cloud::eventarc::v1::CreatePipelineRequest const &, Options)

Create a new Pipeline in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreatePipelineRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.CreatePipelineRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1208). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreatePipeline(NoAwaitTag, google::cloud::eventarc::v1::CreatePipelineRequest const &, Options)

Create a new Pipeline in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreatePipelineRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreatePipeline(google::longrunning::Operation const &, Options)

Create a new Pipeline in a particular project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### UpdatePipeline(google::cloud::eventarc::v1::Pipeline const &, google::protobuf::FieldMask const &, Options)

Update a single pipeline. 

**Parameters**  
---  
**Name** | **Description**  
`pipeline` |  `google::cloud::eventarc::v1::Pipeline const &`   
Required. The Pipeline to be updated.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Optional. The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdatePipeline(NoAwaitTag, google::cloud::eventarc::v1::Pipeline const &, google::protobuf::FieldMask const &, Options)

Update a single pipeline. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`pipeline` |  `google::cloud::eventarc::v1::Pipeline const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdatePipeline(google::cloud::eventarc::v1::UpdatePipelineRequest const &, Options)

Update a single pipeline. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdatePipelineRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.UpdatePipelineRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1230). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdatePipeline(NoAwaitTag, google::cloud::eventarc::v1::UpdatePipelineRequest const &, Options)

Update a single pipeline. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdatePipelineRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdatePipeline(google::longrunning::Operation const &, Options)

Update a single pipeline. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### DeletePipeline(std::string const &, std::string const &, Options)

Delete a single pipeline. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the Pipeline to be deleted.   
`etag` |  `std::string const &`   
Optional. If provided, the Pipeline will only be deleted if the etag matches the current etag on the resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeletePipeline(NoAwaitTag, std::string const &, std::string const &, Options)

Delete a single pipeline. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`etag` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeletePipeline(google::cloud::eventarc::v1::DeletePipelineRequest const &, Options)

Delete a single pipeline. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeletePipelineRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.DeletePipelineRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1250). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.Pipeline](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/pipeline.proto#L39) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeletePipeline(NoAwaitTag, google::cloud::eventarc::v1::DeletePipelineRequest const &, Options)

Delete a single pipeline. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeletePipelineRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeletePipeline(google::longrunning::Operation const &, Options)

Delete a single pipeline. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### GetGoogleApiSource(std::string const &, Options)

Get a single GoogleApiSource. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the google api source to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleApiSource >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetGoogleApiSource(google::cloud::eventarc::v1::GetGoogleApiSourceRequest const &, Options)

Get a single GoogleApiSource. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetGoogleApiSourceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.GetGoogleApiSourceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1273). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleApiSource >` | the result of the RPC. The response message type ([google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListGoogleApiSources(std::string const &, Options)

List GoogleApiSources. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection to list GoogleApiSources on.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::GoogleApiSource >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListGoogleApiSources(google::cloud::eventarc::v1::ListGoogleApiSourcesRequest, Options)

List GoogleApiSources. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListGoogleApiSourcesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.ListGoogleApiSourcesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1284). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::GoogleApiSource >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateGoogleApiSource(std::string const &, google::cloud::eventarc::v1::GoogleApiSource const &, std::string const &, Options)

Create a new GoogleApiSource in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent collection in which to add this google api source.   
`google_api_source` |  `google::cloud::eventarc::v1::GoogleApiSource const &`   
Required. The google api source to create.   
`google_api_source_id` |  `std::string const &`   
Required. The user-provided ID to be assigned to the GoogleApiSource. It should match the format `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateGoogleApiSource(NoAwaitTag, std::string const &, google::cloud::eventarc::v1::GoogleApiSource const &, std::string const &, Options)

Create a new GoogleApiSource in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`google_api_source` |  `google::cloud::eventarc::v1::GoogleApiSource const &`   
  
`google_api_source_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateGoogleApiSource(google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &, Options)

Create a new GoogleApiSource in a particular project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.CreateGoogleApiSourceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1330). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateGoogleApiSource(NoAwaitTag, google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &, Options)

Create a new GoogleApiSource in a particular project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateGoogleApiSource(google::longrunning::Operation const &, Options)

Create a new GoogleApiSource in a particular project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### UpdateGoogleApiSource(google::cloud::eventarc::v1::GoogleApiSource const &, google::protobuf::FieldMask const &, Options)

Update a single GoogleApiSource. 

**Parameters**  
---  
**Name** | **Description**  
`google_api_source` |  `google::cloud::eventarc::v1::GoogleApiSource const &`   
Required. The GoogleApiSource to be updated.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Optional. The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*".   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateGoogleApiSource(NoAwaitTag, google::cloud::eventarc::v1::GoogleApiSource const &, google::protobuf::FieldMask const &, Options)

Update a single GoogleApiSource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`google_api_source` |  `google::cloud::eventarc::v1::GoogleApiSource const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateGoogleApiSource(google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &, Options)

Update a single GoogleApiSource. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.UpdateGoogleApiSourceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1353). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateGoogleApiSource(NoAwaitTag, google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &, Options)

Update a single GoogleApiSource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateGoogleApiSource(google::longrunning::Operation const &, Options)

Update a single GoogleApiSource. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### DeleteGoogleApiSource(std::string const &, std::string const &, Options)

Delete a single GoogleApiSource. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the GoogleApiSource to be deleted.   
`etag` |  `std::string const &`   
Optional. If provided, the MessageBus will only be deleted if the etag matches the current etag on the resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteGoogleApiSource(NoAwaitTag, std::string const &, std::string const &, Options)

Delete a single GoogleApiSource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`etag` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteGoogleApiSource(google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &, Options)

Delete a single GoogleApiSource. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.eventarc.v1.DeleteGoogleApiSourceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/eventarc.proto#L1375). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.eventarc.v1.GoogleApiSource](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/eventarc/v1/google_api_source.proto#L34) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteGoogleApiSource(NoAwaitTag, google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &, Options)

Delete a single GoogleApiSource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteGoogleApiSource(google::longrunning::Operation const &, Options)

Delete a single GoogleApiSource. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
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
