---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-limit-timestamp-range-hbase/
title: Read using a timestamp range filter (HBase) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:17.469760+00:00
---

# Read using a timestamp range filter (HBase)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-limit-timestamp-range-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read using a timestamp range filter (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Creates a limiting filter on a range of cell timestamps.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use filters](https://docs.cloud.google.com/bigtable/docs/using-filters)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static void filterLimitTimestampRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitTimestampRange(projectId, instanceId, tableId);
    }
    
    public static void filterLimitTimestampRange(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose timestamp is from an hour ago or earlier
      // Get a time representing one hour ago
      long timestamp = Instant.now().minus(1, ChronoUnit.HOURS).toEpochMilli();
      try {
        Scan scan = new Scan().setTimeRange(0, timestamp).setMaxVersions();
        readWithFilter(projectId, instanceId, tableId, scan);
      } catch (IOException e) {
        System.out.println("There was an issue with your timestamp \n" + e.toString());
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
