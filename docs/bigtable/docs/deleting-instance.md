---
url: https://docs.cloud.google.com/bigtable/docs/deleting-instance/
title: Delete an instance \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:49.412627+00:00
---

# Delete an instance  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/deleting-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete an instance

Deleting a Bigtable instance lets you remove unused resources and avoid ongoing infrastructure costs when you no longer need the resources. You can remove an instance programmatically by using the [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries) or manually by using the Google Cloud console, the Google Cloud CLI, or the `cbt` CLI .

**Warning:** When you delete a Bigtable instance, you permanently delete the instance's clusters and all of the data in those clusters. Deleting an instance can't be undone.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to delete, then click **Delete instance**. A confirmation dialog appears.

  3. Follow the instructions in the confirmation dialog, then click **Delete**. The instance is permanently deleted.




###  gcloud 

  1. [Install the Google Cloud CLI](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk) if you haven't already.
  2. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  3. Use the [`bigtable instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/delete) to delete an instance:
         
         gcloud bigtable instances delete INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for your instance.




###  cbt 

  1. [Install the `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk) if you haven't already.
  2. If you don't know the instance ID, use the `listinstances` command to view a list of your project's instances: 
         
         cbt listinstances
         

  3. Use the `deleteinstance` command to delete an instance:
         
         cbt deleteinstance INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for your instance.




### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Deletes an instance from the project.
    // Initialize request argument(s).
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = new InstanceName(projectId, instanceId)
    };
    try
    {
        // Make request.
        Console.WriteLine("Waiting for operation to complete...");
        bigtableInstanceAdminClient.DeleteInstance(request);
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Exception while deleting {instanceId} instance");
        Console.WriteLine(ex.Message);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    try {
      String name = "projects/" + projectId + "/instances/" + instanceId;
      DeleteInstanceRequest request = DeleteInstanceRequest.newBuilder().setName(name).build();
      adminClient.deleteInstance(request);
      System.out.println("Instance deleted: " + instanceId);
    } catch (NotFoundException e) {
      System.err.println("Failed to delete non-existent instance: " + e.getMessage());
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    console.log('Deleting Instance');
    const {BigtableInstanceAdminClient} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)').v2;
    const instanceAdminClient = new [BigtableInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)();
    const projectId = await instanceAdminClient.getProjectId();
    await instanceAdminClient.deleteInstance({
      name: `projects/${projectId}/instances/${instanceID}`,
    });
    console.log(`Instance deleted: ${instanceID}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteInstanceRequest;
    
    /**
     * Delete a bigtable instance
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance to be deleted
     */
    function delete_instance(
        string $projectId,
        string $instanceId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    
        printf('Deleting Instance' . PHP_EOL);
        try {
            $deleteInstanceRequest = (new DeleteInstanceRequest())
                ->setName($instanceName);
            $instanceAdminClient->deleteInstance($deleteInstanceRequest);
            printf('Deleted Instance: %s.' . PHP_EOL, $instanceId);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Instance %s does not exists.' . PHP_EOL, $instanceId);
            } else {
                throw $e;
            }
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("\nDeleting instance")
    if not instance.exists():
        print("Instance {} does not exist.".format(instance_id))
    else:
        instance.delete()
        print("Deleted instance: {}".format(instance_id))

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    instance.delete

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
