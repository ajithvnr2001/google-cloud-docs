---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-prod-instance/
title: Create a production instance \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:22.888399+00:00
---

# Create a production instance  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-prod-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Create a production instance Stay organized with collections  Save and categorize content based on your preferences. 

Create a production instance in the current project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance)



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

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a production instance with "<intanceId>-prod" instance ID,
    // with cluster ID "ssd-cluster1", 3 nodes and location us-east1-b.
    displayName += " Prod"; // Display name is for display purposes only. It doesn't have to equal instanceId and can be amended after instance is created.
    string instanceId = Regex.Replace(displayName, @"[^A-Za-z0-9_\.~]+", "-").ToLower();
    
    // Please refer to the link below for the full list of available locations:
    // https://cloud.google.com/bigtable/docs/locations
    string zone1 = "us-east1-b";
    
    // The instance to create.
    Instance myInstance = new Instance
    {
        DisplayName = displayName,
        // You can choose DEVELOPMENT or PRODUCTION type here.
        // If not set, will default to PRODUCTION type.
        // Instance type can be upgraded from DEVELOPMENT to PRODUCTION but cannot be dowgraded after the instance is created.
        Type = Instance.Types.Type.Production,
        Labels = { { "prod-label", "prod-label" } }
    };
    
    // The first cluster to be created within the instance.
    Cluster myCluster1 = new Cluster
    {
        // You can choose SSD or HDD storage type here: StorageType.Ssd or StorageType.Hdd.
        // Cluster storage type can not be changed after the instance is created.
        // If not set will default to SSD type.
        DefaultStorageType = StorageType.Ssd,
        LocationAsLocationName = new LocationName(projectId, zone1),
        // Serve Nodes count can only be set if PRODUCTION type instance is being created.
        // Minimum count of 3 serve nodes must be specified.
        // Serve Nodes count can be increased and decreased after an instance is created.
        ServeNodes = 3
    };
    
    // Initialize request argument(s).
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsProjectName = new ProjectName(projectId),
        Instance = myInstance,
        InstanceId = instanceId,
        // Must specify at lease one cluster.
        // Only PRODUCTION type instance can be created with more than one cluster.
        // Currently all clusters must have the same storage type.
        // Clusters must be set to different locations.
        Clusters = { { "ssd-cluster1", myCluster1 } }
    };
    
    try
    {
        // Make a request.
        Operation<Instance, CreateInstanceMetadata> createInstanceResponse =
            bigtableInstanceAdminClient.CreateInstance(request);
        Console.WriteLine("Waiting for operation to complete...");
    
        // Poll until the returned long-running operation is complete
        Operation<Instance, CreateInstanceMetadata> completedResponse =
            createInstanceResponse.PollUntilCompleted();
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Exception while creating {displayName} instance");
        Console.WriteLine(ex.Message);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a Production Instance with the ID "ssd-instance",
    // cluster id "ssd-cluster", 3 nodes and location "us-central1-f".
    String parent = "projects/" + projectId;
    Instance.Builder instanceObjBuilder =
        Instance.newBuilder()
            .setDisplayName(instanceId)
            .setType(Instance.Type.PRODUCTION)
            .putLabels("department", "accounting");
    
    if (createWithTags) {
      System.out.println("Enabling tags for instance creation.");
      // These are placeholders. You must create these in your GCP Organization/Project first.
      String tagKey = "tagKeys/12345";
      String tagValue = "tagValues/6789";
      instanceObjBuilder.putTags(tagKey, tagValue);
    }
    Instance instanceObj = instanceObjBuilder.build();
    
    Cluster clusterObj =
        Cluster.newBuilder()
            .setLocation("projects/" + projectId + "/locations/us-central1-f")
            .setServeNodes(3)
            .setDefaultStorageType(StorageType.SSD)
            .build();
    CreateInstanceRequest request =
        CreateInstanceRequest.newBuilder()
            .setParent(parent)
            .setInstanceId(instanceId)
            .setInstance(instanceObj)
            .putClusters(clusterId, clusterObj)
            .build();
    // Creates a production instance with the given request.
    try {
      Instance instance = adminClient.createInstanceAsync(request).get();
      System.out.printf("PRODUCTION type instance %s created successfully%n", instance.getName());
    } catch (Exception e) {
      System.err.println("Failed to create instance: " + e.getMessage());
      throw new RuntimeException(e);
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Exception;
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Cluster;
    use Google\Cloud\Bigtable\Admin\V2\CreateInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\GetInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\Instance;
    use Google\Cloud\Bigtable\Admin\V2\Instance\Type as InstanceType;
    use Google\Cloud\Bigtable\Admin\V2\StorageType;
    
    /**
     * Create a production Bigtable instance
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance to be generated
     * @param string $clusterId The ID of the cluster to be generated
     * @param string $locationId The Bigtable region ID where you want your instance to reside
     */
    function create_production_instance(
        string $projectId,
        string $instanceId,
        string $clusterId,
        string $locationId = 'us-east1-b'
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
    
        $projectName = $instanceAdminClient->projectName($projectId);
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    
        $serveNodes = 3;
        $storageType = StorageType::SSD;
        $production = InstanceType::PRODUCTION;
        $labels = ['prod-label' => 'prod-label'];
    
        $instance = new Instance();
        $instance->setDisplayName($instanceId);
    
        $instance->setLabels($labels);
        $instance->setType($production);
    
        $cluster = new Cluster();
        $cluster->setDefaultStorageType($storageType);
        $locationName = $instanceAdminClient->locationName($projectId, $locationId);
        $cluster->setLocation($locationName);
        $cluster->setServeNodes($serveNodes);
        $clusters = [
            $clusterId => $cluster
        ];
        try {
            $getInstanceRequest = (new GetInstanceRequest())
                ->setName($instanceName);
            $instanceAdminClient->getInstance($getInstanceRequest);
            printf('Instance %s already exists.' . PHP_EOL, $instanceId);
            throw new Exception(sprintf('Instance %s already exists.' . PHP_EOL, $instanceId));
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Creating an Instance: %s' . PHP_EOL, $instanceId);
                $createInstanceRequest = (new CreateInstanceRequest())
                    ->setParent($projectName)
                    ->setInstanceId($instanceId)
                    ->setInstance($instance)
                    ->setClusters($clusters);
                $operationResponse = $instanceAdminClient->createInstance($createInstanceRequest);
                $operationResponse->pollUntilComplete();
                if (!$operationResponse->operationSucceeded()) {
                    print('Error: ' . $operationResponse->getError()->getMessage());
                } else {
                    printf('Instance %s created.', $instanceId);
                }
            } else {
                throw $e;
            }
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cluster = instance.cluster(
        cluster_id,
        location_id=location_id,
        serve_nodes=serve_nodes,
        default_storage_type=storage_type,
    )
    if not instance.exists():
        print("\nCreating an instance")
        # Create instance with given options
        operation = instance.create(clusters=[cluster])
        # Ensure the operation completes.
        operation.result(timeout=480)
        print("\nCreated instance: {}".format(instance_id))

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id      = "my-instance"
    # cluster_id       = "my-cluster"
    # cluster_location = "us-east1-b"
    puts "Creating a PRODUCTION Instance"
    job = bigtable.create_instance(
      instance_id,
      display_name: "Sample production instance",
      labels:       { "env": "production" },
      type:         :PRODUCTION # Optional as default type is :PRODUCTION
    ) do |clusters|
      clusters.add cluster_id, cluster_location, nodes: 3, storage_type: :SSD
    end
    
    job.wait_until_done!
    instance = job.instance
    puts "Created Instance: #{instance.instance_id}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
