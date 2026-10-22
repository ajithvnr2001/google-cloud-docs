---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/citrix/
title: Citrix Workspace \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:42.312045+00:00
---

# Citrix Workspace  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/citrix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Citrix Workspace Stay organized with collections  Save and categorize content based on your preferences. 

Citrix Workspace is a digital workspace platform that provides a unified experience for accessing applications, desktops, and data from any device. You use Citrix Workspace to deliver virtual resources, including applications, desktops, and files, on various devices. The virtual desktop environment is often used by enterprises for agent interfaces.

Contact Center AI Platform (CCAI Platform) has been validated to work with Citrix Workspace. There are security features of Citrix Workspace that require specific configuration for successful use and compliance when using with CCAI Platform. 

To learn more about Citrix Workspace, see [Citrix Workspace product pages](https://www.citrix.com/platform/citrix-app-and-desktop-virtualization/).

## Citrix Browser Content Redirection

Citrix Browser Content Redirection (BCR) optimizes the delivery of web browser content to users in virtual environments. One capability of CBR is Offloads Rendering, which shifts the rendering of a web page to an end user's local device instead of rendering the page on a virtual desktop infrastructure (VDI). CBR creates a "browser within a browser" by intercepting the browser content and using the local browser engine to display it.

This offloading reduces the workload on the VDI, leading to improved performance, especially for complex or graphics-intensive web pages. It also minimizes bandwidth consumption because only the rendered output needs to be transmitted. This is ideal for situations where users heavily rely on web browsers within their virtual desktops, such as accessing rich web applications or streaming media.

When using Citrix Workspace, you need to configure Client Fetch & Client Render. This is a redirection rule that enables the agent adapter to route webRTC voice traffic through the agent's local internet connection instead of routing it through the Citrix backend server's internet connection.

For information about how to configure BCR within Citrix, see [Browser content redirection](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/multimedia/browser-content-redirection.html).

**Important:** When using the BCR method, browser notifications are not passed. Agents hear the ringing and see the flashing from the agent adapter, but no browser notifications is displayed.

## Configuring the Citrix Studio policy

To configure a Citrix Studio policy, you must create a policy that specifies an Access Control List (ACL). The policy ACL contains the URL of the System of Record (for example, a CRM or ticketing system) for redirection. The agent adapters make use of an HTML iframe that is embedded into an agent desktop. That agent desktop could be a CRM, a system of record, a ticketing system, or a web page that includes information for your agent. This is the URL that will need to be added to the ACL in Citrix Studio.

If CCAI Platform is in standalone mode (without a System of Record), you should point the policy to the URL of the CCAI Platform instance.

## Installing the BCR browser extension

For instructions to install the BCR browser extension in your Chrome browser, see [Browser content redirection Chrome extension](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/multimedia/browser-content-redirection.html#browser-content-redirection-chrome-extension).

The browser extension for Chrome is available in the Chrome Web Store, and you can deploy it using the Group Policies and ADMX files.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
