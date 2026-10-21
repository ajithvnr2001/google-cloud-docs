---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-strings/
title: Web SDK v3 strings guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:40:42.416341+00:00
---

# Web SDK v3 strings guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-strings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Web SDK v3 strings guide Stay organized with collections  Save and categorize content based on your preferences. 

This is a comprehensive list of strings used in the web SDK v3. The messages configuration can be used to customize any string that appears in the Web SDK. For more information, see [Customizing messages and translations](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-customize).

## General buttons

Component |  Values   
---|---  
`button.yes` | Yes   
`button.no` | No   
`button.cancel` | Cancel   
`button.back` | Back   
`button.exit` | Exit   
`button.end` | End   
`button.close` | Close   
`button.submit` | Submit   
`button.ok` | Okay   
`button.send` | Send   
`button.resend` | Resend   
`button.skip` | Skip   
`button.refresh` | Refresh   
`button.newConversation` | Start A New Conversation   
  
## Home page

Component  |  Values   
---|---  
`home.minimize` | Tap to minimize   
`home.support` | `{0}` Support   
`home.start` | Need any help?   
  
## Main menu

Component  |  Values   
---|---  
`menu.greeting` | Hi there, how can we help?   
`menu.backMessage` | Looks like you changed your mind! How else can we help?   
`menu.emptyMessage` | We're sorry, this support option is not available right now.   
`menu.queueMessage` | Let's help you with `{0}`  
`menu.channelsMessage` | How would you like to communicate?   
`menu.selectOption` | Select an option   
`menu.externalLinkConfirm` | Did that resolve your issue?   
`menu.deflectionDefaultMessage` | We are currently experiencing a high volume of requests with a current wait time of `{0}`. How would you like to reach out?   
`menu.deflectionAfterhourMessage` | We are currently closed. We look forward to helping you during our normal business hours.   
`menu.deflectionKeepWaitingMessage` | Thank you for continuing to wait. The remaining wait time is `{0}`.   
`menu.collectEmail` | Provide your email address   
  
## Channel selection screen

Component  |  Values   
---|---  
`channel.chat` | Chat now   
`channel.instantCall` | Call now   
`channel.scheduledCall` | Schedule call   
`channel.email` | Email   
`channel.keepWaiting` | Keep Waiting   
`channel.selectChat` | Let's connect you to one of our chat support specialists   
`channel.selectInstantCall` | Let one of our support specialists give you a call now   
`channel.selectScheduledCall` | Schedule a time for a support specialist to call and help you   
`channel.selectEmail` | Please send us an email so we can help   
  
## Deflection

Component  |  Values   
---|---  
`deflection.continueEmail` | Continue with Email Support   
`deflection.continueVa` | Continue with Virtual Agent Support   
`deflection.continueHuman` | Continue with Human Agent Support   
`deflection.vaOverCapacity` | Our customer support is experiencing exceptionally high volume. The estimated wait time is `{0}` minutes.   
`deflection.vaAfterHours` | Our support center is closed. Please select the support type you want to continue.   
`deflection.pfOverCapacity` | I'm sorry. I'm having trouble processing your request right now. I can transfer you to a human agent. However, the current estimated wait time is `{0}` minutes due to exceptionally high volume of support requests.   
`deflection.pfAfterHours` | I'm sorry. I'm having trouble processing your request right now. Our support center is currently closed as well. Please send us an email with your support request and we will respond back to you at the earliest.   
`deflection.recurring` | Thanks for your patience! The remaining wait time is `{0}`.   
`deflection.closed` | Unfortunately, our support center is currently closed. Please try reaching us later. Thank you.   
  
## Chat

Component  |  Values   
---|---  
`chat.today` | Today   
`chat.yesterday` | Yesterday   
`chat.newMessages` | `{0}` new messages   
`chat.startMessage` | One moment please...   
`chat.inputPlaceholder` | Type your message here...   
`chat.endButton` | End chat   
`chat.newButton` | New   
`chat.sameButton` | Same   
`chat.endConfirm` | Are you sure you want to end this chat?   
`chat.withOneAgent` | Chatting with `{0}.`  
`chat.withTwoAgents` | Chatting with `{0}` & `{1}`.   
`chat.withMultipleAgents` | Multiple Agents   
`chat.discussWithAgent` | Do you want to discuss this with a human agent?   
`chat.startNewButton` | Start a new chat   
`chat.dropFile` | Drag & Drop image or video here   
`chat.escalateAgent` | Escalate to agent   
`chat.addAttachment` | Add image or video attachment   
`chat.requestCobrowse` | Request Co-browse session   
`chat.timeoutHint` | Your previous chat has ended, please click to start a new chat   
`chat.dismissedHint` | Welcome Back! Do you have the same issue or a new issue?   
`event.chatDismissed` | We have not heard from you in a while. This chat session is closed. Reply back to this message to begin a new chat.   
`event.chatTimeout` | This chat has timed out   
`event.chatEnded` | This chat has ended   
`event.transferToMenu` | `{0}` is transferring this chat to another agent...   
`event.transferToAgent` | `{0}` is adding another agent to this conversation...   
`event.escalationStarted` | We are connecting you with a human agent   
`event.escalationFailed` | We're sorry. We are unable to process your request further at this moment. Please reach out to us again later. Thank you.   
`event.escalationAccepted` | `{0}` just joined the conversation   
`event.cobrowseRequestedFromAgent` | `{0}` is about to request a Co-browse session with you.   
`event.cobrowseRequestedFromEndUser` | Co-browse request sent to Agent.   
`event.cobrowseStarted` | Co-browse started.   
`event.cobrowseEnded` | Co-browse ended.   
`event.cobrowseFailed` | Co-browse failed.   
`event.taskVaStarted` | `{0}` transferred the chat to `{1}`.   
`event.taskVaFinished` | The chat with `{0}` was completed. You were returned to `{1}.`  
`event.taskVaFailed` | The chat with `{0}` failed. You were returned to `{1}`.   
`event.taskVaInterrupted` | The chat with `{0}` was interrupted by `{1}`.   
`event.taskVaCancelled` | The chat with `{0}` was cancelled by `{1}`.   
`event.taskVaDismissed` | The chat with `{0}` was dismissed. You were returned to `{1}`.   
`event.transferAccepted` | `{0}` just joined the conversation   
`event.memberLeft` | `{0}` just left the conversation   
`event.transferFailed` | Transfer has failed   
  
## Files and attachments

Component  |  Values   
---|---  
`upload.failureSize` | Looks like we couldn't upload. Please try uploading a file that is less than `{0}`.   
`upload.failureType` | Looks like we couldn't upload. We only accept .JPG, .PNG, or .MP4.   
`upload.failureUnknown` | Looks like we couldn't upload. Please try again!   
`attachment.attachments` | Attachments   
`attachment.of5` | `{0}` of 5   
`attachment.sizeTotal` | Size: `{0}`  
`attachment.sizeLimit` | Size limit: 18 MB   
`attachment.sizeRemaining` | Size remaining: `{0}`  
`attachment.countLimit` | Attach up to 5 files   
`attachment.removeFile` | Remove file   
`attachment.errorFilesize1` | The file is too big. Please attach files under `{0}`.   
`attachment.errorFilesize2` | Upload another file.   
`attachment.errorUpload1` | There was an error uploading the file.   
`attachment.errorUpload2` | Try again.   
`attachment.errorFiletype1` | File type not supported.   
`attachment.errorFiletype2` | Upload another file.   
`attachment.errorFilename1` | We can't send multiple files with the same filename.   
`attachment.errorFilename2` | Please rename or send another file.   
  
## Chat transcripts

Component  |  Values   
---|---  
`transcript.request` | Request Transcript   
`transcript.message` | Send the chat transcript to your email   
`transcript.placeholder` | Add Email   
`transcript.success1` | The transcript of the completed chat will be emailed to `{0}`.   
`transcript.success2` | The transcript of the completed chat will be emailed to `{0}` and `{1}` other recipients   
`transcript.fail` | The transcript won't be emailed.   
`transcript.overflow` | A maximum of 5 emails are allowed.   
`transcript.expired` | Delivery time expired. Transcripts can only be requested within 2 hours after the chat ends.   
`transcript.maxRequest` | A maximum of 10 transcript requests are allowed.   
`transcript.unableSend` | Unable to send. Please try again.   
  
## Editor

Component  |  Values   
---|---  
`editor.bold` | Bold   
`editor.italic` | Italic   
`editor.underline` | Underline   
`editor.orderedList` | Ordered list   
`editor.bulletedList` | Bulleted list   
`editor.placeholder` | Type your message   
`editor.showFormatting` | Show formatting   
`editor.hideFormatting` | Hide formatting   
`editor.textCountWarn` | You typed `{0}` of allowed `{1}` characters   
  
## Calls

Component  |  Values   
---|---  
`call.description` | Provide your phone number below   
`call.instantTitle` | We'll Call You   
c`all.scheduleTitle` | Let's schedule a Call   
`call.refreshTitle` | Time slots have expired   
`call.refreshContent` | Please refresh to view available time slots.   
`call.waitTime` | wait time   
`call.pickTime` | Pick a time that works best for you   
`call.recordWarning` | Your call may be monitored or recorded for training and quality assurance purposes.   
`call.recordTitle` | Call Recording   
`call.recordContent` | Do you give `{0}` permission to record your call for monitoring and training purposes?   
`call.callMe` | Call Me   
`call.wait` | Wait `{0}`  
`call.phoneNumberPlaceholder` | Your phone number   
`call.phoneNumberLabel` | Phone number   
`call.phoneNumberInvalid` | Enter a valid phone number   
`call.emailPlaceholder` | Your email address   
`call.emailLabel` | Email   
`call.emailInvalid` | Enter a valid email address   
`call.cancelTitle` | Cancel the existing call?   
`call.cancelContent` | You scheduled a support call for `{0}` at `{1}`.   
`call.keepButton` | Keep It   
`call.successTitle` | We'll Call You   
`call.successScheduledContent` | Your phone should ring around - `{0}`  
`call.successInstantContent` | Your phone should be ringing shortly   
  
## Redirection

Component  |  Values   
---|---  
`redirection.title` | Visit the page below   
`redirection.action` | Open this page in a new tab   
  
## Email

Component  |  Values   
---|---  
`email.optional` | Optional   
`email.required` | Required   
`email.send` | Send Message   
`email.sending` | Sending message...   
`email.nameLabel` | Your Name   
`email.namePlaceholder` | Enter name   
`email.emailLabel` | Your Email   
`email.emailPlaceholder` | Enter email   
`email.emailErrorEmpty` | Please enter an email address   
`email.emailErrorInvalid` | Please enter a valid email address   
`email.messageLabel` | Message   
`email.messageErrorEmpty` | Please type a message   
`email.recaptchaNotice` | This site is protected by reCAPTCHA and the Google {privacy} and {terms} apply.   
`email.privacy` | Privacy Policy   
`email.terms` | Terms of Service   
`email.success` | Thank you, your message has been sent.   
`email.deflection` | Please contact us using email: `{0}`.   
`email.oops` | Oops something went wrong!   
`email.resend` | Please try sending again.   
  
## CSAT and agent rating

Component  |  Values   
---|---  
`rating.formTitle` | Rate Your Experience   
`rating.formFeedback` | Let us know how we can improve.   
`rating.resultTitle` | Thank you!   
`rating.resultSubtitle` | We appreciate your feedback   
  
## Survey

Component  |  Values   
---|---  
`survey.errorTitle` | Uh-oh. Something went wrong.   
`survey.errorContent` | There might be an issue here. Please try again.   
survey.required  | Required   
  
## Screen Share

Component  |  Values   
---|---  
`cobrowse.confirmSessionTitle` | Screen Share Session Request   
`cobrowse.confirmSessionContent` | Do you want to share your current screen with the agent?   
`cobrowse.endSessionText` | End Screen Share Session   
`cobrowse.confirmRemoteControlTitle` | Remote Access Request   
`cobrowse.confirmRemoteControlContent` | The agent would like to have access to your currently shared screen to further assist you. Do you want to allow this?   
`cobrowse.confirmFullDeviceTitle` | Screen Share Request   
`cobrowse.confirmFullDeviceContent` | Do you want to share your full screen with the agent? The agent won't be able to control anything on the screen.   
``cobrowse.allowText  | Allow   
`cobrowse.denyText` | Deny   
  
## Text resize

Component  |  Values   
---|---  
`textResize.options` | Options   
`textResize.textSize` | Text size   
`textResize.adjustTextSize` | Adjust text size   
`textResize.header` | Set your preferred reading size   
`textResize.subHeader` | Only text will be adjusted   
`textResize.regular` | Regular   
`textResize.large` | Large   
`textResize.extraLarge` | Extra Large   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
