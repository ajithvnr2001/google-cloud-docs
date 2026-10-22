---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/retail/
title: Retail prebuilt agent \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:18.220721+00:00
---

# Retail prebuilt agent  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/retail/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Retail prebuilt agent Stay organized with collections  Save and categorize content based on your preferences. 

The retail [playbook-based, prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt) lets you search for items, get product recommendations, and place an order.

## Sample dialogs

The following sample dialogs show common scenarios that this prebuilt agent handles.

### Search products and purchase items

The user asks about watches available in the store. The agent recommends products that meet these criteria, and the user adds them to their shopping cart. The user confirms that they want to place an order, and the agent confirms the order with a confirmation number. The user then requests phone recommendations, and the agent suggests phones, adds one to the user's cart, and places an order for the user.

User input | Agent response  
---|---  
hi |   
| Hi, I'm your Google shopping assistant. I can help you search for items and place orders. How can I help you today?  
what watches do you have |   
| We have the Google Watch. Would you like to add it to your cart?  
yes add two please |   
| You got it. I've added two Google Watches to your cart. Anything else?  
can you add one Google Pixel 8 to my cart as well? |   
| You got it. I've added one Google Pixel 8 to your cart. Anything else?  
what's in my cart? |   
| You have one Google Pixel 8 and two Google Watches in your cart. Would you like to check out?  
yes please |   
| Okay, I've placed an order containing one Google Pixel 8 and two Google Watches. Your confirmation number is QKA67DW2.  
| Is there anything else I can help you with today?  
actually can you help me find a new phone too? |   
| We have the Google Phone Pixel 8, and Google Phone Pixel 7, would you like to purchase one of these?  
yes, give me a Pixel 8 |   
| You got it. I've added one Google Phone Pixel 8 to your cart. Anything else?  
no we can check out |   
| You have one Google Phone Pixel 8 in your cart. Would you like to check out using this cart?  
yes |   
| Okay, I've placed an order for you. Your order contains one Google Phone Pixel 8. Your confirmation number is Y43KTF0T.  
| Is there anything else I can help you with today?  
no that's all for me, thanks |   
| Okay, thank you for shopping with Google! Have a nice day.  
  
### Cart management

The user asks to add some items to their cart, and then removes one before placing an order.

User input | Agent response  
---|---  
hi I want to buy a phone |   
| We have the Google Phone Pixel 8 and Google Phone Pixel 7. Which one would you like to purchase?  
give me two of the 8 |   
| You got it. I've added two Google Phone Pixel 8 to your cart. Anything else?  
actually can you remove one of them? |   
| Sure, I've removed one Google Phone Pixel 8 from your cart. Anything else?  
I'm ready to place my order |   
| Okay, I've placed an order containing one Google Phone Pixel 8. Your confirmation number is X0KP6K5T.  
| Is there anything else I can help you with today?  
no, that's it |   
| Okay, thank you for shopping with Google! Have a nice day.  
  
### Product not found

The user asks about a product that the store does not carry.

User input | Agent response  
---|---  
hi |   
| Hi, I'm your Google shopping assistant. I can help you search for items and place orders. How can I help you today?  
I want to buy a car |   
| Sorry, we don't have any cars in stock. Is there anything else you'd like to find?  
yeah, what about watches? |   
| We have the Google Watch. Would you like to add it to your cart?  
no thanks |   
| Is there anything else I can help you with today?  
nope |   
| Okay, thank you for shopping with Google! Have a nice day.  
  
### Unrecognized input

The user asks about a topic unrelated to products or ordering. The agent responds by repeating the topics it covers and asks the user what they would like help with.

User input | Agent response  
---|---  
hi |   
| Hi, I'm your Google shopping assistant. I can help you search for items and place orders. How can I help you today?  
I want to book a hotel |   
| Sorry, I can't help you with that. I can help you search for products including phones, watches, and headphones. I can also help you place orders. How can I help you today?  
  
## Basic setup

Follow these steps to set up this prebuilt agent:

  1. [Import the prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt#import).
  2. Configure the provided [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) with your external services. For more information, see Tool setup.



## Tool setup

This agent includes [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) to integrate with external services. Use the prebuilt tool installer to deploy sample code and data for your prebuilt agent.

####  To deploy and configure sample code and data for the Retail prebuilt agent, expand for instructions. 

  1. Download the [prebuilt tool installer](https://storage.googleapis.com/gassets-api-ai/prebuilt_agents/generative-prebuilt-agents/installer.zip) to a local directory. 
  2. Navigate to the local directory where you downloaded **installer.zip**.
  3. Unzip **installer.zip** and open the `installer` folder.
  4. Review README.md for a detailed overview of the installer and its requirements.
  5. Run `pip install -r requirements.txt` to install requirements.
  6. Run `gcloud auth application-default login` to authenticate using [gcloud auth](https://cloud.google.com/sdk/gcloud/reference/auth). 
  7. Run the installer using `python installer.py --project-id=YOUR_GCP_PROJECT_ID --prebuilt-id=retail`
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



### Google Store API

The Google Store API tool fetches items from the Google Store based on a search term.

### Manage shopping cart

The Manage Shopping Cart tool lets you manage your shopping cart by viewing, adding, and removing items.

### Place order

The Place Order tool places an order with the user's current shopping cart and returns a confirmation number.

### Complete

Your agent is set up and ready for testing.

[ Previous arrow_back  Movie expert  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/movie-expert)

[ Next Shopping assistant  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/shopping-assistant)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
