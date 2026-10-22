---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-property-by-kind-run-query/
title: Property by kind query \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:09.312017+00:00
---

# Property by kind query  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-property-by-kind-run-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Property by kind query Stay organized with collections  Save and categorize content based on your preferences. 

Query property by kind.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Datastore Metadata](https://docs.cloud.google.com/datastore/docs/concepts/metadataqueries)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Key key = _db.CreateKeyFactory("__kind__").CreateKey("Task");
    Query query = new Query("__property__")
    {
        Filter = Filter.HasAncestor(key)
    };
    var properties = new List<string>();
    foreach (Entity entity in _db.RunQuery(query).Entities)
    {
        string kind = entity.Key.Path[0].Name;
        string property = entity.Key.Path[1].Name;
        var representations = entity["property_representation"]
            .ArrayValue.Values.Select(x => x.StringValue)
            .OrderBy(x => x);
        properties.Add($"{property}:" +
            string.Join(",", representations));
    };

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    kindKey := datastore.NameKey("__kind__", "Task", nil)
    query := datastore.NewQuery("__property__").Ancestor(kindKey)
    
    type Prop struct {
    	Repr []string `datastore:"property_representation"`
    }
    
    var props []Prop
    keys, err := client.GetAll(ctx, query, &props)

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Key key = datastore.newKeyFactory().setKind("__kind__").newKey("Task");
    Query<Entity> query =
        Query.newEntityQueryBuilder()
            .setKind("__property__")
            .setFilter(PropertyFilter.hasAncestor(key))
            .build();
    QueryResults<Entity> results = datastore.run(query);
    Map<String, Collection<String>> representationsByProperty = new HashMap<>();
    while (results.hasNext()) {
      Entity result = results.next();
      String propertyName = result.getKey().getName();
      List<StringValue> representations = result.getList("property_representation");
      Collection<String> currentRepresentations = representationsByProperty.get(propertyName);
      if (currentRepresentations == null) {
        currentRepresentations = new HashSet<>();
        representationsByProperty.put(propertyName, currentRepresentations);
      }
      for (StringValue value : representations) {
        currentRepresentations.add(value.get());
      }
    }

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $ancestorKey = $datastore->key('__kind__', 'Task');
    $query = $datastore->query()
        ->kind('__property__')
        ->hasAncestor($ancestorKey);
    $result = $datastore->runQuery($query);
    /* @var array<string,string> $properties */
    $properties = [];
    /* @var Entity $entity */
    foreach ($result as $entity) {
        $propertyName = $entity->key()->path()[1]['name'];
        $propertyType = $entity['property_representation'];
        $properties[$propertyName] = $propertyType;
    }
    // Example values of $properties: ['description' => ['STRING']]

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    # For help authenticating your client, visit
    # https://cloud.google.com/docs/authentication/getting-started
    client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)()
    
    ancestor = client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)("__kind__", "Task")
    query = client.[query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_query)(kind="__property__", ancestor=ancestor)
    
    representations_by_property = {}
    
    for entity in query.fetch():
        property_name = entity.key.[name](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.key.Key.html#google_cloud_datastore_key_Key_name)
        property_types = entity["property_representation"]
    
        representations_by_property[property_name] = property_types

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    ancestor_key = datastore.key "__kind__", "Task"
    query = datastore.query("__property__")
                     .ancestor(ancestor_key)
    
    entities = datastore.run query
    representations = entities.each_with_object({}) do |entity, memo|
      property_name = entity.key.name
      property_types = entity["property_representation"]
      memo[property_name] = property_types
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
