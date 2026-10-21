---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search
title: Package com.google.appengine.api.search (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:49:58.661461+00:00
---

# Package com.google.appengine.api.search (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.search (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides a service for indexing documents and retrieving them using search queries. This is a low-level API that allows users to directly create Documents which can be indexed and retrieved with the help of Index.

A Document is a collection of Fields. Each field is a named and typed value. A document is uniquely identified by its ID and may contain zero or more fields. A field with a given name can have multiple occurrences. Once documents are put into the Index, they can be retrieved via search queries. Typically, a program creates an index. This operation does nothing if the index was already created. Next, a number of documents are inserted into the index. Finally, index is searched and matching documents, or their snippets are returned to the user.
    
    
     public List<ScoredDocument> indexAndSearch(
         String query, Document... documents) {
         SearchService searchService = SearchServiceFactory.getSearchService();
         Index index = searchService.getIndex(
             IndexSpec.newBuilder().setIndexName("indexName"));
         for (Document document : documents) {
           PutResponse response = index.put(document);
           assert response.getResults().get(0).getCode().equals(StatusCode.OK);
         }
         Results<ScoredDocument> results =
             index.search(Query.newBuilder().build(query));
         List<ScoredDocument> matched = new ArrayList<ScoredDocument>(
             results.getNumberReturned());
         for (ScoredDocument result : results) {
           matched.add(result);
         }
         return matched;
     }
     

See Also: [com.google.appengine.api.search.SearchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceFactory)

## Classes 

### [AdminSearchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.AdminSearchServiceFactory)

Builds [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService) instances that are pinned to a specific application and namespace regardless of the "current" appId provided by `ApiProxy.getCurrentEnvironment().getAppId()` and the "current" namespace provided by `NamespaceManager.get()`. 

Note: users should not access this class directly.

### [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)

Represents a cursor on the set of results found for executing a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) during a search on the [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index). 

For example, the following code shows how to use a cursor to get the next page of results 
    
    
     Index index = ...
     Cursor cursor = Cursor.newBuilder().build();
     Query query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(cursor).build("some query"));
    
     // Get the first page of results
     Results<ScoredDocument> results = index.search(query);
    
     // process results
     ...
    
     // Get the next set of results from the returned cursor
     query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(
             results.getCursor()).build("some query"));
    
     results = index.search(query);
     

Alternatively, you can get a cursor to continue from each of the returned results.
    
    
     Cursor cursor =
         Cursor.newBuilder().setPerResult(true).build();
     Query query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(cursor).build("some query"));
    
     // Get the first page of results
     Results<ScoredDocument> results = index.search(query);
    
     // process results
     for (ScoredDocument result : results) {
       // choose a cursor from one of the results
       cursor = result.getCursor();
     }
    
     // Get the next set of results from the result's cursor
     query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(cursor).build("some query"));
    
     results = index.search(query);
     

### [Cursor.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor.Builder)

A builder which constructs Cursor objects.

### [DateUtil](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.DateUtil)

A utility class that centralizes processing of dates.

### [Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)

Represents a user generated document. The following example shows how to create a document consisting of a set of fields, some with plain text and some in HTML; it also adds facets to the document.
    
    
        Document document = Document.newBuilder().setId("document id")
           .setLocale(Locale.UK)
           .addField(Field.newBuilder()
               .setName("subject")
               .setText("going for dinner"))
           .addField(Field.newBuilder()
               .setName("body")
               .setHTML("I found a restaurant."))
           .addField(Field.newBuilder()
               .setName("signature")
               .setText("ten post jest przeznaczony dla odbiorcy")
               .setLocale(new Locale("pl")))
           .addFacet(Facet.withAtom("tag", "food"))
           .addFacet(Facet.withNumber("priority", 5.0))
           .build();
     

The following example shows how to access the fields within a document:
    
    
        Document document = ...
    
        for (Field field : document.getFields()) {
          switch (field.getType()) {
            case TEXT -> use(field.getText());
            case HTML -> use(field.getHtml());
            case ATOM -> use(field.getAtom());
            case DATE -> use(field.getDate());
          }
        }
     

And this example shows how to access the facets within a document:
    
    
        Document document = ...
    
        for (Facet facet : document.getFacets()) {
          switch (facet.getType()) {
            case ATOM -> use(facet.getAtom());
            case NUMBER -> use(facet.getNumber());
          }
        }
     

### [Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)

A builder of documents. This is not thread-safe.

### [Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet)

A `Facet` can be used to categorize a [Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document). It is not a [Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field). 

Search results can contain facets for the extended result set and their value frequency. For example, if a search query is related to "wine", then facets could be "color" with values of "red" and "white", and "year" with values of "2000" and "2005". 

Each facet has a name and exactly one value: atom or number. Facet name lengths are between 1 and [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_NAME_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NAME_LENGTH) characters, and atoms are limited to [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_ATOM_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_ATOM_LENGTH) characters. Numbers must be between [com.google.appengine.api.search.checkers.SearchApiLimits#MINIMUM_NUMBER_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MINIMUM_NUMBER_VALUE) and [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_NUMBER_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NUMBER_VALUE).

### [FacetOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions)

A `FacetOptions` represents facet options such as the number of facets to discover (`discoveryLimit`), the number of values to be included in each discovered facet (`discoveryValueLimit`), and the depth of the results to check (`depth`). Note that discovery is disabled when `discoveryLimit` is zero. 

For example, to discover 10 facets with 5 values each over 1000 extended results:
    
    
       FacetOptions facetOption = FacetOptions.newBuilder()
           .setDiscoverLimit(10)
           .setDiscoverValueLimit(5)
           .setDepth(1000)
           .build();
     

### [FacetOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions.Builder)

Builder for [FacetOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions).

### [FacetRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRange)

A FacetRange is a range with a start (inclusive) and an end (exclusive).

### [FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement)

A Facet Refinement to filter out search results based on a facet value. 

We recommend using refinement token strings instead of this class. We include a refinement token string with each [FacetResultValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResultValue) returned by the backend that can be passed to [Query.Builder#addFacetRefinementFromToken(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder#com_google_appengine_api_search_Query_Builder_addFacetRefinementFromToken_java_lang_String_) to refine follow-up queries. 

We also support manually-specified query refinements by passing an instance of this class to [Query.Builder#addFacetRefinement(FacetRefinement)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder#com_google_appengine_api_search_Query_Builder_addFacetRefinement_com_google_appengine_api_search_FacetRefinement_). 

Example: Request to only return documents that have a number facet named "rating" with a value between one and two:
    
    
     FacetRefinement lowRating = FacetRefinement.withRange("rating", FacetRange.startEnd(1.0, 2.0));
     query.addFacetRefinement(lowRating);
     

### [FacetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest)

A facet request representing parameters for requesting specific facets to be returned with a query result.

For example, to request a facet with a name and specific values:
    
    
       FacetRequest request = FacetRequest.newBuilder().setName("wine_type")
           .addValueConstraint("white").addValueConstraint("red").build();
      

and to request ranges:
    
    
     FacetRequest request = FacetRequest.newBuilder().setName("year")
         .addRange(null, 2000.0)           // year < 2000.0="" .addrange(1980.0,="" 2000.0)="" 1980.0=""><= year="">< 2000.0="" .addrange(2000.0,="" null).build();="" year="">= 2000.0
     

### [FacetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest.Builder)

A facet request builder. Each facet request should at least have the `name` of the facet. It can also includes number of values, a list of constraints on the values or a list of ranges for numeric facets. Note that the list of constraints and the list of ranges are mutually exclusive, i.e. you can specify one of them but not both.

### [FacetResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResult)

Represents a facet result computed from an extended search result set. A facet result contains a name, a type, and a set of values. Name is a single facet name and each value has a label and a count. The value label can be a single facet value name, or a range label (in "[start,end)" format).

### [FacetResult.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResult.Builder)

A builder of facet result. This is not thread-safe.

### [FacetResultValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResultValue)

Represents a single facet result value. The value has a label, a count, and a refinementToken.

### [Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field)

Represents a field of a [Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document), which is a name, an optional locale, and at most one value: text, HTML, atom, date, GeoPoint, untokenizedPrefix, tokenizedPrefix or vector. Field name lengths are between 1 and [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_NAME_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NAME_LENGTH) characters, and text and HTML values are limited to [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_TEXT_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_TEXT_LENGTH). Atoms are limited to [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_ATOM_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_ATOM_LENGTH) characters, both prefix types are limited to [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_PREFIX_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_PREFIX_LENGTH) . Vector field size is limited to [com.google.appengine.api.search.checkers.SearchApiLimits#VECTOR_FIELD_MAX_SIZE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_VECTOR_FIELD_MAX_SIZE) and dates must not have a time component.

There are 5 types of text fields, ATOM, TEXT, HTML, UNTOKENIZED_PREFIX, and TOKENIZED_PREFIX. Atom fields when queried, are checked for equality. For example, if you add a field with name `code` and an ATOM value of "928A 33B-1", then query `code:"928A 33B-1"` would match the document with this field, while query `code:928A` would not. TEXT fields, unlike ATOM, match both on equality or if any token extracted from the original field matches. Thus if `code` field had the value set with [Field.Builder#setText(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder#com_google_appengine_api_search_Field_Builder_setText_java_lang_String_) method, both queries would match. HTML fields have HTML tags stripped before tokenization. Untokenized prefix fields match queries that are prefixes containing the contiguous starting characters of the whole field. For example if the field was "the quick brown fox", the query "the qui" would match whereas "th qui" would not. On the other hand, Tokenized prefix fields match if the query terms are prefixes of individual terms in the field. If the query is a phrase of terms, the ordering of the terms will matter. For example if the field is "the quick brown fox", the query "th qui bro" would match whereas "bro qui the" would not. Vector fields are only used to compute the dot product between a given constant vector and the provided vector field for sorting and field expressions only. for example, if a 3d vector is named "scores" and has a value of (1,2,3) then the expression `dot(scores, vector(3,2,1))` will be evaluated to 10.

### [Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)

A field builder. Fields must have a name, and optionally a locale and at most one of text, html, atom or date.

### [FieldExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FieldExpression)

Represents an expression bound to a returned Field with the given name. FieldExpressions are added to a [QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions), to request an expression computed and returned as the named Field value. For example,
    
    
       FieldExpression.newBuilder()
           .setName("snippet")
           .setExpression("snippet("good story", content)")
           .build()
     

binds a snippet expression to a Field named "snippet", which will be returned in each search result. In this case the returned "snippet" Field will contain a HTML value containing text snippets of the "content" field matching the query "good story".

### [FieldExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FieldExpression.Builder)

A field expression builder. A name and expression must be supplied.

### [GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GeoPoint)

Represents a point on the Earth's surface, in latitude and longitude coordinates.

### [GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest)

A request to get a range of indexes. You can specify a number of restrictions, such as the number of indexes to return, the prefix with which names of the returned indexes must begin, etc.

A namespace may be specified, otherwise the default namespace will be used. Only the indexes defined in the namespace, default or otherwise, will be returned.
    
    
       GetIndexesRequest request = GetIndexesRequest.newBuilder()
           .setIndexNamePrefix("a")
           .setOffset(100)
           .setLimit(10)
           .build();
     

### [GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)

The builder of [GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest)s.

### [GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest)

A request to list objects in an index. You can specify a number of restrictions, such as the number of objects to return, the id of the first object to return, whether to only return keys, etc.
    
    
       GetRequest request = GetRequest.newBuilder()
           .setLimit(500)
           .setStartId("some-id")
           .setReturningIdsOnly(true)
           .build();
     

### [GetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder)

The builder of [GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest)s.

### [GetResponse<T>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)

Represents a result of executing a [GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest). The response contains a list of T.

### [ISearchServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ISearchServiceFactoryProvider)

Factory provider for [ISearchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ISearchServiceFactory).

**Note:** This class is not intended for end users.

### [IndexSpec](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.IndexSpec)

Represents information about an index. This class is used to fully specify the index you want to retrieve from the [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService). To build an instance use the [#newBuilder()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.IndexSpec#com_google_appengine_api_search_IndexSpec_newBuilder__) method and set all required parameters, plus optional values different than the defaults.
    
    
       SearchService searchService = SearchServiceFactory.getSearchService();
    
       IndexSpec spec = IndexSpec.newBuilder()
           .setName("docs")
           .build();
    
       Index index = searchService.getIndex(spec);
     
     

### [IndexSpec.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.IndexSpec.Builder)

A builder of IndexSpec.

### [MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer)

Assigns a document score based on frequency of terms in TextFields and HTMLFields.

If you add a MatchScorer to a SortOptions as in the following code:
    
    
      SortOptions sortOptions = SortOptions.newBuilder()
          .setMatchScorer(MatchScorer.newBuilder())
          .build();
     

then this will sort the documents in descending score order. The scores will be positive. If you want to sort in ascending order, then use the following code:
    
    
       SortOptions sortOptions = SortOptions.newBuilder()
           .setMatchScorer(MatchScorer.newBuilder())
           .addSortExpression(
               SortExpression.newBuilder()
                   .setExpression(SortExpression.SCORE_FIELD_NAME)
                   .setDirection(SortExpression.SortDirection.ASCENDING)
                   .setDefaultValueNumeric(0.0))
           .build();
     

In this example, the score will be negative.

### [MatchScorer.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer.Builder)

A builder that constructs [MatchScorers](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer). A MatchScorer will invoke a scorer on each search result. The following code illustrates building a match scorer to score documents: 
    
    
       MatchScorer scorer = MatchScorer.newBuilder().build();
     

### [OperationResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.OperationResult)

The result of an operation involving the search service.

### [PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse)

Represents a result of putting a list of objects (documents or queries) into an index. The response contains a list of [OperationResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.OperationResult) indicating success or not of putting each of the objects into the index, and a list of Id of the objects which are those given in the request or allocated by the search service to those objects which do not have an Id supplied.

### [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\))

A query to search an index for documents which match, restricting the document fields returned to those given, and scoring and sorting the results, whilst supporting pagination. 

For example, the following query will search for documents where the tokens 'good' and 'story' occur in some fields, returns up to 20 results including the fields 'author' and 'date-sent' as well as snippeted fields 'subject' and 'body'. The results are sorted by 'author' in descending order, getting the next 20 results from the responseCursor in the previously returned results, giving back a single cursor in the [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) to get the next batch of results after this. 
    
    
     QueryOptions options = QueryOptions.newBuilder()
         .setLimit(20)
         .setFieldsToSnippet("subject", "body")
         .setScorer(CustomScorer.newBuilder()
             .addSortExpression(SortExpression.newBuilder()
                 .setExpression("author")
                 .setDirection(SortDirection.DESCENDING)
                 .setDefaultValue("")))
         .setCursor(responseCursor)
         .build();
     Query query = Query.newBuilder()
         .setOptions(options)
         .build("good story");
     
     

The following query will return facet information with the query result:

Query query = Query.newBuilder() .setOptions(options) .setEnableFacetDiscovery(true) .build("tablet");

To customize returned facet or refine the result using a previously returned [FacetResultValue#getRefinementToken](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResultValue#com_google_appengine_api_search_FacetResultValue_getRefinementToken_):

Query query = Query.newBuilder() .setOptions(options) .setEnableFacetDiscovery(true) .setFacetOptions(FacetOptions.newBuilder().setDiscoveryLimit(5).build()) .addReturnFacet("shipping") .addReturnFacet(FacetRequest.newBuilder().setName("department") .addValueConstraint("Computers") .addValueConstraint("Electronics") .build()) .addRefinementToken(refinementToken1) .addRefinementToken(refinementToken2) .build("tablet");

### [Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)

A builder which constructs Query objects.

### [QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions)

Represents options which control where and what in the search results to return, from restricting the document fields returned to those given, and scoring and sorting the results, whilst supporting pagination.

For example, the following options will return documents from search results for some given query, returning up to 20 results including the fields 'author' and 'date-sent' as well as snippeted fields 'subject' and 'body'. The results are sorted by 'author' in descending order, getting the next 20 results from the responseCursor in the previously returned results, giving back a single cursor in the [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) to get the next batch of results after this.
    
    
     QueryOptions request = QueryOptions.newBuilder()
          .setLimit(20)
          .setFieldsToReturn("author", "date-sent")
          .setFieldsToSnippet("subject", "body")
          .setSortOptions(SortOptions.newBuilder().
              .addSortExpression(SortExpression.newBuilder()
                  .setExpression("author")
                  .setDirection(SortExpression.SortDirection.DESCENDING)
                  .setDefaultValue("")))
    
          .setCursor(Cursor.newBuilder().build())
          .build();
     

### [QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)

A builder which constructs QueryOptions objects.

### [RequestStatusUtil](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RequestStatusUtil)

Collection of utility methods for SearchServicePb.RequestStatus.

### [RescoringMatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer)

Assigns a document score based on term frequency weighted on document parts.

If you add a MatchScorer to a SortOptions as in the following code:
    
    
      SortOptions sortOptions = SortOptions.newBuilder()
          .setMatchScorer(RescoringMatchScorer.newBuilder())
          .build();
     

then this will sort the documents in descending score order. The scores will be positive. If you want to sort in ascending order, then use the following code:
    
    
       SortOptions sortOptions = SortOptions.newBuilder()
           .setMatchScorer(RescoringMatchScorer.newBuilder())
           .addSortExpression(
               SortExpression.newBuilder()
                   .setExpression(SortExpression.SCORE_FIELD_NAME)
                   .setDirection(SortExpression.SortDirection.ASCENDING)
                   .setDefaultValueNumeric(0.0))
           .build();
     

The scores in this case will be negative.

### [RescoringMatchScorer.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer.Builder)

A builder that constructs [RescoringMatchScorers](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer). A RescoringMatchScorer will invoke a scorer on each search result. The following code illustrates building a rescoring match scorer to score documents: 

RescoringMatchScorer scorer = RescoringMatchScorer.newBuilder().build();

### [Results<T>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)

Represents a result of executing a search. The Results include an [OperationResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.OperationResult), a collection of results, and a number of found and returned results.

### [Schema](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Schema)

Contains information about the kinds of document [Fields](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field) which are supported by the [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index). 
    
    
       // Get the searchService for the default namespace
       SearchService searchService = SearchServiceFactory.getSearchService();
    
       // Get the first page of indexes available and retrieve schemas
       GetResponse<Index> response = searchService.getIndexes(
           GetIndexesRequest.newBuilder().setSchemaFetched(true).build());
    
       // List out elements of Schema
       for (Index index : response) {
         Schema schema = index.getSchema();
         for (String fieldName : schema.getFieldNames()) {
            List<FieldType> typesForField = schema.getFieldTypes(fieldName);
         }
       }
     

### [Schema.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Schema.Builder)

A builder which constructs Schema objects.

### [ScoredDocument](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument)

Represents a document which may have been scored, possibly some computed expression fields, and a cursor to continue the search from.

### [ScoredDocument.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument.Builder)

A builder of scored documents. This is not thread-safe.

### [SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig)

Configuration options for Search API.

### [SearchServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig.Builder)

Builder for [SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig).

### [SearchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceFactory)

An factory that creates default implementation of [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService).
    
    
       SearchService search = SearchServiceFactory.getSearchService();
     

Optionally, you may pass a [SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig) instance to customize the search service. e.g, setting deadline and namespace:
    
    
       SearchServiceFactory.getSearchService(
           SearchServiceConfig.newBuilder().setDeadline(10.0).setNamespace("acme").build())
     

### [SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression)

Sorting specification for a single dimension. Multi-dimensional sorting is supported by a collection of SortExpressions.

### [SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)

A builder that constructs [SortExpressions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression). The user must provide an expression. The expression can be as simple as a field name, or can be some other expression such as `"score + count(likes) * 0.1"`, which combines a scorer score with a count of the number of likes values times 0.1. A default value must be specified for the expression. 
    
    
       SortExpression expr = SortExpression.newBuilder()
           .setExpression(String.format(
               "%s + count(likes) * 0.1", SortExpression.SCORE_FIELD_NAME))
           .setDirection(SortExpression.SortDirection.ASCENDING)
           .setDefaultValueNumeric(0.0)
           .build()
     

### [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions)

Definition of how to sort documents. You may specify zero or more sort expressions and set a match scorer. If you have a large index, it is advisable to set a limit.

### [SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)

A builder that constructs [SortOptionss](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions). A SortOptions will evaluate each of the [SortExpressions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression) on each search result and apply a sort order with priority given to the sort expressions from left to right. The following code illustrates creating a SortOptions specification to sort documents based on decreasing product rating and then within rating showing cheapest products based on price plus tax, sorting at most 2000 documents. 
    
    
       SortOptions sortOptions = SortOptions.newBuilder()
           .addSortExpression(SortExpression.newBuilder()
               .setExpression("rating")
               .setDirection(SortExpression.SortDirection.DESCENDING)
               .setDefaultValueNumeric(0))
           .addSortExpression(SortExpression.newBuilder()
               .setExpression("price + tax")
               .setDirection(SortExpression.SortDirection.ASCENDING)
               .setDefaultValueNumeric(99999999.00))
           .setLimit(1000)
           .build();
     

The following code fragment shows how the score from a [MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer) can be used in an expression that combines the score with one thousandth of an "importance" field. At most 1000 documents are scored and sorted.
    
    
       SortOptions sortOptions = SortOptions.newBuilder()
           .setMatchScorer(MatchScorer.newBuilder())
           .addSortExpression(SortExpression.newBuilder()
               .setExpression(String.format(
                   "%s + (importance * .001)", SortExpression.SCORE_FIELD_NAME))
               .setDirection(SortExpression.SortDirection.DESCENDING)
               .setDefaultValueNumeric(0))
           .setLimit(1000)
           .build();
     

## Interfaces 

### [ISearchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ISearchServiceFactory)

A factory that creates default implementation of [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService).

### [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index)

An Index allows synchronous and asynchronous adding and deleting of [Documents](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document) as well as synchronous and asynchronous searching for Documents for a given [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)). The following code fragment shows how to add documents, then search the index for documents matching a query.
    
    
      // Get the SearchService for the default namespace
      SearchService searchService = SearchServiceFactory.getSearchService();
      // Get the index. If not yet created, create it.
      Index index = searchService.getIndex(
          IndexSpec.newBuilder().setIndexName("indexName"));
    
      // Create a document.
      Document document = Document.newBuilder()
          .setId("documentId")
          .addField(Field.newBuilder().setName("subject").setText("my first email"))
          .addField(Field.newBuilder().setName("body")
               .setHTML(some content here")
          .build();
    
      // Put the document.
      try {
        index.put(document);
      } catch (PutException e) {
        if (StatusCode.TRANSIENT_ERROR.equals(e.getOperationResult().getCode())) {
          // retry putting document
        }
      }
    
      // Query the index.
      try {
        Results<ScoredDocument> results =
            index.search(Query.newBuilder().build("subject:first body:here"));
    
        // Iterate through the search results.
        for (ScoredDocument document : results) {
          // display results
        }
      } catch (SearchException e) {
        if (StatusCode.TRANSIENT_ERROR.equals(e.getOperationResult().getCode())) {
          // retry
        }
      }
     
     

### [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService)

The SearchService is used to get available indexes, which can be queried about their metadata or have index/delete/search operations performed on them. For example:
    
    
     SearchService searchService = SearchServiceFactory.getSearchService();
     GetResponse<Index> response = searchService.getIndexes(
         GetIndexesRequest.newBuilder());
     for (Index index : response) {
       index.getName();
       index.getNamespace();
       index.search("query");
     }
     

SearchService is also responsible for creating new indexes. For example:
    
    
     SearchService searchService = SearchServiceFactory.getSearchService();
     Index index = searchService.getIndex(IndexSpec.newBuilder().setName("myindex"));
     

## Enums 

### [Field.FieldType](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.FieldType)

The type of the field value.

### [SortExpression.SortDirection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.SortDirection)

The direction search results are sorted by, either ascending or descending.

### [StatusCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.StatusCode)

Status code returned by various index operations.

## Exceptions 

### [DeleteException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.DeleteException)

Thrown to indicate that a search service failure occurred while deleting objects.

### [GetException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetException)

Thrown to indicate that a search service failure occurred while performing a request to get requested objects.

### [PutException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutException)

Thrown to indicate that a search service failure occurred while putting objects into the index.

### [SearchBaseException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchBaseException)

Thrown to indicate that a search service failure occurred.

### [SearchException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchException)

Thrown to indicate that a search service failure occurred while performing a search request.

### [SearchQueryException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchQueryException)

Thrown to indicate that a search query was invalid.

### [SearchServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceException)

Thrown to indicate that a search service failure occurred.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
