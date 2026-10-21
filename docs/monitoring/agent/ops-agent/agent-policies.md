---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-policies/
title: Use agent policies (GA) \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:44.354766+00:00
---

# Use agent policies (GA)  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Use agent policies (GA) Stay organized with collections  Save and categorize content based on your preferences. 

You create and manage agent policies by using the [`gcloud compute instances ops-agents policies`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies) command group in the Google Cloud CLI or the [`ops-agent-policy` Terraform module](https://github.com/terraform-google-modules/terraform-google-cloud-operations/tree/master/modules/ops-agent-policy). Agent policies use the [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) suite of tools in Compute Engine to manage [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management), which can automate the deployment and maintenance of software configurations like the Ops Agent. These policies can't be applied to the legacy Monitoring agent or the legacy Logging agent. 

The GA agent policies use [OS policy assignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicyAssignment) resources in the OS Config API. Although there is a general gcloud CLI command group for managing OS policy assignments, [ `gcloud compute os-config os-policy-assignments`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments), the `gcloud compute instances ops-agents policies` command group is designed specifically for the agent policies described in this document. **Note:** This document describes the GA agent policies. Agent policies are also available in a beta release. For information about the differences between the two releases and about converting beta agent policies to GA agent policies, see [Overview of agent policies for the Ops Agent.](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-policies-overview)

## Before you begin

The `ops-agent-policy` Terraform module is built on top of the `gcloud compute instances ops-agents policies` commands from the Google Cloud SDK. For information about how Terraform works, see [Using Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview).

Before using the Google Cloud CLI or the Terraform module to create agent policies, complete the following steps:

  1. If you are going to use the `gcloud compute instances ops-agents policies` commands and if you haven't done so already, then install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  2. If you are going to use the Terraform module, then do the following:

     1. For information about installing Terraform, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform). Cloud Shell has Terraform already installed.

     2. Clone the `terraform-google-cloud-operations` repository, which contains the `ops-agent-policy` module:
            
            git clone https://github.com/terraform-google-modules/terraform-google-cloud-operations
            

  3. Download and run the [`prepare-for-ops-agents-policies.sh`](https://docs.cloud.google.com/static/stackdriver/docs/prepare-for-ops-agents-policies.sh) script to enable the required APIs and to set the proper permissions for using the Google Cloud CLI or Terraform.

For information about the script, see The `prepare-for-ops-agents-policies.sh` script.

**Note:** The `prepare-for-ops-agents-policies.sh` script is designed to run on Linux. If you're using a machine on a different operating system, then run the script from [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).



### Uninstall the legacy Monitoring agent and Logging agent

If you're creating a policy for the Ops Agent, ensure that your VMs don't have the legacy Logging agent or Monitoring agent installed on them. Running the Ops Agent and the legacy agents on the same VM can cause ingestion of duplicate logs or a conflict in metrics ingestion. If necessary, [uninstall the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/installation#uninstall) and [uninstall the Logging agent](https://docs.cloud.google.com/logging/docs/agent/installation#uninstall) before creating a policy to install the Ops Agent. 

### Verify that the OS Config agent is installed

You might need to manually install and configure the OS Config agent on VMs that predate OS Config. For information about manually installing and verifying the OS Config agent, see the [VM Manager verification checklist](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-manager/verify-setup#manual-check). 

## Find values for operating-system information

If you want to apply agent policies to specific operating systems or versions, you need to know the values that OS Config uses to refer to them.

To find values for the `osShortName` and `osVersion` fields for a VM, use the following commands:
    
    
    gcloud compute instances os-inventory describe INSTANCE_NAME \
    --zone ZONE | grep "^ShortName: "
    
    
    
    gcloud compute instances os-inventory describe INSTANCE_NAME \
    --zone ZONE | grep "^Version: "
    

These commands require the OS Config agent to be installed on the VM.

## Create an agent policy to manage the Ops Agent

### Command-line

To create an agent policy, use the [`gcloud compute instances ops-agents policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/create) command. This command has the following structure:
    
    
    gcloud compute instances ops-agents policies create POLICY_ID \
      --zone ZONE \
      --file path/to/policy-description-file.yaml \
      --project PROJECT_ID
    

When using this command, replace the variables as follows:

  * POLICY_ID is a name for your policy.
  * ZONE is a Compute Engine zone. Agent policies are applied only to VMs in the specified zone; to apply a policy in multiple zones, you must create multiple policies.
  * path/to/policy-description-file.yaml is the path to a YAML file that describes the policy. For information about the structure of this file, see Describe agent policies.
  * PROJECT_ID is the ID of your Google Cloud project.



For information about the other commands in the command group and the available options, see the [`gcloud compute instances ops-agents policies`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies) documentation.

## Describe agent policies

You provide policy information to the `gcloud compute instances ops-agents policies` `create` by creating a YAML file that describes the policy and passing that file to the command as the value of the `--file` option.

This section describes the structure of the policy-description file. For additional information, see Example policy-description files.

### Format of the YAML policy-description file

The description file for an agent policy must include two field groups:

  * `agentsRule`, which tells the agent policy whether to install or remove the Ops Agent, and specifies the version of the Ops Agent to operate on.
  * `instanceFilter`, which describes the VMs on which the apply the policy.



#### Structure of the `agentsRule` field group

The `agentsRule` field group has the following structure:
    
    
    agentsRule:
      packageState: installed|removed
      version: latest|2.*.*|2.x.y

  * The `packageState` field tells the policy the intended state of the Ops Agent. The valid values are `installed` and `removed`.
  * The `version` field indicates the version of the Ops Agent to install or remove. You can specify the following values: 
    * `latest` is the most recent version of the Ops Agent.
    * `2.*.*` is the most recent release of major version 2 of the Ops Agent.
    * `2.x.y` indicates a specific release of major version 2.
For information about the available versions of the Ops Agent, see the agent's [GitHub repository](https://github.com/GoogleCloudPlatform/ops-agent/releases). 



#### Structure of the `instanceFilter` field group

The `instanceFilter` field group indicates the VMs in a zone to which the filter applies. This field group is a YAML representation of the [`InstanceFilter`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#InstanceFilter) structure used by the [`OSPolicyAssignment`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicyAssignment) resource in the OS Config API.

The `instanceFilter` field group has one of the following structures:

  * To apply the agent policy to all VMs in a zone, use the following: 
        
        instanceFilter:
              all: True

If you use the `all: True` filter, then you can't specify any other criteria.
  * To apply the agent policy to a specific set of VMs in a zone, describe the VMs by using a combination of any of the following: 
    * Labels on the VM, either for inclusion or exclusion: 
      * `inclusionLabels:`
      * `exclusionLabels:`
    * Operating system: `inventories:`
For example, the following filter applies the agent policy to the VMs with the specified operating systems that have the label "env=prod" and don't have the label "app=web": 
    
    instanceFilter:
          inclusionLabels:
          - labels:
              env: prod
          exclusionLabels:
          - labels:
              app: web
          inventories:
          - osShortName: rhel
            osVersion: '7.*'
          - osShortName: debian
            osVersion: '11'

For information about finding the operating-system values, see Find operating system information. 



### Terraform

To create a fully customized agent policy, use the `ops-agent-policy` module in the `modules` directory of the `terraform-google-cloud-operations` repository. This module requires the same information that the ``gcloud compute instances ops-agents policies` `create`` command requires. For a description of all the fields used to describe an agent policy, select the **Command-line** tab.

The `examples` directory in the `terraform-google-cloud-operations` repository contains files that provide many of the variables needed by the `ops-agent-policy` module for you. For more information, see Example policy configurations.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For information about how Terraform works, see [Using Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview).

## Verify the status of agent policies

This section describes how to check the status of created policies and the installation of the Ops Agent. This information can also help with troubleshooting your agent policies.

### Compute Engine **OS policies** page

The Compute Engine **OS policies** page provides information about the agent policies that manage the Ops Agent and about VMs on the **VM instances** tab. For example:

  * The **State** column indicates whether a policy was successfully installed ("Compliant"), in progress ("Pending"), possibly failed ("Unknown"), or missing ("No policies").
  * The **VM monitored** column indicates whether the Ops Agent is being managed by the OS Config ("Monitored") or not ("Not monitored"). 

If a policy is "Compliant" but the VM shows "Not monitored", then there might be a problem installing the Ops Agent. You might, for example, have a legacy agent already installed. 




In the Google Cloud console, go to the **OS policies** page: 

[Go to **OS policies**](https://console.cloud.google.com/compute/config/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

The **VM instances** on the Compute Engine **OS policies** tab shows information about agents managed by all OS policies in your Google Cloud project. These policies are labeled `goog-ops-agent-policy`. 

  * The `goog-ops-agent-policy` indicator includes several types of policies: 
    * Policies created by using the `gcloud compute instances ops-agents policies` commands.
    * Policies created for you if you requested [Ops Agent installation when you created the VM](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-agent-vm-creation).
    * Policies created by using Terraform to manage the Ops Agent.

To distinguish between policies, use the **OS policy assignments** tab on the page to see the policy IDs for all the policy assignments in your Google Cloud project.

  * This **VM monitored** column doesn't reflect the installation of the Ops Agent by other means, like manual installation or by [beta agent policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/managing-agent-policies).



### Cloud Monitoring **VM Instances** page

The **VM Instances** page in Cloud Monitoring includes an **Agent** column that lists the agent installed on each VM, and for the Ops Agent, includes an indicator for installed agents that are older than the latest version.

In the Google Cloud console, go to the **VM Instances** page: 

[Go to **VM Instances**](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

## Example policy configurations

This section describes examples for setting up agent policies when using either the Google Cloud SDK or Terraform.

### Command-line

### Example policy-description files

This section provides some examples of YAML policy-description files for a variety of scenarios. The examples assume that you put the YAML in a file named `agent-policy-description.yaml` and that you create the policy in the `us-central1-a` zone by using a command like the following:
    
    
    gcloud compute instances ops-agents policies create POLICY_ID \
      --zone us-central1-a \
      --file agent-policy-description.yaml \
      --project PROJECT_ID

### Install on all VMs

To install the latest version of the Ops Agent on all VMs in the `us-central1-a` zone, use the following policy description:
    
    
    agentsRule:
      packageState: installed
      version: latest
    instanceFilter:
      all: True

### Remove from all VMs

To remove the latest version of the Ops Agent on all VMs in the `us-central1-a` zone, use the following policy description:
    
    
    agentsRule:
      packageState: removed
      version: latest
    instanceFilter:
      all: True

### Install on VMs based on labels

To install the latest version of the Ops Agent on all VMs in the `us-central1-a` zone with the label "env=prod" or "app=web", use the following policy description:
    
    
    agentsRule:
      packageState: installed
      version: latest
    instanceFilter:
      inclusionLabels:
      - labels:
          env: prod
      - labels:
          app: web

When you specify multiple `labels:` entries for inclusion or exclusion, a VM matches if any of the labels is present; that is, the sets of labels for inclusion or exclusion are matched as a logical `OR` operation, not a logical `AND` operation.

### Install on VMs based on other labels

To install the latest version of the Ops Agent on all VMs in the `us-central1-a` zone running Debian 11, except those with the labels "env=prod" and "app=web6", use the following policy description:
    
    
    agentsRule:
      packageState: installed
      version: latest
    instanceFilter:
      exclusionLabels:
      - labels:
          env: prod
          app: web6
      inventories:
      - osShortName: debian
        osVersion: '11'

When you specify multiple key-value pairs under a single `labels:` entry for inclusion or exclusion, a VM matches if all of the labels are present; that is, the labels are matched as a logical `AND` operation, not a logical `OR` operation.

### Install on VMs based on operating system

To install the latest version 2 of the Ops Agent on all VMs running Debian 11 or RHEL 7.* in the `us-central1-a` zone, use the following policy description:
    
    
    agentsRule:
      packageState: installed
      version: 2.*.*
    instanceFilter:
      inventories:
      - osShortName: rhel
        osVersion: '7.*'
      - osShortName: debian
        osVersion: '11'

### Terraform

This section describes the examples in the `examples` directory of the `terraform-google-cloud-operations` repository. These examples contain files that configure many of the variables required by the `ops-agent-policy` module for you. You can also copy and modify the examples. For example, these examples all install the Ops Agent; you can modify them to delete the agent instead.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Example: `ops_agent_policy_install_all`

This example installs the latest version of the Ops Agent on all eligible VMs in your Google Cloud project.

When you run the `terraform plan` or `terraform apply` command, you are prompted for the following values: 

  * PROJECT_ID: The ID of your Google Cloud project



### Example: `ops_agent_policy_install_all_in_region`

This example installs the latest version of the Ops Agent on all eligible VMs in a given region, like `us-west1`. A region contains multiple zones, in this case, `us-west-1a`, `us-west-1b`, and `us-west-1c`. When you run the `terraform plan` or `terraform apply` command, you are prompted for the following values: 

  * PROJECT_ID: The ID of your Google Cloud project
  * REGION: The region in which to install the agent on VMs



### Example: `ops_agent_policy_install_all_in_zone`

This example installs the latest version of the Ops Agent on all eligible VMs in a given zone, like `us-central1-a`.

When you run the `terraform plan` or `terraform apply` command, you are prompted for the following values:

  * PROJECT_ID: The ID of your Google Cloud project
  * ZONE: The zone in which to install the agent on VMs



## Troubleshoot GA agent policies

This section provides information to help you resolve problems with GA agent policies for the Ops Agent. The information described in Verify the status of agent policies might also be helpful.

### The `ops-agents policy` commands fail

When a `gcloud compute instances ops-agents policies` command fails, the response shows a validation error. Correct the errors by fixing the command arguments and flags as suggested by the error message.

In addition to the validation errors, you might see errors that indicate the following conditions:

  * Insufficient IAM permission
  * The OS Config API isn't enabled
  * The specified policy doesn't exist



The following sections describe these conditions in more detail.

#### Insufficient IAM permission

If a `gcloud compute instances ops-agents policies` command fails with a permission error, then make sure you have run the `prepare-for-ops-agents-policies.sh` script as described in Before you begin to set up the OS Config policy roles: 

  * [ OSPolicyAssignment Admin (`roles/osconfig.osPolicyAssignmentAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin): Provides full access to OS policy assignments. 


  * [ OSPolicyAssignment Editor (`roles/osconfig.osPolicyAssignmentEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentEditor): Allows users to get, update, and list OS policy assignments. 


  * [ OSPolicyAssignment Viewer (`roles/osconfig.osPolicyAssignmentViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentViewer): Provides read-only access to get and list OS policy assignments. 



For more information about the `prepare-for-ops-agents-policies.sh` script, see The `prepare-for-ops-agents-policies.sh` script.

#### OS Config API isn't enabled

A sample error looks like the following:
    
    
    API [osconfig.googleapis.com] not enabled on project PROJECT_ID.
    Would you like to enable and retry (this will take a few minutes)?
    (y/N)?
    

You can enter `y` to enable the API, or you can run the `prepare-for-ops-agents-policies.sh` script, described in Before you begin, to grant all the necessary permissions. If you enter `y` at the prompt in the error message, then you still need to run the `prepare-for-ops-agents-policies.sh` script to set the needed permissions.

To verify that the OS Config API is enabled for the project, run the following commands:
    
    
    gcloud services list --project PROJECT_ID | grep osconfig.googleapis.com
    

The expected output follows:
    
    
    osconfig.googleapis.com    Cloud OS Config API
    

#### The policy already exists

A sample error looks like the following:
    
    
    ALREADY_EXISTS: Requested entity already exists
    

This error means this policy already exists with the same name, project ID and region. You can use the `gcloud compute instances ops-agents policies` `describe` command to confirm this.

#### The policy does not exist

A sample error looks like the following:
    
    
    NOT_FOUND: Requested entity was not found
    

This error might meant that the policy was never created, the policy has been deleted, or that the specified policy ID is incorrect. Make sure the POLICY_ID used in a `gcloud compute instances ops-agents policies` `describe`, `update` or `delete` command corresponds to an existing policy. To get a list of agent policies, use the `gcloud compute instances ops-agents policies` `list` command.

### The policy is created but seems to have no effect

OS Config agents are deployed to each Compute Engine instance to manage the packages for the Logging and Monitoring agents. The policy may seem to have no effect if the underlying OS Config agent isn't installed.

### Linux

To verify that the OS Config agent is installed, run the following command:
    
    
    gcloud compute ssh instance-id \
        --project project-id \
        -- sudo systemctl status google-osconfig-agent
    

A sample output is:
    
    
        google-osconfig-agent.service - Google OSConfig Agent
        Loaded: loaded (/lib/systemd/system/google-osconfig-agent.service; enabled; vendor preset:
        Active: active (running) since Wed 2020-01-15 00:14:22 UTC; 6min ago
        Main PID: 369 (google_osconfig)
         Tasks: 8 (limit: 4374)
        Memory: 102.7M
        CGroup: /system.slice/google-osconfig-agent.service
                └─369 /usr/bin/google_osconfig_agent
    

### Windows

To verify that the OS Config agent is installed, run the following steps:

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal, then run the following PowerShell command. You don't need administrator privileges.
         
         Get-Service google_osconfig_agent
         




A sample output is:
    
    
        Status   Name               DisplayName
        ------   ----               -----------
        Running  google_osconfig_a… Google OSConfig Agent
    

If the OS Config agent is not installed, then you might be using an operating system that doesn't support VM Manager. The Compute Engine [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager) document indicates which VM Manager features are supported for each Compute Engine operating system.

If the operating system supports VM Manager, then you can [install the OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#agent-install) manually.

### The OS Config agent is installed but does not install the Ops Agent

To verify if there are any errors when the OS Config agent applies policies, you can check the OS Config agent's log. This can be done either by using Logs Explorer or using SSH or RDP to check individual Compute Engine instances.

To view OS Config agent logs in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), use the following filter:
    
    
    resource.type="gce_instance"
    logId(OSConfigAgent)
    

To view OS Config agent logs, do the following:

###  CentOS, RHEL,  
SLES, SUSE

Run the following command: 
    
    
    gcloud compute ssh INSTANCE_ID \
        --project PROJECT_ID \
        -- sudo cat /var/log/messages \
           | grep "OSConfigAgent\|google-fluentd\|stackdriver-agent"
    

###  Debian, Ubuntu

Run the following command: 
    
    
    gcloud compute ssh INSTANCE_ID \
        --project PROJECT_ID \
        -- sudo cat /var/log/syslog \
           | grep "OSConfigAgent\|google-fluentd\|stackdriver-agent"
    

### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open the Event Viewer app, then select **Windows Logs** > **Application** , and search for logs with `Source` equal to `OSConfigAgent`.




If there is an error connecting to the OS Config service, make sure you run the `prepare-for-ops-agents-policies.sh` script as described in Before you begin to set up the OS Config metadata.

To verify that the OS Config metadata is enabled, you can run the following command:
    
    
    gcloud compute project-info describe \
        --project PROJECT_ID \
        | grep "enable-osconfig\|enable-guest-attributes" -A 1
    

The expected output follows:
    
    
    - key: enable-guest-attributes
      value: 'TRUE'
    - key: enable-osconfig
      value: 'TRUE'
    

### The Ops Agent is installed but not functioning properly

For more information about debugging Ops Agent problems, see [Troubleshoot the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshooting).

## Enable debug-level logs for the OS Config agent

It can be useful to enable debug-level logging in the OS Config agent when reporting an issue.

You can set the `osconfig-log-level: debug` metadata to enable debug-level logging for the OS Config agent. The collected logs have more information to help with the investigation.

To enable debug-level logging for the entire project, run the following command:
    
    
    gcloud compute project-info add-metadata \
        --project PROJECT_ID \
        --metadata osconfig-log-level=debug
    

To enable debug-level logging for one VM, run the following command:
    
    
    gcloud compute instances add-metadata INSTANCE_ID \
        --project PROJECT_ID \
        --metadata osconfig-log-level=debug
    

## Helper scripts

This section provides additional information about the helper scripts described in this document:

  * The `prepare-for-ops-agents-policies.sh` script
  * The `diagnose_policies.sh` script



### The `prepare-for-ops-agents-policies.sh` script

After you download the [`prepare-for-ops-agents-policies.sh`](https://docs.cloud.google.com/static/stackdriver/docs/prepare-for-ops-agents-policies.sh) script, you can use the script to perform the following actions, based on the arguments you provide:

  * Enable the Cloud Logging API, the Cloud Monitoring API, and the OS Config API for the project. 

If the OS Config API was not already enabled, it is enabled in limited-feature mode, which is sufficient for managing agent policies. For more information, see Pricing. 

  * Grant the Identity and Access Management roles [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions#logging.logWriter) and [Monitoring Metric Writer (`roles/monitoring.metricWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions#monitoring.metricWriter) to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) so that the agents can write logs and metrics to the Logging and Cloud Monitoring APIs.

  * Enable the OS Config metadata for the project so that the OS Config agent on each VM is active.

  * Grant one of the following IAM roles to the non-owner users user or service account needed to create and manage policies. Project owners have full access to create and manage policies; all other users or service accounts must be granted one of the following roles: 

    * [ OSPolicyAssignment Admin (`roles/osconfig.osPolicyAssignmentAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin): Provides full access to OS policy assignments. 
    * [ OSPolicyAssignment Editor (`roles/osconfig.osPolicyAssignmentEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentEditor): Allows users to get, update, and list OS policy assignments. 
    * [ OSPolicyAssignment Viewer (`roles/osconfig.osPolicyAssignmentViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentViewer): Provides read-only access to get and list OS policy assignments. 

When running the script, you can specify the OSPolicyAssignment roles as `admin`, `editor`, or `viewer`. The script maps those values to the `roles/osconfig.osPolicyAssignment*` role names. 




The following examples show some common invocations for the script. For more information, see the comments in the script itself.

To enable the APIs, grant the necessary roles to the default service account, and enable the OS Config metadata for a project, run the script as follows:
    
    
    bash prepare-for-ops-agents-policies.sh --project=PROJECT_ID
    

To additionally grant one of the OS Config roles to a user who does not have the Owner (`roles/owner`) role on the project, run the script as follows:
    
    
    bash prepare-for-ops-agents-policies.sh --project=PROJECT_ID \
      --iam-user=USER_EMAIL \
      --iam-policy-access=[admin|editor|viewer]
    

To additionally grant one of the OS Config roles to a non-default service account, run the script as follows:
    
    
    bash prepare-for-ops-agents-policies.sh --project=PROJECT_ID \
      --iam-service-account=SERVICE_ACCT_EMAIL \
      --iam-policy-access=[admin|editor|viewer]
    

### The `diagnose_policies.sh` script

Given a project ID, a Compute Engine instance ID, a Compute Engine zone, and the agent policy ID, the [`diagnose_policies.sh`](https://docs.cloud.google.com/static/stackdriver/docs/diagnose_policies.sh) script automatically collects the necessary information to help diagnose issues with the policy:

  * The OS Config agent version 
  * The underlying OS policy assignment
  * The OS policy assignments that are applicable to this Compute Engine instance
  * A description of this Compute Engine instance 



To invoke the script, run the following command:
    
    
    bash diagnose_policies.sh --project-id=PROJECT_ID \ 
      --gce-instance-id=INSTANCE_ID \
      --policy-id=POLICY_ID \
      --zone=ZONE
    

## Pricing

The `gcloud compute instances ops-agents policies` commands are implemented by using [OS policy assignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicyAssignment) resources from [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager). The `prepare-for-ops-agents-policies.sh` script, described in Before you begin, sets up VM Manager in [limited-feature mode (`OSCONFIG_B`)](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/ProjectFeatureSettings#PatchAndConfigFeatureSet.ENUM_VALUES.OSCONFIG_B), which is sufficient for creating and managing agent policies. There is no cost to use VM Manager in limited mode.

If you have configured VM Manager in full-feature mode (`OSCONFIG_C`), then you might incur costs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
