---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-properties/
title: Property types \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:09.039617+00:00
---

# Property types  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Property types Stay organized with collections  Save and categorize content based on your preferences. 

Use property types.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Entities, Properties, and Keys](https://docs.cloud.google.com/datastore/docs/concepts/entities)
  * [Indexes](https://docs.cloud.google.com/datastore/docs/concepts/indexes)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Entity task = new Entity()
    {
        Key = _db.CreateKeyFactory("Task").CreateKey("sampleTask"),
        ["category"] = "Personal",
        ["created"] = new DateTime(1999, 01, 01, 0, 0, 0, DateTimeKind.Utc),
        ["done"] = false,
        ["priority"] = 4,
        ["percent_complete"] = 10.0,
        ["description"] = new Value()
        {
            StringValue = "Learn Cloud Datastore",
            ExcludeFromIndexes = true
        },
    };

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    type Task struct {
    	Category        string
    	Done            bool
    	Priority        int
    	Description     string `datastore:",noindex"`
    	PercentComplete float64
    	Created         time.Time
    }
    task := &Task{
    	Category:        "Personal",
    	Done:            false,
    	Priority:        4,
    	Description:     "Learn Cloud Datastore",
    	PercentComplete: 10.0,
    	Created:         time.Now(),
    }

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Entity task =
        Entity.newBuilder(taskKey)
            .set("category", "Personal")
            .set("created", Timestamp.now())
            .set("done", false)
            .set("priority", 4)
            .set("percent_complete", 10.0)
            .set(
                "description",
                StringValue.newBuilder("Learn Cloud Datastore").setExcludeFromIndexes(true).build())
            .build();

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $task = $datastore->entity(
        $key,
        [
            'category' => 'Personal',
            'created' => new DateTime(),
            'done' => false,
            'priority' => 4,
            'percent_complete' => 10.0,
            'description' => 'Learn Cloud Datastore'
        ],
        ['excludeFromIndexes' => ['description']]
    );

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    # For help authenticating your client, visit
    # https://cloud.google.com/docs/authentication/getting-started
    client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)()
    
    import datetime
    
    key = client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)("Task")
    task = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Entity](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.entity.Entity.html)(key, exclude_from_indexes=("description",))
    task.update(
        {
            "category": "Personal",
            "description": "Learn Cloud Datastore",
            "created": datetime.datetime.now(tz=datetime.timezone.utc),
            "done": False,
            "priority": 4,
            "percent_complete": 10.5,
        }
    )
    client.[put](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_put)(task)

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    task = datastore.entity "Task" do |t|
      t["category"] = "Personal"
      t["created"] = Time.now
      t["done"] = false
      t["priority"] = 4
      t["percent_complete"] = 10.0
      t["description"] = "Learn Cloud Datastore"
      t.exclude_from_indexes! "description", true
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
