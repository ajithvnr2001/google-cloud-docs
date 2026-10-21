---
url: https://docs.cloud.google.com/bigtable/docs/hbase-batch-exceptions/
title: Handle batch exceptions \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:19.360159+00:00
---

# Handle batch exceptions  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-batch-exceptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Handle batch exceptions

The HBase API provides two ways to send multiple operations as a batch:

  * [`Table#batch(List, Object[])`](https://hbase.apache.org/2.5/apidocs/org/apache/hadoop/hbase/client/Table.html#batch-java.util.List-java.lang.Object:A-) combines multiple gets and mutations into a single batch.
  * [`BufferedMutator#mutate(List<? extends Mutation> mutations)`](https://hbase.apache.org/2.5/apidocs/org/apache/hadoop/hbase/client/BufferedMutator.html#mutate-java.util.List-) combines multiple mutations into a batch or series of batches.



With the Cloud Bigtable HBase client for Java, both of these methods can throw a [`RetriesExhaustedWithDetailsException`](https://hbase.apache.org/2.5/apidocs/org/apache/hadoop/hbase/client/RetriesExhaustedWithDetailsException.html). This exception is thrown when one or more of the batch operations fail for any reason (for example, because the connection failed). It contains a list of failed requests, along with details about the exception that caused each request to fail.

By itself, a `RetriesExhaustedWithDetailsException` does not tell you why a request failed. You must call [`RetriesExhaustedWithDetailsException#getCauses()`](https://hbase.apache.org/2.5/apidocs/org/apache/hadoop/hbase/client/RetriesExhaustedWithDetailsException.html#getCauses--) to retrieve the detailed exceptions for each failed request. You can then log information about each of the detailed exceptions, which will help you diagnose the failure:
    
    
    try {
      mutator.mutate(mutationList);
    } catch (RetriesExhaustedWithDetailsException e) {
      for (Throwable cause : e.getCauses()) {
        cause.printStackTrace();
      }
      throw e;
    }
    

An exception can also be thrown when you call [`flush`](https://hbase.apache.org/2.5/devapidocs/org/apache/hadoop/hbase/procedure/flush/package-summary.html) or [`close`](https://hbase.apache.org/2.5/apidocs/org/apache/hadoop/hbase/client/Connection.html#close--). The same error handling applies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
