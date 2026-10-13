---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-batch-writes/
title: Performs a batch update on a Firestore document \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:26.400683+00:00
---

# Performs a batch update on a Firestore document  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-batch-writes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Performs a batch update on a Firestore document Stay organized with collections  Save and categorize content based on your preferences. 

Performs a batch update on a Firestore document

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transactions and batched writes](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    WriteBatch batch = db.StartBatch();
    
    // Set the data for NYC
    DocumentReference nycRef = db.Collection("cities").Document("NYC");
    Dictionary<string, object> nycData = new Dictionary<string, object>
    {
        { "name", "New York City" }
    };
    batch.Set(nycRef, nycData);
    
    // Update the population for SF
    DocumentReference sfRef = db.Collection("cities").Document("SF");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Population", 1000000}
    };
    batch.Update(sfRef, updates);
    
    // Delete LA
    DocumentReference laRef = db.Collection("cities").Document("LA");
    batch.Delete(laRef);
    
    // Commit the batch
    await batch.CommitAsync();

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/firestore"
    )
    
    func batchWrite(ctx context.Context, client *firestore.Client) error {
    	// Get a new write batch.
    	batch := client.[Batch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Client_Batch)()
    
    	// Set the value of "NYC".
    	nycRef := client.Collection("cities").Doc("NYC")
    	batch.Set(nycRef, map[string]interface{}{
    		"name": "New York City",
    	})
    
    	// Update the population of "SF".
    	sfRef := client.Collection("cities").Doc("SF")
    	batch.Set(sfRef, map[string]interface{}{
    		"population": 1000000,
    	}, firestore.[MergeAll](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_MergeAll))
    
    	// Delete the city "LA".
    	laRef := client.Collection("cities").Doc("LA")
    	batch.Delete(laRef)
    
    	// Commit the batch.
    	_, err := batch.Commit(ctx)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	return err
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Get a new write batch
    WriteBatch batch = db.batch();
    
    // Set the value of 'NYC'
    DocumentReference nycRef = db.collection("cities").document("NYC");
    batch.set(nycRef, new City());
    
    // Update the population of 'SF'
    DocumentReference sfRef = db.collection("cities").document("SF");
    batch.update(sfRef, "population", 1000000L);
    
    // Delete the city 'LA'
    DocumentReference laRef = db.collection("cities").document("LA");
    batch.delete(laRef);
    
    // asynchronously commit the batch
    ApiFuture<List<WriteResult>> future = batch.commit();
    // ...
    // future.get() blocks on batch commit operation
    for (WriteResult result : future.get()) {
      System.out.println("Update time : " + result.getUpdateTime());
    }

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Get a new write batch
    const batch = db.batch();
    
    // Set the value of 'NYC'
    const nycRef = db.collection('cities').doc('NYC');
    batch.set(nycRef, {name: 'New York City'});
    
    // Update the population of 'SF'
    const sfRef = db.collection('cities').doc('SF');
    batch.update(sfRef, {population: 1000000});
    
    // Delete the city 'LA'
    const laRef = db.collection('cities').doc('LA');
    batch.delete(laRef);
    
    // Commit the batch
    await batch.commit();

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $batch = $db->bulkWriter();
    
    # Set the data for NYC
    $nycRef = $db->collection('samples/php/cities')->document('NYC');
    $batch->set($nycRef, [
        'name' => 'New York City'
    ]);
    
    # Update the population for SF
    $sfRef = $db->collection('samples/php/cities')->document('SF');
    $batch->update($sfRef, [
        ['path' => 'population', 'value' => 1000000]
    ]);
    
    # Delete LA
    $laRef = $db->collection('samples/php/cities')->document('LA');
    $batch->delete($laRef);
    
    # Commit the batch
    $batch->commit();

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    batch = db.batch()
    
    # Set the data for NYC
    nyc_ref = db.collection("cities").document("NYC")
    batch.set(nyc_ref, {"name": "New York City"})
    
    # Update the population for SF
    sf_ref = db.collection("cities").document("SF")
    batch.update(sf_ref, {"population": 1000000})
    
    # Delete DEN
    den_ref = db.collection("cities").document("DEN")
    batch.delete(den_ref)
    
    # Commit the batch
    batch.commit()

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    firestore.batch do |b|
      # Set the data for NYC
      b.set "#{collection_path}/NYC", { name: "New York City" }
    
      # Update the population for SF
      b.update "#{collection_path}/SF", { population: 1_000_000 }
    
      # Delete LA
      b.delete "#{collection_path}/LA"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
