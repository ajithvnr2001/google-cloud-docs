---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-clusters/
title: List clusters \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:31.938310+00:00
---

# List clusters  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  List clusters Stay organized with collections  Save and categorize content based on your preferences. 

List all of the cluster names in an instance.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableInstanceAdminClient instance_admin,
       std::string const& project_id) {
      std::string instance_name = cbt::InstanceName(project_id, "-");
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

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    try {
      String parent = "projects/" + projectId + "/instances/" + instanceId;
      ListClustersRequest request = ListClustersRequest.newBuilder().setParent(parent).build();
      ListClustersResponse response = adminClient.listClusters(request);
      for (Cluster cluster : response.getClustersList()) {
        System.out.println(cluster.getName());
      }
    } catch (NotFoundException e) {
      System.err.println("Failed to list clusters from a non-existent instance: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListClustersRequest;
    
    /**
     * List clusters of an instance
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     */
    function list_instance_clusters(
        string $projectId,
        string $instanceId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
    
        $projectName = $instanceAdminClient->projectName($projectId);
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    
        printf('Listing Clusters:' . PHP_EOL);
        $listClustersRequest = (new ListClustersRequest())
            ->setParent($instanceName);
        $getClusters = $instanceAdminClient->listClusters($listClustersRequest)->getClusters();
        $clusters = $getClusters->getIterator();
    
        foreach ($clusters as $cluster) {
            print($cluster->getName() . PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("\nListing clusters...")
    for cluster in instance.list_clusters()[0]:
        print(cluster.cluster_id)

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    bigtable.instance(instance_id).clusters.all do |cluster|
      puts "Cluster: #{cluster.cluster_id}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
