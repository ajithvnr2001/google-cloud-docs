---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-retrieve-entities/
title: Example datastore list tasks \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:21.316959+00:00
---

# Example datastore list tasks  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-retrieve-entities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Example datastore list tasks Stay organized with collections  Save and categorize content based on your preferences. 

Example datastore list tasks

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting started with the Firestore in Datastore mode API](https://docs.cloud.google.com/datastore/docs/datastore-api-tutorial)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Returns a list of all task entities in ascending order of creation time.
    /// </summary>
    IEnumerable<Entity> ListTasks()
    {
        Query query = new Query("Task")
        {
            Order = { { "created", PropertyOrder.Types.Direction.Descending } }
        };
        return _db.RunQuery(query).Entities;
    }
    

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/datastore"
    )
    
    // ListTasks returns all the tasks in ascending order of creation time.
    func ListTasks(projectID string) ([]*Task, error) {
    	ctx := context.Background()
    	client, err := datastore.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Could not create datastore client: %v", err)
    	}
    
    	var tasks []*Task
    	// Create a query to fetch all Task entities, ordered by "created".
    	query := datastore.[NewQuery](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Query_NewQuery)("Task").[Order](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Query_Order)("created")
    	keys, err := client.[GetAll](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/index.html#cloud_google_com_go_datastore_Client_GetAll)(ctx, query, &tasks)
    	if err != nil {
    		return nil, err
    	}
    
    	// Set the id field on each Task from the corresponding key.
    	for i, key := range keys {
    		tasks[i].id = key.ID
    	}
    
    	return tasks, nil
    }
    

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Returns a list of all task entities in ascending order of creation time.
     *
     * @throws DatastoreException if the query fails
     */
    Iterator<Entity> listTasks() {
      Query<Entity> query =
          Query.newEntityQueryBuilder().setKind("Task").setOrderBy(OrderBy.asc("created")).build();
      return datastore.run(query);
    }
    

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    /**
     * Return an iterator for all the tasks in ascending order of creation time.
     *
     * @param string $projectId The Google Cloud project ID.
     */
    function list_tasks(string $projectId)
    {
        $datastore = new DatastoreClient(['projectId' => $projectId]);
    
        $query = $datastore->query()
            ->kind('Task')
            ->order('created');
        $result = $datastore->runQuery($query);
        /* @var Entity $task */
        foreach ($result as $index => $task) {
            printf('ID: %s' . PHP_EOL, $task->key()->pathEnd()['id']);
            printf('  Description: %s' . PHP_EOL, $task['description']);
            printf('  Status: %s' . PHP_EOL, $task['done'] ? 'done' : 'created');
            printf('  Created: %s' . PHP_EOL, $task['created']->format('Y-m-d H:i:s e'));
            print(PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    def list_tasks(client: [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)):
        # Create a query against all of your objects of kind "Task"
        query = client.[query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_query)(kind="Task")
        query.[order](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.query.Query.html#google_cloud_datastore_query_Query_order) = ["created"]
    
        return list(query.fetch())
    
    

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_tasks
      require "google/cloud/datastore"
    
      datastore = Google::Cloud::[Datastore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore.html)
    
      query = datastore.query("Task").order("created")
      tasks = datastore.run query
    
      tasks.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Properties.html) do |t|
        puts t["description"]
        puts t["done"] ? "  Done" : "  Not Done"
        puts "  ID: #{t.key.id}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
