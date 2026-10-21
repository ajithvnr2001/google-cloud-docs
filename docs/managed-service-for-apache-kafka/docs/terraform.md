---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/terraform/
title: Provision Managed Service for Apache Kafka resources with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:09:05.871453+00:00
---

# Provision Managed Service for Apache Kafka resources with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/apis)



Send feedback 

#  Provision Managed Service for Apache Kafka resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Managed Service for Apache Kafka.

This page introduces you to using Terraform with Managed Service for Apache Kafka, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Managed Service for Apache Kafka, code examples, and guides for using Terraform to provision Managed Service for Apache Kafka resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Managed Service for Apache Kafka resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Managed Service for Apache Kafka APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Managed Service for Apache Kafka

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Managed Service for Apache Kafka:

Service | Terraform resources  
---|---  
Managed Kafka | 

  * [google_managed_kafka_acl](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_acl)
  * [google_managed_kafka_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_cluster)
  * [google_managed_kafka_connect_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_connect_cluster)
  * [google_managed_kafka_connector](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_connector)
  * [google_managed_kafka_topic](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_topic)

  
  
## Terraform-based guides for Managed Service for Apache Kafka

The following table lists Terraform-based how-to guides and tutorials for Managed Service for Apache Kafka:

**Guide** | **Details**  
---|---  
[ Create a Google Cloud Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#terraform) | Shows how to create a Managed Service for Apache Kafka cluster using Terraform.  
[ Create a Managed Service for Apache Kafka topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic#terraform) | Shows how to create a topic using Terraform.  
[ Create a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#terraform) | Shows how to create a Connect cluster using Terraform. ([Preview](https://cloud.google.com/products#product-launch-stages))  
[ Create a BigQuery Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector#terraform) | Shows how to create a BigQuery Sink connector using Terraform. ([Preview](https://cloud.google.com/products#product-launch-stages))  
[ Create a Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector#terraform) | Shows how to create a Cloud Storage Sink connector using Terraform. ([Preview](https://cloud.google.com/products#product-launch-stages))  
[ Create a MirrorMaker 2.0 Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector#terraform) | Shows how to create a MirrorMaker 2.0 Source connector using Terraform. ([Preview](https://cloud.google.com/products#product-launch-stages))  
[ Create a Pub/Sub Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector#terraform) | Shows how to create a Pub/Sub Sink connector using Terraform. ([Preview](https://cloud.google.com/products#product-launch-stages))  
[ Create a Pub/Sub Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector#terraform) | Shows how to create a Pub/Sub Source connector using Terraform. ([Preview](https://cloud.google.com/products#product-launch-stages))  
  
## What's next

  * [Terraform code samples for Managed Service for Apache Kafka](https://docs.cloud.google.com/docs/samples?language=terraform&product=apachekafkaforbigquery)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
