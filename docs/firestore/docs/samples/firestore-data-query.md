---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-query/
title: Query a Firestore collection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:30.018914+00:00
---

# Query a Firestore collection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Query a Firestore collection Stay organized with collections  Save and categorize content based on your preferences. 

Query a Firestore collection

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data)
  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Query capitalQuery = db.Collection("cities").WhereEqualTo("Capital", true);
    QuerySnapshot capitalQuerySnapshot = await capitalQuery.GetSnapshotAsync();
    foreach (DocumentSnapshot documentSnapshot in capitalQuerySnapshot.Documents)
    {
        Console.WriteLine("Document data for {0} document:", documentSnapshot.Id);
        Dictionary<string, object> city = documentSnapshot.ToDictionary();
        foreach (KeyValuePair<string, object> pair in city)
        {
            Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
        }
        Console.WriteLine("");
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    func multipleDocs(ctx context.Context, client *firestore.Client) error {
    	fmt.Println("All capital cities:")
    	iter := client.Collection("cities").Where("capital", "==", true).Documents(ctx)
    	for {
    		doc, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Println(doc.Data())
    	}
    	return nil
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // asynchronously retrieve multiple documents
    ApiFuture<QuerySnapshot> future = db.collection("cities").whereEqualTo("capital", true).get();
    // future.get() blocks on response
    List<QueryDocumentSnapshot> documents = future.get().getDocuments();
    for (DocumentSnapshot document : documents) {
      System.out.println(document.getId() + " => " + document.toObject(City.class));
    }

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const citiesRef = db.collection('cities');
    const snapshot = await citiesRef.where('capital', '==', true).get();
    if (snapshot.empty) {
      console.log('No matching documents.');
      return;
    }  
    
    snapshot.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $citiesRef = $db->collection('samples/php/cities');
    $query = $citiesRef->where('capital', '=', true);
    $documents = $query->documents();
    foreach ($documents as $document) {
        if ($document->exists()) {
            printf('Document data for document %s:' . PHP_EOL, $document->id());
            print_r($document->data());
            printf(PHP_EOL);
        } else {
            printf('Document %s does not exist!' . PHP_EOL, $document->id());
        }
    }

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Note: Use of CollectionRef stream() is prefered to get()
    docs = (
        db.collection("cities")
        .where(filter=FieldFilter("capital", "==", True))
        .stream()
    )
    
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = firestore.col collection_path
    
    query = cities_ref.where "capital", "=", true
    
    query.get do |city|
      puts "#{city.document_id} data: #{city.data}."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
