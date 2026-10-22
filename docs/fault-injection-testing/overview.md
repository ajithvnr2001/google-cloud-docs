---
url: https://docs.cloud.google.com/fault-injection-testing/overview/
title: Fault Injection Testing overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:43.592181+00:00
---

# Fault Injection Testing overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/overview/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Fault Injection Testing overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Fault Injection Testing lets you do fault injection experimentation, a method of introducing faults to a system to test its resilience before they cause a real, unexpected failure that impacts your customers. With Fault Injection Testing, you can inject faults into various components in your Google Cloud environment to ensure that your application handles them in a predictable way.

For the initial release of Fault Injection Testing, faults are generally equivalent to a failure of the target resource. These failures should trigger your application to redirect traffic to healthy instances if you've designed fault tolerance into your application.

You are expected to observe your application before, during, and after injecting the fault to verify the application handled the fault as expected.

## Why use Fault Injection Testing?

Fault Injection Testing lets you run experiments on the resiliency of your applications in Google Cloud across a full spectrum of failure scenarios. A primary part of this spectrum is to run experiments to approximate Google Cloud zones and regions failing, which are difficult or impossible for you to fully run on your own. Additionally, Fault Injection Testing serves as a valuable development and improvement tool, allowing you to run experiments on your designed resilience mechanisms prior to introducing them in a production environment. Catching problems before they surface in production allows for faster improvement of designs, avoids costly downtime and reputational loss, and improves your overall experience.

Without a Google Cloud-native fault injection product, you are faced with doing your own experimentation. Doing your own experimentation is problematic – Google Cloud is a shared environment, and in many cases you may lack direct access to the underlying services and infrastructure. This scenario can result in inadequate, toilsome experimentation that may ultimately be ineffective in its goal to properly experiment with your application resilience. Fault Injection Testing helps you reduce the effort to automate these experiments, gives you access to induce failure modes you don't otherwise have access to, and improves the fidelity of your experimentation efforts.

For regulated customers, performing regular experimentation often is a requirement to remain compliant with industry-governing bodies. In these cases, the experimentation often takes the form of disaster recovery testing, showing that the failure of a zone or region won't stop the application from continuing to operate effectively.

## How to use Fault Injection Testing

Before using Fault Injection Testing, ensure the following:

  * The environments to be experimented on have some redundancy in place. When a fault is injected, this environment's application can continue to run on the redundant infrastructure.
  * For Admins or Owners of Google Cloud resources: Be thoughtful about who gets permissions to set up and run Fault Injection Testing experiments. Causing faults on running infrastructure components in your Google Cloud environment will cause disruption. Therefore, you must **grant permission only to operators who understand how their cloud environment is architected** and **how to safely experiment with the resiliency of that architecture** , so that they can configure experiments in a way that doesn't cause unintended disruptions.



Using Fault Injection Testing involves setting up an experiment. To set up a new experiment, you'll first create an experiment template, which defines the fault to be injected and the target resources. Next, you will run the experiment from the template. An experiment is the set of actions defined in the template which will run against the resources you selected in the template.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
