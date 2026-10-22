---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/email/
title: Use recommendations in emails \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:28.370273+00:00
---

# Use recommendations in emails  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Use recommendations in emails Stay organized with collections  Save and categorize content based on your preferences. 

While prediction results from AI Commerce Search are most commonly used in retail websites, you can also use recommendations in email messages. Recommendations in email are usually included as part of marketing campaign email blasts, after-order emails, or abandoned cart emails.

## Choose a model type

The Recommended for You model can be a useful model for emails because it is designed to deliver recommendations in use cases where a user hasn't indicated interest in a specific item. It works best with logged-in users that have some browsing or shopping history.

The Others You May Like model is typically used on product details pages rather than for email campaigns. However, you can use it for emails to recommend similar or complementary items to what a customer has recently viewed.

The Frequently Bought Together model is usually used on the add-to-cart page or the shopping cart page, but can also be used for email.

The Buy it Again model is designed for use on most types of pages and can also be used for email.

## Request requirements

In order to get relevant recommendations back, the [`userId`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserInfo) field must match the user ID that is associated with a logged-in user on your website or app.

Ideally, the `visitorId` field should match the user's last session ID from the site. Because the last session ID isn't always recorded, a random unique identifier can also be sent as the `visitorId` field.

Frequently Bought Together and Others You May Like models also require product IDs in the [`productDetails`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#ProductDetail) section of the predict call. For Frequently Bought Together models, the IDs can be items from a user's most recent purchase.

## Include static predictions in email

You can send static predictions by inserting data into an email template.

The `predict` method can be called in real time as emails go out, or the recommendations can be retrieved individually and saved either as part of an email template or in a database to be referenced later. To have the most up to date recommendations, call the `predict` method as close in time as possible to when the email is sent.

## Call the `predict` method for email

The AI Commerce Search [`predict` method](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/predict) takes some fields as input and returns a list of product recommendations. `visitorId`, `userId`, and `id` are used as input for most recommendations models.

Each prediction request for a user must be made individually, using code or shell scripts.

The following is pseudocode for a predict request:
    
    
    for user in userlist:
      emailTemplate.recommendations = predict(user.visitorid,user.userid,user.lastorder.id,...)
    ...
    format email template as required
    

## Include dynamic predictions in email

Although static predictions can be quickly implemented, they can become outdated more quickly than dynamic predictions. A user might not open the email for some time, and better recommendations could be available by that time. More sophisticated bulk email systems can add dynamic content by including a reference to an image in an HTML email.

The following is example HTML for an image that includes a serving config reference:
    
    
    <img src="https://example.com/recs/email?userid=47832&campaign=2020FALL&servingconfig=fbt>
    

Getting the recommendations back can be done with a Cloud Run function, or any server-side app that can make the prediction request. The predict results then need to be turned into an image. This can be done with a library, such as [ImageMagick](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/tutorials/imagemagick).

Predictions are only made for opened, viewed emails. You can also cache the results rather than creating a new image if the user opens the email again. This reduces the cost of using recommendations for emails.

Because the link destination is typically hard-coded into the email, you don't necessarily know which products will be shown. Redirecting clicks to individual product pages requires additional configuration. You'll usually use a single image for all recommendations, so using an image map can help you determine which product was clicked.

## Quotas

If you plan to run a large batch of predict requests over a short period of time, you should check your quotas. On your project's [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, check **Recommendation prediction requests per project per minute**. You can request an increase by clicking **Edit Quotas** on the quota's details page.

We recommend implementing [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) to retry requests after a delay. The service returns `HTTP 429` responses if quota is exceeded.

## Evaluate results

URL tagging lets you track and evaluate the effectiveness of campaigns. You can use [Google Analytics](https://developers.google.com/analytics/devguides/collection/protocol/v1/email) or another analytics platform to add tracking parameters to links in emails and include that data in reports. Tag recommendation clicks from emails to filter them so that you can evaluate metrics.

If you A/B test multiple recommendations, we recommend doing so within a single campaign. All standard [A/B testing guidelines](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing) for websites still apply.

## What's next

  * [Create a serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) for your model.
  * Learn how to [pause and resume training](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models#pause) for your model.
  * When the model finishes training, [start requesting recommendations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict).
  * Use [A/B experiments](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing) to understand how AI Commerce Search impacts your business.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
