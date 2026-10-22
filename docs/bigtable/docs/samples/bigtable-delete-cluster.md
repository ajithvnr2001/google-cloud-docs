---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-delete-cluster/
title: Delete a cluster \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:39.452134+00:00
---

# Delete a cluster  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-delete-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Delete a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Delete a cluster, given a project ID and instance ID.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Deltes cluster "ssd-cluster2" from instance.
    // At least one cluster must remain on an instance.
    // Initialize request argument(s)
    DeleteClusterRequest request = new DeleteClusterRequest
    {
        ClusterName = new ClusterName(projectId, instanceId, "ssd-cluster2")
    };
    try
    {
        // Make the request
        Console.WriteLine("Waiting for operation to complete...");
        bigtableInstanceAdminClient.DeleteCluster(request);
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Exception deleting cluster {request.ClusterName.ClusterId} from instance {instanceId}");
        Console.WriteLine(ex.Message);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    try {
      String name = "projects/" + projectId + "/instances/" + instanceId + "/clusters/" + CLUSTER;
      DeleteClusterRequest request = DeleteClusterRequest.newBuilder().setName(name).build();
      adminClient.deleteCluster(request);
      System.out.printf("Cluster: %s deleted successfully%n", CLUSTER);
    } catch (NotFoundException e) {
      System.err.println("Failed to delete a non-existent cluster: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteClusterRequest;
    
    /**
     * Delete a cluster
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $clusterId The ID of the cluster to be deleted
     */
    function delete_cluster(
        string $projectId,
        string $instanceId,
        string $clusterId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $clusterName = $instanceAdminClient->clusterName($projectId, $instanceId, $clusterId);
    
        printf('Deleting Cluster' . PHP_EOL);
        try {
            $deleteClusterRequest = (new DeleteClusterRequest())
                ->setName($clusterName);
            $instanceAdminClient->deleteCluster($deleteClusterRequest);
            printf('Cluster %s deleted.' . PHP_EOL, $clusterId);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Cluster %s does not exist.' . PHP_EOL, $clusterId);
            } else {
                throw $e;
            }
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("\nDeleting cluster")
    if cluster.exists():
        cluster.delete()
        print("Cluster deleted: {}".format(cluster_id))
    else:
        print("\nCluster {} does not exist.".format(cluster_id))
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cluster.delete

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
