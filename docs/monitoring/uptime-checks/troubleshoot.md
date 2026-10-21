---
url: https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot/
title: Troubleshoot synthetic monitors and uptime checks \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:56.932020+00:00
---

# Troubleshoot synthetic monitors and uptime checks  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot synthetic monitors and uptime checks Stay organized with collections  Save and categorize content based on your preferences. 

When you encounter issues creating, running, or deleting a synthetic monitor or an uptime check, or when you don't receive expected alert notifications, you can diagnose the cause by inspecting execution logs, metrics, and traces. You can also resolve common configuration errors involving IAM permissions, VPC Service Controls perimeters, and private network targets.

## Find logs

To help you correlate requests with your logs, HTTP and HTTPS requests sent by Cloud Monitoring include a `Check-Id` header that stores the identifier of the associated synthetic monitor or uptime check. To find logs for your synthetic monitors and uptime checks, do the following::

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Do any of the following:

     * To find all logs associated with your synthetic monitors or uptime checks, query by resource type. You can use the **Resource** menu or you can enter a query.

For uptime checks, in the **Resource** menu, select **Uptime Check URL** , or enter the following query into the query editor and then click **Run query** :
           
           resource.type="uptime_url"
           

For synthetic monitors, in the **Resource** menu, select **Cloud Run Revision** , or enter the following query into the query editor and then click **Run query** :
           
           resource.type="cloud_run_revision"
           

     * To find logs that contain information about the response received during a synthetic monitor or uptime check execution, do any of the following:

       * To query by using the ID of the synthetic monitor or uptime check, use the following format when entering the ID into the query editor, and then click **Run query** :
             
             labels.check_id="my-check-id"
             

       * To query for logs that contain response data for requests issued by synthetic monitors and uptime checks, enter the following query into the query editor and then click **Run query** :
             
             "UptimeCheckResult"
             

The previous query matches all log entries that include the string `"UptimeCheckResult"`.

These logs include the following:

       * The ID of the synthetic monitor or uptime check, which is stored in the `labels.check_id` field.

       * For synthetic monitors, the name of your Cloud Run function, which is stored in the `resource.labels.service_name` field.

       * When trace data is collected, the ID of an associated trace, which is stored in the `trace` field.

     * To verify that your service received requests from Google Cloud servers, copy the following query into the query editor and then click **Run query** :
           
           "GoogleStackdriverMonitoring-UptimeChecks"
           

The `protoPayload.ip` field contains one of the addresses used by the uptime-check servers. For information about how to list all IP addresses, see [List IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks).




## Troubleshoot notifications

This section describes some errors you might encounter when configuring alerting policies and provides information for resolving them.

### One checker failed but others didn't

You are reviewing your uptime-check metrics and notice that one checker reported a failure when all other checkers reported success.

There is no action required to resolve this situation.

When only one checker reports a failure, that failure might be the result of the checker's command timing out due to a network issue. That is, instead of the command failing, the command doesn't complete within the specified timeout.

Alerting policies that use the default configuration require failures from at least two checkers before they create an alert and send a notification. A failure reported by a single checker doesn't result in a notification.

### You received a notification and want to debug the failure

  1. To identify when the failure began, do one of the following:

     * For uptime checks, to determine when the failure occurred, view the **Uptime details** page:

       1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

       2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
       3. Find and select the uptime check.

The **Passed checks** chart displays the history of the checks. To identify when the uptime check first failed, you might need to modify the time range for the chart. The time-range selector is located in the toolbar of the **Uptime details** page.

     * For synthetic monitors, to determine when the failure occurred, view the **Uptime details** page:

       1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

       2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
       3. Find and select the synthetic monitor.
  2. For information about how to find associated log data, see Find logs.




### You aren't notified that an uptime check failed

You configured an uptime check and are viewing the **Uptime details** page for that check. You notice that the **Passed checks** graph shows that at least one checker failed. However, you didn't receive a notification.

By default, the alerting policy is configured to create an alert and send a notification when checkers in at least two regions fail to receive a response to an uptime check. These failures must occur simultaneously.

You can edit the condition of the alerting policy so that you are notified when a single region fails to receive a response. However, we encourage you to use the default configuration, which reduces the number of notifications that you might receive due to transient failures.

To view or edit an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Click **See all policies** in the **Policies** pane.
  4. Find the policy that you want to view or edit, and then click the name of the policy.

You can view and edit the policy from the **Policy details** page.




## Troubleshoot public uptime checks

This section describes some errors you might encounter when using public uptime checks and provides information for resolving them.

### Your public uptime checks are failing

You configure a public uptime check, but you receive an error when you perform the verification step.

The following are some possible causes of an uptime check failure:

  * **Connection Error - Refused** : If you are using the default **HTTP** connection type, check that you have a web server installed that is responding to HTTP requests. A connection error can happen on a new instance if you haven't installed a web server; see the [Quickstart for Compute Engine](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine). If you use an **HTTPS** connection type, you might have to perform additional configuration steps. For firewall issues, see [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks).
  * **Name or service not found** : The hostname might be incorrect.
  * **403 Forbidden** : The service is returning an error code to the uptime checker. For example, the default Apache web server configuration returns this code under Amazon Linux, but it returns code **200 (Success)** under some other Linux versions. See the [LAMP tutorial for Amazon Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html) or your web server's documentation.
  * **404 Not found** : The path might be incorrect.
  * **408 Request timeout** , or no response: The port number might be incorrect, the service might not be running, the service might be inaccessible, or the timeout might be too low. Check that your firewall allows traffic from the uptime servers; see [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks). The timeout limit is specified as part of the **Response Validation** options.



To help you troubleshoot failed public uptime checks, you can configure your uptime checks to send up to 3 ICMP pings during the check. The pings can help you distinguish between failures caused, for example, by network connectivity problems and by timeouts in your application. For more information, see [Use ICMP pings](https://docs.cloud.google.com/monitoring/uptime-checks#ping).

### You can't create a public uptime check

You try to create a public uptime check, but the action fails with a message similar to the following:
    
    
    Public uptime checks cannot be configured in a VPC Service Controls perimeter.
    

This error message indicates that your Google Cloud project is in an enabled VPC Service Controls perimeter. You can't create public uptime checks for those configurations.

To resolve this situation, create a [private uptime check](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

## Troubleshoot private uptime checks

This section describes some errors you might encounter when using private uptime checks and provides information for resolving them.

### Creation of uptime check fails

Your Google Cloud project settings might prevent modification of the roles assigned to the service account that uptime checks use to manage interactions with the Service Directory service. In this situation, the creation of the uptime check fails.

This section describes how you can grant the roles that the service account requires:

###  Console 

When you use the Google Cloud console to create the private uptime check, the Google Cloud console issues the commands to grant the Service Directory roles to the service account.

For information about how to grant roles to a service account, see [Authorize the service account](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks#authz_svcacct).

###  gcloud: Scoping project 

The first time you create a private uptime check for a Service Directory service and private resources in a single Google Cloud project, the request might succeed or fail. The result depends on whether you have disabled [automatic role grants for service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) in your project:

  * The first uptime-check creation succeeds if your project permits automatic role grants for service accounts. A service account is created for you and is granted the necessary roles.

  * The first uptime-check creation fails if your project doesn't permit automatic role grants for service accounts. A service account is created, but no roles are granted.




If the creation of the uptime check fails, then do the following:

  1. [Authorize the service account](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks#authz_svcacct).
  2. Wait a few minutes for the permissions to propagate.
  3. Try creating the private uptime check again.



###  gcloud: Monitored project 

The first time you create a private uptime check that targets a Service Directory service in a monitored project or private resources in a different Google Cloud project, the request fails and results in the creation of a Monitoring service account.

How you authorize the service account depends on the number of Google Cloud projects you are using and their relationships. You might have up to four projects involved:

  * The project in which you defined the private uptime check.
  * The monitored project in which you configured the Service Directory service.
  * The project in which you configured the VPC network.
  * The project in which network resources like VMs or load balancers are configured. This project has no role in the service-account authorization discussed here.



When the creation of the first uptime check fails, do the following:

  1. [Authorize the service account](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks#authz_svcacct).
  2. Wait a few minutes for the permissions to propagate.
  3. Try creating the private uptime check again.



### Can't target a Cloud Run service

You want to target a Cloud Run service with a private uptime check, but a Cloud Run service doesn't have an IPv4 address in a customer VPC network that you can register as a Service Directory endpoint.

To target a Cloud Run service with a private uptime check, configure an internal Application Load Balancer with a serverless NEG backend, and register the load balancer's internal IP address in Service Directory. For an example of how to set up the load balancer, see [Set up a regional internal Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless).

### Access denied

Your uptime checks are failing with `VPC_ACCESS_DENIED` results. This result means that some aspect of your network configuration or service-account authorization isn't correct.

Check your service-account authorization for using a scoping project or a monitored project as described in Creation of uptime check fails.

For more information about accessing private networks, see [Configure the network project](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access#configure-the-network-project).

### Anomalous results from private uptime checks

You have a Service Directory service with multiple VMs, and your service configuration contains multiple endpoints. When you shut down one of the VMs, your uptime check still indicates success.

When your service configuration contains multiple endpoints, one is chosen at random. If the VM associated with the chosen endpoint is running, the uptime check succeeds even though one of the VMs is down.

### Default headers

Your uptime checks are returning errors or unexpected results. This might occur if you have overridden default header values.

When a request is sent for a private uptime check to a target endpoint, the request includes the following headers and values:

Header | Value  
---|---  
`HTTP_USER_AGENT` | `GoogleStackdriverMonitoring-UptimeChecks(https://cloud.google.com/monitoring)`  
`HTTP_CONNECTION` | `keep-alive`  
`HTTP_HOST` | IP of Service Directory endpoint  
`HTTP_ACCEPT_ENCODING` | `gzip`, `deflate`, `br`  
`CONTENT_LENGTH` | Calculated from uptime `POST` data  
  
If you attempt to override these values, the following might happen:

  * The uptime check reports errors.
  * The override values are dropped and replaced with the values in the table.



### No data visible

You don't see any data on the uptime check dashboard when your uptime check is in a different Google Cloud project than the Service Directory service.

Ensure that the Google Cloud project that contains the uptime check monitors the Google Cloud project that contains the Service Directory service.

For more information about how to list monitored projects and add additional ones, see [Configure a metrics scope for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

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

### Unable to edit the configuration of a broken-link checker

You created a broken-link checker by using the Google Cloud console, and you want to change the HTML elements that are tested, or you want to modify the URI timeout, retries, wait for selector, and per-link options. However, when you edit the broken-link checker, the Google Cloud console doesn't display the configuration fields.

To resolve this failure, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate the synthetic monitor that you want to edit, click _more_vert_ **More options** , and then select **Edit**.
  4. Click **Edit function**.
  5. Edit the `options` object in the `index.js` file, and then click **Apply function**.

For information about the fields and syntax for this object, see [`broken-links-ok/index.js`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/blob/main/samples/broken-links-ok/index.js).

  6. Click **Save**.




### Google Cloud console reports that saving screenshots failed

**Note:** A synthetic monitor that can't save screenshots continues to test the links contained in a URI.

You created a broken-link checker and configured it to save screenshots. However, the Google Cloud console is displaying one of the following warning messages along with more detailed information:

  * `InvalidStorageLocation`
  * `StorageValidationError`
  * `BucketCreationError`
  * `ScreenshotFileUploadError`



To resolve these failures, try the following:

  * If you see the `InvalidStorageLocation` message, then verify the existence of the Cloud Storage bucket specified in the field named `options.screenshot_options.storage_location`.

  * View the logs related to your Cloud Run function. For more information, see [Finding logs](https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot#trouble-find-logs).

  * Verify that the service account being used in the corresponding Cloud Run function has an Identity and Access Management role that lets it create, access, and write to Cloud Storage buckets.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
