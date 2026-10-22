---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-create-session/
title: Create a session \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:32.532890+00:00
---

# Create a session  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-create-session/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Create a session Stay organized with collections  Save and categorize content based on your preferences. 

Create a session

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get answers and follow-ups](https://docs.cloud.google.com/gemini/enterprise/docs/answer)
  * [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer)



## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    
    def create_session(
        project_id: str,
        location: str,
        engine_id: str,
        user_pseudo_id: str,
    ) -> discoveryengine.Session:
        """Creates a session.
    
        Args:
            project_id: The ID of your Google Cloud project.
            location: The location of the app.
            engine_id: The ID of the app.
            user_pseudo_id: A unique identifier for tracking visitors. For example, this
              could be implemented with an HTTP cookie, which should be able to
              uniquely identify a visitor on a single device.
        Returns:
            discoveryengine.Session: The newly created Session.
        """
    
        client = discoveryengine.SessionServiceClient()
    
        session = client.create_session(
            # The full resource name of the engine
            parent=f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}",
            session=discoveryengine.Session(user_pseudo_id=user_pseudo_id),
        )
    
        # Send Session name in `answer_query()`
        print(f"Session: {session.name}")
        return session
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
