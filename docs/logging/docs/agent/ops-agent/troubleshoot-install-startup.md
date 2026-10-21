---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup/
title: Troubleshoot Ops Agent installation and start-up \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:05.918728+00:00
---

# Troubleshoot Ops Agent installation and start-up  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-install-startup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot Ops Agent installation and start-up Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information to help you diagnose and resolve problems in the installation and start-up of the Ops Agent. If the agent is running but failing to ingest logs or metrics, see [Troubleshoot data ingestion](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-run-ingest).

## Before you begin

Before trying to fix a problem, check the status of the agent's [health checks](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#health-checks).

**Note:** Authorization using the Google Cloud CLI is not supported by the Ops Agent. To ensure that the agent operates correctly, you must revoke any credentials that were created using the Google Cloud CLI.

## Agent fails to install

You may encounter the following errors when running the [installation script](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#joint-install).

### The operating system isn't supported

When the operating system isn't supported, the installation of the Ops Agent fails. The error message might look similar to the following:

**Linux**
    
    
    https://packages.cloud.google.com/yum/repos/google-cloud-ops-agent-el6-x86_64-all/repodata/repomd.xml: [Errno 14] PYCURL ERROR 22 - "The requested URL returned error: 404 Not Found"
    Trying other mirror.
    To address this issue please refer to the below wiki article
    
    https://wiki.centos.org/yum-errors
    
    If above article doesn't help to resolve this issue please use https://bugs.centos.org/.
    
    Error: Cannot retrieve repository metadata (repomd.xml) for repository: google-cloud-ops-agent. Please verify its path and try again
    

### A legacy agent is installed that conflicts with the Ops Agent

When a VM already has the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging) or the [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring) installed, they conflict with the new agent. The error message might look similar to the following:

**Linux**
    
    
    Error:
     Problem: problem with installed package stackdriver-agent-6.0.5-1.el8.x86_64 - package google-cloud-ops-agent-0.1.0-1.el8.x86_64 conflicts with stackdriver-agent provided by stackdriver-agent-6.0.5-1.el8.x86_64
    

The Ops Agent uses new configuration files that aren't compatible with the old agents. For more information, refer to the [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration) guide.

To fix this error, do the following:

  1. Save the custom configuration files for the [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent#agent-artifacts) and the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/configuration#configure).

  2. Uninstall the old [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#uninstall) and [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/installation#uninstall).

After you uninstall the agent, the Google Cloud console might take up to one hour to report this change.




### Ops Agent install fails after failed Monitoring agent install

The installation of the Ops Agent fails after a failed attempt to install the Monitoring agent. On a Debian operating system, the error messages when the Ops Agent fails to install are similar to the following:

**Linux**
    
    
    ...
    E: The repository 'https://packages.cloud.google.com/apt google-cloud-monitoring-jammy-all Release' does not have a Release file.
    ...
    Could not refresh the google-cloud-ops-agent apt repositories.
    

If you try to install the Monitoring agent on an operating system that isn't supported by that agent, then the installation fails. The installation failure occurs after the Monitoring agent repository is added to the system. Installing the Ops Agent after a failed install of the Monitoring agent also fails due to an invalid Monitoring agent repository.

Not all operating systems supported by the Ops Agent are also supported by the Monitoring agent. For information about supported operating systems, see [Ops Agent: Linux operating systems](https://docs.cloud.google.com/monitoring/agent/ops-agent#linux_operating_systems) and [Monitoring agent: Linux operating systems](https://docs.cloud.google.com/monitoring/agent/monitoring#linux_operating_systems).

To install the Ops Agent, do the following:

  1. Remove the repository for the Monitoring agent:

If the script `add-monitoring-agent-repo.sh` is on your system, then run the following command:
         
         sudo bash add-monitoring-agent-repo.sh --remove-repo
         

Otherwise, manually remove the repository:

###  Debian 
         
         sudo rm /etc/apt/sources.list.d/google-cloud-monitoring.list

###  RHEL 
         
         sudo rm /etc/yum.repos.d/google-cloud-monitoring.repo

###  Suse 
         
         sudo rm /etc/zypp/repos.d/google-cloud-monitoring.repo

  2. Run the Ops Agent installation script.




### Ops Agent install fails because the repository refresh fails

The installation of the Ops Agent fails because the refresh of the installed repositories fails.

**Linux**

For an example of the failure message for a Debian operating system, where the repository refresh occurs due to a call to `apt-get update`, see the troubleshooting entry Ops Agent install fails after failed Monitoring agent install.

If you encounter failures when refreshing the repositories, then you must resolve those failures before you can install the Ops Agent. You might be able to resolve these failures by deleting or disabling repositories that aren't necessary.

After you are able to refresh the repositories, you can install the Ops Agent by running the Ops Agent installation script.

### Repository refresh fails because the public key is unavailable

**Linux**

A repository refresh, due to a call to `apt-get update`, fails because the public key is unavailable. This can also occur when installing or upgrading the Ops Agent. You might see the following failure:
    
    
    W: GPG error: http://packages.cloud.google.com/apt google-cloud-ops-agent-focal-all InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY C0BA5CE6DC6315A3
    E: The repository 'http://packages.cloud.google.com/apt google-cloud-ops-agent-focal-all InRelease' is not signed.
    

To fix this error, run the following command to add the missing key to your system:
    
    
    curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
        | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/google-cloud-ops-agent.gpg
    

## Agent is installed but not running

If you have installed the agent but the agent is not running, then the problem might be one of the following:

  * One of the primary components, "Metrics Agent" or "Logging Agent", has failed to start; see Agent services not running.
  * One of the legacy agents is also installed on the VM; see Conflict with currently installed agents.
  * A port that one of the components requires is in use by another process; see Unavailable port.
  * The configuration of the Ops Agent is invalid; see Invalid configuration.



### Agent services not running

When the agent services are running as expected, the Metrics Agent and Logging Agent are listed as running when you query the status:

**For Linux**
    
    
    sudo systemctl status google-cloud-ops-agent"*"
    

Some lines in the output have been deleted for brevity.
    
    
    ● google-cloud-ops-agent.service - Google Cloud Ops Agent
         Loaded: loaded (/lib/systemd/system/google-cloud-ops-agent.service; enabled; vendor preset: enabled)
         Active: active (exited) since Wed 2023-05-03 21:22:28 UTC; 4 weeks 0 days ago
        Process: 3353828 ExecStartPre=/opt/google-cloud-ops-agent/libexec/google_cloud_ops_agent_engine -in /etc/go>
        Process: 3353837 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
       Main PID: 3353837 (code=exited, status=0/SUCCESS)
            CPU: 195ms
    
    [...]
    
    ● google-cloud-ops-agent-opentelemetry-collector.service - **Google Cloud Ops Agent - Metrics Agent**
         Loaded: loaded (/lib/systemd/system/google-cloud-ops-agent-opentelemetry-collector.service; static)
         Active: **active (running)** since Wed 2023-05-03 21:22:29 UTC; 4 weeks 0 days ago
        Process: 3353840 ExecStartPre=/opt/google-cloud-ops-agent/libexec/google_cloud_ops_agent_engine -service=ot>
       Main PID: 3353855 (otelopscol)
          Tasks: 9 (limit: 2355)
         Memory: 65.3M
            CPU: 40min 31.555s
         CGroup: /system.slice/google-cloud-ops-agent-opentelemetry-collector.service
                 └─3353855 /opt/google-cloud-ops-agent/subagents/opentelemetry-collector/otelopscol --config=/run/g>
    
    [...]
    
    ● google-cloud-ops-agent-fluent-bit.service - **Google Cloud Ops Agent - Logging Agent**
         Loaded: loaded (/lib/systemd/system/google-cloud-ops-agent-fluent-bit.service; static)
         Active: **active (running)** since Wed 2023-05-03 21:22:29 UTC; 4 weeks 0 days ago
        Process: 3353838 ExecStartPre=/opt/google-cloud-ops-agent/libexec/google_cloud_ops_agent_engine -service=fl>
       Main PID: 3353856 (google_cloud_op)
          Tasks: 31 (limit: 2355)
         Memory: 58.3M
            CPU: 29min 6.771s
         CGroup: /system.slice/google-cloud-ops-agent-fluent-bit.service
                 ├─3353856 /opt/google-cloud-ops-agent/libexec/google_cloud_ops_agent_wrapper -config_path /etc/goo>
                 └─3353872 /opt/google-cloud-ops-agent/subagents/fluent-bit/bin/fluent-bit --config /run/google-clo>
    
    [...]
    

**For Windows**
    
    
    Get-Service google-cloud-ops-agent*
    
    Status   Name               DisplayName
    ------   ----               -----------
    Running  google-cloud-op... Google Cloud Ops Agent
    Running  google-cloud-op... Google Cloud Ops Agent - Logging Agent
    Running  google-cloud-op... Google Cloud Ops Agent - Metrics Agent
    

If the agent service is not running, you might see the following status:

**Linux**
    
    
    $ sudo service google-cloud-ops-agent status
    ● google-cloud-ops-agent.service - Google Cloud Ops Agent
       Loaded: loaded (/lib/systemd/system/google-cloud-ops-agent.service; enabled; vendor preset: enabled)
       Active: inactive (dead) since Wed 2021-06-30 21:20:43 UTC; 6s ago
    

**Windows**
    
    
    Get-Service google-cloud-ops-agent
    
    Status   Name                    DisplayName
    ------   ----                    -----------
    Stopped  google-cloud-ops-agent  Google Cloud Ops Agent
    

To fix this error, run the following command to start the service:

**Linux**
    
    
    sudo service google-cloud-ops-agent start
    

**Windows**
    
    
    Start-Service google-cloud-ops-agent
    

If the service fails to start, the configuration might be invalid.

### Conflict with currently installed agents

  * The VM already has the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging) or the [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring) installed, and their configuration conflicts with the new agent's configuration. The error message might look similar to the following:

**Windows**
        
        We detected an existing Windows service for the StackdriverLogging agent,
        which is not compatible with the Ops Agent when the Ops Agent configuration
        has a non-empty logging section. Please either remove the logging section
        from the Ops Agent configuration, or disable the StackdriverLogging agent,
        and then retry enabling the Ops Agent.
        

To fix this error, you have two options:

    1. Disable the conflicting section of the Ops Agent configuration file. For more information, refer to the [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration) guide.

    2. Disable the conflicting [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging) or the [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring).

       1. Save any custom configuration files for the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/configuration#configure).
       2. Uninstall the old [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#uninstall) and [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/installation#uninstall).

After you uninstall the agent, the Google Cloud console might take up to one hour to report this change.




### Required port is unavailable

The Ops Agent or one of its components can fail to start when the port needed by the component is being used by another process. The Ops Agent uses the following ports:

  * Port 20201, for the "Metrics Agent" component
  * Port 20202, for the "Logging Agent" component



If a process other than an Ops Agent component is using port 20201 or port 20202, then stop that process and restart the Ops Agent. Use the following steps to determine which process is using the ports:

### Linux

**Metrics Agent component** : To see which process is using port 20201, use the following command:
    
    
    sudo netstat -ns -p | grep '20201'
    

The following output shows the expected result: the Ops Agent metrics collector, `otelopscol`, is using the port:
    
    
    tcp        0      0 127.0.0.1:50138         127.0.0.1:20201         ESTABLISHED 16850/otelopscol
    tcp6       0      0 :::20201                :::*                    LISTEN      16850/otelopscol
    tcp6       0      0 127.0.0.1:20201         127.0.0.1:50138         ESTABLISHED 16850/otelopscol
    

**Logging Agent component** : To see which process is using port 20202, use the following command:
    
    
    sudo netstat -ns -p | grep '20202'
    

The following output shows the expected result: the Ops Agent logs collector, `fluent-bit`, is using the port:
    
    
    tcp        0      0 0.0.0.0:20202           0.0.0.0:*               LISTEN      16640/fluent-bit
    tcp        0      0 127.0.0.1:20202         127.0.0.1:52998         TIME_WAIT   -
    

### Windows

**Metrics Agent component** : To see which process is using port 20201, use the following command:
    
    
    netstat -na -b  | Select-String "20201" -Context 0,1
    

The following output shows the expected result: the Ops Agent metrics collector, `google-cloud-metrics-agent_windows_amd64.exe`, is using the port:
    
    
    >   TCP    0.0.0.0:20201          0.0.0.0:0              LISTENING
       [google-cloud-metrics-agent_windows_amd64.exe]
    >   TCP    127.0.0.1:20201        127.0.0.1:50090        ESTABLISHED
       [google-cloud-metrics-agent_windows_amd64.exe]
    >   TCP    127.0.0.1:50090        127.0.0.1:20201        ESTABLISHED
       [google-cloud-metrics-agent_windows_amd64.exe]
    >   TCP    [::]:20201             [::]:0                 LISTENING
       [google-cloud-metrics-agent_windows_amd64.exe]
    

**Logging Agent component** : To see which process is using port 20202, use the following command:
    
    
    netstat -na -b  | Select-String "20202" -Context 0,1
    

The following output shows the expected result: the Ops Agent logs collector, `fluent-bit.exe`, is using the port:
    
    
    >   TCP    0.0.0.0:20202          0.0.0.0:0              LISTENING
       [fluent-bit.exe]
    >   TCP    127.0.0.1:20202        127.0.0.1:57535        TIME_WAIT
    >   TCP    127.0.0.1:20202        127.0.0.1:57539        TIME_WAIT
        TCP    127.0.0.1:49807        127.0.0.1:49808        ESTABLISHED
    

Port-availability errors can be detected by the [health checks](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#health-checks) run by the Ops Agent.

### Agent lacks API permissions

If the agent fails to start or fails to ingest data, then the problem might be that the "Metrics Agent" or "Logging agent" component lacks the necessary permission to access the API.

The service account used by the Ops Agent requires the following Identity and Access Management roles:

  * For the "Logging Agent" component: [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter)
  * For the "Metrics Agent" component: [Monitoring Metric Writer (`roles/monitoring.metricWriter`)](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc).



These roles include the permissions needed to write logging or metric data and must be granted to the service account associated with the VM. The service account you are using depends on how you configured the VM and authorized the agent. You might be using one of the following:

  * A service account [attached to the VM](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization#authorize_with_an_attached_service_account).
  * A service account [that uses a private key](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization#private_key_authorization).



To identify the service account associated with a VM, do the following:

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. If necessary, click the drop-down list of Google Cloud projects and select the name of your project.

  3. Select the **Instances** tab if necessary.

  4. In the list of VM instances, click on the name of the VM to view the **Details** page for the VM.

  5. Locate the **API and identity management** section of the page. The service account is listed as the value of the **Service account** field.




For information about setting the roles granted to the service account, see [Verify and modify roles of an existing service account](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization#update-svc-acct).

API-permission errors can be detected by the [health checks](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info#health-checks) run by the Ops Agent.

### Invalid configuration

If the configuration is invalid, you might see the following error when trying to restart the agent service:

**Linux**
    
    
    $ sudo service google-cloud-ops-agent restart \
        && sudo service google-cloud-ops-agent status
    ● google-cloud-ops-agent-fluent-bit.service - Google Cloud Ops Agent - Logging Agent
       Loaded: loaded (/usr/lib/systemd/system/google-cloud-ops-agent-fluent-bit.service; static; vendor preset: disabled)
      Drop-In: /usr/lib/systemd/system/google-cloud-ops-agent-fluent-bit.service.d
               └─directories.conf
       Active: failed (Result: exit-code) since Wed 2021-06-30 22:21:08 UTC; 2s ago
      Process: 1141421 ExecStart=/opt/google-cloud-ops-agent/subagents/fluent-bit/bin/fluent-bit --config ${RUNTIME_DIRECTORY}/fluent_bit_main.conf --parser ${RUNTIME_DIRECTORY}/fluent_bit_parser.conf --log_>
      Process: 1141847 ExecStartPre=/opt/google-cloud-ops-agent/libexec/google_cloud_ops_agent_engine -service=fluentbit -in /etc/google-cloud-ops-agent/config.yaml -logs ${LOGS_DIRECTORY} -state ${STATE_DIR>
     Main PID: 1141421 (code=exited, status=0/SUCCESS)
    
    Jun 30 22:21:08 centos8-2 systemd[1]: google-cloud-ops-agent-fluent-bit.service: Control process exited, code=exited status=1
    Jun 30 22:21:08 centos8-2 systemd[1]: google-cloud-ops-agent-fluent-bit.service: Failed with result 'exit-code'.
    Jun 30 22:21:08 centos8-2 systemd[1]: Failed to start Google Cloud Ops Agent - Logging Agent.
    Jun 30 22:21:08 centos8-2 systemd[1]: google-cloud-ops-agent-fluent-bit.service: Service RestartSec=100ms expired, scheduling restart.
    Jun 30 22:21:08 centos8-2 systemd[1]: google-cloud-ops-agent-fluent-bit.service: Scheduled restart job, restart counter is at 5.
    Jun 30 22:21:08 centos8-2 systemd[1]: Stopped Google Cloud Ops Agent - Logging Agent.
    Jun 30 22:21:08 centos8-2 systemd[1]: google-cloud-ops-agent-fluent-bit.service: Start request repeated too quickly.
    Jun 30 22:21:08 centos8-2 systemd[1]: google-cloud-ops-agent-fluent-bit.service: Failed with result 'exit-code'.
    Jun 30 22:21:08 centos8-2 systemd[1]: Failed to start Google Cloud Ops Agent - Logging Agent.
    

Use `journalctl` to get the exact error message:
    
    
    sudo journalctl -xe | grep "google_cloud_ops_agent_engine"
    

You might see a message similar to the following:
    
    
    Jun 30 22:00:26 centos8-2 google_cloud_ops_agent_engine[1141491]: 2021/06/30 22:00:26 the agent config file is not valid YAML. detailed error: yaml: line 21: did not find expected key
    

**Windows**
    
    
    failed to generate config files: can't parse configuration: yaml: line 20: could not find expected ':'
    

To fix the error, correct the invalid configuration and restart the agent. For reference, refer to the [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration) guide.

### Agent crashes and report mentions NVIDIA

You are attempting to run the Ops Agent on a Compute Engine VM with [ attached GPUs](https://cloud.google.com/compute/docs/gpus/create-vm-with-gpus). The agent crashes, and the output mentions NVIDIA.

This is a known issue with Ops Agent versions 2.39.0 and 2.40.0. To mitigate, install Ops Agent version 2.38.0 or versions 2.41.0 or higher. 

## Status information in the Google Cloud console is wrong

The Google Cloud console reports information about the status of agents on Compute Engine VMs in various dashboards, for example, the **VM Instances** dashboard in Cloud Monitoring. If this information does not match what you expect, the cause might simply be a delay as configuration changes work their way thought the system. But unexpected information might also indicate that the agent isn't running as you expect.

### Installed agent reported by Google Cloud console as undetected

The agent must be running and ingesting data for the Google Cloud console to recognize that the agent is present. If you have installed the agent but the console status remains "Not Detected", then the agent is not running or it is running and not ingesting data. For more information, see the following:

  * Agent is installed but not running.
  * [Agent is running, but data is not ingested](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-run-ingest#data-not-ingested).



### Removed agent reported by Google Cloud console as installed

After you uninstall the agent, the Google Cloud console might take up to one hour to report this change.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
