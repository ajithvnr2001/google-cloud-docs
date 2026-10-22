---
url: https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options/
title: Set Dataflow pipeline options \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:11.489923+00:00
---

# Set Dataflow pipeline options  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Set Dataflow pipeline options Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options) for your Dataflow jobs. These pipeline options configure how and where your pipeline runs and which resources it uses.

Pipeline execution is separate from your Apache Beam program's execution. The Apache Beam program that you've written constructs a pipeline for deferred execution. This means that the program generates a series of steps that any supported Apache Beam runner can execute. Compatible runners include the Dataflow runner on Google Cloud and the direct runner that executes the pipeline directly in a local environment.

You can pass parameters into a Dataflow job at runtime. For additional information about setting pipeline options at runtime, see [Configuring pipeline options](https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options).

**Note:** If you're creating a [classic template](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates) that accepts pipeline options, you must use the `ValueProvider` interface in your pipeline code. For more information, see [Use runtime parameters in your pipeline code](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates#runtimeparams).

## Use pipeline options with Apache Beam SDKs

You can use the following SDKs to set pipeline options for Dataflow jobs:

  * Apache Beam SDK for Python
  * Apache Beam SDK for Java
  * Apache Beam SDK for Go



To use the SDKs, you set the pipeline runner and other execution parameters by using the Apache Beam SDK class `PipelineOptions`.

There are two methods for specifying pipeline options:

  * Set pipeline options programmatically by supplying a list of pipeline options.
  * Set pipeline options directly on the command line when you run your pipeline code.



### Set pipeline options programmatically

You can set pipeline options programmatically by creating and modifying a `PipelineOptions` object.

### Java

Construct a [`PipelineOptions`](https://beam.apache.org/documentation/sdks/javadoc/current/index.html?org/apache/beam/sdk/options/PipelineOptions.html) object using the method `PipelineOptionsFactory.fromArgs`.

For an example, see the [Launch on Dataflow sample](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#java_6) section on this page.

### Python

Create a [`PipelineOptions`](https://beam.apache.org/releases/pydoc/current/apache_beam.options.pipeline_options.html) object.

For an example, see the [Launch on Dataflow sample](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#python_6) section on this page.

### Go

Setting pipeline options programmatically using `PipelineOptions` is not supported in the Apache Beam SDK for Go. Use Go command-line arguments.

For an example, see the [Launch on Dataflow sample](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#go_6) section on this page.

### Set pipeline options on the command line

You can set pipeline options by using command-line arguments.

### Java

The following example syntax is from the `WordCount` pipeline in the [Java tutorial](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-java#run-the-pipeline-on-the-dataflow-service).
    
    
    mvn -Pdataflow-runner compile exec:java \
      -Dexec.mainClass=org.apache.beam.examples.WordCount \
      -Dexec.args="--project=PROJECT_ID \
      --gcpTempLocation=gs://BUCKET_NAME/temp/ \
      --output=gs://BUCKET_NAME/output \
      --runner=DataflowRunner \
      --region=REGION"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `REGION`: a [Dataflow region](https://docs.cloud.google.com/dataflow/docs/resources/locations), `us-central1`



### Python

The following example syntax is from the `WordCount` pipeline in the [Python tutorial](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-python#run-the-pipeline-on-the-dataflow-service).
    
    
    python -m apache_beam.examples.wordcount \
      --region DATAFLOW_REGION \
      --input gs://dataflow-samples/shakespeare/kinglear.txt \
      --output gs://STORAGE_BUCKET/results/outputs \
      --runner DataflowRunner \
      --project PROJECT_ID \
      --temp_location gs://STORAGE_BUCKET/tmp/
    

Replace the following:

  * `DATAFLOW_REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy the Dataflow job—for example, `europe-west1`

The `--region` flag overrides the default region that is set in the metadata server, your local client, or environment variables.

  * `STORAGE_BUCKET`: the Cloud Storage bucket name

  * `PROJECT_ID`: the Google Cloud project ID




### Go

The following example syntax is from the `WordCount` pipeline in the [Go tutorial](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-go#run-the-pipeline-on-the-dataflow-service).
    
    
    go run wordcount.go --input gs://dataflow-samples/shakespeare/kinglear.txt \
       --output gs://BUCKET_NAME/results/outputs \
       --runner dataflow \
       --project PROJECT_ID \
       --region DATAFLOW_REGION \
       --staging_location gs://BUCKET_NAME/binaries/

Replace the following:

  * `BUCKET_NAME`: the Cloud Storage bucket name

  * `PROJECT_ID`: the Google Cloud project ID

  * `DATAFLOW_REGION`: The [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy the Dataflow job. For example, `europe-west1`. The `--region` flag overrides the default region that is set in the metadata server, your local client, or environment variables.




### Set experimental pipeline options

In the Java, Python, and Go SDKs, the `experiments` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#basic_options) enables experimental or pre-GA Dataflow features.

#### Set programmatically

To set the `experiments` option programmatically, use the following syntax.

### Java

In your [`PipelineOptions`](https://beam.apache.org/documentation/sdks/javadoc/current/index.html?org/apache/beam/sdk/options/PipelineOptions.html) object, include the `experiments` option by using the following syntax. This example sets the boot disk size to 80 GB with the experiment flag.
    
    
    options.setExperiments("streaming_boot_disk_size_gb=80")
    

For an example that shows how to create the `PipelineOptions` object, see the [Launch on Dataflow sample](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#java_6) section on this page.

### Python

In your [`PipelineOptions`](https://beam.apache.org/releases/pydoc/current/apache_beam.options.pipeline_options.html) object, include the `experiments` option by using the following syntax. This example sets the boot disk size to 80 GB with the experiment flag.
    
    
    beam_options = PipelineOptions(
      beam_args,
      experiments=['streaming_boot_disk_size_gb=80'])
    

For an example that shows how to create the `PipelineOptions` object, see the [Launch on Dataflow sample](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#python_6) section on this page.

### Go

Setting pipeline options programmatically using `PipelineOptions` is not supported in the Apache Beam SDK for Go. Use Go command-line arguments.

#### Set on the command line

To set the `experiments` option on the command line, use the following syntax.

### Java

This example sets the boot disk size to 80 GB with the experiment flag.
    
    
    --experiments=streaming_boot_disk_size_gb=80
    

### Python

This example sets the boot disk size to 80 GB with the experiment flag.
    
    
    --experiments=streaming_boot_disk_size_gb=80
    

### Go

This example sets the boot disk size to 80 GB with the experiment flag.
    
    
    --experiments=streaming_boot_disk_size_gb=80
    

#### Set in a template

To enable an experimental feature when running a Dataflow template, use the `--additional-experiments` flag.

### Classic template
    
    
    gcloud dataflow jobs run JOB_NAME --additional-experiments=EXPERIMENT[,...]
    

### Flex template
    
    
    gcloud dataflow flex-template run JOB_NAME --additional-experiments=EXPERIMENT[,...]
    

### Access the pipeline options object

When you create your `Pipeline` object in your Apache Beam program, pass `PipelineOptions`. When the Dataflow service runs your pipeline, it sends a copy of the `PipelineOptions` to each worker.

### Java

Access `PipelineOptions` inside any `ParDo` transform's `DoFn` instance by using the method `ProcessContext.getPipelineOptions`.

### Python

This feature is not supported in the Apache Beam SDK for Python.

### Go

Access pipeline options using `beam.PipelineOptions`.

## Launch on Dataflow

Run your job on managed Google Cloud resources by using the Dataflow runner service. Running your pipeline with Dataflow creates a Dataflow job, which uses Compute Engine and Cloud Storage resources in your Google Cloud project. For information about Dataflow permissions, see [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).

Dataflow jobs use Cloud Storage to store temporary files during pipeline execution. To avoid being billed for unnecessary storage costs, turn off the soft delete feature on buckets that your Dataflow jobs use for temporary storage. For more information, see [Disable soft delete](https://docs.cloud.google.com/storage/docs/disable-soft-delete).

**Note:** Typing `Ctrl+C` from the command line **does not** cancel your job. The Dataflow service is still running the job on Google Cloud. To cancel the job, use the [Dataflow Monitoring Interface](https://docs.cloud.google.com/dataflow/pipelines/dataflow-monitoring-intf) or the [Dataflow command-line interface](https://docs.cloud.google.com/dataflow/pipelines/dataflow-command-line-intf).

### Set required options

To run your pipeline using Dataflow, set the following pipeline options:

### Java

  * **`project`** : the ID of your Google Cloud project.
  * **`runner`** : the pipeline runner that executes your pipeline. For Google Cloud execution, this must be `DataflowRunner`.
  * **`gcpTempLocation`** : a Cloud Storage path for Dataflow to stage most temporary files. The specified bucket must already exist.

If you don't specify `gcpTempLocation`, then Dataflow uses the value of the `tempLocation` option. If you don't specify either of these options, then Dataflow creates a new Cloud Storage bucket.




### Python

  * **`project`** : your Google Cloud project ID.
  * **`region`** : the region for your Dataflow job.
  * **`runner`** : the pipeline runner that executes your pipeline. For Google Cloud execution, this must be `DataflowRunner`.
  * **`temp_location`** : a Cloud Storage path for Dataflow to stage temporary job files created during the execution of the pipeline.



### Go

  * **`project`** : your Google Cloud project ID.
  * **`region`** : the region for your Dataflow job.
  * **`runner`** : the pipeline runner that executes your pipeline. For Google Cloud execution, this must be `dataflow`.
  * **`staging_location`** : a Cloud Storage path for Dataflow to stage temporary job files created during the execution of the pipeline.



#### Set pipeline options programmatically

The following example code shows how to construct a pipeline by programmatically setting the runner and other required options to execute the pipeline using Dataflow.

### Java
    
    
    // Create and set your PipelineOptions.
    DataflowPipelineOptions options = PipelineOptionsFactory.as(DataflowPipelineOptions.class);
    
    // For cloud execution, set the Google Cloud project, staging location,
    // and set DataflowRunner.
    options.setProject("my-project-id");
    options.setStagingLocation("gs://my-bucket/binaries");
    options.setRunner(DataflowRunner.class);
    
    // Create the Pipeline with the specified options.
    Pipeline p = Pipeline.create(options);
    

### Python
    
    
    import argparse
    
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    
    parser = argparse.ArgumentParser()
    # parser.add_argument('--my-arg', help='description')
    args, beam_args = parser.parse_known_args()
    
    # Create and set your PipelineOptions.
    # For Cloud execution, specify DataflowRunner and set the Cloud Platform
    # project, job name, temporary files location, and region.
    # For more information about regions, check:
    # https://cloud.google.com/dataflow/docs/concepts/regional-endpoints
    beam_options = PipelineOptions(
        beam_args,
        runner='DataflowRunner',
        project='my-project-id',
        job_name='unique-job-name',
        temp_location='gs://my-bucket/temp',
        region='us-central1')
    # Note: Repeatable options like dataflow_service_options or experiments must
    # be specified as a list of string(s).
    # e.g. dataflow_service_options=['enable_prime']
    
    # Create the Pipeline with the specified options.
    with beam.Pipeline(options=beam_options) as pipeline:
      pass  # build your pipeline here.
    

### Go

The Apache Beam SDK for Go uses Go command-line arguments. Use [`flag.Set()`](https://pkg.go.dev/flag#Set) to set flag values.
    
    
    // Use the Go flag package to parse custom options.
    flag.Parse()
    
    // Set the required options programmatically.
    // For Cloud execution, specify the Dataflow runner, Google Cloud
    // project ID, region, and staging location.
    // For more information about regions, see
    // https://cloud.google.com/dataflow/docs/concepts/regional-endpoints
    flag.Set("runner", "dataflow")
    flag.Set("project", "my-project-id")
    flag.Set("region", "us-central1")
    flag.Set("staging_location", "gs://my-bucket/binaries")
    
    beam.Init()
    
    // Create the Pipeline.
    p := beam.NewPipeline()
    s := p.Root()
    

After you've constructed your pipeline, specify all the pipeline reads, transforms, and writes, and run the pipeline.

#### Use pipeline options from the command line

The following example shows how to use pipeline options that are specified on the command line. This example doesn't set the pipeline options programmatically.

### Java
    
    
    // Set your PipelineOptions to the specified command-line options
    MyOptions options = PipelineOptionsFactory.fromArgs(args).withValidation();
    
    // Create the Pipeline with the specified options.
    Pipeline p = Pipeline.create(options);
    

### Python

Use the [Python argparse module](https://docs.python.org/3/library/argparse.html) to parse command-line options.
    
    
    # Use Python argparse module to parse custom arguments
    import argparse
    
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    
    # For more details on how to use argparse, take a look at:
    #   https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input-file',
        default='gs://dataflow-samples/shakespeare/kinglear.txt',
        help='The file path for the input text to process.')
    parser.add_argument(
        '--output-path', required=True, help='The path prefix for output files.')
    args, beam_args = parser.parse_known_args()
    
    # Create the Pipeline with remaining arguments.
    beam_options = PipelineOptions(beam_args)
    with beam.Pipeline(options=beam_options) as pipeline:
      lines = (
          pipeline
          | 'Read files' >> beam.io.ReadFromText(args.input_file)
          | 'Write files' >> beam.io.WriteToText(args.output_path))
    

### Go

Use the [Go `flag` package](https://pkg.go.dev/flag) to parse command-line options. You must parse the options before you call `beam.Init()`. In this example, `output` is a command-line option.
    
    
    // Define configuration options
    var (
      output = flag.String("output", "", "Output file (required).")
    )
    
    // Parse options before beam.Init()
    flag.Parse()
    
    beam.Init()
    
    // Input validation must be done after beam.Init()
    if *output == "" {
      log.Fatal("No output provided!")
    }
    
    p := beam.NewPipeline()
    

After you construct your pipeline, specify all the pipeline reads, transforms, and writes, and then run the pipeline.

### Control execution modes

When an Apache Beam program runs a pipeline on a service such as Dataflow, the program can either run the pipeline asynchronously, or can block until pipeline completion. You can change this behavior by using the following guidance.

### Java

When an Apache Beam Java program runs a pipeline on a service such as Dataflow, it is typically executed asynchronously. To run a pipeline and wait until the job completes, set `DataflowRunner` as the pipeline runner and explicitly call `pipeline.run().waitUntilFinish()`.

When you use `DataflowRunner` and call `waitUntilFinish()` on the `PipelineResult` object returned from `pipeline.run()`, the pipeline executes on Google Cloud but the local code waits for the cloud job to finish and return the final `DataflowPipelineJob` object. While the job runs, the Dataflow service prints job status updates and console messages while it waits.

### Python

When an Apache Beam Python program runs a pipeline on a service such as Dataflow, it is typically executed asynchronously. To block until pipeline completion, use the `wait_until_finish()` method of the `PipelineResult` object, returned from the `run()` method of the runner.

### Go

When an Apache Beam Go program runs a pipeline on Dataflow, it is synchronous by default and blocks until pipeline completion. If you don't want to block, there are two options:

  1. Start the job in a Go routine.
         
         go func() {
           pr, err := beamx.Run(ctx, p)
           if err != nil {
             // Handle the error.
           }
           // Send beam.PipelineResult into a channel.
           results <- pr
         }()
         // Do other operations while the pipeline runs.
         

  2. Use the `--async` command-line flag, which is in the [`jobopts` package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/options/jobopts#pkg-variables).




To view execution details, monitor progress, and verify job completion status, use the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/pipelines/dataflow-monitoring-intf) or the [Dataflow command line interface](https://docs.cloud.google.com/dataflow/pipelines/dataflow-command-line-intf).

### Use streaming sources

### Java

If your pipeline reads from an unbounded data source, such as Pub/Sub, the pipeline automatically executes in streaming mode.

### Python

If your pipeline uses an unbounded data source, such as Pub/Sub, you must set the `streaming` option to true.

### Go

If your pipeline reads from an unbounded data source, such as Pub/Sub, the pipeline automatically executes in streaming mode.

Streaming jobs use a Compute Engine [machine type](https://docs.cloud.google.com/compute/docs/machine-types) with 2 or more vCPUs by default.

**Note:** If your pipeline uses unbounded data sources and sinks, you must pick a [Windowing](https://docs.cloud.google.com/dataflow/model/programming-model-beam) strategy for your unbounded PCollections before you use any aggregation such as a `GroupByKey`.

## Launch locally

Instead of running your pipeline on managed cloud resources, you can choose to execute your pipeline locally. Local execution has certain advantages for testing, debugging, or running your pipeline over small data sets. For example, local execution removes the dependency on the remote Dataflow service and associated Google Cloud project.

When you use local execution, you must run your pipeline with datasets small enough to fit in local memory. You can create a small in-memory dataset using a `Create` transform, or you can use a `Read` transform to work with small local or remote files. Local execution typically provides a faster and easier way to perform testing and debugging with fewer external dependencies, but is limited by the memory that is available in your local environment.

The following example code shows how to construct a pipeline that executes in your local environment.

### Java
    
    
    // Create and set our Pipeline Options.
    PipelineOptions options = PipelineOptionsFactory.create();
    
    // Create the Pipeline with the specified options.
    Pipeline p = Pipeline.create(options);
    

**Note:** For local mode, you don't need to set the runner because `DirectRunner` is already the default. However, you do need to either explicitly include `DirectRunner` as a dependency or add it to the classpath.

### Python
    
    
    import argparse
    
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    
    parser = argparse.ArgumentParser()
    # parser.add_argument('--my-arg')
    args, beam_args = parser.parse_known_args()
    
    # Create and set your Pipeline Options.
    beam_options = PipelineOptions(beam_args)
    args = beam_options.view_as(MyOptions)
    
    with beam.Pipeline(options=beam_options) as pipeline:
      lines = (
          pipeline
          | beam.io.ReadFromText(args.input)
          | beam.io.WriteToText(args.output))
    

**Note:** For local mode, you don't need to set the runner because `DirectRunner` is already the default.

### Go
    
    
    // Parse options before beam.Init()
    flag.Parse()
    
    beam.Init()
    
    p := beam.NewPipeline()
    

**Note:** For local mode, you don't need to set the runner because `direct` is already the default.

After you've constructed your pipeline, run it.

## Create custom pipeline options

You can add your own custom options in addition to the standard `PipelineOptions`. Apache Beam's command line can also parse custom options using command line arguments specified in the same format.

### Java

To add your own options, define an interface with getter and setter methods for each option, as in the following example:
    
    
    public interface MyOptions extends PipelineOptions {
      String getMyCustomOption();
      void setMyCustomOption(String myCustomOption);
    }
    

### Python

To add your own options, use the `add_argument()` method (which behaves exactly like Python's standard [argparse module](https://docs.python.org/3/library/argparse.html)), as in the following example:
    
    
    from apache_beam.options.pipeline_options import PipelineOptions
    
    class MyOptions(PipelineOptions):
      @classmethod
      def _add_argparse_args(cls, parser):
        parser.add_argument('--input')
        parser.add_argument('--output')
    
    

### Go

To add your own options, use the [Go flag package](https://pkg.go.dev/flag) as shown in the following example:
    
    
    var (
      input  = flag.String("input", "", "")
      output = flag.String("output", "", "")
    )
    

You can also specify a description, which appears when a user passes `--help` as a command-line argument, and a default value.

### Java

You set the description and default value using annotations, as follows:
    
    
    public interface MyOptions extends PipelineOptions {
      @Description("My custom command line argument.")
      @Default.String("DEFAULT")
      String getMyCustomOption();
      void setMyCustomOption(String myCustomOption);
    }
    

We recommend that you register your interface with `PipelineOptionsFactory` and then pass the interface when creating the `PipelineOptions` object. When you register your interface with `PipelineOptionsFactory`, the `--help` can find your custom options interface and add it to the output of the `--help` command. `PipelineOptionsFactory` validates that your custom options are compatible with all other registered options.

The following example code shows how to register your custom options interface with `PipelineOptionsFactory`:
    
    
    PipelineOptionsFactory.register(MyOptions.class);
    MyOptions options = PipelineOptionsFactory.fromArgs(args)
                                              .withValidation()
                                              .as(MyOptions.class);
    

Now your pipeline can accept `--myCustomOption=value` as a command-line argument.

### Python

You set the description and default value as follows:
    
    
    from apache_beam.options.pipeline_options import PipelineOptions
    
    class MyOptions(PipelineOptions):
      @classmethod
      def _add_argparse_args(cls, parser):
        parser.add_argument(
            '--input',
            default='gs://dataflow-samples/shakespeare/kinglear.txt',
            help='The file path for the input text to process.')
        parser.add_argument(
            '--output', required=True, help='The path prefix for output files.')
    
    

### Go

You set the description and default value as follows:
    
    
    var (
      input  = flag.String("input", "gs://MY_STORAGE_BUCKET/input", "Input for the pipeline")
      output = flag.String("output", "gs://MY_STORAGE_BUCKET/output", "Output for the pipeline")
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
