---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-run-template/
title: Run a template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:12.975482+00:00
---

# Run a template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-run-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Run a template Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates basic execution of a Dataflow template by job name and template path. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Running classic templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates)



## Code sample

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from googleapiclient.discovery import build
    
    # project = 'your-gcp-project'
    # job = 'unique-job-name'
    # template = 'gs://dataflow-templates/latest/Word_Count'
    # parameters = {
    #     'inputFile': 'gs://dataflow-samples/shakespeare/kinglear.txt',
    #     'output': 'gs://<your-gcs-bucket>/wordcount/outputs',
    # }
    
    dataflow = build("dataflow", "v1b3")
    request = (
        dataflow.projects()
        .templates()
        .launch(
            projectId=project,
            gcsPath=template,
            body={
                "jobName": job,
                "parameters": parameters,
            },
        )
    )
    
    response = request.execute()

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
