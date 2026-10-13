---
url: https://docs.cloud.google.com/sap/docs/tf-for-sap/
title: Automating SAP deployments on Google Cloud with Terraform \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:05.440962+00:00
---

# Automating SAP deployments on Google Cloud with Terraform  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/tf-for-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Automating SAP deployments on Google Cloud with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

You can automate the deployment of Google Cloud infrastructure by using Terraform, an open source tool that lets you automate the creation and management of Google Cloud resources. For information about Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

For select SAP solutions and supporting databases, such as SAP HANA, Google Cloud provides predefined Terraform configuration files that you can use to deploy Google Cloud infrastructure that meets SAP supportability requirements and best practices.

## Supported SAP solutions

Google Cloud provides Terraform configuration files for the following SAP solutions:

  * SAP NetWeaver 
    * On [Linux](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-tf)
    * [High-availability cluster configuration on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles-tf)
    * [High-availability cluster configuration on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel-tf)
  * SAP HANA 
    * [Scale-up system](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf)
    * [Scale-out system without standby nodes](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-deployment-tf)
    * [Scale-out with host auto-failover](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-tf-deployment-guide)
    * [Scale-up system in a Linux high-availability cluster](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment)
    * [Scale-out system in a Linux high-availability cluster](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-ha-tf-deployment)
  * SAP ASE 
    * On [Linux](https://docs.cloud.google.com/sap/docs/sap-ase-deployment-linux-tf)
  * IBM Db2 for SAP 
    * On [Linux](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf)



## What the configuration files deploy

All of the Terraform configuration files that Google Cloud provides for SAP deployments configure or deploy the following elements:

  * One or more Compute Engine virtual machines (VMs)
  * An OS image that you specify
  * One or more Persistent Disk or Hyperdisk volumes
  * Optionally, an Identity and Access Management (IAM) service account that you specify for use by the VMs
  * The Google Cloud APIs that are required by the SAP deployment
  * Optionally, network tags for each VM instance
  * Optionally, an external IP address for each VM instance
  * The latest version of [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning)



For SAP HANA, the Terraform configuration files also deploy:

  * Storage volumes for `/hana/data`, `/hana/log`, `/hana/shared`, `/usr/sap`, and `/hanabackup`
  * Optionally, the SAP HANA system itself
  * For SAP HANA scale-out systems with host auto-failover, a master host, up to 15 worker hosts, and up to 3 standby hosts
  * A Linux high-availability cluster
  * Optionally, for SAP HANA scale-up systems, static IP addresses for the primary and secondary instances
  * Optionally, for SAP HANA scale-out systems, static IP addresses for the master, worker, and standby nodes
  * Optionally, a [sole-tenant node](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-sole-tenancy).



For SAP NetWeaver, the Terraform configuration files also deploy:

  * Storage volumes for `/sapmnt`, `/usr/sap`, and a swap volume
  * Optionally, a Linux high-availability cluster on SLES



For high-availability (HA) clusters, the Terraform configuration files also deploy additional functions and features like internal load balancer, instance group and forwarding rules. For more information, see the deployment guide for your HA scenario.

## Terraform configurations for each SAP deployment

Each predefined Terraform configuration for SAP contains a declarative configuration file `DEPLOYMENT_TYPE.tf`.

For information about the configuration file names or how to download them, see the deployment guide for your scenario.

## Completing the Terraform configuration file

The Terraform configuration files that are provided for SAP deployments conform to the standards defined by Terraform.

The configuration files provided for SAP include the primary module definition followed by comments that declare arguments. The following example is an excerpt from the `sap_hana.tf` file for deploying a SAP HANA scale-out system without standby nodes:
    
    
    #...
    module "sap_hana" {
      source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana/sap_hana_module.zip"
      #
      # By default, this source file uses the latest release of the terraform module
      # for SAP on Google Cloud. To fix your deployments to a specific release
      # of the module, comment out the source property above and uncomment the source property below.
      #
      # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/YYYYMMDDHHMM/terraform/sap_hana/sap_hana_module.zip"
      # ...
      project_id = "example-project-123456"
      zone = "us-central1-f"
      machine_type = "n2-highmem-32"
      subnetwork = "example-subnet-us-central1"
      linux_image = "sles-15-sp2-sap"
      linux_image_project = "suse-sap-cloud"
      # ...
      instance_name = "hana-scaleout"
      # ...
      sap_hana_deployment_bucket = "mybucketname"
      sap_hana_sid = "AB2"
      sap_hana_instance_number = 12
      sap_hana_sidadm_password = "TempPa55word"
      sap_hana_system_password = "TempPa55word"
      sap_hana_scaleout_nodes = 3
      sap_hana_sidadm_uid = 11
      vm_static_ip = "10.0.0.1"
      worker_static_ips = ["10.0.0.2", "10.0.0.3", "10.0.0.4"]
      enable_fast_restart = true
      # ...
    }

To use the optional arguments, remove the comment character, `#`, and specify a value for the argument. Most optional arguments have a default value. When you don't specify an optional argument, the Terraform configuration uses that argument's default value, if any.

For more information about configuration files, see [Terraform Language Documentation](https://www.terraform.io/language).

### Module versioning

The `DEPLOYMENT_TYPE.tf` Terraform configuration files that you download from Google Cloud for SAP deployments contain two instances of the `source` argument: one that is active and one that is included as a comment. You can control which version of the module your configuration uses by removing the leading comment character, `#`, from the `source` argument that you need and adding it to the one that you don't.

By default, when you download a new Terraform configuration file from Google Cloud for SAP deployments, the active `source` argument specifies `latest` as the module version, which means that if Terraform refreshes the files in your working directory when you enter the `terraform init` command, then your configuration uses the latest available version of the Terraform module that Google Cloud provides for SAP deployments.

The second instance of the `source` argument, which by default is deactivated by a leading `#` character, includes the timestamp that identifies the version of the module provided by Google Cloud. For example, in the following sample, `1.5.784645858` is the timestamp that identifies the Terraform module version.
    
    
    #...
    module "sap_hana" {
      source = "https://storage.googleapis.com/cloudsapdeploy/terraform/**latest** /terraform/sap_hana/sap_hana_module.zip"
      #...
      # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/**1.5.784645858** /terraform/sap_hana/sap_hana_module.zip"
      #...
      # arguments...
      #...}

If you need all of your deployments to use the same module version, then in your `DEPLOYMENT_TYPE.tf`, remove the leading `#` character from the `source` argument that includes the version timestamp and add it to the `source` argument that specifies `latest` as the version, as shown in the following example:
    
    
    #...
    module "sap_hana" {
      # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/**latest** /terraform/sap_hana/sap_hana_module.zip"
      #...
      source = "https://storage.googleapis.com/cloudsapdeploy/terraform/**1.5.784645858** /terraform/sap_hana/sap_hana_module.zip"
      #...
      # arguments...
      #...}

When a timestamp is specified, all deployments use the version of the Terraform module that corresponds to the specified timestamp.

### Deploying multiple systems with one configuration file

You can deploy multiple systems using a single Terraform configuration file. You do this by adding `module` blocks to the configuration file for each additional system that you need to deploy.

For SAP deployments, copy the `module` block definition provided by Google Cloud and paste it in the appropriate order in your configuration file.

In each module block, make sure to specify unique values for any instance-specific arguments such as `module` or `instance_name`.

## Applying configurations

You apply a Terraform configuration using the `terraform apply` command.

If you would like to preview the configuration results before actually deploying any Google Cloud resources, then create the Terraform execution plan using the `terraform plan` command.

For detailed application procedures, see the deployment guide for your scenario.

When Terraform completes applying your configuration, in the Cloud Shell, Terraform displays `COMPLETED` for each of the resources it creates and passes control to the shell script. The shell script is invoked as startup script on the deployed VMs.

The shell script configures the deployed resources further and logs its progress in Cloud Logging. An SAP deployment is not complete until the shell scripts complete their processing.

## Post-deployment scripts

You can use a post-deployment script to perform additional actions, like triggering installation of your SAP NetWeaver application, monitoring agents, and so forth.

Post-deployment scripts are the recommended way to customize your configuration because they get control only after the Google Cloud infrastructure is configured according to SAP supportability requirements.

To display status messages for post-deployment scripts, you need to code the scripts to write the messages to the logs. For more information, see the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs).

The status of post-deployment scripts are not included in the messages that Terraform writes to the Cloud Shell or a local Google Cloud CLI shell session.

**Note:** Google Cloud can only provide limited guidance for post-deployment scripts. You are responsible for the coding of any script, the actions it takes, its successful execution, as well as the troubleshooting of any problems that may arise while developing or running it, as well as any problems it might cause in the resulting deployment.

## Getting support for the Terraform configurations

If you need help resolving a problem with the Terraform configurations that Google Cloud provides for SAP, then gather the [required diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-tf-config) and contact Cloud Customer Care.

For more information on getting support for Terraform issues, see [Get support for Terraform issues](https://docs.cloud.google.com/docs/terraform/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
