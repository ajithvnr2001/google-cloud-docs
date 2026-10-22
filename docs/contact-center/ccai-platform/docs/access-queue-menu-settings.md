---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/access-queue-menu-settings/
title: Access queue menu settings and configuration \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:12.269748+00:00
---

# Access queue menu settings and configuration  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/access-queue-menu-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Access queue menu settings and configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can access the settings for a queue in the following ways:

  * Browse for queue settings

  * Open a stand-alone queue settings page




You can find instructions for configuring queue settings in [Queue and menu settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup), [Multicast and deltacast](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast), and other pages in the **Routing** section of the documentation.

## Browse for queue settings

If you have many queues, browsing for a queue is a practical way to find queue settings.

To browse for queue settings, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Click **Edit / View** for the channel type of your queue.

  3. In the **Menu Structure** pane, browse for a queue, and then click it. Its settings appear.

  4. Optional: To quickly open this queue's stand-alone queue settings page later, get the following values from the URL of the current page:

     * **The queue ID** : for example, `29` in `id=29`

     * **The queue language** : for example, `en` in `language=en`




## Queue and Menu configuration

  1. Go to **Settings > Queue**.

  2. Click **Edit / View** on the channel or entry point you're interested in.

  3. Select any queue on the left-hand side.

  4. Click the **ON/OFF** switch for the metric you're interested in configuring for the queue.

  5. Enter the value you would like to set as the target.

  6. Click **Set target metrics.**




## Open a stand-alone queue settings page

You can quickly access a queue settings by opening its stand-alone queue settings page. A stand-alone queue settings page loads faster than a settings page that you browse for, and you can open it directly with a URL. You can also open stand-alone queue settings pages from the Queues menu and the Phone Number Management pane.

### Open a stand-alone queue settings page using a URL

To open a stand-alone queue settings page using a URL, enter the following in your browser:
    
    
    https://YOUR_CCAAS_HOST/queues/QUEUE_ID/LANGUAGE
    

Replace the following:

  * `YOUR_CCAAS_HOST`: your Contact Center AI Platform (CCAI Platform) host

  * `QUEUE_ID`: the queue ID. To get this value, see Browse for queue settings.

  * `LANGUAGE`: the queue language. To get this value, see Browse for queue settings.




### Open a stand-alone queue settings page from the Queues menu

To open a stand-alone queue settings page from the **Queues** menu, follow these steps:

  1. In the CCAI Platform portal, click **Queues**. If you don't see the **Queues** menu, click menu **Menu**.

  2. If you don't see your queue, use the **Search Queue** field to search for it.

  3. In the **Queue Name** column, click your queue. The stand-alone queue settings page for that queue appears. To quickly return to this settings page later, bookmark it.

**Note:** Queues in the **Queue Name** column appear as links only if you have permissions to read or edit queue settings.



### Open a stand-alone queue settings page from the Phone Number Management page

To open a stand-alone queue settings page from the **Phone Number Management** page, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Phone Numbers** pane, click **Phone Number Management**.

  3. In the **Assigned Queues / Agents** column, click your queue. The stand-alone queue settings page for that queue appears. To quickly return to this settings page later, bookmark it.

**Note:** Queues in the **Assigned Queues / Agents** column appear as links only if you have permissions to read or edit queue settings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
