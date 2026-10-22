---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-delete-entity/
title: Delete task \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:13.149324+00:00
---

# Delete task  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-delete-entity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Delete task Stay organized with collections  Save and categorize content based on your preferences. 

Delete a task.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting started with the Firestore in Datastore mode API](https://docs.cloud.google.com/datastore/docs/datastore-api-tutorial)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Deletes a task entity.
    /// </summary>
    /// <param name="id">The ID of the task entity as given by Key.</param>
    void DeleteTask(long id)
    {
        _db.Delete(_keyFactory.CreateKey(id));
    }
    

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/datastore"
    )
    
    // DeleteTask deletes the task with the given ID.
    func DeleteTask(projectID string, taskID int64) error {
    	ctx := context.Background()
    	client, err := datastore.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Could not create datastore client: %v", err)
    	}
    	return client.Delete(ctx, datastore.[IDKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Key_IDKey)("Task", taskID, nil))
    }
    

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Deletes a task entity.
     *
     * @param id The ID of the task entity as given by {@link Key#id()}
     * @throws DatastoreException if the delete fails
     */
    void deleteTask(long id) {
      datastore.delete(keyFactory.newKey(id));
    }
    

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    /**
     * Delete a task with a given id.
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $taskId
     */
    function delete_task(string $projectId, string $taskId)
    {
        $datastore = new DatastoreClient(['projectId' => $projectId]);
    
        $taskKey = $datastore->key('Task', $taskId);
        $datastore->delete($taskKey);
    
        printf('Task %d deleted successfully.' . PHP_EOL, $taskId);
    }

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    def delete_task(client: [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html), task_id: str | int):
        # Create a key for an entity of kind "Task", and with the supplied
        # `task_id` as its Id
        key = client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)("Task", task_id)
        # Use that key to delete its associated document, if it exists
        client.[delete](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_delete)(key)
    
    

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_task task_id
      require "google/cloud/datastore"
    
      datastore = Google::Cloud::[Datastore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore.html)
    
      task = datastore.find "Task", task_id
    
      datastore.delete task
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
