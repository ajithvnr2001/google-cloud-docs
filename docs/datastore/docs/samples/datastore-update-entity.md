---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-update-entity/
title: Example datastore mark task done \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:31.876133+00:00
---

# Example datastore mark task done  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-update-entity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Example datastore mark task done Stay organized with collections  Save and categorize content based on your preferences. 

Example datastore mark task done

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting started with the Firestore in Datastore mode API](https://docs.cloud.google.com/datastore/docs/datastore-api-tutorial)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Marks a task entity as done.
    /// </summary>
    /// <param name="id">The ID of the task entity as given by Key.</param>
    /// <returns>true if the task was found.</returns>
    bool MarkDone(long id)
    {
        using (var transaction = _db.BeginTransaction())
        {
            Entity task = transaction.Lookup(_keyFactory.CreateKey(id));
            if (task != null)
            {
                task["done"] = true;
                transaction.Update(task);
            }
            transaction.Commit();
            return task != null;
        }
    }
    

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/datastore"
    )
    
    // MarkDone marks the task done with the given ID.
    func MarkDone(projectID string, taskID int64) error {
    	ctx := context.Background()
    	client, err := datastore.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Could not create datastore client: %v", err)
    	}
    	defer client.Close()
    	// Create a key using the given integer ID.
    	key := datastore.[IDKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Key_IDKey)("Task", taskID, nil)
    
    	// In a transaction load each task, set done to true and store.
    	_, err = client.[RunInTransaction](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Client_RunInTransaction)(ctx, func(tx *datastore.Transaction) error {
    		var task Task
    		if err := tx.Get(key, &task); err != nil {
    			return err
    		}
    		task.Done = true
    		_, err := tx.Put(key, &task)
    		return err
    	})
    	return err
    }
    

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Marks a task entity as done.
     *
     * @param id The ID of the task entity as given by {@link Key#id()}
     * @return true if the task was found, false if not
     * @throws DatastoreException if the transaction fails
     */
    boolean markDone(long id) {
      Transaction transaction = datastore.newTransaction();
      try {
        Entity task = transaction.get(keyFactory.newKey(id));
        if (task != null) {
          transaction.put(Entity.newBuilder(task).set("done", true).build());
        }
        transaction.commit();
        return task != null;
      } finally {
        if (transaction.isActive()) {
          transaction.rollback();
        }
      }
    }
    

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    /**
     * Mark a task with a given id as done.
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $taskId
     */
    function mark_done(string $projectId, string $taskId)
    {
        $datastore = new DatastoreClient(['projectId' => $projectId]);
    
        $taskKey = $datastore->key('Task', $taskId);
        $transaction = $datastore->transaction();
        $task = $transaction->lookup($taskKey);
        $task['done'] = true;
        $transaction->upsert($task);
        $transaction->commit();
        printf('Task %d updated successfully.' . PHP_EOL, $taskId);
    }

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    def mark_done(client: [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html), task_id: str | int):
        with client.[transaction](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_transaction)():
            # Create a key for an entity of kind "Task", and with the supplied
            # `task_id` as its Id
            key = client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)("Task", task_id)
            # Use that key to load the entity
            task = client.[get](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_get)(key)
    
            if not task:
                raise ValueError(f"Task {task_id} does not exist.")
    
            # Update a field indicating that the associated
            # work has been completed
            task["done"] = True
    
            # Persist the change back to Datastore
            client.[put](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_put)(task)
    
    

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def mark_done task_id
      require "google/cloud/datastore"
    
      datastore = Google::Cloud::[Datastore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-admin/latest/Google-Cloud-Datastore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore.html)
    
      task = datastore.find "Task", task_id
    
      task["done"] = true
    
      datastore.save task
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
