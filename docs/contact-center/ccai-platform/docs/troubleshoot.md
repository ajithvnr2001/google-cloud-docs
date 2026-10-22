---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/troubleshoot/
title: Troubleshooting and common solutions \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:38.319327+00:00
---

# Troubleshooting and common solutions  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Troubleshooting and common solutions Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting help and solutions for common issues.

## Troubleshooting steps

We recommend users perform the following steps if there's an issue:

  1. **Update to the latest version of your browser**. You need the most up-to-date version of a full WebRTC browser.

We support Google Chrome, Safari, and Firefox, but recommend the most recent version of Google Chrome. If you are using another browser you may see unexpected behavior.

  2. **Try to reproduce the issue in Google Chrome** before contacting support. If the issue is resolved using Google Chrome, provide this information when contacting support. If the issue is resolved using another browser, provide this information when contacting support.

  3. **Check and approve all permissions:** Contact Center AI Platform (CCAI Platform) requires permission for browser and microphone permissions. See [Granting Notification Permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/troubleshoot#notification-microphone) for more info.

  4. **Clear the cache and refresh the browser** : Often if a browser and computer have been running for a long time it's a good idea to clear the cache and restart the browser. Steps for clearing a cache in Google Chrome can be found [in this Google Chrome support article](https://support.google.com/accounts/answer/9098093?co=GENIE.Platform=Desktop&visit_id=636724965123845961-242512231&rd=1).

  5. **Ensure that third party cookies in your browser are not blocked.**

  6. **Sign out of Contact Center AI Platform (CCAI Platform) and the CRM:** Contact Center AI Platform (CCAI Platform) software works very closely with a user's CRM software. When these systems become out of sync (i.e. expired tokens), signing out and back into both helps reset the configuration.

  7. **Make sure you are signed into Contact Center AI Platform (CCAI Platform) and the CRM with the same account:** To prevent any mismatches in information transfer, you need to login to your CRM call or chat adapter with the same login credentials.

  8. **Change hardware (headsets & speakers)**\- Headsets and speakers can fail due to age, outdated drivers, or because they are incompatible with Contact Center AI Platform (CCAI Platform) or CRM software. We recommend trying different hardware, especially when audio problems are present.

  9. **Hardwired vs wireless:** Contact Center AI Platform (CCAI Platform) recommends that all agent computers be hardwired to the network using ethernet. We understand this is not always possible, but when troubleshooting is necessary, move from wireless to wired connectivity and attempt to reproduce the issue.

  10. **Change workstation:** Since not all workstations share identical configurations, a way to check whether an agent's workstation is faulty is to move the agent to a known working computer. This will also help to identify if the problem is software or hardware-based.

  11. **Reduce demands on network & CPU by other users & software:** Agents (especially work from home agents) need their networks free of latency and resource-intensive processes. We recommend all unnecessary software that could potentially hog resources (video/music streaming, torrenting software, etc) be shut off. Agent's cell phones shouldn't be connected to shared wireless networks.

**Important:** Remind Work From Home agents that someone else in their home may be using resource-intensive products on the same network.



## Common occurrences and solutions

  * All outbound calls failing for one User

    * When dialing outbound, Agent gets an error "Oops, something went wrong with the call" and when the consumer picks up a call, they hear "Your call has ended". In "Previous Calls," the call gets marked "Failed (Customer Busy) Customer party was busy".

    * Solution: Only use the Contact Center AI Platform (CCAI Platform) adapter in one browser window or tab, including incognito windows.

  * Chromebook audio conflict

    * Problem: While using a Chromebook, when a chat alert comes in during a call, the call audio is disrupted.

    * Solution: Navigate to chrome://flags/#enable-audio-focus-enforcement and change the **Audio Focus Enforcement** setting to **Disabled**.




## Troubleshooting Network Issues

This section outlines common network issues and how to troubleshoot them.

### Steps you can take to help troubleshoot network issues

  1. Set up HTTPS connection monitoring from inside of packet loss, round trip duration, and other monitoring details for your Contact Center AI Platform (CCAI Platform) URL.

It is entirely up to you to choose the monitoring services that are most suited to your needs.

  2. Monitor your bandwidth use on your network to ensure that it is not saturated.

There should be **no packet loss** and a **Round Trip-time** of less than 200 milliseconds* (*this may need to be adjusted).

  3. Confirm the issue is not with network hardware or cabling.

  4. File a ticket with your Internet service provider (ISP) indicating you are seeing high latency or packet loss and other pertinent details with our service and the other services. Other services are listed at [Agent adapter IP allow list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-adapter-ip-allow-list).




## Remote Workers: Monitoring and Adherence

Contact Center AI Platform (CCAI Platform) is set up so that managers and supervisors can manage from their desk, from an office, or from home. That also means managers can ensure quality and adherence for remote workers.

### Monitoring & adherence

  * **Review CSAT scores** : When utilizing Web or Mobile SDKs, use the CSAT measure through Contact Center AI Platform (CCAI Platform) to ensure that agents are providing quality service, regardless of their location. To make comparisons on a large scale with many agents, look at aggregate metrics such as CSAT for remote versus in-house agents.

  * **Listen to live calls or view live chats** : Utilize monitoring features to actively listen to read active support sessions. Use the Monitor feature to hear live calls and view a live chat to monitor connected chats.

  * **Monitor or change agent statues** : Use the Agents tab to view the real-time status of agents and how many calls they've taken and possibly missed.

  * **Reporting** : Use the **Agent Activity - Timeline Report** to view a detailed report of where an agent spent their time. You can compare this to a schedule to determine adherence.

![Google Chrome navigation bar](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/163064f63a9db2.png)




## Granting notification and microphone permissions

In order for agents to be able to place calls, receive calls, and see incoming call and chat notifications, permissions need to be granted in the browser.

The following steps provide you the ability to to grant permission for notifications (using Chrome v62+) as an example browser.

### Blocked adapter due to insufficient permission settings

Since these permission settings are critical to proper Contact Center AI Platform (CCAI Platform) operation, the Adapter will show a warning message and block the usage until the permissions have been granted. Follow these troubleshooting steps, and check the Troubleshooting steps if you are still having issues.

  1. If proper permissions are not allowed, the Contact Center AI Platform (CCAI Platform) adapter will be blocked from use. Follow the link on the adapter or the following instructions to enable.

  2. After following steps to enable, click the **Refresh** button.




### Granting notification and microphone permissions to websites in Chrome

There are 2 ways to grant access, one through the Chrome UI in the navigation bar, and also through your Chrome settings.

#### Chrome navigation bar

  1. From the page of your CRM where you access the Contact Center AI Platform (CCAI Platform) adapter, select the **lock** icon next to the URL in Chrome.

  2. Change the dropdowns for **Microphone** and **Notifications** to "Allow**."**




#### Chrome settings using URL

  1. Navigate to chrome://settings/content.

  2. Click **Notifications**.

  3. Click **Add**.

  4. Enter https://_yourcompany_.domain.co/:443

_yourcompany_ is your Contact Center AI Platform (CCAI Platform) environment name while Contact Center AI Platform (CCAI Platform) is the domain.

  5. Click **Add** to update.

**Note:** If you are using Kustomer, permissions need to also be granted to https://[company name].kustomerapp.com:443.
  6. Repeat the previous steps for the microphone permissions.




### Granting microphone permissions at the OS level

  * For Mac (OS/X Mojave or later), follow the steps in this resource: [Control access to your microphone on Mac.](https://support.apple.com/guide/mac-help/control-access-to-your-microphone-on-mac-mchla1b1e1fe/mac)

  * For PC, follow the steps in this resource: [Windows 10 camera, microphone, and privacy -- Microsoft privacy.](https://support.microsoft.com/en-us/help/4468232/windows-10-camera-microphone-and-privacy)




### Troubleshooting steps

If you have followed the previous steps and the adapter is still blocked by warning messages, use the following steps **_one by one_** to see which removes the warning messages in Chrome.

  1. Ensure your browser is up to date. We recommend using the latest version of Chrome, though Safari and Firefox are also supported. If you are using another browser you may see unexpected behavior. Once the update is done, **_restart_** your system.

  2. Try[ clearing your history, cache and cookies](https://support.google.com/chrome/answer/95589?co=GENIE.Platform=Desktop) (**Ctrl+Shift+Backspace**). Ensure both cache and cookies are checked. Start by clearing from the time period you started facing the issue then, if needed, expand to "beginning of time".

  3. Try using[ incognito mode](https://support.google.com/chrome/answer/95464) (**Ctrl+Shift+N**). If it helps, disable the extensions temporarily and re-enable them one at a time to determine which extension is misbehaving.

  4. Clear **Use hardware acceleration** , in your Chrome browser go to **Menu** > **Settings** > **Show Advanced Settings** > **System menu**.

  5. [Sign out](https://support.google.com/chrome/answer/2390059) of your account and [sign back in](https://support.google.com/chrome/answer/185277?co=GENIE.Platform=Desktop).

  6. Contact Google Cloud support.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
