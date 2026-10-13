---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline
title: Class Pipelines.Pipeline (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:36.177767+00:00
---

# Class Pipelines.Pipeline (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Pipelines.Pipeline (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

The Pipeline class provides a flexible and expressive framework for building complex data transformation and query pipelines for Firestore.

A pipeline takes data sources, such as Firestore collections or collection groups, and applies a series of stages that are chained together. Each stage takes the output from the previous stage (or the data source) and produces an output for the next stage (or as the final output of the pipeline).

Expressions can be used within each stage to filter and transform data through the stage.

NOTE: The chained stages do not prescribe exactly how Firestore will execute the pipeline. Instead, Firestore only guarantees that the result is the same as if the chained stages were executed in order.

Usage Examples:

## Implements

firestore.Pipelines.Pipeline

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Example
    
    
    typescript
    const db: Firestore; // Assumes a valid firestore instance.
    
    // Example 1: Select specific fields and rename 'rating' to 'bookRating'
    const results1 = await db.pipeline()
        .collection('books')
        .select('title', 'author', field('rating').as('bookRating'))
        .execute();
    
    // Example 2: Filter documents where 'genre' is 'Science Fiction' and 'published' is after 1950
    const results2 = await db.pipeline()
        .collection('books')
        .where(and(field('genre').equal('Science Fiction'), field('published').greaterThan(1950)))
        .execute();
    
    // Example 3: Calculate the average rating of books published after 1980
    const results3 = await db.pipeline()
        .collection('books')
        .where(field('published').greaterThan(1980))
        .aggregate(average(field('rating')).as('averageRating'))
        .execute();
    

## Constructors 

### (constructor)(db, stages)
    
    
    constructor(db: Firestore | undefined, stages: Stage[]);

Constructs a new instance of the `Pipeline` class

**Parameters**  
---  
**Name** | **Description**  
`db` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore) | undefined`   
  
`stages` |  `Stage[]`   
  
  
## Methods 

### _execute(transactionOrReadTime, pipelineExecuteOptions)
    
    
    _execute(transactionOrReadTime?: Uint8Array | Timestamp | api.ITransactionOptions, pipelineExecuteOptions?: firestore.Pipelines.PipelineExecuteOptions): Promise<PipelineResponse>;

**Parameters**  
---  
**Name** | **Description**  
`transactionOrReadTime` |  `Uint8Array | [Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp) | google.firestore.v1.ITransactionOptions`   
  
`pipelineExecuteOptions` |  `firestore.Pipelines.PipelineExecuteOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<PipelineResponse>` |   
  
### _toProto(serializer)
    
    
    _toProto(serializer?: Serializer): api.IPipeline;

**Parameter**  
---  
**Name** | **Description**  
`serializer` |  `Serializer`   
  
**Returns**  
---  
**Type** | **Description**  
`api.IPipeline` |   
  
### _toStructuredPipeline(pipelineExecuteOptions)
    
    
    _toStructuredPipeline(pipelineExecuteOptions?: firestore.Pipelines.PipelineExecuteOptions): StructuredPipeline;

**Parameter**  
---  
**Name** | **Description**  
`pipelineExecuteOptions` |  `firestore.Pipelines.PipelineExecuteOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`StructuredPipeline` |   
  
### _validateUserData(ignoreUndefinedProperties)
    
    
    _validateUserData(ignoreUndefinedProperties: boolean): void;

**Parameter**  
---  
**Name** | **Description**  
`ignoreUndefinedProperties` |  `boolean`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addFields(field, additionalFields)
    
    
    addFields(field: firestore.Pipelines.Selectable, ...additionalFields: firestore.Pipelines.Selectable[]): Pipeline;

Adds new fields to outputs from previous stages.

This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones (if there is name overlaps).

The added fields are defined using `Selectable`s, which can be:

  * `Field`: References an existing document field. - `Expression`: Either a literal value (see `constant(value)`) or a computed value (see `Expression`) with an assigned alias using `Expression.as('alias')`.



**Parameters**  
---  
**Name** | **Description**  
`field` |  `firestore.Pipelines.Selectable`   
The first field to add to the documents, specified as a `Selectable`.  
`additionalFields` |  `FirebaseFirestore.Pipelines.Selectable[]`   
Optional additional fields to add to the documents, specified as `Selectable`s.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    firestore.pipeline().collection("books")
      .addFields(
        field("rating").as("bookRating"), // Rename 'rating' to 'bookRating'
        add(5, field("quantity")).as("totalCost")  // Calculate 'totalCost'
      );
    

### addFields(options)
    
    
    addFields(options: firestore.Pipelines.AddFieldsStageOptions): Pipeline;

Adds new fields to outputs from previous stages.

This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones (if there is name overlaps).

The added fields are defined using `Selectable`s, which can be:

  * `Field`: References an existing document field. - `Expression`: Either a literal value (see `constant(value)`) or a computed value (see `Expression`) with an assigned alias using `Expression.as('alias')`}.



**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.AddFieldsStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    firestore.pipeline().collection("books")
      .addFields(
        field("rating").as("bookRating"), // Rename 'rating' to 'bookRating'
        add(5, field("quantity")).as("totalCost")  // Calculate 'totalCost'
      );
    

### aggregate(accumulator, additionalAccumulators)
    
    
    aggregate(accumulator: firestore.Pipelines.AliasedAggregate, ...additionalAccumulators: firestore.Pipelines.AliasedAggregate[]): Pipeline;

Performs aggregation operations on the documents from previous stages.

This stage allows you to calculate aggregate values over a set of documents. You define the aggregations to perform using `AliasedAggregate` expressions which are typically results of calling on `AggregateFunction` instances.

**Parameters**  
---  
**Name** | **Description**  
`accumulator` |  `firestore.Pipelines.AliasedAggregate`   
The first `AliasedAggregate`, wrapping an `AggregateFunction` and providing a name for the accumulated results.  
`additionalAccumulators` |  `FirebaseFirestore.Pipelines.AliasedAggregate[]`   
Optional additional `AliasedAggregate`, each wrapping an `AggregateFunction` and providing a name for the accumulated results.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Calculate the average rating and the total number of books
    firestore.pipeline().collection("books")
        .aggregate(
            field("rating").average().as("averageRating"),
            countAll().as("totalBooks")
        );
    

### aggregate(options)
    
    
    aggregate(options: firestore.Pipelines.AggregateStageOptions): Pipeline;

Performs optionally grouped aggregation operations on the documents from previous stages.

This stage allows you to calculate aggregate values over a set of documents, optionally grouped by one or more fields or functions. You can specify:

  * **Grouping Fields or Functions:** One or more fields or functions to group the documents by. For each distinct combination of values in these fields, a separate group is created. If no grouping fields are provided, a single group containing all documents is used. Not specifying groups is the same as putting the entire inputs into one group.
  * **Accumulators:** One or more accumulation operations to perform within each group. These are defined using `AliasedAggregate` expressions, which are typically created by calling on `AggregateFunction` instances. Each aggregation calculates a value (e.g., sum, average, count) based on the documents within its group.



**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.AggregateStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Calculate the average rating for each genre.
    firestore.pipeline().collection("books")
      .aggregate({
          accumulators: [average(field("rating")).as("avg_rating")]
          groups: ["genre"]
          });
    

### define(aliasedExpression, additionalExpressions)
    
    
    define(aliasedExpression: firestore.Pipelines.AliasedExpression, ...additionalExpressions: firestore.Pipelines.AliasedExpression[]): Pipeline;

Binds one or more expressions to variable names within the pipeline's scope.

The `define` stage establishes a variable environment for the pipeline. It assigns the provided expressions to specific aliases. These variables remain in scope for all subsequent stages (and any nested subqueries), where they can be referenced using the `variable()` function.

This is primarily used to improve query ergonomics by preventing the duplication of complex expression trees, or to explicitly pass state from an outer pipeline into an inner subquery.

**Parameters**  
---  
**Name** | **Description**  
`aliasedExpression` |  `firestore.Pipelines.AliasedExpression`   
The first expression to bind to a variable.  
`additionalExpressions` |  `FirebaseFirestore.Pipelines.AliasedExpression[]`   
Optional additional expressions to bind to a variable.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Bind a mathematical expression to a variable to cleanly reference it multiple times.
    db.pipeline().collection("products")
      .define(
        field("price").multiply(0.8).as("discountedPrice")
      )
      .where(variable("discountedPrice").lessThan(50))
      .select("name", variable("discountedPrice"));
    

### define(options)
    
    
    define(options: firestore.Pipelines.DefineStageOptions): Pipeline;

Binds one or more expressions to variable names within the pipeline's scope.

The `define` stage establishes a variable environment for the pipeline. It assigns the provided expressions to specific aliases. These variables remain in scope for all subsequent stages (and any nested subqueries), where they can be referenced using the `variable()` function.

This is primarily used to improve query ergonomics by preventing the duplication of complex expression trees, or to explicitly pass state from an outer pipeline into an inner subquery.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.DefineStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Bind a mathematical expression to a variable to cleanly reference it multiple times.
    db.pipeline().collection("products")
      .define({
        variables: [field("price").multiply(0.8).as("discountedPrice")]
      })
      .where(variable("discountedPrice").lessThan(50))
      .select("name", variable("discountedPrice"));
    

### delete()
    
    
    delete(): Pipeline;

Performs a delete operation on documents from previous stages.

**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
**Example**
    
    
    typescript
    // Deletes all documents in the "books" collection.
    firestore.pipeline().collection("books")
       .delete();
    

A new object with this stage appended to the stage list.

### distinct(group, additionalGroups)
    
    
    distinct(group: string | firestore.Pipelines.Selectable, ...additionalGroups: Array<string | firestore.Pipelines.Selectable>): Pipeline;

Returns a set of distinct values from the inputs to this stage.

This stage runs through the results from previous stages to include only results with unique combinations of `Expression` values.

The parameters to this stage are defined using `Selectable` expressions or strings:

  * `string`: Name of an existing field - `Field`: References an existing document field. - `AliasedExpression`: Represents the result of a function with an assigned alias name using .



**Parameters**  
---  
**Name** | **Description**  
`group` |  `string | FirebaseFirestore.Pipelines.Selectable`   
The `Selectable` expression or field name to consider when determining distinct value combinations.  
`additionalGroups` |  `Array<string | FirebaseFirestore.Pipelines.Selectable>`   
Optional additional `Selectable` expressions to consider when determining distinct value combinations or strings representing field names.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Get a list of unique author names in uppercase and genre combinations.
    firestore.pipeline().collection("books")
        .distinct(toUppercase(field("author")).as("authorName"), field("genre"), "publishedAt")
        .select("authorName");
    

### distinct(options)
    
    
    distinct(options: firestore.Pipelines.DistinctStageOptions): Pipeline;

Returns a set of distinct values from the inputs to this stage.

This stage runs through the results from previous stages to include only results with unique combinations of `Expression` values.

The parameters to this stage are defined using `Selectable` expressions or strings:

  * `string`: Name of an existing field - `Field`: References an existing document field. - `AliasedExpression`: Represents the result of a function with an assigned alias name using .



**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.DistinctStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Get a list of unique author names in uppercase and genre combinations.
    firestore.pipeline().collection("books")
        .distinct(toUppercase(field("author")).as("authorName"), field("genre"), "publishedAt")
        .select("authorName");
    

### execute(pipelineExecuteOptions)
    
    
    execute(pipelineExecuteOptions?: firestore.Pipelines.PipelineExecuteOptions): Promise<PipelineSnapshot>;

Executes this pipeline and returns a Promise to represent the asynchronous operation.

The returned Promise can be used to track the progress of the pipeline execution and retrieve the results (or handle any errors) asynchronously.

The pipeline results are returned in a `PipelineSnapshot` object, which contains a list of `PipelineResult` objects. Each `PipelineResult` typically represents a single key/value map that has passed through all the stages of the pipeline, however this might differ depending on the stages involved in the pipeline. For example:

  * If there are no stages or only transformation stages, each `PipelineResult` represents a single document.
  * If there is an aggregation, only a single `PipelineResult` is returned, representing the aggregated results over the entire dataset .
  * If there is an aggregation stage with grouping, each `PipelineResult` represents a distinct group and its associated aggregated values.



**Parameter**  
---  
**Name** | **Description**  
`pipelineExecuteOptions` |  `firestore.Pipelines.PipelineExecuteOptions`   
Optionally specify pipeline execution behavior.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[PipelineSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesnapshot)>` | A Promise representing the asynchronous pipeline execution.  
**Example**
    
    
    typescript
    const futureResults = await firestore.pipeline().collection('books')
        .where(greaterThan(field('rating'), 4.5))
        .select('title', 'author', 'rating')
        .execute();
    

### findNearest(options)
    
    
    findNearest(options: firestore.Pipelines.FindNearestStageOptions): Pipeline;

Performs a vector proximity search on the documents from the previous stage, returning the K-nearest documents based on the specified query `vectorValue` and `distanceMeasure`. The returned documents will be sorted in order from nearest to furthest from the query `vectorValue`.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.FindNearestStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Find the 10 most similar books based on the book description.
    const bookDescription = "Lorem ipsum...";
    const queryVector: number[] = ...; // compute embedding of `bookDescription`
    
    firestore.pipeline().collection("books")
        .findNearest({
          field: 'embedding',
          vectorValue: queryVector,
          distanceMeasure: 'euclidean',
          limit: 10,                        // optional
          distanceField: 'computedDistance' // optional
        });
    

### limit(limit)
    
    
    limit(limit: number): Pipeline;

Limits the maximum number of documents returned by previous stages to `limit`.

This stage is particularly useful when you want to retrieve a controlled subset of data from a potentially large result set. It's often used for:

  * **Pagination:** In combination with `offset` to retrieve specific pages of results.
  * **Limiting Data Retrieval:** To prevent excessive data transfer and improve performance, especially when dealing with large collections.



**Parameter**  
---  
**Name** | **Description**  
`limit` |  `number`   
The maximum number of documents to return.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Limit the results to the top 10 highest-rated books
    firestore.pipeline().collection('books')
        .sort(field('rating').descending())
        .limit(10);
    

### limit(options)
    
    
    limit(options: firestore.Pipelines.LimitStageOptions): Pipeline;

Limits the maximum number of documents returned by previous stages to `limit`.

This stage is particularly useful when you want to retrieve a controlled subset of data from a potentially large result set. It's often used for:

  * **Pagination:** In combination with `offset` to retrieve specific pages of results.
  * **Limiting Data Retrieval:** To prevent excessive data transfer and improve performance, especially when dealing with large collections.



**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.LimitStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Limit the results to the top 10 highest-rated books
    firestore.pipeline().collection('books')
        .sort(field('rating').descending())
        .limit(10);
    

### offset(offset)
    
    
    offset(offset: number): Pipeline;

Skips the first `offset` number of documents from the results of previous stages.

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with to control the size of each page.

**Parameter**  
---  
**Name** | **Description**  
`offset` |  `number`   
The number of documents to skip.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Retrieve the second page of 20 results
    firestore.pipeline().collection('books')
        .sort(field('published').descending())
        .offset(20)  // Skip the first 20 results
        .limit(20);   // Take the next 20 results
    

### offset(options)
    
    
    offset(options: firestore.Pipelines.OffsetStageOptions): Pipeline;

Skips the first `offset` number of documents from the results of previous stages.

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with `limit` to control the size of each page.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.OffsetStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Retrieve the second page of 20 results
    firestore.pipeline().collection('books')
        .sort(field('published').descending())
        .offset(20)  // Skip the first 20 results
        .limit(20);   // Take the next 20 results
    

### rawStage(name, params, options)
    
    
    rawStage(name: string, params: unknown[], options?: {
            [key: string]: Expression | unknown;
        }): Pipeline;

Adds a raw stage to the pipeline.

This method provides a flexible way to extend the pipeline's functionality by adding custom stages. Each raw stage is defined by a unique `name` and a set of `params` that control its behavior.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
The unique name of the raw stage to add.  
`params` |  `unknown[]`   
A list of parameters to configure the raw stage's behavior.  
`options` |  `{ [key: string]: [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown; }`   
An object of key value pairs that specifies optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Examples**

Assuming there is no 'where' stage available in SDK:
    
    
    typescript
    // Assume we don't have a built-in 'where' stage
    firestore.pipeline().collection('books')
        .rawStage('where', [field('published').lessThan(1900)]) // Custom 'where' stage
        .select('title', 'author');
    

### removeFields(fieldValue, additionalFields)
    
    
    removeFields(fieldValue: firestore.Pipelines.Field | string, ...additionalFields: Array<firestore.Pipelines.Field | string>): Pipeline;

Remove fields from outputs of previous stages.

**Parameters**  
---  
**Name** | **Description**  
`fieldValue` |  `FirebaseFirestore.Pipelines.Field | string`   
The first field to remove.  
`additionalFields` |  `Array<FirebaseFirestore.Pipelines.Field | string>`   
Optional additional fields to remove.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    firestore.pipeline().collection('books')
      // removes field 'rating' and 'cost' from the previous stage outputs.
      .removeFields(
        field('rating'),
        'cost'
      );
    

### removeFields(options)
    
    
    removeFields(options: firestore.Pipelines.RemoveFieldsStageOptions): Pipeline;

Remove fields from outputs of previous stages.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.RemoveFieldsStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    firestore.pipeline().collection('books')
      // removes field 'rating' and 'cost' from the previous stage outputs.
      .removeFields(
        field('rating'),
        'cost'
      );
    

### replaceWith(fieldName)
    
    
    replaceWith(fieldName: string): Pipeline;

Fully overwrites all fields in a document with those coming from a nested map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

**Parameter**  
---  
**Name** | **Description**  
`fieldName` |  `string`   
The `Field` field containing the nested map.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Input.
    // {
    //  'name': 'John Doe Jr.',
    //  'parents': {
    //    'father': 'John Doe Sr.',
    //    'mother': 'Jane Doe'
    //   }
    // }
    
    // Emit parents as document.
    firestore.pipeline().collection('people').replaceWith('parents');
    
    // Output
    // {
    //  'father': 'John Doe Sr.',
    //  'mother': 'Jane Doe'
    // }
    

### replaceWith(expr)
    
    
    replaceWith(expr: firestore.Pipelines.Expression): Pipeline;

Fully overwrites all fields in a document with those coming from a map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

**Parameter**  
---  
**Name** | **Description**  
`expr` |  `firestore.Pipelines.Expression`   
An `Expression` that when returned evaluates to a map.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Input.
    // {
    //  'name': 'John Doe Jr.',
    //  'parents': {
    //    'father': 'John Doe Sr.',
    //    'mother': 'Jane Doe'
    //   }
    // }
    
    // Emit parents as document.
    firestore.pipeline().collection('people').replaceWith(map({
      foo: 'bar',
      info: {
        name: field('name')
      }
    }));
    
    // Output
    // {
    //  'father': 'John Doe Sr.',
    //  'mother': 'Jane Doe'
    // }
    

### replaceWith(options)
    
    
    replaceWith(options: firestore.Pipelines.ReplaceWithStageOptions): Pipeline;

Fully overwrites all fields in a document with those coming from a map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.ReplaceWithStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Input.
    // {
    //  'name': 'John Doe Jr.',
    //  'parents': {
    //    'father': 'John Doe Sr.',
    //    'mother': 'Jane Doe'
    //   }
    // }
    
    // Emit parents as document.
    firestore.pipeline().collection('people').replaceWith(map({
      foo: 'bar',
      info: {
        name: field('name')
      }
    }));
    
    // Output
    // {
    //  'father': 'John Doe Sr.',
    //  'mother': 'Jane Doe'
    // }
    

### sample(documents)
    
    
    sample(documents: number): Pipeline;

Performs a pseudo-random sampling of the documents from the previous stage.

This stage will filter documents pseudo-randomly. The parameter specifies how number of documents to be returned.

Examples:

**Parameter**  
---  
**Name** | **Description**  
`documents` |  `number`   
The number of documents to sample.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Sample 25 books, if available.
    firestore.pipeline().collection('books')
        .sample(25);
    

### sample(options)
    
    
    sample(options: firestore.Pipelines.SampleStageOptions): Pipeline;

Performs a pseudo-random sampling of the documents from the previous stage.

This stage will filter documents pseudo-randomly. The 'options' parameter specifies how sampling will be performed. See `SampleOptions` for more information.

Examples:

// Sample 10 books, if available. firestore.pipeline().collection("books") .sample({ documents: 10 });

// Sample 50% of books. firestore.pipeline().collection("books") .sample({ percentage: 0.5 });

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.SampleStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
  
### search(options)
    
    
    search(options: firestore.Pipelines.SearchStageOptions): Pipeline;

Add a search stage to the Pipeline.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.SearchStageOptions`   
An object that specifies required and optional parameters for the stage. A new `Pipeline` object with this stage appended to the stage list.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
**Remarks**

A limited set of expressions are supported in the search stage.

**Example**
    
    
    typescript
    db.pipeline().collection('restaurants').search({
      query: documentMatches('breakfast')
    })
    

### select(selection, additionalSelections)
    
    
    select(selection: firestore.Pipelines.Selectable | string, ...additionalSelections: Array<firestore.Pipelines.Selectable | string>): Pipeline;

Selects or creates a set of fields from the outputs of previous stages.

The selected fields are defined using `Selectable` expressions, which can be:

  * `string`: Name of an existing field
  * `Field`: References an existing field.
  * `AliasedExpression`: Represents the result of a function with an assigned alias name using 



If no selections are provided, the output of this stage is empty. Use instead if only additions are desired.

**Parameters**  
---  
**Name** | **Description**  
`selection` |  `FirebaseFirestore.Pipelines.Selectable | string`   
The first field to include in the output documents, specified as `Selectable` expression or string value representing the field name.  
`additionalSelections` |  `Array<FirebaseFirestore.Pipelines.Selectable | string>`   
Optional additional fields to include in the output documents, specified as `Selectable` expressions or `string` values representing field names.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    db.pipeline().collection("books")
      .select(
        "firstName",
        field("lastName"),
        field("address").toUppercase().as("upperAddress"),
      );
    

### select(options)
    
    
    select(options: firestore.Pipelines.SelectStageOptions): Pipeline;

Selects or creates a set of fields from the outputs of previous stages.

The selected fields are defined using `Selectable` expressions, which can be:

  * `string`: Name of an existing field
  * `Field`: References an existing field.
  * `AliasedExpression`: Represents the result of a function with an assigned alias name using 



If no selections are provided, the output of this stage is empty. Use instead if only additions are desired.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.SelectStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    db.pipeline().collection("books")
      .select(
        "firstName",
        field("lastName"),
        field("address").toUppercase().as("upperAddress"),
      );
    

### sort(ordering, additionalOrderings)
    
    
    sort(ordering: firestore.Pipelines.Ordering, ...additionalOrderings: firestore.Pipelines.Ordering[]): Pipeline;

Sorts the documents from previous stages based on one or more `Ordering` criteria.

This stage allows you to order the results of your pipeline. You can specify multiple `Ordering` instances to sort by multiple fields in ascending or descending order. If documents have the same value for a field used for sorting, the next specified ordering will be used. If all orderings result in equal comparison, the documents are considered equal and the order is unspecified.

**Parameters**  
---  
**Name** | **Description**  
`ordering` |  `firestore.Pipelines.Ordering`   
The first `Ordering` instance specifying the sorting criteria.  
`additionalOrderings` |  `FirebaseFirestore.Pipelines.Ordering[]`   
Optional additional `Ordering` instances specifying the additional sorting criteria.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Sort books by rating in descending order, and then by title in ascending order for books
    // with the same rating
    firestore.pipeline().collection("books")
        .sort(
            Ordering.of(field("rating")).descending(),
            Ordering.of(field("title"))  // Ascending order is the default
        );
    

### sort(options)
    
    
    sort(options: firestore.Pipelines.SortStageOptions): Pipeline;

Sorts the documents from previous stages based on one or more `Ordering` criteria.

This stage allows you to order the results of your pipeline. You can specify multiple `Ordering` instances to sort by multiple fields in ascending or descending order. If documents have the same value for a field used for sorting, the next specified ordering will be used. If all orderings result in equal comparison, the documents are considered equal and the order is unspecified.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.SortStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Sort books by rating in descending order, and then by title in ascending order for books
    // with the same rating
    firestore.pipeline().collection("books")
        .sort(
            Ordering.of(field("rating")).descending(),
            Ordering.of(field("title"))  // Ascending order is the default
        );
    

### stream()
    
    
    stream(): NodeJS.ReadableStream;

Executes this pipeline and streams the results as `PipelineResult`s.

**Returns**  
---  
**Type** | **Description**  
`NodeJS.ReadableStream` | {Stream.  
**Example**
    
    
    typescript
    firestore.pipeline().collection('books')
        .where(greaterThan(field('rating'), 4.5))
        .select('title', 'author', 'rating')
        .stream()
        .on('data', (pipelineResult) => {})
        .on('end', () => {});
    

### toArrayExpression()
    
    
    toArrayExpression(): firestore.Pipelines.Expression;

Converts this Pipeline into an expression that evaluates to an array of map (objects), where each result document of the pipeline is represented as a map in the returned array.

Result Unwrapping:

  * If the items have a single field, their values are unwrapped and returned directly in the array.
  * If the items have multiple fields, they are returned as objects in the array.



**Returns**  
---  
**Type** | **Description**  
`firestore.Pipelines.Expression` | An `Expression` representing the execution of this pipeline.  
**Example**
    
    
    typescript
    // Get a list of reviewers for each book
    db.pipeline().collection("books")
        .define(field("id").as("current_book_id"))
        .addFields(
            db.pipeline().collection("reviews")
                .where(field("book_id").equal(variable("current_book_id")))
                .select(field("reviewer"))
                .toArrayExpression()
                .as("reviewers")
        );
    

Output:
    
    
    json
    [
      {
        "id": "1",
        "title": "1984",
        "reviewers": ["Alice", "Bob"]
      }
    ]
    

Multiple Fields:
    
    
    typescript
    // Get a list of reviews (reviewer and rating) for each book
    db.pipeline().collection("books")
        .define(field("id").as("current_book_id"))
        .addFields(
            db.pipeline().collection("reviews")
                .where(field("book_id").equal(variable("current_book_id")))
                .select(field("reviewer"), field("rating"))
                .toArrayExpression()
                .as("reviews")
       );
    

Output:
    
    
    json
    [
      {
        "id": "1",
        "title": "1984",
        "reviews": [
          { "reviewer": "Alice", "rating": 5 },
          { "reviewer": "Bob", "rating": 4 }
        ]
      }
    ]
    

### toScalarExpression()
    
    
    toScalarExpression(): firestore.Pipelines.Expression;

Converts this Pipeline into an expression that evaluates to a single scalar result.

**Runtime Validation:** The runtime validates that the result set contains zero or one item. If zero items, it evaluates to `null`.

Result Unwrapping:

  * If the item has a single field, its value is unwrapped and returned directly.
  * If the item has multiple fields, they are returned as an object.



**Returns**  
---  
**Type** | **Description**  
`firestore.Pipelines.Expression` | An `Expression` representing the execution of this pipeline.  
**Example**
    
    
    typescript
    // Calculate average rating for a restaurant
    db.pipeline().collection("restaurants")
        .define(field("id").as("current_restaurant_id"))
        .addFields(
          db.pipeline().collection("reviews")
            .where(field("restaurant_id").equal(variable("current_restaurant_id")))
            .aggregate(average("rating").as("avg"))
            // Unwraps the single "avg" field to a scalar double
            .toScalarExpression().as("average_rating")
       );
    

Output:
    
    
    json
    {
      "name": "The Burger Joint",
      "average_rating": 4.5
    }
    

Multiple Fields:
    
    
    typescript
    // Calculate average rating AND count for a restaurant
    db.pipeline().collection("restaurants")
        .define(field("id").as("current_restaurant_id"))
        .addFields(
          db.pipeline().collection("reviews")
            .where(field("restaurant_id").equal(variable("current_restaurant_id")))
            .aggregate(
              average("rating").as("avg"),
              count().as("count")
            )
            // Returns an object with "avg" and "count" fields
            .toScalarExpression().as("stats")
       );
    

Output:
    
    
    json
    {
      "name": "The Burger Joint",
      "stats": {
        "avg": 4.5,
        "count": 100
      }
    }
    

### union(other)
    
    
    union(other: firestore.Pipelines.Pipeline): Pipeline;

Performs union of all documents from two pipelines, including duplicates.

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the `other` `Pipeline` given in parameter. The order of documents emitted from this stage is undefined.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `firestore.Pipelines.Pipeline`   
The other `Pipeline` that is part of union.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Emit documents from books collection and magazines collection.
    firestore.pipeline().collection('books')
        .union(firestore.pipeline().collection('magazines'));
    

### union(options)
    
    
    union(options: firestore.Pipelines.UnionStageOptions): Pipeline;

Performs union of all documents from two pipelines, including duplicates.

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the `other` `Pipeline` given in parameter. The order of documents emitted from this stage is undefined.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.UnionStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Emit documents from books collection and magazines collection.
    firestore.pipeline().collection('books')
        .union(firestore.pipeline().collection('magazines'));
    

### unnest(selectable, indexField)
    
    
    unnest(selectable: firestore.Pipelines.Selectable, indexField?: string): Pipeline;

Produces a document for each element in an input array.

For each previous stage document, this stage will emit zero or more augmented documents. The input array specified by the `selectable` parameter, will emit an augmented document for each input array element. The input array element will augment the previous stage document by setting the `alias` field with the array element value.

When `selectable` evaluates to a non-array value (ex: number, null, absent), then the stage becomes a no-op for the current input document, returning it as is with the `alias` field absent.

No documents are emitted when `selectable` evaluates to an empty array.

**Parameters**  
---  
**Name** | **Description**  
`selectable` |  `firestore.Pipelines.Selectable`   
A selectable expression defining the field to unnest and the alias to use for each un-nested element in the output documents.  
`indexField` |  `string`   
An optional string value specifying the field path to write the offset (starting at zero) into the array the un-nested element is from  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Input:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tags": [ "comedy", "space", "adventure" ], ... }
    
    // Emit a book document for each tag of the book.
    firestore.pipeline().collection("books")
        .unnest(field("tags").as('tag'), 'tagIndex');
    
    // Output:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "comedy", "tagIndex": 0, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "space", "tagIndex": 1, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "adventure", "tagIndex": 2, ... }
    

### unnest(options)
    
    
    unnest(options: firestore.Pipelines.UnnestStageOptions): Pipeline;

Produces a document for each element in an input array.

For each previous stage document, this stage will emit zero or more augmented documents. The input array specified by the `selectable` parameter, will emit an augmented document for each input array element. The input array element will augment the previous stage document by setting the `alias` field with the array element value.

When `selectable` evaluates to a non-array value (ex: number, null, absent), then the stage becomes a no-op for the current input document, returning it as is with the `alias` field absent.

No documents are emitted when `selectable` evaluates to an empty array.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.UnnestStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new `Pipeline` object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    // Input:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tags": [ "comedy", "space", "adventure" ], ... }
    
    // Emit a book document for each tag of the book.
    firestore.pipeline().collection("books")
        .unnest(field("tags").as('tag'), 'tagIndex');
    
    // Output:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "comedy", "tagIndex": 0, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "space", "tagIndex": 1, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "adventure", "tagIndex": 2, ... }
    

### update()
    
    
    update(): Pipeline;

Performs an update operation using documents from previous stages.

A new object with this stage appended to the stage list.

**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### update(transformedFields)
    
    
    update(transformedFields: AliasedExpression[]): Pipeline;

Performs an update operation using documents from previous stages.

**Parameter**  
---  
**Name** | **Description**  
`transformedFields` |  `[AliasedExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aliasedexpression)[]`   
The list of transformations to apply. A new object with this stage appended to the stage list.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### where(condition)
    
    
    where(condition: firestore.Pipelines.BooleanExpression): Pipeline;

Filters the documents from previous stages to only include those matching the specified `BooleanExpression`.

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL. You can filter documents based on their field values, using implementations of `BooleanExpression`, typically including but not limited to:

  * field comparators: , (less than), (greater than), etc.
  * logical operators: , , , etc.
  * advanced functions: , , etc.



**Parameter**  
---  
**Name** | **Description**  
`condition` |  `firestore.Pipelines.BooleanExpression`   
The `BooleanExpression` to apply.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    firestore.pipeline().collection("books")
      .where(
        and(
            greaterThan(field("rating"), 4.0),   // Filter for ratings greater than 4.0
            field("genre").equal("Science Fiction") // Equivalent to greaterThan("genre", "Science Fiction")
        )
      );
    

### where(options)
    
    
    where(options: firestore.Pipelines.WhereStageOptions): Pipeline;

Filters the documents from previous stages to only include those matching the specified `BooleanExpression`.

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL. You can filter documents based on their field values, using implementations of `BooleanExpression`, typically including but not limited to:

  * field comparators: , (less than), (greater than), etc.
  * logical operators: , , , etc.
  * advanced functions: , , etc.



**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.WhereStageOptions`   
An object that specifies required and optional parameters for the stage.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` | A new Pipeline object with this stage appended to the stage list.  
**Example**
    
    
    typescript
    firestore.pipeline().collection("books")
      .where(
        and(
            greaterThan(field("rating"), 4.0),   // Filter for ratings greater than 4.0
            field("genre").equal("Science Fiction") // Equivalent to greaterThan("genre", "Science Fiction")
        )
      );
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
