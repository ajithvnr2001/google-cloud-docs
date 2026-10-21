---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/installation/
title: Installing the Cloud Logging agent on individual VMs \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:18.122948+00:00
---

# Installing the Cloud Logging agent on individual VMs  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/installation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Installing the Cloud Logging agent on individual VMs Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Logging agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

The Logging agent streams logs from your VM instances and from selected third-party software packages to Cloud Logging. It is a best practice to run the Logging agent on all your VM instances.

The VM images for Compute Engine don't include the Logging agent, so you must complete these steps to install it on those instances. The agent runs under both Linux and Windows.

If your VMs are running in **Google Kubernetes Engine** or **App Engine** , the agent is already included in the VM image, so you can skip this page.

## Before you begin

To install the agent, ensure that you have the following:

  * A [supported VM instance](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging#supported_vms) in a Google Cloud project.

    * When installing the Logging agent, a minimum of 250 MiB memory is required, but 1 GiB is recommended.

Also ensure your VM is running a [supported operating system](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging#supported_operating_systems).

  * Credentials on the VM instance that authorize communication with Cloud Logging or Cloud Monitoring. Compute Engine VM instances generally have the correct credentials by default. If the following scenario applies to you, then you might not have the proper credentials and must complete the [Authorize the Logging agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/authorization) procedures:

    * Running very old Compute Engine instances or Compute Engine instances created without the default credentials.

To check if you have the proper credentials, run the [Verifying Compute Engine credentials](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/troubleshooting#verify-creds) procedures.

  * For pricing information, go to [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

  * If you're using VMs that don't have access to remote package repositories, refer to the VMs without remote package access section for more information.




## Install the agent from the command line

**Note:** First verify that all conditions are met in the Before you begin section.

To install the agent using the command line, use the following instructions.

### Install the latest version of the agent

To install the latest version of the agent, complete the following steps.

### Linux

  1. Open a terminal connection to your VM instance using SSH or a similar tool and ensure you have `sudo` access.

  2. Change to a directory you have write access to, for example your home directory.

  3. Download and run the agent-installation script by using the following commands:
         
         curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.sh
         sudo bash add-logging-agent-repo.sh --also-install
         

After it is installed, the agent is started automatically.




### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Run the following PowerShell commands:
         
         (New-Object Net.WebClient).DownloadFile("https://dl.google.com/cloudagents/windows/StackdriverLogging-v1-22.exe", "${env:UserProfile}\StackdriverLogging-v1-22.exe")
         & "${env:UserProfile}\StackdriverLogging-v1-22.exe"
         




### Installing a specific version of the agent

To install a specific version of the agent, complete the following steps.

### Linux

  1. Open a terminal connection to your VM instance using SSH or a similar tool and ensure you have `sudo` access.

  2. Change to a directory you have write access to, for example your home directory.

  3. Download the agent installation script:
         
         curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.sh
         

When running the `add-logging-agent-repo.sh` script, you can also set the following flags:

     * `--verbose`: Turns on verbose logging during the script execution.
     * `--also-install`: Installs the agent after adding the agent package repository.
     * `--version`: Sets the agent version for the script to install. For version information, see List all agent versions.
     * `--uninstall`: Uninstalls the agent.
     * `--remove-repo`: Removes the corresponding agent package repository after installing or uninstalling the agent.
     * `--dry-run`: Triggers only a dry run of the script execution and prints out the commands that it is supposed to execute.

See the script comments for more information and example usage.

  4. Add the agent's package repository and install the agent:

     1. To list the available agent versions, see List all agent versions.

     2. For production environments, you might want to pin to a major version to avoid installing major versions that might include backward incompatible changes. To pin to a major version, run:
            
            sudo bash add-logging-agent-repo.sh --also-install \
              --version=MAJOR_VERSION.*.*
            

For example, to pin to the 1.x.x of the agent, run:
            
            sudo bash add-logging-agent-repo.sh --also-install \
              --version=1.*.*
            

     3. To install a specific version of the agent, run:
            
            sudo bash add-logging-agent-repo.sh --also-install \
              --version=MAJOR_VERSION.MINOR_VERSION.PATCH_VERSION
            

  5. Restart the agent service

A restart is required for the configurations that are installed by the catch-all packages above to take effect.
         
         sudo service google-fluentd restart
         




You can delete the installation script after it runs successfully.

  * To verify that the agent is working as expected, run:
        
        sudo service google-fluentd status
        

The status of the agent should be **OK**. 



  * You can also examine the logs and ensure there are no errors:
        
        tail /var/log/google-fluentd/google-fluentd.log
        




If you have trouble with the installation, refer to the [Troubleshooting](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/troubleshooting) page.

### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

**Note:** Only the latest version of the agent is supported on VM instances running Windows. Installing previous versions is not recommended.
     1. Run the following PowerShell commands:
            
            (New-Object Net.WebClient).DownloadFile("https://dl.google.com/cloudagents/windows/StackdriverLogging-v1-22.exe", "${env:UserProfile}\StackdriverLogging-v1-22.exe")
            & "${env:UserProfile}\StackdriverLogging-v1-22.exe"
            

Alternatively, you can browse to the following URL to download and run the agent's installer:

<https://dl.google.com/cloudagents/windows/StackdriverLogging-v1-22.exe>

**Caution:** You must download the installer to a non-system directory, such as `C:\Users\[USERNAME]`. For security reasons, the installer doesn't run from system directories, including the directory `C:\`. If you download the installer to a system directory, move it to another directory before running it.**Note:** The agent installer also supports a “silent” option, `/S`, that can be used in scripting the installation.

To install the agent silently, append the `/S` option to the invocation of the installer:
    
    & "${env:UserProfile}\StackdriverLogging-v1-22.exe" /S
    

**Caution:** Silent installation is an **asynchronous** operation. When the installation command exits, the agent is not yet installed. You can check for a successful installation by looking for the `StackdriverLogging` service.**Note:** The installer places the agent in the `C:\Program Files (x86)\Stackdriver\Google Cloud ObservabilityAgent` directory by default. You can change that directory during installation.

In “silent” mode use the `/D` option to specify the installation directory, for example:
    
    & "${env:UserProfile}\StackdriverLogging-v1-22.exe" /S /D="C:\Stackdriver\Google Cloud Observability\"
    

You can delete the installer when it completes successfully.

If you have trouble with the installation, refer to the [Troubleshooting](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/troubleshooting) page.




## Viewing agent information by using the Google Cloud console

You can find status information about the agent on the pre-configured Monitoring **VM Instances** dashboard. To reach this dashboard, do the following: 

In the Google Cloud console, go to the **VM Instances** page: 

[Go to **VM Instances**](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

The **List** view on the **Inventory** tab on the dashboard lists all VMs and includes a status column for your agent, as shown in the following screenshot:

![The VM Instances dashboard in Monitoring shows the status
of
agents.](https://docs.cloud.google.com/static/monitoring/images/vm-instances-agent-install.png)

The **Agent** column reports the following values:

  * **Not detected** : Either you don't have an agent installed or it is not running. If you aren't sure if you've installed an agent, then you can query for the installed version. If you've installed the agent, then you can restart the agent. 

  * **Ops Agent** : You are running the Ops Agent. If you don't see a green checkmark beside the entry, then there is an agent upgrade available, based on the detected operating system of your VM.

When you hover over the Ops Agent indicator in the table, you see information about the version of the Ops Agent. If you are running an older version, you also see a recommendation to upgrade your agent.

  * **Pending** : The Ops Agent is being installed or upgraded. 

  * **Agent installation failed** : Installation of the Ops Agent failed. 

  * **Not Collecting Telemetry** : Installation of the Ops Agent succeeded, but the agent isn't yet sending telemetry.

  * **Legacy Agent** : You are running the legacy Monitoring or the Logging agent. See [Migrating from the legacy agents to the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition#migrate_legacy) for information on transitioning to the Ops Agent.

  * **Not applicable** : This VM is not a supported platform for running the agent.

  * **VM Stopped** : The VM is not running, so the agent's status is not known.




You can install the Ops Agent by doing the following:

  * Select the VM instances on which you want to install agents.
  * Click the **Install/Update Ops Agent** option on the **Instances** table.



You can also install or update the Ops Agent from the **VM Details** page for a specific VM.

When possible, the agent is installed by using an Ops Agent OS policy. For more information, see [ Manage VMs covered by the Ops Agent OS policy](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-policies-auto-install). Ops Agent OS policies aren't supported on all versions of all operating systems. In this case, clicking **Install/Update Ops Agent** provides a series of commands to run in Cloud Shell.

The Ops Agent collects both metrics and logs by default. You can change this default behavior by [ configuring the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/configuration).

## Optional tasks

This section describes how to perform common maintenance tasks.

### Enable structured logging

When you run the installation script on a Linux VM, the script by default installs the `google-fluentd-catch-all` package when the `--also-install` flag is present. In order to switch to structured logging, complete the following steps.

  1. Back up any local changes to `/etc/google-fluentd/config.d/`.

  2. Run one of the following commands, depending on your Linux distribution:

     * YUM:
           
           sudo yum remove -y google-fluentd-catch-all-config
           sudo yum install -y google-fluentd-catch-all-config-structured
           sudo service google-fluentd restart
           

     * APT:
           
           sudo apt-get remove -y google-fluentd-catch-all-config
           sudo apt-get install -y google-fluentd-catch-all-config-structured
           sudo service google-fluentd restart
           




For information about structured logging, refer to the [structured logging](https://docs.cloud.google.com/logging/docs/structured-logging) guide.

### Configuring the Logging agent

The agent comes preconfigured to monitor certain known log locations. On Linux, those locations are described in the package `google-fluentd-catch-all-config`, which is automatically pulled in by the installation script. On Windows, the agent monitors the Windows Event Log by default.

To adjust the agent configuration, see [Configure the Logging agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/configuration).

### Configure an HTTP proxy

If you use an HTTP proxy for proxying requests to the Logging and Monitoring APIs, do the following:

### Linux

  1. Edit the following configuration file (create the file if it doesn't already exist):
         
         /etc/default/google-fluentd
         

  2. Add the following to the file:
         
         export http_proxy="http://proxy-ip:proxy-port"
          export https_proxy="http://proxy-ip:proxy-port"
          export no_proxy=169.254.169.254  # Skip proxy for the local Metadata Server.
         

  3. Restart the agent by running the following command on your VM instance:
         
         sudo service google-fluentd restart
         




### Windows

  1. If you use an HTTP proxy, run the following command from an administrator command prompt. This sets the `http_proxy` and `https_proxy` environment variables so that the agent can send data using outbound HTTPS:
         
         setx http_proxy http://proxy-ip:proxy-port /m
         setx https_proxy http://proxy-ip:proxy-port /m
         setx no_proxy 169.254.169.254 /m
         




### Determine the agent version

To determine the version of the Logging agent on your system, run the following commands on your VM instance:

### DEBIAN / UBUNTU

Run the following command on Debian or Ubuntu:
    
    
    dpkg-query --show --showformat '${Package} ${Version} ${Architecture} ${Status}\n' google-fluentd google-fluentd-catch-all-config google-fluentd-catch-all-config-structured
    

### SLES / SUSE

Run the following command on SUSE:
    
    
    rpm --query --queryformat '%{NAME} %{VERSION} %{RELEASE} %{ARCH}\n' google-fluentd google-fluentd-catch-all-config google-fluentd-catch-all-config-structured
    

### WINDOWS

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Run the following PowerShell command:
         
         reg query HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\GoogleStackdriverLoggingAgent\ /v Version
         




### Restart the agent

You must restart the Logging agent to pick up changes in configuration files. To restart the agent, use the following instructions.

### LINUX

Run the following command on your instance:
    
    
         sudo service google-fluentd restart
    
    

After restarting the Logging agent, you might want to [send a test message](https://docs.cloud.google.com/logging/docs/agent/troubleshooting#test-agent).

### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Run the following PowerShell command:



    
    
    Restart-Service -Name StackdriverLogging
    

### Upgrade the agent

To upgrade the Logging agent to the latest release, use the following instructions:

**Note:** If you upgraded your instance's Linux operating system to a new major release, then you should first remove the agent and then re-install it using the procedures on this page, instead of completing these upgrade procedures.

### Linux

To upgrade the agent to the latest version, run the following command:
    
    
    sudo bash add-logging-agent-repo.sh --also-install
    

To upgrade the agent to the latest point release of a specific major version, run the following command:
    
    
    sudo bash add-logging-agent-repo.sh --also-install \
      --version=MAJOR_VERSION.*.*
    

### Windows

To upgrade to the latest agent release, install the newest agent as described in Installing on Windows on this page. The installer prompts you to uninstall the previous version of the agent.

### List all agent versions

To list the available versions of the agent, run the following command:

### CENTOS / RHEL

List the available versions of the agent:
    
    
    sudo yum list --showduplicates google-fluentd
    

### DEBIAN / UBUNTU

List the available versions of the agent:
    
    
    sudo apt-cache madison google-fluentd
    

### SLES / SUSE

List the available versions of the agent:
    
    
    sudo zypper search -s google-fluentd
    

### WINDOWS

Installing earlier versions of the agent on Windows is not supported.

### Uninstall the agent

To remove the Logging agent and its configuration files, use the following instructions.

After you uninstall the agent, the Google Cloud console might take up to one hour to report this change.

**Note:** If you added your own `fluentd` configuration files, copy them from the agent's [configuration directory](https://docs.cloud.google.com/logging/docs/agent/configuration#default-config) for safekeeping.

### Linux

Run the following command:
    
    
    sudo bash add-logging-agent-repo.sh --uninstall
    

Optionally, to remove the repository in addition to uninstalling the agent, append `--remove-repo` to the previous command.

### Windows

In the Windows Control Panel, choose **Uninstall a program**. You should see the Logging agent in the list of programs that you can uninstall. You can also run `uninstall.exe` from the directory where you installed the Logging agent.

## VMs without remote package access

Installing the Logging agent [requires access](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging#access) to remote package repositories, for both the agent package and (on Linux) its dependencies.

If you are using [VPC-SC](https://docs.cloud.google.com/vpc-service-controls) or a private network, the network configuration might also affect your ability to install agent dependencies from upstream repositories. The agent packages themselves are accessible by using [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). This can be configured following [Enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).

If your VM host's security policy denies access to remote package repositories, we recommend creating a [custom VM image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) with the agent pre-installed and disabling package management in that image.

## What's next

  * Learn about what [logs the agent sends to Cloud Logging using its default configuration](https://docs.cloud.google.com/logging/docs/agent/default-logs).

  * For information on viewing your logs, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
