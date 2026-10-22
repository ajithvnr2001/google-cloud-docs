---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-print-hbase/
title: Read and print (HBase) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:30.437137+00:00
---

# Read and print (HBase)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-print-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read and print (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Read and print a row.

## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import org.apache.hadoop.hbase.Cell;
    import org.apache.hadoop.hbase.TableName;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.Get;
    import org.apache.hadoop.hbase.client.Result;
    import org.apache.hadoop.hbase.client.ResultScanner;
    import org.apache.hadoop.hbase.client.Scan;
    import org.apache.hadoop.hbase.client.Table;
    import org.apache.hadoop.hbase.filter.CompareFilter.CompareOp;
    import org.apache.hadoop.hbase.filter.Filter;
    import org.apache.hadoop.hbase.filter.MultiRowRangeFilter;
    import org.apache.hadoop.hbase.filter.MultiRowRangeFilter.RowRange;
    import org.apache.hadoop.hbase.filter.RegexStringComparator;
    import org.apache.hadoop.hbase.filter.ValueFilter;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class Reads {
    
      // Write your code here.
      // ...
    
      private static void printRow(Result row) {
        System.out.printf("Reading data for %s%n", Bytes.toString(row.rawCells()[0].getRowArray()));
        String colFamily = "";
        for (Cell cell : row.rawCells()) {
          String currentFamily = Bytes.toString(cell.getFamilyArray());
          if (!currentFamily.equals(colFamily)) {
            colFamily = currentFamily;
            System.out.printf("Column Family %s%n", colFamily);
          }
          System.out.printf(
              "\t%s: %s @%s%n",
              Bytes.toString(cell.getQualifierArray()),
              Bytes.toString(cell.getValueArray()),
              cell.getTimestamp());
        }
        System.out.println();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
