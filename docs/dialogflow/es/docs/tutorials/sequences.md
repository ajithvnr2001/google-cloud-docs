---
url: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/
title: Build a webhook for iterative confirmation of spoken sequences \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:49.449577+00:00
---

# Build a webhook for iterative confirmation of spoken sequences  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Build a webhook for iterative confirmation of spoken sequences Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial walks through building a flow for collecting long digit and alphanumeric sequences where the end-user can speak a few characters at a time. A webhook allows you to validate and confirm the sequence one section at a time, making it easy for end-users to correct the agent when it mishears "BVP" as "BBV", for example.

The lessons in the tutorial include:

  * Using regexp entities with auto speech adaptation.
  * Building webhooks to loop slot-filling.
  * Using contexts to carry data between intents.



The final interaction will behave like this:

Participant | Dialog  
---|---  
End-user | Check my order.  
Agent | What is your sequence? Please pause after a few characters so I can confirm as we go.  
End-user | 12ABC  
Agent | 12ABC. Okay, continue.  
End-user | 34DE  
Agent | 12ABC34BE. Okay, continue.  
End-user | No that's not right.  
Agent | Let's try again. What comes after 12ABC ?  
End-user | 34DE  
Agent | 12ABC34DE. Okay, continue.  
End-user | That's it.  
  
Finally, the webhook validates the full sequence and proceeeds with the rest of your flow.

[ Next Create a sequence recognizer entity  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/create-customize-agent)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
