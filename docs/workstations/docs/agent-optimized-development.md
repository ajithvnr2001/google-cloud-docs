---
url: https://docs.cloud.google.com/workstations/docs/agent-optimized-development/
title: Agent-optimized development \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:02.137896+00:00
---

# Agent-optimized development  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/agent-optimized-development/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Agent-optimized development Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Workstations provides an optimized runtime environment for autonomous and interactive AI coding agents, such as Antigravity CLI and Claude Code. When running agentic development workflows, agents frequently perform long-running, asynchronous tasks (such as code generation, deep refactoring, and test execution) or pause while waiting for human input and review.

Standard workstation idle timeouts can shut down and delete ephemeral workstation VMs during long periods of inactivity, terminating the container and requiring agent context to be reinitialized. **Agent-optimized development** solves this by combining two key features:

  1. **Workstation suspension (`IdleAction.SUSPEND`)**: This feature automatically suspends the workstation VM when it reaches its idle timeout instead of stopping it. Suspending the workstation preserves the virtual machine's RAM, running processes, open files, and active agent context to persistent storage, while stopping vCPU and memory compute costs.
  2. **Lifecycle keep-alive hooks** : These hooks allow AI agents to run a background keep-alive script (`/google/scripts/keep_alive.sh`) during active processing to prevent timeouts, and terminate the script when waiting for user input or after finishing tasks, allowing the workstation to enter an idle state and suspend.



## How agent optimization works

Agent optimization ensures persistent state, cost efficiency, and seamless operation during long-running tasks:

  * **Active processing** : When an agent begins executing user instructions, a lifecycle hook starts `/google/scripts/keep_alive.sh` in the background. This script sends periodic keep-alive signals that prevent Cloud Workstations from marking the workstation as idle.
  * **Waiting for user input or task completion** : When the agent completes its work or pauses to prompt the developer for review or additional input, an event hook terminates the background keep-alive process.
  * **Automatic suspension** : With no active keep-alive signals or incoming traffic, the workstation's idle timer counts down to the configured idle timeout threshold. Upon timing out, Cloud Workstations transitions the workstation to `STATE_SUSPENDED` rather than shutting down.
  * **Instant resumption** : When the developer returns and reconnects (through the Google Cloud console, an IDE, or SSH), the workstation resumes immediately from persistent storage with the full agent state, terminal sessions, and workspace context intact.



## Configure workstation suspension

To enable workstation suspension, update your workstation configuration with an `idleAction` set to `SUSPEND` and an `idleTimeout` duration in seconds, such as `1800s` for 30 minutes.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the `gcloud` CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

###  Console 

To configure suspension on a workstation configuration in the Google Cloud console:

  1. In the Google Cloud console, navigate to **Workstation configurations**.

[Go to Workstation configurations](https://console.cloud.google.com/workstations/configurations)

  2. Click add **Create** , or click an existing configuration and click edit **Edit**.

  3. Complete the **Basic information** section and proceed to **Machine settings**.

  4. Under **Idle timeout** , set the idle timeout duration, such as 30 minutes.

  5. In the **Idle action** drop-down, select **Suspend** (or **Suspend workstation on idle timeout**).

  6. Complete the remaining configuration steps and click **Create** (or **Save**).




###  gcloud 

To create a new workstation configuration with suspension enabled, run the [`gcloud workstations configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create) command with the `--idle-action=suspend` flag:
    
    
    gcloud workstations configs create CONFIG_NAME \
      --cluster=CLUSTER_NAME \
      --region=LOCATION \
      --idle-timeout=1800 \
      --idle-action=suspend
    

To update an existing workstation configuration to use suspension, run the [`gcloud workstations configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/update) command:
    
    
    gcloud workstations configs update CONFIG_NAME \
      --cluster=CLUSTER_NAME \
      --region=LOCATION \
      --idle-timeout=1800 \
      --idle-action=suspend
    

Replace the following:

  * `CONFIG_NAME`: the name of the workstation configuration.
  * `CLUSTER_NAME`: the name of the workstation cluster.
  * `LOCATION`: the region where the workstation cluster is located.



###  REST 

To configure suspension using the REST API, set `idleAction` to `SUSPEND` and `idleTimeout` to the chosen duration in your [`workstationConfigs`](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs) payload:
    
    
    {
      "idleTimeout": "1800s",
      "idleAction": "SUSPEND"
    }
    

## Configure agents with sample keep-alive hooks

Cloud Workstations preconfigured base images come preinstalled with sample agent configuration files under `/google/samples/agents/keepalive/`. These samples demonstrate how to configure AI coding agents to manage the keep-alive lifecycle automatically.

### How agent keep-alive hooks work

Modern AI coding agents provide event hook systems that execute commands at key lifecycle milestones:

  * **Execution start hook** : Triggered before the agent starts processing user input. The hook launches `/google/scripts/keep_alive.sh` in the background and writes the background process ID (PID) to a temporary file (for example, `/tmp/agent_keep_alive.pid`).
  * **Notification / user input wait hook** : Triggered when the agent completes its task or pauses to prompt the user for input. The hook reads the PID from the temporary file and terminates the background `keep_alive.sh` process.



### Claude Code configuration

Claude Code supports lifecycle event hooks configured in its settings. Sample configuration files for Claude Code are located in:
    
    
    /google/samples/agents/keepalive/claude/
    

In Claude Code, the following event hooks manage the keep-alive process:

  1. **`UserPromptSubmit`** : Hook runs when the user submits a prompt. It starts the keep-alive script in the background:
         
         /google/scripts/keep_alive.sh & echo $! > /tmp/claude_keep_alive.pid
         

  2. **`Notification`** : Hook runs when Claude Code emits a notification or pauses for user input. It kills the active keep-alive background process:
         
         if [ -f /tmp/claude_keep_alive.pid ]; then
           kill "$(cat /tmp/claude_keep_alive.pid)" 2>/dev/null || true
           rm -f /tmp/claude_keep_alive.pid
         fi
         




To apply the sample configuration, copy or merge the sample files from `/google/samples/agents/keepalive/claude/` into your Claude configuration directory (for example, `~/.claude/settings.json` or project-level configuration).

### Antigravity CLI configuration

Antigravity CLI supports lifecycle event hooks defined in its settings. Sample configuration files for Antigravity CLI are located in:
    
    
    /google/samples/agents/keepalive/gemini/
    

In Antigravity CLI, the following event hooks manage the keep-alive process:

  1. **`BeforeAgent`** : Hook runs before Antigravity CLI starts executing actions. It starts the keep-alive script in the background:
         
         /google/scripts/keep_alive.sh & echo $! > /tmp/gemini_keep_alive.pid
         

  2. **`Notification`** : Hook runs when the agent completes its turn or requires user feedback. It terminates the keep-alive process:
         
         if [ -f /tmp/gemini_keep_alive.pid ]; then
           kill "$(cat /tmp/gemini_keep_alive.pid)" 2>/dev/null || true
           rm -f /tmp/gemini_keep_alive.pid
         fi
         




To apply the sample configuration, copy or merge the sample files from `/google/samples/agents/keepalive/gemini/` into your Antigravity CLI configuration directory (for example, `~/.gemini/config.yaml` or project settings).

### Custom agent integration

If you build or use custom AI agents, you can implement the same keep-alive pattern by launching `/google/scripts/keep_alive.sh` as a background process during active agent execution and terminating the process when the agent enters an idle or waiting state.

## Resume a suspended workstation

When a workstation is in `STATE_SUSPENDED`, you can resume it at any time:

  * **Google Cloud console** : In the Google Cloud console, go to the **Workstations** page and click **Launch** or **Start** next to the suspended workstation.
  * **`gcloud` CLI**: Run the [`gcloud workstations start`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/start) command:
        
        gcloud workstations start WORKSTATION_NAME \
          --cluster=CLUSTER_NAME \
          --region=LOCATION \
          --config=CONFIG_NAME
        

Replace the following:

    * `WORKSTATION_NAME`: the name of the workstation.
    * `CLUSTER_NAME`: the name of the workstation cluster.
    * `LOCATION`: the region where the workstation cluster is located.
    * `CONFIG_NAME`: the name of the workstation configuration.
  * **Browser or SSH connection** : Navigating to your workstation's web URL or connecting using [SSH](https://docs.cloud.google.com/workstations/docs/ssh-support) automatically triggers the workstation to resume.




Once resumed, all terminal buffers, agent command history, and workspace files are restored exactly as you left them.

## What's next

  * [Create a workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration).
  * Learn more about [AI agent-assisted coding with Gemini CLI](https://docs.cloud.google.com/workstations/docs/ai-agent-assisted-coding-gemini-cli).
  * Explore [Preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images).
  * Learn how to [Connect with SSH support](https://docs.cloud.google.com/workstations/docs/ssh-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
