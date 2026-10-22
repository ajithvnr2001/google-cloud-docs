---
url: https://docs.cloud.google.com/appengine/docs/flexible/known-issues/
title: Known issues in the App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:49.853870+00:00
---

# Known issues in the App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/flexible/resources)



Send feedback 

#  Known issues in the App Engine flexible environment Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

For a full list of known issues or to report a new issue, see the [issue tracker](https://issuetracker.google.com/issues?q=componentid:187250%2B).

  * After you deploy your application with `gcloud app deploy`, you might need to wait 1-2 minutes before your application starts serving at `https://PROJECT_ID.REGION_ID.r.appspot.com`. Until then, you might see HTTP `503` errors.

App Engine often logs these errors as `backend_timeout` or `failed_to_pick_backend` in the global external Application Load Balancer logs. The global external Application Load Balancer sends requests to a service in the App Engine flexible environment regardless of the health of individual instances. After you deploy a new version, the global external Application Load Balancer takes time to update its configuration with the new backend instances. During this transition, the availability of backend services is inconsistent. When migrating traffic to the new version, the global external Application Load Balancer might try to send traffic to instances that aren't fully ready to receive requests, resulting in `503` errors. This might also result in `502` errors, particularly when using a [classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs).

  * If there is an organization policy on your project that restricts access to external IPs, you won't be able to deploy an App Engine flexible environment app with external IP addresses. For example, the organization policy could look as follows:

    * The effective policy for `constraints/compute.vmExternalIpAccess` is set to `DENY_ALL`.
    * The effective policy for `constraints/compute.vmExternalIpAccess` is set to allow only specific VM instances.
    * The effective policy for `constraints/compute.requireOsConfig` is disabled for the project to prevent metadata updates.

These constraints are not automatically detected, and deployments might time out and fail. You can check the organization policy for your project by running the command `gcloud beta resource-manager org-policies describe compute.vmExternalIpAccess --project=my-project --effective`. You can also [override the organizational policy for a specific project](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#override_boolean_policy).

However, even with such organization policies set, you can deploy a private App Engine flexible environment app that uses only its internal IP address.

  * After you deploy a new version of an existing service in the App Engine flexible environment with `gcloud app deploy`, the "Count/sec" metric shown in the "Summary" graph of the App Engine dashboard may decrease significantly. The metric will gradually return to the expected request count over the next 5-10 minutes.

This does not mean that your application is serving fewer requests. When you deploy a new version of your application, there is a delay between the time the new version is ready to serve requests and the time that the metrics for new instances become available.

To ensure that this metric is unaffected by a new version deployment:

    1. Deploy your new version with [`gcloud app deploy --no-promote`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy).
    2. Wait 15 minutes after the deployment completes.
    3. [Migrate traffic to the new version](https://docs.cloud.google.com/appengine/docs/standard/migrating-traffic#migrating_traffic_to_a_new_version).

If you deploy with `--no-promote` but allocate any amount of traffic to the new version before the 15 minute window after the deployment completes, this metric may be impacted.

  * It is not possible in the App Engine flexible environment to configure `app.yaml` so that your app automatically redirects requests to always use HTTPS. This differs from the App Engine standard environment, where you can use the `secure` setting.

As an alternative, you can handle the redirect inside your application code by parsing the value of [`X-Forwarded-Proto` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Proto). You can also encourage clients to use the [`Strict-Transport-Security` header](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-handled#http_strict_transport_security).

  * If you assign a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/user-managed-service-accounts) to an App Engine flexible environment version, your project may be billed for `agent.googleapis.com`-prefixed metrics. Normally, these agent metrics are not charged to your project. We recommend that you continue to use the App Engine default service account until [this issue](https://issuetracker.google.com/issues/201321074) is resolved.

  * You can't establish an SSH connection to a VM Instance using IAP.

  * The App Engine flexible environment has a maximum request timeout of 60 minutes. However, if your application is configured to use a VPC network with strict egress firewall rules (such as denying egress to `0.0.0.0`), you might experience connection drops for requests that take longer than 10 minutes.

This occurs because the underlying VPC Firewall connection tracking entry expires after 10 minutes of inactivity. When the App Engine flexible environment instance attempts to send a response after 10 minutes of inactivity on the connection, the firewall drops the egress packets.

To work around this limitation, follow these steps:

    * To use strict egress deny rules, configure specific egress allow rules to permit traffic to the Google Front End (GFE) IP ranges used by the classic Application Load Balancer, such as `130.211.0.0/22` and `35.191.0.0/16`. For more information, see [Firewall rules](https://docs.cloud.google.com/load-balancing/docs/firewall-rules).
    * Migrate to the [envoy-based application load balancer](https://docs.cloud.google.com/load-balancing/docs/https). This allows you to configure egress allow rules targeting your own [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) range, which is often recommended by security teams instead of external GFE IP ranges.



## Unexpected reduction in number of instances

  * In rare events, your application could see an unexpected reduction in the number of instances due to zone failures, or if an entire group of instances stop responding. To prevent this, Google recommends overprovisioning your application to prevent your system from dropping below the minimum number of instances. You can set your App Engine flexible environment application's [min_num_instances](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#min_num_instances) size when deploying it. Some events that may affect App Engine flexible environment minimum number of instances are:

    1. Rolling out [updates to flexible environment instances](https://docs.cloud.google.com/appengine/docs/flexible#features)
    2. Zonal failure (Stockout issues, such as when your region is at capacity for your selected CPU, etc.)

App Engine flexible environment uses 3 zones to distribute your instances and in such a configuration, we [recommend](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#estimating_instance_group_size) provisioning 50% more instances than required.




## Inconsistent Cloud Load Balancing metrics

The App Engine flexible environment dashboard displays all metrics only for requests routed through a flexible environment-managed backend. If you use App Engine flexible environment with Cloud Load Balancing, certain metrics in the App Engine [metrics table](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-appengine) are reported as metrics from the [`loadbalancing`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-loadbalancing) table instead. For more information, see [HTTP(S) Load Balancing logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring).

## `InterruptedException` in runtimes using JVM during health check failure

When a health check fails, the VM is shutdown. As a symptom of the app container becoming unhealthy, the JVM responds with `InterruptedException` and `NullPointerException` errors. A handler can [respond to the `SIGTERM` signal](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#application_shutdown) sent by the container during shutdown, to perform any necessary clean-up or debugging actions, to prevent exceptions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
