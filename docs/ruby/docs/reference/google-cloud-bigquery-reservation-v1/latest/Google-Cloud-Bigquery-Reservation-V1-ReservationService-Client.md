---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client/
title: BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:25.145052+00:00
---

# BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.

Client for the ReservationService service.

This API allows users to manage their BigQuery reservations.

A reservation provides computational resource guarantees, in the form of [slots](https://cloud.google.com/bigquery/docs/slots), to users. A slot is a unit of computational power in BigQuery, and serves as the basic unit of parallelism. In a scan of a multi-partitioned table, a single slot operates on a single partition of the table. A reservation resource exists as a child resource of the admin project and location, e.g.: `projects/myproject/locations/US/reservations/reservationName`.

A capacity commitment is a way to purchase compute capacity for BigQuery jobs (in the form of slots) with some committed period of usage. A capacity commitment resource exists as a child resource of the admin project and location, e.g.: `projects/myproject/locations/US/capacityCommitments/id`.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Bigquery::Reservation::V1::ReservationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ReservationService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client-Configuration "Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ReservationService clients
    ::Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ReservationService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client#Google__Cloud__Bigquery__Reservation__V1__ReservationService__Client_configure_class_ "Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client-Configuration "Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client-Configuration)) 



### #create_assignment
    
    
    def create_assignment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment
    def create_assignment(parent: nil, assignment: nil, assignment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Creates an assignment object which allows the given project to submit jobs of a certain type using slots from the specified reservation.

Currently a resource (project, folder, organization) can only have one assignment per each (job_type, location) combination, and that reservation will be used for all jobs of the matching type.

Different assignments can be created on different levels of the projects, folders or organization hierarchy. During query execution, the assignment is looked up at the project, folder and organization levels in that order. The first assignment found is applied to the query.

When creating assignments, it does not matter if other assignments exist at higher levels.

Example:

  * The organization `organizationA` contains two projects, `project1` and `project2`.
  * Assignments for all three entities (`organizationA`, `project1`, and `project2`) could all be created and mapped to the same or different reservations.



"None" assignments represent an absence of the assignment. Projects assigned to None use on-demand pricing. To create a "None" assignment, use "none" as a reservation_id in the parent. Example parent: `projects/myproject/locations/US/reservations/none`.

Returns `google.rpc.Code.PERMISSION_DENIED` if user does not have 'bigquery.admin' permissions on the project using the reservation and the project that owns this reservation.

Returns `google.rpc.Code.INVALID_ARGUMENT` when location of the assignment does not match location of the reservation.

**Overloads**
    
    
    def create_assignment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Pass arguments to `create_assignment` via a request object, either of type [CreateAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateAssignmentRequest "Google::Cloud::Bigquery::Reservation::V1::CreateAssignmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::CreateAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateAssignmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_assignment(parent: nil, assignment: nil, assignment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Pass arguments to `create_assignment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name of the assignment E.g. `projects/myproject/locations/US/reservations/team1-prod`
  * **assignment** ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment), ::Hash) — Assignment resource to create. 
  * **assignment_id** (::String) — The optional assignment ID. Assignment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. Max length is 64 characters. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::CreateAssignmentRequest.new
    
    # Call the create_assignment method.
    result = client.create_assignment request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::Assignment.
    p result

### #create_capacity_commitment
    
    
    def create_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment
    def create_capacity_commitment(parent: nil, capacity_commitment: nil, enforce_single_admin_project_per_org: nil, capacity_commitment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Creates a new capacity commitment resource.

**Overloads**
    
    
    def create_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `create_capacity_commitment` via a request object, either of type [CreateCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateCapacityCommitmentRequest "Google::Cloud::Bigquery::Reservation::V1::CreateCapacityCommitmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::CreateCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateCapacityCommitmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_capacity_commitment(parent: nil, capacity_commitment: nil, enforce_single_admin_project_per_org: nil, capacity_commitment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `create_capacity_commitment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of the parent reservation. E.g., `projects/myproject/locations/US`
  * **capacity_commitment** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment), ::Hash) — Content of the capacity commitment to create. 
  * **enforce_single_admin_project_per_org** (::Boolean) — If true, fail the request if another project in the organization has a capacity commitment. 
  * **capacity_commitment_id** (::String) — The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split or merged. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::CreateCapacityCommitmentRequest.new
    
    # Call the create_capacity_commitment method.
    result = client.create_capacity_commitment request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment.
    p result

### #create_reservation
    
    
    def create_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation
    def create_reservation(parent: nil, reservation_id: nil, reservation: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Creates a new reservation resource.

**Overloads**
    
    
    def create_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `create_reservation` via a request object, either of type [CreateReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateReservationRequest "Google::Cloud::Bigquery::Reservation::V1::CreateReservationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::CreateReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateReservationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_reservation(parent: nil, reservation_id: nil, reservation: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `create_reservation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Project, location. E.g., `projects/myproject/locations/US`
  * **reservation_id** (::String) — The reservation ID. It must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. 
  * **reservation** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation), ::Hash) — Definition of the new reservation to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::CreateReservationRequest.new
    
    # Call the create_reservation method.
    result = client.create_reservation request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::Reservation.
    p result

### #create_reservation_group
    
    
    def create_reservation_group(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup
    def create_reservation_group(parent: nil, reservation_group_id: nil, reservation_group: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Creates a new reservation group.

**Overloads**
    
    
    def create_reservation_group(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Pass arguments to `create_reservation_group` via a request object, either of type [CreateReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateReservationGroupRequest "Google::Cloud::Bigquery::Reservation::V1::CreateReservationGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::CreateReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CreateReservationGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_reservation_group(parent: nil, reservation_group_id: nil, reservation_group: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Pass arguments to `create_reservation_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Project, location. E.g., `projects/myproject/locations/US`
  * **reservation_group_id** (::String) — Required. The reservation group ID. It must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. 
  * **reservation_group** ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup), ::Hash) — Required. New Reservation Group to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::CreateReservationGroupRequest.new
    
    # Call the create_reservation_group method.
    result = client.create_reservation_group request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::ReservationGroup.
    p result

### #delete_assignment
    
    
    def delete_assignment(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_assignment(name: nil) -> ::Google::Protobuf::Empty

Deletes a assignment. No expansion will happen.

Example:

  * Organization `organizationA` contains two projects, `project1` and `project2`.
  * Reservation `res1` exists and was created previously.
  * CreateAssignment was used previously to define the following associations between entities and reservations: `<organizationA, res1>` and `<project1, res1>`



In this example, deletion of the `<organizationA, res1>` assignment won't affect the other assignment `<project1, res1>`. After said deletion, queries from `project1` will still use `res1` while queries from `project2` will switch to use on-demand mode.

**Overloads**
    
    
    def delete_assignment(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_assignment` via a request object, either of type [DeleteAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteAssignmentRequest "Google::Cloud::Bigquery::Reservation::V1::DeleteAssignmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::DeleteAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteAssignmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_assignment(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_assignment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource, e.g. `projects/myproject/locations/US/reservations/team1-prod/assignments/123`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::DeleteAssignmentRequest.new
    
    # Call the delete_assignment method.
    result = client.delete_assignment request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_capacity_commitment
    
    
    def delete_capacity_commitment(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_capacity_commitment(name: nil, force: nil) -> ::Google::Protobuf::Empty

Deletes a capacity commitment. Attempting to delete capacity commitment before its commitment_end_time will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`.

**Overloads**
    
    
    def delete_capacity_commitment(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_capacity_commitment` via a request object, either of type [DeleteCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteCapacityCommitmentRequest "Google::Cloud::Bigquery::Reservation::V1::DeleteCapacityCommitmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::DeleteCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteCapacityCommitmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_capacity_commitment(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_capacity_commitment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the capacity commitment to delete. E.g., `projects/myproject/locations/US/capacityCommitments/123`
  * **force** (::Boolean) — Can be used to force delete commitments even if assignments exist. Deleting commitments with assignments may cause queries to fail if they no longer have access to slots. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::DeleteCapacityCommitmentRequest.new
    
    # Call the delete_capacity_commitment method.
    result = client.delete_capacity_commitment request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_reservation
    
    
    def delete_reservation(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_reservation(name: nil) -> ::Google::Protobuf::Empty

Deletes a reservation. Returns `google.rpc.Code.FAILED_PRECONDITION` when reservation has assignments.

**Overloads**
    
    
    def delete_reservation(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_reservation` via a request object, either of type [DeleteReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteReservationRequest "Google::Cloud::Bigquery::Reservation::V1::DeleteReservationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::DeleteReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteReservationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_reservation(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_reservation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the reservation to retrieve. E.g., `projects/myproject/locations/US/reservations/team1-prod`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::DeleteReservationRequest.new
    
    # Call the delete_reservation method.
    result = client.delete_reservation request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_reservation_group
    
    
    def delete_reservation_group(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_reservation_group(name: nil) -> ::Google::Protobuf::Empty

Deletes a reservation. Returns `google.rpc.Code.FAILED_PRECONDITION` when reservation has assignments.

**Overloads**
    
    
    def delete_reservation_group(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_reservation_group` via a request object, either of type [DeleteReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteReservationGroupRequest "Google::Cloud::Bigquery::Reservation::V1::DeleteReservationGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::DeleteReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-DeleteReservationGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_reservation_group(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_reservation_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the reservation group to retrieve. E.g., `projects/myproject/locations/US/reservationGroups/team1-prod`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::DeleteReservationGroupRequest.new
    
    # Call the delete_reservation_group method.
    result = client.delete_reservation_group request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #failover_reservation
    
    
    def failover_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation
    def failover_reservation(name: nil, failover_mode: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Fail over a reservation to the secondary location. The operation should be done in the current secondary location, which will be promoted to the new primary location for the reservation. Attempting to failover a reservation in the current primary location will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`.

**Overloads**
    
    
    def failover_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `failover_reservation` via a request object, either of type [FailoverReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-FailoverReservationRequest "Google::Cloud::Bigquery::Reservation::V1::FailoverReservationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::FailoverReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-FailoverReservationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def failover_reservation(name: nil, failover_mode: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `failover_reservation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the reservation to failover. E.g., `projects/myproject/locations/US/reservations/team1-prod`
  * **failover_mode** ([::Google::Cloud::Bigquery::Reservation::V1::FailoverMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-FailoverMode)) — Optional. A parameter that determines how writes that are pending replication are handled after a failover is initiated. If not specified, HARD failover mode is used by default. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::FailoverReservationRequest.new
    
    # Call the failover_reservation method.
    result = client.failover_reservation request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::Reservation.
    p result

### #get_bi_reservation
    
    
    def get_bi_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation
    def get_bi_reservation(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation

Retrieves a BI reservation.

**Overloads**
    
    
    def get_bi_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation

Pass arguments to `get_bi_reservation` via a request object, either of type [GetBiReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetBiReservationRequest "Google::Cloud::Bigquery::Reservation::V1::GetBiReservationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::GetBiReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetBiReservationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_bi_reservation(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation

Pass arguments to `get_bi_reservation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the requested reservation, for example: `projects/{project_id}/locations/{location_id}/biReservation`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::BiReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-BiReservation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::BiReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-BiReservation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::GetBiReservationRequest.new
    
    # Call the get_bi_reservation method.
    result = client.get_bi_reservation request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::BiReservation.
    p result

### #get_capacity_commitment
    
    
    def get_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment
    def get_capacity_commitment(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Returns information about the capacity commitment.

**Overloads**
    
    
    def get_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `get_capacity_commitment` via a request object, either of type [GetCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetCapacityCommitmentRequest "Google::Cloud::Bigquery::Reservation::V1::GetCapacityCommitmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::GetCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetCapacityCommitmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_capacity_commitment(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `get_capacity_commitment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the capacity commitment to retrieve. E.g., `projects/myproject/locations/US/capacityCommitments/123`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::GetCapacityCommitmentRequest.new
    
    # Call the get_capacity_commitment method.
    result = client.get_capacity_commitment request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment.
    p result

### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Gets the access control policy for a resource. May return:

  * A`NOT_FOUND` error if the resource doesn't exist or you don't have the permission to view it.
  * An empty policy if the resource exists but doesn't have a set policy.



Supported resources are:

  * Reservations
  * ReservationAssignments



To call this method, you must have the following Google IAM permissions:

  * `bigqueryreservation.reservations.getIamPolicy` to get policies on reservations.



**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type [Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-GetIamPolicyRequest "Google::Iam::V1::GetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-GetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. 
  * **options** ([::Google::Iam::V1::GetPolicyOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-GetPolicyOptions), ::Hash) — OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::GetIamPolicyRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #get_reservation
    
    
    def get_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation
    def get_reservation(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Returns information about the reservation.

**Overloads**
    
    
    def get_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `get_reservation` via a request object, either of type [GetReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetReservationRequest "Google::Cloud::Bigquery::Reservation::V1::GetReservationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::GetReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetReservationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_reservation(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `get_reservation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the reservation to retrieve. E.g., `projects/myproject/locations/US/reservations/team1-prod`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::GetReservationRequest.new
    
    # Call the get_reservation method.
    result = client.get_reservation request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::Reservation.
    p result

### #get_reservation_group
    
    
    def get_reservation_group(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup
    def get_reservation_group(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Returns information about the reservation group.

**Overloads**
    
    
    def get_reservation_group(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Pass arguments to `get_reservation_group` via a request object, either of type [GetReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetReservationGroupRequest "Google::Cloud::Bigquery::Reservation::V1::GetReservationGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::GetReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-GetReservationGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_reservation_group(name: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Pass arguments to `get_reservation_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the reservation group to retrieve. E.g., `projects/myproject/locations/US/reservationGroups/team1-prod`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::GetReservationGroupRequest.new
    
    # Call the get_reservation_group method.
    result = client.get_reservation_group request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::ReservationGroup.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ReservationService client object.

**Yields**

  * (config) — Configure the ReservationService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_assignments
    
    
    def list_assignments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>
    def list_assignments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Lists assignments.

Only explicitly created assignments will be returned.

Example:

  * Organization `organizationA` contains two projects, `project1` and `project2`.
  * Reservation `res1` exists and was created previously.
  * CreateAssignment was used previously to define the following associations between entities and reservations: `<organizationA, res1>` and `<project1, res1>`



In this example, ListAssignments will just return the above two assignments for reservation `res1`, and no expansion/merge will happen.

The wildcard "-" can be used for reservations in the request. In that case all assignments belongs to the specified project and location will be listed.

**Note** "-" cannot be used for projects nor locations.

**Overloads**
    
    
    def list_assignments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Pass arguments to `list_assignments` via a request object, either of type [ListAssignmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListAssignmentsRequest "Google::Cloud::Bigquery::Reservation::V1::ListAssignmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::ListAssignmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListAssignmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_assignments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Pass arguments to `list_assignments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name e.g.:

`projects/myproject/locations/US/reservations/team1-prod`

Or:

`projects/myproject/locations/US/reservations/-`

  * **page_size** (::Integer) — The maximum number of items to return per page. 
  * **page_token** (::String) — The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::ListAssignmentsRequest.new
    
    # Call the list_assignments method.
    result = client.list_assignments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Reservation::V1::Assignment.
      p item
    end

### #list_capacity_commitments
    
    
    def list_capacity_commitments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment>
    def list_capacity_commitments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment>

Lists all the capacity commitments for the admin project.

**Overloads**
    
    
    def list_capacity_commitments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment>

Pass arguments to `list_capacity_commitments` via a request object, either of type [ListCapacityCommitmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListCapacityCommitmentsRequest "Google::Cloud::Bigquery::Reservation::V1::ListCapacityCommitmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::ListCapacityCommitmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListCapacityCommitmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_capacity_commitments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment>

Pass arguments to `list_capacity_commitments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of the parent reservation. E.g., `projects/myproject/locations/US`
  * **page_size** (::Integer) — The maximum number of items to return. 
  * **page_token** (::String) — The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::ListCapacityCommitmentsRequest.new
    
    # Call the list_capacity_commitments method.
    result = client.list_capacity_commitments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment.
      p item
    end

### #list_reservation_groups
    
    
    def list_reservation_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup>
    def list_reservation_groups(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup>

Lists all the reservation groups for the project in the specified location.

**Overloads**
    
    
    def list_reservation_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup>

Pass arguments to `list_reservation_groups` via a request object, either of type [ListReservationGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListReservationGroupsRequest "Google::Cloud::Bigquery::Reservation::V1::ListReservationGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::ListReservationGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListReservationGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_reservation_groups(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup>

Pass arguments to `list_reservation_groups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name containing project and location, e.g.: `projects/myproject/locations/US`
  * **page_size** (::Integer) — The maximum number of items to return per page. 
  * **page_token** (::String) — The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::ListReservationGroupsRequest.new
    
    # Call the list_reservation_groups method.
    result = client.list_reservation_groups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup.
      p item
    end

### #list_reservations
    
    
    def list_reservations(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Reservation>
    def list_reservations(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Reservation>

Lists all the reservations for the project in the specified location.

**Overloads**
    
    
    def list_reservations(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Reservation>

Pass arguments to `list_reservations` via a request object, either of type [ListReservationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListReservationsRequest "Google::Cloud::Bigquery::Reservation::V1::ListReservationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::ListReservationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ListReservationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_reservations(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Reservation>

Pass arguments to `list_reservations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name containing project and location, e.g.: `projects/myproject/locations/US`
  * **page_size** (::Integer) — The maximum number of items to return per page. 
  * **page_token** (::String) — The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::ListReservationsRequest.new
    
    # Call the list_reservations method.
    result = client.list_reservations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Reservation::V1::Reservation.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #merge_capacity_commitments
    
    
    def merge_capacity_commitments(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment
    def merge_capacity_commitments(parent: nil, capacity_commitment_ids: nil, capacity_commitment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Merges capacity commitments of the same plan into a single commitment.

The resulting capacity commitment has the greater commitment_end_time out of the to-be-merged capacity commitments.

Attempting to merge capacity commitments of different plan will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`.

**Overloads**
    
    
    def merge_capacity_commitments(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `merge_capacity_commitments` via a request object, either of type [MergeCapacityCommitmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-MergeCapacityCommitmentsRequest "Google::Cloud::Bigquery::Reservation::V1::MergeCapacityCommitmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::MergeCapacityCommitmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-MergeCapacityCommitmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def merge_capacity_commitments(parent: nil, capacity_commitment_ids: nil, capacity_commitment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `merge_capacity_commitments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Parent resource that identifies admin project and location e.g., `projects/myproject/locations/us`
  * **capacity_commitment_ids** (::Array<::String>) — Ids of capacity commitments to merge. These capacity commitments must exist under admin project and location specified in the parent. ID is the last portion of capacity commitment name e.g., 'abc' for projects/myproject/locations/US/capacityCommitments/abc 
  * **capacity_commitment_id** (::String) — Optional. The optional resulting capacity commitment ID. Capacity commitment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character cannot be a dash. Max length is 64 characters. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::MergeCapacityCommitmentsRequest.new
    
    # Call the merge_capacity_commitments method.
    result = client.merge_capacity_commitments request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment.
    p result

### #move_assignment
    
    
    def move_assignment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment
    def move_assignment(name: nil, destination_id: nil, assignment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Moves an assignment under a new reservation.

This differs from removing an existing assignment and recreating a new one by providing a transactional change that ensures an assignee always has an associated reservation.

**Overloads**
    
    
    def move_assignment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Pass arguments to `move_assignment` via a request object, either of type [MoveAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-MoveAssignmentRequest "Google::Cloud::Bigquery::Reservation::V1::MoveAssignmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::MoveAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-MoveAssignmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def move_assignment(name: nil, destination_id: nil, assignment_id: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Pass arguments to `move_assignment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the assignment, e.g. `projects/myproject/locations/US/reservations/team1-prod/assignments/123`
  * **destination_id** (::String) — The new reservation ID, e.g.: `projects/myotherproject/locations/US/reservations/team2-prod`
  * **assignment_id** (::String) — The optional assignment ID. A new assignment name is generated if this field is empty.

This field can contain only lowercase alphanumeric characters or dashes. Max length is 64 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::MoveAssignmentRequest.new
    
    # Call the move_assignment method.
    result = client.move_assignment request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::Assignment.
    p result

### #search_all_assignments
    
    
    def search_all_assignments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>
    def search_all_assignments(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Looks up assignments for a specified resource for a particular region. If the request is about a project:

  1. Assignments created on the project will be returned if they exist.
  2. Otherwise assignments created on the closest ancestor will be returned.
  3. Assignments for different JobTypes will all be returned.



The same logic applies if the request is about a folder.

If the request is about an organization, then assignments created on the organization will be returned (organization doesn't have ancestors).

Comparing to ListAssignments, there are some behavior differences:

  1. permission on the assignee will be verified in this API.
  2. Hierarchy lookup (project->folder->organization) happens in this API.
  3. Parent here is `projects/_/locations/_`, instead of `projects/_/locations/_ reservations/*`.



**Overloads**
    
    
    def search_all_assignments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Pass arguments to `search_all_assignments` via a request object, either of type [SearchAllAssignmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SearchAllAssignmentsRequest "Google::Cloud::Bigquery::Reservation::V1::SearchAllAssignmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::SearchAllAssignmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SearchAllAssignmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def search_all_assignments(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Pass arguments to `search_all_assignments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name with location (project name could be the wildcard '-'), e.g.: `projects/-/locations/US`. 
  * **query** (::String) — 

Please specify resource name as assignee in the query.

Examples:

    * `assignee=projects/myproject`
    * `assignee=folders/123`
    * `assignee=organizations/456`
  * **page_size** (::Integer) — The maximum number of items to return per page. 
  * **page_token** (::String) — The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::SearchAllAssignmentsRequest.new
    
    # Call the search_all_assignments method.
    result = client.search_all_assignments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Reservation::V1::Assignment.
      p item
    end

### #search_assignments
    
    
    def search_assignments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>
    def search_assignments(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Deprecated: Looks up assignments for a specified resource for a particular region. If the request is about a project:

  1. Assignments created on the project will be returned if they exist.
  2. Otherwise assignments created on the closest ancestor will be returned.
  3. Assignments for different JobTypes will all be returned.



The same logic applies if the request is about a folder.

If the request is about an organization, then assignments created on the organization will be returned (organization doesn't have ancestors).

Comparing to ListAssignments, there are some behavior differences:

  1. permission on the assignee will be verified in this API.
  2. Hierarchy lookup (project->folder->organization) happens in this API.
  3. Parent here is `projects/_/locations/_`, instead of `projects/_/locations/_ reservations/*`.



**Note** "-" cannot be used for projects nor locations.

**Overloads**
    
    
    def search_assignments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Pass arguments to `search_assignments` via a request object, either of type [SearchAssignmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SearchAssignmentsRequest "Google::Cloud::Bigquery::Reservation::V1::SearchAssignmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::SearchAssignmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SearchAssignmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def search_assignments(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::Reservation::V1::Assignment>

Pass arguments to `search_assignments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the admin project(containing project and location), e.g.: `projects/myproject/locations/US`. 
  * **query** (::String) — 

Please specify resource name as assignee in the query.

Examples:

    * `assignee=projects/myproject`
    * `assignee=folders/123`
    * `assignee=organizations/456`
  * **page_size** (::Integer) — The maximum number of items to return per page. 
  * **page_token** (::String) — The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::SearchAssignmentsRequest.new
    
    # Call the search_assignments method.
    result = client.search_assignments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Reservation::V1::Assignment.
      p item
    end

### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Sets an access control policy for a resource. Replaces any existing policy.

Supported resources are:

  * Reservations



To call this method, you must have the following Google IAM permissions:

  * `bigqueryreservation.reservations.setIamPolicy` to set policies on reservations.



**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type [Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-SetIamPolicyRequest "Google::Iam::V1::SetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-SetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 
  * **policy** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-Policy), ::Hash) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::SetIamPolicyRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #split_capacity_commitment
    
    
    def split_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentResponse
    def split_capacity_commitment(name: nil, slot_count: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentResponse

Splits capacity commitment to two commitments of the same plan and `commitment_end_time`.

A common use case is to enable downgrading commitments.

For example, in order to downgrade from 10000 slots to 8000, you might split a 10000 capacity commitment into commitments of 2000 and 8000. Then, you delete the first one after the commitment end time passes.

**Overloads**
    
    
    def split_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentResponse

Pass arguments to `split_capacity_commitment` via a request object, either of type [SplitCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SplitCapacityCommitmentRequest "Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SplitCapacityCommitmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def split_capacity_commitment(name: nil, slot_count: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentResponse

Pass arguments to `split_capacity_commitment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name e.g.,: `projects/myproject/locations/US/capacityCommitments/123`
  * **slot_count** (::Integer) — Number of slots in the capacity commitment after the split. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SplitCapacityCommitmentResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SplitCapacityCommitmentResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentRequest.new
    
    # Call the split_capacity_commitment method.
    result = client.split_capacity_commitment request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::SplitCapacityCommitmentResponse.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Gets your permissions on a resource. Returns an empty set of permissions if the resource doesn't exist.

Supported resources are:

  * Reservations



No Google IAM permissions are required to call this method.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-TestIamPermissionsRequest "Google::Iam::V1::TestIamPermissionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-TestIamPermissionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. 
  * **permissions** (::Array<::String>) — The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::TestIamPermissionsRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Iam::V1::TestIamPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_assignment
    
    
    def update_assignment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment
    def update_assignment(assignment: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Updates an existing assignment.

Only the `priority` field can be updated.

**Overloads**
    
    
    def update_assignment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Pass arguments to `update_assignment` via a request object, either of type [UpdateAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateAssignmentRequest "Google::Cloud::Bigquery::Reservation::V1::UpdateAssignmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::UpdateAssignmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateAssignmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_assignment(assignment: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment

Pass arguments to `update_assignment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **assignment** ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment), ::Hash) — Content of the assignment to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Standard field mask for the set of fields to be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Assignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::UpdateAssignmentRequest.new
    
    # Call the update_assignment method.
    result = client.update_assignment request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::Assignment.
    p result

### #update_bi_reservation
    
    
    def update_bi_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation
    def update_bi_reservation(bi_reservation: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation

Updates a BI reservation.

Only fields specified in the `field_mask` are updated.

A singleton BI reservation always exists with default size 0. In order to reserve BI capacity it needs to be updated to an amount greater than 0. In order to release BI capacity reservation size must be set to 0.

**Overloads**
    
    
    def update_bi_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation

Pass arguments to `update_bi_reservation` via a request object, either of type [UpdateBiReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateBiReservationRequest "Google::Cloud::Bigquery::Reservation::V1::UpdateBiReservationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::UpdateBiReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateBiReservationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_bi_reservation(bi_reservation: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::BiReservation

Pass arguments to `update_bi_reservation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **bi_reservation** ([::Google::Cloud::Bigquery::Reservation::V1::BiReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-BiReservation), ::Hash) — A reservation to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — A list of fields to be updated in this request. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::BiReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-BiReservation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::BiReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-BiReservation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::UpdateBiReservationRequest.new
    
    # Call the update_bi_reservation method.
    result = client.update_bi_reservation request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::BiReservation.
    p result

### #update_capacity_commitment
    
    
    def update_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment
    def update_capacity_commitment(capacity_commitment: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Updates an existing capacity commitment.

Only `plan` and `renewal_plan` fields can be updated.

Plan can only be changed to a plan of a longer commitment period. Attempting to change to a plan with shorter commitment period will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`.

**Overloads**
    
    
    def update_capacity_commitment(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `update_capacity_commitment` via a request object, either of type [UpdateCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateCapacityCommitmentRequest "Google::Cloud::Bigquery::Reservation::V1::UpdateCapacityCommitmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::UpdateCapacityCommitmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateCapacityCommitmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_capacity_commitment(capacity_commitment: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment

Pass arguments to `update_capacity_commitment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **capacity_commitment** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment), ::Hash) — Content of the capacity commitment to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Standard field mask for the set of fields to be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::UpdateCapacityCommitmentRequest.new
    
    # Call the update_capacity_commitment method.
    result = client.update_capacity_commitment request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment.
    p result

### #update_reservation
    
    
    def update_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation
    def update_reservation(reservation: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Updates an existing reservation resource.

**Overloads**
    
    
    def update_reservation(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `update_reservation` via a request object, either of type [UpdateReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateReservationRequest "Google::Cloud::Bigquery::Reservation::V1::UpdateReservationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::UpdateReservationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateReservationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_reservation(reservation: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation

Pass arguments to `update_reservation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **reservation** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation), ::Hash) — Content of the reservation to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Standard field mask for the set of fields to be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::UpdateReservationRequest.new
    
    # Call the update_reservation method.
    result = client.update_reservation request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::Reservation.
    p result

### #update_reservation_group
    
    
    def update_reservation_group(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup
    def update_reservation_group(reservation_group: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Updates an existing reservation group resource.

**Overloads**
    
    
    def update_reservation_group(request, options = nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Pass arguments to `update_reservation_group` via a request object, either of type [UpdateReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateReservationGroupRequest "Google::Cloud::Bigquery::Reservation::V1::UpdateReservationGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Reservation::V1::UpdateReservationGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-UpdateReservationGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_reservation_group(reservation_group: nil, update_mask: nil) -> ::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup

Pass arguments to `update_reservation_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **reservation_group** ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup), ::Hash) — Required. Content of the reservation group to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Standard field mask for the set of fields to be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::ReservationGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationGroup)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/reservation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Reservation::V1::UpdateReservationGroupRequest.new
    
    # Call the update_reservation_group method.
    result = client.update_reservation_group request
    
    # The returned object is of type Google::Cloud::Bigquery::Reservation::V1::ReservationGroup.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
