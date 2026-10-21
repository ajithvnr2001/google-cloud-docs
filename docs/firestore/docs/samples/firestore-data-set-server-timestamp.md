---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-server-timestamp/
title: Update a Firestore document Timestamp \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:51.221499+00:00
---

# Update a Firestore document Timestamp  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-server-timestamp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Update a Firestore document Timestamp Stay organized with collections  Save and categorize content based on your preferences. 

Update a Firestore document Timestamp

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference cityRef = db.Collection("cities").Document("new-city-id");
    await cityRef.UpdateAsync("Timestamp", Timestamp.GetCurrentTimestamp());

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/firestore"
    )
    
    func updateDocServerTimestamp(ctx context.Context, client *firestore.Client) error {
    	// ...
    
    	_, err := client.Collection("objects").Doc("some-id").Set(ctx, map[string]interface{}{
    		"timestamp": firestore.[ServerTimestamp](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Delete_ServerTimestamp),
    	}, firestore.[MergeAll](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_MergeAll))
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	return err
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference docRef = db.collection("objects").document("some-id");
    // Update the timestamp field with the value from the server
    ApiFuture<WriteResult> writeResult = docRef.update("timestamp", FieldValue.serverTimestamp());
    System.out.println("Update time : " + writeResult.get());

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a document reference
    const docRef = db.collection('objects').doc('some-id');
    
    // Update the timestamp field with the value from the server
    const res = await docRef.update({
      timestamp: FieldValue.serverTimestamp()
    });

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $docRef = $db->collection('samples/php/objects')->document('some-id');
    $docRef->update([
        ['path' => 'timestamp', 'value' => FieldValue::serverTimestamp()]
    ]);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = db.collection("objects").document("some-id")
    city_ref.update({"timestamp": firestore.SERVER_TIMESTAMP})

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = firestore.doc "#{collection_path}/new-city-id"
    city_ref.update({ timestamp: firestore.field_server_time })

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
