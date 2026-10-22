---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/facet-search/
title: Faceted search \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:57.310986+00:00
---

# Faceted search  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/facet-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Faceted search Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Faceted search gives you the ability to attach categorical information to your documents. A facet is an attribute/value pair. For example, the facet named "size" might have values "small", "medium", and "large."

By using facets with search, you can retrieve summary information to help you refine a query and "drill down" into your results in a series of steps.

This is useful for applications like shopping sites, where you intend to offer a set of filters for customers to narrow down the products that they want to see.

The aggregated data for a facet shows you how a facet's values are distributed. For instance, the facet "size" may appear in many of the documents in your result set. The aggregated data for that facet might show that the value "small" appeared 100 times, "medium" 300 times, and "large" 250 times. Each facet/value pair represents a subset of documents in the query result. A key, called a _refinement_ , is associated with each pair. You can include refinements in a query to retrieve documents that match the query string and that have the facet values corresponding to one or more refinements.

When you perform a search, you can choose which facets to collect and show with the results, or you can enable facet discovery to automatically select the facets that appear most often in your documents.

## Adding facets to a document

Add facets to a document before you add the document to an index. Do this at the same time you specify the document's fields:
    
    
    def add_faceted_document(index):
        document = search.Document(
            doc_id="doc1",
            fields=[search.AtomField(name="name", value="x86")],
            facets=[
                search.AtomFacet(name="type", value="computer"),
                search.NumberFacet(name="ram_size_gb", value=8),
            ],
        )
    
        index.put(document)

A facet is similar to a document field; it has a name, and takes one value.

Facet names follow the same rules as document fields: Names are case sensitive and can only contain ASCII characters. They must start with a letter and can contain letters, digits, or underscore. A name cannot be longer than 500 characters.

The value of a facet can be either an atomic string (no longer than 500 characters) or a number (a double precision floating point value between -2,147,483,647 and 2,147,483,647).

You can assign multiple values to a facet on one document by adding a facet with the same name and type many times, using a different value each time.

There is no limit to the number of values a facet can have. There is also no limit to the number of facets that you can add to a document or the number of uniquely-named facets in an index.

Note that each time you use a facet, it can take either an atomic or numeric value. A facet with the name "size" can be attached to one document with the string value "small" and another document with the numeric value 8. In fact, the same facet can appear multiple times on the same document with both kinds of values. We do not recommend using both atom and number values for the same facet, even though it is allowed.

While a facet has a specific type when you add it to a document, the search results gather _all_ of its values together. For example, the results for facet "size" might show that there were 100 instances of the value "small", 150 instances of "medium", and 135 instances of numeric values in the range [4, 8). The exact numeric values and their frequency distribution are not shown.

When you retrieve a document using a query, you cannot directly access its facets and values. You must request that facet information be returned with your query, as explained in the next section.

## Using a faceted search to retrieve facet information

You can ask the search backend to discover the most frequently used facets for you. This is called automatic facet discovery. You can also retrieve facet information explicitly by selecting a facet by name, or by name and value. You can mix and match all three kinds of facet retrieval in a single query.

Asking for facet information will not affect the documents your query returns. It can affect performance. Performing a faceted search with the default depth of 1000 has the same effect as setting the sort options scorer limit to 1000.

### Automatic facet discovery

Automatic facet discovery looks for the facets that appear most often _in the aggregate_ in your documents. For example, suppose the documents matching your query include a "color" facet that appears 5 times with the value "red", 5 times with the value "white", and 5 times with the color "blue". This facet has a total count of 15. For the purposes of discovery, it would be ranked higher than another facet "shade" that appears in the same matching documents 6 times with the value "dark" and 7 times with the value "light".

You must enable facet discovery by setting it in your Query:
    
    
    def facet_discovery(index):
        # Create the query and enable facet discovery.
        query = search.Query("name:x86", enable_facet_discovery=True)
        results = index.search(query)
    
        for facet in results.facets:
            print("facet {}.".format(facet.name))
            for value in facet.values:
                print(
                    "{}: count={}, refinement_token={}".format(
                        value.label, value.count, value.refinement_token
                    )
                )

When you retrieve facets by discovery, by default only the 10 most often occurring values for a facet will be returned.

You can increase this limit up to 100 using the `FacetOptions` `discovery_limit` parameter.

Note that automatic facet discovery is not meant to return all possible facets and their values. Facets returned from discovery may vary from run to run. If a fixed set of facets is desired, use a `return_facets` parameter on your query.

String values will be returned individually. The numeric values of a discovered facet are returned in a single range [min max). You can examine this range and create a smaller subrange for a later query.

### Selecting facets by name

To retrieve information about a facet by its name only, add a `return_facets` parameter to your query, including the facet name in the list:
    
    
    def facet_by_name(index):
        # Create the query and specify to only return the "type" and "ram_size_gb"
        # facets.
        query = search.Query("name:x86", return_facets=["type", "ram_size_gb"])
        results = index.search(query)
    
        for facet in results.facets:
            print("facet {}".format(facet.name))
            for value in facet.values:
                print(
                    "{}: count={}, refinement_token={}".format(
                        value.label, value.count, value.refinement_token
                    )
                )

When you retrieve facets by name, by default only the 10 most often occurring values for a facet will be returned.

You can increase this limit up to 20 using the `FacetOptions` `discovery_value_limit` parameter.

### Selecting facets by name and value

To retrieve information only about particular values of a facet, add a `return_facets` parameter that includes a `FacetRequest` object with a values list:
    
    
    def facet_by_name_and_value(index):
        # Create the query and specify to return the "type" facet with values
        # "computer" and "printer" and the "ram_size_gb" facet with value in the
        # ranges [0,4), [4, 8), and [8, max].
        query = search.Query(
            "name:x86",
            return_facets=[
                search.FacetRequest("type", values=["computer", "printer"]),
                search.FacetRequest(
                    "ram_size_gb",
                    ranges=[
                        search.FacetRange(end=4),
                        search.FacetRange(start=4, end=8),
                        search.FacetRange(start=8),
                    ],
                ),
            ],
        )
    
        results = index.search(query)
        for facet in results.facets:
            print("facet {}".format(facet.name))
            for value in facet.values:
                print(
                    "{}: count={}, refinement_token={}".format(
                        value.label, value.count, value.refinement_token
                    )
                )

The values in a single `FacetRequest` must all be the same type, either a list of string values or, for numbers, a list of `FacetRanges`, which are intervals that are closed on the left (start), and open on the right (end). If your facet has a mix of string and number values, add separate `FacetRequests` for each.

### Options

You can control faceted search by adding the `facet_options` parameter to a Query call. This parameter takes a single instance of `FacetOptions`. Use this parameter to override the default behavior of faceted search.
    
    
    options = FacetOptions(discover_facet_limit=5,
                           discover_facet_value_limit=10,
                           depth=6000);
    

Parameter | Description | Default  
---|---|---  
`discover_facet_limit` | Number of facets to discover if facet discovery is turned on. If 0, facet discovery will be disabled. | 10  
`discover_facet_value_limit` | Number of values to be returned for each of the top discovered facets. | 10  
`depth` | The minimum number of documents in query results to evaluate to gather facet information. | 1000  
  
The `depth` option applies to all three kinds of facet aggregation: by name, name and value, and auto-discovery. The other options are for auto-discovery only.

Note that facet depth is usually much greater than the query limit. Facet results are computed to at least the depth number of documents.

If you have set the sort options scoring limit higher than depth, than the scoring limit will be used instead.

## Retrieving facet results

When you use faceted search parameters in a query, the aggregated facet information comes with the query result itself.

A query will have a list of `FacetResult`. There will be one result in the list for each facet that appeared in a document that matched your query. For each result, you'll get:

  * The facet name
  * A list of the most frequent values for the facet. For each value there is an approximate count of how many times it appeared and a refinement key that can be used to retrieve the documents that match this query and facet value.



Note that the values list will include a facet's string _and_ numeric values. If the facet was auto-discovered, its numeric values are returned as a single interval [min max). If you explicitly asked for a numeric facet with one or more ranges in your query, the list will contain one closed-open interval [start end) for each range.

The list of facet values might not include all of the values found in your documents, since query options determine how many documents to examine and how many values to return.

The aggregated information for each facet can be read from the search results:
    
    
    query = search.Query(...)
    results = index.search(query)
    for facet_info in results.facets:
      ...
    

For example, a query may have found documents that included a "size" facet with the string values and numeric values. The FacetResult for this facet will be constructed like this:
    
    
    FacetResult(name='size', values=[
      FacetResultValue(label='[8, 10)', 22, refinement=refinement_key),
      FacetResultValue(label='small', 100, refinement=refinement_key),
      FacetResultValue(label='medium', 300, refinement=refinement_key),
      FacetResultValue(label='large', 250, refinement=refinement_key)])
    

The `label` parameter is constructed from a facet value. For numeric values `label` is the representation of a range.

The `refinement_key` is a web/url safe string that can be used in a later query to retrieve the documents matching that result's facet name and value.

## Using facets to refine/filter a query

The refinement associated with each `FacetResultValue` can be used to further narrow your results to include only documents that have those facet values. To refine queries with one or more of these keys, pass them to the query object:
    
    
    query = search.Query(..., facet_refinements=[refinement_key1, refinement_key2, refinement_key3])
    

You can combine refinements for one or more different facets in the same request. All the refinements belonging to the same facet are joined with an OR. Refinements for different facets are combined with AND.

It is also possible to create a custom `FacetRefinement` key by hand. Please see the class documentation for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
