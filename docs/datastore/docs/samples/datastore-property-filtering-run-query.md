---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-property-filtering-run-query/
title: Property filter query \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:08.450289+00:00
---

# Property filter query  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-property-filtering-run-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Property filter query Stay organized with collections  Save and categorize content based on your preferences. 

Use a property filter query.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Datastore Metadata](https://docs.cloud.google.com/datastore/docs/concepts/metadataqueries)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Key key = _db.CreateKeyFactory("__kind__").CreateKey("Task");
    Key startKey = new KeyFactory(key, "__property__")
        .CreateKey("priority");
    Query query = new Query("__property__")
    {
        Filter = Filter.GreaterThanOrEqual("__key__", startKey)
    };
    var properties = new List<string>();
    foreach (Entity entity in _db.RunQuery(query).Entities)
    {
        string kind = entity.Key.Path[0].Name;
        string property = entity.Key.Path[1].Name;
        properties.Add($"{kind}.{property}");
    };

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Key startKey =
        datastore
            .newKeyFactory()
            .setKind("__property__")
            .addAncestors(PathElement.of("__kind__", "Task"))
            .newKey("priority");
    Query<Key> query =
        Query.newKeyQueryBuilder()
            .setKind("__property__")
            .setFilter(PropertyFilter.ge("__key__", startKey))
            .build();
    Map<String, Collection<String>> propertiesByKind = new HashMap<>();
    QueryResults<Key> keys = datastore.run(query);
    while (keys.hasNext()) {
      Key key = keys.next();
      String kind = key.getParent().getName();
      String propertyName = key.getName();
      Collection<String> properties = propertiesByKind.get(kind);
      if (properties == null) {
        properties = new HashSet<String>();
        propertiesByKind.put(kind, properties);
      }
      properties.add(propertyName);
    }

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $ancestorKey = $datastore->key('__kind__', 'Task');
    $startKey = $datastore->key('__property__', 'priority')
        ->ancestorKey($ancestorKey);
    $query = $datastore->query()
        ->kind('__property__')
        ->filter('__key__', '>=', $startKey);
    $result = $datastore->runQuery($query);
    /* @var array<string> $properties */
    $properties = [];
    /* @var Entity $entity */
    foreach ($result as $entity) {
        $kind = $entity->key()->path()[0]['name'];
        $propertyName = $entity->key()->path()[1]['name'];
        $properties[] = "$kind.$propertyName";
    }

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    start_key = datastore.key [["__kind__", "Task"], ["__property__", "priority"]]
    query = datastore.query("__property__")
                     .select("__key__")
                     .where("__key__", ">=", start_key)
    
    entities = datastore.run query
    properties_by_kind = entities.each_with_object({}) do |entity, memo|
      kind = entity.key.parent.name
      prop = entity.key.name
      memo[kind] ||= []
      memo[kind] << prop
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
