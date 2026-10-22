---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-run-query-projection/
title: Run projection query \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:21.631020+00:00
---

# Run projection query  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-run-query-projection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Run projection query Stay organized with collections  Save and categorize content based on your preferences. 

Run a projection query.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Datastore queries](https://docs.cloud.google.com/datastore/docs/concepts/queries)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Query query = new Query("Task")
    {
        Projection = { "priority", "percent_complete" }
    };
    List<long> priorities = new List<long>();
    List<double> percentCompletes = new List<double>();
    foreach (var entity in _db.RunQuery(query).Entities)
    {
        priorities.Add((long)entity["priority"]);
        percentCompletes.Add((double)entity["percent_complete"]);
    }

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    var priorities []int
    var percents []float64
    it := client.Run(ctx, query)
    for {
    	var task Task
    	if _, err := it.Next(&task); err == iterator.Done {
    		break
    	} else if err != nil {
    		log.Fatal(err)
    	}
    	priorities = append(priorities, task.Priority)
    	percents = append(percents, task.PercentComplete)
    }

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    List<Long> priorities = new LinkedList<>();
    List<Double> percentCompletes = new LinkedList<>();
    QueryResults<ProjectionEntity> tasks = datastore.run(query);
    while (tasks.hasNext()) {
      ProjectionEntity task = tasks.next();
      priorities.add(task.getLong("priority"));
      percentCompletes.add(task.getDouble("percent_complete"));
    }

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $priorities = array();
    $percentCompletes = array();
    $result = $datastore->runQuery($query);
    /* @var Entity $task */
    foreach ($result as $task) {
        $priorities[] = $task['priority'];
        $percentCompletes[] = $task['percent_complete'];
    }

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    priorities = []
    percent_completes = []
    
    for task in query.fetch():
        priorities.append(task["priority"])
        percent_completes.append(task["percent_complete"])

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    priorities = []
    percent_completes = []
    datastore.run(query).each do |task|
      priorities << task["priority"]
      percent_completes << task["percent_complete"]
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
