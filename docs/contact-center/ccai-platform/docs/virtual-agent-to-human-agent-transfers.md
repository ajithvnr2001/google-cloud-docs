---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-to-human-agent-transfers/
title: Virtual agent to human agent transfers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:10.693906+00:00
---

# Virtual agent to human agent transfers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-to-human-agent-transfers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agent to human agent transfers Stay organized with collections  Save and categorize content based on your preferences. 

You can use custom payloads with [Gemini Enterprise for Customer Experience](https://docs.cloud.google.com/customer-engagement-ai) or [Dialogflow](https://docs.cloud.google.com/dialogflow/docs) to configure your virtual support agents to transfer a voice session directly to a human agent. You can identify the human agent using the agent's extension number or agent ID. Transferring directly to a human agent eliminates the intermediate step of transferring to a queue before transferring to the agent. This can improve wait times and customer satisfaction. Human agents can see conversation history in the call adapter when virtual agents transfer calls.

## Deflections

If you've configured queue-level deflections for after hours or overcapacity, Google recommends using agent extensions to transfer calls from virtual agents to human agents. Transfers using agent extensions support deflections, while transfers using agent IDs don't support them.

## Custom payload using an agent extension

The following is an example of a custom payload for a virtual agent to human agent transfer using an agent extension:
    
    
    {
      "ujet": {
        "type": "action",
        "action": "direct",
        "escalation_reason": "ESCALATION_REASON",
        "allow_virtual_agent": false,
        "agent_extension": AGENT_EXTENSION,
        "fallback_menu": FALLBACK_MENU,
        "language": "LANGUAGE"
      }
    }
    

Replace the following:

  * `ESCALATION_REASON`: possible values:

    * `by_virtual_agent`: a planned transfer.

    * `by_consumer`: an escalation.

  * `AGENT_EXTENSION`: the extension number of the agent to transfer the call to.

  * `FALLBACK_MENU`: the menu ID for the queue to fall back to if the transfer fails. For more information, see Fallback behavior.

  * `LANGUAGE`: the queue language to fall back to. Default: the virtual agent's current language.




## Custom payload using an agent ID

The following is an example of a custom payload for a virtual agent to human agent transfer using an agent ID.

**Note:** Google recommends using an agent extension to transfer calls to a human agent when possible. For more information, see Deflections.
    
    
    {
      "ujet": {
        "type": "action",
        "action": "direct",
        "escalation_reason": "ESCALATION_REASON",
        "allow_virtual_agent": false,
        "agent_id": AGENT_ID,
        "fallback_menu": FALLBACK_MENU,
        "language": "LANGUAGE"
      }
    }
    

Replace the following:

  * `ESCALATION_REASON`: possible values:

    * `by_virtual_agent`: a planned transfer.

    * `by_consumer`: an escalation.

  * `AGENT_ID`: the agent ID of the agent to transfer the call to.

  * `FALLBACK_MENU`: the menu ID for the queue to fall back to if the transfer fails. For more information, see Fallback behavior.

  * `LANGUAGE`: the queue language to fall back to. Default: the virtual agent's current language.




## Fallback behavior

If a transfer from a virtual agent to a human agent fails (for example, if the agent extension number or agent ID is invalid) the system initiates the following fallback sequence:

  * **First fallback:** The system transfers the end-user to the queue of the current session. If this fallback fails (for example, there are no human agents assigned to the queue), then the system attempts the second fallback.

  * **Second fallback:** The system transfers the end-user to the queue specified by `fallback_menu` in the custom payload. If this fallback fails, then the call ends.




## Reporting

How transfers appear in dashboards depends on their `escalation_reason` value:

  * **`by_virtual_agent`** : appears as **Planned Transfers**.

  * **`by_consumer`** : appears as **Escalated**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
