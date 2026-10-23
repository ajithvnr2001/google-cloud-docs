---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-composing-chain-hbase/
title: Read using a chain filter (HBase) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:41.497659+00:00
---

# Read using a chain filter (HBase)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-composing-chain-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read using a chain filter (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Creates a composite filter using chaining.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use filters](https://docs.cloud.google.com/bigtable/docs/using-filters)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static void filterComposingChain() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterComposingChain(projectId, instanceId, tableId);
    }
    
    public static void filterComposingChain(String projectId, String instanceId, String tableId) {
      // A filter that selects one cell per row AND within the column family cell_plan
      Filter familyFilter =
          new FamilyFilter(CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("cell_plan")));
      Filter columnCountGetFilter = new ColumnCountGetFilter(3);
    
      FilterList filter = new FilterList(FilterList.Operator.MUST_PASS_ALL);
      filter.addFilter(columnCountGetFilter);
      filter.addFilter(familyFilter);
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
