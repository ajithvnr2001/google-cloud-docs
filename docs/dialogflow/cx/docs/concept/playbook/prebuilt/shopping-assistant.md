---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/shopping-assistant/
title: Shopping assistant prebuilt agent with Vertex AI Search for retail \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:17.222133+00:00
---

# Shopping assistant prebuilt agent with Vertex AI Search for retail  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/shopping-assistant/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Shopping assistant prebuilt agent with Vertex AI Search for retail Stay organized with collections  Save and categorize content based on your preferences. 

The shopping assistant [playbook-based prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt) provides retail product queries, ordering, order status, and order cancellation. It uses [Vertex AI Search for Retail](https://docs.cloud.google.com/retail/docs) and [custom fulfillment payloads](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/fulfillment), providing a rich visual experience.

## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt agent.

### Product and review comparison

The user asks to browse traditional sarees. The agent presents some popular options and the user selects the first one. The user asks for matching shoes. The agent presents popular options and the user asks to compare reviews and selects the highest-rated option. The agent asks about the size and confirms the shoes were added to the cart.

User input | Agent response  
---|---  
show me traditional sarees |   
| [Presents products] Do any of these products catch your interest, or are you after different options?  
1st one is looking good |   
| Great choice! The Indian beauty Self Design, Printed Fashion Georgette Sari is a beautiful piece. Since sarees are typically one size, it will fit perfectly. Would you like to add it to your cart?  
do you have a matching heels with it? |   
| [Presents products] Do any of these products catch your interest, or are you after different options?  
yes but can you go through the customer review and pick the best one from these |   
| The Flat n Heels Women Heels has an average rating of 4 out of 5 stars, while the Glitzy Galz Women Heels has an average rating of 4.5 out of 5 stars. Customers who purchased the Flat n Heels Women Heels had mixed reviews, with some finding them comfortable at first but uncomfortable after a few hours, while others praised their comfort. The Glitzy Galz Women Heels, on the other hand, received mostly positive reviews, with customers praising their fit, quality, and design. Which one would you like to add to your cart?  
whichever has the best review and ratings |   
| The Glitzy Galz Women Heels has the highest rating of 4.5 out of 5 stars. What size would you like to go with the Glitzy Galz Women Heels? We have sizes ranging from 5 to 11.  
6 |   
| Perfect! The Glitzy Galz Women Heels in size 6 has been added to your cart with quantity 1. Is there anything else you'd like to add to your cart?  
  
### End-to-end shopping experience

The user browses the product catalog. The agent presents recommendations based on the user's request. After a few searches, the user finds an item to purchase. The agent confirms the size and quantity of the item to purchase, as well as the expected delivery date. The user requests a different delivery date, which is not available, and agrees to the original delivery date. The agent confirms the delivery, payment and contact information on file. The user updates the delivery information and confirms. The agent places the order and provides the user with the order number.

User input | Agent response  
---|---  
It is getting cold. Do you have good sweaters |   
| [Presents products]. Do any of these products catch your interest, or are you after different options?  
I like the women's sweater for my wife, but i am looking for a boy's sweater |   
| [Presents products]. Do any of these products catch your interest, or are you after different options?  
add the first women's sweater to the cart |   
| What size would you like to go with the Nineteen Solid Round Neck Casual Women's Sweater? We have sizes ranging from extra small to extra-large.  
medium |   
| Perfect! The Nineteen Solid Round Neck Casual Women's Sweater in size medium has been added to your cart with quantity 1. Is there anything else you'd like to add to your cart?  
no |   
| The earliest we can get the Nineteen Solid Round Neck Casual Women's Sweater to you is by April 29, 2024. Does that work for you?  
can you deliver it on April 28? |   
| I'm sorry, but we're unable to deliver the Nineteen Solid Round Neck Casual Women's Sweater on April 28, 2024. The earliest we can deliver it is April 29, 2024.  
ok keep the delivery date as it is |   
| Alright, your Nineteen Solid Round Neck Casual Women's Sweater will be delivered on April 29, 2024. Now, let's review your profile details to ensure everything is up-to-date:\  
Delivery Address: 638 Maple Street, Apt 11, Cupertino, CA 95014\ |   
| Payment Info: Visa ending in 4111  
Contact Number: 416-555-5555  
Email: email@example.com  
Please review these details. If everything is correct, simply confirm. If you need to make any changes, let me know.  
my address has changed to 371 Talbot Street Carmichael, CA 95608 |   
| Your delivery address has been successfully updated to 371 Talbot Street, Carmichael, CA 95608. Is there anything else you'd like to modify?  
no |   
| Your order for the Nineteen Solid Round Neck Casual Women's Sweater has been successfully placed with the order ID ee6b4cc7. It's scheduled for delivery on April 29, 2024.  
thanks |   
| Your order has been placed successfully! Is there anything else I can help you with?  
no thanks |   
| I'm glad I could help! If you ever need anything from Cymbal Apparel, I'm just a click away.\  
  
### Checking the status of an order

The user requests to check the status of an order. The agent collects the order number and retrieves the order information. The agent provides details about the items in the order, as well as its current status and expected delivery date.

User input | Agent response  
---|---  
Hi |   
| Feel free to select from the options above, or just type in what you're looking for and I'll assist you.  
I want to check the status of my order |   
| Sure, I can help you with that. To get started, can you please provide me with your order ID?  
ee6b4cc7 |   
| Your order is confirmed! It's currently being processed.  
Here's what you ordered:  
Nineteen Solid Round Neck Casual Women's Sweater  
Size: Medium  
Quantity: 1  
Estimated Delivery: April 29, 2024  
Is there anything else I can help you with?  
No thanks |   
| I'm glad I could help! If you ever need anything from Cymbal Apparel, I'm just a click away.  
  
### Returning an order

The user wants to return an order. The agent collects the order number, retrieves the order details and confirms the item to be returned. The agent then initiates the return process and provides a return label for the user to print and attach to the package.

User input | Agent response  
---|---  
Hi |   
| Feel free to select from the options above, or just type in what you're looking for and I'll assist you.  
I want to return my order |   
| I'm here to help you with your return. To kick things off, could you please share your order number with me?  
0fc77d64 |   
| Thank you for providing your order number. I've found your order placed on April 12th, 2024. The order contains a YK Printed Boy's Round Neck Dark Blue T-Shirt in size small. Is that the item you'd like to return?  
yes |   
| Alright, I've initiated the return process. You'll find the return label attached below. Please print it out and attach it to your package before sending it back. Is there anything else I can help you with?  
No thanks |   
| I'm glad I could help! If you ever need anything from Cymbal Apparel, I'm just a click away.  
  
## Basic setup

To set up this prebuilt agent:

  1. [Import the prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt#import).
  2. Configure the provided [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) with your external services, see Tool setup.



## Tool setup

This agent includes [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) that are used to integrate with external services. In order to configure these tools, follow these steps:

  1. Create a [Firestore database](https://docs.cloud.google.com/firestore/docs/manage-databases#create_a_database) named `apparel-db`.
  2. Create a [Firestore Integration connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_firestore/configure).
  3. [Download](https://storage.googleapis.com/gassets-api-ai/prebuilt_agents/generative-prebuilt-agents/retail_assistant/apparel-search-prod-app-integration.json) the Application Integration for the Shopping Assistant.
  4. Replace all references to `projects/customermod-genai-sa/locations/us-central1/connections/firestore` with the identifier of the connector created in step 2.
  5. [Upload](https://docs.cloud.google.com/application-integration/docs/upload-download-integrations#upload-an-integration) and [publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations#publish-integrations) the integration.
  6. Grant the `Cloud Functions Invoker` roles to your Dialogflow Service Agent.
  7. Follow the steps to [set up your Retail catalog](https://docs.cloud.google.com/retail/docs/overview)
  8. Update the [attribute controls](https://docs.cloud.google.com/retail/docs/attribute-config) to make the following fields retrievable: ageGroups, availability, categories, colorFamilies, colors, conditions, cost, currencyCode, description, discount, images, materials, patterns, price, sizes, title, uri.
  9. [Import](https://docs.cloud.google.com/retail/docs/upload-catalog) the [sample catalog](https://storage.googleapis.com/gassets-api-ai/prebuilt_agents/generative-prebuilt-agents/retail_assistant/products.jsonl) into branch 1 of your catalog and make it the default branch.
  10. Download the Cloud Run Function available [here](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/dialogflow-prebuilt-agents/cloud-functions) and update `config.toml`.
  11. Follow the steps to [deploy the Cloud Run Function](https://docs.cloud.google.com/functions/docs/deploy).
  12. Grant the `Retail Viewer` IAM role to the Cloud Run Function you deployed.
  13. For the following tools: `get-order-status`, `order-lookup`, `place-order` and `return-order`, update the `paths` property to reference the integration you created in step 5 in the OpenAPI specs and choose [Service Account authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#openapi_tool_api_authentication) with a service account to which you grant the `Application Integration Invoker` role.
  14. Update the server URL property to the Cloud Run Function you deployed for remaining tools.



### Product Search

The `search-products` tool retrieves the best-matched products based on the search query and the offset value from the product catalog. The tool returns a custom payload response which includes product details. This custom payload is used by the UI to display the products in rich content form.

### Product Details

The `get-product-details` tool fetches product details from the product catalog using the Retail API. The retrieved product details are then transformed and returned in a simplified format, used by the agent to answer questions about products it has shown the user

### Product Reviews

The `get-reviews` tool is utilized to retrieve reviews for products. It expects a list of shown products and fetches reviews for each product. The generated reviews are transformed into a custom template (review_template) format suitable for display in a rich user interface.

### Similar Products

The `similar-products` tool facilitates the discovery of products similar to a specified product using the Retail Recommendation API. It accepts a product ID and utilizes the Retail Recommendation API to predict similar products from the product catalog.

### Delivery Date

The `store-delivery-date` tool is responsible for storing the user's preferred delivery date for items in the shopping cart which should be compared to the earliest estimated delivery date.

The `get-delivery-date` tool is responsible for estimating the delivery date for items in the shopping cart.

### User Details

The `get-user-info` tool retrieves the user's personal information, including shipping address, payment information, phone number and email, while the update-user-info tool is responsible for updating the user's information.

### Order Management

The `place-order` tool handles the process of placing an order for the shopping cart items. It stores the order in Firestore with the order data which includes order ID, status, creation timestamp, and list of products. It returns the order number to the agent.

The `order-lookup` tool fetches order data from a Firestore database based on the provided order ID.

The `return-order` tool updates the status of an order to 'return_pending' in the Firestore database, indicating that the return has been initiated from the customer, and the order is pending for a return.

The `get-order-status` tool is responsible for fetching the status of an order and, if the order has been shipped, tracking it using the DHL API. It provides appropriate messages based on the status of the order.

## Complete

Your agent and its integrations should now be set up and ready to test.

[ Previous arrow_back  Retail  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/retail)

[ Next Travel  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/travel)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
