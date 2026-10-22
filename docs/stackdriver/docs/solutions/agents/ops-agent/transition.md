---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition/
title: Transition to the Generally Available version of the Ops Agent \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:46.750788+00:00
---

# Transition to the Generally Available version of the Ops Agent  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Transition to the Generally Available version of the Ops Agent Stay organized with collections  Save and categorize content based on your preferences. 

The Ops Agent is now Generally Available. The GA version incorporates fixes and improvements based on the feedback from Preview users. This guide provides migration steps for the following users:

  * Ops Agent Preview users to migrate to the GA version of the agent.

  * Users of the legacy Logging and Monitoring agents to migrate to the Ops Agent.




## Migrating from Ops Agent Preview to the GA version

To install the latest version of the Ops Agent, complete the [Upgrading the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#upgrade) procedures.

If you edited the agent's default configuration to remove the `default_pipeline`, add the following snippet to the [agent configuration](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration) to keep that pipeline disabled:
    
    
    logging:
      service:
        pipelines:
          default_pipeline:
            receivers: []
            exporters: []
    metrics:
      service:
        pipelines:
          default_pipeline:
            receivers: []
            exporters: []
    

### Changes in commands for managing the Ops Agent

The following table lists the commands for managing the agent that changed for the GA release:

Procedure | GA version | Preview version  
---|---|---  
Starting the agent | `sudo service google-cloud-ops-agent start` | N/A  
Stopping the agent | `sudo service google-cloud-ops-agent stop` | N/A  
[Restarting the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart) | `sudo service google-cloud-ops-agent restart` | `sudo systemctl restart google-cloud-ops-agent.target`  
[Checking agent status](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-install-startup#systemd-not-running) | `sudo service google-cloud-ops-agent status` | `sudo systemctl status google-cloud-ops-agent.target`  
  
## Migrating from the legacy agents to the Ops Agent

To migrate from the legacy Logging and Monitoring agents, complete the following steps.

  1. Uninstall the [Logging](https://docs.cloud.google.com/logging/docs/agent/logging/installation#uninstall) and the [Monitoring](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#uninstall) agents.

After you uninstall the agent, the Google Cloud console might take up to one hour to report this change.

  2. Install the latest version of the [Ops Agent on a single virtual machine](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#install-latest-version).

You also have the option of [installing and managing the Ops Agent on multiple VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index).

  3. [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration) as needed.




## Differences in how metrics are collected

The following table describes differences in the data ingested by the Ops Agent and the legacy Monitoring agent. Metric type, omitting  
`agent.googleapis.com` | Ops Agent (GA)† | Ops Agent (Preview)† | Legacy Monitoring agent  
---|---|---|---  
[ `cpu_state`](https://docs.cloud.google.com/monitoring/api/metrics_agent#cpu/utilization) | The possible values for Windows are `idle`, `interrupt,`   
`system` and `user`. | The possible values for Windows are `idle`, `interrupt,`   
`system` and `user`. | The possible values for Windows are `idle` and `used`.   
[ `disk/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_agent#disk/bytes_used) and  
[ `disk/percent_used`](https://docs.cloud.google.com/monitoring/api/metrics_agent#disk/percent_used) | Ingested with the full path in the `device` label; for example, `/dev/sda15`.  
  
Not ingested for virtual devices like `tmpfs` and `udev`. | Ingested without `/dev` in the path in the `device` label; for example, `sda15`.  
  
Ingested for virtual devices like `tmpfs` and `udev`. | Ingested without `/dev` in the path in the `device` label; for example, `sda15`.  
  
Ingested for virtual devices like `tmpfs` and `udev`.  
†The **GA** column refers to Ops Agent versions 2.0.0 and higher. The **Preview** column refers to Ops Agent versions less than 2.0.0.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
