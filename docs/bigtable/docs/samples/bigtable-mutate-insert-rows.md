---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-mutate-insert-rows/
title: Insert rows with mutate \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:54.949798+00:00
---

# Insert rows with mutate  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-mutate-insert-rows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Insert rows with mutate Stay organized with collections  Save and categorize content based on your preferences. 

Insert rows using mutate.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    [](cbt::Table table) {
      // Write several rows in a single operation, each row has some trivial data.
      cbt::BulkMutation bulk;
      for (int i = 0; i != 5000; ++i) {
        // Note: This example uses sequential numeric IDs for simplicity, but
        // this can result in poor performance in a production application.
        // Since rows are stored in sorted order by key, sequential keys can
        // result in poor distribution of operations across nodes.
        //
        // For more information about how to design a Bigtable schema for the
        // best performance, see the documentation:
        //
        //     https://cloud.google.com/bigtable/docs/schema-design
        char buf[32];
        snprintf(buf, sizeof(buf), "key-%06d", i);
        cbt::SingleRowMutation mutation(buf);
        mutation.emplace_back(
            cbt::SetCell("fam", "col0", "value0-" + std::to_string(i)));
        mutation.emplace_back(
            cbt::SetCell("fam", "col1", "value1-" + std::to_string(i)));
        bulk.emplace_back(std::move(mutation));
      }
      std::vector<cbt::FailedMutation> failures =
          table.BulkApply(std::move(bulk));
      if (failures.empty()) {
        std::cout << "All mutations applied successfully\n";
        return;
      }
      // By default, the `table` object uses the `SafeIdempotentMutationPolicy`
      // which does not retry if any of the mutations fails and are
      // not-idempotent. In this example we simply print such failures, if any,
      // and ignore them otherwise.
      std::cerr << "The following mutations failed and were not retried:\n";
      for (auto const& f : failures) {
        std::cerr << "index[" << f.original_index() << "]=" << f.status() << "\n";
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
