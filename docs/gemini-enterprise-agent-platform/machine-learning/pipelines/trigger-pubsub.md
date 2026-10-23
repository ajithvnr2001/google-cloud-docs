---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/trigger-pubsub/
title: Trigger a pipeline run with Pub/Sub \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:54.831655+00:00
---

# Trigger a pipeline run with Pub/Sub  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/trigger-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Trigger a pipeline run with Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to write, deploy, and trigger a pipeline run using an [Event-Driven Cloud Function](https://docs.cloud.google.com/functions/docs/writing#event-driven_functions) with a [Cloud Pub/Sub trigger](https://docs.cloud.google.com/functions/docs/calling/pubsub). Follow these steps:

  1. Define an ML pipeline using the Kubeflow Pipelines (KFP) SDK and compile it into a YAML file.

  2. Upload the compiled pipeline definition to a Cloud Storage bucket.

  3. Use Cloud Run functions to create, configure, and deploy a function that's triggered by a new or existing Pub/Sub topic.




### Define and compile a pipeline

Using Kubeflow Pipelines SDK, build a scheduled pipeline and compile it into a YAML file.

Sample `hello-world-scheduled-pipeline`:
    
    
    from kfp import compiler
    from kfp import dsl
    
    # A simple component that prints and returns a greeting string
    @dsl.component
    def hello_world(message: str) -> str:
        greeting_str = f'Hello, {message}'
        print(greeting_str)
        return greeting_str
    
    # A simple pipeline that contains a single hello_world task
    @dsl.pipeline(
        name='hello-world-scheduled-pipeline')
    def hello_world_scheduled_pipeline(greet_name: str):
        hello_world_task = hello_world(greet_name)
    
    # Compile the pipeline and generate a YAML file
    compiler.Compiler().compile(pipeline_func=hello_world_scheduled_pipeline,
                                package_path='hello_world_scheduled_pipeline.yaml')
    

### Upload compiled pipeline YAML to Cloud Storage bucket

  1. Open the Cloud Storage browser in the Google Cloud console.  


[Cloud Storage Browser](https://console.cloud.google.com/storage/browser/)

  2. Click the Cloud Storage bucket you created when you [configured your project](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-project).

  3. Using either an existing folder or a new folder, upload your compiled pipeline YAML (in this example `hello_world_scheduled_pipeline.yaml`) to the selected folder.

  4. Click the uploaded YAML file to access the details. Copy the **gsutil URI** for later use.




### Create a Cloud Run functions with a Pub/Sub trigger

  1. Visit the Cloud Run functions page in the console.

[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click the **Create function** button.

  3. In the **Basics** section, give your function a name (for example `my-scheduled-pipeline-function`).

  4. In the **Trigger** section, select **Cloud Pub/Sub** as the Trigger type.

![create function configuration choose pubsub as Trigger type image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/pipelines/images/trigger-type-cloud-pubsub.png)

  5. In the **Select a Cloud Pub/Sub topic** list, click **Create a topic**.

  6. In the **Create a topic** box, give your new topic a name (for example `my-scheduled-pipeline-topic`), and select **Create topic**.

  7. Leave all other fields as default and click **Save** to save the Trigger section configuration.

  8. Leave all other fields as default and click **Next** to proceed to the Code section.

  9. Under **Runtime** , select **Python 3.7**.

  10. In **Entry** point, input "subscribe" (the example code entry point function name).

  11. Under **Source code** , select **Inline Editor** if it's not already selected.

  12. In the `main.py` file, add in the following code:
         
         import base64
           import json
           from google.cloud import aiplatform
         
           PROJECT_ID = 'your-project-id'                     # <---CHANGE THIS
           REGION = 'your-region'                             # <---CHANGE THIS
           PIPELINE_ROOT = 'your-cloud-storage-pipeline-root' # <---CHANGE THIS
         
           def subscribe(event, context):
             """Triggered from a message on a Cloud Pub/Sub topic.
             Args:
                   event (dict): Event payload.
                   context (google.cloud.functions.Context): Metadata for the event.
             """
             # decode the event payload string
             payload_message = base64.b64decode(event['data']).decode('utf-8')
             # parse payload string into JSON object
             payload_json = json.loads(payload_message)
             # trigger pipeline run with payload
             trigger_pipeline_run(payload_json)
         
           def trigger_pipeline_run(payload_json):
             """Triggers a pipeline run
             Args:
                   payload_json: expected in the following format:
                     {
                       "pipeline_spec_uri": "<path-to-your-compiled-pipeline>",
                       "parameter_values": {
                         "greet_name": "<any-greet-string>"
                       }
                     }
             """
             pipeline_spec_uri = payload_json['pipeline_spec_uri']
             parameter_values = payload_json['parameter_values']
         
             # Create a PipelineJob using the compiled pipeline from pipeline_spec_uri
             aiplatform.[init](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.html)(
                 project=PROJECT_ID,
                 location=REGION,
             )
             job = aiplatform.[PipelineJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.PipelineJob.html)(
                 display_name='hello-world-pipeline-cloud-function-invocation',
                 template_path=pipeline_spec_uri,
                 pipeline_root=PIPELINE_ROOT,
                 enable_caching=False,
                 parameter_values=parameter_values
             )
         
             # Submit the PipelineJob
             job.submit()
         

Replace the following:

     * PROJECT_ID: The Google Cloud project that this pipeline runs in.
     * REGION: The region that this pipeline runs in.
     * PIPELINE_ROOT: Specify a Cloud Storage URI that your pipelines service account can access. The artifacts of your pipeline runs are stored in the pipeline root.
  13. In the `requirements.txt` file, replace the contents with the following package requirements:
         
         google-api-python-client>=1.7.8,<2
         google-cloud-aiplatform
         

  14. Click **deploy** to deploy the Function.




## What's next

  * Learn more about [Google Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs).
  * [Visualize and analyze pipeline results](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/visualize-pipeline).
  * Learn how to [create triggers in Cloud Runfrom Pub/Sub events](https://docs.cloud.google.com/functions/docs/calling/pubsub).
  * To view code samples for using Pub/Sub, refer to the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?p=pubsub).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
