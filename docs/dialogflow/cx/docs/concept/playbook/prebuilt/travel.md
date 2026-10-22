---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/travel/
title: Travel prebuilt agent \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:12.500239+00:00
---

# Travel prebuilt agent  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/travel/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Travel prebuilt agent Stay organized with collections  Save and categorize content based on your preferences. 

The Travel [playbook-based prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt) allows users to search for points of interest (POI), get travel recommendations, and book hotels. The agent uses user profile data to customize recommendations for the user, if provided.

## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt agent.

### POI search and hotel booking

The user asks about restaurants in Washington DC. The agent recommends a few points of interest, and the user asks to book a hotel. The agent collects required information, including the hotel, check-in date, check-out date, number of travelers, and number of rooms. The user confirms the information and the agent books the stay, providing the user with a confirmation number.

User input | Agent response  
---|---  
hi are there any good seafood restaurants in Washington DC? |   
| Here are some seafood restaurants in Washington DC:  
\- The Oceanaire Seafood Room  
\- Tony and Joe's Seafood Place  
\- Joe's Seafood, Prime Steak & Stone Crab  
| Anything else I can help you with?  
I'd like to book a stay for four nights in DC |   
| Here are some hotels in Washington DC that I found. Which one would you like to book?:  
\- Cambria Hotel Washington D.C. Navy Yard Riverfront  
\- Beacon Hotel & Corporate Quarters  
\- Holiday Inn Washington Capitol - Natl Mall, an IHG Hotel  
Beacon Hotel sounds good |   
| Great, let me just confirm a few details. You'll be staying 4 nights, from 11-06 to 11-10 correct?  
actually I'll check in on the 8th |   
| Ok, so you'll be checking in on 11-08 and checking out on 11-12?  
yes that's perfect |   
| Great, let me just confirm your booking details  
Hotel Name = Beacon Hotel & Corporate Quarters  
Check In Date = November 8th  
Check Out Date = November 12th  
# Rooms = 1  
# Travelers = 1  
  
Is that correct?  
my son will be coming with me |   
| Ok, so 2 travelers. Let me update your booking details  
Hotel Name = Beacon Hotel & Corporate Quarters  
Check In Date = November 8th  
Check Out Date = November 12th  
# Rooms = 1  
# Travelers = 2  
  
Is that correct?  
yes, please book it for me |   
| Great! We've confirmed your booking and have Confirmation # 2UDVXUUV for your records.  
| Anything else I can help you with?  
no that's it, thanks! |   
| Thanks for traveling with Google! Have a nice day.  
  
### Travel inspiration

The user says that they would like to take their family on a ski trip. The agent suggests some ski destinations in the United States, and the user asks if the agent has any recommendations out of the country. The agent presents a list of destinations outside of the United States. Finally, the user asks the agent to book a stay at one of the destinations and the agent presents a list of hotels nearby.

User input | Agent response  
---|---  
I'd like to take my family on a ski trip, any suggestions? |   
| I love skiing! Here's a few popular ski destinations in the United States:  
\- Arapahoe Basin  
\- Aspen Highlands  
\- Beaver Creek  
\- Breckenridge  
\- Sun Peaks Resort  
I was thinking somewhere outside of the states, do you have anything in mind? |   
| Of course! Here are some popular ski destinations outside of the United States:  
\- St. Moritz  
\- Niseko United  
\- Hakuba Valley  
\- Nozawa Onsen  
\- Whistler Blackcomb  
\- Big White Ski Resort  
\- Sun Peaks Resort  
great, thanks! can you book me a stay at Whistler Blackcomb? |   
| Here are some hotels in Whistler Blackcomb. Which one would you like to book?:  
\- Blackcomb Lodge  
\- Blackcomb Springs Suites - True Ski-in, Ski-out Resort  
\- Pinnacle Hotel Whistler  
\- Fairmont Château Whistler  
  
## Basic setup

To set up this prebuilt agent:

  1. [Import the prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt#import).
  2. Configure the provided [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) with your external services, see Tool setup.



## Tool setup

This agent includes [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) that are used to integrate with external services. You can use the prebuilt tool installer to deploy sample code and data for your prebuilt agent.

####  To deploy and configure sample code and data for the Travel prebuilt agent, expand for instructions. 

  1. Download the [prebuilt tool installer](https://storage.googleapis.com/gassets-api-ai/prebuilt_agents/generative-prebuilt-agents/installer.zip) to a local directory. 
  2. Navigate to the local directory where you downloaded **installer.zip**.
  3. Unzip **installer.zip** and open the `installer` folder.
  4. Review README.md for a detailed overview of the installer and its requirements.
  5. Run `pip install -r requirements.txt` to install requirements.
  6. Run `gcloud auth application-default login` to authenticate using [gcloud auth](https://cloud.google.com/sdk/gcloud/reference/auth). 
  7. Run the installer using `python installer.py --project-id=YOUR_GCP_PROJECT_ID --prebuilt-id=travel`
  8. After deploying all required services, configure each tool in the prebuilt agent with the provided URL(s) logged by the installer: 

### Generative AI App Builder

     1. If you have not yet imported the prebuilt agent, [import the agent into your project](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt#import). 
     2. Go to the **Generative AI App Builder**. 

[Generative AI App Builder](https://console.cloud.google.com/gen-app-builder//start)

     3. Select your project from the console drop-down.
     4. Select your app.
     5. Click on the icon for **Tools**.
     6. For each tool in the agent, edit the schema to replace the URL in the `servers:` field with the endpoint logged by the installer. 
     7. Click **Save**.

### Dialogflow CX

     1. If you have not yet imported the prebuilt agent, [import the agent into your project](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt#import). 
     2. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
     3. Choose your Google Cloud project.
     4. Select your agent.
     5. Click on the icon for **Generative resources**.
     6. Click **Tools**.
     7. For each tool in the agent, edit the schema to replace the URL in the `servers` field with the endpoint logged by the installer. 
     8. Click **Save**.
  9. Grant the Compute Engine service account (`your-project-number-developer.gserviceaccount.com`) the **Cloud Datastore User** role, so the newly deployed Cloud Run functions can access Firestore. 



### Places search

The `places_search` tool is used to get information about points of interest, including points of interest near a location.

### Hotel search

The `hotel_search` tool is used to get information about hotels, including hotels near a location.

### Hotel booking

The `hotel_booking` tool is used to create and get information about hotel bookings.

### Get user profile

The `get_user_profile` tool is used to retrieve user profiles that can be used to customize recommendations for the user.

### Complete

Your agent and its integrations should now be set up and ready to test.

[ Previous arrow_back  Shopping assistant  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/shopping-assistant)

[ Next Flow-based prebuilt agents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agents-prebuilt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
