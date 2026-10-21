---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates/
title: Creating classic Dataflow templates \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:38.994289+00:00
---

# Creating classic Dataflow templates  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Creating classic Dataflow templates Stay organized with collections  Save and categorize content based on your preferences. 

In this document, you learn how to create a custom classic template from your Dataflow pipeline code. Classic templates package existing Dataflow pipelines to create reusable templates that you can customize for each job by changing specific pipeline parameters. Rather than writing the template, you use a command to generate the template from an existing pipeline. 

The following is a brief overview of the process. Details of this process are provided in subsequent sections.

  1. In your pipeline code, use the [`ValueProvider`](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates#about-runtime-parameters-and-the-valueprovider-interface) interface for all pipeline options that you want to set or use at runtime. Use `DoFn` objects that accept runtime parameters.
  2. Extend your template with additional metadata so that custom parameters are validated when the classic template is run. Examples of such metadata include the name of your custom classic template and optional parameters.
  3. Check if the pipeline I/O connectors support `ValueProvider` objects, and make changes as required.
  4. Create and stage the custom classic template.
  5. Run the custom classic template.



To learn about the different kinds of Dataflow templates, their benefits, and when to choose a classic template, see [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).

## Required permissions for running a classic template

The permissions that you need to run the Dataflow classic template depend on where you run the template, and whether your source and sink for the pipeline are in another project.

For more information about running Dataflow pipelines either locally or by using Google Cloud, see [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).

For a list of Dataflow roles and permissions, see [Dataflow access control](https://docs.cloud.google.com/dataflow/docs/concepts/access-control).

## Limitations

  * The following [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#resource_utilization) isn't supported with classic templates. If you need to control the number of worker harness threads, use [Flex Templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates). 

### Java
        
        numberOfWorkerHarnessThreads
          

### Python
        
        number_of_worker_harness_threads
          

  * The Dataflow runner doesn't support the `ValueProvider` options for Pub/Sub topics and subscription parameters. If you require Pub/Sub options in your runtime parameters, use Flex Templates.



## About runtime parameters and the `ValueProvider` interface

The `ValueProvider` interface allows pipelines to accept runtime parameters. Apache Beam provides three types of `ValueProvider` objects.

Name | Description  
---|---  
`RuntimeValueProvider` |  `RuntimeValueProvider` is the default `ValueProvider` type. `RuntimeValueProvider` allows your pipeline to accept a value that is only available during pipeline execution. The value is not available during pipeline construction, so you can't use the value to change your pipeline's workflow graph. You can use `isAccessible()` to check if the value of a `ValueProvider` is available. If you call `get()` before pipeline execution, Apache Beam returns an error:  
` Value only available at runtime, but accessed from a non-runtime context.` Use `RuntimeValueProvider` when you do not know the value ahead of time. To change the parameter values at runtime, do not set values for the parameters in the template. Set the values for the parameters when you create jobs from the template.  
`StaticValueProvider` |  `StaticValueProvider` lets you provide a static value to your pipeline. The value is available during pipeline construction, so you can use the value to change your pipeline's workflow graph. Use `StaticValueProvider` when you know the value ahead of time. See the StaticValueProvider section for examples.  
`NestedValueProvider` |  `NestedValueProvider` lets you compute a value from another `ValueProvider` object. `NestedValueProvider` wraps a `ValueProvider`, and the type of the wrapped `ValueProvider` determines whether the value is accessible during pipeline construction. Use `NestedValueProvider` when you want to use the value to compute another value at runtime. See the NestedValueProvider section for examples.  
  
## Use runtime parameters in your pipeline code

This section walks through how to use `ValueProvider`, `StaticValueProvider`, and `NestedValueProvider`.

**Note:** If you don't use the `ValueProvider` interface in your classic template, the pipeline options that you want to set or use at runtime might be ignored.

### Use `ValueProvider` in your pipeline options

Use `ValueProvider` for all pipeline options that you want to set or use at runtime.

For example, the following `WordCount` code snippet does not support runtime parameters. The code adds an input file option, creates a pipeline, and reads lines from the input file:

### Java
    
    
      public interface WordCountOptions extends PipelineOptions {
        @Description("Path of the file to read from")
        @Default.String("gs://dataflow-samples/shakespeare/kinglear.txt")
        String getInputFile();
        void setInputFile(String value);
      }
    
      public static void main(String[] args) {
        WordCountOptions options =
              PipelineOptionsFactory.fromArgs(args).withValidation()
                .as(WordCountOptions.class);
        Pipeline p = Pipeline.create(options);
    
        p.apply("ReadLines", TextIO.read().from(options.getInputFile()));
        ...

### Python
    
    
      class WordcountOptions(PipelineOptions):
        @classmethod
        def _add_argparse_args(cls, parser):
          parser.add_argument(
              '--input',
              default='gs://dataflow-samples/shakespeare/kinglear.txt',
              help='Path of the file to read from')
          parser.add_argument(
              '--output',
              required=True,
              help='Output file to write results to.')
      pipeline_options = PipelineOptions(['--output', 'some/output_path'])
      p = beam.Pipeline(options=pipeline_options)
    
      wordcount_options = pipeline_options.view_as(WordcountOptions)
      lines = p | 'read' >> ReadFromText(wordcount_options.input)

To add runtime parameter support, modify the input file option to use `ValueProvider`.

### Java

Use `ValueProvider<String>` instead of `String` for the type of the input file option.
    
    
      public interface WordCountOptions extends PipelineOptions {
        @Description("Path of the file to read from")
        @Default.String("gs://dataflow-samples/shakespeare/kinglear.txt")
        ValueProvider<String> getInputFile();
        void setInputFile(ValueProvider<String> value);
      }
    
      public static void main(String[] args) {
        WordCountOptions options =
              PipelineOptionsFactory.fromArgs(args).withValidation()
                .as(WordCountOptions.class);
        Pipeline p = Pipeline.create(options);
    
        p.apply("ReadLines", TextIO.read().from(options.getInputFile()));
        ...

### Python

Replace `add_argument` with `add_value_provider_argument`.
    
    
     class WordcountOptions(PipelineOptions):
        @classmethod
        def _add_argparse_args(cls, parser):
          # Use add_value_provider_argument for arguments to be templatable
          # Use add_argument as usual for non-templatable arguments
          parser.add_value_provider_argument(
              '--input',
              default='gs://dataflow-samples/shakespeare/kinglear.txt',
              help='Path of the file to read from')
          parser.add_argument(
              '--output',
              required=True,
              help='Output file to write results to.')
      pipeline_options = PipelineOptions(['--output', 'some/output_path'])
      p = beam.Pipeline(options=pipeline_options)
    
      wordcount_options = pipeline_options.view_as(WordcountOptions)
      lines = p | 'read' >> ReadFromText(wordcount_options.input)

### Use `ValueProvider` in your functions

To use runtime parameter values in your own functions, update the functions to use `ValueProvider` parameters.

The following example contains an integer `ValueProvider` option, and a simple function that adds an integer. The function depends on the `ValueProvider` integer. During execution, the pipeline applies `MySumFn` to every integer in a `PCollection` that contains `[1, 2, 3]`. If the runtime value is 10, the resulting `PCollection` contains `[11, 12, 13]`.

### Java
    
    
      public interface SumIntOptions extends PipelineOptions {
          // New runtime parameter, specified by the --int
          // option at runtime.
          ValueProvider<Integer> getInt();
          void setInt(ValueProvider<Integer> value);
      }
    
      class MySumFn extends DoFn<Integer, Integer> {
          ValueProvider<Integer> mySumInteger;
    
          MySumFn(ValueProvider<Integer> sumInt) {
              // Store the value provider
              this.mySumInteger = sumInt;
          }
    
          @ProcessElement
          public void processElement(ProcessContext c) {
             // Get the value of the value provider and add it to
             // the element's value.
             c.output(c.element() + mySumInteger.get());
          }
      }
    
      public static void main(String[] args) {
        SumIntOptions options =
              PipelineOptionsFactory.fromArgs(args).withValidation()
                .as(SumIntOptions.class);
    
        Pipeline p = Pipeline.create(options);
    
        p.apply(Create.of(1, 2, 3))
          // Get the value provider and pass it to MySumFn
         .apply(ParDo.of(new MySumFn(options.getInt())))
         .apply("ToString", MapElements.into(TypeDescriptors.strings()).via(x -> x.toString()))
         .apply("OutputNums", TextIO.write().to("numvalues"));
    
        p.run();
      }

### Python
    
    
      import apache_beam as beam
      from apache_beam.options.pipeline_options import PipelineOptions
      from apache_beam.options.value_provider import StaticValueProvider
      from apache_beam.io import WriteToText
    
      class UserOptions(PipelineOptions):
        @classmethod
        def _add_argparse_args(cls, parser):
          parser.add_value_provider_argument('--templated_int', type=int)
    
      class MySumFn(beam.DoFn):
        def __init__(self, templated_int):
          self.templated_int = templated_int
    
        def process(self, an_int):
          yield self.templated_int.get() + an_int
    
      pipeline_options = PipelineOptions()
      p = beam.Pipeline(options=pipeline_options)
    
      user_options = pipeline_options.view_as(UserOptions)
      sum = (p
             | 'ReadCollection' >> beam.io.ReadFromText(
                 'gs://some/integer_collection')
             | 'StringToInt' >> beam.Map(lambda w: int(w))
             | 'AddGivenInt' >> beam.ParDo(MySumFn(user_options.templated_int))
             | 'WriteResultingCollection' >> WriteToText('some/output_path'))

### Use `StaticValueProvider`

To provide a static value to your pipeline, use `StaticValueProvider`.

This example uses `MySumFn`, which is a `DoFn` that takes a `ValueProvider<Integer>`. If you know the value of the parameter ahead of time, you can use `StaticValueProvider` to specify your static value as a `ValueProvider`. 

### Java

This code gets the value at pipeline runtime:
    
    
      .apply(ParDo.of(new MySumFn(options.getInt())))

Instead, you can use `StaticValueProvider` with a static value:
    
    
      .apply(ParDo.of(new MySumFn(StaticValueProvider.of(10))))

### Python

This code gets the value at pipeline runtime:
    
    
      beam.ParDo(MySumFn(user_options.templated_int))

Instead, you can use `StaticValueProvider` with a static value:
    
    
      beam.ParDo(MySumFn(StaticValueProvider(int,10)))

You can also use `StaticValueProvider` when you implement an I/O module that supports both regular parameters and runtime parameters. `StaticValueProvider` reduces the code duplication from implementing two similar methods.

### Java

The source code for this example is from Apache Beam's [TextIO.java on GitHub](https://github.com/apache/beam/blob/master/sdks/java/core/src/main/java/org/apache/beam/sdk/io/TextIO.java).
    
    
      // Create a StaticValueProvider<String> from a regular String parameter
      // value, and then call .from() with this new StaticValueProvider.
      public Read from(String filepattern) {
        checkNotNull(filepattern, "Filepattern cannot be empty.");
        return from(StaticValueProvider.of(filepattern));
      }
    
      // This method takes a ValueProvider parameter.
      public Read from(ValueProvider<String> filepattern) {
        checkNotNull(filepattern, "Filepattern cannot be empty.");
        return toBuilder().setFilepattern(filepattern).build();
      }

### Python

In this example, there is a single constructor that accepts both a `string` or a `ValueProvider` argument. If the argument is a `string`, it is converted to a `StaticValueProvider`.
    
    
    class Read():
    
      def __init__(self, filepattern):
        if isinstance(filepattern, str):
          # Create a StaticValueProvider from a regular string parameter
          filepattern = StaticValueProvider(str, filepattern)
    
        self.filepattern = filepattern

### Use `NestedStaticValueProvider`

To compute a value from another `ValueProvider` object, use `NestedValueProvider`.

`NestedValueProvider` takes a `ValueProvider` and a `SerializableFunction` translator as input. When you call `.get()` on a `NestedValueProvider`, the translator creates a new value based on the `ValueProvider` value. This translation lets you use a `ValueProvider` value to create the final value that you want.

**Note:** `NestedValueProvider` accepts only one value input. You can't use a `NestedValueProvider` to combine two different values.

In the following example, the user provides the filename `file.txt`. The transform prepends the path `gs://directory_name/` to the filename. Calling `.get()` returns `gs://directory_name/file.txt`.

### Java
    
    
      public interface WriteIntsOptions extends PipelineOptions {
          // New runtime parameter, specified by the --fileName
          // option at runtime.
          ValueProvider<String> getFileName();
          void setFileName(ValueProvider<String> value);
      }
    
      public static void main(String[] args) {
         WriteIntsOptions options =
              PipelineOptionsFactory.fromArgs(args).withValidation()
                .as(WriteIntsOptions.class);
        Pipeline p = Pipeline.create(options);
    
        p.apply(Create.of(1, 2, 3))
         // Write to the computed complete file path.
         .apply("OutputNums", TextIO.write().to(NestedValueProvider.of(
            options.getFileName(),
            new SerializableFunction<String, String>() {
              @Override
              public String apply(String file) {
                return "gs://directoryname/" + file;
              }
            })));
    
        p.run();
      }

## Use metadata in your pipeline code

You can extend your template with additional metadata so that custom parameters are validated when the template is run. If you want to create metadata for your template, follow these steps:

  1. Create a JSON-formatted file named `TEMPLATE_NAME_metadata` using the parameters in Metadata parameters and the format in Example metadata file. Replace `TEMPLATE_NAME` with the name of your template. 

Ensure the metadata file does not have a filename extension. For example, if your template name is `myTemplate`, then its metadata file must be `myTemplate_metadata`. 

  2. Store the metadata file in Cloud Storage in the same folder as the template.



### Metadata parameters

Parameter key |  | Required | Description of the value  
---|---|---|---  
**`name`** |  | Yes | The name of your template.  
**`description`** |  | No | A short paragraph of text describing the template.  
**`streaming`** |  | No | If `true`, this template supports streaming. The default value is `false`.  
**`supportsAtLeastOnce`** |  | No | If `true`, this template supports at-least-once processing. The default value is `false`. Set this parameter to `true` if the template is designed to work with [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes).   
**`supportsExactlyOnce`** |  | No | If `true`, this template supports [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once). The default value is `true`.  
**`defaultStreamingMode`** |  | No | The default streaming mode, for templates that support both at-least-once mode and exactly-once mode. Use one of the following values: `"AT_LEAST_ONCE"`, `"EXACTLY_ONCE"`. If unspecified, the default streaming mode is exactly-once.   
**`parameters`** |  | No | An array of additional parameters that the template uses. An empty array is used by default.  
**`name`** | Yes | The name of the parameter that is used in your template.  
**`label`** | Yes | A human readable string that is used in the Google Cloud console to label the parameter.  
**`helpText`** | Yes | A short paragraph of text that describes the parameter.  
**`isOptional`** | No | `false` if the parameter is required and `true` if the parameter is optional. Unless set with a value, `isOptional` defaults to `false`. If you do not include this parameter key for your metadata, the metadata becomes a required parameter.  
**`regexes`** | No | An array of POSIX-egrep regular expressions in string form that is used to validate the value of the parameter. For example, `["^[a-zA-Z][a-zA-Z0-9]+"]` is a single regular expression that validates that the value starts with a letter and then has one or more characters. An empty array is used by default.  
  
### Example metadata file

### Java

The Dataflow service uses the following metadata to validate the [WordCount template's](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/master/v1/src/main/java/com/google/cloud/teleport/templates/WordCount.java) custom parameters:
    
    
    {
      "description": "An example pipeline that counts words in the input file.",
      "name": "Word Count",
      "streaming": false,
      "parameters": [
        {
          "regexes": [
            "^gs:\\/\\/[^\\n\\r]+$"
          ],
          "name": "inputFile",
          "helpText": "Path of the file pattern glob to read from - for example, gs://dataflow-samples/shakespeare/kinglear.txt",
          "label": "Input Cloud Storage file(s)"
        },
        {
          "regexes": [
            "^gs:\\/\\/[^\\n\\r]+$"
          ],
          "name": "output",
          "helpText": "Path and filename prefix for writing output files - for example, gs://MyBucket/counts",
          "label": "Output Cloud Storage file(s)"
        }
      ]
    }

### Python

The Dataflow service uses the following metadata to validate the [WordCount template's](https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount.py) custom parameters:
    
    
    {
      "description": "An example pipeline that counts words in the input file.",
      "name": "Word Count",
      "streaming": false,
      "parameters": [
        {
          "regexes": [
            "^gs:\\/\\/[^\\n\\r]+$"
          ],
          "name": "input",
          "helpText": "Path of the file pattern glob to read from - for example, gs://dataflow-samples/shakespeare/kinglear.txt",
          "label": "Input Cloud Storage file(s)"
        },
        {
          "regexes": [
            "^gs:\\/\\/[^\\n\\r]+$"
          ],
          "name": "output",
          "helpText": "Path and filename prefix for writing output files - for example, gs://MyBucket/counts",
          "label": "Output Cloud Storage file(s)"
        }
      ]
    }

You can download metadata files for the Google-provided templates from the Dataflow [template directory](https://console.cloud.google.com/storage/browser/dataflow-templates/latest). 

## Supported pipeline I/O connectors and `ValueProvider`

### Java

Some I/O connectors contain methods that accept `ValueProvider` objects. To determine support for a specific connector and method, see the [API reference documentation](https://beam.apache.org/documentation/sdks/javadoc/current/) for the I/O connector. Supported methods have an overload with a `ValueProvider`. If a method does not have an overload, the method does not support runtime parameters. The following I/O connectors have at least partial `ValueProvider` support:

  * File-based IOs: `TextIO`, `AvroIO`, `FileIO`, `TFRecordIO`, `XmlIO`
  * `BigQueryIO`*****
  * `BigtableIO` (requires SDK 2.3.0 or later)
  * `PubSubIO`
  * `SpannerIO`

*** Note:** If you want to run a batch pipeline that reads from BigQuery, you must use `.withTemplateCompatibility()` on all BigQuery reads.

### Python

Some I/O connectors contain methods that accept `ValueProvider` objects. To determine support for I/O connectors and their methods, see the [API reference documentation](https://beam.apache.org/documentation/sdks/pydoc/current/) for the connector. The following I/O connectors accept runtime parameters:

  * File-based IOs: `textio`, `avroio`, `tfrecordio`



## Create and stage a classic template

After you write your pipeline, you must create and stage your template file. When you create and stage a template, the staging location contains additional files that are necessary to run your template. If you delete the staging location, the template fails to run. The Dataflow job does not run immediately after you stage the template. To run a custom template-based Dataflow job, you can use the [Google Cloud console](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates#custom-templates), the [Dataflow REST API](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates#using-the-rest-api), or the [gcloud CLI](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates#using-gcloud).

**Note:** Creating and staging a template requires authentication. For instructions about how to create a service account and a service account key, see the quickstart for the language you are using: [Java quickstart](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-java), [Python quickstart](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python), or [Go quickstart](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-go).

The following example shows how to stage a template file:

### Java

This Maven command creates and stages a template at the Cloud Storage location specified with `--templateLocation`.

**Note:** If you use the Apache Beam SDK for Java 2.15.0 or later, you must specify `--region`.
    
    
        mvn compile exec:java \
         -Dexec.mainClass=com.example.myclass \
         -Dexec.args="--runner=DataflowRunner \
                      --project=PROJECT_ID \
                      --stagingLocation=gs://BUCKET_NAME/staging \
                      --templateLocation=gs://BUCKET_NAME/templates/TEMPLATE_NAME \
                      --region=REGION" \
         -P dataflow-runner
        

Verify that the `templateLocation` path is correct. Replace the following:

  * `com.example.myclass`: your Java class
  * `PROJECT_ID`: your project ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `TEMPLATE_NAME`: the name of your template
  * `REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) to deploy your Dataflow job in



### Python

This Python command creates and stages a template at the Cloud Storage location specified with `--template_location`.

**Note:** If you use the Apache Beam SDK for Python 2.15.0 or later, you must specify `--region`.
    
    
      python -m examples.mymodule \
        --runner DataflowRunner \
        --project PROJECT_ID \
        --staging_location gs://BUCKET_NAME/staging \
        --template_location gs://BUCKET_NAME/templates/TEMPLATE_NAME \
        --region REGION
    

Verify that the `template_location` path is correct. Replace the following:

  * `examples.mymodule`: your Python module
  * `PROJECT_ID`: your project ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `TEMPLATE_NAME`: the name of your template
  * `REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) to deploy your Dataflow job in



After you create and stage your template, your next step is to [run the template](https://docs.cloud.google.com/dataflow/docs/templates/running-templates). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
