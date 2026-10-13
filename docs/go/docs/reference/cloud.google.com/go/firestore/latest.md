---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/
title: Cloud Firestore API - Package cloud.google.com/go/firestore (v1.26.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:33.688400+00:00
---

# Cloud Firestore API - Package cloud.google.com/go/firestore (v1.26.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Firestore API - Package cloud.google.com/go/firestore (v1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/firestore). 

Package firestore provides a client for reading and writing to a Cloud Firestore database. 

See <https://cloud.google.com/firestore/docs> for an introduction to Cloud Firestore and additional help on using the Firestore API. 

See <https://godoc.org/cloud.google.com/go> for authentication, timeouts, connection pooling and similar aspects of this package. 

Note: you can't use both Cloud Firestore and Cloud Datastore in the same project. 

## Creating a Client

To start working with this package, create a client with a project ID:
    
    
    ctx := context.Background()
    client, err := firestore.NewClient(ctx, "projectID")
    if err != nil {
        // TODO: Handle error.
    }

## CollectionRefs and DocumentRefs

In Firestore, documents are sets of key-value pairs, and collections are groups of documents. A Firestore database consists of a hierarchy of alternating collections and documents, referred to by slash-separated paths like "States/California/Cities/SanFrancisco". 

This client is built around references to collections and documents. CollectionRefs and DocumentRefs are lightweight values that refer to the corresponding database entities. Creating a ref does not involve any network traffic.
    
    
    states := client.Collection("States")
    ny := states.Doc("NewYork")
    // Or, in a single call:
    ny = client.Doc("States/NewYork")

## Reading

Use DocumentRef.Get to read a document. The result is a DocumentSnapshot. Call its Data method to obtain the entire document contents as a map.
    
    
    docsnap, err := ny.Get(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    dataMap := docsnap.Data()
    fmt.Println(dataMap)

You can also obtain a single field with DataAt, or extract the data into a struct with DataTo. With the type definition
    
    
    type State struct {
        Capital    string  `firestore:"capital"`
        Population float64 `firestore:"pop"` // in millions
    }

we can extract the document's data into a value of type State:
    
    
    var nyData State
    if err := docsnap.DataTo(&nyData); err != nil {
        // TODO: Handle error.
    }

Note that this client supports struct tags beginning with "firestore:" that work like the tags of the encoding/json package, letting you rename fields, ignore them, or omit their values when empty. 

To retrieve multiple documents from their references in a single call, use Client.GetAll.
    
    
    docsnaps, err := client.GetAll(ctx, []*firestore.DocumentRef{
        states.Doc("Wisconsin"), states.Doc("Ohio"),
    })
    if err != nil {
        // TODO: Handle error.
    }
    for _, ds := range docsnaps {
        _ = ds // TODO: Use ds.
    }

## Writing

For writing individual documents, use the methods on DocumentReference. Create creates a new document.
    
    
    wr, err := ny.Create(ctx, State{
        Capital:    "Albany",
        Population: 19.8,
    })
    if err != nil {
        // TODO: Handle error.
    }
    fmt.Println(wr)

The first return value is a WriteResult, which contains the time at which the document was updated. 

Create fails if the document exists. Another method, Set, either replaces an existing document or creates a new one.
    
    
    ca := states.Doc("California")
    _, err = ca.Set(ctx, State{
        Capital:    "Sacramento",
        Population: 39.14,
    })

To update some fields of an existing document, use Update. It takes a list of paths to update and their corresponding values.
    
    
    _, err = ca.Update(ctx, []firestore.Update{{Path: "capital", Value: "Sacramento"}})

Use DocumentRef.Delete to delete a document.
    
    
    _, err = ny.Delete(ctx)

## Preconditions

You can condition Deletes or Updates on when a document was last changed. Specify these preconditions as an option to a Delete or Update method. The check and the write happen atomically with a single RPC.
    
    
    docsnap, err = ca.Get(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    _, err = ca.Update(ctx,
        []firestore.Update{{Path: "capital", Value: "Sacramento"}},
        firestore.LastUpdateTime(docsnap.UpdateTime))

Here we update a doc only if it hasn't changed since we read it. You could also do this with a transaction. 

To perform multiple writes at once, use a WriteBatch. Its methods chain for convenience. 

WriteBatch.Commit sends the collected writes to the server, where they happen atomically.
    
    
    writeResults, err := client.Batch().
        Create(ny, State{Capital: "Albany"}).
        Update(ca, []firestore.Update{{Path: "capital", Value: "Sacramento"}}).
        Delete(client.Doc("States/WestDakota")).
        Commit(ctx)

## Queries

You can use SQL to select documents from a collection. Begin with the collection, and build up a query using Select, Where and other methods of Query.
    
    
    q := states.Where("pop", ">", 10).OrderBy("pop", firestore.Desc)

Supported operators include '<', '<=', '>', '>=', '==', 'in', 'array-contains', and 'array-contains-any'. 

Call the Query's Documents method to get an iterator, and use it like the other Google Cloud Client iterators.
    
    
    iter := q.Documents(ctx)
    defer iter.Stop()
    for {
        doc, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            // TODO: Handle error.
        }
        fmt.Println(doc.Data())
    }

To get all the documents in a collection, you can use the collection itself as a query.
    
    
    iter = client.Collection("States").Documents(ctx)

Firestore supports similarity search over embedding vectors. See Query.FindNearest for details. 

## Collection Group Partition Queries

You can partition the documents of a Collection Group allowing for smaller subqueries.
    
    
    collectionGroup = client.CollectionGroup("States")
    partitions, err = collectionGroup.GetPartitionedQueries(ctx, 20)

You can also Serialize/Deserialize queries making it possible to run/stream the queries elsewhere; another process or machine for instance.
    
    
    queryProtos := make([][]byte, 0)
    for _, query := range partitions {
        protoBytes, err := query.Serialize()
        // handle err
        queryProtos = append(queryProtos, protoBytes)
        ...
    }
    
    for _, protoBytes := range queryProtos {
        query, err := client.CollectionGroup("").Deserialize(protoBytes)
        ...
    }

## Transactions

Use a transaction to execute reads and writes atomically. All reads must happen before any writes. Transaction creation, commit, rollback and retry are handled for you by the Client.RunTransaction method; just provide a function and use the read and write methods of the Transaction passed to it.
    
    
    ny := client.Doc("States/NewYork")
    err := client.RunTransaction(ctx, func(ctx context.Context, tx *firestore.Transaction) error {
        doc, err := tx.Get(ny) // tx.Get, NOT ny.Get!
        if err != nil {
            return err
        }
        pop, err := doc.DataAt("pop")
        if err != nil {
            return err
        }
        return tx.Update(ny, []firestore.Update{{Path: "pop", Value: pop.(float64) + 0.2}})
    })
    if err != nil {
        // TODO: Handle error.
    }

## Google Cloud Firestore Emulator

This package supports the Cloud Firestore emulator, which is useful for testing and development. Environment variables are used to indicate that Firestore traffic should be directed to the emulator instead of the production Firestore service. 

To install and run the emulator and its environment variables, see the documentation at <https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore/>. Once the emulator is running, set FIRESTORE_EMULATOR_HOST to the API endpoint.
    
    
    // Set FIRESTORE_EMULATOR_HOST environment variable.
    err := os.Setenv("FIRESTORE_EMULATOR_HOST", "localhost:9000")
    if err != nil {
        // TODO: Handle error.
    }
    // Create client as usual.
    client, err := firestore.NewClient(ctx, "my-project-id")
    if err != nil {
        // TODO: Handle error.
    }
    defer client.Close()

##  Constants 

### Delete, ServerTimestamp
    
    
    const (
    	// Delete is used as a value in a call to Update or Set with merge to indicate
    	// that the corresponding key should be deleted.
    	Delete sentinel = [iota](https://pkg.go.dev/builtin#iota)
    
    	// ServerTimestamp is used as a value in a call to Update to indicate that the
    	// key's value should be set to the time at which the server processed
    	// the request.
    	//
    	// ServerTimestamp must be the value of a field directly; it cannot appear in
    	// array or struct values, or in any value that is itself inside an array or
    	// struct.
    	ServerTimestamp
    )

### DefaultDatabaseID
    
    
    const DefaultDatabaseID = "(default)"

DefaultDatabaseID is name of the default database

### DefaultTransactionMaxAttempts
    
    
    const DefaultTransactionMaxAttempts = 5

DefaultTransactionMaxAttempts is the default number of times to attempt a transaction.

### DetectProjectID
    
    
    const DetectProjectID = detect.ProjectIDSentinel

DetectProjectID is a sentinel value that instructs NewClient to detect the project ID. It is given in place of the projectID argument. NewClient will use the project ID from the given credentials or the default credentials (<https://developers.google.com/accounts/docs/application-default-credentials>) if no credentials were provided. When providing credentials, not all options will allow NewClient to extract the project ID. Specifically a JWT does not have the project ID encoded.

### DocumentID
    
    
    const DocumentID = "__name__"

DocumentID is the special field name representing the ID of a document in queries.

## Variables 

### ErrPipelineWithoutDatabase, ErrRelativeScopeUnionUnsupported
    
    
    var (
    	// ErrPipelineWithoutDatabase is returned when a pipeline is executed without a database such as a subcollection pipeline.
    	ErrPipelineWithoutDatabase = errors.New("firestore: pipeline without a database cannot be executed directly, only as part of another pipeline")
    	// ErrRelativeScopeUnionUnsupported is returned when a union is used with a relative scope pipeline.
    	ErrRelativeScopeUnionUnsupported = errors.New("firestore: union only supports combining root pipelines; relative scope pipelines (like subcollection pipelines) are not supported")
    )

### LogWatchStreams
    
    
    var LogWatchStreams = [false](https://pkg.go.dev/builtin#false)

LogWatchStreams controls whether watch stream status changes are logged. This feature is EXPERIMENTAL and may disappear at any time.

### ReadOnly
    
    
    var ReadOnly = ro{}

ReadOnly is a TransactionOption that makes the transaction read-only. Read-only transactions cannot issue write operations, but are more efficient.

## Functions 

### func ArrayRemove 
    
    
    func ArrayRemove(elems ...interface{}) arrayRemove

ArrayRemove specifies elements to be removed from whatever array already exists in the server.

If a value exists and it's an array, values are removed from it. All duplicate values are removed. If a value exists and it's not an array, the value is replaced by an empty array. If a value does not exist, an empty array is created.

ArrayRemove must be the value of a field directly; it cannot appear in array or struct values, or in any value that is itself inside an array or struct.

#### Example

##### update
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	co := client.Doc("States/Colorado")
    	wr, err := co.Update(ctx, []firestore.Update{
    		{Path: "cities", Value: firestore.[ArrayRemove](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_ArrayRemove)("Denver")},
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

### func ArrayUnion 
    
    
    func ArrayUnion(elems ...interface{}) arrayUnion

ArrayUnion specifies elements to be added to whatever array already exists in the server, or to create an array if no value exists.

If a value exists and it's an array, values are appended to it. Any duplicate value is ignored. If a value exists and it's not an array, the value is replaced by an array of the values in the ArrayUnion. If a value does not exist, an array of the values in the ArrayUnion is created.

ArrayUnion must be the value of a field directly; it cannot appear in array or struct values, or in any value that is itself inside an array or struct.

#### Examples

##### create
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	wr, err := client.Doc("States/Colorado").Create(ctx, map[string]interface{}{
    		"cities": firestore.[ArrayUnion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_ArrayUnion)("Denver", "Golden", "Boulder"),
    		"pop":    5.5,
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

##### update
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	co := client.Doc("States/Colorado")
    	wr, err := co.Update(ctx, []firestore.Update{
    		{Path: "cities", Value: firestore.[ArrayUnion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_ArrayUnion)("Broomfield")},
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

### func FieldTransformIncrement 
    
    
    func FieldTransformIncrement(n interface{}) transform

FieldTransformIncrement returns a special value that can be used with Set, Create, or Update that tells the server to transform the field's current value by the given value.

The supported values are:
    
    
    int, int8, int16, int32, int64
    uint8, uint16, uint32
    float32, float64
    

If the field does not yet exist, the transformation will set the field to the given value.

### func FieldTransformMaximum 
    
    
    func FieldTransformMaximum(n interface{}) transform

FieldTransformMaximum returns a special value that can be used with Set, Create, or Update that tells the server to set the field to the maximum of the field's current value and the given value.

The supported values are:
    
    
    int, int8, int16, int32, int64
    uint8, uint16, uint32
    float32, float64
    

If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If a maximum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the larger operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The maximum of a zero stored value and zero input value is always the stored value. The maximum of any numeric value x and NaN is NaN.

### func FieldTransformMinimum 
    
    
    func FieldTransformMinimum(n interface{}) transform

FieldTransformMinimum returns a special value that can be used with Set, Create, or Update that tells the server to set the field to the minimum of the field's current value and the given value.

The supported values are:
    
    
    int, int8, int16, int32, int64
    uint8, uint16, uint32
    float32, float64
    

If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If a minimum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the smaller operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The minimum of a zero stored value and zero input value is always the stored value. The minimum of any numeric value x and NaN is NaN.

### func Fields 
    
    
    func Fields(f [any](https://pkg.go.dev/builtin#any)) [][any](https://pkg.go.dev/builtin#any)

Fields is a helper function that returns its arguments as a slice of any. It is used to provide variadic-like ergonomics for pipeline stages that accept a slice of fields or expressions.

### func Increment 
    
    
    func Increment(n interface{}) transform

Increment is an alias for FieldTransformIncrement.

#### Examples

##### create
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	wr, err := client.Doc("States/Colorado").Create(ctx, map[string]interface{}{
    		"cities": []string{"Denver", "Golden", "Boulder"},
    		"pop":    firestore.[Increment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Increment)(7), // "pop" will be set to 7.
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

##### update
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	co := client.Doc("States/Colorado")
    	wr, err := co.Update(ctx, []firestore.Update{
    		{Path: "pop", Value: firestore.[Increment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Increment)(7)}, // "pop" will incremented by 7.
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

### func MaxAttempts 
    
    
    func MaxAttempts(n [int](https://pkg.go.dev/builtin#int)) maxAttempts

MaxAttempts is a TransactionOption that configures the maximum number of times to try a transaction. In defaults to DefaultTransactionMaxAttempts.

### func Ptr 
    
    
    func Ptr(t T) *T

Ptr returns a pointer to its argument. It can be used to initialize pointer fields:
    
    
    findNearestOptions.DistanceThreshold = firestore.Ptr[float64](0.1)
    

### func WithCommitResponseTo 
    
    
    func WithCommitResponseTo(r *CommitResponse) commitResponse

WithCommitResponseTo returns a TransactionOption that specifies where the CommitResponse should be written on successful commit. Nothing is written on a failed commit.

## AddFieldsOption
    
    
    type AddFieldsOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

AddFieldsOption is an option for an AddFields pipeline stage.

## AggregateFunction
    
    
    type AggregateFunction interface {
    	As(alias [string](https://pkg.go.dev/builtin#string)) *AliasedAggregate
    	// contains filtered or unexported methods
    }

AggregateFunction represents an aggregation function in a pipeline.

### func ArrayAgg 
    
    
    func ArrayAgg(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

ArrayAgg returns an array containing all values of the expression when evaluated on each document in the group. If the expression resolves to an absent value, it is converted to NULL. The order of elements in the output array is not stable and shouldn't be relied upon.

### func ArrayAggDistinct 
    
    
    func ArrayAggDistinct(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

ArrayAggDistinct returns an array containing all distinct values of the expression when evaluated on each document in the group. If the expression resolves to an absent value, it is converted to NULL. The order of elements in the output array is not stable and shouldn't be relied upon.

### func Average 
    
    
    func Average(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

Average creates an aggregation that calculates the average (mean) of values from an expression or a field's values across multiple stage inputs. fieldOrExpr can be a field path string, [FieldPath] or [Expression] Example:
    
    
        // Calculate the average age of users
        Average(FieldOf("info.age")).As("averageAge")       // FieldOf returns Expr
        Average(FieldOfPath("info.age")).As("averageAge") // FieldOfPath returns Expr
        Average("info.age").As("averageAge")              // String implicitly becomes FieldOf(...).As(...)
        Average(FieldPath([]string{"info", "age"})).As("averageAge")
    

### func Count 
    
    
    func Count(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

Count creates an aggregation that counts the number of stage inputs with valid evaluations of the provided field or expression. fieldOrExpr can be a field path string, [FieldPath] or [Expression] Example:
    
    
        // Count the number of items where the price is greater than 10
        Count(FieldOf("price").Gt(10)).As("expensiveItemCount") // FieldOf("price").Gt(10) is a BooleanExpr
        // Count the total number of products
        Count("productId").As("totalProducts")                  // String implicitly becomes FieldOf(...).As(...)
    

### func CountAll 
    
    
    func CountAll() AggregateFunction

CountAll creates an aggregation that counts the total number of stage inputs.

Example:
    
    
        // Count the total number of users
        CountAll().As("totalUsers")
    

### func CountDistinct 
    
    
    func CountDistinct(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

CountDistinct creates an aggregation that counts the number of distinct values of the provided field or expression. fieldOrExpr can be a field path string, [FieldPath] or [Expression] Example:
    
    
        // CountDistinct the number of distinct items where the price is greater than 10
        CountDistinct(FieldOf("price").Gt(10)).As("expensiveItemCount") // FieldOf("price").Gt(10) is a BooleanExpr
        // CountDistinct the total number of distinct products
        CountDistinct("productId").As("totalProducts")                  // String implicitly becomes FieldOf(...).As(...)
    

### func CountIf 
    
    
    func CountIf(condition BooleanExpression) AggregateFunction

CountIf creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true. Example:
    
    
    CountIf(FieldOf("published").Equal(true)).As("publishedCount")
    

### func First 
    
    
    func First(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

First returns the value of the expression for the first document in the group.

### func Last 
    
    
    func Last(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

Last returns the value of the expression for the last document in the group.

### func Maximum 
    
    
    func Maximum(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

Maximum creates an aggregation that calculates the maximum of values from an expression or a field's values across multiple stage inputs.

Example:
    
    
        // Find the highest order amount
        Maximum(FieldOf("orderAmount")).As("maxOrderAmount") // FieldOf returns Expr
        Maximum("orderAmount").As("maxOrderAmount")          // String implicitly becomes FieldOf(...).As(...)
    

### func Minimum 
    
    
    func Minimum(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

Minimum creates an aggregation that calculates the minimum of values from an expression or a field's values across multiple stage inputs.

Example:
    
    
        // Find the lowest order amount
        Minimum(FieldOf("orderAmount")).As("minOrderAmount") // FieldOf returns Expr
        Minimum("orderAmount").As("minOrderAmount")          // String implicitly becomes FieldOf(...).As(...)
    

### func RawAggregate 
    
    
    func RawAggregate(name [string](https://pkg.go.dev/builtin#string), fieldOrExprs [any](https://pkg.go.dev/builtin#any)) AggregateFunction

RawAggregate creates a raw aggregation function.

This method provides a way to call aggregation functions that are supported by the Firestore backend but that are not available as specific factory methods in this class.

Example:
    
    
    RawAggregate("sum", "orderAmount").As("totalRevenue")
    

### func Sum 
    
    
    func Sum(fieldOrExpr [any](https://pkg.go.dev/builtin#any)) AggregateFunction

Sum creates an aggregation that calculates the sum of values from an expression or a field's values across multiple stage inputs.

Example:
    
    
        // Calculate the total revenue from a set of orders
        Sum(FieldOf("orderAmount")).As("totalRevenue") // FieldOf returns Expr
        Sum("orderAmount").As("totalRevenue")          // String implicitly becomes FieldOf(...).As(...)
    

## AggregateOption
    
    
    type AggregateOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

AggregateOption is an option for executing a pipeline aggregation stage.

### func WithAggregateGroups 
    
    
    func WithAggregateGroups(groups [any](https://pkg.go.dev/builtin#any)) AggregateOption

WithAggregateGroups specifies the fields or expressions to group the documents by. Each of the grouping keys can be a string field path, a [FieldPath], or a [Selectable] expression.

## AggregationQuery
    
    
    type AggregationQuery struct {
    	// contains filtered or unexported fields
    }

AggregationQuery allows for generating aggregation results of an underlying basic query. A single AggregationQuery can contain multiple aggregations.

### func (*AggregationQuery) Get 
    
    
    func (a *AggregationQuery) Get(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (AggregationResult, [error](https://pkg.go.dev/builtin#error))

Get retrieves the aggregation query results from the service.

### func (*AggregationQuery) GetResponse 
    
    
    func (a *AggregationQuery) GetResponse(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (aro *AggregationResponse, err [error](https://pkg.go.dev/builtin#error))

GetResponse runs the aggregation with the options provided in the query

### func (*AggregationQuery) Pipeline 
    
    
    func (aq *AggregationQuery) Pipeline() *Pipeline

Pipeline creates a new [Pipeline] from the aggregation query. All of the operations of the underlying query will be converted to pipeline stages, and an aggregate stage will be added for the aggregations.

### func (*AggregationQuery) Transaction 
    
    
    func (a *AggregationQuery) Transaction(tx *Transaction) *AggregationQuery

Transaction specifies that aggregation query should run within provided transaction

### func (*AggregationQuery) WithAvg 
    
    
    func (a *AggregationQuery) WithAvg(path [string](https://pkg.go.dev/builtin#string), alias [string](https://pkg.go.dev/builtin#string)) *AggregationQuery

WithAvg specifies that the aggregation query should provide an average of the values of the provided field in the results returned by the underlying Query. The alias argument can be empty or a valid Firestore document field name. It can be used as key in the AggregationResult to get the average value. If alias is empty, Firestore will autogenerate a key.

### func (*AggregationQuery) WithAvgPath 
    
    
    func (a *AggregationQuery) WithAvgPath(fp FieldPath, alias [string](https://pkg.go.dev/builtin#string)) *AggregationQuery

WithAvgPath specifies that the aggregation query should provide an average of the values of the provided field in the results returned by the underlying Query. The path argument can be a single field or a dot-separated sequence of fields, and must not contain any of the runes "˜*/[]". The alias argument can be empty or a valid Firestore document field name. It can be used as key in the AggregationResult to get the average value. If alias is empty, Firestore will autogenerate a key.

### func (*AggregationQuery) WithCount 
    
    
    func (a *AggregationQuery) WithCount(alias [string](https://pkg.go.dev/builtin#string)) *AggregationQuery

WithCount specifies that the aggregation query provide a count of results returned by the underlying Query.

### func (*AggregationQuery) WithSum 
    
    
    func (a *AggregationQuery) WithSum(path [string](https://pkg.go.dev/builtin#string), alias [string](https://pkg.go.dev/builtin#string)) *AggregationQuery

WithSum specifies that the aggregation query should provide a sum of the values of the provided field in the results returned by the underlying Query. The alias argument can be empty or a valid Firestore document field name. It can be used as key in the AggregationResult to get the sum value. If alias is empty, Firestore will autogenerate a key.

### func (*AggregationQuery) WithSumPath 
    
    
    func (a *AggregationQuery) WithSumPath(fp FieldPath, alias [string](https://pkg.go.dev/builtin#string)) *AggregationQuery

WithSumPath specifies that the aggregation query should provide a sum of the values of the provided field in the results returned by the underlying Query. The path argument can be a single field or a dot-separated sequence of fields, and must not contain any of the runes "˜*/[]". The alias argument can be empty or a valid Firestore document field name. It can be used as key in the AggregationResult to get the sum value. If alias is empty, Firestore will autogenerate a key.

## AggregationResponse
    
    
    type AggregationResponse struct {
    	Result AggregationResult
    
    	// Query explain metrics. This is only present when ExplainOptions is provided.
    	ExplainMetrics *ExplainMetrics
    }

AggregationResponse contains AggregationResult and response from the run options in the query

## AggregationResult
    
    
    type AggregationResult map[[string](https://pkg.go.dev/builtin#string)]interface{}

AggregationResult contains the results of an aggregation query.

### func (AggregationResult) Data 
    
    
    func (ar AggregationResult) Data() map[[string](https://pkg.go.dev/builtin#string)]interface{}

Data returns the AggregationResult's fields as a map of native Go types. It is equivalent to
    
    
    var m map[string]interface{}
    ar.DataTo(&m)
    

### func (AggregationResult) DataTo 
    
    
    func (ar AggregationResult) DataTo(p interface{}) [error](https://pkg.go.dev/builtin#error)

DataTo uses the aggregation result's fields to populate p, which can be a pointer to a map[string]interface{} or a pointer to a struct.

See DocumentSnapshot.DataTo for how Firestore values are converted to Go values.

## AliasedAggregate
    
    
    type AliasedAggregate struct {
    	// contains filtered or unexported fields
    }

AliasedAggregate is an aliased [AggregateFunction]. It's used to give a name to the result of an aggregation.

### func Accumulators 
    
    
    func Accumulators(a ...*AliasedAggregate) []*AliasedAggregate

Accumulators is a helper function that returns its arguments as a slice of *AliasedAggregate. It is used to provide variadic-like ergonomics for the Aggregate pipeline stage.

## AliasedExpression
    
    
    type AliasedExpression struct {
    	// contains filtered or unexported fields
    }

AliasedExpression represents an expression with an alias. It implements the [Selectable] interface, allowing it to be used in projection stages like `Select` and `AddFields`.

### func AliasedExpressions 
    
    
    func AliasedExpressions(v ...*AliasedExpression) []*AliasedExpression

AliasedExpressions is a helper function that returns its arguments as a slice of *AliasedExpression. It is used to provide variadic-like ergonomics for the [Pipeline.Define] pipeline stage.

## AndFilter
    
    
    type AndFilter struct {
    	Filters []EntityFilter
    }

AndFilter represents the intersection of two or more filters.

## BSONBinary
    
    
    type BSONBinary struct {
    	Subtype [byte](https://pkg.go.dev/builtin#byte)
    	Data    [][byte](https://pkg.go.dev/builtin#byte)
    }

BSONBinary represents BSON Binary data with subtype != 0.

## BSONDecimal128
    
    
    type BSONDecimal128 [string](https://pkg.go.dev/builtin#string)

BSONDecimal128 represents a BSON Decimal128.

## BSONInt32
    
    
    type BSONInt32 [int32](https://pkg.go.dev/builtin#int32)

BSONInt32 represents a BSON 32-bit integer.

## BSONMaxKey
    
    
    type BSONMaxKey struct{}

BSONMaxKey represents BSON MaxKey.

## BSONMinKey
    
    
    type BSONMinKey struct{}

BSONMinKey represents BSON MinKey.

## BSONObjectID
    
    
    type BSONObjectID [string](https://pkg.go.dev/builtin#string)

BSONObjectID represents a BSON ObjectID as a 24-character lowercase hex string.

### func (BSONObjectID) String 
    
    
    func (id BSONObjectID) String() [string](https://pkg.go.dev/builtin#string)

String returns the string representation of the BSONObjectID.

## BSONRegex
    
    
    type BSONRegex struct {
    	Pattern [string](https://pkg.go.dev/builtin#string)
    	Options [string](https://pkg.go.dev/builtin#string)
    }

BSONRegex represents a BSON Regular Expression.

## BSONTimestamp
    
    
    type BSONTimestamp struct {
    	Seconds   [uint32](https://pkg.go.dev/builtin#uint32)
    	Increment [uint32](https://pkg.go.dev/builtin#uint32)
    }

BSONTimestamp represents a BSON Timestamp.

## BooleanExpression
    
    
    type BooleanExpression interface {
    	Expression // Embed Expr interface
    
    	// Conditional creates an expression that evaluates a condition and returns one of two expressions.
    	//
    	// The parameter 'thenVal' is the expression to return if the condition is true.
    	// The parameter 'elseVal' is the expression to return if the condition is false.
    	Conditional(thenVal, elseVal [any](https://pkg.go.dev/builtin#any)) Expression
    	// IfErrorBoolean creates a boolean expression that evaluates and returns the receiver expression if it does not produce an error;
    	// otherwise, it evaluates and returns `catchExpr`.
    	//
    	// The parameter 'catchExpr' is the boolean expression to return if the receiver expression errors.
    	IfErrorBoolean(catchExpr BooleanExpression) BooleanExpression
    	// Not creates an expression that negates a boolean expression.
    	Not() BooleanExpression
    	// CountIf creates an aggregation that counts the number of stage inputs where the this boolean expression
    	// evaluates to true.
    	CountIf() AggregateFunction
    	// contains filtered or unexported methods
    }

BooleanExpression is an interface that represents a boolean expression in a pipeline.

### func And 
    
    
    func And(condition BooleanExpression, right ...BooleanExpression) BooleanExpression

And creates an expression that performs a logical 'AND' operation.

### func ArrayContains 
    
    
    func ArrayContains(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), value [any](https://pkg.go.dev/builtin#any)) BooleanExpression

ArrayContains creates an expression that checks if an array contains a specified element.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * value is the element to check for.



Example:
    
    
    // Check if the 'tags' array contains "Go".
    ArrayContains("tags", "Go")
    

### func ArrayContainsAll 
    
    
    func ArrayContainsAll(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), values [any](https://pkg.go.dev/builtin#any)) BooleanExpression

ArrayContainsAll creates an expression that checks if an array contains all of the provided values.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * values can be an array of values or an expression that evaluates to an array.



Example:
    
    
    // Check if the 'tags' array contains both "Go" and "Firestore".
    ArrayContainsAll("tags", []string{"Go", "Firestore"})
    

### func ArrayContainsAny 
    
    
    func ArrayContainsAny(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), values [any](https://pkg.go.dev/builtin#any)) BooleanExpression

ArrayContainsAny creates an expression that checks if an array contains any of the provided values.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * values can be an array of values or an expression that evaluates to an array.



Example:
    
    
    // Check if the 'tags' array contains either "Go" or "Firestore".
    ArrayContainsAny("tags", []string{"Go", "Firestore"})
    

### func DocumentMatches 
    
    
    func DocumentMatches(query [string](https://pkg.go.dev/builtin#string)) BooleanExpression

DocumentMatches creates a boolean expression that performs a full-text search on all indexed search fields in the document.

This Expression can only be used within a Search stage.

Example:
    
    
    client.Pipeline().Collection("restaurants").
        Search(WithSearchQuery(DocumentMatches("waffles OR pancakes")))
    

  * query: Define the search query using the search domain-specific language (DSL).



Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func EndsWith 
    
    
    func EndsWith(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), suffix [any](https://pkg.go.dev/builtin#any)) BooleanExpression

EndsWith creates an expression that checks if a string field or expression ends with a given suffix.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].
  * suffix string or [Expression] to check for.



Example:
    
    
    // Check if the 'filename' field ends with ".go".
    EndsWith("filename", ".go")
    

### func Equal 
    
    
    func Equal(left, right [any](https://pkg.go.dev/builtin#any)) BooleanExpression

Equal creates an expression that checks if field's value or an expression is equal to an expression or a constant value, returning it as a BooleanExpr.

  * left: The field path string, [FieldPath] or [Expression] to compare.
  * right: The constant value or [Expression] to compare to.



Example:
    
    
        // Check if the 'age' field is equal to 21
        Equal(FieldOf("age"), 21)
    
        // Check if the 'age' field is equal to an expression
        Equal(FieldOf("age"), FieldOf("minAge").Add(10))
    
        // Check if the 'age' field is equal to the 'limit' field
        Equal("age", FieldOf("limit"))
    
        // Check if the 'city' field is equal to string constant "London"
        Equal("city", "London")
    

### func EqualAny 
    
    
    func EqualAny(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), values [any](https://pkg.go.dev/builtin#any)) BooleanExpression

EqualAny creates an expression that checks if a field or expression is equal to any of the provided values.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression].
  * values can be an array of values or an expression that evaluates to an array.



Example:
    
    
    // Check if the 'status' field is either "active" or "pending".
    EqualAny("status", []string{"active", "pending"})
    

### func FieldExists 
    
    
    func FieldExists(exprOrField [any](https://pkg.go.dev/builtin#any)) BooleanExpression

FieldExists creates an expression that checks if a field exists.

### func GreaterThan 
    
    
    func GreaterThan(left, right [any](https://pkg.go.dev/builtin#any)) BooleanExpression

GreaterThan creates an expression that checks if field's value or an expression is greater than an expression or a constant value, returning it as a BooleanExpr.

  * left: The field path string, [FieldPath] or [Expression] to compare.
  * right: The constant value or [Expression] to compare to.



Example:
    
    
        // Check if the 'age' field is greater than 21
        GreaterThan(FieldOf("age"), 21)
    
        // Check if the 'age' field is greater than an expression
        GreaterThan(FieldOf("age"), FieldOf("minAge").Add(10))
    
        // Check if the 'age' field is greater than the 'limit' field
        GreaterThan("age", FieldOf("limit"))
    

### func GreaterThanOrEqual 
    
    
    func GreaterThanOrEqual(left, right [any](https://pkg.go.dev/builtin#any)) BooleanExpression

GreaterThanOrEqual creates an expression that checks if field's value or an expression is greater than or equal to an expression or a constant value, returning it as a BooleanExpr.

  * left: The field path string, [FieldPath] or [Expression] to compare.
  * right: The constant value or [Expression] to compare to.



Example:
    
    
        // Check if the 'age' field is greater than or equal to 21
        GreaterThanOrEqual(FieldOf("age"), 21)
    
        // Check if the 'age' field is greater than or equal to an expression
        GreaterThanOrEqual(FieldOf("age"), FieldOf("minAge").Add(10))
    
        // Check if the 'age' field is greater than or equal to the 'limit' field
        GreaterThanOrEqual("age", FieldOf("limit"))
    

### func IfErrorBoolean 
    
    
    func IfErrorBoolean(tryExpr BooleanExpression, catchExpr BooleanExpression) BooleanExpression

IfErrorBoolean creates a boolean expression that evaluates and returns `tryExpr` if it does not produce an error; otherwise, it evaluates and returns `catchExpr`. It returns a new [BooleanExpression] representing the if_error operation.

  * tryExpr is the boolean expression to try.
  * catchExpr is the boolean expression to return if `tryExpr` errors.



### func IsAbsent 
    
    
    func IsAbsent(exprOrField [any](https://pkg.go.dev/builtin#any)) BooleanExpression

IsAbsent creates an expression that checks if an expression evaluates to an absent value.

### func IsError 
    
    
    func IsError(expr Expression) BooleanExpression

IsError creates an expression that checks if an expression evaluates to an error.

### func IsType 
    
    
    func IsType(exprOrField [any](https://pkg.go.dev/builtin#any), dataType [string](https://pkg.go.dev/builtin#string)) BooleanExpression

IsType creates an expression that checks if an expression is of a specific type.

  * exprOrField can be a field path string, [FieldPath] or an [Expression].
  * dataType can be a valid type name. Valid values are "null", "array", "boolean", "bytes", "timestamp", "geo_point", "number", "int32", "int64", "float64", "decimal128", "map", "reference", "string", "vector", "max_key", "min_key", "min_array", "object_id", "regex", "request_timestamp"



### func LessThan 
    
    
    func LessThan(left, right [any](https://pkg.go.dev/builtin#any)) BooleanExpression

LessThan creates an expression that checks if field's value or an expression is less than an expression or a constant value, returning it as a BooleanExpr.

  * left: The field path string, [FieldPath] or [Expression] to compare.
  * right: The constant value or [Expression] to compare to.



Example:
    
    
        // Check if the 'age' field is less than 21
        LessThan(FieldOf("age"), 21)
    
        // Check if the 'age' field is less than an expression
        LessThan(FieldOf("age"), FieldOf("minAge").Add(10))
    
        // Check if the 'age' field is less than the 'limit' field
        LessThan("age", FieldOf("limit"))
    

### func LessThanOrEqual 
    
    
    func LessThanOrEqual(left, right [any](https://pkg.go.dev/builtin#any)) BooleanExpression

LessThanOrEqual creates an expression that checks if field's value or an expression is less than or equal to an expression or a constant value, returning it as a BooleanExpr.

  * left: The field path string, [FieldPath] or [Expression] to compare.
  * right: The constant value or [Expression] to compare to.



Example:
    
    
        // Check if the 'age' field is less than or equal to 21
        LessThanOrEqual(FieldOf("age"), 21)
    
        // Check if the 'age' field is less than or equal to an expression
        LessThanOrEqual(FieldOf("age"), FieldOf("minAge").Add(10))
    
        // Check if the 'age' field is less than or equal to the 'limit' field
        LessThanOrEqual("age", FieldOf("limit"))
    

### func Like 
    
    
    func Like(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), pattern [any](https://pkg.go.dev/builtin#any)) BooleanExpression

Like creates an expression that performs a case-sensitive wildcard string comparison.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].
  * pattern string or [Expression] to search for. You can use "%" as a wildcard character.



Example:
    
    
    // Check if the 'name' field starts with "G".
    Like("name", "G%")
    

### func Nor 
    
    
    func Nor(condition BooleanExpression, right ...BooleanExpression) BooleanExpression

Nor creates an expression that performs a logical 'NOR' operation.

### func Not 
    
    
    func Not(condition BooleanExpression) BooleanExpression

Not creates an expression that negates a boolean expression.

### func NotEqual 
    
    
    func NotEqual(left, right [any](https://pkg.go.dev/builtin#any)) BooleanExpression

NotEqual creates an expression that checks if field's value or an expression is not equal to an expression or a constant value, returning it as a BooleanExpr.

  * left: The field path string, [FieldPath] or [Expression] to compare.
  * right: The constant value or [Expression] to compare to.



Example:
    
    
        // Check if the 'age' field is not equal to 21
        NotEqual(FieldOf("age"), 21)
    
        // Check if the 'age' field is not equal to an expression
        NotEqual(FieldOf("age"), FieldOf("minAge").Add(10))
    
        // Check if the 'age' field is not equal to the 'limit' field
        NotEqual("age", FieldOf("limit"))
    
        // Check if the 'city' field is not equal to string constant "London"
        NotEqual("city", "London")
    

### func NotEqualAny 
    
    
    func NotEqualAny(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), values [any](https://pkg.go.dev/builtin#any)) BooleanExpression

NotEqualAny creates an expression that checks if a field or expression is not equal to any of the provided values.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression].
  * values can be an array of values or an expression that evaluates to an array.



Example:
    
    
    // Check if the 'status' field is not "archived" or "deleted".
    NotEqualAny("status", []string{"archived", "deleted"})
    

### func Or 
    
    
    func Or(condition BooleanExpression, right ...BooleanExpression) BooleanExpression

Or creates an expression that performs a logical 'OR' operation.

### func RawBooleanFunction 
    
    
    func RawBooleanFunction(name [string](https://pkg.go.dev/builtin#string), exprs [any](https://pkg.go.dev/builtin#any)) BooleanExpression

RawBooleanFunction creates a 'raw' boolean function expression. This is useful if the expression is available in the backend, but not yet in the current version of the SDK.

### func RegexContains 
    
    
    func RegexContains(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), pattern [any](https://pkg.go.dev/builtin#any)) BooleanExpression

RegexContains creates an expression that checks if a string contains a match for a regular expression.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].
  * pattern is the regular expression to search for.



Example:
    
    
    // Check if the 'email' field contains a gmail address.
    RegexContains("email", "@gmail\\.com$")
    

### func RegexMatch 
    
    
    func RegexMatch(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), pattern [any](https://pkg.go.dev/builtin#any)) BooleanExpression

RegexMatch creates an expression that checks if a string matches a regular expression.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].
  * pattern is the regular expression to match against.



Example:
    
    
    // Check if the 'zip_code' field is a 5-digit number.
    RegexMatch("zip_code", "^[0-9]{5}$")
    

### func StartsWith 
    
    
    func StartsWith(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), prefix [any](https://pkg.go.dev/builtin#any)) BooleanExpression

StartsWith creates an expression that checks if a string field or expression starts with a given prefix.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].
  * prefix string or [Expression] to check for.



Example:
    
    
    // Check if the 'name' field starts with "Mr.".
    StartsWith("name", "Mr.")
    

### func StringContains 
    
    
    func StringContains(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), substring [any](https://pkg.go.dev/builtin#any)) BooleanExpression

StringContains creates an expression that checks if a string contains a specified substring.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].
  * substring is the string to search for.



Example:
    
    
    // Check if the 'description' field contains the word "Firestore".
    StringContains("description", "Firestore")
    

### func Xor 
    
    
    func Xor(condition BooleanExpression, right ...BooleanExpression) BooleanExpression

Xor creates an expression that performs a logical 'XOR' operation.

## BulkWriter
    
    
    type BulkWriter struct {
    	// contains filtered or unexported fields
    }

A BulkWriter supports concurrent writes to multiple documents. The BulkWriter submits document writes in maximum batches of 20 writes per request. Each request can contain many different document writes: create, delete, update, and set are all supported.

Only one operation (create, set, update, delete) per document is allowed. BulkWriter cannot promise atomicity: individual writes can fail or succeed independent of each other. Bulkwriter does not apply writes in any set order; thus a document can't have set on it immediately after creation.

### func (*BulkWriter) Create 
    
    
    func (bw *BulkWriter) Create(doc *DocumentRef, datum interface{}) (*BulkWriterJob, [error](https://pkg.go.dev/builtin#error))

Create adds a document creation write to the queue of writes to send. Note: You cannot write to (Create, Update, Set, or Delete) the same document more than once.

### func (*BulkWriter) Delete 
    
    
    func (bw *BulkWriter) Delete(doc *DocumentRef, preconds ...Precondition) (*BulkWriterJob, [error](https://pkg.go.dev/builtin#error))

Delete adds a document deletion write to the queue of writes to send. Note: You cannot write to (Create, Update, Set, or Delete) the same document more than once.

### func (*BulkWriter) End 
    
    
    func (bw *BulkWriter) End()

End sends all enqueued writes in parallel and closes the BulkWriter to new requests. After calling End(), calling any additional method automatically returns with an error. This method completes when there are no more pending writes in the queue.

### func (*BulkWriter) Flush 
    
    
    func (bw *BulkWriter) Flush()

Flush commits all writes that have been enqueued up to this point in parallel. This method blocks execution.

### func (*BulkWriter) Set 
    
    
    func (bw *BulkWriter) Set(doc *DocumentRef, datum interface{}, opts ...SetOption) (*BulkWriterJob, [error](https://pkg.go.dev/builtin#error))

Set adds a document set write to the queue of writes to send. Note: You cannot write to (Create, Update, Set, or Delete) the same document more than once.

### func (*BulkWriter) Update 
    
    
    func (bw *BulkWriter) Update(doc *DocumentRef, updates []Update, preconds ...Precondition) (*BulkWriterJob, [error](https://pkg.go.dev/builtin#error))

Update adds a document update write to the queue of writes to send. Note: You cannot write to (Create, Update, Set, or Delete) the same document more than once.

## BulkWriterJob
    
    
    type BulkWriterJob struct {
    	// contains filtered or unexported fields
    }

BulkWriterJob provides read-only access to the results of a BulkWriter write attempt.

### func (*BulkWriterJob) Results 
    
    
    func (j *BulkWriterJob) Results() (*WriteResult, [error](https://pkg.go.dev/builtin#error))

Results gets the results of the BulkWriter write attempt. This method blocks if the results for this BulkWriterJob haven't been received.

## Client
    
    
    type Client struct {
    	UsesEmulator [bool](https://pkg.go.dev/builtin#bool) // a boolean that indicates if the client is using the emulator
    	// contains filtered or unexported fields
    }

A Client provides access to the Firestore service.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), projectID [string](https://pkg.go.dev/builtin#string), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new Firestore client that uses the given project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close() // Close client when done.
    	_ = client           // TODO: Use client.
    }
    

### func NewClientWithDatabase 
    
    
    func NewClientWithDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), projectID [string](https://pkg.go.dev/builtin#string), databaseID [string](https://pkg.go.dev/builtin#string), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClientWithDatabase creates a new Firestore client that accesses the specified database.

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), projectID [string](https://pkg.go.dev/builtin#string), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new Firestore client that uses the REST API.

### func (*Client) Batch (deprecated)
    
    
    func (c *Client) Batch() *WriteBatch

Batch returns a WriteBatch.

Deprecated: The WriteBatch API has been replaced with the transaction and the bulk writer API. For atomic transaction operations, use `Transaction`. For bulk read and write operations, use `BulkWriter`.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    	b := client.[Batch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Client_Batch)()
    	_ = b // TODO: Use batch.
    }
    

### func (*Client) BulkWriter 
    
    
    func (c *Client) BulkWriter(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *BulkWriter

BulkWriter returns a BulkWriter instance. The context passed to the BulkWriter remains stored through the lifecycle of the object. This context allows callers to cancel BulkWriter operations.

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes any resources held by the client.

Close need not be called at program exit.

### func (*Client) Collection 
    
    
    func (c *Client) Collection(path [string](https://pkg.go.dev/builtin#string)) *CollectionRef

Collection creates a reference to a collection with the given path. A path is a sequence of IDs separated by slashes.

Collection returns nil if path contains an even number of IDs or any ID is empty.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    	coll1 := client.Collection("States")
    	coll2 := client.Collection("States/NewYork/Cities")
    	fmt.Println(coll1, coll2)
    }
    

### func (*Client) CollectionGroup 
    
    
    func (c *Client) CollectionGroup(collectionID [string](https://pkg.go.dev/builtin#string)) *CollectionGroupRef

CollectionGroup creates a reference to a group of collections that include the given ID, regardless of parent document.

For example, consider: France/Cities/Paris = {population: 100} Canada/Cities/Montreal = {population: 90}

CollectionGroup can be used to query across all "Cities" regardless of its parent "Countries". See ExampleCollectionGroup for a complete example.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	// Given:
    	// France/Cities/Paris = {population: 100}
    	// Canada/Cities/Montreal = {population: 95}
    
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	// Query for ANY city with >95 pop, regardless of country.
    	docs, err := client.CollectionGroup("Cities").
    		Where("pop", ">", 95).
    		[OrderBy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_OrderBy)("pop", firestore.[Desc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Asc_Desc)).
    		Limit(10).
    		Documents(ctx).
    		GetAll()
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	_ = docs // TODO: Use docs.
    }
    

### func (*Client) Collections 
    
    
    func (c *Client) Collections(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *CollectionIterator

Collections returns an iterator over the top-level collections.

### func (*Client) Doc 
    
    
    func (c *Client) Doc(path [string](https://pkg.go.dev/builtin#string)) *DocumentRef

Doc creates a reference to a document with the given path. A path is a sequence of IDs separated by slashes.

Doc returns nil if path contains an odd number of IDs or any ID is empty.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    	doc1 := client.Doc("States/NewYork")
    	doc2 := client.Doc("States/NewYork/Cities/Albany")
    	fmt.Println(doc1, doc2)
    }
    

### func (*Client) DocFromFullPath 
    
    
    func (c *Client) DocFromFullPath(fullPath [string](https://pkg.go.dev/builtin#string)) *DocumentRef

DocFromFullPath creates a reference to a document from its full, absolute path, also known as its Google Cloud resource name. The path must be in the format: "projects/{projectID}/databases/{databaseID}/documents/{collectionID}/{documentID}/..." This method returns nil if:

  * The fullPath is empty.
  * The fullPath does not match the expected resource name format (e.g., missing "projects/" or "/documents/").
  * The projectID or databaseID in the fullPath do not match the client's configuration.
  * The fullPath refers to a collection instead of a document (i.e., has an odd number of segments after "/documents/").
  * The fullPath contains any empty path segments.



### func (*Client) GetAll 
    
    
    func (c *Client) GetAll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), docRefs []*DocumentRef) (_ []*DocumentSnapshot, err [error](https://pkg.go.dev/builtin#error))

GetAll retrieves multiple documents with a single call. The DocumentSnapshots are returned in the order of the given DocumentRefs. The return value will always contain the same number of DocumentSnapshots as the number of DocumentRefs in the input.

If the same DocumentRef is specified multiple times in the input, the return value will contain the same number of DocumentSnapshots referencing the same document.

If a document is not present, the corresponding DocumentSnapshot's Exists method will return false.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    	docs, err := client.GetAll(ctx, []*firestore.[DocumentRef](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_DocumentRef){
    		client.Doc("States/NorthCarolina"),
    		client.Doc("States/SouthCarolina"),
    		client.Doc("States/WestCarolina"),
    		client.Doc("States/EastCarolina"),
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// docs is a slice with four DocumentSnapshots, but the last two are
    	// nil because there is no West or East Carolina.
    	fmt.Println(docs)
    }
    

### func (*Client) Pipeline 
    
    
    func (c *Client) Pipeline() *PipelineSource

Pipeline creates a PipelineSource to start building a Firestore pipeline.

### func (*Client) RunTransaction 
    
    
    func (c *Client) RunTransaction(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), f func([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *Transaction) [error](https://pkg.go.dev/builtin#error), opts ...TransactionOption) (err [error](https://pkg.go.dev/builtin#error))

RunTransaction runs f in a transaction. f should use the transaction it is given for all Firestore operations. For any operation requiring a context, f should use the context it is passed, not the first argument to RunTransaction.

f must not call Commit or Rollback on the provided Transaction.

If f returns nil, RunTransaction commits the transaction. If the commit fails due to a conflicting transaction, RunTransaction retries f. It gives up and returns an error after a number of attempts that can be configured with the MaxAttempts option. If the commit succeeds, RunTransaction returns a nil error.

If f returns non-nil, then the transaction will be rolled back and this method will return the same error. The function f is not retried.

Note that when f returns, the transaction is not committed. Calling code must not assume that any of f's changes have been committed until RunTransaction returns nil.

Since f may be called more than once, f should usually be idempotent – that is, it should have the same result when called multiple times.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	// write the CommitResponse here, via firestore.WithCommitResponse (below)
    	var cr firestore.CommitResponse
    
    	nm := client.Doc("States/NewMexico")
    	err = client.[RunTransaction](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Client_RunTransaction)(ctx, func(ctx context.Context, tx *firestore.Transaction) error {
    		doc, err := tx.Get(nm) // tx.Get, NOT nm.Get!
    		if err != nil {
    			return err
    		}
    		pop, err := doc.[DataAt](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_DocumentSnapshot_DataAt)("pop")
    		if err != nil {
    			return err
    		}
    		return tx.Update(nm, []firestore.Update{{Path: "pop", Value: pop.(float64) + 0.2}})
    	}, firestore.[WithCommitResponseTo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_WithCommitResponseTo)(&cr))
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// CommitResponse can be accessed here
    }
    

### func (*Client) WithAlwaysUseImplicitOrderBy 
    
    
    func (c *Client) WithAlwaysUseImplicitOrderBy(b [bool](https://pkg.go.dev/builtin#bool)) *Client

WithAlwaysUseImplicitOrderBy configures the default behavior for queries. If enabled, queries will automatically inject an OrderBy clause for the Document ID (`__name__`) if one is not explicitly provided. In addition, it will automatically inject OrderBy clauses for any inequality filters (e.g. >, <, !=) present in the query if they are missing from the explicit orders. This ensures strictly deterministic query results and is especially useful when executing backwards pagination (e.g. limitToLast) without cursors.

### func (*Client) WithReadOptions 
    
    
    func (c *Client) WithReadOptions(opts ...ReadOption) *Client

WithReadOptions specifies constraints for accessing documents from the database, e.g. at what time snapshot to read the documents.

## CollectionGroupOption
    
    
    type CollectionGroupOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

CollectionGroupOption is an option for a CollectionGroup pipeline stage.

## CollectionGroupRef
    
    
    type CollectionGroupRef struct {
    
    	// Use the methods of Query on a CollectionGroupRef to create and run queries.
    	Query
    	// contains filtered or unexported fields
    }

A CollectionGroupRef is a reference to a group of collections sharing the same ID.

### func (CollectionGroupRef) GetPartitionedQueries 
    
    
    func (cgr CollectionGroupRef) GetPartitionedQueries(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), partitionCount [int](https://pkg.go.dev/builtin#int)) ([]Query, [error](https://pkg.go.dev/builtin#error))

GetPartitionedQueries returns a slice of Query objects, each containing a partition of a collection group. partitionCount must be a positive value and the number of returned partitions may be less than the requested number if providing the desired number would result in partitions with very few documents.

If a Collection Group Query would return a large number of documents, this can help to subdivide the query to smaller working units that can be distributed.

If the goal is to run the queries across processes or workers, it may be useful to use `Query.Serialize` and `Query.Deserialize` to serialize the query.

## CollectionIterator
    
    
    type CollectionIterator struct {
    	// contains filtered or unexported fields
    }

CollectionIterator is an iterator over sub-collections of a document.

### func (*CollectionIterator) GetAll 
    
    
    func (it *CollectionIterator) GetAll() ([]*CollectionRef, [error](https://pkg.go.dev/builtin#error))

GetAll returns all the collections remaining from the iterator.

### func (*CollectionIterator) Next 
    
    
    func (it *CollectionIterator) Next() (*CollectionRef, [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

In addition, if Next returns an error other than iterator.Done, all subsequent calls will return the same error. To continue iteration, a new CollectionIterator must be created.

### func (*CollectionIterator) PageInfo 
    
    
    func (it *CollectionIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the google.golang.org/api/iterator package for details.

## CollectionOption
    
    
    type CollectionOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

CollectionOption is an option for a Collection pipeline stage.

## CollectionRef
    
    
    type CollectionRef struct {
    
    	// Parent is the document of which this collection is a part. It is
    	// nil for top-level collections.
    	Parent *DocumentRef
    
    	// The full resource path of the collection: "projects/P/databases/D/documents..."
    	Path [string](https://pkg.go.dev/builtin#string)
    
    	// ID is the collection identifier.
    	ID [string](https://pkg.go.dev/builtin#string)
    
    	// Use the methods of Query on a CollectionRef to create and run queries.
    	Query
    	// contains filtered or unexported fields
    }

A CollectionRef is a reference to Firestore collection.

### func (*CollectionRef) Add 
    
    
    func (c *CollectionRef) Add(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), data interface{}) (*DocumentRef, *WriteResult, [error](https://pkg.go.dev/builtin#error))

Add generates a DocumentRef with a unique ID. It then creates the document with the given data, which can be a map[string]interface{}, a struct or a pointer to a struct.

Add returns an error in the unlikely event that a document with the same ID already exists.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	doc, wr, err := client.Collection("Users").Add(ctx, map[string]interface{}{
    		"name":  "Alice",
    		"email": "aj@example.com",
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(doc, wr)
    }
    

### func (*CollectionRef) Doc 
    
    
    func (c *CollectionRef) Doc(id [string](https://pkg.go.dev/builtin#string)) *DocumentRef

Doc returns a DocumentRef that refers to the document in the collection with the given identifier.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	fl := client.Collection("States").Doc("Florida")
    	ta := client.Collection("States").Doc("Florida/Cities/Tampa")
    
    	fmt.Println(fl, ta)
    }
    

### func (*CollectionRef) DocumentRefs 
    
    
    func (c *CollectionRef) DocumentRefs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *DocumentRefIterator

DocumentRefs returns references to all the documents in the collection, including missing documents. A missing document is a document that does not exist but has sub-documents.

### func (*CollectionRef) NewDoc 
    
    
    func (c *CollectionRef) NewDoc() *DocumentRef

NewDoc returns a DocumentRef with a uniquely generated ID.

NewDoc will panic if crypto/rand cannot generate enough bytes to make a new doc ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	doc := client.Collection("Users").[NewDoc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_CollectionRef_NewDoc)()
    
    	fmt.Println(doc)
    }
    

### func (*CollectionRef) WithReadOptions 
    
    
    func (c *CollectionRef) WithReadOptions(opts ...ReadOption) *CollectionRef

WithReadOptions specifies constraints for accessing documents from the database, e.g. at what time snapshot to read the documents.

## CollectionSourceOption
    
    
    type CollectionSourceOption interface {
    	CollectionOption
    	CollectionGroupOption
    }

CollectionSourceOption is an option that can be applied to both Collection and CollectionGroup pipeline stages.

### func WithForceIndex 
    
    
    func WithForceIndex(index [string](https://pkg.go.dev/builtin#string)) CollectionSourceOption

WithForceIndex specifies an index to force the query to use.

### func WithIgnoreIndexFields 
    
    
    func WithIgnoreIndexFields(fields [string](https://pkg.go.dev/builtin#string)) CollectionSourceOption

WithIgnoreIndexFields specifies fields to ignore when selecting an index.

## CommitResponse
    
    
    type CommitResponse struct {
    	// contains filtered or unexported fields
    }

CommitResponse exposes information about a committed transaction.

### func (*CommitResponse) CommitTime 
    
    
    func (r *CommitResponse) CommitTime() [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

CommitTime returns the commit time from the commit response.

## CompositeFilter
    
    
    type CompositeFilter interface {
    	EntityFilter
    	// contains filtered or unexported methods
    }

CompositeFilter represents a composite Firestore filter.

## DatabaseOption
    
    
    type DatabaseOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

DatabaseOption is an option for a Database pipeline stage.

## DefineOption
    
    
    type DefineOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

DefineOption is an option for a Define pipeline stage.

## DeleteOption
    
    
    type DeleteOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

DeleteOption is an option for a Delete pipeline stage.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

## Direction
    
    
    type Direction [int32](https://pkg.go.dev/builtin#int32)

Direction is the sort direction for result ordering.

### Asc, Desc
    
    
    const (
    	// Asc sorts results from smallest to largest.
    	Asc Direction = Direction(pb.StructuredQuery_ASCENDING)
    
    	// Desc sorts results from largest to smallest.
    	Desc Direction = Direction(pb.StructuredQuery_DESCENDING)
    )

## DistanceMeasure
    
    
    type DistanceMeasure [int32](https://pkg.go.dev/builtin#int32)

DistanceMeasure is the distance measure to use when comparing vectors with [Query.FindNearest] or [Query.FindNearestPath].

### DistanceMeasureEuclidean, DistanceMeasureCosine, DistanceMeasureDotProduct
    
    
    const (
    	// DistanceMeasureEuclidean is used to measures the Euclidean distance between the vectors. See
    	// [Euclidean] to learn more.
    	//
    	// [Euclidean]: https://en.wikipedia.org/wiki/Euclidean_distance
    	DistanceMeasureEuclidean DistanceMeasure = DistanceMeasure(pb.StructuredQuery_FindNearest_EUCLIDEAN)
    
    	// DistanceMeasureCosine compares vectors based on the angle between them, which allows you to
    	// measure similarity that isn't based on the vectors magnitude.
    	// We recommend using dot product with unit normalized vectors instead of
    	// cosine distance, which is mathematically equivalent with better
    	// performance. See [Cosine Similarity] to learn more.
    	//
    	// [Cosine Similarity]: https://en.wikipedia.org/wiki/Cosine_similarity
    	DistanceMeasureCosine DistanceMeasure = DistanceMeasure(pb.StructuredQuery_FindNearest_COSINE)
    
    	// DistanceMeasureDotProduct is similar to cosine but is affected by the magnitude of the vectors. See
    	// [Dot Product] to learn more.
    	//
    	// [Dot Product]: https://en.wikipedia.org/wiki/Dot_product
    	DistanceMeasureDotProduct DistanceMeasure = DistanceMeasure(pb.StructuredQuery_FindNearest_DOT_PRODUCT)
    )

## DistinctOption
    
    
    type DistinctOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

DistinctOption is an option for a Distinct pipeline stage.

## DocumentChange
    
    
    type DocumentChange struct {
    	Kind DocumentChangeKind
    	Doc  *DocumentSnapshot
    	// The document snapshot before the change.
    	// This will be nil for DocumentAdded events.
    	// For DocumentRemoved events, this will be the same as Doc.
    	// For DocumentModified events, this will be the document before the modification.
    	OldDoc *DocumentSnapshot
    	// The zero-based index of the document in the sequence of query results prior to this change,
    	// or -1 if the document was not present.
    	OldIndex [int](https://pkg.go.dev/builtin#int)
    	// The zero-based index of the document in the sequence of query results after this change,
    	// or -1 if the document is no longer present.
    	NewIndex [int](https://pkg.go.dev/builtin#int)
    }

A DocumentChange describes the change to a document from one query snapshot to the next.

## DocumentChangeKind
    
    
    type DocumentChangeKind [int](https://pkg.go.dev/builtin#int)

DocumentChangeKind describes the kind of change to a document between query snapshots.

### DocumentAdded, DocumentRemoved, DocumentModified
    
    
    const (
    	// DocumentAdded indicates that the document was added for the first time.
    	DocumentAdded DocumentChangeKind = [iota](https://pkg.go.dev/builtin#iota)
    	// DocumentRemoved indicates that the document was removed.
    	DocumentRemoved
    	// DocumentModified indicates that the document was modified.
    	DocumentModified
    )

### func (DocumentChangeKind) String 
    
    
    func (k DocumentChangeKind) String() [string](https://pkg.go.dev/builtin#string)

String returns the string representation of the DocumentChangeKind.

## DocumentIterator
    
    
    type DocumentIterator struct {
    	// contains filtered or unexported fields
    }

DocumentIterator is an iterator over documents returned by a query.

### func (*DocumentIterator) ExplainMetrics 
    
    
    func (it *DocumentIterator) ExplainMetrics() (*ExplainMetrics, [error](https://pkg.go.dev/builtin#error))

ExplainMetrics returns query explain metrics. This is only present when [ExplainOptions] is added to the query (see [Query.WithRunOptions]), and after the iterator reaches the end. An error is returned if either of those conditions does not hold.

### func (*DocumentIterator) GetAll 
    
    
    func (it *DocumentIterator) GetAll() ([]*DocumentSnapshot, [error](https://pkg.go.dev/builtin#error))

GetAll returns all the documents remaining from the iterator. It is not necessary to call Stop on the iterator after calling GetAll.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	q := client.Collection("States").
    		Where("pop", ">", 10).
    		[OrderBy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_OrderBy)("pop", firestore.[Desc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Asc_Desc)).
    		Limit(10) // a good idea with GetAll, to avoid filling memory
    	docs, err := q.Documents(ctx).GetAll()
    	if err != nil {
    		// TODO: Handle error.
    	}
    	for _, doc := range docs {
    		fmt.Println(doc.Data())
    	}
    }
    

### func (*DocumentIterator) Next 
    
    
    func (it *DocumentIterator) Next() (*DocumentSnapshot, [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

In addition, if Next returns an error other than iterator.Done, all subsequent calls will return the same error. To continue iteration, a new DocumentIterator must be created.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	q := client.Collection("States").
    		Where("pop", ">", 10).
    		[OrderBy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_OrderBy)("pop", firestore.[Desc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Asc_Desc))
    	iter := q.Documents(ctx)
    	defer iter.Stop()
    	for {
    		doc, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		fmt.Println(doc.Data())
    	}
    }
    

### func (*DocumentIterator) Stop 
    
    
    func (it *DocumentIterator) Stop()

Stop stops the iterator, freeing its resources. Always call Stop when you are done with a DocumentIterator. It is not safe to call Stop concurrently with Next.

## DocumentRef
    
    
    type DocumentRef struct {
    	// The CollectionRef that this document is a part of. Never nil.
    	Parent *CollectionRef
    
    	// The full resource path of the document. A document "doc-1" in collection
    	// "coll-1" would be: "projects/P/databases/D/documents/coll-1/doc-1".
    	Path [string](https://pkg.go.dev/builtin#string)
    
    	// The ID of the document: the last component of the resource path.
    	ID [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported fields
    }

A DocumentRef is a reference to a Firestore document.

### func (*DocumentRef) Collection 
    
    
    func (d *DocumentRef) Collection(id [string](https://pkg.go.dev/builtin#string)) *CollectionRef

Collection returns a reference to sub-collection of this document.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	mi := client.Collection("States").Doc("Michigan")
    	cities := mi.Collection("Cities")
    
    	fmt.Println(cities)
    }
    

### func (*DocumentRef) Collections 
    
    
    func (d *DocumentRef) Collections(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *CollectionIterator

Collections returns an iterator over the immediate sub-collections of the document.

### func (*DocumentRef) Create 
    
    
    func (d *DocumentRef) Create(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), data interface{}) (_ *WriteResult, err [error](https://pkg.go.dev/builtin#error))

Create creates the document with the given data. It returns an error if a document with the same ID already exists.

The data argument can be a map with string keys, a struct, or a pointer to a struct. The map keys or exported struct fields become the fields of the firestore document. The values of data are converted to Firestore values as follows:

  * bool converts to Bool.
  * string converts to String.
  * int, int8, int16, int32 and int64 convert to Integer.
  * uint8, uint16 and uint32 convert to Integer. uint, uint64 and uintptr are disallowed, because they may be able to represent values that cannot be represented in an int64, which is the underlying type of a Integer.
  * float32 and float64 convert to Double.
  * []byte converts to Bytes.
  * time.Time and *ts.Timestamp convert to Timestamp. ts is the package "google.golang.org/protobuf/types/known/timestamppb".
  * *latlng.LatLng converts to GeoPoint. latlng is the package "google.golang.org/genproto/googleapis/type/latlng". You should always use a pointer to a LatLng.
  * Slices convert to Array.
  * *firestore.DocumentRef converts to Reference.
  * Maps and structs convert to Map.
  * nils of any type convert to Null.



Pointers and interface{} are also permitted, and their elements processed recursively.

Struct fields can have tags like those used by the encoding/json package. Tags begin with "firestore:" and are followed by "-", meaning "ignore this field," or an alternative name for the field. Following the name, these comma-separated options may be provided:

  * omitempty: Do not encode this field if it is empty. A value is empty if it is a zero value, or an array, slice or map of length zero.
  * serverTimestamp: The field must be of type time.Time. serverTimestamp is a sentinel token that tells Firestore to substitute the server time into that field. When writing, if the field has the zero value, the server will populate the stored document with the time that the request is processed. However, if the field value is non-zero it won't be saved.



#### Examples

##### map
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	wr, err := client.Doc("States/Colorado").Create(ctx, map[string]interface{}{
    		"capital": "Denver",
    		"pop":     5.5,
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

##### struct
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	type State struct {
    		Capital    string  `firestore:"capital"`
    		Population float64 `firestore:"pop"` // in millions
    	}
    
    	wr, err := client.Doc("States/Colorado").Create(ctx, State{
    		Capital:    "Denver",
    		Population: 5.5,
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

### func (*DocumentRef) Delete 
    
    
    func (d *DocumentRef) Delete(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), preconds ...Precondition) (_ *WriteResult, err [error](https://pkg.go.dev/builtin#error))

Delete deletes the document. If the document doesn't exist, it does nothing and returns no error.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	// Oops, Ontario is a Canadian province...
    	if _, err = client.Doc("States/Ontario").Delete(ctx); err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DocumentRef) Get 
    
    
    func (d *DocumentRef) Get(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (_ *DocumentSnapshot, err [error](https://pkg.go.dev/builtin#error))

Get retrieves the document. If the document does not exist, Get return a NotFound error, which can be checked with
    
    
    status.Code(err) == codes.NotFound
    

In that case, Get returns a non-nil DocumentSnapshot whose Exists method return false and whose ReadTime is the time of the failed read operation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	docsnap, err := client.Doc("States/Ohio").Get(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	_ = docsnap // TODO: Use DocumentSnapshot.
    }
    

### func (*DocumentRef) Set 
    
    
    func (d *DocumentRef) Set(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), data interface{}, opts ...SetOption) (_ *WriteResult, err [error](https://pkg.go.dev/builtin#error))

Set creates or overwrites the document with the given data. See DocumentRef.Create for the acceptable values of data. Without options, Set overwrites the document completely. Specify one of the Merge options to preserve an existing document's fields. To delete some fields, use a Merge option with firestore.Delete as the field value.

#### Examples
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	// Overwrite the document with the given data. Any other fields currently
    	// in the document will be removed.
    	wr, err := client.Doc("States/Alabama").Set(ctx, map[string]interface{}{
    		"capital": "Montgomery",
    		"pop":     4.9,
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

##### merge
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	// Overwrite only the fields in the map; preserve all others.
    	_, err = client.Doc("States/Alabama").Set(ctx, map[string]interface{}{
    		"pop": 5.2,
    	}, firestore.[MergeAll](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_MergeAll))
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	type State struct {
    		Capital    string  `firestore:"capital"`
    		Population float64 `firestore:"pop"` // in millions
    	}
    
    	// To do a merging Set with struct data, specify the exact fields to overwrite.
    	// MergeAll is disallowed here, because it would probably be a mistake: the "capital"
    	// field would be overwritten with the empty string.
    	_, err = client.Doc("States/Alabama").Set(ctx, State{Population: 5.2}, firestore.[Merge](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_SetOption_Merge)([]string{"pop"}))
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DocumentRef) Snapshots 
    
    
    func (d *DocumentRef) Snapshots(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *DocumentSnapshotIterator

Snapshots returns an iterator over snapshots of the document. Each time the document changes or is added or deleted, a new snapshot will be generated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    	iter := client.Doc("States/Idaho").Snapshots(ctx)
    	defer iter.Stop()
    	for {
    		docsnap, err := iter.Next()
    		if err != nil {
    			// TODO: Handle error.
    		}
    		_ = docsnap // TODO: Use DocumentSnapshot.
    	}
    }
    

### func (*DocumentRef) Update 
    
    
    func (d *DocumentRef) Update(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), updates []Update, preconds ...Precondition) (_ *WriteResult, err [error](https://pkg.go.dev/builtin#error))

Update updates the document. The values at the given field paths are replaced, but other fields of the stored document are untouched.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	tenn := client.Doc("States/Tennessee")
    	wr, err := tenn.Update(ctx, []firestore.Update{
    		{Path: "pop", Value: 6.6},
    		{FieldPath: []string{".", "*", "/"}, Value: "odd"},
    	})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(wr.[UpdateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_UpdateTime))
    }
    

### func (*DocumentRef) WithReadOptions 
    
    
    func (d *DocumentRef) WithReadOptions(opts ...ReadOption) *DocumentRef

WithReadOptions specifies constraints for accessing documents from the database, e.g. at what time snapshot to read the documents.

## DocumentRefIterator
    
    
    type DocumentRefIterator struct {
    	// contains filtered or unexported fields
    }

DocumentRefIterator is an iterator over DocumentRefs.

### func (*DocumentRefIterator) GetAll 
    
    
    func (it *DocumentRefIterator) GetAll() ([]*DocumentRef, [error](https://pkg.go.dev/builtin#error))

GetAll returns all the DocumentRefs remaining from the iterator.

### func (*DocumentRefIterator) Next 
    
    
    func (it *DocumentRefIterator) Next() (*DocumentRef, [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

In addition, if Next returns an error other than iterator.Done, all subsequent calls will return the same error. To continue iteration, a new DocumentRefIterator must be created.

### func (*DocumentRefIterator) PageInfo 
    
    
    func (it *DocumentRefIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the google.golang.org/api/iterator package for details.

## DocumentSnapshot
    
    
    type DocumentSnapshot struct {
    	// The DocumentRef for this document.
    	Ref *DocumentRef
    
    	// Read-only. The time at which the document was created.
    	// Increases monotonically when a document is deleted then
    	// recreated. It can also be compared to values from other documents and
    	// the read time of a query.
    	CreateTime time.Time
    
    	// Read-only. The time at which the document was last changed. This value
    	// is initially set to CreateTime then increases monotonically with each
    	// change to the document. It can also be compared to values from other
    	// documents and the read time of a query.
    	UpdateTime time.Time
    
    	// Read-only. The time at which the document was read.
    	ReadTime time.Time
    	// contains filtered or unexported fields
    }

A DocumentSnapshot contains document data and metadata.

### func (*DocumentSnapshot) Data 
    
    
    func (d *DocumentSnapshot) Data() map[[string](https://pkg.go.dev/builtin#string)]interface{}

Data returns the DocumentSnapshot's fields as a map. It is equivalent to
    
    
    var m map[string]interface{}
    d.DataTo(&m)
    

except that it returns nil if the document does not exist.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	docsnap, err := client.Doc("States/Ohio").Get(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	ohioMap := docsnap.Data()
    	fmt.Println(ohioMap["capital"])
    }
    

### func (*DocumentSnapshot) DataAt 
    
    
    func (d *DocumentSnapshot) DataAt(path [string](https://pkg.go.dev/builtin#string)) (interface{}, [error](https://pkg.go.dev/builtin#error))

DataAt returns the data value denoted by path.

The path argument can be a single field or a dot-separated sequence of fields, and must not contain any of the runes "˜*/[]". Use DataAtPath instead for such a path.

See DocumentSnapshot.DataTo for how Firestore values are converted to Go values.

If the document does not exist, DataAt returns a NotFound error.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	docsnap, err := client.Doc("States/Ohio").Get(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	cap, err := docsnap.[DataAt](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_DocumentSnapshot_DataAt)("capital")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(cap)
    }
    

### func (*DocumentSnapshot) DataAtPath 
    
    
    func (d *DocumentSnapshot) DataAtPath(fp FieldPath) (interface{}, [error](https://pkg.go.dev/builtin#error))

DataAtPath returns the data value denoted by the FieldPath fp. If the document does not exist, DataAtPath returns a NotFound error.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	docsnap, err := client.Doc("States/Ohio").Get(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	pop, err := docsnap.[DataAtPath](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_DocumentSnapshot_DataAtPath)([]string{"capital", "population"})
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(pop)
    }
    

### func (*DocumentSnapshot) DataTo 
    
    
    func (d *DocumentSnapshot) DataTo(p interface{}) [error](https://pkg.go.dev/builtin#error)

DataTo uses the document's fields to populate p, which can be a pointer to a map[string]interface{} or a pointer to a struct.

Firestore field values are converted to Go values as follows:

  * Null converts to nil.
  * Bool converts to bool.
  * String converts to string.
  * Integer converts int64. When setting a struct field, any signed or unsigned integer type is permitted except uint, uint64 or uintptr. Overflow is detected and results in an error.
  * Double converts to float64. When setting a struct field, float32 is permitted. Overflow is detected and results in an error.
  * Bytes is converted to []byte.
  * Timestamp converts to time.Time.
  * GeoPoint converts to *latlng.LatLng, where latlng is the package "google.golang.org/genproto/googleapis/type/latlng".
  * Arrays convert to []interface{}. When setting a struct field, the field may be a slice or array of any type and is populated recursively. Slices are resized to the incoming value's size, while arrays that are too long have excess elements filled with zero values. If the array is too short, excess incoming values will be dropped.
  * Vectors convert to []float64
  * Maps convert to map[string]interface{}. When setting a struct field, maps of key type string and any value type are permitted, and are populated recursively.
  * References are converted to *firestore.DocumentRefs.



Field names given by struct field tags are observed, as described in DocumentRef.Create.

Only the fields actually present in the document are used to populate p. Other fields of p are left unchanged.

If the document does not exist, DataTo returns a NotFound error.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	docsnap, err := client.Doc("States/Ohio").Get(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	type State struct {
    		Capital    string  `firestore:"capital"`
    		Population float64 `firestore:"pop"` // in millions
    	}
    
    	var s State
    	if err := docsnap.DataTo(&s); err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(s)
    }
    

### func (*DocumentSnapshot) Exists 
    
    
    func (d *DocumentSnapshot) Exists() [bool](https://pkg.go.dev/builtin#bool)

Exists reports whether the DocumentSnapshot represents an existing document. Even if Exists returns false, the Ref and ReadTime fields of the DocumentSnapshot are valid.

## DocumentSnapshotIterator
    
    
    type DocumentSnapshotIterator struct {
    	// contains filtered or unexported fields
    }

DocumentSnapshotIterator is an iterator over snapshots of a document. Call Next on the iterator to get a snapshot of the document each time it changes. Call Stop on the iterator when done.

For an example, see DocumentRef.Snapshots.

### func (*DocumentSnapshotIterator) Next 
    
    
    func (it *DocumentSnapshotIterator) Next() (*DocumentSnapshot, [error](https://pkg.go.dev/builtin#error))

Next blocks until the document changes, then returns the DocumentSnapshot for the current state of the document. If the document has been deleted, Next returns a DocumentSnapshot whose Exists method returns false.

Next is not expected to return iterator.Done unless it is called after Stop. Rarely, networking issues may also cause iterator.Done to be returned.

In addition, if Next returns an error other than iterator.Done, all subsequent calls will return the same error. To continue iteration, a new DocumentSnapshotIterator must be created.

### func (*DocumentSnapshotIterator) Stop 
    
    
    func (it *DocumentSnapshotIterator) Stop()

Stop stops receiving snapshots. You should always call Stop when you are done with a DocumentSnapshotIterator, to free up resources. It is not safe to call Stop concurrently with Next.

## DocumentsOption
    
    
    type DocumentsOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

DocumentsOption is an option for a Documents pipeline stage.

## EntityFilter
    
    
    type EntityFilter interface {
    	// contains filtered or unexported methods
    }

EntityFilter represents a Firestore filter.

## ExecuteOption
    
    
    type ExecuteOption interface {
    	// contains filtered or unexported methods
    }

ExecuteOption is an option for executing a pipeline query.

### func WithExplainMode 
    
    
    func WithExplainMode(mode ExplainMode) ExecuteOption

WithExplainMode sets the execution mode for pipeline explain.

## ExecutionStats
    
    
    type ExecutionStats struct {
    	// Total number of results returned, including documents, projections,
    	// aggregation results, keys.
    	ResultsReturned [int64](https://pkg.go.dev/builtin#int64)
    	// Total time to execute the query in the backend.
    	ExecutionDuration *time.Duration
    	// Total billable read operations.
    	ReadOperations [int64](https://pkg.go.dev/builtin#int64)
    	// Debugging statistics from the execution of the query. Note that the
    	// debugging stats are subject to change as Firestore evolves. It could
    	// include:
    	//
    	//	{
    	//	  "indexes_entries_scanned": "1000",
    	//	  "documents_scanned": "20",
    	//	  "billing_details" : {
    	//	     "documents_billable": "20",
    	//	     "index_entries_billable": "1000",
    	//	     "min_query_cost": "0"
    	//	  }
    	//	}
    	DebugStats *map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any)
    }

ExecutionStats represents execution statistics for the query.

## ExplainMetrics
    
    
    type ExplainMetrics struct {
    
    	// Planning phase information for the query.
    	PlanSummary *PlanSummary
    	// Aggregated stats from the execution of the query. Only present when
    	// ExplainOptions.analyze is set to true
    	ExecutionStats *ExecutionStats
    }

ExplainMetrics represents explain metrics for the query.

## ExplainMode
    
    
    type ExplainMode [string](https://pkg.go.dev/builtin#string)

ExplainMode is the execution mode for pipeline explain.

### ExplainModeAnalyze
    
    
    const (
    	// ExplainModeAnalyze both plans and executes the query.
    	ExplainModeAnalyze ExplainMode = "analyze"
    )

## ExplainOptions
    
    
    type ExplainOptions struct {
    	// When false (the default), Query Explain plans the query, but skips over the
    	// execution stage. This will return planner stage information.
    	//
    	// When true, Query Explain both plans and executes the query. This returns all
    	// the planner information along with statistics from the query execution runtime.
    	// This will include the billing information of the query along with system-level
    	// insights into the query execution.
    	Analyze [bool](https://pkg.go.dev/builtin#bool)
    }

ExplainOptions are Query Explain options. Query Explain allows you to submit Cloud Firestore queries to the backend and receive detailed performance statistics on backend query execution in return.

## ExplainStats
    
    
    type ExplainStats struct {
    	// contains filtered or unexported fields
    }

ExplainStats is query explain stats.

Contains all metadata related to pipeline planning and execution, specific contents depend on the supplied pipeline options.

### func (*ExplainStats) RawData 
    
    
    func (es *ExplainStats) RawData() (*[anypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb).[Any](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb#Any), [error](https://pkg.go.dev/builtin#error))

RawData returns the explain stats in an encoded proto format, as returned from the Firestore backend. The caller is responsible for unpacking this proto message.

### func (*ExplainStats) Text 
    
    
    func (es *ExplainStats) Text() ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

Text returns the explain stats as a string from the Firestore backend. If explain stats were requested with `outputFormat = 'text'`, the string is returned verbatim. If `outputFormat = 'json'`, this returns the explain stats as stringified JSON.

## Expression
    
    
    type Expression interface {
    
    	// Add creates an expression that adds two expressions together, returning it as an Expr.
    	//
    	// The parameter 'other' can be a numeric constant or a numeric [Expression].
    	Add(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// Subtract creates an expression that subtracts the right expression from the left expression, returning it as an Expr.
    	//
    	// The parameter 'other' can be a numeric constant or a numeric [Expression].
    	Subtract(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// Multiply creates an expression that multiplies the left and right expressions, returning it as an Expr.
    	//
    	// The parameter 'other' can be a numeric constant or a numeric [Expression].
    	Multiply(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// Divide creates an expression that divides the left expression by the right expression, returning it as an Expr.
    	//
    	// The parameter 'other' can be a numeric constant or a numeric [Expression].
    	Divide(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// Abs creates an expression that is the absolute value of the input field or expression.
    	Abs() Expression
    	// Floor creates an expression that is the largest integer that isn't less than the input field or expression.
    	Floor() Expression
    	// Ceil creates an expression that is the smallest integer that isn't less than the input field or expression.
    	Ceil() Expression
    	// Exp creates an expression that is the Euler's number e raised to the power of the input field or expression.
    	Exp() Expression
    	// Log creates an expression that is logarithm of the left expression to base as the right expression, returning it as an Expr.
    	//
    	// The parameter 'other' can be a numeric constant or a numeric [Expression].
    	Log(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// Log10 creates an expression that is the base 10 logarithm of the input field or expression.
    	Log10() Expression
    	// Ln creates an expression that is the natural logarithm (base e) of the input field or expression.
    	Ln() Expression
    	// Mod creates an expression that computes the modulo of the left expression by the right expression, returning it as an Expr.
    	//
    	// The parameter 'other' can be a numeric constant or a numeric [Expression].
    	Mod(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// Pow creates an expression that computes the left expression raised to the power of the right expression, returning it as an Expr.
    	//
    	// The parameter 'other' can be a numeric constant or a numeric [Expression].
    	Pow(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// Round creates an expression that rounds the input field or expression to nearest integer.
    	Round() Expression
    	// RoundToPrecision creates an expression that rounds the input field or expression to a specified number of decimal places.
    	RoundToPrecision(places [any](https://pkg.go.dev/builtin#any)) Expression
    	// Trunc creates an expression that truncates a number to an integer.
    	Trunc() Expression
    	// TruncToPrecision creates an expression that truncates a number to a specified number of decimal places.
    	//
    	// The parameter 'places' is the number of decimal places to truncate to. It can be an int, int32, int64 or [Expression].
    	TruncToPrecision(places [any](https://pkg.go.dev/builtin#any)) Expression
    
    	// Sqrt creates an expression that is the square root of the input field or expression.
    	Sqrt() Expression
    	// Cmp creates an expression that compares two expressions.
    	// Returns -1 if left < right,="" 0="" if="" left="=" right,="" and="" 1="" if="" left=""> right.
    	//
    	// The parameter 'other' can be a constant or an [Expression].
    	Cmp(other [any](https://pkg.go.dev/builtin#any)) Expression
    
    	// Array operations
    	// ArrayContains creates a boolean expression that checks if an array contains a specific value.
    	//
    	// The parameter 'value' can be a constant (e.g., string, int, bool) or an [Expression].
    	ArrayContains(value [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// ArrayContainsAll creates a boolean expression that checks if an array contains all the specified values.
    	//
    	// The parameter 'values' can be a slice of constants (e.g., []string, []int) or an [Expression] that evaluates to an array.
    	ArrayContainsAll(values [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// ArrayContainsAny creates a boolean expression that checks if an array contains any of the specified values.
    	//
    	// The parameter 'values' can be a slice of constants (e.g., []string, []int) or an [Expression] that evaluates to an array.
    	ArrayContainsAny(values [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// ArrayLength creates an expression that calculates the length of an array.
    	ArrayLength() Expression
    	// EqualAny creates a boolean expression that checks if the expression is equal to any of the specified values.
    	//
    	// The parameter 'values' can be a slice of constants (e.g., []string, []int) or an [Expression] that evaluates to an array.
    	EqualAny(values [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// NotEqualAny creates a boolean expression that checks if the expression is not equal to any of the specified values.
    	//
    	// The parameter 'values' can be a slice of constants (e.g., []string, []int) or an [Expression] that evaluates to an array.
    	NotEqualAny(values [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// ArrayGet creates an expression that retrieves an element from an array at a specified index.
    	//
    	// The parameter 'offset' is the 0-based index of the element to retrieve.
    	// It can be an integer constant or an [Expression] that evaluates to an integer.
    	ArrayGet(offset [any](https://pkg.go.dev/builtin#any)) Expression
    	// Offset creates an expression that accesses an element from an array at a specified index.
    	//
    	// This is a field access function. If the input is not an array, or if the index
    	// is out of bounds, it evaluates to an absent value.
    	//
    	// The parameter 'index' is the 0-based index of the element to retrieve. It can be an int or an [Expression].
    	// Supports negative indexing (e.g., -1 returns the last element).
    	Offset(index [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArrayReverse creates an expression that reverses the order of elements in an array.
    	ArrayReverse() Expression
    	// ArrayConcat creates an expression that concatenates multiple arrays into a single array.
    	//
    	// The parameter 'otherArrays' can be a mix of array constants (e.g., []string, []int) or [Expression]s that evaluate to arrays.
    	ArrayConcat(otherArrays ...[any](https://pkg.go.dev/builtin#any)) Expression
    	// ArraySum creates an expression that calculates the sum of all elements in a numeric array.
    	ArraySum() Expression
    	// ArrayMaximum creates an expression that finds the maximum element in a numeric array.
    	ArrayMaximum() Expression
    	// ArrayMaximumN creates an expression that finds the N maximum elements in an array.
    	//
    	// The parameter 'n' can be an integer constant or an [Expression] that evaluates to an integer.
    	ArrayMaximumN(n [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArrayMinimum creates an expression that finds the minimum element in a numeric array.
    	ArrayMinimum() Expression
    	// ArrayMinimumN creates an expression that finds the N minimum elements in an array.
    	//
    	// The parameter 'n' can be an integer constant or an [Expression] that evaluates to an integer.
    	ArrayMinimumN(n [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArrayFirst creates an expression that returns the first element of an array.
    	ArrayFirst() Expression
    	// ArrayFirstN creates an expression that returns the first N elements of an array.
    	//
    	// The parameter 'n' can be an integer constant or an [Expression] that evaluates to an integer.
    	ArrayFirstN(n [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArrayLast creates an expression that returns the last element of an array.
    	ArrayLast() Expression
    	// ArrayLastN creates an expression that returns the last N elements of an array.
    	//
    	// The parameter 'n' can be an integer constant or an [Expression] that evaluates to an integer.
    	ArrayLastN(n [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArraySliceToEnd creates an expression that returns a slice of an array starting from the specified offset.
    	//
    	// The parameter 'offset' is the 0-based index of the first element to include. It can be an int, int32, int64 or [Expression].
    	ArraySliceToEnd(offset [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArraySlice creates an expression that returns a slice of an array starting from the specified offset with a given length.
    	//
    	// The parameter 'offset' is the 0-based index of the first element to include. It can be an int, int32, int64 or [Expression].
    	// The parameter 'length' is the number of elements to include. It can be an int, int32, int64 or [Expression].
    	ArraySlice(offset, length [any](https://pkg.go.dev/builtin#any)) Expression
    	// ReferenceSliceToEnd creates an expression that returns a subset of segments from a document reference.
    	//
    	// The parameter 'offset' is the 0-based index of the first element to include. It can be an int, int32, int64 or [Expression].
    	ReferenceSliceToEnd(offset [any](https://pkg.go.dev/builtin#any)) Expression
    	// ReferenceSlice creates an expression that returns a subset of segments from a document reference.
    	//
    	// The parameter 'offset' is the 0-based index of the first element to include. It can be an int, int32, int64 or [Expression].
    	// The parameter 'length' is the number of elements to include. It can be an int, int32, int64 or [Expression].
    	ReferenceSlice(offset, length [any](https://pkg.go.dev/builtin#any)) Expression
    
    	// ArrayIndexOf creates an expression that returns the first index of a search value in an array.
    	//
    	// The parameter 'search' is the value to search for. It can be a constant or [Expression].
    	ArrayIndexOf(search [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArrayIndexOfAll creates an expression that returns the indices of all occurrences of a search value in an array.
    	//
    	// The parameter 'search' is the value to search for. It can be a constant or [Expression].
    	ArrayIndexOfAll(search [any](https://pkg.go.dev/builtin#any)) Expression
    	// ArrayLastIndexOf creates an expression that returns the last index of a search value in an array.
    	//
    	// The parameter 'search' is the value to search for. It can be a constant or [Expression].
    	ArrayLastIndexOf(search [any](https://pkg.go.dev/builtin#any)) Expression
    	// First returns the value of the expression for the first document in the group.
    	First() AggregateFunction
    	// Last returns the value of the expression for the last document in the group.
    	Last() AggregateFunction
    	// ArrayAgg returns an array containing all values of the expression when evaluated on each document in the group.
    	//
    	// If the expression resolves to an absent value, it is converted to NULL.
    	// The order of elements in the output array is not stable and shouldn't be relied upon.
    	ArrayAgg() AggregateFunction
    	// ArrayAggDistinct returns an array containing all distinct values of the expression when evaluated on each document in the group.
    	//
    	// If the expression resolves to an absent value, it is converted to NULL.
    	// The order of elements in the output array is not stable and shouldn't be relied upon.
    	ArrayAggDistinct() AggregateFunction
    	// ArrayFilter creates an expression for array_filter(array, param, body).
    	//
    	// The parameter 'param' is the name of the parameter to use in the body expression.
    	// The parameter 'body' is the expression to evaluate for each element of the array.
    	ArrayFilter(param [string](https://pkg.go.dev/builtin#string), body BooleanExpression) Expression
    	// ArrayTransform applies a transformation to each element of an array.
    	//
    	// The parameter 'param' is the name of the parameter to use in the transform expression.
    	// The parameter 'body' is the expression to evaluate for each element of the array.
    	ArrayTransform(param [string](https://pkg.go.dev/builtin#string), body Expression) Expression
    	// ArrayTransformWithIndex applies a transformation to each element of an array, providing the index.
    	//
    	// The parameter 'param' is the name of the parameter to use in the transform expression for the element.
    	// The parameter 'indexParam' is the name of the parameter to use in the transform expression for the index.
    	// The parameter 'body' is the expression to evaluate for each element of the array.
    	ArrayTransformWithIndex(param, indexParam [string](https://pkg.go.dev/builtin#string), body Expression) Expression
    	// LogicalMaximum returns the maximum value of the expression and the specified values.
    	LogicalMaximum(others ...[any](https://pkg.go.dev/builtin#any)) Expression
    	// LogicalMinimum returns the minimum value of the expression and the specified values.
    	LogicalMinimum(others ...[any](https://pkg.go.dev/builtin#any)) Expression
    
    	// Timestamp operations
    	// TimestampAdd creates an expression that adds a specified amount of time to a timestamp.
    	//
    	// The parameter 'unit' can be a string constant (e.g.,  "day") or an [Expression] that evaluates to a valid unit string.
    	// Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day".
    	// The parameter 'amount' can be an integer constant or an [Expression] that evaluates to an integer.
    	TimestampAdd(unit, amount [any](https://pkg.go.dev/builtin#any)) Expression
    	// TimestampSubtract creates an expression that subtracts a specified amount of time from a timestamp.
    	//
    	// The parameter 'unit' can be a string constant (e.g.,  "hour") or an [Expression] that evaluates to a valid unit string.
    	// Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day".
    	// The parameter 'amount' can be an integer constant or an [Expression] that evaluates to an integer.
    	TimestampSubtract(unit, amount [any](https://pkg.go.dev/builtin#any)) Expression
    	// TimestampTruncate creates an expression that truncates a timestamp to a specified granularity.
    	//
    	// The parameter 'granularity' can be a string constant (e.g.,  "month") or an [Expression] that evaluates to a valid granularity string.
    	// Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)",
    	// "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear".
    	TimestampTruncate(granularity [any](https://pkg.go.dev/builtin#any)) Expression
    	// TimestampTruncateWithTimezone creates an expression that truncates a timestamp to a specified granularity in a given timezone.
    	//
    	// The parameter 'granularity' can be a string constant (e.g.,  "week") or an [Expression] that evaluates to a valid granularity string.
    	// Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)",
    	// "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear".
    	// The parameter 'timezone' can be a string constant (e.g., "America/Los_Angeles") or an [Expression] that evaluates to a valid timezone string.
    	// Valid values are from the TZ database or in the format "Etc/GMT-1".
    	TimestampTruncateWithTimezone(granularity [any](https://pkg.go.dev/builtin#any), timezone [any](https://pkg.go.dev/builtin#any)) Expression
    	// TimestampToUnixMicros creates an expression that converts a timestamp expression to the number of microseconds since
    	// the Unix epoch (1970-01-01 00:00:00 UTC).
    	TimestampToUnixMicros() Expression
    	// TimestampToUnixMillis creates an expression that converts a timestamp expression to the number of milliseconds since
    	// the Unix epoch (1970-01-01 00:00:00 UTC).
    	TimestampToUnixMillis() Expression
    	// TimestampToUnixSeconds creates an expression that converts a timestamp expression to the number of seconds since
    	// the Unix epoch (1970-01-01 00:00:00 UTC).
    	TimestampToUnixSeconds() Expression
    	// TimestampExtract creates an expression that extracts a part from a timestamp.
    	// - part can be a string or an [Expression]. Valid parts include "microsecond", "millisecond", "second", "minute", "hour", "day",
    	//   "dayofweek", "dayofyear", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)",
    	//   "week(friday)", "week(saturday)", "week(sunday)", "month", "quarter", "year", "isoweek", and "isoyear".
    	TimestampExtract(part [any](https://pkg.go.dev/builtin#any)) Expression
    	// TimestampExtractWithTimezone creates an expression that extracts a part from a timestamp in a given timezone.
    	// - timestamp can be a field path string, [FieldPath] or [Expression].
    	// - part can be a string or an [Expression]. Valid parts include "microsecond", "millisecond", "second", "minute", "hour", "day",
    	//   "dayofweek", "dayofyear", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)",
    	//   "week(friday)", "week(saturday)", "week(sunday)", "month", "quarter", "year", "isoweek", and "isoyear".
    	// - timezone can be a string or an [Expression].
    	TimestampExtractWithTimezone(part, timezone [any](https://pkg.go.dev/builtin#any)) Expression
    	// TimestampDiff creates an expression that calculates the difference between two timestamps.
    	//
    	// The parameter 'start' can be a field path string, [FieldPath] or [Expression].
    	// The parameter 'unit' can be a string constant (e.g., "day") or an [Expression] that evaluates to a valid unit string.
    	TimestampDiff(start, unit [any](https://pkg.go.dev/builtin#any)) Expression
    	// UnixMicrosToTimestamp creates an expression that converts a Unix timestamp in microseconds to a Firestore timestamp.
    	UnixMicrosToTimestamp() Expression
    	// UnixMillisToTimestamp creates an expression that converts a Unix timestamp in milliseconds to a Firestore timestamp.
    	UnixMillisToTimestamp() Expression
    	// UnixSecondsToTimestamp creates an expression that converts a Unix timestamp in seconds to a Firestore timestamp.
    	UnixSecondsToTimestamp() Expression
    
    	// Comparison operations
    	// Equal creates a boolean expression that checks if the expression is equal to the other value.
    	//
    	// The parameter 'other' can be a constant (e.g., string, int, bool) or an [Expression].
    	Equal(other [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// NotEqual creates a boolean expression that checks if the expression is not equal to the other value.
    	//
    	// The parameter 'other' can be a constant (e.g., string, int, bool) or an [Expression].
    	NotEqual(other [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// GreaterThan creates a boolean expression that checks if the expression is greater than the other value.
    	//
    	// The parameter 'other' can be a constant (e.g., string, int, bool) or an [Expression].
    	GreaterThan(other [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// GreaterThanOrEqual creates a boolean expression that checks if the expression is greater than or equal to the other value.
    	//
    	// The parameter 'other' can be a constant (e.g., string, int, bool) or an [Expression].
    	GreaterThanOrEqual(other [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// LessThan creates a boolean expression that checks if the expression is less than the other value.
    	//
    	// The parameter 'other' can be a constant (e.g., string, int, bool) or an [Expression].
    	LessThan(other [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// LessThanOrEqual creates a boolean expression that checks if the expression is less than or equal to the other value.
    	//
    	// The parameter 'other' can be a constant (e.g., string, int, bool) or an [Expression].
    	LessThanOrEqual(other [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    
    	// General functions
    	// Length creates an expression that calculates the length of string, array, map or vector.
    	Length() Expression
    	// Reverse creates an expression that reverses a string, or array.
    	Reverse() Expression
    	// Concat creates an expression that concatenates expressions together.
    	//
    	// The parameter 'others' can be a list of constants (e.g., string, int) or [Expression].
    	Concat(others ...[any](https://pkg.go.dev/builtin#any)) Expression
    
    	// Key functions
    	// GetCollectionID creates an expression that returns the ID of the collection that contains the document.
    	GetCollectionID() Expression
    	// GetDocumentID creates an expression that returns the ID of the document.
    	GetDocumentID() Expression
    	// GetParent creates an expression that returns the parent document of a document reference.
    	GetParent() Expression
    	// GetField creates an expression that accesses a field/property of a document field using the provided key.
    	//
    	// The parameter 'key' can be a string constant or an [Expression] that evaluates to a string.
    	GetField(key [any](https://pkg.go.dev/builtin#any)) Expression
    
    	// Logical functions
    	// IfError creates an expression that evaluates and returns the receiver expression if it does not produce an error;
    	// otherwise, it evaluates and returns `catchExprOrValue`.
    	//
    	// The parameter 'catchExprOrValue' is the expression or value to return if the receiver expression errors.
    	IfError(catchExprOrValue [any](https://pkg.go.dev/builtin#any)) Expression
    	// IsError returns a boolean expression that checks if the expression evaluates to an error.
    	IsError() BooleanExpression
    	// FieldExists returns a boolean expression that checks if the field exists.
    	FieldExists() BooleanExpression
    	// IsAbsent returns a boolean expression that checks if the field is absent.
    	IsAbsent() BooleanExpression
    	// IfAbsent creates an expression that returns a default value if an expression evaluates to an absent value.
    	//
    	// The parameter 'catchExprOrValue' is the value to return if the expression is absent.
    	// It can be a constant or an [Expression].
    	IfAbsent(catchExprOrValue [any](https://pkg.go.dev/builtin#any)) Expression
    	// IfNull creates an expression that returns a default value if an expression evaluates to null.
    	//
    	// The parameter 'elseValueOrExpr' can be a constant or [Expression].
    	IfNull(elseValueOrExpr [any](https://pkg.go.dev/builtin#any)) Expression
    	// Coalesce returns the first non-null, non-absent argument, without evaluating the rest of the arguments.
    	// When all arguments are null or absent, returns the last argument.
    	//
    	// The parameter 'others' can be a list of constants or [Expression].
    	Coalesce(replacement [any](https://pkg.go.dev/builtin#any), others ...[any](https://pkg.go.dev/builtin#any)) Expression
    
    	// Object functions
    	// MapGet creates an expression that accesses a value from a map (object) field using the provided key.
    	//
    	// The parameter 'strOrExprkey' is the key to access in the map.
    	// It can be a string constant or an [Expression] that evaluates to a string.
    	MapGet(strOrExprkey [any](https://pkg.go.dev/builtin#any)) Expression
    	// MapMerge creates an expression that merges multiple maps into a single map.
    	// If multiple maps have the same key, the later value is used.
    	//
    	// The parameter 'secondMap' is an [Expression] representing the second map.
    	// The parameter 'otherMaps' is a list of additional [Expression]s representing maps to merge.
    	MapMerge(secondMap Expression, otherMaps ...Expression) Expression
    	// MapRemove creates an expression that removes a key from a map.
    	//
    	// The parameter 'strOrExprkey' is the key to remove from the map.
    	// It can be a string constant or an [Expression] that evaluates to a string.
    	MapRemove(strOrExprkey [any](https://pkg.go.dev/builtin#any)) Expression
    	// MapSet creates an expression that updates a map with key-value pairs.
    	//
    	// The parameter 'keysAndValues' is a list of alternating key and value arguments.
    	MapSet(key [any](https://pkg.go.dev/builtin#any), value [any](https://pkg.go.dev/builtin#any), moreKeysAndValues ...[any](https://pkg.go.dev/builtin#any)) Expression
    	// MapKeys creates an expression that returns the keys of a map as an array.
    	MapKeys() Expression
    	// MapValues creates an expression that returns the values of a map as an array.
    	MapValues() Expression
    	// MapEntries creates an expression that returns the entries of a map as an array of key-value maps.
    	MapEntries() Expression
    
    	// Aggregators
    	// Sum creates an aggregate function that calculates the sum of the expression.
    	Sum() AggregateFunction
    	// Average creates an aggregate function that calculates the average of the expression.
    	Average() AggregateFunction
    	// Count creates an aggregate function that counts the number of documents.
    	Count() AggregateFunction
    	// CountDistinct creates an aggregate function that counts the distinct values of the expression.
    	CountDistinct() AggregateFunction
    	// Maximum creates an aggregate function that finds the maximum value of the expression.
    	Maximum() AggregateFunction
    	// Minimum creates an aggregate function that finds the minimum value of the expression.
    	Minimum() AggregateFunction
    
    	// Data size functions
    	// StorageSize creates an expression that calculates the storage size of a field or [Expression] in bytes.
    	StorageSize() Expression
    
    	// String functions
    	// ByteLength creates an expression that calculates the length of a string represented by a field or [Expression] in UTF-8
    	// bytes.
    	ByteLength() Expression
    	// CharLength creates an expression that calculates the character length of a string field or expression in UTF8.
    	CharLength() Expression
    	// EndsWith creates a boolean expression that checks if the string expression ends with the specified suffix.
    	//
    	// The parameter 'suffix' can be a string constant or an [Expression] that evaluates to a string.
    	EndsWith(suffix [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// Like creates a boolean expression that checks if the string expression matches the specified pattern.
    	//
    	// The parameter 'suffix' can be a string constant or an [Expression] that evaluates to a string.
    	Like(suffix [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// RegexContains creates a boolean expression that checks if the string expression contains a match for the specified regex pattern.
    	//
    	// The parameter 'pattern' can be a string constant or an [Expression] that evaluates to a string.
    	RegexContains(pattern [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// RegexFind creates an expression that returns the first substring that matches the specified regex pattern.
    	//
    	// The parameter 'pattern' can be a string constant or an [Expression] that evaluates to a string.
    	RegexFind(pattern [any](https://pkg.go.dev/builtin#any)) Expression
    	// RegexFindAll creates an expression that returns all substrings that match the specified regex pattern.
    	//
    	// The parameter 'pattern' can be a string constant or an [Expression] that evaluates to a string.
    	RegexFindAll(pattern [any](https://pkg.go.dev/builtin#any)) Expression
    	// RegexMatch creates a boolean expression that checks if the string expression matches the specified regex pattern.
    	//
    	// The parameter 'pattern' can be a string constant or an [Expression] that evaluates to a string.
    	RegexMatch(pattern [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// StartsWith creates a boolean expression that checks if the string expression starts with the specified prefix.
    	//
    	// The parameter 'prefix' can be a string constant or an [Expression] that evaluates to a string.
    	StartsWith(prefix [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// StringConcat creates an expression that concatenates multiple strings into a single string.
    	//
    	// The parameter 'otherStrings' can be a mix of string constants or [Expression]s that evaluate to strings.
    	StringConcat(otherStrings ...[any](https://pkg.go.dev/builtin#any)) Expression
    	// StringContains creates a boolean expression that checks if the string expression contains the specified substring.
    	//
    	// The parameter 'substring' can be a string constant or an [Expression] that evaluates to a string.
    	StringContains(substring [any](https://pkg.go.dev/builtin#any)) BooleanExpression
    	// StringIndexOf creates an expression that returns the index of a search value in a string.
    	//
    	// The parameter 'search' can be a string constant or an [Expression] that evaluates to a string.
    	StringIndexOf(search [any](https://pkg.go.dev/builtin#any)) Expression
    	// StringRepeat creates an expression that repeats a string a specified number of times.
    	//
    	// The parameter 'repetition' can be an integer constant or an [Expression] that evaluates to an integer.
    	StringRepeat(repetition [any](https://pkg.go.dev/builtin#any)) Expression
    	// StringReplaceOne creates an expression that replaces the first occurrence of a search value with a replacement value.
    	//
    	// The parameter 'search' can be a string constant or an [Expression] that evaluates to a string.
    	// The parameter 'replacement' can be a string constant or an [Expression] that evaluates to a string.
    	StringReplaceOne(search, replacement [any](https://pkg.go.dev/builtin#any)) Expression
    	// StringReplaceAll creates an expression that replaces all occurrences of a search value with a replacement value.
    	//
    	// The parameter 'search' can be a string constant or an [Expression] that evaluates to a string.
    	// The parameter 'replacement' can be a string constant or an [Expression] that evaluates to a string.
    	StringReplaceAll(search, replacement [any](https://pkg.go.dev/builtin#any)) Expression
    	// StringReverse creates an expression that reverses a string.
    	StringReverse() Expression
    	// Join creates an expression that joins the elements of a string array into a single string.
    	//
    	// The parameter 'delimiter' can be a string constant or an [Expression] that evaluates to a string.
    	Join(delimiter [any](https://pkg.go.dev/builtin#any)) Expression
    	// Substring creates an expression that returns a substring of a string.
    	//
    	// The parameter 'index' is the starting index of the substring.
    	// It can be an integer constant or an [Expression] that evaluates to an integer.
    	// The parameter 'offset' is the length of the substring.
    	// It can be an integer constant or an [Expression] that evaluates to an integer.
    	Substring(index, offset [any](https://pkg.go.dev/builtin#any)) Expression
    	// ToLower creates an expression that converts a string to lowercase.
    	ToLower() Expression
    	// ToUpper creates an expression that converts a string to uppercase.
    	ToUpper() Expression
    	// Trim creates an expression that removes leading and trailing whitespace from a string.
    	Trim() Expression
    	// TrimValue creates an expression that removes leading and trailing whitespace or specified characters from a string.
    	TrimValue(valuesToTrim [any](https://pkg.go.dev/builtin#any)) Expression
    	// LTrim creates an expression that removes leading whitespace from a string.
    	LTrim() Expression
    	// LTrimValue creates an expression that removes leading whitespace or specified characters from a string.
    	LTrimValue(valuesToTrim [any](https://pkg.go.dev/builtin#any)) Expression
    	// RTrim creates an expression that removes trailing whitespace from a string.
    	RTrim() Expression
    	// RTrimValue creates an expression that removes trailing whitespace or specified characters from a string.
    	RTrimValue(valuesToTrim [any](https://pkg.go.dev/builtin#any)) Expression
    	// Split creates an expression that splits a string by a delimiter.
    	//
    	// The parameter 'delimiter' can be a string constant or an [Expression] that evaluates to a string.
    	Split(delimiter [any](https://pkg.go.dev/builtin#any)) Expression
    
    	// Type creates an expression that returns the type of the expression.
    	Type() Expression
    	// IsType creates a boolean expression that checks if the expression is of a specific type.
    	//
    	// The parameter 'dataType' can be one of the following string constants:
    	//   "null", "array", "boolean", "bytes", "timestamp", "geo_point", "number",
    	//   "int32", "int64", "float64", "decimal128", "map", "reference", "string",
    	//   "vector", "max_key", "min_key", "object_id", "regex", "request_timestamp".
    	IsType(dataType [string](https://pkg.go.dev/builtin#string)) BooleanExpression
    
    	// Vector functions
    	// CosineDistance creates an expression that calculates the cosine distance between two vectors.
    	//
    	// The parameter 'other' can be [Vector32], [Vector64], []float32, []float64 or an [Expression] that evaluates to a vector.
    	CosineDistance(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// DotProduct creates an expression that calculates the dot product of two vectors.
    	//
    	// The parameter 'other' can be [Vector32], [Vector64], []float32, []float64 or an [Expression] that evaluates to a vector.
    	DotProduct(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// EuclideanDistance creates an expression that calculates the euclidean distance between two vectors.
    	//
    	// The parameter 'other' can be [Vector32], [Vector64], []float32, []float64 or an [Expression] that evaluates to a vector.
    	EuclideanDistance(other [any](https://pkg.go.dev/builtin#any)) Expression
    	// VectorLength creates an expression that calculates the length of a vector.
    	VectorLength() Expression
    
    	// Ordering
    	// Ascending creates an ordering expression for ascending order.
    	Ascending() Ordering
    	// Descending creates an ordering expression for descending order.
    	Descending() Ordering
    
    	// GeoDistance creates an expression that evaluates to the distance in meters between the location in the expression and the query location.
    	//
    	// The parameter 'location' is the query location.
    	//
    	// Example:
    	//
    	//	client.Pipeline().Collection("restaurants").
    	//		Search(
    	//			WithSearchQuery("waffles"),
    	//			WithSearchSort(Ascending(FieldOf("location").GeoDistance(&latlng.LatLng{Latitude: 37.0, Longitude: -122.0}))),
    	//		)
    	//
    	// Experimental: Update, Delete and Search stages in pipeline queries are in public preview
    	// and are subject to potential breaking changes in future versions,
    	// regardless of any other documented package stability guarantees.
    	GeoDistance(location *latlng.LatLng) Expression
    
    	// As assigns an alias to an expression.
    	// Aliases are useful for renaming fields in the output of a stage.
    	As(alias [string](https://pkg.go.dev/builtin#string)) *AliasedExpression
    	// contains filtered or unexported methods
    }

Expression represents an expression that can be evaluated to a value within the execution of a [Pipeline].

Expressions are the building blocks for creating complex queries and transformations in Firestore pipelines. They can represent:

  * Field references: Access values from document fields.
  * Literals: Represent constant values (strings, numbers, booleans).
  * Function calls: Apply functions to one or more expressions.
  * Aggregations: Calculate aggregate values (e.g., sum, average) using [AggregateFunction] instances.



The [Expression] interface provides a fluent API for building expressions. You can chain together method calls to create complex expressions.

### func Abs 
    
    
    func Abs(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Abs creates an expression that is the absolute value of the input field or expression.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func Add 
    
    
    func Add(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Add creates an expression that adds two expressions together, returning it as an Expr.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a numeric constant or a numeric [Expression].



### func Array 
    
    
    func Array(elements [any](https://pkg.go.dev/builtin#any)) Expression

Array creates an expression that represents a Firestore array.

  * elements can be any number of values or expressions that will form the elements of the array.



### func ArrayConcat 
    
    
    func ArrayConcat(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), otherArrays [any](https://pkg.go.dev/builtin#any)) Expression

ArrayConcat creates an expression that concatenates multiple arrays into a single array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * otherArrays are the other arrays to concatenate.



### func ArrayFilter 
    
    
    func ArrayFilter(array [any](https://pkg.go.dev/builtin#any), param [string](https://pkg.go.dev/builtin#string), body BooleanExpression) Expression

ArrayFilter creates an expression for array_filter(array, param, body).

  * array can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * param is the name of the parameter to use in the body expression.
  * body is the expression to evaluate for each element of the array.



### func ArrayFirst 
    
    
    func ArrayFirst(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ArrayFirst creates an expression that returns the first element of an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.



### func ArrayFirstN 
    
    
    func ArrayFirstN(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), n [any](https://pkg.go.dev/builtin#any)) Expression

ArrayFirstN creates an expression that returns the first N elements of an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * n can be an int, int32, int64 or [Expression].



### func ArrayFromSlice 
    
    
    func ArrayFromSlice(elements []T) Expression

ArrayFromSlice creates a new array expression from a slice of elements. This function is necessary for creating an array from an existing typed slice (e.g., []int), as the [Array] function (which takes variadic arguments) cannot directly accept a typed slice using the spread operator (...). It handles the conversion of each element to `any` internally.

### func ArrayGet 
    
    
    func ArrayGet(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), offset [any](https://pkg.go.dev/builtin#any)) Expression

ArrayGet creates an expression that retrieves an element from an array at a specified index.

This is a typed function. It expects the first argument to be an array. If the target is not an array, the query will fail with a type error. If the target is null, the result is null.

For a version that returns an absent value (UNSET) instead of failing on type mismatch, use [Offset].

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * offset is the 0-based index of the element to retrieve. Supports negative indexing.



### func ArrayIndexOf 
    
    
    func ArrayIndexOf(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), search [any](https://pkg.go.dev/builtin#any)) Expression

ArrayIndexOf creates an expression that returns the first index of a search value in an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * search is the value to search for. It can be a constant or [Expression].



### func ArrayIndexOfAll 
    
    
    func ArrayIndexOfAll(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), search [any](https://pkg.go.dev/builtin#any)) Expression

ArrayIndexOfAll creates an expression that returns the indices of all occurrences of a search value in an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * search is the value to search for. It can be a constant or [Expression].



### func ArrayLast 
    
    
    func ArrayLast(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ArrayLast creates an expression that returns the last element of an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.



### func ArrayLastIndexOf 
    
    
    func ArrayLastIndexOf(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), search [any](https://pkg.go.dev/builtin#any)) Expression

ArrayLastIndexOf creates an expression that returns the last index of a search value in an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * search is the value to search for. It can be a constant or [Expression].



### func ArrayLastN 
    
    
    func ArrayLastN(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), n [any](https://pkg.go.dev/builtin#any)) Expression

ArrayLastN creates an expression that returns the last N elements of an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * n can be an int, int32, int64 or [Expression].



### func ArrayLength 
    
    
    func ArrayLength(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ArrayLength creates an expression that calculates the length of an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.



### func ArrayMaximum 
    
    
    func ArrayMaximum(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ArrayMaximum creates an expression that finds the maximum element in a numeric array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a numeric array.



### func ArrayMaximumN 
    
    
    func ArrayMaximumN(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), n [any](https://pkg.go.dev/builtin#any)) Expression

ArrayMaximumN creates an expression that finds the N maximum elements in an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * n can be an int, int32, int64 or [Expression].



### func ArrayMinimum 
    
    
    func ArrayMinimum(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ArrayMinimum creates an expression that finds the minimum element in a numeric array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a numeric array.



### func ArrayMinimumN 
    
    
    func ArrayMinimumN(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), n [any](https://pkg.go.dev/builtin#any)) Expression

ArrayMinimumN creates an expression that finds the N minimum elements in an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * n can be an int, int32, int64 or [Expression].



### func ArrayReverse 
    
    
    func ArrayReverse(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ArrayReverse creates an expression that reverses the order of elements in an array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.



### func ArraySlice 
    
    
    func ArraySlice(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), offset [any](https://pkg.go.dev/builtin#any), length [any](https://pkg.go.dev/builtin#any)) Expression

ArraySlice creates an expression that returns a slice of an array starting from the specified offset with a given length.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * offset is the 0-based index of the first element to include. It can be an int, int32, int64 or [Expression].
  * length is the number of elements to include. It can be an int, int32, int64 or [Expression].



### func ArraySliceToEnd 
    
    
    func ArraySliceToEnd(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), offset [any](https://pkg.go.dev/builtin#any)) Expression

ArraySliceToEnd creates an expression that returns a slice of an array starting from the specified offset.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * offset is the 0-based index of the first element to include. It can be an int, int32, int64 or [Expression].



### func ArraySum 
    
    
    func ArraySum(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ArraySum creates an expression that calculates the sum of all elements in a numeric array.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a numeric array.



### func ArrayTransform 
    
    
    func ArrayTransform(array [any](https://pkg.go.dev/builtin#any), param [string](https://pkg.go.dev/builtin#string), body Expression) Expression

ArrayTransform applies a transformation to each element of an array.

  * array can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * param is the name of the parameter to use in the transform expression.
  * body is the expression to evaluate for each element of the array.



### func ArrayTransformWithIndex 
    
    
    func ArrayTransformWithIndex(array [any](https://pkg.go.dev/builtin#any), param, indexParam [string](https://pkg.go.dev/builtin#string), body Expression) Expression

ArrayTransformWithIndex applies a transformation to each element of an array, providing the index.

  * array can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * param is the name of the parameter to use in the transform expression for the element.
  * indexParam is the name of the parameter to use in the transform expression for the index.
  * body is the expression to evaluate for each element of the array.



### func ByteLength 
    
    
    func ByteLength(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ByteLength creates an expression that calculates the length of a string represented by a field or [Expression] in UTF-8 bytes.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].



### func Ceil 
    
    
    func Ceil(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Ceil creates an expression that is the smallest integer that isn't less than the input field or expression.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func CharLength 
    
    
    func CharLength(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

CharLength creates an expression that calculates the character length of a string field or expression in UTF8.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].



### func Cmp 
    
    
    func Cmp(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Cmp creates an expression that compares the left and right expressions, returning it as an Expr. Returns -1 if left < right, 0 if left == right, and 1 if left > right.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a constant or an [Expression].



### func Coalesce 
    
    
    func Coalesce(exprOrField [any](https://pkg.go.dev/builtin#any), replacement [any](https://pkg.go.dev/builtin#any), others [any](https://pkg.go.dev/builtin#any)) Expression

Coalesce returns the first non-null, non-absent argument, without evaluating the rest of the arguments. When all arguments are null or absent, returns the last argument.

  * exprOrField can be a field path string, [FieldPath] or an [Expression].
  * replacement is the fallback expression or value if the first one evaluates to null or is absent.
  * others are optional additional expressions or values to check.



### func Concat 
    
    
    func Concat(exprOrField [any](https://pkg.go.dev/builtin#any), others [any](https://pkg.go.dev/builtin#any)) Expression

Concat creates an expression that concatenates expressions together.

  * exprOrField can be a field path string, [FieldPath] or an [Expression].
  * others can be a list of constants or [Expression].



Example:
    
    
    // Concat the 'name' field with a constant string.
    Concat("name", "-suffix")
    

### func Conditional 
    
    
    func Conditional(condition BooleanExpression, thenValOrExpr, elseValOrExpr [any](https://pkg.go.dev/builtin#any)) Expression

Conditional creates an expression that evaluates a condition and returns one of two expressions.

  * condition is the boolean expression to evaluate.
  * thenValOrExpr is the value or expression to return if the condition is true.
  * elseValOrExpr is the value or expression to return if the condition is false.



### func ConstantOf 
    
    
    func ConstantOf(value [any](https://pkg.go.dev/builtin#any)) Expression

ConstantOf creates a new constant [Expression] from a Go value. It accepts primitive types (strings, numbers, booleans), slices, arrays, maps, structs, and specific Firestore types such as time.Time, *timestamppb.Timestamp, []byte, Vector32, Vector64, *latlng.LatLng, and *DocumentRef.

### func ConstantOfNull 
    
    
    func ConstantOfNull() Expression

ConstantOfNull creates a new constant [Expression] representing a null value.

### func ConstantOfVector32 
    
    
    func ConstantOfVector32(value [][float32](https://pkg.go.dev/builtin#float32)) Expression

ConstantOfVector32 creates a new [Vector32] constant [Expression] from a slice of float32s.

### func ConstantOfVector64 
    
    
    func ConstantOfVector64(value [][float64](https://pkg.go.dev/builtin#float64)) Expression

ConstantOfVector64 creates a new [Vector64] constant [Expression] from a slice of float64s.

### func CosineDistance 
    
    
    func CosineDistance(vector1 [any](https://pkg.go.dev/builtin#any), vector2 [any](https://pkg.go.dev/builtin#any)) Expression

CosineDistance creates an expression that calculates the cosine distance between two vectors.

  * vector1 can be a field path string, [FieldPath] or [Expression].
  * vector2 can be [Vector32], [Vector64], []float32, []float64 or [Expression].



### func CurrentDocument 
    
    
    func CurrentDocument() Expression

CurrentDocument creates an expression that represents the current document being processed.

This expression is useful when you need to access the entire document as a map, or pass the document itself to a function or subquery.

Example:
    
    
    // Define the current document as a variable "doc"
    client.Pipeline().Collection("books").
        Define(AliasedExpressions(CurrentDocument().As("doc"))).
        // Access a field from the defined document variable
        Select(Fields(GetField(Variable("doc"), "title")))
    

### func CurrentTimestamp 
    
    
    func CurrentTimestamp() Expression

CurrentTimestamp creates an expression that returns the current timestamp.

### func Divide 
    
    
    func Divide(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Divide creates an expression that divides the left expression by the right expression, returning it as an Expr.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a numeric constant or a numeric [Expression].



### func DotProduct 
    
    
    func DotProduct(vector1 [any](https://pkg.go.dev/builtin#any), vector2 [any](https://pkg.go.dev/builtin#any)) Expression

DotProduct creates an expression that calculates the dot product of two vectors.

  * vector1 can be a field path string, [FieldPath] or [Expression].
  * vector2 can be [Vector32], [Vector64], []float32, []float64 or [Expression].



### func EuclideanDistance 
    
    
    func EuclideanDistance(vector1 [any](https://pkg.go.dev/builtin#any), vector2 [any](https://pkg.go.dev/builtin#any)) Expression

EuclideanDistance creates an expression that calculates the euclidean distance between two vectors.

  * vector1 can be a field path string, [FieldPath] or [Expression].
  * vector2 can be [Vector32], [Vector64], []float32, []float64 or [Expression].



### func Exp 
    
    
    func Exp(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Exp creates an expression that is the Euler's number e raised to the power of the input field or expression.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func FieldOf 
    
    
    func FieldOf(path T) Expression

FieldOf creates a new field [Expression] from a dot separated field path string or [FieldPath].

### func Floor 
    
    
    func Floor(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Floor creates an expression that is the largest integer that isn't less than the input field or expression.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func GeoDistance 
    
    
    func GeoDistance(field [any](https://pkg.go.dev/builtin#any), location *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)) Expression

GeoDistance creates an expression that evaluates to the distance in meters between the location in the specified field and the query location.

This Expression can only be used within a Search stage.

Example:
    
    
    client.Pipeline().Collection("restaurants").
        Search(
            WithSearchQuery("waffles"),
            WithSearchSort(Ascending(GeoDistance("location", &latlng.LatLng{Latitude: 37.0, Longitude: -122.0}))),
        )
    

  * field: Specifies the field in the document which contains the GeoPoint for distance computation. It can be a field path string, [FieldPath] or [Expression].
  * location: Compute distance to this GeoPoint.



Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func GetCollectionID 
    
    
    func GetCollectionID(exprOrField [any](https://pkg.go.dev/builtin#any)) Expression

GetCollectionID creates an expression that returns the ID of the collection that contains the document.

  * exprOrField can be a field path string, [FieldPath] or an [Expression] that evaluates to a field path.



### func GetDocumentID 
    
    
    func GetDocumentID(exprStringOrDocRef [any](https://pkg.go.dev/builtin#any)) Expression

GetDocumentID creates an expression that returns the ID of the document.

  * exprStringOrDocRef can be a string, a [DocumentRef], or an [Expression] that evaluates to a document reference.



### func GetField 
    
    
    func GetField(exprOrField [any](https://pkg.go.dev/builtin#any), key [any](https://pkg.go.dev/builtin#any)) Expression

GetField creates an expression that accesses a field/property of a document field using the provided key.

  * exprOrField: The expression representing the document or map.
  * key: The key of the field to access.



### func GetParent 
    
    
    func GetParent(exprStringOrDocRef [any](https://pkg.go.dev/builtin#any)) Expression

GetParent creates an expression that returns the parent document of a document reference.

  * exprStringOrDocRef can be a string representation of the document path, a [DocumentRef], or an [Expression] that evaluates to a document path.



### func IfAbsent 
    
    
    func IfAbsent(exprOrField [any](https://pkg.go.dev/builtin#any), elseValueOrExpr [any](https://pkg.go.dev/builtin#any)) Expression

IfAbsent creates an expression that returns a default value if an expression evaluates to an absent value.

  * exprOrField is the field or expression to check. It can be a field path string, [FieldPath] or an [Expression].
  * elseValueOrExpr is the value or expression to return if the expression is absent. It can be a constant or an [Expression].



### func IfError 
    
    
    func IfError(tryExpr Expression, catchExprOrValue [any](https://pkg.go.dev/builtin#any)) Expression

IfError creates an expression that evaluates and returns `tryExpr` if it does not produce an error; otherwise, it evaluates and returns `catchExprOrValue`. It returns a new [Expression] representing the if_error operation.

  * tryExpr is the expression to try.
  * catchExprOrValue is the expression or value to return if `tryExpr` errors.



### func IfNull 
    
    
    func IfNull(exprOrField [any](https://pkg.go.dev/builtin#any), elseValueOrExpr [any](https://pkg.go.dev/builtin#any)) Expression

IfNull creates an expression that returns a default value if an expression evaluates to null. Note: This function provides a fallback for both absent and explicit null values. In contrast, IfAbsent only triggers for missing fields.

  * exprOrField can be a field path string, [FieldPath] or an [Expression].
  * elseValueOrExpr is the default value or expression to return if the first evaluates to null.



### func Join 
    
    
    func Join(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), delimiter [any](https://pkg.go.dev/builtin#any)) Expression

Join creates an expression that joins the elements of a string array into a single string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string array.
  * delimiter is the string to use as a separator between elements.



### func LTrim 
    
    
    func LTrim(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

LTrim creates an expression that removes leading whitespace from a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.



### func LTrimValue 
    
    
    func LTrimValue(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), charsOrExprToTrim [any](https://pkg.go.dev/builtin#any)) Expression

LTrimValue creates an expression that removes leading whitespace or specified characters from a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * charsOrExprToTrim is a string or [Expression] specifying characters to remove.



### func Length 
    
    
    func Length(exprOrField [any](https://pkg.go.dev/builtin#any)) Expression

Length creates an expression that calculates the length of string, array, map or vector.

  * exprOrField can be a field path string, [FieldPath] or an [Expression] that returns a string, array, map or vector when evaluated.



Example:
    
    
    // Length of the 'name' field.
    Length("name")
    

### func Ln 
    
    
    func Ln(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Ln creates an expression that is the natural logarithm (base e) of the input field or expression.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func Log 
    
    
    func Log(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Log creates an expression that is logarithm of the left expression to base as the right expression, returning it as an Expr.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a constant or an [Expression].



### func Log10 
    
    
    func Log10(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Log10 creates an expression that is the base 10 logarithm of the input field or expression.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func LogicalMaximum 
    
    
    func LogicalMaximum(exprOrField [any](https://pkg.go.dev/builtin#any), others [any](https://pkg.go.dev/builtin#any)) Expression

LogicalMaximum creates an expression that evaluates to the maximum value in a list of expressions.

  * exprOrField can be a field path string, [FieldPath] or an [Expression].
  * others can be a list of constants or [Expression].



### func LogicalMinimum 
    
    
    func LogicalMinimum(exprOrField [any](https://pkg.go.dev/builtin#any), others [any](https://pkg.go.dev/builtin#any)) Expression

LogicalMinimum creates an expression that evaluates to the minimum value in a list of expressions.

  * exprOrField can be a field path string, [FieldPath] or an [Expression].
  * others can be a list of constants or [Expression].



### func Map 
    
    
    func Map(elements map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any)) Expression

Map creates an expression that creates a Firestore map value from an input object.

  * elements: The input map to evaluate in the expression.



### func MapEntries 
    
    
    func MapEntries(exprOrField [any](https://pkg.go.dev/builtin#any)) Expression

MapEntries creates an expression that returns the entries of a map as an array of key-value maps.

  * exprOrField: The expression representing the map.



### func MapGet 
    
    
    func MapGet(exprOrField [any](https://pkg.go.dev/builtin#any), strOrExprkey [any](https://pkg.go.dev/builtin#any)) Expression

MapGet creates an expression that accesses a value from a map (object) field using the provided key.

  * exprOrField: The expression representing the map.
  * strOrExprkey: The key to access in the map.



### func MapKeys 
    
    
    func MapKeys(exprOrField [any](https://pkg.go.dev/builtin#any)) Expression

MapKeys creates an expression that returns the keys of a map as an array.

  * exprOrField: The expression representing the map.



### func MapMerge 
    
    
    func MapMerge(exprOrField [any](https://pkg.go.dev/builtin#any), secondMap Expression, otherMaps ...Expression) Expression

MapMerge creates an expression that merges multiple maps into a single map. If multiple maps have the same key, the later value is used.

  * exprOrField: First map field path string, [FieldPath] or an [Expression]
  * secondMap: Second map expression that will be merged.
  * otherMaps: Additional maps to merge.



### func MapRemove 
    
    
    func MapRemove(exprOrField [any](https://pkg.go.dev/builtin#any), strOrExprkey [any](https://pkg.go.dev/builtin#any)) Expression

MapRemove creates an expression that removes a key from a map.

  * exprOrField: The expression representing the map.
  * strOrExprkey: The key to remove from the map.



### func MapSet 
    
    
    func MapSet(exprOrField [any](https://pkg.go.dev/builtin#any), key [any](https://pkg.go.dev/builtin#any), value [any](https://pkg.go.dev/builtin#any), moreKeysAndValues [any](https://pkg.go.dev/builtin#any)) Expression

MapSet creates an expression that updates a map with key-value pairs.

  * exprOrField: The expression representing the map.
  * key: The first key to set. It can be a string or an [Expression].
  * value: The first value to set. It can be a literal value or an [Expression].
  * moreKeysAndValues: Optional additional alternating key and value arguments.



### func MapValues 
    
    
    func MapValues(exprOrField [any](https://pkg.go.dev/builtin#any)) Expression

MapValues creates an expression that returns the values of a map as an array.

  * exprOrField: The expression representing the map.



### func Mod 
    
    
    func Mod(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Mod creates an expression that computes the modulo of the left expression by the right expression, returning it as an Expr.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a numeric constant or a numeric [Expression].



### func Multiply 
    
    
    func Multiply(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Multiply creates an expression that multiplies the left and right expressions, returning it as an Expr.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a numeric constant or a numeric [Expression].



### func Offset 
    
    
    func Offset(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), index [any](https://pkg.go.dev/builtin#any)) Expression

Offset creates an expression that accesses an element from an array at a specified index.

This is a field access function. If the input is not an array, or if the index is out of bounds, it evaluates to an absent value.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to an array.
  * index is the 0-based index of the element to retrieve. It can be an int or an [Expression]. Supports negative indexing (e.g., -1 returns the last element).



### func Pow 
    
    
    func Pow(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Pow creates an expression that computes the left expression raised to the power of the right expression, returning it as an Expr.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a numeric constant or a numeric [Expression].



### func RTrim 
    
    
    func RTrim(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

RTrim creates an expression that removes trailing whitespace from a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.



### func RTrimValue 
    
    
    func RTrimValue(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), charsOrExprToTrim [any](https://pkg.go.dev/builtin#any)) Expression

RTrimValue creates an expression that removes trailing whitespace or specified characters from a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * charsOrExprToTrim is a string or [Expression] specifying characters to remove.



### func Rand 
    
    
    func Rand() Expression

Rand returns a pseudo-random floating point number, chosen uniformly between 0.0 (inclusive) and 1.0 (exclusive).

### func ReferenceSlice 
    
    
    func ReferenceSlice(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), offset [any](https://pkg.go.dev/builtin#any), length [any](https://pkg.go.dev/builtin#any)) Expression

ReferenceSlice creates an expression that returns a subset of segments from a document reference with a given length.

  * exprOrField can be a field path string, [FieldPath] or an [Expression] that evaluates to a document reference.
  * offset is the 0-based index of the first segment to include. It can be an int, int32, int64 or [Expression].
  * length is the number of segments to include. It can be an int, int32, int64 or [Expression].



### func ReferenceSliceToEnd 
    
    
    func ReferenceSliceToEnd(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), offset [any](https://pkg.go.dev/builtin#any)) Expression

ReferenceSliceToEnd creates an expression that returns a subset of segments from a document reference.

  * exprOrField can be a field path string, [FieldPath] or an [Expression] that evaluates to a document reference.
  * offset is the 0-based index of the first segment to include. It can be an int, int32, int64 or [Expression].



### func RegexFind 
    
    
    func RegexFind(exprOrField [any](https://pkg.go.dev/builtin#any), pattern [any](https://pkg.go.dev/builtin#any)) Expression

RegexFind creates an expression that returns the first substring that matches the specified regex pattern.

  * exprOrField: The expression representing the string to search.
  * pattern is the regular expression to search for. It can be a string or [Expression] that evaluates to a string.



### func RegexFindAll 
    
    
    func RegexFindAll(exprOrField [any](https://pkg.go.dev/builtin#any), pattern [any](https://pkg.go.dev/builtin#any)) Expression

RegexFindAll creates an expression that returns all substrings that match the specified regex pattern.

  * exprOrField: The expression representing the string to search.
  * pattern is the regular expression to search for. It can be a string or [Expression] that evaluates to a string.



This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

### func Reverse 
    
    
    func Reverse(exprOrField [any](https://pkg.go.dev/builtin#any)) Expression

Reverse creates an expression that reverses a string, or array.

  * exprOrField can be a field path string, [FieldPath] or an [Expression] that returns a string, or array when evaluated.



Example:
    
    
    // Reverse the 'name' field.
    

Reverse("name")

### func Round 
    
    
    func Round(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Round creates an expression that rounds the input field or expression to nearest integer.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func RoundToPrecision 
    
    
    func RoundToPrecision(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any), places [any](https://pkg.go.dev/builtin#any)) Expression

RoundToPrecision creates an expression that rounds a number to a specified number of decimal places. If places is positive, rounds off digits to the right of the decimal point. If places is negative, rounds off digits to the left of the decimal point.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.
  * places can be an int, int32, int64 or [Expression].



### func Score 
    
    
    func Score() Expression

Score creates an expression that evaluates to the search score that reflects the topicality of the document to all of the text predicates (for example: DocumentMatches) in the search query.

This Expression can only be used within a Search stage.

Example:
    
    
    client.Pipeline().Collection("restaurants").
        Search(WithSearchQuery("waffles"), WithSearchSort(Descending(Score())))
    

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func Split 
    
    
    func Split(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), delimiter [any](https://pkg.go.dev/builtin#any)) Expression

Split creates an expression that splits a string by a delimiter.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * delimiter is the string to use to split by.



### func Sqrt 
    
    
    func Sqrt(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Sqrt creates an expression that is the square root of the input field or expression.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func StorageSize 
    
    
    func StorageSize(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

StorageSize creates an expression that calculates the storage size of a field or [Expression] in bytes.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].



### func StringConcat 
    
    
    func StringConcat(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), otherStrings [any](https://pkg.go.dev/builtin#any)) Expression

StringConcat creates an expression that concatenates multiple strings into a single string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * otherStrings are optional additional string expressions or string constants to concatenate.



### func StringIndexOf 
    
    
    func StringIndexOf(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), search [any](https://pkg.go.dev/builtin#any)) Expression

StringIndexOf creates an expression that returns the index of a search value in a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * search is the value to search for. It can be a string or [Expression].



### func StringRepeat 
    
    
    func StringRepeat(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), repetition [any](https://pkg.go.dev/builtin#any)) Expression

StringRepeat creates an expression that repeats a string a specified number of times.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * repetition is the number of times to repeat the string. It can be an int, int32, int64 or [Expression].



### func StringReplaceAll 
    
    
    func StringReplaceAll(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), search, replacement [any](https://pkg.go.dev/builtin#any)) Expression

StringReplaceAll creates an expression that replaces all occurrences of a search value with a replacement value.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * search is the value to search for. It can be a string or [Expression].
  * replacement is the value to replace with. It can be a string or [Expression].



### func StringReplaceOne 
    
    
    func StringReplaceOne(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), search, replacement [any](https://pkg.go.dev/builtin#any)) Expression

StringReplaceOne creates an expression that replaces the first occurrence of a search value with a replacement value.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * search is the value to search for. It can be a string or [Expression].
  * replacement is the value to replace with. It can be a string or [Expression].



### func StringReverse 
    
    
    func StringReverse(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

StringReverse creates an expression that reverses a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.



### func Substring 
    
    
    func Substring(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), index [any](https://pkg.go.dev/builtin#any), length [any](https://pkg.go.dev/builtin#any)) Expression

Substring creates an expression that returns a substring of a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * index is the starting index of the substring.
  * length is the length of the substring.



### func Subtract 
    
    
    func Subtract(left, right [any](https://pkg.go.dev/builtin#any)) Expression

Subtract creates an expression that subtracts the right expression from the left expression, returning it as an Expr.

  * left can be a field path string, [FieldPath] or [Expression].
  * right can be a numeric constant or a numeric [Expression].



### func SwitchOn 
    
    
    func SwitchOn(condition BooleanExpression, result [any](https://pkg.go.dev/builtin#any), others [any](https://pkg.go.dev/builtin#any)) Expression

SwitchOn creates an expression that evaluates to the result corresponding to the first true condition.

This function behaves like a `switch` statement. It accepts an alternating sequence of conditions and their corresponding results. If an odd number of arguments is provided, the final argument serves as a default fallback result. If no default is provided and no condition evaluates to true, it throws an error.

  * condition: The first condition to check. Must be a [BooleanExpression].
  * result: The result to return if the first condition is true. Can be an [Expression] or a literal value.
  * others: Additional alternating conditions and results, optionally followed by a default fallback value.



Example:
    
    
    firestore.SwitchOn(
        firestore.FieldOf("score").GreaterThan(90), "A",
        firestore.FieldOf("score").GreaterThan(80), "B",
        "F", // Default result
    )
    

### func TimestampAdd 
    
    
    func TimestampAdd(timestamp, unit, amount [any](https://pkg.go.dev/builtin#any)) Expression

TimestampAdd creates an expression that adds a specified amount of time to a timestamp.

  * timestamp can be a field path string, [FieldPath] or [Expression].
  * unit can be a string or an [Expression]. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day".
  * amount can be an int, int32, int64 or [Expression].



### func TimestampDiff 
    
    
    func TimestampDiff(end, start, unit [any](https://pkg.go.dev/builtin#any)) Expression

TimestampDiff creates an expression that calculates the difference between two timestamps.

  * end can be a field path string, [FieldPath] or [Expression].
  * start can be a field path string, [FieldPath] or [Expression].
  * unit can be a string or an [Expression]. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day".



### func TimestampExtract 
    
    
    func TimestampExtract(timestamp, part [any](https://pkg.go.dev/builtin#any)) Expression

TimestampExtract creates an expression that extracts a part from a timestamp.

  * timestamp can be a field path string, [FieldPath] or [Expression].
  * part can be a string or an [Expression]. Valid parts include "microsecond", "millisecond", "second", "minute", "hour", "day", "dayofweek", "dayofyear", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "month", "quarter", "year", "isoweek", and "isoyear".



### func TimestampExtractWithTimezone 
    
    
    func TimestampExtractWithTimezone(timestamp, part, timezone [any](https://pkg.go.dev/builtin#any)) Expression

TimestampExtractWithTimezone creates an expression that extracts a part from a timestamp in a given timezone.

  * timestamp can be a field path string, [FieldPath] or [Expression].
  * part can be a string or an [Expression]. Valid parts include "microsecond", "millisecond", "second", "minute", "hour", "day", "dayofweek", "dayofyear", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "month", "quarter", "year", "isoweek", and "isoyear".
  * timezone can be a string or an [Expression].



### func TimestampSubtract 
    
    
    func TimestampSubtract(timestamp, unit, amount [any](https://pkg.go.dev/builtin#any)) Expression

TimestampSubtract creates an expression that subtracts a specified amount of time from a timestamp.

  * timestamp can be a field path string, [FieldPath] or [Expression].
  * unit can be a string or an [Expression]. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day".
  * amount can be an int, int32, int64 or [Expression].



### func TimestampToUnixMicros 
    
    
    func TimestampToUnixMicros(timestamp [any](https://pkg.go.dev/builtin#any)) Expression

TimestampToUnixMicros creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

  * timestamp can be a field path string, [FieldPath] or [Expression].



### func TimestampToUnixMillis 
    
    
    func TimestampToUnixMillis(timestamp [any](https://pkg.go.dev/builtin#any)) Expression

TimestampToUnixMillis creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

  * timestamp can be a field path string, [FieldPath] or [Expression].



### func TimestampToUnixSeconds 
    
    
    func TimestampToUnixSeconds(timestamp [any](https://pkg.go.dev/builtin#any)) Expression

TimestampToUnixSeconds creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

  * timestamp can be a field path string, [FieldPath] or [Expression].



### func TimestampTruncate 
    
    
    func TimestampTruncate(timestamp, granularity [any](https://pkg.go.dev/builtin#any)) Expression

TimestampTruncate creates an expression that truncates a timestamp to a specified granularity.

  * timestamp can be a field path string, [FieldPath] or [Expression].
  * granularity can be a string or an [Expression]. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear".



### func TimestampTruncateWithTimezone 
    
    
    func TimestampTruncateWithTimezone(timestamp, granularity [any](https://pkg.go.dev/builtin#any), timezone [any](https://pkg.go.dev/builtin#any)) Expression

TimestampTruncateWithTimezone creates an expression that truncates a timestamp to a specified granularity in a given timezone.

  * timestamp can be a field path string, [FieldPath] or [Expression].
  * granularity can be a string or an [Expression]. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear".
  * timezone can be a string or an [Expression]. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1".



### func ToLower 
    
    
    func ToLower(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ToLower creates an expression that converts a string to lowercase.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.



### func ToUpper 
    
    
    func ToUpper(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

ToUpper creates an expression that converts a string to uppercase.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.



### func Trim 
    
    
    func Trim(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Trim creates an expression that removes leading and trailing whitespace from a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.



### func TrimValue 
    
    
    func TrimValue(exprOrFieldPath [any](https://pkg.go.dev/builtin#any), charsOrExprToTrim [any](https://pkg.go.dev/builtin#any)) Expression

TrimValue creates an expression that removes specified characters from the beginning and end of a string.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that evaluates to a string.
  * charsOrExprToTrim is a string or [Expression] specifying characters to remove.



### func Trunc 
    
    
    func Trunc(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Trunc creates an expression that truncates a number to an integer.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.



### func TruncToPrecision 
    
    
    func TruncToPrecision(numericExprOrFieldPath [any](https://pkg.go.dev/builtin#any), places [any](https://pkg.go.dev/builtin#any)) Expression

TruncToPrecision creates an expression that truncates a number to a specified number of decimal places.

  * numericExprOrFieldPath can be a field path string, [FieldPath] or an [Expression] that returns a number when evaluated.
  * places can be an int, int32, int64 or [Expression].



### func Type 
    
    
    func Type(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

Type creates an expression that returns the type of the expression.

  * exprOrFieldPath can be a field path string, [FieldPath] or an [Expression].



### func UnixMicrosToTimestamp 
    
    
    func UnixMicrosToTimestamp(micros [any](https://pkg.go.dev/builtin#any)) Expression

UnixMicrosToTimestamp creates an expression that converts a Unix timestamp in microseconds to a Firestore timestamp.

  * micros can be a field path string, [FieldPath] or [Expression].



### func UnixMillisToTimestamp 
    
    
    func UnixMillisToTimestamp(millis [any](https://pkg.go.dev/builtin#any)) Expression

UnixMillisToTimestamp creates an expression that converts a Unix timestamp in milliseconds to a Firestore timestamp.

  * millis can be a field path string, [FieldPath] or [Expression].



### func UnixSecondsToTimestamp 
    
    
    func UnixSecondsToTimestamp(seconds [any](https://pkg.go.dev/builtin#any)) Expression

UnixSecondsToTimestamp creates an expression that converts a Unix timestamp in seconds to a Firestore timestamp.

  * seconds can be a field path string, [FieldPath] or [Expression].



### func Variable 
    
    
    func Variable(name [string](https://pkg.go.dev/builtin#string)) Expression

Variable creates an expression that retrieves the value of a variable bound via Define.

Example:
    
    
    // Define a variable "discountedPrice" and use it in a filter
    client.Pipeline().Collection("products").
        Define(AliasedExpressions(Multiply("price", 0.9).As("discountedPrice"))).
        Where(LessThan(Variable("discountedPrice"), 100))
    

### func VectorLength 
    
    
    func VectorLength(exprOrFieldPath [any](https://pkg.go.dev/builtin#any)) Expression

VectorLength creates an expression that calculates the length of a vector.

  * exprOrFieldPath can be a field path string, [FieldPath] or [Expression].



## FieldNotFoundError
    
    
    type FieldNotFoundError struct {
    	Path [string](https://pkg.go.dev/builtin#string)
    }

FieldNotFoundError is returned by DocumentSnapshot.DataAt and DocumentSnapshot.DataAtPath when the given field does not exist.

### func (*FieldNotFoundError) Error 
    
    
    func (e *FieldNotFoundError) Error() [string](https://pkg.go.dev/builtin#string)

## FieldPath
    
    
    type FieldPath [][string](https://pkg.go.dev/builtin#string)

A FieldPath is a non-empty sequence of non-empty fields that reference a value.

A FieldPath value should only be necessary if one of the field names contains one of the runes ".˜*/[]". Most methods accept a simpler form of field path as a string in which the individual fields are separated by dots. For example,
    
    
    []string{"a", "b"}
    

is equivalent to the string form
    
    
    "a.b"
    

but
    
    
    []string{"*"}
    

has no equivalent string form.

## FindNearestOption
    
    
    type FindNearestOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

FindNearestOption is an option for a FindNearest pipeline stage.

### func WithFindNearestDistanceField 
    
    
    func WithFindNearestDistanceField(field [string](https://pkg.go.dev/builtin#string)) FindNearestOption

WithFindNearestDistanceField specifies the name of the field to store the calculated distance.

### func WithFindNearestLimit 
    
    
    func WithFindNearestLimit(limit [int](https://pkg.go.dev/builtin#int)) FindNearestOption

WithFindNearestLimit specifies the maximum number of nearest neighbors to return.

## FindNearestOptions
    
    
    type FindNearestOptions struct {
    	// DistanceThreshold specifies a threshold for which no less similar documents
    	// will be returned. The behavior of the specified [DistanceMeasure] will
    	// affect the meaning of the distance threshold. Since [DistanceMeasureDotProduct]
    	// distances increase when the vectors are more similar, the comparison is inverted.
    	// For [DistanceMeasureEuclidean], [DistanceMeasureCosine]: WHERE distance <= distancethreshold="" for="" [distancemeasuredotproduct]:="" where="" distance="">= distance_threshold
    	DistanceThreshold *[float64](https://pkg.go.dev/builtin#float64)
    
    	// DistanceResultField specifies name of the document field to output the result of
    	// the vector distance calculation.
    	// If the field already exists in the document, its value get overwritten with the distance calculation.
    	// Otherwise, a new field gets added to the document.
    	DistanceResultField [string](https://pkg.go.dev/builtin#string)
    }

FindNearestOptions are options for a FindNearest vector query.

## FunctionExpression
    
    
    type FunctionExpression interface {
    	Expression
    	// contains filtered or unexported methods
    }

FunctionExpression represents Firestore [Pipeline] functions, which can be evaluated within pipeline execution.

## LimitOption
    
    
    type LimitOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

LimitOption is an option for a Limit pipeline stage.

## LiteralsOption
    
    
    type LiteralsOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

LiteralsOption is an option for a Literals pipeline stage.

## OffsetOption
    
    
    type OffsetOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

OffsetOption is an option for an Offset pipeline stage.

## OrFilter
    
    
    type OrFilter struct {
    	Filters []EntityFilter
    }

OrFilter represents a union of two or more filters.

## Ordering
    
    
    type Ordering struct {
    	Expr      Expression
    	Direction OrderingDirection
    }

Ordering specifies the field and direction for sorting.

### func Ascending 
    
    
    func Ascending(expr Expression) Ordering

Ascending creates an Ordering for ascending sort direction.

### func Descending 
    
    
    func Descending(expr Expression) Ordering

Descending creates an Ordering for descending sort direction.

### func Orders 
    
    
    func Orders(o ...Ordering) []Ordering

Orders is a helper function that returns its arguments as a slice of Ordering. It is used to provide variadic-like ergonomics for the Sort pipeline stage.

## OrderingDirection
    
    
    type OrderingDirection [string](https://pkg.go.dev/builtin#string)

OrderingDirection is the sort direction for pipeline result ordering.

### OrderingAsc, OrderingDesc
    
    
    const (
    	// OrderingAsc sorts results from smallest to largest.
    	OrderingAsc OrderingDirection = OrderingDirection("ascending")
    
    	// OrderingDesc sorts results from largest to smallest.
    	OrderingDesc OrderingDirection = OrderingDirection("descending")
    )

## Pipeline
    
    
    type Pipeline struct {
    	// contains filtered or unexported fields
    }

Pipeline class provides a flexible and expressive framework for building complex data transformation and query pipelines for Firestore.

A pipeline takes data sources, such as Firestore collections or collection groups, and applies a series of stages that are chained together. Each stage takes the output from the previous stage (or the data source) and produces an output for the next stage (or as the final output of the pipeline).

Expressions can be used within each stages to filter and transform data through the stage.

NOTE: The chained stages do not prescribe exactly how Firestore will execute the pipeline. Instead, Firestore only guarantees that the result is the same as if the chained stages were executed in order.

### func Subcollection 
    
    
    func Subcollection(path [string](https://pkg.go.dev/builtin#string)) *Pipeline

Subcollection creates a new [Pipeline] that operates on a subcollection of the current document.

This method allows you to start a new pipeline that operates on a subcollection of the current document. It is intended to be used as a subquery.

Note: A pipeline created with `Subcollection` cannot be executed directly using [Pipeline.Execute]. It must be used within a parent pipeline.

Example:
    
    
    client.Pipeline().Collection("books").
        AddFields(Selectables(
            Subcollection("reviews").
                Aggregate(Accumulators(Average("rating").As("avg_rating"))).
                ToScalarExpression().As("average_rating"),
        ))
    

### func (*Pipeline) AddFields 
    
    
    func (p *Pipeline) AddFields(fields []Selectable, opts ...AddFieldsOption) *Pipeline

AddFields adds new fields to outputs from previous stages.

This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones (if there is name overlaps).

The added fields are defined using [Selectable]'s. Use [Selectables] to provide variadic-like ergonomics for the fields argument.

### func (*Pipeline) Aggregate 
    
    
    func (p *Pipeline) Aggregate(accumulators []*AliasedAggregate, opts ...AggregateOption) *Pipeline

Aggregate performs aggregation operations on the documents from previous stages. This stage allows you to calculate aggregate values over a set of documents. You define the aggregations to perform using [AliasedAggregate] expressions which are typically results of calling AggregateFunction.As on [AggregateFunction] instances. Use [Accumulators] to provide variadic-like ergonomics for the accumulators argument.

Example:
    
    
    client.Pipeline().Collection("users").
        Aggregate(Accumulators(Sum("age").As("age_sum")))
    

### func (*Pipeline) Define 
    
    
    func (p *Pipeline) Define(variables []*AliasedExpression, opts ...DefineOption) *Pipeline

Define defines one or more variables in the pipeline's scope. `Define` is used to bind a value to a variable for internal reuse within the pipeline body (accessed via the [Variable] function).

This stage is useful for declaring reusable values or intermediate calculations that can be referenced multiple times in later parts of the pipeline, improving readability and maintainability.

Each variable is defined using an [AliasedExpression], which pairs an expression with a name (alias).

Example:
    
    
    // Define a variable and use it in a filter
    client.Pipeline().Collection("products").
        Define(AliasedExpressions(
            Multiply("price", 0.9).As("discountedPrice"),
            Add("stock", 10).As("newStock"),
        )).
        Where(LessThan(Variable("discountedPrice"), 100)).
        Select(Fields("name", Variable("newStock")))
    

### func (*Pipeline) Delete 
    
    
    func (p *Pipeline) Delete(opts ...DeleteOption) *Pipeline

Delete deletes the documents from previous stages.

Example:
    
    
    client.Pipeline().Collection("logs").
        Where(Equal("status", "archived")).
        Delete()
    

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func (*Pipeline) Distinct 
    
    
    func (p *Pipeline) Distinct(fields [][any](https://pkg.go.dev/builtin#any), opts ...DistinctOption) *Pipeline

Distinct removes duplicate documents from the outputs of previous stages.

You can optionally specify fields or [Selectable] expressions to determine distinctness. If no fields are specified, the entire document is used to determine distinctness. Use [Fields] to provide variadic-like ergonomics for the fields argument.

### func (*Pipeline) Execute 
    
    
    func (p *Pipeline) Execute(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...ExecuteOption) *PipelineSnapshot

Execute executes the pipeline and returns a snapshot of the results.

### func (*Pipeline) FindNearest 
    
    
    func (p *Pipeline) FindNearest(vectorField [any](https://pkg.go.dev/builtin#any), queryVector [any](https://pkg.go.dev/builtin#any), measure PipelineDistanceMeasure, opts ...FindNearestOption) *Pipeline

FindNearest performs vector distance (similarity) search with given parameters to the stage inputs.

This stage adds a "nearest neighbor search" capability to your pipelines. Given a field that stores vectors and a target vector, this stage will identify and return the inputs whose vector field is closest to the target vector.

The vectorField can be a string, a FieldPath or an Expr. The queryVector can be Vector32, Vector64, []float32, or []float64.

### func (*Pipeline) Limit 
    
    
    func (p *Pipeline) Limit(limit [int](https://pkg.go.dev/builtin#int), opts ...LimitOption) *Pipeline

Limit limits the maximum number of documents returned by previous stages.

### func (*Pipeline) Offset 
    
    
    func (p *Pipeline) Offset(offset [int](https://pkg.go.dev/builtin#int), opts ...OffsetOption) *Pipeline

Offset skips the first `offset` number of documents from the results of previous stages.

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with [*Pipeline.Limit] to control the size of each page.

Example: Retrieve the second page of 20 results
    
    
      client.Pipeline().Collection("books").
          .Offset(20)   // Skip the first 20 results
          .Limit(20)    // Take the next 20 results
    

### func (*Pipeline) RawStage 
    
    
    func (p *Pipeline) RawStage(name [string](https://pkg.go.dev/builtin#string), args [][any](https://pkg.go.dev/builtin#any), opts ...StageOption) *Pipeline

RawStage adds a generic stage to the pipeline. This method provides a flexible way to extend the pipeline's functionality by adding custom stages.

Example:
    
    
    // Assume we don't have a built-in "where" stage
    client.Pipeline().Collection("books").
        RawStage("where", []any{LessThan(FieldOf("published"), 1900)}).
        Select(Fields("title", "author"))
    

### func (*Pipeline) RemoveFields 
    
    
    func (p *Pipeline) RemoveFields(fields [][any](https://pkg.go.dev/builtin#any), opts ...RemoveFieldsOption) *Pipeline

RemoveFields removes fields from outputs from previous stages. fieldpaths can be a string or a [FieldPath] or an expression obtained by calling [FieldOf]. Use [Fields] to provide variadic-like ergonomics for the fields argument.

### func (*Pipeline) ReplaceWith 
    
    
    func (p *Pipeline) ReplaceWith(fieldpathOrExpr [any](https://pkg.go.dev/builtin#any), opts ...ReplaceWithOption) *Pipeline

ReplaceWith fully overwrites all fields in a document with those coming from a nested map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

Example:
    
    
    // Input: { "name": "John Doe Jr.", "parents": { "father": "John Doe Sr.", "mother": "Jane Doe" } }
    // Emit parents as document.
    client.Pipeline().Collection("people").ReplaceWith("parents")
    // Output: { "father": "John Doe Sr.", "mother": "Jane Doe" }
    

### func (*Pipeline) Sample 
    
    
    func (p *Pipeline) Sample(sampler *Sampler, opts ...SampleOption) *Pipeline

Sample performs a pseudo-random sampling of the documents from the previous stage.

This stage will filter documents pseudo-randomly. The behavior is defined by the Sampler. Use WithDocLimit or WithPercentage to create a Sampler.

Example:
    
    
    // Sample 10 books, if available.
    client.Pipeline().Collection("books").Sample(WithDocLimit(10))
    
    // Sample 50% of books.
    client.Pipeline().Collection("books").Sample(WithPercentage(0.5))
    

### func (*Pipeline) Search 
    
    
    func (p *Pipeline) Search(opts ...SearchOption) *Pipeline

Search adds a search stage to the Pipeline. This must be the first stage of the pipeline. A limited set of expressions are supported in the search stage. Use [WithSearchQuery] to specify the search query.

Example:
    
    
    client.Pipeline().Collection("restaurants").Search(
        WithSearchQuery(DocumentMatches("waffles OR pancakes")),
        WithSearchSort(Descending(Score())),
        WithSearchRetrievalDepth(10),
    )
    

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func (*Pipeline) Select 
    
    
    func (p *Pipeline) Select(fields [][any](https://pkg.go.dev/builtin#any), opts ...SelectOption) *Pipeline

Select selects or creates a set of fields from the outputs of previous stages. The selected fields are defined using field path string, [FieldPath] or [Selectable] expressions. [Selectable] expressions can be:

  * Field: References an existing field.
  * Function: Represents the result of a function with an assigned alias name using [FunctionExpression.As].



Use [Fields] to provide variadic-like ergonomics for the fields argument.

Example:
    
    
        client.Pipeline().Collection("users").Select(Fields("info.email"))
        client.Pipeline().Collection("users").Select(Fields(FieldOf("info.email")))
        client.Pipeline().Collection("users").Select(Fields(FieldOf([]string{"info", "email"})))
        client.Pipeline().Collection("users").Select([]any{"info.email", "name"})
        client.Pipeline().Collection("users").Select(Fields(Add("age", 5).As("agePlus5")))
    

### func (*Pipeline) Sort 
    
    
    func (p *Pipeline) Sort(orders []Ordering, opts ...SortOption) *Pipeline

Sort sorts the documents by the given fields and directions. Use [Orders] to provide variadic-like ergonomics for the orders argument.

### func (*Pipeline) ToArrayExpression 
    
    
    func (p *Pipeline) ToArrayExpression() Expression

ToArrayExpression converts this Pipeline into an expression that evaluates to an array result.

Example:
    
    
    // Embed a subcollection of reviews as an array into each restaurant document
    client.Pipeline().Collection("restaurants").
        AddFields(Selectables(
            Subcollection("reviews").
                Select(Fields("reviewer", "rating")).
                ToArrayExpression().As("reviews"),
        ))
    // Output format:
    // [
    //   {
    //     "name": "The Burger Joint",
    //     "reviews": [
    //       { "reviewer": "Alice", "rating": 5 },
    //       { "reviewer": "Bob", "rating": 4 }
    //     ]
    //   }
    // ]
    

### func (*Pipeline) ToScalarExpression 
    
    
    func (p *Pipeline) ToScalarExpression() Expression

ToScalarExpression converts this Pipeline into an expression that evaluates to a single scalar result. Used for 1:1 lookups or Aggregations when the subquery is expected to return a single value or object.

Example:
    
    
    // Calculate average rating for each restaurant using a subquery
    client.Pipeline().Collection("restaurants").
        AddFields(Selectables(
            Subcollection("reviews").
                Aggregate(Accumulators(Average("rating").As("avg_score"))).
                ToScalarExpression().As("stats"),
        ))
    // Output format:
    // [
    //   {
    //     "name": "The Burger Joint",
    //     "stats": {
    //       "avg_score": 4.8,
    //       "review_count": 120
    //     }
    //   }
    // ]
    

### func (*Pipeline) Union 
    
    
    func (p *Pipeline) Union(other *Pipeline, opts ...UnionOption) *Pipeline

Union performs union of all documents from two pipelines, including duplicates.

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the other [*Pipeline] given in parameter. The order of documents emitted from this stage is undefined.

Example:
    
    
    // Emit documents from books collection and magazines collection.
    client.Pipeline().Collection("books").
        Union(client.Pipeline().Collection("magazines"))
    

### func (*Pipeline) Unnest 
    
    
    func (p *Pipeline) Unnest(field Selectable, opts ...UnnestOption) *Pipeline

Unnest produces a document for each element in an array field. For each input document, this stage outputs zero or more documents. Each output document is a copy of the input document, but the array field is replaced by an element from the array. The `field` parameter specifies the array field to unnest. It can be a string representing the field path or a [Selectable] expression. The alias of the selectable will be used as the new field name.

### func (*Pipeline) UnnestWithAlias 
    
    
    func (p *Pipeline) UnnestWithAlias(fieldpath [any](https://pkg.go.dev/builtin#any), alias [string](https://pkg.go.dev/builtin#string), opts ...UnnestOption) *Pipeline

UnnestWithAlias produces a document for each element in an array field, with a specified alias for the unnested field. It can optionally take UnnestOptions.

### func (*Pipeline) Update 
    
    
    func (p *Pipeline) Update(opts ...UpdateOption) *Pipeline

Update performs an update operation using documents from previous stages.

This method updates the documents in the database based on the data flowing through the pipeline. You can optionally specify a list of [Selectable] field transformations using [WithUpdateTransformations]. If no transformations are provided, the entire document flowing from the previous stage is used as the update payload.

Example:
    
    
    // In-place update
    client.Pipeline().Literals(updateData).Update()
    
    // Update with transformations
    client.Pipeline().Collection("books").
        Where(GreaterThan("price", 50)).
        Update(WithUpdateTransformations(ConstantOf("Discounted").As("status")))
    

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func (*Pipeline) Where 
    
    
    func (p *Pipeline) Where(condition BooleanExpression, opts ...WhereOption) *Pipeline

Where filters the documents from previous stages to only include those matching the specified [BooleanExpression].

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL.

### func (*Pipeline) WithReadOptions 
    
    
    func (p *Pipeline) WithReadOptions(opts ...ReadOption) *Pipeline

WithReadOptions specifies constraints for accessing documents from the database, such as ReadTime.

## PipelineDistanceMeasure
    
    
    type PipelineDistanceMeasure [string](https://pkg.go.dev/builtin#string)

PipelineDistanceMeasure is the distance measure for find_nearest pipeline stage.

### PipelineDistanceMeasureEuclidean, PipelineDistanceMeasureCosine, PipelineDistanceMeasureDotProduct
    
    
    const (
    	// PipelineDistanceMeasureEuclidean is used to measures the Euclidean distance between the vectors.
    	PipelineDistanceMeasureEuclidean PipelineDistanceMeasure = "euclidean"
    	// PipelineDistanceMeasureCosine compares vectors based on the angle between them.
    	PipelineDistanceMeasureCosine PipelineDistanceMeasure = "cosine"
    	// PipelineDistanceMeasureDotProduct is similar to cosine but is affected by the magnitude of the vectors.
    	PipelineDistanceMeasureDotProduct PipelineDistanceMeasure = "dot_product"
    )

## PipelineResult
    
    
    type PipelineResult struct {
    	// contains filtered or unexported fields
    }

PipelineResult is a result returned from executing a pipeline.

### func (*PipelineResult) CreateTime 
    
    
    func (p *PipelineResult) CreateTime() *[time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

CreateTime returns the time at which the document was created.

### func (*PipelineResult) Data 
    
    
    func (p *PipelineResult) Data() map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any)

Data returns the PipelineResult's fields as a map. It is equivalent to
    
    
    var m map[string]any
    p.DataTo(&m)
    

### func (*PipelineResult) DataTo 
    
    
    func (p *PipelineResult) DataTo(v [any](https://pkg.go.dev/builtin#any)) [error](https://pkg.go.dev/builtin#error)

DataTo uses the PipelineResult's fields to populate v, which can be a pointer to a map[string]any or a pointer to a struct. This is similar to [DocumentSnapshot.DataTo]

### func (*PipelineResult) ExecutionTime 
    
    
    func (p *PipelineResult) ExecutionTime() *[time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

ExecutionTime returns the time at which the document(s) were read.

### func (*PipelineResult) Exists 
    
    
    func (p *PipelineResult) Exists() [bool](https://pkg.go.dev/builtin#bool)

Exists reports whether the PipelineResult represents an document. Even if Exists returns false, the rest of the fields are valid.

### func (*PipelineResult) Ref 
    
    
    func (p *PipelineResult) Ref() *DocumentRef

Ref returns the DocumentRef for this result.

### func (*PipelineResult) UpdateTime 
    
    
    func (p *PipelineResult) UpdateTime() *[time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

UpdateTime returns the time at which the document was last changed.

## PipelineResultIterator
    
    
    type PipelineResultIterator struct {
    	// contains filtered or unexported fields
    }

PipelineResultIterator is an iterator over PipelineResults from a pipeline execution.

### func (*PipelineResultIterator) GetAll 
    
    
    func (it *PipelineResultIterator) GetAll() ([]*PipelineResult, [error](https://pkg.go.dev/builtin#error))

GetAll returns all the documents remaining from the iterator. It is not necessary to call Stop on the iterator after calling GetAll.

### func (*PipelineResultIterator) Next 
    
    
    func (it *PipelineResultIterator) Next() (*PipelineResult, [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

In addition, if Next returns an error other than iterator.Done, all subsequent calls will return the same error. To continue iteration, a new PipelineResultIterator must be created.

### func (*PipelineResultIterator) Stop 
    
    
    func (it *PipelineResultIterator) Stop()

Stop stops the iterator, freeing its resources. Always call Stop when you are done with a DocumentIterator. It is not safe to call Stop concurrently with Next.

## PipelineSnapshot
    
    
    type PipelineSnapshot struct {
    	// contains filtered or unexported fields
    }

PipelineSnapshot contains zero or more [PipelineResult] objects representing the documents returned by a pipeline query. It provides methods to iterate over the documents and access metadata about the query results.

### func (*PipelineSnapshot) ExecutionTime 
    
    
    func (ps *PipelineSnapshot) ExecutionTime() (*[time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time), [error](https://pkg.go.dev/builtin#error))

ExecutionTime returns the time at which the pipeline was executed. It is available only after the iterator reaches the end.

### func (*PipelineSnapshot) ExplainStats 
    
    
    func (ps *PipelineSnapshot) ExplainStats() *ExplainStats

ExplainStats returns stats from query explain. If [WithExplainMode] was set to [ExplainModeExplain] or left unset, then no stats will be available.

### func (*PipelineSnapshot) Results 
    
    
    func (ps *PipelineSnapshot) Results() *PipelineResultIterator

Results returns an iterator over the query results.

## PipelineSource
    
    
    type PipelineSource struct {
    	// contains filtered or unexported fields
    }

PipelineSource is a factory for creating Pipeline instances. It is obtained by calling [Client.Pipeline].

### func (*PipelineSource) Collection 
    
    
    func (ps *PipelineSource) Collection(path [string](https://pkg.go.dev/builtin#string), opts ...CollectionOption) *Pipeline

Collection creates a new [Pipeline] that operates on the specified Firestore collection.

### func (*PipelineSource) CollectionGroup 
    
    
    func (ps *PipelineSource) CollectionGroup(collectionID [string](https://pkg.go.dev/builtin#string), opts ...CollectionGroupOption) *Pipeline

CollectionGroup creates a new [Pipeline] that operates on all documents in a group of collections that include the given ID, regardless of parent document.

For example, consider: Countries/France/Cities/Paris = {population: 100} Countries/Canada/Cities/Montreal = {population: 90}

CollectionGroup can be used to query across all "Cities" regardless of its parent "Countries".

### func (*PipelineSource) CreateFromAggregationQuery 
    
    
    func (ps *PipelineSource) CreateFromAggregationQuery(query *AggregationQuery) *Pipeline

CreateFromAggregationQuery creates a new [Pipeline] from the given [AggregationQuery]. Under the hood, this will translate the query semantics (order by document ID, etc.) to an equivalent pipeline.

### func (*PipelineSource) CreateFromQuery 
    
    
    func (ps *PipelineSource) CreateFromQuery(query Queryer) *Pipeline

CreateFromQuery creates a new [Pipeline] from the given [Queryer]. Under the hood, this will translate the query semantics (order by document ID, etc.) to an equivalent pipeline.

### func (*PipelineSource) Database 
    
    
    func (ps *PipelineSource) Database(opts ...DatabaseOption) *Pipeline

Database creates a new [Pipeline] that operates on all documents in the Firestore database.

### func (*PipelineSource) Documents 
    
    
    func (ps *PipelineSource) Documents(refs []*DocumentRef, opts ...DocumentsOption) *Pipeline

Documents creates a new [Pipeline] that operates on a specific set of Firestore documents.

### func (*PipelineSource) Literals 
    
    
    func (ps *PipelineSource) Literals(documents []map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any), opts ...LiteralsOption) *Pipeline

Literals creates a new [Pipeline] that operates on a fixed set of predefined document objects.

## PlanSummary
    
    
    type PlanSummary struct {
    	// The indexes selected for the query. For example:
    	//
    	//	[
    	//	  {"query_scope": "Collection", "properties": "(foo ASC, __name__ ASC)"},
    	//	  {"query_scope": "Collection", "properties": "(bar ASC, __name__ ASC)"}
    	//	]
    	IndexesUsed []*map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any)
    }

PlanSummary represents planning phase information for the query.

## Precondition
    
    
    type Precondition interface {
    	// contains filtered or unexported methods
    }

A Precondition modifies a Firestore update or delete operation.

### Exists
    
    
    var Exists Precondition

Exists is a Precondition that checks for the existence of a resource before writing to it. If the check fails, the write does not occur.

### func LastUpdateTime 
    
    
    func LastUpdateTime(t [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) Precondition

LastUpdateTime returns a Precondition that checks that a resource must exist and must have last been updated at the given time. If the check fails, the write does not occur.

## PropertyFilter
    
    
    type PropertyFilter struct {
    	Path     [string](https://pkg.go.dev/builtin#string)
    	Operator [string](https://pkg.go.dev/builtin#string)
    	Value    interface{}
    }

PropertyFilter represents a filter on single property.

Path can be a single field or a dot-separated sequence of fields denoting property path, and must not contain any of the runes "˜*/[]". Operator must be one of "==", "!=", "<", "<=", ">", ">=", "array-contains", "array-contains-any", "in" or "not-in".

## PropertyPathFilter
    
    
    type PropertyPathFilter struct {
    	Path     FieldPath
    	Operator [string](https://pkg.go.dev/builtin#string)
    	Value    interface{}
    }

PropertyPathFilter represents a filter on single property.

Path can be an array of fields denoting property path. Operator must be one of "==", "!=", "<", "<=", ">", ">=", "array-contains", "array-contains-any", "in" or "not-in".

## Query
    
    
    type Query struct {
    	// contains filtered or unexported fields
    }

Query represents a Firestore query.

Query values are immutable. Each Query method creates a new Query; it does not modify the old.

### func (Query) Deserialize 
    
    
    func (q Query) Deserialize(bytes [][byte](https://pkg.go.dev/builtin#byte)) (Query, [error](https://pkg.go.dev/builtin#error))

Deserialize takes a slice of bytes holding the wire-format message of RunQueryRequest, the underlying proto message used by Queries. It then populates and returns a Query object that can be used to execute that Query.

### func (Query) Documents 
    
    
    func (q Query) Documents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *DocumentIterator

Documents returns an iterator over the query's resulting documents.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	q := client.Collection("States").Select("pop").
    		Where("pop", ">", 10).
    		[OrderBy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_OrderBy)("pop", firestore.[Desc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Asc_Desc)).
    		Limit(10)
    	iter1 := q.Documents(ctx)
    	_ = iter1 // TODO: Use iter1.
    
    	// You can call Documents directly on a CollectionRef as well.
    	iter2 := client.Collection("States").Documents(ctx)
    	_ = iter2 // TODO: Use iter2.
    }
    

##### path_methods
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	q := client.Collection("Unusual").[SelectPaths](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_SelectPaths)([]string{"*"}, []string{"[~]"}).
    		[WherePath](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_WherePath)([]string{"/"}, ">", 10).
    		[OrderByPath](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_OrderByPath)([]string{"/"}, firestore.[Desc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Asc_Desc)).
    		Limit(10)
    	iter1 := q.Documents(ctx)
    	_ = iter1 // TODO: Use iter1.
    
    	// You can call Documents directly on a CollectionRef as well.
    	iter2 := client.Collection("States").Documents(ctx)
    	_ = iter2 // TODO: Use iter2.
    }
    

### func (Query) EndAt 
    
    
    func (q Query) EndAt(docSnapshotOrFieldValues ...interface{}) Query

EndAt returns a new Query that specifies that results should end at the document with the given field values. See Query.StartAt for more information.

Calling EndAt overrides a previous call to EndAt or EndBefore.

### func (Query) EndBefore 
    
    
    func (q Query) EndBefore(docSnapshotOrFieldValues ...interface{}) Query

EndBefore returns a new Query that specifies that results should end just before the document with the given field values. See Query.StartAt for more information.

Calling EndBefore overrides a previous call to EndAt or EndBefore.

### func (Query) FindNearest 
    
    
    func (q Query) FindNearest(vectorField [string](https://pkg.go.dev/builtin#string), queryVector [any](https://pkg.go.dev/builtin#any), limit [int](https://pkg.go.dev/builtin#int), measure DistanceMeasure, options *FindNearestOptions) VectorQuery

FindNearest returns a query that can perform vector distance (similarity) search.

The returned query, when executed, performs a distance search on the specified vectorField against the given queryVector and returns the top documents that are closest to the queryVector according to measure. At most limit documents are returned.

Only documents whose vectorField field is a Vector32 or Vector64 of the same dimension as queryVector participate in the query; all other documents are ignored. In particular, fields of type []float32 or []float64 are ignored.

The vectorField argument can be a single field or a dot-separated sequence of fields, and must not contain any of the runes "˜*/[]".

The queryVector argument can be any of the following types:

  * []float32
  * []float64
  * Vector32
  * Vector64



#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	//
    	q := client.Collection("descriptions").
    		FindNearest("Embedding", []float32{1, 2, 3}, 5, firestore.[DistanceMeasureDotProduct](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_DistanceMeasureEuclidean_DistanceMeasureCosine_DistanceMeasureDotProduct), &firestore.[FindNearestOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_FindNearestOptions){
    			DistanceThreshold:   firestore.[Ptr](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Ptr)(20.0),
    			DistanceResultField: "vector_distance",
    		})
    	iter1 := q.Documents(ctx)
    	_ = iter1 // TODO: Use iter1.
    }
    

### func (Query) FindNearestPath 
    
    
    func (q Query) FindNearestPath(vectorFieldPath FieldPath, queryVector [any](https://pkg.go.dev/builtin#any), limit [int](https://pkg.go.dev/builtin#int), measure DistanceMeasure, options *FindNearestOptions) VectorQuery

FindNearestPath is like [Query.FindNearest] but it accepts a [FieldPath].

### func (Query) Limit 
    
    
    func (q Query) Limit(n [int](https://pkg.go.dev/builtin#int)) Query

Limit returns a new Query that specifies the maximum number of first results to return. It must not be negative.

### func (Query) LimitToLast 
    
    
    func (q Query) LimitToLast(n [int](https://pkg.go.dev/builtin#int)) Query

LimitToLast returns a new Query that specifies the maximum number of last results to return. It must not be negative.

### func (*Query) NewAggregationQuery 
    
    
    func (q *Query) NewAggregationQuery() *AggregationQuery

NewAggregationQuery returns an AggregationQuery with this query as its base query.

### func (Query) Offset 
    
    
    func (q Query) Offset(n [int](https://pkg.go.dev/builtin#int)) Query

Offset returns a new Query that specifies the number of initial results to skip. It must not be negative.

### func (Query) OrderBy 
    
    
    func (q Query) OrderBy(path [string](https://pkg.go.dev/builtin#string), dir Direction) Query

OrderBy returns a new Query that specifies the order in which results are returned. A Query can have multiple OrderBy/OrderByPath specifications. OrderBy appends the specification to the list of existing ones.

The path argument can be a single field or a dot-separated sequence of fields, and must not contain any of the runes "˜*/[]".

To order by document name, use the special field path DocumentID.

### func (Query) OrderByPath 
    
    
    func (q Query) OrderByPath(fp FieldPath, dir Direction) Query

OrderByPath returns a new Query that specifies the order in which results are returned. A Query can have multiple OrderBy/OrderByPath specifications. OrderByPath appends the specification to the list of existing ones.

### func (Query) Pipeline 
    
    
    func (q Query) Pipeline() *Pipeline

Pipeline creates a new [Pipeline] from the query. All of the operations of the query will be converted to pipeline stages. For example, `query.Where("f", "==", 1).Limit(10).OrderBy("f", Asc).Pipeline()` is equivalent to `client.Pipeline().Collection("C").Where(Equal("f", 1)).Limit(10).Sort(Ascending("f"))`.

### func (Query) Select 
    
    
    func (q Query) Select(paths [string](https://pkg.go.dev/builtin#string)) Query

Select returns a new Query that specifies the paths to return from the result documents. Each path argument can be a single field or a dot-separated sequence of fields, and must not contain any of the runes "˜*/[]".

An empty Select call will produce a query that returns only document IDs.

### func (Query) SelectPaths 
    
    
    func (q Query) SelectPaths(fieldPaths ...FieldPath) Query

SelectPaths returns a new Query that specifies the field paths to return from the result documents.

An empty SelectPaths call will produce a query that returns only document IDs.

### func (Query) Serialize 
    
    
    func (q Query) Serialize() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

Serialize creates a RunQueryRequest wire-format byte slice from a Query object. This can be used in combination with Deserialize to marshal Query objects. This could be useful, for instance, if executing a query formed in one process in another.

### func (Query) Snapshots 
    
    
    func (q Query) Snapshots(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *QuerySnapshotIterator

Snapshots returns an iterator over snapshots of the query. Each time the query results change, a new snapshot will be generated.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	q := client.Collection("States").
    		Where("pop", ">", 10).
    		[OrderBy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_OrderBy)("pop", firestore.[Desc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Asc_Desc)).
    		Limit(10)
    	qsnapIter := q.Snapshots(ctx)
    	// Listen forever for changes to the query's results.
    	for {
    		qsnap, err := qsnapIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		fmt.Printf("At %s there were %d results.\n", qsnap.[ReadTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_ReadOption_ReadTime), qsnap.Size)
    		_ = qsnap.Documents // TODO: Iterate over the results if desired.
    		_ = qsnap.Changes   // TODO: Use the list of incremental changes if desired.
    	}
    }
    

### func (Query) StartAfter 
    
    
    func (q Query) StartAfter(docSnapshotOrFieldValues ...interface{}) Query

StartAfter returns a new Query that specifies that results should start just after the document with the given field values. See Query.StartAt for more information.

Calling StartAfter overrides a previous call to StartAt or StartAfter.

### func (Query) StartAt 
    
    
    func (q Query) StartAt(docSnapshotOrFieldValues ...interface{}) Query

StartAt returns a new Query that specifies that results should start at the document with the given field values.

StartAt may be called with a single DocumentSnapshot, representing an existing document within the query. The document must be a direct child of the location being queried (not a parent document, or document in a different collection, or a grandchild document, for example).

Otherwise, StartAt should be called with one field value for each OrderBy clause, in the order that they appear. For example, in
    
    
    q.OrderBy("X", Asc).OrderBy("Y", Desc).StartAt(1, 2)
    

results will begin at the first document where X = 1 and Y = 2.

If an OrderBy call uses the special DocumentID field path, the corresponding value should be the document ID relative to the query's collection. For example, to start at the document "NewYork" in the "States" collection, write
    
    
    client.Collection("States").OrderBy(DocumentID, firestore.Asc).StartAt("NewYork")
    

Calling StartAt overrides a previous call to StartAt or StartAfter.

### func (Query) Where 
    
    
    func (q Query) Where(path, op [string](https://pkg.go.dev/builtin#string), value interface{}) Query

Where returns a new Query that filters the set of results. A Query can have multiple filters. The path argument can be a single field or a dot-separated sequence of fields, and must not contain any of the runes "˜*/[]". The op argument must be one of "==", "!=", "<", "<=", ">", ">=", "array-contains", "array-contains-any", "in" or "not-in". WARNING: Using WhereEntity with Simple and Composite filters is recommended.

### func (Query) WhereEntity 
    
    
    func (q Query) WhereEntity(ef EntityFilter) Query

WhereEntity returns a query with provided filter.

EntityFilter can be a simple filter or a composite filter PropertyFilter and PropertyPathFilter are supported simple filters AndFilter and OrFilter are supported composite filters Entity filters in multiple calls are joined together by AND

### func (Query) WherePath 
    
    
    func (q Query) WherePath(fp FieldPath, op [string](https://pkg.go.dev/builtin#string), value interface{}) Query

WherePath returns a new Query that filters the set of results. A Query can have multiple filters. The op argument must be one of "==", "!=", "<", "<=", ">", ">=", "array-contains", "array-contains-any", "in" or "not-in". WARNING: Using WhereEntity with Simple and Composite filters is recommended.

### func (*Query) WithReadOptions 
    
    
    func (q *Query) WithReadOptions(opts ...ReadOption) *Query

WithReadOptions specifies constraints for accessing documents from the database, e.g. at what time snapshot to read the documents.

### func (Query) WithRunOptions 
    
    
    func (q Query) WithRunOptions(opts ...RunOption) Query

WithRunOptions allows passing options to the query Calling WithRunOptions overrides a previous call to WithRunOptions.

## QuerySnapshot
    
    
    type QuerySnapshot struct {
    	// An iterator over the query results.
    	// It is not necessary to call Stop on this iterator.
    	Documents *DocumentIterator
    
    	// The number of results in this snapshot.
    	Size [int](https://pkg.go.dev/builtin#int)
    
    	// The changes since the previous snapshot.
    	Changes []DocumentChange
    
    	// The time at which this snapshot was obtained from Firestore.
    	ReadTime time.Time
    }

A QuerySnapshot is a snapshot of query results. It is returned by QuerySnapshotIterator.Next whenever the results of a query change.

## QuerySnapshotIterator
    
    
    type QuerySnapshotIterator struct {
    	// The Query used to construct this iterator.
    	Query Query
    	// contains filtered or unexported fields
    }

QuerySnapshotIterator is an iterator over snapshots of a query. Call Next on the iterator to get a snapshot of the query's results each time they change. Call Stop on the iterator when done.

For an example, see Query.Snapshots.

### func (*QuerySnapshotIterator) Next 
    
    
    func (it *QuerySnapshotIterator) Next() (*QuerySnapshot, [error](https://pkg.go.dev/builtin#error))

Next blocks until the query's results change, then returns a QuerySnapshot for the current results.

Next is not expected to return iterator.Done unless it is called after Stop. Rarely, networking issues may also cause iterator.Done to be returned.

In addition, if Next returns an error other than iterator.Done, all subsequent calls will return the same error. To continue iteration, a new QuerySnapshotIterator must be created.

### func (*QuerySnapshotIterator) Stop 
    
    
    func (it *QuerySnapshotIterator) Stop()

Stop stops receiving snapshots. You should always call Stop when you are done with a QuerySnapshotIterator, to free up resources. It is not safe to call Stop concurrently with Next.

## Queryer
    
    
    type Queryer interface {
    	// contains filtered or unexported methods
    }

A Queryer is a Query or a CollectionRef. CollectionRefs act as queries whose results are all the documents in the collection.

## RawOptions
    
    
    type RawOptions map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any)

RawOptions specifies raw options to be passed to the Firestore backend. These options are not validated by the SDK and are passed directly to the backend. Options specified here will take precedence over any options with the same name set by the SDK.

## ReadOption
    
    
    type ReadOption interface {
    	// contains filtered or unexported methods
    }

ReadOption interface allows for abstraction of computing read time settings.

### func ReadTime 
    
    
    func ReadTime(t [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) ReadOption

ReadTime specifies a time-specific snapshot of the database to read.

## RemoveFieldsOption
    
    
    type RemoveFieldsOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

RemoveFieldsOption is an option for an RemoveFields pipeline stage.

## ReplaceWithOption
    
    
    type ReplaceWithOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

ReplaceWithOption is an option for a ReplaceWith pipeline stage.

## RunOption
    
    
    type RunOption interface {
    	// contains filtered or unexported methods
    }

RunOption are options used while running a query

## SampleMode
    
    
    type SampleMode [string](https://pkg.go.dev/builtin#string)

SampleMode defines the mode for the sample stage.

### SampleModeDocuments, SampleModePercent
    
    
    const (
    	// SampleModeDocuments samples a fixed number of documents.
    	SampleModeDocuments SampleMode = "documents"
    	// SampleModePercent samples a percentage of documents.
    	SampleModePercent SampleMode = "percent"
    )

## SampleOption
    
    
    type SampleOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

SampleOption is an option for a Sample pipeline stage.

## Sampler
    
    
    type Sampler struct {
    	Size [any](https://pkg.go.dev/builtin#any)
    	Mode SampleMode
    }

Sampler is used to define a sample operation.

### func WithDocLimit 
    
    
    func WithDocLimit(limit [int](https://pkg.go.dev/builtin#int)) *Sampler

WithDocLimit creates a Sampler for sampling a fixed number of documents.

### func WithPercentage 
    
    
    func WithPercentage(percentage [float64](https://pkg.go.dev/builtin#float64)) *Sampler

WithPercentage creates a Sampler for sampling a percentage of documents.

## SearchOption
    
    
    type SearchOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

SearchOption is an option for a Search pipeline stage.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithSearchAddFields 
    
    
    func WithSearchAddFields(fields ...Selectable) SearchOption

WithSearchAddFields specifies the fields to add to each document.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithSearchLanguageCode 
    
    
    func WithSearchLanguageCode(languageCode [string](https://pkg.go.dev/builtin#string)) SearchOption

WithSearchLanguageCode specifies the BCP-47 language code of text in the search query, such as "en" or "sr".

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithSearchLimit 
    
    
    func WithSearchLimit(limit [int64](https://pkg.go.dev/builtin#int64)) SearchOption

WithSearchLimit specifies the maximum number of documents to return from the search stage. The limit is applied after documents are scored and sorted.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithSearchOffset 
    
    
    func WithSearchOffset(offset [int64](https://pkg.go.dev/builtin#int64)) SearchOption

WithSearchOffset specifies the number of documents to skip from the beginning of the search result set.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithSearchQuery 
    
    
    func WithSearchQuery(query [any](https://pkg.go.dev/builtin#any)) SearchOption

WithSearchQuery specifies the search query that will be used to query and score documents by the search stage. It can be a string (automatically wrapped in DocumentMatches) or a BooleanExpression.

Example:
    
    
    client.Pipeline().Collection("restaurants").Search(
        WithSearchQuery("waffles"),
    )
    

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithSearchRetrievalDepth 
    
    
    func WithSearchRetrievalDepth(depth [int64](https://pkg.go.dev/builtin#int64)) SearchOption

WithSearchRetrievalDepth specifies the maximum number of documents to retrieve. Documents will be retrieved in the pre-sort order specified by the search index.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithSearchSort 
    
    
    func WithSearchSort(orders ...Ordering) SearchOption

WithSearchSort specifies how the returned documents are sorted. One or more ordering are required.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

## SelectOption
    
    
    type SelectOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

SelectOption is an option for a Select pipeline stage.

## Selectable
    
    
    type Selectable interface {
    	// contains filtered or unexported methods
    }

Selectable is an interface for expressions that can be selected in a pipeline.

### func Selectables 
    
    
    func Selectables(s ...Selectable) []Selectable

Selectables is a helper function that returns its arguments as a slice of Selectable. It is used to provide variadic-like ergonomics for pipeline stages that accept a slice of Selectable expressions.

## SetOption
    
    
    type SetOption interface {
    	// contains filtered or unexported methods
    }

A SetOption modifies a Firestore set operation.

### MergeAll
    
    
    var MergeAll SetOption = merge{/* contains filtered or unexported fields */}

MergeAll is a SetOption that causes all the field paths given in the data argument to Set to be overwritten. It is not supported for struct data.

### func Merge 
    
    
    func Merge(fps ...FieldPath) SetOption

Merge returns a SetOption that causes only the given field paths to be overwritten. Other fields on the existing document will be untouched. It is an error if a provided field path does not refer to a value in the data passed to Set.

## SimpleFilter
    
    
    type SimpleFilter interface {
    	EntityFilter
    	// contains filtered or unexported methods
    }

SimpleFilter represents a simple Firestore filter.

## SortOption
    
    
    type SortOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

SortOption is an option for a Sort pipeline stage.

## StageOption
    
    
    type StageOption interface {
    	// contains filtered or unexported methods
    }

StageOption is an option for configuring a pipeline stage.

## Transaction
    
    
    type Transaction struct {
    	// contains filtered or unexported fields
    }

Transaction represents a Firestore transaction.

### func (*Transaction) Create 
    
    
    func (t *Transaction) Create(dr *DocumentRef, data interface{}) [error](https://pkg.go.dev/builtin#error)

Create adds a Create operation to the Transaction. See DocumentRef.Create for details.

### func (*Transaction) Delete 
    
    
    func (t *Transaction) Delete(dr *DocumentRef, opts ...Precondition) [error](https://pkg.go.dev/builtin#error)

Delete adds a Delete operation to the Transaction. See DocumentRef.Delete for details.

### func (*Transaction) DocumentRefs 
    
    
    func (t *Transaction) DocumentRefs(cr *CollectionRef) *DocumentRefIterator

DocumentRefs returns references to all the documents in the collection, including missing documents. A missing document is a document that does not exist but has sub-documents.

### func (*Transaction) Documents 
    
    
    func (t *Transaction) Documents(q Queryer) *DocumentIterator

Documents returns a DocumentIterator based on given Query or CollectionRef. The results will be in the context of the transaction.

### func (*Transaction) Execute 
    
    
    func (t *Transaction) Execute(p *Pipeline, opts ...ExecuteOption) *PipelineSnapshot

Execute runs the given pipeline in the context of the transaction.

### func (*Transaction) Get 
    
    
    func (t *Transaction) Get(dr *DocumentRef) (*DocumentSnapshot, [error](https://pkg.go.dev/builtin#error))

Get gets the document in the context of the transaction. The transaction holds a pessimistic lock on the returned document. If the document does not exist, Get returns a NotFound error, which can be checked with
    
    
    status.Code(err) == codes.NotFound
    

### func (*Transaction) GetAll 
    
    
    func (t *Transaction) GetAll(drs []*DocumentRef) ([]*DocumentSnapshot, [error](https://pkg.go.dev/builtin#error))

GetAll retrieves multiple documents with a single call. The DocumentSnapshots are returned in the order of the given DocumentRefs. If a document is not present, the corresponding DocumentSnapshot's Exists method will return false. The transaction holds a pessimistic lock on all of the returned documents.

### func (*Transaction) Set 
    
    
    func (t *Transaction) Set(dr *DocumentRef, data interface{}, opts ...SetOption) [error](https://pkg.go.dev/builtin#error)

Set adds a Set operation to the Transaction. See DocumentRef.Set for details.

### func (*Transaction) Update 
    
    
    func (t *Transaction) Update(dr *DocumentRef, data []Update, opts ...Precondition) [error](https://pkg.go.dev/builtin#error)

Update adds a new Update operation to the Transaction. See DocumentRef.Update for details.

### func (*Transaction) WithReadOptions 
    
    
    func (t *Transaction) WithReadOptions(opts ...ReadOption) *Transaction

WithReadOptions specifies constraints for accessing documents from the database, e.g. at what time snapshot to read the documents. Note: ReadTime cannot be set via WithReadOptions on a Transaction. If ReadTime is passed, subsequent calls to the transaction will return an error. Use TransactionReadTime option when starting the transaction instead.

## TransactionOption
    
    
    type TransactionOption interface {
    	// contains filtered or unexported methods
    }

A TransactionOption is an option passed to Client.Transaction.

### func TransactionReadTime 
    
    
    func TransactionReadTime(t [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) TransactionOption

TransactionReadTime is a TransactionOption that configures the transaction to read data at a specific time in the past. Specifying this option forces the transaction to be read-only.

## UnionOption
    
    
    type UnionOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

UnionOption is an option for a Union pipeline stage.

## UnnestOption
    
    
    type UnnestOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

UnnestOption is an option for executing a pipeline unnest stage.

### func WithUnnestIndexField 
    
    
    func WithUnnestIndexField(indexField [any](https://pkg.go.dev/builtin#any)) UnnestOption

WithUnnestIndexField specifies the name of the field to store the array index of the unnested element.

## Update
    
    
    type Update struct {
    	Path      [string](https://pkg.go.dev/builtin#string) // Will be split on dots, and must not contain any of "˜*/[]".
    	FieldPath FieldPath
    	Value     interface{}
    }

An Update describes an update to a value referred to by a path. An Update should have either a non-empty Path or a non-empty FieldPath, but not both.

See DocumentRef.Create for acceptable values. To delete a field, specify firestore.Delete as the value.

### func (Update) String 
    
    
    func (u Update) String() [string](https://pkg.go.dev/builtin#string)

String returns string representation of firestore.Update

## UpdateOption
    
    
    type UpdateOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

UpdateOption is an option for an Update pipeline stage.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

### func WithUpdateTransformations 
    
    
    func WithUpdateTransformations(field Selectable, additionalFields ...Selectable) UpdateOption

WithUpdateTransformations specifies the list of field transformations to apply in an update operation.

Experimental: Update, Delete and Search stages in pipeline queries are in public preview and are subject to potential breaking changes in future versions, regardless of any other documented package stability guarantees.

## Vector32
    
    
    type Vector32 [][float32](https://pkg.go.dev/builtin#float32)

Vector32 is an embedding vector of float32s.

## Vector64
    
    
    type Vector64 [][float64](https://pkg.go.dev/builtin#float64)

Vector64 is an embedding vector of float64s.

## VectorQuery
    
    
    type VectorQuery struct {
    	// contains filtered or unexported fields
    }

VectorQuery represents a query that uses [Query.FindNearest] or [Query.FindNearestPath].

### func (VectorQuery) Deserialize 
    
    
    func (vq VectorQuery) Deserialize(bytes [][byte](https://pkg.go.dev/builtin#byte)) (VectorQuery, [error](https://pkg.go.dev/builtin#error))

Deserialize takes a slice of bytes holding the wire-format message of RunQueryRequest, the underlying proto message used by Queries. It then populates and returns a VectorQuery object that can be used to execute that VectorQuery.

### func (VectorQuery) Documents 
    
    
    func (vq VectorQuery) Documents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *DocumentIterator

Documents returns an iterator over the vector query's resulting documents.

### func (VectorQuery) Serialize 
    
    
    func (vq VectorQuery) Serialize() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

Serialize creates a RunQueryRequest wire-format byte slice from a VectorQuery object. This can be used in combination with Deserialize to marshal VectorQuery objects. This could be useful, for instance, if executing a query formed in one process in another.

## WhereOption
    
    
    type WhereOption interface {
    	StageOption
    	// contains filtered or unexported methods
    }

WhereOption is an option for a Where pipeline stage.

## WriteBatch (deprecated)
    
    
    type WriteBatch struct {
    	// contains filtered or unexported fields
    }

A WriteBatch holds multiple database updates. Build a batch with the Create, Set, Update and Delete methods, then run it with the Commit method. Errors in Create, Set, Update or Delete are recorded instead of being returned immediately. The first such error is returned by Commit.

Deprecated: The WriteBatch API has been replaced with the transaction and the bulk writer API. For atomic transaction operations, use `Transaction`. For bulk read and write operations, use `BulkWriter`.

### func (*WriteBatch) Commit (deprecated)
    
    
    func (b *WriteBatch) Commit(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (_ []*WriteResult, err [error](https://pkg.go.dev/builtin#error))

Commit applies all the writes in the batch to the database atomically. Commit returns an error if there are no writes in the batch, if any errors occurred in constructing the writes, or if the Commmit operation fails.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, "project-id")
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    
    	type State struct {
    		Capital    string  `firestore:"capital"`
    		Population float64 `firestore:"pop"` // in millions
    	}
    
    	ny := client.Doc("States/NewYork")
    	ca := client.Doc("States/California")
    
    	writeResults, err := client.[Batch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Client_Batch)().
    		Create(ny, State{Capital: "Albany", Population: 19.8}).
    		Set(ca, State{Capital: "Sacramento", Population: 39.14}).
    		Delete(client.Doc("States/WestDakota")).
    		Commit(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	fmt.Println(writeResults)
    }
    

### func (*WriteBatch) Create (deprecated)
    
    
    func (b *WriteBatch) Create(dr *DocumentRef, data interface{}) *WriteBatch

Create adds a Create operation to the batch. See DocumentRef.Create for details.

### func (*WriteBatch) Delete (deprecated)
    
    
    func (b *WriteBatch) Delete(dr *DocumentRef, opts ...Precondition) *WriteBatch

Delete adds a Delete operation to the batch. See DocumentRef.Delete for details.

### func (*WriteBatch) Set (deprecated)
    
    
    func (b *WriteBatch) Set(dr *DocumentRef, data interface{}, opts ...SetOption) *WriteBatch

Set adds a Set operation to the batch. See DocumentRef.Set for details.

### func (*WriteBatch) Update (deprecated)
    
    
    func (b *WriteBatch) Update(dr *DocumentRef, data []Update, opts ...Precondition) *WriteBatch

Update adds an Update operation to the batch. See DocumentRef.Update for details.

## WriteResult
    
    
    type WriteResult struct {
    	// The time at which the document was updated, or created if it did not
    	// previously exist. Writes that do not actually change the document do
    	// not change the update time.
    	UpdateTime time.Time
    }

A WriteResult is returned by methods that write documents.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
