---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-or-create-table/
title: Get or create a table \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:54.379039+00:00
---

# Get or create a table  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-get-or-create-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Get or create a table Stay organized with collections  Save and categorize content based on your preferences. 

Get table details if it exists, or autocreate a table if it does not exist.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableTableAdminClient admin, std::string const& project_id,
       std::string const& instance_id, std::string const& table_id) {
      std::string instance_name = cbt::InstanceName(project_id, instance_id);
      std::string table_name = cbt::TableName(project_id, instance_id, table_id);
    
      google::bigtable::admin::v2::GetTableRequest r;
      r.set_name(table_name);
      r.set_view(google::bigtable::admin::v2::Table::FULL);
    
      StatusOr<google::bigtable::admin::v2::Table> table = admin.GetTable(r);
      if (!table &&
          table.status().code() == google::cloud::StatusCode::kNotFound) {
        // The table does not exist, try to create the table.
        table = admin.CreateTable(instance_name, table_id, {});
        if (!table) throw std::move(table).status();
        // The schema returned by a `CreateTable()` request does not include all
        // the metadata for a table, we need to explicitly request the rest:
        table = admin.GetTable(std::move(r));
      }
      if (!table) throw std::move(table).status();
      std::cout << "Table metadata: " << table->DebugString() << "\n";
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
