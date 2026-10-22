---
url: https://docs.cloud.google.com/dataflow/docs/sample-template/
title: Run a sample template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:17.237693+00:00
---

# Run a sample template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/sample-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Run a sample template Stay organized with collections  Save and categorize content based on your preferences. 

The WordCount template is a batch pipeline that reads text from Cloud Storage, tokenizes the text lines into individual words, and performs a frequency count on each of the words. For more information about WordCount, see [WordCount Example Pipeline](https://docs.cloud.google.com/dataflow/examples/wordcount-example).

If the Cloud Storage bucket is outside of your [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview), create an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) that allows access to the bucket.

## Template parameters

Parameter | Description  
---|---  
`inputFile` | The Cloud Storage input file's path.  
`outputFile` | The Cloud Storage output file's path and prefix.  
  
## Run the WordCount template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the WordCount template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/latest/Word_Count \
        --region REGION_NAME \
        --parameters \
        inputFile=gs://dataflow-samples/shakespeare/kinglear.txt,output=gs://BUCKET_NAME/output/my_output
    

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 

  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`

  * `BUCKET_NAME`: the name of your Cloud Storage bucket




### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/latest/Word_Count
    {
        "jobName": "JOB_NAME",
        "parameters": {
           "inputFile" : "gs://dataflow-samples/shakespeare/kinglear.txt",
           "output": "gs://BUCKET_NAME/output/my_output"
        },
        "environment": { "zone": "us-central1-f" }
    }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 


  * `JOB_NAME`: a unique job name of your choice 

  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`

  * `BUCKET_NAME`: the name of your Cloud Storage bucket




### Template source code

### Java
    
    
    /*
     * Copyright (C) 2016 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License"); you may not
     * use this file except in compliance with the License. You may obtain a copy of
     * the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
     * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
     * License for the specific language governing permissions and limitations under
     * the License.
     */
    package com.google.cloud.teleport.templates;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.templates.WordCount.WordCountOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.metrics.Counter;
    import org.apache.beam.sdk.metrics.Metrics;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.Count;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.PTransform;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.SimpleFunction;
    import org.apache.beam.sdk.values.KV;
    import org.apache.beam.sdk.values.PCollection;
    
    /**
     * A template that counts words in text files.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Word_Count.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Word_Count",
        category = TemplateCategory.GET_STARTED,
        displayName = "Word Count",
        description =
            "Batch pipeline. Reads text from Cloud Storage, tokenizes text lines into individual words,"
                + " and performs frequency count on each of the words.",
        optionsClass = WordCountOptions.class,
        contactInformation = "https://cloud.google.com/support")
    public class WordCount {
    
      static class ExtractWordsFn extends DoFn<String, String> {
        private final Counter emptyLines = Metrics.counter(ExtractWordsFn.class, "emptyLines");
    
        @ProcessElement
        public void processElement(ProcessContext c) {
          // Check if the line is empty.
          if (c.element().trim().isEmpty()) {
            emptyLines.inc();
            return;
          }
    
          // Split the line into words.
          String[] words = c.element().split("[^a-zA-Z']+");
    
          // Output each word encountered into the output PCollection.
          for (String word : words) {
            if (!word.isEmpty()) {
              c.output(word);
            }
          }
        }
      }
    
      /** A SimpleFunction that converts a Word and Count into a printable string. */
      public static class FormatAsTextFn extends SimpleFunction<KV<String, Long>, String> {
        @Override
        public String apply(KV<String, Long> input) {
          return input.getKey() + ": " + input.getValue();
        }
      }
    
      /**
       * A PTransform that converts a PCollection containing lines of text into a PCollection of
       * formatted word counts.
       */
      public static class CountWords
          extends PTransform<PCollection<String>, PCollection<KV<String, Long>>> {
        @Override
        public PCollection<KV<String, Long>> expand(PCollection<String> lines) {
    
          // Convert lines of text into individual words.
          PCollection<String> words = lines.apply(ParDo.of(new ExtractWordsFn()));
    
          // Count the number of times each word occurs.
          PCollection<KV<String, Long>> wordCounts = words.apply(Count.<String>perElement());
    
          return wordCounts;
        }
      }
    
      /**
       * Options supported by {@link com.google.cloud.teleport.templates.WordCount}.
       *
       * <p>Inherits standard configuration options.
       */
      public interface WordCountOptions extends PipelineOptions {
    
        @TemplateParameter.GcsReadFile(
            order = 1,
            description = "Input file(s) in Cloud Storage",
            helpText =
                "The input file pattern Dataflow reads from. Use the example file "
                    + "(gs://dataflow-samples/shakespeare/kinglear.txt) or enter the path to your own "
                    + "using the same format: gs://your-bucket/your-file.txt")
        ValueProvider<String> getInputFile();
    
        void setInputFile(ValueProvider<String> value);
    
        @TemplateParameter.GcsWriteFolder(
            order = 2,
            description = "Output Cloud Storage file prefix",
            helpText = "Path and filename prefix for writing output files. Ex: gs://your-bucket/counts")
        ValueProvider<String> getOutput();
    
        void setOutput(ValueProvider<String> value);
      }
    
      public static void main(String[] args) {
        WordCountOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(WordCountOptions.class);
        Pipeline p = Pipeline.create(options);
        p.apply("ReadLines", TextIO.read().from(options.getInputFile()))
            .apply(new CountWords())
            .apply(MapElements.via(new FormatAsTextFn()))
            .apply("WriteCounts", TextIO.write().to(options.getOutput()));
    
        p.run();
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
