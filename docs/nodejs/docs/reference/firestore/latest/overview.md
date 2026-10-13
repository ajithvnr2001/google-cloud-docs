---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview/
title: Package @google-cloud/firestore (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:32.204765+00:00
---

# Package @google-cloud/firestore (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Package @google-cloud/firestore (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

## Classes 

### [Aggregate](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregate)

Concrete implementation of the Aggregate type.

### [AggregateField](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield)

Represents an aggregation that can be performed by Firestore.

### [AggregateQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatequery)

A query that calculates aggregations over an underlying query.

### [AggregateQuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatequerysnapshot)

The results of executing an aggregation query.

### [BsonObjectId](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bsonobjectid)

Represents a BSON ObjectId type in Firestore documents.

BsonObjectId

### [BsonTimestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bsontimestamp)

Represents a Request Timestamp type in Firestore documents.

### [BulkWriter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter)

A Firestore BulkWriter that can be used to perform a large number of writes in parallel.

BulkWriter

### [BulkWriterError](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwritererror)

The error thrown when a BulkWriter operation fails.

BulkWriterError

### [BundleBuilder](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bundlebuilder)

Builds a Firestore data bundle with results from the given document and query snapshots.

### [Bytes](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bytes)

An immutable object representing an array of bytes.

### [CollectionGroup](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectiongroup)

A `CollectionGroup` refers to all documents that are contained in a collection or subcollection with a specific collection ID.

CollectionGroup

### [CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)

A CollectionReference object can be used for adding documents, getting document references, and querying for documents (using the methods inherited from [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)).

CollectionReference Query

### [Decimal128Value](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/decimal128value)

Represents a 128-bit decimal type in Firestore documents.

### [DocumentChange](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentchange)

A DocumentChange represents a change to the documents matching a query. It contains the document affected and the type of change that occurred.

DocumentChange

### [DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)

A DocumentReference refers to a document location in a Firestore database and can be used to write, read, or listen to the location. The document at the referenced location may or may not exist. A DocumentReference can also be used to create a [CollectionReference][CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference) to a subcollection.

DocumentReference

### [DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)

A DocumentSnapshot is an immutable representation for a document in a Firestore database. The data can be extracted with [data()] or [get(fieldPath)] to get a specific field.

For a DocumentSnapshot that points to a non-existing document, any data access will return 'undefined'. You can use the [exists] property to explicitly verify a document's existence.

DocumentSnapshot

### [ExecutionStats](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/executionstats)

ExecutionStats contains information about the execution of a query.

ExecutionStats

### [ExplainMetrics](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/explainmetrics)

ExplainMetrics contains information about planning and execution of a query.

ExplainMetrics

### [ExplainResults](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/explainresults)

ExplainResults contains information about planning, execution, and results of a query.

ExplainResults

### [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)

A dot-separated path for navigating sub-objects (e.g. nested maps) within a document.

### [FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)

Sentinel values that can be used when writing documents with set(), create() or update().

FieldValue

### [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)

A `Filter` represents a restriction on one or more field values and can be used to refine the results of a [Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query). `Filters`s are created by invoking , , or and can then be passed to to create a new [Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) instance that also contains this `Filter`.

### [Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)

The Firestore client represents a Firestore Database and is the entry point for all Firestore operations.

### [GeoPoint](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/geopoint)

An immutable object representing a geographic location in Firestore. The location is represented as a latitude/longitude pair.

### [Int32Value](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/int32value)

Represents a 32-bit integer type in Firestore documents.

### [MaxKey](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/maxkey)

Represents the Firestore "Max Key" data type.

MaxKey

### [MinKey](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/minkey)

Represents the Firestore "Min Key" data type.

MinKey

### [Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)

A class that represents an aggregate function.

### [Pipelines.AliasedAggregate](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aliasedaggregate)

An AggregateFunction with alias.

### [Pipelines.AliasedExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aliasedexpression)

Represents an expression that has been assigned an alias using the `.as()` method.

This class wraps an existing `Expression` and associates it with a user-defined alias, allowing the expression's result to be referred to by name in the output of a Firestore pipeline query.

### [Pipelines.BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)

An expression that evaluates to a boolean value.

This expression type is useful for filter conditions.

### [Pipelines.Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)

Represents an expression that can be evaluated to a value within the execution of a `Pipeline`.

Expressions are the building blocks for creating complex queries and transformations in Firestore pipelines. They can represent:

  * **Field references:** Access values from document fields. - **Literals:** Represent constant values (strings, numbers, booleans). - **Function calls:** Apply functions to one or more expressions.



The `Expression` class provides a fluent API for building expressions. You can chain together method calls to create complex expressions.

### [Pipelines.Field](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.field)

Represents a reference to a field in a Firestore document, or outputs of a `Pipeline` stage.

Field references are used to access document field values in expressions and to specify fields for sorting, filtering, and projecting data in Firestore pipelines.

You can create a `Field` instance using the static `field` method:
    
    
    // Create a Field instance for the 'name' field
    const nameField = field("name");
    
    // Create a Field instance for a nested field 'address.city'
    const cityField = field("address.city");
    

### [Pipelines.FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)

This class defines the base class for Firestore `Pipeline` functions, which can be evaluated within pipeline execution.

Typically, you would not use this class or its children directly. Use either the functions like `and`, `equal`, or the methods on `Expression` (, , etc.) to construct new Function instances.

### [Pipelines.Ordering](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.ordering)

Represents an ordering criterion for sorting documents in a Firestore pipeline.

You create `Ordering` instances using the `ascending` and `descending` helper functions.

### [Pipelines.Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)

The Pipeline class provides a flexible and expressive framework for building complex data transformation and query pipelines for Firestore.

A pipeline takes data sources, such as Firestore collections or collection groups, and applies a series of stages that are chained together. Each stage takes the output from the previous stage (or the data source) and produces an output for the next stage (or as the final output of the pipeline).

Expressions can be used within each stage to filter and transform data through the stage.

NOTE: The chained stages do not prescribe exactly how Firestore will execute the pipeline. Instead, Firestore only guarantees that the result is the same as if the chained stages were executed in order.

Usage Examples:

### [Pipelines.PipelineResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelineresult)

A PipelineResult contains data read from a Firestore Pipeline. The data can be extracted with the `data()` or `get(String)` methods.

If the PipelineResult represents a non-document result, `ref` will return a undefined value.

### [Pipelines.PipelineSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesnapshot)

Represents the results of a Firestore pipeline execution.

A `PipelineSnapshot` contains zero or more `PipelineResult` objects representing the documents returned by a pipeline query. It provides methods to iterate over the documents and access metadata about the query results.

### [Pipelines.PipelineSource](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesource)

Represents the source of a Firestore `Pipeline`.

### [PlanSummary](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/plansummary)

PlanSummary contains information about the planning stage of a query.

PlanSummary

### [Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)

A Query refers to a query which you can read or stream from. You can also construct refined Query objects by adding filters and ordering.

Query

### [QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot)

A QueryDocumentSnapshot contains data read from a document in your Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted with [data()] or [get()] to get a specific field.

A QueryDocumentSnapshot offers the same API surface as a [DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot). Since query results contain only existing documents, the [exists] property will always be true and [data()] will never return 'undefined'.

QueryDocumentSnapshot DocumentSnapshot

### [QueryPartition](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querypartition)

A split point that can be used in a query as a starting and/or end point for the query results. The cursors returned by and can only be used in a query that matches the constraint of query that produced this partition.

QueryPartition

### [QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot)

A QuerySnapshot contains zero or more [QueryDocumentSnapshot][QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) objects representing the results of a query. The documents can be accessed as an array via the [documents] property or enumerated using the [forEach] method. The number of documents can be determined via the [empty] and [size] properties.

QuerySnapshot

### [RegexValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/regexvalue)

Represents a regular expression type in Firestore documents.

RegexValue

### [Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)

A Timestamp represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time. It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.

### [Transaction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction)

A reference to a transaction.

The Transaction object passed to a transaction's updateFunction provides the methods to read and write data within the transaction context. See [runTransaction()].

Transaction

### [VectorQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquery)

A query that finds the documents whose vector fields are closest to a certain query vector. Create an instance of `VectorQuery` with .

### [VectorQuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquerysnapshot)

A `VectorQuerySnapshot` contains zero or more `QueryDocumentSnapshot` objects representing the results of a query. The documents can be accessed as an array via the `docs` property or enumerated using the `forEach` method. The number of documents can be determined via the `empty` and `size` properties.

### [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)

Represent a vector type in Firestore documents. Create an instance with [FieldValue.vector()](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue).

VectorValue

### [WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)

A Firestore WriteBatch that can be used to atomically commit multiple write operations at once.

WriteBatch

### [WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)

A WriteResult wraps the write time set by the Firestore servers on sets(), updates(), and creates().

WriteResult

## Interfaces 

### [AggregateSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatespec)

A type whose property values are all `AggregateField` objects.

### [VectorQueryOptions](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorqueryoptions)

Specifies the behavior of the [VectorQuery](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquery) generated by a call to .

## Variables 

### DEFAULT_MAX_IDLE_CHANNELS
    
    
    DEFAULT_MAX_IDLE_CHANNELS = 1

### DEFAULT_MAX_TRANSACTION_ATTEMPTS
    
    
    DEFAULT_MAX_TRANSACTION_ATTEMPTS = 5

The maximum number of times to attempt a transaction before failing.

### MAX_REQUEST_RETRIES
    
    
    MAX_REQUEST_RETRIES = 5

The maximum number of times to retry idempotent requests.

## Functions 

### Pipelines.abs(expr)
    
    
    export declare function abs(expr: Expression): FunctionExpression;

Creates an expression that computes the absolute value of a numeric value.

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compute the absolute value of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the absolute value of the numeric value.  
  
### Pipelines.abs(fieldName)
    
    
    export declare function abs(fieldName: string): FunctionExpression;

Creates an expression that computes the absolute value of a numeric value.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field to compute the absolute value of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the absolute value of the numeric value.  
  
### Pipelines.add(first, second)
    
    
    export declare function add(first: Expression, second: Expression | unknown): FunctionExpression;

Creates an expression that adds the result of two expressions together.
    
    
    // Add the value of the 'quantity' field and the 'reserve' field.
    add(field("quantity"), field("reserve"));
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to add.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal to add.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the addition operation.  
  
### Pipelines.add(fieldName, second)
    
    
    export declare function add(fieldName: string, second: Expression | unknown): FunctionExpression;

Creates an expression that adds a field's value to the result of an expression.
    
    
    // Add the value of the 'quantity' field and the 'reserve' field.
    add("quantity", field("reserve"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the value to add.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal to add.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the addition operation.  
  
### Pipelines.and(first, second, more)
    
    
    export declare function and(first: BooleanExpression, second: BooleanExpression, ...more: BooleanExpression[]): BooleanExpression;

Creates an expression that performs a logical 'AND' operation on multiple filter conditions.
    
    
    // Check if the 'age' field is greater than 18 AND the 'city' field is "London" AND
    // the 'status' field is "active"
    const condition = and(greaterThan("age", 18), equal("city", "London"), equal("status", "active"));
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The first filter condition.  
`second` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The second filter condition.  
`more` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)[]`  
Additional filter conditions to 'AND' together.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the logical 'AND' operation.  
  
### Pipelines.array(elements)
    
    
    export declare function array(elements: unknown[]): FunctionExpression;

Creates an expression that creates a Firestore array value from an input array.
    
    
    // Create an array value from the input array and reference the 'baz' field value from the input document.
    array(['bar', field('baz')]).as('foo');
    

**Parameter**  
---  
**Name** | **Description**  
`elements` | `unknown[]`  
The input array to evaluate in the expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the array function.  
  
### Pipelines.arrayAgg(expression)
    
    
    export declare function arrayAgg(expression: Expression): AggregateFunction;

Creates an aggregation that collects all values of an expression across multiple stage inputs into an array.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to collect values from.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'array_agg' aggregation.  
**Remarks**

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

#### Example
    
    
    typescript
    // Collect all tags from books into an array
    arrayAgg(field("tags")).as("allTags");
    

### Pipelines.arrayAgg(fieldName)
    
    
    export declare function arrayAgg(fieldName: string): AggregateFunction;

Creates an aggregation that collects all values of a field across multiple stage inputs into an array.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to collect values from.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'array_agg' aggregation.  
**Remarks**

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

#### Example
    
    
    typescript
    // Collect all tags from books into an array
    arrayAgg("tags").as("allTags");
    

### Pipelines.arrayAggDistinct(expression)
    
    
    export declare function arrayAggDistinct(expression: Expression): AggregateFunction;

Creates an aggregation that collects all distinct values of an expression across multiple stage inputs into an array.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to collect values from.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'array_agg_distinct' aggregation.  
**Remarks**

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

#### Example
    
    
    typescript
    // Collect all distinct tags from books into an array
    arrayAggDistinct(field("tags")).as("allDistinctTags");
    

### Pipelines.arrayAggDistinct(fieldName)
    
    
    export declare function arrayAggDistinct(fieldName: string): AggregateFunction;

Creates an aggregation that collects all distinct values of a field across multiple stage inputs into an array.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to collect values from.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'array_agg_distinct' aggregation.  
**Remarks**

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

#### Example
    
    
    typescript
    // Collect all distinct tags from books into an array
    arrayAggDistinct("tags").as("allDistinctTags");
    

### Pipelines.arrayConcat(firstArray, secondArray, otherArrays)
    
    
    export declare function arrayConcat(firstArray: Expression, secondArray: Expression | unknown[], ...otherArrays: Array

Creates an expression that concatenates an array expression with other arrays.
    
    
    // Combine the 'items' array with two new item arrays
    arrayConcat(field("items"), [field("newItems"), field("otherItems")]);
    

**Parameters**  
---  
**Name** | **Description**  
`firstArray` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first array expression to concatenate to.  
`secondArray` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown[]`  
The second array expression or array literal to concatenate to.  
`otherArrays` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown[]>`  
Optional additional array expressions or array literals to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the concatenated array.  
  
### Pipelines.arrayConcat(firstArrayField, secondArray, otherArrays)
    
    
    export declare function arrayConcat(firstArrayField: string, secondArray: Expression | unknown[], ...otherArrays: Array

Creates an expression that concatenates a field's array value with other arrays.
    
    
    // Combine the 'items' array with two new item arrays
    arrayConcat("items", [field("newItems"), field("otherItems")]);
    

**Parameters**  
---  
**Name** | **Description**  
`firstArrayField` | `string`  
The first array to concatenate to.  
`secondArray` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown[]`  
The second array expression or array literal to concatenate to.  
`otherArrays` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown[]>`  
Optional additional array expressions or array literals to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the concatenated array.  
  
### Pipelines.arrayContains(array, element)
    
    
    export declare function arrayContains(array: Expression, element: Expression): BooleanExpression;

Creates an expression that checks if an array expression contains a specific element.
    
    
    // Check if the 'colors' array contains the value of field 'selectedColor'
    arrayContains(field("colors"), field("selectedColor"));
    

**Parameters**  
---  
**Name** | **Description**  
`array` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The array expression to check.  
`element` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The element to search for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains' comparison.  
  
### Pipelines.arrayContains(array, element)
    
    
    export declare function arrayContains(array: Expression, element: unknown): BooleanExpression;

Creates an expression that checks if an array expression contains a specific element.
    
    
    // Check if the 'colors' array contains "red"
    arrayContains(field("colors"), "red");
    

**Parameters**  
---  
**Name** | **Description**  
`array` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The array expression to check.  
`element` | `unknown`  
The element to search for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains' comparison.  
  
### Pipelines.arrayContains(fieldName, element)
    
    
    export declare function arrayContains(fieldName: string, element: Expression): BooleanExpression;

Creates an expression that checks if a field's array value contains a specific element.
    
    
    // Check if the 'colors' array contains the value of field 'selectedColor'
    arrayContains("colors", field("selectedColor"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`element` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The element to search for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains' comparison.  
  
### Pipelines.arrayContains(fieldName, element)
    
    
    export declare function arrayContains(fieldName: string, element: unknown): BooleanExpression;

Creates an expression that checks if a field's array value contains a specific value.
    
    
    // Check if the 'colors' array contains "red"
    arrayContains("colors", "red");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`element` | `unknown`  
The element to search for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains' comparison.  
  
### Pipelines.arrayContainsAll(array, values)
    
    
    export declare function arrayContainsAll(array: Expression, values: Array

Creates an expression that checks if an array expression contains all the specified elements.
    
    
    // Check if the "tags" array contains all of the values: "SciFi", "Adventure", and the value from field "tag1"
    arrayContainsAll(field("tags"), [field("tag1"), constant("SciFi"), "Adventure"]);
    

**Parameters**  
---  
**Name** | **Description**  
`array` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The array expression to check.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_all' comparison.  
  
### Pipelines.arrayContainsAll(fieldName, values)
    
    
    export declare function arrayContainsAll(fieldName: string, values: Array

Creates an expression that checks if a field's array value contains all the specified values or expressions.
    
    
    // Check if the 'tags' array contains both of the values from field 'tag1', the value "SciFi", and "Adventure"
    arrayContainsAll("tags", [field("tag1"), "SciFi", "Adventure"]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_all' comparison.  
  
### Pipelines.arrayContainsAll(array, arrayExpression)
    
    
    export declare function arrayContainsAll(array: Expression, arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if an array expression contains all the specified elements.
    
    
    // Check if the "tags" array contains all of the values: "SciFi", "Adventure", and the value from field "tag1"
    arrayContainsAll(field("tags"), [field("tag1"), constant("SciFi"), "Adventure"]);
    

**Parameters**  
---  
**Name** | **Description**  
`array` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The array expression to check.  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_all' comparison.  
  
### Pipelines.arrayContainsAll(fieldName, arrayExpression)
    
    
    export declare function arrayContainsAll(fieldName: string, arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if a field's array value contains all the specified values or expressions.
    
    
    // Check if the 'tags' array contains both of the values from field 'tag1', the value "SciFi", and "Adventure"
    arrayContainsAll("tags", [field("tag1"), "SciFi", "Adventure"]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_all' comparison.  
  
### Pipelines.arrayContainsAny(array, values)
    
    
    export declare function arrayContainsAny(array: Expression, values: Array

Creates an expression that checks if an array expression contains any of the specified elements.
    
    
    // Check if the 'categories' array contains either values from field "cate1" or "Science"
    arrayContainsAny(field("categories"), [field("cate1"), "Science"]);
    

**Parameters**  
---  
**Name** | **Description**  
`array` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The array expression to check.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_any' comparison.  
  
### Pipelines.arrayContainsAny(fieldName, values)
    
    
    export declare function arrayContainsAny(fieldName: string, values: Array

Creates an expression that checks if a field's array value contains any of the specified elements.
    
    
    // Check if the 'groups' array contains either the value from the 'userGroup' field
    // or the value "guest"
    arrayContainsAny("categories", [field("cate1"), "Science"]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_any' comparison.  
  
### Pipelines.arrayContainsAny(array, values)
    
    
    export declare function arrayContainsAny(array: Expression, values: Expression): BooleanExpression;

Creates an expression that checks if an array expression contains any of the specified elements.
    
    
    // Check if the 'categories' array contains either values from field "cate1" or "Science"
    arrayContainsAny(field("categories"), array([field("cate1"), "Science"]));
    

**Parameters**  
---  
**Name** | **Description**  
`array` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The array expression to check.  
`values` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that evaluates to an array, whose elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_any' comparison.  
  
### Pipelines.arrayContainsAny(fieldName, values)
    
    
    export declare function arrayContainsAny(fieldName: string, values: Expression): BooleanExpression;

Creates an expression that checks if a field's array value contains any of the specified elements.
    
    
    // Check if the 'groups' array contains either the value from the 'userGroup' field
    // or the value "guest"
    arrayContainsAny("categories", array([field("cate1"), "Science"]));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`values` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that evaluates to an array, whose elements to check for in the array field.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_any' comparison.  
  
### Pipelines.arrayFilter(fieldName, alias, filter)
    
    
    export declare function arrayFilter(fieldName: string, alias: string, filter: BooleanExpression): FunctionExpression;

Creates an expression that filters an array using a provided alias and predicate expression.
    
    
    // Get a filtered array of the 'scores' field containing only elements greater than 50.
    arrayFilter("scores", "score", greaterThan(variable("score"), 50));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`alias` | `string`  
The variable name to use for each element.  
`filter` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The predicate boolean expression to evaluate for each element.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the filtered array.  
  
### Pipelines.arrayFilter(arrayExpression, alias, filter)
    
    
    export declare function arrayFilter(arrayExpression: Expression, alias: string, filter: BooleanExpression): FunctionExpression;

Creates an expression that filters an array using a provided alias and predicate expression.
    
    
    // Filter "scores" to include only values greater than 50
    arrayFilter(field("scores"), "score", greaterThan(variable("score"), 50));
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`alias` | `string`  
The variable name to use for each element.  
`filter` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The predicate boolean expression to evaluate for each element.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the filtered array.  
  
### Pipelines.arrayFirst(fieldName)
    
    
    export declare function arrayFirst(fieldName: string): FunctionExpression;

Creates an expression that returns the first element of an array.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first element.  
  
#### Example
    
    
    typescript
    // Get the first tag from the 'tags' array field
    arrayFirst("tags");
    

### Pipelines.arrayFirst(arrayExpression)
    
    
    export declare function arrayFirst(arrayExpression: Expression): FunctionExpression;

Creates an expression that returns the first element of an array.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first element.  
  
#### Example
    
    
    typescript
    // Get the first tag from the 'tags' array field
    arrayFirst(field("tags"));
    

### Pipelines.arrayFirstN(fieldName, n)
    
    
    export declare function arrayFirstN(fieldName: string, n: number): FunctionExpression;

Creates an expression that returns the first `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first `n` elements.  
  
#### Example
    
    
    typescript
    // Get the first 3 tags from the 'tags' array field
    arrayFirstN("tags", 3);
    

### Pipelines.arrayFirstN(fieldName, n)
    
    
    export declare function arrayFirstN(fieldName: string, n: Expression): FunctionExpression;

Creates an expression that returns the first `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first `n` elements.  
  
#### Example
    
    
    typescript
    // Get the first n tags from the 'tags' array field
    arrayFirstN("tags", field("count"));
    

### Pipelines.arrayFirstN(arrayExpression, n)
    
    
    export declare function arrayFirstN(arrayExpression: Expression, n: number): FunctionExpression;

Creates an expression that returns the first `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first `n` elements.  
  
#### Example
    
    
    typescript
    // Get the first 3 elements from an array expression
    arrayFirstN(field("tags"), 3);
    

### Pipelines.arrayFirstN(arrayExpression, n)
    
    
    export declare function arrayFirstN(arrayExpression: Expression, n: Expression): FunctionExpression;

Creates an expression that returns the first `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first `n` elements.  
  
#### Example
    
    
    typescript
    // Get the first n elements from an array expression
    arrayFirstN(field("tags"), field("count"));
    

### Pipelines.arrayGet(arrayField, index)
    
    
    export declare function arrayGet(arrayField: string, index: number): FunctionExpression;

Creates an expression that indexes into an array from the beginning or end and return the element. If the index exceeds the array length, an error is returned. A negative index, starts from the end.
    
    
    // Return the value in the tags field array at index 1.
    arrayGet('tags', 1);
    

**Parameters**  
---  
**Name** | **Description**  
`arrayField` | `string`  
The name of the array field.  
`index` | `number`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new Expression representing the 'arrayGet' operation.  
  
### Pipelines.arrayGet(arrayField, indexExpr)
    
    
    export declare function arrayGet(arrayField: string, indexExpr: Expression): FunctionExpression;

Creates an expression that indexes into an array from the beginning or end and return the element. If the index exceeds the array length, an error is returned. A negative index, starts from the end.
    
    
    // Return the value in the tags field array at index specified by field
    // 'favoriteTag'.
    arrayGet('tags', field('favoriteTag'));
    

**Parameters**  
---  
**Name** | **Description**  
`arrayField` | `string`  
The name of the array field.  
`indexExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An Expression evaluating to the index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new Expression representing the 'arrayGet' operation.  
  
### Pipelines.arrayGet(arrayExpression, index)
    
    
    export declare function arrayGet(arrayExpression: Expression, index: number): FunctionExpression;

Creates an expression that indexes into an array from the beginning or end and return the element. If the index exceeds the array length, an error is returned. A negative index, starts from the end.
    
    
    // Return the value in the tags field array at index 1.
    arrayGet(field('tags'), 1);
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An Expression evaluating to an array.  
`index` | `number`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new Expression representing the 'arrayGet' operation.  
  
### Pipelines.arrayGet(arrayExpression, indexExpr)
    
    
    export declare function arrayGet(arrayExpression: Expression, indexExpr: Expression): FunctionExpression;

Creates an expression that indexes into an array from the beginning or end and return the element. If the index exceeds the array length, an error is returned. A negative index, starts from the end.
    
    
    // Return the value in the tags field array at index specified by field
    // 'favoriteTag'.
    arrayGet(field('tags'), field('favoriteTag'));
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An Expression evaluating to an array.  
`indexExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An Expression evaluating to the index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new Expression representing the 'arrayGet' operation.  
  
### Pipelines.arrayIndexOf(fieldName, search)
    
    
    export declare function arrayIndexOf(fieldName: string, search: unknown | Expression): FunctionExpression;

Creates an expression that returns the first index of the search value in an array. Returns -1 if the value is not found.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array to search.  
`search` | `unknown | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
  
#### Example
    
    
    typescript
    // Get the index of "politics" in the 'tags' array field
    arrayIndexOf("tags", "politics");
    

### Pipelines.arrayIndexOf(arrayExpression, search)
    
    
    export declare function arrayIndexOf(arrayExpression: Expression, search: unknown | Expression): FunctionExpression;

Creates an expression that returns the first index of the search value in an array. Returns -1 if the value is not found.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array to search.  
`search` | `unknown | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
  
#### Example
    
    
    typescript
    // Get the index of "politics" in the 'tags' array field
    arrayIndexOf(field("tags"), "politics");
    

### Pipelines.arrayIndexOfAll(fieldName, search)
    
    
    export declare function arrayIndexOfAll(fieldName: string, search: unknown | Expression): FunctionExpression;

Creates an expression that returns all indices of the search value in an array.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array to search.  
`search` | `unknown | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the indices.  
  
#### Example
    
    
    typescript
    // Get all indices of 5 in the 'scores' array field
    arrayIndexOfAll("scores", 5);
    

### Pipelines.arrayIndexOfAll(arrayExpression, search)
    
    
    export declare function arrayIndexOfAll(arrayExpression: Expression, search: unknown | Expression): FunctionExpression;

Creates an expression that returns all indices of the search value in an array.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array to search.  
`search` | `unknown | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the indices.  
  
#### Example
    
    
    typescript
    // Get all indices of 5 in the 'scores' array field
    arrayIndexOfAll(field("scores"), 5);
    

### Pipelines.arrayLast(fieldName)
    
    
    export declare function arrayLast(fieldName: string): FunctionExpression;

Creates an expression that returns the last element of an array.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last element.  
  
#### Example
    
    
    typescript
    // Get the last tag from the 'tags' array field
    arrayLast("tags");
    

### Pipelines.arrayLast(arrayExpression)
    
    
    export declare function arrayLast(arrayExpression: Expression): FunctionExpression;

Creates an expression that returns the last element of an array.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last element.  
  
#### Example
    
    
    typescript
    // Get the last tag from the 'tags' array field
    arrayLast(field("tags"));
    

### Pipelines.arrayLastIndexOf(fieldName, search)
    
    
    export declare function arrayLastIndexOf(fieldName: string, search: unknown | Expression): FunctionExpression;

Creates an expression that returns the last index of the search value in an array. Returns -1 if the value is not found.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array to search.  
`search` | `unknown | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
  
#### Example
    
    
    typescript
    // Get the last index of "politics" in the 'tags' array field
    arrayLastIndexOf("tags", "politics");
    

### Pipelines.arrayLastIndexOf(arrayExpression, search)
    
    
    export declare function arrayLastIndexOf(arrayExpression: Expression, search: unknown | Expression): FunctionExpression;

Creates an expression that returns the last index of the search value in an array. Returns -1 if the value is not found.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array to search.  
`search` | `unknown | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
  
#### Example
    
    
    typescript
    // Get the last index of "politics" in the 'tags' array field
    arrayLastIndexOf(field("tags"), "politics");
    

### Pipelines.arrayLastN(fieldName, n)
    
    
    export declare function arrayLastN(fieldName: string, n: number): FunctionExpression;

Creates an expression that returns the last `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last `n` elements.  
  
#### Example
    
    
    typescript
    // Get the last 3 tags from the 'tags' array field
    arrayLastN("tags", 3);
    

### Pipelines.arrayLastN(fieldName, n)
    
    
    export declare function arrayLastN(fieldName: string, n: Expression): FunctionExpression;

Creates an expression that returns the last `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last `n` elements.  
  
#### Example
    
    
    typescript
    // Get the last n tags from the 'tags' array field
    arrayLastN("tags", field("count"));
    

### Pipelines.arrayLastN(arrayExpression, n)
    
    
    export declare function arrayLastN(arrayExpression: Expression, n: number): FunctionExpression;

Creates an expression that returns the last `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last `n` elements.  
  
#### Example
    
    
    typescript
    // Get the last 3 elements from an array expression
    arrayLastN(field("tags"), 3);
    

### Pipelines.arrayLastN(arrayExpression, n)
    
    
    export declare function arrayLastN(arrayExpression: Expression, n: Expression): FunctionExpression;

Creates an expression that returns the last `n` elements of an array.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last `n` elements.  
  
#### Example
    
    
    typescript
    // Get the last n elements from an array expression
    arrayLastN(field("tags"), field("count"));
    

### Pipelines.arrayLength(fieldName)
    
    
    export declare function arrayLength(fieldName: string): FunctionExpression;

Creates an expression that calculates the length of an array in a specified field.
    
    
    // Get the number of items in field 'cart'
    arrayLength('cart');
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing an array to calculate the length of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the array.  
  
### Pipelines.arrayLength(array)
    
    
    export declare function arrayLength(array: Expression): FunctionExpression;

Creates an expression that calculates the length of an array expression.
    
    
    // Get the number of items in the 'cart' array
    arrayLength(field("cart"));
    

**Parameter**  
---  
**Name** | **Description**  
`array` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The array expression to calculate the length of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the array.  
  
### Pipelines.arrayMaximum(fieldName)
    
    
    export declare function arrayMaximum(fieldName: string): FunctionExpression;

Creates an expression that returns the maximum value in an array.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the maximum value.  
  
#### Example
    
    
    typescript
    // Get the maximum value from the 'scores' array field
    arrayMaximum("scores");
    

### Pipelines.arrayMaximum(arrayExpression)
    
    
    export declare function arrayMaximum(arrayExpression: Expression): FunctionExpression;

Creates an expression that returns the maximum value in an array.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the maximum value.  
  
#### Example
    
    
    typescript
    // Get the maximum value from the 'scores' array field
    arrayMaximum(field("scores"));
    

### Pipelines.arrayMaximumN(fieldName, n)
    
    
    export declare function arrayMaximumN(fieldName: string, n: number): FunctionExpression;

Creates an expression that returns the largest `n` elements of an array.

Note: Returns the n largest non-null elements in the array, in descending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the largest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the top 3 scores from the 'scores' array field
    arrayMaximumN("scores", 3);
    

### Pipelines.arrayMaximumN(fieldName, n)
    
    
    export declare function arrayMaximumN(fieldName: string, n: Expression): FunctionExpression;

Creates an expression that returns the largest `n` elements of an array.

Note: Returns the n largest non-null elements in the array, in descending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the largest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the top n scores from the 'scores' array field
    arrayMaximumN("scores", field("count"));
    

### Pipelines.arrayMaximumN(arrayExpression, n)
    
    
    export declare function arrayMaximumN(arrayExpression: Expression, n: number): FunctionExpression;

Creates an expression that returns the largest `n` elements of an array.

Note: Returns the n largest non-null elements in the array, in descending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the largest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the top 3 elements from an array expression
    arrayMaximumN(field("scores"), 3);
    

### Pipelines.arrayMaximumN(arrayExpression, n)
    
    
    export declare function arrayMaximumN(arrayExpression: Expression, n: Expression): FunctionExpression;

Creates an expression that returns the largest `n` elements of an array.

Note: Returns the n largest non-null elements in the array, in descending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the largest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the top n elements from an array expression
    arrayMaximumN(field("scores"), field("count"));
    

### Pipelines.arrayMinimum(fieldName)
    
    
    export declare function arrayMinimum(fieldName: string): FunctionExpression;

Creates an expression that returns the minimum value in an array.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the minimum value.  
  
#### Example
    
    
    typescript
    // Get the minimum value from the 'scores' array field
    arrayMinimum("scores");
    

### Pipelines.arrayMinimum(arrayExpression)
    
    
    export declare function arrayMinimum(arrayExpression: Expression): FunctionExpression;

Creates an expression that returns the minimum value in an array.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the minimum value.  
  
#### Example
    
    
    typescript
    // Get the minimum value from the 'scores' array field
    arrayMinimum(field("scores"));
    

### Pipelines.arrayMinimumN(fieldName, n)
    
    
    export declare function arrayMinimumN(fieldName: string, n: number): FunctionExpression;

Creates an expression that returns the smallest `n` elements of an array.

Note: Returns the n smallest non-null elements in the array, in ascending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the smallest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the bottom 3 scores from the 'scores' array field
    arrayMinimumN("scores", 3);
    

### Pipelines.arrayMinimumN(fieldName, n)
    
    
    export declare function arrayMinimumN(fieldName: string, n: Expression): FunctionExpression;

Creates an expression that returns the smallest `n` elements of an array.

Note: Returns the n smallest non-null elements in the array, in ascending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the smallest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the bottom n scores from the 'scores' array field
    arrayMinimumN(field("scores"), field("count"));
    

### Pipelines.arrayMinimumN(arrayExpression, n)
    
    
    export declare function arrayMinimumN(arrayExpression: Expression, n: number): FunctionExpression;

Creates an expression that returns the smallest `n` elements of an array.

Note: Returns the n smallest non-null elements in the array, in ascending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `number`  
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the smallest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the bottom 3 scores from the 'scores' array field
    arrayMinimumN(field("scores"), 3);
    

### Pipelines.arrayMinimumN(arrayExpression, n)
    
    
    export declare function arrayMinimumN(arrayExpression: Expression, n: Expression): FunctionExpression;

Creates an expression that returns the smallest `n` elements of an array.

Note: Returns the n smallest non-null elements in the array, in ascending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`n` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the smallest `n` elements.  
  
#### Example
    
    
    typescript
    // Get the bottom n scores from the 'scores' array field
    arrayMinimumN(field("scores"), field("count"));
    

### Pipelines.arrayReverse(fieldName)
    
    
    export declare function arrayReverse(fieldName: string): FunctionExpression;

Creates an expression that reverses an array.
    
    
    // Reverse the value of the 'myArray' field.
    arrayReverse("myArray");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to reverse.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed array.  
  
### Pipelines.arrayReverse(arrayExpression)
    
    
    export declare function arrayReverse(arrayExpression: Expression): FunctionExpression;

Creates an expression that reverses an array.
    
    
    // Reverse the value of the 'myArray' field.
    arrayReverse(field("myArray"));
    

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to an array value, which will be reversed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed array.  
  
### Pipelines.arraySlice(arrayName, offset, length)
    
    
    export declare function arraySlice(arrayName: string, offset: number | Expression, length?: number | Expression): FunctionExpression;

Creates an expression that returns a slice of an array from `offset` with `length` elements.
    
    
    // Get 5 elements from the 'items' array field starting from index 2
    arraySlice("items", 2, 5);
    
    // Get n elements from the 'items' array field starting from index 2
    arraySlice("items", 2, field("length"));
    

**Parameters**  
---  
**Name** | **Description**  
`arrayName` | `string`  
The name of the field containing the array.  
`offset` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The starting offset.  
`length` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The optional length of the slice.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the sliced array.  
  
### Pipelines.arraySlice(arrayExpression, offset, length)
    
    
    export declare function arraySlice(arrayExpression: Expression, offset: number | Expression, length?: number | Expression): FunctionExpression;

Creates an expression that returns a slice of an array from `offset` with `length` elements.
    
    
    // Get 5 elements from an array expression starting from index 2
    arraySlice(field("items"), 2, 5);
    
    // Get n elements from an array expression starting from index 2
    arraySlice(field("items"), 2, field("length"));
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`offset` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The starting offset.  
`length` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The optional length of the slice.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the sliced array.  
  
### Pipelines.arraySum(fieldName)
    
    
    export declare function arraySum(fieldName: string): FunctionExpression;

Creates an expression that computes the sum of the elements in an array.
    
    
    // Compute the sum of the elements in the 'scores' field.
    arraySum("scores");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to compute the sum of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the sum of the elements in the array.  
  
### Pipelines.arraySum(expression)
    
    
    export declare function arraySum(expression: Expression): FunctionExpression;

Creates an expression that computes the sum of the elements in an array.
    
    
    // Compute the sum of the elements in the 'scores' field.
    arraySum(field("scores"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric array, which the sum will be computed for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the sum of the elements in the array.  
  
### Pipelines.arrayTransform(fieldName, elementAlias, transform)
    
    
    export declare function arrayTransform(fieldName: string, elementAlias: string, transform: Expression): FunctionExpression;

Creates an expression that applies a provided transformation to each element in an array.
    
    
    // Transform "scores" array by multiplying each score by 10
    arrayTransform("scores", "score", multiply(variable("score"), 10));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`elementAlias` | `string`  
The variable name to use for each element.  
`transform` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The lambda expression used to transform the elements.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the transformed array.  
  
### Pipelines.arrayTransform(arrayExpression, elementAlias, transform)
    
    
    export declare function arrayTransform(arrayExpression: Expression, elementAlias: string, transform: Expression): FunctionExpression;

Creates an expression that applies a provided transformation to each element in an array.
    
    
    // Transform "scores" array by multiplying each score by 10
    arrayTransform(field("scores"), "score", multiply(variable("score"), 10));
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`elementAlias` | `string`  
The variable name to use for each element.  
`transform` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The lambda expression used to transform the elements.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the transformed array.  
  
### Pipelines.arrayTransformWithIndex(fieldName, elementAlias, indexAlias, transform)
    
    
    export declare function arrayTransformWithIndex(fieldName: string, elementAlias: string, indexAlias: string, transform: Expression): FunctionExpression;

Creates an expression that applies a provided transformation to each element in an array, providing the element's index to the transformation expression.
    
    
    // Transform "scores" array by adding the index to each score
    arrayTransformWithIndex("scores", "score", "i", add(variable("score"), variable("i")));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the array.  
`elementAlias` | `string`  
The variable name to use for each element.  
`indexAlias` | `string`  
The variable name to use for the current index.  
`transform` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The lambda expression used to transform the elements.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the transformed array.  
  
### Pipelines.arrayTransformWithIndex(arrayExpression, elementAlias, indexAlias, transform)
    
    
    export declare function arrayTransformWithIndex(arrayExpression: Expression, elementAlias: string, indexAlias: string, transform: Expression): FunctionExpression;

Creates an expression that applies a provided transformation to each element in an array, providing the element's index to the transformation expression.
    
    
    // Transform "scores" array by adding the index to each score
    arrayTransformWithIndex(field("scores"), "score", "i", add(variable("score"), variable("i")));
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the array.  
`elementAlias` | `string`  
The variable name to use for each element.  
`indexAlias` | `string`  
The variable name to use for the current index.  
`transform` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression used to transform the elements.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the transformed array.  
  
### Pipelines.ascending(expr)
    
    
    export declare function ascending(expr: Expression): Ordering;

Creates a `Field` instance representing the field at the given path.
    
    
    // Sort documents by the 'name' field in lowercase in ascending order
    db.pipeline().collection("users")
      .sort(ascending(field("name").toLower()));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to create an ascending ordering for.  
**Returns**  
---  
**Type** | **Description**  
`[Ordering](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.ordering)` | A new `Ordering` for ascending sorting.  
  
### Pipelines.ascending(fieldName)
    
    
    export declare function ascending(fieldName: string): Ordering;

Creates an `Ordering` that sorts documents in ascending order based on a field.
    
    
    // Sort documents by the 'name' field in ascending order
    db.pipeline().collection("users")
      .sort(ascending("name"));
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field to create an ascending ordering for.  
**Returns**  
---  
**Type** | **Description**  
`[Ordering](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.ordering)` | A new `Ordering` for ascending sorting.  
  
### Pipelines.average(expression)
    
    
    export declare function average(expression: Expression): AggregateFunction;

Creates an aggregation that calculates the average (mean) of values from an expression across multiple stage inputs.
    
    
    // Calculate the average age of users
    average(field("age")).as("averageAge");
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the values to average.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'average' aggregation.  
  
### Pipelines.average(fieldName)
    
    
    export declare function average(fieldName: string): AggregateFunction;

Creates an aggregation that calculates the average (mean) of a field's values across multiple stage inputs.
    
    
    // Calculate the average age of users
    average("age").as("averageAge");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing numeric values to average.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'average' aggregation.  
  
### Pipelines.byteLength(expr)
    
    
    export declare function byteLength(expr: Expression): FunctionExpression;

Creates an expression that calculates the byte length of a string in UTF-8, or just the length of a Blob.
    
    
    // Calculate the length of the 'myString' field in bytes.
    byteLength(field("myString"));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string in bytes.  
  
### Pipelines.byteLength(fieldName)
    
    
    export declare function byteLength(fieldName: string): FunctionExpression;

Creates an expression that calculates the length of a string represented by a field in UTF-8 bytes, or just the length of a Blob.
    
    
    // Calculate the length of the 'myString' field in bytes.
    byteLength("myString");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string in bytes.  
  
### Pipelines.ceil(fieldName)
    
    
    export declare function ceil(fieldName: string): FunctionExpression;

Creates an expression that computes the ceiling of a numeric value.
    
    
    // Compute the ceiling of the 'price' field.
    ceil("price");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to compute the ceiling of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the ceiling of the numeric value.  
  
### Pipelines.ceil(expression)
    
    
    export declare function ceil(expression: Expression): FunctionExpression;

Creates an expression that computes the ceiling of a numeric value.
    
    
    // Compute the ceiling of the 'price' field.
    ceil(field("price"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which the ceiling will be computed for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the ceiling of the numeric value.  
  
### Pipelines.charLength(fieldName)
    
    
    export declare function charLength(fieldName: string): FunctionExpression;

Creates an expression that calculates the character length of a string field in UTF8.
    
    
    // Get the character length of the 'name' field in UTF-8.
    strLength("name");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string.  
  
### Pipelines.charLength(stringExpression)
    
    
    export declare function charLength(stringExpression: Expression): FunctionExpression;

Creates an expression that calculates the character length of a string expression in UTF-8.
    
    
    // Get the character length of the 'name' field in UTF-8.
    strLength(field("name"));
    

**Parameter**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to calculate the length of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string.  
  
### Pipelines.coalesce(expression, replacement, others)
    
    
    export declare function coalesce(expression: Expression, replacement: Expression | unknown, ...others: Array

Creates an expression that returns the first non-null, non-absent argument, without evaluating the rest of the arguments. When all arguments are null or absent, returns the last argument.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to check for null.  
`replacement` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The fallback expression or value if the first one is null.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Optional additional expressions to check if previous ones are null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the coalesce operation.  
  
#### Example
    
    
    typescript
    // Returns the value of the first non-null, non-absent field among 'preferredName', 'fullName',
    // or the last argument if all previous fields are null.
    coalesce(field("preferredName"), field("fullName"), constant("Anonymous"))
    

### Pipelines.coalesce(fieldName, replacement, others)
    
    
    export declare function coalesce(fieldName: string, replacement: Expression | unknown, ...others: Array

Creates an expression that returns the first non-null, non-absent argument, without evaluating the rest of the arguments. When all arguments are null or absent, returns the last argument.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the first field to check for null.  
`replacement` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The fallback expression or value if the first one is null.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Optional additional expressions to check if previous ones are null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the coalesce operation.  
  
#### Example
    
    
    typescript
    // Returns the value of the first non-null, non-absent field among 'preferredName', 'fullName',
    // or the last argument if all previous fields are null.
    coalesce("preferredName", field("fullName"), constant("Anonymous"))
    

### Pipelines.collectionId(fieldName)
    
    
    export declare function collectionId(fieldName: string): FunctionExpression;

Creates an expression that returns the collection ID from a path.
    
    
    // Get the collection ID from a path.
    collectionId("__name__");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to get the collection ID from.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the collectionId operation.  
  
### Pipelines.collectionId(expression)
    
    
    export declare function collectionId(expression: Expression): FunctionExpression;

Creates an expression that returns the collection ID from a path.
    
    
    // Get the collection ID from a path.
    collectionId(field("__name__"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a path, which the collection ID will be extracted from.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the collectionId operation.  
  
### Pipelines.concat(first, second, others)
    
    
    export declare function concat(first: Expression, second: Expression | unknown, ...others: Array

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.
    
    
    // Concatenate the 'firstName' and 'lastName' fields with a space in between.
    concat(field("firstName"), " ", field("lastName"))
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expressions to concatenate.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second literal or expression to concatenate.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Additional literals or expressions to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the concatenation.  
  
### Pipelines.concat(fieldName, second, others)
    
    
    export declare function concat(fieldName: string, second: Expression | unknown, ...others: Array

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.
    
    
    // Concatenate a field with a literal string.
    concat(field("firstName"), "Doe")
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of a field to concatenate.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second literal or expression to concatenate.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Additional literal or expressions to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the concatenation.  
  
### Pipelines.conditional(condition, thenExpr, elseExpr)
    
    
    export declare function conditional(condition: BooleanExpression, thenExpr: Expression, elseExpr: Expression): FunctionExpression;

Creates a conditional expression that evaluates to a 'then' expression if a condition is true and an 'else' expression if the condition is false.
    
    
    // If 'age' is greater than 18, return "Adult"; otherwise, return "Minor".
    conditional(
        greaterThan("age", 18), constant("Adult"), constant("Minor"));
    

**Parameters**  
---  
**Name** | **Description**  
`condition` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The condition to evaluate.  
`thenExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to evaluate if the condition is true.  
`elseExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to evaluate if the condition is false.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the conditional expression.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: number): Expression;

Creates an 'Expression' instance for a number value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `number`  
The number value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: firestore.VectorValue): Expression;

Creates an 'Expression' instance for a VectorValue value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `firestore.VectorValue`  
The VectorValue value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: string): Expression;

Creates an 'Expression' instance for a string value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `string`  
The string value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: boolean): BooleanExpression;

Creates an 'Expression' instance for a boolean value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `boolean`  
The boolean value.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: null): Expression;

Creates an 'Expression' instance for a null value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `null`  
The null value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: firestore.GeoPoint): Expression;

Creates an 'Expression' instance for a GeoPoint value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `firestore.GeoPoint`  
The GeoPoint value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: firestore.Timestamp): Expression;

Creates an 'Expression' instance for a Timestamp value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `firestore.Timestamp`  
The Timestamp value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: Date): Expression;

Creates an 'Expression' instance for a Date value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `Date`  
The Date value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: Buffer | Uint8Array): Expression;

Creates an 'Expression' instance for a Buffer | Uint8Array value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `"\"buffer\"".__global.Buffer | Uint8Array`  
The Buffer | Uint8Array value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.constant(value)
    
    
    export declare function constant(value: firestore.DocumentReference): Expression;

Creates an 'Expression' instance for a DocumentReference value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `firestore.DocumentReference`  
The DocumentReference value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` instance.  
  
### Pipelines.cosineDistance(fieldName, vector)
    
    
    export declare function cosineDistance(fieldName: string, vector: number[] | VectorValue): FunctionExpression;

Calculates the Cosine distance between a field's vector value and a literal vector value.
    
    
    // Calculate the Cosine distance between the 'location' field and a target location
    cosineDistance("location", [37.7749, -122.4194]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the first vector.  
`vector` | `number[] | [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)`  
The other vector (as an array of doubles) or [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Cosine distance between the two vectors.  
  
### Pipelines.cosineDistance(fieldName, vectorExpression)
    
    
    export declare function cosineDistance(fieldName: string, vectorExpression: Expression): FunctionExpression;

Calculates the Cosine distance between a field's vector value and a vector expression.
    
    
    // Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
    cosineDistance("userVector", field("itemVector"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the first vector.  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The other vector (represented as an Expression) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the cosine distance between the two vectors.  
  
### Pipelines.cosineDistance(vectorExpression, vector)
    
    
    export declare function cosineDistance(vectorExpression: Expression, vector: number[] | VectorValue): FunctionExpression;

Calculates the Cosine distance between a vector expression and a vector literal.
    
    
    // Calculate the cosine distance between the 'location' field and a target location
    cosineDistance(field("location"), [37.7749, -122.4194]);
    

**Parameters**  
---  
**Name** | **Description**  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first vector (represented as an Expression) to compare against.  
`vector` | `number[] | [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)`  
The other vector (as an array of doubles or VectorValue) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the cosine distance between the two vectors.  
  
### Pipelines.cosineDistance(vectorExpression, otherVectorExpression)
    
    
    export declare function cosineDistance(vectorExpression: Expression, otherVectorExpression: Expression): FunctionExpression;

Calculates the Cosine distance between two vector expressions.
    
    
    // Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
    cosineDistance(field("userVector"), field("itemVector"));
    

**Parameters**  
---  
**Name** | **Description**  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first vector (represented as an Expression) to compare against.  
`otherVectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The other vector (represented as an Expression) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the cosine distance between the two vectors.  
  
### Pipelines.count(expression)
    
    
    export declare function count(expression: Expression): AggregateFunction;

Creates an aggregation that counts the number of stage inputs with valid evaluations of the provided expression.
    
    
    // Count the number of items where the price is greater than 10
    count(field("price").greaterThan(10)).as("expensiveItemCount");
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to count.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'count' aggregation.  
  
### Pipelines.count(fieldName)
    
    
    export declare function count(fieldName: string): AggregateFunction;

Creates an aggregation that counts the number of stage inputs where the input field exists.
    
    
    // Count the total number of products
    count("productId").as("totalProducts");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to count.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'count' aggregation.  
  
### Pipelines.countAll()
    
    
    export declare function countAll(): AggregateFunction;

Creates an aggregation that counts the total number of stage inputs.
    
    
    // Count the total number of input documents
    countAll().as("totalDocument");
    

**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'countAll' aggregation.  
  
### Pipelines.countDistinct(expr)
    
    
    export declare function countDistinct(expr: Expression | string): AggregateFunction;

Creates an aggregation that counts the number of distinct values of a field.

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | string`  
The expression or field to count distinct values of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'count_distinct' aggregation.  
  
### Pipelines.countIf(booleanExpr)
    
    
    export declare function countIf(booleanExpr: BooleanExpression): AggregateFunction;

Creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true.
    
    
    // Count the number of documents where 'is_active' field equals true
    countIf(field("is_active").equal(true)).as("numActiveDocuments");
    

**Parameter**  
---  
**Name** | **Description**  
`booleanExpr` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The boolean expression to evaluate on each input.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'countIf' aggregation.  
  
### Pipelines.currentDocument()
    
    
    export declare function currentDocument(): Expression;

Creates an expression that represents the current document being processed.

**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | An `Expression` representing the current document.  
  
#### Example
    
    
    typescript
    // Define the current document as a variable "doc"
    firestore.pipeline().collection("books")
        .define(currentDocument().as("doc"))
        // Access a field from the defined document variable
        .select(variable("doc").getField("title"));
    

### Pipelines.currentTimestamp()
    
    
    export declare function currentTimestamp(): FunctionExpression;

Creates an expression that evaluates to the current server timestamp.
    
    
    // Get the current server timestamp
    currentTimestamp()
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new Expression representing the current server timestamp.  
  
### Pipelines.descending(expr)
    
    
    export declare function descending(expr: Expression): Ordering;

Creates an `Ordering` that sorts documents in descending order based on an expression.
    
    
    // Sort documents by the 'name' field in lowercase in descending order
    db.pipeline().collection("users")
      .sort(descending(field("name").toLower()));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to create a descending ordering for.  
**Returns**  
---  
**Type** | **Description**  
`[Ordering](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.ordering)` | A new `Ordering` for descending sorting.  
  
### Pipelines.descending(fieldName)
    
    
    export declare function descending(fieldName: string): Ordering;

Creates an `Ordering` that sorts documents in descending order based on a field.
    
    
    // Sort documents by the 'name' field in descending order
    db.pipeline().collection("users")
      .sort(descending("name"));
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field to create a descending ordering for.  
**Returns**  
---  
**Type** | **Description**  
`[Ordering](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.ordering)` | A new `Ordering` for descending sorting.  
  
### Pipelines.divide(dividend, divisort)
    
    
    export declare function divide(dividend: Expression, divisort: Expression): FunctionExpression;

Creates an expression that divides two expressions.
    
    
    // Divide the 'total' field by the 'count' field
    divide(field("total"), field("count"));
    

**Parameters**  
---  
**Name** | **Description**  
`dividend` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to be divided.  
`divisort` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the division operation.  
  
### Pipelines.divide(dividend, divisor)
    
    
    export declare function divide(dividend: Expression, divisor: unknown): FunctionExpression;

Creates an expression that divides an expression by a constant value.
    
    
    // Divide the 'value' field by 10
    divide(field("value"), 10);
    

**Parameters**  
---  
**Name** | **Description**  
`dividend` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to be divided.  
`divisor` | `unknown`  
The constant value to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the division operation.  
  
### Pipelines.divide(dividend, divisor)
    
    
    export declare function divide(dividend: string, divisor: Expression): FunctionExpression;

Creates an expression that divides a field's value by an expression.
    
    
    // Divide the 'total' field by the 'count' field
    divide("total", field("count"));
    

**Parameters**  
---  
**Name** | **Description**  
`dividend` | `string`  
The field name to be divided.  
`divisor` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the division operation.  
  
### Pipelines.divide(dividend, divisor)
    
    
    export declare function divide(dividend: string, divisor: unknown): FunctionExpression;

Creates an expression that divides a field's value by a constant value.
    
    
    // Divide the 'value' field by 10
    divide("value", 10);
    

**Parameters**  
---  
**Name** | **Description**  
`dividend` | `string`  
The field name to be divided.  
`divisor` | `unknown`  
The constant value to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the division operation.  
  
### Pipelines.documentId(documentPath)
    
    
    export declare function documentId(documentPath: string | firestore.DocumentReference): FunctionExpression;

Creates an expression that returns the document ID from a path.
    
    
    // Get the document ID from a path.
    documentId(myDocumentReference);
    

**Parameter**  
---  
**Name** | **Description**  
`documentPath` | `string | FirebaseFirestore.DocumentReference`  
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the documentId operation.  
  
### Pipelines.documentId(documentPathExpr)
    
    
    export declare function documentId(documentPathExpr: Expression): FunctionExpression;

Creates an expression that returns the document ID from a path.
    
    
    // Get the document ID from a path.
    documentId(field("__path__"));
    

**Parameter**  
---  
**Name** | **Description**  
`documentPathExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the documentId operation.  
  
### Pipelines.documentMatches(rquery)
    
    
    export declare function documentMatches(rquery: string | Expression): BooleanExpression;

Perform a full-text search on the document.

**Parameter**  
---  
**Name** | **Description**  
`rquery` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Define the search query using the search domain-specific language (DSL).  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A `BooleanExpression` representing the documentMatches function.  
**Remarks**

This Expression can only be used within a `search` stage.

### Pipelines.dotProduct(fieldName, vector)
    
    
    export declare function dotProduct(fieldName: string, vector: number[] | VectorValue): FunctionExpression;

Calculates the dot product between a field's vector value and a double array.
    
    
    // Calculate the dot product distance between a feature vector and a target vector
    dotProduct("features", [0.5, 0.8, 0.2]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the first vector.  
`vector` | `number[] | [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)`  
The other vector (as an array of doubles or VectorValue) to calculate with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the dot product between the two vectors.  
  
### Pipelines.dotProduct(fieldName, vectorExpression)
    
    
    export declare function dotProduct(fieldName: string, vectorExpression: Expression): FunctionExpression;

Calculates the dot product between a field's vector value and a vector expression.
    
    
    // Calculate the dot product distance between two document vectors: 'docVector1' and 'docVector2'
    dotProduct("docVector1", field("docVector2"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the first vector.  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The other vector (represented as an Expression) to calculate with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the dot product between the two vectors.  
  
### Pipelines.dotProduct(vectorExpression, vector)
    
    
    export declare function dotProduct(vectorExpression: Expression, vector: number[] | VectorValue): FunctionExpression;

Calculates the dot product between a vector expression and a double array.
    
    
    // Calculate the dot product between a feature vector and a target vector
    dotProduct(field("features"), [0.5, 0.8, 0.2]);
    

**Parameters**  
---  
**Name** | **Description**  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first vector (represented as an Expression) to calculate with.  
`vector` | `number[] | [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)`  
The other vector (as an array of doubles or VectorValue) to calculate with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the dot product between the two vectors.  
  
### Pipelines.dotProduct(vectorExpression, otherVectorExpression)
    
    
    export declare function dotProduct(vectorExpression: Expression, otherVectorExpression: Expression): FunctionExpression;

Calculates the dot product between two vector expressions.
    
    
    // Calculate the dot product between two document vectors: 'docVector1' and 'docVector2'
    dotProduct(field("docVector1"), field("docVector2"));
    

**Parameters**  
---  
**Name** | **Description**  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first vector (represented as an Expression) to calculate with.  
`otherVectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The other vector (represented as an Expression) to calculate with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the dot product between the two vectors.  
  
### Pipelines.endsWith(fieldName, suffix)
    
    
    export declare function endsWith(fieldName: string, suffix: string): BooleanExpression;

Creates an expression that checks if a field's value ends with a given postfix.
    
    
    // Check if the 'filename' field ends with ".txt"
    endsWith("filename", ".txt");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`suffix` | `string`  
The postfix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'ends with' comparison.  
  
### Pipelines.endsWith(fieldName, suffix)
    
    
    export declare function endsWith(fieldName: string, suffix: Expression): BooleanExpression;

Creates an expression that checks if a field's value ends with a given postfix.
    
    
    // Check if the 'url' field ends with the value of the 'extension' field
    endsWith("url", field("extension"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`suffix` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the postfix.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'ends with' comparison.  
  
### Pipelines.endsWith(stringExpression, suffix)
    
    
    export declare function endsWith(stringExpression: Expression, suffix: string): BooleanExpression;

Creates an expression that checks if a string expression ends with a given postfix.
    
    
    // Check if the result of concatenating 'firstName' and 'lastName' fields ends with "Jr."
    endsWith(field("fullName"), "Jr.");
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check.  
`suffix` | `string`  
The postfix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'ends with' comparison.  
  
### Pipelines.endsWith(stringExpression, suffix)
    
    
    export declare function endsWith(stringExpression: Expression, suffix: Expression): BooleanExpression;

Creates an expression that checks if a string expression ends with a given postfix.
    
    
    // Check if the result of concatenating 'firstName' and 'lastName' fields ends with "Jr."
    endsWith(field("fullName"), constant("Jr."));
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check.  
`suffix` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The postfix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'ends with' comparison.  
  
### Pipelines.equal(left, right)
    
    
    export declare function equal(left: Expression, right: Expression): BooleanExpression;

Creates an expression that checks if two expressions are equal.
    
    
    // Check if the 'age' field is equal to an expression
    equal(field("age"), field("minAge").add(10));
    

**Parameters**  
---  
**Name** | **Description**  
`left` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to compare.  
`right` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The second expression to compare.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the equality comparison.  
  
### Pipelines.equal(expression, value)
    
    
    export declare function equal(expression: Expression, value: unknown): BooleanExpression;

Creates an expression that checks if an expression is equal to a constant value.
    
    
    // Check if the 'age' field is equal to 21
    equal(field("age"), 21);
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the equality comparison.  
  
### Pipelines.equal(fieldName, expression)
    
    
    export declare function equal(fieldName: string, expression: Expression): BooleanExpression;

Creates an expression that checks if a field's value is equal to an expression.
    
    
    // Check if the 'age' field is equal to the 'limit' field
    equal("age", field("limit"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the equality comparison.  
  
### Pipelines.equal(fieldName, value)
    
    
    export declare function equal(fieldName: string, value: unknown): BooleanExpression;

Creates an expression that checks if a field's value is equal to a constant value.
    
    
    // Check if the 'city' field is equal to string constant "London"
    equal("city", "London");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the equality comparison.  
  
### Pipelines.equalAny(expression, values)
    
    
    export declare function equalAny(expression: Expression, values: Array

Creates an expression that checks if an expression, when evaluated, is equal to any of the provided values or expressions.
    
    
    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    equalAny(field("category"), [constant("Electronics"), field("primaryType")]);
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression whose results to compare.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The values to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'IN' comparison.  
  
### Pipelines.equalAny(expression, arrayExpression)
    
    
    export declare function equalAny(expression: Expression, arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if an expression is equal to any of the provided values.
    
    
    // Check if the 'category' field is set to a value in the disabledCategories field
    equalAny(field("category"), field('disabledCategories'));
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression whose results to compare.  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that evaluates to an array, whose elements to check for equality to the input.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'IN' comparison.  
  
### Pipelines.equalAny(fieldName, values)
    
    
    export declare function equalAny(fieldName: string, values: Array

Creates an expression that checks if a field's value is equal to any of the provided values or expressions.
    
    
    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    equalAny("category", [constant("Electronics"), field("primaryType")]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field to compare.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The values to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'IN' comparison.  
  
### Pipelines.equalAny(fieldName, arrayExpression)
    
    
    export declare function equalAny(fieldName: string, arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if a field's value is equal to any of the provided values or expressions.
    
    
    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    equalAny("category", ["Electronics", field("primaryType")]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field to compare.  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that evaluates to an array, whose elements to check for equality to the input field.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'IN' comparison.  
  
### Pipelines.euclideanDistance(fieldName, vector)
    
    
    export declare function euclideanDistance(fieldName: string, vector: number[] | VectorValue): FunctionExpression;

Calculates the Euclidean distance between a field's vector value and a double array.
    
    
    // Calculate the Euclidean distance between the 'location' field and a target location
    euclideanDistance("location", [37.7749, -122.4194]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the first vector.  
`vector` | `number[] | [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)`  
The other vector (as an array of doubles or VectorValue) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Euclidean distance between the two vectors.  
  
### Pipelines.euclideanDistance(fieldName, vectorExpression)
    
    
    export declare function euclideanDistance(fieldName: string, vectorExpression: Expression): FunctionExpression;

Calculates the Euclidean distance between a field's vector value and a vector expression.
    
    
    // Calculate the Euclidean distance between two vector fields: 'pointA' and 'pointB'
    euclideanDistance("pointA", field("pointB"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the first vector.  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The other vector (represented as an Expression) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Euclidean distance between the two vectors.  
  
### Pipelines.euclideanDistance(vectorExpression, vector)
    
    
    export declare function euclideanDistance(vectorExpression: Expression, vector: number[] | VectorValue): FunctionExpression;

Calculates the Euclidean distance between a vector expression and a double array.
    
    
    // Calculate the Euclidean distance between the 'location' field and a target location
    
    euclideanDistance(field("location"), [37.7749, -122.4194]);
    

**Parameters**  
---  
**Name** | **Description**  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first vector (represented as an Expression) to compare against.  
`vector` | `number[] | [VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)`  
The other vector (as an array of doubles or VectorValue) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Euclidean distance between the two vectors.  
  
### Pipelines.euclideanDistance(vectorExpression, otherVectorExpression)
    
    
    export declare function euclideanDistance(vectorExpression: Expression, otherVectorExpression: Expression): FunctionExpression;

Calculates the Euclidean distance between two vector expressions.
    
    
    // Calculate the Euclidean distance between two vector fields: 'pointA' and 'pointB'
    euclideanDistance(field("pointA"), field("pointB"));
    

**Parameters**  
---  
**Name** | **Description**  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first vector (represented as an Expression) to compare against.  
`otherVectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The other vector (represented as an Expression) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Euclidean distance between the two vectors.  
  
### Pipelines.exists(value)
    
    
    export declare function exists(value: Expression): BooleanExpression;

Creates an expression that checks if a field exists.
    
    
    // Check if the document has a field named "phoneNumber"
    exists(field("phoneNumber"));
    

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluates to the name of the field to check.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'exists' check.  
  
### Pipelines.exists(fieldName)
    
    
    export declare function exists(fieldName: string): BooleanExpression;

Creates an expression that checks if a field exists.
    
    
    // Check if the document has a field named "phoneNumber"
    exists("phoneNumber");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'exists' check.  
  
### Pipelines.exp(expression)
    
    
    export declare function exp(expression: Expression): FunctionExpression;

Creates an expression that computes e to the power of the expression's result.
    
    
    // Compute e to the power of 2.
    exp(constant(2));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the exp of the numeric value.  
  
### Pipelines.exp(fieldName)
    
    
    export declare function exp(fieldName: string): FunctionExpression;

Creates an expression that computes e to the power of the expression's result.
    
    
    // Compute e to the power of the 'value' field.
    exp('value');
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the exp of the numeric value.  
  
### Pipelines.field(field)
    
    
    export declare function field(field: string | firestore.FieldPath): Field;

Creates a `Field` instance representing the field at the given path.

The path can be a simple field name (e.g., "name") or a dot-separated path to a nested field (e.g., "address.city").
    
    
    // Create a Field instance for the 'title' field
    const titleField = field("title");
    
    // Create a Field instance for a nested field 'author.firstName'
    const authorFirstNameField = field("author.firstName");
    

**Parameter**  
---  
**Name** | **Description**  
`field` | `string | FirebaseFirestore.FieldPath`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.Field](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.field)` | A new `Field` instance representing the specified field.  
  
### Pipelines.first(expression)
    
    
    export declare function first(expression: Expression): AggregateFunction;

Creates an aggregation that finds the first value of an expression across multiple stage inputs.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to find the first value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'first' aggregation.  
  
#### Example
    
    
    typescript
    // Find the first value of the 'rating' field
    first(field("rating")).as("firstRating");
    

### Pipelines.first(fieldName)
    
    
    export declare function first(fieldName: string): AggregateFunction;

Creates an aggregation that finds the first value of a field across multiple stage inputs.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to find the first value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'first' aggregation.  
  
#### Example
    
    
    typescript
    // Find the first value of the 'rating' field
    first("rating").as("firstRating");
    

### Pipelines.floor(expr)
    
    
    export declare function floor(expr: Expression): FunctionExpression;

Creates an expression that computes the floor of a numeric value.

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compute the floor of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the floor of the numeric value.  
  
### Pipelines.floor(fieldName)
    
    
    export declare function floor(fieldName: string): FunctionExpression;

Creates an expression that computes the floor of a numeric value.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to compute the floor of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the floor of the numeric value.  
  
### Pipelines.geoDistance(fieldName, location)
    
    
    export declare function geoDistance(fieldName: string | Field, location: GeoPoint | Expression): Expression;

Evaluates to the distance in meters between the location in the specified field and the query location.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string | [Field](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.field)`  
Specifies the field in the document which contains the first GeoPoint for distance computation.  
`location` | `[GeoPoint](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/geopoint) | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Compute distance to this GeoPoint.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | An `Expression` representing the geoDistance function.  
**Remarks**

This Expression can only be used within a `search` stage.

### Pipelines.getField(expression, key)
    
    
    export declare function getField(expression: Expression, key: string): Expression;

Creates an expression that gets a field from this map (object).

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluating to the map from which the field will be extracted.  
`key` | `string`  
The field to access in the document.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` representing the value of the field in the document.  
  
#### Example
    
    
    typescript
    // Get the value of the "city" field in the "address" document.
    getField(field("address"), "city")
    

### Pipelines.getField(expression, keyExpr)
    
    
    export declare function getField(expression: Expression, keyExpr: Expression): Expression;

Creates an expression that gets a field from this map (object).

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluating to the map from which the field will be extracted.  
`keyExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the key to access in the document.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` representing the value of the field in the document.  
  
#### Example
    
    
    typescript
    // Get the value of the "city" field in the "address" document.
    getField(field("address"), "city")
    

### Pipelines.getField(fieldName, key)
    
    
    export declare function getField(fieldName: string, key: string): Expression;

Creates an expression that returns the value of a field from the document with the given field name.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the map/document.  
`key` | `string`  
The key to access.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` representing the value of the field in the document.  
  
#### Example
    
    
    typescript
    // Get the value of the "city" field in the "address" document.
    getField("address", "city")
    

### Pipelines.getField(fieldName, keyExpr)
    
    
    export declare function getField(fieldName: string, keyExpr: Expression): Expression;

Creates an expression that returns the value of a field from the document with the given field name.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the map/document.  
`keyExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The key expression to access.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` representing the value of the field in the document.  
  
#### Example
    
    
    typescript
    // Get the value of the "city" field in the "address" document.
    getField("address", variable("addressField"))
    

### Pipelines.greaterThan(left, right)
    
    
    export declare function greaterThan(left: Expression, right: Expression): BooleanExpression;

Creates an expression that checks if the first expression is greater than the second expression.
    
    
    // Check if the 'age' field is greater than 18
    greaterThan(field("age"), Constant(9).add(9));
    

**Parameters**  
---  
**Name** | **Description**  
`left` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to compare.  
`right` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The second expression to compare.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than comparison.  
  
### Pipelines.greaterThan(expression, value)
    
    
    export declare function greaterThan(expression: Expression, value: unknown): BooleanExpression;

Creates an expression that checks if an expression is greater than a constant value.
    
    
    // Check if the 'age' field is greater than 18
    greaterThan(field("age"), 18);
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than comparison.  
  
### Pipelines.greaterThan(fieldName, expression)
    
    
    export declare function greaterThan(fieldName: string, expression: Expression): BooleanExpression;

Creates an expression that checks if a field's value is greater than an expression.
    
    
    // Check if the value of field 'age' is greater than the value of field 'limit'
    greaterThan("age", field("limit"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than comparison.  
  
### Pipelines.greaterThan(fieldName, value)
    
    
    export declare function greaterThan(fieldName: string, value: unknown): BooleanExpression;

Creates an expression that checks if a field's value is greater than a constant value.
    
    
    // Check if the 'price' field is greater than 100
    greaterThan("price", 100);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than comparison.  
  
### Pipelines.greaterThanOrEqual(left, right)
    
    
    export declare function greaterThanOrEqual(left: Expression, right: Expression): BooleanExpression;

Creates an expression that checks if the first expression is greater than or equal to the second expression.
    
    
    // Check if the 'quantity' field is greater than or equal to the field "threshold"
    greaterThanOrEqual(field("quantity"), field("threshold"));
    

**Parameters**  
---  
**Name** | **Description**  
`left` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to compare.  
`right` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The second expression to compare.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than or equal to comparison.  
  
### Pipelines.greaterThanOrEqual(expression, value)
    
    
    export declare function greaterThanOrEqual(expression: Expression, value: unknown): BooleanExpression;

Creates an expression that checks if an expression is greater than or equal to a constant value.
    
    
    // Check if the 'quantity' field is greater than or equal to 10
    greaterThanOrEqual(field("quantity"), 10);
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than or equal to comparison.  
  
### Pipelines.greaterThanOrEqual(fieldName, value)
    
    
    export declare function greaterThanOrEqual(fieldName: string, value: Expression): BooleanExpression;

Creates an expression that checks if a field's value is greater than or equal to an expression.
    
    
    // Check if the value of field 'age' is greater than or equal to the value of field 'limit'
    greaterThanOrEqual("age", field("limit"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`value` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than or equal to comparison.  
  
### Pipelines.greaterThanOrEqual(fieldName, value)
    
    
    export declare function greaterThanOrEqual(fieldName: string, value: unknown): BooleanExpression;

Creates an expression that checks if a field's value is greater than or equal to a constant value.
    
    
    // Check if the 'score' field is greater than or equal to 80
    greaterThanOrEqual("score", 80);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than or equal to comparison.  
  
### Pipelines.ifAbsent(ifExpr, elseExpr)
    
    
    export declare function ifAbsent(ifExpr: Expression, elseExpr: Expression): Expression;

Creates an expression that returns the `elseExpr` argument if `ifExpr` is absent, else return the result of the `ifExpr` argument evaluation.
    
    
    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    ifAbsent(field("optional_field"), constant("default_value"))
    

**Parameters**  
---  
**Name** | **Description**  
`ifExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check for absence.  
`elseExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression that will be evaluated and returned if [ifExpr] is absent.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the ifAbsent operation.  
  
### Pipelines.ifAbsent(ifExpr, elseValue)
    
    
    export declare function ifAbsent(ifExpr: Expression, elseValue: unknown): Expression;

Creates an expression that returns the `elseValue` argument if `ifExpr` is absent, else return the result of the `ifExpr` argument evaluation.
    
    
    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    ifAbsent(field("optional_field"), "default_value")
    

**Parameters**  
---  
**Name** | **Description**  
`ifExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check for absence.  
`elseValue` | `unknown`  
The value that will be returned if `ifExpr` evaluates to an absent value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new [Expression] representing the ifAbsent operation.  
  
### Pipelines.ifAbsent(ifFieldName, elseExpr)
    
    
    export declare function ifAbsent(ifFieldName: string, elseExpr: Expression): Expression;

Creates an expression that returns the `elseExpr` argument if `ifFieldName` is absent, else return the value of the field.
    
    
    // Returns the value of the optional field 'optional_field', or returns the value of
    // 'default_field' if 'optional_field' is absent.
    ifAbsent("optional_field", field("default_field"))
    

**Parameters**  
---  
**Name** | **Description**  
`ifFieldName` | `string`  
The field to check for absence.  
`elseExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression that will be evaluated and returned if `ifFieldName` is absent.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the ifAbsent operation.  
  
### Pipelines.ifAbsent(ifFieldName, elseValue)
    
    
    export declare function ifAbsent(ifFieldName: string | Expression, elseValue: Expression | unknown): Expression;

Creates an expression that returns the `elseValue` argument if `ifFieldName` is absent, else return the value of the field.
    
    
    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    ifAbsent("optional_field", "default_value")
    

**Parameters**  
---  
**Name** | **Description**  
`ifFieldName` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The field to check for absence.  
`elseValue` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The value that will be returned if [ifFieldName] is absent.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the ifAbsent operation.  
  
### Pipelines.ifError(tryExpr, catchExpr)
    
    
    export declare function ifError(tryExpr: BooleanExpression, catchExpr: BooleanExpression): BooleanExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation.

This overload is useful when a BooleanExpression is required.
    
    
    // Create an expression that protects against a divide by zero error
    // but always returns a boolean expression.
    ifError(constant(50).divide('length').gt(1), constant(false));
    

**Parameters**  
---  
**Name** | **Description**  
`tryExpr` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The try expression.  
`catchExpr` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The catch expression that will be evaluated and returned if the tryExpr produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expr` representing the 'ifError' operation.  
  
### Pipelines.ifError(tryExpr, catchExpr)
    
    
    export declare function ifError(tryExpr: Expression, catchExpr: Expression): FunctionExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation.
    
    
    // Returns the first item in the title field arrays, or returns
    // the entire title field if the array is empty or the field is another type.
    ifError(field("title").arrayGet(0), field("title"));
    

**Parameters**  
---  
**Name** | **Description**  
`tryExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The try expression.  
`catchExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The catch expression that will be evaluated and returned if the tryExpr produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the 'ifError' operation.  
  
### Pipelines.ifError(tryExpr, catchValue)
    
    
    export declare function ifError(tryExpr: Expression, catchValue: unknown): FunctionExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation.
    
    
    // Returns the first item in the title field arrays, or returns
    // "Default Title"
    ifError(field("title").arrayGet(0), "Default Title");
    

**Parameters**  
---  
**Name** | **Description**  
`tryExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The try expression.  
`catchValue` | `unknown`  
The value that will be returned if the tryExpr produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the 'ifError' operation.  
  
### Pipelines.ifNull(ifExpr, elseExpr)
    
    
    export declare function ifNull(ifExpr: Expression, elseExpr: Expression): FunctionExpression;

Creates an expression that returns the `elseExpr` argument if `ifExpr` is null, else return the result of the `ifExpr` argument evaluation.

**Parameters**  
---  
**Name** | **Description**  
`ifExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check for null.  
`elseExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression that will be evaluated and returned if `ifExpr` is null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the ifNull operation.  
**Remarks**

This function provides a fallback for both absent and explicit null values. In contrast, only triggers for missing fields.

#### Example
    
    
    typescript
    // Returns the user's preferred name, or if that is null, returns their full name.
    ifNull(field("preferredName"), field("fullName"))
    

### Pipelines.ifNull(ifExpr, elseValue)
    
    
    export declare function ifNull(ifExpr: Expression, elseValue: unknown): FunctionExpression;

Creates an expression that returns the `elseValue` argument if `ifExpr` is null, else return the result of the `ifExpr` argument evaluation.

**Parameters**  
---  
**Name** | **Description**  
`ifExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check for null.  
`elseValue` | `unknown`  
The value that will be returned if `ifExpr` evaluates to null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the ifNull operation.  
**Remarks**

This function provides a fallback for both absent and explicit null values. In contrast, only triggers for missing fields.

#### Example
    
    
    typescript
    // Returns the user's display name, or returns "Anonymous" if the field is null.
    ifNull(field("displayName"), "Anonymous")
    

### Pipelines.ifNull(ifFieldName, elseExpr)
    
    
    export declare function ifNull(ifFieldName: string, elseExpr: Expression): FunctionExpression;

Creates an expression that returns the `elseExpr` argument if `ifFieldName` is null, else return the value of the field.

**Parameters**  
---  
**Name** | **Description**  
`ifFieldName` | `string`  
The field to check for null.  
`elseExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression that will be evaluated and returned if `ifFieldName` is null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the ifNull operation.  
**Remarks**

This function provides a fallback for both absent and explicit null values. In contrast, only triggers for missing fields.

#### Example
    
    
    typescript
    // Returns the user's preferred name, or if that is null, returns their full name.
    ifNull("preferredName", field("fullName"))
    

### Pipelines.ifNull(ifFieldName, elseValue)
    
    
    export declare function ifNull(ifFieldName: string, elseValue: unknown): FunctionExpression;

Creates an expression that returns the `elseValue` argument if `ifFieldName` is null, else return the value of the field.

**Parameters**  
---  
**Name** | **Description**  
`ifFieldName` | `string`  
The field to check for null.  
`elseValue` | `unknown`  
The value that will be returned if `ifFieldName` is null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the ifNull operation.  
**Remarks**

This function provides a fallback for both absent and explicit null values. In contrast, only triggers for missing fields.

#### Example
    
    
    typescript
    // Returns the user's display name, or returns "Anonymous" if the field is null.
    ifNull("displayName", "Anonymous")
    

### Pipelines.isAbsent(value)
    
    
    export declare function isAbsent(value: Expression): BooleanExpression;

Creates an expression that returns `true` if a value is absent. Otherwise, returns `false` even if the value is `null`.
    
    
    // Check if the field `value` is absent.
    isAbsent(field("value"));
    

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'isAbsent' check.  
  
### Pipelines.isAbsent(field)
    
    
    export declare function isAbsent(field: string): BooleanExpression;

Creates an expression that returns `true` if a field is absent. Otherwise, returns `false` even if the field value is `null`.
    
    
    // Check if the field `value` is absent.
    isAbsent("value");
    

**Parameter**  
---  
**Name** | **Description**  
`field` | `string`  
The field to check.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'isAbsent' check.  
  
### Pipelines.isError(value)
    
    
    export declare function isError(value: Expression): BooleanExpression;

Creates an expression that checks if a given expression produces an error.
    
    
    // Check if the result of a calculation is an error
    isError(field("title").arrayContains(1));
    

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'isError' check.  
  
### Pipelines.isType(fieldName, type)
    
    
    export declare function isType(fieldName: string, type: string): BooleanExpression;

Creates an expression that checks if the value in the specified field is of the given type.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to check.  
`type` | `string`  
The type to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `BooleanExpression` that evaluates to true if the field's value is of the given type, false otherwise.  
**Remarks**

Null or undefined fields evaluate to skip/error. Use `ifAbsent()` / `isAbsent()` to evaluate missing data. Supported values for `type` are: `'null'`, `'array'`, `'boolean'`, `'bytes'`, `'timestamp'`, `'geo_point'`, `'number'`, `'int32'`, `'int64'`, `'float64'`, `'decimal128'`, `'map'`, `'reference'`, `'string'`, `'vector'`, `'max_key'`, `'min_key'`, `'object_id'`, `'regex'`, `'request_timestamp'`.

#### Example
    
    
    typescript
    // Check if the 'price' field is a floating point number (evaluating to true inside pipeline conditionals)
    isType('price', 'float64');
    

### Pipelines.isType(expression, type)
    
    
    export declare function isType(expression: Expression, type: string): BooleanExpression;

Creates an expression that checks if the result of an expression is of the given type.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check.  
`type` | `string`  
The type to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `BooleanExpression` that evaluates to true if the expression's result is of the given type, false otherwise.  
**Remarks**

Null or undefined fields evaluate to skip/error. Use `ifAbsent()` / `isAbsent()` to evaluate missing data. Supported values for `type` are: `'null'`, `'array'`, `'boolean'`, `'bytes'`, `'timestamp'`, `'geo_point'`, `'number'`, `'int32'`, `'int64'`, `'float64'`, `'decimal128'`, `'map'`, `'reference'`, `'string'`, `'vector'`, `'max_key'`, `'min_key'`, `'object_id'`, `'regex'`, `'request_timestamp'`.

#### Example
    
    
    typescript
    // Check if the result of a calculation is a number
    isType(add('count', 1), 'number')
    

### Pipelines.join(arrayFieldName, delimiter)
    
    
    export declare function join(arrayFieldName: string, delimiter: string): Expression;

Creates an expression that joins the elements of an array into a string.
    
    
    // Join the elements of the 'tags' field with a comma and space.
    join("tags", ", ")
    

**Parameters**  
---  
**Name** | **Description**  
`arrayFieldName` | `string`  
The name of the field containing the array.  
`delimiter` | `string`  
The string to use as a delimiter.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the join operation.  
  
### Pipelines.join(arrayExpression, delimiterExpression)
    
    
    export declare function join(arrayExpression: Expression, delimiterExpression: Expression): Expression;

Creates an expression that joins the elements of an array into a string.
    
    
    // Join an array of string using the delimiter from the 'separator' field.
    join(array(['foo', 'bar']), field("separator"))
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that evaluates to an array.  
`delimiterExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression that evaluates to the delimiter string.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the join operation.  
  
### Pipelines.join(arrayExpression, delimiter)
    
    
    export declare function join(arrayExpression: Expression, delimiter: string): Expression;

Creates an expression that joins the elements of an array into a string.
    
    
    // Join the elements of the 'tags' field with a comma and space.
    join(field("tags"), ", ")
    

**Parameters**  
---  
**Name** | **Description**  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that evaluates to an array.  
`delimiter` | `string`  
The string to use as a delimiter.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the join operation.  
  
### Pipelines.join(arrayFieldName, delimiterExpression)
    
    
    export declare function join(arrayFieldName: string, delimiterExpression: Expression): Expression;

Creates an expression that joins the elements of an array into a string.
    
    
    // Join the elements of the 'tags' field with the delimiter from the 'separator' field.
    join('tags', field("separator"))
    

**Parameters**  
---  
**Name** | **Description**  
`arrayFieldName` | `string`  
The name of the field containing the array.  
`delimiterExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression that evaluates to the delimiter string.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the join operation.  
  
### Pipelines.last(expression)
    
    
    export declare function last(expression: Expression): AggregateFunction;

Creates an aggregation that finds the last value of an expression across multiple stage inputs.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to find the last value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'last' aggregation.  
  
#### Example
    
    
    typescript
    // Find the last value of the 'rating' field
    last(field("rating")).as("lastRating");
    

### Pipelines.last(fieldName)
    
    
    export declare function last(fieldName: string): AggregateFunction;

Creates an aggregation that finds the last value of a field across multiple stage inputs.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to find the last value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'last' aggregation.  
  
#### Example
    
    
    typescript
    // Find the last value of the 'rating' field
    last("rating").as("lastRating");
    

### Pipelines.length(fieldName)
    
    
    export declare function length(fieldName: string): FunctionExpression;

Creates an expression that calculates the length of a string, array, map, vector, or bytes.
    
    
    // Get the length of the 'name' field.
    length("name");
    
    // Get the number of items in the 'cart' array.
    length("cart");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to calculate the length of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string, array, map, vector, or bytes.  
  
### Pipelines.length(expression)
    
    
    export declare function length(expression: Expression): FunctionExpression;

Creates an expression that calculates the length of a string, array, map, vector, or bytes.
    
    
    // Get the length of the 'name' field.
    length(field("name"));
    
    // Get the number of items in the 'cart' array.
    length(field("cart"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a string, array, map, vector, or bytes, which the length will be calculated for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string, array, map, vector, or bytes.  
  
### Pipelines.lessThan(left, right)
    
    
    export declare function lessThan(left: Expression, right: Expression): BooleanExpression;

Creates an expression that checks if the first expression is less than the second expression.
    
    
    // Check if the 'age' field is less than 30
    lessThan(field("age"), field("limit"));
    

**Parameters**  
---  
**Name** | **Description**  
`left` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to compare.  
`right` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The second expression to compare.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than comparison.  
  
### Pipelines.lessThan(expression, value)
    
    
    export declare function lessThan(expression: Expression, value: unknown): BooleanExpression;

Creates an expression that checks if an expression is less than a constant value.
    
    
    // Check if the 'age' field is less than 30
    lessThan(field("age"), 30);
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than comparison.  
  
### Pipelines.lessThan(fieldName, expression)
    
    
    export declare function lessThan(fieldName: string, expression: Expression): BooleanExpression;

Creates an expression that checks if a field's value is less than an expression.
    
    
    // Check if the 'age' field is less than the 'limit' field
    lessThan("age", field("limit"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than comparison.  
  
### Pipelines.lessThan(fieldName, value)
    
    
    export declare function lessThan(fieldName: string, value: unknown): BooleanExpression;

Creates an expression that checks if a field's value is less than a constant value.
    
    
    // Check if the 'price' field is less than 50
    lessThan("price", 50);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than comparison.  
  
### Pipelines.lessThanOrEqual(left, right)
    
    
    export declare function lessThanOrEqual(left: Expression, right: Expression): BooleanExpression;

Creates an expression that checks if the first expression is less than or equal to the second expression.
    
    
    // Check if the 'quantity' field is less than or equal to 20
    lessThanOrEqual(field("quantity"), field("limit"));
    

**Parameters**  
---  
**Name** | **Description**  
`left` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to compare.  
`right` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The second expression to compare.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than or equal to comparison.  
  
### Pipelines.lessThanOrEqual(expression, value)
    
    
    export declare function lessThanOrEqual(expression: Expression, value: unknown): BooleanExpression;

Creates an expression that checks if an expression is less than or equal to a constant value.
    
    
    // Check if the 'quantity' field is less than or equal to 20
    lessThanOrEqual(field("quantity"), 20);
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than or equal to comparison.  
  
### Pipelines.lessThanOrEqual(fieldName, expression)
    
    
    export declare function lessThanOrEqual(fieldName: string, expression: Expression): BooleanExpression;

Creates an expression that checks if a field's value is less than or equal to an expression.
    
    
    // Check if the 'quantity' field is less than or equal to the 'limit' field
    lessThanOrEqual("quantity", field("limit"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than or equal to comparison.  
  
### Pipelines.lessThanOrEqual(fieldName, value)
    
    
    export declare function lessThanOrEqual(fieldName: string, value: unknown): BooleanExpression;

Creates an expression that checks if a field's value is less than or equal to a constant value.
    
    
    // Check if the 'score' field is less than or equal to 70
    lessThanOrEqual("score", 70);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than or equal to comparison.  
  
### Pipelines.like(fieldName, pattern)
    
    
    export declare function like(fieldName: string, pattern: string): BooleanExpression;

Creates an expression that performs a case-sensitive wildcard string comparison against a field.
    
    
    // Check if the 'title' field contains the string "guide"
    like("title", "%guide%");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`pattern` | `string`  
The pattern to search for. You can use "%" as a wildcard character.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'like' comparison.  
  
### Pipelines.like(fieldName, pattern)
    
    
    export declare function like(fieldName: string, pattern: Expression): BooleanExpression;

Creates an expression that performs a case-sensitive wildcard string comparison against a field.
    
    
    // Check if the 'title' field contains the string "guide"
    like("title", field("pattern"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The pattern to search for. You can use "%" as a wildcard character.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'like' comparison.  
  
### Pipelines.like(stringExpression, pattern)
    
    
    export declare function like(stringExpression: Expression, pattern: string): BooleanExpression;

Creates an expression that performs a case-sensitive wildcard string comparison.
    
    
    // Check if the 'title' field contains the string "guide"
    like(field("title"), "%guide%");
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to perform the comparison on.  
`pattern` | `string`  
The pattern to search for. You can use "%" as a wildcard character.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'like' comparison.  
  
### Pipelines.like(stringExpression, pattern)
    
    
    export declare function like(stringExpression: Expression, pattern: Expression): BooleanExpression;

Creates an expression that performs a case-sensitive wildcard string comparison.
    
    
    // Check if the 'title' field contains the string "guide"
    like(field("title"), field("pattern"));
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to perform the comparison on.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The pattern to search for. You can use "%" as a wildcard character.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'like' comparison.  
  
### Pipelines.ln(fieldName)
    
    
    export declare function ln(fieldName: string): FunctionExpression;

Creates an expression that computes the natural logarithm of a numeric value.
    
    
    // Compute the natural logarithm of the 'value' field.
    ln("value");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to compute the natural logarithm of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the natural logarithm of the numeric value.  
  
### Pipelines.ln(expression)
    
    
    export declare function ln(expression: Expression): FunctionExpression;

Creates an expression that computes the natural logarithm of a numeric value.
    
    
    // Compute the natural logarithm of the 'value' field.
    ln(field("value"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which the natural logarithm will be computed for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the natural logarithm of the numeric value.  
  
### Pipelines.log10(fieldName)
    
    
    export declare function log10(fieldName: string): FunctionExpression;

Creates an expression that computes the base-10 logarithm of a numeric value.
    
    
    // Compute the base-10 logarithm of the 'value' field.
    log10("value");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to compute the base-10 logarithm of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the base-10 logarithm of the numeric value.  
  
### Pipelines.log10(expression)
    
    
    export declare function log10(expression: Expression): FunctionExpression;

Creates an expression that computes the base-10 logarithm of a numeric value.
    
    
    // Compute the base-10 logarithm of the 'value' field.
    log10(field("value"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which the base-10 logarithm will be computed for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the base-10 logarithm of the numeric value.  
  
### Pipelines.logicalMaximum(first, second, others)
    
    
    export declare function logicalMaximum(first: Expression, second: Expression | unknown, ...others: Array

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.
    
    
    // Returns the largest value between the 'field1' field, the 'field2' field,
    // and 1000
    logicalMaximum(field("field1"), field("field2"), 1000);
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first operand expression.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Optional additional expressions or literals.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the logical max operation.  
  
### Pipelines.logicalMaximum(fieldName, second, others)
    
    
    export declare function logicalMaximum(fieldName: string, second: Expression | unknown, ...others: Array

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.
    
    
    // Returns the largest value between the 'field1' field, the 'field2' field,
    // and 1000.
    logicalMaximum("field1", field("field2"), 1000);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The first operand field name.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Optional additional expressions or literals.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the logical max operation.  
  
### Pipelines.logicalMinimum(first, second, others)
    
    
    export declare function logicalMinimum(first: Expression, second: Expression | unknown, ...others: Array

Creates an expression that returns the smallest value between multiple input expressions and literal values. Based on Firestore's value type ordering.
    
    
    // Returns the smallest value between the 'field1' field, the 'field2' field,
    // and 1000.
    logicalMinimum(field("field1"), field("field2"), 1000);
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first operand expression.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Optional additional expressions or literals.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the logical min operation.  
  
### Pipelines.logicalMinimum(fieldName, second, others)
    
    
    export declare function logicalMinimum(fieldName: string, second: Expression | unknown, ...others: Array

Creates an expression that returns the smallest value between a field's value and other input expressions or literal values. Based on Firestore's value type ordering.
    
    
    // Returns the smallest value between the 'field1' field, the 'field2' field,
    // and 1000.
    logicalMinimum("field1", field("field2"), 1000);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The first operand field name.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal.  
`others` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
Optional additional expressions or literals.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the logical min operation.  
  
### Pipelines.ltrim(fieldName, valueToTrim)
    
    
    export declare function ltrim(fieldName: string, valueToTrim?: string | Expression | Uint8Array | Buffer): FunctionExpression;

Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string or byte array.  
`valueToTrim` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the trimmed string or byte array.  
  
#### Example
    
    
    typescript
    // Trim whitespace from the beginning of the 'userInput' field
    ltrim(field("userInput"));
    
    // Trim quotes from the beginning of the 'userInput' field
    ltrim(field("userInput"), '"');
    

### Pipelines.ltrim(expression, valueToTrim)
    
    
    export declare function ltrim(expression: Expression, valueToTrim?: string | Expression | Uint8Array | Buffer): FunctionExpression;

Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string or byte array.  
`valueToTrim` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the trimmed string or byte array.  
  
#### Example
    
    
    typescript
    // Trim whitespace from the beginning of the 'userInput' field
    ltrim(field("userInput"));
    
    // Trim quotes from the beginning of the 'userInput' field
    ltrim(field("userInput"), '"');
    

### Pipelines.map(elements)
    
    
    export declare function map(elements: Record

Creates an expression that creates a Firestore map value from an input object.
    
    
    // Create a map from the input object and reference the 'baz' field value from the input document.
    map({foo: 'bar', baz: field('baz')}).as('data');
    

**Parameter**  
---  
**Name** | **Description**  
`elements` | `Record<string, unknown>`  
The input map to evaluate in the expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the map function.  
  
### Pipelines.mapEntries(mapField)
    
    
    export declare function mapEntries(mapField: string): FunctionExpression;

Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`.

**Parameter**  
---  
**Name** | **Description**  
`mapField` | `string`  
The map field to get the entries of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the entries of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

#### Example
    
    
    typescript
    // Get the entries of the 'address' map field
    mapEntries("address");
    

### Pipelines.mapEntries(mapExpression)
    
    
    export declare function mapEntries(mapExpression: Expression): FunctionExpression;

Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`.

**Parameter**  
---  
**Name** | **Description**  
`mapExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the map to get the entries of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the entries of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

#### Example
    
    
    typescript
    // Get the entries of the map expression
    mapEntries(map({"city": "San Francisco"}));
    

### Pipelines.mapGet(fieldName, subField)
    
    
    export declare function mapGet(fieldName: string, subField: string): FunctionExpression;

Accesses a value from a map (object) field using the provided key.
    
    
    // Get the 'city' value from the 'address' map field
    mapGet("address", "city");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name of the map field.  
`subField` | `string`  
The key to access in the map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the value associated with the given key in the map.  
  
### Pipelines.mapGet(mapExpression, subField)
    
    
    export declare function mapGet(mapExpression: Expression, subField: string): FunctionExpression;

Accesses a value from a map (object) expression using the provided key.
    
    
    // Get the 'city' value from the 'address' map field
    mapGet(field("address"), "city");
    

**Parameters**  
---  
**Name** | **Description**  
`mapExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the map.  
`subField` | `string`  
The key to access in the map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the value associated with the given key in the map.  
  
### Pipelines.mapKeys(mapField)
    
    
    export declare function mapKeys(mapField: string): FunctionExpression;

Creates an expression that returns the keys of a map.

**Parameter**  
---  
**Name** | **Description**  
`mapField` | `string`  
The map field to get the keys of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the keys of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

#### Example
    
    
    typescript
    // Get the keys of the 'address' map field
    mapKeys("address");
    

### Pipelines.mapKeys(mapExpression)
    
    
    export declare function mapKeys(mapExpression: Expression): FunctionExpression;

Creates an expression that returns the keys of a map.

**Parameter**  
---  
**Name** | **Description**  
`mapExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the map to get the keys of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the keys of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

#### Example
    
    
    typescript
    // Get the keys of the map expression
    mapKeys(map({"city": "San Francisco"}));
    

### Pipelines.mapMerge(mapField, secondMap, otherMaps)
    
    
    export declare function mapMerge(mapField: string, secondMap: Record

Creates an expression that merges multiple map values.
    
    
    // Merges the map in the settings field with, a map literal, and a map in
    // that is conditionally returned by another expression
    mapMerge('settings', { enabled: true }, conditional(field('isAdmin'), { admin: true}, {})
    

**Parameters**  
---  
**Name** | **Description**  
`mapField` | `string`  
Name of a field containing a map value that will be merged.  
`secondMap` | `Record<string, unknown> | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
A required second map to merge. Represented as a literal or an expression that returns a map.  
`otherMaps` | `Array<Record<string, unknown> | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)>`  
Optional additional maps to merge. Each map is represented as a literal or an expression that returns a map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.mapMerge(firstMap, secondMap, otherMaps)
    
    
    export declare function mapMerge(firstMap: Record

Creates an expression that merges multiple map values.
    
    
    // Merges the map in the settings field with, a map literal, and a map in
    // that is conditionally returned by another expression
    mapMerge(field('settings'), { enabled: true }, conditional(field('isAdmin'), { admin: true}, {})
    

**Parameters**  
---  
**Name** | **Description**  
`firstMap` | `Record<string, unknown> | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression or literal map value that will be merged.  
`secondMap` | `Record<string, unknown> | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
A required second map to merge. Represented as a literal or an expression that returns a map.  
`otherMaps` | `Array<Record<string, unknown> | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)>`  
Optional additional maps to merge. Each map is represented as a literal or an expression that returns a map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.mapRemove(mapField, key)
    
    
    export declare function mapRemove(mapField: string, key: string): FunctionExpression;

Creates an expression that removes a key from the map at the specified field name.
    
    
    // Removes the key 'city' field from the map in the address field of the input document.
    mapRemove('address', 'city');
    

**Parameters**  
---  
**Name** | **Description**  
`mapField` | `string`  
The name of a field containing a map value.  
`key` | `string`  
The name of the key to remove from the input map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.mapRemove(mapExpr, key)
    
    
    export declare function mapRemove(mapExpr: Expression, key: string): FunctionExpression;

Creates an expression that removes a key from the map produced by evaluating an expression.
    
    
    // Removes the key 'baz' from the input map.
    mapRemove(map({foo: 'bar', baz: true}), 'baz');
    

**Parameters**  
---  
**Name** | **Description**  
`mapExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression return a map value.  
`key` | `string`  
The name of the key to remove from the input map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.mapRemove(mapField, keyExpr)
    
    
    export declare function mapRemove(mapField: string, keyExpr: Expression): FunctionExpression;

Creates an expression that removes a key from the map at the specified field name.
    
    
    // Removes the key 'city' field from the map in the address field of the input document.
    mapRemove('address', constant('city'));
    

**Parameters**  
---  
**Name** | **Description**  
`mapField` | `string`  
The name of a field containing a map value.  
`keyExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that produces the name of the key to remove from the input map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.mapRemove(mapExpr, keyExpr)
    
    
    export declare function mapRemove(mapExpr: Expression, keyExpr: Expression): FunctionExpression;

Creates an expression that removes a key from the map produced by evaluating an expression.
    
    
    // Removes the key 'baz' from the input map.
    mapRemove(map({foo: 'bar', baz: true}), constant('baz'));
    

**Parameters**  
---  
**Name** | **Description**  
`mapExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression return a map value.  
`keyExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that produces the name of the key to remove from the input map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.mapSet(mapField, key, value, moreKeyValues)
    
    
    export declare function mapSet(mapField: string, key: string | Expression, value: unknown, ...moreKeyValues: unknown[]): FunctionExpression;

Creates an expression that returns a new map with the specified entries added or updated.

**Parameters**  
---  
**Name** | **Description**  
`mapField` | `string`  
The map field to set entries in.  
`key` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The key to set. Must be a string or a constant string expression.  
`value` | `unknown`  
The value to set.  
`moreKeyValues` | `unknown[]`  
Additional key-value pairs to set.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the map with the entries set.  
**Remarks**

This only performs shallow updates to the map. Setting a value to `null` will retain the key with a `null` value. To remove a key entirely, use `mapRemove`.

#### Example
    
    
    typescript
    // Set the 'city' to 'San Francisco' in the 'address' map field
    mapSet("address", "city", "San Francisco");
    

### Pipelines.mapSet(mapExpression, key, value, moreKeyValues)
    
    
    export declare function mapSet(mapExpression: Expression, key: string | Expression, value: unknown, ...moreKeyValues: unknown[]): FunctionExpression;

Creates an expression that returns a new map with the specified entries added or updated.

**Parameters**  
---  
**Name** | **Description**  
`mapExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the map.  
`key` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The key to set. Must be a string or a constant string expression.  
`value` | `unknown`  
The value to set.  
`moreKeyValues` | `unknown[]`  
Additional key-value pairs to set.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the map with the entries set.  
**Remarks**

This only performs shallow updates to the map. Setting a value to `null` will retain the key with a `null` value. To remove a key entirely, use `mapRemove`.

#### Example
    
    
    typescript
    // Set the 'city' to "San Francisco"
    mapSet(map({"state": "California"}), "city", "San Francisco");
    

### Pipelines.mapValues(mapField)
    
    
    export declare function mapValues(mapField: string): FunctionExpression;

Creates an expression that returns the values of a map.

**Parameter**  
---  
**Name** | **Description**  
`mapField` | `string`  
The map field to get the values of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the values of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

#### Example
    
    
    typescript
    // Get the values of the 'address' map field
    mapValues("address");
    

### Pipelines.mapValues(mapExpression)
    
    
    export declare function mapValues(mapExpression: Expression): FunctionExpression;

Creates an expression that returns the values of a map.

**Parameter**  
---  
**Name** | **Description**  
`mapExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the map to get the values of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the values of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

#### Example
    
    
    typescript
    // Get the values of the map expression
    mapValues(map({"city": "San Francisco"}));
    

### Pipelines.maximum(expression)
    
    
    export declare function maximum(expression: Expression): AggregateFunction;

Creates an aggregation that finds the maximum value of an expression across multiple stage inputs.
    
    
    // Find the highest score in a leaderboard
    maximum(field("score")).as("highestScore");
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to find the maximum value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'max' aggregation.  
  
### Pipelines.maximum(fieldName)
    
    
    export declare function maximum(fieldName: string): AggregateFunction;

Creates an aggregation that finds the maximum value of a field across multiple stage inputs.
    
    
    // Find the highest score in a leaderboard
    maximum("score").as("highestScore");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to find the maximum value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'max' aggregation.  
  
### Pipelines.minimum(expression)
    
    
    export declare function minimum(expression: Expression): AggregateFunction;

Creates an aggregation that finds the minimum value of an expression across multiple stage inputs.
    
    
    // Find the lowest price of all products
    minimum(field("price")).as("lowestPrice");
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to find the minimum value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'min' aggregation.  
  
### Pipelines.minimum(fieldName)
    
    
    export declare function minimum(fieldName: string): AggregateFunction;

Creates an aggregation that finds the minimum value of a field across multiple stage inputs.
    
    
    // Find the lowest price of all products
    minimum("price").as("lowestPrice");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to find the minimum value of.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'min' aggregation.  
  
### Pipelines.mod(left, right)
    
    
    export declare function mod(left: Expression, right: Expression): FunctionExpression;

Creates an expression that calculates the modulo (remainder) of dividing two expressions.
    
    
    // Calculate the remainder of dividing 'field1' by 'field2'.
    mod(field("field1"), field("field2"));
    

**Parameters**  
---  
**Name** | **Description**  
`left` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The dividend expression.  
`right` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The divisor expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the modulo operation.  
  
### Pipelines.mod(expression, value)
    
    
    export declare function mod(expression: Expression, value: unknown): FunctionExpression;

Creates an expression that calculates the modulo (remainder) of dividing an expression by a constant.
    
    
    // Calculate the remainder of dividing 'field1' by 5.
    mod(field("field1"), 5);
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The dividend expression.  
`value` | `unknown`  
The divisor constant.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the modulo operation.  
  
### Pipelines.mod(fieldName, expression)
    
    
    export declare function mod(fieldName: string, expression: Expression): FunctionExpression;

Creates an expression that calculates the modulo (remainder) of dividing a field's value by an expression.
    
    
    // Calculate the remainder of dividing 'field1' by 'field2'.
    mod("field1", field("field2"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The dividend field name.  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The divisor expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the modulo operation.  
  
### Pipelines.mod(fieldName, value)
    
    
    export declare function mod(fieldName: string, value: unknown): FunctionExpression;

Creates an expression that calculates the modulo (remainder) of dividing a field's value by a constant.
    
    
    // Calculate the remainder of dividing 'field1' by 5.
    mod("field1", 5);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The dividend field name.  
`value` | `unknown`  
The divisor constant.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the modulo operation.  
  
### Pipelines.multiply(first, second)
    
    
    export declare function multiply(first: Expression, second: Expression | unknown): FunctionExpression;

Creates an expression that multiplies the result of two expressions together.
    
    
    // Multiply the 'quantity' field by the 'price' field
    multiply(field("quantity"), field("price"));
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to multiply.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal to multiply.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the multiplication operation.  
  
### Pipelines.multiply(fieldName, second)
    
    
    export declare function multiply(fieldName: string, second: Expression | unknown): FunctionExpression;

Creates an expression that multiplies a field's value by the result of an expression.
    
    
    // Multiply the 'quantity' field by the 'price' field
    multiply("quantity", field("price"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the value to multiply.  
`second` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`  
The second expression or literal to multiply.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the multiplication operation.  
  
### Pipelines.nor(first, second, more)
    
    
    export declare function nor(first: BooleanExpression, second: BooleanExpression, ...more: BooleanExpression[]): BooleanExpression;

Creates an expression that performs a logical 'NOR' operation on multiple filter conditions.

**Parameters**  
---  
**Name** | **Description**  
`first` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The first filter condition.  
`second` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The second filter condition.  
`more` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)[]`  
Additional filter conditions to 'NOR' together.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the logical 'NOR' operation.  
  
#### Example
    
    
    typescript
    // Check if neither the 'age' field is greater than 18 nor the 'city' field is "London"
    const condition = nor(
      greaterThan("age", 18),
      equal("city", "London")
    );
    

### Pipelines.not(booleanExpr)
    
    
    export declare function not(booleanExpr: BooleanExpression): BooleanExpression;

Creates an expression that negates a filter condition.
    
    
    // Find documents where the 'completed' field is NOT true
    not(equal("completed", true));
    

**Parameter**  
---  
**Name** | **Description**  
`booleanExpr` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The filter condition to negate.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the negated filter condition.  
  
### Pipelines.notEqual(left, right)
    
    
    export declare function notEqual(left: Expression, right: Expression): BooleanExpression;

Creates an expression that checks if two expressions are not equal.
    
    
    // Check if the 'status' field is not equal to field 'finalState'
    notEqual(field("status"), field("finalState"));
    

**Parameters**  
---  
**Name** | **Description**  
`left` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The first expression to compare.  
`right` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The second expression to compare.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the inequality comparison.  
  
### Pipelines.notEqual(expression, value)
    
    
    export declare function notEqual(expression: Expression, value: unknown): BooleanExpression;

Creates an expression that checks if an expression is not equal to a constant value.
    
    
    // Check if the 'status' field is not equal to "completed"
    notEqual(field("status"), "completed");
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the inequality comparison.  
  
### Pipelines.notEqual(fieldName, expression)
    
    
    export declare function notEqual(fieldName: string, expression: Expression): BooleanExpression;

Creates an expression that checks if a field's value is not equal to an expression.
    
    
    // Check if the 'status' field is not equal to the value of 'expectedStatus'
    notEqual("status", field("expectedStatus"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the inequality comparison.  
  
### Pipelines.notEqual(fieldName, value)
    
    
    export declare function notEqual(fieldName: string, value: unknown): BooleanExpression;

Creates an expression that checks if a field's value is not equal to a constant value.
    
    
    // Check if the 'country' field is not equal to "USA"
    notEqual("country", "USA");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`value` | `unknown`  
The constant value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the inequality comparison.  
  
### Pipelines.notEqualAny(element, values)
    
    
    export declare function notEqualAny(element: Expression, values: Array

Creates an expression that checks if an expression is not equal to any of the provided values or expressions.
    
    
    // Check if the 'status' field is neither "pending" nor the value of 'rejectedStatus'
    notEqualAny(field("status"), ["pending", field("rejectedStatus")]);
    

**Parameters**  
---  
**Name** | **Description**  
`element` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The values to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'NOT IN' comparison.  
  
### Pipelines.notEqualAny(fieldName, values)
    
    
    export declare function notEqualAny(fieldName: string, values: Array

Creates an expression that checks if a field's value is not equal to any of the provided values or expressions.
    
    
    // Check if the 'status' field is neither "pending" nor the value of 'rejectedStatus'
    notEqualAny("status", [constant("pending"), field("rejectedStatus")]);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`values` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`  
The values to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'NOT IN' comparison.  
  
### Pipelines.notEqualAny(element, arrayExpression)
    
    
    export declare function notEqualAny(element: Expression, arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if an expression is not equal to any of the provided values or expressions.
    
    
    // Check if the 'status' field is neither "pending" nor the value of the field 'rejectedStatus'
    notEqualAny(field("status"), ["pending", field("rejectedStatus")]);
    

**Parameters**  
---  
**Name** | **Description**  
`element` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to compare.  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The values to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'NOT IN' comparison.  
  
### Pipelines.notEqualAny(fieldName, arrayExpression)
    
    
    export declare function notEqualAny(fieldName: string, arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if a field's value is not equal to any of the values in the evaluated expression.
    
    
    // Check if the 'status' field is not equal to any value in the field 'rejectedStatuses'
    notEqualAny("status", field("rejectedStatuses"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to compare.  
`arrayExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The values to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'NOT IN' comparison.  
  
### Pipelines.or(first, second, more)
    
    
    export declare function or(first: BooleanExpression, second: BooleanExpression, ...more: BooleanExpression[]): BooleanExpression;

Creates an expression that performs a logical 'OR' operation on multiple filter conditions.
    
    
    // Check if the 'age' field is greater than 18 OR the 'city' field is "London" OR
    // the 'status' field is "active"
    const condition = or(greaterThan("age", 18), equal("city", "London"), equal("status", "active"));
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The first filter condition.  
`second` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The second filter condition.  
`more` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)[]`  
Additional filter conditions to 'OR' together.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the logical 'OR' operation.  
  
### Pipelines.parent(documentPath)
    
    
    export declare function parent(documentPath: string | firestore.DocumentReference): FunctionExpression;

Creates an expression that returns the parent document of a document reference.

**Parameter**  
---  
**Name** | **Description**  
`documentPath` | `string | FirebaseFirestore.DocumentReference`  
A string path or DocumentReference to get the parent from.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the parent operation.  
  
#### Example
    
    
    typescript
    // Get the parent document of a document reference.
    parent(myDocumentReference);
    

### Pipelines.parent(documentPathExpr)
    
    
    export declare function parent(documentPathExpr: Expression): FunctionExpression;

Creates an expression that returns the parent document of a document reference.

**Parameter**  
---  
**Name** | **Description**  
`documentPathExpr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An Expression evaluating to a document reference.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the parent operation.  
  
#### Example
    
    
    typescript
    // Get the parent document of a document reference.
    parent(field("__path__"));
    

### Pipelines.pow(base, exponent)
    
    
    export declare function pow(base: Expression, exponent: Expression): FunctionExpression;

Creates an expression that returns the value of the base expression raised to the power of the exponent expression.
    
    
    // Raise the value of the 'base' field to the power of the 'exponent' field.
    pow(field("base"), field("exponent"));
    

**Parameters**  
---  
**Name** | **Description**  
`base` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to raise to the power of the exponent.  
`exponent` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to raise the base to the power of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the power operation.  
  
### Pipelines.pow(base, exponent)
    
    
    export declare function pow(base: Expression, exponent: number): FunctionExpression;

Creates an expression that returns the value of the base expression raised to the power of the exponent.
    
    
    // Raise the value of the 'base' field to the power of 2.
    pow(field("base"), 2);
    

**Parameters**  
---  
**Name** | **Description**  
`base` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to raise to the power of the exponent.  
`exponent` | `number`  
The constant value to raise the base to the power of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the power operation.  
  
### Pipelines.pow(base, exponent)
    
    
    export declare function pow(base: string, exponent: Expression): FunctionExpression;

Creates an expression that returns the value of the base field raised to the power of the exponent expression.
    
    
    // Raise the value of the 'base' field to the power of the 'exponent' field.
    pow("base", field("exponent"));
    

**Parameters**  
---  
**Name** | **Description**  
`base` | `string`  
The name of the field to raise to the power of the exponent.  
`exponent` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to raise the base to the power of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the power operation.  
  
### Pipelines.pow(base, exponent)
    
    
    export declare function pow(base: string, exponent: number): FunctionExpression;

Creates an expression that returns the value of the base field raised to the power of the exponent.
    
    
    // Raise the value of the 'base' field to the power of 2.
    pow("base", 2);
    

**Parameters**  
---  
**Name** | **Description**  
`base` | `string`  
The name of the field to raise to the power of the exponent.  
`exponent` | `number`  
The constant value to raise the base to the power of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the power operation.  
  
### Pipelines.rand()
    
    
    export declare function rand(): FunctionExpression;

Creates an expression that generates a random number between 0.0 and 1.0 but not including 1.0.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the rand operation.  
  
#### Example
    
    
    typescript
    // Generate a random number between 0.0 and 1.0.
    rand();
    

### Pipelines.regexContains(fieldName, pattern)
    
    
    export declare function regexContains(fieldName: string, pattern: string): BooleanExpression;

Creates an expression that checks if a string field contains a specified regular expression as a substring.
    
    
    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains("description", "(?i)example");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`pattern` | `string`  
The regular expression to use for the search.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.regexContains(fieldName, pattern)
    
    
    export declare function regexContains(fieldName: string, pattern: Expression): BooleanExpression;

Creates an expression that checks if a string field contains a specified regular expression as a substring.
    
    
    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains("description", field("pattern"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to use for the search.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.regexContains(stringExpression, pattern)
    
    
    export declare function regexContains(stringExpression: Expression, pattern: string): BooleanExpression;

Creates an expression that checks if a string expression contains a specified regular expression as a substring.
    
    
    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains(field("description"), "(?i)example");
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to perform the comparison on.  
`pattern` | `string`  
The regular expression to use for the search.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.regexContains(stringExpression, pattern)
    
    
    export declare function regexContains(stringExpression: Expression, pattern: Expression): BooleanExpression;

Creates an expression that checks if a string expression contains a specified regular expression as a substring.
    
    
    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains(field("description"), field("pattern"));
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to perform the comparison on.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to use for the search.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.regexFind(fieldName, pattern)
    
    
    export declare function regexFind(fieldName: string, pattern: string): FunctionExpression;

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string to search.  
`pattern` | `string`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the regular expression find function.  
  
#### Example
    
    
    typescript
    // Extract the domain name from an email field
    regexFind("email", "@[A-Za-z0-9.-]+");
    

### Pipelines.regexFind(fieldName, pattern)
    
    
    export declare function regexFind(fieldName: string, pattern: Expression): FunctionExpression;

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string to search.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the regular expression find function.  
  
#### Example
    
    
    typescript
    // Extract a substring from 'email' based on a pattern stored in another field
    regexFind("email", field("pattern"));
    

### Pipelines.regexFind(stringExpression, pattern)
    
    
    export declare function regexFind(stringExpression: Expression, pattern: string): FunctionExpression;

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to search.  
`pattern` | `string`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the regular expression find function.  
  
#### Example
    
    
    typescript
    // Extract the domain from a lower-cased email address
    regexFind(field("email"), "@[A-Za-z0-9.-]+");
    

### Pipelines.regexFind(stringExpression, pattern)
    
    
    export declare function regexFind(stringExpression: Expression, pattern: Expression): FunctionExpression;

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to search.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the regular expression find function.  
  
#### Example
    
    
    typescript
    // Extract a substring based on a dynamic pattern field
    regexFind(field("email"), field("pattern"));
    

### Pipelines.regexFindAll(fieldName, pattern)
    
    
    export declare function regexFindAll(fieldName: string, pattern: string): FunctionExpression;

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string to search.  
`pattern` | `string`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` that evaluates to an array of matched substrings.  
  
#### Example
    
    
    typescript
    // Extract all hashtags from a post content field
    regexFindAll("content", "#[A-Za-z0-9_]+");
    

### Pipelines.regexFindAll(fieldName, pattern)
    
    
    export declare function regexFindAll(fieldName: string, pattern: Expression): FunctionExpression;

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string to search.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` that evaluates to an array of matched substrings.  
  
#### Example
    
    
    typescript
    // Extract all matches from 'content' based on a pattern stored in another field
    regexFindAll("content", field("pattern"));
    

### Pipelines.regexFindAll(stringExpression, pattern)
    
    
    export declare function regexFindAll(stringExpression: Expression, pattern: string): FunctionExpression;

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to search.  
`pattern` | `string`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` that evaluates to an array of matched substrings.  
  
#### Example
    
    
    typescript
    // Extract all mentions from a lower-cased comment
    regexFindAll(field("comment"), "@[A-Za-z0-9_]+");
    

### Pipelines.regexFindAll(stringExpression, pattern)
    
    
    export declare function regexFindAll(stringExpression: Expression, pattern: Expression): FunctionExpression;

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to search.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` that evaluates to an array of matched substrings.  
  
#### Example
    
    
    typescript
    // Extract all matches based on a dynamic pattern expression
    regexFindAll(field("comment"), field("pattern"));
    

### Pipelines.regexMatch(fieldName, pattern)
    
    
    export declare function regexMatch(fieldName: string, pattern: string): BooleanExpression;

Creates an expression that checks if a string field matches a specified regular expression.
    
    
    // Check if the 'email' field matches a valid email pattern
    regexMatch("email", "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`pattern` | `string`  
The regular expression to use for the match.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the regular expression match.  
  
### Pipelines.regexMatch(fieldName, pattern)
    
    
    export declare function regexMatch(fieldName: string, pattern: Expression): BooleanExpression;

Creates an expression that checks if a string field matches a specified regular expression.
    
    
    // Check if the 'email' field matches a valid email pattern
    regexMatch("email", field("pattern"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to use for the match.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the regular expression match.  
  
### Pipelines.regexMatch(stringExpression, pattern)
    
    
    export declare function regexMatch(stringExpression: Expression, pattern: string): BooleanExpression;

Creates an expression that checks if a string expression matches a specified regular expression.
    
    
    // Check if the 'email' field matches a valid email pattern
    regexMatch(field("email"), "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}");
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to match against.  
`pattern` | `string`  
The regular expression to use for the match.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the regular expression match.  
  
### Pipelines.regexMatch(stringExpression, pattern)
    
    
    export declare function regexMatch(stringExpression: Expression, pattern: Expression): BooleanExpression;

Creates an expression that checks if a string expression matches a specified regular expression.
    
    
    // Check if the 'email' field matches a valid email pattern
    regexMatch(field("email"), field("pattern"));
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to match against.  
`pattern` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The regular expression to use for the match.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the regular expression match.  
  
### Pipelines.reverse(stringExpression)
    
    
    export declare function reverse(stringExpression: Expression): FunctionExpression;

Creates an expression that reverses a string.
    
    
    // Reverse the value of the 'myString' field.
    reverse(field("myString"));
    

**Parameter**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a string value, which will be reversed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed string.  
  
### Pipelines.reverse(field)
    
    
    export declare function reverse(field: string): FunctionExpression;

Creates an expression that reverses a string value in the specified field.
    
    
    // Reverse the value of the 'myString' field.
    reverse("myString");
    

**Parameter**  
---  
**Name** | **Description**  
`field` | `string`  
The name of the field representing the string to reverse.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed string.  
  
### Pipelines.round(fieldName)
    
    
    export declare function round(fieldName: string): FunctionExpression;

Creates an expression that rounds a numeric value to the nearest whole number.
    
    
    // Round the value of the 'price' field.
    round("price");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to round.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the rounded value.  
  
### Pipelines.round(expression)
    
    
    export declare function round(expression: Expression): FunctionExpression;

Creates an expression that rounds a numeric value to the nearest whole number.
    
    
    // Round the value of the 'price' field.
    round(field("price"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which will be rounded.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the rounded value.  
  
### Pipelines.round(fieldName, decimalPlaces)
    
    
    export declare function round(fieldName: string, decimalPlaces: number | Expression): FunctionExpression;

Creates an expression that rounds a numeric value to the specified number of decimal places.
    
    
    // Round the value of the 'price' field to two decimal places.
    round("price", 2);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to round.  
`decimalPlaces` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
A constant or expression specifying the rounding precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the rounded value.  
  
### Pipelines.round(expression, decimalPlaces)
    
    
    export declare function round(expression: Expression, decimalPlaces: number | Expression): FunctionExpression;

Creates an expression that rounds a numeric value to the specified number of decimal places.
    
    
    // Round the value of the 'price' field to two decimal places.
    round(field("price"), constant(2));
    

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which will be rounded.  
`decimalPlaces` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
A constant or expression specifying the rounding precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the rounded value.  
  
### Pipelines.rtrim(fieldName, valueToTrim)
    
    
    export declare function rtrim(fieldName: string, valueToTrim?: string | Expression | Uint8Array | Buffer): FunctionExpression;

Trims whitespace or a specified set of characters/bytes from the end of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string or byte array.  
`valueToTrim` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the trimmed string or byte array.  
  
#### Example
    
    
    typescript
    // Trim whitespace from the end of the 'userInput' field
    rtrim(field("userInput"));
    
    // Trim quotes from the end of the 'userInput' field
    rtrim(field("userInput"), '"');
    

### Pipelines.rtrim(expression, valueToTrim)
    
    
    export declare function rtrim(expression: Expression, valueToTrim?: string | Expression | Uint8Array | Buffer): FunctionExpression;

Trims whitespace or a specified set of characters/bytes from the end of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string or byte array.  
`valueToTrim` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the trimmed string or byte array.  
  
#### Example
    
    
    typescript
    // Trim whitespace from the end of the 'userInput' field
    rtrim(field("userInput"));
    
    // Trim quotes from the end of the 'userInput' field
    rtrim(field("userInput"), '"');
    

### Pipelines.score()
    
    
    export declare function score(): Expression;

Evaluates to the search score that reflects the topicality of the document to all the text predicates (for example: `documentMatches`) in the search `query` provided to the `search` stage. If the `query` provided to the search stage is not set or does not contain any text predicates, then this score will always be `0`.

**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | An `Expression` representing the score function.  
**Remarks**

This Expression can only be used within a `search` stage.

### Pipelines.split(fieldName, delimiter)
    
    
    export declare function split(fieldName: string, delimiter: string): FunctionExpression;

Creates an expression that splits the value of a field on the provided delimiter.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
Split the value in this field.  
`delimiter` | `string`  
Split on this delimiter.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the split function.  
  
#### Example
    
    
    typescript
    // Split the 'scoresCsv' field on delimiter ','
    split('scoresCsv', ',')
    

### Pipelines.split(fieldName, delimiter)
    
    
    export declare function split(fieldName: string, delimiter: Expression): FunctionExpression;

Creates an expression that splits the value of a field on the provided delimiter.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
Split the value in this field.  
`delimiter` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Split on this delimiter returned by evaluating this expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the split function.  
  
#### Example
    
    
    typescript
    // Split the 'scores' field on delimiter ',' or ':' depending on the stored format
    split('scores', conditional(field('format').equal('csv'), constant(','), constant(':'))
    

### Pipelines.split(expression, delimiter)
    
    
    export declare function split(expression: Expression, delimiter: string): FunctionExpression;

Creates an expression that splits a string into an array of substrings based on the provided delimiter.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Split the result of this expression.  
`delimiter` | `string`  
Split on this delimiter.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the split function.  
  
#### Example
    
    
    typescript
    // Split the 'scoresCsv' field on delimiter ','
    split(field('scoresCsv'), ',')
    

### Pipelines.split(expression, delimiter)
    
    
    export declare function split(expression: Expression, delimiter: Expression): FunctionExpression;

Creates an expression that splits a string into an array of substrings based on the provided delimiter.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Split the result of this expression.  
`delimiter` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Split on this delimiter returned by evaluating this expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the split function.  
  
#### Example
    
    
    typescript
    // Split the 'scores' field on delimiter ',' or ':' depending on the stored format
    split(field('scores'), conditional(field('format').equal('csv'), constant(','), constant(':'))
    

### Pipelines.sqrt(expression)
    
    
    export declare function sqrt(expression: Expression): FunctionExpression;

Creates an expression that computes the square root of a numeric value.
    
    
    // Compute the square root of the 'value' field.
    sqrt(field("value"));
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which the square root will be computed for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the square root of the numeric value.  
  
### Pipelines.sqrt(fieldName)
    
    
    export declare function sqrt(fieldName: string): FunctionExpression;

Creates an expression that computes the square root of a numeric value.
    
    
    // Compute the square root of the 'value' field.
    sqrt("value");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to compute the square root of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the square root of the numeric value.  
  
### Pipelines.startsWith(fieldName, prefix)
    
    
    export declare function startsWith(fieldName: string, prefix: string): BooleanExpression;

Creates an expression that checks if a field's value starts with a given prefix.
    
    
    // Check if the 'name' field starts with "Mr."
    startsWith("name", "Mr.");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`prefix` | `string`  
The prefix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'starts with' comparison.  
  
### Pipelines.startsWith(fieldName, prefix)
    
    
    export declare function startsWith(fieldName: string, prefix: Expression): BooleanExpression;

Creates an expression that checks if a field's value starts with a given prefix.
    
    
    // Check if the 'fullName' field starts with the value of the 'firstName' field
    startsWith("fullName", field("firstName"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name to check.  
`prefix` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the prefix.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'starts with' comparison.  
  
### Pipelines.startsWith(stringExpression, prefix)
    
    
    export declare function startsWith(stringExpression: Expression, prefix: string): BooleanExpression;

Creates an expression that checks if a string expression starts with a given prefix.
    
    
    // Check if the result of concatenating 'firstName' and 'lastName' fields starts with "Mr."
    startsWith(field("fullName"), "Mr.");
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check.  
`prefix` | `string`  
The prefix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'starts with' comparison.  
  
### Pipelines.startsWith(stringExpression, prefix)
    
    
    export declare function startsWith(stringExpression: Expression, prefix: Expression): BooleanExpression;

Creates an expression that checks if a string expression starts with a given prefix.
    
    
    // Check if the result of concatenating 'firstName' and 'lastName' fields starts with "Mr."
    startsWith(field("fullName"), field("prefix"));
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to check.  
`prefix` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The prefix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'starts with' comparison.  
  
### Pipelines.stringConcat(fieldName, secondString, otherStrings)
    
    
    export declare function stringConcat(fieldName: string, secondString: Expression | string, ...otherStrings: Array

Creates an expression that concatenates string functions, fields or constants together.
    
    
    // Combine the 'firstName', " ", and 'lastName' fields into a single string
    stringConcat("firstName", " ", field("lastName"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The field name containing the initial string value.  
`secondString` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | string`  
An expression or string literal to concatenate.  
`otherStrings` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | string>`  
Optional additional expressions or literals (typically strings) to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the concatenated string.  
  
### Pipelines.stringConcat(firstString, secondString, otherStrings)
    
    
    export declare function stringConcat(firstString: Expression, secondString: Expression | string, ...otherStrings: Array

Creates an expression that concatenates string expressions together.
    
    
    // Combine the 'firstName', " ", and 'lastName' fields into a single string
    stringConcat(field("firstName"), " ", field("lastName"));
    

**Parameters**  
---  
**Name** | **Description**  
`firstString` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The initial string expression to concatenate to.  
`secondString` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | string`  
An expression or string literal to concatenate.  
`otherStrings` | `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | string>`  
Optional additional expressions or literals (typically strings) to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the concatenated string.  
  
### Pipelines.stringContains(fieldName, substring)
    
    
    export declare function stringContains(fieldName: string, substring: string): BooleanExpression;

Creates an expression that checks if a string field contains a specified substring.
    
    
    // Check if the 'description' field contains "example".
    stringContains("description", "example");
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`substring` | `string`  
The substring to search for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.stringContains(fieldName, substring)
    
    
    export declare function stringContains(fieldName: string, substring: Expression): BooleanExpression;

Creates an expression that checks if a string field contains a substring specified by an expression.
    
    
    // Check if the 'description' field contains the value of the 'keyword' field.
    stringContains("description", field("keyword"));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
`substring` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the substring to search for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.stringContains(stringExpression, substring)
    
    
    export declare function stringContains(stringExpression: Expression, substring: string): BooleanExpression;

Creates an expression that checks if a string expression contains a specified substring.
    
    
    // Check if the 'description' field contains "example".
    stringContains(field("description"), "example");
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to perform the comparison on.  
`substring` | `string`  
The substring to search for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.stringContains(stringExpression, substring)
    
    
    export declare function stringContains(stringExpression: Expression, substring: Expression): BooleanExpression;

Creates an expression that checks if a string expression contains a substring specified by another expression.
    
    
    // Check if the 'description' field contains the value of the 'keyword' field.
    stringContains(field("description"), field("keyword"));
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to perform the comparison on.  
`substring` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the substring to search for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
  
### Pipelines.stringIndexOf(fieldName, search)
    
    
    export declare function stringIndexOf(fieldName: string, search: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that finds the index of the first occurrence of a substring or byte sequence.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string or byte array.  
`search` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The substring or byte sequence to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the index of the first occurrence.  
  
#### Example
    
    
    typescript
    // Find the index of "foo" in the 'text' field
    stringIndexOf("text", "foo");
    

### Pipelines.stringIndexOf(expression, search)
    
    
    export declare function stringIndexOf(expression: Expression, search: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that finds the index of the first occurrence of a substring or byte sequence.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string or byte array.  
`search` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The substring or byte sequence to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the index of the first occurrence.  
  
#### Example
    
    
    typescript
    // Find the index of "foo" in the 'text' field
    stringIndexOf(field("text"), "foo");
    

### Pipelines.stringRepeat(fieldName, repetitions)
    
    
    export declare function stringRepeat(fieldName: string, repetitions: number | Expression): FunctionExpression;

Creates an expression that repeats a string or byte array a specified number of times.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string or byte array.  
`repetitions` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The number of times to repeat the string or byte array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the repeated string or byte array.  
  
#### Example
    
    
    typescript
    // Repeat the 'label' field 3 times
    stringRepeat("label", 3);
    

### Pipelines.stringRepeat(expression, repetitions)
    
    
    export declare function stringRepeat(expression: Expression, repetitions: number | Expression): FunctionExpression;

Creates an expression that repeats a string or byte array a specified number of times.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string or byte array.  
`repetitions` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The number of times to repeat the string or byte array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the repeated string or byte array.  
  
#### Example
    
    
    typescript
    // Repeat the 'label' field 3 times
    stringRepeat(field("label"), 3);
    

### Pipelines.stringReplaceAll(fieldName, find, replacement)
    
    
    export declare function stringReplaceAll(fieldName: string, find: string | Expression | Uint8Array | Buffer, replacement: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string or byte array.  
`find` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The substring or byte sequence to search for.  
`replacement` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The replacement string or byte sequence.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the string or byte array with replacements.  
  
#### Example
    
    
    typescript
    // Replace all occurrences of "foo" with "bar" in the 'text' field
    stringReplaceAll("text", "foo", "bar");
    

### Pipelines.stringReplaceAll(expression, find, replacement)
    
    
    export declare function stringReplaceAll(expression: Expression, find: string | Expression | Uint8Array | Buffer, replacement: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string or byte array.  
`find` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The substring or byte sequence to search for.  
`replacement` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The replacement string or byte sequence.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the string or byte array with replacements.  
  
#### Example
    
    
    typescript
    // Replace all occurrences of "foo" with "bar" in the 'text' field
    stringReplaceAll(field("text"), "foo", "bar");
    

### Pipelines.stringReplaceOne(fieldName, find, replacement)
    
    
    export declare function stringReplaceOne(fieldName: string, find: string | Expression | Uint8Array | Buffer, replacement: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string or byte array.  
`find` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The substring or byte sequence to search for.  
`replacement` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The replacement string or byte sequence.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the string or byte array with the replacement.  
  
#### Example
    
    
    typescript
    // Replace the first occurrence of "foo" with "bar" in the 'text' field
    stringReplaceOne("text", "foo", "bar");
    

### Pipelines.stringReplaceOne(expression, find, replacement)
    
    
    export declare function stringReplaceOne(expression: Expression, find: string | Expression | Uint8Array | Buffer, replacement: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string or byte array.  
`find` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The substring or byte sequence to search for.  
`replacement` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`  
The replacement string or byte sequence.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new representing the string or byte array with the replacement.  
  
#### Example
    
    
    typescript
    // Replace the first occurrence of "foo" with "bar" in the 'text' field
    stringReplaceOne(field("text"), "foo", "bar");
    

### Pipelines.stringReverse(stringExpression)
    
    
    export declare function stringReverse(stringExpression: Expression): FunctionExpression;

Creates an expression that reverses a string.
    
    
    // Reverse the value of the 'myString' field.
    stringReverse(field("myString"));
    

**Parameter**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a string value, which will be reversed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed string.  
  
### Pipelines.stringReverse(field)
    
    
    export declare function stringReverse(field: string): FunctionExpression;

Creates an expression that reverses a string value in the specified field.
    
    
    // Reverse the value of the 'myString' field.
    stringReverse("myString");
    

**Parameter**  
---  
**Name** | **Description**  
`field` | `string`  
The name of the field representing the string to reverse.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed string.  
  
### Pipelines.subcollection(path)
    
    
    export declare function subcollection(path: string): Pipeline;

Creates a new Pipeline targeted at a subcollection relative to the current document context. This creates a pipeline without a database instance, suitable for embedding as a subquery. If executed directly, this pipeline will fail.

**Parameter**  
---  
**Name** | **Description**  
`path` | `string`  
The relative path to the subcollection.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### Pipelines.subcollection(options)
    
    
    export declare function subcollection(options: firestore.Pipelines.SubcollectionStageOptions): Pipeline;

Creates a new Pipeline targeted at a subcollection relative to the current document context.

**Parameter**  
---  
**Name** | **Description**  
`options` | `firestore.Pipelines.SubcollectionStageOptions`  
Options defining how this SubcollectionStage is evaluated.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### Pipelines.substring(field, position, length)
    
    
    export declare function substring(field: string, position: number, length?: number): FunctionExpression;

Creates an expression that returns a substring of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`field` | `string`  
The name of a field containing a string or byte array to compute the substring from.  
`position` | `number`  
Index of the first character of the substring.  
`length` | `number`  
Length of the substring.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.substring(input, position, length)
    
    
    export declare function substring(input: Expression, position: number, length?: number): FunctionExpression;

Creates an expression that returns a substring of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`input` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression returning a string or byte array to compute the substring from.  
`position` | `number`  
Index of the first character of the substring.  
`length` | `number`  
Length of the substring.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.substring(field, position, length)
    
    
    export declare function substring(field: string, position: Expression, length?: Expression): FunctionExpression;

Creates an expression that returns a substring of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`field` | `string`  
The name of a field containing a string or byte array to compute the substring from.  
`position` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that returns the index of the first character of the substring.  
`length` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that returns the length of the substring.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.substring(input, position, length)
    
    
    export declare function substring(input: Expression, position: Expression, length?: Expression): FunctionExpression;

Creates an expression that returns a substring of a string or byte array.

**Parameters**  
---  
**Name** | **Description**  
`input` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression returning a string or byte array to compute the substring from.  
`position` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that returns the index of the first character of the substring.  
`length` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression that returns the length of the substring.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### Pipelines.subtract(minuend, subtrahend)
    
    
    export declare function subtract(minuend: Expression, subtrahend: Expression): FunctionExpression;

Creates an expression that subtracts two expressions.
    
    
    // Subtract the 'discount' field from the 'price' field
    subtract(field("price"), field("discount"));
    

**Parameters**  
---  
**Name** | **Description**  
`minuend` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to subtract from.  
`subtrahend` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the subtraction operation.  
  
### Pipelines.subtract(minuend, subtrahend)
    
    
    export declare function subtract(minuend: Expression, subtrahend: unknown): FunctionExpression;

Creates an expression that subtracts a constant value from an expression.
    
    
    // Subtract the constant value 2 from the 'value' field
    subtract(field("value"), 2);
    

**Parameters**  
---  
**Name** | **Description**  
`minuend` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to subtract from.  
`subtrahend` | `unknown`  
The constant value to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the subtraction operation.  
  
### Pipelines.subtract(minuendFieldName, subtrahend)
    
    
    export declare function subtract(minuendFieldName: string, subtrahend: Expression): FunctionExpression;

Creates an expression that subtracts an expression from a field's value.
    
    
    // Subtract the 'discount' field from the 'price' field
    subtract("price", field("discount"));
    

**Parameters**  
---  
**Name** | **Description**  
`minuendFieldName` | `string`  
The field name to subtract from.  
`subtrahend` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the subtraction operation.  
  
### Pipelines.subtract(minuendFieldName, subtrahend)
    
    
    export declare function subtract(minuendFieldName: string, subtrahend: unknown): FunctionExpression;

Creates an expression that subtracts a constant value from a field's value.
    
    
    // Subtract 20 from the value of the 'total' field
    subtract("total", 20);
    

**Parameters**  
---  
**Name** | **Description**  
`minuendFieldName` | `string`  
The field name to subtract from.  
`subtrahend` | `unknown`  
The constant value to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the subtraction operation.  
  
### Pipelines.sum(expression)
    
    
    export declare function sum(expression: Expression): AggregateFunction;

Creates an aggregation that calculates the sum of values from an expression across multiple stage inputs.
    
    
    // Calculate the total revenue from a set of orders
    sum(field("orderAmount")).as("totalRevenue");
    

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression to sum up.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'sum' aggregation.  
  
### Pipelines.sum(fieldName)
    
    
    export declare function sum(fieldName: string): AggregateFunction;

Creates an aggregation that calculates the sum of a field's values across multiple stage inputs.
    
    
    // Calculate the total revenue from a set of orders
    sum("orderAmount").as("totalRevenue");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing numeric values to sum up.  
**Returns**  
---  
**Type** | **Description**  
`[Pipelines.AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'sum' aggregation.  
  
### Pipelines.switchOn(condition, result, others)
    
    
    export declare function switchOn(condition: BooleanExpression, result: Expression, ...others: Array

Creates an expression that evaluates to the result corresponding to the first true condition.

**Parameters**  
---  
**Name** | **Description**  
`condition` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The first condition to check.  
`result` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The result if the first condition is true.  
`others` | `Array<[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression) | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)>`  
Additional conditions and results, and optionally a default value.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the switch operation.  
**Remarks**

This function behaves like a `switch` statement. It accepts an alternating sequence of conditions and their corresponding results. If an odd number of arguments is provided, the final argument serves as a default fallback result. If no default is provided and no condition evaluates to true, it throws an error.

#### Example
    
    
    typescript
    // Return "Active" if field "status" is 1, "Pending" if field "status" is 2,
    // and default to "Unknown" if none of the conditions are true.
    switchOn(
      equal(field("status"), 1), constant("Active"),
      equal(field("status"), 2), constant("Pending"),
      constant("Unknown")
    )
    

### Pipelines.timestampAdd(timestamp, unit, amount)
    
    
    export declare function timestampAdd(timestamp: Expression, unit: Expression, amount: Expression): FunctionExpression;

Creates an expression that adds a specified amount of time to a timestamp.
    
    
    // Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
    timestampAdd(field("timestamp"), field("unit"), field("amount"));
    

**Parameters**  
---  
**Name** | **Description**  
`timestamp` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the timestamp.  
`unit` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'.  
`amount` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluates to amount of the unit.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
  
### Pipelines.timestampAdd(timestamp, unit, amount)
    
    
    export declare function timestampAdd(timestamp: Expression, unit: firestore.Pipelines.TimeUnit, amount: number): FunctionExpression;

Creates an expression that adds a specified amount of time to a timestamp.
    
    
    // Add 1 day to the 'timestamp' field.
    timestampAdd(field("timestamp"), "day", 1);
    

**Parameters**  
---  
**Name** | **Description**  
`timestamp` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the timestamp.  
`unit` | `firestore.Pipelines.TimeUnit`  
The unit of time to add (e.g., "day", "hour").  
`amount` | `number`  
The amount of time to add.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
  
### Pipelines.timestampAdd(fieldName, unit, amount)
    
    
    export declare function timestampAdd(fieldName: string, unit: firestore.Pipelines.TimeUnit, amount: number): FunctionExpression;

Creates an expression that adds a specified amount of time to a timestamp represented by a field.
    
    
    // Add 1 day to the 'timestamp' field.
    timestampAdd("timestamp", "day", 1);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the timestamp.  
`unit` | `firestore.Pipelines.TimeUnit`  
The unit of time to add (e.g., "day", "hour").  
`amount` | `number`  
The amount of time to add.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
  
### Pipelines.timestampDiff(endFieldName, startFieldName, unit)
    
    
    export declare function timestampDiff(endFieldName: string, startFieldName: string, unit: firestore.Pipelines.TimeUnit | Expression): FunctionExpression;

Creates an expression that calculates the difference between two timestamps.

**Parameters**  
---  
**Name** | **Description**  
`endFieldName` | `string`  
The name of the field representing the ending timestamp.  
`startFieldName` | `string`  
The name of the field representing the starting timestamp.  
`unit` | `FirebaseFirestore.Pipelines.TimeUnit | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The unit of time for the difference (e.g., "day", "hour").  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the difference as an integer.  
  
#### Example
    
    
    typescript
    // Calculate the difference in days between 'endTime' and 'startTime' fields.
    timestampDiff('endTime', 'startTime', 'day')
    

### Pipelines.timestampDiff(endFieldName, startExpression, unit)
    
    
    export declare function timestampDiff(endFieldName: string, startExpression: Expression, unit: firestore.Pipelines.TimeUnit | Expression): FunctionExpression;

Creates an expression that calculates the difference between two timestamps.

**Parameters**  
---  
**Name** | **Description**  
`endFieldName` | `string`  
The name of the field representing the ending timestamp.  
`startExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The starting timestamp for the difference calculation.  
`unit` | `FirebaseFirestore.Pipelines.TimeUnit | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The unit of time for the difference (e.g., "day", "hour").  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the difference as an integer.  
  
#### Example
    
    
    typescript
    // Calculate the difference in days between 'endTime' field and a starting timestamp expression.
    timestampDiff('endTime', field('startTime'), 'day')
    

### Pipelines.timestampDiff(endExpression, startFieldName, unit)
    
    
    export declare function timestampDiff(endExpression: Expression, startFieldName: string, unit: firestore.Pipelines.TimeUnit | Expression): FunctionExpression;

Creates an expression that calculates the difference between two timestamps.

**Parameters**  
---  
**Name** | **Description**  
`endExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The ending timestamp for the difference calculation.  
`startFieldName` | `string`  
The name of the field representing the starting timestamp.  
`unit` | `FirebaseFirestore.Pipelines.TimeUnit | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The unit of time for the difference (e.g., "day", "hour").  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the difference as an integer.  
  
#### Example
    
    
    typescript
    // Calculate the difference in days between an ending timestamp expression and 'startTime' field.
    timestampDiff(field('endTime'), 'startTime', 'day')
    

### Pipelines.timestampDiff(endExpression, startExpression, unit)
    
    
    export declare function timestampDiff(endExpression: Expression, startExpression: Expression, unit: firestore.Pipelines.TimeUnit | Expression): FunctionExpression;

Creates an expression that calculates the difference between two timestamps.

**Parameters**  
---  
**Name** | **Description**  
`endExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The ending timestamp for the difference calculation.  
`startExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The starting timestamp for the difference calculation.  
`unit` | `FirebaseFirestore.Pipelines.TimeUnit | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The unit of time for the difference (e.g., "day", "hour").  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the difference as an integer.  
  
#### Example
    
    
    typescript
    // Calculate the difference in days between two timestamp expressions.
    timestampDiff(field('endTime'), field('startTime'), 'day')
    

### Pipelines.timestampExtract(fieldName, part, timezone)
    
    
    export declare function timestampExtract(fieldName: string, part: firestore.Pipelines.TimePart, timezone?: string | Expression): FunctionExpression;

Creates an expression that extracts a specified part from a timestamp.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the timestamp.  
`part` | `firestore.Pipelines.TimePart`  
The part to extract from the timestamp (e.g., "year", "month", "day").  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for extraction. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1." Defaults to "UTC" if not specified.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the extracted part as an integer.  
  
#### Example
    
    
    typescript
    // Extract the year from the 'createdAt' timestamp.
    timestampExtract('createdAt', 'year')
    

### Pipelines.timestampExtract(fieldName, part, timezone)
    
    
    export declare function timestampExtract(fieldName: string, part: Expression, timezone?: string | Expression): FunctionExpression;

Creates an expression that extracts a specified part from a timestamp.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the timestamp.  
`part` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluating to the part to extract.  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for extraction. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1." Defaults to "UTC" if not specified.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the extracted part as an integer.  
  
#### Example
    
    
    typescript
    // Extract the part specified by the field 'part' from 'createdAt'.
    timestampExtract('createdAt', field('part'))
    

### Pipelines.timestampExtract(timestampExpression, part, timezone)
    
    
    export declare function timestampExtract(timestampExpression: Expression, part: firestore.Pipelines.TimePart, timezone?: string | Expression): FunctionExpression;

Creates an expression that extracts a specified part from a timestamp.

**Parameters**  
---  
**Name** | **Description**  
`timestampExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluating to the timestamp.  
`part` | `firestore.Pipelines.TimePart`  
The part to extract from the timestamp (e.g., "year", "month", "day").  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for extraction. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1." Defaults to "UTC" if not specified.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the extracted part as an integer.  
  
#### Example
    
    
    typescript
    // Extract the year from the timestamp returned by the expression.
    timestampExtract(field('createdAt'), 'year')
    

### Pipelines.timestampExtract(timestampExpression, part, timezone)
    
    
    export declare function timestampExtract(timestampExpression: Expression, part: Expression, timezone?: string | Expression): FunctionExpression;

Creates an expression that extracts a specified part from a timestamp.

**Parameters**  
---  
**Name** | **Description**  
`timestampExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluating to the timestamp.  
`part` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluating to the part to extract.  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for extraction. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1." Defaults to "UTC" if not specified.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the extracted part as an integer.  
  
#### Example
    
    
    typescript
    // Extract the part specified by the field 'part' from the timestamp.
    timestampExtract(field('createdAt'), field('part'))
    

### Pipelines.timestampSubtract(timestamp, unit, amount)
    
    
    export declare function timestampSubtract(timestamp: Expression, unit: Expression, amount: Expression): FunctionExpression;

Creates an expression that subtracts a specified amount of time from a timestamp.
    
    
    // Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
    timestampSubtract(field("timestamp"), field("unit"), field("amount"));
    

**Parameters**  
---  
**Name** | **Description**  
`timestamp` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the timestamp.  
`unit` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'.  
`amount` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression evaluates to amount of the unit.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
  
### Pipelines.timestampSubtract(timestamp, unit, amount)
    
    
    export declare function timestampSubtract(timestamp: Expression, unit: firestore.Pipelines.TimeUnit, amount: number): FunctionExpression;

Creates an expression that subtracts a specified amount of time from a timestamp.
    
    
    // Subtract 1 day from the 'timestamp' field.
    timestampSubtract(field("timestamp"), "day", 1);
    

**Parameters**  
---  
**Name** | **Description**  
`timestamp` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the timestamp.  
`unit` | `firestore.Pipelines.TimeUnit`  
The unit of time to subtract (e.g., "day", "hour").  
`amount` | `number`  
The amount of time to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
  
### Pipelines.timestampSubtract(fieldName, unit, amount)
    
    
    export declare function timestampSubtract(fieldName: string, unit: firestore.Pipelines.TimeUnit, amount: number): FunctionExpression;

Creates an expression that subtracts a specified amount of time from a timestamp represented by a field.
    
    
    // Subtract 1 day from the 'timestamp' field.
    timestampSubtract("timestamp", "day", 1);
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the timestamp.  
`unit` | `firestore.Pipelines.TimeUnit`  
The unit of time to subtract (e.g., "day", "hour").  
`amount` | `number`  
The amount of time to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
  
### Pipelines.timestampToUnixMicros(expr)
    
    
    export declare function timestampToUnixMicros(expr: Expression): FunctionExpression;

Creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).
    
    
    // Convert the 'timestamp' field to microseconds since epoch.
    timestampToUnixMicros(field("timestamp"));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of microseconds since epoch.  
  
### Pipelines.timestampToUnixMicros(fieldName)
    
    
    export declare function timestampToUnixMicros(fieldName: string): FunctionExpression;

Creates an expression that converts a timestamp field to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).
    
    
    // Convert the 'timestamp' field to microseconds since epoch.
    timestampToUnixMicros("timestamp");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of microseconds since epoch.  
  
### Pipelines.timestampToUnixMillis(expr)
    
    
    export declare function timestampToUnixMillis(expr: Expression): FunctionExpression;

Creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).
    
    
    // Convert the 'timestamp' field to milliseconds since epoch.
    timestampToUnixMillis(field("timestamp"));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of milliseconds since epoch.  
  
### Pipelines.timestampToUnixMillis(fieldName)
    
    
    export declare function timestampToUnixMillis(fieldName: string): FunctionExpression;

Creates an expression that converts a timestamp field to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).
    
    
    // Convert the 'timestamp' field to milliseconds since epoch.
    timestampToUnixMillis("timestamp");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of milliseconds since epoch.  
  
### Pipelines.timestampToUnixSeconds(expr)
    
    
    export declare function timestampToUnixSeconds(expr: Expression): FunctionExpression;

Creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).
    
    
    // Convert the 'timestamp' field to seconds since epoch.
    timestampToUnixSeconds(field("timestamp"));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of seconds since epoch.  
  
### Pipelines.timestampToUnixSeconds(fieldName)
    
    
    export declare function timestampToUnixSeconds(fieldName: string): FunctionExpression;

Creates an expression that converts a timestamp field to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).
    
    
    // Convert the 'timestamp' field to seconds since epoch.
    timestampToUnixSeconds("timestamp");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of seconds since epoch.  
  
### Pipelines.timestampTruncate(fieldName, granularity, timezone)
    
    
    export declare function timestampTruncate(fieldName: string, granularity: firestore.Pipelines.TimeGranularity, timezone?: string | Expression): FunctionExpression;

Creates an expression that truncates a timestamp to a specified granularity.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
Truncate the timestamp value contained in this field.  
`granularity` | `firestore.Pipelines.TimeGranularity`  
The granularity to truncate to.  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1".  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the truncated timestamp.  
  
#### Example
    
    
    typescript
    // Truncate the 'createdAt' timestamp to the beginning of the day.
    timestampTruncate('createdAt', 'day')
    

### Pipelines.timestampTruncate(fieldName, granularity, timezone)
    
    
    export declare function timestampTruncate(fieldName: string, granularity: Expression, timezone?: string | Expression): FunctionExpression;

Creates an expression that truncates a timestamp to a specified granularity.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
Truncate the timestamp value contained in this field.  
`granularity` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The granularity to truncate to.  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1".  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the truncated timestamp.  
  
#### Example
    
    
    typescript
    // Truncate the 'createdAt' timestamp to the granularity specified in the field 'granularity'.
    timestampTruncate('createdAt', field('granularity'))
    

### Pipelines.timestampTruncate(timestampExpression, granularity, timezone)
    
    
    export declare function timestampTruncate(timestampExpression: Expression, granularity: firestore.Pipelines.TimeGranularity, timezone?: string | Expression): FunctionExpression;

Creates an expression that truncates a timestamp to a specified granularity.

**Parameters**  
---  
**Name** | **Description**  
`timestampExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Truncate the timestamp value that is returned by this expression.  
`granularity` | `firestore.Pipelines.TimeGranularity`  
The granularity to truncate to.  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1".  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the truncated timestamp.  
  
#### Example
    
    
    typescript
    // Truncate the 'createdAt' timestamp to the beginning of the day.
     timestampTruncate(field('createdAt'), 'day')
    

### Pipelines.timestampTruncate(timestampExpression, granularity, timezone)
    
    
    export declare function timestampTruncate(timestampExpression: Expression, granularity: Expression, timezone?: string | Expression): FunctionExpression;

Creates an expression that truncates a timestamp to a specified granularity.

**Parameters**  
---  
**Name** | **Description**  
`timestampExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Truncate the timestamp value that is returned by this expression.  
`granularity` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The granularity to truncate to.  
`timezone` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1".  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the truncated timestamp.  
  
#### Example
    
    
    typescript
    // Truncate the 'createdAt' timestamp to the granularity specified in the field 'granularity'.
    timestampTruncate(field('createdAt'), field('granularity'))
    

### Pipelines.toLower(fieldName)
    
    
    export declare function toLower(fieldName: string): FunctionExpression;

Creates an expression that converts a string field to lowercase.
    
    
    // Convert the 'name' field to lowercase
    toLower("name");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the lowercase string.  
  
### Pipelines.toLower(stringExpression)
    
    
    export declare function toLower(stringExpression: Expression): FunctionExpression;

Creates an expression that converts a string expression to lowercase.
    
    
    // Convert the 'name' field to lowercase
    toLower(field("name"));
    

**Parameter**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to convert to lowercase.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the lowercase string.  
  
### Pipelines.toUpper(fieldName)
    
    
    export declare function toUpper(fieldName: string): FunctionExpression;

Creates an expression that converts a string field to uppercase.
    
    
    // Convert the 'title' field to uppercase
    toUpper("title");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the uppercase string.  
  
### Pipelines.toUpper(stringExpression)
    
    
    export declare function toUpper(stringExpression: Expression): FunctionExpression;

Creates an expression that converts a string expression to uppercase.
    
    
    // Convert the 'title' field to uppercase
    toUppercase(field("title"));
    

**Parameter**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string to convert to uppercase.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the uppercase string.  
  
### Pipelines.trim(fieldName, valueToTrim)
    
    
    export declare function trim(fieldName: string, valueToTrim?: string | Expression): FunctionExpression;

Creates an expression that removes leading and trailing whitespace from a string or byte array.
    
    
    // Trim whitespace from the 'userInput' field
    trim("userInput");
    
    // Trim quotes from the 'userInput' field
    trim("userInput", '"');
    

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the string or byte array.  
`valueToTrim` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Optional This parameter is treated as a set of characters or bytes that will be trimmed from the input. If not specified, then whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the trimmed string.  
  
### Pipelines.trim(stringExpression, valueToTrim)
    
    
    export declare function trim(stringExpression: Expression, valueToTrim?: string | Expression): FunctionExpression;

Creates an expression that removes leading and trailing characters from a string or byte array expression.
    
    
    // Trim whitespace from the 'userInput' field
    trim(field("userInput"));
    
    // Trim quotes from the 'userInput' field
    trim(field("userInput"), '"');
    

**Parameters**  
---  
**Name** | **Description**  
`stringExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the string or byte array to trim.  
`valueToTrim` | `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
Optional This parameter is treated as a set of characters or bytes that will be trimmed from the input. If not specified, then whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the trimmed string or byte array.  
  
### Pipelines.trunc(fieldName)
    
    
    export declare function trunc(fieldName: string): FunctionExpression;

Creates an expression that truncates the numeric value of a field to an integer.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field containing the number to truncate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the truncated value.  
  
#### Example
    
    
    typescript
    // Truncate the value of the 'rating' field.
    trunc("rating");
    

### Pipelines.trunc(expression)
    
    
    export declare function trunc(expression: Expression): FunctionExpression;

Creates an expression that truncates the numeric value of an expression to an integer.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which will be truncated.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the truncated value.  
  
#### Example
    
    
    typescript
    // Truncate the value of the 'rating' field.
    trunc(field("rating"));
    

### Pipelines.trunc(fieldName, decimalPlaces)
    
    
    export declare function trunc(fieldName: string, decimalPlaces: number | Expression): FunctionExpression;

Creates an expression that truncates a numeric value to the specified number of decimal places.

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field to truncate.  
`decimalPlaces` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
A constant or expression specifying the truncation precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the truncated value.  
  
#### Example
    
    
    typescript
    // Truncate the value of the 'rating' field to two decimal places.
    trunc("rating", 2);
    

### Pipelines.trunc(expression, decimalPlaces)
    
    
    export declare function trunc(expression: Expression, decimalPlaces: number | Expression): FunctionExpression;

Creates an expression that truncates a numeric value to the specified number of decimal places.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
An expression evaluating to a numeric value, which will be truncated.  
`decimalPlaces` | `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
A constant or expression specifying the truncation precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the truncated value.  
  
#### Example
    
    
    typescript
    // Truncate the value of the 'rating' field to two decimal places.
    trunc(field("rating"), constant(2));
    

### Pipelines.type(fieldName)
    
    
    export declare function type(fieldName: string): FunctionExpression;

Creates an expression that returns the data type of the data in the specified field.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the data type.  
  
#### Example
    
    
    typescript
    // Get the data type of the value in field 'title'
    type('title')
    

### Pipelines.type(expression)
    
    
    export declare function type(expression: Expression): FunctionExpression;

Creates an expression that returns the data type of an expression's result.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the data type.  
  
#### Example
    
    
    typescript
    // Get the data type of a conditional expression
    type(conditional(exists('foo'), constant(1), constant(true)))
    

### Pipelines.unixMicrosToTimestamp(expr)
    
    
    export declare function unixMicrosToTimestamp(expr: Expression): FunctionExpression;

Creates an expression that interprets an expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.
    
    
    // Interpret the 'microseconds' field as microseconds since epoch.
    unixMicrosToTimestamp(field("microseconds"));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the number of microseconds since epoch.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
  
### Pipelines.unixMicrosToTimestamp(fieldName)
    
    
    export declare function unixMicrosToTimestamp(fieldName: string): FunctionExpression;

Creates an expression that interprets a field's value as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.
    
    
    // Interpret the 'microseconds' field as microseconds since epoch.
    unixMicrosToTimestamp("microseconds");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the number of microseconds since epoch.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
  
### Pipelines.unixMillisToTimestamp(expr)
    
    
    export declare function unixMillisToTimestamp(expr: Expression): FunctionExpression;

Creates an expression that interprets an expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.
    
    
    // Interpret the 'milliseconds' field as milliseconds since epoch.
    unixMillisToTimestamp(field("milliseconds"));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the number of milliseconds since epoch.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
  
### Pipelines.unixMillisToTimestamp(fieldName)
    
    
    export declare function unixMillisToTimestamp(fieldName: string): FunctionExpression;

Creates an expression that interprets a field's value as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.
    
    
    // Interpret the 'milliseconds' field as milliseconds since epoch.
    unixMillisToTimestamp("milliseconds");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the number of milliseconds since epoch.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
  
### Pipelines.unixSecondsToTimestamp(expr)
    
    
    export declare function unixSecondsToTimestamp(expr: Expression): FunctionExpression;

Creates an expression that interprets an expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.
    
    
    // Interpret the 'seconds' field as seconds since epoch.
    unixSecondsToTimestamp(field("seconds"));
    

**Parameter**  
---  
**Name** | **Description**  
`expr` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the number of seconds since epoch.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
  
### Pipelines.unixSecondsToTimestamp(fieldName)
    
    
    export declare function unixSecondsToTimestamp(fieldName: string): FunctionExpression;

Creates an expression that interprets a field's value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.
    
    
    // Interpret the 'seconds' field as seconds since epoch.
    unixSecondsToTimestamp("seconds");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the number of seconds since epoch.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
  
### Pipelines.variable(name)
    
    
    export declare function variable(name: string): Expression;

Creates an expression that retrieves the value of a variable bound via `define()`.

**Parameter**  
---  
**Name** | **Description**  
`name` | `string`  
The name of the variable to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | An `Expression` representing the variable's value.  
  
#### Example
    
    
    typescript
    db.pipeline().collection("products")
      .define(
        field("price").multiply(0.9).as("discountedPrice"),
        field("stock").add(10).as("newStock")
      )
      .where(variable("discountedPrice").lessThan(100))
      .select(field("name"), variable("newStock"));
    

### Pipelines.vectorLength(vectorExpression)
    
    
    export declare function vectorLength(vectorExpression: Expression): FunctionExpression;

Creates an expression that calculates the length of a Firestore Vector.
    
    
    // Get the vector length (dimension) of the field 'embedding'.
    vectorLength(field("embedding"));
    

**Parameter**  
---  
**Name** | **Description**  
`vectorExpression` | `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`  
The expression representing the Firestore Vector.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the array.  
  
### Pipelines.vectorLength(fieldName)
    
    
    export declare function vectorLength(fieldName: string): FunctionExpression;

Creates an expression that calculates the length of a Firestore Vector represented by a field.
    
    
    // Get the vector length (dimension) of the field 'embedding'.
    vectorLength("embedding");
    

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `string`  
The name of the field representing the Firestore Vector.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the array.  
  
### Pipelines.xor(first, second, additionalConditions)
    
    
    export declare function xor(first: BooleanExpression, second: BooleanExpression, ...additionalConditions: BooleanExpression[]): BooleanExpression;

Creates an expression that performs a logical 'XOR' (exclusive OR) operation on multiple BooleanExprs.
    
    
    // Check if only one of the conditions is true: 'age' greater than 18, 'city' is "London",
    // or 'status' is "active".
    const condition = xor(
        greaterThan("age", 18),
        equal("city", "London"),
        equal("status", "active"));
    

**Parameters**  
---  
**Name** | **Description**  
`first` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The first condition.  
`second` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`  
The second condition.  
`additionalConditions` | `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)[]`  
Additional conditions to 'XOR' together.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the logical 'XOR' operation.  
  
### setLogFunction(logger)
    
    
    export declare function setLogFunction(logger: ((msg: string) => void) | null): void;

Sets or disables the log function for all active Firestore instances.

**Parameter**  
---  
**Name** | **Description**  
`logger` | `((msg: string) => void) | null`  
A log function that takes a message (such as `console.log`) or `null` to turn off logging.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
## Type Aliases 

### AggregateFieldType
    
    
    export type AggregateFieldType = ReturnType

The union of all `AggregateField` types that are supported by Firestore.

### AggregateType
    
    
    export type AggregateType = 'count' | 'avg' | 'sum';

Union type representing the aggregate type to be performed.

### DocumentChangeType
    
    
    export type DocumentChangeType = 'added' | 'removed' | 'modified';

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
