---
url: https://docs.cloud.google.com/profiler/docs/samples/profiler-python-appengine-flex/
title: Python App Engine flexible environment \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:50.672230+00:00
---

# Python App Engine flexible environment  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/samples/profiler-python-appengine-flex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Samples ](https://docs.cloud.google.com/profiler/docs/samples)



#  Python App Engine flexible environment Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to initialize Cloud Profiler with Python on App Engine flexible environment.

## Code sample

### Python

For more information, see the [Profiler Python API reference documentation](https://github.com/GoogleCloudPlatform/cloud-profiler-python). 

To authenticate to Profiler, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import googlecloudprofiler
    
    # Profiler initialization. It starts a daemon thread which continuously
    # collects and uploads profiles. Best done as early as possible.
    try:
        # service and service_version can be automatically inferred when
        # running on App Engine. project_id must be set if not running
        # on GCP.
        googlecloudprofiler.start(verbose=3)
    except (ValueError, NotImplementedError) as exc:
        print(exc)  # Handle errors here
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudprofiler). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
