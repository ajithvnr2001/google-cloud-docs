---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-listen-handle-error/
title: Handle Firestore watch listener errors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:00.539343+00:00
---

# Handle Firestore watch listener errors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-listen-handle-error/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Handle Firestore watch listener errors Stay organized with collections  Save and categorize content based on your preferences. 

Handle Firestore watch listener errors

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get real-time updates](https://docs.cloud.google.com/firestore/native/docs/query-data/listen)



## Code sample

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    )
    
    // listenErrors demonstrates how to handle listening errors.
    func listenErrors(ctx context.Context, w io.Writer, projectID, collection string) error {
    	// projectID := "project-id"
    	ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    	defer cancel()
    
    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	it := client.Collection(collection).Snapshots(ctx)
    	for {
    		snap, err := it.Next()
    		// Canceled will be returned when ctx is cancelled and DeadlineExceeded will
    		// be returned when ctx reaches its deadline.
    		if e := status.Code(err); e == codes.Canceled || e == codes.DeadlineExceeded {
    			return nil
    		}
    		if err != nil {
    			return fmt.Errorf("Snapshots.Next: %w", err)
    		}
    		if snap != nil {
    			for _, change := range snap.Changes {
    				if change.Kind == firestore.[DocumentAdded](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_DocumentAdded_DocumentRemoved_DocumentModified) {
    					fmt.Fprintf(w, "New city: %v\n", change.Doc.Data())
    				}
    			}
    		}
    	}
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    db.collection("cities")
        .addSnapshotListener(
            new EventListener<QuerySnapshot>() {
              @Override
              public void onEvent(
                  @Nullable QuerySnapshot snapshots, @Nullable FirestoreException e) {
                if (e != null) {
                  System.err.println("Listen failed: " + e);
                  return;
                }
    
                for (DocumentChange dc : snapshots.getDocumentChanges()) {
                  if (dc.getType() == Type.ADDED) {
                    System.out.println("New city: " + dc.getDocument().getData());
                  }
                }
              }
            });

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    db.collection('cities')
      .onSnapshot((snapshot) => {
        //...
      }, (error) => {
        //...
      });

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    listener = firestore.col(collection_path).listen do |snapshot|
      snapshot.changes.each do |change|
        puts "New city: #{change.doc.document_id}" if change.added?
      end
    end
    
    # Register to be notified when unhandled errors occur.
    listener.on_error do |error|
      puts "Listen failed: #{error.message}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
