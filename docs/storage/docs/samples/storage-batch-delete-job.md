---
url: https://docs.cloud.google.com/storage/docs/samples/storage-batch-delete-job/
title: Storage Batch Delete Job \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:57.256510+00:00
---

# Storage Batch Delete Job  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-batch-delete-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Batch Delete Job Stay organized with collections  Save and categorize content based on your preferences. 

Delete a storage batch operations job

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage batch operation jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id, std::string const& job_id) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      auto const name = parent + "/jobs/" + job_id;
      auto status = client.DeleteJob(name);
      if (!status.ok()) throw status;
      std::cout << "Deleted job: " << name << "\n";
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\DeleteJobRequest;
    
    /**
     * Delete a batch job.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     * @param string $jobId A unique identifier for this job.
     *        (e.g. '94d60cc1-2d95-41c5-b6e3-ff66cd3532d5')
     */
    function delete_job(string $projectId, string $jobId): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
        $formattedName = $parent . '/jobs/' . $jobId;
    
        $request = new DeleteJobRequest([
            'name' => $formattedName,
        ]);
    
        $storageBatchOperationsClient->deleteJob($request);
    
        printf('Deleted job: %s', $formattedName);
    }

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage_batch_operations"
    
    # Deletes a Storage Batch Operations job.
    #
    # @param project_id [String] The ID of your Google Cloud project.
    # @param job_id [String] The ID of the Storage Batch Operations job to be deleted.
    #
    # @example
    #   delete_job project_id: "your-project-id", job_id: "your-job-id"
    #
    def delete_job project_id:, job_id:
      client = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html).[storage_batch_operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations/latest/Google-Cloud-StorageBatchOperations.html)
      parent = "projects/#{project_id}/locations/global"
      request = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::DeleteJobRequest.new name: "#{parent}/jobs/#{job_id}"
    
      begin
        result = client.delete_job request
        message = "The #{job_id} is deleted."
      rescue StandardError
        # This error is thrown when the job is not deleted.
        message = "Failed to delete job #{job_id}. Error: #{result.error.message}"
      end
      puts message
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
