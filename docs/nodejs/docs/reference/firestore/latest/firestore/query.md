---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query/
title: Class Query (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:36.879843+00:00
---

# Class Query (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Query (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A Query refers to a query which you can read or stream from. You can also construct refined Query objects by adding filters and ordering.

Query

## Implements

FirebaseFirestore.Query<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Query` class.

## Properties 

### firestore
    
    
    get firestore(): Firestore;

The [Firestore][Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore) instance for the Firestore database (useful for performing transactions, etc.).

{Firestore} Query#firestore

**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    collectionRef.add({foo: 'bar'}).then(documentReference => {
      let firestore = documentReference.firestore;
      console.log(`Root location for document is ${firestore.formattedName}`);
    });
    

## Methods 

### _findNearest(options)
    
    
    _findNearest(options: VectorQueryOptions): VectorQuery<AppModelType, DbModelType>;

**Parameter**  
---  
**Name** | **Description**  
`options` |  `[VectorQueryOptions](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorqueryoptions)`   
  
**Returns**  
---  
**Type** | **Description**  
`[VectorQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquery)<AppModelType, DbModelType>` |   
  
### _getResponse(transactionOrReadTime, explainOptions)
    
    
    _getResponse(transactionOrReadTime?: Uint8Array | Timestamp | api.ITransactionOptions, explainOptions?: firestore.ExplainOptions): Promise<QueryResponse<QuerySnapshot<AppModelType, DbModelType>>>;

**Parameters**  
---  
**Name** | **Description**  
`transactionOrReadTime` |  `Uint8Array | [Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp) | google.firestore.v1.ITransactionOptions`   
  
`explainOptions` |  `firestore.ExplainOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<QueryResponse<[QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot)<AppModelType, DbModelType>>>` |   
  
### _isCollectionGroupQuery()
    
    
    _isCollectionGroupQuery(): boolean;

Returns a value indicating if this query is a collection group query

**Returns**  
---  
**Type** | **Description**  
`boolean` |   
  
### aggregate(aggregateSpec)
    
    
    aggregate<T extends firestore.AggregateSpec>(aggregateSpec: T): AggregateQuery<T, AppModelType, DbModelType>;

Returns a query that can perform the given aggregations.

The returned query, when executed, calculates the specified aggregations over the documents in the result set of this query without actually downloading the documents.

Using the returned query to perform aggregations is efficient because only the final aggregation values, not the documents' data, is downloaded. The returned query can perform aggregations of the documents count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

**Parameter**  
---  
**Name** | **Description**  
`aggregateSpec` |  `T`   
An `AggregateSpec` object that specifies the aggregates to perform over the result set. The AggregateSpec specifies aliases for each aggregate, which can be used to retrieve the aggregate result.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatequery)<T, AppModelType, DbModelType>` |   
**Type Parameter**  
---  
**Name** | **Description**  
`T` |   
**Example**
    
    
    typescript
    const aggregateQuery = col.aggregate(query, {
      countOfDocs: count(),
      totalHours: sum('hours'),
      averageScore: average('score')
    });
    
    const aggregateSnapshot = await aggregateQuery.get();
    const countOfDocs: number = aggregateSnapshot.data().countOfDocs;
    const totalHours: number = aggregateSnapshot.data().totalHours;
    const averageScore: number | null = aggregateSnapshot.data().averageScore;
    

### count()
    
    
    count(): AggregateQuery<{
            count: firestore.AggregateField<number>;
        }, AppModelType, DbModelType>;

Returns a query that counts the documents in the result set of this query.

The returned query, when executed, counts the documents in the result set of this query without actually downloading the documents.

Using the returned query to count the documents is efficient because only the final count, not the documents' data, is downloaded. The returned query can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

**Returns**  
---  
**Type** | **Description**  
`[AggregateQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatequery)<{ count: FirebaseFirestore.AggregateField<number>; }, AppModelType, DbModelType>` | a query that counts the documents in the result set of this query. The count can be retrieved from `snapshot.data().count`, where `snapshot` is the `AggregateQuerySnapshot` resulting from running the returned query.  
  
### endAt(fieldValuesOrDocumentSnapshot)
    
    
    endAt(...fieldValuesOrDocumentSnapshot: Array<unknown>): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) that ends at the provided set of field values relative to the order of the query. The order of the provided values must match the order of the order by clauses of the query.

**Parameter**  
---  
**Name** | **Description**  
`fieldValuesOrDocumentSnapshot` |  `Array<unknown>`   
The snapshot of the document the query results should end at or the field values to end this query at, in order of the query's order by.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} A query with the new ending point.  
**Example**
    
    
    let query = firestore.collection('col');
    
    query.orderBy('foo').endAt(42).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### endBefore(fieldValuesOrDocumentSnapshot)
    
    
    endBefore(...fieldValuesOrDocumentSnapshot: Array<unknown>): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) that ends before the set of field values relative to the order of the query. The order of the provided values must match the order of the order by clauses of the query.

**Parameter**  
---  
**Name** | **Description**  
`fieldValuesOrDocumentSnapshot` |  `Array<unknown>`   
The snapshot of the document the query results should end before or the field values to end this query before, in order of the query's order by.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} A query with the new ending point.  
**Example**
    
    
    let query = firestore.collection('col');
    
    query.orderBy('foo').endBefore(42).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### explain(options)
    
    
    explain(options?: firestore.ExplainOptions): Promise<ExplainResults<QuerySnapshot<AppModelType, DbModelType>>>;

Plans and optionally executes this query. Returns a Promise that will be resolved with the planner information, statistics from the query execution (if any), and the query results (if any).

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.ExplainOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ExplainResults](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/explainresults)<[QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot)<AppModelType, DbModelType>>>` | A Promise that will be resolved with the planner information, statistics from the query execution (if any), and the query results (if any).  
  
### explainStream(explainOptions)
    
    
    explainStream(explainOptions?: firestore.ExplainOptions): NodeJS.ReadableStream;

Executes the query and streams the results as the following object: {document?: DocumentSnapshot, metrics?: ExplainMetrics}

The stream surfaces documents one at a time as they are received from the server, and at the end, it will surface the metrics associated with executing the query.

**Parameter**  
---  
**Name** | **Description**  
`explainOptions` |  `firestore.ExplainOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`NodeJS.ReadableStream` |   
**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    let count = 0;
    
    query.explainStream({analyze: true}).on('data', (data) => {
      if (data.document) {
        // Use data.document which is a DocumentSnapshot instance.
        console.log(`Found document with name '${data.document.id}'`);
        ++count;
      }
      if (data.metrics) {
        // Use data.metrics which is an ExplainMetrics instance.
      }
    }).on('end', () => {
      console.log(`Received ${count} documents.`);
    });
    

### findNearest(vectorField, queryVector, options)
    
    
    findNearest(vectorField: string | firestore.FieldPath, queryVector: firestore.VectorValue | Array<number>, options: {
            limit: number;
            distanceMeasure: 'EUCLIDEAN' | 'COSINE' | 'DOT_PRODUCT';
        }): VectorQuery<AppModelType, DbModelType>;

Returns a query that can perform vector distance (similarity) search with given parameters.

The returned query, when executed, performs a distance (similarity) search on the specified `vectorField` against the given `queryVector` and returns the top documents that are closest to the `queryVector`.

Only documents whose `vectorField` field is a [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue) of the same dimension as `queryVector` participate in the query, all other documents are ignored.

**Parameters**  
---  
**Name** | **Description**  
`vectorField` |  `string | FirebaseFirestore.FieldPath`   
A string or [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath) specifying the vector field to search on.  
`queryVector` |  `FirebaseFirestore.VectorValue | Array<number>`   
The [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue) used to measure the distance from `vectorField` values in the documents.  
`options` |  `{ limit: number; distanceMeasure: 'EUCLIDEAN' | 'COSINE' | 'DOT_PRODUCT'; }`   
Options control the vector query. `limit` specifies the upper bound of documents to return, must be a positive integer with a maximum value of 1000. `distanceMeasure` specifies what type of distance is calculated when performing the query.  
**Returns**  
---  
**Type** | **Description**  
`[VectorQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquery)<AppModelType, DbModelType>` |   
**Example**
    
    
    // Returns the closest 10 documents whose Euclidean distance from their 'embedding' fields are closed to [41, 42].
    const vectorQuery = col.findNearest('embedding', [41, 42], {limit: 10, distanceMeasure: 'EUCLIDEAN'});
    
    const querySnapshot = await vectorQuery.get();
    querySnapshot.forEach(...);
    

### findNearest(options)
    
    
    findNearest(options: VectorQueryOptions): VectorQuery<AppModelType, DbModelType>;

Returns a query that can perform vector distance (similarity) search with given parameters.

The returned query, when executed, performs a distance (similarity) search on the specified `vectorField` against the given `queryVector` and returns the top documents that are closest to the `queryVector`.

Only documents whose `vectorField` field is a [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue) of the same dimension as `queryVector` participate in the query, all other documents are ignored.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `[VectorQueryOptions](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorqueryoptions)`   
An argument specifying the behavior of the [VectorQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquery) returned by this function. See [VectorQueryOptions](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorqueryoptions).  
**Returns**  
---  
**Type** | **Description**  
`[VectorQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquery)<AppModelType, DbModelType>` |   
**Example**
    
    
    // Returns the closest 10 documents whose Euclidean distance from their 'embedding' fields are closed to [41, 42].
    const vectorQuery = col.findNearest({
        vectorField: 'embedding',
        queryVector: [41, 42],
        limit: 10,
        distanceMeasure: 'EUCLIDEAN',
        distanceResultField: 'distance',
        distanceThreshold: 0.125
    });
    
    const querySnapshot = await aggregateQuery.get();
    querySnapshot.forEach(...);
    

### get()
    
    
    get(): Promise<QuerySnapshot<AppModelType, DbModelType>>;

Executes the query and returns the results as a [QuerySnapshot][QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot).

**Returns**  
---  
**Type** | **Description**  
`Promise<[QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot)<AppModelType, DbModelType>>` | {Promise.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### isEqual(other)
    
    
    isEqual(other: firestore.Query<AppModelType, DbModelType>): boolean;

Returns true if this `Query` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.Query<AppModelType, DbModelType>`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `Query` is equal to the provided value.  
  
### limit(limit)
    
    
    limit(limit: number): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) that only returns the first matching documents.

This function returns a new (immutable) instance of the Query (rather than modify the existing instance) to impose the limit.

**Parameter**  
---  
**Name** | **Description**  
`limit` |  `number`   
The maximum number of items to return.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} The created Query.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '>', 42);
    
    query.limit(1).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### limitToLast(limit)
    
    
    limitToLast(limit: number): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) that only returns the last matching documents.

You must specify at least one orderBy clause for limitToLast queries, otherwise an exception will be thrown during execution.

Results for limitToLast queries cannot be streamed via the `stream()` API.

**Parameter**  
---  
**Name** | **Description**  
`limit` |  `number`   
The maximum number of items to return.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | The created Query.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '>', 42);
    
    query.limitToLast(1).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Last matching document is ${documentSnapshot.ref.path}`);
      });
    });
    

### offset(offset)
    
    
    offset(offset: number): Query<AppModelType, DbModelType>;

Specifies the offset of the returned results.

This function returns a new (immutable) instance of the [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) (rather than modify the existing instance) to impose the offset.

**Parameter**  
---  
**Name** | **Description**  
`offset` |  `number`   
The offset to apply to the Query results  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} The created Query.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '>', 42);
    
    query.limit(10).offset(20).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### onSnapshot(onNext, onError)
    
    
    onSnapshot(onNext: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void, onError?: (error: Error) => void): () => void;

Attaches a listener for QuerySnapshot events.

**Parameters**  
---  
**Name** | **Description**  
`onNext` |  `(snapshot: [QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot)<AppModelType, DbModelType>) => void`   
A callback to be called every time a new [QuerySnapshot][QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot) is available.  
`onError` |  `(error: Error) => void`   
A callback to be called if the listen fails or is cancelled. No further callbacks will occur.  
**Returns**  
---  
**Type** | **Description**  
`() => void` | {function()} An unsubscribe function that can be called to cancel the snapshot listener.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    let unsubscribe = query.onSnapshot(querySnapshot => {
      console.log(`Received query snapshot of size ${querySnapshot.size}`);
    }, err => {
      console.log(`Encountered error: ${err}`);
    });
    
    // Remove this listener.
    unsubscribe();
    

### orderBy(fieldPath, directionStr)
    
    
    orderBy(fieldPath: string | firestore.FieldPath, directionStr?: firestore.OrderByDirection): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) that's additionally sorted by the specified field, optionally in descending order instead of ascending.

This function returns a new (immutable) instance of the Query (rather than modify the existing instance) to impose the field mask.

**Parameters**  
---  
**Name** | **Description**  
`fieldPath` |  `string | FirebaseFirestore.FieldPath`   
The field to sort by.  
`directionStr` |  `firestore.OrderByDirection`   
Optional direction to sort by ('asc' or 'desc'). If not specified, order will be ascending.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} The created Query.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '>', 42);
    
    query.orderBy('foo', 'desc').get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### select(fieldPaths)
    
    
    select(...fieldPaths: Array<string | FieldPath>): Query;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) instance that applies a field mask to the result and returns only the specified subset of fields. You can specify a list of field paths to return, or use an empty list to only return the references of matching documents.

Queries that contain field masks cannot be listened to via `onSnapshot()` listeners.

This function returns a new (immutable) instance of the Query (rather than modify the existing instance) to impose the field mask.

**Parameter**  
---  
**Name** | **Description**  
`fieldPaths` |  `Array<string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)>`   
The field paths to return.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)` | {Query} The created Query.  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    let documentRef = collectionRef.doc('doc');
    
    return documentRef.set({x:10, y:5}).then(() => {
      return collectionRef.where('x', '>', 5).select('y').get();
    }).then((res) => {
      console.log(`y is ${res.docs[0].get('y')}.`);
    });
    

### startAfter(fieldValuesOrDocumentSnapshot)
    
    
    startAfter(...fieldValuesOrDocumentSnapshot: Array<unknown>): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) that starts after the provided set of field values relative to the order of the query. The order of the provided values must match the order of the order by clauses of the query.

**Parameter**  
---  
**Name** | **Description**  
`fieldValuesOrDocumentSnapshot` |  `Array<unknown>`   
The snapshot of the document the query results should start after or the field values to start this query after, in order of the query's order by.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} A query with the new starting point.  
**Example**
    
    
    let query = firestore.collection('col');
    
    query.orderBy('foo').startAfter(42).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### startAt(fieldValuesOrDocumentSnapshot)
    
    
    startAt(...fieldValuesOrDocumentSnapshot: Array<unknown>): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) that starts at the provided set of field values relative to the order of the query. The order of the provided values must match the order of the order by clauses of the query.

**Parameter**  
---  
**Name** | **Description**  
`fieldValuesOrDocumentSnapshot` |  `Array<unknown>`   
The snapshot of the document the query results should start at or the field values to start this query at, in order of the query's order by.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} A query with the new starting point.  
**Example**
    
    
    let query = firestore.collection('col');
    
    query.orderBy('foo').startAt(42).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### stream()
    
    
    stream(): NodeJS.ReadableStream;

Executes the query and streams the results as [QueryDocumentSnapshots][QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot).

**Returns**  
---  
**Type** | **Description**  
`NodeJS.ReadableStream` | {Stream.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    let count = 0;
    
    query.stream().on('data', (documentSnapshot) => {
      console.log(`Found document with name '${documentSnapshot.id}'`);
      ++count;
    }).on('end', () => {
      console.log(`Total count is ${count}`);
    });
    

### where(fieldPath, opStr, value)
    
    
    where(fieldPath: string | FieldPath, opStr: firestore.WhereFilterOp, value: unknown): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) with the additional filter that documents must contain the specified field and that its value should satisfy the relation constraint provided.

This function returns a new (immutable) instance of the Query (rather than modify the existing instance) to impose the filter.

**Parameters**  
---  
**Name** | **Description**  
`fieldPath` |  `string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)`   
The name of a property value to compare.  
`opStr` |  `firestore.WhereFilterOp`   
A comparison operation in the form of a string. Acceptable operator strings are "<", "<=", "==", "!=", ">=", ">", "array-contains", "in", "not-in", and "array-contains-any".  
`value` |  `unknown`   
The value to which to compare the field for inclusion in a query.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} The created Query.  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    collectionRef.where('foo', '==', 'bar').get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### where(filter)
    
    
    where(filter: Filter): Query<AppModelType, DbModelType>;

Creates and returns a new [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) with the additional filter that documents should satisfy the relation constraint(s) provided.

This function returns a new (immutable) instance of the Query (rather than modify the existing instance) to impose the filter.

**Parameter**  
---  
**Name** | **Description**  
`filter` |  `[Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)`   
A unary or composite filter to apply to the Query.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query} The created Query.  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    collectionRef.where(Filter.and(Filter.where('foo', '==', 'bar'), Filter.where('foo', '!=', 'baz'))).get()
      .then(querySnapshot => {
        querySnapshot.forEach(documentSnapshot => {
          console.log(`Found document at ${documentSnapshot.ref.path}`);
        });
    });
    

### withConverter(converter)
    
    
    withConverter<NewAppModelType, NewDbModelType extends firestore.DocumentData = firestore.DocumentData>(converter: firestore.FirestoreDataConverter<NewAppModelType, NewDbModelType> | null): Query<NewAppModelType, NewDbModelType>;

**Parameter**  
---  
**Name** | **Description**  
`converter` |  `FirebaseFirestore.FirestoreDataConverter<NewAppModelType, NewDbModelType> | null`   
  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<NewAppModelType, NewDbModelType>` |   
**Type Parameters**  
---  
**Name** | **Description**  
`NewAppModelType` |   
`NewDbModelType` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
