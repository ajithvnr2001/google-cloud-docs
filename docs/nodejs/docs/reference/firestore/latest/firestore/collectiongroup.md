---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectiongroup/
title: Class CollectionGroup (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:33.684147+00:00
---

# Class CollectionGroup (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectiongroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class CollectionGroup (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A `CollectionGroup` refers to all documents that are contained in a collection or subcollection with a specific collection ID.

CollectionGroup

## Inheritance

[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType> > CollectionGroup

## Implements

FirebaseFirestore.CollectionGroup<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(firestore, collectionId, converter)
    
    
    constructor(firestore: Firestore, collectionId: string, converter: firestore.FirestoreDataConverter<AppModelType, DbModelType> | undefined);

Constructs a new instance of the `CollectionGroup` class

**Parameters**  
---  
**Name** | **Description**  
`firestore` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)`   
  
`collectionId` |  `string`   
  
`converter` |  `FirebaseFirestore.FirestoreDataConverter<AppModelType, DbModelType> | undefined`   
  
  
## Methods 

### getPartitions(desiredPartitionCount)
    
    
    getPartitions(desiredPartitionCount: number): AsyncIterable<QueryPartition<AppModelType, DbModelType>>;

Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned cursors are split points that can be used as starting and end points for individual query invocations.

**Parameter**  
---  
**Name** | **Description**  
`desiredPartitionCount` |  `number`   
The desired maximum number of partition points. The number must be strictly positive. The actual number of partitions returned may be fewer.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[QueryPartition](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querypartition)<AppModelType, DbModelType>>` | {AsyncIterable  
**Example**
    
    
    const query = firestore.collectionGroup('collectionId');
    for await (const partition of query.getPartitions(42)) {
      const partitionedQuery = partition.toQuery();
      const querySnapshot = await partitionedQuery.get();
      console.log(`Partition contained ${querySnapshot.length} documents`);
    }
    
    

### withConverter(converter)
    
    
    withConverter<NewAppModelType, NewDbModelType extends firestore.DocumentData = firestore.DocumentData>(converter: firestore.FirestoreDataConverter<NewAppModelType, NewDbModelType> | null): CollectionGroup<NewAppModelType, NewDbModelType>;

Applies a custom data converter to this `CollectionGroup`, allowing you to use your own custom model objects with Firestore. When you call get() on the returned `CollectionGroup`, the provided converter will convert between Firestore data of type `NewDbModelType` and your custom type `NewAppModelType`.

Using the converter allows you to specify generic type arguments when storing and retrieving objects from Firestore.

Passing in `null` as the converter parameter removes the current converter.

**Parameter**  
---  
**Name** | **Description**  
`converter` |  `FirebaseFirestore.FirestoreDataConverter<NewAppModelType, NewDbModelType> | null`   
Converts objects to and from Firestore. Passing in `null` removes the current converter.  
**Returns**  
---  
**Type** | **Description**  
`[CollectionGroup](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectiongroup)<NewAppModelType, NewDbModelType>` | {CollectionGroup} A `CollectionGroup` that uses the provided converter.  
**Type Parameters**  
---  
**Name** | **Description**  
`NewAppModelType` |   
`NewDbModelType` |   
**Example**
    
    
    class Post {
      constructor(readonly title: string, readonly author: string) {}
    
      toString(): string {
        return this.title + ', by ' + this.author;
      }
    }
    
    const postConverter = {
      toFirestore(post: Post): FirebaseFirestore.DocumentData {
        return {title: post.title, author: post.author};
      },
      fromFirestore(
        snapshot: FirebaseFirestore.QueryDocumentSnapshot
      ): Post {
        const data = snapshot.data();
        return new Post(data.title, data.author);
      }
    };
    
    const querySnapshot = await Firestore()
      .collectionGroup('posts')
      .withConverter(postConverter)
      .get();
    for (const doc of querySnapshot.docs) {
      const post = doc.data();
      post.title; // string
      post.toString(); // Should be defined
      post.someNonExistentProperty; // TS error
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
