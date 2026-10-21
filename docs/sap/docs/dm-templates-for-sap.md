---
url: https://docs.cloud.google.com/sap/docs/dm-templates-for-sap/
title: Automating SAP deployments on Google Cloud with Deployment Manager \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:30.896332+00:00
---

# Automating SAP deployments on Google Cloud with Deployment Manager  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/dm-templates-for-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Automating SAP deployments on Google Cloud with Deployment Manager Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Deployment Manager reaches end of support on March 31, 2026. For more information, see [Cloud Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

To automate the deployment of SAP solutions on Google Cloud, we recommend that you use Terraform or Workload Manager. For more information, see [Overview of automating SAP deployments on Google Cloud](https://docs.cloud.google.com/sap/docs/automation-for-sap).

You can automate the deployment of Google Cloud infrastructure by using [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs), a service that automates the creation and management of Google Cloud resources.

For select SAP solutions and supporting databases, such as SAP HANA, Google Cloud provides pre-defined Cloud Deployment Manager configuration templates that you can use to deploy Google Cloud infrastructure that meets SAP supportability requirements and best practices.

## Supported SAP solutions

Google Cloud provides Cloud Deployment Manager configurations for the following SAP solutions:

  * SAP NetWeaver 
    * On [Linux](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-dm)
    * On [Windows](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-dm)
  * SAP HANA 
    * [Scale-up](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide)
    * [Scale-out with host auto-failover](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-deployment-guide)
    * [Scale-up in a Linux High-availability cluster](https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment)
  * SAP ASE 
    * On [Linux](https://docs.cloud.google.com/sap/docs/sap-ase-deployment-linux)
    * On [Windows](https://docs.cloud.google.com/sap/docs/sap-ase-deployment-windows)
  * SAP MaxDB 
    * On [Linux](https://docs.cloud.google.com/sap/docs/sap-maxdb-deployment-linux)
    * On [Windows](https://docs.cloud.google.com/sap/docs/sap-maxdb-deployment-windows)
  * IBM Db2 
    * On Linux. You can download the template from: 
          
          https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_db2/template.yaml

The steps for using the Db2 template for Linux are not documented, but are very similar to the steps for the ASE and MaxDB Linux templates.
    * On Linux in an [HA cluster on Linux](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-ha-deployment-guide)
    * On Windows. You can download the template from: 
          
          https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_db2-win/template.yaml

The steps for using the Db2 template for Windows are not documented, but are very similar to the steps for the ASE and MaxDB Windows templates.



## What the templates deploy

All of the Deployment Manager templates that Google Cloud provides for SAP deployments configure or deploy the following elements:

  * One or more Compute Engine virtual machines (VMs)
  * An OS image that you specify
  * One or more persistent disks
  * Optionally, an Identity and Access Management (IAM) service account that you specify for use by the VMs
  * The Google Cloud APIs that are required by the SAP deployment
  * Optionally, network tags for each VM instance
  * Optionally, a public IP address for each VM instance
  * The latest version of [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning)



For SAP HANA, the Deployment Manager templates also deploy:

  * Storage volumes for `/hana/shared` and `/hanabackup`
  * Optionally, the SAP HANA system itself
  * For SAP HANA scale-out systems with host auto-failover, a master host, up to 15 worker hosts, and up to 3 standby hosts
  * For SAP HANA scale-up systems, a Linux high-availability cluster



For SAP NetWeaver, the Deployment Manager templates also deploy:

  * Storage volumes for `/sapmnt`, `/usr/sap`, and a swap volume



## Deployment Manager files for each SAP deployment

Each pre-defined Deployment Manager configuration for SAP contains following set of files:

  * A YAML configuration file, `template.yaml`
  * A Python template file, `deployment-type.py`, such as `sap_hana.py`, `sap_hana_scaleout.py,` or `sap_nw.py`.
  * A Python schema file, `deployment-type.py.schema`, such as `sap_hana.py.schema`, `sap_hana_scaleout.py.schema,` or `sap_nw.py.schema`.
  * At least one shell script, `startup.sh` or `startup.ps1`



You specify the properties of your Google Cloud resources in the `template.yaml` configuration file.

## Completing the `template.yaml` configuration file

The `template.yaml` configuration files that are provided for SAP deployments conform to the standards defined by Deployment Manager.

The configuration files provided for SAP include the primary resource definition followed by a comment section that contains advanced properties that are less commonly used. The following example is an excerpt from the `template.yaml` file for SAP HANA:
    
    
    resources:
    - name: sap_hana
      type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/sap_hana.py
      #
      # By default, this configuration file uses the latest release of the deployment
      # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
      # of the scripts, comment out the type property above and uncomment the type property below.
      #
      # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/**202103111102** /dm-templates/sap_hana/sap_hana.py
      #
      properties:
        instanceName: [VM_NAME]
        instanceType: [MACHINE_TYPE]
        zone: [ZONE]
        subnetwork: [SUBNETWORK]
        linuxImage: family/[IMAGE_FAMILY]
        linuxImageProject: [IMAGE_PROJECT]
        sap_hana_deployment_bucket: [MEDIA_BUCKET]
        sap_hana_sid: [SID]
        sap_hana_instance_number: [INSTANCE_NUMBER]
        sap_hana_sidadm_password: [PASSWORD]
        sap_hana_system_password: [PASSWORD]
        sap_hana_scaleout_nodes: [NUMBER_OF_WORKER_NODES]
        #
        # --- Advanced Options ---
        # The following advanced options are not usually needed. To use an advanced option, remove
        # the comment indicator, #, before the parameter name and specify an appropriate value.
        #
        # networkTag: [TAG]
        #    Adds network tags to your instance. This is useful if you do routing or define
        #    firewall rules by tags. By default, no tags are added to your VM. Multiple tags
        #    can be assigned by separating them with commas
        #
         ...
    

To use the advanced properties, remove the comment character, `#`, and specify a value for the property.

For more information configuration files, see [Deployment Manager Fundamentals](https://docs.cloud.google.com/deployment-manager/docs/fundamentals).

### Template versioning

You can control which version of the Deployment Manager template that your SAP deployments use by specifying a version timestamp on the `type` property in the YAML configuration file.

By default, when you download a new `template.yaml` configuration file, the `type` property specifies `latest` as the version, which means that your deployments always use the latest available version of the Deployment Manager templates.

In the comments that follow the `type` property is an alternative `type` property specification that includes the timestamp of the latest available version at the time you downloaded the `template.yaml` file. For example:
    
    
    resources:
    - name: sap_hana
      type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/**latest** /dm-templates/sap_hana/sap_hana.py
      #
      # By default, this configuration file uses the latest release of the deployment
      # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
      # of the scripts, comment out the type property above and uncomment the type property below.
      #
      # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/**202103111102** /dm-templates/sap_hana/sap_hana.py
      #
      properties:
      ...

If you need all of your deployments to use the same template version, replace the `type` property specification that includes `latest` with the `type` property specification that includes the timestamp. For example:
    
    
    resources:
    - name: sap_hana
      type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/**202103111102** /dm-templates/sap_hana/sap_hana.py
      properties:
      ...

When a timestamp is specified, all deployments use the version of the Deployment Manager template that corresponds to the specified timestamp.

You can see which template version Deployment Manager used for an SAP deployment in the Google Cloud console by clicking the name of the deployment on the [Deployments page](https://console.cloud.google.com/dm/deployments) and then clicking **Expanded config VIEW** under **Deployment properties**. The timestamp of the version appears after `startup-script` in the `metadata` section, as shown in the following example:
    
    
    metadata:
      items:
      - key: startup-script
        value: curl -s https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/**202103111102** /dm-templates/sap_hana/startup.sh
          | bash -s https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/**202103111102** /dm-templates

### Deploying multiple resources with one configuration file

You can deploy multiple resources with a single configuration file by adding more resource definitions to the file.

For SAP deployments, copy the `-name`, `type`, and `properties:` sections of the pre-defined resource and paste it below to create the new resource definition.

In each resource definition, be sure to specify unique values for the following items:

  * name
  * instanceName



## Running deployments

You start a deployment by issuing the following command:
    
    
    gcloud deployment-manager deployments create [DEPLOYMENT-NAME] --config [TEMPLATE-NAME].yaml

If you would like to preview the deployment results before actually deploying any Google Cloud resources, append the `--preview` flag to the command.

When you start a deployment, Deployment Manager validates the specifications in the `template.yaml` file against definitions that are contained in the `deployment-type.py.schema` file. If validation is successful, Deployment Manager creates the Google Cloud resources by using the resource definitions in the `template.yaml` and `deployment-type.py` files.

When Deployment Manager processing is complete, in the Cloud Shell, Deployment Manager displays `COMPLETED` for each of the resources it creates and passes control to the shell script.

The shell script configures the deployed resources further and logs its progress in Cloud Logging. An SAP deployment is not complete until the shell scripts complete their processing.

Deployment Manager also creates an entry on the [**Deployments**](https://console.cloud.google.com/dm/deployments) page in the Google Cloud console, where you can find additional details about your deployment.

**Warning:** Do not delete a deployment unless you need to delete all of the Google Cloud resources that are associated with the deployment or the deployment failed. Deleting a deployment also deletes all of the resources that the deployment created.

## Advanced customization of the templates

Beyond adding VM definitions or other minor changes in the YAML configuration file, if you are an advanced user, you can customize the Deployment Manager templates that are provided by Google Cloud in other ways, but there are risks in doing so.

If you modify the templates, you assume the responsibility for the modified template, including making sure that it is up to date and that Deployment Manager can process it. You also assume responsibility for ensuring that the Google Cloud infrastructure and SAP systems that the modified templates deploy meet SAP and Google Cloud supportability requirements, including SAP requirements.

Modifications to the Deployment Manager templates also make it more difficult for Google Cloud to support your deployment. The SAP specialists in Cloud Customer Care are familiar with the unmodified templates and the configurations that they deploy, but will not be familiar with your unique customizations. If you need support from Google Cloud for a deployment or configuration that uses a customized template, be prepared to explain your customizations and to wait longer for the support case to be resolved.

Before modifying the Deployment Manager templates that are provided by Google Cloud for SAP, make sure that you have an appropriately-skilled technical team available to advise on the changes, evaluate the impact of the changes on the performance of your system, and to help troubleshoot issues that might arise later. If you don't have such a team, [implementation partners](https://cloud.google.com/find-a-partner/?search=SAP&sort-type=RELEVANCE) or [Google Cloud Professional Services](https://cloud.google.com/consulting) have specialists that can help.

To make changes, you need to understand:

  * The SAP supportability requirements that are defined in the SAP documentation and SAP Notes that apply to your SAP products.
  * Deployment Manager and how to work with deployments, configurations, and templates. See the [Deployment Manager documentation](https://docs.cloud.google.com/deployment-manager/docs).
  * Depending on the type of change you are making, Python or shell scripting languages.



### Types of advanced customization

Modifications that are considered advanced customizations include:

  * Custom processing or actions in a post-deployment script. This is the recommended method for including advanced customizations in your deployments.
  * The use of operating system types other than the supported versions of Red Hat Enterprise Linux for SAP or SUSE Linux Enterprise Server for SAP.
  * Modifications to the backend scripts that are provided as part of the template: 
    * The shell scripts (bash or powershell).
    * The Python dynamic configuration and schema files.
  * For High Availability deployments: 
    * Customization of Pacemaker configuration settings. If you find a particular function to be missing, please provide feedback on the documentation page.
    * Changes to the default template for HANA Scale-out deployment with standby nodes.



Regardless of the type of change you make, make sure that your changes result in an SAP system that is within the support scope that is defined by the SAP product documentation and SAP Notes that are applicable to your system. **Note:** For production deployments of SAP HANA, do not change: 

  * The disk size calculations, which adhere to SAP certification requirements
  * The disk type



### Template files that you can customize

Google Cloud recommends that you limit customizations to the `.yaml` configuration file, although you can modify the other Deployment Manager files as well, as long as the resulting SAP system meets SAP supportability requirements.

Which files you need to modify depends on the type of changes you need to make.

To add additional validation checks for property values that are specific to your environment, you can add the property definitions to the `deployment-type.py.schema` file.

In the `deployment-type.py` file, you can make changes such as:

  * Add additional calculations on the values in the configuration file, such as IP ranges or disk sizes. Note that changing disk sizes, especially for SAP HANA, can result in configuration that does not meet SAP support requirements.
  * Add additional VM instance metadata.
  * Adjust disk names.



### Downloading the template files

To download the files you can use the following commands after you replace the red italic text with the values for the template you need:
    
    
    wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/template-directory/file-name.py
    wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/template-directory/file-name.py.schema
    wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/template-directory/startup.sh
    wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/template-directory/template.yaml

For example, if you need to download the template files for a SAP HANA scale-up deployment, use the following commands:
    
    
    wget https://storage.cloud.google.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/sap_hana.py
    wget https://storage.cloud.google.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/sap_hana.py.schema
    wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/startup.sh
    wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/template.yaml

### Using your modified template files

When you are done modifying the template files, upload them to a Cloud Storage bucket or a web server and update the URLs in the `template.yaml` and other files to the file location.

## Post-deployment scripts

You can use a post-deployment script to perform additional actions, like triggering installation of your SAP NetWeaver application, monitoring agents, and so forth.

Post-deployment scripts are the recommended way to customize your deployments because they get control only after the Google Cloud infrastructure is configured according to SAP supportability requirements.

To display status messages for post-deployment scripts, you need to code the scripts to write the messages to the logs. For more information, see the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs).

The status of post-deployment scripts are not included in the messages that Deployment Manager writes to the Cloud Shell or a local Google Cloud CLI shell session.

**Note:** Google Cloud can only provide limited guidance for post-deployment scripts. You are responsible for the coding of any script, the actions it takes, its successful execution, as well as the troubleshooting of any problems that may arise while developing or running it, as well as any problems it might cause in the resulting deployment.

## Getting support for the Deployment Manager templates for SAP

If you need help resolving a problem with the Deployment Manager templates for SAP, gather the required diagnostic information and contact Cloud Customer Care. For a list of the required diagnostic information, see [Deployment Manager templates for SAP diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-dmt).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
