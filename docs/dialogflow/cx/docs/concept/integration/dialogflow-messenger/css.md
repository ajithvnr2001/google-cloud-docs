---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/css/
title: Dialogflow CX Messenger CSS customizations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:49.933261+00:00
---

# Dialogflow CX Messenger CSS customizations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/css/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Dialogflow CX Messenger CSS customizations Stay organized with collections  Save and categorize content based on your preferences. 

You can customize the style of your chat dialog by setting [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties).

**Caution:** CSS customization won't render in Internet Explorer 11, as it does not support CSS variables. Default styles will be rendered instead.

## General styling

The following CSS variables provide general styling options:

Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-font-family` | Optional | "Google Sans", "Helvetica Neue", sans-serif | Font family to use throughout the widget  
`df-messenger-font-size` | Optional | 14px | Text size to use throughout the widget  
`df-messenger-font-color` | Optional | #1f1f1f | Text color to use throughout the widget  
`df-messenger-primary-color` | Optional | #0b57d0 | Primary color for elements throughout the widget (such as title bar background, action button background and more)  
`df-messenger-focus-color` | Optional | #1e88e5 | Color of the focus ring around elements  
`df-messenger-focus-color-contrast` | Optional | white | Color of the focus ring around elements when inside a parent with a background color (such as the title bar)  
`df-messenger-chat-border` | Optional | none | Border for the dialog  
`df-messenger-chat-border-radius` | Optional | 0 | Border radius for the dialog  
  
## Styling for `df-messenger-chat-bubble`

When using the `df-messenger-chat-bubble` element, the following CSS variables can be provided:

Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-chat-window-height` | Optional | 480px | Height of the chat window  
`df-messenger-chat-window-width` | Optional | 320px | Width of the chat window  
`df-messenger-chat-window-offset` | Optional | 16px | Distance between the chat bubble and the chat window  
`df-messenger-chat-window-box-shadow` | Optional | none | Box shadow of the chat window  
`df-messenger-chat-collapse-icon-size` | Optional | unset | Size of the collapse button icon in the title bar  
`df-messenger-chat-bubble-icon-size` | Optional | 36px | Size of the icon for the chat bubble  
`df-messenger-chat-bubble-close-icon-size` | Optional | 24px | Size of the close icon for the chat bubble  
`df-messenger-chat-bubble-close-icon-transform-rotate` | Optional | -90deg | Rotation of the close icon for the chat bubble, rotates to 0deg on closing the chat  
`df-messenger-chat-bubble-icon-color` | Optional | white | Color of the icon and close icon for the chat bubble  
`df-messenger-chat-bubble-size` | Optional | 64px | Size of the chat bubble  
`df-messenger-chat-bubble-background` | Optional | #0b57d0 | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the chat bubble  
`df-messenger-chat-bubble-border-radius` | Optional | 32px | Border radius of the chat bubble  
`df-messenger-chat-bubble-border` | Optional | none | Border of the chat bubble  
`df-messenger-chat-border-minimized` | Optional | none | Border of the chat in minimized form  
`df-messenger-chat-border-radius-minimized` | Optional | 0 | Border radius of the chat in minimized form  
  
## Styling for titlebar

For the titlebar, the following CSS variables can be provided:

Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-titlebar-background` | Optional | #0b57d0 | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the title bar  
`df-messenger-titlebar-padding` | Optional | 0 15px | Padding of the title bar  
`df-messenger-titlebar-border` | Optional | none | Border for the title bar  
`df-messenger-titlebar-border-bottom` | Optional | none | Border bottom of the title bar  
`df-messenger-titlebar-title-align` | Optional | start | Text alignment of the title text(s) in the title bar, allowed values are `start`, `center` or `end`  
`df-messenger-titlebar-font-color` | Optional | white | Text color of the text in the title bar  
`df-messenger-titlebar-letter-spacing` | Optional | normal | Letter spacing of the text in the title bar  
`df-messenger-titlebar-title-font-size` | Optional | 18px | Text size of the title text in the title bar  
`df-messenger-titlebar-title-font-family` | Optional | "Google Sans", "Helvetica Neue", sans-serif | Font family of the title text in the title bar  
`df-messenger-titlebar-title-font-weight` | Optional | 400 | Font weight of the title text in the title bar  
`df-messenger-titlebar-title-line-height` | Optional | normal | Line height of the title text in the title bar  
`df-messenger-titlebar-title-letter-spacing` | Optional | normal | Letter spacing of the title text in the title bar  
`df-messenger-titlebar-subtitle-font-color` | Optional | white | Text color of the subtitle text in the title bar  
`df-messenger-titlebar-subtitle-font-size` | Optional | 18px | Text size of the subtitle text in the title bar  
`df-messenger-titlebar-subtitle-font-family` | Optional | "Google Sans", "Helvetica Neue", sans-serif | Font family of the subtitle text in the title bar  
`df-messenger-titlebar-subtitle-font-weight` | Optional | 400 | Font weight of the subtitle text in the title bar  
`df-messenger-titlebar-subtitle-line-height` | Optional | normal | Line height of the subtitle text in the title bar  
`df-messenger-titlebar-subtitle-letter-spacing` | Optional | normal | Letter spacing of the subtitle text in the title bar  
`df-messenger-titlebar-title-order` | Optional | row | Order elements in the title bar, allowed values are `row` or `row-reverse`. This value is only effective if the `chat-title-icon` attribute has been specified.  
`df-messenger-titlebar-icon-width` | Optional | 18px | The width of the icon in the title bar. This value is only applied if the `chat-title-icon` has been specified.  
`df-messenger-titlebar-icon-height` | Optional | 18px | The height of the icon in the title bar. This value is only applied if the `chat-title-icon` has been specified.  
`df-messenger-titlebar-icon-padding` | Optional | 0 12px 0 0 | The padding around the icon in the title bar. This value is only applied if the `chat-title-icon` has been specified.  
  
## Styling for chat window

For the chat window, the following CSS variables can be provided:

Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-chat-background` | Optional | #fafafa | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the agent dialog where messages are shown  
`df-messenger-chat-padding` | Optional | 10px | Padding of the agent dialog where messages are shown  
`df-messenger-messagelist-border` | Optional | none | Border of the message list  
`df-messenger-message-border` | Optional | none | Border of the agent dialog messages  
`df-messenger-message-font-size` | Optional | 14px | Text size of the agent dialog messages  
`df-messenger-message-font-family` | Optional | "Google Sans", "Helvetica Neue", sans-serif | Font family of the agent dialog messages  
`df-messenger-message-font-weight` | Optional | normal | Font weight of the agent dialog messages  
`df-messenger-message-bot-background` | Optional | #ecf3fe | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the messages sent by the agent  
`df-messenger-message-bot-border` | Optional | none | Border of the messages sent by the agent  
`df-messenger-message-bot-font-color` | Optional | #1f1f1f | Text color of the messages sent by the agent  
`df-messenger-message-bot-font-weight` | Optional | normal | Font weight of the messages sent by the agent  
`df-messenger-message-user-background` | Optional | #e1e3e1 | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the messages sent by the user  
`df-messenger-message-user-border` | Optional | none | Border of the messages sent by the user  
`df-messenger-message-user-font-color` | Optional | #1f1f1f | Text color of the messages sent by the user  
`df-messenger-message-user-font-weight` | Optional | normal | Font weight of the messages sent by the user  
`df-messenger-message-spacing` | Optional | 10px | Space between two messages  
`df-messenger-message-border-radius` | Optional | 8px | Border radius for messages, applies to all corners  
`df-messenger-message-bot-border-top-left-radius` | Optional | 8px | Border radius top left for agent messages, overrides generic radius  
`df-messenger-message-bot-border-top-right-radius` | Optional | 8px | Border radius top right for agent messages, overrides generic radius  
`df-messenger-message-bot-border-bottom-left-radius` | Optional | 8px | Border radius bottom left for agent messages, overrides generic radius  
`df-messenger-message-bot-border-bottom-right-radius` | Optional | 8px | Border radius bottom right for agent messages, overrides generic radius  
`df-messenger-message-user-border-top-left-radius` | Optional | 8px | Border radius top left for user messages, overrides generic radius  
`df-messenger-message-user-border-top-right-radius` | Optional | 8px | Border radius top right for user messages, overrides generic radius  
`df-messenger-message-user-border-bottom-left-radius` | Optional | 8px | Border radius bottom left for user messages, overrides generic radius  
`df-messenger-message-user-border-bottom-right-radius` | Optional | 8px | Border radius bottom right for user messages, overrides generic radius  
`df-messenger-message-stack-spacing` | Optional | 10px | Space between two consecutive messages  
`df-messenger-message-bot-stack-border-top-left-radius` | Optional | 8px | Border radius top left for consecutive agent messages, overrides agent top left radius  
`df-messenger-message-bot-stack-border-top-right-radius` | Optional | 8px | Border radius top right for consecutive agent messages, overrides agent top right radius  
`df-messenger-message-bot-stack-border-bottom-left-radius` | Optional | 8px | Border radius bottom left for consecutive agent messages, overrides agent bottom left radius  
`df-messenger-message-bot-stack-border-bottom-right-radius` | Optional | 8px | Border radius bottom right for consecutive agent messages, overrides agent bottom right radius  
`df-messenger-message-user-stack-border-top-left-radius` | Optional | 8px | Border radius top left for consecutive user messages, overrides user top left radius  
`df-messenger-message-user-stack-border-top-right-radius` | Optional | 8px | Border radius top right for consecutive user messages, overrides user top right radius  
`df-messenger-message-user-stack-border-bottom-left-radius` | Optional | 8px | Border radius bottom left for consecutive user messages, overrides user bottom left radius  
`df-messenger-message-user-stack-border-bottom-right-radius` | Optional | 8px | Border radius bottom right for consecutive user messages, overrides user bottom right radius  
`df-messenger-message-user-writing-image-width` | Optional | 24px | Width of the image shown while the agent is writing, only active if `bot-writing-image` is set  
`df-messenger-message-bot-writing-image-height` | Optional | 24px | Height of the image shown while the agent is writing, only active if `bot-writing-image` is set  
`df-messenger-message-bot-writing-font-color` | Optional | #1f1f1f | Text color of the text shown while the agent is writing  
`df-messenger-message-bot-writing-font-weight` | Optional | normal | Font weight of the text shown while the agent is writing  
`df-messenger-message-bot-writing-font-size` | Optional | 14px | Text size of the text shown while the agent is writing  
`df-messenger-message-bot-writing-border` | Optional | none | Border of the message shown while the agent is writing  
`df-messenger-message-bot-writing-background` | Optional | #ecf3fe | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the message shown while the agent is writing  
`df-messenger-message-bot-writing-padding` | Optional | 12px | Padding of the message shown while the agent is writing  
`df-messenger-message-bot-writing-spacing` | Optional | 10px | Space between the message shown while the agent is writing and the previous message  
`df-messenger-chat-scroll-button-enabled-display` | Optional | none | Defines the display of the "Jump to Bottom" button, set to `flex` to enable the button  
`df-messenger-chat-scroll-button-align` | Optional | center | Alignment of the "Jump to Bottom" button, allowed values include `flex-start`, `center`, `flex-end`  
`df-messenger-chat-scroll-button-container-padding` | Optional | 8px | Padding of the container around the "Jump to Bottom" button  
`df-messenger-chat-scroll-button-text-display` | Optional | inline | Display of the text next to the icon in the "Jump to Bottom" button, use `none` to hide the text  
`df-messenger-chat-scroll-button-font-size` | Optional | 14px | Text size of the "Jump to Bottom" button  
`df-messenger-chat-scroll-button-font-color` | Optional | white | Text color of the "Jump to Bottom" button  
`df-messenger-chat-scroll-button-background` | Optional | #0b57d0 | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the "Jump to Bottom" button  
`df-messenger-chat-scroll-button-border-radius` | Optional | 999px | Border radius of the "Jump to Bottom" button  
`df-messenger-chat-messagelist-scroll-shadow-background` | Optional | radial-gradient(farthest-side at 50% 100%, `rgba(0,0,0,.2)`, transparent) bottom | Shadow that is shown on the bottom of the message list when the list is not scrolled to the bottom, set to `none` to disable  
  
## Styling for actor images

Actor images are the images shown alongside messages of either the bot or the actor. For those actor images, the following CSS variables can be provided:

**Note:** The flags require the `bot-actor-image` or `user-actor-image` attributes to be active respectively.Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-message-actor-spacing` | Optional | 16px | Distance between the actor image and the messages  
`df-messenger-message-bot-actor-order` | Optional | row | Order of actor image and messages. Use `row` to have the actor image on the left and messages on the right, or `row-reverse` to have the actor image on the right and messages on the left.  
`df-messenger-message-user-actor-order` | Optional | row-reverse | Order of actor image and messages. Use `row-reverse` to have the actor image on the right and messages on the left, or `row` to have the actor image on the left and messages on the right.  
`df-messenger-message-actor-direction` | Optional | column | Should be the opposite of `df-messenger-message-bot-actor-order` and `df-messenger-message-user-actor-order`, use `column` when these are `row` based, or `row` when they are `column` based.  
`df-messenger-message-actor-align` | Optional | flex-start | Alignment of the actor in relation to the messages. Use `flex-start` to have the actor image on top, `center` to have the actor image centered, or `flex-end` to have the actor image on the bottom.  
`df-messenger-message-actor-border-radius` | Optional | 999px | Border radius of the actor image  
`df-messenger-message-actor-padding` | Optional | 8px | Padding of the actor image  
`df-messenger-message-actor-image-size` | Optional | 24px | Size of the actor image image  
`df-messenger-message-bot-actor-background` | Optional | white | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the agent's actor image  
`df-messenger-message-bot-actor-border` | Optional | none | Border of the agent's actor image  
`df-messenger-message-bot-actor-offset` | Optional | 0 | Offset to move the agent's actor image  
`df-messenger-message-user-actor-background` | Optional | white | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the user's actor image  
`df-messenger-message-user-actor-border` | Optional | none | Border of the user's actor image  
`df-messenger-message-user-actor-offset` | Optional | 0 | Offset to move the user's actor image  
  
## Styling for user input

For the user input, the following CSS variables can be provided:

Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-send-icon-color` | Optional | #0b57d0 | Color of the "send" icon in the user input  
`df-messenger-send-icon-color-hover` | Optional | #0b57d0 | Color of the "send" icon in the user input when hovered  
`df-messenger-send-icon-color-active` | Optional | #0b57d0 | Color of the "send" icon in the user input when text can be sent  
`df-messenger-send-icon-offset-x` | Optional | 0 | Vertical offset of the "send" icon in the user input  
`df-messenger-send-icon-offset-y` | Optional | -4px | Horizontal offset of the "send" icon in the user input  
`df-messenger-input-background` | Optional | white | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the user input  
`df-messenger-input-padding` | Optional | 8px | Overall padding between the user input field (including send message button) and the container.  
`df-messenger-input-inner-padding` | Optional | 0px 48px 0px 0 | Inner padding between the user input field (not including send message button) and the container.  
`df-messenger-input-border` | Optional | none | Border of the user input  
`df-messenger-input-border-top` | Optional | 1px solid #e0e0e0 | Top border of the user input  
`df-messenger-input-border-bottom` | Optional | none | Border bottom of the text field of the user input  
`df-messenger-input-font-family` | Optional | "Google Sans", "Helvetica Neue", sans-serif | Font family of the user input  
`df-messenger-input-font-color` | Optional | #1f1f1f | Text color of the user input  
`df-messenger-input-font-size` | Optional | 14px | Text size of the user input  
`df-messenger-input-font-weight` | Optional | normal | Font weight of the user input  
`df-messenger-input-box-border` | Optional | none | Border of the user input box  
`df-messenger-input-box-focus-border` | Optional | none | Border of the user input box while focused  
`df-messenger-input-box-border-radius` | Optional | 0 | Border radius of the user input box  
`df-messenger-input-box-padding` | Optional | 12px 0 | Padding of the user input box  
`df-messenger-input-box-focus-padding` | Optional | 12px 0 | Padding of the user input box while focused  
`df-messenger-input-gutter` | Optional | stable | [Scrollbar gutter](https://developer.mozilla.org/en-US/docs/Web/CSS/scrollbar-gutter) of the user input  
`df-messenger-input-info-font-size` | Optional | 14px | Text size of informational messages in the user input  
`df-messenger-input-info-font-weight` | Optional | normal | Font weight of informational messages in the user input  
`df-messenger-input-info-padding` | Optional | 14px 16px | Padding of informational messages in the user input  
`df-messenger-input-info-line-height` | Optional | 20px | Line height of informational messages in the user input  
`df-messenger-input-long-text-warning-display` | Optional | none | If set to `block`, will show a warning message once the input exceeds 256 characters. Only active if the [`max-query-length` attribute](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/html) is higher (e.g. disabled). [Additional documentation](https://docs.cloud.google.com/dialogflow/quotas#length_limits).  
`df-messenger-input-warning-background` | Optional | #fef7e0 | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the warning message in the user input  
`df-messenger-input-warning-color` | Optional | #410e0b | Text color of the warning message in the user input  
`df-messenger-input-warning-icon-color` | Optional | #e37400 | Color of the icon in the warning message in the user input  
`df-messenger-input-error-background` | Optional | #f9dedc | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the error message in the user input  
`df-messenger-input-error-color` | Optional | #410e0b | Text color of the error message in the user input  
`df-messenger-input-error-icon-color` | Optional | #b3261e | Color of the icon in the warning message in the user input  
  
## Styling for authentication overlay

When using an authenticated setup, the following CSS variables can be provided for the overlay:

Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-auth-background` | Optional | rgba(204, 204, 204, .8) | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the agent dialog when authentication is shown  
`df-messenger-auth-button-background` | Optional | #0b57d0 | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the authentication button  
`df-messenger-auth-button-font-family` | Optional | "Google Sans", "Helvetica Neue", sans-serif | Font family of the authentication button  
`df-messenger-auth-button-font-color` | Optional | white | Text color of the authentication button  
`df-messenger-auth-button-font-size` | Optional | 14px | Text size of the authentication button  
`df-messenger-auth-button-border` | Optional | none | Border of the authentication button  
`df-messenger-auth-button-border-radius` | Optional | 8px | Border radius of the authentication button  
  
## Feedback styling

When the [answer feedback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger#answer-feedback) feature is enabled, the following CSS variables can be provided for the feedback controls.

Properties | Input policy | Default value | Description  
---|---|---|---  
`df-messenger-message-feedback-icon-distance` | Optional | 8px | Distance between the thumbs up and down buttons  
`df-messenger-message-feedback-icon-font-color` | Optional | #444746 | Color of the thumbs up and down buttons  
`df-messenger-message-feedback-icon-font-color-active` | Optional | #444746 | Color of the thumbs up and down buttons when active  
`df-messenger-message-feedback-icon-border` | Optional | none | Border of the thumbs up and down buttons  
`df-messenger-message-feedback-icon-border-radius` | Optional | 0 | Border radius of the thumbs up and down buttons  
`df-messenger-message-feedback-icon-background` | Optional | none | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the thumbs up and down buttons  
`df-messenger-message-feedback-icon-background-hover` | Optional | none | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the thumbs up and down buttons when hovered  
`df-messenger-message-feedback-icon-padding` | Optional | 0 | Padding of the thumbs up and down buttons  
`df-messenger-message-rich-feedback-spacing` | Optional | 10px | Spacing of elements in the rich feedback  
`df-messenger-message-rich-feedback-padding` | Optional | 0 | Padding of the rich feedback  
`df-messenger-message-rich-feedback-background` | Optional | none | [Background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) of the rich feedback  
`df-messenger-message-rich-feedback-border-radius` | Optional | 0 | Border radius of the rich feedback  
`df-messenger-message-rich-feedback-border` | Optional | none | Border of the rich feedback  
`df-messenger-rich-feedback-offset-left` | Optional | 0 | Offset on the left side  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
