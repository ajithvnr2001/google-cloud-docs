---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection/
title: Delete a Firestore collection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:10.383062+00:00
---

# Delete a Firestore collection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Delete a Firestore collection Stay organized with collections  Save and categorize content based on your preferences. 

Delete a Firestore collection and documents within.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Delete documents and fields](https://docs.cloud.google.com/firestore/native/docs/manage-data/delete-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function deleteCollection(db, collectionPath) {
      const collectionRef = db.collection(collectionPath);
      return await db.recursiveDelete(collectionRef);
    }
    

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_collection(coll_ref):
    
        print(f"Recursively deleting collection: {coll_ref}")
        db.recursive_delete(coll_ref)
    

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = firestore.col collection_path
    query      = cities_ref
    
    query.get do |document_snapshot|
      puts "Deleting document #{document_snapshot.document_id}."
      document_ref = document_snapshot.ref
      document_ref.delete
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
