---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-get-as-map/
title: Retrieve Firestore Document as Map \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:34.876040+00:00
---

# Retrieve Firestore Document as Map  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-get-as-map/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Retrieve Firestore Document as Map Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve Firestore Document as Map

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference docRef = db.Collection("cities").Document("SF");
    DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
    if (snapshot.Exists)
    {
        Console.WriteLine("Document data for {0} document:", snapshot.Id);
        Dictionary<string, object> city = snapshot.ToDictionary();
        foreach (KeyValuePair<string, object> pair in city)
        {
            Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
        }
    }
    else
    {
        Console.WriteLine("Document {0} does not exist!", snapshot.Id);
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func docAsMap(ctx context.Context, client *firestore.Client) (map[string]interface{}, error) {
    	dsnap, err := client.Collection("cities").Doc("SF").Get(ctx)
    	if err != nil {
    		return nil, err
    	}
    	m := dsnap.Data()
    	fmt.Printf("Document data: %#v\n", m)
    	return m, nil
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference docRef = db.collection("cities").document("SF");
    // asynchronously retrieve the document
    ApiFuture<DocumentSnapshot> future = docRef.get();
    // ...
    // future.get() blocks on response
    DocumentSnapshot document = future.get();
    if (document.exists()) {
      System.out.println("Document data: " + document.getData());
    } else {
      System.out.println("No such document!");
    }

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const cityRef = db.collection('cities').doc('SF');
    const doc = await cityRef.get();
    if (!doc.exists) {
      console.log('No such document!');
    } else {
      console.log('Document data:', doc.data());
    }

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $docRef = $db->collection('samples/php/cities')->document('SF');
    $snapshot = $docRef->snapshot();
    
    if ($snapshot->exists()) {
        printf('Document data:' . PHP_EOL);
        print_r($snapshot->data());
    } else {
        printf('Document %s does not exist!' . PHP_EOL, $snapshot->id());
    }

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    doc_ref = db.collection("cities").document("SF")
    
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document!")

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    doc_ref  = firestore.doc "#{collection_path}/SF"
    snapshot = doc_ref.get
    if snapshot.exists?
      puts "#{snapshot.document_id} data: #{snapshot.data}."
    else
      puts "Document #{snapshot.document_id} does not exist!"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
