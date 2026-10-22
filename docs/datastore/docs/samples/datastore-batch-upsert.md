---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-batch-upsert/
title: Batch upsert \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:13.954225+00:00
---

# Batch upsert  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-batch-upsert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Batch upsert Stay organized with collections  Save and categorize content based on your preferences. 

Perform a batch upsert.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Entities, Properties, and Keys](https://docs.cloud.google.com/datastore/docs/concepts/entities)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    var taskList = new[]
    {
        new Entity()
        {
            Key = _keyFactory.CreateIncompleteKey(),
            ["category"] = "Personal",
            ["done"] = false,
            ["priority"] = 4,
            ["description"] = "Learn Cloud Datastore"
        },
        new Entity()
        {
            Key = _keyFactory.CreateIncompleteKey(),
            ["category"] = "Personal",
            ["done"] = "false",
            ["priority"] = 5,
            ["description"] = "Integrate Cloud Datastore"
        }
    };
    var keyList = _db.Upsert(taskList[0], taskList[1]);

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    tasks := []*Task{
    	{
    		Category:    "Personal",
    		Done:        false,
    		Priority:    4,
    		Description: "Learn Cloud Datastore",
    	},
    	{
    		Category:    "Personal",
    		Done:        false,
    		Priority:    5,
    		Description: "Integrate Cloud Datastore",
    	},
    }
    keys := []*datastore.Key{
    	datastore.IncompleteKey("Task", nil),
    	datastore.IncompleteKey("Task", nil),
    }
    
    keys, err := client.PutMulti(ctx, keys, tasks)

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    FullEntity<IncompleteKey> task1 =
        FullEntity.newBuilder(keyFactory.newKey())
            .set("category", "Personal")
            .set("done", false)
            .set("priority", 4)
            .set("description", "Learn Cloud Datastore")
            .build();
    FullEntity<IncompleteKey> task2 =
        Entity.newBuilder(keyFactory.newKey())
            .set("category", "Personal")
            .set("done", false)
            .set("priority", 5)
            .set("description", "Integrate Cloud Datastore")
            .build();
    List<Entity> tasks = datastore.add(task1, task2);
    Key taskKey1 = tasks.get(0).getKey();
    Key taskKey2 = tasks.get(1).getKey();

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $result = $datastore->upsertBatch($tasks);

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    # For help authenticating your client, visit
    # https://cloud.google.com/docs/authentication/getting-started
    client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)()
    
    task1 = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Entity](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.entity.Entity.html)(client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)("Task", 1))
    
    task1.update(
        {
            "category": "Personal",
            "done": False,
            "priority": 4,
            "description": "Learn Cloud Datastore",
        }
    )
    
    task2 = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Entity](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.entity.Entity.html)(client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)("Task", 2))
    
    task2.update(
        {
            "category": "Work",
            "done": False,
            "priority": 8,
            "description": "Integrate Cloud Datastore",
        }
    )
    
    client.[put_multi](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_put_multi)([task1, task2])

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    task_1 = datastore.entity "Task" do |t|
      t["category"] = "Personal"
      t["done"] = false
      t["priority"] = 4
      t["description"] = "Learn Cloud Datastore"
    end
    
    task_2 = datastore.entity "Task" do |t|
      t["category"] = "Personal"
      t["done"] = false
      t["priority"] = 5
      t["description"] = "Integrate Cloud Datastore"
    end
    
    tasks = datastore.save task_1, task_2
    task_key_1 = tasks[0].key
    task_key_2 = tasks[1].key

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
