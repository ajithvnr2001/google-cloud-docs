---
url: https://docs.cloud.google.com/access-context-manager/docs/custom-access-levels/
title: Custom access levels \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:19.143257+00:00
---

# Custom access levels  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/custom-access-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Custom access levels Stay organized with collections  Save and categorize content based on your preferences. 

Using Access Context Manager, you can create access levels that permit access to data based on the context of a request. While Access Context Manager already provides a method of creating [basic access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level), you can also create custom access levels. Custom access levels enable your organization to use the device and context data of third-party security and endpoint management vendors to permit access to Google Cloud resources.

Custom access levels use boolean expressions written in a subset of [Common Expression Language](https://opensource.google.com/projects/cel) (CEL) to test the attributes of a client making a request.

In the Google Cloud console, custom access levels are configured using **Advanced Mode** when you create an access level.

To learn more about building CEL expressions for custom access levels, see the [custom access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec).

To start using custom access levels, see [Creating custom access levels](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level).

After custom access levels are created, they can be [managed like other access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
