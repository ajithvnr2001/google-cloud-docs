---
url: https://docs.cloud.google.com/storage/docs/samples/storage-batch-create-job/
title: Storage Batch Create Job \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:53.784154+00:00
---

# Storage Batch Create Job  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-batch-create-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Batch Create Job Stay organized with collections  Save and categorize content based on your preferences. 

Create a storage batch operations job

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage batch operation jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id, std::string const& job_id,
       std::string const& target_bucket_name, std::string const& object_prefix) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      namespace sbo = google::cloud::storagebatchoperations::v1;
      sbo::Job job;
      sbo::BucketList* bucket_list = job.mutable_bucket_list();
      sbo::BucketList::Bucket* bucket_config = bucket_list->add_buckets();
      bucket_config->set_bucket(target_bucket_name);
      sbo::PrefixList* prefix_list_config = bucket_config->mutable_prefix_list();
      prefix_list_config->add_included_object_prefixes(object_prefix);
      sbo::DeleteObject* delete_object_config = job.mutable_delete_object();
      delete_object_config->set_permanent_object_deletion_enabled(false);
      auto result = client.CreateJob(parent, job, job_id).get();
      if (!result) throw result.status();
      std::cout << "Created job: " << result->name() << "\n";
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\CreateJobRequest;
    use Google\Cloud\StorageBatchOperations\V1\Job;
    use Google\Cloud\StorageBatchOperations\V1\BucketList;
    use Google\Cloud\StorageBatchOperations\V1\BucketList\Bucket;
    use Google\Cloud\StorageBatchOperations\V1\PrefixList;
    use Google\Cloud\StorageBatchOperations\V1\DeleteObject;
    
    /**
     * Create a new batch job.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     * @param string $jobId A unique identifier for this job.
     *        (e.g. '94d60cc1-2d95-41c5-b6e3-ff66cd3532d5')
     * @param string $bucketName The name of your Cloud Storage bucket to operate on.
     *        (e.g. 'my-bucket')
     * @param string $objectPrefix The prefix of objects to include in the operation.
     *        (e.g. 'prefix1')
     */
    function create_job(string $projectId, string $jobId, string $bucketName, string $objectPrefix): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
    
        $prefixListConfig = new PrefixList(['included_object_prefixes' => [$objectPrefix]]);
        $bucket = new Bucket(['bucket' => $bucketName, 'prefix_list' => $prefixListConfig]);
        $bucketList = new BucketList(['buckets' => [$bucket]]);
    
        $deleteObject = new DeleteObject(['permanent_object_deletion_enabled' => false]);
    
        $job = new Job(['bucket_list' => $bucketList, 'delete_object' => $deleteObject]);
    
        $request = new CreateJobRequest([
            'parent' => $parent,
            'job_id' => $jobId,
            'job' => $job,
        ]);
        $response = $storageBatchOperationsClient->createJob($request);
    
        printf('Created job: %s', $response->getName());
    }

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage_batch_operations"
    
    # Creates a Storage Batch Operations job to delete objects in a bucket
    # that match a given prefix. The deletion is a "soft delete", meaning
    # objects can be recovered if versioning is enabled on the bucket.
    #
    # @param bucket_name [String] The name of the Google Cloud Storage bucket.
    # @param prefix [String] The prefix of the objects to be included in the job.
    #   The job will operate on all objects whose names start with this prefix.
    # @param job_id [String] A unique identifier for the job.
    # @param project_id [String] The ID of the Google Cloud project where the job will be created.
    #
    # @example
    #   create_job(
    #     bucket_name: "your-unique-bucket-name",
    #     prefix: "test-files/",
    #     job_id: "your-job-id",
    #     project_id: "your-project-id"
    #   )
    #
    def create_job bucket_name:, prefix:, job_id:, project_id:
      client = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html).[storage_batch_operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations/latest/Google-Cloud-StorageBatchOperations.html)
    
      parent = "projects/#{project_id}/locations/global"
    
      prefix_list = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::PrefixList.new(
        included_object_prefixes: [prefix]
      )
    
      bucket = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::BucketList::Bucket.new(
        bucket: bucket_name,
        prefix_list: prefix_list
      )
    
      bucket_list = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::BucketList.new(
        buckets: [bucket]
      )
    
      # Define the delete operation
      delete_object = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::DeleteObject.new(
        permanent_object_deletion_enabled: false
      )
    
      # Build the job
      job = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::Job.new(
        bucket_list: bucket_list,
        delete_object: delete_object
      )
    
      request = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::CreateJobRequest.new parent: parent, job_id: job_id, job: job
      create_job_operation = client.create_job request
    
      # To fetch job details using get_job to confirm creation
      get_request = Google::Cloud::[StorageBatchOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1.html)::GetJobRequest.new name: "#{parent}/jobs/#{job_id}"
    
      begin
        ## Waiting for operation to complete
        create_job_operation.wait_until_done!
        ## Fetch the newly created job to confirm creation
        job_detail = client.get_job get_request
        message = "Storage Batch Operations job #{job_detail.name} is created."
      rescue StandardError
        # This error is thrown when the job is not created.
        message = "Failed to create job #{job_id}. Error: #{create_job_operation.error.message}"
      end
      puts message
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
