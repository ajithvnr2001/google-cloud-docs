---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-partition-query/
title: Query a collection group using a partitioned query \u00a0|\u00a0 Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:24.273560+00:00
---

# Query a collection group using a partitioned query  |  Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-partition-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Query a collection group using a partitioned query Stay organized with collections  Save and categorize content based on your preferences. 

Query a collection group using a partitioned query

## Code sample

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities := client.CollectionGroup("cities")
    
    // Get a partioned query for the cities collection group, with a maximum
    // partition count of 10
    partitionedQueries, err := cities.GetPartitionedQueries(ctx, 10)
    if err != nil {
    	return fmt.Errorf("GetPartitionedQueries: %w", err)
    }
    
    fmt.Printf("Collection Group query partitioned to %d queries\n", len(partitionedQueries))
    
    // Retrieve the first query and iterate over the documents contained.
    query := partitionedQueries[0]
    iter := query.Documents(ctx)
    for {
    	doc, err := iter.Next()
    	if err == iterator.Done {
    		break
    	}
    	if err != nil {
    		return fmt.Errorf("documents iterator: %w", err)
    	}
    	fmt.Println(doc.Data())
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
