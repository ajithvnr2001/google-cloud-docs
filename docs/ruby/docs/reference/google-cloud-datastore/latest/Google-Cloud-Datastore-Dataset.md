---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset/
title: Firestore in Datastore mode API - Class Google::Cloud::Datastore::Dataset (v2.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:55.536274+00:00
---

# Firestore in Datastore mode API - Class Google::Cloud::Datastore::Dataset (v2.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Firestore in Datastore mode API - Class Google::Cloud::Datastore::Dataset (v2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.4 

Reference documentation and code samples for the Firestore in Datastore mode API class Google::Cloud::Datastore::Dataset.

## Dataset

Dataset is the data saved in a project's Datastore. Dataset is analogous to a database in relational database world.

Dataset is the main object for interacting with Google Datastore. [Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity "Google::Cloud::Datastore::Entity \(class\)") objects are created, read, updated, and deleted by Dataset.

See [Google::Cloud#datastore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud#Google__Cloud_datastore_instance_ "Google::Cloud#datastore \(method\)")

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    
    tasks = datastore.run query

## Methods 

### #allocate_ids
    
    
    def allocate_ids(incomplete_key, count = 1) -> Array<Google::Cloud::Datastore::Key>

Generate IDs for a Key before creating an entity.

**Parameters**

  * **incomplete_key** ([Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key)) — A Key without `id` or `name` set. 
  * **count** (String) — The number of new key IDs to create. 



**Returns**

  * (Array<[Google::Cloud::Datastore::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key)>) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task"
    task_keys = datastore.allocate_ids task_key, 5

### #commit
    
    
    def commit() { |commit| ... } -> Array<Google::Cloud::Datastore::Entity>

Make multiple changes in a single commit.

**Yields**

  * (commit) — a block for making changes 



**Yield Parameter**

  * **commit** ([Commit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Commit)) — The object that changes are made on 



**Returns**

  * (Array<[Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)>) — The entities that were persisted. 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    datastore.commit do |c|
      c.save task3, task4
      c.delete task1, task2
    end

### #database_id
    
    
    def database_id() -> String

The Datastore database connected to.

**Returns**

  * (String) — ID of the database 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new(
      project_id: "my-todo-project",
      credentials: "/path/to/keyfile.json",
      database_id: "my-database"
    )
    
    datastore.database_id #=> "my-database"

### #delete
    
    
    def delete(*entities_or_keys) -> Boolean

Remove entities from the Datastore.

**Parameter**

  * **entities_or_keys** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity), [Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key)) — One or more Entity or Key objects to remove. 



**Returns**

  * (Boolean) — Returns `true` if successful 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    datastore.delete task1, task2

### #entity
    
    
    def entity(*key_or_path, project: nil, namespace: nil) { |entity| ... } -> Google::Cloud::Datastore::Entity

Create a new empty Entity instance. This is a convenience method to make the creation of Entity objects easier.

**Parameters**

  * **key_or_path** ([Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key), Array<Array(String,(String|Integer|nil))>) — An optional list of pairs for the key's path. Each pair may include the key's kind (String) and an id (Integer) or name (String). This is optional. 
  * **project** (String) _(defaults to: nil)_ — The project of the Key. This is optional. 
  * **namespace** (String) _(defaults to: nil)_ — namespace kind of the Key. This is optional. 



**Yields**

  * (entity) — a block yielding a new entity 



**Yield Parameter**

  * **entity** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — the newly created entity object 



**Returns**

  * ([Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) 



**Examples**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity

The previous example is equivalent to:
    
    
    require "google/cloud/datastore"
    
    task = Google::Cloud::Datastore::Entity.new

The key can also be passed in as an object:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", "sampleTask"
    task = datastore.entity task_key

Or the key values can be passed in as parameters:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity "Task", "sampleTask"

The previous example is equivalent to:
    
    
    require "google/cloud/datastore"
    
    task_key = Google::Cloud::Datastore::Key.new "Task", "sampleTask"
    task = Google::Cloud::Datastore::Entity.new
    task.key = task_key

The newly created entity can also be configured using block:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity "Task", "sampleTask" do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 4
      t["description"] = "Learn Cloud Datastore"
    end

The previous example is equivalent to:
    
    
    require "google/cloud/datastore"
    
    task_key = Google::Cloud::Datastore::Key.new "Task", "sampleTask"
    task = Google::Cloud::Datastore::Entity.new
    task.key = task_key
    task["type"] = "Personal"
    task["done"] = false
    task["priority"] = 4
    task["description"] = "Learn Cloud Datastore"

### #filter
    
    
    def filter(name, operator, value) -> Google::Cloud::Datastore::Filter

Create a new Filter instance. This is a convenience method to make the creation of Filter objects easier.

**Parameters**

  * **name** (String) — The property to filter by. 
  * **operator** (String) — The operator to filter by. Defaults to nil. 
  * **value** (Object) — 

The value to compare the property to. Defaults to nil. Possible values are:

    * Integer
    * Float/BigDecimal
    * String
    * Boolean
    * Array
    * Date/Time
    * StringIO
    * Google::Cloud::Datastore::Key
    * Google::Cloud::Datastore::Entity
    * nil



**Returns**

  * ([Google::Cloud::Datastore::Filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Filter)) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    filter = datastore.filter("done", "=", false)

### #find
    
    
    def find(key_or_kind, id_or_name = nil, consistency: nil, read_time: nil) -> Google::Cloud::Datastore::Entity, nil

**Aliases**

  * [#get](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_get_instance_)



Retrieve an entity by key.

**Parameters**

  * **key_or_kind** ([Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key), String) — A Key object or `kind` string value. 
  * **id_or_name** (Integer, String, nil) — The Key's `id` or `name` value if a `kind` was provided in the first parameter. 
  * **consistency** (Symbol) _(defaults to: nil)_ — The non-transactional read consistency to use. Cannot be set to `:strong` for global queries. Accepted values are `:eventual` and `:strong`.

The default consistency depends on the type of lookup used. See [Eventual Consistency in Google Cloud Datastore](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8) for more information. 

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities as they were at the given time. This may not be older than 270 seconds. Optional 



**Returns**

  * ([Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity), nil) 



**Examples**

Finding an entity with a key:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", "sampleTask"
    task = datastore.find task_key

Finding an entity with a `kind` and `id`/`name`:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"

### #find_all
    
    
    def find_all(*keys, consistency: nil, read_time: nil) -> Google::Cloud::Datastore::Dataset::LookupResults

**Aliases**

  * [#lookup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_lookup_instance_)



Retrieve the entities for the provided keys. The order of results is undefined and has no relation to the order of `keys` arguments.

**Parameters**

  * **keys** ([Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key)) — One or more Key objects to find records for. 
  * **consistency** (Symbol) _(defaults to: nil)_ — The non-transactional read consistency to use. Cannot be set to `:strong` for global queries. Accepted values are `:eventual` and `:strong`.

The default consistency depends on the type of lookup used. See [Eventual Consistency in Google Cloud Datastore](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8) for more information. 

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities as they were at the given time. This may not be older than 270 seconds. Optional 



**Returns**

  * ([Google::Cloud::Datastore::Dataset::LookupResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-LookupResults)) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key1 = datastore.key "Task", "sampleTask1"
    task_key2 = datastore.key "Task", "sampleTask2"
    tasks = datastore.find_all task_key1, task_key2

### #get
    
    
    def get(key_or_kind, id_or_name = nil, consistency: nil, read_time: nil) -> Google::Cloud::Datastore::Entity, nil

**Alias Of** : [#find](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_find_instance_)

Retrieve an entity by key.

**Parameters**

  * **key_or_kind** ([Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key), String) — A Key object or `kind` string value. 
  * **id_or_name** (Integer, String, nil) — The Key's `id` or `name` value if a `kind` was provided in the first parameter. 
  * **consistency** (Symbol) _(defaults to: nil)_ — The non-transactional read consistency to use. Cannot be set to `:strong` for global queries. Accepted values are `:eventual` and `:strong`.

The default consistency depends on the type of lookup used. See [Eventual Consistency in Google Cloud Datastore](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8) for more information. 

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities as they were at the given time. This may not be older than 270 seconds. Optional 



**Returns**

  * ([Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity), nil) 



**Examples**

Finding an entity with a key:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", "sampleTask"
    task = datastore.find task_key

Finding an entity with a `kind` and `id`/`name`:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"

### #gql
    
    
    def gql(query, bindings = {}) -> Google::Cloud::Datastore::GqlQuery

Create a new GqlQuery instance. This is a convenience method to make the creation of GqlQuery objects easier.

**Parameters**

  * **query** (String) — The GQL query string. 
  * **bindings** (Hash) — Named bindings for the GQL query string, each key must match regex `[A-Za-z_$][A-Za-z_$0-9]*`, must not match regex `__.*__`, and must not be `""`. The value must be an `Object` that can be stored as an Entity property value, or a `Cursor`. 



**Returns**

  * ([Google::Cloud::Datastore::GqlQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-GqlQuery)) 



**Examples**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = datastore.gql "SELECT * FROM Task WHERE done = @done",
                              done: false
    tasks = datastore.run gql_query

The previous example is equivalent to:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = Google::Cloud::Datastore::GqlQuery.new
    gql_query.query_string = "SELECT * FROM Task WHERE done = @done"
    gql_query.named_bindings = {done: false}
    tasks = datastore.run gql_query

### #insert
    
    
    def insert(*entities) -> Array<Google::Cloud::Datastore::Entity>

Insert one or more entities to the Datastore. An InvalidArgumentError will raised if the entities cannot be inserted.

**Parameter**

  * **entities** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — One or more entity objects to be inserted. 



**Returns**

  * (Array<[Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)>) 



**Examples**

Insert a new entity:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity "Task" do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 4
      t["description"] = "Learn Cloud Datastore"
    end
    task.key.id #=> nil
    datastore.insert task
    task.key.id #=> 123456

Insert multiple new entities in a batch:
    
    
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
    
    task_key1, task_key2 = datastore.insert(task1, task2).map(&:key)

### #key
    
    
    def key(*path, project: nil, namespace: nil) -> Google::Cloud::Datastore::Key

Create a new Key instance. This is a convenience method to make the creation of Key objects easier.

**Parameters**

  * **path** (Array<Array(String,(String|Integer|nil))>) — An optional list of pairs for the key's path. Each pair may include the key's kind (String) and an id (Integer) or name (String). This is optional. 
  * **project** (String) _(defaults to: nil)_ — The project of the Key. This is optional. 
  * **namespace** (String) _(defaults to: nil)_ — namespace kind of the Key. This is optional. 



**Returns**

  * ([Google::Cloud::Datastore::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key)) 



**Examples**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key = datastore.key "Task", "sampleTask"

The previous example is equivalent to:
    
    
    require "google/cloud/datastore"
    
    task_key = Google::Cloud::Datastore::Key.new "Task", "sampleTask"

Create an empty key:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    key = datastore.key

Create an incomplete key:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    key = datastore.key "User"

Create a key with a parent:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    key = datastore.key [["TaskList", "default"],
                         ["Task", "sampleTask"]]
    key.path #=> [["TaskList", "default"], ["Task", "sampleTask"]]

Create a key with multi-level ancestry:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    key = datastore.key([
      ["User", "alice"],
      ["TaskList", "default"],
      ["Task", "sampleTask"]
    ])
    key.path.count #=> 3
    key.path[0] #=> ["User", "alice"]
    key.path[1] #=> ["TaskList", "default"]
    key.path[2] #=> ["Task", "sampleTask"]

Create an incomplete key with a parent:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    key = datastore.key "TaskList", "default", "Task"
    key.path #=> [["TaskList", "default"], ["Task", nil]]

Create a key with a project and namespace:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    key = datastore.key ["TaskList", "default"], ["Task", "sampleTask"],
                        project: "my-todo-project",
                        namespace: "example-ns"
    key.path #=> [["TaskList", "default"], ["Task", "sampleTask"]]
    key.project #=> "my-todo-project"
    key.namespace #=> "example-ns"

### #lookup
    
    
    def lookup(*keys, consistency: nil, read_time: nil) -> Google::Cloud::Datastore::Dataset::LookupResults

**Alias Of** : [#find_all](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_find_all_instance_)

Retrieve the entities for the provided keys. The order of results is undefined and has no relation to the order of `keys` arguments.

**Parameters**

  * **keys** ([Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Key)) — One or more Key objects to find records for. 
  * **consistency** (Symbol) _(defaults to: nil)_ — The non-transactional read consistency to use. Cannot be set to `:strong` for global queries. Accepted values are `:eventual` and `:strong`.

The default consistency depends on the type of lookup used. See [Eventual Consistency in Google Cloud Datastore](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8) for more information. 

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities as they were at the given time. This may not be older than 270 seconds. Optional 



**Returns**

  * ([Google::Cloud::Datastore::Dataset::LookupResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-LookupResults)) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_key1 = datastore.key "Task", "sampleTask1"
    task_key2 = datastore.key "Task", "sampleTask2"
    tasks = datastore.find_all task_key1, task_key2

### #project
    
    
    def project()

**Alias Of** : [#project_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_project_id_instance_)

The Datastore project connected to.

**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new(
      project_id: "my-todo-project",
      credentials: "/path/to/keyfile.json"
    )
    
    datastore.project_id #=> "my-todo-project"

### #project_id
    
    
    def project_id()

**Aliases**

  * [#project](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_project_instance_)



The Datastore project connected to.

**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new(
      project_id: "my-todo-project",
      credentials: "/path/to/keyfile.json"
    )
    
    datastore.project_id #=> "my-todo-project"

### #query
    
    
    def query(*kinds) -> Google::Cloud::Datastore::Query

Create a new Query instance. This is a convenience method to make the creation of Query objects easier.

**Parameter**

  * **kinds** (String) — The kind of entities to query. This is optional. 



**Returns**

  * ([Google::Cloud::Datastore::Query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query)) 



**Examples**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    tasks = datastore.run query

The previous example is equivalent to:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = Google::Cloud::Datastore::Query.new.
      kind("Task").
      where("done", "=", false)
    tasks = datastore.run query

### #read_only_transaction
    
    
    def read_only_transaction(read_time: nil) { |tx| ... }

**Aliases**

  * [#snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_snapshot_instance_)



Creates a read-only transaction that provides a consistent snapshot of Cloud Datastore. This can be useful when multiple reads are needed to render a page or export data that must be consistent.

A read-only transaction cannot modify entities; in return they do not contend with other read-write or read-only transactions. Using a read-only transaction for transactions that only read data will potentially improve throughput.

Read-only single-group transactions never fail due to concurrent modifications, so you don't have to implement retries upon failure. However, multi-entity-group transactions can fail due to concurrent modifications, so these should have retries.

**Parameter**

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities at the given time. This may not be older than 60 seconds. Optional 



**Yields**

  * (tx) — a block yielding a new transaction 



**Yield Parameter**

  * **tx** ([ReadOnlyTransaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-ReadOnlyTransaction)) — the transaction object 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_list_key = datastore.key "TaskList", "default"
    query = datastore.query("Task").
      ancestor(task_list_key)
    
    tasks = nil
    
    datastore.read_only_transaction do |tx|
      task_list = tx.find task_list_key
      if task_list
        tasks = tx.run query
      end
    end

### #run
    
    
    def run(query, namespace: nil, consistency: nil, read_time: nil, explain_options: nil) -> Google::Cloud::Datastore::Dataset::QueryResults

**Aliases**

  * [#run_query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_run_query_instance_)



Retrieve entities specified by a Query.

**Parameters**

  * **query** ([Query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query), [GqlQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-GqlQuery)) — The object with the search criteria. 
  * **namespace** (String) _(defaults to: nil)_ — The namespace the query is to run within. 
  * **consistency** (Symbol) _(defaults to: nil)_ — The non-transactional read consistency to use. Cannot be set to `:strong` for global queries. Accepted values are `:eventual` and `:strong`.

The default consistency depends on the type of query used. See [Eventual Consistency in Google Cloud Datastore](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8) for more information. 

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities as they were at the given time. This may not be older than 270 seconds. Optional. 
  * **explain_options** (Hash, Google::Cloud::Datastore::V1::ExplainOptions) _(defaults to: nil)_ — The options for query explanation. Provide this argument to enable explain metrics. If this argument is left unset, the results will not include explain metrics. See V1::ExplainOptions for details. Optional. 



**Returns**

  * ([Google::Cloud::Datastore::Dataset::QueryResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults)) 



**Examples**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    tasks = datastore.run query

Run an ancestor query with eventual consistency:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_list_key = datastore.key "TaskList", "default"
    query = datastore.query.kind("Task").
      ancestor(task_list_key)
    
    tasks = datastore.run query, consistency: :eventual

Run the query within a namespace with the `namespace` option:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    tasks = datastore.run query, namespace: "example-ns"

Run the query with a GQL string.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = datastore.gql "SELECT * FROM Task WHERE done = @done",
                              done: false
    tasks = datastore.run gql_query

Run the GQL query within a namespace with `namespace` option:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = datastore.gql "SELECT * FROM Task WHERE done = @done",
                              done: false
    tasks = datastore.run gql_query, namespace: "example-ns"

Run the query with explain options to get query plan and execution statistics.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    results = datastore.run query, explain_options: { analyze: true }
    
    # The explain_metrics are available on the results object only after
    # all results have been retrieved. You must iterate through all
    # pages of results to get the metrics.
    all_tasks = []
    loop do
      results.each { |task| all_tasks << task }
      break unless results.next?
      results = results.next
    end
    
    # The `results` object now holds the last page of results,
    # and contains the explain_metrics.
    if results.explain_metrics
      stats = results.explain_metrics.execution_stats
      puts "Results returned: #{stats.results_returned}"
      puts "Read operations: #{stats.read_operations}"
    end

Run the query with explain options using a `Google::Cloud::Datastore::V1::ExplainOptions` object.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    explain_options = Google::Cloud::Datastore::V1::ExplainOptions.new
    results = datastore.run query, explain_options: explain_options
    
    # You must iterate through all pages of results to get the metrics.
    loop do
      break unless results.next?
      results = results.next
    end
    
    if results.explain_metrics
      stats = results.explain_metrics.execution_stats
      puts "Read operations: #{stats.read_operations}"
    end

### #run_aggregation
    
    
    def run_aggregation(aggregate_query, namespace: nil, consistency: nil, read_time: nil, explain_options: nil) -> Google::Cloud::Datastore::Dataset::AggregateQueryResults

Retrieve aggregate results specified by an AggregateQuery.

**Parameters**

  * **aggregate_query** ([AggregateQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-AggregateQuery), [GqlQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-GqlQuery)) — The object with the aggregate criteria. 
  * **namespace** (String) _(defaults to: nil)_ — The namespace the query is to run within. 
  * **consistency** (Symbol) _(defaults to: nil)_ — The non-transactional read consistency to use. Cannot be set to `:strong` for global queries. Accepted values are `:eventual` and `:strong`. 
  * **read_time** (Time) _(defaults to: nil)_ — Reads entities as they were at the given time. This may not be older than 270 seconds. Optional

The default consistency depends on the type of query used. See [Eventual Consistency in Google Cloud Datastore](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8) for more information. 

  * **explain_options** (Hash, Google::Cloud::Datastore::V1::ExplainOptions) _(defaults to: nil)_ — The options for query explanation. Provide this argument to enable explain metrics. If this argument is left unset, the results will not include explain metrics. See V1::ExplainOptions for details. Optional. 



**Returns**

  * ([Google::Cloud::Datastore::Dataset::AggregateQueryResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-AggregateQueryResults)) 



**Examples**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
                     .where("done", "=", false)
    
    aggregate_query = query.aggregate_query
    
    res = datastore.run_aggregation aggregate_query

Run an aggregate ancestor query with eventual consistency:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_list_key = datastore.key "TaskList", "default"
    query = datastore.query.kind("Task")
                     .ancestor(task_list_key)
    
    aggregate_query = query.aggregate_query
    
    res = datastore.run_aggregation aggregate_query, consistency: :eventual

Run the aggregate query within a namespace with the `namespace` option:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
                     .where("done", "=", false)
    
    aggregate_query = query.aggregate_query
    
    res = datastore.run_aggregation aggregate_query, namespace: "example-ns"

Run the aggregate query with a GQL string.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = datastore.gql "SELECT COUNT(*) FROM Task WHERE done = @done",
                              done: false
    res = datastore.run_aggregation gql_query

Run the aggregate GQL query within a namespace with `namespace` option:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = datastore.gql "SELECT COUNT(*) FROM Task WHERE done = @done",
                              done: false
    res = datastore.run_aggregation gql_query, namespace: "example-ns"

Run the aggregate query with explain options to get query plan and execution statistics.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    aggregate_query = query.aggregate_query.add_count aggregate_alias: "total"
    results = datastore.run_aggregation aggregate_query, explain_options: { analyze: true }
    
    if results.explain_metrics
      stats = results.explain_metrics.execution_stats
      puts "Read operations: #{stats.read_operations}"
    end

### #run_query
    
    
    def run_query(query, namespace: nil, consistency: nil, read_time: nil, explain_options: nil) -> Google::Cloud::Datastore::Dataset::QueryResults

**Alias Of** : [#run](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_run_instance_)

Retrieve entities specified by a Query.

**Parameters**

  * **query** ([Query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Query), [GqlQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-GqlQuery)) — The object with the search criteria. 
  * **namespace** (String) _(defaults to: nil)_ — The namespace the query is to run within. 
  * **consistency** (Symbol) _(defaults to: nil)_ — The non-transactional read consistency to use. Cannot be set to `:strong` for global queries. Accepted values are `:eventual` and `:strong`.

The default consistency depends on the type of query used. See [Eventual Consistency in Google Cloud Datastore](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8) for more information. 

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities as they were at the given time. This may not be older than 270 seconds. Optional. 
  * **explain_options** (Hash, Google::Cloud::Datastore::V1::ExplainOptions) _(defaults to: nil)_ — The options for query explanation. Provide this argument to enable explain metrics. If this argument is left unset, the results will not include explain metrics. See V1::ExplainOptions for details. Optional. 



**Returns**

  * ([Google::Cloud::Datastore::Dataset::QueryResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults)) 



**Examples**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    tasks = datastore.run query

Run an ancestor query with eventual consistency:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_list_key = datastore.key "TaskList", "default"
    query = datastore.query.kind("Task").
      ancestor(task_list_key)
    
    tasks = datastore.run query, consistency: :eventual

Run the query within a namespace with the `namespace` option:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").
      where("done", "=", false)
    tasks = datastore.run query, namespace: "example-ns"

Run the query with a GQL string.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = datastore.gql "SELECT * FROM Task WHERE done = @done",
                              done: false
    tasks = datastore.run gql_query

Run the GQL query within a namespace with `namespace` option:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    gql_query = datastore.gql "SELECT * FROM Task WHERE done = @done",
                              done: false
    tasks = datastore.run gql_query, namespace: "example-ns"

Run the query with explain options to get query plan and execution statistics.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    results = datastore.run query, explain_options: { analyze: true }
    
    # The explain_metrics are available on the results object only after
    # all results have been retrieved. You must iterate through all
    # pages of results to get the metrics.
    all_tasks = []
    loop do
      results.each { |task| all_tasks << task }
      break unless results.next?
      results = results.next
    end
    
    # The `results` object now holds the last page of results,
    # and contains the explain_metrics.
    if results.explain_metrics
      stats = results.explain_metrics.execution_stats
      puts "Results returned: #{stats.results_returned}"
      puts "Read operations: #{stats.read_operations}"
    end

Run the query with explain options using a `Google::Cloud::Datastore::V1::ExplainOptions` object.
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    explain_options = Google::Cloud::Datastore::V1::ExplainOptions.new
    results = datastore.run query, explain_options: explain_options
    
    # You must iterate through all pages of results to get the metrics.
    loop do
      break unless results.next?
      results = results.next
    end
    
    if results.explain_metrics
      stats = results.explain_metrics.execution_stats
      puts "Read operations: #{stats.read_operations}"
    end

### #save
    
    
    def save(*entities) -> Array<Google::Cloud::Datastore::Entity>

**Aliases**

  * [#upsert](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_upsert_instance_)



Persist one or more entities to the Datastore.

**Parameter**

  * **entities** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — One or more entity objects to be saved. 



**Returns**

  * (Array<[Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)>) 



**Examples**

Insert a new entity:
    
    
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

Insert multiple new entities in a batch:
    
    
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
    
    task_key1, task_key2 = datastore.save(task1, task2).map(&:key)

Update an existing entity:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"
    task["priority"] = 5
    datastore.save task

### #snapshot
    
    
    def snapshot(read_time: nil) { |tx| ... }

**Alias Of** : [#read_only_transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_read_only_transaction_instance_)

Creates a read-only transaction that provides a consistent snapshot of Cloud Datastore. This can be useful when multiple reads are needed to render a page or export data that must be consistent.

A read-only transaction cannot modify entities; in return they do not contend with other read-write or read-only transactions. Using a read-only transaction for transactions that only read data will potentially improve throughput.

Read-only single-group transactions never fail due to concurrent modifications, so you don't have to implement retries upon failure. However, multi-entity-group transactions can fail due to concurrent modifications, so these should have retries.

**Parameter**

  * **read_time** (Time) _(defaults to: nil)_ — Reads entities at the given time. This may not be older than 60 seconds. Optional 



**Yields**

  * (tx) — a block yielding a new transaction 



**Yield Parameter**

  * **tx** ([ReadOnlyTransaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-ReadOnlyTransaction)) — the transaction object 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task_list_key = datastore.key "TaskList", "default"
    query = datastore.query("Task").
      ancestor(task_list_key)
    
    tasks = nil
    
    datastore.read_only_transaction do |tx|
      task_list = tx.find task_list_key
      if task_list
        tasks = tx.run query
      end
    end

### #transaction
    
    
    def transaction(deadline: nil, previous_transaction: nil) { |tx| ... }

Creates a Datastore Transaction.

Transactions using the block syntax are committed upon block completion and are automatically retried when known errors are raised during commit. All other errors will be passed on.

All changes are accumulated in memory until the block completes. Transactions will be automatically retried when possible, until `deadline` is reached. This operation makes separate API requests to begin and commit the transaction.

**Parameters**

  * **deadline** (Numeric) _(defaults to: nil)_ — The total amount of time in seconds the transaction has to succeed. The default is `60`. 
  * **previous_transaction** (String) _(defaults to: nil)_ — The transaction identifier of a transaction that is being retried. Read-write transactions may fail due to contention. A read-write transaction can be retried by specifying `previous_transaction` when creating the new transaction.

Specifying `previous_transaction` provides information that can be used to improve throughput. In particular, if transactional operations A and B conflict, specifying the `previous_transaction` can help to prevent livelock. (See [Transaction#id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Transaction#Google__Cloud__Datastore__Transaction_id_instance_ "Google::Cloud::Datastore::Transaction#id \(method\)")) 




**Yields**

  * (tx) — a block yielding a new transaction 



**Yield Parameter**

  * **tx** ([Transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Transaction)) — the transaction object 



**Examples**

Runs the given block in a database transaction:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity "Task", "sampleTask" do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 4
      t["description"] = "Learn Cloud Datastore"
    end
    
    datastore.transaction do |tx|
      if tx.find(task.key).nil?
        tx.save task
      end
    end

If no block is given, a Transaction object is returned:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.entity "Task", "sampleTask" do |t|
      t["type"] = "Personal"
      t["done"] = false
      t["priority"] = 4
      t["description"] = "Learn Cloud Datastore"
    end
    
    tx = datastore.transaction
    begin
      if tx.find(task.key).nil?
        tx.save task
      end
      tx.commit
    rescue
      tx.rollback
    end

### #update
    
    
    def update(*entities) -> Array<Google::Cloud::Datastore::Entity>

Update one or more entities to the Datastore. An InvalidArgumentError will raised if the entities cannot be updated.

**Parameter**

  * **entities** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — One or more entity objects to be updated. 



**Returns**

  * (Array<[Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)>) 



**Examples**

Update an existing entity:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"
    task["done"] = true
    datastore.save task

Update multiple new entities in a batch:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task").where("done", "=", false)
    tasks = datastore.run query
    tasks.each { |t| t["done"] = true }
    datastore.update tasks

### #upsert
    
    
    def upsert(*entities) -> Array<Google::Cloud::Datastore::Entity>

**Alias Of** : [#save](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_save_instance_)

Persist one or more entities to the Datastore.

**Parameter**

  * **entities** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — One or more entity objects to be saved. 



**Returns**

  * (Array<[Google::Cloud::Datastore::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)>) 



**Examples**

Insert a new entity:
    
    
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

Insert multiple new entities in a batch:
    
    
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
    
    task_key1, task_key2 = datastore.save(task1, task2).map(&:key)

Update an existing entity:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    task = datastore.find "Task", "sampleTask"
    task["priority"] = 5
    datastore.save task

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
