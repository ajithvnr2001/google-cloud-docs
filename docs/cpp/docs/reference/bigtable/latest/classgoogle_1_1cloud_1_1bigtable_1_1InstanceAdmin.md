---
url: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin/
title: Class InstanceAdmin (2.47.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:58.209744+00:00
---

# Class InstanceAdmin (2.47.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class InstanceAdmin (2.47.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Implements the APIs to administer Cloud Bigtable instances. 

###### Thread-safety

Instances of this class created via copy-construction or copy-assignment share the underlying pool of connections. Access to these copies via multiple threads is guaranteed to work. Two threads operating concurrently on the same instance of this class is not guaranteed to work.

###### Cost

Creating a new object of type [`InstanceAdmin`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin) is comparable to creating a few objects of type `std::string` or a few objects of type `std::shared_ptr<int>`. The class represents a shallow handle to a remote object.

###### Error Handling

This class uses [`StatusOr`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` to report errors. When an operation fails to perform its work the returned [`StatusOr`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains the error details. If the `ok()` member function in the [`StatusOr`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` returns `true` then it contains the expected result. Operations that do not return a value simply return a [`google::cloud::Status`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) indicating success or the details of the error Please consult the [`StatusOr` documentation](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) for more details.
    
    
    namespace cbt = google::cloud::bigtable;
    namespace btadmin = google::bigtable::admin::v2;
    cbt::InstanceAdmin admin = ...;
    google::cloud::StatusOr<btadmin::Instance> instance = admin.GetInstance(...);
    
    if (!instance) {
      std::cerr << "Error fetching instance\n";
      return;
    }
    
    // Use `instance` as a smart pointer here, e.g.:
    std::cout << "The full instance name is " << instance->name() << "\n";
    

In addition, the [main page](about:invalid#zCSafez) contains examples using [`StatusOr`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` to handle errors.

###### Retry, Backoff, and Idempotency Policies

The library automatically retries requests that fail with transient errors, and uses [truncated exponential backoff](https://cloud.google.com/storage/docs/exponential-backoff) to backoff between retries. The default policies are to continue retrying for up to 10 minutes. On each transient failure the backoff period is doubled, starting with an initial backoff of 100 milliseconds. The backoff period growth is truncated at 60 seconds. The default idempotency policy is to only retry idempotent operations. Note that most operations that change state are **not** idempotent. The application can override these policies when constructing objects of this class. The documentation for the constructors show examples of this in action.

###### See Also

<https://cloud.google.com/bigtable/> for an overview of Cloud Bigtable.

###### See Also

<https://cloud.google.com/bigtable/docs/overview> for an overview of the Cloud Bigtable data model.

###### See Also

<https://cloud.google.com/bigtable/docs/instances-clusters-nodes> for an introduction of the main APIs into Cloud Bigtable.

###### See Also

<https://cloud.google.com/bigtable/docs/reference/service-apis-overview> for an overview of the underlying Cloud Bigtable API.

###### See Also

[`google::cloud::StatusOr`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) for a description of the error reporting class used by this library.

###### See Also

[`LimitedTimeRetryPolicy`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1LimitedTimeRetryPolicy) and [`LimitedErrorCountRetryPolicy`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1LimitedErrorCountRetryPolicy) for alternative retry policies.

###### See Also

[`ExponentialBackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1ExponentialBackoffPolicy) to configure different parameters for the exponential backoff policy.

###### See Also

[`SafeIdempotentMutationPolicy`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1SafeIdempotentMutationPolicy) and [`AlwaysRetryMutationPolicy`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1AlwaysRetryMutationPolicy) for alternative idempotency policies. 

## Constructors 

### InstanceAdmin(std::shared_ptr< bigtable_admin::BigtableInstanceAdminConnection >, std::string)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< bigtable_admin::BigtableInstanceAdminConnection >`   
  
`project` |  `std::string`   
  
  
### InstanceAdmin(std::shared_ptr< InstanceAdminClient >)

**Parameter**  
---  
**Name** | **Description**  
`client` |  `std::shared_ptr< InstanceAdminClient >`   
the interface to create grpc stubs, report errors, etc.   
  
### InstanceAdmin(std::shared_ptr< InstanceAdminClient >, Policies &&...)

Create a new [InstanceAdmin](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin) using explicit policies to handle RPC errors. 

###### See Also

[GenericPollingPolicy](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1GenericPollingPolicy), [ExponentialBackoffPolicy](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1ExponentialBackoffPolicy), [LimitedErrorCountRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1LimitedErrorCountRetryPolicy), [LimitedTimeRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1LimitedTimeRetryPolicy). 

**Parameters**  
---  
**Name** | **Description**  
`client` |  `std::shared_ptr< InstanceAdminClient >`   
the interface to create grpc stubs, report errors, etc.   
`policies` |  `Policies &&...`   
the set of policy overrides for this object.   
`typename...` |  ``   
  
  
## Functions 

### project_name() const

The full name (`projects/<project_id>`) of the project. 

**Returns**  
---  
**Type** | **Description**  
`std::string const &` |   
  
### project_id() const

The project id, i.e., [`project_name()`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin#classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin_1a2d46537e624d548137163c9e80624de9) without the `projects/` prefix. 

**Returns**  
---  
**Type** | **Description**  
`std::string const &` |   
  
### WithNewTarget(std::string) const

Returns an [InstanceAdmin](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin) that reuses the connection and configuration of this [InstanceAdmin](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1InstanceAdmin), but with a different resource name. 

**Parameter**  
---  
**Name** | **Description**  
`project_id` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`InstanceAdmin` |   
  
### InstanceName(std::string const &) const

Return the fully qualified name of the given instance_id. 

**Parameter**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
### ClusterName(std::string const &, std::string const &) const

Return the fully qualified name of the given cluster_id in give instance_id. 

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
  
`cluster_id` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
### AppProfileName(std::string const &, std::string const &) const

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
  
`profile_id` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
### CreateInstance(InstanceConfig)

Create a new instance of Cloud Bigtable. 

**Warning:** Note that this is operation can take seconds or minutes to complete. The application may prefer to perform other work while waiting for this operation. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::future;
      using ::google::cloud::Location;
      using ::google::cloud::Project;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& zone) {
        auto const project = Project(project_id);
        std::string project_name = project.FullName();
        std::string cluster_id = instance_id + "-c1";
    
        google::bigtable::admin::v2::Instance in;
        in.set_type(google::bigtable::admin::v2::Instance::PRODUCTION);
        in.set_display_name("Put description here");
    
        google::bigtable::admin::v2::Cluster cluster;
        cluster.set_location(Location(project, zone).FullName());
        cluster.set_serve_nodes(3);
        cluster.set_default_storage_type(google::bigtable::admin::v2::HDD);
    
        std::map<std::string, google::bigtable::admin::v2::Cluster> cluster_map = {
            {cluster_id, std::move(cluster)}};
    
        future<StatusOr<google::bigtable::admin::v2::Instance>> instance_future =
            instance_admin.CreateInstance(project_name, instance_id, std::move(in),
                                          std::move(cluster_map));
        // Show how to perform additional work while the long running operation
        // completes. The application could use future.then() instead.
        std::cout << "Waiting for instance creation to complete " << std::flush;
        instance_future.wait_for(std::chrono::seconds(1));
        std::cout << '.' << std::flush;
        auto instance = instance_future.get();
        if (!instance) throw std::move(instance).status();
        std::cout << "DONE, details=" << instance->DebugString() << "\n";
      }
    

**Parameter**  
---  
**Name** | **Description**  
`instance_config` |  `InstanceConfig`   
a description of the new instance to be created. instance_id and a display_name parameters must be set in instance_config,

  * instance_id : must be between 6 and 33 characters.
  * display_name : must be between 4 and 30 characters. 

  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::bigtable::admin::v2::Instance > >` | a future that becomes satisfied when (a) the operation has completed successfully, in which case it returns a proto with the Instance details, (b) the operation has failed, in which case the future contains an [`google::cloud::Status`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) with the details of the failure, or (c) the state of the operation is unknown after the time allocated by the retry policies has expired, in which case the future contains the last error status.  
  
### CreateCluster(ClusterConfig, std::string const &, std::string const &)

Create a new Cluster of Cloud Bigtable. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::future;
      using ::google::cloud::Location;
      using ::google::cloud::Project;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& cluster_id, std::string const& zone) {
        auto const project = Project(project_id);
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
    
        google::bigtable::admin::v2::Cluster c;
        c.set_location(Location(project, zone).FullName());
        c.set_serve_nodes(3);
        c.set_default_storage_type(google::bigtable::admin::v2::HDD);
    
        future<StatusOr<google::bigtable::admin::v2::Cluster>> cluster_future =
            instance_admin.CreateCluster(instance_name, cluster_id, std::move(c));
    
        // Applications can wait asynchronously, in this example we just block.
        auto cluster = cluster_future.get();
        if (!cluster) throw std::move(cluster).status();
        std::cout << "Successfully created cluster " << cluster->name() << "\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`cluster_config` |  `ClusterConfig`   
a description of the new cluster to be created.   
`instance_id` |  `std::string const &`   
the id of the instance in the project   
`cluster_id` |  `std::string const &`   
the id of the cluster in the project that needs to be created. It must be between 6 and 30 characters.  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::bigtable::admin::v2::Cluster > >` |   
  
### UpdateInstance(InstanceUpdateConfig)

Update an existing instance of Cloud Bigtable. 

**Warning:** Note that this is operation can take seconds or minutes to complete. The application may prefer to perform other work while waiting for this operation. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::future;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        StatusOr<google::bigtable::admin::v2::Instance> instance =
            instance_admin.GetInstance(instance_name);
        if (!instance) throw std::move(instance).status();
        // Modify the instance and prepare the mask with the modified field
        instance->set_display_name("Modified Display Name");
        google::protobuf::FieldMask mask;
        mask.add_paths("display_name");
    
        future<StatusOr<google::bigtable::admin::v2::Instance>> instance_future =
            instance_admin.PartialUpdateInstance(std::move(*instance),
                                                 std::move(mask));
        instance_future
            .then([](future<StatusOr<google::bigtable::admin::v2::Instance>> f) {
              auto updated_instance = f.get();
              if (!updated_instance) {
                throw std::move(updated_instance).status();
              }
              std::cout << "UpdateInstance details : "
                        << updated_instance->DebugString() << "\n";
            })
            .get();  // block until done to simplify example
      }
    

**Parameter**  
---  
**Name** | **Description**  
`instance_update_config` |  `InstanceUpdateConfig`   
config with modified instance.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::bigtable::admin::v2::Instance > >` | a future that becomes satisfied when (a) the operation has completed successfully, in which case it returns a proto with the Instance details, (b) the operation has failed, in which case the future contains an exception (typically `bigtable::GrpcError`) with the details of the failure, or (c) the state of the operation is unknown after the time allocated by the retry policies has expired, in which case the future contains an exception of type `bigtable::PollTimeout`.  
  
### ListInstances()

Obtain the list of instances in the project. 

**Note:** In some circumstances Cloud Bigtable may be unable to obtain the full list of instances, typically because some transient failure has made specific zones unavailable. In this cases the service returns a separate list of `failed_locations` that represent the unavailable zones. Applications may want to retry the operation after the transient conditions have cleared. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::Project;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id) {
        std::string project_name = Project(project_id).FullName();
        StatusOr<google::bigtable::admin::v2::ListInstancesResponse> instances =
            instance_admin.ListInstances(project_name);
        if (!instances) throw std::move(instances).status();
        for (auto const& instance : instances->instances()) {
          std::cout << instance.name() << "\n";
        }
        if (!instances->failed_locations().empty()) {
          std::cout << "The Cloud Bigtable service reports that the following "
                       "locations are temporarily unavailable and no information "
                       "about instances in these locations can be obtained:\n";
          for (auto const& failed_location : instances->failed_locations()) {
            std::cout << failed_location << "\n";
          }
        }
      }
    

**Returns**  
---  
**Type** | **Description**  
`StatusOr< InstanceList >` |   
  
### GetInstance(std::string const &)

Return the details of `instance_id`. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        StatusOr<google::bigtable::admin::v2::Instance> instance =
            instance_admin.GetInstance(instance_name);
        if (!instance) throw std::move(instance).status();
        std::cout << "GetInstance details : " << instance->DebugString() << "\n";
      }
    

**Parameter**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::bigtable::admin::v2::Instance >` |   
  
### DeleteInstance(std::string const &)

Deletes the instances in the project. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::Status;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        Status status = instance_admin.DeleteInstance(instance_name);
        if (!status.ok()) throw std::runtime_error(status.message());
        std::cout << "Successfully deleted the instance " << instance_id << "\n";
      }
    

**Parameter**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the id of the instance in the project that needs to be deleted  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### ListClusters()

Obtain the list of clusters in an instance. 

**Note:** In some circumstances Cloud Bigtable may be unable to obtain the full list of clusters, typically because some transient failure has made specific zones unavailable. In this cases the service returns a separate list of `failed_locations` that represent the unavailable zones. Applications may want to retry the operation after the transient conditions have cleared. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        StatusOr<google::bigtable::admin::v2::ListClustersResponse> clusters =
            instance_admin.ListClusters(instance_name);
        if (!clusters) throw std::move(clusters).status();
        std::cout << "Cluster Name List\n";
        for (auto const& cluster : clusters->clusters()) {
          std::cout << "Cluster Name:" << cluster.name() << "\n";
        }
        if (!clusters->failed_locations().empty()) {
          std::cout << "The Cloud Bigtable service reports that the following "
                       "locations are temporarily unavailable and no information "
                       "about clusters in these locations can be obtained:\n";
          for (auto const& failed_location : clusters->failed_locations()) {
            std::cout << failed_location << "\n";
          }
        }
      }
      (std::move(instance_admin), argv.at(0), argv.at(1));
    }
    
    void ListAllClusters(
        google::cloud::bigtable_admin::BigtableInstanceAdminClient instance_admin,
        std::vector<std::string> const& argv) {
    

**Returns**  
---  
**Type** | **Description**  
`StatusOr< ClusterList >` |   
  
### ListClusters(std::string const &)

Obtain the list of clusters in an instance. 

**Note:** In some circumstances Cloud Bigtable may be unable to obtain the full list of clusters, typically because some transient failure has made specific zones unavailable. In this cases the service returns a separate list of `failed_locations` that represent the unavailable zones. Applications may want to retry the operation after the transient conditions have cleared. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        StatusOr<google::bigtable::admin::v2::ListClustersResponse> clusters =
            instance_admin.ListClusters(instance_name);
        if (!clusters) throw std::move(clusters).status();
        std::cout << "Cluster Name List\n";
        for (auto const& cluster : clusters->clusters()) {
          std::cout << "Cluster Name:" << cluster.name() << "\n";
        }
        if (!clusters->failed_locations().empty()) {
          std::cout << "The Cloud Bigtable service reports that the following "
                       "locations are temporarily unavailable and no information "
                       "about clusters in these locations can be obtained:\n";
          for (auto const& failed_location : clusters->failed_locations()) {
            std::cout << failed_location << "\n";
          }
        }
      }
      (std::move(instance_admin), argv.at(0), argv.at(1));
    }
    
    void ListAllClusters(
        google::cloud::bigtable_admin::BigtableInstanceAdminClient instance_admin,
        std::vector<std::string> const& argv) {
    

**Parameter**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< ClusterList >` |   
  
### UpdateCluster(ClusterConfig)

Update an existing cluster of Cloud Bigtable. 

**Warning:** Note that this is operation can take seconds or minutes to complete. The application may prefer to perform other work while waiting for this operation. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& cluster_id) {
        std::string cluster_name =
            cbt::ClusterName(project_id, instance_id, cluster_id);
        // GetCluster first and then modify it.
        StatusOr<google::bigtable::admin::v2::Cluster> cluster =
            instance_admin.GetCluster(cluster_name);
        if (!cluster) throw std::move(cluster).status();
    
        // The state cannot be sent on updates, so clear it first.
        cluster->clear_state();
        // Set the desired cluster configuration.
        cluster->set_serve_nodes(4);
    
        auto modified_cluster =
            instance_admin.UpdateCluster(std::move(*cluster)).get();
        if (!modified_cluster) {
          throw std::move(modified_cluster).status();
        }
        std::cout << "cluster details : " << cluster->DebugString() << "\n";
      }
    

**Parameter**  
---  
**Name** | **Description**  
`cluster_config` |  `ClusterConfig`   
cluster with updated values.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::bigtable::admin::v2::Cluster > >` | a future that becomes satisfied when (a) the operation has completed successfully, in which case it returns a proto with the Instance details, (b) the operation has failed, in which case the future contains an exception (typically `bigtable::GrpcError`) with the details of the failure, or (c) the state of the operation is unknown after the time allocated by the retry policies has expired, in which case the future contains an exception of type `bigtable::PollTimeout`.  
  
### DeleteCluster(std::string const &, std::string const &)

Deletes the specified cluster of an instance in the project. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::Status;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& cluster_id) {
        std::string cluster_name =
            cbt::ClusterName(project_id, instance_id, cluster_id);
        Status status = instance_admin.DeleteCluster(cluster_name);
        if (!status.ok()) throw std::runtime_error(status.message());
      }
    

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the id of the instance in the project   
`cluster_id` |  `std::string const &`   
the id of the cluster in the project that needs to be deleted  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### GetCluster(std::string const &, std::string const &)

Gets the specified cluster of an instance in the project. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& cluster_id) {
        std::string cluster_name =
            cbt::ClusterName(project_id, instance_id, cluster_id);
        StatusOr<google::bigtable::admin::v2::Cluster> cluster =
            instance_admin.GetCluster(cluster_name);
        if (!cluster) throw std::move(cluster).status();
        std::cout << "GetCluster details : " << cluster->DebugString() << "\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the id of the instance in the project   
`cluster_id` |  `std::string const &`   
the id of the cluster in the project that needs to be deleted   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::bigtable::admin::v2::Cluster >` | a Cluster for given instance_id and cluster_id.  
  
### CreateAppProfile(std::string const &, AppProfileConfig)

Create a new application profile. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Multi-cluster Routing Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& profile_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
    
        google::bigtable::admin::v2::AppProfile ap;
        ap.mutable_multi_cluster_routing_use_any()->Clear();
    
        StatusOr<google::bigtable::admin::v2::AppProfile> profile =
            instance_admin.CreateAppProfile(instance_name, profile_id,
                                            std::move(ap));
        if (!profile) throw std::move(profile).status();
        std::cout << "New profile created with name=" << profile->name() << "\n";
      }
    

###### Single Cluster Routing Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& profile_id, std::string const& cluster_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
    
        google::bigtable::admin::v2::AppProfile ap;
        ap.mutable_single_cluster_routing()->set_cluster_id(cluster_id);
    
        StatusOr<google::bigtable::admin::v2::AppProfile> profile =
            instance_admin.CreateAppProfile(instance_name, profile_id,
                                            std::move(ap));
        if (!profile) throw std::move(profile).status();
        std::cout << "New profile created with name=" << profile->name() << "\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the instance for the new application profile.   
`config` |  `AppProfileConfig`   
the configuration for the new application profile.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::bigtable::admin::v2::AppProfile >` | The proto describing the new application profile.  
  
### GetAppProfile(std::string const &, std::string const &)

Fetch the detailed information about an existing application profile. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& profile_id) {
        std::string profile_name =
            cbt::AppProfileName(project_id, instance_id, profile_id);
        StatusOr<google::bigtable::admin::v2::AppProfile> profile =
            instance_admin.GetAppProfile(profile_name);
        if (!profile) throw std::move(profile).status();
        std::cout << "Application Profile details=" << profile->DebugString()
                  << "\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the instance to look the profile in.   
`profile_id` |  `std::string const &`   
the id of the profile within that instance.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::bigtable::admin::v2::AppProfile >` | The proto describing the application profile.  
  
### UpdateAppProfile(std::string const &, std::string const &, AppProfileUpdateConfig)

Updates an existing application profile. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Change Description Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::future;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& profile_id, std::string const& description) {
        std::string profile_name =
            cbt::AppProfileName(project_id, instance_id, profile_id);
    
        google::bigtable::admin::v2::AppProfile profile;
        profile.set_name(profile_name);
        profile.set_description(description);
    
        google::protobuf::FieldMask mask;
        mask.add_paths("description");
    
        future<StatusOr<google::bigtable::admin::v2::AppProfile>> profile_future =
            instance_admin.UpdateAppProfile(std::move(profile), std::move(mask));
        auto modified_profile = profile_future.get();
        if (!modified_profile) throw std::move(modified_profile).status();
        std::cout << "Updated AppProfile: " << modified_profile->DebugString()
                  << "\n";
      }
    

###### Change Routing to Any Cluster Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::future;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& profile_id) {
        std::string profile_name =
            cbt::AppProfileName(project_id, instance_id, profile_id);
    
        google::bigtable::admin::v2::UpdateAppProfileRequest req;
        req.mutable_app_profile()->set_name(profile_name);
        req.mutable_app_profile()->mutable_multi_cluster_routing_use_any()->Clear();
        req.mutable_update_mask()->add_paths("multi_cluster_routing_use_any");
        req.set_ignore_warnings(true);
    
        future<StatusOr<google::bigtable::admin::v2::AppProfile>> profile_future =
            instance_admin.UpdateAppProfile(std::move(req));
        auto modified_profile = profile_future.get();
        if (!modified_profile) throw std::move(modified_profile).status();
        std::cout << "Updated AppProfile: " << modified_profile->DebugString()
                  << "\n";
      }
    

###### Change Routing to a Specific Cluster Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::future;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& profile_id, std::string const& cluster_id) {
        std::string profile_name =
            cbt::AppProfileName(project_id, instance_id, profile_id);
    
        google::bigtable::admin::v2::UpdateAppProfileRequest req;
        req.mutable_app_profile()->set_name(profile_name);
        req.mutable_app_profile()->mutable_single_cluster_routing()->set_cluster_id(
            cluster_id);
        req.mutable_update_mask()->add_paths("single_cluster_routing");
        req.set_ignore_warnings(true);
    
        future<StatusOr<google::bigtable::admin::v2::AppProfile>> profile_future =
            instance_admin.UpdateAppProfile(std::move(req));
        auto modified_profile = profile_future.get();
        if (!modified_profile) throw std::move(modified_profile).status();
        std::cout << "Updated AppProfile: " << modified_profile->DebugString()
                  << "\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the instance for the new application profile.   
`profile_id` |  `std::string const &`   
the id (not the full name) of the profile to update.   
`config` |  `AppProfileUpdateConfig`   
the configuration for the new application profile.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::bigtable::admin::v2::AppProfile > >` | The proto describing the new application profile.  
  
### ListAppProfiles(std::string const &)

List the application profiles in an instance. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StreamRange;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        StreamRange<google::bigtable::admin::v2::AppProfile> profiles =
            instance_admin.ListAppProfiles(instance_name);
        std::cout << "The " << instance_id << " instance has "
                  << std::distance(profiles.begin(), profiles.end())
                  << " application profiles\n";
        for (auto& profile : profiles) {
          if (!profile) throw std::move(profile).status();
          std::cout << profile->DebugString() << "\n";
        }
      }
    

**Parameter**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the instance to list the profiles for.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::vector< google::bigtable::admin::v2::AppProfile > >` | a std::vector with the protos describing any profiles.  
  
### DeleteAppProfile(std::string const &, std::string const &, bool)

Delete an existing application profile. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::Status;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& profile_id, bool ignore_warnings) {
        std::string profile_name =
            cbt::AppProfileName(project_id, instance_id, profile_id);
    
        google::bigtable::admin::v2::DeleteAppProfileRequest req;
        req.set_name(profile_name);
        req.set_ignore_warnings(ignore_warnings);
    
        Status status = instance_admin.DeleteAppProfile(std::move(req));
        if (!status.ok()) throw std::runtime_error(status.message());
        std::cout << "Application Profile deleted\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the instance to look the profile in.   
`profile_id` |  `std::string const &`   
the id of the profile within that instance.   
`ignore_warnings` |  `bool`   
if true, ignore safety checks when deleting the application profile. This value is to to `true` by default. Passing `false` causes this function to fail even when no operations are pending.  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### GetNativeIamPolicy(std::string const &)

Gets the native policy for `instance_id`. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        StatusOr<google::iam::v1::Policy> policy =
            instance_admin.GetIamPolicy(instance_name);
        if (!policy) throw std::move(policy).status();
        std::cout << "The IAM Policy for " << instance_id << " is\n"
                  << policy->DebugString() << "\n";
      }
    

**Parameter**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the instance to query.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | google::iam::v1::Policy the full IAM policy for the instance.  
  
### SetIamPolicy(std::string const &, google::iam::v1::Policy const &)

Sets the IAM policy for an instance. 

**Warning:** ETags are currently not used by Cloud Bigtable. 

###### Idempotency

This operation is always treated as non-idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& project_id, std::string const& instance_id,
         std::string const& role, std::string const& member) {
        std::string instance_name = cbt::InstanceName(project_id, instance_id);
        StatusOr<google::iam::v1::Policy> current =
            instance_admin.GetIamPolicy(instance_name);
        if (!current) throw std::move(current).status();
        // This example adds the member to all existing bindings for that role. If
        // there are no such bindings, it adds a new one. This might not be what the
        // user wants, e.g. in case of conditional bindings.
        size_t num_added = 0;
        for (auto& binding : *current->mutable_bindings()) {
          if (binding.role() == role) {
            binding.add_members(member);
            ++num_added;
          }
        }
        if (num_added == 0) {
          *current->add_bindings() = cbt::IamBinding(role, {member});
        }
        StatusOr<google::iam::v1::Policy> policy =
            instance_admin.SetIamPolicy(instance_name, *current);
        if (!policy) throw std::move(policy).status();
        std::cout << "The IAM Policy for " << instance_id << " is\n"
                  << policy->DebugString() << "\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
which instance to set the IAM policy for.   
`iam_policy` |  `google::iam::v1::Policy const &`   
google::iam::v1::Policy object containing role and members.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | google::iam::v1::Policy the current IAM policy for the instance.  
  
### TestIamPermissions(std::string const &, std::vector< std::string > const &)

Returns a permission set that the caller has on the specified instance. 

###### Idempotency

This operation is read-only and therefore it is always idempotent.

###### Thread-safety

Two threads concurrently calling this member function on the same instance of this class are **not** guaranteed to work. Consider copying the object and using different copies in each thread.

###### Example
    
    
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
      [](cbta::BigtableInstanceAdminClient instance_admin,
         std::string const& resource_name,
         std::vector<std::string> const& permissions) {
        auto result = instance_admin.TestIamPermissions(resource_name, permissions);
        if (!result) throw std::move(result).status();
        std::cout << "The current user has the following permissions [";
        std::cout << absl::StrJoin(result->permissions(), ", ");
        std::cout << "]\n";
      }
    

###### See Also

<https://cloud.google.com/bigtable/docs/access-control> for a list of valid permissions on Google Cloud Bigtable. 

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `std::string const &`   
the ID of the instance to query.   
`permissions` |  `std::vector< std::string > const &`   
set of permissions to check for the resource.  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::vector< std::string > >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
