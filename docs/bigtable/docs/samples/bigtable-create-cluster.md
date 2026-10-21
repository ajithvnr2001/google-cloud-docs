---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-cluster/
title: Create a cluster \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:50.899776+00:00
---

# Create a cluster  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Create a cluster in the current project, given an instance ID.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create an additional cluster with cluster id "ssd-cluster2" with 3 nodes and location us-east1-d.
    // Additional cluster can only be created in PRODUCTION type instance.
    // Additional cluster must have same storage type as existing cluster.
    // Please read about routing_policy for more information on mutli cluster instances.
    // https://cloud.google.com/bigtable/docs/reference/admin/rpc/google.bigtable.admin.v2#google.bigtable.admin.v2.AppProfile.MultiClusterRoutingUseAny
    // Cluster to be created within the instance.
    Cluster myCluster2 = new Cluster
    {
        DefaultStorageType = StorageType.Ssd,
        LocationAsLocationName = new LocationName(projectId, zone2),
        ServeNodes = 3
    };
    // Initialize request argument(s).
    CreateClusterRequest request = new CreateClusterRequest
    {
        ParentAsInstanceName = new InstanceName(projectId, instanceId),
        ClusterId = "ssd-cluster2",
        Cluster = myCluster2
    };
    try
    {
        // Make the request
        Console.WriteLine("Waiting for operation to complete...");
        Operation<Cluster, CreateClusterMetadata> response = bigtableInstanceAdminClient.CreateCluster(request);
        // Poll until the returned long-running operation is complete
        Operation<Cluster, CreateClusterMetadata> completedResponse = response.PollUntilCompleted();
    
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Exception creating additional cluster {request.ClusterId} in instance {instanceId}");
        Console.WriteLine(ex.Message);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    try {
      String parent = "projects/" + projectId + "/instances/" + instanceId;
      Cluster clusterObj =
          Cluster.newBuilder()
              .setLocation("projects/" + projectId + "/locations/us-central1-c")
              .setServeNodes(3)
              .setDefaultStorageType(StorageType.SSD)
              .build();
      CreateClusterRequest request =
          CreateClusterRequest.newBuilder()
              .setParent(parent)
              .setClusterId(CLUSTER)
              .setCluster(clusterObj)
              .build();
      adminClient.createClusterAsync(request).get();
      System.out.printf("Cluster: %s created successfully%n", CLUSTER);
    } catch (Exception e) {
      System.err.println("Failed to add cluster: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Cluster;
    use Google\Cloud\Bigtable\Admin\V2\CreateClusterRequest;
    use Google\Cloud\Bigtable\Admin\V2\GetClusterRequest;
    use Google\Cloud\Bigtable\Admin\V2\GetInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\ListClustersRequest;
    use Google\Cloud\Bigtable\Admin\V2\StorageType;
    
    /**
     * Create a cluster in an existing Bigtable instance
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the parent Bigtable instance
     * @param string $clusterId The ID of the cluster to be generated
     * @param string $locationId The Bigtable region ID where you want your cluster to reside
     */
    function create_cluster(
        string $projectId,
        string $instanceId,
        string $clusterId,
        string $locationId = 'us-east1-b'
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
    
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
        $clusterName = $instanceAdminClient->clusterName($projectId, $instanceId, $clusterId);
    
        printf('Adding Cluster to Instance %s' . PHP_EOL, $instanceId);
        try {
            $getInstanceRequest = (new GetInstanceRequest())
                ->setName($instanceName);
            $instanceAdminClient->getInstance($getInstanceRequest);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Instance %s does not exists.' . PHP_EOL, $instanceId);
                return;
            } else {
                throw $e;
            }
        }
        printf('Listing Clusters:' . PHP_EOL);
    
        $storage_type = StorageType::SSD;
        $serve_nodes = 3;
        $listClustersRequest = (new ListClustersRequest())
            ->setParent($instanceName);
    
        $clustersBefore = $instanceAdminClient->listClusters($listClustersRequest)->getClusters();
        $clusters = $clustersBefore->getIterator();
        foreach ($clusters as $cluster) {
            print($cluster->getName() . PHP_EOL);
        }
    
        $cluster = new Cluster();
        $cluster->setServeNodes($serve_nodes);
        $cluster->setDefaultStorageType($storage_type);
        $cluster->setLocation(
            $instanceAdminClient->locationName(
                $projectId,
                $locationId
            )
        );
        try {
            $getClusterRequest = (new GetClusterRequest())
                ->setName($clusterName);
            $instanceAdminClient->getCluster($getClusterRequest);
            printf('Cluster %s already exists, aborting...', $clusterId);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                $createClusterRequest = (new CreateClusterRequest())
                    ->setParent($instanceName)
                    ->setClusterId($clusterId)
                    ->setCluster($cluster);
                $operationResponse = $instanceAdminClient->createCluster($createClusterRequest);
    
                $operationResponse->pollUntilComplete();
                if ($operationResponse->operationSucceeded()) {
                    $result = $operationResponse->getResult();
                    printf('Cluster created: %s', $clusterId);
                } else {
                    $error = $operationResponse->getError();
                    printf('Cluster not created: %s', $error?->getMessage());
                }
            } else {
                throw $e;
            }
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("\nListing clusters...")
    for cluster in instance.list_clusters()[0]:
        print(cluster.cluster_id)
    cluster = instance.cluster(
        cluster_id,
        location_id=location_id,
        serve_nodes=serve_nodes,
        default_storage_type=storage_type,
    )
    if cluster.exists():
        print("\nCluster not created, as {} already exists.".format(cluster_id))
    else:
        operation = cluster.create()
        # Ensure the operation completes.
        operation.result(timeout=480)
        print("\nCluster created: {}".format(cluster_id))

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # cluster_id       = "my-cluster"
    # cluster_location = "us-east1-b"
    job = instance.create_cluster(
      cluster_id,
      cluster_location,
      nodes:        3,
      storage_type: :SSD
    )
    
    job.wait_until_done!
    cluster = job.cluster

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
