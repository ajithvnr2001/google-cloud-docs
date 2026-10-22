---
url: https://docs.cloud.google.com/profiler/docs/samples/profiler-python-quickstart/
title: Initializing Cloud Profiler on Google Compute Engine or Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:50.643100+00:00
---

# Initializing Cloud Profiler on Google Compute Engine or Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/samples/profiler-python-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Samples ](https://docs.cloud.google.com/profiler/docs/samples)



#  Initializing Cloud Profiler on Google Compute Engine or Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to initialize Cloud Profiler with Python on Google Compute Engine or Google Kubernetes Engine.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Profiling Python applications](https://docs.cloud.google.com/profiler/docs/profiling-python)



## Code sample

### Python

For more information, see the [Profiler Python API reference documentation](https://github.com/GoogleCloudPlatform/cloud-profiler-python). 

To authenticate to Profiler, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import googlecloudprofiler
    
    
    def main():
        # Profiler initialization. It starts a daemon thread which continuously
        # collects and uploads profiles. Best done as early as possible.
        try:
            googlecloudprofiler.start(
                service="hello-profiler",
                service_version="1.0.1",
                # verbose is the logging level. 0-error, 1-warning, 2-info,
                # 3-debug. It defaults to 0 (error) if not set.
                verbose=3,
                # project_id must be set if not running on GCP.
                # project_id='my-project-id',
            )
        except (ValueError, NotImplementedError) as exc:
            print(exc)  # Handle errors here

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudprofiler). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
