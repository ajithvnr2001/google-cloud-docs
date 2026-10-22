---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/department-of-motor-vehicles/
title: Department of Motor Vehicles (DMV) prebuilt agent \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:09.348341+00:00
---

# Department of Motor Vehicles (DMV) prebuilt agent  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/department-of-motor-vehicles/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Department of Motor Vehicles (DMV) prebuilt agent Stay organized with collections  Save and categorize content based on your preferences. 

The Department of Motor Vehicles (DMV) [playbook-based prebuilt agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt) allows users to renew their driver's license online and book appointments at DMV field offices.

## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt agent.

### Renew driver's license

User requests to renew their driver's license. The agent collects required information including the user's license number, license expiration date, the name on the license, and date of birth. The agent then verifies that the license is eligible for renewal and confirms that the user would like to proceed with an online renewal. The agent creates the online application and provides a confirmation number.

User input | Agent response  
---|---  
Hi |   
| Hi, I'm your DMV assistant. I can help you renew your driver's license online and book an appointment at a DMV field office. How can I help you today?  
I'd like to renew my driver's license |   
| Please tell me your latest driver's license number.  
Yes, it's ABCD1234. |   
| Thank you, I have found your profile. Please provide the expiration date of the license.  
09-01-2023 |   
| Please tell me the name on the license.  
The name on the license is Jacky Wang |   
| Thank you. What is your date of birth?  
1985-02-03 |   
| Could you please confirm the information for me?  
Driver name: Jacky Wang  
Date of birth: 02-03-1985  
Driver's license number: ABCD1234  
Expiration date: 09-01-2023  
Yes that's right |   
| Thank you. I have verified your information. You are eligible for online renewal. Would you like to renew your driver's license online?  
Yes |   
| You have successfully applied for renewal of your driver's license. Your confirmation number is 3LKCN0JS.  
| Is there anything else I can help you with today?  
No I'm done thanks |   
| Thank you! Have a nice day.  
  
### Book appointment

User requests to book an appointment. The agent collects required information including the specific DMV office, appointment date, and appointment time. After confirming the collected details with the user, the agent books the appointment for the user and provides a confirmation number.

User input | Agent response  
---|---  
Can you help me book an appointment? |   
| I can help you book an appointment. Could you provide me with an address so that I can search for nearby DMV offices for you?  
Yes, it's 1st Main street, MN. |   
| Thank you. I have found the following nearby DMV offices for you. Could you please select one?  
1\. Minnesota Driver & Vehicle Services: 2929 Chicago Ave, Minneapolis, MN 55407  
2\. Apple Valley DMV: 15026 Glazier Ave, Apple Valley, MN 55124  
I want to go to Brooklyn DMV |   
| I'm sorry, I cannot find the DMV you provided. Could you select from the list:  
1\. Minnesota Driver & Vehicle Services  
2\. Apple Valley DMV  
Then Apple Valley DMV |   
| What date would you like to make an appointment for? I have the following available:  
1\. 12-13-2023  
2\. 12-14-2023  
3\. 12-15-2023  
If none of these dates work for you, you can also tell me another date you'd prefer.  
I want to go on December 16, 2023 |   
| Sorry, our office closes on weekends. Would you like to select one of the following dates instead?  
1\. 12-18-2023  
2\. 12-19-2023  
3\. 12-20-2023  
December 19, 2023 |   
| Thank you. What time would you like to visit? I have these times open for 12-19-2023:  
1\. 9:30  
2\. 10:00  
3\. 11:30  
nine |   
| I am sorry. 9:00 doesn't work. What time would you like to visit? I have  
1\. 9:30  
2\. 10:00  
3\. 11:30  
nine thirty |   
| Please confirm whether you'd like to book this appointment:  
DMV office: Apple Valley DMV  
Appointment date: 12-19-2023  
Appointment time: 9:30  
Yes works for me |   
| Thank you. I have booked the appointment, your confirmation number is BNFG987H.  
| Is there anything else I can help you with today?  
Nope |   
| Thanks for contacting your DMV assistant. Have a nice day!  
  
### Unrecognized input

User asks about a topic unrelated to renewing a driver's license or booking an appointment. The agent responds by clarifying what topics it can handle.

User input | Agent response  
---|---  
hi |   
| Hi, I'm your DMV assistant. I can help you renew your driver's license online and book an appointment at a DMV field office. How can I help you today?  
I want to buy a car |   
| Sorry, I didn't get that. I can help you with renewing a driver's license or booking an appointment.  
| How can I help you today?  
I want to book an appointment |   
| I can help you book an appointment. Could you provide me with an address so that I can search for nearby DMV offices for you?  
how much is this going to cost me? |   
| Sorry, I'm not able to determine expected fees. Please refer to your local DMV's website for all services and fees.  
| Would you like to continue?  
no that's it |   
| Is there anything else I can help you with today?  
no that's all |   
| Okay, thanks for contacting your DMV assistant. Have a nice day!  
  
## Basic setup

To set up this prebuilt agent:

  1. [Import the prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt#import).
  2. Configure the provided [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) with your external services, see Tool setup.



## Tool setup

This agent includes [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) that are used to integrate with external services. You can use the prebuilt tool installer to deploy sample code and data for your prebuilt agent.

####  To deploy and configure sample code and data for the DMV prebuilt agent, expand for instructions. 

  1. Download the [prebuilt tool installer](https://storage.googleapis.com/gassets-api-ai/prebuilt_agents/generative-prebuilt-agents/installer.zip) to a local directory. 
  2. Navigate to the local directory where you downloaded **installer.zip**.
  3. Unzip **installer.zip** and open the `installer` folder.
  4. Review README.md for a detailed overview of the installer and its requirements.
  5. Run `pip install -r requirements.txt` to install requirements.
  6. Run `gcloud auth application-default login` to authenticate using [gcloud auth](https://cloud.google.com/sdk/gcloud/reference/auth). 
  7. Run the installer using `python installer.py --project-id=YOUR_GCP_PROJECT_ID --prebuilt-id=dmv`
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



### Renew license tool

The `dmv_renew_tool` tool is used to verify driver's license details, including driver name, date of birth, license number, and expiration date. Once the required information has been collected and verified, this tool is used to check whether a license is eligible for renewal. If the license is eligible for renewal, the tool is used to submit a renewal application for the user.

### Book appointment tool

The `dmv_book_appointment_tool` tool retrieves available appointment information, including local offices, appointment dates, and appointment times. Once a valid office, date, and time slot have been selected, this tool is used to book the appointment.

### Complete

Your agent and its integrations should now be set up and ready to test.

[ Previous arrow_back  Airline support  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/airline)

[ Next Movie expert  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/movie-expert)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
