---
url: https://docs.cloud.google.com/dataflow/docs/guides/job-graph/
title: Dataflow job graphs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:17.150699+00:00
---

# Dataflow job graphs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/job-graph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow job graphs Stay organized with collections  Save and categorize content based on your preferences. 

The Dataflow monitoring interface provides a graphical representation of each job: the _job graph_. The job graph also provides a job summary, a job log, and information about each step in the pipeline.

To view the job graph for a job, perform the following steps:

  1. In the Google Cloud console, go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Select a job.

  3. Click the **Job graph** tab.




By default, the job graph page displays the **Graph view**. To view your job graph as a table, in **Job steps view** , select **Table view**. The table view contains the same information in a different format. The table view is helpful in the following scenarios:

  * Your job has many stages, making the job graph difficult to navigate.
  * You want to sort the job steps by a specific property. For example, you can sort the table by [wall time](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel#wall-time) to identify slow steps.



## Graph view

The job graph represents each transform in the pipeline as a box. The following image shows a job graph with three transforms: `Read PubSub Events`, `5m Window`, and `Write File(s)`.

![Screenshot of the job graph in the monitoring UI](https://docs.cloud.google.com/static/dataflow/images/job-graph.png)

Each box contains the following information:

  * Transform name

  * Status; one of the following:

    * **Running** : the step is running
    * **Queued** : the step in a [FlexRS job](https://docs.cloud.google.com/dataflow/docs/guides/flexrs#delayed_scheduling) is queued
    * **Succeeded** : the step finished successfully
    * **Stopped** : the step stopped because the job stopped
    * **Unknown** : the step failed to report status
    * **Failed** : the step failed to complete
  * [Data lag](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel#data-watermark)

  * [Wall time](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel#wall-time)

  * [Maximum operation latency](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel#operation-latency)

  * The number of job stages that execute this step




If a step represents a [composite transform](https://beam.apache.org/documentation/programming-guide/#composite-transforms), you can expand the step to view the sub-transforms. To expand the step, click the expand_more **Expand node** arrow.

## Transform names

Dataflow has a few different ways to obtain the transform name that's shown in the monitoring job graph. Transform names are used in publicly-visible places, including the Dataflow monitoring interface, log files, and debugging tools. Don't use transform names that include personally identifiable information, such as usernames or organization names.

### Java

  * **Dataflow can use a name that you assign** when you apply your transform. The first argument you supply to the `apply` method is your transform name.
  * **Dataflow can infer the transform name** , either from the class name, if you build a custom transform, or the name of your `DoFn` function object, if you use a core transform such as `ParDo`.



### Python

  * **Dataflow can use a name that you assign** when you apply your transform. You can set the transform name by specifying the transform's `label` argument.
  * **Dataflow can infer the transform name** , either from the class name, if you build a custom transform, or the name of your `DoFn` function object, if you use a core transform such as `ParDo`.



### Go

  * **Dataflow can use a name that you assign** when you apply your transform. You can set the transform name by specifying the `Scope`.
  * **Dataflow can infer the transform name** , either from the struct name if you're using a structural `DoFn` or from the function name if you're using a functional `DoFn`.



## View step information

When you click a step in the job graph, the **Step Info** panel shows more details about the step. For more information, see [Job step information](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel).

## Bottlenecks

If Dataflow detects a bottleneck, the job graph shows an warning alert symbol on the affected steps. To see the cause of the bottleneck, click the step to open the [**Step Info** panel](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel). For more information, see [Troubleshoot bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks).

![Two job steps with bottleneck alerts](https://docs.cloud.google.com/static/dataflow/images/bottleneck-alert.png)

## Example job graphs

This section shows some example pipeline code and the corresponding job graphs.

### Basic job graph

**Pipeline Code:**

### Java
    
    
      // Read the lines of the input text.
      p.apply("ReadLines", TextIO.read().from(options.getInputFile()))
         // Count the words.
         .apply(new CountWords())
         // Write the formatted word counts to output.
         .apply("WriteCounts", TextIO.write().to(options.getOutput()));

### Python
    
    
    (
        pipeline
        # Read the lines of the input text.
        | 'ReadLines' >> beam.io.ReadFromText(args.input_file)
        # Count the words.
        | CountWords()
        # Write the formatted word counts to output.
        | 'WriteCounts' >> beam.io.WriteToText(args.output_path))

### Go
    
    
      // Create the pipeline.
      p := beam.NewPipeline()
        s := p.Root()
      // Read the lines of the input text.
      lines := textio.Read(s, *input)
      // Count the words.
      counted := beam.ParDo(s, CountWords, lines)
      // Write the formatted word counts to output.
      textio.Write(s, *output, formatted)

**Note:** Some names in the image to the right don't match the transform names in this SDK. |  **Job graph:** ![The execution graph for a WordCount pipeline as shown in the Dataflow monitoring
              interface.](https://docs.cloud.google.com/static/dataflow/images/dataflow-job-exec-graph-collapsed.png)  
---|---  
Figure 1: The pipeline code for a WordCount pipeline shown with the resulting execution graph in the Dataflow monitoring interface.

### Job graph with composite transforms

[Composite transforms](https://beam.apache.org/documentation/programming-guide/#composite-transforms) are transforms that contain multiple nested sub-transforms. In the job graph, composite transforms are expandable. To expand the transform and view the sub-transforms, click the arrow.

**Pipeline Code:**

### Java
    
    
      // The CountWords Composite Transform
      // inside the WordCount pipeline.
    
      public static class CountWords
        extends PTransform<PCollection<String>, PCollection<String>> {
    
        @Override
        public PCollection<String> apply(PCollection<String> lines) {
    
          // Convert lines of text into individual words.
          PCollection<String> words = lines.apply(
            ParDo.of(new ExtractWordsFn()));
    
          // Count the number of times each word occurs.
          PCollection<KV<String, Long>> wordCounts =
            words.apply(Count.<String>perElement());
    
          return wordCounts;
        }
      }

**Note:** `FormatCounts` in the image isn't relevant to this SDK.

### Python
    
    
    # The CountWords Composite Transform inside the WordCount pipeline.
    @beam.ptransform_fn
    def CountWords(pcoll):
      return (
          pcoll
          # Convert lines of text into individual words.
          | 'ExtractWords' >> beam.ParDo(ExtractWordsFn())
          # Count the number of times each word occurs.
          | beam.combiners.Count.PerElement()
          # Format each word and count into a printable string.
          | 'FormatCounts' >> beam.ParDo(FormatCountsFn()))

### Go
    
    
      // The CountWords Composite Transform inside the WordCount pipeline.
      func CountWords(s beam.Scope, lines beam.PCollection) beam.PCollection {
        s = s.Scope("CountWords")
    
        // Convert lines of text into individual words.
        col := beam.ParDo(s, &extractFn{SmallWordLength: *smallWordLength}, lines)
    
        // Count the number of times each word occurs.
        return stats.Count(s, col)
      }

**Note:** `FormatCounts` in the image isn't relevant to this SDK. Some names in the image don't match the transform names in this SDK. |  **Job graph:** ![The job graph for a WordCount pipeline with the CountWords transform expanded
              to show its component transforms.](https://docs.cloud.google.com/static/dataflow/images/dataflow-job-exec-graph-expanded.png)  
---|---  
Figure 2: The pipeline code for the sub-steps of the CountWords transform. Shown with the job graph expanded for the entire pipeline.

In your pipeline code, you might use the following code to invoke your composite transform:
    
    
    result = transform.apply(input);

Composite transforms invoked in this manner omit the expected nesting and might appear expanded in the Dataflow monitoring interface. Your pipeline might also generate warnings or errors about stable unique names at pipeline execution time.

To avoid these issues, invoke your transforms by using the [recommended format](https://docs.cloud.google.com/dataflow/model/transforms):

`result = input.apply(transform);`

## What's next

  * [View detailed job step information](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel)
  * [View job stages in the **Execution details** tab](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details)
  * [Troubleshoot your pipeline](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
