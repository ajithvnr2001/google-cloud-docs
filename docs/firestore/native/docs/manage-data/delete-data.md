---
url: https://docs.cloud.google.com/firestore/native/docs/manage-data/delete-data/
title: Delete documents and fields \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:23.988126+00:00
---

# Delete documents and fields  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/manage-data/delete-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete documents and fields

The following examples demonstrate how to delete documents, fields, and collections.

## Delete documents

To delete a document, use the following language-specific `delete()` methods:

### Web version 9

Use the `deleteDoc()` method:
    
    
    import { doc, deleteDoc } from "firebase/firestore";
    
    await deleteDoc(doc(db, "cities", "DC"));
    
    [delete_document.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/delete_document.js#L8-L10)

### Web version 8

Use the `delete()` method:
    
    
    db.collection("cities").doc("DC").delete().then(() => {
        console.log("Document successfully deleted!");
    }).catch((error) => {
        console.error("Error removing document: ", error);
    });
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L514-L518)

##### Swift

Use the `delete()` method:

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    do {
      try await db.collection("cities").document("DC").delete()
      print("Document successfully removed!")
    } catch {
      print("Error removing document: \(error)")
    }
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L436-L441)

##### Objective-C

Use the `deleteDocumentWithCompletion:` method:

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[[self.db collectionWithPath:@"cities"] documentWithPath:@"DC"]
        deleteDocumentWithCompletion:^(NSError * _Nullable error) {
          if (error != nil) {
            NSLog(@"Error removing document: %@", error);
          } else {
            NSLog(@"Document successfully removed!");
          }
    }];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L364-L371)

##### Kotlin  
Android

Use the `delete()` method:
    
    
    db.collection("cities").document("DC")
        .delete()
        .addOnSuccessListener { Log.d(TAG, "DocumentSnapshot successfully deleted!") }
        .addOnFailureListener { e -> Log.w(TAG, "Error deleting document", e) }
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L405-L408)

##### Java  
Android

Use the `delete()` method:
    
    
    db.collection("cities").document("DC")
            .delete()
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(Void aVoid) {
                    Log.d(TAG, "DocumentSnapshot successfully deleted!");
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    Log.w(TAG, "Error deleting document", e);
                }
            });
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L515-L528)

### Dart

Use the `delete()` method:
    
    
    db.collection("cities").doc("DC").delete().then(
          (doc) => print("Document deleted"),
          onError: (e) => print("Error updating document $e"),
        );
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L355-L358)

##### Java

Use the `delete()` method:
    
    
    // asynchronously delete a document
    ApiFuture<WriteResult> writeResult = db.collection("cities").document("DC").delete();
    // ...
    System.out.println("Update time : " + writeResult.get().getUpdateTime());
    
    [ManageDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L299-L302)

##### Python

Use the `delete()` method:
    
    
    db.collection("cities").document("DC").delete()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L826-L826)

##### Python  
(Async)

Use the `delete()` method:
    
    
    await db.collection("cities").document("DC").delete()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L680-L680)

##### C++

Use the `Delete()` method:
    
    
    db->Collection("cities").Document("DC").Delete().OnCompletion(
        [](const Future<void>& future) {
          if (future.error() == Error::kErrorOk) {
            std::cout << "DocumentSnapshot successfully deleted!" << std::endl;
          } else {
            std::cout << "Error deleting document: " << future.error_message()
                      << std::endl;
          }
        });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L386-L394)

##### Node.js

Use the `delete()` method:
    
    
    const res = await db.collection('cities').doc('DC').delete();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L362-L362)

##### Go

Use the `Delete()` method:
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/firestore"
    )
    
    func deleteDoc(ctx context.Context, client *firestore.Client) error {
    	_, err := client.Collection("cities").Doc("DC").Delete(ctx)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    
    	return err
    }
    
    
    [save_data_delete_doc.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/save_data_delete_doc.go#L18-L35)

##### PHP

Use the `delete()` method:
    
    
    $db->collection('samples/php/cities')->document('DC')->delete();
    
    [data_delete_doc.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/data_delete_doc.php#L40-L40)

##### Unity

Use the `DeleteAsync()` method:
    
    
    DocumentReference cityRef = db.Collection("cities").Document("DC");
    cityRef.DeleteAsync();

##### C#

Use the `DeleteAsync()` method:
    
    
    DocumentReference cityRef = db.Collection("cities").Document("DC");
    await cityRef.DeleteAsync();
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/DeleteData/Program.cs#L38-L39)

##### Ruby

Use the `delete()` method:
    
    
    city_ref = firestore.doc "#{collection_path}/DC"
    city_ref.delete
    
    [delete_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/delete_data.rb#L24-L25)

**Warning:** Deleting a document does not delete its subcollections!

When you delete a document, Firestore does not automatically delete the documents within its subcollections. You can still access the subcollection documents by reference. For example, you can access the document at path `/mycoll/mydoc/mysubcoll/mysubdoc` even if you delete the parent document at `/mycoll/mydoc`.

Non-existent parent documents [appear in the console](https://docs.cloud.google.com/firestore/native/docs/using-console#non-existent-parent-documents), but they don't appear in query results and snapshots.

If you want to delete a document and all the documents within its subcollections, you must do so manually. For more information, see Delete Collections.

## Delete fields

To delete specific fields from a document, use the following language-specific `FieldValue.delete()` methods when you update a document:

### Web version 9

Use the `deleteField()` method:
    
    
    import { doc, updateDoc, deleteField } from "firebase/firestore";
    
    const cityRef = doc(db, 'cities', 'BJ');
    
    // Remove the 'capital' field from the document
    await updateDoc(cityRef, {
        capital: deleteField()
    });
    
    [update_delete_field.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/update_delete_field.js#L8-L15)

### Web version 8

Use the `FieldValue.delete()` method:
    
    
    var cityRef = db.collection('cities').doc('BJ');
    
    // Remove the 'capital' field from the document
    var removeCapital = cityRef.update({
        capital: firebase.firestore.FieldValue.delete()
    });
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L818-L823)

##### Swift

Use the `FieldValue.delete()` method:

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    do {
    
      try await db.collection("cities").document("BJ").updateData([
        "capital": FieldValue.delete(),
      ])
      print("Document successfully updated")
    } catch {
      print("Error updating document: \(error)")
    }
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L481-L489)

##### Objective-C

Use the `fieldValueForDelete:` method:

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[[self.db collectionWithPath:@"cities"] documentWithPath:@"BJ"] updateData:@{
      @"capital": [FIRFieldValue fieldValueForDelete]
    } completion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error updating document: %@", error);
      } else {
        NSLog(@"Document successfully updated");
      }
    }];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L414-L422)

##### Kotlin  
Android

Use the `FieldValue.delete()` method:
    
    
    val docRef = db.collection("cities").document("BJ")
    
    // Remove the 'capital' field from the document
    val updates = hashMapOf<String, Any>(
        "capital" to FieldValue.delete(),
    )
    
    docRef.update(updates).addOnCompleteListener { }
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1103-L1110)

##### Java  
Android

Use the `FieldValue.delete()` method:
    
    
    DocumentReference docRef = db.collection("cities").document("BJ");
    
    // Remove the 'capital' field from the document
    Map<String,Object> updates = new HashMap<>();
    updates.put("capital", FieldValue.delete());
    
    docRef.update(updates).addOnCompleteListener(new OnCompleteListener<Void>() {
        // ...
        // ...
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1321-L1332)

### Dart

Use the `FieldValue.delete()` method:
    
    
    final docRef = db.collection("cities").doc("BJ");
    
    // Remove the 'capital' field from the document
    final updates = <String, dynamic>{
      "capital": FieldValue.delete(),
    };
    
    docRef.update(updates);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L364-L371)

##### Java

Use the `FieldValue.delete()` method:
    
    
    DocumentReference docRef = db.collection("cities").document("BJ");
    Map<String, Object> updates = new HashMap<>();
    updates.put("capital", FieldValue.delete());
    // Update and delete the "capital" field in the document
    ApiFuture<WriteResult> writeResult = docRef.update(updates);
    System.out.println("Update time : " + writeResult.get());
    
    [ManageDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L286-L291)

##### Python

Use the `firestore.DELETE_FIELD` method:
    
    
    city_ref = db.collection("cities").document("BJ")
    city_ref.update({"capital": firestore.DELETE_FIELD})
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L833-L834)

##### Python  
(Async)

Use the `firestore.DELETE_FIELD` method:
    
    
    city_ref = db.collection("cities").document("BJ")
    await city_ref.update({"capital": firestore.DELETE_FIELD})
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L687-L688)

##### C++

Use the `FieldValue::Delete()` method:
    
    
    DocumentReference doc_ref = db->Collection("cities").Document("BJ");
    doc_ref.Update({{"capital", FieldValue::Delete()}})
        .OnCompletion([](const Future<void>& future) { /*...*/ });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L408-L410)

##### Node.js

Use the `FieldValue.delete()` method:
    
    
    // Create a document reference
    const cityRef = db.collection('cities').doc('BJ');
    
    // Remove the 'capital' field from the document
    const res = await cityRef.update({
      capital: FieldValue.delete()
    });
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L324-L330)

##### Go

Use the `firestore.Delete` method:
    
    
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
    
    
    [save_data_delete_field.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/save_data_delete_field.go#L18-L47)

##### PHP

Use the `FieldValue::deleteField()` method:
    
    
    $cityRef = $db->collection('samples/php/cities')->document('BJ');
    $cityRef->update([
        ['path' => 'capital', 'value' => FieldValue::deleteField()]
    ]);
    
    [data_delete_field.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/data_delete_field.php#L41-L44)

##### Unity

Use the `FieldValue.Delete` method:
    
    
    DocumentReference cityRef = db.Collection("cities").Document("BJ");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Capital", FieldValue.Delete }
    };

##### C#

Use the `FieldValue.Delete` method:
    
    
    DocumentReference cityRef = db.Collection("cities").Document("BJ");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Capital", FieldValue.Delete }
    };
    await cityRef.UpdateAsync(updates);
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/DeleteData/Program.cs#L48-L53)

##### Ruby

Use the `firestore.field_delete` method:
    
    
    city_ref = firestore.doc "#{collection_path}/BJ"
    city_ref.update({ capital: firestore.field_delete })
    
    [delete_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/delete_data.rb#L36-L37)

## Delete collections

To delete an entire collection or subcollection in Firestore, retrieve (read) all the documents within the collection or subcollection and delete them. This process incurs both read and delete costs. If you have larger collections, you may want to delete the documents in smaller batches to avoid out-of-memory errors. Repeat the process until you've deleted the entire collection or subcollection.

Deleting a collection requires coordinating an unbounded number of individual delete requests. If you need to delete entire collections, do so only from a trusted server environment. While it is possible to delete a collection from a mobile/web client, doing so has negative security and performance implications.

The following snippets are simplified for clarity and don't include error handling, security, deleting subcollections, or performance optimizations. To learn more about one recommended approach to deleting collections in production, see [Deleting Collections and Subcollections](https://docs.cloud.google.com/firestore/native/docs/solutions/delete-collections).

#####  Web 
    
    
    // Deleting collections from a Web client is not recommended.

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    // Deleting collections from an Apple client is not recommended.

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    // Deleting collections from an Apple client is not recommended.
      

##### Kotlin  
Android
    
    
    // Deleting collections from an Android client is not recommended.

##### Java  
Android
    
    
    // Deleting collections from an Android client is not recommended.

### Dart

Deleting collections from the client is not recommended.

##### Java
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.firestore.[CollectionReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.CollectionReference.html);
    import com.google.cloud.firestore.[Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html);
    import com.google.cloud.firestore.[FirestoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html);
    
    public class DeleteCollection {
    
      /**
       * Delete a collection and all its subcollections.
       *
       * @param projectId The Google Cloud project ID
       * @param collectionName The name of the collection to delete
       */
      public static void deleteCollection(String projectId, String collectionName) throws Exception {
        [FirestoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html) firestoreOptions =
            [FirestoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html#com_google_cloud_firestore_FirestoreOptions_getDefaultInstance__)().toBuilder().setProjectId(projectId).build();
        try ([Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html) db = firestoreOptions.getService()) {
          [CollectionReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.CollectionReference.html) collection = db.collection(collectionName);
    
          ApiFuture<Void> future = db.[recursiveDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_recursiveDelete_com_google_cloud_firestore_CollectionReference_)(collection);
    
          future.get();
          System.out.println("Collection and all its subcollections deleted successfully.");
        }
      }
    
      public static void main(String[] args) throws Exception {
        String projectId = "example-project-id";
        String collectionName = "example-collection-name";
    
        deleteCollection(projectId, collectionName);
      }
    }
    
    [DeleteCollection.java](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/ccae4f9c2e68c2d00dd6dc88e98143a539ddfe8c/firestore/samples/src/main/java/com/example/firestore/DeleteCollection.java#L20-L53)

##### Python
    
    
    def delete_collection(coll_ref):
    
        print(f"Recursively deleting collection: {coll_ref}")
        db.recursive_delete(coll_ref)
    
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L842-L846)

##### Python  
(Async)
    
    
    async def delete_collection(coll_ref):
    
        await db.recursive_delete(coll_ref)
    
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L696-L699)

##### C++
    
    
    // This is not supported. Delete data using CLI as discussed below.
      

##### Node.js
    
    
    async function deleteCollection(db, collectionPath) {
      const collectionRef = db.collection(collectionPath);
      return await db.recursiveDelete(collectionRef);
    }
    
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L950-L954)

##### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    func deleteCollection(w io.Writer, projectID, collectionName string,
    	batchSize int) error {
    
    	// Instantiate a client
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return err
    	}
    
    	col := client.Collection(collectionName)
    	bulkwriter := client.BulkWriter(ctx)
    
    	for {
    		// Get a batch of documents
    		iter := col.Limit(batchSize).Documents(ctx)
    		numDeleted := 0
    
    		// Iterate through the documents, adding
    		// a delete operation for each one to the BulkWriter.
    		for {
    			doc, err := iter.Next()
    			if err == iterator.Done {
    				break
    			}
    			if err != nil {
    				return err
    			}
    
    			bulkwriter.Delete(doc.[Ref](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_Ref))
    			numDeleted++
    		}
    
    		// If there are no documents to delete,
    		// the process is over.
    		if numDeleted == 0 {
    			bulkwriter.[End](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_BulkWriter_End)()
    			break
    		}
    
    		bulkwriter.[Flush](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_BulkWriter_Flush)()
    	}
    	fmt.Fprintf(w, "Deleted collection \"%s\"", collectionName)
    	return nil
    }
    
    
    [save_data_delete_collection.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/save_data_delete_collection.go#L18-L73)

##### PHP
    
    
    function data_delete_collection(string $projectId, string $collectionName, int $batchSize)
    {
        // Create the Cloud Firestore client
        $db = new FirestoreClient([
            'projectId' => $projectId,
        ]);
        $collectionReference = $db->collection($collectionName);
        $documents = $collectionReference->limit($batchSize)->documents();
        while (!$documents->isEmpty()) {
            foreach ($documents as $document) {
                printf('Deleting document %s' . PHP_EOL, $document->id());
                $document->reference()->delete();
            }
            $documents = $collectionReference->limit($batchSize)->documents();
        }
    }
    
    [data_delete_collection.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/data_delete_collection.php#L36-L51)

##### Unity
    
    
    // This is not supported. Delete data using CLI as discussed below.

##### C#
    
    
    private static async Task DeleteCollection(CollectionReference collectionReference, int batchSize)
    {
        QuerySnapshot snapshot = await collectionReference.Limit(batchSize).GetSnapshotAsync();
        IReadOnlyList<DocumentSnapshot> documents = snapshot.Documents;
        while (documents.Count > 0)
        {
            foreach (DocumentSnapshot document in documents)
            {
                Console.WriteLine("Deleting document {0}", document.Id);
                await document.Reference.DeleteAsync();
            }
            snapshot = await collectionReference.Limit(batchSize).GetSnapshotAsync();
            documents = snapshot.Documents;
        }
        Console.WriteLine("Finished deleting all documents from the collection.");
    }
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/DeleteData/Program.cs#L59-L74)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    query      = cities_ref
    
    query.get do |document_snapshot|
      puts "Deleting document #{document_snapshot.document_id}."
      document_ref = document_snapshot.ref
      document_ref.delete
    end
    
    [delete_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/delete_data.rb#L48-L55)

## Delete data with TTL policies

A TTL policy designates a given field as the expiration time for documents in a given collection group. TTL delete operations count towards your document delete costs.

For information about setting TTL, see [Manage data retention with TTL policies](https://docs.cloud.google.com/firestore/native/docs/ttl).

## Bulk deletion jobs

Firestore supports several tools for bulk deletion. You should select a tool based on the number of documents you need to delete and the level of configurability you need.

**Note:** Deleting a large number of documents [can impact latency](https://docs.cloud.google.com/firestore/native/docs/best-practices#avoid-skipping). If latency is caused by too many recent deletes, the issue should automatically resolve after some time. If the issue does not resolve, [contact support](https://cloud.google.com/support-hub).

For smaller jobs of thousands of documents, use the console or the Firebase CLI. For larger jobs, these tools might start to timeout and require you to run the tool multiple times.

### Console

You can [delete documents and collections from the Firestore page in the console](https://docs.cloud.google.com/firestore/native/docs/using-console#delete_data). Deleting a document from the console deletes all of the nested data in that document, including any subcollections.

### Firebase CLI

You can also use the [Firebase CLI](https://firebase.google.com/docs/cli) to delete documents and collections. Use the following command to delete data:

**Note:** Deleting data with the Firebase CLI incurs read and delete costs. For more information, see [Pricing](https://firebase.google.com/docs/firestore/pricing#pricing_by_location). 
    
    
    firebase firestore:delete  --database=DATABASE_ID PATH
    

Replace DATABASE_ID with your database ID and PATH with a path to a document or collection.

For large deletion jobs (millions of documents), use one of the following:

### Managed bulk delete

Firestore supports bulk deleting one or more collection groups. For more information, see [Bulk delete data](https://docs.cloud.google.com/firestore/native/docs/manage-data/bulk-delete). 

### Dataflow connector

You can use [Dataflow](https://cloud.google.com/dataflow/docs/overview) for bulk operations on your database. This option is the most configurable, but also requires more set up than other bulk delete options. See the Firestore connector for Dataflow introduction [blog post](https://cloud.google.com/blog/topics/developers-practitioners/using-firestore-and-apache-beam-data-processing) has an example of deleting all documents in a collection group. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
