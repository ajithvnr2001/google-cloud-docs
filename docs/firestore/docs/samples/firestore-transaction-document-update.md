---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-transaction-document-update/
title: Updating a Firestore document in a transaction \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:00.143037+00:00
---

# Updating a Firestore document in a transaction  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-transaction-document-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Updating a Firestore document in a transaction Stay organized with collections  Save and categorize content based on your preferences. 

Updating a Firestore document in a transaction

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transactions and batched writes](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference cityRef = db.Collection("cities").Document("SF");
    await db.RunTransactionAsync(async transaction =>
    {
        DocumentSnapshot snapshot = await transaction.GetSnapshotAsync(cityRef);
        long newPopulation = snapshot.GetValue<long>("Population") + 1;
        Dictionary<string, object> updates = new Dictionary<string, object>
        {
            { "Population", newPopulation}
        };
        transaction.Update(cityRef, updates);
    });

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/firestore"
    )
    
    func runSimpleTransaction(ctx context.Context, client *firestore.Client) error {
    	// ...
    
    	ref := client.Collection("cities").Doc("SF")
    	err := client.[RunTransaction](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Client_RunTransaction)(ctx, func(ctx context.Context, tx *firestore.Transaction) error {
    		doc, err := tx.Get(ref) // tx.Get, NOT ref.Get!
    		if err != nil {
    			return err
    		}
    		pop, err := doc.[DataAt](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_DocumentSnapshot_DataAt)("population")
    		if err != nil {
    			return err
    		}
    		return tx.Set(ref, map[string]interface{}{
    			"population": pop.(int64) + 1,
    		}, firestore.[MergeAll](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_MergeAll))
    	})
    	if err != nil {
    		// Handle any errors appropriately in this section.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	return err
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Initialize doc
    final DocumentReference docRef = db.collection("cities").document("SF");
    City city = new City("SF");
    city.setCountry("USA");
    city.setPopulation(860000L);
    docRef.set(city).get();
    
    // run an asynchronous transaction
    ApiFuture<Void> futureTransaction =
        db.runTransaction(
            transaction -> {
              // retrieve document and increment population field
              DocumentSnapshot snapshot = transaction.get(docRef).get();
              long oldPopulation = snapshot.getLong("population");
              transaction.update(docRef, "population", oldPopulation + 1);
              return null;
            });
    // block on transaction operation using transaction.get()

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Initialize document
    const cityRef = db.collection('cities').doc('SF');
    await cityRef.set({
      name: 'San Francisco',
      state: 'CA',
      country: 'USA',
      capital: false,
      population: 860000
    });
    
    try {
      await db.runTransaction(async (t) => {
        const doc = await t.get(cityRef);
    
        // Add one person to the city population.
        // Note: this could be done without a transaction
        //       by updating the population using FieldValue.increment()
        const newPopulation = doc.data().population + 1;
        t.update(cityRef, {population: newPopulation});
      });
    
      console.log('Transaction success!');
    } catch (e) {
      console.log('Transaction failure:', e);
    }

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $cityRef = $db->collection('samples/php/cities')->document('SF');
    $db->runTransaction(function (Transaction $transaction) use ($cityRef) {
        $snapshot = $transaction->snapshot($cityRef);
        $newPopulation = $snapshot['population'] + 1;
        $transaction->update($cityRef, [
            ['path' => 'population', 'value' => $newPopulation]
        ]);
    });

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    transaction = db.transaction()
    city_ref = db.collection("cities").document("SF")
    
    @firestore.transactional
    def update_in_transaction(transaction, city_ref):
        snapshot = city_ref.get(transaction=transaction)
        transaction.update(city_ref, {"population": snapshot.get("population") + 1})
    
    update_in_transaction(transaction, city_ref)

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = firestore.doc "#{collection_path}/SF"
    
    firestore.transaction do |tx|
      new_population = tx.get(city_ref).data[:population] + 1
      puts "New population is #{new_population}."
      tx.update city_ref, { population: new_population }
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
