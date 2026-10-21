---
url: https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider/
title: Install the Compute Engine Symphony provider \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:20:35.304183+00:00
---

# Install the Compute Engine Symphony provider  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install the Compute Engine Symphony provider Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install and configure the IBM Symphony provider for Compute Engine. You learn how to set up Pub/Sub to monitor virtual machine (VM) instance events, build and install the provider plugin, and configure the provider instance within your Symphony host factory environment.

For more information about Symphony Connectors for Google Cloud, see [Integrate IBM Spectrum Symphony with Google Cloud](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony).

## Before you begin

To install the Symphony provider for Compute Engine, you must have the following resources:

  * A running IBM Spectrum Symphony cluster with the host factory service enabled. You have the hostname of your IBM Spectrum Symphony primary host.
  * A dedicated service account with the required roles. For more information on how you create this service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create).
  * A firewall rule that you have configured to allow communication between Symphony primary host and Compute Engine. For example:
        
        gcloud compute firewall-rules create allow-symphony-primary-to-compute \
            --project=PROJECT_ID \
            --direction=INGRESS \
            --priority=1000 \
            --network=NETWORK_NAME \
            --allow=all \
            --source-tags=NETWORK_TAGS_MASTER \
            --target-tags=NETWORK_TAGS
        
        gcloud compute firewall-rules create allow-symphony-compute-to-primary \
            --project=PROJECT_ID \
            --direction=INGRESS \
            --priority=1000 \
            --network=NETWORK_NAME \
            --allow=all \
            --source-tags=NETWORK_TAGS \
            --target-tags=NETWORK_TAGS_MASTER
        

Replace the following:

    * `PROJECT_ID`: the ID of your Google Cloud project.
    * `NETWORK_NAME`: the name of the VPC network where your Symphony resources are deployed.
    * `NETWORK_TAGS_MASTER`: the network tag applied to your Symphony primary host VM.
    * `NETWORK_TAGS`: the network tag applied to your Symphony compute node VMs.

For more information, see [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules).




### Required roles

To get the permissions that you need to create and manage instances that use a service account, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare your Compute Engine environment

To let the Symphony host factory create and manage VMs, you need to configure several Google Cloud resources:

  * **Instance template** : a blueprint that defines the configuration of the Symphony compute VMs that the host factory creates.

  * **Managed Instance Group (MIG):** a group of identical VMs that are created by using an instance template. The host factory scales this group up or down by adding or removing VMs based on workload demand.

  * **Pub/Sub topic and subscription** : a messaging service that notifies the Symphony provider about VM lifecycle events, such as preemptions or deletions. This service lets the provider maintain an accurate state of the cluster.




### Create an instance template

Create an instance template for the Symphony compute hosts by using the [gcloud compute instance-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) command. This template defines the properties of the VMs that it creates. These VMs must have Symphony installed. You can either use an image with Symphony pre-installed, or use a startup script to install Symphony after you create the VMs. For information about installing Symphony on a compute host VM, see [Installing on a Linux compute host](https://www.ibm.com/docs/en/spectrum-symphony/7.3.2?topic=environment-installing-linux-compute-host) in the IBM documentation.
    
    
      gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --network-interface=nic-type=GVNIC,stack-type=IPV4_ONLY,subnet=SUBNET_NAME,no-address \
        --instance-template-region=REGION \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/trace.append \
        --tags=NETWORK_TAGS \
        --create-disk=auto-delete=yes,boot=yes,device-name=INSTANCE_TEMPLATE_NAME,image-family=rocky-linux-9,image-project=rocky-linux-cloud,mode=rw,size=20,type=pd-balanced \
        --shielded-secure-boot \
        --shielded-vtpm \
        --shielded-integrity-monitoring
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: a name for your new instance template.
  * `MACHINE_TYPE`: the machine type for your compute instances. For more information, see [Create a VM with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).
  * `SUBNET_NAME`: the name of the subnet for your instances. For more information, see [View the network configuration for an instance](https://docs.cloud.google.com/compute/docs/instances/view-network-properties).
  * `SERVICE_ACCOUNT_EMAIL`: the email of the service account that you set up in the Before you begin section. Ensure this service account has the roles specified in the Required roles section.
  * `REGION`: the Google Cloud region where you want to create your resources.
  * `NETWORK_TAGS`: a network tag to apply to your instances, which can be used for firewall rules—for example, `symphony-compute`.



### Create a managed instance group

Create a managed instance group (MIG) by using the instance template from the previous step. The host factory provider scales this group by adding or removing instances based on workload demand.
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --project=PROJECT_ID \
        --base-instance-name=INSTANCE_GROUP_NAME \
        --template=projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME \
        --size=0 \
        --zone=ZONE
        --default-action-on-vm-failure=repair \
        --no-force-update-on-repair \
        --standby-policy-mode=manual \
        --list-managed-instances-results=pageless
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: your chosen name for the managed instance group.
  * `PROJECT_ID`: the ID of your Google Cloud project. For more information, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template that you created in the previous step.
  * `REGION`: the region where your resources are located, such as `us-east`.
  * `ZONE`: the zone within the selected region, such as `a`.



For more information on creating MIGs, see [Create a MIG in a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig).

### Set up Pub/Sub

To let the Symphony provider receive notifications about VM lifecycle events, configure a Pub/Sub topic and subscription:

  1. On your Symphony primary host, set the following environment variables:
         
         export GCP_PROJECT=PROJECT_ID
         export PUBSUB_TOPIC=PUBSUB_TOPIC
         

Replace the following:

     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `PUBSUB_TOPIC`: A name for your Google Cloud topic, such as `hf-gce-vm-events`.
  2. Create a Pub/Sub topic:
         
         gcloud pubsub topics create $PUBSUB_TOPIC
         

  3. Use the [gcloud logging sinks create command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) to create a logging sink to export audit logs to Pub/Sub:
         
         gcloud logging sinks create ${PUBSUB_TOPIC}-sink \
             pubsub.googleapis.com/projects/${GCP_PROJECT}/topics/${PUBSUB_TOPIC} \
             --log-filter="
             logName=\"projects/${GCP_PROJECT}/logs/cloudaudit.googleapis.com%2Factivity\"
             resource.type=(\"gce_instance_group_manager\" OR \"gce_instance\")
             protoPayload.methodName=(
                 \"v1.compute.instanceGroupManagers.createInstances\"
                 OR
                 \"v1.compute.instanceGroupManagers.deleteInstances\"
                 OR
                 \"v1.compute.instances.insert\"
                 OR
                 \"v1.compute.instances.delete\"
             )
             " \
             --description="Exports MIG VM create/delete audit logs to Pub/Sub"
         

The output of this command includes a service account that you use in the next step.

  4. Grant the [Pub/Sub Publisher (`roles/pubsub.publisher`)](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) role to the service account from the previous step:
         
         gcloud pubsub topics add-iam-policy-binding $PUBSUB_TOPIC \
             --member="serviceAccount:LOGGING_SINK_SERVICE_ACCOUNT" \
             --role="roles/pubsub.publisher"
         

Replace `LOGGING_SINK_SERVICE_ACCOUNT` with the service account name from the logging sink creation output.

  5. Create a subscription to receive the logs:
         
         gcloud pubsub subscriptions create ${PUBSUB_TOPIC}-sub \
             --topic=${PUBSUB_TOPIC}
         

  6. Verify that your service account has the correct permissions to subscribe to the subscription:
         
         gcloud pubsub subscriptions add-iam-policy-binding ${PUBSUB_TOPIC}-sub \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/pubsub.subscriber"
         

Replace `SERVICE_ACCOUNT_EMAIL` with the email of the service account that manages your instance group. This is the same service account you set up in the Before you begin section.




The Pub/Sub setup is complete. For more information on how to configure Pub/Sub, see [Publish and receive messages in Pub/Sub by using the Google Cloud CLI](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-gcloud).

## Load the host factory environment variables

Before you can configure or manage the host factory services, you must load the Symphony environment variables into your shell session. On your Symphony primary host VM, run the following command:
    
    
    source INSTALL_FOLDER/profile.platform
    

Replace `INSTALL_FOLDER` with the path to your install folder. The default Symphony installation folder path is `/opt/ibm/spectrumcomputing`. If you installed Symphony in a different location, then use the correct path for your environment.

This command executes the `profile.platform` script, which exports essential environment variables like `$EGO_TOP` and `$HF_TOP` and adds the Symphony command-line tools to your shell's `PATH`. You must run this command for each new terminal session to ensure the environment is configured correctly.

## Install the provider plugin

To integrate the Compute Engine provider with the Symphony host factory service, install the prebuilt provider plugin from the RPM package or build the provider from the source code.

### Install the prebuilt provider plugin

To install the provider plugin by using RPM packages, follow these steps on your Symphony primary host:

  1. Add the `yum` repository for the Google Cloud Symphony Connectors:
         
         sudo tee /etc/yum.repos.d/google-cloud-symphony-connector.repo << EOM
         [google-cloud-symphony-connector] name=Google Cloud Symphony Connector
         baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-symphony-connector-x86-64
         enabled=1
         gpgcheck=0
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
                https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOM
         

  2. Install the provider package for Compute Engine:
         
         sudo yum install -y hf-gcpgce-provider.x86_64
         




The RPM package installs the provider executables and scripts into the correct directories for the Symphony host factory service. After installation, the directory structure appears as follows:
    
    
    ├── bin
    │   └── hf-gce
    └── scripts
        ├── getAvailableTemplates.sh
        ├── getRequestStatus.sh
        ├── getReturnRequests.sh
        ├── requestMachines.sh
        └── requestReturnMachines.sh
    

### Build the provider from the source code

To build and install the CLI executable in the `bin` directory of the provider plugin directory, follow these steps:

  1. Clone the `symphony-gcp-connector` repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/symphony-gcp-connector.git
         

  2. Navigate to the `hf-provider` directory in your project:
         
         cd PROJECT_ROOT/hf-provider
         

Replace `PROJECT_ROOT` with the path to the top-level directory that contains the hf-provider directory, such as `/home/user/symphony-gcp-connector`.

  3. If you don't have `uv` installed, then install it:
         
         pip install uv
         

  4. Create a Python virtual environment by using `uv`:
         
         uv venv
         

  5. Activate the virtual environment:
         
         source .venv/bin/activate
         

  6. Install the required project dependencies:
         
         uv pip install .
         

  7. Install PyInstaller, which bundles the Python application into a standalone executable:
         
         uv pip install pyinstaller
         

  8. Create the `hf-gce` CLI for Compute Engine clusters:
         
         uv run pyinstaller hf-gce.spec --clean
         

  9. To verify the installation, run the `--help` command for an executable. You might see an error if you don't set the required environment variables.
         
         dist/hf-gce --help
         

  10. Copy the executable to the provider plugin `bin` directory:
         
         mkdir -p ${HF_TOP}/${HF_VERSION}/providerplugins/gcpgce/bin
         cp dist/hf-gce ${HF_TOP}/${HF_VERSION}/providerplugins/gcpgce/bin/
         

  11. Copy the scripts to the provider plugin `scripts` directory:
         
         cp -R ./resources/gce_cli/1.2/providerplugins/gcpgce/scripts ${HF_TOP}/${HF_VERSION}/providerplugins/gcpgce/
         

The OS must support the version of Python used to build the executables. The executables were tested with Python 3.9.6.




After installation, the directory structure for the provider plugin is similar to this example:
    
    
    ├── bin
    │   └── hf-gce
    └── scripts
        ├── getAvailableTemplates.sh
        ├── getRequestStatus.sh
        ├── getReturnRequests.sh
        ├── requestMachines.sh
        └── requestReturnMachines.sh
    

## Enable the provider plugin

To enable the Compute Engine provider plugin, register it in the host factory configuration:

  1. Open the `$HF_TOP/conf/providerplugins/hostProviderPlugins.json` file.

The `$HF_TOP` environment variable is defined in your environment when you use the source command. The value is the path to the top-level installation directory for the IBM Spectrum Symphony host factory service.

  2. Add a `gcpgce` provider plugin section:
         
         {
             "name": "gcpgce",
             "enabled": 1,
             "scriptPath": "${HF_TOP}/${HF_VERSION}/providerplugins/gcpgce/scripts/"
         }
         

If you are using version 1.2 of the provider plugin with the default value for `$HF_TOP`, the resulting `scriptPath` value is: `INSTALL_FOLDER/hostfactory/1.2/providerplugins/gcpgce/scripts/`.




## Set up a provider instance

To configure the Compute Engine provider for your environment, create a provider instance.

  1. Set up the directory for the provider instance:

     * If you built the provider from source code, then you must create the directory and configuration files manually:
           
           mkdir -p $HF_TOP/conf/providers/gcpgceinst/
           

     * If you installed with RPM, then this directory already exists and contains example configuration files. Copy the example files to create your configuration:
           
           cp $HF_TOP/conf/providers/gcpgceinst/gcpgceinstprov_config.json.dist $HF_TOP/conf/providers/gcpgceinst/gcpgceinstprov_config.json
           cp $HF_TOP/conf/providers/gcpgceinst/gcpgceinstprov_templates.json.dist $HF_TOP/conf/providers/gcpgceinst/gcpgceinstprov_templates.json
           

  2. In the `$HF_TOP/conf/providers/gcpgceinst/` directory, create or edit a `gcpgceinstprov_config.json` file. This file contains the main configuration for the provider. The provider supports the following configuration variables. You must specify variables that have no default value in this configuration.

Variable Name | Description | Default Value  
---|---|---  
`HF_DBDIR` | The location where this provider stores its state database. | Defined in the HostFactory environment as `$HF_DBDIR`.  
`HF_TEMPLATES_FILENAME` | The name of the templates file. | `gcpgceinstprov_templates.json`  
`GCP_CREDENTIALS_FILE` | The location of the Google Cloud service account credentials file. | The application uses the default credentials if you don't specify this value.  
`GCP_PROJECT_ID` | The ID of the Google Cloud project. | None  
`GCP_INSTANCE_PREFIX` | A string to prepend to all hosts created by this provider. | `sym-`  
`LOGFILE` | The location of the log file that the provider sends logs to. | A file with a generated name, located in the directory defined by the HostFactory environment variable `HF_PROVIDER_LOGDIR`.  
`LOG_LEVEL` | The Python log level | `WARNING`  
`PUBSUB_TIMEOUT` | If the most recent Pub/Sub event is older than this duration, in seconds, the Pub/Sub listener disconnects. This timeout only applies when the Pub/Sub event listener is automatically launched. Otherwise, the listener runs indefinitely, and the administrator must control the lifecycle. | `600`  
`PUBSUB_TOPIC` | The name of the Pub/Sub topic. This variable is for backward compatibility only. | `hf-gce-vm-events`  
`PUBSUB_SUBSCRIPTION` | The name of the Pub/Sub subscription to monitor for VM events. | `hf-gce-vm-events-sub`  
`PUBSUB_LOCKFILE` | The name of the file that indicates whether the Pub/Sub event listener is active. | `/tmp/sym_hf_gcp_pubsub.lock`  
`PUBSUB_AUTOLAUNCH` | If set to `true`, the provider attempts to automatically launch the Pub/Sub event listener. If `false`, you must launch the Pub/Sub event listener by using the method of your choice, with the command `hf-gce monitorEvents`. | `true`  
  
The following example shows a basic configuration:
         
         {
             "GCP_PROJECT_ID": "PROJECT_ID",
             "LOG_LEVEL":"INFO",
             "PUBSUB_SUBSCRIPTION": "PUBSUB_SUBSCRIPTION",
             "PUBSUB_TIMEOUT": 100
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `PUBSUB_SUBSCRIPTION`: the name of the Pub/Sub subscription that you created to monitor VM events. For more information, see Set up Pub/Sub.
  3. In the same directory, create or edit a `gcpgceinstprov_templates.json` file. This file defines the templates for the VMs that the provider can create. The attributes in the template must align with the configuration of the supporting instance group.

     * If you installed with RPM, then use the `gcpgceinstprov_templates.json` file that you created in the previous steps as a starting point.
     * If you built from source, then use the following example template:
           
           {
               "templates": [
                   {
                       "templateId": "template-gcp-01",
                       "maxNumber": 10,
                       "attributes": {
                           "type": [ "String", "X86_64" ],
                           "ncpus": [ "Numeric", "1" ],
                           "nram": [ "Numeric", "1024" ]
                       },
                       "gcp_zone": "GCP_ZONE",
                       "gcp_instance_group": "INSTANCE_GROUP_NAME"
                   }
               ]
           }
           

Replace the following:

       * `GCP_ZONE`: the Google Cloud zone where your instance group is located, such as `us-central1-a`.
       * `INSTANCE_GROUP_NAME`: the name of the instance group that the provider manages, such as `symphony-compute-ig`.
  4. After you create these files, verify that your provider instance directory is similar to this example:
         
         ├── gcpgceinstprov_config.json
         └── gcpgceinstprov_templates.json
         




## Enable the provider instance

To activate the provider instance, enable it in the host factory configuration file:

  1. Open the `$HF_TOP/conf/providers/hostProviders.json` file.

  2. Add a `gcpgceinst` provider instance section:
         
         {
             "name": "gcpgceinst",
             "enabled": 1,
             "plugin": "gcpgce",
             "confPath": "${HF_CONFDIR}/providers/gcpgceinst/",
             "workPath": "${HF_WORKDIR}/providers/gcpgceinst/",
             "logPath": "${HF_LOGDIR}/"
         }
         

**Important:** Don't replace the `${HF_CONFDIR}`, `${HF_WORKDIR}`, and `${HF_LOGDIR}` variables in this configuration. The IBM Spectrum Symphony host factory automatically defines these environment variables.

When you configure your shell session by using the `source command`, this script sets these variables to point to the correct subdirectories within your Symphony installation. The host factory service then uses these variables to construct the full paths at runtime.




## Enable the requestor instance

To let a specific Symphony component use the Compute Engine provider to provision resources, enable it for that requestor.

  1. Open the `$HF_TOP/conf/requestors/hostRequestors.json` file.

  2. In the appropriate requestor instance, add `gcpgceinst` to the `providers` parameter:
         
         "providers": ["gcpgceinst"],
         

The provider value must match the provider name you use in Enable the provider instance.




## Start the host factory service

To apply your configuration changes, start the host factory service. On your Symphony primary host VM, sign in as the cluster administrator and start the service:
    
    
    sed -i -e "s|MANUAL|AUTOMATIC|g" $EGO_ESRVDIR/esc/conf/services/hostfactory.xml
    egosh user logon -u "SYMPHONY_USERNAME -x "SYMPHONY_PASSWORD
    egosh service start HostFactory
    

Replace the following:

  * `SYMPHONY_USERNAME`: the Symphony username for authentication.
  * `SYMPHONY_PASSWORD`: the password for the Symphony user.



## Test connectors

Create a resource request to test the provider for Compute Engine.

To do so, use one of the following methods:

  * **Symphony GUI** : For instructions on how to create a resource request by using the Symphony GUI, see [Manually scheduling cloud host requests and returns](https://www.ibm.com/docs/en/spectrum-symphony/7.3.2?topic=manually-scheduling-cloud-host-requests-returns) in the IBM documentation.

  * **REST API** : To create a resource request using the REST API, follow these steps:

    1. Find the host and port of the host factory REST API:
           
           egosh client view REST_HOST_FACTORY_URL
           

The output is similar to this example:
           
           CLIENT NAME: REST_HOST_FACTORY_URL
           DESCRIPTION: http://sym2.us-central1-c.c.symphonygcp.internal:9080/platform/rest/hostfactory/
           TTL        : 0
           LOCATION   : 40531@10.0.0.33
           USER       : Admin
           
           CHANNEL INFORMATION:
           CHANNEL             STATE
           9                   CONNECTED
           

    2. To create a resource request using the REST API, use the following command:
           
           HOST=PRIMARY_HOST
           PORT=PORT
           TEMPLATE_NAME=INSTANCE_TEMPLATE_NAME
           PROVIDER_NAME=gcpgceinst
           
           curl -X POST -u "SYMPHONY_USER:SYMPHONY_PASSWORD" -H "Content-Type: application/json" -d "{ \"demand_hosts\": [ { \"prov_name\": \"$PROVIDER_NAME\", \"template_name\": \"$TEMPLATE_NAME\", \"ninstances\": 1 } ] }" \
           http://$HOST:$PORT/platform/rest/hostfactory/requestor/admin/request
           

Replace the following:

       * `PRIMARY_HOST`: the hostname of your primary host from the output of the previous command.
       * `PORT`: the port number of your primary host from the output of the previous command, such as `9080`.
       * `SYMPHONY_TEMPLATE_ID`: The `templateId` defined in the `gcpgceinstprov_templates.json` file, such as `template-gcp-01`.
       * `SYMPHONY_USER`: the Symphony user for authentication.
       * `SYMPHONY_PASSWORD`: the password for the Symphony user.

If successful, then the output is similar to this example:
    
    {"scheduled_request_id":["SD-641ef442-1f9e-40ae-ae16-90e152ed60d2"]}
    




## What's next

  * [Install the GKE provider](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-kubernetes-provider)
  * [Troubleshoot IBM Spectrum Symphony connectors](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/troubleshoot-symphony)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
