---
url: https://docs.cloud.google.com/monitoring/synthetic-monitors/create/
title: Create a synthetic monitor \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:39.694996+00:00
---

# Create a synthetic monitor  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/synthetic-monitors/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create a synthetic monitor Stay organized with collections  Save and categorize content based on your preferences. 

Synthetic monitors let you periodically test the availability, consistency, and performance of your services, applications, web pages, and APIs. Each synthetic monitor invokes a Node.js test script that you deploy as a Cloud Run function, and records the execution status and latency. You can then configure an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) to notify you when a test fails.

## About synthetic monitors

A synthetic monitor periodically executes a single-purpose [2nd gen Cloud Run function](https://docs.cloud.google.com/functions/docs/concepts/overview) that is deployed on [Cloud Run](https://docs.cloud.google.com/run). When you create the synthetic monitor, you define the Cloud Run function, which must be written in Node.js, and the execution frequency. For example, you can configure your Cloud Run function to interact with a web page by using [Puppeteer](https://pptr.dev/). You can also configure your Cloud Run function to interact with an API by using the [Axios](https://axios-http.com/docs/intro) module. You might also want to [test resources that are within a VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).

To create your Cloud Run function, you can use an inline editor or you can upload a zip file. If you choose to use the inline editor, then you can start with a provided skeleton. After you create a synthetic monitor, Cloud Monitoring uses a scheduling system that schedules periodic execution of your Cloud Run function. While you specify the region where your Cloud Run function exists, the commands that trigger the execution can originate in any region supported by the uptime-check servers. For more information, see [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks).

You can create an alerting policy so that you're notified when there are test failures:

  * When you create a synthetic monitor by using the Google Cloud console, the default behavior is to create an alerting policy. You supply the notification channels. The default alerting policy is configured to notify you when there are two or more consecutive test failures.

  * When you create a synthetic monitor by using the Cloud Monitoring API, you must create the alerting policy to monitor the [`uptime_check/check_passed`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed) metric type for the Cloud Run resource that the Cloud Run function is running on.




### Execution frequency considerations

You configure how often your Cloud Run function is executed. To determine the frequency of executions, consider the [service level objective (SLO)](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring) for your service. To catch potential SLO violations, you need to execute the tests frequently. However, the SLO for your service isn't the only consideration. You also need to consider how the rate of executions translates into load on your service and into your costs. Each execution provides load on your service, so the more frequently you execute your Cloud Run function, the more load you apply to your service. For reference, the default execution interval for uptime checks is one minute.

The execution frequency also determines how quickly you can be notified when your test fails. Monitoring opens an alert and sends a notification after the second consecutive failure of a test. For example, if your execution frequency is 5 minutes, then it can take 10 minutes before there are two failed tests. You're notified after the second test failure.

### Cloud Run function sample code

For templates and samples, see [Samples for synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/samples). You can use these samples as a starting point for your Cloud Run function. If you are an experienced developer, then consider [using Gemini to generate code for synthetic monitors](https://console.cloud.google.com/monitoring/synthetic-monitoring?walkthrough_id=monitoring--gemini--monitoring-synthetic-monitor-prompt) and thus reduce your development time. Using Gemini to generate code is in Public Preview.

The [generic template](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-synthetic-nodejs), which you can select when you create a synthetic monitor by using the Google Cloud console, is configured to collect trace and log data for outbound HTTP requests. The solution leverages the OpenTelemetry [auto-instrumentation-node](https://www.npmjs.com/package/@opentelemetry/auto-instrumentations-node) module and the [winston logger](https://www.npmjs.com/package/winston). Due to the dependency on open source products, you should expect changes in the structure of trace and log data. Therefore, the collected trace and log data should be used only for debugging purposes.

You can implement your own approach to collect trace and log data for outbound HTTP requests. For an example of a custom approach, see the class [`SyntheticAutoInstrumentation`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/blob/main/packages/synthetics-sdk-api/src/auto_instrumentation.ts#L82).

### Cloud Run function configuration

When you configure your Cloud Run function, you must either specify the runtime, build, connections, and security settings, or accept the default settings:

  * The default value for the allocated memory might not be sufficient. We recommend that you set this field to be at least 2 GiB.

  * The default value for the inbound data transfer settings of your Cloud Run function is to allow all traffic. You can use this setting or a more restrictive setting.

When you allow all traffic, the first phase of validation performed by Cloud Run functions, which is done at the network level, always passes. The second phase of validation determines whether the caller has been granted permission to execute the Cloud Run function. Authorization is dependent upon the caller's Identity and Access Management (IAM) role. By default, Cloud Monitoring is granted permission to execute your Cloud Run function. For information about how to view or modify the inbound data transfer settings, see [Ingress settings](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#ingress_settings).




### Cloud Run function restrictions

  * The name of your Cloud Run function must not contain an underscore.

  * You can collect trace and log data for outbound HTTP requests only when you use the generic template.

  * Only HTTP functions are supported. If you use the Google Cloud console to create your synthetic monitor, then you're provided a default function that queries a URL. The source for the default function, which can be modified, is available in the [`generic-synthetic-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-synthetic-nodejs) Git repository.

For information about HTTP functions, see [Write HTTP functions](https://docs.cloud.google.com/run/docs/write-functions#write-http-functions).

  * If you use the API, then the deployment command must specify that the Cloud Run function is 2nd generation. If you use the Google Cloud console, then deployment is handled for you. For more information, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy).

  * The runtime environment is restricted to [Node.js](https://nodejs.org/). For a list of supported versions, see [Runtime support](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js).




### Data collected by synthetic monitors

This section describes the data that is collected for your synthetic monitor. For information about how to view execution results, see [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore).

#### Execution history

For each synthetic monitor, a history of execution results is collected. This data includes the following:

  * A time series that records success or failure of executions over time.

  * A time series that records the execution duration of the code. The execution time of the function isn't recorded. The latency data is written as an [`uptime_check/request_latency`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/request_latency) time series for the Cloud Run resource that the Cloud Run function is running on. A chart of this data is provided on the **Synthetic monitor details** page.

  * Logs that contain information about synthetic monitor executions, such as information about the test and failure details. The available logs depend on your Cloud Run function. For example, if you use the [Mocha](https://mochajs.org/) template, then the logs include information about whether the test passed or failed and test duration. The stack trace, when included, lists the line of code that failed, the error types, and the error messages.

  * Optionally, traces and logs for outbound HTTP requests. For information about how to collect this data, see Request latency.




#### Cloud Run function metrics and logs

Monitoring and Logging also collect metrics and logs for your Cloud Run function. This data, which is collected by Cloud Run functions, includes information on the number of executions per second, execution time, and memory utilization of your function.

#### Request latency

Latency data for the HTTP request made by the synthetic monitor is automatically collected and stored by Cloud Trace.

To collect trace, log, and latency data for the outbound HTTP requests made by your synthetic monitor, you must use the [generic template](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-synthetic-nodejs). For more information, see [Samples for synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/samples).

## Before you begin

Configure your project and your IAM roles, and select the interface that you plan to use. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

### Configure your project and roles

  1. To get the permissions that you need to view and modify synthetic monitors by using the Google Cloud console, ask your administrator to grant you the following IAM roles on your project: 

     * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)
     * [Cloud Functions Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Enable the Cloud Monitoring API, Artifact Registry API, Cloud Build API, Cloud Functions API, Cloud Logging API, Pub/Sub API, and Cloud Run Admin API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,cloudfunctions.googleapis.com,logging.googleapis.com,pubsub.googleapis.com,run.googleapis.com)

  3. Verify that your Google Cloud project contains the default Compute Engine service account. This service account is created when you enable the Compute Engine API and has a name similar to `12345-compute@developer.gserviceaccount.com`.

In the Google Cloud console, go to the **Service Accounts** page: 

[Go to **Service Accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

If the default Compute Engine service account doesn't exist, then click **Create service account** and complete the dialog.

  4. Ensure that the default Compute Engine service account, or the service account that you created, has been granted the role of Editor (`roles/editor`).

To view the roles granted to your service account, do the following:

     1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. Select **Include Google-provided role grants**.
     3. If the service account used by your synthetic monitor isn't listed, or if it hasn't been granted a role that includes the permissions in the role of Cloud Trace Agent (`roles/cloudtrace.agent`), then grant this role to your service account.
  5. Configure the notification channels that you want to use to receive notifications. We recommend that you create multiple types of notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options) and [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api). 



### Select the interface you plan to use

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## Create a synthetic monitor

**Warning:** Don't configure a synthetic monitor to test `https://www.google.com`. If you use the example code, then ensure that you modify the `url` field before you deploy the sample code.

###  Console 

When you create a synthetic monitor by using the Google Cloud console, a new Cloud Run function (2nd gen) is deployed and the monitor for that Cloud Run function is created. You can't create a synthetic monitor that monitors an existing Cloud Run function.

  1. Ensure that you've enabled the required APIs, that your project contains a default Compute Engine service account, and that this account has been granted the role of Editor (`roles/editor`). For more information, see Before you begin.

  2. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  4. Select **Create Synthetic Monitor**.
  5. Select the template for your Cloud Run function:

     * **Custom synthetic monitor** : Use this template when you want to collect log data or trace data for outbound HTTP requests.

     * **Mocha synthetic monitor** : Use this template when you write Mocha test suites.

     * **Broken link checker** : Use this template to test a URI and a configurable number of links found at that URI. For information about the fields for this checker, see [Create a broken-link checker](https://docs.cloud.google.com/monitoring/synthetic-monitors/broken-links).

  6. Enter a name for the monitor.

  7. Optional: Update the **Response Timeout** and the **Check Frequency** , and add user-defined labels.

  8. Do one of the following:

     * If you have [access to Gemini Code Assist in this project](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini) and want help writing your code, then click **Help me code**. This feature is in Public Preview. For guidance on prompts, see [Learn about writing prompts for synthetic monitors](https://console.cloud.google.com/monitoring/synthetic-monitoring?walkthrough_id=monitoring--gemini--monitoring-synthetic-monitor-prompt).

After you are satisfied with the code, click **Insert into Cloud Function**.

     * Click **Create Function**.

  9. In the Cloud Run function dialog, do the following:

     1. Enter a display name and select a region. Names must be unique within a region.

**Note:** Don't include an underscore in the name of your Cloud Run function.

     2. In the **Runtime, build, connections and security settings** section, do the following:

        * Review the default settings and update them when necessary.
**Note:** The default settings for the allocated memory, CPU, and security might not be sufficient. We recommend that you set the memory to at least 2 GiB.
        * In the **Runtime service account** field, select a service account.
     3. Edit generated code, or write or upload code for your Cloud Run function:

        * To edit generated code, enter your own code, or load the default sample function, select **Inline Editor**. The sample function, which is dependent upon the template that you selected previously, sends a request to a specific URL. You can modify the default function.

        * To load a zip file from your local system, select **ZIP upload**.

If you upload a zip file from your local system, then you must also specify a Cloud Storage bucket for the zip file. If you don't have an appropriate Cloud Storage bucket, then create one.

**Note:** When you create a new storage bucket, the bucket is immediately opened, the message `No objects found` is displayed, and the options are **Select** or **Cancel**. Click **Cancel** to return to the **Create function** dialog. Next, for the destination bucket, select **Browse** , and then select your Cloud Storage bucket.
        * To load a zip file from your Cloud Storage, select **ZIP from Cloud Storage** , select the storage bucket, and then select the zip file to load.

You can also create a Cloud Run function by using the Cloud Run functions pages in the Google Cloud console. To create a synthetic monitor that monitors a copy of that Cloud Run function, go to the **Source** tab and click **Download zip**. You can then upload the zip file.

     4. Click **Apply function**.

  10. Configure the [alerting policy](https://docs.cloud.google.com/monitoring/alerts):

     1. Optional: Update the alerting policy name and the duration of failure before notifications are sent.

     2. Add the notification channels.

  11. Click **Create**.

The Cloud Run function that you defined is built and deployed as 2nd gen, and the synthetic monitor is created.




###  gcloud 

When you create a synthetic monitor by using the Google Cloud CLI or the Cloud Monitoring API, you pass the function name to the API call. Therefore, you can only create a synthetic monitor that monitors an existing Cloud Run function.

  1. Ensure that you've enabled the required APIs, that your project contains a default Compute Engine service account, and that this account has been granted the role of Editor (`roles/editor`). For more information, see Before you begin.

  2. Configure the Google Cloud CLI to set a default project by using the [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command: 
         
         gcloud config set project PROJECT_ID
         

Before you run the previous command, replace the following:

     * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  3. Write and deploy your 2nd gen Cloud Run function. 

For example, to deploy the `synthetics-sdk-nodejs` sample in the [`Google Cloud/synthetics-sdk-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs) repository, do the following:

     1. Clone the repository and go to the location of the source code:
            
            git clone https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs.git
            cd synthetics-sdk-nodejs/samples/generic-synthetic-nodejs
            

     2. Deploy the Cloud Run function by using the [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) command:
            
            gcloud functions deploy FUNCTION_NAME \
            --gen2 --region="us-west2" --source="." \
            --entry-point=SyntheticFunction --trigger-http --runtime=nodejs18
            

In the `gcloud functions deploy` command, do the following:

        * Ensure that the value of the FUNCTION_NAME field is unique within its deployment region.

**Note:** Don't include an underscore in the name of your Cloud Run function.

        * Include the `--gen2` flag and set the deployment region.

        * Set the `--entry-point` field as follows:

          * Mocha: `SyntheticMochaSuite`
          * Not Mocha: `SyntheticFunction`
        * Set the `--runtime` field to `nodejs18`.

        * Include the `--trigger-http` flag.

        * Set the `--ingress-settings` field when you don't want to use the default setting, which allows all traffic.

Cloud Run functions builds and then deploys your Cloud Run function. The results of the Google Cloud CLI command include information about the function, including its fully qualified name:
    
    name: projects/PROJECT_ID/locations/REGION/functions/FUNCTION_NAME
    

For more information about deploying a function, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy).

To list the Cloud Run functions in your Google Cloud project, use the [`gcloud functions list`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/list) command:
    
    gcloud functions list
    

The response to this call is a list of entries, where each entry lists a Cloud Run function:
    
    NAME: function-1
    STATE: ACTIVE
    TRIGGER: HTTP Trigger
    REGION: us-west2
    ENVIRONMENT: 2nd gen
    

To find the fully qualified name for a specific Cloud Run function, run the [`gcloud monitoring uptime describe`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/describe) command. 

  4. To create the synthetic monitor, run the [`gcloud monitoring uptime create`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create) command:
         
         gcloud monitoring uptime create DISPLAY_NAME --synthetic-target=TARGET
         

Before you run the previous command, replace the following:

     * DISPLAY_NAME: The name for your synthetic monitor.
     * TARGET: The fully qualified name of your Cloud Run function.
  5. Create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts).

Due to the complexity of the alerting policy configuration, we recommend that you go to the **Synthetic monitors** page in the Google Cloud console, and use the options to create an alerting policy. With this approach, most alerting policy fields are populated for you. To create the alerting policy by using the Google Cloud console, click **Create policy** from the **Synthetic monitors** page.

If you plan to use the Google Cloud CLI or the Cloud Monitoring API, then configure the filter of the condition as follows:
         
         "filter": "resource.type = \"cloud_run_revision\" AND
                     metric.type = \"monitoring.googleapis.com/uptime_check/check_passed\" AND
                     metric.labels.check_id = \"CHECK_ID\"",
         

The condition monitors [`uptime_check/check_passed`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed) time series that are written by your synthetic monitor. Be sure to replace CHECK_ID with the identifier of the synthetic monitor, which is included in the response data of a create command.

For information about how to create an alerting policy, see [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api).




###  Terraform 

For information about how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands) and [Terraform reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

To create a synthetic monitor and an alerting policy to monitor that check, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) for you project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  2. Ensure that you've enabled the required APIs, that your project contains a default Compute Engine service account, and that this account has been granted the role of Editor (`roles/editor`). For more information, see Before you begin.

  3. Edit your Terraform configuration file and add a [`google_storage_bucket`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket) resource, and then apply your changes.

The following code defines a Cloud Storage bucket in the `US` location:
         
         resource "google_storage_bucket" "gcf_source" {
            name = "gcf-v2-source-9948673986912-us"
            location = "US"
            uniform_bucket_level_access = true
         }
         

  4. Edit your Terraform configuration file and add a [`google_storage_bucket_object`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object) resource, and then apply your changes.

The resource specifies the name of the object in your bucket, and the location of the zip file on your local system. For example, when you apply the following code, a file with the name `example-function.zip` is added to your storage bucket:
         
         resource "google_storage_bucket_object" "object" {
            name = "example-function.zip"
            bucket = google_storage_bucket.gcf_source.name
            source = "generic-synthetic-node.js.zip"
         }
         

  5. Edit your Terraform configuration file and add a [`google_cloudfunctions2_function`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function) resource, and then apply your changes.

**Note:** Don't include an underscore in the name of your Cloud Run function.

Ensure that your `google_cloudfunctions2_function` resource specifies a Node.js runtime and the entry point used by synthetic monitors. For example, when you apply the following code, a function with the name `sm-central1` is deployed:
         
         resource "google_cloudfunctions2_function" "central1" {
            name = "sm-central1"
            location = "us-central1"
         
            build_config {
               runtime = "nodejs20"
               entry_point = "SyntheticFunction"
               source {
                     storage_source {
                        bucket = google_storage_bucket.gcf_source.name
                        object = google_storage_bucket_object.object.name
                     }
               }
            }
         
            service_config {
               max_instance_count = 1
               available_memory = "256Mi"
               timeout_seconds  = 60
            }
         }
         

  6. To create a synthetic monitor, edit your Terraform configuration file and add a [`google_monitoring_uptime_check_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_uptime_check_config) resource, and then apply your changes.

For this resource, specify the `synthetic_monitor` block:
         
         resource "google_monitoring_uptime_check_config" "synthetic" {
            display_name = "sm-central1"
            timeout = "30s"
         
            synthetic_monitor {
               cloud_function_v2 {
                     name = google_cloudfunctions2_function.central1.id
               }
            }
         }
         

  7. Optional: Create a notification channel and an alerting policy.

The following steps use the Google Cloud console to create the notification channel and alerting policy. This approach ensures that the alerting policy only monitors the data generated by your synthetic monitor.

     1. To create a notification channel, do the following:

        1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

        2. Select **Manage notification channels**.
        3. Go to the type of channel that you want to add, click **Add** , and then complete the dialog.
     2. To create an alerting policy, do the following:

        1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

        2. Locate your synthetic monitor, select _more_vert_ **More** , and then select **Add alert policy**.
        3. In the dialog, go to the **Notifications and name** section, expand **Notification Channels** , and make your selections.
        4. Name the alerting policy and then click **Create policy**.



###  REST 

When you create a synthetic monitor by using the Google Cloud CLI or the Cloud Monitoring API, you pass the function name to the API call. Therefore, you can only create a synthetic monitor that monitors an existing Cloud Run function.

  1. Ensure that you've enabled the required APIs, that your project contains a default Compute Engine service account, and that this account has been granted the role of Editor (`roles/editor`). For more information, see Before you begin.

  2. Configure the Google Cloud CLI to set a default project by using the [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command: 
         
         gcloud config set project PROJECT_ID
         

Before you run the previous command, replace the following:

     * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  3. Write and deploy your 2nd gen Cloud Run function. 

For example, to deploy the `synthetics-sdk-nodejs` sample in the [`Google Cloud/synthetics-sdk-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs) repository, do the following:

     1. Clone the repository and go to the location of the source code:
            
            git clone https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs.git
            cd synthetics-sdk-nodejs/samples/generic-synthetic-nodejs
            

     2. Deploy the Cloud Run function by using the [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) command:
            
            gcloud functions deploy FUNCTION_NAME \
            --gen2 --region="us-west2" --source="." \
            --entry-point=SyntheticFunction --trigger-http --runtime=nodejs18
            

In the `gcloud functions deploy` command, do the following:

        * Ensure that the value of the FUNCTION_NAME field is unique within its deployment region.

**Note:** Don't include an underscore in the name of your Cloud Run function.

        * Include the `--gen2` flag and set the deployment region.

        * Set the `--entry-point` field as follows:

          * Mocha: `SyntheticMochaSuite`
          * Not Mocha: `SyntheticFunction`
        * Set the `--runtime` field to `nodejs18`.

        * Include the `--trigger-http` flag.

        * Set the `--ingress-settings` field when you don't want to use the default setting, which allows all traffic.

Cloud Run functions builds and then deploys your Cloud Run function. The results of the Google Cloud CLI command include information about the function, including its fully qualified name:
    
    name: projects/PROJECT_ID/locations/REGION/functions/FUNCTION_NAME
    

For more information about deploying a function, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy).

To list the Cloud Run functions in your Google Cloud project, use the [`gcloud functions list`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/list) command:
    
    gcloud functions list
    

The response to this call is a list of entries, where each entry lists a Cloud Run function:
    
    NAME: function-1
    STATE: ACTIVE
    TRIGGER: HTTP Trigger
    REGION: us-west2
    ENVIRONMENT: 2nd gen
    

To find the fully qualified name for a specific Cloud Run function, run the [`gcloud monitoring uptime describe`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/describe) command. 

  4. To create a synthetic monitor, do the following:

     1. Click [`projects.uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) to open the API reference page for the method.
     2. Click **Try it** to open APIs Explorer.
     3. Set the following fields and then run the command.

        * Parent field: The project in which to create the synthetic monitor. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. This field has the following format:
    
    projects/PROJECT_ID
    

        * In the request body, specify the following:

        * `displayName`: Set to the display name for your synthetic monitor.

        * `syntheticMonitor`: Set to the fully qualified name of your Cloud Run function.

On success, the response of the API call is similar to the following:
    
    {
    "name": "projects/myproject/uptimeCheckConfigs/17272586127463315332",
    "displayName": "MyMonitor",
    ...
    "syntheticMonitor": {
    "cloudFunctionV2": {
       "name": "projects/myproject/locations/us-west2/functions/function-1",
       "cloudRunRevision": {
       "type": "cloud_run_revision",
       "labels": {
          "project_id": "myproject",
          "configuration_name": "",
          "location": "us-west2",
          "revision_name": "",
          "service_name": "function-1"
       }
       }
    }
    }
    }
    

  5. Create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts).

Due to the complexity of the alerting policy configuration, we recommend that you go to the **Synthetic monitors** page in the Google Cloud console, and use the options to create an alerting policy. With this approach, most alerting policy fields are populated for you. To create the alerting policy by using the Google Cloud console, click **Create policy** from the **Synthetic monitors** page.

If you plan to use the Google Cloud CLI or the Cloud Monitoring API, then configure the filter of the condition as follows:
         
         "filter": "resource.type = \"cloud_run_revision\" AND
                     metric.type = \"monitoring.googleapis.com/uptime_check/check_passed\" AND
                     metric.labels.check_id = \"CHECK_ID\"",
         

The condition monitors [`uptime_check/check_passed`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed) time series that are written by your synthetic monitor. Be sure to replace CHECK_ID with the identifier of the synthetic monitor, which is included in the response data of a create command.

For information about how to create an alerting policy, see [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api).




## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Troubleshoot synthetic monitors

This section provides information that you can use to help you troubleshoot your synthetic monitors.

### Error message after enabling the APIs

You open the create flow for a synthetic monitor and are prompted to enable at least one API. After you enable the APIs, a message similar to the following is displayed:
    
    
    An error occurred during fetching available regions: Cloud Functions API has
    not been used in project PROJECT_ID before or it is disabled.
    

The error message recommends that you verify that the API is enabled and then advises that you wait and retry the action.

To verify that the API is enabled, go to the **APIs & Services** page for your project:

[Go to APIs & Services](https://console.cloud.google.com/projectselector/apis)

After you've verified that the API is enabled, you can continue with the create flow. The condition resolves automatically after the API enablement propagates through the backend.

### Outbound HTTP requests aren't being traced

You configure your synthetic monitor to collect trace data for outbound HTTP requests. Your trace data only shows one span, similar to the following screenshot:

![Cloud Trace displaying only one trace.](https://docs.cloud.google.com/static/monitoring/images/syn-mon-bad-svc-acct.png)

To resolve this situation, ensure that your service account has been granted the role of Cloud Trace Agent (`roles/cloudtrace.agent`). A role of Editor (`roles/editor`) is also sufficient.

To view the roles granted to your service account, do the following:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select **Include Google-provided role grants**.
  4. If the service account used by your synthetic monitor isn't listed, or if it hasn't been granted a role that includes the permissions in the role of Cloud Trace Agent (`roles/cloudtrace.agent`), then grant this role to your service account.

If you don't know the name of your service account, then in the navigation menu, select **Service Accounts**.




### In progress status

The **Synthetic monitors** page lists a synthetic monitor with a status of `In progress`. A status of `In progress` means that the synthetic monitor was recently created and there isn't any data to display, or that the function failed to deploy.

To determine if the function failed to deploy, try the following:

  * Ensure that the name of your Cloud Run function doesn't contain an underscore. If an underscore is present, remove the underscore and redeploy the Cloud Run function.

  * Open the **Synthetic monitor details** page for the synthetic monitor.

If you see the following message, then delete the synthetic monitor.
        
        Cloud Function not found for this Synthetic monitor. Please confirm it exists or delete this monitor.
        

The error message indicates that the function was deleted and therefore the synthetic monitor is unable to execute the function.

  * Open the Cloud Run functions page for the function. To open this page from the **Synthetic monitor details** page, click **Code** , and then click the function name.

If you see a message similar to the following, then the function failed to deploy.
        
        This function has failed to deploy and will not work correctly. Please edit and redeploy
        

To resolve this failure, review the function code and correct the errors that are preventing the function from building or deploying.




When you create a synthetic monitor, it might take several minutes for the function to be deployed and executed.

### Warning status

The **Synthetic monitors** page lists a synthetic monitor with a status of `Warning`. A status of `Warning` means that the execution results are inconsistent. This might indicate a design issue with your test, or it might indicate that what is being tested has inconsistent behavior.

### Failing status

The **Synthetic monitors** page lists a synthetic monitor with a status of `Failing`. To get more information about the failure reason, view the most recent execution history.

  * If the error message `Request failed with status code 429` is shown, then the target of the HTTP request rejected the command. To resolve this failure, you must change the target of your synthetic monitor.

The endpoint `https://www.google.com` rejects requests made by synthetic monitors.

  * If the failure is returning an execution time of `0ms`, then the Cloud Run function might be running out of memory. To resolve this failure, edit your Cloud Run function, and then increase the memory to at least 2 GiB and set the CPU field to `1`.




### Delete fails for a synthetic monitor

You use the Cloud Monitoring API to delete a synthetic monitor, but the API call fails with a response similar to the following:
    
    
    {
      "error": {
        "code": 400,
        "message": "Request contains an invalid argument.",
        "status": "INVALID_ARGUMENT",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.DebugInfo",
            "detail": "[ORIGINAL ERROR] generic::invalid_argument: Cannot delete check 1228258045726183344. One or more alerting policies is using it.Delete the alerting policy with id projects/myproject/alertPolicies/16594654141392976482 and any other policies using this uptime check and try again."
          }
        ]
      }
    }
    

To resolve the failure, delete alerting policies that monitor the results of the synthetic monitor, and then delete the synthetic monitor.

## What's next

  * [Samples for synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/samples)
  * [Manage synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/manage)
  * [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
