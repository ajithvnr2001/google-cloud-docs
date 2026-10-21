---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-field/
title: Update a Firestore document field \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:51.916804+00:00
---

# Update a Firestore document field  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Update a Firestore document field Stay organized with collections  Save and categorize content based on your preferences. 

Update a Firestore document field

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference cityRef = db.Collection("cities").Document("new-city-id");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Capital", false }
    };
    await cityRef.UpdateAsync(updates);
    
    // You can also update a single field with: await cityRef.UpdateAsync("Capital", false);

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/firestore"
    )
    
    func updateDoc(ctx context.Context, client *firestore.Client) error {
    	// ...
    
    	_, err := client.Collection("cities").Doc("DC").Update(ctx, []firestore.Update{
    		{
    			Path:  "capital",
    			Value: true,
    		},
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	return err
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Update an existing document
    DocumentReference docRef = db.collection("cities").document("DC");
    
    // (async) Update one field
    ApiFuture<WriteResult> future = docRef.update("capital", true);
    
    // ...
    WriteResult result = future.get();
    System.out.println("Write result: " + result);

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const cityRef = db.collection('cities').doc('DC');
    
    // Set the 'capital' field of the city
    const res = await cityRef.update({capital: true});

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $cityRef = $db->collection('samples/php/cities')->document('DC');
    $cityRef->update([
        ['path' => 'capital', 'value' => true]
    ]);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = db.collection("cities").document("DC")
    
    # Set the capital field
    city_ref.update({"capital": True})

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = firestore.doc "#{collection_path}/DC"
    city_ref.update({ capital: true })

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
