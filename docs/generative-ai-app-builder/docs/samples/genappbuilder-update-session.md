---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-update-session/
title: Update a session \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:40.323631+00:00
---

# Update a session  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-update-session/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Update a session Stay organized with collections  Save and categorize content based on your preferences. 

Update a session

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get answers and follow-ups](https://docs.cloud.google.com/gemini/enterprise/docs/answer)
  * [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer)



## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import discoveryengine_v1 as discoveryengine
    from google.protobuf import field_mask_pb2
    
    
    def update_session(
        project_id: str,
        location: str,
        engine_id: str,
        session_id: str,
    ) -> discoveryengine.Session:
        """Updates a session.
    
        Args:
            project_id: The ID of your Google Cloud project.
            location: The location of the app.
            engine_id: The ID of the app.
            session_id: The ID of the session.
        Returns:
            discoveryengine.Session: The updated Session.
        """
        client = discoveryengine.SessionServiceClient()
    
        # The full resource name of the session
        name = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/sessions/{session_id}"
    
        session = discoveryengine.Session(
            name=name,
            state=discoveryengine.Session.State.IN_PROGRESS,  # Options: IN_PROGRESS, STATE_UNSPECIFIED
        )
    
        # Fields to Update
        update_mask = field_mask_pb2.FieldMask(paths=["state"])
    
        session = client.update_session(session=session, update_mask=update_mask)
        print(f"Updated session: {session.name}")
        return session
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
