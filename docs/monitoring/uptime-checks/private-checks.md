---
url: https://docs.cloud.google.com/monitoring/uptime-checks/private-checks/
title: Create private uptime checks \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:26.063054+00:00
---

# Create private uptime checks  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/uptime-checks/private-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create private uptime checks Stay organized with collections  Save and categorize content based on your preferences. 

Private uptime checks let you test the availability of internal resources—such as virtual machines (VMs) or L4 internal load balancers (ILBs)—without exposing them to the public internet. These checks use [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) to send HTTP, HTTPS, or TCP requests to internal IP addresses in a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs) network while respecting [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) permissions and VPC Service Controls perimeters.

To configure uptime checks for publicly accessible endpoints instead, see [Create public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks).

This feature is supported only for Google Cloud projects. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

## About private uptime checks

The internal IP addresses for resources on the private network are recorded by [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) services with [private network access](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access#configure-the-network-project) enabled. To use private uptime checks, you must configure private network access by using the Service Directory product.

The Google Cloud project that stores the private uptime check and the Google Cloud project that stores the Service Directory service can be different projects. Cloud Monitoring lets you monitor resources in multiple Google Cloud projects from one project by using a metrics scope. The project in which the uptime check is defined is the scoping project of a metrics scope; the metrics scope is a list of all projects the scoping project monitors. The Service Directory service might be defined in the scoping project or in a project in the metrics scope. For more information about metrics scopes, see [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings).

The private network and its resources, like VMs or load balancers, can also be in a different Google Cloud project. This project doesn't have to be in the metrics scope of the uptime check's scoping project. The Service Directory service collects the uptime metrics, so it must be in the metrics scope, but the resources it encapsulates don't.

This document describes how to set up a private network and configure Service Directory resources for it by using the Google Cloud console or the API. The API examples assume that the private network and the Service Directory service are in the scoping project of the uptime check. However, Create a private uptime check also describes how to use the API to create an uptime check that uses a Service Directory service in the metrics scope.

## Before you begin

Complete the following steps in the Google Cloud project where you plan to create your private uptime check. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  1. Enable APIs:

###  Console 

Enable the Cloud Monitoring, Service Directory, Service Networking, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,servicedirectory.googleapis.com,servicenetworking.googleapis.com,compute.googleapis.com)

###  gcloud 

Enable the Cloud Monitoring, Service Directory, Service Networking, and Compute Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable monitoring.googleapis.com servicedirectory.googleapis.com servicenetworking.googleapis.com compute.googleapis.com

  2. Configure the notification channels that you want to use to receive notifications. We recommend that you create multiple types of notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  3. Configure a private network and configure a VM or ILB to have access to that private network. For more information, see [Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).

Private checks that target ILBs are limited to the regions with uptime checkers. The uptime-check region `USA` includes the `USA_OREGON`, `USA_IOWA`, and `USA_VIRGINIA` regions. Each of the `USA_*` regions has one checker, and `USA` includes all three. The other uptime-check regions, `EUROPE`, `SOUTH_AMERICA`, and `ASIA_PACIFIC`, each have one checker. To remove this limitation, you must configure global access to your load balancer. For more information about how to configure global access, see the ILB tab in the Configure Service Directory resources section of this document.

If you plan to check an ILB that doesn't permit global access, then select one of the following regions for your ILB:

     * `us-east4`
     * `us-central1`
     * `us-west1`
     * `europe-west1`
     * `southamerica-east1`
     * `asia-southeast1`
  4. Determine which interface to use:

     * Google Cloud console: Lets you create an uptime check when a VM is servicing requests. This interface guides you through configuring Service Directory resources, authorizing the service account, and configuring the network firewall rules.

     * Command line interfaces: You can use Google Cloud CLI and the Cloud Monitoring API to create private uptime checks when ILBs and VMs are servicing requests.

  5. If you plan to use the command line to configure your private uptime checks, then complete the Prerequisite steps.




## Create a private uptime check

This section explains how to create and configure private uptime checks of Service Directory services:

  * To use the Google Cloud console, select the **Console** tab.

  * To use the Cloud Monitoring API and to configure the Service Directory service to be in the same Google Cloud project as the uptime check, select the **gcloud: Scoping project** tab.

  * To use the Cloud Monitoring API and to configure the Service Directory service to be in a project monitored by the metrics scope of the uptime check's project, select the **gcloud: Monitored project** tab.




###  Console 

To create an uptime check by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Click **Create Uptime Check**.

![Create an uptime check dialog.](https://docs.cloud.google.com/static/monitoring/images/uf22-create-uptime-check.png)

  4. Specify a private uptime check:

     1. Select the protocol, which can be **HTTP** , **HTTPS** , or **TCP**.

     2. Choose the **Internal IP** resource type.

  5. If you don't have a Service Directory service configured for your project or if you want to create a Service Directory service, then click **View** and complete the **Private Uptime Check Prerequisites** pane:

     1. If prompted, enable the Compute Engine API or the Service Directory API. Enabling the APIs might take a minute to complete.

     2. Expand _arrow_drop_down_ **Service Account** , if shown, and then click **Create Service Account**.

When a Monitoring service account doesn't exist, one is created. Then, Monitoring grants the service account two Service Directory roles.

     3. Expand the _arrow_drop_down_ **Service Directory** menu and then do the following:

        1. Expand _arrow_drop_down_ **Region** and then select the region of the VM that is serving requests.
        2. Expand _arrow_drop_down_ **Namespace** and then either select an existing Service Directory namespace or click **Create namespace** and create a namespace.
        3. Click **Service name** and enter a service name. Services are the targets of private uptime checks.
        4. Click **Endpoint name** and enter a name for the endpoint. An endpoint is a pair of IP address and port values that a service can use to handle requests. When your service contains multiple endpoints, one endpoint is chosen at random.
        5. Expand _arrow_drop_down_ **Network** and then select your private network.
        6. Expand _arrow_drop_down_ **Instance** and then select the VM on the private network that is serving requests. After you select the instance, its internal IP address is displayed.
        7. Click **Done**.
     4. Expand _arrow_drop_down_ **Firewall rules** :

        1. Expand _arrow_drop_down_ **Network** and select the network to which the network rule is attached.

        2. Click **Create Firewall Rules**.

The firewall rule enables inbound TCP traffic from routes 35.199.192.0/19. A route from 35.199.192.0/19 supports connectivity to forwarding targets that use private routing. For more information, see [VPC routes](https://docs.cloud.google.com/vpc/docs/routes).

  6. In the **Private Uptime Check** pane, to specify the Service Directory service to use, do one of the following:

     * Select **Use fully qualified service name** and then enter the fully qualified name of the service:
           
           projects/SERVICE_DIRECTORY_PROJECT_ID/locations/REGION/namespaces/PRIVATE_NAMESPACE/services/PRIVATE_SERVICE
           

     * Select the **Region** , **Namespace** , and **Service** by using the menus. If you created a service, then these fields are selected for you.

  7. In the **Private Uptime Check** pane, complete the description of the target of the uptime check:

     1. Optional: Enter a path component for the request.

Private uptime checks that use the HTTP or HTTPS protocol send a request to `http://target/path`. In this expression, the `target` is the internal IP address configured in the Service Directory endpoint.

If you leave the **Path** field blank or if you set the value to `/`, then the request is issued to `http://target/`.

     2. Optional: To set how often the uptime check executes, use the **Check frequency** field.

     3. Optional: To select checker regions, or to configure authentication, headers for HTTP and HTTPS checks, and other values, click **More target options** :

        * **Regions** : Select the regions where the uptime checks are to receive requests. An uptime check must have at least three checkers. There's one checker in all regions except the **United States** , which has three checkers. The default setting, **Global** , includes all regions.
        * **Request Method** : Select `GET` or `POST`.
        * **Body** : For HTTP `POST` checks, enter the URL-encoded body; you must do the encoding yourself. For all other checks, leave this field empty.
        * **Host header** : Don't set this field when configuring private uptime checks. 
        * **Port** : Any value you set here overrides the port in your Service Directory endpoint configuration. Don't set a value here if you want the endpoint configuration to be used. 
        * **Custom Headers** : Supply custom headers, and optionally, encrypt them. Encryption hides the values in the header in the form. Use encryption for headers related to authentication that you don't want visible to others.
        * **Authentication** : Provide a single username and password. These values are sent as an Authorization header. If you set values here, don't set a separate Authorization header; if you set an Authorization header, don't set values here. Passwords are always hidden in the form.
  8. Click **Continue** and configure the response requirements. All settings in this section have default values:

     * To set a timeout period for the uptime check, use the **Response Timeout** field. An uptime check fails when no response is received from more than one location within this period.

     * To configure the uptime check to perform content matching, ensure that the toggle label is **Content matching is enabled** :

       * Select the **Response Content Match Type** from the menu of options. This field determines how the response content is compared to the returned data. For example, assume that the response content is `abcd` and the content match type is **Contains**. The uptime check is successful only when the response data contains `abcd`. For more information, see [Validate response data](https://docs.cloud.google.com/monitoring/uptime-checks/response-validation).
       * Enter the **Response content**. The response content must be a string no longer than 1024 bytes. In the API, this field is the [`ContentMatcher`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcher) object.
     * To prevent log entries from being created due to uptime checks, clear **Log check failures**.

     * For the HTTP uptime checks, configure the acceptable response codes. By default, HTTP uptime checks mark any `2xx` response as a successful response.

  9. Click **Continue** and configure alerting policies and notifications.

To be notified when an uptime check fails, create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) and configure [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options) for that policy:

     1. Optional: Update the name of the alerting policy.
     2. Optional: In the **Duration** field, select how long the uptime checks must fail before notifications are sent. By default, notifications are sent when at least two regions report uptime check failures for a duration of at least one minute.
     3. In the box labeled **Notification channels** , expand _arrow_drop_down_ **Menu** , select the channels to add, and then click **OK**.

In the menu, the notification channels are grouped alphabetically for each channel type.

If you don't want to create an alerting policy, then ensure that the text of the toggle button is **Do not create an alert**.

  10. Click **Continue** and complete the uptime check:

     1. Enter a descriptive title for the uptime check.

     2. Optional: To add user-defined labels to your uptime check, do the following:

        1. Click _expand_more_ **Show user labels**.
        2. In the **Key** field, enter a name for the label. Label names must start with a lowercase letter, and they can contain lowercase letters, numerals, underscores, and dashes. For example, enter `severity`.
        3. In the **Value** field, enter a value for your label. Label values can contain lowercase letters, numerals, underscores, and dashes. For example, enter `critical`.
        4. For each additional label, click **Add user label** and then enter the key and value of the label.
     3. To verify your uptime check configuration, click **Test**. If the result isn't what you expect, see Troubleshooting, correct your configuration, and then repeat the verification step.

     4. Click **Create**.




###  gcloud: Scoping project 

To create the configuration for a private uptime check, you create an [`UptimeCheckConfig`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig) object and pass that object to the [`uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) method in the Cloud Monitoring API.

The `UptimeCheckConfig` object for a private uptime check differs from the object for a public uptime check in the following ways:

  * The monitored resource specified in the uptime-check configuration must be of type [`servicedirectory_service`](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service). This resource type has the following labels: 
    * `project_id`: The project ID associated with the Service Directory service.
    * `location`: The cloud region associated with the service.
    * `namespace_name`: The Service Directory namespace.
    * `service_name`: The name of the Service Directory service.

**Note** : The values for these labels are determined when you Configure Service Directory resources.

  * You don't need to specify a `port` value in the uptime-check configuration. The port value from the Service Directory endpoint overrides any value set in the uptime-check configuration, and the check fails if no port is specified in the Service Directory configuration.

  * The uptime-check configuration must specify the `checker_type` field with the value `VPC_CHECKERS`. This value is required for private uptime checks. By default, uptime checks are public, so public uptime checks don't need to specify this field.



The following JSON code illustrates an `UptimeCheckConfig` object for a private uptime check using the Service Directory resources configured for a VM instance on a private network:
    
    
    {
      "displayName": "private-check-demo",
      "monitoredResource": {
        "type": "servicedirectory_service",
        "labels": {
          "project_id": "SERVICE_DIRECTORY_PROJECT_ID",
          "service_name": "PRIVATE_SERVICE",
          "namespace_name": "PRIVATE_NAMESPACE",
          "location": "REGION"
        }
      },
      "httpCheck": {
        "requestMethod": "GET"
      },
      "period": "60s",
      "timeout": "10s",
      "checker_type": "VPC_CHECKERS"
    }
    

To create a private uptime check when the Service Directory service is in the same Google Cloud project as the uptime check, do the following:

  1. Set the default Google Cloud project for the gcloud CLI:
         
         gcloud config set project PROJECT_ID
         

  2. Create an environment variable to store your project ID:
         
         export PROJECT_ID=$(gcloud config get-value core/project)
         

  3. Create an environment variable to hold an access token:
         
         export TOKEN=`gcloud auth print-access-token`
         

  4. Use the `curl` tool to invoke the [`uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) method and post a configuration object to it:
         
         curl https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/uptimeCheckConfigs \
         -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
         --request POST --data '{
         "displayName": "private-check-demo",
         "monitoredResource": {
           "type": "servicedirectory_service",
           "labels": {
             "project_id": "'"$PROJECT_ID"'",
             "service_name": "PRIVATE_SERVICE",
             "namespace_name": "PRIVATE_NAMESPACE",
             "location": "REGION"
           }
         },
         "httpCheck": {
           "requestMethod": "GET"
         },
         "period": "60s",
         "timeout": "10s",
         "checker_type": "VPC_CHECKERS"
         }'
         




If the creation of the uptime check fails, then verify that the service account has the necessary roles. For more information, see Creation of uptime check fails.

###  gcloud: Monitored project 

To create the configuration for a private uptime check, you create an [`UptimeCheckConfig`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig) object and pass that object to the [`uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) method in the Cloud Monitoring API.

The `UptimeCheckConfig` object for a private uptime check differs from the object for a public uptime check in the following ways:

  * The monitored resource specified in the uptime-check configuration must be of type [`servicedirectory_service`](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service). This resource type has the following labels: 
    * `project_id`: The project ID associated with the Service Directory service.
    * `location`: The cloud region associated with the service.
    * `namespace_name`: The Service Directory namespace.
    * `service_name`: The name of the Service Directory service.

**Note** : The values for these labels are determined when you Configure Service Directory resources.

  * You don't need to specify a `port` value in the uptime-check configuration. The port value from the Service Directory endpoint overrides any value set in the uptime-check configuration, and the check fails if no port is specified in the Service Directory configuration.

  * The uptime-check configuration must specify the `checker_type` field with the value `VPC_CHECKERS`. This value is required for private uptime checks. By default, uptime checks are public, so public uptime checks don't need to specify this field.



The following JSON code illustrates an `UptimeCheckConfig` object for a private uptime check using the Service Directory resources configured for a VM instance on a private network:
    
    
    {
      "displayName": "private-check-demo",
      "monitoredResource": {
        "type": "servicedirectory_service",
        "labels": {
          "project_id": "SERVICE_DIRECTORY_PROJECT_ID",
          "service_name": "PRIVATE_SERVICE",
          "namespace_name": "PRIVATE_NAMESPACE",
          "location": "REGION"
        }
      },
      "httpCheck": {
        "requestMethod": "GET"
      },
      "period": "60s",
      "timeout": "10s",
      "checker_type": "VPC_CHECKERS"
    }
    

To create a private uptime check when the Service Directory service is in a Google Cloud project that is monitored by the metrics scope of the uptime check's Google Cloud project, do the following:

  1. Configure the gcloud CLI to default to the Google Cloud project where the uptime check is to be created:
         
         gcloud config set project PROJECT_ID
         

  2. Create an environment variable to store your project ID:
         
         export PROJECT_ID=$(gcloud config get-value core/project)
         

  3. Create an environment variable to store the project ID of the Google Cloud project in which the Service Directory service is defined:
         
         export MONITORED_PROJECT_ID=MONITORED_PROJECT_ID
         

This project must be in the metrics scope of the uptime check's project.

  4. Create an environment variable to hold an access token:
         
         export TOKEN=`gcloud auth print-access-token`
         

  5. Use the `curl` tool to invoke the [`uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) method and post a configuration object to it:
         
         curl https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/uptimeCheckConfigs \
         -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
         --request POST --data '{
         "displayName": "private-check-demo",
         "monitoredResource": {
           "type": "servicedirectory_service",
           "labels": {
             "project_id": "'"$MONITORED_PROJECT_ID"'",
             "service_name": "PRIVATE_SERVICE",
             "namespace_name": "PRIVATE_NAMESPACE",
             "location": "REGION"
           }
         },
         "httpCheck": {
           "requestMethod": "GET"
         },
         "period": "60s",
         "timeout": "10s",
         "checker_type": "VPC_CHECKERS"
         }'
         




If the creation of the uptime check fails, then verify that the service account has the necessary roles. For more information, see Creation of uptime check fails.

There can be a delay of up to 5 minutes before the uptime check results start to flow into Monitoring. During that time, the uptime check dashboard reports the status as "no data available."

## Prerequisite steps

If you plan to use the Google Cloud console interface, then go to Create a private uptime check. The Google Cloud console guides you through all prerequisite steps.

If you plan to use the command line to configure your private uptime checks, then you must complete the following steps before you can create the uptime check:

  1. Configure Service Directory resources
  2. Authorize the service account
  3. Configure firewall rules



### Configure Service Directory resources

Private uptime checks determine the availability of a resource by using an internal IP address that is recorded by a [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) service. You can configure a Service Directory service for the following resources:

  * VMs on a private network
  * L4 internal load balancers (ILBs)



To use private uptime checks, you must configure the following Service Directory resources:

  * _Endpoint_ : An endpoint is a pair of IP address and port values that a service can use to handle requests. When your service contains multiple endpoints, one endpoint is chosen at random.
  * _Service_ : A service is a collection of endpoints that provide a set of behaviors. Services are the targets of private uptime checks.
  * _Namespace_ : A namespace holds a set of service names and their associated endpoints. Namespaces let you group services together for consistent management.



You can configure these resources with the gcloud CLI or the Google Cloud console. When you use the console, the configuration steps are included in the **Create Uptime Check** dialog.

###  Console 

When you use the Google Cloud console, after you select **Internal IP** as the resource type for an uptime check, you are prompted to create a Service Directory namespace and a service.

###  gcloud: VM 

For information about the commands used in this document for services, namespaces, and endpoints, see the [`gcloud service-directory` command group](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory).

To create Service Directory resources for a VM, do the following:

  1. Configure the Google Cloud CLI to default to the Google Cloud project where the Service Directory resources are to be created:
         
         gcloud config set project PROJECT_ID
         

  2. Create environment variables to store your project ID and project number:
         
         export PROJECT_ID=$(gcloud config get-value core/project)
         
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='get(projectNumber)')
         

  3. Create a Service Directory namespace:
         
         gcloud service-directory namespaces create PRIVATE_NAMESPACE --location=REGION
         

  4. Create a Service Directory service in the namespace:
         
         gcloud service-directory services create PRIVATE_SERVICE \
         --namespace PRIVATE_NAMESPACE --location=REGION
         

  5. Create an environment variable to hold the IP address of the VM on the private network:
         
         export INTERNAL_IP=$(gcloud compute instances describe --zone=ZONE \
         PRIVATE_SERVICE_INSTANCE --format='get(networkInterfaces[0].networkIP)')
         

  6. Create a Service Directory endpoint that contains the internal IP address and a port:
         
         gcloud service-directory endpoints create PRIVATE_ENDPOINT \
         --location=REGION --namespace=PRIVATE_NAMESPACE \
         --service=PRIVATE_SERVICE \
         --network=projects/$PROJECT_NUMBER/locations/global/networks/PRIVATE_CHECK_NETWORK \
         --address=$INTERNAL_IP --port=80
         




###  gcloud: L4 ILB 

For information about the commands used in this document for services, namespaces, and endpoints, see the [`gcloud service-directory` command group](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory).

You can use private uptime checks to monitor availability of an L4 internal load balancer (ILB) by creating Service Directory resources for the L4 ILB.

When you create new L4 ILBs, you can use the automatic integration provided by Service Directory; for more information, see [Configure internal load balancers in Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-ilb-in-sd).

If you have L4 ILBs that were created without using the automatic integration provided by Service Directory, then you can manually configure the Service Directory resources by doing the following:

  1. Configure the Google Cloud CLI to default to the Google Cloud project where the Service Directory resources are to be created:
         
         gcloud config set project PROJECT_ID
         

  2. Create environment variables to store your project ID and project number:
         
         export PROJECT_ID=$(gcloud config get-value core/project)
         
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='get(projectNumber)')
         

  3. To permit all uptime checkers to transfer data to your L4 ILB, enable global access to the ILB:
         
         gcloud compute forwarding-rules update ILB_FORWARDING_RULE_NAME \
         --region=ILB_REGION --allow-global-access
         

If your L4 ILB doesn't permit global access, then uptime metrics are available only if ILB_REGION is one of the following:

     * `us-east4`
     * `us-central1`
     * `us-west1`
     * `europe-west1`
     * `southamerica-east1`
     * `asia-southeast1`
  4. Create a Service Directory namespace:
         
         gcloud service-directory namespaces create PRIVATE_NAMESPACE_FOR_ILB\
         --location=REGION
         

  5. Create a Service Directory service in the namespace:
         
         gcloud service-directory services create PRIVATE_SERVICE_FOR_ILB \
         --namespace PRIVATE_NAMESPACE_FOR_ILB --location=REGION
         

  6. Create an environment variable to hold the IP address of the load balancer on the private network:
         
         export INTERNAL_IP=$( gcloud compute forwarding-rules describe ILB_FORWARDING_RULE_NAME\
         --region=ILB_REGION --format='get(IPAddress)')
         

  7. Create a Service Directory endpoint that contains the internal IP address and a port:
         
         gcloud service-directory endpoints create PRIVATE_ENDPOINT_FOR_ILB \
         --location=ILB_REGION --namespace=PRIVATE_NAMESPACE_FOR_ILB \
         --service=PRIVATE_SERVICE_FOR_ILB \
         --network=projects/$PROJECT_NUMBER/locations/global/networks/PRIVATE_CHECK_NETWORK \
         --address=$INTERNAL_IP --port=80
         




### Authorize the service account

Uptime checks use a Monitoring-owned service account to manage interactions with the Service Directory service. The service account name has the following format:
    
    
    service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com

When this service account doesn't exist, Monitoring creates the service account when you create the private uptime check. You can't create this service account.

When you create a private uptime check, Monitoring attempts to grant the service account two Service Directory roles. However, when you use the API, your Google Cloud project settings might prevent Monitoring from granting roles to the service account. In this situation, the creation of the uptime check fails.

This section describes how you can grant the required roles to an existing service account:

###  Console 

When you use the Google Cloud console, after you select **Internal IP** as the resource type for an uptime check, you are prompted to authorize the service account.

###  gcloud: Scoping project 

To grant the [Service Directory roles](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory) to an existing service account, do the following:

  1. Configure the gcloud CLI to default to the Google Cloud project where the uptime check is to be created:
         
         gcloud config set project PROJECT_ID
         

  2. Create environment variables to store the project ID and project number:
         
         export PROJECT_ID=$(gcloud config get-value core/project)
         
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='get(projectNumber)')
         

  3. Run the following commands:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
         --member='serviceAccount:service-'$PROJECT_NUMBER'@gcp-sa-monitoring-notification.iam.gserviceaccount.com' \
         --role='roles/servicedirectory.viewer'
         
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
         --member='serviceAccount:service-'$PROJECT_NUMBER'@gcp-sa-monitoring-notification.iam.gserviceaccount.com' \
         --role='roles/servicedirectory.pscAuthorizedService'
         

The previous commands grant the following roles to the service account:

     * `roles/servicedirectory.viewer`
     * `roles/servicedirectory.pscAuthorizedService`



###  gcloud: Monitored project 

To grant the [Service Directory roles](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory) to an existing service account, do the following:

  1. Configure the gcloud CLI to default to the Google Cloud project where the uptime check is to be created:
         
         gcloud config set project PROJECT_ID
         

  2. Create environment variables to store the project ID and project number:
         
         export PROJECT_ID=$(gcloud config get-value core/project)
         
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='get(projectNumber)')
         

  3. Create an environment variable to hold the project ID of the project in which the Service Directory service is defined:
         
         export MONITORED_PROJECT_ID=MONITORED_PROJECT_ID
         

This project must be in the metrics scope of the uptime check's project.

  4. Create an environment variable to hold the project ID of the project where the network is defined:
         
         export NETWORK_PROJECT_ID=NETWORK_PROJECT_ID
         

This project doesn't need to be in the metrics scope of the uptime check's project.

  5. Run the following commands:
         
         gcloud projects add-iam-policy-binding $MONITORED_PROJECT_ID \
         --member='serviceAccount:service-'$PROJECT_NUMBER'@gcp-sa-monitoring-notification.iam.gserviceaccount.com' \
         --role='roles/servicedirectory.viewer'
         
         
         gcloud projects add-iam-policy-binding $NETWORK_PROJECT_ID \
         --member='serviceAccount:service-'$PROJECT_NUMBER'@gcp-sa-monitoring-notification.iam.gserviceaccount.com' \
         --role='roles/servicedirectory.pscAuthorizedService'
         

The previous commands grant the following roles to the service account:

     * `roles/servicedirectory.viewer` for the monitored project in which the Service Directory service is configured, `$MONITORED_PROJECT_ID`.
     * `roles/servicedirectory.pscAuthorizedService` for the project in which the private network is configured, `$NETWORK_PROJECT_ID`.



### Configure firewall rules

You must create a firewall rule that enables inbound TCP traffic from routes 35.199.192.0/19. A route from 35.199.192.0/19 supports connectivity to forwarding targets that use private routing. For more information, see [VPC routes](https://docs.cloud.google.com/vpc/docs/routes).

###  Console 

When you use the Google Cloud console, after you select **Internal IP** as the resource type for an uptime check, you are prompted to configure the firewall rules.

###  gcloud 

To create a firewall rule that permits inbound TCP traffic through the firewall for private network access, run the following command:

  1. Configure the gcloud CLI to default to the Google Cloud project where the uptime check is to be created:
         
         gcloud config set project PROJECT_ID
         

  2. Create environment variables to store the project ID and project number:
         
         export PROJECT_ID=$(gcloud config get-value core/project)
         

  3. Create the network rule:
         
         gcloud compute firewall-rules create PRIVATE_CHECK_NETWORK_HOPE_RULE \
         --network="PRIVATE_CHECK_NETWORK"  \
         --action=allow   --direction=ingress   --source-ranges="35.199.192.0/19" \
         --rules=tcp   --project="$PROJECT_ID"
         

In the previous command, PRIVATE_CHECK_NETWORK is the network to which this rule is attached while PRIVATE_CHECK_NETWORK_HOPE_RULE is the name of the firewall rule.




For more information about this step, see [Configure the network project](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access#configure-the-network-project).

## Limitations

When using private uptime checks, validation of SSL certificates is disabled, regardless of configuration.

Private uptime checks don't support endpoints that have redirections.

## Troubleshooting

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

## What's next

  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)
  * [Create alerting policies for uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies)
  * [Chart uptime-check metrics](https://docs.cloud.google.com/monitoring/charts/uptime-charts)
  * [Pricing and limits](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
