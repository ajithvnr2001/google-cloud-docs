---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-app-profile/
title: AppProfile details \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:49.238185+00:00
---

# AppProfile details  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-app-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  AppProfile details Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve AppProfile details.

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
      std::string profile_name =
          cbt::AppProfileName(project_id, instance_id, profile_id);
      StatusOr<google::bigtable::admin::v2::AppProfile> profile =
          instance_admin.GetAppProfile(profile_name);
      if (!profile) throw std::move(profile).status();
      std::cout << "Application Profile details=" << profile->DebugString()
                << "\n";
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetAppProfileRequest;
    
    /**
     * Get the App Profile
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $appProfileId The ID of the App Profile to fetch
     */
    function get_app_profile(
        string $projectId,
        string $instanceId,
        string $appProfileId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $appProfileName = $instanceAdminClient->appProfileName($projectId, $instanceId, $appProfileId);
    
        printf('Fetching the App Profile %s' . PHP_EOL, $appProfileId);
        try {
            $getAppProfileRequest = (new GetAppProfileRequest())
                ->setName($appProfileName);
            $appProfile = $instanceAdminClient->getAppProfile($getAppProfileRequest);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('App profile %s does not exist.' . PHP_EOL, $appProfileId);
                return;
            }
            throw $e;
        }
    
        printf('Printing Details:' . PHP_EOL);
    
        // Fetch some commonly used metadata
        printf('Name: %s' . PHP_EOL, $appProfile->getName());
        printf('Etag: %s' . PHP_EOL, $appProfile->getEtag());
        printf('Description: %s' . PHP_EOL, $appProfile->getDescription());
        printf('Routing Policy: %s' . PHP_EOL, $appProfile->getRoutingPolicy());
    
        if ($appProfile->hasSingleClusterRouting()) {
            $clusterId = $appProfile->getSingleClusterRouting()->getClusterId();
            $singleRowTransactions = $appProfile->getSingleClusterRouting()->getAllowTransactionalWrites() ? 'Yes' : 'No';
            printf('Cluster: %s' . PHP_EOL, $clusterId);
            printf('Single-Row Transactions: %s' . PHP_EOL, $singleRowTransactions);
        }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
