---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-events/
title: Headless web SDK events \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:51:32.836993+00:00
---

# Headless web SDK events  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless web SDK events Stay organized with collections  Save and categorize content based on your preferences. 

The headless web SDK provides events that you can listen to in order to handle specific actions or updates within your application. You can add and remove event listeners using the `.on` and `.off` methods.
    
    
    const handleReady = () => {
      console.log("**** client is ready")
    }
    
    client.on("ready", handleReady)
    
    // client.off("ready", handleReady)
    

## General events

The following are general events for the SDK

### `ready`

Emitted when the client is ready for communication.
    
    
    client.on("ready", () => {
    })
    

### `authenticated`

Emitted when the client has authenticated with the user's token.
    
    
    client.on("authenticated", () => {
    })
    

## Chat events

The following are chat session specific events.

### `chat.ongoing`

Emitted when there is an ongoing chat.
    
    
    client.on("chat.ongoing", (chat) => {
      console.log(chat)
    })
    

### `chat.updated`

Emitted when the chat instance has updated.
    
    
    client.on("chat.updated", (chat) => {
      // the `chat` property on `client` has updated
      console.log(chat)
    })
    

### `chat.message`

Emitted when there is a new message.
    
    
    client.on("chat.message", message => {
      console.log(message)
    })
    

The message type:
    
    
    interface MessageResponse {
      $index: number;
      $sid: string;
      $timestamp: Date;
      $userType: string;
      $userId: number;
      type: string;
      content?: string;
      event?: string;
      file?: File;
    
      // extra parameters
      [key: string]: unknown;
    }
    

### `chat.memberJoined`

Emitted when a new member joins the conversation.
    
    
    client.on("chat.memberJoined", (identity) => {
      console.log(identity)
    })
    

### `chat.memberLeft`

Emitted when a member leaves the conversation.
    
    
    client.on("chat.memberLeft", (identity) => {
      console.log(identity)
    })
    

### `chat.connected`

Emitted when the chat is connected with the conversation provider.
    
    
    client.on("chat.connected", () => {
      console.log("connected")
    })
    

In rare cases there might be latency issues that cause a message to be sent in a chat before the SDK joins the chat. When this occurs you can use `fetchMessages` to get all existing messages in a conversation after a chat has connected. See the following code sample:
    
    
    client.on("chat.connected", async () = {
      const messages = await
    client.fetchMessages()
    })
    

### `chat.disconnected`

Emitted when the chat is disconnected from the conversation provider.
    
    
    client.on("chat.disconnected", () => {
      console.log("disconnected")
    })
    

### `chat.dismissed`

Emitted when the chat's status is changed to `dismissed`.
    
    
    client.on("chat.dismissed", () => {
      console.log("dismissed")
    })
    

### `chat.timeout`

Emitted when the chat is ended, with the reason being `timeout`.
    
    
    client.on("chat.timeout", () => {
      console.log("timeout")
    })
    

### `chat.ended`

Emitted when the chat is ended.
    
    
    client.on("chat.ended", () => {
      console.log("ended")
    })
    

### `chat.destroyed`

Emitted when `destroyChat` is called.
    
    
    client.on("chat.destroyed", () => {
      console.log("destroyed")
    })
    

### `chat.checkInRequested`

Emitted when chat can be checked in.

### `chat.checkInTimedOut`

Emitted when chat check in has timed out.

## Typing events

When an agent starts typing, the chat adapter sends a signal that results in the `typingStarted` event being sent to the headless web SDK. When the agent stops typing, a signal is sent after three seconds that results in a `typingEnded` event being sent to the headless web SDK. The three-second timeout isn't configurable.

**Note:** The 3 second timeout is not configurable.

### `chat.typingStarted`

Emitted when a member starts typing.
    
    
    client.on("chat.typingStarted", (identity) => {
      console.log(identity)
    })
    

### `chat.typingEnded`

Emitted when a member stops typing.
    
    
    client.on("chat.typingEnded", (identity) => {
      console.log(identity)
    })
    

## Chat check-in events

Chat check-in asks an end-user to confirm that they're ready before connecting to an agent. This section documents the headless web SDK methods for implementing chat check-in. For more information, see [Chat check-in](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-check-in).

### `checkIn`

Sends a confirmation signal to the server indicating the end-user is present and ready to connect with an agent during the check-in window. Updates the chat's `check_in_status` locally after the server acknowledges. Use this in response to the `chat.checkInRequested` event.

**Method signature**

`checkIn(): Promise<CheckInResponse>`

**Return value**

Returns a `CheckInResponse` object.

**Interfaces**
    
    
    interface CheckInResponse {
      chat_id: number;
      check_in_status: CheckInStatus;
      check_in_at?: string;
    }
    enum CheckInStatus {
      CONFIRMED = 'confirmed',
      EXITED = 'exited',
      PENDING = 'pending',
      REQUESTED = 'requested',
      SKIPPED = 'skipped',
      TIMED_OUT = 'timed_out',
    }
    

**Example**
    
    
    try {
      const response = await client.checkIn()
    } catch (error) {
      // handle error
    }
    

### `exitCheckIn`

Removes the user from the check-in queue.

**Method signature**

`exitCheckIn(): Promise<CheckInResponse>`

**Return value**

Returns a `CheckInResponse` object.

**Interfaces**
    
    
    interface CheckInResponse {
      chat_id: number;
      check_in_status: CheckInStatus;
      check_in_at?: string;
    }
    enum CheckInStatus {
      CONFIRMED = 'confirmed',
      EXITED = 'exited',
      PENDING = 'pending',
      REQUESTED = 'requested',
      SKIPPED = 'skipped',
      TIMED_OUT = 'timed_out',
    }
    

### `notifyCheckInState`

Notifies the backend of the check-in dialog visibility state.

**Method signature**

`notifyCheckInState(data: CheckInVisibilityStateRequest): Promise<void>`

**Interfaces**
    
    
    interface CheckInVisibilityStateRequest {
      widget_minimized?: boolean;
      tab_inactive?: boolean;
    }
    **Example**
    
    try {
      const visibilityState = {
        widget_minimized: true,
        tab_inactive: false,
      }
      await client.notifyCheckInState(visibilityState)
    } catch (error) {
      // handle error
    }
    

### `rejoinChat`

Places the user back in queue after failure to confirm check-in.

**Method signature**

`rejoinChat(): Promise<CheckInResponse>`

**Return value**

Returns a `CheckInResponse` object.

**Interfaces**
    
    
    interface CheckInResponse {
      chat_id: number;
      check_in_status: CheckInStatus;
      check_in_at?: string;
    }
    enum CheckInStatus {
      CONFIRMED = 'confirmed',
      EXITED = 'exited',
      PENDING = 'pending',
      REQUESTED = 'requested',
      SKIPPED = 'skipped',
      TIMED_OUT = 'timed_out',
    }
    

**Example**
    
    
    try {
      const response = await client.rejoinChat()
    } catch (error) {
      // handle error
    

### `trackCheckInEvent`

Signals to the backend when check-in events have been triggered by the UI. This is used when the check-in dialog has been displayed to the end-user.

**Method signature**

`trackCheckInEvent(): Promise<void>`

**Example**
    
    
    try {
      await client.trackCheckInEvent()
    } catch (error) {
      // handle error
    

## Cobrowse events

The following are events specific to Co-browse:

### `cobrowse.request`

Emitted when an end-user or agent requests to start a Co-browse session.
    
    
    client.on("cobrowse.request", { from } => {
      console.log("request by", from)
    })
    

### `cobrowse.loaded`

Emitted when a Co-browse session is loaded.
    
    
    client.on("cobrowse.loaded", session => {
      console.log("cobrowse session", session)
    })
    

### `cobrowse.updated`

Emitted when a Co-browse session is updated.
    
    
    client.on("cobrowse.updated", session => {
      console.log("cobrowse session", session)
    })
    

### `cobrowse.ended`

Emitted when a Co-browse session is ended.
    
    
    client.on("cobrowse.ended", session => {
      console.log("cobrowse session", session)
    })
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
