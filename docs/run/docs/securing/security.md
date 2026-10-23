---
url: https://docs.cloud.google.com/run/docs/securing/security/
title: Security design overview \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:15.248725+00:00
---

# Security design overview  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Security design overview Stay organized with collections  Save and categorize content based on your preferences. 

Learn how Cloud Run implements security best practices to protect your data and explore how to use these features to meet your security requirements. 

## Architecture

Cloud Run runs on top of [Borg](https://research.google/pubs/pub43438/) in the same environment where Google deploys billions of containers a week, hosting some of the biggest sites in the world, including Gmail and YouTube. Because Cloud Run components share the same infrastructure, they are built to the same security standards as other Google services.

To learn more about our approach to security, read the [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper) whitepaper.

The Cloud Run architecture contains many different infrastructure components. The following diagram shows how these components respond to requests to your service and Cloud Run Admin API calls:

[ ![Illusatration of Cloud Run infrastructure components](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-arch.svg)](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-arch.svg) **Figure 1.** Diagram of Cloud Run infrastructure components.

### Requests to your service

When a request is made to your Cloud Run service either through your custom domain or directly to your `run.app` URL, the request is handled by the following components:

  * **Google Front End (GFE):** the Google [global infrastructure service](https://docs.cloud.google.com/docs/security/infrastructure/design#google_front_end_service) that terminates TLS connections and applies protections against [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) attacks when you make a request to the `run.app` URL. Cloud Run is a regional service, so when a request is accessed via the `run.app` URL, the GFE forwards the request to Cloud Run through an encrypted channel in the appropriate region.
  * **[Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview):** when you set up Cloud Load Balancing to handle your custom domain, it includes the GFE functionality mentioned previously. You can also configure Google Cloud load balancers to perform additional functions, such as traffic management and access control.
  * **HTTP proxy:** a zonal component that load balances incoming HTTP requests to the instances of your sandboxed applications.
  * **Scheduler:** selects the app servers to host instances of your sandboxed applications.
  * **App server:** a zonal and multi-tenant compute node that creates and manages the sandboxes that run the instances of each application's container.
  * **Sandbox:** isolates user code from the system and other customers. Learn more in the following Compute security section.
  * **Storage:** exposes a file server interface for container images imported from [supported container registries](https://docs.cloud.google.com/run/docs/deploying#images).
  * **Metadata server:** provides sandbox-specific credentials and metadata.
  * **Outbound networking:** manages outbound traffic initiated by the sandbox.



### Cloud Run Admin API calls

When a request is made to the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/rest), the request is handled by the following components:

  * **Google Front End (GFE):** the Google global infrastructure service that terminates TLS connections and applies protections against DoS attacks.
  * **Control plane:** validates and writes your application configurations to storage.
  * **Config storage:** stores application configurations in [Spanner](https://cloud.google.com/spanner) and [Bigtable](https://docs.cloud.google.com/bigtable) for access by other components, such as app server, scheduler, and networking elements.



## Compute security

An instance is defined as the unit where your configured containers run. When you [deploy a single container image](https://docs.cloud.google.com/run/docs/deploying), each instance runs a single container. When you [deploy multiple container images (sidecars)](https://docs.cloud.google.com/run/docs/deploying#sidecars), each instance contains the set of containers.

Each Cloud Run instance is protected (sandboxed) from every other by a boundary enforced by a virtual machine monitor (VMM). While we do provide some degree of container boundary enforcement, it's not as strong as the instance boundary around your container or containers.

### Execution environments

Cloud Run components run on Google's container-management system, Borg. Cloud Run offers two [execution environments](https://docs.cloud.google.com/run/docs/about-execution-environments):

  * **First generation:** Based on the [gVisor](https://gvisor.dev/) container security platform, this option has a small codebase, which provides a smaller attack surface. Every change is security-reviewed and most changes are written in a memory-safe manner. Further hardening is achieved by using [Secure Computing Mode (seccomp)](https://en.wikipedia.org/wiki/Seccomp#seccomp-bpf) system call filtering.

  * **Second generation:** Based on Linux microVMs, this option provides more compatibility and performance for custom workloads. Further hardening is achieved by using seccomp system call filtering and [Sandbox2](https://developers.google.com/code-sandboxing/sandbox2/explained) Linux namespaces.




Both of these execution environments use two layers of sandboxing consisting of a hardware-backed layer equivalent to individual VMs (x86 virtualization) and a software kernel layer, as shown in the following diagram:

[ ![In both execution
      environments, the user container is isolated from other workloads through
      two layers of sandboxing.](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-compute.svg)](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-compute.svg) **Figure 2.** In both execution environments, the user container is isolated from other workloads through two layers of sandboxing. 

If your service makes use of third-party infrastructure for securing containers, use the second generation execution environment.

### Cloud Run Threat Detection

To continuously monitor the state of your Cloud Run resources for detecting common runtime attacks, such as suspicious binaries or malicious code, use [Cloud Run Threat Detection](https://docs.cloud.google.com/run/docs/securing/cloud-run-threat-detection).

## Data encryption and storage

Cloud Run instances are stateless. Terminating an instance discards its state. Therefore, all new instances are started from a clean slate.

If you have stateful data, you can manage your data in the following ways:

  * Store stateful data in external storage services, such as [Cloud SQL](https://cloud.google.com/sql) or [Memorystore](https://cloud.google.com/memorystore).
  * Integrate with [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) for [secure storage](https://docs.cloud.google.com/run/docs/configuring/services/secrets) of sensitive data such as API keys and passwords.



Beyond that, Cloud Run integrates with many other Google Cloud systems to manage and access your data in the following ways:

  * Service configuration data is stored in [Spanner](https://cloud.google.com/spanner) and [Bigtable](https://docs.cloud.google.com/bigtable).
  * Monitoring and logging data is sent to [Google Cloud Observability](https://cloud.google.com/products/observability).
  * Container images are imported from [supported container registries](https://docs.cloud.google.com/run/docs/deploying#images) and can be optionally encrypted by using [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/run/docs/securing/using-cmek).



Across Google Cloud, all your data is [encrypted at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

Cloud Run complies with Google Cloud-wide initiatives for data protection and transparency, including [access transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services) and [data residency](https://cloud.google.com/terms/data-residency).

## Network security

Cloud Run and all other Google Cloud services [encrypt all traffic in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit). You can incorporate both egress and ingress controls into your Cloud Run services or jobs to add an additional layer of restriction. Organization administrators can also enforce egress and ingress by setting [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints).

### Egress (outbound) traffic

Egress traffic that exits from Cloud Run is treated as transport layer 4 (TCP and UDP).

By default, egress traffic takes one of the following paths when exiting Cloud Run:

  * **Target destination is in VPC network:** traffic travels to a VPC network or Shared VPC network in your project by using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) or a [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) connector. The connector is a regional resource that sits directly on the VPC network.
  * **Target destination is not in VPC network:** traffic routes directly to the target destination within Google's network or the public internet.

[ ![Cloud Run networking path to VPC and non-VPC networks](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-egress-connector.svg)](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-egress-connector.svg) **Figure 3.** Egress traffic can travel to a VPC or to a non-VPC network using Direct VPC egress or a connector.

#### Controlling egress

For additional control over egress traffic, use the [VPC egress setting](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress) to route all your traffic to your VPC network by using Direct VPC egress or connectors.

Once it's on the VPC network, you can use VPC tools to manage the traffic, for example:

  * Apply [firewall rules](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#restrict-access) to your service's traffic, or change the way your traffic is [routed](https://docs.cloud.google.com/vpc/docs/routes).
  * Enable [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) to inspect the traffic.



Organization administrators can also enforce egress by setting the [Allowed VPC egress settings (Cloud Run)](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) list constraint.

### Ingress (inbound) traffic

In contrast to egress, Cloud Run's ingress traffic is at application layer 7 (HTTP).

**Note:** Content in this section only applies to Cloud Run services. Cloud Run jobs do not have ingress.

Cloud Run accepts incoming ingress traffic from the following sources:

  * **Public internet:** requests are routed directly from public sources to your Cloud Run services with the option of routing traffic through an [external HTTP(S) load balancer](https://docs.cloud.google.com/load-balancing/docs/https).

  * **VPC network:** you can route traffic from a VPC network to Cloud Run services by using [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access), [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect), or an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless). Traffic of this type always stays within Google's network.

  * **Google Cloud services:** traffic travels directly to Cloud Run from other Google Cloud services, such as BigQuery or even Cloud Run itself. In some cases, you can also configure these services to route through a VPC network. Traffic of this type always stays within Google's network.


[ ![Diagram of Cloud Run infrastructure components](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-ingress.svg)](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-ingress.svg) **Figure 4.** Layer 7 HTTP network ingress (inbound) traffic to Cloud Run.

Cloud Run's network security model includes the following ingress traffic properties:

  * **Direct traffic to the default`run.app` URL:** the `run.app` URL always requires HTTPS for traffic to enter Cloud Run. Google's frontend-serving infrastructure terminates TLS and then forwards the traffic to Cloud Run and to your container through an encrypted channel. You can [disable the default URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url).
  * **Traffic to a custom domain associated with your Google Cloud load balancer:** For HTTPS traffic, Google Cloud internal and external load balancers terminate TLS and forward traffic to Cloud Run and your container through an encrypted channel. Google Cloud load balancers also let you apply additional security features such as [IAP](https://docs.cloud.google.com/iap), [Cloud Armor](https://cloud.google.com/security/products/armor), and [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts).



For more information about configuring VPC network traffic to Cloud Run, see [Receive requests from VPC networks](https://docs.cloud.google.com/run/docs/securing/private-networking#from-vpc).

#### Controlling ingress

Cloud Run [ingress controls](https://docs.cloud.google.com/run/docs/securing/ingress) manage what traffic enters Cloud Run to ensure that traffic comes only from trusted sources.

For Cloud Run services that serve only internal clients, you can configure the "internal" setting so that only traffic from the following internal sources can enter Cloud Run:

  * VPC networks in your project or [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls) perimeter, including Cloud Run services that route all their traffic through the VPC network.
  * The Shared VPC network that the Cloud Run service is attached to.
  * Some Google Cloud services, such as BigQuery, that are in your project or VPC Service Controls perimeter.
  * Traffic from on-premises clients that traverse your VPC network to reach Cloud Run.

**Note:** If your Cloud Run service is a backend to an external load balancer, use the "internal + load balancing" setting instead.

If you are using an external or internal load balancer, you can [disable the default `run.app` URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url).

Organization administrators can also enforce ingress by setting [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints).

For more information about controlling ingress, see [Restricting ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress).

## Access control

Access controls are used to restrict who has access to your Cloud Run services and jobs.

### Who can manage your service or job

To control who manages your Cloud Run service or job, Cloud Run uses [IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) for authorizing users and service accounts.

### What your service or job can access

To control what your Cloud Run workloads can reach via the network, you can force all traffic through the VPC network and apply VPC firewall rules, as previously described in the Network security section.

If you're using Direct VPC egress, you can attach network tags to the Cloud Run resource and reference the network tags in the firewall rule. If you're using Serverless VPC Access, you can apply firewall rules to the connector instances.

Use IAM to control what resources your Cloud Run service or job can access. Services and jobs use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) by default. For sensitive workloads, use a dedicated service account so that you can grant only the permissions that the workload needs to do its work. Learn more about [using per-service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) to manage a dedicated service account. For information about how Cloud Run reminds users to create a dedicated service account, see [Secure Cloud Run services with Recommender](https://docs.cloud.google.com/run/docs/recommender).

### Who can invoke your service or execute your job

Cloud Run provides several different options to control who invokes your service or executes your job.

#### Ingress controls

For managing ingress of Cloud Run services at the networking level, see Controlling ingress in the previous section.

Cloud Run jobs don't serve requests and therefore don't use ingress controls when executing jobs.

#### IAM for your service

Use the [`run.routes.invoke`](https://docs.cloud.google.com/run/docs/reference/iam/permissions#services) permission to configure who can access your Cloud Run service in the following ways:

  * Grant the permission to select service accounts or groups to allow access to the service. All requests must have an HTTP Authorization header containing an OpenID Connect ID token signed by Google for one of the authorized service accounts.

  * Select **Allow public access** to [disable the Cloud Run Invoker IAM check](https://docs.cloud.google.com/run/docs/securing/managing-access#disable_invoker) and allow unauthenticated access. Cloud Run performs an IAM check on every request when the Cloud Run Invoker IAM check is enabled.




To ensure that only members of your organization can invoke a Cloud Run service, an organization administrator can set the [Domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) organization policy. Organization administrators can also opt out of specific Cloud Run services. Select **Allow public access** when domain restricted sharing is enabled to create public URLs.

Learn more about [common use cases for authentication](https://docs.cloud.google.com/run/docs/authenticating/overview) and how Cloud Run [uses access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access).

#### Enable Identity-Aware Proxy for a Cloud Run service

Enable IAP on Cloud Run to secure traffic to a Cloud Run service by routing it to IAP for authentication. You can also use Workforce Identity Federation with IAP on Cloud Run. Learn how to [Configure Identity-Aware Proxy for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run).

#### Load balancer security features for your service

If you configured a Cloud Run service to be a backend to a Google Cloud load balancer, secure this path using the following methods:

  * Block direct traffic from the public internet to the `run.app` URL by [setting ingress](https://docs.cloud.google.com/run/docs/securing/ingress#settings) to one of the internal options.
  * [Disable the default `run.app` URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url).
  * Optionally, you can enable security features on the Google Cloud load balancer, such as [Cloud Armor](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#serverless), [IAP](https://docs.cloud.google.com/iap), and [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts).



#### IAM for your job

Use the [`run.jobs.run`](https://docs.cloud.google.com/run/docs/reference/iam/permissions#jobs) permission to configure who can execute your Cloud Run job in the following ways:

  * Grant the permission to select service accounts or groups to allow access to the job. If the job is triggered by another service, such as [Cloud Scheduler](https://docs.cloud.google.com/scheduler), the service account that's used must have the `run.jobs.run` permission on the job.

  * Grant the permission to the logged-in user to execute a job from the Google Cloud console. If the job is triggered by another service, such as [Cloud Scheduler](https://docs.cloud.google.com/scheduler), the service account or group that's used must have the `run.jobs.run` permission on the job.




To ensure that only members of your organization can execute a Cloud Run job, an organization administrator can set the [Domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) constraint. Organization administrators can also opt out specific Cloud Run jobs.

### VPC Service Controls

Your Cloud Run services can be part of a [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls) perimeter so that you can use VPC Service Controls to gate access and mitigate exfiltration risk. Learn more about [using VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls).

## Supply chain security

### Google Cloud's buildpacks-managed base images

Services that are deployed [from source code](https://docs.cloud.google.com/run/docs/deploying-source-code) using [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) are built using Google-provided base images. Google maintains these base images and provides routine patches on a weekly basis. In emergency situations involving critical security vulnerabilities, we're able to make patches available within hours.

### Cloud Run internal supply chain security

Because it runs on Borg, Cloud Run implements all of the same supply chain security that's standard across all Google services, such as Gmail and YouTube. Read more about Google internal supply chain practices in the [BeyondProd](https://docs.cloud.google.com/docs/security/beyondprod) and [Binary Authorization for Borg](https://docs.cloud.google.com/docs/security/binary-authorization-for-borg) whitepapers.

### Binary Authorization

Cloud Run has built-in support for [Binary Authorization](https://docs.cloud.google.com/binary-authorization) to ensure that only trusted container images are deployed on Cloud Run. Read more at [Set up overview for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/overview).

### Software supply chain security insights

Cloud Administrators can view security information about the supply chain of their deployed containers directly from a panel in the Google Cloud console. Read more at [View software supply chain security insights](https://docs.cloud.google.com/run/docs/securing/view-security-insights).

## Execution environment security

**Preview — Cloud Run automatic base image updates**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run supports automatic base image updates with compatible containers. Security updates are applied with zero downtime on the service by executing a rebase on the container base image.

Services that are [deployed from source](https://docs.cloud.google.com/run/docs/deploying-source-code), which include Cloud Run utilize Google Cloud's buildpacks and are compatible with automatic security updates.

Services with automatic security updates enabled are deployed using Google-provided base images. Google maintains these base images and provides routine patches after a period of stability testing. In emergency situations involving critical security vulnerabilities, we're able to make patches available within hours.

To learn more about execution environment security updates, see how to [configure security updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates).

## What's next

  * For an end-to-end walkthrough of how to set up networking, see the Cloud Run [Serverless Networking Guide](https://services.google.com/fh/files/misc/serverless_networking_guide.pdf).
  * Learn how to [detect threats using Cloud Run Threat Detection](https://docs.cloud.google.com/run/docs/securing/cloud-run-threat-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
