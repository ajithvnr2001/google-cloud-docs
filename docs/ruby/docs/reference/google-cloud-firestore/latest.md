---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/
title: Cloud Firestore \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:20.684043+00:00
---

# Cloud Firestore  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.1  3.0.0  2.16.1  2.15.1  2.14.0  2.13.1  2.12.0  2.11.0  2.10.1  2.9.1  2.8.0  2.7.2  2.6.6 

Cloud Firestore is a NoSQL document database built for automatic scaling, high performance, and ease of application development. While the Cloud Firestore interface has many of the same features as traditional databases, as a NoSQL database it differs from them in the way it describes relationships between data objects.

For more information about Cloud Firestore, read the [Cloud Firestore Documentation](https://cloud.google.com/firestore/docs/).

The goal of google-cloud is to provide an API that is comfortable to Rubyists. Authentication is handled by [Firestore.new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore#Google__Cloud__Firestore_new_class_ "Google::Cloud::Firestore.new \(method\)"). You can provide the project and credential information to connect to the Cloud Firestore service, or if you are running on Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run this configuration is taken care of for you. You can read more about the options for connecting in the [Authentication Guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/AUTHENTICATION "Authentication Guide").

## Adding data

Cloud Firestore stores data in Documents, which are stored in Collections. Cloud Firestore creates collections and documents implicitly the first time you add data to the document. (For more information, see [Adding Data to Cloud Firestore](https://cloud.google.com/firestore/docs/manage-data/add-data).

To create or overwrite a single document, use [Client#doc](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client#Google__Cloud__Firestore__Client_doc_instance_ "Google::Cloud::Firestore::Client#doc \(method\)") to obtain a document reference. (This does not create a document in Cloud Firestore.) Then, call [DocumentReference#set](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentReference#Google__Cloud__Firestore__DocumentReference_set_instance_ "Google::Cloud::Firestore::DocumentReference#set \(method\)") to create the document or overwrite an existing document:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    nyc_ref.set({ name: "New York City" }) # Document created

When you use this combination of `doc` and `set` to create a new document, you must specify an ID for the document. (In the example above, the ID is "NYC".) However, if you do not have a meaningful ID for the document, you may omit the ID from a call to [CollectionReference#doc](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-CollectionReference#Google__Cloud__Firestore__CollectionReference_doc_instance_ "Google::Cloud::Firestore::CollectionReference#doc \(method\)"), and Cloud Firestore will auto-generate an ID for you.
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection reference
    cities_col = firestore.col "cities"
    
    # Get a document reference with data
    random_ref = cities_col.doc
    random_ref.set({ name: "New York City" })
    
    # The document ID is randomly generated
    random_ref.document_id #=> "RANDOMID123XYZ"

You can perform both of the operations shown above, auto-generating an ID and creating the document, in a single call to [CollectionReference#add](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-CollectionReference#Google__Cloud__Firestore__CollectionReference_add_instance_ "Google::Cloud::Firestore::CollectionReference#add \(method\)").
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection reference
    cities_col = firestore.col "cities"
    
    # Get a document reference with data
    random_ref = cities_col.add({ name: "New York City" })
    
    # The document ID is randomly generated
    random_ref.document_id #=> "RANDOMID123XYZ"

You can also use `add` to create an empty document:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection reference
    cities_col = firestore.col "cities"
    
    # Create a document without data
    random_ref = cities_col.add
    
    # The document ID is randomly generated
    random_ref.document_id #=> "RANDOMID123XYZ"

## Retrieving collection references

Collections are simply named containers for documents. A collection contains documents and nothing else. It can't directly contain raw fields with values, and it can't contain other collections. You do not need to "create" or "delete" collections. After you create the first document in a collection, the collection exists. If you delete all of the documents in a collection, it no longer exists. (For more information, see [Cloud Firestore Data Model](https://cloud.google.com/firestore/docs/data-model).)

Use [Client#cols](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client#Google__Cloud__Firestore__Client_cols_instance_ "Google::Cloud::Firestore::Client#cols \(method\)") to list the root-level collections:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get the root collections
    firestore.cols.each do |col|
      puts col.collection_id
    end

Retrieving a reference to a single root-level collection is similar:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get the cities collection
    cities_col = firestore.col "cities"

To list the collections in a document, first get the document reference, then use [DocumentReference#cols](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentReference#Google__Cloud__Firestore__DocumentReference_cols_instance_ "Google::Cloud::Firestore::DocumentReference#cols \(method\)"):
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    nyc_ref.cols.each do |col|
      puts col.collection_id
    end

Again, retrieving a reference to a single collection is similar::
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    # Get precincts sub-collection
    precincts_col = nyc_ref.col "precincts"

## Reading data

You can retrieve a snapshot of the data in a single document with [DocumentReference#get](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentReference#Google__Cloud__Firestore__DocumentReference_get_instance_ "Google::Cloud::Firestore::DocumentReference#get \(method\)"), which returns an instance of [DocumentSnapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentSnapshot "Google::Cloud::Firestore::DocumentSnapshot \(class\)"):
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    nyc_snap = nyc_ref.get
    nyc_snap[:population] #=> 1000000

In the example above, [DocumentSnapshot#[]](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentSnapshot#Google__Cloud__Firestore__DocumentSnapshot_\[\]_instance_ "Google::Cloud::Firestore::DocumentSnapshot#\[\] \(method\)") is used to access a top-level field. To access nested fields, use [FieldPath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-FieldPath "Google::Cloud::Firestore::FieldPath \(class\)"):
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    user_snap = firestore.doc("users/frank").get
    
    nested_field_path = firestore.field_path :favorites, :food
    user_snap.get(nested_field_path) #=> "Pizza"

Or, use [Client#get_all](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client#Google__Cloud__Firestore__Client_get_all_instance_ "Google::Cloud::Firestore::Client#get_all \(method\)") to retrieve a list of document snapshots (data):
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get and print city documents
    cities = ["cities/NYC", "cities/SF", "cities/LA"]
    firestore.get_all(cities).each do |city|
      puts "#{city.document_id} has #{city[:population]} residents."
    end

To retrieve all of the document snapshots in a collection, use [CollectionReference#get](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query#Google__Cloud__Firestore__Query_get_instance_ "Google::Cloud::Firestore::Query#get \(method\)"):
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection reference
    cities_col = firestore.col "cities"
    
    # Get and print all city documents
    cities_col.get do |city|
      puts "#{city.document_id} has #{city[:population]} residents."
    end

The example above is actually a simple query without filters. Let's look at some other queries for Cloud Firestore.

## Querying data

Use [Query#where](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query#Google__Cloud__Firestore__Query_where_instance_ "Google::Cloud::Firestore::Query#where \(method\)") to filter queries on a field:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection reference
    cities_col = firestore.col "cities"
    
    # Create a query
    query = cities_col.where(:population, :>=, 1000000)
    
    query.get do |city|
      puts "#{city.document_id} has #{city[:population]} residents."
    end

You can order the query results with [Query#order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query#Google__Cloud__Firestore__Query_order_instance_ "Google::Cloud::Firestore::Query#order \(method\)"):
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection reference
    cities_col = firestore.col "cities"
    
    # Create a query
    query = cities_col.order(:name, :desc)
    
    query.get do |city|
      puts "#{city.document_id} has #{city[:population]} residents."
    end

Query methods may be chained, as in this example using [Query#limit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query#Google__Cloud__Firestore__Query_limit_instance_ "Google::Cloud::Firestore::Query#limit \(method\)") and [Query#offset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query#Google__Cloud__Firestore__Query_offset_instance_ "Google::Cloud::Firestore::Query#offset \(method\)") to perform pagination:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection reference
    cities_col = firestore.col "cities"
    
    # Create a query
    query = cities_col.limit(5).offset(10)
    
    query.get do |city|
      puts "#{city.document_id} has #{city[:population]} residents."
    end

See [Managing Indexes in Cloud Firestore](https://cloud.google.com/firestore/docs/query-data/indexing) to ensure the best performance for your queries.

## Updating data

You can use [DocumentReference#set](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentReference#Google__Cloud__Firestore__DocumentReference_set_instance_ "Google::Cloud::Firestore::DocumentReference#set \(method\)") to completely overwrite an existing document:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    nyc_ref.set({ name: "New York City" })

Or, to selectively update only the fields appearing in your `data` argument, set the `merge` option to `true`:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    nyc_ref.set({ name: "New York City" }, merge: true)

Use [DocumentReference#update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentReference#Google__Cloud__Firestore__DocumentReference_update_instance_ "Google::Cloud::Firestore::DocumentReference#update \(method\)") to directly update a deeply-nested field with a [Google::Cloud::Firestore::FieldPath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-FieldPath "Google::Cloud::Firestore::FieldPath \(class\)"):
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    user_ref = firestore.doc "users/frank"
    
    nested_field_path = firestore.field_path :favorites, :food
    user_ref.update({ nested_field_path => "Pasta" })

### Listening for changes

You can listen to a document reference or a collection reference/query for changes. The current document snapshot or query results snapshot will be yielded first, and each time the contents change.

You can use [DocumentReference#listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentReference#Google__Cloud__Firestore__DocumentReference_listen_instance_ "Google::Cloud::Firestore::DocumentReference#listen \(method\)") to be notified of changes to a single document:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    listener = nyc_ref.listen do |snapshot|
      puts "The population of #{snapshot[:name]} "
      puts "is #{snapshot[:population]}."
    end
    
    # When ready, stop the listen operation and close the stream.
    listener.stop

You can use [Query#listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query#Google__Cloud__Firestore__Query_listen_instance_ "Google::Cloud::Firestore::Query#listen \(method\)") to be notified of changes to any document contained in the query:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Create a query
    query = firestore.col(:cities).order(:population, :desc)
    
    listener = query.listen do |snapshot|
      puts "The query snapshot has #{snapshot.docs.count} documents "
      puts "and has #{snapshot.changes.count} changes."
    end
    
    # When ready, stop the listen operation and close the stream.
    listener.stop

## Using transactions and batched writes

Cloud Firestore supports atomic operations for reading and writing data. In a set of atomic operations, either all of the operations succeed, or none of them are applied. There are two types of atomic operations in Cloud Firestore: A transaction is a set of read and write operations on one or more documents, while a batched write is a set of only write operations on one or more documents. (For more information, see [Transactions and Batched Writes](https://cloud.google.com/firestore/docs/manage-data/transactions).

### Transactions

A transaction consists of any number of read operations followed by any number of write operations. (Read operations must always come before write operations.) In the case of a concurrent update by another client, Cloud Firestore runs the entire transaction again. Therefore, transaction blocks should be idempotent and should not not directly modify application state.
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    city = firestore.col("cities").doc("SF")
    city.set({ name: "San Francisco",
               state: "CA",
               country: "USA",
               capital: false,
               population: 860000 })
    
    firestore.transaction do |tx|
      new_population = tx.get(city).data[:population] + 1
      tx.update(city, { population: new_population })
    end

### Batched writes

If you do not need to read any documents in your operation set, you can execute multiple write operations as a single batch. A batch of writes completes atomically and can write to multiple documents. Batched writes are also useful for migrating large data sets to Cloud Firestore.
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    firestore.batch do |b|
      # Set the data for NYC
      b.set("cities/NYC", { name: "New York City" })
    
      # Update the population for SF
      b.update("cities/SF", { population: 1000000 })
    
      # Delete LA
      b.delete("cities/LA")
    end

## Deleting data

Use [DocumentReference#delete](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-DocumentReference#Google__Cloud__Firestore__DocumentReference_delete_instance_ "Google::Cloud::Firestore::DocumentReference#delete \(method\)") to delete a document from Cloud Firestore:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    nyc_ref.delete

To delete specific fields from a document, use the [Client.field_delete](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client#Google__Cloud__Firestore__Client_field_delete_instance_ "Google::Cloud::Firestore::Client#field_delete \(method\)") method when you update a document:
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a document reference
    nyc_ref = firestore.doc "cities/NYC"
    
    nyc_ref.update({ name: "New York City",
                     trash: firestore.field_delete })

To delete an entire collection or sub-collection in Cloud Firestore, retrieve all the documents within the collection or sub-collection and delete them. If you have larger collections, you may want to delete the documents in smaller batches to avoid out-of-memory errors. Repeat the process until you've deleted the entire collection or sub-collection.

## Additional information

Google Firestore can be configured to use gRPC's logging. To learn more, see the [Logging guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/LOGGING "Logging guide").

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
