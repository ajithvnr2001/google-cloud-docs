---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-list-instances/
title: List instances \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:24.349862+00:00
---

# List instances  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-list-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  List instances Stay organized with collections  Save and categorize content based on your preferences. 

List the instances in the current project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get instance information](https://docs.cloud.google.com/bigtable/docs/get-instance-information)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Lists instances in the project.
    // Initialize request argument(s).
    ListInstancesRequest listInstancesRequest = new ListInstancesRequest
    {
        ParentAsProjectName = new ProjectName(projectId)
    };
    try
    {
        // Make a request.
        Console.WriteLine("Waiting for operation to complete...");
        ListInstancesResponse instances = bigtableInstanceAdminClient.ListInstances(listInstancesRequest);
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Exception while requesting information about instances in {projectId} project");
        Console.WriteLine(ex.Message);
        return -1;
    }
    Console.WriteLine(new string('-', 50));

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    try {
      String parent = "projects/" + projectId;
      ListInstancesRequest request = ListInstancesRequest.newBuilder().setParent(parent).build();
      ListInstancesResponse response = adminClient.listInstances(request);
      for (Instance instance : response.getInstancesList()) {
        System.out.println(instance.getName());
      }
    } catch (Exception e) {
      System.err.println("Failed to list instances: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListInstancesRequest;
    
    /**
     * List Bigtable instances in a project
     *
     * @param string $projectId The Google Cloud project ID
     */
    function list_instance(string $projectId): void
    {
        $instanceAdminClient = new BigtableInstanceAdminClient();
    
        $projectName = $instanceAdminClient->projectName($projectId);
    
        printf('Listing Instances:' . PHP_EOL);
        $listInstancesRequest = (new ListInstancesRequest())
            ->setParent($projectName);
    
        $getInstances = $instanceAdminClient->listInstances($listInstancesRequest)->getInstances();
        $instances = $getInstances->getIterator();
    
        foreach ($instances as $instance) {
            print($instance->getName() . PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("\nListing instances:")
    for instance_local in client.list_instances()[0]:
        print(instance_local.instance_id)

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    bigtable.instances.all do |instance|
      puts "Instance: #{instance.instance_id}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
