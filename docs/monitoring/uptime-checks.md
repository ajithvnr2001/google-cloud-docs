---
url: https://docs.cloud.google.com/monitoring/uptime-checks/
title: Create public uptime checks \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:13.555816+00:00
---

# Create public uptime checks  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/uptime-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create public uptime checks Stay organized with collections  Save and categorize content based on your preferences. 

Public uptime checks let you test the availability of publicly accessible URLs and Google Cloud resources by sending periodic HTTP, HTTPS, or TCP requests from multiple locations around the world. When you create an uptime check, you can also configure an alerting policy to notify you if the target fails to respond. To test resources on a private network instead, see [Create private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

## About uptime checks

Public uptime checks can determine the availability of the following monitored resources: 

  * [Uptime check URL](https://docs.cloud.google.com/monitoring/api/resources#tag_uptime_url)
  * [VM instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)
  * [App Engine application](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)
  * [Kubernetes service](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_service)
  * [Amazon Elastic Compute Cloud (EC2) instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)
  * [Cloud Run Revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)



For HTTP and HTTPS, all URL redirects are followed and the final response received by the uptime check is used to evaluate any success criteria. For HTTPS checks, the SSL certificate expiry time is computed based on the server certificate received in the final response.

For an uptime check to succeed, the following conditions must be met:

  * The HTTP status must match the criteria you specify.
  * The response data has no required content or the required content is present.



Uptime checks don't load page assets or run JavaScript, and the default configuration of an uptime check doesn't include authentication.

## Before you begin

Complete the following steps in the Google Cloud project that will store the uptime check. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  1. To get the permissions that you need to create uptime checks, ask your administrator to grant you the following IAM roles on your project: 

     * Google Cloud console users: [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) 
     * API users: 
       * [Monitoring Uptime Check Configurations Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.uptimeCheckConfigEditor) (`roles/monitoring.uptimeCheckConfigEditor`)
       * [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`)
       * [Monitoring NotificationChannel Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelEditor) (`roles/monitoring.notificationChannelEditor`)

**Note:** If you plan to create an uptime check on a Cloud Run service, then you must also have the [`run.routes.invoke`](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.routes.invoke) permission on that service.
  2. Verify that the resource that you want to check either has a public endpoint or is behind a configurable firewall.

For all other configurations, you must create a private uptime check. For more information, see [Create private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

  3. When your resource is behind a firewall, configure that firewall to permit incoming traffic from the IP addresses of the uptime-check servers. For more information, see [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks).

  4. Configure the notification channels that you want to use to receive notifications. We recommend that you create multiple types of notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  5. Identify at least three checkers for your uptime check. The uptime-check region `USA` includes the `USA_OREGON`, `USA_IOWA`, and `USA_VIRGINIA` regions. Each of the `USA_*` regions has one checker, and `USA` includes all three. The other uptime-check regions, `EUROPE`, `SOUTH_AMERICA`, and `ASIA_PACIFIC`, each have one checker. 

If you select **Global** when using the Google Cloud console, or select `REGION_UNSPECIFIED` when using the API, then uptime checks are issued from all uptime-check regions.

  6. Select the tab for how you plan to use the samples on this page:

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

### C#

To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. If you're using a local shell, then create local authentication credentials for your user account: 
            
            gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. If you're using a local shell, then create local authentication credentials for your user account: 
            
            gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. If you're using a local shell, then create local authentication credentials for your user account: 
            
            gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. If you're using a local shell, then create local authentication credentials for your user account: 
            
            gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### PHP

To use the PHP samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. If you're using a local shell, then create local authentication credentials for your user account: 
            
            gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. If you're using a local shell, then create local authentication credentials for your user account: 
            
            gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Ruby

To use the Ruby samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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




## Create an uptime check

This section explains how to create and configure uptime checks.

To create an uptime check for an external load balancer that has at least one TCP, HTTP, or HTTPS port configured, you can follow these instructions. An alternative is to go to the **Service details** page for the service and then click **Create uptime check**. When you start from the **Service details** page, the service-specific fields are prepopulated.

**Note:** All uptime checks use either HTTP `GET` or `POST` requests or TCP requests.

### Console

To create an uptime check by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Click **Create Uptime Check**.

![Create an uptime check dialog.](https://docs.cloud.google.com/static/monitoring/images/uf22-create-uptime-check.png)

  4. Specify the target of the uptime check:

     1. Select the protocol. You can select **HTTP** , **HTTPS** , or **TCP**.

     2. Choose one of the following resource types:

        * **URL** : Any IPv4 address or hostname. Path and port are entered separately.
        * **Kubernetes LoadBalancer Service** : Kubernetes Service of LoadBalancer type.
        * **Cloud Run Service** : If you select a Cloud Run service as the target of an uptime check, then make sure that you have the [`run.routes.invoke`](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.routes.invoke) permission on that service.
        * **App Engine** : App Engine applications (modules).
        * **Instance** : Compute Engine or AWS EC2 instances.
        * **Elastic Load Balancer** : AWS load balancer.
**Note:** Don't select **Internal IP** , as this resource type can't be a target of a public uptime check.
     3. Enter the protocol-specific fields:

        * For TCP checks, enter the port.

        * For HTTP and HTTPS checks, you can enter a path within your host or resource. All uptime checks that use these protocols send a request to `http://target/path`. In this expression, for a URL resource, `target` is a hostname or IP address. For an App Engine resource, `target` is a hostname derived from the service name. For instance and load balancer resources, `target` is an IP address derived from the name you provided for the resource or the group of resources.

If you leave the `path` field blank or if you set the value to `/`, then the request is issued to `http://target/`.

For example, to issue an uptime check to the URL resource `example.com/tester`, set the **Hostname** field to `example.com` and the **Path** field to `/tester`.

Suppose you've deployed a server to App Engine with a dispatcher that supports `/` and `/hello`. To issue the uptime check to the `/` handler, leave the **Path** field empty. To issue the uptime check to the `/hello` handler, set the value of the **Path** field to `/hello`.

     4. Enter the resource-specific fields:

        * For **URL** resources, enter the hostname in the **Hostname** field. For example, enter `example.com`.

**Note:** Create checks against direct URLs when possible.
        * For **App Engine** resources, enter the service name in the **Service** field.

        * For **Elastic Load Balancer** and **Instance** resources, complete the **Applies to** field as follows:

          * To issue an uptime check to a single instance or load balancer, select **Single** and then use the menu to select the specific instance or load balancer.
          * To issue an uptime check to a Monitoring group, select **Group** , and then use the menu to select the group name.
     5. Optional: To set how often the uptime check executes, use the **Check frequency** field.

     6. Optional: To select checker regions, or to configure SSL certificates, authentication, headers, and ports for HTTP and HTTPS checks, click **More target options** :

        * **Regions** : Select the regions where the uptime checks are to receive requests. An uptime check must have at least three checkers. There's one checker in all regions except the **United States** , which has three checkers. The default setting, **Global** , includes all regions.
        * **ICMP Pings** : Configure the uptime check to send up to three pings. For more information, see Use ICMP pings.
        * **Request Method** : For HTTP checks, select the request method.
        * **Body** : For HTTP POST checks, enter the URL-encoded body; you must do the encoding yourself. For all other checks, leave this field empty.
        * **Host header** : Fill this field in to check virtual hosts. This field isn't available for TCP checks.
        * **Port** : Specify a port number.
        * **Custom Headers** : Supply custom headers, and encrypt them if desired. Encryption hides the values of the header in the form. Use encryption for headers related to authentication that you don't want visible to others.
        * **Authentication** : These values are sent as an Authorization header. This field isn't available for TCP checks.

**Note:** Don't set the **Authentication** fields when you send an Authorization header. If you set the **Authentication** fields and send an Authorization header, then an `Invalid Argument` error occurs.

Choose from the following options:

          * **Basic Authentication** : Provide a single username and password. Passwords are always hidden in the form.
          * **Service Agent Authentication** : When enabled, an [identity token](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) is generated for the monitoring [service agent](https://docs.cloud.google.com/iam/docs/service-agents). This option is available only for HTTPS checks.
        * **SSL Certificate Validation** : If you selected HTTPS for a URL resource, then by default, the service attempts to connect over HTTPS and validate the SSL certificate. Uptime checks fail when a URL has an invalid certificate. Reasons for an invalid certificate include the following:

          * An expired certificate
          * A self-signed certificate
          * A certificate with a domain-name mismatch
          * A certificate that uses the Authority Information Access (AIA) extension.
**Note:** A revoked SSL certificate isn't considered invalid.

To force an HTTPS uptime check to validate the SSL certificate, select **Validate SSL certificates**.

To disable SSL certificate validation, clear **Validate SSL certificates**.

If you have SSL Certificates with [AIA Extensions](http://www.pkiglobe.org/auth_info_access.html), then you must disable SSL certificate validation. These types of certificates aren't supported and fail the validation sequence. Typically, the error message is "Responded with SSL handshake Error in 10000 ms".

You can use the metric `monitoring.googleapis.com/uptime_check/time_until_ssl_cert_expires` to create an alerting policy that notifies you before your certificate expires. For more information, see [Sample policies: Uptime-check policy](https://docs.cloud.google.com/monitoring/alerts/policies-in-json).

  5. Click **Continue** and configure the response requirements. All settings in this section have default values:

     * To change the timeout period for the uptime check, use the **Response Timeout** field. An uptime check fails when no response is received from more than one location within this period.

**Note:** If you create checks against redirection URLs, then increase the **Response Timeout** to 30 seconds or more.
     * To configure the uptime check to perform content matching, ensure that the toggle label is **Content matching is enabled** :

       * Select the **Response Content Match Type** from the menu of options. This field determines how the response content is compared to the returned data. For example, assume that the response content is `abcd` and the content match type is **Contains**. The uptime check is successful only when the response data contains `abcd`. For more information, see [Validate response data](https://docs.cloud.google.com/monitoring/uptime-checks/response-validation).
       * Enter the **Response content**. The response content must be a string no longer than 1024 bytes. In the API, this field is the [`ContentMatcher`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcher) object.
**Note:** Enable response content matching when you select the TCP protocol.
     * To prevent log entries from being created due to uptime checks, clear **Log check failures**.

     * For the HTTP uptime checks, configure the acceptable response codes. By default, HTTP uptime checks mark any `2xx` response as a successful response.

  6. Click **Continue** and configure notifications.

To be notified when an uptime check fails, create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) and configure [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options) for that policy:

     1. Optional: Update the name of the alerting policy.
     2. Optional: In the **Duration** field, select how long the uptime checks must fail before notifications are sent. By default, notifications are sent when at least two regions report uptime check failures for a duration of at least one minute.
     3. In the box labeled **Notification channels** , click _arrow_drop_down_ **Menu** , select the channels to add, and then click **OK**.

In the menu, the notification channels are grouped alphabetically for each channel type.

If you don't want to create an alerting policy, then ensure that the text of the toggle button is **Do not create an alert**.

  7. Click **Continue** and complete your uptime check:

     1. Enter a descriptive title for the uptime check.

     2. Optional: To add user-defined labels to your uptime check, do the following:

        1. Click _expand_more_ **Show user labels**.
        2. In the **Key** field, enter a name for the label. Label names must start with a lowercase letter, and they can contain lowercase letters, numerals, underscores, and dashes. For example, enter `severity`.
        3. In the **Value** field, enter a value for your label. Label values can contain lowercase letters, numerals, underscores, and dashes. For example, enter `critical`.
        4. For each additional label, click **Add user label** and then enter the key and value of the label.
     3. To verify your uptime check configuration, click **Test**. If the result isn't what you expect, see Check failures, correct your configuration, and then repeat the verification step.

     4. Click **Create**. If you select **Create** and a required field isn't populated, then an error message is displayed.




### gcloud

To create the uptime check, run the [`gcloud monitoring uptime create`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create) command:
    
    
    gcloud monitoring uptime create DISPLAY_NAME REQUIRED_FLAGS OPTIONAL_FLAGS --project=PROJECT_ID
    

Before you run the previous command, replace the following:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  * DISPLAY_NAME: The name for your uptime check.

  * REQUIRED_FLAGS: Configure to specify the resource probed by the uptime check. For example, the following command creates an uptime check that tests the URL EXAMPLE.com for a particular project:
        
        gcloud monitoring uptime create DISPLAY_NAME \
        --resource-labels=host=EXAMPLE.com,project_id=PROJECT_ID \
        --resource-type=uptime-url
        

The previous command specifies values for each label required by the resource type `uptime-url`.

**Note:** In the previous command, set the `resource-type` field to `uptime-url`; don't use `uptime_url`. The Google Cloud CLI commands don't follow the same naming conventions as Cloud Monitoring. For a list of valid values for the `resource-type` field, see the [`gcloud monitoring uptime create`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create) documentation.
  * OPTIONAL_FLAGS: Configure these flags to override default values. For example, you must set the `--protocol` flag when the protocol isn't `http`.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

To create an uptime check and an alerting policy to monitor that check, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) for you project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  2. Edit your Terraform configuration file and add a [`google_monitoring_uptime_check_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_uptime_check_config) resource, and then apply the configuration file.

The following example illustrates a configuration that checks a public URL:
         
         resource "google_monitoring_uptime_check_config" "example" {
             display_name = "example"
             timeout      = "60s"
         
             http_check {
                 port = "80"
                 request_method = "GET"
             }
         
             monitored_resource {
                 type = "uptime_url"
                 labels = {
                     project_id = "PROJECT_ID"
                     host="EXAMPLE.com"
                 }
             }
         
             checker_type = "STATIC_IP_CHECKERS"
         }
         

In the previous expression:

     * PROJECT_ID is the ID of your project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
     * EXAMPLE.com is the Host URL.
  3. Optional: Create a notification channel and an alerting policy:

The following steps use the Google Cloud console to create the notification channel and alerting policy. This approach ensures that the alerting policy only monitors the data generated by your uptime check.

     1. To create a notification channel, do the following:

        1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

        2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
        3. Select **Manage notification channels**.
        4. Go to the type of channel that you want to add, click **Add** , and then complete the dialog.
     2. To create an alerting policy, do the following:

        1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

        2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
        3. Locate your uptime check, select _more_vert_ **More** , and then select **Add alert policy**.
        4. In the dialog, go to the **Notifications and name** section, expand **Notification Channels** , and make your selections.
        5. Name the alerting policy and then click **Create policy**.

You can create an alerting policy by adding a [`google_monitoring_alert_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy) resource to your configuration file and applying the new configuration.




### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object CreateUptimeCheck(string projectId, string hostName,
        string displayName)
    {
        // Define a new config.
        var config = new UptimeCheckConfig()
        {
            DisplayName = displayName,
            MonitoredResource = new MonitoredResource()
            {
                Type = "uptime_url",
                Labels = { { "host", hostName } }
            },
            HttpCheck = new UptimeCheckConfig.Types.HttpCheck()
            {
                Path = "/",
                Port = 80,
            },
            Timeout = TimeSpan.FromSeconds(10).ToDuration(),
            Period = TimeSpan.FromMinutes(5).ToDuration()
        };
        // Create a client.
        var client = UptimeCheckServiceClient.Create();
        ProjectName projectName = new ProjectName(projectId);
        // Create the config.
        var newConfig = client.CreateUptimeCheckConfig(
            projectName,
            config,
            CallSettings.FromExpiration(
                Expiration.FromTimeout(
                    TimeSpan.FromMinutes(2))));
        Console.WriteLine(newConfig.Name);
        return 0;
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void createUptimeCheck(
        String projectId, String displayName, String hostName, String pathName) throws IOException {
      CreateUptimeCheckConfigRequest request =
          CreateUptimeCheckConfigRequest.newBuilder()
              .setParent(ProjectName.format(projectId))
              .setUptimeCheckConfig(
                  UptimeCheckConfig.newBuilder()
                      .setDisplayName(displayName)
                      .setMonitoredResource(
                          MonitoredResource.newBuilder()
                              .setType("uptime_url")
                              .putLabels("host", hostName))
                      .setHttpCheck(HttpCheck.newBuilder().setPath(pathName).setPort(80))
                      .setTimeout(Duration.newBuilder().setSeconds(10))
                      .setPeriod(Duration.newBuilder().setSeconds(300)))
              .build();
      try (UptimeCheckServiceClient client = UptimeCheckServiceClient.create()) {
        UptimeCheckConfig config = client.createUptimeCheckConfig(request);
        System.out.println("Uptime check created: " + config.getName());
      } catch (Exception e) {
        usage("Exception creating uptime check: " + e.toString());
        throw e;
      }
    }

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // createGet creates an example uptime check on a GET request.
    func createGet(w io.Writer, projectID string) (*monitoringpb.UptimeCheckConfig, error) {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.CreateUptimeCheckConfigRequest{
    		Parent: "projects/" + projectID,
    		UptimeCheckConfig: &monitoringpb.UptimeCheckConfig{
    			DisplayName: "new GET uptime check",
    			Resource: &monitoringpb.UptimeCheckConfig_MonitoredResource{
    				MonitoredResource: &monitoredres.MonitoredResource{
    					Type: "uptime_url",
    					Labels: map[string]string{
    						"host": "example.com",
    					},
    				},
    			},
    			CheckRequestType: &monitoringpb.UptimeCheckConfig_HttpCheck_{
    				HttpCheck: &monitoringpb.UptimeCheckConfig_HttpCheck{
    					RequestMethod: monitoringpb.UptimeCheckConfig_HttpCheck_GET,
    					Path:          "/",
    					Port:          80,
    				},
    			},
    			Timeout: &duration.Duration{Seconds: 10},
    			Period:  &duration.Duration{Seconds: 300},
    		},
    	}
    	config, err := client.CreateUptimeCheckConfig(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateUptimeCheckConfig GET: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully created GET uptime check %q\n", config.GetDisplayName())
    	return config, nil
    }
    
    // createPost creates an example uptime check on a POST request.
    func createPost(w io.Writer, projectID string) (*monitoringpb.UptimeCheckConfig, error) {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.CreateUptimeCheckConfigRequest{
    		Parent: "projects/" + projectID,
    		UptimeCheckConfig: &monitoringpb.UptimeCheckConfig{
    			DisplayName: "new POST uptime check",
    			Resource: &monitoringpb.UptimeCheckConfig_MonitoredResource{
    				MonitoredResource: &monitoredres.MonitoredResource{
    					Type: "uptime_url",
    					Labels: map[string]string{
    						"host": "example.com",
    					},
    				},
    			},
    			CheckRequestType: &monitoringpb.UptimeCheckConfig_HttpCheck_{
    				HttpCheck: &monitoringpb.UptimeCheckConfig_HttpCheck{
    					RequestMethod: monitoringpb.UptimeCheckConfig_HttpCheck_POST,
    					ContentType:   monitoringpb.UptimeCheckConfig_HttpCheck_URL_ENCODED,
    					Path:          "/",
    					Port:          80,
    					Body:          []byte(base64.URLEncoding.EncodeToString([]byte("key: value"))),
    				},
    			},
    			Timeout: &duration.Duration{Seconds: 10},
    			Period:  &duration.Duration{Seconds: 300},
    		},
    	}
    	config, err := client.CreateUptimeCheckConfig(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateUptimeCheckConfig POST: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully created POST uptime check %q\n", config.GetDisplayName())
    	return config, nil
    }
    

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[UptimeCheckServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment and edit the following lines of code.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const hostname = 'mydomain.com';
    
    const request = {
      // i.e. parent: 'projects/my-project-id'
      parent: client.projectPath(projectId),
      uptimeCheckConfig: {
        displayName: 'My Uptime Check',
        monitoredResource: {
          // See the Uptime Check docs for supported MonitoredResource types
          type: 'uptime_url',
          labels: {
            host: hostname,
          },
        },
        httpCheck: {
          path: '/',
          port: 80,
        },
        timeout: {
          seconds: 10,
        },
        period: {
          seconds: 300,
        },
      },
    };
    
    // Creates an uptime check config for a GCE instance
    const [uptimeCheckConfig] = await client.createUptimeCheckConfig(request);
    console.log('Uptime check created:');
    console.log(`ID: ${uptimeCheckConfig.name}`);
    console.log(`Display Name: ${uptimeCheckConfig.displayName}`);
    console.log('Resource: %j', uptimeCheckConfig.monitoredResource);
    console.log('Period: %j', uptimeCheckConfig.period);
    console.log('Timeout: %j', uptimeCheckConfig.timeout);
    console.log(`Check type: ${uptimeCheckConfig.check_request_type}`);
    console.log(
      'Check: %j',
      uptimeCheckConfig.httpCheck || uptimeCheckConfig.tcpCheck
    );
    console.log(
      `Content matchers: ${uptimeCheckConfig.contentMatchers
        .map(matcher => matcher.content)
        .join(', ')}`
    );
    console.log(`Regions: ${uptimeCheckConfig.selectedRegions.join(', ')}`);
    

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Api\MonitoredResource;
    use Google\Cloud\Monitoring\V3\Client\UptimeCheckServiceClient;
    use Google\Cloud\Monitoring\V3\CreateUptimeCheckConfigRequest;
    use Google\Cloud\Monitoring\V3\UptimeCheckConfig;
    
    /**
     * Example:
     * ```
     * create_uptime_check($projectId, 'myproject.appspot.com', 'Test Uptime Check!');
     * ```
     *
     * @param string $projectId Your project ID
     * @param string $hostName
     * @param string $displayName
     */
    function create_uptime_check($projectId, $hostName = 'example.com', $displayName = 'New uptime check')
    {
        $projectName = 'projects/' . $projectId;
        $uptimeCheckClient = new UptimeCheckServiceClient([
            'projectId' => $projectId,
        ]);
    
        $monitoredResource = new MonitoredResource();
        $monitoredResource->setType('uptime_url');
        $monitoredResource->setLabels(['host' => $hostName]);
    
        $uptimeCheckConfig = new UptimeCheckConfig();
        $uptimeCheckConfig->setDisplayName($displayName);
        $uptimeCheckConfig->setMonitoredResource($monitoredResource);
        $createUptimeCheckConfigRequest = (new CreateUptimeCheckConfigRequest())
            ->setParent($projectName)
            ->setUptimeCheckConfig($uptimeCheckConfig);
    
        $uptimeCheckConfig = $uptimeCheckClient->createUptimeCheckConfig($createUptimeCheckConfigRequest);
    
        printf('Created an uptime check: %s' . PHP_EOL, $uptimeCheckConfig->getName());
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_uptime_check_config_get(
        project_id: str, host_name: str = None, display_name: str = None
    ) -> uptime.UptimeCheckConfig:
        """Creates a new uptime check configuration
    
        Args:
            project_id: Google Cloud project id where the uptime check is created
            host_name: An example label's value for the "host" label
            display_name: A human friendly name of the configuration
    
        Returns:
            A structure that describes a new created uptime check
        """
        config = monitoring_v3.UptimeCheckConfig()
        config.display_name = display_name or "New GET uptime check"
        config.monitored_resource = {
            "type": "uptime_url",
            "labels": {"host": host_name or "example.com"},
        }
        config.http_check = {
            "request_method": monitoring_v3.UptimeCheckConfig.HttpCheck.RequestMethod.GET,
            "path": "/",
            "port": 80,
        }
        config.timeout = {"seconds": 10}
        config.period = {"seconds": 300}
    
        client = monitoring_v3.UptimeCheckServiceClient()
        new_config = client.create_uptime_check_config(
            request={"parent": project_id, "uptime_check_config": config}
        )
        pprint.pprint(new_config)
        return new_config
    
    
    def create_uptime_check_config_post(
        project_id: str, host_name: str = None, display_name: str = None
    ) -> uptime.UptimeCheckConfig:
        """Creates a new uptime check configuration
    
        Args:
            project_id: Google Cloud project id where the uptime check is created
            host_name: An example label's value for the "host" label
            display_name: A human friendly name of the configuration
    
        Returns:
            A structure that describes a new created uptime check
        """
        config = monitoring_v3.UptimeCheckConfig()
        config.display_name = display_name or "New POST uptime check"
        config.monitored_resource = {
            "type": "uptime_url",
            "labels": {"host": host_name or "example.com"},
        }
        config.http_check = {
            "request_method": monitoring_v3.UptimeCheckConfig.HttpCheck.RequestMethod.POST,
            "content_type": monitoring_v3.UptimeCheckConfig.HttpCheck.ContentType.URL_ENCODED,
            "body": "foo=bar".encode("utf-8"),
            "path": "/",
            "port": 80,
        }
        config.timeout = {"seconds": 10}
        config.period = {"seconds": 300}
    
        client = monitoring_v3.UptimeCheckServiceClient()
        new_config = client.create_uptime_check_config(
            request={"parent": project_id, "uptime_check_config": config}
        )
        pprint.pprint(new_config)
        return new_config
    
    

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    def create_uptime_check_config project_id: nil, host_name: nil, display_name: nil
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
      project_name = client.project_path project: project_id
      config = {
        display_name:       display_name.nil? ? "New uptime check" : display_name,
        monitored_resource: {
          type:   "uptime_url",
          labels: { "host" => host_name.nil? ? "example.com" : host_name }
        },
        http_check:         { path: "/", port: 80 },
        timeout:            { seconds: 10 },
        period:             { seconds: 300 }
      }
      new_config = client.create_uptime_check_config \
        parent:              project_name,
        uptime_check_config: config
      puts new_config.name
      new_config
    end

### REST

To create an uptime check, call the [`projects.uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) method. Set the method's parameters as follows:

  * **parent** : Required. The project in which to create the uptime check. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. This field has the following format:
        
        projects/PROJECT_ID
        

  * The request body must contain an `UptimeCheckConfig` object for the new uptime check. This page provides information about a few fields. For complete documentation on this object and its fields, see [`UptimeCheckConfig`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig):

    * Leave the `name` field of the configuration object blank. The system sets this field when it constructs the response configuration object.

    * If you are configuring an HTTP or HTTPS check, then you must populate the [`HttpCheck`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck) field of the `UptimeCheckConfig` object. In this object, set the [`requestMethod`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck.FIELDS.request_method) field as `GET` or `POST`. If this field is omitted or set to `METHOD_UNSPECIFIED`, then a `GET` request is issued.

If you are configuring a `POST` request, then complete the [`contentType`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck.FIELDS.content_type), optional [`customContentType`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck.FIELDS.custom_content_type), and [`body`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck.FIELDS.body) fields.




The `create` method returns the [`UptimeCheckConfig`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) object for the new configuration.

If the created uptime configuration doesn't work as expected, see the Check failures section on this page. 

There can be a delay of up to 5 minutes before the uptime check results start to flow into Monitoring. During that time, the uptime check dashboard reports the status as "no data available."

## Use ICMP pings

To help you troubleshoot failed public uptime checks, you can configure your uptime checks to send up to 3 ICMP pings during the check. The pings can help you distinguish between failures caused, for example, by network connectivity problems and by timeouts in your application.

By default, uptime checks don't send pings. Each ping adds some latency to the uptime check. Private uptime checks can't send pings.

When a public uptime check fails, the results of the pings are written to Cloud Logging logs. If the ping fails, then the following fields are added to the `httpRequest` field in the log entry:

  * `rtt_usec`: round-trip time for each unsuccessful ping request.
  * `unreachable_count`: number of ping requests that returned the status code `ICMP_DEST_UNREACH`.
  * `no_answer_count`: number of ping requests that timed out and returned no response.



The results of pings for successful uptime checks aren't logged.

### Configure pings

Each uptime-check configuration includes either an [`HttpCheck`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck) object or a [`TcpCheck`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#TcpCheck) object. Both of these objects include a `pingConfig` field. Use this field to specify the number of ICMP pings to include with each check, up to 3. By default, no pings are sent.

To configure pings, do one of the following:

  * When using the Google Cloud console, expand **More target options** and enter a value in the **ICMP Pings** field.

  * When using the Cloud Monitoring API, use the [`PingConfig`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#PingConfig) object, which has the following structure:
        
        {
          "pingsCount": integer
        }
        

For more information about using the Monitoring API for uptime-check configurations, see Create an uptime check: API or [Edit an uptime check: API](https://docs.cloud.google.com/monitoring/uptime-checks/manage#monitoring_uptime_check_update-rest).




## Verify your uptime check

When you create an uptime check in the Google Cloud console, you can test the configuration before saving.

### Successful checks

An uptime check is successful when the following conditions are true:

  * The HTTP status matches the criteria you selected.
  * The response has no required content, or a search of the response for the required content is successful.



### Failed checks

The following are some possible causes of an uptime check failure:

  * **Connection Error - Refused** : If you are using the default **HTTP** connection type, check that you have a web server installed that is responding to HTTP requests. A connection error can happen on a new instance if you haven't installed a web server; see the [Quickstart for Compute Engine](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine). If you use an **HTTPS** connection type, you might have to perform additional configuration steps. For firewall issues, see [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks).
  * **Name or service not found** : The hostname might be incorrect.
  * **403 Forbidden** : The service is returning an error code to the uptime checker. For example, the default Apache web server configuration returns this code under Amazon Linux, but it returns code **200 (Success)** under some other Linux versions. See the [LAMP tutorial for Amazon Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html) or your web server's documentation.

If you see this error message and the target of your uptime check is a Cloud Run service, then make sure that you have the [`run.routes.invoke`](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.routes.invoke) permission on that service.

  * **404 Not found** : The path might be incorrect.

  * **408 Request timeout** , or no response: The port number might be incorrect, the service might not be running, the service might be inaccessible, or the timeout might be too low. Check that your firewall allows traffic from the uptime servers; see [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks). The timeout limit is specified as part of the **Response Validation** options.

A request timeout might occur due to network congestion. For example, due to temporary network congestion, you might notice that [one checker fails but all other checkers succeed](https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot#one-checker-failed). The failure of a single checker doesn't cause a notification when your alerting policy uses the default configuration.




If your uptime check is configured to send pings, then the results of pings for failed uptime checks are written to Cloud Logging. For more information, see [Use ICMP pings](https://docs.cloud.google.com/monitoring/uptime-checks#ping).

## Limitations

Public uptime checks are not supported inside of a VPC Service Controls perimeter. Private uptime checks can be within a VPC Service Controls perimeter. For more information, see [Create private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

## What's next

  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)
  * [Create alerting policies for uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies)
  * [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks)
  * [Chart uptime-check metrics](https://docs.cloud.google.com/monitoring/charts/uptime-charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
