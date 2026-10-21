---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-composing-interleave-hbase/
title: Read using an interleave filter (HBase) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:12:14.471474+00:00
---

# Read using an interleave filter (HBase)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-composing-interleave-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read using an interleave filter (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Creates a composite filter using interleaving.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use filters](https://docs.cloud.google.com/bigtable/docs/using-filters)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static void filterComposingInterleave() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterComposingInterleave(projectId, instanceId, tableId);
    }
    
    public static void filterComposingInterleave(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells with the value true OR with the column qualifier os_build
      Filter qualifierFilter =
          new QualifierFilter(CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("os_build")));
      Filter valueFilter =
          new ValueFilter(CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("true")));
    
      FilterList filter = new FilterList(Operator.MUST_PASS_ONE);
      filter.addFilter(qualifierFilter);
      filter.addFilter(valueFilter);
    
      Scan scan = new Scan().setFilter(filter).setMaxVersions();
      readWithFilter(projectId, instanceId, tableId, scan);
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
