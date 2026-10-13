---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/
title: Google Cloud Datastore \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:49.925074+00:00
---

# Google Cloud Datastore  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Datastore Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.4 

Google Cloud Datastore is a fully managed, schemaless database for storing non-relational data. You should feel at home if you are familiar with relational databases, but there are some key differences to be aware of to make the most of using Datastore.

The goal of google-cloud is to provide an API that is comfortable to Rubyists. Your authentication credentials are detected automatically in Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run. In other environments you can configure authentication easily, either directly in your code or via environment variables. Read more about the options for connecting in the [Authentication Guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/AUTHENTICATION "Authentication Guide").
    
    
    require "googleauth"
    require "google/cloud/datastore"
    
    credentials = ::Google::Auth::ServiceAccountCredentials.make_creds(
      json_key_io: ::File.open("/path/to/keyfile.json")
    )
    
    datastore = Google::Cloud::Datastore.new(
      project_id: "my-todo-project",
      credentials: credentials
    )
    
    task = datastore.find "Task", "sampleTask"
    task["priority"] = 5
    datastore.save task

To learn more about Datastore, read the [Google Cloud Datastore Concepts Overview ](https://cloud.google.com/datastore/docs/concepts/overview).

## Retrieving records

Records, called "entities" in Datastore, are retrieved by using a key. The key is more than a numeric identifier, it is a complex data structure that can be used to model relationships. The simplest key has a string `kind` value and either a numeric `id` value or a string `name` value. A single record can be retrieved by calling [Google::Cloud::Datastore::Dataset#find](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_find_instance_ "Google::Cloud::Datastore::Dataset#find \(method\)") and passing the parts of the key:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"

Optionally, [Google::Cloud::Datastore::Dataset#find](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_find_instance_ "Google::Cloud::Datastore::Dataset#find \(method\)") can be given a key object:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", 123456
    task = datastore.find task_key

See [Google::Cloud::Datastore::Dataset#find](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_find_instance_ "Google::Cloud::Datastore::Dataset#find \(method\)")

## Querying records

Multiple records can be found that match criteria. (See [Google::Cloud::Datastore::Query#where](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query#Google__Cloud__Datastore__Query_where_instance_ "Google::Cloud::Datastore::Query#where \(method\)"))
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    
    tasks = datastore.run query

Records can also be ordered. (See [Google::Cloud::Datastore::Query#order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query#Google__Cloud__Datastore__Query_order_instance_ "Google::Cloud::Datastore::Query#order \(method\)"))
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      order("created")
    
    tasks = datastore.run query

The number of records returned can be specified. (See [Google::Cloud::Datastore::Query#limit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query#Google__Cloud__Datastore__Query_limit_instance_ "Google::Cloud::Datastore::Query#limit \(method\)"))
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      limit(5)
    
    tasks = datastore.run query

When using Datastore in a multitenant application, a query may be run within a namespace using the `namespace` option. (See [Multitenancy](https://cloud.google.com/datastore/docs/concepts/multitenancy))
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    
    tasks = datastore.run query, namespace: "example-ns"

Records' key structures can also be queried. (See [Google::Cloud::Datastore::Query#ancestor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query#Google__Cloud__Datastore__Query_ancestor_instance_ "Google::Cloud::Datastore::Query#ancestor \(method\)"))
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_list_key = datastore.key "TaskList", "default"
    
    query = datastore.query("Task").
      ancestor(task_list_key)
    
    tasks = datastore.run query

See [Google::Cloud::Datastore::Query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query "Google::Cloud::Datastore::Query \(class\)") and [Google::Cloud::Datastore::Dataset#run](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_run_instance_ "Google::Cloud::Datastore::Dataset#run \(method\)")

### Paginating records

All records may not return at once, but multiple calls can be made to Datastore to return them all.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    tasks = datastore.run query
    tasks.all do |t|
      puts t["description"]
    end

See [Google::Cloud::Datastore::Dataset::LookupResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-LookupResults "Google::Cloud::Datastore::Dataset::LookupResults \(class\)") and [Google::Cloud::Datastore::Dataset::QueryResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults "Google::Cloud::Datastore::Dataset::QueryResults \(class\)")

## Creating records

New entities can be created and persisted buy calling [Google::Cloud::Datastore::Dataset#save](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_save_instance_ "Google::Cloud::Datastore::Dataset#save \(method\)"). The entity must have a key to be saved. If the key is incomplete then it will be completed when saved.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity "Task" do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 4
      t["description"] = "Learn Cloud Datastore"
    end
    task.key.id #=> nil
    datastore.save task
    task.key.id #=> 123456

Multiple new entities may be created in a batch.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task1 = datastore.entity "Task" do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 4
      t["description"] = "Learn Cloud Datastore"
    end
    
    task2 = datastore.entity "Task" do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 5
      t["description"] = "Integrate Cloud Datastore"
    end
    
    tasks = datastore.save(task1, task2)
    task_key1 = tasks[0].key
    task_key2 = tasks[1].key

Entities in Datastore form a hierarchically structured space similar to the directory structure of a file system. When you create an entity, you can optionally designate another entity as its parent; the new entity is a child of the parent entity.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", "sampleTask"
    task_key.parent = datastore.key "TaskList", "default"
    
    task = datastore.entity task_key do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 5
      t["description"] = "Integrate Cloud Datastore"
    end

## Setting properties

Entities hold properties. A property has a name that is a string or symbol, and a value that is an object. Most value objects are supported, including `String`, `Integer`, `Date`, `Time`, and even other entity or key objects. Changes to the entity's properties are persisted by calling [Google::Cloud::Datastore::Dataset#save](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_save_instance_ "Google::Cloud::Datastore::Dataset#save \(method\)").
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"
    # Read the priority property
    task["priority"] #=> 4
    # Write the priority property
    task["priority"] = 5
    # Persist the changes
    datastore.save task

Array properties can be used to store more than one value.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity "Task", "sampleTask" do |t|
      t["tags"] = ["fun", "programming"]
      t["collaborators"] = ["alice", "bob"]
    end

## Deleting records

Entities can be removed from Datastore by calling [Google::Cloud::Datastore::Dataset#delete](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_delete_instance_ "Google::Cloud::Datastore::Dataset#delete \(method\)") and passing the entity object or the entity's key object.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"
    datastore.delete task

Multiple entities may be deleted in a batch.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key1 = datastore.key "Task", "sampleTask1"
    task_key2 = datastore.key "Task", "sampleTask2"
    datastore.delete task_key1, task_key2

## Transactions

Complex logic can be wrapped in a transaction. All queries and updates within the [Google::Cloud::Datastore::Dataset#transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_transaction_instance_ "Google::Cloud::Datastore::Dataset#transaction \(method\)") block are run within the transaction scope, and will be automatically committed when the block completes.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", "sampleTask"
    
    datastore.transaction do |tx|
      if tx.find(task_key).nil?
        task = datastore.entity task_key do |t|
          t["type"] = "Personal"
          t["done"] = false
          t["priority"] = 4
          t["description"] = "Learn Cloud Datastore"
        end
        tx.save task
      end
    end

Alternatively, if no block is given the transaction object is returned allowing you to commit or rollback manually.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", "sampleTask"
    
    tx = datastore.transaction
    begin
      if tx.find(task_key).nil?
        task = datastore.entity task_key do |t|
          t["type"] = "Personal"
          t["done"] = false
          t["priority"] = 4
          t["description"] = "Learn Cloud Datastore"
        end
        tx.save task
      end
      tx.commit
    rescue
      tx.rollback
    end

A read-only transaction cannot modify entities; in return they do not contend with other read-write or read-only transactions. Using a read-only transaction for transactions that only read data will potentially improve throughput.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_list_key = datastore.key "TaskList", "default"
    query = datastore.query("Task").
      ancestor(task_list_key)
    
    tasks = nil
    
    datastore.transaction read_only: true do |tx|
      task_list = tx.find task_list_key
      if task_list
        tasks = tx.run query
      end
    end

See [Google::Cloud::Datastore::Transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Transaction "Google::Cloud::Datastore::Transaction \(class\)") and [Google::Cloud::Datastore::Dataset#transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_transaction_instance_ "Google::Cloud::Datastore::Dataset#transaction \(method\)")

## Querying metadata

Datastore provides programmatic access to some of its metadata to support meta-programming, implementing backend administrative functions, simplify consistent caching, and similar purposes. The metadata available includes information about the entity groups, namespaces, entity kinds, and properties your application uses, as well as the property representations for each property.

The special entity kind `__namespace__` can be used to find all the namespaces used in your application entities.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("__namespace__").
      select("__key__").
      where("__key__", ">=", datastore.key("__namespace__", "g")).
      where("__key__", "<", datastore.key("__namespace__",="" "h"))="" namespaces="datastore.run(query).map" do="" |entity|="" entity.key.name="" end="">

The special entity kind `__kind__` can be used to return all the kinds used in your application.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("__kind__").
      select("__key__")
    
    kinds = datastore.run(query).map do |entity|
      entity.key.name
    end

Property queries return entities of kind `__property__` denoting the indexed properties associated with an entity kind. (Unindexed properties are not included.)
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("__property__").
      select("__key__")
    
    entities = datastore.run(query)
    properties_by_kind = entities.each_with_object({}) do |entity, memo|
      kind = entity.key.parent.name
      prop = entity.key.name
      memo[kind] ||= []
      memo[kind] < prop="" end="">

Property queries support ancestor filtering on a `__kind__` or `__property__` key, to limit the query results to a single kind or property. The `property_representation` property in the entity representing property `p` of kind `k` is an array containing all representations of `p`'s value in any entity of kind `k`.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    ancestor_key = datastore.key "__kind__", "Task"
    query = datastore.query("__property__").
      ancestor(ancestor_key)
    
    entities = datastore.run(query)
    representations = entities.each_with_object({}) do |entity, memo|
      property_name = entity.key.name
      property_types = entity["property_representation"]
      memo[property_name] = property_types
    end

Property queries can also be filtered with a range over the pseudo-property `__key__`, where the keys denote either `__kind__` or `__property__` entities.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    start_key = datastore.key "__property__", "priority"
    start_key.parent = datastore.key "__kind__", "Task"
    query = datastore.query("__property__").
      select("__key__").
      where("__key__", ">=", start_key)
    
    entities = datastore.run(query)
    properties_by_kind = entities.each_with_object({}) do |entity, memo|
      kind = entity.key.parent.name
      prop = entity.key.name
      memo[kind] ||= []
      memo[kind] < prop="" end="">

## Configuring timeout

You can configure the request `timeout` value in seconds.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new timeout: 120

## Additional information

Google Cloud Datastore can be configured to use an emulator or to enable gRPC's logging. To learn more, see the [Emulator guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/EMULATOR "Emulator guide") and [Logging guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/LOGGING "Logging guide").

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
