---
url: https://docs.cloud.google.com/bigtable/docs/samples-cpp-hello/
title: C++ hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:32.273413+00:00
---

# C++ hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-cpp-hello/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# C++ hello world

This example is a simple "hello world" application, written in C++, that illustrates how to do the following:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.



## Set up authentication

To use the C++ samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

## Running the sample

This example uses the [Cloud Bigtable package](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest) of the [Google Cloud client library for C++](https://github.com/googleapis/google-cloud-cpp) to communicate with Bigtable.

To run this sample program, follow the [instructions on GitHub](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/bigtable/examples).

## Using the Google Cloud client library with Bigtable

The sample application connects to Bigtable and demonstrates some simple operations.

### Installing and importing the client library

Download or clone the [Bigtable C++ client library](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/bigtable) from GitHub, then compile it. Follow the compiler instructions on the top-level [README](https://github.com/googleapis/google-cloud-cpp/blob/main/README.md).

Include the required headers.
    
    
    #include "google/cloud/bigtable/admin/bigtable_table_admin_client.h"
    #include "google/cloud/bigtable/resource_names.h"
    #include "google/cloud/bigtable/table.h"

### Connecting to Bigtable

Use [`MakeBigtableTableAdminConnection()`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/namespacegoogle_1_1cloud_1_1bigtable__admin.html#a7c020b286209baa8dcd7b8a906d11ca5) to construct a [`BigtableTableAdminClient`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable__admin_1_1BigtableTableAdminClient.html), which you will use to create a table.
    
    
    // Connect to the Cloud Bigtable Admin API.
    cbta::BigtableTableAdminClient table_admin(
        cbta::MakeBigtableTableAdminConnection());
    
    //! [connect data]
    // Create an object to access the Cloud Bigtable Data API.
    cbt::Table table(cbt::MakeDataConnection({cbt::InstanceResource(
                         google::cloud::Project(project_id), instance_id)}),
                     cbt::TableResource(project_id, instance_id, table_id));
    //! [connect data]

### Creating a table

Define a schema for the table that has one column family. Set a garbage collection rule for the column family to keep a maximum of one version of each value. Use that schema to instantiate a table object using [`BigtableTableAdminClient::CreateTable()`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable__admin_1_1BigtableTableAdminClient.html#a3ea5cf5a526dc0f8502619eecb50c2b7). Then create a data client that you can use to get data in and out of your table.

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
    // Define the desired schema for the Table.
    google::bigtable::admin::v2::Table t;
    auto& families = *t.mutable_column_families();
    families["family"].mutable_gc_rule()->set_max_num_versions(1);
    
    // Create a table.
    std::string instance_name = cbt::InstanceName(project_id, instance_id);
    StatusOr<google::bigtable::admin::v2::Table> schema =
        table_admin.CreateTable(instance_name, table_id, std::move(t));

### Writing rows to a table

Loop through a list of greeting strings to create some new rows for the table. In each iteration, use [`SingleRowMutation`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1SingleRowMutation.html) to define a row and assign it a row key and value. Then call [`Table::Apply()`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Table.html#a7b9b5ebc792bb35befd3e75733a4999a) to apply the mutation to the row.
    
    
    std::vector<std::string> greetings{"Hello World!", "Hello Cloud Bigtable!",
                                       "Hello C++!"};
    int i = 0;
    for (auto const& greeting : greetings) {
      // Each row has a unique row key.
      //
      // Note: This example uses sequential numeric IDs for simplicity, but
      // this can result in poor performance in a production application.
      // Since rows are stored in sorted order by key, sequential keys can
      // result in poor distribution of operations across nodes.
      //
      // For more information about how to design a Bigtable schema for the
      // best performance, see the documentation:
      //
      //     https://cloud.google.com/bigtable/docs/schema-design
      std::string row_key = "key-" + std::to_string(i);
      google::cloud::Status status = table.Apply(cbt::SingleRowMutation(
          std::move(row_key), cbt::SetCell("family", "c0", greeting)));
    
      if (!status.ok()) throw std::runtime_error(status.message());
      ++i;
    }

### Creating a filter

Before you read the data that you wrote, create a filter, using [`Filter::ColumnRangeClosed()`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Filter.html#a18c55b828cf305cb5db44b4980df7127), to limit the data that Bigtable returns. This filter tells Bigtable to return only the most recent version of each value, even if the table contains older cells that have expired but have not yet been removed by garbage collection.
    
    
    cbt::Filter filter = cbt::Filter::ColumnRangeClosed("family", "c0", "c0");

### Reading a row by its key

Call the [`Table::ReadRow()`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Table.html#abc1c974c7574139e579b59d3a599c102) function, passing in the row key and the filter, to get one version of each value in that row.
    
    
    StatusOr<std::pair<bool, cbt::Row>> result = table.ReadRow("key-0", filter);
    if (!result) throw std::move(result).status();
    if (!result->first) {
      std::cout << "Cannot find row 'key-0' in the table: " << table.table_name()
                << "\n";
      return;
    }
    cbt::Cell const& cell = result->second.cells().front();
    std::cout << cell.family_name() << ":" << cell.column_qualifier() << "    @ "
              << cell.timestamp().count() << "us\n"
              << '"' << cell.value() << '"' << "\n";

### Scanning all table rows

Use [`Table::ReadRows()`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Table.html#ade2f35db5d9296bd9f4dce9244c9ba40) to read a range of rows from the table.
    
    
    for (auto& row : table.ReadRows(cbt::RowRange::InfiniteRange(),
                                    cbt::Filter::PassAllFilter())) {
      if (!row) throw std::move(row).status();
      std::cout << row->row_key() << ":\n";
      for (cbt::Cell const& c : row->cells()) {
        std::cout << "\t" << c.family_name() << ":" << c.column_qualifier()
                  << "    @ " << c.timestamp().count() << "us\n"
                  << "\t\"" << c.value() << '"' << "\n";
      }
    }

### Deleting a table

Delete the table with [`BigtableTableAdminClient::DeleteTable()`](https://googleapis.dev/cpp/google-cloud-bigtable/latest/classgoogle_1_1cloud_1_1bigtable__admin_1_1BigtableTableAdminClient.html#af02061b7e8f2d0b7a580050e1e95cad3).
    
    
    google::cloud::Status status = table_admin.DeleteTable(table.table_name());
    if (!status.ok()) throw std::runtime_error(status.message());

## Putting it all together

Here is the full example without comments.
    
    
    
    #include "google/cloud/bigtable/admin/bigtable_table_admin_client.h"
    #include "google/cloud/bigtable/resource_names.h"
    #include "google/cloud/bigtable/table.h"
    #include "google/cloud/bigtable/examples/bigtable_examples_common.h"
    #include "google/cloud/bigtable/testing/random_names.h"
    #include "google/cloud/internal/getenv.h"
    #include "google/cloud/internal/random.h"
    #include "google/cloud/log.h"
    #include <iostream>
    
    namespace {
    
    using ::google::cloud::bigtable::examples::Usage;
    
    void BigtableHelloWorld(std::vector<std::string> const& argv) {
      if (argv.size() != 3) {
        throw Usage{"hello-world <project-id> <instance-id> <table-id>"};
      }
      std::string const& project_id = argv[0];
      std::string const& instance_id = argv[1];
      std::string const& table_id = argv[2];
    
      namespace cbt = ::google::cloud::bigtable;
      namespace cbta = ::google::cloud::bigtable_admin;
      using ::google::cloud::StatusOr;
    
      cbta::BigtableTableAdminClient table_admin(
          cbta::MakeBigtableTableAdminConnection());
    
      cbt::Table table(cbt::MakeDataConnection({cbt::InstanceResource(
                           google::cloud::Project(project_id), instance_id)}),
                       cbt::TableResource(project_id, instance_id, table_id));
    
      google::bigtable::admin::v2::Table t;
      auto& families = *t.mutable_column_families();
      families["family"].mutable_gc_rule()->set_max_num_versions(1);
    
      std::string instance_name = cbt::InstanceName(project_id, instance_id);
      StatusOr<google::bigtable::admin::v2::Table> schema =
          table_admin.CreateTable(instance_name, table_id, std::move(t));
    
      std::vector<std::string> greetings{"Hello World!", "Hello Cloud Bigtable!",
                                         "Hello C++!"};
      int i = 0;
      for (auto const& greeting : greetings) {
        std::string row_key = "key-" + std::to_string(i);
        google::cloud::Status status = table.Apply(cbt::SingleRowMutation(
            std::move(row_key), cbt::SetCell("family", "c0", greeting)));
    
        if (!status.ok()) throw std::runtime_error(status.message());
        ++i;
      }
    
      cbt::Filter filter = cbt::Filter::ColumnRangeClosed("family", "c0", "c0");
    
      StatusOr<std::pair<bool, cbt::Row>> result = table.ReadRow("key-0", filter);
      if (!result) throw std::move(result).status();
      if (!result->first) {
        std::cout << "Cannot find row 'key-0' in the table: " << table.table_name()
                  << "\n";
        return;
      }
      cbt::Cell const& cell = result->second.cells().front();
      std::cout << cell.family_name() << ":" << cell.column_qualifier() << "    @ "
                << cell.timestamp().count() << "us\n"
                << '"' << cell.value() << '"' << "\n";
    
      for (auto& row : table.ReadRows(cbt::RowRange::InfiniteRange(),
                                      cbt::Filter::PassAllFilter())) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << ":\n";
        for (cbt::Cell const& c : row->cells()) {
          std::cout << "\t" << c.family_name() << ":" << c.column_qualifier()
                    << "    @ " << c.timestamp().count() << "us\n"
                    << "\t\"" << c.value() << '"' << "\n";
        }
      }
    
      google::cloud::Status status = table_admin.DeleteTable(table.table_name());
      if (!status.ok()) throw std::runtime_error(status.message());
    }
    
    void RunAll(std::vector<std::string> const& argv) {
      namespace examples = ::google::cloud::bigtable::examples;
      namespace cbt = ::google::cloud::bigtable;
    
      if (!argv.empty()) throw Usage{"auto"};
      if (!examples::RunAdminIntegrationTests()) return;
      examples::CheckEnvironmentVariablesAreSet({
          "GOOGLE_CLOUD_PROJECT",
          "GOOGLE_CLOUD_CPP_BIGTABLE_TEST_INSTANCE_ID",
      });
      auto const project_id =
          google::cloud::internal::GetEnv("GOOGLE_CLOUD_PROJECT").value();
      auto const instance_id = google::cloud::internal::GetEnv(
                                   "GOOGLE_CLOUD_CPP_BIGTABLE_TEST_INSTANCE_ID")
                                   .value();
    
      auto generator = google::cloud::internal::DefaultPRNG(std::random_device{}());
      auto table_id = cbt::testing::RandomTableId(generator);
    
      std::cout << "\nRunning the BigtableHelloWorld() example" << std::endl;
      BigtableHelloWorld({project_id, instance_id, table_id});
    }
    
    }  // namespace
    
    int main(int argc, char* argv[]) try {
      google::cloud::bigtable::examples::Example example({
          {"auto", RunAll},
          {"hello-world", BigtableHelloWorld},
      });
      return example.Run(argc, argv);
    } catch (std::exception const& ex) {
      std::cerr << ex.what() << "\n";
      ::google::cloud::LogSink::Instance().Flush();
      return 1;
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
