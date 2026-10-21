---
url: https://docs.cloud.google.com/docs/terraform/iac-overview/
title: Infrastructure as Code on Google Cloud \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:13:24.352477+00:00
---

# Infrastructure as Code on Google Cloud  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/iac-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Infrastructure as Code on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Infrastructure as Code (IaC) is the process of provisioning and managing software application infrastructure using _code_ instead of graphical user interfaces or command-line scripts.

Provisioning application infrastructure typically involves setting up and managing virtual machines, database connections, storage, and other infrastructure elements. Manually managing this infrastructure is time consuming and error prone, especially when managing applications at scale.

IaC lets you define your infrastructure with configuration files, which allow you to build, change, and manage your infrastructure in a safe and repeatable way. You can define resource configurations that you can version, reuse, and share. IaC lets you specify the desired state of your infrastructure. You can then deploy the same configuration multiple times to create reproducible development, test, and production environments.

IaC allows you to treat your infrastructure provisioning and configuration in the same manner as you handle application code. You can store your provisioning configuration logic in source control and you can take advantage of continuous integration and continuous deployment (CI/CD) pipelines.

## Benefits of IaC

Using IaC to set up and manage your application infrastructure is a best practice for a number of common use cases. [Google manages its systems with IaC](https://www.usenix.org/publications/loginonline/prodspec-and-annealing-intent-based-actuation-google-production), and established it as a [standard practice](https://sre.google/workbook/configuration-design/) internally.

IaC offers the following benefits:

  * You can define your infrastructure based on your requirements and reuse the same configuration to create multiple environments consistently.
  * You can automate the creation and management of your cloud resources, including for deployment and test environments.
  * You can treat infrastructure changes like you treat application changes. For example, you can ensure that changes to the configuration are reviewed and automatically validated. Managing production environments through change-controlled processes using IaC is a best practice.
  * You can keep a history of all configuration changes. Changes can be audited and reverted.
  * You can have a single source of truth for your cloud infrastructure.



## IaC tools for Google Cloud

Google Cloud is tightly integrated with many IaC tools. Choose one of the following tools depending on your use case:

  * **Terraform**

In general, to configure and manage Google Cloud infrastructure using code, use the Terraform provider for Google Cloud.

HashiCorp Terraform is an IaC tool that lets you define resources in cloud and on-premises in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle. For more information, see [Overview of Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/terraform-overview).

  * **Infrastructure Manager**

If you're looking to automate the deployment of your Terraform configuration, use Infrastructure Manager (Infra Manager).

Infra Manager automates the deployment and management of Google Cloud infrastructure resources using Terraform. Infra Manager lets you deploy programmatically to Google Cloud, allowing you to use this service rather than maintaining a different toolchain to work with Terraform on Google Cloud. For more information, see [Infra Manager overview](https://docs.cloud.google.com/infrastructure-manager/docs/overview). 

  * **Terraform Cloud and Terraform Enterprise**

If you require full change management with Terraform across your organization, use Terraform Cloud or Terraform Enterprise.

Terraform Cloud is a software as a service (SaaS) application that runs Terraform in a stable, remote environment and securely stores state and secrets. Terraform Cloud also integrates with the Terraform CLI and connects to common version control systems (VCS) like GitHub, GitLab, and Bitbucket. When you connect a Terraform Cloud workspace to a VCS repository, new commits and changes can automatically trigger Terraform plans. Terraform Cloud also offers an API, allowing you to integrate it into existing workflows.

Terraform Enterprise lets you set up a self-hosted distribution of Terraform Cloud. It offers customizable resource limits and is ideal for organizations with strict security and compliance requirements.

For more information, see the [Terraform Editions page in the Hashicorp documentation](https://developer.hashicorp.com/terraform/intro/terraform-editions).

  * **Cloud Development Kit for Terraform**

If you want to generate infrastructure with a general-purpose programming language instead of using Hashicorp Configuration Language (HCL), use Cloud Development Kit for Terraform (CDKTF).

[CDKTF](https://developer.hashicorp.com/terraform/cdktf) lets you configure Terraform using a programming language to define and provision Google Cloud infrastructure and lets you use your existing toolchain for processes like testing and dependency management.

  * **Pulumi**

[Pulumi](https://www.pulumi.com/docs/clouds/gcp/) is another tool you can use to provision infrastructure using programming languages. You can use Google Cloud provider for Pulumi to author infrastructure code using programming languages such as TypeScript, Python, Go, C#, Java or YAML.

  * **Config Controller and Config Connector**

To manage Google Cloud resources through Kubernetes, use Config Controller and Config Connector.

Config Controller and Config Connector let you configure Google Cloud services and resources using Kubernetes tooling. You can use GitOps tools like [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview), and Kubernetes APIs, and you can configure and use platform-engineering primitives such as admission webhooks and operators.

For more information see the [Config Controller overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview) and [Config Connector overview](https://docs.cloud.google.com/config-connector/docs/overview). 

  * **Crossplane**

Another option to manage Google Cloud resources through Kubernetes is by using Crossplane.

Crossplane connects your Kubernetes cluster to external, non-Kubernetes resources, and allows platform teams to build custom Kubernetes APIs to consume those resources. Crossplane acts as a [Kubernetes controller](https://kubernetes.io/docs/concepts/architecture/controller/) to watch the state of the external resources and provide state enforcement. With Crossplane installed in a Kubernetes cluster, users only communicate with Kubernetes. Crossplane manages the communication to external resources like Google Cloud. If something modifies or deletes a resource outside of Kubernetes, Crossplane reverses the change or recreates the deleted resource.

For more information, see the [Crossplane documentation](https://docs.crossplane.io/v1.18/).

  * **Ansible**

If you want to automate provisioning, configuration management, application deployment, orchestration, and other IT processes, use Ansible. For more information, see [Ansible for Google Cloud](https://docs.ansible.com/ansible/latest/collections/google/cloud/).




## What's next

  * Learn more about [Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview)
  * Learn how to [create a basic web server on Compute Engine using Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform)
  * Learn how to [store Terraform state in a Cloud Storage bucket](https://docs.cloud.google.com/docs/terraform/resource-management/store-state)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
