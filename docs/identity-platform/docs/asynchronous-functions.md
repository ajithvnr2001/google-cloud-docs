---
url: https://docs.cloud.google.com/identity-platform/docs/asynchronous-functions/
title: Customizing the authentication flow using asynchronous functions \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:55.071472+00:00
---

# Customizing the authentication flow using asynchronous functions  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/asynchronous-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Customizing the authentication flow using asynchronous functions 

This document shows you how to extend Identity Platform authentication using asynchronous [Cloud Run functions](https://docs.cloud.google.com/functions).

Asynchronous functions let you trigger non-blocking tasks in response to user creation and deletion. They are useful for starting long-running operations or performing auxiliary tasks, like sending a welcome email.

To directly modify the result of an authentication operation, see [Extending authentication with blocking functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions). The user object that an asynchronous function receives does not contain updates from the blocking function.

## Before you begin

Create an app with Identity Platform. See the [Quickstart](https://docs.cloud.google.com/identity-platform/docs/quickstart-email-password) to learn how.

## Creating an asynchronous function

To create and deploy an asynchronous function, follow the steps in [Get started: write, test, and deploy your first functions](https://firebase.google.com/docs/functions/get-started).

## Responding to user creation

The `onCreate` event triggers whenever a user account is created. This includes anonymous sessions and accounts created with the Admin SDK. The function does not trigger when a user signs in for the first time using a custom token.

The following example shows how to register a handler for `onCreate`:

###  Node.js 
    
    
    exports.myFunction = functions.auth.user().onCreate((user) => {
      // TODO.
    });
    

## Responding to user deletion

The `onDelete` event triggers whenever a user account is deleted. The following example shows how to register a handler for `onDelete`:

###  Node.js 
    
    
    exports.myFunction = functions.auth.user().onDelete((user) => {
      // TODO.
    });
    

## Getting user information

The `onCreate` and `onDelete` events provide `User` and `EventContext` objects that contain information about the created or deleted user. For example:

###  Node.js 
    
    
    exports.myFunction = functions.auth.user().onCreate((user, context) => {
      const email = user.email; // The email of the user.
      const displayName = user.displayName; // The display name of the user.
    });
    

See the [`UserRecord` API reference](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord) and the [`EventContext` API reference](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext) for a list of available fields.

## What's next

  * Extend authentication with [blocking functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions).
  * Learn more about [Cloud Run functions](https://docs.cloud.google.com/functions/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
