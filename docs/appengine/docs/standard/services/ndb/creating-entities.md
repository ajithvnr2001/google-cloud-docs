---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entities/
title: Creating, retrieving, updating, and deleting entities \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:50.958950+00:00
---

# Creating, retrieving, updating, and deleting entities  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Creating, retrieving, updating, and deleting entities Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Data objects in Datastore are known as _entities_ , each of which is categorized under a particular _kind_ for the purpose of queries. For instance, if you are writing a human resources application you might represent each employee with an entity of kind `Employee`. Note that the entity data values are in the form of [properties](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference#properties_and_value_types). 

For more information about entities, see the documentation on [ancestor paths](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-keys#using_the_ancestor_path_in_the_key) and [transactions](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/transactions). **Important:** Inefficient data store code can result in unnecessarily high costs! So before you write your code, you should learn about [write costs](https://cloud.google.com/datastore/pricing).

## Creating entities and setting properties

You create an entity and set by calling the constructor method for its model class. See [Creating and Using Entity Model Classes](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-models) for information on creating an entity model class.

The following example shows how to invoke a model class constructor with keyword arguments:
    
    
    sandy = Account(
        username='Sandy', userid=123, email='sandy@example.com')

This code creates an object in your program's main memory. However, note that the entity disappears when the process terminates, so you must also persist the entity to Datastore, by calling `put()`, as follows:
    
    
    sandy_key = sandy.put()

Notice that this returns a key that you can use for retrieving the entity from Datastore later.

Set properties by using one of the following options:

  * Specify the entity's properties to the constructor with keyword arguments: 
        
        sandy = Account(
            username='Sandy', userid=123, email='sandy@example.com')

  * Set properties manually after entity creation: 
        
        sandy = Account()
        sandy.username = 'Sandy'
        sandy.userid = 123
        sandy.email = 'sandy@example.com'

  * Use the `populate()` convenience method to set several properties in one operation: 
        
        sandy = Account()
        sandy.populate(
            username='Sandy',
            userid=123,
            email='sandy@gmail.com')




However you choose to set the entity's properties, the property types (in this case, `StringProperty` and `IntegerProperty`) enforce type checking.

For example:
    
    
    bad = Account(
        username='Sandy', userid='not integer')  # raises an exception

`...`
    
    
    sandy.username = 42  # raises an exception

## Retrieving Entities from Keys

If you have an entity's key, you can retrieve the entity from Datastore:
    
    
    sandy = sandy_key.get()

The Key methods `kind()` and `id()` recover the entity's kind and identifier from the key:
    
    
    kind_string = sandy_key.kind()  # returns 'Account'
    ident = sandy_key.id()  # returns '2'

You can also use an entity's key to obtain an encoded string suitable for embedding in a URL:
    
    
    url_string = sandy_key.urlsafe()

This produces a result like `agVoZWxsb3IPCxIHQWNjb3VudBiZiwIM` which can later be used to reconstruct the key and retrieve the original entity:
    
    
    sandy_key = ndb.Key(urlsafe=url_string)
    sandy = sandy_key.get()

Notice that the URL-safe string looks cryptic, but it is not encrypted! It can easily be decoded to recover the original entity's kind and identifier:
    
    
    key = Key(urlsafe=url_string)
    kind_string = key.kind()
    ident = key.id()

If you use such URL-safe keys, don't use sensitive data such as email addresses as entity identifiers. A possible solution would be to use a hash of the sensitive data as the identifier. This stops third parties, who can see the encrypted keys, from using them to harvest email addresses, though it doesn't stop them from independently generating their own hash of a known email address and using it to check whether that address is present in Datastore.

## Updating entities

To update an existing entity, retrieve it from Datastore, modify its properties, and store it back again:
    
    
    sandy = key.get()
    sandy.email = 'sandy@example.co.uk'
    sandy.put()

You can ignore the value returned by `put()` in this case, since an entity key doesn't change when you update it.

## Deleting entities

When an entity is no longer needed, you can remove it from Datastore with the key's `delete()` method:
    
    
    sandy.key.delete()

Note that this is an operation on the key, not on the entity itself. It always returns `None`.

## Deleting entities in bulk

If you need to delete a large number of entities, we recommend [using Dataflow to delete entities in bulk](https://docs.cloud.google.com/datastore/docs/bulk-delete).

## Using batch operations

**Note:** The `ndb` library automatically batches most calls to Datastore, so in most cases you don't need to use the explicit batching operations shown below.

You can process a collection of entities or keys in a single call rather than individually in separate calls, for example inside a loop. This results in a single remote procedure call (RPC) for the batch, rather than a separate RPC call for each entity.

The following code shows how you do this:
    
    
    list_of_keys = ndb.put_multi(list_of_entities)
    list_of_entities = ndb.get_multi(list_of_keys)
    ndb.delete_multi(list_of_keys)

**Note:** The methods shown above interact correctly with the [context and caching](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/cache); they don't correspond directly to specific RPC calls.

In the above code, you pass a list of key objects to `ndb.get_multi` to fetch multiple entities in a batch; `ndb.get_multi` returns a list of entity objects, with `None` values for keys that do not have a corresponding entity in Datastore. Getting the entities in this way results in fewer calls to Datastore for the entire batch. (The number of calls per batch depends on your batch size settings.)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
