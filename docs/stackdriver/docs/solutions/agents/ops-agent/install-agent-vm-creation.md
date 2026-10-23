---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vm-creation/
title: Install the Ops Agent during VM creation \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:38.879577+00:00
---

# Install the Ops Agent during VM creation  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vm-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Install the Ops Agent during VM creation Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how the Google Cloud console can automatically install the Ops Agent for you when you create a VM instance. During the installation process, the Compute Engine [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) creates an Ops Agent OS policy that installs the agent and reinstalls it when necessary. The VM Manager helps you get the Ops Agent running on your VM and ensures that the agent is always installed.

## Overview

The VM Manager uses OS policies to manage the Ops Agent installation. A configuration policy is applied to a VM by using a mapping called an _assignment ID_ , which looks like the following example:
    
    
    goog-ops-agent-v2-x86-template-1-0-0-ZONE
    

An assignment ID for an Ops Agent OS policy consists of the following components:

  * The name of the policy: "goog-ops-agent"
  * A template for creating the policy: "v2-x86-template"
  * A version string for the template. The version, which might change over time, is a value like "1-0-0".
  * The zone to which the assignment ID applies, a value like "us-central1-a".



A VM is associated with an assignment ID by using the labels on the VM instance. A Compute Engine VM is a monitored resource of type [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance) and includes a `zone` label. When you use the Google Cloud console to create a VM with the Ops Agent installed, the VM Manager adds another label to the VM, which looks like `goog-ops-agent-policy:v2-x86-template-1-0-0`. This label identifies the policy, template, and version:

  * Label key, the identifier for the policy: `goog-ops-agent-policy`
  * Label value, the policy template and version: `v2-x86-template-1-0-0`



When you create a VM in the Google Cloud console, you can select the **Install Ops Agent for Monitoring and Logging** checkbox. When you click **Create** , VM Manager assigns the VM a label of `goog-ops-agent-policy:v2-x86-template-1-0-0` and installs the Ops Agent. If the VM is the first VM in its zone, then VM Manager also creates an Ops Agent OS policy and an Ops Agent OS policy assignment for that zone.

While a zone has an Ops Agent OS policy assignment, the Ops Agent OS policy monitors VMs that have the following characteristics:

  * The VM has the `goog-ops-agent-policy:v2-x86-template-1-0-0` label.
  * The VM is in the same zone as the Ops Agent OS policy assignment.



The Ops Agent OS policy checks every hour whether its covered VMs have the Ops Agent installed. If the Ops Agent isn't installed, then the Ops Agent OS policy installs the latest version of the agent.

## Create a VM with automatic installation of the Ops Agent

To install the Ops Agent automatically during VM creation and apply the Ops Agent OS policy assignment to the VM, do the following:

  1. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/osconfig.osPolicyAssignmentEditor`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  2. Follow the steps in [Create a VM instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage). Before you click **Create** , select the **Install Ops Agent for Monitoring and Logging** checkbox: 

![The Install Ops Agent for Monitoring and Logging checkbox.](https://docs.cloud.google.com/static/stackdriver/images/ops_agent_auto_install.png)

**Note:** When you select the **Install Ops Agent for Monitoring and Logging** checkbox during VM creation, the examples on the tabs in the **Equivalent code** flyout are updated to include the steps for creating the Ops Agent OS policy. There is no REST equivalent for creating an Ops Agent OS policy.
  3. Click **Create**. 

When you install the Ops Agent automatically for the first time in a zone, if you don't have VM Manager enabled for your Google Cloud project, then the VM-creation process does the following:

     1. Enables VM Manager to operate in [restricted mode](https://docs.cloud.google.com/compute/docs/vm-manager#pricing).
     2. Creates the Ops Agent OS policy and an Ops Agent OS policy assignment for the zone. The Ops Agent OS policy is a field of the policy assignment.
     3. Enables Patch, OS policies, and OS inventory management by setting the VM metadata label `enable-osconfig` to `TRUE`.
     4. Creates the VM and assigns it the Ops Agent OS policy label.

If you create a VM and automatically install the Ops Agent in a zone where an Ops Agent OS policy assignment already exists, then the VM-creation process creates the VM and assigns it the Ops Agent OS policy label.




## Example

Your Google Cloud project doesn't have any Ops Agent OS policy assignments. You create two VMs, _instance-1_ and _instance-2_ in the `us-central1-a` zone. You then create _instance-3_ and _instance-4_ in the `us-east1-b` zone. _instance-1_ , _instance-2_ , and _instance-3_ had the **Install Ops Agent for Monitoring and Logging** checkbox selected during creation.

  * When you create _instance-1_ , VM Manager creates an Ops Agent OS policy for the `us-central1-a` zone and an OS policy assignment with the ID `goog-ops-agent-v2-x86-template-1-0-0-us-central1-a`. VM Manager then sets the policy label on _instance-1_.
  * When you create _instance-2_ , VM Manager sets the same policy label on _instance-2_.
  * When you create _instance-3_ , VM Manager creates an Ops Agent OS policy for the `us-east1-b` zone and an OS policy assignment with the ID `goog-ops-agent-v2-x86-template-1-0-0-us-east1-b`. VM Manager then assigns the policy label to _instance-3_.



The Ops Agent OS policies then cover the following VMs based on the Ops Agent OS policy assignment IDs:

OS Policy Assignment ID | Covers VMs In: | Covered VMs  
---|---|---  
goog-ops-agent-v2-x86-template-1-0-0-us-central1-a | us-central1-a | _instance-1_ , _instance-2_  
goog-ops-agent-v2-x86-template-1-0-0-us-east1-b | us-east1-b | _instance-3_  
  
By default, _instance-4_ isn't covered because you didn't select **Install Ops Agent for Monitoring and Logging** , so it doesn't have the `goog-ops-agent-policy:v2-x86-template-1-0-0` label. If you also want to apply the Ops Agent OS policy to _instance-4_ , then see [Add Ops Agent OS policy coverage to an existing VM](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-policies-auto-install#add-coverage).

## Manage Ops Agent versions on VMs covered by the Ops Agent OS policy

The Ops Agent OS policy doesn't update the Ops Agent when new versions of the agent are released. As long as the VM has some version of the Ops Agent installed, the policy does nothing. If you uninstall the Ops Agent, then the policy detects that the Ops Agent isn't installed and then installs the latest version.

To upgrade your VM to the latest version of the Ops Agent, uninstall the version that you are currently running and let the Ops Agent OS policy install the latest version.

If you need to install a previous version of the Ops Agent, you can [uninstall the Ops Agent on VMs covered by the Ops Agent OS policy](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-policies-auto-install#uninstall) and then [install a specific version of the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#install-specific-version).

## Troubleshooting

For information about troubleshooting agent installation and Ops Agent OS policies, see [Manage VMs covered by the Ops Agent OS policy](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-policies-auto-install) and [Agent diagnostics tool for automatic installation policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#agent_diagnostics_tool_for_automatic_installation_policies).

## Pricing

OS policies are generic tools for installing packages. By default, when VM Manager is enabled because you've created a VM with the Ops Agent automatically installed, VM Manager is enabled in the limited mode. For information about VM Manager modes and pricing, see [VM Manager Pricing](https://docs.cloud.google.com/compute/docs/vm-manager#pricing).

## What's next

For information about managing VMs covered by the Ops Agent OS policy, see [Manage VMs covered by the Ops Agent OS policy](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-policies-auto-install).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
