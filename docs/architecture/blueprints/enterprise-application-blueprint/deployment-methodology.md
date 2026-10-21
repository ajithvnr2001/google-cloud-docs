---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology/
title: Deployment methodology \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:37.186026+00:00
---

# Deployment methodology  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deployment methodology Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

The enterprise application blueprint is deployed through a series of automated systems and pipelines. Each pipeline deploys a particular aspect of the blueprint. Pipelines provide a controllable, auditable, and repeatable mechanism for building out the blueprint. The following diagram shows the interaction of the various pipelines, repositories, and personas.

![Blueprint pipelines.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-deployment.svg)

The blueprint uses the following pipelines:

  * The _foundation infrastructure pipeline_ (part of the enterprise foundations blueprint) deploys the application factory, the multi-tenant infrastructure pipeline, and the fleet-scope pipeline.
  * The _multi-tenant infrastructure pipeline_ deploys the GKE clusters, and the other managed services that the enterprise application blueprint relies on.
  * The _fleet-scope pipeline_ configures fleet scopes, namespaces, and RBAC roles and bindings.
  * The _application factory_ provides a mechanism to deploy new application pipelines through a templated process.
  * The _application CI/CD pipeline_ provides a CI/CD pipeline to deploy services into GKE clusters.
  * _Config Sync_ deploys and maintains additional Kubernetes configurations, including Policy Controller constraints.



## Repositories, repository contributors, and repository change approvers

The blueprint pipelines are triggered through changes to Git repositories. The following table describes the repositories that are used throughout the blueprint, who contributes to the repository, who approves changes to the repository, which pipeline uses the repository, and the description of what the repository contains.

Repository | Repository contributor | Repository change approver | Pipeline | Description  
---|---|---|---|---  
`infra` | Developer platform developer | Developer platform administrator | Foundation infrastructure pipeline | Repository that contains the code to deploy the multi-tenant infrastructure pipeline, the application, and the fleet-scope pipeline  
`eab-infra` | Developer platform developer | Developer platform administrator | Multi-tenant infrastructure | The Terraform modules that are used by developer platform teams when they create the infrastructure  
`fleet-scope` | Developer platform developer | Developer platform administrator | Fleet-scope | The repository that defines the fleet team scopes and namespaces in the fleet  
`app-factory` | Developer platform developer | Developer platform administrator | Application factory | The code that defines the application repository and references the modules in the `terraform-modules` repository  
`app-template` | Application developer | Application operator | Application factory | The base code that is placed in the `app-code` repository when the repository is first created  
`terraform-modules` | Developer platform developer | Developer platform administrator | Application factoryMulti-tenant infrastructure | The Terraform modules that define the application and the infrastructure  
`app-code` | Application developer | Application operator | Application CI/CD | The application code that is deployed into the GKE clusters  
`config-policy` | Developer platform developer | Developer platform administrator | Config Sync | The policies that are used by the GKE clusters to maintain their configurations  
  
Automated pipelines help build security, auditability, traceability, repeatability, controllability, and compliance into the deployment process. By using different systems that have different permissions and putting different people into different operating groups, you create separation of responsibilities and follow the principle of least privilege.

## Foundation infrastructure pipeline

The [foundation infrastructure](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/5-app-infra) pipeline is described in the enterprise foundations blueprint and is used as a generic entrypoint for further resource deployments. The following table describes the components that the pipeline creates.

Component | Description  
---|---  
Multi-tenant infrastructure pipeline | Creates the shared infrastructure that is used by all tenants of the developer platform.  
Fleet-scope pipeline | Creates namespaces and RBAC role bindings.  
Application factory | Creates the application CI/CD pipelines that are used to deploy the services.  
  
## Multi-tenant infrastructure pipeline

The multi-tenant infrastructure infrastructure pipeline deploys fleets, GKE clusters, and related shared resources. The following diagram shows the components of the multi-tenant infrastructure pipeline.

![Infrastructure pipeline components.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-infra-pipeline.svg)

The following table describes the components that the multi-tenant infrastructure pipeline builds.

Component | Description  
---|---  
GKE clusters | Provides hosting for the services of the containerized application.  
Policy Controller | Provides policies that help ensure the proper configuration of the GKE clusters and services.  
Config Sync | Applies the Policy Controller policies to clusters and maintains consistant appplication of the policies.  
[Cloud Key Management Service (Cloud KMS)](https://cloud.google.com/security/products/security-key-management) key | Creates the encryption key that is based on the customer-managed encryption key (CMEK) for GKE, AlloyDB for PostgreSQL, and Secret Manager.  
Secret Manager secret | Provides a secret store for the [RSA key pair](https://github.com/GoogleCloudPlatform/bank-of-anthos/tree/ff95e6d82afb38cccab80cfe2453f2d600bf7453/extras/jwt) that's used for user authentication with [JSON Web Tokens (JWT)](https://docs.cloud.google.com/docs/authentication/use-cases#jwts).  
[Cloud Armor](https://docs.cloud.google.com/armor) security policy | Provides the policy that's used by the Cloud Armor web-application firewall.  
  
## Fleet-scope pipeline

The fleet-scope pipeline is responsible for configuring the namespaces and RBAC bindings in the fleet's GKE clusters. The following table describes the components that the fleet-scope pipeline builds.

Component | Description  
---|---  
[Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) | Defines the logical clusters within the physical cluster.  
[RBAC (roles and bindings)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#:~:text=A%20role%20binding%20grants%20the,grants%20that%20access%20cluster%2Dwide.) | Defines the authorization that a Kubernetes service account has at the cluster level or namespace level.  
  
## Application factory

The application factory is deployed by the foundation infrastructure pipeline and is used to create infrastructure for each new application. This infrastructure includes a Google Cloud project which holds the application CI/CD pipeline.

As engineering organizations scale, the application team can onboard new applications using the application factory. Scaling enables growth by adding discrete application CI/CD pipelines and supporting the infrastructure for deploying new applications within the multi-tenant architecture. The following diagram shows the application factory.

![Application factory components.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-app-factory.svg)

The application factory has the following components:

  * **Application factory repository:** A Git repository that stores the declarative application definition.
  * **Pipelines to create applications:** Pipelines that require Cloud Build to complete the following: 
    * Create a declarative application definition and store it in the application catalog.
    * Apply the declarative application definition to create the application resources.
  * **Starter application template repository:** Templates for creating a simple application (for example, a Python, Golang, or Java microservice).
  * **Shared modules:** Terraform modules that are created with standard practices and that are used for multiple purposes, including application onboarding and deployment.



The following table lists the components that the application factory creates for each application.

Component | Description  
---|---  
Application source code repository | Contains source code and related configuration used for building and deploying a specific application.  
Application CI/CD pipeline | A Cloud Build based pipeline that is used to connect to the source code repository and provides a CI/CD pipeline for deploying application services.  
  
## Application CI/CD pipeline

The application CI/CD pipeline enables automated build and deployment of container-based applications. The pipeline consists of [continuous integration (CI)](https://en.wikipedia.org/wiki/Continuous_integration) and [continuous deployment (CD)](https://en.wikipedia.org/wiki/Continuous_deployment) steps. The pipeline architecture is based on the [Secure CI/CD blueprint](http://github.com/googlecloudplatform/terraform-google-secure-cicd).

The application CI/CD pipeline uses immutable container images across your environments. Immutable container images help ensure that the same image is deployed across all environments and isn't modified while the container is running. If you must update the application code or apply a patch, you build a new image and redeploy it. The use of immutable container images requires you to [externalize your container configuration](https://kubernetes.io/docs/tutorials/configuration/configure-java-microservice/configure-java-microservice/) so that configuration information is read during run time.

To reach GKE clusters over a private network path and manage `kubeconfig` authentication, the application CI/CD pipeline interacts with the GKE clusters through the Connect gateway. The pipeline also uses [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) for the CI/CD environment.

Each application source code repository includes Kubernetes configurations. These configurations enable applications to successfully run as Kubernetes services on GKE. The following table describes the types of Kubernetes configurations that the application CI/CD pipeline applies.

Component | Description  
---|---  
[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Defines a scaled set of pods (containers).  
[Service](https://kubernetes.io/docs/concepts/services-networking/service/) | Makes a deployment reachable over the cluster network.  
[Virtual service](https://istio.io/latest/docs/reference/config/networking/virtual-service/) | Makes a service part of the service mesh.  
[Destination rule](https://istio.io/latest/docs/reference/config/networking/destination-rule/) | Defines how peers on the service mesh should reach a virtual service. Used in the blueprint to configure locality load balancing for east-west traffic.  
[Authorization policy](https://istio.io/latest/docs/reference/config/security/authorization-policy/) | Sets access control between workloads in the service mesh.  
[Kubernetes service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) | Defines the identity that's used by a Kubernetes service. [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) defines the Google Cloud service account that's used to access Google Cloud resources.  
[Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway) | Allows external ingress traffic to reach a service. The gateway is only required by deployments that receive external traffic.  
[GCPBackendPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources) | Configure SSL, Cloud Armor, session affinity, and connection draining for deployments that receive external traffic. GCPBackendPolicy is used only by deployments that receive external traffic.  
[PodMonitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) | Configures collection of Prometheus metrics exported by an application.  
  
### Continuous integration

The following diagram shows the continuous integration process.

![Blueprint continuous integration process.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-cicd-ci.svg)

The process is the following:

  1. A developer commits application code to the application source repository. This operation [triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) Cloud Build to begin the integration pipeline.
  2. Cloud Build creates a [container image](https://docs.cloud.google.com/build/docs/building/build-containers), [pushes](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) the container image to Artifact Registry, and creates an [image digest](https://docs.cloud.google.com/solutions/using-container-images).
  3. Cloud Build performs automated tests for the application. Depending on the application language, different testing packages may be performed.
  4. Cloud Build performs the following scans on the container image: 
     1. Cloud Build analyzes the container using the [Container Structure Tests](https://github.com/GoogleContainerTools/container-structure-test) framework. This framework performs command tests, file existence tests, file content tests, and metadata tests.
     2. Cloud Build uses [vulnerability scanning](https://docs.cloud.google.com/artifact-analysis/docs/vulnerability-scanning) to identify any vulnerabilities in the container image against a vulnerability database that's maintained by Google Cloud.
  5. Cloud Build approves the image to continue in the pipeline after successful scan results.
  6. [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) signs the image. Binary Authorization is a service on Google Cloud that provides software supply-chain security for container-based applications by using [policies](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies), [rules](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#rules), [notes](https://docs.cloud.google.com/container-registry/docs/container-analysis#note), [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations), [attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors), and [signers](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#signers). At deployment time, the Binary Authorization policy enforcer helps ensure the provenance of the container before allowing the container to deploy.
  7. Cloud Build creates a release in Cloud Deploy to begin the deployment process.



To see the security information for a build, go to the [Security insights panel](https://docs.cloud.google.com/build/docs/view-build-security-insights#view_the_security_insights_side_panel). These insights include [vulnerabilities](https://docs.cloud.google.com/build/docs/view-build-security-insights#vulnerabilities) that were detected using Artifact Analysis, and the build's [level of security assurance](https://docs.cloud.google.com/build/docs/view-build-security-insights#slsa_level) denoted by SLSA guidelines.

### Continuous deployment

The following diagram shows the continuous deployment process.

![Blueprint continuous deployment process.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-cicd-cd.svg)

The process is the following:

  1. At the end of the build process, the application CI/CD pipeline creates a new [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) release to launch the newly built container images progressively to each environment.
  2. Cloud Deploy initiates a rollout to the first environment of the deployment pipeline, which is usually development. Each deployment stage is configured to require manual approval.
  3. The Cloud Deploy pipelines uses sequential deployment to deploy images to each cluster in an environment in order.
  4. At the end of each deployment stage, Cloud Deploy [verifies](https://docs.cloud.google.com/deploy/docs/verify-deployment) the functionality of the deployed containers. These steps are configurable within the [Skaffold](https://skaffold.dev/) configuration for the applications.



## Deploying a new application

The following diagram shows how the application factory and application CI/CD pipeline work together to create and deploy a new application.

![Process for deploying an application.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-app-deployment.svg)

The process for defining a new application is the following:

  1. An application operator defines a new application within their tenant by executing a Cloud Build trigger to generate the application definition.
  2. The trigger adds a new entry for the application in Terraform and commits the change to the application factory repository.
  3. The committed change triggers the creation of application-specific repositories and projects.
  4. Cloud Build completes the following: 
     1. Creates two new Git repositories to host the application's source code and IaC.
     2. Pushes the Kubernetes manifests for network policies, and Workload Identity Federation for GKE to the Configuration management repository.
     3. Creates the application's CI/CD project and the Cloud Build IaC trigger.
  5. The Cloud Build IaC trigger for the application creates the application CI/CD pipeline and the Artifact Registry repository in the application's CI/CD project.
  6. Config Sync deploys the network policies and Workload Identity Federation for GKE configurations to the multi-tenant GKE clusters.
  7. The fleet scope creation pipeline creates the fleet scope and namespace for the application on multi-tenant GKE clusters.
  8. The application's CI/CD pipeline performs the initial deployment of the application to the GKE clusters.
  9. Optionally, the application team uses the Cloud Build IaC trigger to deploy projects and additional resources (for example, databases and other managed services) to dedicated single-tenant projects, one for each environment.



## GKE configuration and policy management

In the blueprint, developer platform administrators use [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) to create cluster-level configurations in each environment. Config Sync connects to a Git repository which serves as the source of truth for the chosen state of the cluster configuration. Config Sync continuously monitors the actual state of the configuration in the clusters and reconciles any discrepancies by applying updates to ensure adherence to the chosen state, despite manual changes. Configs are applied to the environments (development, non-production, and production) by using a [branching strategy](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/safe-rollouts-with-config-sync#use_git_branches) on the repository.

In this blueprint, Config Sync applies [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) constraints. These configurations define security and compliance controls as defined by developer platform administrators for the organization. This blueprint relies on other pipelines to apply other configurations: the application CI/CD pipelines apply application-specific configuration, and the fleet-scope pipeline creates namespaces and associated role bindings.

## What's next

  * Read about the [Cymbal Bank application architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/cymbal-bank) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
