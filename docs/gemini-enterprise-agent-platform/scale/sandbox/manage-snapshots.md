---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/manage-snapshots/
title: Manage snapshots \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:42.923546+00:00
---

# Manage snapshots  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/manage-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Manage snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Sandbox snapshots in Gemini Enterprise Agent Platform let you save the current state of a sandbox and restore it later. This is useful for lifecycle management tasks such as restoring a known good state or exploring variation branches.

Snapshots provide several benefits for managing your agent workflows:

  * **State persistence** : Save the exact state of the sandbox, including installed libraries, file system changes, and memory state.
  * **Efficiency** : Instead of recreating a complex environment from scratch, you can restore it from a snapshot in seconds.
  * **Checkpointing** : Create checkpoints during a long-running agent task to allow recovery if something goes wrong.
  * **Branching** : Create multiple sandboxes from the same snapshot to explore different paths or test variations.



### Limitations

You cannot restore a sandbox snapshot to a new sandbox environment if any of the following conditions are true:

  * The new sandbox uses a different server architecture (for example, `amd64` versus `arm64`).
  * The new sandbox uses a different sandbox runtime version (for example, after a GKE cluster upgrade).
  * The new sandbox uses a different container image URI.



### Retention

When you create a snapshot, it's retained for the duration specified in the `ttl` property. To delete a snapshot before the TTL expires, see Delete a snapshot.

## Create a snapshot

To create a snapshot of a sandbox, use the Python SDK:
    
    
    import agentplatform
    
    client = agentplatform.Client(project='PROJECT_ID', location='LOCATION')
    sandbox_name = 'projects/PROJECT_ID/locations/LOCATION/reasoningEngines/INSTANCE_ID/sandboxEnvironments/SANDBOX_ID'
    
    snapshot_operation = client.sandboxes.snapshots.create(
        source_sandbox_environment_name=sandbox_name,
        config={
            "display_name": "DISPLAY_NAME",
            "ttl": "3600s",
        }
    )
    print(f"Snapshot creation initiated: {snapshot_operation.name}")
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The Google Cloud region of your resource. See [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).
  * `INSTANCE_ID`: The Agent Platform instance ID.
  * `SANDBOX_ID`: The existing sandbox ID to create a snapshot for.
  * `DISPLAY_NAME`: A descriptive display name for your snapshot.



## Restore from a snapshot

You can restore a sandbox state by referencing a saved snapshot when creating a new sandbox environment:
    
    
    agent_instance_name = 'projects/PROJECT_ID/locations/LOCATION/reasoningEngines/INSTANCE_ID
    snapshot_name = 'projects/PROJECT_ID/locations/LOCATION/reasoningEngines/INSTANCE_ID/sandboxEnvironments/SANDBOX_ID'
    
    # Restore from a snapshot
    new_sandbox_operation = client.sandboxes.create(
        name=agent_instance_name,
        config={
            "display_name": "restored-sandbox",
            "sandbox_environment_snapshot": snapshot_name,
        }
    )
    

## List snapshots

To list all sandbox snapshots associated with an Agent Platform instance:
    
    
    snapshots_response = client.sandboxes.snapshots.list(name=agent_instance_name)
    
    for snapshot in snapshots_response.sandbox_environment_snapshots:
        print(snapshot.name)
    

## View snapshot details

To view the configuration of a specific sandbox snapshot:
    
    
    snapshot = client.sandboxes.snapshots.get(name=snapshot_name)
    print(snapshot)
    

## Delete a snapshot

To explicitly delete a sandbox snapshot when they are no longer needed:
    
    
    client.sandboxes.snapshots.delete(name=snapshot_name)
    print("Snapshot deleted.")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
