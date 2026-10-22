---
url: https://docs.cloud.google.com/bigtable/docs/samples-map-reduce/
title: Hadoop MapReduce job with Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:49.670081+00:00
---

# Hadoop MapReduce job with Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-map-reduce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Hadoop MapReduce job with Bigtable

This example uses [Hadoop](https://hadoop.apache.org/) to perform a simple MapReduce job that counts the number of times a word appears in a text file. The MapReduce job uses Bigtable to store the results of the map operation. The code for this example is in the GitHub repository [GoogleCloudPlatform/cloud-bigtable-examples](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/), in the directory `java/dataproc-wordcount`.

## Set up authentication

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

## Overview of the code sample

The code sample provides a simple command-line interface that takes one or more text files and a table name as input, finds all of the words that appear in the file, and counts how many times each word appears. The MapReduce logic appears in the [`WordCountHBase` class](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples//blob/master/java/dataproc-wordcount/src/main/java/com/example/bigtable/sample/WordCountHBase.java).

First, a mapper tokenizes the text file's contents and generates key-value pairs, where the key is a word from the text file and the value is `1`:
    
    
    public static class TokenizerMapper extends
        Mapper<Object, Text, ImmutableBytesWritable, IntWritable> {
    
      private final static IntWritable one = new IntWritable(1);
    
      @Override
      public void map(Object key, Text value, Context context) throws IOException,
          InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString());
        ImmutableBytesWritable word = new ImmutableBytesWritable();
        while (itr.hasMoreTokens()) {
          word.set(Bytes.toBytes(itr.nextToken()));
          context.write(word, one);
        }
      }
    }
    

A reducer then sums the values for each key and writes the results to a Bigtable table that you specified. Each row key is a word from the text file. Each row contains a `cf:count` column, which contains the number of times the row key appears in the text file.
    
    
    public static class MyTableReducer extends
        TableReducer<ImmutableBytesWritable, IntWritable, ImmutableBytesWritable> {
    
      @Override
      public void reduce(ImmutableBytesWritable key, Iterable<IntWritable> values, Context context)
          throws IOException, InterruptedException {
        int sum = sum(values);
        Put put = new Put(key.get());
        put.addColumn(COLUMN_FAMILY, COUNT_COLUMN_NAME, Bytes.toBytes(sum));
        context.write(null, put);
      }
    
      public int sum(Iterable<IntWritable> values) {
        int i = 0;
        for (IntWritable val : values) {
          i += val.get();
        }
        return i;
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
