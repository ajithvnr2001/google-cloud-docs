---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/manage-policies-auto-install/
title: Manage VMs covered by the Ops Agent OS policy \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:40.195649+00:00
---

# Manage VMs covered by the Ops Agent OS policy  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/manage-policies-auto-install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Manage VMs covered by the Ops Agent OS policy Stay organized with collections  Save and categorize content based on your preferences. 

If you created Compute Engine VMs with the Ops Agent installed during creation or, in some cases, if you [installed the agent on existing VMs by using the Google Cloud console](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#gce-ui-install), then Google Cloud also created VM Manager OS policies that install and monitor the Ops Agent. This document describes how to query those Ops Agent OS policies and manage the Ops Agent on VMs covered by the policies. For information about creating VMs with the Ops Agent automatically installed, see [Install the Ops Agent during VM creation](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-agent-vm-creation).

After an Ops Agent OS policy has been created, you can do the following:

  * Determine which VMs are covered by the policy.
  * Determine which zones are covered by the policy.
  * Extend policy coverage to existing VMs.
  * Uninstall the agent from a VM covered by the policy.



## Find VMs covered by Ops Agent OS policies

You can use the Google Cloud console or the Google Cloud CLI to see which VMs in your Google Cloud project are covered by Ops Agent OS policies through an OS policy assignment. If you believe a VM is missing coverage, you can troubleshoot by doing the following:

  * [Verify that a VM has an Ops Agent OS policy label](https://docs.cloud.google.com/monitoring/agent/ops-agent/manage-policies-auto-install#view-label).
  * [Verify that an Ops Agent OS policy assignment was successfully rolled out](https://docs.cloud.google.com/monitoring/agent/ops-agent/manage-policies-auto-install#view-assignments).



### Verify that an Ops Agent OS policy is assigned to VMs in a zone

To verify that the VMs in a zone are covered by the Ops Agent OS policy, use either the Google Cloud console or the gcloud CLI to see whether the VM is related to an Ops Agent OS policy assignment.

###  Console 

  1. In the Google Cloud console, go to the **OS policies** page: 

[Go to **OS policies**](https://console.cloud.google.com/compute/config/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. On the **VM instances** tab, select the VM that you want to check.

  3. If the VM is covered by an Ops Agent OS policy, then the **OS policy id** column includes `goog-ops-agent-policy` and the state is "Compliant".




###  gcloud 

To display a list of Ops Agent OS policy assignments in a zone, run the following command:
    
    
    gcloud compute os-config os-policy-assignment-reports list --location=ZONE --filter="ASSIGNMENT_ID ~ goog-ops-agent"
    

The output shows a list of VMs with an Ops Agent OS policy assignment. If the Ops Agent is installed on the VM, the Summary column has a value of "1/1 policies compliant".
    
    
    INSTANCE    ASSIGNMENT_ID                                    LOCATION    UPDATE_TIME                  SUMMARY
    instance-1  goog-ops-agent-v2-x86-template-1-0-0-us-east4-c  us-east4-c  2023-04-28T02:11:15.118088Z  1/1 policies compliant
    instance-3  goog-ops-agent-v2-x86-template-1-0-0-us-east4-c  us-east4-c  2023-04-28T02:11:15.118088Z  1/1 policies compliant
    

### Verify that a VM has an Ops Agent OS policy label

To see which VMs in your Google Cloud project have the Ops Agent OS policy label, `goog-ops-agent-policy`, use either the Google Cloud console or the gcloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select the name of your VM.

  3. In the **Basic information** panel, locate the **Labels** entry.

If the VM is covered by the Ops Agent OS policy, then it has a label like `goog-ops-agent-policy:v2-x86-template-1-0-0`.




###  gcloud 

To see all the VMs that have the Ops Agent OS policy label `goog-ops-agent-policy`, run the following command:
    
    
    gcloud compute instances list --format="table(name,zone,labels)" --filter="labels=goog-ops-agent-policy"
    

The output shows the name, zone, and labels of the VMs. For example:
    
    
    NAME                  ZONE           LABELS
    test-vm1              us-central1-a  {'goog-ops-agent-policy': 'v2-x86-template-1-0-0'}
    test-vm1              us-east4-c     {'goog-ops-agent-policy': 'v2-x86-template-1-0-0'}
    

To see whether a specific VM has the Ops Agent OS policy label, run the following command:
    
    
    gcloud compute instances describe --format "yaml(labels)" --zone=ZONE VM_NAME
    

The output shows a list of labels for your VM. If your VM has the Ops Agent OS policy label, then `goog-ops-agent-policy` appears in the `labels` list. For example:
    
    
    labels:
      goog-ops-agent-policy: v2-x86-template-1-0-0
    

### Verify that an Ops Agent OS policy assignment was successfully rolled out

View your Google Cloud project OS policy assignments to verify that an Ops Agent OS policy assignment was correctly deployed to a specific zone.

###  Console 

  1. In the Google Cloud console, go to the **OS policies** page: 

[Go to **OS policies**](https://console.cloud.google.com/compute/config/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. To see the state of OS policy rollouts, click the **OS policy assignments** tab.

Ops Agent OS policy assignments have IDs that start with the string "goog-ops-agent". If the assignment was rolled out successfully, then it has a rollout state of "Succeeded".




###  gcloud 

To view all Ops Agent OS policy assignments in a zone, run the following command:
    
    
    gcloud compute os-config os-policy-assignments list --location=ZONE --filter="ASSIGNMENT_ID ~ goog-ops-agent"
    

The output shows a list of Ops Agent OS policy assignments in a zone. If the assignment was rolled out successfully, then it has a rollout state of "SUCCEEDED". For example:
    
    
    ASSIGNMENT_ID                                       ROLLOUT_STATE    REVISION_CREATE_TIME       REVISION_ID    
    goog-ops-agent-v2-x86-template-1-4-0-us-central1-b  SUCCEEDED        2023-01-28T05:23:41Z.      940df3e9-77fd-470b-84df-53fb24825c4a
    goog-ops-agent-v2-x86-template-1-0-0-us-central1-b  SUCCEEDED        2022-01-28T05:23:41Z.      qwareaff-efte-erew-aeet-faer234t4gga
    

To view details about a specific Ops Agent OS policy assignment, run the following command:
    
    
    gcloud compute os-config os-policy-assignments describe POLICY_ASSIGNMENT_ID --location=ZONE
    

## Uninstall the Ops Agent on VMs covered by the Ops Agent OS policy

If you manually [uninstall the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#uninstall) on a VM covered by the Ops Agent OS policy, then the policy re-installs it. To uninstall the Ops Agent, you must first remove the `goog-ops-agent-policy` label from the VM. After you have removed the Ops Agent OS policy label from a VM, you can uninstall the Ops Agent permanently.

### Uninstall the Ops Agent on a specific VM

To remove the policy and uninstall the Ops Agent from a specific VM, you can use the Google Cloud console or the gcloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select the name of the VM that you want to edit.

  3. Click **Edit**.

  4. Go to the **Labels** section and then click **\+ Add Labels**.

  5. Locate the label with the key `goog-ops-agent-policy` and click **Delete item**.

  6. [Uninstall the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#uninstall).




###  gcloud 

  1. To remove the `goog-ops-agent-policy` label from a VM, run the following command:
         
         gcloud compute instances update VM_NAME \
           --remove-labels=goog-ops-agent-policy
         

  2. [Uninstall the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#uninstall).




### Uninstall the Ops Agent on all VMs

To uninstall the Ops Agent from VMs in zone that has an Ops Agent OS policy assignment, use the script provided by Cloud Monitoring. You can't uninstall the agent from a group of VMs by using the Google Cloud console.

To run the script, you must have the [GuestPolicy Editor role](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyEditor) (`roles/osconfig.guestPolicyEditor`).

Run the following script in Cloud Shell. You can provide any number of zones:
    
    
    curl -sSO https://dl.google.com/cloudagents/undo-ops-agent-policies.sh
    bash undo-ops-agent-policies.sh ZONE1 ZONE2
    

The script performs the following tasks in each zone:

  1. Finds all Ops Agent OS policies.
  2. Edits each policy so that it uninstalls the Ops Agent on its covered VMs.
  3. Deletes the Ops Agent OS policy.
  4. Removes the `goog-ops-agent-policy` label from each covered VM.



## Add Ops Agent OS policy coverage to an existing VM

The Ops Agent OS policy covers only VMs that have the `goog-ops-agent-policy` label and are in the same zone as an existing Ops Agent OS policy assignment. However, you can extend coverage to other VMs that were created without the Ops Agent OS policy assigned to them.

To extend policy coverage to a VM, you need to know the template version of the Ops Agent OS policy assignment in your zone. If your zone has multiple Ops Agent OS policy assignments, then find the assignment with the latest template version. To show a list of Ops Agent OS policy assignments in a zone, run the following command:
    
    
    gcloud compute os-config os-policy-assignments list --location=ZONE
      --filter="ASSIGNMENT_ID ~ goog-ops-agent"
    

To extend policy coverage to other VMs, use either the Google Cloud console or the gcloud CLI:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. In the **VM instances** list, select the checkboxes next to the VMs that you want to label and then click **Labels**.

  3. To add labels, click **+Add label** and add the key-value pair. The key must be `goog-ops-agent-policy` and the value is the desired template version, such as `1-0-0`.

  4. Save your changes.




###  gcloud 

To extend policy coverage to a VM without coverage, run the following commands:
    
    
    gcloud compute instances update VM_NAME --zone=ZONE
      --update-labels=goog-ops-agent-policy:v2-x86-template-1-0-0
    
    
    
    gcloud compute instances add-metadata VM_NAME --zone=ZONE
      --metadata=enable-osconfig=TRUE
    

## Permission

Ops Agent installation uses VM Manager and requires permissions to activate the VM Manager API and create a policy. The required permissions are all available using the [Editor role](https://docs.cloud.google.com/iam/docs/understanding-roles#editor) (`roles/Editor`). Or you can ask a project administrator to grant the minimal permissions using the Google Cloud CLI.

Required permissions for installing the Ops Agent during VM creation:

  * `serviceusage.services.get`
  * `serviceusage.services.enable`
  * `osconfig.osPolicyAssignments.get`
  * `osconfig.osPolicyAssignments.create`
  * `osconfig.projectFeatureSettings.update`
  * `compute.instances.create`



Required permissions for installing Ops Agent on existing VMs:

  * `serviceusage.services.get`
  * `serviceusage.services.enable`
  * `osconfig.osPolicyAssignments.get`
  * `osconfig.osPolicyAssignments.create`
  * `osconfig.projectFeatureSettings.update`
  * `compute.instances.setMetadata`
  * `compute.instances.setLabels`



You can find corresponding roles that provide those permissions in the [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

Sample commands to grant roles for permissions:
    
    
    gcloud projects add-iam-policy-binding project-id --member='user:user-email' --role='roles/osconfig.projectFeatureSettingsEditor'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
