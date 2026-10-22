---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-replicated-cluster/
title: Create a replicated cluster \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:29.738264+00:00
---

# Create a replicated cluster  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-replicated-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Create a replicated cluster Stay organized with collections  Save and categorize content based on your preferences. 

Create a replicated cluster in the current project.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::future;
    using ::google::cloud::Location;
    using ::google::cloud::Project;
    using ::google::cloud::StatusOr;
    
    [](cbta::BigtableInstanceAdminClient instance_admin,
       std::string const& project_id, std::string const& instance_id,
       std::string const& zone_a, std::string const& zone_b) {
      auto const project = Project(project_id);
      std::string project_name = project.FullName();
      std::string c1 = instance_id + "-c1";
      std::string c2 = instance_id + "-c2";
    
      google::bigtable::admin::v2::Instance in;
      in.set_type(google::bigtable::admin::v2::Instance::PRODUCTION);
      in.set_display_name("Put description here");
    
      google::bigtable::admin::v2::Cluster cluster1;
      cluster1.set_location(Location(project, zone_a).FullName());
      cluster1.set_serve_nodes(3);
      cluster1.set_default_storage_type(google::bigtable::admin::v2::HDD);
    
      google::bigtable::admin::v2::Cluster cluster2;
      cluster2.set_location(Location(project, zone_b).FullName());
      cluster2.set_serve_nodes(3);
      cluster2.set_default_storage_type(google::bigtable::admin::v2::HDD);
    
      std::map<std::string, google::bigtable::admin::v2::Cluster> cluster_map = {
          {c1, std::move(cluster1)}, {c2, std::move(cluster2)}};
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
