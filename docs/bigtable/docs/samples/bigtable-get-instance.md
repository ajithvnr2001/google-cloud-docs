---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-instance/
title: Get instance details \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:54.314689+00:00
---

# Get instance details  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Get instance details Stay organized with collections  Save and categorize content based on your preferences. 

Get instance details given the instance ID in the current project. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get instance information](https://docs.cloud.google.com/bigtable/docs/get-instance-information)



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
      StatusOr<google::bigtable::admin::v2::Instance> instance =
          instance_admin.GetInstance(instance_name);
      if (!instance) throw std::move(instance).status();
      std::cout << "GetInstance details : " << instance->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Initialize request argument(s).
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = new InstanceName(projectId, instanceId)
    };
    try
    {
        // Make Request.
        Console.WriteLine("Waiting for operation to complete...");
        Instance respond = bigtableInstanceAdminClient.GetInstance(request);
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Exception retreiving {instanceId} instance");
        Console.WriteLine(ex.Message);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Instance instance = null;
    try {
      String name = "projects/" + projectId + "/instances/" + instanceId;
      GetInstanceRequest request = GetInstanceRequest.newBuilder().setName(name).build();
      instance = adminClient.getInstance(request);
      System.out.println("Instance ID: " + instance.getName());
      System.out.println("Display Name: " + instance.getDisplayName());
      System.out.print("Labels: ");
      Map<String, String> labels = instance.getLabelsMap();
      for (String key : labels.keySet()) {
        System.out.printf("%s - %s", key, labels.get(key));
      }
      System.out.println("\nState: " + instance.getState());
      System.out.println("Type: " + instance.getType());
    } catch (NotFoundException e) {
      System.err.println("Failed to get non-existent instance: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\Instance\State;
    use Google\Cloud\Bigtable\Admin\V2\Instance\Type;
    
    /**
     * Get a Bigtable instance
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     */
    function get_instance(
        string $projectId,
        string $instanceId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    
        printf('Fetching the Instance %s' . PHP_EOL, $instanceId);
        try {
            $getInstanceRequest = (new GetInstanceRequest())
                ->setName($instanceName);
            $instance = $instanceAdminClient->getInstance($getInstanceRequest);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Instance %s does not exists.' . PHP_EOL, $instanceId);
                return;
            }
            throw $e;
        }
    
        printf('Printing Details:' . PHP_EOL);
    
        // Fetch some commonly used metadata
        printf('Name: ' . $instance->getName() . PHP_EOL);
        printf('Display Name: ' . $instance->getDisplayName() . PHP_EOL);
        printf('State: ' . State::name($instance->getState()) . PHP_EOL);
        printf('Type: ' . Type::name($instance->getType()) . PHP_EOL);
        printf('Labels: ' . PHP_EOL);
    
        $labels = $instance->getLabels();
    
        // Labels are an object of the MapField class which implement the IteratorAggregate, Countable
        // and ArrayAccess interfaces so you can do the following:
        printf("\tNum of Labels: " . $labels->count() . PHP_EOL);
        printf("\tLabel with a key(dev-label): " . ($labels['dev-label'] ?? 'N/A') . PHP_EOL);
    
        // we can even loop over all the labels
        foreach ($labels as $key => $val) {
            printf("\t$key: $val" . PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print(
        "\nName of instance: {}\nLabels: {}".format(
            instance.display_name, instance.labels
        )
    )

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    instance = bigtable.instance instance_id
    puts "Get Instance id: #{instance.instance_id}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
