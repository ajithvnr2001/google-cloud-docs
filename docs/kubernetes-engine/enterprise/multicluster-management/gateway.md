---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/
title: Connect to registered clusters with the Connect gateway \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:14.142237+00:00
---

# Connect to registered clusters with the Connect gateway  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Connect to registered clusters with the Connect gateway Stay organized with collections  Save and categorize content based on your preferences. 

Fleets in Google Cloud are logical groups of Kubernetes clusters and other resources that can be managed together, created by registering clusters to Google Cloud. The Connect gateway builds on the power of fleets to let GKE users connect to and run commands against fleet member clusters in a simple, consistent, and secured way, whether the clusters are on Google Cloud, other public clouds, or on-premises, and makes it easier to automate DevOps processes across all your clusters.

This guide assumes that you are already familiar with some basic fleet concepts, and with registering clusters to a fleet. If not, you can find out more in the [Fleet management overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/fleet-overview), the [Fleet creation overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/fleet-creation), and their linked guides. You should also be familiar with Kubernetes tools and concepts, including `kubectl`, `client-go` (if you want to use the gateway for automation purposes), role-based access control (RBAC), and core Kubernetes Resources.

By default the Connect gateway uses your Google ID to authenticate to clusters, with support for third party identity providers using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), and with group-based authentication support via GKE Identity Service. If you want to find out more about GKE Identity Service, or use it as a standalone third-party authentication option, see [Introducing GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity).

## Why use the Connect gateway?

There are many challenges in managing workloads when your clusters are running in multiple clouds and hybrid environments. Clusters might be running in different virtual private clouds (VPCs) and leverage different identity providers, making connectivity, authentication, and authorization more complicated. Sometimes, just finding out which clusters exist across these environments is difficult.

The Connect gateway makes it easy to:

  * **Discover** what clusters exist (on Google Cloud, on another public cloud, or on-premises) and are registered to your fleet through a simple query.
  * **Connect** to a desired cluster using the same infrastructure we use to display registered GKE clusters in the Google Cloud console.
  * **Authenticate** using the same identities you use with Google Cloud services.
  * **Authorize** consistently across all your clusters registered in a fleet.



The gateway authenticates your Google Cloud identity and provides the connection to the cluster's API server via the Connect service.

You can interact with clusters directly yourself through the gateway using command line tools that accept a `kubeconfig` such as `kubectl`. You can also easily leverage the gateway with your build pipelines and other DevOps automation. You can see an example of how to do this in our [Integrating with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/tutorials/cloud-build-integration) tutorial.

You can also use the Connect service to connect to registered clusters outside Google Cloud with your Google Cloud identity in the Google Cloud console. To do this, follow the instructions in [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console).

## How it works

Here is the flow that a typical user or service (such as a CI/CD pipeline) performs to use the Connect gateway, after appropriate authentication and authorization is configured. For more detailed user instructions, see our [usage guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using).

  1. The user or service discovers clusters by listing fleet Membership resources with the Google Cloud CLI.
         
         gcloud container fleet memberships list
         

  2. The user or service fetches the Connect gateway-specific `kubeconfig` needed to reach their selected cluster by using the Google Cloud CLI.
         
         gcloud container fleet memberships get-credentials membership-name
         

If you're already familiar with using the gcloud CLI with GKE, this is similar to running `gcloud container clusters get-credentials` using your Google Cloud account, letting you (if authorized) access any cluster registered and connected within your project's fleet.

  3. The user or service executes their commands as they normally would with`kubectl` or `client-go`, using the downloaded `kubeconfig` file.

     1. The user/service is authenticated by the Connect gateway, and authorization is checked to ensure they have permission to use the gateway. For GKE clusters, gateway connects to the GKE cluster directly.
     2. For non-GKE Kubernetes clusters, the request is forwarded through the Connect service and Connect Agent to the corresponding Kubernetes API server.
     3. For non-GKE Kubernetes clusters, the Kubernetes API server authorizes the request, which requires that the Connect agent is authorized to impersonate the user or service, and that the user or service is authorized to execute the desired request.

**Note:** Using Chrome Enterprise Premium with IP address restrictions as an attribute, including through geographical restrictions, is not supported by the Connect gateway for GKE clusters.

### Google Group support

In the standard flow described in the previous section, the user's request is authorized based on their individual ID. However, in many cases it's useful to be able to authorize users on the basis of their membership of _Google Groups_. Authorizing based on group membership means you don't have to set up separate authorization for each account, making policies simpler to manage and easier to audit. So, for example, you can easily share cluster access to a team, removing the need to manually add/remove individual users from clusters when they join or leave the team. With some additional setup using [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity), you can configure the Connect gateway to get Google Group membership information for the user.

You can find out more about how this feature works and how to set it up in [Set up the Connect gateway with Google Groups](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).

**Note:** The Connect gateway's Google groups feature is supported for Google Distributed Cloud deployments [on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem) and [on bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/concepts/about-bare-metal) from Distributed Cloud software only version 1.13 onwards.

If you want to use this feature with attached clusters or other GKE environments, contact [Cloud Customer Care](https://docs.cloud.google.com/support) or [the Connect gateway team](mailto:connect-gateway-feedback@google.com).

### Third-party identity support

In addition to working with Google Workspace users and groups, Connect gateway supports authorization using third-party identities, such as Azure Active Directory and Okta. By using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), you can use an external identity provider to authenticate and authorize a workforce—a group of users, such as employees, partners, and contractors—using Identity and Access Management, so that the users can access Google Cloud services like Connect gateway. With some additional setup using [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity), you can configure the Connect gateway to get third-party group membership information for users.

For GKE attached clusters, this feature is available for all [supported Kubernetes cluster versions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/reference/supported-versions).

You can find out more about how this feature works and how to set it up in [Set up the Connect gateway with third-party identities](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-third-party).

If you prefer, you can set up third-party authentication entirely using GKE Identity Service following the instructions in its [documentation](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity).

### Latency

The total latency of a request via the gateway can be divided into two parts: the RTT (Round Trip Time) from the Connect gateway service to the Connect agent, and the request execution time inside the cluster. The extra latency brought by the RTT is p95<500ms and p99<1s. Note that most `kubectl` commands perform a series of several different requests, each requiring a round-trip, before rendering a response to the user.

## What's next?

  * Learn how to [set up the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup) for users and service accounts
  * Learn how to [set up Google Groups support for the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).
  * Learn how to connect to and run commands against a registered cluster [using the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using)
  * See an example of how to use the Connect gateway as part of your DevOps automation in our [Integrating with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/tutorials/cloud-build-integration) tutorial.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
