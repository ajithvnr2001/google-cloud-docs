---
url: https://docs.cloud.google.com/storage/docs/samples/storage-batch-list-jobs/
title: Storage Batch List Jobs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:22.652880+00:00
---

# Storage Batch List Jobs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-batch-list-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Batch List Jobs Stay organized with collections  Save and categorize content based on your preferences. 

List storage batch operations jobs

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage batch operation jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      for (auto const& job : client.ListJobs(parent)) {
        if (!job) throw job.status();
        std::cout << job->name() << "\n";
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\ListJobsRequest;
    
    /**
     * List Jobs in a given project.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     */
    function list_jobs(string $projectId): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
    
        $request = new ListJobsRequest([
            'parent' => $parent,
        ]);
    
        $jobs = $storageBatchOperationsClient->listJobs($request);
    
        foreach ($jobs as $job) {
            printf('Job name: %s' . PHP_EOL, $job->getName());
        }
    }

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage_batch_operations"
    
    # Lists Storage Batch Operations jobs for a given project.
    #
    # @param project_id [String] The ID of your Google Cloud project.
    #
    # @example
    #   list_jobs project_id: "your-project-id"
    #
    
    def list_jobs project_id:
      client = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html).[storage_batch_operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations/latest/Google-Cloud-StorageBatchOperations.html)
      parent = "projects/#{project_id}/locations/global"
      request = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::ListJobsRequest.new parent: parent, page_size: 10
      job_list = client.list_jobs request
      job_list.each { |job| puts "Job name: #{job.name} present in the list" }
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
