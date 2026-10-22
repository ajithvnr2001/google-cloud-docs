---
url: https://docs.cloud.google.com/bigtable/docs/samples-ruby-hello/
title: Ruby hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:02.523127+00:00
---

# Ruby hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-ruby-hello/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ruby hello world

This code sample is a "hello world" application that runs on Ruby. The sample illustrates how to complete the following tasks:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.



## Set up authentication

To use the Ruby samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

**Note:** To execute the following samples, ensure that the authenticated account has the **Bigtable Admin** IAM role. For information about granting roles to an account, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Setting up your environment

In order to run this sample, you need to have Ruby installed.

### 1\. Install Ruby

To check the minimum required Ruby version for the client library, see `required_ruby_version` in the [`google-cloud-bigtable.gemspec` file](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-bigtable/google-cloud-bigtable.gemspec).

Setting up Ruby on a Compute Engine VM If you want to run the sample on a Compute Engine VM, follow these instructions to set up Ruby on a Debian or Ubuntu VM.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If you don't have a Linux VM that uses the Debian or Ubuntu operating system, create one and connect to it. For more information, see [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/quickstart-linux).

  3. In the terminal window for your VM, update your package lists:
         
         sudo apt update
         

  4. Install Ruby, Ruby development tools, and `build-essential`, which are required by the client library:
         
         sudo apt install -y ruby ruby-dev build-essential
         

  5. Verify that the installed Ruby version meets the minimum requirement specified in the [`google-cloud-bigtable.gemspec` file](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-bigtable/google-cloud-bigtable.gemspec):
         
         ruby --version
         




### 2\. Install the client library

To install the client library:

  1. Initialize bundler to create a `Gemfile` in your project's root directory:
         
         bundle init
         

  2. Add `google-cloud-bigtable` to your `Gemfile` and install it:
         
         bundle add google-cloud-bigtable
         




For more information about the client library, see the [`google-cloud-bigtable` README](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-bigtable/README.md).

## Running the sample

This code sample uses the [Ruby client library for Bigtable](https://github.com/googleapis/google-cloud-ruby/tree/master/google-cloud-bigtable) package of the [Google Cloud Client Library for Ruby](https://github.com/googleapis/google-cloud-ruby) to communicate with Bigtable.

To run this sample program, follow the [instructions for the sample on GitHub](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-bigtable/samples/README.md#run-samples).

## Using the Cloud Client Library with Bigtable

The sample application connects to Bigtable and demonstrates some simple operations.

### Requiring the client library

The sample requires `google/cloud/bigtable`, which provides the [`Bigtable`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable.html) module.
    
    
    require "google/cloud/bigtable"

### Connecting to Bigtable

Establish the variables you will use in your application, replacing "YOUR_PROJECT_ID" with the ID of a valid Google Cloud project. Then create a new [`Bigtable`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable.html) object that you will use to connect to Bigtable.
    
    
    # These variables are used in the sample code below.
    # instance_id      = "my-instance"
    # table_id         = "my-table"
    # column_family    = "cf"
    # column_qualifier = "greeting"
    
    bigtable = Google::Cloud::Bigtable.new
    table_client = bigtable.table_admin_client

### Creating a table

Check to see if your table already exists. If it doesn't, call the [`create_table()`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable/Project.html#create_table-instance_method) method to create a [`Table`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Bigtable/Admin/V2/Table.html) object. The table has a single column family that retains one version of each value.

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
    # This is the full resource name for the table. Use this name to make admin
    # calls for the table, such as reading or deleting the resource.
    table_name = table_client.table_path project: bigtable.project_id,
                                         instance: instance_id,
                                         table: table_id
    begin
      # Attempt to get the table to see if it already exists
      table_client.get_table name: table_name
      puts "#{table_id} is already exists."
      exit 0
    rescue Google::Cloud::NotFoundError
      # The table doesn't exist, so let's create it.
      # The following is the resource name for the table's instance.
      instance_name = table_client.instance_path project: bigtable.project_id,
                                                 instance: instance_id
      # This is the configuration of the table's column families.
      table_config = {
        column_families: {
          column_family => {
            gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.max_num_versions(1)
          }
        }
      }
      # Now call the API to create the table.
      table_client.create_table parent: instance_name,
                                table_id: table_id,
                                table: table_config
      puts "Table #{table_id} created."
    end

### Writing rows to a table

Next, use a string array of greetings to create some new rows for the table. For each greeting, create an entry using the table's [`new_mutation_entry()`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable/MutationOperations.html#new_mutation_entry-instance_method) method. Next, use the entry's [`set_cell()`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable/MutationEntry.html#set_cell-instance_method) method to assign the column family, column qualifier, the greeting, and a timestamp to the entry. Finally, write that entry to the table using the table's [`mutate_row()`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable/MutationOperations.html#mutate_row-instance_method) method.

**Note:** In this sample application, `set_Cell()` is only called once per mutation, but you can call it up to 10,000 times per single mutation.
    
    
    puts "Write some greetings to the table #{table_id}"
    greetings = ["Hello World!", "Hello Bigtable!", "Hello Ruby!"]
    
    # Get a table data object for the new table we created.
    table = bigtable.table instance_id, table_id
    
    # Insert rows one by one
    # Note: To perform multiple mutation on multiple rows use `mutate_rows`.
    greetings.each_with_index do |value, i|
      puts " Writing,  Row key: greeting#{i}, Value: #{value}"
    
      entry = table.new_mutation_entry "greeting#{i}"
      entry.set_cell(
        column_family,
        column_qualifier,
        value,
        timestamp: (Time.now.to_f * 1_000_000).round(-3)
      )
    
      table.mutate_row entry
    end

### Creating a filter

Before you read the data that you wrote, create a filter to limit the data that Bigtable returns. This filter tells Bigtable to return only the most recent version of each value, even if the table contains older versions that haven't been garbage-collected.
    
    
    # Only retrieve the most recent version of the cell.
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_column 1

### Reading a row by its row key

Create a row object, then call the [`read_row()`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable/ReadOperations.html#read_row-instance_method) method, passing in the filter, to get one version of each value in that row.
    
    
    puts "Reading a single row by row key"
    row = table.read_row "greeting0", filter: filter
    puts "Row key: #{row.key}, Value: #{row.cells[column_family].first.value}"

### Scanning all table rows

Call the [`read_rows()`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable/ReadOperations.html#read_rows-instance_method) method, passing in the filter, to get all of the rows in the table. Because you passed in the filter, Bigtable returns only one version of each value.
    
    
    puts "Reading the entire table"
    table.read_rows.each do |row|
      puts "Row key: #{row.key}, Value: #{row.cells[column_family].first.value}"
    end

### Deleting a table

Delete the table with the table's [`delete()`](https://googleapis.dev/ruby/google-cloud-bigtable/latest/Google/Cloud/Bigtable/Table.html#delete-instance_method) method.
    
    
    puts "Deleting the table #{table_id}"
    # Call the admin API to delete the table given its full resource path.
    table_client.delete_table name: table_name

## Putting it all together

Here is the full code sample without comments.
    
    
    # Copyright 2021 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    def hello_world instance_id, table_id, column_family, column_qualifier
      require "google/cloud/bigtable"
    
      # These variables are used in the sample code below.
      # instance_id      = "my-instance"
      # table_id         = "my-table"
      # column_family    = "cf"
      # column_qualifier = "greeting"
    
      bigtable = Google::Cloud::Bigtable.new
      table_client = bigtable.table_admin_client
    
      # This is the full resource name for the table. Use this name to make admin
      # calls for the table, such as reading or deleting the resource.
      table_name = table_client.table_path project: bigtable.project_id,
                                           instance: instance_id,
                                           table: table_id
      begin
        # Attempt to get the table to see if it already exists
        table_client.get_table name: table_name
        puts "#{table_id} is already exists."
        exit 0
      rescue Google::Cloud::NotFoundError
        # The table doesn't exist, so let's create it.
        # The following is the resource name for the table's instance.
        instance_name = table_client.instance_path project: bigtable.project_id,
                                                   instance: instance_id
        # This is the configuration of the table's column families.
        table_config = {
          column_families: {
            column_family => {
              gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.max_num_versions(1)
            }
          }
        }
        # Now call the API to create the table.
        table_client.create_table parent: instance_name,
                                  table_id: table_id,
                                  table: table_config
        puts "Table #{table_id} created."
      end
    
      puts "Write some greetings to the table #{table_id}"
      greetings = ["Hello World!", "Hello Bigtable!", "Hello Ruby!"]
    
      # Get a table data object for the new table we created.
      table = bigtable.table instance_id, table_id
    
      # Insert rows one by one
      # Note: To perform multiple mutation on multiple rows use `mutate_rows`.
      greetings.each_with_index do |value, i|
        puts " Writing,  Row key: greeting#{i}, Value: #{value}"
    
        entry = table.new_mutation_entry "greeting#{i}"
        entry.set_cell(
          column_family,
          column_qualifier,
          value,
          timestamp: (Time.now.to_f * 1_000_000).round(-3)
        )
    
        table.mutate_row entry
      end
    
      # Only retrieve the most recent version of the cell.
      filter = Google::Cloud::Bigtable::RowFilter.cells_per_column 1
    
      puts "Reading a single row by row key"
      row = table.read_row "greeting0", filter: filter
      puts "Row key: #{row.key}, Value: #{row.cells[column_family].first.value}"
    
      puts "Reading the entire table"
      table.read_rows.each do |row|
        puts "Row key: #{row.key}, Value: #{row.cells[column_family].first.value}"
      end
    
      puts "Deleting the table #{table_id}"
      # Call the admin API to delete the table given its full resource path.
      table_client.delete_table name: table_name
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
