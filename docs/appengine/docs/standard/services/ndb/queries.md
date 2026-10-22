---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries/
title: NDB Queries \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:52.905056+00:00
---

# NDB Queries  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Queries Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

An application can use queries to search the Datastore for entities that match specific search criteria called filters.

## Overview

An application can use queries to search the Datastore for entities that match specific search criteria called filters. For example, an application that keeps track of several guestbooks could use a query to retrieve messages from one guestbook, ordered by date:
    
    
    from google.appengine.ext import ndb

`...`
    
    
    class Greeting(ndb.Model):
        """Models an individual Guestbook entry with content and date."""
        content = ndb.StringProperty()
        date = ndb.DateTimeProperty(auto_now_add=True)
    
        @classmethod
        def query_book(cls, ancestor_key):
            return cls.query(ancestor=ancestor_key).order(-cls.date)

Some queries are more complex than others; the datastore needs pre-built indexes for these. These pre-built indexes are specified in a configuration file, `index.yaml`. On the development server, if you run a query that needs an index that you haven't specified, the development server automatically adds it to its `index.yaml`. But in your web site, a query that needs a not-yet-specified index fails. Thus, the typical development cycle is to try a new query on the development server and then update the web site to use the automatically-changed `index.yaml`. You can update `index.yaml` separately from uploading the application by running `gcloud app deploy index.yaml`. If your datastore has many entities, it takes a long time to create a new index for them; in this case, it's wise to update the index definitions before uploading code that uses the new index. You can use the Administration Console to find out when the indexes have finished building. 

The App Engine Datastore natively supports filters for exact matches (the == operator) and comparisons (the <, <=, > and >= operators). It supports combining multiple filters using a Boolean `AND` operation, with some limitations (see below). 

In addition to the native operators, the API supports the `!=` operator, combining groups of filters using the Boolean `OR` operation, and the `IN` operation, which test for equality to one of a list of possible values (like Python's 'in' operator). These operations don't map 1:1 to the Datastore's native operations; thus they are a little quirky and slow, relatively. They are implemented using in-memory merging of result streams. Note that `p != v` is implemented as "p < v OR p > v". (This matters for repeated properties.) 

**Limitations:** The Datastore enforces some restrictions on queries. Violating these will cause it to raise exceptions. For example, combining too many filters, using inequalities for multiple properties, or combining an inequality with a sort order on a different property are all currently disallowed. Also filters referencing multiple properties sometimes require secondary indexes to be configured. 

**Unsupported:** The Datastore does not directly support substring matches, case-insensitive matches, or so-called full-text search. There are ways to implement case-insensitive matches and even full-text search using computed properties. 

## Filtering by Property Values

Recall the **Account** class from [NDB Properties](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference): 
    
    
    class Account(ndb.Model):
        username = ndb.StringProperty()
        userid = ndb.IntegerProperty()
        email = ndb.StringProperty()

Usually you don't want to retrieve _all_ entities of a given kind; you want only those with a specific value or range of values for some property. 

Property objects overload some operators to return filter expressions that can be used to control a query: for example, to find all Account entities whose userid property has the exact value 42, you can use the expression 
    
    
    query = Account.query(Account.userid == 42)

(If you are sure that there was just one `Account` with that `userid`, you might prefer to use `userid` as a key. `Account.[get_by_id](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass#Model_get_by_id)(...)` is faster than `Account.query(...).get()`.) 

NDB supports these operations: 

`property == value  
property < value  
property <= value  
property > value  
property >= value  
property != value  
property.IN([value1, value2])`

To filter for an inequality, you can use syntax like the following: 
    
    
    query = Account.query(Account.userid >= 40)

This finds all Account entities whose `userid` property is greater than or equal to 40. 

Two of these operations, != and IN, are implemented as combinations of the others, and are a little quirky as described in != and IN. 

You can specify multiple filters: 
    
    
    query = Account.query(Account.userid >= 40, Account.userid < 50)

This combines the specified filter arguments, returning all Account entities whose userid value is greater than or equal to 40 and less than 50. 

**Note:** As mentioned earlier, the Datastore rejects queries using inequality filtering on more than one property. 

Instead of specifying an entire query filter in a single expression, you may find it more convenient to build it up in steps: for example: 
    
    
    query1 = Account.query()  # Retrieve all Account entitites
    query2 = query1.filter(Account.userid >= 40)  # Filter on userid >= 40
    query3 = query2.filter(Account.userid < 50)  # Filter on userid < 50 too

`query3` is equivalent to the `query` variable from the previous example. Note that query objects are immutable, so the construction of `query2` does not affect `query1` and the construction of `query3` does not affect `query1` or `query2`. 

## The != and IN Operations

Recall the **Article** class from [NDB Properties](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference): 
    
    
    class Article(ndb.Model):
        title = ndb.StringProperty()
        stars = ndb.IntegerProperty()
        tags = ndb.StringProperty(repeated=True)

The `!=` (not-equal) and `IN` (membership) operations are implemented by combining other filters using the `OR` operation. The first of these, 
    
    
    property != value

is implemented as 
    
    
    (property < value) OR (property > value)

For example, 
    
    
    query = Article.query(Article.tags != 'perl')

is equivalent to 
    
    
    query = Article.query(ndb.OR(Article.tags < 'perl',
                                 Article.tags > 'perl'))

**Note:** Perhaps surprisingly, this query does not search for `Article` entities that don't include 'perl' as a tag! Rather, it finds all entities with at least one tag unequal to 'perl'. For example, the following entity would be included in the results, even though it has 'perl' as one of its tags:  
  

    
    
    Article(title='Perl + Python = Parrot',
            stars=5,
            tags=['python', 'perl'])

However, this one would not be included:  
  

    
    
    Article(title='Introduction to Perl',
            stars=3,
            tags=['perl'])

  
There is no way to query for entities that do not include a tag equal to 'perl'. 

Similarly, the IN operation 
    
    
    property IN [value1, value2, ...]

which tests for membership in a list of possible values, is implemented as 
    
    
    (property == value1) OR (property == value2) OR ...

For example, 
    
    
    query = Article.query(Article.tags.IN(['python', 'ruby', 'php']))

is equivalent to 
    
    
    query = Article.query(ndb.OR(Article.tags == 'python',
                                 Article.tags == 'ruby',
                                 Article.tags == 'php'))

**Note:** Queries using `OR` de-duplicate their results: the result stream doesn't include entity more than once, even if an entity matches two or more subqueries. 

## Querying for Repeated Properties

The `Article` class defined in the preceding section also serves as an example of querying for repeated properties. Notably, a filter like 
    
    
    Article.tags == 'python'

uses a single value, even though `Article.tags` is a repeated property. You cannot compare repeated properties to list objects (the Datastore won't understand it), and a filter like 
    
    
    Article.tags.IN(['python', 'ruby', 'php'])

does something completely different from searching for `Article` entities whose tags value is the list `['python', 'ruby', 'php']`: it searches for entities whose `tags` value (regarded as a list) contains _at least one_ of those values. 

Querying for a value of `None` on a repeated property has undefined behavior; don't do that. 

## Combining AND and OR Operations

You can nest `AND` and `OR` operations arbitrarily. For example: 
    
    
    query = Article.query(ndb.AND(Article.tags == 'python',
                                  ndb.OR(Article.tags.IN(['ruby', 'jruby']),
                                         ndb.AND(Article.tags == 'php',
                                                 Article.tags != 'perl'))))

However, due to `OR`'s implementation, a query of this form that is too complex might fail with an exception. You are safer if you normalize these filters so there is (at most) a single `OR` operation at the top of the expression tree, and a single level of `AND` operations below that.

To perform this normalization, you need to remember both your rules of Boolean logic, and how the `!=` and `IN` filters are actually implemented: 

  1. Expand the `!=` and `IN` operators to their primitive form, where `!=` becomes a check for the property being < or > than the value, and `IN` becomes a check for the property being == to the first value or the second value or...all the way to the last value in the list.
  2. An `AND` with an `OR` inside it is equivalent to an `OR` of multiple `AND`s applied to the original `AND` operands, with a single `OR` operand substituted for the original `OR`. For example `AND(a, b, OR(c, d))` is equivalent to `OR(AND(a, b, c), AND(a, b, d))`
  3. An `AND` that has an operand that is itself an `AND` operation can incorporate the operands of the nested `AND` into the enclosing `AND`. For example `AND(a, b, AND(c, d))` is equivalent to `AND(a, b, c, d)`
  4. An `OR` that has an operand that is itself an `OR` operation can incorporate the operands of the nested `OR` into the enclosing `OR`. For example `OR(a, b, OR(c, d))` is equivalent to `OR(a, b, c, d)`



If we apply these transformations in stages to the example filter, using a simpler notation than Python, you get: 

  1. Using rule #1 on the `IN` and `!=` operators: 
         
         AND(tags == 'python',
           OR(tags == 'ruby',
              tags == 'jruby',
              AND(tags == 'php',
                  OR(tags < 'perl', tags > 'perl'))))

  2. Using rule #2 on the innermost `OR` nested within an `AND`: 
         
         AND(tags == 'python',
           OR(tags == 'ruby',
              tags == 'jruby',
              OR(AND(tags == 'php', tags < 'perl'),
                 AND(tags == 'php', tags > 'perl'))))

  3. Using rule #4 on the `OR` nested within another `OR`: 
         
         AND(tags == 'python',
           OR(tags == 'ruby',
              tags == 'jruby',
              AND(tags == 'php', tags < 'perl'),
              AND(tags == 'php', tags > 'perl')))

  4. Using rule #2 on the remaining `OR` nested within an `AND`: 
         
         OR(AND(tags == 'python', tags == 'ruby'),
            AND(tags == 'python', tags == 'jruby'),
            AND(tags == 'python', AND(tags == 'php', tags < 'perl')),
            AND(tags == 'python', AND(tags == 'php', tags > 'perl')))

  5. Using rule #3 to collapse the remaining nested `AND`s: 
         
         OR(AND(tags == 'python', tags == 'ruby'),
            AND(tags == 'python', tags == 'jruby'),
            AND(tags == 'python', tags == 'php', tags < 'perl'),
            AND(tags == 'python', tags == 'php', tags > 'perl'))




**Caution:** For some filters, this normalization can cause a combinatorial explosion. Consider the `AND` of 3 `OR` clauses with 2 basic clauses each. When normalized, this becomes an `OR` of 8 `AND` clauses with 3 basic clauses each: that is, 6 terms become 24. 

## Specifying Sort Orders

You can use the `order()` method to specify the order in which a query returns its results. This method takes a list of arguments, each of which is either a property object (to be sorted in ascending order) or its negation (denoting descending order). For example: 
    
    
    query = Greeting.query().order(Greeting.content, -Greeting.date)

This retrieves all `Greeting` entities, sorted by ascending value of their `content` property. Runs of consecutive entities with the same content property will be sorted by descending value of their `date` property. You can use multiple `order()` calls to the same effect: 
    
    
    query = Greeting.query().order(Greeting.content).order(-Greeting.date)

**Note:** When combining filters with `order()`, the Datastore rejects certain combinations. In particular, when you use an inequality filter, the first sort order (if any) must specify the same property as the filter. Also, you sometimes need to configure a secondary index. 

## Ancestor Queries

Ancestor queries allow you to make strongly consistent queries to the datastore, however entities with the same ancestor are limited to 1 write per second. Here's a simple comparison of the tradeoffs and structure between an ancestor and non-ancestor query using customers and their associated purchases in the datastore.

In the following non-ancestor example, there's one entity in the datastore for each `Customer`, and one entity in the datastore for each `Purchase`, with a `KeyProperty` that points to the customer.
    
    
    class Customer(ndb.Model):
        name = ndb.StringProperty()
    
    class Purchase(ndb.Model):
        customer = ndb.KeyProperty(kind=Customer)
        price = ndb.IntegerProperty()

To find all the purchases that belong to the customer, you can use the following query:
    
    
    purchases = Purchase.query(
        Purchase.customer == customer_entity.key).fetch()

In this case, the datastore offers high write throughput, but only eventual consistency. If a new purchase was added you may get stale data. You can eliminate this behavior using ancestor queries. 

For customers and purchases with ancestor queries, you still have the same structure with two separate entities. The customer part is the same. However, when you create purchases, you no longer need to specify the `KeyProperty()` for purchases anymore. This is because when you use ancestor queries, you call the customer entity's key when you create a purchase entity.
    
    
    class Customer(ndb.Model):
        name = ndb.StringProperty()
    
    class Purchase(ndb.Model):
        price = ndb.IntegerProperty()

Each purchase has a key, and the customer has its own key as well. However, each purchase key will have the customer_entity's key embedded in it. Remember, this will be limited to one write per ancestor per second. The following creates an entity with an ancestor:
    
    
    purchase = Purchase(parent=customer_entity.key)

To query for the purchases of a given customer, use the following query.
    
    
    purchases = Purchase.query(ancestor=customer_entity.key).fetch()

## Query Attributes

Query objects have the following read-only data attributes: 

Attribute | Type | Default | Description   
---|---|---|---  
kind | `str` | `None` | Kind name (usually the class name)   
ancestor | `Key` | `None` | Ancestor specified to query   
filters | `FilterNode` | `None` | Filter expression   
orders | `Order` | `None` | Sort orders   
  
Printing a query object (or calling `str()` or `repr()` on it) produces a nicely-formatted string representation: 
    
    
    print(Employee.query())
    # -> Query(kind='Employee')
    print(Employee.query(ancestor=ndb.Key(Manager, 1)))
    # -> Query(kind='Employee', ancestor=Key('Manager', 1))

##  Filtering for Structured Property Values

A query can filter directly for the field values of structured properties. For example, a query for all contacts with an address whose city is `'Amsterdam'` would look like 
    
    
    query = Contact.query(Contact.addresses.city == 'Amsterdam')

If you combine multiple such filters, the filters may match _different_ `Address` sub-entities within the same Contact entity. For example: 
    
    
    query = Contact.query(Contact.addresses.city == 'Amsterdam',  # Beware!
                          Contact.addresses.street == 'Spear St')

may find contacts with an address whose city is `'Amsterdam'` and another (different) address whose street is `'Spear St'`. However, at least for equality filters, you can create a query that returns only results with multiple values in a single sub-entity: 
    
    
    query = Contact.query(Contact.addresses == Address(city='San Francisco',
                                                       street='Spear St'))

If you use this technique, properties of the sub-entity equal to `None` are ignored in the query. If a property has a default value, you have to explicitly set it to `None` to ignore it in the query, otherwise the query includes a filter requiring that property value to be equal to the default. For example, if the `Address` model had a property `country` with `default='us'`, the above example would only return contacts with country equal to `'us'`; to consider contacts with other country values, you would need to filter for `Address(city='San Francisco', street='Spear St', **country=None**)`. 

If a sub-entity has any property values equal to `None`, they are ignored. Thus, it doesn't make sense to filter for a sub-entity property value of `None`. 

## Using Properties Named by String

Sometimes you want to filter or order a query based on a property whose name is specified by string. For example, if you let the user enter search queries like `tags:python`, it would be convenient to somehow turn that into a query like 
    
    
    Article.query(Article."tags" == "python") # does NOT work

If your model is an `[Expando](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-models#expando)`, then your filter can use `GenericProperty`, the class `Expando` uses for dynamic properties: 
    
    
    property_to_query = 'location'
    query = FlexEmployee.query(ndb.GenericProperty(property_to_query) == 'SF')

Using `GenericProperty` also works if your model is not an `Expando`, but if you want to ensure that you are only using defined property names, you can also use the `_properties` class attribute 
    
    
    query = Article.query(Article._properties[keyword] == value)

or use `getattr()` to get it from the class: 
    
    
    query = Article.query(getattr(Article, keyword) == value)

The difference is that `getattr()` uses the "Python name" of the property while `_properties` is indexed by the "datastore name" of the property. These only differ when the property was declared with something like 
    
    
    class ArticleWithDifferentDatastoreName(ndb.Model):
        title = ndb.StringProperty('t')

Here the Python name is `title` but the datastore name is `t`. 

These approaches also work for ordering query results: 
    
    
    expando_query = FlexEmployee.query().order(ndb.GenericProperty('location'))
    
    property_query = Article.query().order(Article._properties[keyword])
    

## Query Iterators

While a query is in progress, its state is held in an iterator object. (Most applications won't use them directly; it's normally more straightforward to call `fetch(20)` than to manipulate the iterator object.) There are two basic ways to get such an object: 

  * using Python's built-in `iter()` function on a `Query` object 
  * calling the `Query` object's `iter()` method 



The first supports the use of a Python `for` loop (which implicitly calls the `iter()` function) to loop over a query. 
    
    
    for greeting in greetings:
        self.response.out.write(
            '<blockquote>%s</blockquote>' % cgi.escape(greeting.content))

The second way, using the `Query` object's `iter()` method, allows you to pass options to the iterator to affect its behavior. For example, to use a keys-only query in a `for` loop, you can write this: 
    
    
    for key in query.iter(keys_only=True):
        print(key)

Query iterators have other useful methods: 

Method | Description   
---|---  
`__iter__()` | Part of Python's iterator protocol.   
`next()` | Returns the next result or raises the exception `StopIteration` if there is none.  
  
  
`has_next()` | Returns `True` if a subsequent `next()` call will return a result, `False` if it will raise `StopIteration`.  
  
Blocks until the answer to this question is known and buffers the result (if any) until you retrieve it with `next()`.   
`probably_has_next()` | Like `has_next()`, but uses a faster (and sometimes inaccurate) shortcut.  
  
May return a false positive (`True` when `next()` would actually raise `StopIteration`), but never a false negative (`False` when `next()` would actually return a result).   
`cursor_before()` | Returns a query cursor representing a point just before the last result returned.  
  
Raises an exception if no cursor is available (in particular, if the `produce_cursors` query option was not passed).   
`cursor_after()` | Returns a query cursor representing a point just after the last result returned.  
  
Raises an exception if no cursor is available (in particular, if the `produce_cursors` query option was not passed).   
`index_list()` | Returns a list of indexes used by an executed query, including primary, composite, kind, and single-property indexes.   
  
## Query Cursors

A _query cursor_ is a small opaque data structure representing a resumption point in a query. This is useful for showing a user a page of results at a time; it's also useful for handling long jobs that might need to stop and resume. A typical way to use them is with a query's `fetch_page()` method. It works somewhat like `fetch()`, but it returns a triple `(results, cursor, more)`. The returned `more` flag indicates that there are probably more results; a UI can use this, for example, to suppress a "Next Page" button or link. To request subsequent pages, pass the cursor returned by one `fetch_page()` call into the next. A `BadArgumentError` is raised if you pass in an invalid cursor. Note that the validation only checks whether the value is base64 encoded. You'll have to do any further needed validation. 

Thus, to let the user view all entities matching a query, fetching them a page at a time, your code might look like: 
    
    
    from google.appengine.datastore.datastore_query import Cursor

`...`
    
    
    class List(webapp2.RequestHandler):
        GREETINGS_PER_PAGE = 10
    
        def get(self):
            """Handles requests like /list?cursor=1234567."""
            cursor = Cursor(urlsafe=self.request.get('cursor'))
            greets, next_cursor, more = Greeting.query().fetch_page(
                self.GREETINGS_PER_PAGE, start_cursor=cursor)
    
            self.response.out.write('<html><body>')
    
            for greeting in greets:
                self.response.out.write(
                    '<blockquote>%s</blockquote>' % cgi.escape(greeting.content))
    
            if more and next_cursor:
                self.response.out.write('<a href="/list?cursor=%s">More...</a>' %
                                        next_cursor.urlsafe())
    
            self.response.out.write('</body></html>')

Note the use of `urlsafe()` and `Cursor(urlsafe=s)` to serialize and deserialize the cursor. This allows you to pass a cursor to a client on the web in the response to one request, and receive it back from the client in a later request. 

**Note:** The `fetch_page()` method typically returns a cursor even if there are no more results, but this is not guaranteed: the cursor value returned may be `None`. Note also that because the `more` flag is implemented using the iterator's `probably_has_next()` method, in rare circumstances it may return `True` even though the next page is empty. 

Some NDB queries don't support query cursors, but you can fix them. If a query uses `IN`, `OR`, or `!=`, then the query results won't work with cursors _unless_ ordered by key. If an application doesn't order the results by key and calls `fetch_page()`, it gets a `BadArgumentError`. If ` User.query(User.name.IN(['Joe', 'Jane'])).order(User.name).fetch_page(N) ` gets an error, change it to ` User.query(User.name.IN(['Joe', 'Jane'])).order(User.name**, User.key**).fetch_page(N)`

Instead of "paging" through query results, you can use a query's `iter()` method to get a cursor at a precise point. To do this, pass `produce_cursors=True` to `iter()`; when the iterator is at the right place, call its `cursor_after()` to get a cursor that's just after that. (Or, similarly, call `cursor_before()` for a cursor just before.) Note that calling `cursor_after()` or `cursor_before()` may make a blocking Datastore call, rerunning part of the query in order to extract a cursor that points to the middle of a batch. 

To use a cursor to page backwards through query results, create a reverse query: 
    
    
    # Set up.
    q = Bar.query()
    q_forward = q.order(Bar.key)
    q_reverse = q.order(-Bar.key)
    
    # Fetch a page going forward.
    bars, cursor, more = q_forward.fetch_page(10)
    
    # Fetch the same page going backward.
    r_bars, r_cursor, r_more = q_reverse.fetch_page(10, start_cursor=cursor)
    

## Calling a Function for each Entity ("Mapping")

Suppose you need to get the `Account` entities corresponding to the `Message` entities returned by a query. You could write something like this: 
    
    
    message_account_pairs = []
    for message in message_query:
        key = ndb.Key('Account', message.userid)
        account = key.get()
        message_account_pairs.append((message, account))
    

However, this is pretty inefficient: it waits to fetch an entity, then uses the entity; waits for the next entity, uses the entity. There is a lot of waiting time. Another way is to write a callback function that is mapped over the query results: 
    
    
    def callback(message):
        key = ndb.Key('Account', message.userid)
        account = key.get()
        return message, account
    
    message_account_pairs = message_query.map(callback)
    # Now message_account_pairs is a list of (message, account) tuples.

This version will run somewhat faster than the simple `for` loop above because some concurrency is possible. However, because the `get()` call in `callback()` is still synchronous, the gain is not tremendous. This is a good place to use [asynchronous gets](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/async#using). 

## GQL

GQL is a SQL-like language for retrieving entities or keys from the App Engine Datastore. While GQL's features are different from those of a query language for a traditional relational database, the GQL syntax is similar to that of SQL. The GQL syntax is described in the [GQL Reference](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/gqlreference). 

You can use GQL to construct queries. This is similar to creating a query with `Model.query()`, but uses GQL syntax to define the query filter and order. To use it: 

  * `ndb.gql(querystring)` returns a `Query` object (the same type as returned by `Model.query()`). All the usual methods are available on such `Query` objects: `fetch()`, `map_async()`, `filter()`, etc. 
  * `Model.gql(querystring)` is a shorthand for `ndb.gql("SELECT * FROM Model " + querystring)`. Typically, querystring is something like `"WHERE prop1 > 0 AND prop2 = TRUE"`. 
  * To query models containing structured properties, you can use `foo.bar` in your GQL syntax to reference subproperties. 
  * GQL supports SQL-like parameter bindings. An application can define a query and then bind values into it: 
        
        query = ndb.gql("SELECT * FROM Article WHERE stars > :1")
        query2 = query.bind(3)
        

or 
        
        query = ndb.gql("SELECT * FROM Article WHERE stars > :1", 3)

Calling a query's `bind()` function returns a new query; it does not change the original. 

  * If your model class overrides the `_get_kind()` class method, your GQL query should use the kind returned by that function, not the class name. 
  * If a property in your model overrides its name (e.g., `foo = StringProperty('bar')`) your GQL query should use the overridden property name (in the example, `bar`). 



Always use the parameter-binding feature if some values in your query are user-supplied variables. This avoids attacks based on syntactic hacks. 

It is an error to query for a model that hasn't been imported (or, more generally, defined). 

It is an error to use a property name that is not defined by the model class unless that model is an Expando. 

Specifying a limit or offset to the query's `fetch()` overrides the limit or offset set by GQL's `OFFSET` and `LIMIT` clauses. Don't combine GQL's `OFFSET` and `LIMIT` with `fetch_page()` Note that the 1,000 result maximum imposed by App Engine on queries applies to both offset and limit. 

If you are accustomed to SQL, beware of false assumptions when using GQL. GQL is translated to NDB's native query API. This is different from a typical Object-Relational mapper (like SQLAlchemy or Django's database support), where the API calls are translated into SQL before they are transmitted to the database server. GQL does not support Datastore modifications (inserts, deletes or updates); it only supports queries. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
