---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools/
title: Manage agent pools \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:41.199569+00:00
---

# Manage agent pools  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Manage agent pools Stay organized with collections  Save and categorize content based on your preferences. 

An [agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-overview#how-agent-pools-work) is a collection of [agents](https://docs.cloud.google.com/storage-transfer/docs/on-prem-overview#how-agents-work) that use the same configuration, with uniform access and visibility to your source and destination. Agent pools also provide control over transfer bandwidth limits.

All agents must belong to an agent pool.

This guide describes how to use agent pools.

## Before you begin

You must have the correct permissions on your project to work with agent pools. Refer to [Access control with IAM](https://docs.cloud.google.com/storage-transfer/docs/access-control#on-prem-agent) for details.

You can [view your current permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#view-access).

To use `gcloud` commands, [install the gcloud command-line tool](https://docs.cloud.google.com/sdk/docs/install).

## Create an agent pool

Don't include sensitive information such as personally identifiable information (PII) or security data in your agent pool name or agent ID prefix. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

To create an agent pool:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

The **Agent pools** page is displayed, listing your existing agent pools.

  2. Click **Create another pool**.

  3. Name your pool, and optionally describe it.

  4. You may choose to set a bandwidth limit that will apply to the pool as a whole. The specified bandwidth in MB/s will be split amongst all of the agents in the pool. See [Manage network bandwidth](https://docs.cloud.google.com/storage-transfer/docs/obtaining-bandwidth-on-prem) for more information.

  5. Click **Create**.




### REST API

Use [projects.agentPools.create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/create):
    
    
    POST https://storagetransfer.googleapis.com/v1/projects/PROJECT_ID/agentPools?agent_pool_id=AGENT_POOL_ID
    

Replace the following:

  * `PROJECT_ID`: The project ID that you're creating the agent pool in.
  * `AGENT_POOL_ID`: The agent pool ID that you are creating.



If an agent pool is stuck in the `Creating` state for more than 30 minutes, we recommend deleting the agent pool and creating it again.

Revoking required Storage Transfer Service permissions from a project while an agent pool is in the `Creating` state leads to incorrect service behavior.

###  gcloud CLI 

To create an agent pool with the `gcloud` command line tool, run [`gcloud transfer agent-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create).
    
    
    gcloud transfer agent-pools create AGENT_POOL
    

Where the following options are available:

  * AGENT_POOL is a unique, permanent identifier for this pool.

  * `--no-async` blocks other tasks in your terminal until the pool has been created. If not included, pool creation runs asynchronously.

  * `--bandwidth-limit` defines how much of your bandwidth in MB/s to make available to this pool's agents. A bandwidth limit applies to all agents in a pool and can help prevent the pool's transfer workload from disrupting other operations that share your bandwidth. For example, enter '50' to set a bandwidth limit of 50 MB/s. By leaving this flag unspecified, this pool's agents will use all bandwidth available to them.

  * `--display-name` is a modifiable name to help you identify this pool. You can include details that might not fit in the pool's unique full resource name.




## Assign agents to a pool

New agent pools are empty and must have agents assigned to them. An agent can only be assigned to an agent pool at the time of the agent's creation.

If an agent pool is not specified, the agent is assigned to the `transfer_service_default` pool.

To create an agent and assign it to a pool:

###  Google Cloud console 

  1. From the [Agent pools](https://console.cloud.google.com/transfer/agent-pools) page, select the pool to assign the agent(s) to.

  2. Click **Install agent**. The Agent installation guide appears.

  3. Follow the instructions to create the agent in this agent pool.




###  gcloud CLI 

To use the `gcloud` command-line tool to create an agent and assign it to a pool, run [`gcloud transfer agents install`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agents/install). The agent must be installed on a machine with root access to the file system.
    
    
    gcloud transfer agents install --pool=AGENT_POOL
    

To install agents to use with an S3-compatible source, provide access credentials either as environment variables as the values of `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, or stored as default credentials in your system's configuration files.
    
    
    export AWS_ACCESS_KEY_ID=ID
    export AWS_SECRET_ACCESS_KEY=SECRET
    gcloud transfer agents install --pool=AGENT_POOL
    

See [Manage transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) for more details.

For additional options, see [Advanced agent options](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details).

To manage agents, see [Manage transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents).

## Assign an agent pool to a job

Once your agent pool has been created, it can be assigned to a job during job [creation](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) or [update](https://docs.cloud.google.com/storage-transfer/docs/manage-transfers).

## Update an agent pool

You can update an agent pool's display name and bandwidth limit.

To update an agent pool:

###  Google Cloud console 

In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

You can edit the following items:

  * The agent pool's display name: Click edit **Edit** next to the current **Agent pool** name.

  * The agent pool's bandwidth limit: Click **Set bandwidth limit** , and enter a new bandwidth limit in the **Set bandwidth limit** dialog. Click **Set Limit** to apply the new bandwidth limit. The bandwidth is shared across all agents in the pool.




### REST API

To update an agent pool, use [`projects.agentPools.patch`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/patch) with a [field mask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask) of the fields to update. The following agent pool fields can be updated:

  * [`displayName`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools#AgentPool.FIELDS.display_name)
  * [`bandwidthLimit`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools#AgentPool.FIELDS.bandwidth_limit)



For example, to update the `displayName` to `my-transfer`, you would provide the field mask `"displayName,my-transfer"`.

The following is an example patch request to update the display name:
    
    
    PATCH https://storagetransfer.googleapis.com/v1/projects/PROJECT_ID/agentPools/AGENT_POOL:"displayName,NEW_DISPLAY_NAME"
    

Replace the following:

  * `PROJECT_ID`: The project ID that you're updating the agent pool in.
  * `AGENT_POOL`: The name of the agent pool that you're updating.
  * `NEW_DISPLAY_NAME`: The new display name for this agent pool.



The following is an example patch request to update the bandwidth limit:
    
    
    PATCH https://storagetransfer.googleapis.com/v1/projects/PROJECT_ID/agentPools/AGENT_POOL:"bandwidthLimit,NEW_LIMIT"
    

Replace the following:

  * `PROJECT_ID`: The project ID that you're updating the agent pool in.
  * `AGENT_POOL`: The agent pool ID that you are updating.
  * `NEW_LIMIT`: The new bandwidth limit for this agent pool.



###  gcloud CLI 

To use the `gcloud` command-line tool to update an agent pool, run [`gcloud transfer agent-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update).
    
    
    gcloud transfer agent-pools update AGENT_POOL \
      [--bandwidth-limit=NEW_BANDWIDTH_LIMIT] [--clear-bandwidth-limit] \
      [--clear-display-name] [--display-name=NEW_DISPLAY_NAME]
    
    

The following argument is required:

  * AGENT_POOL is the unique, permanent identifier for this pool. `AGENT_POOL` identifies the agent pool to update, and cannot be updated itself.



The following flags can be specified with this command:

  * `--bandwidth-limit` can be updated, or removed by specifying `--clear-bandwidth-limit` instead. See [Create an agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools#create-pool) for more details about bandwidth limits.

  * `--display-name` can be updated, or deleted with the `--clear-display-name` flag instead.




## Delete an agent pool

You can delete an agent pool that has no active agents and no active job runs.

To delete an agent pool:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

  2. Click delete **Delete**. Read the pop-up, then click **Delete** to confirm.

If the delete button isn't active, you'll need to stop all agents and jobs that are associated with this pool.




### REST API

Use [projects.agentPools.delete](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/delete):
    
    
    DELETE https://storagetransfer.googleapis.com/v1/projects/PROJECT_ID/agentPools/AGENT_POOL
    

Replace the following:

  * `PROJECT_ID`: The project ID that you're deleting the agent pool from.
  * `AGENT_POOL`: The agent pool name.



###  gcloud CLI 

To use the `gcloud` command-line tool to delete an agent pool, run [`gcloud transfer agent-pools delete`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/delete).
    
    
    gcloud transfer agent-pools delete AGENT_POOL
    

The following argument is required:

  * AGENT_POOL is the unique, permanent identifier for this pool.



Before you can delete a pool, all agents in the pool must be stopped, the pool's jobs must be disabled, and there must be no in-progress transfer operations for this pool.

To view all jobs associated with a pool, [select your pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools#get-pools) in the Google Cloud console and click the **Transfer jobs** tab.

## Get an agent pool

To get an agent pool:

###  Google Cloud console 

In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

The page displays a list of all agent pools associated with your project, and the following information for each agent pool:

  * Agent pool name
  * Connection status
  * Number of connected agents
  * Bandwidth limit, if set
  * Number of associated transfer jobs
  * The agent pool's display name



To view a specific agent pool, click the agent pool's **Name**.

The following actions are available from an agent pool's information page:

  * Install agent: displays instructions for installing Transfer agents.
  * Stop agent: Select an agent in the table, then click **Stop Agent**.
  * List transfer jobs: Click **Transfer Jobs** to display the transfer jobs agents in this pool are connected to.



### REST API

Use [projects.agentPools.get](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/get):
    
    
    GET https://storagetransfer.googleapis.com/v1/projects/PROJECT_ID/agentPools/AGENT_POOL
    

Replace the following:

  * `PROJECT_ID`: The project ID that you're getting an agent pool of.
  * `AGENT_POOL`: The agent pool to retrieve.



###  gcloud CLI 

To use the `gcloud` command-line tool to retrieve an agent pool, run [`gcloud transfer agent-pools describe`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/describe).
    
    
    gcloud transfer agent-pools describe AGENT_POOL
    

The following argument is required:

  * AGENT_POOL is the unique, permanent identifier for this pool.



## List agent pools

To list your agent pools:

###  Google Cloud console 

In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

All agent pools are displayed.

### REST API

Use [projects.agentPools.list](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/list):
    
    
    GET https://storagetransfer.googleapis.com/v1/projects/PROJECT_ID/agentPools
    

Replace the following:

  * `PROJECT_ID`: The project ID for which to list agent pools.



###  gcloud CLI 

To use the `gcloud` command-line tool to list agent pools, run [`gcloud transfer agent-pools list`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list).
    
    
    gcloud transfer agent-pools list \
      [--limit=LIMIT] \
      [--names=[NAMES,...]] \
      [--page-size=PAGE_SIZE]
    

The following flags can be specified with this command:

  * `--limit` defines the maximum number of agent pools to return.

  * `--names` specifies the names of the agent pools to list. Separate multiple names with commas; for example, `--names=foo,bar`. If not specified, all agent pools in your current project are listed.

  * `--page-size` defines the batching behavior for this command. By default, the `list` command batches responses into 256 items, automatically fetching the next batch until all items are listed or `limit` is reached.




The command returns a list of matching agent pools and their configuration details. The following example shows a sample response.
    
    
    name: projects/my-project-123/agentPools/my-first-pool
    state: CREATED
    ---
    bandwidthLimit:
      limitMbps: '120'
    displayName: Source A to destination Z.
    name: projects/my-project-123/agentPools/a2z-pool
    state: CREATED
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
