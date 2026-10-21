---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-update-app-profile/
title: Update an AppProfile \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:04.388963+00:00
---

# Update an AppProfile  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-update-app-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Update an AppProfile Stay organized with collections  Save and categorize content based on your preferences. 

Update an AppProfile.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::future;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableInstanceAdminClient instance_admin,
       std::string const& project_id, std::string const& instance_id,
       std::string const& profile_id, std::string const& description) {
      std::string profile_name =
          cbt::AppProfileName(project_id, instance_id, profile_id);
    
      google::bigtable::admin::v2::AppProfile profile;
      profile.set_name(profile_name);
      profile.set_description(description);
    
      google::protobuf::FieldMask mask;
      mask.add_paths("description");
    
      future<StatusOr<google::bigtable::admin::v2::AppProfile>> profile_future =
          instance_admin.UpdateAppProfile(std::move(profile), std::move(mask));
      auto modified_profile = profile_future.get();
      if (!modified_profile) throw std::move(modified_profile).status();
      std::cout << "Updated AppProfile: " << modified_profile->DebugString()
                << "\n";
    }
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::future;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableInstanceAdminClient instance_admin,
       std::string const& project_id, std::string const& instance_id,
       std::string const& profile_id) {
      std::string profile_name =
          cbt::AppProfileName(project_id, instance_id, profile_id);
    
      google::bigtable::admin::v2::UpdateAppProfileRequest req;
      req.mutable_app_profile()->set_name(profile_name);
      req.mutable_app_profile()->mutable_multi_cluster_routing_use_any()->Clear();
      req.mutable_update_mask()->add_paths("multi_cluster_routing_use_any");
      req.set_ignore_warnings(true);
    
      future<StatusOr<google::bigtable::admin::v2::AppProfile>> profile_future =
          instance_admin.UpdateAppProfile(std::move(req));
      auto modified_profile = profile_future.get();
      if (!modified_profile) throw std::move(modified_profile).status();
      std::cout << "Updated AppProfile: " << modified_profile->DebugString()
                << "\n";
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\AppProfile;
    use Google\Cloud\Bigtable\Admin\V2\AppProfile\SingleClusterRouting;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\UpdateAppProfileRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Update an App Profile
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $clusterId The ID of the new cluster where the new App Profile will route it's requests(in case of single cluster routing)
     * @param string $appProfileId The ID of the App Profile to update
     */
    function update_app_profile(
        string $projectId,
        string $instanceId,
        string $clusterId,
        string $appProfileId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $appProfileName = $instanceAdminClient->appProfileName($projectId, $instanceId, $appProfileId);
    
        $appProfile = new AppProfile([
            'name' => $appProfileName,
            'description' => 'The updated description',
        ]);
    
        // create a new routing policy
        // allow_transactional_writes refers to Single-Row-Transactions(https://cloud.google.com/bigtable/docs/app-profiles#single-row-transactions)
        $routingPolicy = new SingleClusterRouting([
            'cluster_id' => $clusterId,
            'allow_transactional_writes' => true
        ]);
    
        // set the newly created routing policy to our app profile
        $appProfile->setSingleClusterRouting($routingPolicy);
    
        // or we could also create a multi cluster routing policy like so:
        // $routingPolicy = new \Google\Cloud\Bigtable\Admin\V2\AppProfile\MultiClusterRoutingUseAny();
        // $appProfile->setMultiClusterRoutingUseAny($routingPolicy);
    
        // returns a string identifier depending on SingleClusterRouting or MultiClusterRoutingUseAny
        $routingPolicyStr = $appProfile->getRoutingPolicy();
    
        $updateMask = new FieldMask([
            'paths' => ['description', $routingPolicyStr]
        ]);
    
        printf('Updating the AppProfile %s' . PHP_EOL, $appProfileId);
    
        try {
            // Bigtable warns you while updating the routing policy, or when toggling the allow_transactional_writes
            // to force it to update, we set ignoreWarnings to true.
            // If you just want to update something simple like description, you can remove it.
            $updateAppProfileRequest = (new UpdateAppProfileRequest())
                ->setAppProfile($appProfile)
                ->setUpdateMask($updateMask)
                ->setIgnoreWarnings(true);
            $operationResponse = $instanceAdminClient->updateAppProfile($updateAppProfileRequest);
    
            $operationResponse->pollUntilComplete();
            if ($operationResponse->operationSucceeded()) {
                $updatedAppProfile = $operationResponse->getResult();
                printf('App profile updated: %s' . PHP_EOL, $updatedAppProfile->getName());
                // doSomethingWith($updatedAppProfile)
            } else {
                $error = $operationResponse->getError();
                // handleError($error)
            }
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('App Profile %s does not exist.' . PHP_EOL, $appProfileId);
                return;
            }
            throw $e;
        }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
