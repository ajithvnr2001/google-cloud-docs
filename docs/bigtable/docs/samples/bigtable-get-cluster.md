---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-cluster/
title: Get cluster details \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:51.934304+00:00
---

# Get cluster details  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Get cluster details Stay organized with collections  Save and categorize content based on your preferences. 

Get cluster details given the instance ID in the current project.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetClusterRequest;
    use Google\Cloud\Bigtable\Admin\V2\Instance\State;
    use Google\Cloud\Bigtable\Admin\V2\StorageType;
    
    /**
     * Get a Bigtable cluster
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $clusterId The ID of the cluster to fetch
     */
    function get_cluster(
        string $projectId,
        string $instanceId,
        string $clusterId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
    
        printf('Fetching the Cluster %s' . PHP_EOL, $clusterId);
        try {
            $clusterName = $instanceAdminClient->clusterName($projectId, $instanceId, $clusterId);
            $getClusterRequest = (new GetClusterRequest())
                ->setName($clusterName);
            $cluster = $instanceAdminClient->getCluster($getClusterRequest);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Cluster %s does not exists.' . PHP_EOL, $clusterId);
                return;
            }
            throw $e;
        }
    
        printf('Printing Details:' . PHP_EOL);
    
        // Fetch some commonly used metadata
        printf('Name: ' . $cluster->getName() . PHP_EOL);
        printf('Location: ' . $cluster->getLocation() . PHP_EOL);
        printf('State: ' . State::name($cluster->getState()) . PHP_EOL);
        printf('Default Storage Type: ' . StorageType::name($cluster->getDefaultStorageType()) . PHP_EOL);
        printf('Nodes: ' . $cluster->getServeNodes() . PHP_EOL);
        printf('Encryption Config: ' . ($cluster->hasEncryptionConfig() ? $cluster->getEncryptionConfig()->getKmsKeyName() : 'N/A') . PHP_EOL);
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
