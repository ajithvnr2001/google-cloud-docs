---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages/
title: Configure IVR messages \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:45.180138+00:00
---

# Configure IVR messages  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure IVR messages Stay organized with collections  Save and categorize content based on your preferences. 

This section explains how to configure messages for the IVR channel. You can configure IVR messages globally and at the queue level. You can enter text-to-speech messages or upload your own custom audio files.

**Note:** Text-to-speech isn't available for Turkish, Arabic, Thai, and Vietnamese. For these languages, upload custom audio files for your IVR-specific messages.

## Configure global IVR messages

This section explains how to configure IVR messages globally.

### Configure the language selection message

You can configure a language selection message to play at the start of all IVR calls. You can also choose to skip this message.

To configure the language selection message, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Languages & Messages**. If you don't see the **Settings** menu, click menu **Menu**.

  2. For **Language Selection Message** , do one of the following:

     * To configure a text-to-speech message, do the following:

       1. Select **Text-to-speech**.

       2. In the text field, enter the language selection text that you want to play at the beginning of an IVR call—for example, `For English, press 1. For Spanish, press 2. For French, press 3. For German, press 4. For Japanese, press 5.`.

     * To upload an audio recording for language selection, do the following:

       1. Select **Upload Audio Recording for Language Selection**.

       2. Navigate to an audio recording, and then click **Open**.

     * To skip the language selection message, do the following:

       1. Select **Skip language selection**.

       2. In the **Default language** list, select your default routing language.

  3. Click **Save Languages**.




## Customize IVR-specific messages

You can customize the messages that play in the IVR workflow.

To customize IVR-specific messages, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Languages & Messages**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **IVR-specific Messages** section. This section contains several message types.

  3. Edit the text-to-speech message or upload an audio file for any message type that you want to configure.

  4. Optional: To start IVR calls without a greeting, for **IVR Greeting** , select **Skip IVR Greeting**.

**Note:** If a DAP greeting is configured on a sub-queue, it overrides this setting.
  5. Click **Save**.




### IVR message types

The following message types are available:

  * **IVR Greeting** : the initial message played before the queue menu readout. If you configure a DAP greeting message on a child queue or leaf queue, the DAP greeting message overrides the IVR greeting message on that queue.

Example: `Thank you for calling us.`

  * **Dial 0 - Back to Previous Menu** : plays after sub-queue options are played.

Example: `and press 0 to go back to the previous menu.`

  * **Invalid queue selection** : plays when the end-user selects an option that doesn't exist.

Example: `You have selected an invalid menu option.`

  * **Ask Permission to Record** : plays if **Ask User Permission To Record** is selected in the **Call Recording Settings** pane for a queue. For more information, see [Record settings at the queue level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording-config#record-settings-at-queue-level).

Example: `If you would like to not be recorded for monitoring purposes please press 1.`

  * **After Hour Deflection** : plays when an end-user calls after business hours.

Example: `Our offices are currently closed.`

  * **Overcapacity Deflection** : plays when the overcapacity call deflection threshold has been reached.

Example: `Thank you for waiting, we will be with you shortly.`

  * **Overcapacity Deflection Message Options** : lists the overcapacity deflection options that are configured in the **Settings > Calls > Overcapacity Deflection** pane and indicates which number to press to select each option. Options are listed in the order that they appear in the **Overcapacity Deflection** pane. This message plays directly after the overcapacity deflection message. If the end-user doesn't select an option, `keep waiting` is automatically selected. The overcapacity messages repeat every four minutes.

Example: `To receive a callback and keep your place in the queue, press 1. To remain on the line and keep waiting, press 2.`

  * **Overcapacity Deflection Phone Option** : plays when the end-user selects the option to deflect to a different phone number.

Example: `Please wait, your call is being redirected.`

  * **Overcapacity Deflection Callback Option** : plays when the end-user selects the callback option.

Example: `We keep your place in queue and will call you back as soon as a representative is available.`

  * **Overcapacity Deflection Wait Option** : plays when the end-user is waiting on hold.

Example: `Thank you for continuing to hold.`




## Configure queue-level IVR messages

This section explains how to configure IVR messages at the queue level. For more information, see [IVR: Add and edit queue menus](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-and-edit-ivr-queue-menus#add-and-edit-ivr-queue-menus).

### Configure the IVR menu readout

You can configure an IVR menu readout to play when an end-user arrives in a queue. You can also choose to skip this message.

To configure the IVR menu readout, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click **Menu Structure**.

  4. In the **Settings** pane, for **IVR Queue Menu Readout** , do one of the following:

     * To configure a text-to-speech message, do the following:

       1. Select **Text-to-speech**.

       2. In the text field, enter the IVR queue menu readout message—for example, `Press one for product issues, press two for order status, press three for billing information.`.

     * To upload an audio recording for the IVR queue menu readout, do the following:

       1. Select **Customized record file**.

       2. Navigate to an audio recording, and then click **Open**.

       3. Click **Save**.

     * To skip the IVR queue menu readout, do the following. This routes callers directly to the default queue that you specify. Google recommends this for single-destination call flows to speed up connections.

       1. Click **Skip IVR Menu readout**.

       2. In the **Default queue** field, enter a search keyword to find a queue. A list of queues appears.

       3. Click the queue that you want to be the default, and then click **Save**.




### Configure a parent queue message

You can configure a readout of child queues when an end-user arrives in a parent queue. Parent queues contain child queues and can't have agents assigned to them.

To configure a parent queue message, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click a parent queue.

  4. In the **Settings** pane, for **IVR Voice Settings** , do one of the following:

     * Select **Text-to-speech**. This plays a message announcing child queue options when the caller selects this queue. You can't edit this message.

Example: `For NAME_OF_CHILD_QUEUE_1, press 1, for NAME_OF_CHILD_QUEUE_2, press 2.`

     * To upload an audio recording for the parent queue message, do the following. Your audio recording should announce the child queue options—for example, `For NAME_OF_CHILD_QUEUE_1, press 1, for NAME_OF_CHILD_QUEUE_2, press 2.`.

       1. Select **Customized record file**.

       2. Navigate to an audio recording, and then click **Open**.

  5. Click **Save IVR**.




### Configure a leaf queue message

You can configure a readout that announces that the end-user has arrived at a leaf queue. Leaf queues can have agents assigned to them. They can't contain child queues.

To configure a leaf queue message, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click a leaf queue.

  4. In the **Settings** pane, for **IVR Voice Settings** , do one of the following:

     * Select **Text-to-speech**. This plays a message that announces that the queue has been selected. You can't edit this message.

Example: `You have selected NAME_OF_LEAF QUEUE.`

     * To upload an audio recording for the leaf queue message, do the following. Your audio recording should announce that the leaf queue has been selected—for example, `You have selected NAME_OF_LEAF QUEUE.`.

       1. Select **Customized record file**.

       2. Navigate to an audio recording, and then click **Open**.

  5. Click **Save IVR**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
