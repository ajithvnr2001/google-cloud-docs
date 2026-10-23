---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/managing-agent-policies/
title: Use agent policies (beta) \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:58.566399+00:00
---

# Use agent policies (beta)  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/managing-agent-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Use agent policies (beta) Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You create and manage agent policies by using the [`gcloud beta compute instances ops-agents policies`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies) command group in the Google Cloud CLI or the [`agent-policy` Terraform module](https://github.com/terraform-google-modules/terraform-google-cloud-operations/tree/master/modules/agent-policy). Agent policies use the [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) suite of tools in Compute Engine to manage [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management), which can automate the deployment and maintenance of software configurations like the Google Cloud Observability agents: the Ops Agent, the legacy Monitoring agent, and the legacy Logging agent. **Caution:** As of September 28, 2026, the legacy Monitoring and Logging agents have reached their end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

**Note:** This document describes the beta agent policies. For new policies, we recommend that you use [ VM Extension Manager policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-vmem-policies) for fleet-wide installation and management of the Ops Agent. With VM extension policies, you can provide and manage custom configuration for the Ops Agent and manage version control, including auto-upgrades and version pinning. Extension policies can be applied zonally or globally, across all zones in a Google Cloud project. 

VM Extension Manager policies are available in a preview release. If your environment requires the stability of GA releases, then we recommend that you use GA agent policies to manage the Ops Agent. For information about the GA agent policies, see [Use agent policies (GA).](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies)

## Create an agent policy

This section describes using the Google Cloud SDK for managing agent policies. For information about using Terraform, see Terraform integration.

To create an agent policy by using the Google Cloud CLI, complete the following steps:

  1. If you haven't done so already, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

The agent policies described in this document use the `beta` command group.

  2. If you haven't done so already, install the `beta` component of the gcloud CLI:
         
         gcloud components install beta
         

To check if you have the `beta` component for the installed, run:
         
         gcloud components list
         

If you previously installed the `beta` component, ensure you have the latest version:
         
         gcloud components update
         

  3. Download and use the following script to enable the APIs and to set the proper permissions for using the Google Cloud CLI: [`set-permissions.sh`](https://docs.cloud.google.com/static/stackdriver/docs/set-permissions.sh).

For information about the script, refer to The `set-permissions.sh` script.

**Note:** The `set-permissions.sh` script is designed to run on Linux. If you're using a machine on a different operating system, then run the script from [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).
  4. Use the `gcloud beta compute instances ops-agents policies` `create` command to create a policy. For the syntax of the command, see the [`gcloud beta compute instances ops-agents policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies/create#SYNOPSIS) documentation.

For examples showing how to format the command, see the [Examples](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies/create#EXAMPLES) section in the Google Cloud CLI documentation.

For more information about the other commands in the command group and the available options, see the [`gcloud beta compute instances ops-agents policies`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies) documentation.




### Best practices for using agent policies

To control the impact to production systems during rollout, we recommend that you use instance labels and zones to filter the instances that the policy applies to.

If you're creating a policy for the Ops Agent, ensure that your VMs don't have the legacy Logging agent or Monitoring agent installed on them. Running the Ops Agent and the legacy agents on the same VM can cause ingestion of duplicate logs or a conflict in metrics ingestion. If necessary, [uninstall the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/installation#uninstall) and [uninstall the Logging agent](https://docs.cloud.google.com/logging/docs/agent/installation#uninstall) before creating a policy to install the Ops Agent. 

Here is an example of a phased rollout plan for Debian 11 VMs in a project called `my_project`:

Phase 1: Create a policy named `ops-agents-policy-safe-rollout` to install the Ops Agent on all VMs with the labels `env=test` and `app=myproduct`.
    
    
    gcloud beta compute instances \
        ops-agents policies create ops-agents-policy-safe-rollout \
        --agent-rules="type=ops-agent,version=current-major,package-state=installed,enable-autoupgrade=true" \
        --os-types=short-name=debian,version=11 \
        --group-labels=env=test,app=myproduct \
        --project=my_project
    

For more information about specifying the operating system, see [`gcloud beta compute instances ops-agents policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies/create#--os-types).

Phase 2: Update that policy to target VMs in a single zone that have the labels `env=prod` and `app=myproduct`.
    
    
    gcloud beta compute instances \
        ops-agents policies update ops-agents-policy-safe-rollout \
        --group-labels=env=prod,app=myproduct \
        --zones=us-central1-c \
    

Phase 3: Update that policy to clear the zones filter so it rolls out globally
    
    
    gcloud beta compute instances \
        ops-agents policies update ops-agents-policy-safe-rollout \
        --clear-zones
    

### Policies on VMs that predate OS Config

You might need to manually install and configure the OS Config agent on VMs that predate OS Config. For information about manually installing and verifying the OS Config agent, see the [VM Manager verification checklist](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-manager/verify-setup#manual-check). 

## Troubleshoot beta agent policies

This section provides information to help you resolve problems with beta agent policies for the Ops Agent, the legacy Monitoring agent, and the legacy Logging agent.

### The `ops-agents policy` commands fail

When a `gcloud beta compute instances ops-agents policies` command fails, the response shows a validation error. Correct the errors by fixing the command arguments and flags as suggested by the error message.

In addition to the validation errors, you might see errors that indicate the following conditions:

  * Insufficient IAM permission
  * The OS Config API isn't enabled
  * The specified policy doesn't exist



The following sections describe these conditions in more detail.

#### Insufficient IAM permission

If a `gcloud beta compute instances ops-agents policies` command fails with a permission error, then make sure you have run the `set-permissions.sh` script as described in Create an agent policy to set up the OS Config policy roles: 

  * [ GuestPolicy Admin (`roles/osconfig.guestPolicyAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyAdmin): Provides full access to guest policies. 
  * [ GuestPolicy Editor (`roles/osconfig.guestPolicyEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyEditor): Allows users to get, update, and list guest policies. 
  * [ GuestPolicy Viewer (`roles/osconfig.guestPolicyViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyViewer): Provides read-only access to get and list guest policies. 



For more information about the `set-permissions.sh` script, see The `set-permissions.sh` script.

#### OS Config API isn't enabled

A sample error looks like the following:
    
    
    API [osconfig.googleapis.com] not enabled on project PROJECT_ID.
    Would you like to enable and retry (this will take a few minutes)?
    (y/N)?
    

You can enter `y` to enable the API, or you can run the `set-permissions.sh` script, described in Create an agent policy, to grant all the necessary permissions. If you enter `y` at the prompt in the error message, then you still need to run the `set-permissions.sh` script to set the needed permissions.

To verify that the OS Config API is enabled for the project, run the following commands:
    
    
    gcloud services list --project PROJECT_ID | grep osconfig.googleapis.com
    

The expected output follows:
    
    
    osconfig.googleapis.com    Cloud OS Config API
    

#### The policy already exists

A sample error looks like the following:
    
    
    ALREADY_EXISTS: Requested entity already exists
    

This error means this policy already exists with the same name, project ID and region. You can use the `gcloud beta compute instances ops-agents policies` `describe` command to confirm this.

#### The policy does not exist

A sample error looks like the following:
    
    
    NOT_FOUND: Requested entity was not found
    

This error might meant that the policy was never created, the policy has been deleted, or that the specified policy ID is incorrect. Make sure the POLICY_ID used in a `gcloud beta compute instances ops-agents policies` `describe`, `update` or `delete` command corresponds to an existing policy. To get a list of agent policies, use the `gcloud beta compute instances ops-agents policies` `list` command.

### The policy is created, but seems to have no effect

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

### The OS Config agent is installed, but it does not install the Ops Agent

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




If there is an error connecting to the OS Config service, make sure you run the `set-permissions.sh` script as described in Create an agent policy to set up the OS Config metadata.

To verify that the OS Config metadata is enabled, you can run the following command:
    
    
    gcloud compute project-info describe \
        --project PROJECT_ID \
        | grep "enable-osconfig\|enable-guest-attributes" -A 1
    

The expected output follows:
    
    
    - key: enable-guest-attributes
      value: 'TRUE'
    - key: enable-osconfig
      value: 'TRUE'
    

### The Ops Agent is installed, but not functioning properly

For more information about debugging Ops Agent problems, see [Troubleshoot the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshooting)

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

  * The `set-permissions.sh` script
  * The `diagnose.sh` script



### The `set-permissions.sh` script

After you download the [`set-permissions.sh`](https://docs.cloud.google.com/static/stackdriver/docs/set-permissions.sh) script, you can use the script to perform the following actions, based on the arguments you provide:

  * Enable the Cloud Logging API, the Cloud Monitoring API, and the OS Config API for the project. 

  * Grant the Identity and Access Management roles [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions#logging.logWriter) and [Monitoring Metric Writer (`roles/monitoring.metricWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions#monitoring.metricWriter) to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) so that the agents can write logs and metrics to the Logging and Cloud Monitoring APIs.

  * Enable the OS Config metadata for the project so that the OS Config agent on each VM is active.

  * Grant one of the following IAM roles to the non-owner users user or service account needed to create and manage policies. Project owners have full access to create and manage policies; all other users or service accounts must be granted one of the following roles: 

    * [ GuestPolicy Admin (`roles/osconfig.guestPolicyAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyAdmin): Provides full access to guest policies. 
    * [ GuestPolicy Editor (`roles/osconfig.guestPolicyEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyEditor): Allows users to get, update, and list guest policies. 
    * [ GuestPolicy Viewer (`roles/osconfig.guestPolicyViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyViewer): Provides read-only access to get and list guest policies. 

When running the script, you only need to specify the `guestPolicy*` part of the role name. The script supplies the `roles/osconfig.` part of the name. 




The following examples show some common invocations for the script. For more information, see the comments in the script itself.

To enable the APIs, grant the necessary roles to the default service account, and enable the OS Config metadata for a project, run the script as follows:
    
    
    bash set-permissions.sh --project=PROJECT_ID
    

To additionally grant one of the OS Config roles to a user who does not have the Owner (`roles/owner`) role on the project, run the script as follows:
    
    
    bash set-permissions.sh --project=PROJECT_ID \
      --iam-user=USER_EMAIL \
      --iam-permission-role=guestPolicy[Admin|Editor|Viewer]
    

To additionally grant one of the OS Config roles to a non-default service account, run the script as follows:
    
    
    bash set-permissions.sh --project=PROJECT_ID \
      --iam-service-account=SERVICE_ACCT_EMAIL \
      --iam-permission-role=guestPolicy[Admin|Editor|Viewer]
    

### The `diagnose.sh` script

Given a project ID, a Compute Engine instance ID, and the agent policy ID, the [`diagnose.sh`](https://docs.cloud.google.com/static/stackdriver/docs/diagnose.sh) script automatically collects the necessary information to help diagnose issues with the policy:

  * The OS Config agent version 
  * The underlying OS Config guest policy
  * The policies that are applicable to this Compute Engine instance
  * The agent package repositories that are pulled on to this Compute Engine instance 



To invoke the script, run the following command:
    
    
    bash diagnose.sh --project-id=PROJECT_ID \ 
      --gce-instance-id=INSTANCE_ID \
      --policy-id=POLICY_ID 
    

## Terraform integration

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For information about how Terraform works, see [Using Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview).

Terraform support for agent policies is built on top of the Google Cloud CLI commands. To create an agent policy by using Terraform, follow the Terraform module [`agent-policy` instructions](https://github.com/terraform-google-modules/terraform-google-cloud-operations/tree/master/modules/agent-policy/README.md). You can also find example policies in the [`examples` directory](https://github.com/terraform-google-modules/terraform-google-cloud-operations/tree/master/examples).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
