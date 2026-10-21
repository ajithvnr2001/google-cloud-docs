---
url: https://docs.cloud.google.com/dataflow/docs/guides/gae-mapreduce-migration/
title: Migrate from App Engine MapReduce to Apache Beam and Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:57.018544+00:00
---

# Migrate from App Engine MapReduce to Apache Beam and Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/gae-mapreduce-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Migrate from App Engine MapReduce to Apache Beam and Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Apache Beam and Dataflow let you modernize legacy App Engine MapReduce jobs with unified stream and batch processing on fully managed infrastructure. In this tutorial, you'll learn how to translate App Engine MapReduce concepts into Apache Beam pipelines and run them on Dataflow.

## Why migrate?

App Engine MapReduce is a programming model for processing large amounts of data in a parallel and distributed fashion. It is useful for large, long-running tasks that cannot be handled within the scope of a single request, such as:

  * Analyzing application logs
  * Aggregating related data from external sources
  * Transforming data from one format to another
  * Exporting data for external analysis



However, App Engine MapReduce is a community-maintained, [open source library](https://github.com/GoogleCloudPlatform/appengine-mapreduce/wiki/1-MapReduce) that is built on top of App Engine services and is no longer supported by Google.

Dataflow, on the other hand, is fully supported by Google, and provides extended functionality compared to App Engine MapReduce.

### Migration cases

The following are some example cases where you could benefit from migrating from App Engine MapReduce to Apache Beam and Dataflow:

  * Store your Datastore database application data in a BigQuery data warehouse for analytical processing using SQL.
  * Use Dataflow as an alternative to App Engine MapReduce for maintenance or updates of your Datastore dataset.
  * Back up parts of your Datastore database to Cloud Storage.



## What is Dataflow and Apache Beam?

Dataflow is a managed service for executing a wide variety of data processing patterns. Apache Beam is a unified programming model that provides SDKs for defining data processing workflows. Use Apache Beam to create complex pipelines for both batch and streaming and run them on Dataflow.

## Getting started with Dataflow and Apache Beam

To get started, follow the quickstart of your choice:

  * [Using Java and Apache Maven](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-java)
  * [Using Python](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python)
  * [Using Go](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-go)



### Creating and running a pipeline

When using App Engine MapReduce, you create data processing classes, add the MapReduce library, and once the job's specification and settings are defined, you create and start the job in one step using the static `start()` method on the appropriate job class.

For Map jobs, you create the `Input` and `Output` classes and the `Map` class that does the mapping. For App Engine MapReduce jobs, you create `Input` and `Output` classes, and define the `Mapper` and `Reducer` classes for data transformations.

With Apache Beam you do things slightly differently; you create a pipeline. You use input and output connectors to read and write from your data sources and sinks. You use predefined data transforms (or write your own) to implement your data transformations. Then, once your code is ready, you deploy your pipeline to the Dataflow service.

### Converting App Engine MapReduce jobs to Apache Beam pipelines

The following table presents the Apache Beam equivalents of the **map** , **shuffle** , and **reduce** steps of the App Engine MapReduce model.

### Java

App Engine MapReduce | Apache Beam equivalent  
---|---  
Map | MapElements<InputT,OutputT>  
Shuffle | GroupByKey<K,V>  
Reduce | Combine.GroupedValues<K,InputT,OutputT>  
  
A common practice is to use `Combine.PerKey<K,InputT,OutputT>` instead of `GroupByKey` and `CombineValues`.

### Python

App Engine MapReduce | Apache Beam equivalent  
---|---  
Map | beam.Map  
Shuffle | beam.GroupByKey  
Reduce | beam.CombineValues  
  
A common practice is to use `beam.CombinePerKey` instead of `beam.GroupByKey` and `beam.CombineValues`.

### Go

App Engine MapReduce | Apache Beam equivalent  
---|---  
Map | beam.ParDo  
Shuffle | beam.GroupByKey  
Reduce | beam.Combine  
  
  
The following sample code demonstrates how to implement the App Engine MapReduce model in Apache Beam:

### Java

Taken from [MinimalWordCount.java](https://github.com/apache/beam/blob/master/examples/java/src/main/java/org/apache/beam/examples/MinimalWordCount.java): 
    
    
    p.apply(TextIO.read().from("gs://apache-beam-samples/shakespeare/*"))
    
     // Apply a ParDo that returns a PCollection, where each element is an
     // individual word in Shakespeare's texts.
     .apply("ExtractWords", ParDo.of(new DoFn<String, String>() {
                       @ProcessElement
                       public void processElement(ProcessContext c) {
                         for (String word : c.element().split(ExampleUtils.TOKENIZER_PATTERN)) {
                           if (!word.isEmpty()) {
                             c.output(word);
                           }
                         }
                       }
                     }))
    
     // Apply the Count transform that returns a new PCollection of key/value pairs,
     // where each key represents a unique word in the text.
     .apply(Count.perElement())
    
     // Apply a MapElements transform that formats our PCollection of word counts
     // into a printable string, suitable for writing to an output file.
     .apply("FormatResults", MapElements.via(new SimpleFunction<KV<String, Long>, String>() {
                       @Override
                       public String apply(KV<String, Long> input) {
                         return input.getKey() + ": " + input.getValue();
                       }
                     }))
    
     // Apply a write transform that writes the contents of the PCollection to a
     // series of text files.
     .apply(TextIO.write().to("wordcounts"));

### Python

Taken from [wordcount_minimal.py](https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount_minimal.py): 
    
    
    # Read the text file[pattern] into a PCollection.
    lines = p | ReadFromText(known_args.input)
    
    # Count the occurrences of each word.
    counts = (
        lines
        | 'Split' >> (beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
                      .with_output_types(unicode))
        | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum))
    
    # Format the counts into a PCollection of strings.
    output = counts | 'Format' >> beam.Map(lambda (w, c): '%s: %s' % (w, c))
    
    # Write the output using a "Write" transform that has side effects.
    # pylint: disable=expression-not-assigned
    output | WriteToText(known_args.output)

### Go

Taken from [minimal_wordcount.go](https://github.com/apache/beam/blob/master/sdks/go/examples/minimal_wordcount/minimal_wordcount.go): 
    
    
    // beam.Init() is an initialization hook that must be called on startup.
    beam.Init()
    
    // Create the Pipeline object and root scope.
    p := beam.NewPipeline()
    s := p.Root()
    lines := textio.Read(s, "gs://apache-beam-samples/shakespeare/kinglear.txt")
    
    // Invoke a ParDo transform on our PCollection of text lines.
    // This ParDo invokes a DoFn (defined in-line) on each element that
    // tokenizes the text line into individual words. The ParDo returns a
    // PCollection of type string, where each element is an individual word in
    // Shakespeare's collected texts.
    words := beam.ParDo(s, func(line string, emit func(string)) {
        for _, word := range wordRE.FindAllString(line, -1) {
            emit(word)
        }
    }, lines)
    
    // Invoke the stats.Count transform on our PCollection of
    // individual words. The Count transform returns a new PCollection of
    // key/value pairs, where each key represents a unique word in the text.
    // The associated value is the occurrence count for that word.
    counted := stats.Count(s, words)
    
    // Use a ParDo to format our PCollection of word counts into a printable
    // string, suitable for writing to an output file. When each element
    // produces exactly one element, the DoFn can return it.
    formatted := beam.ParDo(s, func(w string, c int) string {
        return fmt.Sprintf("%s: %v", w, c)
    }, counted)
    
    // Invoke textio.Write at the end of the pipeline to write
    // the contents of a PCollection (in this case, our PCollection of
    // formatted strings) to a text file.
    textio.Write(s, "wordcounts.txt", formatted)

## Additional Apache Beam and Dataflow benefits

If you choose to migrate your App Engine MapReduce jobs to Apache Beam pipelines, you will benefit from several features that Apache Beam and Dataflow have to offer.

### Scheduling Dataflow jobs

If you are familiar with App Engine [task queues](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue), you can [schedule your recurring jobs using Cron](https://docs.cloud.google.com/appengine/docs/standard/python/config/cron). This [example](https://cloud.google.com/blog/products/bigquery/designing-etl-architecture-for-a-cloud-native-data-warehouse-on-google-cloud-platform) demonstrates how to use App Engine Cron to schedule your Apache Beam pipelines.

There are several additional ways to schedule execution of your pipeline. You can:

  * Use Dataflow [templates](https://docs.cloud.google.com/dataflow/docs/templates/overview) to stage your pipelines on Cloud Storage and execute them from a variety of environments.
  * Use [App Engine Cron service or Cloud Run functions](https://cloud.google.com/blog/products/data-analytics/scheduling-dataflow-pipelines-using-app-engine-cron-service-or-cloud-functions).
  * Use [Apache Airflow](https://airflow.incubator.apache.org/).



### Monitoring Dataflow jobs

To [monitor your App Engine MapReduce jobs](https://github.com/GoogleCloudPlatform/appengine-mapreduce/wiki/2.2-Monitoring-a-Job), you depend on an `appspot.com`-hosted URL.

When you execute your pipelines using the Dataflow managed service, you can monitor the pipelines using the convenient Dataflow web-based [monitoring user interface](https://docs.cloud.google.com/dataflow/pipelines/dataflow-monitoring-intf). You can also use [ Cloud Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring) for additional information about your pipelines.

### Reading and writing

In Apache Beam, App Engine MapReduce's [Readers and Writers](https://github.com/GoogleCloudPlatform/appengine-mapreduce/wiki/3.4-Readers-and-Writers) are called data sources and sinks, or [I/O connectors](https://beam.apache.org/documentation/io/built-in/) .

Apache Beam has many I/O connectors for several Google Cloud services, such as Bigtable, BigQuery, Datastore, Cloud SQL, and others. There are also I/O connectors created by Apache Beam contributors for non-Google services, such as Apache Cassandra and MongoDB.

## What's next

  * [Learn about the Apache Beam Programming Model](https://docs.cloud.google.com/dataflow/model/programming-model-beam)
  * [Learn how to design, create, and test your pipeline](https://docs.cloud.google.com/dataflow/pipelines/creating-a-pipeline-beam)
  * [Work through the example walkthroughs](https://docs.cloud.google.com/dataflow/examples/examples-beam)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
