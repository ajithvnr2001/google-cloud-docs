---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation/
title: Installing the Ops Agent on individual VMs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:44.275403+00:00
---

# Installing the Ops Agent on individual VMs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Installing the Ops Agent on individual VMs Stay organized with collections  Save and categorize content based on your preferences. 

The Ops Agent collects logs and metrics on Compute Engine instances, sending your logs to Cloud Logging and your metrics to Cloud Monitoring.

## Before you begin

To install the agent, ensure that you have the following:

  * A [supported VM instance](https://docs.cloud.google.com/logging/docs/agent/ops-agent#supported_vms) in a Google Cloud project.

  * A [supported operating system](https://docs.cloud.google.com/logging/docs/agent/ops-agent#supported_operating_systems).

  * Credentials on the VM instance that authorize communication with Cloud Logging and Cloud Monitoring. Compute Engine VM instances generally have the correct credentials. By default, the Ops Agent uses the Compute Engine service account, and that service account has the roles necessary for writing logs and metrics: [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) and [Monitoring Metric Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`).

If you are running very old Compute Engine instances or if you created Compute Engine instances without the default credentials, then you might not have the proper credentials. You must complete the [Authorize the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization) procedures.

  * Ensure that you [enable the services](https://docs.cloud.google.com/service-usage/docs/enable-disable) for both the Cloud Logging API and Cloud Monitoring API.

  * Ensure your VM doesn't have the legacy [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent) or [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent) installed on it. This can cause ingestion of duplicate logs or a conflict in metrics ingestion. In addition, this agent uses new configuration files that are not compatible with the old agents.

If you have the old agents installed, save the [custom configuration files for the Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent#agent-artifacts) and the [custom configuration files for the Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/configuration#configure), and complete the [uninstall steps for the Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#uninstall) and the [uninstall steps for the Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/installation#uninstall).

  * For users with VMs that don't have access to remote package repositories, refer to the VMs without remote package access section for more information.




## Install the agent automatically during VM creation

For more information, see [Install the Ops Agent during VM creation](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-agent-vm-creation).

## Install the agent from the command line

**Note:** First verify that all conditions are met in the Before you begin section.

To install the agent using the command line, use the following instructions.

### Install the latest version of the agent

To install the latest version of the agent, complete the following steps.

### Linux

  1. Open a terminal connection to your VM instance using SSH or a similar tool and ensure you have `sudo` access.

  2. Change to a directory you have write access to, for example your home directory.

  3. Download and run the agent-installation script by using the following commands:
         
         curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
         sudo bash add-google-cloud-ops-agent-repo.sh --also-install
         

After it is installed, the agent is started automatically.




### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Run the following PowerShell commands:
         
         (New-Object Net.WebClient).DownloadFile("https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.ps1", "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1")
         Invoke-Expression "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1 -AlsoInstall"
         




### Installing a specific version of the agent

To install a specific version of the agent, complete the following steps.

### Linux

  1. Open a terminal connection to your VM instance using SSH or a similar tool and ensure you have `sudo` access.

  2. Change to a directory you have write access to, for example your home directory.

  3. Download the agent installation script:
         
         curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
         

When running the `add-google-cloud-ops-agent-repo.sh` script, you can also set the following flags:

     * `--verbose`: Turns on verbose logging during the script execution.
     * `--also-install`: Installs the agent after adding the agent package repository.
     * `--version`: Sets the agent version for the script to install. For version information, see List all agent versions.
     * `--uninstall`: Uninstalls the agent.
     * `--remove-repo`: Removes the corresponding agent package repository after installing or uninstalling the agent.
     * `--dry-run`: Triggers only a dry run of the script execution and prints out the commands that it is supposed to execute.
     * `--uninstall-standalone-logging-agent`: Uninstalls the legacy Logging agent (`StackdriverLogging`).
     * `--uninstall-standalone-monitoring-agent`: Uninstalls the legacy Monitoring agent (`StackdriverMonitoring`).

See the script comments for more information and example usage.

  4. Add the agent's package repository and install the agent:

     1. To list the available agent versions, see List all agent versions.

     2. For production environments, you might want to pin to a major version to avoid installing major versions that might include backward incompatible changes. To pin to a major version, run:
            
            sudo bash add-google-cloud-ops-agent-repo.sh --also-install \
              --version=MAJOR_VERSION.*.*
            

For example, to pin to the 1.x.x of the agent, run:
            
            sudo bash add-google-cloud-ops-agent-repo.sh --also-install \
              --version=1.*.*
            

     3. To install a specific version of the agent, run:
            
            sudo bash add-google-cloud-ops-agent-repo.sh --also-install \
              --version=MAJOR_VERSION.MINOR_VERSION.PATCH_VERSION
            




You can delete the installation script after it runs successfully.

  * To verify that the agent is working as expected, run:
        
        sudo systemctl status google-cloud-ops-agent"*"
        

Verify that the components "Logging Agent" and "Metrics Agent" are running. 




If you have trouble with the installation, refer to the [Troubleshooting](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshooting) page.

### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Download the agent installation script:
         
         (New-Object Net.WebClient).DownloadFile("https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.ps1", "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1")
         

When running the `add-google-cloud-ops-agent-repo.ps1` script, you can also set the following flags:

     * `-Verbose`: Turns on verbose logging during the script execution.
     * `-AlsoInstall`: Installs the agent after adding the agent package repository.
     * `-Version`: Sets the agent version for the script to install. For version information, see List all agent versions.
     * `-Uninstall`: Uninstalls the agent.
     * `-RemoveRepo`: Removes the corresponding agent package repository after installing or uninstalling the agent.
     * `-WhatIf`: Triggers only a dry run of the script execution and prints out the commands that it is supposed to execute.
     * `-UninstallStandaloneLoggingAgent`: Uninstalls the legacy Logging agent (`StackdriverLogging`).
     * `-UninstallStandaloneMonitoringAgent`: Uninstalls the legacy Monitoring agent (`StackdriverMonitoring`).

See the script comments for more information and example usage.

  4. Add the agent's package repository and install the agent:

     1. To list the available agent versions, see List all agent versions.

     2. For production environments, you might want to pin to a major version to avoid installing major versions that might include backward incompatible changes. To pin to a major version, run:
            
            Invoke-Expression "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1 -AlsoInstall -Version MAJOR_VERSION.*.*"
            

For example, to pin to the 1.x.x of the agent, run:
            
            Invoke-Expression "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1 -AlsoInstall -Version 1.*.*"
            

     3. To install a specific version of the agent, run:
            
            Invoke-Expression "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1 -AlsoInstall -Version version-number"
            

For example:
            
            Invoke-Expression "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1 -AlsoInstall -Version 1.0.1"
            




You can delete the installation script after it runs successfully.

  * To verify that the agent is working as expected, run:
        
        Get-Service google-cloud-ops-agent
        

The status of the agent should be `Running`.




If you have trouble with the installation, refer to the [Troubleshooting](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshooting) page.

## Install the agent by using the Google Cloud console

**Note:** First verify that all conditions are met in the Before you begin section.

You can install the Ops Agent on one or more Compute Engine VMs by using the Google Cloud console from the Cloud Monitoring or Compute Engine pages.

###  Cloud Monitoring 

In the Google Cloud console, go to the **VM Instances** page: 

[Go to **VM Instances**](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

The **List** view on the **Inventory** tab on the dashboard lists all VMs and includes a status column for your agent, as shown in the following screenshot:

![The VM Instances dashboard in Monitoring shows the status
of
agents.](https://docs.cloud.google.com/static/monitoring/images/vm-instances-agent-install.png)

The **Agent** column reports the following values:

  * **Not detected** : Either you don't have an agent installed or it is not running. If you aren't sure if you've installed an agent, then you can query for the installed version. If you've installed the agent, then you can restart the agent. If you've installed and started the Ops Agent but the status remains **Not detected** , then the agent might not have started correctly or is unable to send metrics. 

To troubleshoot start-up problems, see [Agent is installed but not running](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup#agent-not-running). To troubleshoot metric-ingestion problems, see [Troubleshoot data ingestion](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-run-ingest). The general [agent-diagnostics script](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#agent-diagnostics) and [health checks](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#health-checks) might also be helpful. 

  * **Ops Agent** : You are running the Ops Agent. If you don't see a green checkmark beside the entry, then there is an agent upgrade available, based on the detected operating system of your VM.

When you hover over the Ops Agent indicator in the table, you see information about the version of the Ops Agent. If you are running an older version, you also see a recommendation to upgrade your agent.

  * **Pending** : The Ops Agent is being installed or upgraded. 

If the agent installation remains **Pending** for more than 10 minutes, then there might be a problem in applying the Ops Agent OS policy or starting the agent. For troubleshooting information, see [ Agent diagnostics tool for automatic installation policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#agent_diagnostics_tool_for_automatic_installation_policies).

  * **Agent installation failed** : Installation of the Ops Agent failed. For troubleshooting information, see [Agent fails to install](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup#install-failed).

  * **Not Collecting Telemetry** : Installation of the Ops Agent succeeded, but the agent isn't yet sending telemetry.

It usually takes about 10 minutes for telemetry to flow from a new agent. You can refresh the page to update the status. If this status persists for longer than 10 minutes, it might indicate a problem with the ingestion of the telemetry. For more information, see [Agent is installed but not running](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup#agent-not-running).

  * **Legacy Agent** : You are running the legacy Monitoring or the Logging agent. See [Migrating from the legacy agents to the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition#migrate_legacy) for information on transitioning to the Ops Agent.

  * **Not applicable** : This VM is not a supported platform for running the agent.

  * **VM Stopped** : The VM is not running, so the agent's status is not known.




You can install the Ops Agent by doing the following:

  * Select the VM instances on which you want to install agents.
  * Click the **Install/Update Ops Agent** option on the **Instances** table.



You can also install or update the Ops Agent from the **VM Details** page for a specific VM.

When possible, the agent is installed by using an Ops Agent OS policy. For more information, see [ Manage VMs covered by the Ops Agent OS policy](https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-policies-auto-install). Ops Agent OS policies aren't supported on all versions of all operating systems. In this case, clicking **Install/Update Ops Agent** provides a series of commands to run in Cloud Shell.

The Ops Agent collects both metrics and logs by default. You can change this default behavior by [ configuring the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration).

###  Compute Engine 

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Click the name of the VM on which you want to install the agent.

  3. Click the **Observability** tab.

  4. Click **Install Ops Agent**.

When possible, the agent is installed by using an Ops Agent OS policy. For more information, see [ Manage VMs covered by the Ops Agent OS policy](https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-policies-auto-install). Ops Agent OS policies aren't supported on all versions of all operating systems. In this case, clicking **Install/Update Ops Agent** provides a series of commands to run in Cloud Shell.

The Ops Agent collects both metrics and logs by default. You can change this default behavior by [ configuring the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration).

If the agent installation remains **Pending** for more than 10 minutes, then there might be a problem in applying the Ops Agent OS policy or starting the agent. For troubleshooting information, see [ Agent diagnostics tool for automatic installation policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#agent_diagnostics_tool_for_automatic_installation_policies).




## Verify that the Ops Agent is running

To verify that the Ops Agent is running, you can use either of the following:

  * **VM Instances** dashboard: This dashboard lets you view the agent installation status across your VM fleet. However, the status might be inaccurate if the VM lacks necessary access scopes or if the associated service account has insufficient IAM roles.

  * gcpdiag: gcpdiag provides more reliable and robust information about agent status than the **VM Instances** dashboard, verifying both agent installation and transmission of telemetry from the VM. Using gcpdiag has some [prerequisites](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#gcpdiag-for-ops-agent-before-you-begin), it provides a better way to monitor agent status.




### Use **VM Instances** dashboard

In the Google Cloud console, go to the **VM Instances** page: 

[Go to **VM Instances**](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

The **List** view on the **Inventory** tab on the dashboard lists all VMs and includes a status column for your agent.

The **Agent** column reports the following values:

  * **Not detected** : Either you don't have an agent installed or it is not running. If you aren't sure if you've installed an agent, then you can query for the installed version. If you've installed the agent, then you can restart the agent. If you've installed and started the Ops Agent but the status remains **Not detected** , then the agent might not have started correctly or is unable to send metrics. 

To troubleshoot start-up problems, see [Agent is installed but not running](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup#agent-not-running). To troubleshoot metric-ingestion problems, see [Troubleshoot data ingestion](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-run-ingest). The general [agent-diagnostics script](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#agent-diagnostics) and [health checks](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#health-checks) might also be helpful. 

  * **Ops Agent** : You are running the Ops Agent. If you don't see a green checkmark beside the entry, then there is an agent upgrade available, based on the detected operating system of your VM.

When you hover over the Ops Agent indicator in the table, you see information about the version of the Ops Agent. If you are running an older version, you also see a recommendation to upgrade your agent.

  * **Pending** : The Ops Agent is being installed or upgraded. 

If the agent installation remains **Pending** for more than 10 minutes, then there might be a problem in applying the Ops Agent OS policy or starting the agent. For troubleshooting information, see [ Agent diagnostics tool for automatic installation policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#agent_diagnostics_tool_for_automatic_installation_policies).

  * **Agent installation failed** : Installation of the Ops Agent failed. For troubleshooting information, see [Agent fails to install](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup#install-failed).

  * **Not Collecting Telemetry** : Installation of the Ops Agent succeeded, but the agent isn't yet sending telemetry.

It usually takes about 10 minutes for telemetry to flow from a new agent. You can refresh the page to update the status. If this status persists for longer than 10 minutes, it might indicate a problem with the ingestion of the telemetry. For more information, see [Agent is installed but not running](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup#agent-not-running).

  * **Legacy Agent** : You are running the legacy Monitoring or the Logging agent. See [Migrating from the legacy agents to the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition#migrate_legacy) for information on transitioning to the Ops Agent.

  * **Not applicable** : This VM is not a supported platform for running the agent.

  * **VM Stopped** : The VM is not running, so the agent's status is not known.




### Use gcpdiag

For information about using gcpdiag, see [Verify agent status by using gcpdiag](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#agent-status-gcpdiag-cmd).

## Optional tasks

This section describes how to perform common maintenance tasks.

### Configure an HTTP proxy

If you use an HTTP proxy for proxying requests to the Logging and Monitoring APIs, do the following:

### Linux

  1. Edit the following configuration file (create the file if it doesn't already exist):
         
         /etc/systemd/system.conf
         

  2. Add the following to the file:
         
         DefaultEnvironment="HTTP_PROXY=http://proxy-ip:proxy-port" "HTTPS_PROXY=http://proxy-ip:proxy-port" "NO_PROXY=http://metadata.google.internal"  # Skip proxy for the local Metadata Server.
         

  3. Reload the environment variables:
         
         sudo systemctl daemon-reload
         

  4. Restart the agent by running the following command on your VM instance:
         
         sudo systemctl restart google-cloud-ops-agent"*"
         




### Windows

  1. If you use an HTTP proxy, run the following command from an administrator command prompt. This sets the `HTTP_PROXY` and `HTTPS_PROXY` environment variables so that the agent can send data using outbound HTTPS:
         
         setx HTTP_PROXY http://proxy-ip:proxy-port /m
         setx HTTPS_PROXY http://proxy-ip:proxy-port /m
         setx no_proxy "metadata.google.internal,169.254.169.254" /m
         




### Determine the agent version

To determine the version of the Ops Agent on your system, run the following commands on your VM instance:

### Google Cloud console

To see the version of your Ops Agent on a VM:

  * Locate the entry for the VM in the **Instances** table in the Monitoring **VM Instances** page. For navigation information, see Install the agent by using the Google Cloud console.

  * Hover over the **Ops Agent** indicator in the table entry.




### CENTOS / RHEL

Run the following command on Red Hat or CentOS Linux:
    
    
    rpm --query --queryformat '%{NAME} %{VERSION} %{RELEASE} %{ARCH}\n' google-cloud-ops-agent
    

### DEBIAN / UBUNTU

Run the following command on Debian or Ubuntu:
    
    
    dpkg-query --show --showformat '${Package} ${Version} ${Architecture} ${Status}\n' google-cloud-ops-agent
    

### SLES / SUSE

Run the following command on SUSE:
    
    
    rpm --query --queryformat '%{NAME} %{VERSION} %{RELEASE} %{ARCH}\n' google-cloud-ops-agent
    

### WINDOWS

Run the following command on Windows:
    
    
    googet installed google-cloud-ops-agent
    

### Restart the agent

You must restart the Ops Agent to pick up changes in configuration files. To restart the agent, use the following instructions.

### LINUX

Run the following command on your instance:
    
    
         sudo systemctl restart google-cloud-ops-agent
    
    

### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Run the following PowerShell command:



    
    
    Restart-Service google-cloud-ops-agent -Force
    

### Upgrade the agent

To upgrade the Ops Agent to the latest release, use the following instructions:

**Note:** If you upgraded your instance's Linux operating system to a new major release, then you should first remove the agent and then re-install it using the procedures on this page, instead of completing these upgrade procedures.

### Google Cloud console

You can upgrade the Ops Agent by using Cloud Monitoring installation instructions. For more information, see Install the agent by using the Google Cloud console.

### Linux

To upgrade the agent to the latest version, run the following command:
    
    
    sudo bash add-google-cloud-ops-agent-repo.sh --also-install
    

To upgrade the agent to the latest point release of a specific major version, run the following command:
    
    
    sudo bash add-google-cloud-ops-agent-repo.sh --also-install \
      --version=MAJOR_VERSION.*.*
    

### Windows

To upgrade to the latest agent release:

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

**Note:** If you're upgrading your agent from a version earlier than 2.0.3 to version 2.0.3 or later, the upgrade removes the old config file. If you customized your agent configuration, be sure to save a backup of your configuration file before upgrading, and then to apply the necessary changes to the configuration file after the upgrade.
         
         Copy-Item -Path "C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml" -Destination "C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.bak"
         

  3. Run the following PowerShell commands to remove your installed agent and to run the installation command:
         
         googet -noconfirm remove google-cloud-ops-agent
         googet -noconfirm install google-cloud-ops-agent
         




### List all agent versions

To list the available versions of the agent, run the following command:

### CENTOS / RHEL

List the available versions of the agent:
    
    
    sudo yum list --showduplicates google-cloud-ops-agent
    

### DEBIAN / UBUNTU

List the available versions of the agent:
    
    
    sudo apt-cache madison google-cloud-ops-agent
    

### SLES / SUSE

List the available versions of the agent:
    
    
    sudo zypper search -s google-cloud-ops-agent
    

### WINDOWS

List the available versions of the agent:
    
    
    googet available google-cloud-ops-agent
    

### Uninstall the agent

To remove the Ops Agent and its configuration files, use the following instructions.

**Note:** If the Ops Agent was installed during VM creation, see [Manage VMs covered by Ops Agent OS policy](https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-policies-auto-install).

After you uninstall the agent, the Google Cloud console might take up to one hour to report this change.

### Linux

Run the following command:
    
    
    sudo bash add-google-cloud-ops-agent-repo.sh --uninstall
    

Optionally, to remove the repository in addition to uninstalling the agent, append `--remove-repo` to the previous command.

### Windows

To uninstall the Ops Agent, follow the following steps:

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Run the following PowerShell command:
         
         googet -noconfirm remove google-cloud-ops-agent
         




## VMs without remote package access

Installing the Ops Agent [requires access](https://docs.cloud.google.com/logging/docs/agent/ops-agent#access) to remote package repositories, for both the agent package and (on Linux) its dependencies.

If you are using [VPC-SC](https://docs.cloud.google.com/vpc-service-controls) or a private network, the network configuration might also affect your ability to install agent dependencies from upstream repositories. The agent packages themselves are accessible by using [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). This can be configured following [Enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).

If your VM host's security policy denies access to remote package repositories, we recommend creating a [custom VM image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) with the agent pre-installed and disabling package management in that image.

## What's next

  * Learn about what [logs the agent sends to Cloud Logging using its default configuration](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#default).

  * For information on viewing your logs, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
