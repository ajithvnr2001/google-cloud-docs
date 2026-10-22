---
url: https://docs.cloud.google.com/bigtable/docs/get-instance-information/
title: Get instance information \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:54.011959+00:00
---

# Get instance information  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/get-instance-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get instance information

This page explains how to list all instances in a project and get instance details programmatically using [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries) or manually using the Google Cloud console, Google Cloud CLI, or cbt CLI :

## List instances

To get a list of instances, do the following:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

The **Instances** page displays a list of instances.




###  gcloud 

Use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of instances:
    
    
      gcloud bigtable instances list
    

###  cbt 

Use the `listinstances` command to view a list of instances:
    
    
      cbt listinstances
    

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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {BigtableInstanceAdminClient} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)').v2;
    const instanceAdminClient = new [BigtableInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)();
    const projectId = await instanceAdminClient.getProjectId();
    const [instances] = await instanceAdminClient.listInstances({
      parent: `projects/${projectId}`,
    });
    instances.instances.forEach(instance => {
      console.log(instance.name);
    });

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

## Get instance details

To get details about an instance, do the following:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose details you want to view.

The **[Instance overview](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-overview)** page displays detailed information about the instance, such as the ID, name, storage type, CPU utilization, and edition.




###  gcloud 

Use the [`bigtable instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/describe) to view details of an instance:
    
    
        gcloud bigtable instances describe INSTANCE_ID
    

Replace the following:

  * `INSTANCE_ID`: The permanent identifier for the instance. 



###  cbt 

Use the `listclusters` command to view a view details of an instance:
    
    
        cbt listclusters INSTANCE_ID
    

Replace the following:

  * `INSTANCE_ID`: The permanent identifier for the instance. 



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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {BigtableInstanceAdminClient} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)').v2;
    const instanceAdminClient = new [BigtableInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)();
    const projectId = await instanceAdminClient.getProjectId();
    const [instance2] = await instanceAdminClient.getInstance({
      name: `projects/${projectId}/instances/${instanceID}`,
    });
    console.log(`Instance ID: ${instance2.name}`);
    console.log(`Instance Meta: ${JSON.stringify(instance2.labels)}`);

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

  * Find out how to [modify an instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance).
  * Learn how to [delete an instance](https://docs.cloud.google.com/bigtable/docs/deleting-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
