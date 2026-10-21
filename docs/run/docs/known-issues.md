---
url: https://docs.cloud.google.com/run/docs/known-issues/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:27.581139+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/known-issues/




Stay organized with collections  Save and categorize content based on your preferences. 

Known issues in Cloud Run

This page lists known issues, limitations, and unsupported features in Cloud Run.

You can also check for existing issues or open new issues in the [public issue trackers](https://docs.cloud.google.com/support/docs/issue-trackers).

Select your problem category:

DeploymentServingConnectivity and securityURLObservabilityUnsupported services and features

Or filter the known issues:

Category | Issue and workaround  
---|---  
Connectivity and security | 

### SSH connections fail when cold-starting a multi-container Cloud Run service

When an [SSH](https://docs.cloud.google.com/run/docs/troubleshooting/ssh) connection cold-starts a multi-container Cloud Run service with [container startup order](https://docs.cloud.google.com/run/docs/configuring/services/containers#container-ordering) (`container-dependencies`), the request is routed before the container environment is ready. Cloud Run returns an HTTP `500` error and immediately stops the new instance. If you connect using the Google Cloud CLI, the command fails.  To work around this issue, connect using SSH only when an instance is already running. For example, send a request to the service first to start an instance, or configure [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances).   
Deployment | 

### Long-running operations for enabling or disabling SSH on Cloud Run instances might return early

Long-running operations (LROs) for enabling or disabling [SSH](https://docs.cloud.google.com/run/docs/troubleshooting/ssh) on Cloud Run instances might return before the operation is complete.   
Connectivity and security | 

### SSH connections might occasionally fail after enabling or disabling SSH

[SSH](https://docs.cloud.google.com/run/docs/troubleshooting/ssh) connections might occasionally fail, particularly after you enable or disable SSH. If a connection fails, retry the connection.   
Serving | 

### Restart policy `Always` stops Cloud Run instances when a container exits with code 0

When a multi-container Cloud Run instance has its restart policy set to `Always` and any container exits with code 0, Cloud Run stops the instance instead of restarting it.   
Deployment | 

### The `dependsOn` container dependency flag does not work for Cloud Run instances

The `dependsOn` flag for multi-container Cloud Run instances is non-functional. Dependencies specified between containers in multi-container instances are not enforced during container startup.   
Serving | 

### Delayed service recovery after lifting an exceeded spend cap or re-enabling billing

If your project has exceeded its spend cap or has had billing disabled, your Cloud Run resources might experience a delay of up to 30 minutes before they resume serving traffic after you lift the spend cap or re-enable billing. During this period, requests might fail with `429` or `503` errors (with logs indicating "The request was aborted because there was no available instance") or instances may fail to start.  There is no manual workaround. You must wait for up to 30 minutes for your resources to become healthy again.   
Connectivity and security | 

### VPC connectors for worker pools are not production-ready

Serverless VPC Access connectors with Cloud Run worker pools are available in Preview and only supported over Terraform using the the Cloud Run v2 API. There is a lack of support in the Google Cloud console, Google Cloud CLI, YAML, and the Cloud Run v1 API. Furthermore, production readiness components such as monitoring metrics are not supported.   
Observability | 

### Linear increase in ingress-to-region latency metric

You might observe an artificial linear increase in the `run.googleapis.com/request_latency/ingress_to_region` metric, most commonly when you place a service behind an external Application Load Balancer using the HTTP/2 protocol and connections are reused. This occurs because the initial request timestamp might not refresh for subsequent requests on the same connection, while the regional arrival time continues to advance.  This pattern is a metric-reporting anomaly. This issue doesn't represent actual data plane latency, which typically remains low. The metric eventually corrects itself when the connection closes or the counter resets.   
Deployment | 

### High deployment latency in some regions

Creating or updating Cloud Run resources might be slower than expected in some regions like `us-central1`. If deployment latency is an issue in a particular region, Google recommends deploying to another region.   
Deployment | 

### Cloud Run job tasks might be spuriously marked as retried

In some situations, a task can be marked as retried, even when the task succeeded on its first try. Until this issue is resolved, Google recommends keeping the `--max-retries` parameter set to 3 or higher to avoid spurious execution failures.   
Deployment | 

### Volume Mounts are incompatible with Config Connector

If you deploy your Cloud Run service or job with Config Connector, your volume mounts won't be persisted next time you deploy. You may also experience issues using Config Connector with services or jobs that have volume mounts already applied.   
Serving | 

### `HOME` environment variable is set to `/home` in first generation execution environment

Cloud Run first generation execution environment sets the `HOME` environment variable to `/home`. The second generation execution environment sets the HOME variable to the value in `/etc/passwd` for the running user, or falls back to `/home` if the `/etc/passwd` doesn't exist, or if the user can't be found in `/etc/passwd`.   
Serving | 

### You can't mount secrets on `/tmp` in first generation execution environment

If you use [first generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments), you can't mount secrets on `/tmp` directly. However, you can mount secrets on any subdirectory of `/tmp`.   
Serving | 

### High request latency with custom domains when invoking from some regions

Requests to Cloud Run services using custom domains might have a very high latency from some locations. This issue is more pronounced for Cloud Run services in `asia-northeast1` and `us-east4`. If you observe this issue, you can achieve greater performance with Cloud Load Balancing using a [serverless NEG](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless).   
Serving | 

### Sometimes a request might be sent to instances before startup probe results are known

Cloud Run might use the request sent to the service endpoint to start an instance. Before the startup probe results are known, Cloud Run might also assign the request to the instance. If the probe passes, then the instance will process the request at the `receiveTimestamp` listed in the Cloud Run request log. If the probe fails, then Cloud Run logs failure without entering the service's code.   
Connectivity and security | 

### Custom domain mappings require enabled `` URLs

You can only map custom domains for Cloud Run services that have a default `` URL. Until this issue is resolved, if you've [disabled the default `` URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url), we recommend that you enable the default `` URL, map the custom domain, and then disable the default `` URL again.   
Connectivity and security | 

### Serverless VPC Access doesn't support IPv6

You can't use IPv6 when sending traffic through Serverless VPC Access connectors. IPv6 is supported when [Direct VPC egress uses dual-stack subnets](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#set_up_dual-stack_services_and_jobs) or when accessing non-VPC endpoints while `vpc-egress` is set to `private-ranges-only`.   
Connectivity and security | 

### IP addresses not clearly identified when in use by serverless

When you use Direct VPC egress, you can identify IP addresses reserved by Cloud Run that are currently in use, displayed as `None` instead of `Serverless` on the [IP addresses page](https://console.cloud.google.com/networking/addresses/list) in the Google Cloud console.   
URL | 

### Reserved URL paths

You can't use the following URL paths: 

  * Paths starting with `/_ah/`
  * Some paths ending with `z`. To prevent conflicts with reserved paths, we recommend avoiding all paths that end in `z`

  
URL | 

### Some encoded URL characters are decoded

Cloud Run decodes some encoded characters in the Cloud Run services URL before reaching the container instance. For example, `%41` is automatically decoded to `A`.   
Unsupported services and features | 

### Unsupported services

[Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)  
Unsupported services and features | 

### HTTP/2 Push

Cloud Run [supports HTTP/2](https://docs.cloud.google.com/run/docs/configuring/http2), but not [HTTP/2 Server Push](https://en.wikipedia.org/wiki/HTTP/2_Server_Push).   
Unsupported services and features | 

### HTTP methods

Cloud Run doesn't support requests with HTTP methods like `TRACE` and `CONNECT`. As a result, these methods aren't received by services running on Cloud Run.   
Unsupported services and features | 

### Built-in Cloud SQL connections aren't available for Cloud Run jobs running with multiple containers.

The Cloud Run feature of connecting to Cloud SQL instances is not supported for Cloud Run jobs running with multiple containers. Your jobs will continue to run, but Cloud Run won't mount the `/cloudsql` directory inside the containers.   
  
top

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
