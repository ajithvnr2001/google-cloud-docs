---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/datastore/
title: Package google.golang.org/appengine/v2/datastore (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:48.659936+00:00
---

# Package google.golang.org/appengine/v2/datastore (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/datastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/datastore (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/datastore). 

Package datastore provides a client for App Engine's datastore service. 

## Basic Operations

Entities are the unit of storage and are associated with a key. A key consists of an optional parent key, a string application ID, a string kind (also known as an entity type), and either a StringID or an IntID. A StringID is also known as an entity name or key name. 

It is valid to create a key with a zero StringID and a zero IntID; this is called an incomplete key, and does not refer to any saved entity. Putting an entity into the datastore under an incomplete key will cause a unique key to be generated for that entity, with a non-zero IntID. 

An entity's contents are a mapping from case-sensitive field names to values. Valid value types are: 

  * signed integers (int, int8, int16, int32 and int64), 
  * bool, 
  * string, 
  * float32 and float64, 
  * []byte (up to 1 megabyte in length), 
  * any type whose underlying type is one of the above predeclared types, 
  * ByteString, 
  * *Key, 
  * time.Time (stored with microsecond precision), 
  * appengine.BlobKey, 
  * appengine.GeoPoint, 
  * structs whose fields are all valid value types, 
  * slices of any of the above. 



Slices of structs are valid, as are structs that contain slices. However, if one struct contains another, then at most one of those can be repeated. This disqualifies recursively defined struct types: any struct T that (directly or indirectly) contains a []T. 

The Get and Put functions load and save an entity's contents. An entity's contents are typically represented by a struct pointer. 

Example code:
    
    
    type Entity struct {
        Value string
    }
    
    func handle(w http.ResponseWriter, r *http.Request) {
        ctx := appengine.NewContext(r)
    
        k := datastore.NewKey(ctx, "Entity", "stringID", 0, nil)
        e := new(Entity)
        if err := datastore.Get(ctx, k, e); err != nil {
            http.Error(w, err.Error(), 500)
            return
        }
    
        old := e.Value
        e.Value = r.URL.Path
    
        if _, err := datastore.Put(ctx, k, e); err != nil {
            http.Error(w, err.Error(), 500)
            return
        }
    
        w.Header().Set("Content-Type", "text/plain; charset=utf-8")
        fmt.Fprintf(w, "old=%q\nnew=%q\n", old, e.Value)
    }

GetMulti, PutMulti and DeleteMulti are batch versions of the Get, Put and Delete functions. They take a []*Key instead of a *Key, and may return an appengine.MultiError when encountering partial failure. 

## Properties

An entity's contents can be represented by a variety of types. These are typically struct pointers, but can also be any type that implements the PropertyLoadSaver interface. If using a struct pointer, you do not have to explicitly implement the PropertyLoadSaver interface; the datastore will automatically convert via reflection. If a struct pointer does implement that interface then those methods will be used in preference to the default behavior for struct pointers. Struct pointers are more strongly typed and are easier to use; PropertyLoadSavers are more flexible. 

The actual types passed do not have to match between Get and Put calls or even across different calls to datastore. It is valid to put a *PropertyList and get that same entity as a *myStruct, or put a *myStruct0 and get a *myStruct1. Conceptually, any entity is saved as a sequence of properties, and is loaded into the destination value on a property-by-property basis. When loading into a struct pointer, an entity that cannot be completely represented (such as a missing field) will result in an ErrFieldMismatch error but it is up to the caller whether this error is fatal, recoverable or ignorable. 

By default, for struct pointers, all properties are potentially indexed, and the property name is the same as the field name (and hence must start with an upper case letter). 

Fields may have a `datastore:&quot;name,options&quot;` tag. The tag name is the property name, which must be one or more valid Go identifiers joined by ".", but may start with a lower case letter. An empty tag name means to just use the field name. A "-" tag name means that the datastore will ignore that field. 

The only valid options are "omitempty" and "noindex". 

If the options include "omitempty" and the value of the field is empty, then the field will be omitted on Save. The empty values are false, 0, any nil interface value, and any array, slice, map, or string of length zero. Struct field values will never be empty. 

If options include "noindex" then the field will not be indexed. All fields are indexed by default. Strings or byte slices longer than 1500 bytes cannot be indexed; fields used to store long strings and byte slices must be tagged with "noindex" or they will cause Put operations to fail. 

To use multiple options together, separate them by a comma. The order does not matter. 

If the options is "" then the comma may be omitted. 

Example code:
    
    
    // A and B are renamed to a and b.
    // A, C and J are not indexed.
    // D's tag is equivalent to having no tag at all (E).
    // I is ignored entirely by the datastore.
    // J has tag information for both the datastore and json packages.
    type TaggedStruct struct {
        A int `datastore:"a,noindex"`
        B int `datastore:"b"`
        C int `datastore:",noindex"`
        D int `datastore:""`
        E int
        I int `datastore:"-"`
        J int `datastore:",noindex" json:"j"`
    }

## Structured Properties

If the struct pointed to contains other structs, then the nested or embedded structs are flattened. For example, given these definitions:
    
    
    type Inner1 struct {
        W int32
        X string
    }
    
    type Inner2 struct {
        Y float64
    }
    
    type Inner3 struct {
        Z bool
    }
    
    type Outer struct {
        A int16
        I []Inner1
        J Inner2
        Inner3
    }

then an Outer's properties would be equivalent to those of:
    
    
    type OuterEquivalent struct {
        A     int16
        IDotW []int32  `datastore:"I.W"`
        IDotX []string `datastore:"I.X"`
        JDotY float64  `datastore:"J.Y"`
        Z     bool
    }

If Outer's embedded Inner3 field was tagged as `datastore:&quot;Foo&quot;` then the equivalent field would instead be: FooDotZ bool `datastore:&quot;Foo.Z&quot;`. 

If an outer struct is tagged "noindex" then all of its implicit flattened fields are effectively "noindex". 

## The PropertyLoadSaver Interface

An entity's contents can also be represented by any type that implements the PropertyLoadSaver interface. This type may be a struct pointer, but it does not have to be. The datastore package will call Load when getting the entity's contents, and Save when putting the entity's contents. Possible uses include deriving non-stored fields, verifying fields, or indexing a field only if its value is positive. 

Example code:
    
    
    type CustomPropsExample struct {
        I, J int
        // Sum is not stored, but should always be equal to I + J.
        Sum int `datastore:"-"`
    }
    
    func (x *CustomPropsExample) Load(ps []datastore.Property) error {
        // Load I and J as usual.
        if err := datastore.LoadStruct(x, ps); err != nil {
            return err
        }
        // Derive the Sum field.
        x.Sum = x.I + x.J
        return nil
    }
    
    func (x *CustomPropsExample) Save() ([]datastore.Property, error) {
        // Validate the Sum field.
        if x.Sum != x.I + x.J {
            return nil, errors.New("CustomPropsExample has inconsistent sum")
        }
        // Save I and J as usual. The code below is equivalent to calling
        // "return datastore.SaveStruct(x)", but is done manually for
        // demonstration purposes.
        return []datastore.Property{
            {
                Name:  "I",
                Value: int64(x.I),
            },
            {
                Name:  "J",
                Value: int64(x.J),
            },
        }, nil
    }

The *PropertyList type implements PropertyLoadSaver, and can therefore hold an arbitrary entity's contents. 

## Queries

Queries retrieve entities based on their properties or key's ancestry. Running a query yields an iterator of results: either keys or (key, entity) pairs. Queries are re-usable and it is safe to call Query.Run from concurrent goroutines. Iterators are not safe for concurrent use. 

Queries are immutable, and are either created by calling NewQuery, or derived from an existing query by calling a method like Filter or Order that returns a new query value. A query is typically constructed by calling NewQuery followed by a chain of zero or more such methods. These methods are: 

  * Ancestor and Filter constrain the entities returned by running a query. 
  * Order affects the order in which they are returned. 
  * Project constrains the fields returned. 
  * Distinct de-duplicates projected entities. 
  * KeysOnly makes the iterator return only keys, not (key, entity) pairs. 
  * Start, End, Offset and Limit define which sub-sequence of matching entities to return. Start and End take cursors, Offset and Limit take integers. Start and Offset affect the first result, End and Limit affect the last result. If both Start and Offset are set, then the offset is relative to Start. If both End and Limit are set, then the earliest constraint wins. Limit is relative to Start+Offset, not relative to End. As a special case, a negative limit means unlimited. 



Example code:
    
    
    type Widget struct {
        Description string
        Price       int
    }
    
    func handle(w http.ResponseWriter, r *http.Request) {
        ctx := appengine.NewContext(r)
        q := datastore.NewQuery("Widget").
            Filter("Price <", 1000).
            Order("-Price")
        b := new(bytes.Buffer)
        for t := q.Run(ctx); ; {
            var x Widget
            key, err := t.Next(&x)
            if err == datastore.Done {
                break
            }
            if err != nil {
                serveError(ctx, w, err)
                return
            }
            fmt.Fprintf(b, "Key=%v\nWidget=%#v\n\n", key, x)
        }
        w.Header().Set("Content-Type", "text/plain; charset=utf-8")
        io.Copy(w, b)
    }

## Transactions

RunInTransaction runs a function in a transaction. 

Example code:
    
    
    type Counter struct {
        Count int
    }
    
    func inc(ctx context.Context, key *datastore.Key) (int, error) {
        var x Counter
        if err := datastore.Get(ctx, key, &x); err != nil && err != datastore.ErrNoSuchEntity {
            return 0, err
        }
        x.Count++
        if _, err := datastore.Put(ctx, key, &x); err != nil {
            return 0, err
        }
        return x.Count, nil
    }
    
    func handle(w http.ResponseWriter, r *http.Request) {
        ctx := appengine.NewContext(r)
        var count int
        err := datastore.RunInTransaction(ctx, func(ctx context.Context) error {
            var err1 error
            count, err1 = inc(ctx, datastore.NewKey(ctx, "Counter", "singleton", 0, nil))
            return err1
        }, nil)
        if err != nil {
            serveError(ctx, w, err)
            return
        }
        w.Header().Set("Content-Type", "text/plain; charset=utf-8")
        fmt.Fprintf(w, "Count=%d", count)
    }

## Metadata

The datastore package provides access to some of App Engine's datastore metadata. This metadata includes information about the entity groups, namespaces, entity kinds, and properties in the datastore, as well as the property representations for each property. 

Example code:
    
    
    func handle(w http.ResponseWriter, r *http.Request) {
        // Print all the kinds in the datastore, with all the indexed
        // properties (and their representations) for each.
        ctx := appengine.NewContext(r)
    
        kinds, err := datastore.Kinds(ctx)
        if err != nil {
            serveError(ctx, w, err)
            return
        }
    
        w.Header().Set("Content-Type", "text/plain; charset=utf-8")
        for _, kind := range kinds {
            fmt.Fprintf(w, "%s:\n", kind)
            props, err := datastore.KindProperties(ctx, kind)
            if err != nil {
                fmt.Fprintln(w, "\t(unable to retrieve properties)")
                continue
            }
            for p, rep := range props {
                fmt.Fprintf(w, "\t-%s (%s)\n", p, strings.Join(rep, ", "))
            }
        }
    }

## Variables 

### ErrInvalidEntityType, ErrInvalidKey, ErrNoSuchEntity
    
    
    var (
    	// ErrInvalidEntityType is returned when functions like Get or Next are
    	// passed a dst or src argument of invalid type.
    	ErrInvalidEntityType = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("datastore: invalid entity type")
    	// ErrInvalidKey is returned when an invalid key is presented.
    	ErrInvalidKey = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("datastore: invalid key")
    	// ErrNoSuchEntity is returned when no entity was found for a given key.
    	ErrNoSuchEntity = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("datastore: no such entity")
    )

### Done
    
    
    var Done = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("datastore: query has no more results")

Done is returned when a query iteration has completed.

### ErrConcurrentTransaction
    
    
    var ErrConcurrentTransaction = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("datastore: concurrent transaction")

ErrConcurrentTransaction is returned when a transaction is rolled back due to a conflict with a concurrent transaction.

## Functions 

### func AllocateIDRange 
    
    
    func AllocateIDRange(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), kind [string](https://pkg.go.dev/builtin#string), parent *Key, start, end [int64](https://pkg.go.dev/builtin#int64)) (err [error](https://pkg.go.dev/builtin#error))

AllocateIDRange allocates a range of IDs with specific endpoints. The range is inclusive at both the low and high end. Once these IDs have been allocated, you can manually assign them to newly created entities.

The Datastore's automatic ID allocator never assigns a key that has already been allocated (either through automatic ID allocation or through an explicit AllocateIDs call). As a result, entities written to the given key range will never be overwritten. However, writing entities with manually assigned keys in this range may overwrite existing entities (or new entities written by a separate request), depending on the error returned.

Use this only if you have an existing numeric ID range that you want to reserve (for example, bulk loading entities that already have IDs). If you don't care about which IDs you receive, use AllocateIDs instead.

AllocateIDRange returns nil if the range is successfully allocated. If one or more entities with an ID in the given range already exist, it returns a KeyRangeCollisionError. If the Datastore has already cached IDs in this range (e.g. from a previous call to AllocateIDRange), it returns a KeyRangeContentionError. Errors of other types indicate problems with arguments or an error returned directly from the Datastore.

### func AllocateIDs 
    
    
    func AllocateIDs(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), kind [string](https://pkg.go.dev/builtin#string), parent *Key, n [int](https://pkg.go.dev/builtin#int)) (low, high [int64](https://pkg.go.dev/builtin#int64), err [error](https://pkg.go.dev/builtin#error))

AllocateIDs returns a range of n integer IDs with the given kind and parent combination. kind cannot be empty; parent may be nil. The IDs in the range returned will not be used by the datastore's automatic ID sequence generator and may be used with NewKey without conflict.

The range is inclusive at the low end and exclusive at the high end. In other words, valid intIDs x satisfy low <= x && x < high.

If no error is returned, low + n == high.

### func Delete 
    
    
    func Delete(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key *Key) [error](https://pkg.go.dev/builtin#error)

Delete deletes the entity for the given key.

### func DeleteMulti 
    
    
    func DeleteMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key []*Key) [error](https://pkg.go.dev/builtin#error)

DeleteMulti is a batch version of Delete.

### func EnableKeyConversion 
    
    
    func EnableKeyConversion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context))

EnableKeyConversion enables encoded key compatibility with the Cloud Datastore client library (cloud.google.com/go/datastore). Encoded keys generated by the Cloud Datastore client library will be decoded into App Engine datastore keys.

The context provided must be an App Engine context if running in App Engine first generation runtime. This can be called in the /_ah/start handler. It is safe to call multiple times, and is cheap to call, so can also be inserted as middleware.

Enabling key compatibility does not affect the encoding format used by Key.Encode, it only expands the type of keys that are able to be decoded with DecodeKey.

### func Get 
    
    
    func Get(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key *Key, dst interface{}) [error](https://pkg.go.dev/builtin#error)

Get loads the entity stored for k into dst, which must be a struct pointer or implement PropertyLoadSaver. If there is no such entity for the key, Get returns ErrNoSuchEntity.

The values of dst's unmatched struct fields are not modified, and matching slice-typed fields are not reset before appending to them. In particular, it is recommended to pass a pointer to a zero valued struct on each Get call.

ErrFieldMismatch is returned when a field is to be loaded into a different type than the one it was stored from, or when a field is missing or unexported in the destination struct. ErrFieldMismatch is only returned if dst is a struct pointer.

### func GetMulti 
    
    
    func GetMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key []*Key, dst interface{}) [error](https://pkg.go.dev/builtin#error)

GetMulti is a batch version of Get.

dst must be a []S, []*S, []I or []P, for some struct type S, some interface type I, or some non-interface non-pointer type P such that P or *P implements PropertyLoadSaver. If an []I, each element must be a valid dst for Get: it must be a struct pointer or implement PropertyLoadSaver.

As a special case, PropertyList is an invalid type for dst, even though a PropertyList is a slice of structs. It is treated as invalid to avoid being mistakenly passed when []PropertyList was intended.

### func KindProperties 
    
    
    func KindProperties(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), kind [string](https://pkg.go.dev/builtin#string)) (map[[string](https://pkg.go.dev/builtin#string)][][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

KindProperties returns all the indexed properties for the given kind. The properties are returned as a map of property names to a slice of the representation types. The representation types for the supported Go property types are:
    
    
    "INT64":     signed integers and time.Time
    "DOUBLE":    float32 and float64
    "BOOLEAN":   bool
    "STRING":    string, []byte and ByteString
    "POINT":     appengine.GeoPoint
    "REFERENCE": *Key
    "USER":      (not used in the Go runtime)
    

### func Kinds 
    
    
    func Kinds(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) ([][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

Kinds returns the names of all the kinds in the current namespace.

### func LoadStruct 
    
    
    func LoadStruct(dst interface{}, p []Property) [error](https://pkg.go.dev/builtin#error)

LoadStruct loads the properties from p to dst. dst must be a struct pointer.

### func Namespaces 
    
    
    func Namespaces(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) ([][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

Namespaces returns all the datastore namespaces.

### func RunInTransaction 
    
    
    func RunInTransaction(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), f func(tc [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [error](https://pkg.go.dev/builtin#error), opts *TransactionOptions) [error](https://pkg.go.dev/builtin#error)

RunInTransaction runs f in a transaction. It calls f with a transaction context tc that f should use for all App Engine operations.

If f returns nil, RunInTransaction attempts to commit the transaction, returning nil if it succeeds. If the commit fails due to a conflicting transaction, RunInTransaction retries f, each time with a new transaction context. It gives up and returns ErrConcurrentTransaction after three failed attempts. The number of attempts can be configured by specifying TransactionOptions.Attempts.

If f returns non-nil, then any datastore changes will not be applied and RunInTransaction returns that same error. The function f is not retried.

Note that when f returns, the transaction is not yet committed. Calling code must be careful not to assume that any of f's changes have been committed until RunInTransaction returns nil.

Since f may be called multiple times, f should usually be idempotent. datastore.Get is not idempotent when unmarshaling slice fields.

Nested transactions are not supported; c may not be a transaction context.

## ByteString
    
    
    type ByteString [][byte](https://pkg.go.dev/builtin#byte)

ByteString is a short byte slice (up to 1500 bytes) that can be indexed.

## Cursor
    
    
    type Cursor struct {
    	// contains filtered or unexported fields
    }

Cursor is an iterator's position. It can be converted to and from an opaque string. A cursor can be used from different HTTP requests, but only with a query with the same kind, ancestor, filter and order constraints.

### func DecodeCursor 
    
    
    func DecodeCursor(s [string](https://pkg.go.dev/builtin#string)) (Cursor, [error](https://pkg.go.dev/builtin#error))

DecodeCursor decodes a cursor from its base-64 string representation.

### func (Cursor) String 
    
    
    func (c Cursor) String() [string](https://pkg.go.dev/builtin#string)

String returns a base-64 string representation of a cursor.

## Entity
    
    
    type Entity struct {
    	Key        *Key
    	Properties []Property
    }

An Entity is the value type for a nested struct. This type is only used for a Property's Value.

## ErrFieldMismatch
    
    
    type ErrFieldMismatch struct {
    	StructType [reflect](https://pkg.go.dev/reflect).[Type](https://pkg.go.dev/reflect#Type)
    	FieldName  [string](https://pkg.go.dev/builtin#string)
    	Reason     [string](https://pkg.go.dev/builtin#string)
    }

ErrFieldMismatch is returned when a field is to be loaded into a different type than the one it was stored from, or when a field is missing or unexported in the destination struct. StructType is the type of the struct pointed to by the destination argument passed to Get or to Iterator.Next.

### func (*ErrFieldMismatch) Error 
    
    
    func (e *ErrFieldMismatch) Error() [string](https://pkg.go.dev/builtin#string)

## Iterator
    
    
    type Iterator struct {
    	// contains filtered or unexported fields
    }

Iterator is the result of running a query.

### func (*Iterator) Cursor 
    
    
    func (t *Iterator) Cursor() (Cursor, [error](https://pkg.go.dev/builtin#error))

Cursor returns a cursor for the iterator's current location.

### func (*Iterator) Next 
    
    
    func (t *Iterator) Next(dst interface{}) (*Key, [error](https://pkg.go.dev/builtin#error))

Next returns the key of the next result. When there are no more results, Done is returned as the error.

If the query is not keys only and dst is non-nil, it also loads the entity stored for that key into the struct pointer or PropertyLoadSaver dst, with the same semantics and possible errors as for the Get function.

## Key
    
    
    type Key struct {
    	// contains filtered or unexported fields
    }

Key represents the datastore key for a stored entity, and is immutable.

### func DecodeKey 
    
    
    func DecodeKey(encoded [string](https://pkg.go.dev/builtin#string)) (*Key, [error](https://pkg.go.dev/builtin#error))

DecodeKey decodes a key from the opaque representation returned by Encode.

### func NewIncompleteKey 
    
    
    func NewIncompleteKey(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), kind [string](https://pkg.go.dev/builtin#string), parent *Key) *Key

NewIncompleteKey creates a new incomplete key. kind cannot be empty.

### func NewKey 
    
    
    func NewKey(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), kind, stringID [string](https://pkg.go.dev/builtin#string), intID [int64](https://pkg.go.dev/builtin#int64), parent *Key) *Key

NewKey creates a new key. kind cannot be empty. Either one or both of stringID and intID must be zero. If both are zero, the key returned is incomplete. parent must either be a complete key or nil.

### func Put 
    
    
    func Put(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key *Key, src interface{}) (*Key, [error](https://pkg.go.dev/builtin#error))

Put saves the entity src into the datastore with key k. src must be a struct pointer or implement PropertyLoadSaver; if a struct pointer then any unexported fields of that struct will be skipped. If k is an incomplete key, the returned key will be a unique key generated by the datastore.

### func PutMulti 
    
    
    func PutMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key []*Key, src interface{}) ([]*Key, [error](https://pkg.go.dev/builtin#error))

PutMulti is a batch version of Put.

src must satisfy the same conditions as the dst argument to GetMulti.

### func (*Key) AppID 
    
    
    func (k *Key) AppID() [string](https://pkg.go.dev/builtin#string)

AppID returns the key's application ID.

### func (*Key) Encode 
    
    
    func (k *Key) Encode() [string](https://pkg.go.dev/builtin#string)

Encode returns an opaque representation of the key suitable for use in HTML and URLs. This is compatible with the Python and Java runtimes.

### func (*Key) Equal 
    
    
    func (k *Key) Equal(o *Key) [bool](https://pkg.go.dev/builtin#bool)

Equal returns whether two keys are equal.

### func (*Key) GobDecode 
    
    
    func (k *Key) GobDecode(buf [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

### func (*Key) GobEncode 
    
    
    func (k *Key) GobEncode() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

### func (*Key) Incomplete 
    
    
    func (k *Key) Incomplete() [bool](https://pkg.go.dev/builtin#bool)

Incomplete returns whether the key does not refer to a stored entity. In particular, whether the key has a zero StringID and a zero IntID.

### func (*Key) IntID 
    
    
    func (k *Key) IntID() [int64](https://pkg.go.dev/builtin#int64)

IntID returns the key's integer ID, which may be 0.

### func (*Key) Kind 
    
    
    func (k *Key) Kind() [string](https://pkg.go.dev/builtin#string)

Kind returns the key's kind (also known as entity type).

### func (*Key) MarshalJSON 
    
    
    func (k *Key) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

### func (*Key) Namespace 
    
    
    func (k *Key) Namespace() [string](https://pkg.go.dev/builtin#string)

Namespace returns the key's namespace.

### func (*Key) Parent 
    
    
    func (k *Key) Parent() *Key

Parent returns the key's parent key, which may be nil.

### func (*Key) String 
    
    
    func (k *Key) String() [string](https://pkg.go.dev/builtin#string)

String returns a string representation of the key.

### func (*Key) StringID 
    
    
    func (k *Key) StringID() [string](https://pkg.go.dev/builtin#string)

StringID returns the key's string ID (also known as an entity name or key name), which may be "".

### func (*Key) UnmarshalJSON 
    
    
    func (k *Key) UnmarshalJSON(buf [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

## KeyRangeCollisionError
    
    
    type KeyRangeCollisionError struct {
    	// contains filtered or unexported fields
    }

### func (*KeyRangeCollisionError) Error 
    
    
    func (e *KeyRangeCollisionError) Error() [string](https://pkg.go.dev/builtin#string)

## KeyRangeContentionError
    
    
    type KeyRangeContentionError struct {
    	// contains filtered or unexported fields
    }

### func (*KeyRangeContentionError) Error 
    
    
    func (e *KeyRangeContentionError) Error() [string](https://pkg.go.dev/builtin#string)

## Property
    
    
    type Property struct {
    	// Name is the property name.
    	Name [string](https://pkg.go.dev/builtin#string)
    	// Value is the property value. The valid types are:
    	//	- int64
    	//	- bool
    	//	- string
    	//	- float64
    	//	- ByteString
    	//	- *Key
    	//	- time.Time
    	//	- appengine.BlobKey
    	//	- appengine.GeoPoint
    	//	- []byte (up to 1 megabyte in length)
    	//	- *Entity (representing a nested struct)
    	// This set is smaller than the set of valid struct field types that the
    	// datastore can load and save. A Property Value cannot be a slice (apart
    	// from []byte); use multiple Properties instead. Also, a Value's type
    	// must be explicitly on the list above; it is not sufficient for the
    	// underlying type to be on that list. For example, a Value of "type
    	// myInt64 int64" is invalid. Smaller-width integers and floats are also
    	// invalid. Again, this is more restrictive than the set of valid struct
    	// field types.
    	//
    	// A Value will have an opaque type when loading entities from an index,
    	// such as via a projection query. Load entities into a struct instead
    	// of a PropertyLoadSaver when using a projection query.
    	//
    	// A Value may also be the nil interface value; this is equivalent to
    	// Python's None but not directly representable by a Go struct. Loading
    	// a nil-valued property into a struct will set that field to the zero
    	// value.
    	Value interface{}
    	// NoIndex is whether the datastore cannot index this property.
    	NoIndex [bool](https://pkg.go.dev/builtin#bool)
    	// Multiple is whether the entity can have multiple properties with
    	// the same name. Even if a particular instance only has one property with
    	// a certain name, Multiple should be true if a struct would best represent
    	// it as a field of type []T instead of type T.
    	Multiple [bool](https://pkg.go.dev/builtin#bool)
    }

Property is a name/value pair plus some metadata. A datastore entity's contents are loaded and saved as a sequence of Properties. An entity can have multiple Properties with the same name, provided that p.Multiple is true on all of that entity's Properties with that name.

### func SaveStruct 
    
    
    func SaveStruct(src interface{}) ([]Property, [error](https://pkg.go.dev/builtin#error))

SaveStruct returns the properties from src as a slice of Properties. src must be a struct pointer.

## PropertyList
    
    
    type PropertyList []Property

PropertyList converts a []Property to implement PropertyLoadSaver.

### func (*PropertyList) Load 
    
    
    func (l *PropertyList) Load(p []Property) [error](https://pkg.go.dev/builtin#error)

Load loads all of the provided properties into l. It does not first reset *l to an empty slice.

### func (*PropertyList) Save 
    
    
    func (l *PropertyList) Save() ([]Property, [error](https://pkg.go.dev/builtin#error))

Save saves all of l's properties as a slice or Properties.

## PropertyLoadSaver
    
    
    type PropertyLoadSaver interface {
    	Load([]Property) [error](https://pkg.go.dev/builtin#error)
    	Save() ([]Property, [error](https://pkg.go.dev/builtin#error))
    }

PropertyLoadSaver can be converted from and to a slice of Properties.

## Query
    
    
    type Query struct {
    	// contains filtered or unexported fields
    }

Query represents a datastore query.

### func NewQuery 
    
    
    func NewQuery(kind [string](https://pkg.go.dev/builtin#string)) *Query

NewQuery creates a new Query for a specific entity kind.

An empty kind means to return all entities, including entities created and managed by other App Engine features, and is called a kindless query. Kindless queries cannot include filters or sort orders on property values.

### func (*Query) Ancestor 
    
    
    func (q *Query) Ancestor(ancestor *Key) *Query

Ancestor returns a derivative query with an ancestor filter. The ancestor should not be nil.

### func (*Query) BatchSize 
    
    
    func (q *Query) BatchSize(size [int](https://pkg.go.dev/builtin#int)) *Query

BatchSize returns a derivative query to fetch the supplied number of results at once. This value should be greater than zero, and equal to or less than the Limit.

### func (*Query) Count 
    
    
    func (q *Query) Count(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) ([int](https://pkg.go.dev/builtin#int), [error](https://pkg.go.dev/builtin#error))

Count returns the number of results for the query.

The running time and number of API calls made by Count scale linearly with the sum of the query's offset and limit. Unless the result count is expected to be small, it is best to specify a limit; otherwise Count will continue until it finishes counting or the provided context expires.

### func (*Query) Distinct 
    
    
    func (q *Query) Distinct() *Query

Distinct returns a derivative query that yields de-duplicated entities with respect to the set of projected fields. It is only used for projection queries. Distinct cannot be used with DistinctOn.

### func (*Query) DistinctOn 
    
    
    func (q *Query) DistinctOn(fieldNames [string](https://pkg.go.dev/builtin#string)) *Query

DistinctOn returns a derivative query that yields de-duplicated entities with respect to the set of the specified fields. It is only used for projection queries. The field list should be a subset of the projected field list. DistinctOn cannot be used with Distinct.

### func (*Query) End 
    
    
    func (q *Query) End(c Cursor) *Query

End returns a derivative query with the given end point.

### func (*Query) EventualConsistency 
    
    
    func (q *Query) EventualConsistency() *Query

EventualConsistency returns a derivative query that returns eventually consistent results. It only has an effect on ancestor queries.

### func (*Query) Filter 
    
    
    func (q *Query) Filter(filterStr [string](https://pkg.go.dev/builtin#string), value interface{}) *Query

Filter returns a derivative query with a field-based filter. The filterStr argument must be a field name followed by optional space, followed by an operator, one of ">", "<", ">=", "<=", or "=". Fields are compared against the provided value using the operator. Multiple filters are AND'ed together.

### func (*Query) GetAll 
    
    
    func (q *Query) GetAll(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), dst interface{}) ([]*Key, [error](https://pkg.go.dev/builtin#error))

GetAll runs the query in the given context and returns all keys that match that query, as well as appending the values to dst.

dst must have type _[]S or *[]_ S or *[]P, for some struct type S or some non- interface, non-pointer type P such that P or *P implements PropertyLoadSaver.

As a special case, *PropertyList is an invalid type for dst, even though a PropertyList is a slice of structs. It is treated as invalid to avoid being mistakenly passed when *[]PropertyList was intended.

The keys returned by GetAll will be in a 1-1 correspondence with the entities added to dst.

If q is a “keys-only” query, GetAll ignores dst and only returns the keys.

The running time and number of API calls made by GetAll scale linearly with the sum of the query's offset and limit. Unless the result count is expected to be small, it is best to specify a limit; otherwise GetAll will continue until it finishes collecting results or the provided context expires.

### func (*Query) KeysOnly 
    
    
    func (q *Query) KeysOnly() *Query

KeysOnly returns a derivative query that yields only keys, not keys and entities. It cannot be used with projection queries.

### func (*Query) Limit 
    
    
    func (q *Query) Limit(limit [int](https://pkg.go.dev/builtin#int)) *Query

Limit returns a derivative query that has a limit on the number of results returned. A negative value means unlimited.

### func (*Query) Offset 
    
    
    func (q *Query) Offset(offset [int](https://pkg.go.dev/builtin#int)) *Query

Offset returns a derivative query that has an offset of how many keys to skip over before returning results. A negative value is invalid.

### func (*Query) Order 
    
    
    func (q *Query) Order(fieldName [string](https://pkg.go.dev/builtin#string)) *Query

Order returns a derivative query with a field-based sort order. Orders are applied in the order they are added. The default order is ascending; to sort in descending order prefix the fieldName with a minus sign (-).

### func (*Query) Project 
    
    
    func (q *Query) Project(fieldNames [string](https://pkg.go.dev/builtin#string)) *Query

Project returns a derivative query that yields only the given fields. It cannot be used with KeysOnly.

### func (*Query) Run 
    
    
    func (q *Query) Run(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *Iterator

Run runs the query in the given context.

### func (*Query) Start 
    
    
    func (q *Query) Start(c Cursor) *Query

Start returns a derivative query with the given start point.

## TransactionOptions
    
    
    type TransactionOptions struct {
    	// XG is whether the transaction can cross multiple entity groups. In
    	// comparison, a single group transaction is one where all datastore keys
    	// used have the same root key. Note that cross group transactions do not
    	// have the same behavior as single group transactions. In particular, it
    	// is much more likely to see partially applied transactions in different
    	// entity groups, in global queries.
    	// It is valid to set XG to true even if the transaction is within a
    	// single entity group.
    	XG [bool](https://pkg.go.dev/builtin#bool)
    	// Attempts controls the number of retries to perform when commits fail
    	// due to a conflicting transaction. If omitted, it defaults to 3.
    	Attempts [int](https://pkg.go.dev/builtin#int)
    	// ReadOnly controls whether the transaction is a read only transaction.
    	// Read only transactions are potentially more efficient.
    	ReadOnly [bool](https://pkg.go.dev/builtin#bool)
    }

TransactionOptions are the options for running a transaction.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
