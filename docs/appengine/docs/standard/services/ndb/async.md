---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/async/
title: NDB Asynchronous Operation \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:26.655000+00:00
---

# NDB Asynchronous Operation  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Asynchronous Operation Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

When optimizing an application's performance, consider its NDB use. For example, if an application reads a value that isn't in cache, that read takes a while. You might be able to speed up your application by performing Datastore actions in parallel with other things, or performing a few Datastore actions in parallel with each other. 

The NDB Client Library provides many asynchronous ("async") functions. Each of these functions lets an application send a request to the Datastore. The function returns immediately, returning a `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` object. The application can do other things while the Datastore handles the request. After the Datastore handles the request, the application can get the results from the `Future` object. 

## Using Async APIs and Futures

Almost every synchronous NDB function has an `_async` counterpart. For example, `put()` has `put_async()`. The async function's arguments are always the same as those of the synchronous version. The return value of an async method is always either a `Future` or (for "multi" functions) a list of `Future`s. 

A _Future_ is an object that maintains state for an operation that has been initiated but may not yet have completed; all async APIs return one or more `Futures`. You can call the `Future`'s `get_result()` function to ask it for the result of its operation; the Future then blocks, if necessary, until the result is available, and then gives it to you. `get_result()` returns the value that would be returned by the synchronous version of the API. 

**Note:** If you've used Futures in certain other programming languages, you might think you can use a Future as a result directly. That doesn't work here. Those languages use [ implicit futures](https://en.wikipedia.org/wiki/Future_\(programming\)#Implicit_vs._explicit); NDB uses explicit futures. Call `get_result()` to get an NDB `Future`'s result. 

What if the operation raises an exception? That depends on when the exception occurs. If NDB notices a problem when _making_ a request (perhaps an argument of the wrong type), the `_async()` method raises an exception. But if the exception is detected by, say, the Datastore server, the `_async()` method returns a `Future`, and the exception will be raised when your application calls its `get_result()`. Don't worry too much about this, it all ends up behaving quite natural; perhaps the biggest difference is that if a traceback gets printed, you'll see some pieces of the low-level asynchronous machinery exposed. 

For example, suppose you are writing a guestbook application. If the user is logged in, you want to present a page showing the most recent guestbook posts. This page should also show the user their nickname. The application needs two kinds of information: the logged-in user's account information and the contents of the guestbook posts. The "synchronous" version of this application might look like: 
    
    
    uid = users.get_current_user().user_id()
    acct = Account.get_by_id(uid)  # I/O action 1
    qry = Guestbook.query().order(-Guestbook.post_date)
    recent_entries = qry.fetch(10)  # I/O action 2
    
    # ...render HTML based on this data...
    self.response.out.write('<html><body>{}</body></html>'.format(''.join(
        '<p>{}</p>'.format(entry.content) for entry in recent_entries)))
    

There are two independent I/O actions here: getting the `Account` entity and fetching recent `Guestbook` entities. Using the synchronous API, these happen one after the other; we wait to receive the account information before fetching the guestbook entities. But the application doesn't need the account information right away. We can take advantage of this and use async APIs: 
    
    
    uid = users.get_current_user().user_id()
    **acct_future = Account.get_by_id_async(uid)  # Start I/O action #1**
    qry = Guestbook.query().order(-Guestbook.post_date)
    **recent_entries_future = qry.fetch_async(10)  # Start I/O action #2**
    **acct = acct_future.get_result()  # Complete #1**
    **recent_entries = recent_entries_future.get_result()  # Complete #2**
    
    # ...render HTML based on this data...
    self.response.out.write('<html><body>{}</body></html>'.format(''.join(
        '<p>{}</p>'.format(entry.content) for entry in recent_entries)))

This version of the code first creates two `Futures` (`acct_future` and `recent_entries_future`), and then waits for them. The server works on both requests in parallel. Each `_async()` function call creates a Future object and sends a request to the Datastore server. The server can start working on the request right away. The server responses may come back in any arbitrary order; the Future object link responses to their corresponding requests. ![Synchronous requests don't overlap, but asynchronous ones can.](https://docs.cloud.google.com/static/appengine/docs/standard/services/ndb/guestbook_sync_vs_async.png)Synchronous vs. Async requests

The total (real) time spent in the async version is roughly equal to the maximum time across the operations. The total time spent in the synchronous version exceeds the sum of the operation times. If you can run more operations in parallel, then async operations help more. 

## Using Tasklets

An NDB _tasklet_ is a piece of code that might run concurrently with other code. If you write a tasklet, your application can use it much like it uses an async NDB function: it calls the tasklet, which returns a `Future`; later, calling the `Future`'s `get_result()` method gets the result. 

Tasklets are a way to write concurrent functions without threads; tasklets are executed by an event loop and can suspend themselves blocking for I/O or some other operation using a yield statement. The notion of a blocking operation is abstracted into the `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` class, but a tasklet may also `yield` an RPC in order to wait for that RPC to complete. When the tasklet has a result, it `raise`s an `ndb.Return` exception; NDB then associates the result with the previously-`yield`ed `Future`. 

When you write an NDB tasklet, you use `yield` and `raise` in an unusual way. Thus, if you look for examples of how to use these, you probably will not find code like an NDB tasklet. 

To turn a function into an NDB tasklet: 

  * decorate the function with `@ndb.tasklet`, 
  * replace all synchronous datastore calls with `yield`s of asynchronous datastore calls, 
  * make the function "return" its return value with `raise ndb.Return(retval)` (not necessary if the function doesn't return anything). 



An application can use tasklets for finer control over asynchronous APIs. As an example, consider the following schema: 
    
    
    class Account(ndb.Model):
        email = ndb.StringProperty()
        nickname = ndb.StringProperty()
    
        def nick(self):
            return self.nickname or self.email  # Whichever is non-empty

`...`
    
    
    class Message(ndb.Model):
        text = ndb.StringProperty()
        when = ndb.DateTimeProperty(auto_now_add=True)
        author = ndb.KeyProperty(kind=Account)  # references Account

When displaying a message, it makes sense to show the author's nickname. The "synchronous" way to fetch the data to show a list of messages might look like this: 
    
    
    qry = Message.query().order(-Message.when)
    for msg in qry.fetch(20):
        acct = msg.author.get()
        self.response.out.write(
            '<p>On {}, {} wrote:'.format(msg.when, acct.nick()))
        self.response.out.write('<p>{}'.format(msg.text))

Unfortunately, this approach is inefficient. You might see the following "staircase" pattern. ![Synchronous "Gets" occur in series](https://docs.cloud.google.com/static/appengine/docs/standard/services/ndb/query_get_get_sync.png)Synchronous "Gets" occur in series.

This part of the program would be faster if those "Gets" could overlap. You might rewrite the code to use `get_async`, but it is tricky to keep track of which async requests and messages belong together. 

The application can define its own "async" function by making it a tasklet. This allows you to organize the code in a less confusing way. 

Furthermore, instead of using `acct = key.get()` or `acct = key.get_async().get_result()`, the function should use `acct = **yield** key.get**_async**()`. This `yield` tells NDB that this is a good place to suspend this tasklet and let other tasklets run. 

Decorating a generator function with `@ndb.tasklet` makes the function return a `Future` instead of a generator object. Within the tasklet, any `yield` of a `Future` waits for and returns the `Future`'s result. 

For example: 
    
    
    **@ndb.tasklet**
    def callback(msg):
    ** acct = yield msg.author.get_async()**
    ** raise ndb.Return('On {}, {} wrote:\n{}'.format(**
    ** msg.when, acct.nick(), msg.text))**
    
    qry = Message.query().order(-Message.when)
    **outputs = qry.map(callback, limit=20)**
    for output in outputs:
        self.response.out.write('<p>{}</p>'.format(output))

Take note that although `get_async()` returns a `Future`, the tasklet framework causes the `yield` expression to return the `Future`'s result to variable `acct`. 

The `map()` calls `callback()` several times. But the `yield ..._async()` in `callback()` lets NDB's scheduler send off many async requests before waiting for any of them to finish. ![Overlapping Async "Gets"](https://docs.cloud.google.com/static/appengine/docs/standard/services/ndb/query_get_get_tasklet.png)Overlapping Async "Gets"

If you look at this in Appstats, you might be surprised to see that these multiple Gets don't just overlap—they all go through in the same request. NDB implements an "_autobatcher_." The autobatcher bundles multiple requests up in a single batch RPC to the server; it does this in such a way that as long as there is more work to do (another callback may run) it collects keys. As soon as one of the results is needed, the autobatcher sends the batch RPC. Unlike most requests, queries are not "batched".

When a tasklet runs, it gets its default namespace from whatever the default was when the tasklet was spawned, or whatever the tasklet changed it to while running. In other words, the default namespace is not associated with or stored in the [Context](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/contextclass), and changing the default namespace in one tasklet does not affect the default namespace in other tasklets, except those spawned by it.

## Tasklets, Parallel Queries, Parallel Yield

You can use tasklets so that multiple queries fetch records at the same time. For example, suppose your application has a page that displays the contents of a shopping cart and a list of special offers. The schema might look like this: 
    
    
    class Account(ndb.Model):
        pass
    
    
    class InventoryItem(ndb.Model):
        name = ndb.StringProperty()
    
    
    class CartItem(ndb.Model):
        account = ndb.KeyProperty(kind=Account)
        inventory = ndb.KeyProperty(kind=InventoryItem)
        quantity = ndb.IntegerProperty()
    
    
    class SpecialOffer(ndb.Model):
        inventory = ndb.KeyProperty(kind=InventoryItem)

A "synchronous" function that gets shopping cart items and special offers might look like the following: 
    
    
    def get_cart_plus_offers(acct):
        cart = CartItem.query(CartItem.account == acct.key).fetch()
        offers = SpecialOffer.query().fetch(10)
        ndb.get_multi([item.inventory for item in cart] +
                      [offer.inventory for offer in offers])
        return cart, offers

This example uses queries to fetch lists of cart items and offers; it then fetches details about the inventory items with `get_multi()`. (This function doesn't use the return value of `get_multi()` directly. It calls `get_multi()` to fetch all the inventory details into the cache so that they can be read quickly later.) `get_multi` combines many Gets into one request. But the query fetches happen one after the other. To make those fetches happen at the same time, overlap the two queries: 
    
    
    def get_cart_plus_offers_async(acct):
    ** cart_future = CartItem.query(CartItem.account == acct.key).fetch_async()**
    ** offers_future = SpecialOffer.query().fetch_async(10)**
    ** cart = cart_future.get_result()**
    ** offers = offers_future.get_result()**
        ndb.get_multi([item.inventory for item in cart] +
                      [offer.inventory for offer in offers])
        return cart, offers

The `get_multi()` call is still separate: it depends on the query results, so you can't combine it with the queries. 

Suppose this application sometimes needs the cart, sometimes the offers, and sometimes both. You want to organize your code so that there's a function to get the cart and a function to get the offers. If your application calls these functions together, ideally their queries could "overlap." To do this, make these functions tasklets: 
    
    
    @ndb.tasklet
    def get_cart_tasklet(acct):
        cart = yield CartItem.query(CartItem.account == acct.key).fetch_async()
        yield ndb.get_multi_async([item.inventory for item in cart])
        raise ndb.Return(cart)
    
    
    @ndb.tasklet
    def get_offers_tasklet(acct):
        offers = yield SpecialOffer.query().fetch_async(10)
        yield ndb.get_multi_async([offer.inventory for offer in offers])
        raise ndb.Return(offers)
    
    
    @ndb.tasklet
    def get_cart_plus_offers_tasklet(acct):
        cart, offers = yield get_cart_tasklet(acct), get_offers_tasklet(acct)
        raise ndb.Return((cart, offers))

That `yield x, y` is important but easy to overlook. If that were two separate `yield` statements, they would happen in series. But `yield`ing a tuple of tasklets is a _parallel yield_ : the tasklets can run in parallel and the `yield` waits for all of them to finish and returns the results. (In some programming languages, this is known as a _barrier_.) 

If you turn one piece of code into a tasklet, you will probably want to do more soon. If you notice "synchronous" code that could run in parallel with a tasklet, it's probably a good idea to make it a tasklet, too. Then you can parallelize it with a parallel `yield`. 

If you write a request function (a webapp2 request function, a Django view function, etc.) to be a tasklet, it won't do what you want: it yields but then stops running. In this situation, you want to decorate the function with `@ndb.synctasklet`. `@ndb.synctasklet` is like `@ndb.tasklet` but altered to call `get_result()` on the tasklet. This turns your tasklet into a function that returns its result in the usual way. 

## Query Iterators in Tasklets

To iterate over query results in a tasklet, use the following pattern: 
    
    
    qry = Model.query()
    **qit = qry.iter()**
    **while (yield qit.has_next_async()):**
    ** entity = qit.next()**
        # Do something with entity
        if is_the_entity_i_want(entity):
            raise ndb.Return(entity)

This is the tasklet-friendly equivalent of the following: 
    
    
    # DO NOT DO THIS IN A TASKLET
    qry = Model.query()
    **for entity in qry:**
        # Do something with entity
        if is_the_entity_i_want(entity):
            raise ndb.Return(entity)

The three bold lines in the first version are the tasklet-friendly equivalent of the single bold line in the second version. Tasklets can only be suspended at a `yield` keyword. The `yield`-less for loop doesn't let other tasklets run. 

You might wonder why this code uses a query iterator at all instead of fetching all the entities using `qry.fetch_async()`. The application might have so many entities that they don't fit in RAM. Perhaps you're looking for an entity and can stop iterating once you find it; but you can't express your search criteria with just the query language. You might use an iterator to load entities to check, then break out of the loop when you find what you want. 

## Async Urlfetch with NDB

An NDB `Context` has an asynchronous `urlfetch()` function that parallelizes nicely with NDB tasklets, for example: 
    
    
    @ndb.tasklet
    def get_google():
        context = ndb.get_context()
        result = yield context.urlfetch("http://www.google.com/")
        if result.status_code == 200:
            raise ndb.Return(result.content)
    

The URL Fetch service has its own [ asynchronous request API](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests#issuing_an_asynchronous_request). It's fine, but not always easy to use with NDB tasklets. 

## Using Asynchronous Transactions

Transactions may also be done asynchronously. You can pass an existing function to `ndb.transaction_async()`, or use the `@ndb.transactional_async` decorator. Like the other async functions, this will return an NDB `Future`: 
    
    
    @ndb.transactional_async
    def update_counter(counter_key):
        counter = counter_key.get()
        counter.value += 1
        counter.put()
    

Transactions also work with tasklets. For example, we could change our `update_counter` code to `yield` while waiting on blocking RPCs: 
    
    
    @ndb.transactional_tasklet
    def update_counter(counter_key):
        counter = yield counter_key.get_async()
        counter.value += 1
        yield counter.put_async()
    

## Using Future.wait_any()

Sometimes you want to make multiple asynchronous requests and return whenever the first one completes. You can do this using the `ndb.Future.wait_any()` class method: 
    
    
    def get_first_ready():
        urls = ["http://www.google.com/", "http://www.blogspot.com/"]
        context = ndb.get_context()
        futures = [context.urlfetch(url) for url in urls]
        first_future = ndb.Future.wait_any(futures)
        return first_future.get_result().content

Unfortunately, there is no convenient way to turn this into a tasklet; a parallel `yield` waits for all `Future`s to complete—including those you don't want to wait for. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
