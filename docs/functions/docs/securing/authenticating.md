---
url: https://docs.cloud.google.com/functions/docs/securing/authenticating/
title: Authenticate for invocation \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:24.385361+00:00
---

# Authenticate for invocation  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/securing/authenticating/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticate for invocation

This document provides supplemental information on how to invoke functions created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis)—for example, using `gcloud functions`, the REST API, or Terraform. For detailed information and examples, see the Cloud Run [Authenticate requests](https://docs.cloud.google.com/run/docs/authenticating/overview) guides. The topics covered in the Cloud Run guides also apply to functions created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis), since v2 functions also use the [Cloud Run Invoker role](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker) (`roles/run.invoker`).

To invoke an authenticated function, the underlying **principal** must meet the following requirements:

  * Have permission to invoke the function.
  * Provide an ID token when it invokes the function.



Cloud Run functions supports two different kinds of identities, which are also called **principals** :

  * Service accounts: These are special accounts that serve as the identity of a non-person, like a function or an application or a VM. They give you a way to authenticate these non-persons.
  * User accounts: These accounts represent people, either as individual Google Account holders or as part of a Google-controlled entity like a Google Group.



See the [IAM overview](https://docs.cloud.google.com/iam/docs/overview) to learn more about basic IAM concepts.

To invoke an authenticated function, the principal must have the invoker IAM **permission** :

  * `run.routes.invoke`. This is usually through the [Cloud Run Invoker role](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker). This permission must be assigned on the Cloud Run service resource.



To grant these permissions, follow the steps in the Cloud Run [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#set-up-sa) guide.

For permission to create, update, or perform other administrative actions on a function, the principal must have an appropriate **role**. Roles include permissions that define the actions that the principal is allowed to do. See [Using IAM to Authorize Access](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam) for more information.

Event-driven functions can only be invoked by the event source that they're subscribed to. HTTP functions, however, can be invoked by different identity types originating from different places, such as by a developer testing the function or by another service using the function. Identities must provide an ID token for authentication. The account in use must also have the appropriate permissions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
