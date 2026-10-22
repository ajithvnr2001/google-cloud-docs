---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/projectionqueries/
title: Project queries \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:02.962989+00:00
---

# Project queries  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/projectionqueries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Project queries Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Most Datastore [queries](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/queries) return whole [entities](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/entities) as their results, but often an application is actually interested in only a few of the entity's properties. _Projection queries_ allow you to query Datastore for just those specific properties of an entity that you actually need, at lower latency and cost than retrieving the entire entity.

Projection queries are similar to SQL queries of the form:
    
    
    SELECT name, email, phone FROM CUSTOMER
    

You can use all of the filtering and sorting features available for standard entity queries, subject to the limitations described below. The query returns abridged results with only the specified properties (`name`, `email`, and `phone` in the example) populated with values; all other properties have no data.

## Using projection queries

Consider the following model: 
    
    
    class Article(ndb.Model):
        title = ndb.StringProperty()
        author = ndb.StringProperty()
        tags = ndb.StringProperty(repeated=True)

You specify a projection this way:
    
    
    def print_author_tags():
        query = Article.query()
        articles = query.fetch(20, projection=[Article.author, Article.tags])
        for article in articles:
            print(article.author)
            print(article.tags)
            # article.title will raise a ndb.UnprojectedPropertyError

You handle the results of these queries just as you would for a standard entity query: for example, by iterating over the results.
    
    
    for article in articles:
            print(article.author)
            print(article.tags)
            # article.title will raise a ndb.UnprojectedPropertyError
    
    

You can project indexed sub-properties from a structured property. To get only the `city` property of a contact's `address` structured property, you could use a projection like:
    
    
    class Address(ndb.Model):
        type = ndb.StringProperty()  # E.g., 'home', 'work'
        street = ndb.StringProperty()
        city = ndb.StringProperty()

`...`
    
    
    class Contact(ndb.Model):
        name = ndb.StringProperty()
        addresses = ndb.StructuredProperty(Address, repeated=True)

`...`
    
    
    Contact.query().fetch(projection=["name", "addresses.city"])
    Contact.query().fetch(projection=[Contact.name, Contact.addresses.city])

## Grouping(experimental)

Projection queries can use the `distinct` keyword to ensure that only completely unique results will be returned in a result set. This will only return the first result for entities which have the same values for the properties that are being projected.
    
    
    Article.query(projection=[Article.author], group_by=[Article.author])
    Article.query(projection=[Article.author], distinct=True)

Both queries are equivalent and will produce each author's name only once. 

## Limitations on projections

Projection queries are subject to the following limitations:

  * **Only indexed properties can be projected.**

Projection is not supported for properties that are not indexed, whether explicitly or implicitly. Long text strings ([`Text`](https://docs.cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference#types)) and long byte strings ([`Blob`](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference#types)) are not indexed. 

  * **The same property cannot be projected more than once.**

  * **Properties referenced in an equality (`=`) or membership (`IN`) filter cannot be projected.**

For example,
        
        SELECT A FROM kind WHERE B = 1
        

is valid (projected property not used in the equality filter), as is
        
        SELECT A FROM kind WHERE A > 1
        

(not an equality filter), but
        
        SELECT A FROM kind WHERE A = 1
        

(projected property used in equality filter) is not.

  * **Results returned by a projection query cannot be saved back to Datastore.**

Because the query returns results that are only partially populated, you cannot write them back to Datastore.




## Projections and multiple-valued properties

Projecting a property with multiple values will not populate all values for that property. Instead, a separate entity will be returned for each unique combination of projected values matching the query. For example, suppose you have an entity of kind `Foo` with two multiple-valued properties, `A` and `B`:
    
    
    entity = Foo(A=[1, 1, 2, 3], B=['x', 'y', 'x'])

Then the projection query
    
    
    SELECT A, B FROM Foo WHERE A < 3
    

will return four entities with the following combinations of values:

`A` = `1`, `B` = `'x'`  
`A` = `1`, `B` = `'y'`  
`A` = `2`, `B` = `'x'`  
`A` = `2`, `B` = `'y'`

Note that if an entity has a multiple-valued property with no values, no entries will be included in the index, and no results for that entity will be returned from a projection query including that property.

**Warning:** Including more than one multiple-valued property in a projection will result in an [exploding index](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/indexes#index-limits).

## Indexes for projections

Projection queries require all properties specified in the projection to be included in a Datastore [index](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/indexes). The App Engine development server automatically generates the needed indexes for you in the index configuration file, `index.yaml`, which is uploaded with your application.

One way to minimize the number of indexes required is to project the same properties consistently, even when not all of them are always needed. For example, these queries require two separate indexes:
    
    
    SELECT A, B FROM Kind
    SELECT A, B, C FROM Kind
    

However, if you always project properties `A`, `B`, and `C`, even when `C` is not required, only one index will be needed.

Converting an existing query into a projection query may require building a new index if the properties in the projection are not already included in another part of the query. For example, suppose you had an existing query like
    
    
    SELECT * FROM Kind WHERE A > 1 ORDER BY A, B
    

which requires the index
    
    
    Index(Kind, A, B)
    

Converting this to either of the projection queries
    
    
    SELECT C FROM Kind WHERE A > 1 ORDER BY A, B
    SELECT A, B, C FROM Kind WHERE A > 1 ORDER BY A, B
    

introduces a new property (`C`) and thus will require building a new index `Index(Kind,` `A,` `B,` `C)`. Note that the projection query
    
    
    SELECT A, B FROM Kind WHERE A > 1 ORDER BY A, B
    

would _not_ change the required index, since the projected properties `A` and `B` were already included in the existing query.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
