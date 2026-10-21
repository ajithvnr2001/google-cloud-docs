---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-agent-vmem-policies/
title: Troubleshoot VM Extension Manager policies for the Ops Agent \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:43.082521+00:00
---

# Troubleshoot VM Extension Manager policies for the Ops Agent  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-agent-vmem-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot VM Extension Manager policies for the Ops Agent Stay organized with collections  Save and categorize content based on your preferences. 

To diagnose problems with VM Extension Manager policies that manage the Ops Agent, use the troubleshooting techniques described in this document. For information about troubleshooting the Ops Agent, see [Troubleshoot the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshooting).

## ``gcloud compute zone-vm-extension-policies`` commands fail

When a ``gcloud compute zone-vm-extension-policies`` command fails, the response includes troubleshooting suggestions. Correct any errors in the command flags or arguments suggested by the error message.

If the output of the command mentions insufficient IAM permissions, then review the necessary roles and permissions described in [Grant the roles required to use VM Extension Manager](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-agent-vmem-policies#grant-roles-vmem).

## The extension policy is created, but the Ops Agent status is "not detected"

You successfully created an extension policy, but the Ops Agent shows a "not detected" [status](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-agent-vmem-policies#verify-agent-status) on the VM.

The Ops Agent might show as "not detected" if either of the following occurs:

  * The extension policy fails to install the Ops Agent.
  * An installed Ops Agent encounters an error condition that prevents it from running.



The following sections describe how to diagnose these cases.

### Verify that the Ops Agent was installed by the policy

VM Extension Manager policies use the [Compute Engine guest agent](https://docs.cloud.google.com/compute/docs/images/guest-environment#guest-agent) to manage the Ops Agent as a VM extension.

To determine if the Ops Agent was installed by the extension policy, use one of the following to look for log entries from the guest agent:

###  Logs Explorer 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query and click **Run query** :

`log_id("GCEGuestAgentManager")`




###  Linux 

Run the following command on the Compute Engine VM:

`journalctl -u google-guest-agent-manager`

###  Windows

Run the following command on the Compute Engine VM:

`Get-Eventlog -Source google_guest_agent_manager -LogName Application`

If you see logs containing a string like `Failed to install plugin "ops-agent-plugin" ...`, or the query returns no logs, then the extension policy failed to install the Ops Agent. For next steps, see Extension policy fails to install the Ops Agent.

If you see logs containing a string like `Successfully installed plugin "ops-agent_nnnnnnnn"`, then the extension policy successfully installed the Ops Agent. For next steps, see Installed Ops Agent is "not detected".

#### Extension policy fails to install the Ops Agent

An extension policy might be ineffective if one of the following is true:

  * The guest agent is not installed on the VM. To diagnose and fix this condition, do the following:

    1. Verify that the VM is using one of the [operating systems](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#supported_operating_systems) supported for the Compute Engine guest environment.

    2. [View the packages installed on the VM](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages) to verify that `google-guest-agent` is included.

    3. If the `google-guest-agent` is not installed, then [install the guest agent](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#in_place).

  * The guest agent is installed but outdated. To diagnose and fix this condition, do the following:

    1. [Validate the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages) to determine the version of the `google-guest-agent` package. VM Extension Manager requires version `20241209.01` or newer.

    2. If the version of the `google-guest-agent` is older than `20241209.01`, then [update the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest).

  * The VM's operating system is not supported by VM Extension Manager. For more information, see [Review supported operating systems](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies#verify-os-support).




#### Installed Ops Agent has status "not detected"

The Ops Agent can have a status of "not detected" if one of the following is true:

  * There are observability agents installed on the VM already. Existing agents can cause conflicts and must be uninstalled. For more information, see [Uninstall any observability agents](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies#uninstall-agents).

After uninstalling any previously installed agents, you can [restart the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-agent-vmem-policies#restart-agent-vmem).

  * The Ops Agent has insufficient permissions to send data to Cloud Logging and Cloud Monitoring. For more information, see [Common reasons for telemetry-transmission failures](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-run-ingest#common-agent-telemetry-transmission-errors).




### Verify that the Ops Agent configuration is valid

You provided a custom configuration to the Ops Agent by creating or updating an extension policy, but the agent status is "not detected". The problem might be an error in your custom configuration. Use the guest agent debug logs to look for configuration errors.

#### Enable guest agent debug logging

For information about enabling debug logging for the guest agent, see [View debug logs for the guest agent](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#debug-guest-agent).

#### Examine debug logs

###  Logs Explorer 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query and click **Run query** :

severity>=DEBUG log_id("GCEGuestAgentManager") "The agent config file is not valid"




###  Linux 

Run the following command on the Linux Compute Engine VM:

`journalctl -u google-guest-agent-manager | grep "The agent config file is not valid"`

###  Windows

Run the following command on the Windows Compute Engine VM:

`Get-Eventlog -Source google_guest_agent_manager -LogName Application | Where-Object {$_.Message -like "*The agent config file is not valid*"}`

If you see logs containing the string `The agent config file is not valid`, then the custom configuration for the Ops Agent you provided when creating or updating the extension policy is invalid.

To fix this problem, do the following:

  * Correct the configuration by referring to [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration). For information about the structure of an Ops Agent configuration file.

  * [Update](https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-agent-vmem-policies) the extension policy with the corrected configuration.




## Linux `systemctl status` and Windows `Get-Service` commands don't work with the Ops Agent

You run a command like `sudo systemctl status google-cloud-ops-agent"*"` but it returns no information.

When the Ops Agent is installed and managed by VM Extension Manager, the Ops Agent isn't managed by the system-management service of the operating system, that is, `systemd` on Linux or the Windows Service Manager on Windows.

To find the status information for an Ops Agent managed by VM Extension Manager, see the following:

  * [Agent health checks](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#health-checks)
  * [Agent self logs](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#self-logs).



## Linux `systemctl restart` and Windows `Restart-Service` commands don't work with the Ops Agent

You run a command like `sudo systemctl restart google-cloud-ops-agent` but the Ops Agent isn't restarted.

When the Ops Agent is installed and managed by VM Extension Manager, the Ops Agent isn't managed by the system-management service of the operating system, that is, `systemd` on Linux or the Windows Service Manager on Windows. Therefore, you can't stop or start the Ops Agent manually, and commands like the following don't work with the Ops Agent:

  * Linux: `sudo systemctl [stop|start|restart]`
  * Windows: `Stop-Service`, `Start-Service`, `Restart-Service`



To stop or restart an Ops Agent managed by VM Extension Manager, you must uninstall the agent by deleting the extension policy. For more information about stopping or restarting the Ops Agent, see [Restart an Ops Agent installed by an extension policy](https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-agent-vmem-policies#restart-agent-vmem).

## Additional troubleshooting information

For more information about troubleshooting the creation and use of VM Extension Manager policies, see [Troubleshoot VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#troubleshooting).

For more information about troubleshooting the Ops Agent, see [Troubleshoot the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
