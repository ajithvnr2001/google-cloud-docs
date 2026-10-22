---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/devserver/
title: Using the local development server \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:59.035788+00:00
---

# Using the local development server  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/devserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Using the local development server Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Important:** Before running the local development server, follow the [setup instructions](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server#set-up).

The [local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server) runs on your local machine and emulates most of the Search API's capabilities.

A few features are not available on the server. You should not attempt to 

### Functions in expressions

These functions are not available:

  * `pow()`



### Snippet() Expressions

The development server supports snippets, but the snippet selection and formatting algorithms are not the same as those used in a deployed app. Snippet results will not be exactly the same in the two environments.

### Stemming

Stemming of field values (for example "~cat") is not implemented. The stem operator will be ignored and the value will be treated as an ordinary exact match.

### Tokenization

String fields in Asian languages are not tokenized on the development server.

### Scoring

The match scoring mechanism is not implemented.

### Diacriticals

Diacritical marks (such as accent marks) cannot be used in atom, text, and HTML fields.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
