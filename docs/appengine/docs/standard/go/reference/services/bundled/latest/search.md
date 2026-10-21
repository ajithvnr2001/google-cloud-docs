---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/search/
title: Package google.golang.org/appengine/v2/search (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:51.330558+00:00
---

# Package google.golang.org/appengine/v2/search (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/search (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/search). 

Package search provides a client for App Engine's search service. 

## Basic Operations

Indexes contain documents. Each index is identified by its name: a human-readable ASCII string. 

Within an index, documents are associated with an ID, which is also a human-readable ASCII string. A document's contents are a mapping from case-sensitive field names to values. Valid types for field values are: 

  * string, 
  * search.Atom, 
  * search.HTML, 
  * time.Time (stored with millisecond precision), 
  * float64 (value between -2,147,483,647 and 2,147,483,647 inclusive), 
  * appengine.GeoPoint. 



The Get and Put methods on an Index load and save a document. A document's contents are typically represented by a struct pointer. 

Example code:
    
    
    type Doc struct {
        Author   string
        Comment  string
        Creation time.Time
    }
    
    index, err := search.Open("comments")
    if err != nil {
        return err
    }
    newID, err := index.Put(ctx, "", &Doc{
        Author:   "gopher",
        Comment:  "the truth of the matter",
        Creation: time.Now(),
    })
    if err != nil {
        return err
    }

A single document can be retrieved by its ID. Pass a destination struct to Get to hold the resulting document.
    
    
    var doc Doc
    err := index.Get(ctx, id, &doc)
    if err != nil {
        return err
    }

## Search and Listing Documents

Indexes have two methods for retrieving multiple documents at once: Search and List. 

Searching an index for a query will result in an iterator. As with an iterator from package datastore, pass a destination struct to Next to decode the next result. Next will return Done when the iterator is exhausted.
    
    
    for t := index.Search(ctx, "Comment:truth", nil); ; {
        var doc Doc
        id, err := t.Next(&doc)
        if err == search.Done {
            break
        }
        if err != nil {
            return err
        }
        fmt.Fprintf(w, "%s -> %#v\n", id, doc)
    }

Search takes a string query to determine which documents to return. The query can be simple, such as a single word to match, or complex. The query language is described at <https://cloud.google.com/appengine/docs/standard/go/search/query_strings>

Search also takes an optional SearchOptions struct which gives much more control over how results are calculated and returned. 

Call List to iterate over all documents in an index.
    
    
    for t := index.List(ctx, nil); ; {
        var doc Doc
        id, err := t.Next(&doc)
        if err == search.Done {
            break
        }
        if err != nil {
            return err
        }
        fmt.Fprintf(w, "%s -> %#v\n", id, doc)
    }

## Fields and Facets

A document's contents can be represented by a variety of types. These are typically struct pointers, but they can also be represented by any type implementing the FieldLoadSaver interface. The FieldLoadSaver allows metadata to be set for the document with the DocumentMetadata type. Struct pointers are more strongly typed and are easier to use; FieldLoadSavers are more flexible. 

A document's contents can be expressed in two ways: fields and facets. 

Fields are the most common way of providing content for documents. Fields can store data in multiple types and can be matched in searches using query strings. 

Facets provide a way to attach categorical information to a document. The only valid types for facets are search.Atom and float64. Facets allow search results to contain summaries of the categories matched in a search, and to restrict searches to only match against specific categories. 

By default, for struct pointers, all of the struct fields are used as document fields, and the field name used is the same as on the struct (and hence must start with an upper case letter). Struct fields may have a `search:&quot;name,options&quot;` tag. The name must start with a letter and be composed only of word characters. A "-" tag name means that the field will be ignored. If options is "facet" then the struct field will be used as a document facet. If options is "" then the comma may be omitted. There are no other recognized options. 

Example code:
    
    
    // A and B are renamed to a and b.
    // A, C and I are facets.
    // D's tag is equivalent to having no tag at all (E).
    // F and G are ignored entirely by the search package.
    // I has tag information for both the search and json packages.
    type TaggedStruct struct {
        A float64 `search:"a,facet"`
        B float64 `search:"b"`
        C float64 `search:",facet"`
        D float64 `search:""`
        E float64
        F float64 `search:"-"`
        G float64 `search:"-,facet"`
        I float64 `search:",facet" json:"i"`
    }

## The FieldLoadSaver Interface

A document's contents can also be represented by any type that implements the FieldLoadSaver interface. This type may be a struct pointer, but it does not have to be. The search package will call Load when loading the document's contents, and Save when saving them. In addition to a slice of Fields, the Load and Save methods also use the DocumentMetadata type to provide additional information about a document (such as its Rank, or set of Facets). Possible uses for this interface include deriving non-stored fields, verifying fields or setting specific languages for string and HTML fields. 

Example code:
    
    
    type CustomFieldsExample struct {
        // Item's title and which language it is in.
        Title string
        Lang  string
        // Mass, in grams.
        Mass int
    }
    
    func (x *CustomFieldsExample) Load(fields []search.Field, meta *search.DocumentMetadata) error {
        // Load the title field, failing if any other field is found.
        for _, f := range fields {
            if f.Name != "title" {
                return fmt.Errorf("unknown field %q", f.Name)
            }
            s, ok := f.Value.(string)
            if !ok {
                return fmt.Errorf("unsupported type %T for field %q", f.Value, f.Name)
            }
            x.Title = s
            x.Lang = f.Language
        }
        // Load the mass facet, failing if any other facet is found.
        for _, f := range meta.Facets {
            if f.Name != "mass" {
                return fmt.Errorf("unknown facet %q", f.Name)
            }
            m, ok := f.Value.(float64)
            if !ok {
                return fmt.Errorf("unsupported type %T for facet %q", f.Value, f.Name)
            }
            x.Mass = int(m)
        }
        return nil
    }
    
    func (x *CustomFieldsExample) Save() ([]search.Field, *search.DocumentMetadata, error) {
        fields := []search.Field{
            {Name: "title", Value: x.Title, Language: x.Lang},
        }
        meta := &search.DocumentMetadata{
            Facets: {
                {Name: "mass", Value: float64(x.Mass)},
            },
        }
        return fields, meta, nil
    }

## Variables 

### ErrInvalidDocumentType, ErrNoSuchDocument, ErrTooManyDocuments
    
    
    var (
    	// ErrInvalidDocumentType is returned when methods like Put, Get or Next
    	// are passed a dst or src argument of invalid type.
    	ErrInvalidDocumentType = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("search: invalid document type")
    
    	// ErrNoSuchDocument is returned when no document was found for a given ID.
    	ErrNoSuchDocument = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("search: no such document")
    
    	// ErrTooManyDocuments is returned when the user passes too many documents to
    	// PutMulti or DeleteMulti.
    	ErrTooManyDocuments = [fmt](https://pkg.go.dev/fmt).[Errorf](https://pkg.go.dev/fmt#Errorf)("search: too many documents given to put or delete (max is %d)", maxDocumentsPerPutDelete)
    )

### Done
    
    
    var Done = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("search: query has no more results")

Done is returned when a query iteration has completed.

## Functions 

### func LoadStruct 
    
    
    func LoadStruct(dst interface{}, f []Field) [error](https://pkg.go.dev/builtin#error)

LoadStruct loads the fields from f to dst. dst must be a struct pointer.

## Atom
    
    
    type Atom [string](https://pkg.go.dev/builtin#string)

Atom is a document field whose contents are indexed as a single indivisible string.

## Cursor
    
    
    type Cursor [string](https://pkg.go.dev/builtin#string)

Cursor represents an iterator's position.

The string value of a cursor is web-safe. It can be saved and restored for later use.

## DocumentMetadata
    
    
    type DocumentMetadata struct {
    	// Rank is an integer specifying the order the document will be returned in
    	// search results. If zero, the rank will be set to the number of seconds since
    	// 2011-01-01 00:00:00 UTC when being Put into an index.
    	Rank [int](https://pkg.go.dev/builtin#int)
    	// Facets is the set of facets for this document.
    	Facets []Facet
    }

DocumentMetadata is a struct containing information describing a given document.

## ErrFacetMismatch
    
    
    type ErrFacetMismatch struct {
    	StructType [reflect](https://pkg.go.dev/reflect).[Type](https://pkg.go.dev/reflect#Type)
    	FacetName  [string](https://pkg.go.dev/builtin#string)
    	Reason     [string](https://pkg.go.dev/builtin#string)
    }

ErrFacetMismatch is returned when a facet is to be loaded into a different type than the one it was stored from, or when a field is missing or unexported in the destination struct. StructType is the type of the struct pointed to by the destination argument passed to Iterator.Next.

### func (*ErrFacetMismatch) Error 
    
    
    func (e *ErrFacetMismatch) Error() [string](https://pkg.go.dev/builtin#string)

## ErrFieldMismatch
    
    
    type ErrFieldMismatch struct {
    	FieldName [string](https://pkg.go.dev/builtin#string)
    	Reason    [string](https://pkg.go.dev/builtin#string)
    }

ErrFieldMismatch is returned when a field is to be loaded into a different than the one it was stored from, or when a field is missing or unexported in the destination struct.

### func (*ErrFieldMismatch) Error 
    
    
    func (e *ErrFieldMismatch) Error() [string](https://pkg.go.dev/builtin#string)

## Facet
    
    
    type Facet struct {
    	// Name is the facet name. A valid facet name matches /[A-Za-z][A-Za-z0-9_]*/.
    	// A facet name cannot be longer than 500 characters.
    	Name [string](https://pkg.go.dev/builtin#string)
    	// Value is the facet value.
    	//
    	// When being used in documents (for example, in
    	// DocumentMetadata.Facets), the valid types are:
    	//  - search.Atom,
    	//  - float64.
    	//
    	// When being used in SearchOptions.Refinements or being returned
    	// in FacetResult, the valid types are:
    	//  - search.Atom,
    	//  - search.Range.
    	Value interface{}
    }

Facet is a name/value pair which is used to add categorical information to a document.

## FacetResult
    
    
    type FacetResult struct {
    	Facet
    
    	// Count is the number of times this specific facet and value appeared in the
    	// matching documents.
    	Count [int](https://pkg.go.dev/builtin#int)
    }

FacetResult represents the number of times a particular facet and value appeared in the documents matching a search request.

## FacetSearchOption
    
    
    type FacetSearchOption interface {
    	// contains filtered or unexported methods
    }

FacetSearchOption controls what facet information is returned in search results.

### func AutoFacetDiscovery 
    
    
    func AutoFacetDiscovery(facetLimit, valueLimit [int](https://pkg.go.dev/builtin#int)) FacetSearchOption

AutoFacetDiscovery returns a FacetSearchOption which enables automatic facet discovery for the search. Automatic facet discovery looks for the facets which appear the most often in the aggregate in the matched documents.

The maximum number of facets returned is controlled by facetLimit, and the maximum number of values per facet by facetLimit. A limit of zero indicates a default limit should be used.

### func FacetDiscovery 
    
    
    func FacetDiscovery(name [string](https://pkg.go.dev/builtin#string), value ...interface{}) FacetSearchOption

FacetDiscovery returns a FacetSearchOption which selects a facet to be returned with the search results. By default, the most frequently occurring values for that facet will be returned. However, you can also specify a list of particular Atoms or specific Ranges to return.

### func FacetDocumentDepth 
    
    
    func FacetDocumentDepth(depth [int](https://pkg.go.dev/builtin#int)) FacetSearchOption

FacetDocumentDepth returns a FacetSearchOption which controls the number of documents to be evaluated with preparing facet results.

## Field
    
    
    type Field struct {
    	// Name is the field name. A valid field name matches /[A-Za-z][A-Za-z0-9_]*/.
    	Name [string](https://pkg.go.dev/builtin#string)
    	// Value is the field value. The valid types are:
    	//  - string,
    	//  - search.Atom,
    	//  - search.HTML,
    	//  - time.Time (stored with millisecond precision),
    	//  - float64,
    	//  - GeoPoint.
    	Value interface{}
    	// Language is a two-letter ISO 639-1 code for the field's language,
    	// defaulting to "en" if nothing is specified. It may only be specified for
    	// fields of type string and search.HTML.
    	Language [string](https://pkg.go.dev/builtin#string)
    	// Derived marks fields that were calculated as a result of a
    	// FieldExpression provided to Search. This field is ignored when saving a
    	// document.
    	Derived [bool](https://pkg.go.dev/builtin#bool)
    }

Field is a name/value pair. A search index's document can be loaded and saved as a sequence of Fields.

### func SaveStruct 
    
    
    func SaveStruct(src interface{}) ([]Field, [error](https://pkg.go.dev/builtin#error))

SaveStruct returns the fields from src as a slice of Field. src must be a struct pointer.

## FieldExpression
    
    
    type FieldExpression struct {
    	// Name is the name to use for the computed field.
    	Name [string](https://pkg.go.dev/builtin#string)
    
    	// Expr is evaluated to provide a custom content snippet for each document.
    	// See https://cloud.google.com/appengine/docs/standard/go/search/options for
    	// the supported expression syntax.
    	Expr [string](https://pkg.go.dev/builtin#string)
    }

FieldExpression defines a custom expression to evaluate for each result.

## FieldList
    
    
    type FieldList []Field

FieldList converts a []Field to implement FieldLoadSaver.

### func (*FieldList) Load 
    
    
    func (l *FieldList) Load(f []Field, _ *DocumentMetadata) [error](https://pkg.go.dev/builtin#error)

Load loads all of the provided fields into l. It does not first reset *l to an empty slice.

### func (*FieldList) Save 
    
    
    func (l *FieldList) Save() ([]Field, *DocumentMetadata, [error](https://pkg.go.dev/builtin#error))

Save returns all of l's fields as a slice of Fields.

## FieldLoadSaver
    
    
    type FieldLoadSaver interface {
    	Load([]Field, *DocumentMetadata) [error](https://pkg.go.dev/builtin#error)
    	Save() ([]Field, *DocumentMetadata, [error](https://pkg.go.dev/builtin#error))
    }

FieldLoadSaver can be converted from and to a slice of Fields with additional document metadata.

## HTML
    
    
    type HTML [string](https://pkg.go.dev/builtin#string)

HTML is a document field whose contents are indexed as HTML. Only text nodes are indexed: "foo**bar" will be treated as "foobar".**

****

## Index
    
    
    type Index struct {
    	// contains filtered or unexported fields
    }

Index is an index of documents.

### func Open 
    
    
    func Open(name [string](https://pkg.go.dev/builtin#string)) (*Index, [error](https://pkg.go.dev/builtin#error))

Open opens the index with the given name. The index is created if it does not already exist.

The name is a human-readable ASCII string. It must contain no whitespace characters and not start with "!".

### func (*Index) Delete 
    
    
    func (x *Index) Delete(c context.Context, id [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a document from the index.

### func (*Index) DeleteMulti 
    
    
    func (x *Index) DeleteMulti(c context.Context, ids [][string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

DeleteMulti deletes multiple documents from the index.

The returned error may be an instance of appengine.MultiError, in which case it will be the same size as srcs and the individual errors inside will correspond with the items in srcs.

### func (*Index) Get 
    
    
    func (x *Index) Get(c context.Context, id [string](https://pkg.go.dev/builtin#string), dst interface{}) [error](https://pkg.go.dev/builtin#error)

Get loads the document with the given ID into dst.

The ID is a human-readable ASCII string. It must be non-empty, contain no whitespace characters and not start with "!".

dst must be a non-nil struct pointer or implement the FieldLoadSaver interface.

ErrFieldMismatch is returned when a field is to be loaded into a different type than the one it was stored from, or when a field is missing or unexported in the destination struct. ErrFieldMismatch is only returned if dst is a struct pointer. It is up to the callee to decide whether this error is fatal, recoverable, or ignorable.

### func (*Index) List 
    
    
    func (x *Index) List(c context.Context, opts *ListOptions) *Iterator

List lists all of the documents in an index. The documents are returned in increasing ID order.

### func (*Index) Put 
    
    
    func (x *Index) Put(c context.Context, id [string](https://pkg.go.dev/builtin#string), src interface{}) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

Put saves src to the index. If id is empty, a new ID is allocated by the service and returned. If id is not empty, any existing index entry for that ID is replaced.

The ID is a human-readable ASCII string. It must contain no whitespace characters and not start with "!".

src must be a non-nil struct pointer or implement the FieldLoadSaver interface.

### func (*Index) PutMulti 
    
    
    func (x *Index) PutMulti(c context.Context, ids [][string](https://pkg.go.dev/builtin#string), srcs []interface{}) ([][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

PutMulti is like Put, but is more efficient for adding multiple documents to the index at once.

Up to 200 documents can be added at once. ErrTooManyDocuments is returned if you try to add more.

ids can either be an empty slice (which means new IDs will be allocated for each of the documents added) or a slice the same size as srcs.

The error may be an instance of appengine.MultiError, in which case it will be the same size as srcs and the individual errors inside will correspond with the items in srcs.

### func (*Index) Search 
    
    
    func (x *Index) Search(c context.Context, query [string](https://pkg.go.dev/builtin#string), opts *SearchOptions) *Iterator

Search searches the index for the given query.

## Iterator
    
    
    type Iterator struct {
    	// contains filtered or unexported fields
    }

Iterator is the result of searching an index for a query or listing an index.

### func (*Iterator) Count 
    
    
    func (t *Iterator) Count() [int](https://pkg.go.dev/builtin#int)

Count returns an approximation of the number of documents matched by the query. It is only valid to call for iterators returned by Search.

### func (*Iterator) Cursor 
    
    
    func (t *Iterator) Cursor() Cursor

Cursor returns the cursor associated with the current document (that is, the document most recently returned by a call to Next).

Passing this cursor in a future call to Search will cause those results to commence with the first document after the current document.

### func (*Iterator) Facets 
    
    
    func (t *Iterator) Facets() ([][]FacetResult, [error](https://pkg.go.dev/builtin#error))

Facets returns the facets found within the search results, if any facets were requested in the SearchOptions.

### func (*Iterator) Next 
    
    
    func (t *Iterator) Next(dst interface{}) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

Next returns the ID of the next result. When there are no more results, Done is returned as the error.

dst must be a non-nil struct pointer, implement the FieldLoadSaver interface, or be a nil interface value. If a non-nil dst is provided, it will be filled with the indexed fields. dst is ignored if this iterator was created with an IDsOnly option.

## ListOptions
    
    
    type ListOptions struct {
    	// StartID is the inclusive lower bound for the ID of the returned
    	// documents. The zero value means all documents will be returned.
    	StartID [string](https://pkg.go.dev/builtin#string)
    
    	// Limit is the maximum number of documents to return. The zero value
    	// indicates no limit.
    	Limit [int](https://pkg.go.dev/builtin#int)
    
    	// IDsOnly indicates that only document IDs should be returned for the list
    	// operation; no document fields are populated.
    	IDsOnly [bool](https://pkg.go.dev/builtin#bool)
    }

ListOptions are the options for listing documents in an index. Passing a nil *ListOptions is equivalent to using the default values.

## Range
    
    
    type Range struct {
    	Start, End [float64](https://pkg.go.dev/builtin#float64)
    }

Range represents a numeric range with inclusive start and exclusive end. Start may be specified as math.Inf(-1) to indicate there is no minimum value, and End may similarly be specified as math.Inf(1); at least one of Start or End must be a finite number.

### func AtLeast 
    
    
    func AtLeast(min [float64](https://pkg.go.dev/builtin#float64)) Range

AtLeast returns a Range matching any value greater than, or equal to, min.

### func LessThan 
    
    
    func LessThan(max [float64](https://pkg.go.dev/builtin#float64)) Range

LessThan returns a Range matching any value less than max.

## Scorer
    
    
    type Scorer interface {
    	// contains filtered or unexported methods
    }

A Scorer defines how a document is scored.

### MatchScorer, RescoringMatchScorer
    
    
    var (
    	// MatchScorer assigns a score based on term frequency in a document.
    	MatchScorer Scorer = enumScorer{[pb](https://pkg.go.dev/google.golang.org/appengine/v2/internal/search).[ScorerSpec_MATCH_SCORER](https://pkg.go.dev/google.golang.org/appengine/v2/internal/search#ScorerSpec_MATCH_SCORER)}
    
    	// RescoringMatchScorer assigns a score based on the quality of the query
    	// match. It is similar to a MatchScorer but uses a more complex scoring
    	// algorithm based on match term frequency and other factors like field type.
    	// Please be aware that this algorithm is continually refined and can change
    	// over time without notice. This means that the ordering of search results
    	// that use this scorer can also change without notice.
    	RescoringMatchScorer Scorer = enumScorer{[pb](https://pkg.go.dev/google.golang.org/appengine/v2/internal/search).[ScorerSpec_RESCORING_MATCH_SCORER](https://pkg.go.dev/google.golang.org/appengine/v2/internal/search#ScorerSpec_RESCORING_MATCH_SCORER)}
    )

## SearchOptions
    
    
    type SearchOptions struct {
    	// Limit is the maximum number of documents to return. The zero value
    	// indicates no limit.
    	Limit [int](https://pkg.go.dev/builtin#int)
    
    	// IDsOnly indicates that only document IDs should be returned for the search
    	// operation; no document fields are populated.
    	IDsOnly [bool](https://pkg.go.dev/builtin#bool)
    
    	// Sort controls the ordering of search results.
    	Sort *SortOptions
    
    	// Fields specifies which document fields to include in the results. If omitted,
    	// all document fields are returned. No more than 100 fields may be specified.
    	Fields [][string](https://pkg.go.dev/builtin#string)
    
    	// Expressions specifies additional computed fields to add to each returned
    	// document.
    	Expressions []FieldExpression
    
    	// Facets controls what facet information is returned for these search results.
    	// If no options are specified, no facet results will be returned.
    	Facets []FacetSearchOption
    
    	// Refinements filters the returned documents by requiring them to contain facets
    	// with specific values. Refinements are applied in conjunction for facets with
    	// different names, and in disjunction otherwise.
    	Refinements []Facet
    
    	// Cursor causes the results to commence with the first document after
    	// the document associated with the cursor.
    	Cursor Cursor
    
    	// Offset specifies the number of documents to skip over before returning results.
    	// When specified, Cursor must be nil.
    	Offset [int](https://pkg.go.dev/builtin#int)
    
    	// CountAccuracy specifies the maximum result count that can be expected to
    	// be accurate. If zero, the count accuracy defaults to 20.
    	CountAccuracy [int](https://pkg.go.dev/builtin#int)
    }

SearchOptions are the options for searching an index. Passing a nil *SearchOptions is equivalent to using the default values.

## SortExpression
    
    
    type SortExpression struct {
    	// Expr is evaluated to provide a sorting value for each document.
    	// See https://cloud.google.com/appengine/docs/standard/go/search/options for
    	// the supported expression syntax.
    	Expr [string](https://pkg.go.dev/builtin#string)
    
    	// Reverse causes the documents to be sorted in ascending order.
    	Reverse [bool](https://pkg.go.dev/builtin#bool)
    
    	// The default value to use when no field is present or the expresion
    	// cannot be calculated for a document. For text sorts, Default must
    	// be of type string; for numeric sorts, float64.
    	Default interface{}
    }

SortExpression defines a single dimension for sorting a document.

## SortOptions
    
    
    type SortOptions struct {
    	// Expressions is a slice of expressions representing a multi-dimensional
    	// sort.
    	Expressions []SortExpression
    
    	// Scorer, when specified, will cause the documents to be scored according to
    	// search term frequency.
    	Scorer Scorer
    
    	// Limit is the maximum number of objects to score and/or sort. Limit cannot
    	// be more than 10,000. The zero value indicates a default limit.
    	Limit [int](https://pkg.go.dev/builtin#int)
    }

SortOptions control the ordering and scoring of search results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
