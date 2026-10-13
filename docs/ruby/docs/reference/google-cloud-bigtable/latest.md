---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/
title: Cloud Bigtable \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:36.398046+00:00
---

# Cloud Bigtable  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable Stay organized with collections  Save and categorize content based on your preferences. 

2.13.0 (latest)  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.5 

Cloud Bigtable is a petabyte-scale, fully managed NoSQL database service for large analytical and operational workloads. Ideal for ad tech, fintech, and IoT, Cloud Bigtable offers consistent sub-10ms latency. Replication provides higher availability, higher durability, and resilience in the face of zonal failures. Cloud Bigtable is designed with a storage engine for machine learning applications and provides easy integration with open source big data tools.

For more information about Cloud Bigtable, read the [Cloud Bigtable Documentation](https://cloud.google.com/bigtable/docs/).

The goal of google-cloud is to provide an API that is comfortable to Rubyists. Your authentication credentials are detected automatically in Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run. In other environments you can configure authentication easily, either directly in your code or via environment variables. Read more about the options for connecting in the [Authentication Guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/AUTHENTICATION "Authentication Guide").

## Creating instances and clusters

When you first use Cloud Bigtable, you must create an instance, which is an allocation of resources that are used by Cloud Bigtable. When you create an instance, you must specify at least one cluster. Clusters describe where your data is stored and how many nodes are used for your data.

To create an instance, use the instance admin client, which you can get from [Project#instance_admin_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Project#Google__Cloud__Bigtable__Project_instance_admin_client_instance_ "Google::Cloud::Bigtable::Project#instance_admin_client \(method\)"). The following example creates a production instance with one cluster and three nodes:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    instance_client = bigtable.instance_admin_client
    
    instance_attrs = {
      display_name: "Instance for user data",
      labels: { "env" => "dev"}
    }
    clusters = {
      "test-cluster" => {
        location: "us-east1-b",
        nodes: 3,
        storage_type: :SSD
      }
    }
    job = instance_client.create_instance(
      parent: "projects/my-project",
      instance_id: "my-instance",
      instance: instance_attrs,
      clusters: clusters
    )
    
    job.done? #=> false
    
    # To block until the operation completes.
    job.wait_until_done!
    job.done? #=> true
    
    if job.error?
      status = job.error
    else
      instance = job.response.instance
    end

You can also create a low-cost development instance for development and testing, with performance limited to the equivalent of a one-node cluster. There are no monitoring or throughput guarantees; replication is not available; and the SLA does not apply. When creating a development instance, you do not specify `nodes` for your clusters:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    instance_client = bigtable.instance_admin_client
    
    instance_attrs = {
      display_name: "Instance for user data",
      type: :DEVELOPMENT,
      labels: { "env" => "dev"}
    }
    clusters = {
      "test-cluster" => {
        location: "us-east1-b", # nodes not allowed
      }
    }
    job = instance_client.create_instance(
      parent: "projects/my-project",
      instance_id: "my-instance",
      instance: instance_attrs,
      clusters: clusters
    )
    
    job.done? #=> false
    
    # Reload job until completion.
    job.wait_until_done!
    job.done? #=> true
    
    if job.error?
      status = job.error
    else
      instance = job.response.instance
    end

You can upgrade a development instance to a production instance at any time.

## Creating tables

Cloud Bigtable stores data in massively scalable tables, each of which is a sorted key/value map. The table is composed of rows, each of which typically describes a single entity, and columns, which contain individual values for each row. Each row is indexed by a single row key, and columns that are related to one another are typically grouped together into a column family. Each column is identified by a combination of the column family and a column qualifier, which is a unique name within the column family.

Each row/column intersection can contain multiple cells, or versions, at different timestamps, providing a record of how the stored data has been altered over time. Cloud Bigtable tables are sparse; if a cell does not contain any data, it does not take up any space.

To create an instance, use the table admin client, which you can get from [Project#table_admin_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Project#Google__Cloud__Bigtable__Project_table_admin_client_instance_ "Google::Cloud::Bigtable::Project#table_admin_client \(method\)"), as illustrated in the following example:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table_client = bigtable.table_admin_client
    
    instance_name = table_client.instance_path project: "my-project", instance: "my-instance"
    table = table_client.create_table parent: instance_name,
                                      table_id: "my-table",
                                      table: {}
    
    puts table.name

When you create a table, you can specify the column families to use in the table, as well as a list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions):
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table_client = bigtable.table_admin_client
    
    instance_name = table_client.instance_path project: "my-project", instance: "my-instance"
    initial_splits = [
      {key: "user-00001"},
      {key: "user-100000"},
      {key: "others"}
    ]
    column_families = {
      "cf1" => {
        gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.max_num_versions(5)
      },
      "cf2" => {
        gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.max_age(600)
      },
      "cf3" => {
        gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.union(
          Google::Cloud::Bigtable::Admin::V2::GcRule.max_age(1800),
          Google::Cloud::Bigtable::Admin::V2::GcRule.max_num_versions(3)
        )
      }
    }
    table = table_client.create_table parent: instance_name,
                                      table_id: "my-table",
                                      table: {column_families: column_families},
                                      initial_splits: initial_splits
    
    puts table

You can also add, update, and delete column families later:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table_client = bigtable.table_admin_client
    
    table_name = table_client.table_path project: "my-project",
                                         instance: "my-instance",
                                         table: "my-table"
    modifications = [
      {
        id: "cf4",
        create: {
          gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.max_age(600)
        }
      },
      {
        id: "cf5",
        create: {
          gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.max_num_versions(5)
        }
      },
      {
        id: "cf2",
        update: {
          gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.union(
            Google::Cloud::Bigtable::Admin::V2::GcRule.max_age(600),
            Google::Cloud::Bigtable::Admin::V2::GcRule.max_num_versions(3)
          )
        }
      },
      {
        id: "cf3",
        drop: true
      }
    ]
    table_client.modify_column_families name: table_name, modifications: modifications

## Writing data

The [Table](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Table "Google::Cloud::Bigtable::Table \(class\)") class allows you to perform the following types of writes:

  * Simple writes
  * Increments and appends
  * Conditional writes
  * Batch writes



See [Cloud Bigtable writes](https://cloud.google.com/bigtable/docs/writes) for detailed information about writing data.

### Simple writes

Use [Table#mutate_row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-MutationOperations#Google__Cloud__Bigtable__MutationOperations_mutate_row_instance_ "Google::Cloud::Bigtable::MutationOperations#mutate_row \(method\)") to make one or more mutations to a single row:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    
    table = bigtable.table("my-instance", "my-table")
    
    entry = table.new_mutation_entry("user-1")
    entry.set_cell(
      "cf1",
      "field1",
      "XYZ",
      timestamp: (Time.now.to_f * 1000000).round(-3) # microseconds
    ).delete_cells("cf2", "field02")
    
    table.mutate_row(entry)

### Increments and appends

If you want to append data to an existing value or increment an existing numeric value, use [Table#read_modify_write_row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-MutationOperations#Google__Cloud__Bigtable__MutationOperations_read_modify_write_row_instance_ "Google::Cloud::Bigtable::MutationOperations#read_modify_write_row \(method\)"):
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table("my-instance", "my-table")
    
    rule_1 = table.new_read_modify_write_rule("cf", "field01")
    rule_1.append("append-xyz")
    
    rule_2 = table.new_read_modify_write_rule("cf", "field01")
    rule_2.increment(1)
    
    row = table.read_modify_write_row("user01", [rule_1, rule_2])
    
    puts row.cells

Do not use `read_modify_write_row` if you are using an app profile that has multi-cluster routing. (See [AppProfile#routing_policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-AppProfile#Google__Cloud__Bigtable__AppProfile_routing_policy_instance_ "Google::Cloud::Bigtable::AppProfile#routing_policy \(method\)").)

### Conditional writes

To check a row for a condition and then, depending on the result, write data to that row, use [Table#check_and_mutate_row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-MutationOperations#Google__Cloud__Bigtable__MutationOperations_check_and_mutate_row_instance_ "Google::Cloud::Bigtable::MutationOperations#check_and_mutate_row \(method\)"):
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table("my-instance", "my-table")
    
    predicate_filter = Google::Cloud::Bigtable::RowFilter.key("user-10")
    on_match_mutations = Google::Cloud::Bigtable::MutationEntry.new
    on_match_mutations.set_cell(
      "cf1",
      "field1",
      "XYZ",
      timestamp: (Time.now.to_f * 1000000).round(-3) # microseconds
    ).delete_cells("cf2", "field02")
    
    otherwise_mutations = Google::Cloud::Bigtable::MutationEntry.new
    otherwise_mutations.delete_from_family("cf3")
    
    predicate_matched = table.check_and_mutate_row(
      "user01",
      predicate_filter,
      on_match: on_match_mutations,
      otherwise: otherwise_mutations
    )
    
    if predicate_matched
      puts "All predicates matched"
    end

Do not use `check_and_mutate_row` if you are using an app profile that has multi-cluster routing. (See [AppProfile#routing_policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-AppProfile#Google__Cloud__Bigtable__AppProfile_routing_policy_instance_ "Google::Cloud::Bigtable::AppProfile#routing_policy \(method\)").)

### Batch writes

You can write more than one row in a single RPC using [Table#mutate_rows](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-MutationOperations#Google__Cloud__Bigtable__MutationOperations_mutate_rows_instance_ "Google::Cloud::Bigtable::MutationOperations#mutate_rows \(method\)"):
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    
    table = bigtable.table("my-instance", "my-table")
    
    entries = []
    entries < table.new_mutation_entry("row-1").set_cell("cf1",="" "field1",="" "xyz")="" entries="">< table.new_mutation_entry("row-2").set_cell("cf1",="" "field1",="" "abc")="" responses="table.mutate_rows(entries)" responses.each="" do="" |response|="" puts="" response.status.description="" end="">

Each entry in the request is atomic, but the request as a whole is not. As shown above, Cloud Bigtable returns a list of responses corresponding to the entries.

## Reading data

The [Table](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Table "Google::Cloud::Bigtable::Table \(class\)") class also enables you to read data.

Use [Table#read_row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ReadOperations#Google__Cloud__Bigtable__ReadOperations_read_row_instance_ "Google::Cloud::Bigtable::ReadOperations#read_row \(method\)") to read a single row by key:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table("my-instance", "my-table")
    
    row = table.read_row("user-1")

If desired, you can apply a filter:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table("my-instance", "my-table")
    
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_row(3)
    
    row = table.read_row("user-1", filter: filter)

For multiple rows, the [Table#read_rows](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ReadOperations#Google__Cloud__Bigtable__ReadOperations_read_rows_instance_ "Google::Cloud::Bigtable::ReadOperations#read_rows \(method\)") method streams back the contents of all requested rows in key order:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table("my-instance", "my-table")
    
    table.read_rows(keys: ["user-1", "user-2"]).each do |row|
      puts row
    end

Instead of specifying individual keys (or a range), you can often just use a filter:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table("my-instance", "my-table")
    
    filter = table.filter.key("user-*")
    # OR
    # filter = Google::Cloud::Bigtable::RowFilter.key("user-*")
    
    table.read_rows(filter: filter).each do |row|
      puts row
    end

## Deleting rows, tables, and instances

Use [Table#drop_row_range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Table#Google__Cloud__Bigtable__Table_drop_row_range_instance_ "Google::Cloud::Bigtable::Table#drop_row_range \(method\)") to delete some or all of the rows in a table:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    
    table = bigtable.table("my-instance", "my-table")
    
    # Delete rows using row key prefix.
    table.drop_row_range(row_key_prefix: "user-100")
    
    # Delete all data With timeout
    table.drop_row_range(delete_all_data: true, timeout: 120) # 120 seconds.

Delete tables and instances using [Table#delete](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Table#Google__Cloud__Bigtable__Table_delete_instance_ "Google::Cloud::Bigtable::Table#delete \(method\)") and [Instance#delete](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Instance#Google__Cloud__Bigtable__Instance_delete_instance_ "Google::Cloud::Bigtable::Instance#delete \(method\)"), respectively:
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    
    instance = bigtable.instance("my-instance")
    table = instance.table("my-table")
    
    table.delete
    
    instance.delete

## Additional information

Google Bigtable can be configured to use an emulator or to enable gRPC's logging. To learn more, see the [Emulator guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/EMULATOR "Emulator guide") and [Logging guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/LOGGING "Logging guide").

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
