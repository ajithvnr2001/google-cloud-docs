---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-quickstart/
title: Quickstart \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:21.505311+00:00
---

# Quickstart  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Save an entity.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Datastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.html);
    
    namespace GoogleCloudSamples
    {
        public class QuickStart
        {
            public static void Main(string[] args)
            {
                // Your Google Cloud Platform project ID
                string projectId = "YOUR-PROJECT-ID";
    
                // Instantiates a client
                [DatastoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreDb.html) db = [DatastoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreDb.html#Google_Cloud_Datastore_V1_DatastoreDb_Create_System_String_System_String_Google_Cloud_Datastore_V1_DatastoreClient_)(projectId);
    
                // The kind for the new entity
                string kind = "Task";
                // The name/ID for the new entity
                string name = "sampletask1";
                [KeyFactory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.KeyFactory.html) keyFactory = db.[CreateKeyFactory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreDb.html#Google_Cloud_Datastore_V1_DatastoreDb_CreateKeyFactory_System_String_)(kind);
                // The Cloud Datastore key for the new entity
                [Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Key.html) key = keyFactory.[CreateKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.KeyFactory.html#Google_Cloud_Datastore_V1_KeyFactory_CreateKey_System_Int64_)(name);
    
                var task = new [Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Entity.html)
                {
                    Key = key,
                    ["description"] = "Buy milk"
                };
                using ([DatastoreTransaction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreTransaction.html) transaction = db.[BeginTransaction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreDb.html#Google_Cloud_Datastore_V1_DatastoreDb_BeginTransaction_Google_Api_Gax_Grpc_CallSettings_)())
                {
                    // Saves the task
                    transaction.[Upsert](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreTransaction.html#Google_Cloud_Datastore_V1_DatastoreTransaction_Upsert_Google_Cloud_Datastore_V1_Entity___)(task);
                    transaction.[Commit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreTransaction.html#Google_Cloud_Datastore_V1_DatastoreTransaction_Commit_Google_Api_Gax_Grpc_CallSettings_)();
    
                    Console.WriteLine($"Saved {task.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Key.html).[Path](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Key.html#Google_Cloud_Datastore_V1_Key_Path)[0].Name}: {(string)task["description"]}");
                }
            }
        }
    }
    

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample datastore-quickstart fetches an entity from Google Cloud Datastore.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/datastore"
    )
    
    type Task struct {
    	Description string
    }
    
    func main() {
    	ctx := context.Background()
    
    	// Set your Google Cloud Platform project ID.
    	projectID := "YOUR_PROJECT_ID"
    
    	// Creates a client.
    	client, err := datastore.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// Sets the kind for the new entity.
    	kind := "Task"
    	// Sets the name/ID for the new entity.
    	name := "sampletask1"
    	// Creates a Key instance.
    	taskKey := datastore.[NameKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Key_NameKey)(kind, name, nil)
    
    	// Creates a Task instance.
    	task := Task{
    		Description: "Buy milk",
    	}
    
    	// Saves the new entity.
    	if _, err := client.Put(ctx, taskKey, &task); err != nil {
    		log.Fatalf("Failed to save task: %v", err)
    	}
    
    	fmt.Printf("Saved %v: %v\n", taskKey, task.Description)
    }
    

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.datastore.[Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html);
    import com.google.cloud.datastore.[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html);
    import com.google.cloud.datastore.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html);
    import com.google.cloud.datastore.[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key.html);
    
    public class QuickstartSample {
      public static void main(String... args) throws Exception {
        // Instantiates a client
        [Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html) datastore = [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html).getDefaultInstance().getService();
    
        // The kind for the new entity
        String kind = "Task";
        // The name/ID for the new entity
        String name = "sampletask1";
        // The Cloud Datastore key for the new entity
        [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key.html) taskKey = datastore.[newKeyFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html#com_google_cloud_datastore_Datastore_newKeyFactory__)().setKind(kind).[newKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.KeyFactory.html#com_google_cloud_datastore_KeyFactory_newKey__)(name);
    
        // Prepares the new entity
        [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html) task = [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html).newBuilder(taskKey).set("description", "Buy milk").build();
    
        // Saves the entity
        datastore.[put](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html#com_google_cloud_datastore_Datastore_put_com_google_cloud_datastore_FullEntity____)(task);
    
        System.out.printf("Saved %s: %s%n", task.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity.html#com_google_cloud_datastore_BaseEntity_getKey__)().getName(), task.[getString](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity.html#com_google_cloud_datastore_BaseEntity_getString_java_lang_String_)("description"));
    
        // Retrieve entity
        [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html) retrieved = datastore.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html#com_google_cloud_datastore_Datastore_get_com_google_cloud_datastore_Key_com_google_cloud_datastore_DatastoreExecutionOptions_)(taskKey);
    
        System.out.printf("Retrieved %s: %s%n", taskKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key.html#com_google_cloud_datastore_Key_getName__)(), retrieved.[getString](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity.html#com_google_cloud_datastore_BaseEntity_getString_java_lang_String_)("description"));
      }
    }

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    use Google\Cloud\Datastore\DatastoreClient;
    
    # Your Google Cloud Platform project ID
    $projectId = 'YOUR_PROJECT_ID';
    
    # Instantiates a client
    $datastore = new DatastoreClient([
        'projectId' => $projectId
    ]);
    
    # The kind for the new entity
    $kind = 'Task';
    
    # The name/ID for the new entity
    $name = 'sampletask1';
    
    # The Cloud Datastore key for the new entity
    $taskKey = $datastore->key($kind, $name);
    
    # Prepares the new entity
    $task = $datastore->entity($taskKey, ['description' => 'Buy milk']);
    
    # Saves the entity
    $datastore->upsert($task);
    
    echo 'Saved ' . $task->key() . ': ' . $task['description'] . PHP_EOL;

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    # Instantiates a client
    datastore_client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)()
    
    # The kind for the new entity
    kind = "Task"
    # The name/ID for the new entity
    name = "sampletask1"
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)(kind, name)
    
    # Prepares the new entity
    task = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Entity](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.entity.Entity.html)(key=task_key)
    task["description"] = "Buy milk"
    
    # Saves the entity
    datastore_client.[put](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_put)(task)
    
    print(f"Saved {task.key.[name](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.key.Key.html#google_cloud_datastore_key_Key_name)}: {task['description']}")

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    require "google/cloud/datastore"
    
    # Instantiate a client
    datastore = Google::Cloud::[Datastore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore.html)
    
    # The kind for the new entity
    kind = "Task"
    # The name/ID for the new entity
    # task_name = "sampleTask"
    # The Cloud Datastore key for the new entity
    task_key = datastore.key kind, task_name
    
    # Prepares the new entity
    task = datastore.entity task_key do |t|
      t["description"] = "Buy milk"
    end
    
    # Saves the entity
    datastore.save task
    
    puts "Saved #{task.key.name}: #{task['description']}"
    task_key = datastore.find task_key

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
