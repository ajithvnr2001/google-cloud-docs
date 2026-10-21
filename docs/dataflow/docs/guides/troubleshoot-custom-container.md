---
url: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-custom-container/
title: Troubleshoot custom containers in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:02.230531+00:00
---

# Troubleshoot custom containers in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-custom-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Troubleshoot custom containers in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for troubleshooting issues that might occur when using custom containers with Dataflow. It focuses on issues with containers or workers not starting. If your workers are able to start and work is progressing, follow the general guidance for [Troubleshooting your pipeline](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline).

Before contacting support, ensure that you have ruled out problems related to your container image:

  * Follow the steps to [test your container image locally](https://docs.cloud.google.com/dataflow/docs/guides/run-custom-container#testing-locally).
  * Search for errors in the [Job logs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline#check_job_error_messages) or in Worker logs, and compare any errors found with the [common error](https://docs.cloud.google.com/dataflow/docs/guides/common-errors) guidance.
  * Make sure that the Apache Beam SDK version and language version that you're using to launch the pipeline match the SDK version on your custom container image.
  * If using Java, make sure that the Java major version you use to launch the pipeline matches the version installed in your container image.
  * If using Python, make sure that the Python major-minor version you use to launch the pipeline matches the version installed in your container image, and that the image does not have conflicting dependencies. You can run [`pip check`](https://pip.pypa.io/en/stable/cli/pip_check/) to confirm.



## Find worker logs related to custom containers

Fine the Dataflow worker logs for container-related error messages can by using [Logs Explorer](https://console.cloud.google.com/logs/query):

  1. Select log names. Custom container startup errors are most likely to be in one of the following:

     * `dataflow.googleapis.com/kubelet`
     * `dataflow.googleapis.com/docker`
     * `dataflow.googleapis.com/worker-startup`
     * `dataflow.googleapis.com/harness-startup`
  2. Select the `Dataflow Step` resource and specify the `job_id`.


**Note:** You can also find the worker logs directly from the **Job** page. Select **Logs > Worker Logs > Go to Logs Explorer**.

If you're seeing `Error Syncing pod...` log messages, follow the common [error guidance](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#error-syncing-pod). You can query for these log messages in Dataflow worker logs by using [Logs Explorer](https://console.cloud.google.com/logs/query) with the following query:
    
    
    resource.type="dataflow_step" AND jsonPayload.message:("IMAGE_URI") AND severity="ERROR"
    

## Common Issues

The following are some common issues when using custom containers.

### Job has errors or failed because container image cannot be pulled

Dataflow workers must be able to access custom container images. If the worker is unable to pull the image due to invalid URLs, misconfigured credentials, or missing network access, the worker fails to start.

For batch jobs where no work has started and several workers are unable to start sequentially, Dataflow fails the job. Otherwise, Dataflow logs errors but does not take further action to avoid destroying long-running job state.

For information about how to fix this issue, see [Image pull request failed with error](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#error-pulling-container-image) in the Troubleshoot Dataflow errors page.

### Workers are not starting or work is not progressing

Sometimes, if the SDK container fails to start due to an error, Dataflow is unable to determine whether the error is permanent or fatal. Dataflow then continuously attempts to restart the worker.

If there are no obvious errors but you see `[topologymanager] RemoveContainer` `INFO`-level logs in `dataflow.googleapis.com/kubelet`, these logs indicate that the custom container image is exiting early and did not start the long-running worker SDK process.

If workers have started successfully but no work is happening, an error might be preventing the SDK container from starting. In this case, the following error appears in the diagnostic recommendations:
    
    
    Failed to start container
    

In addition, the worker logs don't contain lines such as the following:
    
    
    Executing: python -m apache_beam.runners.worker.sdk_worker_main or Executing: java ... FnHarness
    

Find specific errors in Worker logs and check [common error guidance](https://docs.cloud.google.com/dataflow/docs/guides/common-errors).

Common causes for these issues include the following:

  * Problems with package installation, such as `pip` installation errors due to dependency issues. See [Error syncing pod ... failed to "StartContainer"](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#error-syncing-pod).
  * If the container used is not compatible with the worker VM's CPU architecture, you might see errors like `exec format error`. For more information, see [Error syncing pod ... failed to "StartContainer"](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#error-syncing-pod).
  * Errors with the custom command arguments or with the `ENTRYPOINT` set in the Dockerfile. For example, a custom `ENTRYPOINT` does not start the default boot script `/opt/apache/beam/boot` or does not pass arguments appropriately to this script. For more information, see [Modifying the container entrypoint](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#custom-entrypoint).
  * Errors when the Apache Beam SDK version is mismatched between the launch environment and the runtime environment. In one failure mode, the default values that are set in the Apache Beam SDK pipeline options might become unrecognized. For example, you might see errors such as `sdk_worker_main.py: error: argument --flink_version: invalid choice: '1.16' (choose from '1.12', '1.13', '1.14', '1.15')` in the worker logs. To remediate, install the same version of the Apache Beam SDK in the container image as you use to launch the pipeline. For more information, see [Make the launch environment compatible with the runtime environment](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies#make-the-launch-environment-compatible-with-the-runtime-environment).



### Running as a non-root user isn't supported

In general, you're not able to run custom SDK container images or custom template container images for Flex Templates as a non-root user. If you try to run containers as a non-root user, the pipeline fails.

For more information, see [Runtime environment](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#runtime-environment), or contact your [account team](https://docs.cloud.google.com/dataflow/docs/support/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
