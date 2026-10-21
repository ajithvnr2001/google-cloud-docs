---
url: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates/
title: Troubleshoot Flex Templates \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:25.210608+00:00
---

# Troubleshoot Flex Templates  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Troubleshoot Flex Templates Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting tips and debugging strategies that you might find helpful if you're using Dataflow Flex Templates. By default, the Flex Template launch process has a timeout of 12 mins. This launch process includes pulling the template container image and executing the code to construct the job graph. If the launch doesn't complete within this 12 minute window, the job fails with the error "Timeout in polling result file". This information can help you detect a polling timeout, determine the reason behind the timeout, and correct the problem.

## Error loading template list in the Google Cloud console

In the Google Cloud console, when you try to view the list of templates in the Dataflow **Create job from template** page, you see an error similar to the following:
    
    
    Error retrieving templates. Custom templates can still be used.
    

If your organization uses [principal access boundary (PAB) policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies), principals (such as users or service accounts) might be blocked from viewing and running Google-provided templates. To resolve this issue, try the guidance in [Access Google-provided templates with principal access boundary policies](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#access-templates-pab).

## Polling timeout errors

Your job might return one of the following error messages:
    
    
    Timeout in polling result file: FILE_PATH. Possible causes are:
    1. Your launch takes too long time to finish. Please check the logs on stackdriver.
    2. Service account SERVICE_ACCOUNT may not have enough permissions to pull
    container image IMAGE_PATH or create new objects in FILE_PATH.
    3. Transient errors occurred, please try again.
    
    
    
    Timeout in polling result file: FILE_PATH.
    Service account: SERVICE_ACCOUNT
    Image URL: IMAGE_PATH
    Troubleshooting guide at https://cloud.google.com/dataflow/docs/guides/common-errors#timeout-polling
    

This error can occur for the following reasons:

  1. The base Docker image was overridden.
  2. The service account that fills in SERVICE_ACCOUNT does not have some necessary permissions.
  3. External IP addresses are disabled, and VMs can't connect to the set of external IP addresses used by Google APIs and services.
  4. The launcher VM cannot resolve or access gcr.io.
  5. Large Flex Template container image.
  6. The program that creates the graph takes too long to finish.
  7. Code running in the launcher VM takes too long to finish.
  8. Intermittent network or Cloud Storage errors.
  9. Pipeline options are being overwritten.
  10. Python users: Installing or staging dependencies takes too long.
  11. There was a transient error.



To resolve this issue, first check for transient errors by checking the job logs and retrying.

Follow the guidance in the Early startup issues section to enable serial port logging, which might reveal additional information.

If those steps don't resolve the issue, try the following troubleshooting steps.

### Optional: Run templates to further diagnose your issue

To further identify which of the previous reasons might be causing this error, use the following strategies:

  1. Run the [WordCount](https://docs.cloud.google.com/dataflow/docs/sample-template) Google-provided template. Be sure to provide parameters unique to your use case, such as the subnetwork from a Shared VPC project, private IP for worker VMs, and Dataflow worker service account you want to use. For more information on how to provide these parameters, see the [gcloud Reference](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) and [API Reference](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).

If you're able to complete this job successfully, that indicates that Networking, IAM Permissions, and [ Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) are likely configured correctly.

  2. Complete the [Run a pipeline by using the job builder](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-job-builder) quickstart, which runs the job as a Flex Template. If your job fails before launching the worker VM, [access the launcher VM](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) and try to download a sample Docker image using a command similar to the following:
         
         docker run --entrypoint /bin/bash -it gcr.io/dataflow-templates/2025-03-11-00_rc02/yaml-template
         

If this command fails, there may be a networking issue with downloading images. In this case, work with your internal networking team.

  3. Run a [Google-provided Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) and check the result. If the Google-provided template job completes successfully, this indicates that the problem is likely related to your specific custom template code files. In this case you need to continue troubleshooting your specific code to resolve the issue.




### Verify Docker entrypoint

Try this step if you're running a template from a custom Docker image rather than using one of the provided templates.

Check for the container entrypoint using the following command:
    
    
    docker inspect $TEMPLATE_IMAGE
    

The following output is expected:

### Java

`/opt/google/dataflow/java_template_launcher`

### Python

`/opt/google/dataflow/python_template_launcher`

If you get a different output, then the entrypoint of your Docker container is overridden. Restore `$TEMPLATE_IMAGE` to the default.

### Check service account permissions

Check that the service account mentioned in the message has the following permissions:

  * It must be able to read and write the Cloud Storage path that fills in `${file_path}` in the message.
  * It must be able to read the Docker image that fills in `${image_url}` in the message.



### Configure Private Google Access

If external IP addresses are disabled, you need to allow Compute Engine VMs to connect to the set of external IP addresses used by [Google APIs and services](https://developers.google.com/apis-explorer/). Enable Private Google Access on the subnet used by the network interface of the VM.

For configuration details, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

By default, when a Compute Engine VM lacks an external IP address assigned to its network interface, it can only send packets to other internal IP address destinations.

### GCR.io access issues

Flex Template launcher VMs require access to `gcr.io` to pull a logging agent container (`gcr.io/dataflow-templates-base/template-launcher-logger-distroless`). This agent is responsible for streaming launcher logs to Cloud Logging. If the launcher VM cannot resolve or connect to `gcr.io`, the startup process might stop responding, leading to a polling timeout.

This issue can occur even if your custom template image is stored in Artifact Registry, because the logging agent is always pulled from `gcr.io`.

To diagnose and resolve this issue:

  1. **Enable serial port logging** : Follow the steps in the Early startup issues section. If you see that the `cloud-init` process is stuck or if there are errors related to `gcr-wait-online.service`, a DNS or networking issue is likely.

  2. **SSH into the launcher VM** : Use the `gcloud compute ssh` command to connect to the launcher VM while it is still running:
         
         gcloud compute ssh launcher-JOB_ID --tunnel-through-iap
         

Replace `JOB_ID` with the ID of your Dataflow job.

  3. **Verify DNS resolution** : Run the following commands inside the launcher VM:
         
         curl -I https://gcr.io
         

If the command fails with a `"Could not resolve host"` error, your DNS configuration is missing an entry for `gcr.io`.

  4. **Check for stuck startup services** : Examine the `cloud-init` output log:
         
         sudo cat /var/log/cloud-init-output.log
         

Look for messages indicating that the process is waiting for the network or for `gcr.io` to become accessible.




Additionally, make sure that your VPC's DNS settings allow for the resolution of `gcr.io`. In some private network configurations, you might need to add a specific DNS `A` record for `gcr.io` pointing to the [Restricted Google APIs or Private Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-options) IP ranges.

### Large container image

If your Flex Template container image is large, pulling and launching the template may exceed the default 12-minute timeout leading to job failure.

To mitigate the issue, try the following strategies :

  * Optimize your image to reduce its size to speed up the pulling process.
  * Use the `--launcher-machine-type` flag to select a machine type with more CPU cores, which helps pull the image faster and leads to a faster launch.
  * Use the `--launcher-vm-timeout-secs` flag to specify a longer timeout duration for the launcher VM, allowing it to go beyond the default 12-minute limit.



### Check if the launcher program fails to exit

The program that constructs the pipeline must finish before the pipeline can be launched. The polling error could indicate that it took too long to do so.

Some things you can do to locate the cause in code are:

  * Make sure no threads are blocking the program from exiting. Some clients might create their own threads, and if these clients are not shut down, the program waits forever for these threads to be joined.
  * In the code that defines your pipeline, don't use `waitUntilFinish` (for Java) or `wait_until_finish` (for Python). These functions block the program from exiting, which prevents the Flex Template from launching the pipeline.



Pipelines launched directly that don't use a template don't have these limitations. Therefore, if the pipeline worked directly but not as a template, then the use of a template might be the root cause. Finding the issue in the template and fixing the template might resolve the issue.

### Long-running code in the launcher VM

If the code in your main program takes too long to execute, the Flex Template might time out before the pipeline launches. This can happen if the code performs complex computations or makes synchronous calls to external resources during initialization.

To diagnose this issue, [check the job logs](https://docs.cloud.google.com/dataflow/docs/guides/logging#MonitoringLogs) for any operation that takes a long time to complete. Examples include requests for external resources, large data lookups, or heavy initialization logic that you can move to the pipeline execution phase.

### Intermittent network or Cloud Storage errors

Intermittent "Timeout in polling result file" or "Failed to read the result file" errors can occur due to high network latency or transient issues with the Cloud Storage API. Chronic network contention in your VPC, specifically within the Private Google Access path, often causes latencies of 400–500 ms.

A "Timeout in polling result file" is typically a slow failure, while a "Failed to read the result file" is a fast failure, but both often indicate the same underlying connectivity issue.

To diagnose these intermittent failures:

  1. **Check for network latency** : Monitor the network latency within your VPC. Sustained high latency can cause timeouts when the launcher VM attempts to write or read the job result file from Cloud Storage.
  2. **Monitor Cloud Storage API metrics** :

     1. In the Google Cloud console, navigate to the **APIs & Services** dashboard.

[Go to Enabled APIs & services](https://console.cloud.google.com/project/_/apis/dashboard)

     2. Filter and select the **Cloud Storage API**.

     3. Review the charts for **Traffic** (sent and received bytes) and **Error rate**.

     4. Look for spikes in **5xx errors** (such as 503 errors) that align with the exact time of the job failures.




If you identify spikes in errors or high latency, investigate your VPC's network performance or [contactCloud Customer Care](https://docs.cloud.google.com/dataflow/docs/support/getting-support) for assistance with potential service disruptions.

### Verify whether required pipeline options are suppressed

When using Flex Templates, you can configure some but not all pipeline options during pipeline initialization. For more information, see the Failed to read the job file section in this document.

### Python users: Dependency management

If you're running a Python Flex Template job that supplies extra dependencies in a `requirements.txt` file, your job might fail to launch. This failure happens when downloading or installing the dependencies specified in the requirements file takes longer than the time allocated for launching the Flex template.

To optimize your job's performance, prepackage the dependencies when building your template to avoid the necessity to download or install the dependencies during template launch. For more information, see the [Package dependencies for Python](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#dependencies-python) section in "Configure Flex Templates."

## Job launch failures

The following section contains common errors that lead to job launch failures and steps for resolving or troubleshooting the errors.

### Permission denied when loading a template file

When you try to run a Google-provided template using the gcloud CLI, you see an error similar to the following:
    
    
    ERROR: (gcloud.dataflow.flex-template.run) PERMISSION_DENIED: Template file
    failed to load: TEMPLATE_PATH. Permissions denied.
    USER does not have storage.objects.get access to the Google
    Cloud Storage object. Operations on resource are denied due to an IAM
    Principal Access Boundary Policy.
    

`TEMPLATE_PATH` is a path to a template in a Cloud Storage bucket that contains the Google-provided templates, such as `gs://dataflow-templates` or `gs://dataflow-templates-REGION_NAME`.

If your organization uses [principal access boundary (PAB) policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies), principals (such as users or service accounts) might be blocked from viewing and running Google-provided templates. To resolve this issue, try the guidance in [Access Google-provided templates with principal access boundary policies](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#access-templates-pab).

### Early startup issues

When the template launching process fails in an early stage, regular Flex Template logs might not be available. To investigate startup issues, enable [serial port logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output) for the templates launcher VM.

To enable logging for Java templates, set the `enableLauncherVmSerialPortLogging` option to `true`. To enable logging for Python and Go templates, set the `enable_launcher_vm_serial_port_logging` option to `true`. In the Google Cloud console, the parameter is listed in **Optional parameters** as **Enable Launcher VM Serial Port Logging**.

You can view the serial port output logs of the templates launcher VM in Cloud Logging. To find the logs for a particular launcher VM, use the query `resource.type="gce_instance" "launcher-number"` where number starts with the current date in the format `YYYMMDD`.

[Your organization policy](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#setting_an_organization_policy) might prohibit you from enabling serial port outputs logging.

### Failed to read the job file

When you try to run a job from a Flex Template, your job might fail with the following error:
    
    
    Failed to read the job file : gs://dataflow-staging-REGION-PROJECT_ID/staging/template_launches/TIMESTAMP/job_object...
    

This error occurs when the necessary pipeline initialization options are overwritten. When using Flex Templates, you can configure some but not all pipeline options during pipeline initialization. If the command line arguments required by the Flex Template are overwritten, the job might ignore, override, or discard the pipeline options passed by the template launcher. The job might fail to launch, or a job that doesn't use the Flex Template might launch.

To avoid this issue, during pipeline initialization, don't change the following [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options) in user code or in the `metadata.json` file:

### Java

  * `runner`
  * `project`
  * `jobName`
  * `templateLocation`
  * `region`



### Python

  * `runner`
  * `project`
  * `job_name`
  * `template_location`
  * `region`



### Go

  * `runner`
  * `project`
  * `job_name`
  * `template_location`
  * `region`



### Failed to read the result file

When you try to run a job from a Flex Template, your job might fail with the following error:
    
    
    Failed to read the result file : gs://BUCKET_NAME...
    

This error occurs when the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) doesn't have all the permissions that it needs to run a Flex Template.

For the list of required permissions, see [Permissions to run a Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#permissions_to_run_a_flex_template).

This error can also be caused by:

  * Attempting to run a Flex Template as a non-root user, which generally isn't supported. For more details, see [Running as a non-root user is not supported](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-custom-container#non-root-not-supported), or contact your [account team](https://docs.cloud.google.com/dataflow/docs/support/getting-support).
  * Intermittent network latency or Cloud Storage API issues. For more information, see Intermittent network or Cloud Storage errors.



### Permission denied on resource

When you try to run a job from a Flex Template, your job might fail with the following error:
    
    
    Permission "MISSING_PERMISSION" denied on resource "projects/PROJECT_ID/locations/REGION/repositories/REPOSITORY_NAME" (or it may not exist).
    

This error occurs when the used service account does not have permissions to access necessary resources to run a Flex Template.

To avoid this issue, verify that the service account has the [required permissions](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#permissions_to_run_a_flex_template). Adjust the service account permissions as needed.

### Flag provided but not defined

When you try to run a Go Flex Template with the `worker_machine_type` pipeline option, the pipeline fails with the following error:
    
    
    flag provided but not defined: -machine_type
    

This error is caused by a known issue in the Apache Beam Go SDK versions 2.47.0 and earlier. To resolve this issue, upgrade to Apache Beam Go version 2.48.0 or later.

### Unable to fetch remote job server jar

If you try to run a job from a Flex Template when you're not connected to the internet, your job might fail with the following error:
    
    
    Unable to fetch remote job server jar at
    https://repo.maven.apache.org/maven2/org/apache/beam/beam-sdks-java-io-expansion-service/VERSION/beam-sdks-java-io-expansion-service-VERSION.jar:
    \u003curlopen error [Errno 101] Network is unreachable\u003e
    

This error occurs because the VM is unable to download the Apache Beam Java package from the internet. This package is required when you run a multi-language job by using a Flex Template.

To resolve this issue, make one of the following changes:

  * Connect to the internet. When connected to the internet, your job can access the required file.

  * Include the Apache Beam Java package in your local directory so that your job can access it locally. Put the file in the following directory: `/root/.apache_beam/cache/jars/`. For example, `/root/.apache_beam/cache/jars/beam-sdks-java-io-expansion-service-SDK_VERSION.jar`.




### Unable to get filesystem from specified path

When you try to run a job from a Flex Template, your job might fail with the following error:
    
    
    ValueError: Unable to get filesystem from specified path, please use
    the correct path or ensure the required dependency is installed, e.g., pip
    install apache-beam[gcp]. Path specified: PATH
    

This error occurs when the job uses a Flex Template container image, and the container image doesn't contain a Java installation.

To resolve this issue, add the following line to your Dockerfile:

`sh RUN apt-get update && apt-get install -y openjdk-17-jdk`

This command installs Java in your container environment.

### Launcher VM resource exhaustion

When you try to run a job from a Flex Template, your job might fail with the following error:
    
    
    Failed to start the VM, launcher-ID, used for launching because of status code: INTERNAL, reason: Unknown error in operation 'OPERATION_ID': [ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS] 'The zone 'projects/PROJECT_ID/zones/ZONE_ID' does not have enough resources available to fulfill the request.
    

The VM name `launcher-ID` represents the launcher VM name. The launcher VM is responsible for gathering job resources, such as the template code and image, before building and submitting the job graph to the Dataflow service to start work.

If you don't specify the `launcherMachineType` parameter, Dataflow chooses a default machine type for the launcher VM, typically `e2-standard-2`. This choice is independent of the worker `machineType`. Resource exhaustion errors can happen if this default machine type isn't available in the job's region or zone. To use a specific machine type, set `launcherMachineType`.

To resolve this issue, use one of the following strategies:

  * Update the launcher machine type to a different [machine type](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm) and retry the job. 
    * REST API: Set [`launchParameter.environment.launcherMachineType`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch#flextemplateruntimeenvironment) in the `flexTemplates.launch` method.
    * gcloud CLI: Set the [`--launcher-machine-type`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--launcher-machine-type) flag in the `gcloud dataflow flex-template run` command.
  * If you set the `zone` parameter, remove it so Dataflow can place the launcher VM in a zone with capacity.
  * Launch your Flex Template from a different [region](https://docs.cloud.google.com/dataflow/docs/resources/locations).



## Flex Template launcher delay

When you submit a Flex Template job, the job request goes into a Spanner queue. The template launcher picks up the job from the Spanner queue and then runs the template. When Spanner has a message backlog, a significant delay might occur between the time you submit the job and the time the job launches.

To work around this issue, launch your Flex Template from a different region.

## The template parameters are invalid

When you try to use the gcloud CLI to run a job that uses a [Google-provided template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates), the following error occurs:
    
    
    ERROR: (gcloud.beta.dataflow.flex-template.run) INVALID_ARGUMENT: The template
    parameters are invalid. Details: defaultSdkHarnessLogLevel: Unrecognized
    parameter defaultWorkerLogLevel: Unrecognized parameter
    

This error occurs because some Google-provided templates don't support the `defaultSdkHarnessLog` and `defaultWorkerLog` options.

To resolve this issue, use the appropriate method for your template type.

##### Flex Templates

For Flex Templates, use the `--additional-pipeline-options` flag to pass the pipeline options as a string. For example, using the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command:
    
    
    gcloud dataflow flex-template run JOB_NAME \
    --template-file-gcs-location=GCS_TEMPLATE_PATH \
    --additional-pipeline-options=defaultSdkHarnessLogLevel=WARN,defaultWorkerLogLevel=WARN
    

Replace the following values:

  * `JOB_NAME`: the name of your Dataflow job
  * `GCS_TEMPLATE_PATH`: the Cloud Storage path to the template file



##### Classic templates

For classic templates, the workaround is to copy the template specification file to a Cloud Storage bucket and add the following additional parameters to the file.
    
    
    "metadata": {
        ...
        "parameters": [
          ...,
          {
            "name": "defaultSdkHarnessLogLevel",
            "isOptional": true,
            "paramType": "TEXT"
          },
          {
            "name": "defaultWorkerLogLevel",
            "isOptional": true,
            "paramType": "TEXT"
          }
        ]
      }
    

After you make this change to the template file, use the following flag when you [run the template](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates).
    
    
    --gcs-location=gs://BUCKET_NAME/FILENAME
    

Replace the following values:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `FILENAME`: the name of your template specification file



## Flex Template launcher logs show wrong severity

When a [custom Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates) launch fails, the following message appears in the log files with the severity `ERROR`:
    
    
    ERROR: Error occurred in the launcher container: Template launch failed. See console logs.
    

The root cause of the launch failure usually appears in the logs prior to this message with the severity `INFO`. Although this log level may be incorrect, it is expected, because the Flex template launcher has no way to extract severity details from the log messages produced by the Apache Beam application.

If you want to see the correct severity for every message in the launcher log, configure your template to generate logs in the JSON format instead of in plain text. This configuration allows the template launcher to extract the correct log message severity. Use the following message structure:
    
    
    {
      "message": "The original log message",
      "severity": "DEBUG/INFO/WARN/ERROR"
    }
    

In Java, you can use [Logback logger](https://logback.qos.ch/documentation.html) with a custom JSON [appender](https://logback.qos.ch/manual/appenders.html) implementation. For more information, see the [Logback example configuration](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/f0029e203fbcfd3ea32b1632c70add1d6088ed38/structured-logging/src/main/resources/logback.xml) and the [JSON appender example code](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/ae826040fe19c3d1cb4c80763403dd4f257711db/structured-logging/src/main/java/com/google/cloud/teleport/v2/logging/JsonAppender.java#L28) in GitHub.

This issue only impacts the logs generated by the Flex Template launcher when the pipeline is launching. When the launch succeeds and the pipeline is running, the logs produced by Dataflow workers have the proper severity.

[Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) show the correct severity during job launch, because the Google-provided templates use this JSON logging approach. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
