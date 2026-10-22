---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-from-map/
title: Add a Firestore document using a map \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:58.710600+00:00
---

# Add a Firestore document using a map  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-from-map/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Add a Firestore document using a map Stay organized with collections  Save and categorize content based on your preferences. 

Add a Firestore document using a map

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference docRef = db.Collection("cities").Document("LA");
    Dictionary<string, object> city = new Dictionary<string, object>
    {
        { "name", "Los Angeles" },
        { "state", "CA" },
        { "country", "USA" }
    };
    await docRef.SetAsync(city);

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/firestore"
    )
    
    func addDocAsMap(ctx context.Context, client *firestore.Client) error {
    	_, err := client.Collection("cities").Doc("LA").Set(ctx, map[string]interface{}{
    		"name":    "Los Angeles",
    		"state":   "CA",
    		"country": "USA",
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	return err
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a Map to store the data we want to set
    Map<String, Object> docData = new HashMap<>();
    docData.put("name", "Los Angeles");
    docData.put("state", "CA");
    docData.put("country", "USA");
    docData.put("regions", Arrays.asList("west_coast", "socal"));
    // Add a new document (asynchronously) in collection "cities" with id "LA"
    ApiFuture<WriteResult> future = db.collection("cities").document("LA").set(docData);
    // ...
    // future.get() blocks on response
    System.out.println("Update time : " + future.get().getUpdateTime());

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const data = {
      name: 'Los Angeles',
      state: 'CA',
      country: 'USA'
    };
    
    // Add a new document in collection "cities" with ID 'LA'
    const res = await db.collection('cities').doc('LA').set(data);

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $data = [
        'name' => 'Los Angeles',
        'state' => 'CA',
        'country' => 'USA'
    ];
    $db->collection('samples/php/cities')->document('LA')->set($data);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    data = {"name": "Los Angeles", "state": "CA", "country": "USA"}
    
    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection("cities").document("LA").set(data)

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = firestore.doc "#{collection_path}/LA"
    
    data = {
      name:    "Los Angeles",
      state:   "CA",
      country: "USA"
    }
    
    city_ref.set data

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
