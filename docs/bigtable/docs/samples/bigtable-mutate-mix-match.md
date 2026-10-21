---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-mutate-mix-match/
title: Mix mutations \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:57.061572+00:00
---

# Mix mutations  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-mutate-mix-match/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Mix mutations Stay organized with collections  Save and categorize content based on your preferences. 

Mix and match mutation operations such as inserting rows and deleting a column.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::Status;
    using ::google::cloud::StatusOr;
    [](cbt::Table table, std::string const& key, std::string const& family,
       std::string const& old_name, std::string const& new_name) {
      StatusOr<std::pair<bool, cbt::Row>> row =
          table.ReadRow(key, cbt::Filter::ColumnName(family, old_name));
    
      if (!row) throw std::move(row).status();
      if (!row->first) throw std::runtime_error("Cannot find row " + key);
    
      cbt::SingleRowMutation mutation(key);
      for (auto const& cell : row->second.cells()) {
        // Create a new cell
        auto timestamp_in_milliseconds =
            std::chrono::duration_cast<std::chrono::milliseconds>(
                cell.timestamp());
        mutation.emplace_back(cbt::SetCell(family, new_name,
                                           timestamp_in_milliseconds,
                                           std::move(cell).value()));
      }
      mutation.emplace_back(cbt::DeleteFromColumn("fam", old_name));
    
      google::cloud::Status status = table.Apply(std::move(mutation));
      if (!status.ok()) throw std::runtime_error(status.message());
      std::cout << "Row successfully updated\n";
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
