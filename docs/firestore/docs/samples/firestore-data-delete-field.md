---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-field/
title: Delete a Firestore field \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:45.549582+00:00
---

# Delete a Firestore field  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Delete a Firestore field Stay organized with collections  Save and categorize content based on your preferences. 

Delete a Firestore field

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Delete documents and fields](https://docs.cloud.google.com/firestore/native/docs/manage-data/delete-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference cityRef = db.Collection("cities").Document("BJ");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Capital", FieldValue.Delete }
    };
    await cityRef.UpdateAsync(updates);

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/firestore"
    )
    
    func deleteField(ctx context.Context, client *firestore.Client) error {
    	_, err := client.Collection("cities").Doc("BJ").Update(ctx, []firestore.Update{
    		{
    			Path:  "capital",
    			Value: firestore.[Delete](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Delete_ServerTimestamp),
    		},
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	// ...
    	return err
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference docRef = db.collection("cities").document("BJ");
    Map<String, Object> updates = new HashMap<>();
    updates.put("capital", FieldValue.delete());
    // Update and delete the "capital" field in the document
    ApiFuture<WriteResult> writeResult = docRef.update(updates);
    System.out.println("Update time : " + writeResult.get());

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a document reference
    const cityRef = db.collection('cities').doc('BJ');
    
    // Remove the 'capital' field from the document
    const res = await cityRef.update({
      capital: FieldValue.delete()
    });

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $cityRef = $db->collection('samples/php/cities')->document('BJ');
    $cityRef->update([
        ['path' => 'capital', 'value' => FieldValue::deleteField()]
    ]);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = db.collection("cities").document("BJ")
    city_ref.update({"capital": firestore.DELETE_FIELD})

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = firestore.doc "#{collection_path}/BJ"
    city_ref.update({ capital: firestore.field_delete })

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
