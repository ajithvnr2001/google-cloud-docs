---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-app-profile/
title: Create an AppProfile \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:23.980655+00:00
---

# Create an AppProfile  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-app-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Create an AppProfile Stay organized with collections  Save and categorize content based on your preferences. 

Create an AppProfile.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableInstanceAdminClient instance_admin,
       std::string const& project_id, std::string const& instance_id,
       std::string const& profile_id) {
      std::string instance_name = cbt::InstanceName(project_id, instance_id);
    
      google::bigtable::admin::v2::AppProfile ap;
      ap.mutable_multi_cluster_routing_use_any()->Clear();
    
      StatusOr<google::bigtable::admin::v2::AppProfile> profile =
          instance_admin.CreateAppProfile(instance_name, profile_id,
                                          std::move(ap));
      if (!profile) throw std::move(profile).status();
      std::cout << "New profile created with name=" << profile->name() << "\n";
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\AppProfile;
    use Google\Cloud\Bigtable\Admin\V2\AppProfile\SingleClusterRouting;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateAppProfileRequest;
    
    /**
     * Create an App Profile
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $clusterId The ID of the cluster where the new App Profile will route it's requests(in case of single cluster routing)
     * @param string $appProfileId The ID of the App Profile to create
     */
    function create_app_profile(
        string $projectId,
        string $instanceId,
        string $clusterId,
        string $appProfileId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    
        $appProfile = new AppProfile([
            'name' => $appProfileId,
            'description' => 'Description for this newly created AppProfile'
        ]);
    
        // create a new routing policy
        // allow_transactional_writes refers to Single-Row-Transactions(https://cloud.google.com/bigtable/docs/app-profiles#single-row-transactions)
        $routingPolicy = new SingleClusterRouting([
            'cluster_id' => $clusterId,
            'allow_transactional_writes' => false
        ]);
    
        // set the newly created routing policy to our app profile
        $appProfile->setSingleClusterRouting($routingPolicy);
    
        // we could also create a multi cluster routing policy like so:
        // $routingPolicy = new \Google\Cloud\Bigtable\Admin\V2\AppProfile\MultiClusterRoutingUseAny();
        // $appProfile->setMultiClusterRoutingUseAny($routingPolicy);
    
        printf('Creating a new AppProfile %s' . PHP_EOL, $appProfileId);
    
        try {
            $createAppProfileRequest = (new CreateAppProfileRequest())
                ->setParent($instanceName)
                ->setAppProfileId($appProfileId)
                ->setAppProfile($appProfile);
            $newAppProfile = $instanceAdminClient->createAppProfile($createAppProfileRequest);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'ALREADY_EXISTS') {
                printf('AppProfile %s already exists.', $appProfileId);
                return;
            }
            throw $e;
        }
    
        printf('AppProfile created: %s', $newAppProfile->getName());
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
