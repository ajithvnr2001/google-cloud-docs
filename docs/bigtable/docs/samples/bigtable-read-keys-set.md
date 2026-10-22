---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-read-keys-set/
title: Read by keys \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:59.209222+00:00
---

# Read by keys  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-read-keys-set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read by keys Stay organized with collections  Save and categorize content based on your preferences. 

Read using a noncontiguous set of row keys.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table, std::vector<std::string> const& row_keys) {
      auto row_set = cbt::RowSet();
    
      for (auto const& row_key : row_keys) {
        row_set.Append(row_key);
      }
    
      cbt::Filter filter = cbt::Filter::Latest(1);
      for (StatusOr<cbt::Row>& row : table.ReadRows(std::move(row_set), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << ":\n";
        for (auto const& cell : row->cells()) {
          std::cout << "\t" << cell.family_name() << ":"
                    << cell.column_qualifier() << "    @ "
                    << cell.timestamp().count() << "us\n"
                    << "\t\"" << cell.value() << '"' << "\n";
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
