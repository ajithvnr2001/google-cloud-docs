---
url: https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-best-practices/
title: Best practices for highly parallel workflows \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:27.250161+00:00
---

# Best practices for highly parallel workflows  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Best practices for highly parallel workflows Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance about best practices to follow when building and running Dataflow HPC highly parallel workflows, including how to use external code in your pipelines, how to run the pipeline, and how to manage error handling.

**Note:** When discussing supported code for Dataflow, this document concentrates on the Java SDK for Apache Beam. You can also use the Python SDK. Many of the discussion points are relevant for both. Example code for this guide is available in the Apache Beam [GitHub repository](https://github.com/apache/beam/tree/master/examples/java/src/main/java/org/apache/beam/examples/subprocess). For an example that uses the Python SDK, see the [Use custom containers with C++ libraries](https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-tutorial) tutorial.

## Include external code in your pipeline

A key differentiator for highly parallel pipelines is that they use C++ code within the [`DoFn`](https://beam.apache.org/documentation/programming-guide/#creating-a-dofn) rather than one of the standard Apache Beam SDK languages. For Java pipelines, to make it easier to use C++ libraries in the pipeline, it is recommended that you use external procedure calls. This section describes the general approach used for running external (C++) code in Java pipelines.

An Apache Beam pipeline definition has several key components:

  * `PCollections` are immutable collections of homogeneous elements.
  * `PTransforms` are used to define the transformations to a `PCollection` that generates another `PCollection`. 
  * The pipeline is the construct that allows you, through code, to declare the interactions between `PTransforms` and `PCollections`. The pipeline is represented as a [directed acyclic graph (DAG)](https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-about#dag). 



When you use code from a language that is not one of the standard Apache Beam SDK languages, place the code in the `PTransform`, which is within the `DoFn`, and use one of the standard SDK languages to define the pipeline itself. We recommend using the Apache Beam Python SDK to define the pipeline, because the Python SDK has a utility class that makes the use of other code simpler. You can, however, use the other Apache Beam SDKs.

You can use the code to conduct quick experiments without requiring a full build. For a production system, you typically create your own binaries, which gives you the freedom to tune the process to your needs.

The following diagram illustrates the two usages of pipeline data:

  * Data is used to drive the process.
  * Data is acquired during processing and joined to the driver data.



![Two stages of pipeline data](https://docs.cloud.google.com/static/dataflow/images/running-external-binaries-beam-grid-computing-2-stages-of-pipeline.svg)

On this page, primary data (from the source) is referred to as _driving data_ , and secondary data (from the processing phase) is referred to as _joining data_.

In a finance use case, the driving data might be a few hundred thousand trades. Each trade needs to be processed in conjunction with market data. In that case, the market data is the joining data. In a media use case, the driving data might be image files that require processing but don't need other data sources, and therefore don't use joining data.

### Size considerations for driving data

If the size of the driving data element is in the low-megabyte range, treat it with the normal Apache Beam paradigm of creating a `PCollection` object from the source and sending the object to the Apache Beam transforms for processing.

If the size of the driving data element is in the high megabytes or in the gigabytes, as is typical for media, you can put the driving data into Cloud Storage. Then, in the starting `PCollection` object, reference the storage URI, and only a URI reference to that data is used.

### Size considerations for joining data

If the joining data is a few hundred megabytes or less, use a [side input](https://beam.apache.org/documentation/programming-guide/#side-inputs) to get this data to the Apache Beam transforms. The side input sends the data packet to every worker that needs it.

If the joining data is in the gigabyte or terabyte range, use either Bigtable or Cloud Storage to merge the joining data to the driving data, depending on the nature of the data. Bigtable is ideal for finance scenarios where market data is often accessed as key-value lookups from Bigtable. For more information about designing your Bigtable schema, including recommendations for working with time-series data, see the following Bigtable documentation:

  * [Schema design](https://docs.cloud.google.com/bigtable/docs/schema-design)
  * [Schema design with time-series data](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series)



## Run the external code

You can run external code in Apache Beam in many ways.

  * Create a process that's called from a `DoFn` object inside a Dataflow transform.

  * Use [JNI](https://wikipedia.org/wiki/Java_Native_Interface) with the Java SDK.

**Note:** JNI provides a method for passing data into and out of the external library. Because JNI is very efficient, this approach is ideal if the C++ library is well established and stable. However, if the C++ code is prone to crashing, C++ code can generate [segfaults](https://wikipedia.org/wiki/Segmentation_fault). Trying to catch these errors is problematic, because any failure can also take down the calling process, resulting in a Dataflow retry of that bundle of work.
  * Create a subprocess directly from the `DoFn` object. Although this approach is not the most efficient, it's robust and straightforward to implement. Because of the potential issues with using JNI, this page demonstrates using a subprocess call.




As you design your workflow, consider the complete end-to-end pipeline. Any inefficiencies in the way the process is run are offset by the fact that the data movement from the source all the way to the sink is accomplished with a single pipeline. If you compare this approach to others, look at the end-to-end times of the pipeline as well as end-to-end costs.

### Pull the binaries into the hosts

When you use a supported Apache Beam language, the Apache Beam SDK [automatically moves all required code to the workers](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#parallelization-and-distribution). However, when you make a call to external code, you must move the code manually.

![Binary files stored in buckets](https://docs.cloud.google.com/static/dataflow/images/running-external-binaries-beam-grid-computing-binaries-in-buckets.svg)

To move the code, do the following. The example demonstrates the steps for the Apache Beam Java SDK.

  1. Store the compiled external code, along with versioning information, in Cloud Storage.
  2. In the [`@Setup`](https://beam.apache.org/documentation/sdks/javadoc/current/org/apache/beam/sdk/transforms/DoFn.Setup.html) method, create a synchronized block to check whether the code file is available on the local resource. Rather than implementing a physical check, you can confirm availability using a static variable when the first thread finishes.
  3. If the file isn't available, use the Cloud Storage client library to pull the file from the Cloud Storage bucket to the local worker. A recommended approach is to use the Apache Beam [`FileSystems`](https://beam.apache.org/documentation/sdks/javadoc/current/org/apache/beam/sdk/io/FileSystems.html) class for this task.
  4. After the file is moved, confirm that the execute bit is set on the code file.
  5. In a production system, check the hash of the binaries to ensure that the file has been copied correctly.



Using the Apache Beam [`filesToStage`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/options/FileStagingOptions.html#setFilesToStage-java.util.List-) function is also an option, but it removes some of the advantages of the runner's ability to automatically package and move your Java code. In addition, because the call to the subprocess needs an absolute file location, you need to use code to determine the class path and therefore the location of the file moved by `filesToStage`. We don't recommend this approach.

### Run the external binaries

Before you can run external code, you need to build a wrapper for it. Write this wrapper in the same language as the external code (for example, C++) or as a shell script. The wrapper lets you pass file handles and implement optimizations as described in the Design processing for small CPU cycles section on this page. Your wrapper does not need to be sophisticated. The following snippet shows an outline of a wrapper in C++.
    
    
    int main(int argc, char* argv[])
    {
        if(argc < 3){
            std::cerr << "Required return file and data to process" << '\n';
            return 1;
        }
    
        std::string returnFile = argv[1];
        std::string word = argv[2];
    
        std::ofstream myfile;
        myfile.open (returnFile);
        myfile << word;
        myfile.close();
        return 0;
    }
    

This code reads two parameters from the argument list. The first parameter is the location of the return file where the data is pushed. The second parameter is the data that the code echoes to the user. In real-world implementations, this code would do more than echo "Hello, world"!

After you write the wrapper code, run the external code by doing the following:

  1. Transmit the data to the external code binaries.
  2. Run the binaries, catch any errors, and log errors and results.
  3. Handle the logging information.
  4. Capture data from the completed processing.



### Transmit the data to the binaries

To start the process of running the library, transmit data to the C++ code. This step is where you can take advantage of Dataflow integration with other Google Cloud tools. A tool like Bigtable can deal with very large datasets and handle low-latency and high-concurrency access, which allows thousands of cores to simultaneously access the dataset. In addition, Bigtable can preprocess data, allowing data shaping, enrichment, and filtering. All of this work can be done in Apache Beam [transforms](https://beam.apache.org/documentation/programming-guide/#transforms) before you run the external code.

For a production system, the recommended path is to use a [protocol buffer](https://developers.google.com/protocol-buffers/) to encapsulate the input data. You can convert the input data to bytes and base64 encode it before passing it to the external library. The two ways to pass this data to the external library are as follows:

  * Small input data. For small data that doesn't exceed the system's maximum length for a command argument, pass the argument in position 2 of the process being built with `java.lang.ProcessBuilder`.
  * Large input data. For larger data sizes, create a file whose name includes a [UUID](https://wikipedia.org/wiki/Universally_unique_identifier) in order to contain the data required by the process.



### Run the C++ code, catch errors, and log

Capturing and handling error information is a critical part of your pipeline. The resources used by the Dataflow runner are ephemeral, and it's often difficult to inspect worker log files. You must make sure that you capture and push all useful information to Dataflow runner logging, and that you store the logging data in one or more Cloud Storage buckets.

The recommended approach is to redirect `stdout` and `stderr` to files, which lets you avoid any out-of-memory considerations. For example, in the Dataflow runner that calls the C++ code, you could include lines like the following:

###  Java 
    
    
      import java.lang.ProcessBuilder.Redirect;
      ...
          processbuilder.redirectError(Redirect.appendTo(errfile));
          processbuilder.redirectOutput(Redirect.appendTo(outFile));
    

###  Python 
    
    
    # Requires Apache Beam 2.34 or later.
    stopping_times, bad_values = (
        integers
        | beam.Map(collatz.total_stopping_time).with_exception_handling(
            use_subprocess=True))
    
    # Write the bad values to a side channel.
    bad_values | 'WriteBadValues' >> beam.io.WriteToText(
        os.path.splitext(output_path)[0] + '-bad.txt')
    

#### Handle logging information

Many use cases involve processing millions of elements. Successful processing generates logs with little or no value, so you must make a business decision about retaining the log data. For example, consider these alternatives to retaining all log data:

  * If information contained in logs from successful element processing isn't valuable, don't keep it.
  * Create logic that samples the log data, such as sampling only every 10,000 log entries. If the processing is homogenous, such as when many iterations of the code generate essentially identical log data, this approach provides an effective balance between retaining log data and optimizing processing.



For failure conditions, the amount of data dumped to logs might be large. An effective strategy for handling large quantities of error log data is to read the first few lines of the log entry and push just those lines to Cloud Logging. You can load the rest of the log file into Cloud Storage buckets. This approach lets you look at the first lines of the error logs later and then, if needed, refer to Cloud Storage for the whole file.

Checking the size of the log file is also useful. If the file size is zero, you can safely ignore it or record a log message that the file had no data.

### Capture data from completed processing

It's not recommended that you use `stdout` to pass the result of the computation back to the `DoFn` function. Other code that your C++ code calls, and even your own code, might send messages to `stdout` as well, polluting the `stdoutput` stream that otherwise contains logging data. Instead, it's a better practice to make a change to the C++ wrapper code to allow the code to accept a parameter indicating where to create the file that stores the value. Ideally, this file should be stored in a language-neutral way using [protocol buffers](https://developers.google.com/protocol-buffers/docs/overview), which allows the C++ code to pass an object back to the Java or Python code. The `DoFn` object can read the result directly from the file and pass the result information on to its own `output` call.

Experience has shown the importance of running [unit tests](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines#unit-tests) dealing with the process itself. It's important to implement a unit test that runs the process independently of the Dataflow pipeline. Debugging the library can be done much more efficiently if it is standalone and doesn't have to run the whole pipeline.

## Design processing for small CPU cycles

Calling a subprocess has overhead. Depending on your workload, you might need to do extra work to reduce the ratio between work being done and the administrative overhead of starting and shutting down the process.

In the media use case, the size of the driving data element might be in the high megabytes or in the gigabytes. As a result, processing for each data element can take many minutes. In that case, the cost of calling the subprocess is insignificant compared to the overall processing time. The best approach in this situation is to have a single element start its own process.

However, in other use cases, such as finance, processing requires very small units of CPU time (tens of milliseconds). In that case, the overhead of calling the subprocess is disproportionately large. A solution to this issue is to make use of Apache Beam's [`GroupByKey`](https://beam.apache.org/documentation/programming-guide/#groupbykey) transform to create batches of between 50 and 100 elements to be fed into the process. For example, you can follow these steps:

  * In a [`DoFn`](https://beam.apache.org/documentation/programming-guide/#creating-a-dofn) function, create a key-value pair. If you are processing financial trades, you can use the trade number as the key. If you don't have a unique number to use as the key, you can generate a checksum from the data and use a modulo function to create partitions of 50 elements.
  * Send the key to a [`GroupByKey.create`](https://beam.apache.org/documentation/programming-guide/#groupbykey) function, which returns a `KV<key,Iterable<data>>` collection that contains the 50 elements that you can then send to the process.



## Limit worker parallelism

When you work with a language that's natively supported in the Dataflow runner, you never need to think about what's happening to the worker. Dataflow has many processes that oversee flow control and threads in batch or stream mode.

However, if you're using an external language like C++, be aware that you're doing something a little out of the ordinary by starting subprocesses. In batch mode, the Dataflow runner uses a small ratio of working threads to CPUs compared to streaming mode. It's recommended, especially in streaming mode, that you create a semaphore within your class to more directly control an individual worker's parallelism.

For example, with media processing, you might not want hundreds of transcoding elements to be processed in parallel by a single worker. In cases like those, you can create a utility class that provides permits to the `DoFn` function for the work being carried out. Using this class lets you take direct control of the worker threads within your pipeline.

## Use high-capacity data sinks in Google Cloud

After the data has been processed, it's sent to a data sink. The sink needs to be able to handle the volume of results that are created by your grid processing solution.

The following diagram shows some of the sinks available in Google Cloud when Dataflow is running a grid workload.

![Sinks available in Google Cloud](https://docs.cloud.google.com/static/dataflow/images/running-external-binaries-beam-grid-computing-sinks.svg)

Bigtable, BigQuery, and Pub/Sub can all deal with very large streams of data. For example, each Bigtable node can handle 10,000 inserts per second of up to 1K in size with horizontal scalability. As a result, a 100-node Bigtable cluster can absorb 1,000,000 messages per second generated by the Dataflow grid.

## Manage segfaults

When you use C++ code within a pipeline, you need to decide how to manage segfaults, because they have non-local ramifications if not dealt with correctly. The Dataflow runner creates processes as needed in Java, Python, or Go, and then assigns work to the processes in the form of bundles.

If the call to the C++ code is done using tightly coupled tools, such as [JNI](https://wikipedia.org/wiki/Java_Native_Interface) or Cython, and the C++ process segfaults, the calling process and Java Virtual Machine (JVM) also crash. In this scenario, bad data points aren't catchable. To make bad data points catchable, use a looser coupling, which branches away bad data and allows the pipeline to continue. However, with mature C++ code that is fully tested against all data variations, you can use mechanisms like Cython.

## What's next

  * Follow the [tutorial](https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-tutorial) to create a pipeline that uses custom containers with C++ libraries.

  * View the example code for this page in the Apache Beam [GitHub repository](https://github.com/apache/beam/tree/master/examples/java/src/main/java/org/apache/beam/examples/subprocess).

  * Learn more about [building pipelines with Apache Beam](https://beam.apache.org/documentation/programming-guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
