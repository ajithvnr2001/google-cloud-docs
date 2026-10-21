---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-customize/
title: Customize messages and translations \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:07:59.883262+00:00
---

# Customize messages and translations  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-customize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Customize messages and translations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** A message won't be sent to the end-user if the default string is empty.

The `messages` configuration can be used to customize any string that appears in the Web SDK. This includes existing languages or adding new languages (ex. `de`, `es`, `fr`, `ja`).
    
    
    ccaas.config({
      messages: {
        [lang]: {
          [group]: {
            [key]: '__string__'
          }
        }
      }
    })
    

The following is an example of a `messages` object which is customizing an English copy:
    
    
    ccaas.config({
     messages: {
       en: {
         button: {
           yes: 'OK'
          }
       }
     }
    })
    

For a list of all web SDK messages that you can customize, see the [Web SDK v3 Strings Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-strings).

## Common messages

These messages are used everywhere the common element appears throughout the the web SDK.

### button
    
    
    {
      "yes": "Yes",
      "no": "No",
      "cancel": "Cancel",
      "back": "Back",
      "exit": "Exit",
      "end": "End",
      "close": "Close",
      "submit": "Submit",
      "ok": "Okay",
      "send": "Send",
      "resend": "Resend",
      "skip": "Skip",
      "refresh": "Refresh",
      "continueConversation": "Continue conversation",
      "newConversation": "Start A New conversation"
    }
    

Example:
    
    
    ccaas.config({
      messages: {
        en: {
          button: {
            yes: 'OK'
          }
        }
      }
    })
    

## Home page

These messages are only used on the Home Page. This is typically the first screen a consumer sees when starting the web SDK.

### Home
    
    
    {
      "minimize": "Tap to minimize",
      "support": "{0} Support",
      "start": "Need any help?"
    }
    ccaas.config({
      messages: {
        en: {
          home: {
            start: 'Hi, how can I help you?'
          }
        }
      }
    })
    

## Menu page

These messages are used on the Menu screens. These include the queue and channel selection screens.

### menu
    
    
    {
      "greeting": "Hi there, how can we help?",
      "backMessage": "Looks like you changed your mind! How else can we help?",
      "emptyMessage": "We're sorry, this support option is not available right now.",
      "queueMessage": "Let's help you with {0}",
      "channelsMessage": "How would you like to communicate?",
      "selectOption": "Select an option",
      "externalLinkConfirm": "Did that resolve your issue?",
      "deflectionDefaultMessage": "We are currently experiencing a high volume of requests with a current wait time of {0}. How would you like to reach out?",
      "deflectionAfterhourMessage": "We are currently closed. We look forward to helping you during our normal business hours.",
      "deflectionKeepWaitingMessage": "Thank you for continuing to wait. The remaining wait time is {0}.",
      "collectEmail": "Provide your email address",
      "additionalOptions": "Additional options",
      "ahdOptionsCloseMessage": "We're sorry, but we're unable to continue this conversation because our support center is now closed. Please select from one of the available options."
    }
    

### channel
    
    
    {
      "chat": "Chat now",
      "instantCall": "Call now",
      "scheduledCall": "Schedule call",
      "email": "Email",
      "keepWaiting": "Keep Waiting",
      "selectChat": "Let's connect you to one of our chat support specialists",
      "selectInstantCall": "Let one of our support specialists give you a call now",
      "selectScheduledCall": "Let's schedule a time for a support specialist to call and help you",
      "selectEmail": "Please send us an email so we can help"
    }
    

## Redirection

These messages are used pages that include redirection messages.

### redirection
    
    
    {
      "title": "Visit the page below",
      "action": "Open this page in a new tab"
    }
    Example:
    ccaas.config({
      messages: {
        en: {
          redirection: {
            action: 'Open a new tab'
          }
        }
      }
    })
    

## Call channel

These messages are used when a user selects the call channel.

### call

The following code sample contains standard call channel messages:
    
    
    {
      "description": "Provide your phone number below",
      "instantTitle": "We'll Call You",
      "scheduleTitle": "Let's Schedule a Call",
      "refreshTitle": "Time slots have expired",
      "refreshContent": "Please refresh to view available time slots.",
      "waitTime": "wait time",
      "pickTime": "Pick a time that works best for you",
      "recordWarning": "Your call may be monitored or recorded for training and quality assurance purposes.",
      "recordTitle": "Call Recording",
      "recordContent": "Do you give {0} permission to record your call for monitoring and training purposes?",
      "callMe": "Call Me",
      "wait": "Estimated wait time: {0}",
      "phoneNumberPlaceholder": "Your phone number",
      "phoneNumberLabel": "Phone number",
      "phoneNumberInvalid": "Enter a valid phone number",
      "emailPlaceholder": "Your email address",
      "emailLabel": "Email",
      "emailInvalid": "Enter a valid email address",
      "cancelTitle": "Cancel the existing call?",
      "cancelContent": "You scheduled a support call for {0} at {1}.",
      "keepButton": "Keep It",
      "successTitle": "We'll Call You",
      "successScheduledContent": "Your phone should ring around - {0}",
      "successInstantContent": "Your phone should be ringing shortly"
    }
    

The following code sample contains [scheduled call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#scheduled-calls) messages.
    
    
    {
      "scheduledCallSelectTime": "Select a time.",
      "scheduledCallGenericFailure": "Unable to schedule call.",
      "scheduledCallSuccessFirst": "Scheduled Call.",
      "scheduledCallCancelLabel": "Cancel call?",
      "scheduledCallUnavailableLabelFirst": "Time slot unavailable.",
      "scheduledCallCancelSuccess": "Call successfully cancelled.",
      "scheduledCallSelectDay": "Select a day.",
      "noTimeSlots": "No time slots available.",
      "scheduledCallTryAgain": "Please try again.",
      "scheduledCallSuccessSecond": "We will call you.",
      "scheduledCallCancelAreYouSure": "Are you sure you want to cancel this call? This action cannot be undone.",
      "scheduledCallUnavailableLabelSecond": "This slot is no longer available. Please select another time.",
      "scheduledCallInvalidEmail": "Enter a valid email."
    }
    

The following code sample contains buttons for [scheduled calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#scheduled-calls).
    
    
    {
      "button.rescheduleCall": "Reschedule call.",
      "button.scheduleCall": "Schedule call.",
      "button.cancelCall": "Cancel call.",
      "button.keepCall": "Keep call."
    }
    

## Chat channel

These messages are used once a consumer selects the chat channel.

### chat
    
    
    {
      "today": "Today",
      "yesterday": "Yesterday",
      "newMessages": "{0} new messages",
      "startMessage": "One moment please...",
      "inputPlaceholder": "Type your message here...",
      "endButton": "End chat",
      "endConfirm": "Are you sure you want to end this chat?",
      "withOneAgent": "Chatting with {0}",
      "withTwoAgents": "Chatting with {0} & {1}",
      "withMultipleAgents": "Multiple Agents",
      "discussWithAgent": "Do you want to discuss this with a human agent?",
      "dropFile": "Drag & Drop image or video here",
      "escalateAgent": "Escalate to agent",
      "addAttachment": "Add image or video attachment",
      "requestCobrowse": "Request Co-browse session",
      "timeoutHint": "Your previous chat has ended, please click to start a new chat",
      "dismissedHint": "Welcome Back! Do you have the same issue or a new issue?"
    }
    

### upload
    
    
    {
      "failureSize": "Looks like we couldn't upload. Please try uploading a file that is less than {0}.",
      "failureType": "Looks like we couldn't upload. We only accept .JPG, .PNG, or .MP4.",
      "failureUnknown": "Looks like we couldn't upload. Please try again!"
    }
    

### transcript
    
    
    {
          "requestTranscript": "Request Transcript",
          "message": "Send the chat transcript to your email",
          "placeholder": "Add Email",
          "success1": "The transcript of the completed chat will be emailed to {0}",
          "success2": "The transcript of the completed chat will be emailed to {0} and {1} other recipients",
          "fail": "The transcript will not be emailed.",
          "overflow": "A maximum of 5 emails are allowed.",
          "expired": "Delivery time expired. Transcripts can only be requested within 2 hours after the chat ends.",
          "maxRequest": "A maximum of 10 transcript requests are allowed.",
          "unableSend": "Unable to send. Please try again.",
          "requested": "Transcript requested",
          "emailTranscript": "Email transcript",
          "request": "Request",
          "helpText": "Enter up to 5 email addresses",
          "deleteEmail": "Delete email",
          "downloadTranscript": "Download transcript",
          "updated": "Transcript request updated",
          "invalidEmail": "Invalid email address. Please enter a valid email.",
          "emptyEmail": "Please enter a valid email.",
          "requestCompleted": "Transcript request completed"
    }
    

### event
    
    
    {
      "chatDismissed": "We have not heard from you in a while. This chat session is closed.",
      "chatTimeout": "This chat has timed out",
      "chatEnded": "This chat has ended",
      "transferToMenu": "{0} is transferring this chat to another agent...",
      "transferToAgent": "{0} is adding another agent to this conversation...",
      "escalationStarted": "We are connecting you with a human agent",
      "escalationFailed": "We're sorry. We are unable to process your request further at this moment. Please reach out to us again later. Thank you.",
      "escalationAccepted": "{0} just joined the conversation",
      "cobrowseRequestedFromAgent": "{0} is about to request a Co-browse session with you.",
      "cobrowseRequestedFromEndUser": "Co-browse request sent to Agent.",
      "cobrowseStarted": "Co-browse started.",
      "cobrowseEnded": "Co-browse ended.",
      "cobrowseFailed": "Co-browse failed.",
      "taskVaStarted": "{0} transferred the chat to {1}",
      "taskVaFinished": "The chat with {0} was completed. You were returned to {1}",
      "taskVaFailed": "The chat with {0} failed. You were returned to {1}",
      "taskVaInterrupted": "The chat with {0} was interrupted by {1}",
      "taskVaCancelled": "The chat with {0} was cancelled by {1}",
      "taskVaDismissed": "The chat with {0} was dismissed. You were returned to {1}",
      "transferAccepted": "{0} just joined the conversation",
      "memberLeft": "{0} just left the conversation",
      "transferFailed": "Transfer has failed"
    }
    

### rating
    
    
    {
      "formTitle": "Rate Your Experience",
      "formFeedback": "Let us know how we can improve.",
      "resultTitle": "Thank you!",
      "resultSubtitle": "We appreciate your feedback"
    }
    

### survey
    
    
    {
      "errorTitle": "Uh-oh. Something went wrong.",
      "errorContent": "There might be an issue here. Please try again.",
      "required": "Required"
    }
    

### deflection
    
    
    {
      "continueEmail": "Continue with Email Support",
      "continueVa": "Continue with Virtual Agent Support",
      "continueHuman": "Continue with Human Agent Support",
      "vaOverCapacity": "Our customer support is experiencing exceptionally high volume. The estimated wait time is {0} minutes.",
      "vaAfterHours": "Our support center is closed. Please select the support type you want to continue.",
      "pfOverCapacity": "I'm sorry. I'm having trouble processing your request right now. I can transfer you to a human agent. However, the current estimated wait time is {0} minutes due to exceptionally high volume of support requests.",
      "pfAfterHours": "I'm sorry. I'm having trouble processing your request right now. Our support center is currently closed as well. Please send us an email with your support request and we will respond back to you at the earliest.",
      "recurring": "Thanks for your patience! The remaining wait time is {0}.",
      "closed": "Unfortunately, our support center is currently closed. Please try reaching us later. Thank you."
    }
    

### area
    
    
    {
      "widgetOpen": "Open Support Widget",
      "widgetClosed": "Minimize Support Widget",
    }
    

### form
    
    
    {
      "closeButton": "Close form",
      "confirmCloseTitle": "Confirm form closure",
      "confirmCloseContent1": "Are you sure you're ready to close this form? Any unsubmitted data will be lost.",
      "confirmCloseContent2": "You can minimize the form to return to the conversation without losing any data.",
      "startNewTitle": "Start new form",
      "startNewContent": "Starting a new form will close the form that is in progress, and any unsubmitted data will be lost.",
      "failedError": "Form failed to load",
      "timeoutError": "Form has timed out",
      "statusInProgress": "In Progress",
      "statusCompleted": "Completed",
      "submissionFailedTitle": "Form Submission Failed",
      "submissionFailedContent": "There was an issue submitting your form. Please try again."
    }
    

### ewt
    
    
    {
      "connecting": "We're working on connecting you with an agent.\nThanks for your patience.",
      "escalateToAgent": "You're being transferred to a live support representative...",
      "transferToAgent": "You're being transferred to another support representative...",
      "queuePosition": "Your queue position",
      "estimateWaitTime": "Estimated wait time",
      "done": "Done"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
