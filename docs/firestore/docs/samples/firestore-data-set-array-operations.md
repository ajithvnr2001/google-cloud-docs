---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-array-operations/
title: Update a Firestore document containing an array field \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:52.472712+00:00
---

# Update a Firestore document containing an array field  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-array-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Update a Firestore document containing an array field Stay organized with collections  Save and categorize content based on your preferences. 

Update a Firestore document containing an array field.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference washingtonRef = db.Collection("cities").Document("DC");
    
    // Atomically add a new region to the "regions" array field.
    await washingtonRef.UpdateAsync("Regions", FieldValue.ArrayUnion("greater_virginia"));
    
    // Atomically remove a region from the "regions" array field.
    await washingtonRef.UpdateAsync("Regions", FieldValue.ArrayRemove("east_coast"));

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference washingtonRef = db.collection("cities").document("DC");
    
    // Atomically add a new region to the "regions" array field.
    ApiFuture<WriteResult> arrayUnion =
        washingtonRef.update("regions", FieldValue.arrayUnion("greater_virginia"));
    System.out.println("Update time : " + arrayUnion.get());
    
    // Atomically remove a region from the "regions" array field.
    ApiFuture<WriteResult> arrayRm =
        washingtonRef.update("regions", FieldValue.arrayRemove("east_coast"));
    System.out.println("Update time : " + arrayRm.get());

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // ...
    const washingtonRef = db.collection('cities').doc('DC');
    
    // Atomically add a new region to the "regions" array field.
    const unionRes = await washingtonRef.update({
      regions: FieldValue.arrayUnion('greater_virginia')
    });
    // Atomically remove a region from the "regions" array field.
    const removeRes = await washingtonRef.update({
      regions: FieldValue.arrayRemove('east_coast')
    });
    
    // To add or remove multiple items, pass multiple arguments to arrayUnion/arrayRemove
    const multipleUnionRes = await washingtonRef.update({
      regions: FieldValue.arrayUnion('south_carolina', 'texas')
      // Alternatively, you can use spread operator in ES6 syntax
      // const newRegions = ['south_carolina', 'texas']
      // regions: FieldValue.arrayUnion(...newRegions)
    });

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $cityRef = $db->collection('samples/php/cities')->document('DC');
    
    // Atomically add a new region to the "regions" array field.
    $cityRef->update([
        ['path' => 'regions', 'value' => FieldValue::arrayUnion(['greater_virginia'])]
    ]);
    
    // Atomically remove a region from the "regions" array field.
    $cityRef->update([
        ['path' => 'regions', 'value' => FieldValue::arrayRemove(['east_coast'])]
    ]);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = db.collection("cities").document("DC")
    
    # Atomically add a new region to the 'regions' array field.
    city_ref.update({"regions": firestore.ArrayUnion(["greater_virginia"])})
    
    # // Atomically remove a region from the 'regions' array field.
    city_ref.update({"regions": firestore.ArrayRemove(["east_coast"])})

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = firestore.doc "#{collection_path}/DC"
    
    # Atomically add a new region to the 'regions' array field.
    city_ref.update({ regions: firestore.field_array_union("greater_virginia") })
    
    # Atomically remove a region from the 'regions' array field.
    city_ref.update({ regions: firestore.field_array_delete("east_coast") })

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
