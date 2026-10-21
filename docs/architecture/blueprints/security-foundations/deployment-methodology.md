---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology/
title: Deployment methodology \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:29.825939+00:00
---

# Deployment methodology  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deployment methodology Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

We recommend that you use declarative infrastructure to deploy your foundation in a consistent and controllable manner. This approach helps enable consistent governance by enforcing policy controls about acceptable resource configurations into your pipelines. The blueprint is deployed using a GitOps flow, with Terraform used to define infrastructure as code (IaC), a Git repository for version control and approval of code, and Cloud Build for CI/CD automation in the deployment pipeline. For an introduction to this concept, see [managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code).

The following sections describe how the deployment pipeline is used to manage resources in your organization.

## Pipeline layers

To separate the teams and technology stack that are responsible for managing different layers of your environment, we recommend a model that uses different pipelines and different personas that are responsible for each layer of the stack.

The following diagram introduces our recommended model for separating a foundation pipeline, infrastructure pipeline, and application pipeline.

![Blueprint pipelines.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-access-patterns.svg)

The diagram introduces the pipeline layers in this model:

  * The _foundation pipeline_ deploys the foundation resources that are used across the platform. We recommend that a single central team is responsible for managing the foundation resources that are consumed by multiple business units and workloads.
  * The _infrastructure pipeline_ deploys projects and infrastructure that are used by workloads, such as VM instances or databases. The blueprint sets up a separate infrastructure pipeline for each business unit, or you might prefer a single infrastructure pipeline used by multiple teams.
  * The _application pipeline_ deploys the artifacts for each workload, such as containers or images. You might have many different application teams with individual application pipelines.



The following sections introduce the usage of each pipeline layer.

### The foundation pipeline

The foundation pipeline deploys the foundation resources. It also sets up the infrastructure pipeline that is used to deploy infrastructure used by workloads.

To create the foundation pipeline, you first clone or fork the terraform-example-foundation to your own Git repository. Follow the steps in the [`0-bootstrap` README file](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/0-bootstrap) to configure your bootstrap folder and resources.

Stage | Description  
---|---  
[`0-bootstrap`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/0-bootstrap) | Bootstraps a Google Cloud organization. This step also configures a CI/CD pipeline for the blueprint code in subsequent stages.

  * The **CICD project** contains the Cloud Build foundation pipeline for deploying resources.
  * The **`seed` project** includes the Cloud Storage buckets that contain the Terraform state of the foundation infrastructure and includes highly privileged service accounts that are used by the foundation pipeline to create resources. The Terraform state is protected through storage [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning). When the CI/CD pipeline runs, it acts as the service accounts that are managed in the `seed` project.

  
  
After you create the foundation pipeline in the `0-bootstrap` stage, the following stages deploy resources on the foundation pipeline. Review the README directions for each stage and implement each stage sequentially.

Stage | Description  
---|---  
[`1-org`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/1-org) | Sets up top-level shared folders, projects for shared services, organization-level logging, and baseline security settings through organization policies.  
[`2-environments`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/2-environments) | Sets up development, non-production, and production environments within the Google Cloud organization that you've created.  
[`3-networks-dual-svpc`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/3-networks-dual-svpc)or[`3-networks-hub-and-spoke`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/3-networks-hub-and-spoke) | Sets up shared VPCs in your chosen topology and the associated network resources.  
  
### The infrastructure pipeline

The infrastructure pipeline deploys the projects and infrastructure (for example, the VM instances and databases) that are used by workloads. The foundation pipeline deploys multiple infrastructure pipelines. This separation between the foundation pipeline and infrastructure pipeline allows for a separation between platform-wide resources and workload-specific resources.

The following diagram describes how the blueprint configures multiple infrastructure pipelines that are intended for use by separate teams.

![Multiple infrastructure pipelines](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/multiple-infrastructure-pipelines.svg)

The diagram describes the following key concepts:

  * Each infrastructure pipeline is used to manage infrastructure resources independently of the foundation resources.
  * Each business unit has its own infrastructure pipeline, managed in a dedicated project in the `common` folder.
  * Each of the infrastructure pipelines has a service account with permission to deploy resources only to the projects that are associated with that business unit. This strategy creates a separation of duties between the privileged service accounts used for the foundation pipeline and those used by each infrastructure pipeline



This approach with multiple infrastructure pipelines is recommended when you have multiple entities inside your organization that have the skills and appetite to manage their infrastructure separately, particularly if they have different requirements such as the types of pipeline validation policy they want to enforce. Alternatively, you might prefer to have a single infrastructure pipeline managed by a single team with consistent validation policies.

In the [terraform-example-foundation](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master), stage 4 configures an infrastructure pipeline, and stage 5 demonstrates an example of using that pipeline to deploy infrastructure resources.

Stage | Description  
---|---  
[`4-projects`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/4-projects) | Sets up a folder structure, projects, and an infrastructure pipeline.  
[`5-app-infra`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/5-app-infra) (optional) | Deploys workload projects with a Compute Engine instance using the infrastructure pipeline as an example.  
  
### The application pipeline

The application pipeline is responsible for deploying application artifacts for each individual workload, such as images or Kubernetes containers that run the business logic of your application. These artifacts are deployed to infrastructure resources that were deployed by your infrastructure pipeline.

The enterprise foundation blueprint sets up your foundation pipeline and infrastructure pipeline, but doesn't deploy an application pipeline. For an example application pipeline, see the [enterprise application blueprint](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/architecture).

## Automating your pipeline with Cloud Build

The blueprint uses Cloud Build to automate CI/CD processes. The following table describes the controls are built into the foundation pipeline and infrastructure pipeline that are deployed by the [terraform-example-foundation](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master) repository. If you are developing your own pipelines using other CI/CD automation tools, we recommend that you apply similar controls.

Control | Description  
---|---  
Separate build configurations to validate code before deploying | The blueprint uses two Cloud Build [build configuration files](https://docs.cloud.google.com/build/docs/build-config-file-schema) for the entire pipeline, and each repository that is associated with a stage has two Cloud Build [triggers](https://docs.cloud.google.com/build/docs/triggers) that are associated with those build configuration files. When code is pushed to a repository branch, the build configuration files are triggered to first run [`cloudbuild-tf-plan.yaml`](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/build/cloudbuild-tf-plan.yaml) which validates your code with policy checks and Terraform plan against that branch, then [`cloudbuild-tf-apply.yaml`](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/build/cloudbuild-tf-apply.yaml) runs `terraform apply` on the outcome of that plan.  
Terraform policy checks | The blueprint includes a set of Open Policy Agent constraints that are enforced by the [policy validation](https://docs.cloud.google.com/docs/terraform/policy-validation) in Google Cloud CLI. These constraints define the acceptable resource configurations that can be deployed by your pipeline. If a build doesn't meet policy in the first build configuration, then the second build configuration doesn't deploy any resources.The [policies enforced in the blueprint](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/policy-library/policies/constraints) are forked from [`GoogleCloudPlatform/policy-library`](https://github.com/GoogleCloudPlatform/policy-library) on GitHub. You can write additional policies for the library to enforce custom policies to meet your requirements.  
Principle of least privilege | The foundation pipeline has a different service account for each stage with an allow policy that grants only the minimum IAM roles for that stage. Each Cloud Build trigger runs as the specific service account for that stage. Using different accounts helps mitigate the risk that modifying one repository could impact the resources that are managed by another repository. To understand the particular IAM roles applied to each service account, see the [`sa.tf`](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/0-bootstrap/sa.tf) Terraform code in the bootstrap stage.  
Cloud Build private pools | The blueprint uses Cloud Build [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview). Private pools let you optionally enforce additional controls such as restricting access to public repositories or running Cloud Build inside a VPC Service Controls perimeter.  
Cloud Build custom builders | The blueprint creates its own [custom builder](https://docs.cloud.google.com/build/docs/cloud-builders#writing_your_own_custom_builder) to run Terraform. For more information, see [`0-bootstrap/Dockerfile`](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/0-bootstrap/Dockerfile). This control enforces that the pipeline consistently runs with a known set of libraries at pinned versions.  
Deployment approval | Optionally, you can add a [manual approval](https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-on-approval) stage to Cloud Build. This approval adds an additional checkpoint after the build is triggered but before it runs so that a privileged user can manually approve the build.  
  
## Branching strategy

We recommend a [persistent branch](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows) strategy for submitting code to your Git system and deploying resources through the foundation pipeline. The following diagram describes the persistent branch strategy.

![The blueprint deployment branching strategy](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-deployment-branching.svg)

The diagram describes three persistent branches in Git (development, non-production, and production) that reflect the corresponding Google Cloud environments. There are also multiple ephemeral feature branches that don't correspond to resources that are deployed in your Google Cloud environments.

We recommend that you enforce a [pull request (PR)](https://git-scm.com/docs/git-request-pull) process into your Git system so that any code that is merged to a persistent branch has an approved PR.

To develop code with this persistent branch strategy, follow these high-level steps:

  1. When you're developing new capabilities or working on a bug fix, create a new branch based off of the development branch. Use a naming convention for your branch that includes the type of change, a ticket number or other identifier, and a human-readable description, like `feature/123456-org-policies`.
  2. When you complete the work in the feature branch, open a PR that targets the development branch.
  3. When you submit the PR, the PR triggers the foundation pipeline to perform `terraform plan` and `terraform validate` to stage and verify the changes.
  4. After you validate the changes to the code, merge the feature or bug fix into the development branch.
  5. The merge process triggers the foundation pipeline to run `terraform apply` to deploy the latest changes in the development branch to the development environment.
  6. Review the changes in the development environment using any manual reviews, functional tests, or end-to-end tests that are relevant to your use case. Then promote changes to the non-production environment by opening a PR that targets the non-production branch and merge your changes.
  7. To deploy resources to the production environment, repeat the same process as step 6: review and validate the deployed resources, open a PR to the production branch, and merge.



## What's next

  * Read about [operations best practices](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
