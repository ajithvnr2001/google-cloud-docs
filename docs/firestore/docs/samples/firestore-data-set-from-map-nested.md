---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-from-map-nested/
title: Add a Firestore document using a nested map \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:41.107421+00:00
---

# Add a Firestore document using a nested map  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-from-map-nested/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Add a Firestore document using a nested map Stay organized with collections  Save and categorize content based on your preferences. 

Add a Firestore document using a nested map

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference docRef = db.Collection("data").Document("one");
    Dictionary<string, object> docData = new Dictionary<string, object>
    {
        { "stringExample", "Hello World" },
        { "booleanExample", false },
        { "numberExample", 3.14159265 },
        { "nullExample", null },
        { "arrayExample", new object[] { 5, true, "Hello" } },
        { "objectExample", new Dictionary<string, object>
            {
                { "a", 5 },
                { "b", true},
            }
        }
    };
    
    await docRef.SetAsync(docData);

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    	"time"
    
    	"cloud.google.com/go/firestore"
    )
    
    func addDocDataTypes(ctx context.Context, client *firestore.Client) error {
    	doc := make(map[string]interface{})
    	doc["stringExample"] = "Hello world!"
    	doc["booleanExample"] = true
    	doc["numberExample"] = 3.14159265
    	doc["dateExample"] = time.Now()
    	doc["arrayExample"] = []interface{}{5, true, "hello"}
    	doc["nullExample"] = nil
    	doc["objectExample"] = map[string]interface{}{
    		"a": 5,
    		"b": true,
    	}
    
    	_, err := client.Collection("data").Doc("one").Set(ctx, doc)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	return err
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Map<String, Object> docData = new HashMap<>();
    docData.put("stringExample", "Hello, World");
    docData.put("booleanExample", false);
    docData.put("numberExample", 3.14159265);
    docData.put("nullExample", null);
    
    ArrayList<Object> arrayExample = new ArrayList<>();
    Collections.addAll(arrayExample, 5L, true, "hello");
    docData.put("arrayExample", arrayExample);
    
    Map<String, Object> objectExample = new HashMap<>();
    objectExample.put("a", 5L);
    objectExample.put("b", true);
    
    docData.put("objectExample", objectExample);
    
    ApiFuture<WriteResult> future = db.collection("data").document("one").set(docData);
    System.out.println("Update time : " + future.get().getUpdateTime());

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const data = {
      stringExample: 'Hello, World!',
      booleanExample: true,
      numberExample: 3.14159265,
      dateExample: Timestamp.fromDate(new Date('December 10, 1815')),
      arrayExample: [5, true, 'hello'],
      nullExample: null,
      objectExample: {
        a: 5,
        b: true
      }
    };
    
    const res = await db.collection('data').doc('one').set(data);

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $data = [
        'stringExample' => 'Hello World',
        'booleanExample' => true,
        'numberExample' => 3.14159265,
        'dateExample' => new Timestamp(new DateTime()),
        'arrayExample' => array(5, true, 'hello'),
        'nullExample' => null,
        'objectExample' => ['a' => 5, 'b' => true],
        'documentReferenceExample' => $db->collection('samples/php/data')->document('two'),
    ];
    $db->collection('samples/php/data')->document('one')->set($data);
    printf('Set multiple data-type data for the one document in the data collection.' . PHP_EOL);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    data = {
        "stringExample": "Hello, World!",
        "booleanExample": True,
        "numberExample": 3.14159265,
        "dateExample": datetime.datetime.now(tz=datetime.timezone.utc),
        "arrayExample": [5, True, "hello"],
        "nullExample": None,
        "objectExample": {"a": 5, "b": True},
    }
    
    db.collection("data").document("one").set(data)

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    doc_ref = firestore.doc "#{collection_path}/one"
    
    data = {
      stringExample:  "Hello, World!",
      booleanExample: true,
      numberExample:  3.14159265,
      dateExample:    DateTime.now,
      arrayExample:   [5, true, "hello"],
      nullExample:    nil,
      objectExample:  {
        a: 5,
        b: true
      }
    }
    
    doc_ref.set data

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
