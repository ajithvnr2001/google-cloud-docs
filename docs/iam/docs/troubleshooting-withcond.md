---
url: https://docs.cloud.google.com/iam/docs/troubleshooting-withcond/
title: Troubleshooting \"withcond\" in policies and role bindings \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:50.380040+00:00
---

# Troubleshooting "withcond" in policies and role bindings  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/troubleshooting-withcond/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Troubleshooting "withcond" in policies and role bindings Stay organized with collections  Save and categorize content based on your preferences. 

When you view an [allow policy](https://docs.cloud.google.com/iam/docs/allow-policies), you might see role names that include the string `withcond`, followed by a hash value. For example, you might see a role name like `roles/iam.serviceAccountAdmin_withcond_2b17cc25d2cd9e2c54d8`.

This page explains when and why you might see the string `withcond` in an allow policy. It also recommends actions you should take if you see this string.

## Policy versions and conditional role bindings

An allow policy can be represented in several different forms. Each form is known as an [_allow policy version_](https://docs.cloud.google.com/iam/docs/allow-policies#versions).

In an allow policy that uses version `1`, some role bindings might contain the string `withcond` in a role name, followed by a hash value:
    
    
    {
      "bindings": [
        {
          "members": [
            "user:dana@example.com"
          ],
          **"role" : "roles/iam.serviceAccountAdmin_withcond_2b17cc25d2cd9e2c54d8"**
        }
      ],
      "etag": "BwUjMhCsNvY=",
      **"version" : 1**
    }

This format indicates that the role binding is [conditional](https://docs.cloud.google.com/iam/docs/allow-policies#conditional-bindings). In other words, the role is granted only if specific conditions are met.

Version `1` allow policies don't show these conditions. If you see the string `withcond` and a hash value, then the role binding includes a condition that you cannot see.

## Solution: Specify policy version 3

To ensure that you can view and update the entire allow policy, including its conditions, you must always specify version `3` when you get or set an allow policy. To specify version `3`, complete the tasks in the following sections.

### Update the gcloud tool

If you use the Google Cloud CLI, run `gcloud version` to check its version number. The output includes a string similar to `Google Cloud CLI 279.0.0`.

If the version number is less than 263.0.0, run `gcloud components update` to update the gcloud CLI. In version 263.0.0 and later, the gcloud CLI automatically specifies an allow policy version that supports conditions.

### Update client libraries

If your application uses a client library, follow these steps:

  1. Find the name and version number for the client library, then check the list of [client libraries that support allow policy versions](https://docs.cloud.google.com/iam/docs/allow-policies#libraries).

     * If you already use a recent version of the client library, and it supports allow policy versions, you don't need to update your client library. Continue to the next step.

     * If you use an older version of the client library, and a later version supports allow policy versions, update your client library to the latest version.

     * If you use a client library that does not support allow policy versions, you can add another client library that supports allow policy versions to your application. Use that client library to work with allow policies. Alternatively, you can use the [IAM REST API](https://docs.cloud.google.com/iam/docs/reference/rest) directly.

  2. Update any code in your application that gets and sets allow policies:

     * When you get an allow policy, always [specify version `3`](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) in the request.
     * When you set an allow policy, always [set the `version` field of the allow policy to `3`](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-set), and include the [`etag` field](https://docs.cloud.google.com/iam/docs/allow-policies#etag) in your request.

**Important:** If you omit the `etag` field, IAM allows you to overwrite the old allow policy with the new allow policy, even if this action causes data loss.



### Update REST API calls

If your application uses the [IAM REST API](https://docs.cloud.google.com/iam/docs/reference/rest) directly, update any code that gets and sets allow policies:

  * When you get an allow policy, always [specify version `3`](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) in the request.
  * When you set an allow policy, always [set the `version` field of the allow policy to `3`](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-set), and include the [`etag` field](https://docs.cloud.google.com/iam/docs/allow-policies#etag) in your request.

**Important:** If you omit the `etag` field, IAM allows you to overwrite the old allow policy with the new allow policy, even if this action causes data loss.



### Update management tools for policies

If you keep local copies of your allow policies—for example, if you store them in a version control system and treat them as code—make sure that all of the tools you use meet these criteria:

  * All requests to get or set an allow policy specify version `3`
  * All requests to set an allow policy include the `etag` field in the request



If a tool does not meet these criteria, check for an updated version of the tool.

Also, make sure your management tools preserve conditional role grants, rather than adding a duplicate role grant that does not include a condition. For example, consider the following scenario:

  1. You grant the Create Service Accounts role (`roles/iam.serviceAccountCreator`) to the user Mahan on the folder `my-folder`. The allow policy for the folder looks similar to this example:
         
         {
           "bindings": [
             **{
               "members": [
                 "user:mahan@example.com"
               ],
               "role": "roles/iam.serviceAccountCreator"
             }**
           ],
           "etag": "BuFmmMhCsNY=",
           **"version" : 1**
         }

  2. You use a tool to retrieve the allow policy and store it in a version control system.

  3. You add a condition so that Mahan can create service accounts only during the normal work week, based on the date and time in Berlin, Germany. The updated allow policy looks similar to this example:
         
         {
           "bindings": [
             {
               "members": [
                 "user:mahan@example.com"
               ],
               "role": "roles/iam.serviceAccountCreator",
               **"condition" : {
                 "title": "work_week_only",
                 "expression": "request.time.getDayOfWeek('Europe/Berlin') >= 1 && request.time.getDayOfWeek('Europe/Berlin') <= 5"
               }**
             }
           ],
           "etag": "BwWcR/B3tNk=",
           **"version" : 3**
         }

  4. You use a tool to retrieve the updated allow policy. The tool does not specify an allow policy version when it requests the allow policy, so you receive a version `1` allow policy with a modified role name:
         
         {
           "bindings": [
             {
               "members": [
                 "user:mahan@example.com"
               ],
               **"role" : "roles/iam.serviceAccountCreator_withcond_a75dc089e6fa084bd379"**
             }
           ],
           "etag": "BwWcR/B3tNk=",
           **"version" : 1**
         }




At this point, the management tool might decide that the binding from Mahan to the role `roles/iam.serviceAccountCreator` has disappeared, and that it should restore the original role binding to the allow policy:

Avoid: Additional role binding with no condition
    
    
    {
      "bindings": [
        {
          "members": [
            "user:mahan@example.com"
          ],
          "role": "roles/iam.serviceAccountCreator_withcond_a75dc089e6fa084bd379"
        },
        **{
          "members": [
            "user:mahan@example.com"
          ],
          "role": "roles/iam.serviceAccountCreator"
        }**
      ],
      "etag": "BwWd3HjhKxE=",
      **"version" : 1**
    }

**This change is not correct.** It grants the role `roles/iam.serviceAccountCreator` to Mahan regardless of the day of the week. As a result, the condition in the first role binding has no effect.

If your management tools try to make this type of change, don't approve the change. Instead, you must update your management tools to specify version `3` in requests.

## What's next

  * Learn more about [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).
  * Find out how to specify an allow policy version when you [get an allow policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) or [set an allow policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-set).
  * Understand how to grant access conditionally with [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
