---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-guide/
title: Chat platform API integration guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:05:49.890821+00:00
---

# Chat platform API integration guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat platform API integration guide Stay organized with collections  Save and categorize content based on your preferences. 

Use this guide to build a server-side chat integration with the Apps API. By the end, your integration will be able to:

  * Authenticate to the Apps API.

  * Create or update an end user.

  * Start a chat for that end user.

  * Receive and verify webhook events from Contact Center AI Platform.

  * Send text messages into the chat.

  * Handle optional branches such as pre-chat transcript import, queue-selection virtual-agent routing, escalation deflections, and media attachments.

  * End the chat when the conversation is complete.




This guide is for developers who are building a backend service that connects a customer-owned chat experience to CCAI Platform. It assumes you can create API credentials in CCAI Platform, host an HTTPS webhook endpoint, store secrets securely, and make HTTP requests from your server.

This guide supplements the [Apps API Chat endpoints](https://externals.ujet.co/apidocs/apps/publication.html#Chats). Use the API reference for the exhaustive request and response schema, and use this guide for the recommended end-to-end implementation flow.

## Terminology

The following definitions apply to this document:

  * **Customer** : The CCAI Platform customer that is implementing the chat integration in their own software.

  * **Consumer** : The customer-owned server-side application that makes requests to the Apps API and receives CCAI Platform webhook events.

  * **End user** : The person using the customer's software to start or continue a chat with an agent or virtual agent.

  * **Chat** : The CCAI Platform conversation resource that the Apps API creates.

  * **Webhook endpoint** : The HTTPS endpoint in the consumer application that receives chat events from CCAI Platform.




## Before you begin

Before you begin, make sure you have the following:

  * Apps API credentials

    * Create API credentials in CCAI Platform from **Settings** > **Developer Settings** > **API Credentials**.

    * Store the credential secret securely. Don't expose it in browser or mobile-client code.

  * Tenant URL details

    * Identify your CCAI Platform subdomain and domain.

    * The Apps API base URL is: `https://YOUR_SUBDOMAIN.YOUR_DOMAIN/apps/api/v1`

  * Webhook endpoint

    * Host a public HTTPS endpoint that can receive POST requests from CCAI Platform.

    * Configure the endpoint in CCAI Platform developer settings.

    * Generate and store the webhook primary and secondary secrets.

  * Queue or menu configuration

    * Identify the queue or menu that new chats enter.

    * If you use a queue-selection virtual agent, configure that virtual agent and assign it to the entry queue before creating chats through the API.

  * End-user identity

    * Decide which stable identifier your system will use for each end user.

    * Store the CCAI Platform end-user ID returned by the Apps API.

  * Rate-limit handling

    * CCAI Platform rate-limits the Apps API. Build retries and backoff into your integration, and avoid sending bursts of requests for a single tenant.



## Authentication and webhook security

Your integration uses two authentication paths:

  * Apps API authentication for requests from your server to CCAI Platform.

  * Webhook signature verification for requests from CCAI Platform to your server.




### Authenticate Apps API requests

Requests use HTTP basic authentication. Create an API token in CCAI Platform under **Settings** > **Developer Settings** > **API Credentials** , and pass it in the **password** field (recommended). If your tenant uses the legacy authentication path, you can instead pass your company key as the username and your company secret as the password. See the [Apps API reference](https://externals.ujet.co/apidocs/apps/publication.html#Chats) for the full authentication setup. The following example demonstrates how to authenticate an Apps API request using basic authentication:
    
    
    curl -X GET \
      https://YOUR_SUBDOMAIN.YOUR_DOMAIN/apps/api/v1/chats/{chat_id} \
      -u "YOUR_SUBDOMAIN:YOUR_API_TOKEN" \
      -H "Accept: application/json"
    

Store credentials in a server-side secret store, rotate them according to your security policy, and never ship them in browser or mobile apps.

### Verify webhook requests

CCAI Platform sends chat events to your webhook endpoint. Each webhook request includes:

  * `X-Signature`

  * `X-Signature-Timestamp`




The `X-Signature` header can contain a primary signature, a secondary signature, or both:
    
    
    primary=<primary_signature> secondary=<secondary_signature>
    

Each signature is a Base64-encoded HMAC-SHA256 digest. The signed value is the timestamp header concatenated with the raw JSON request body:
    
    
    X-Signature-Timestamp + raw_request_body
    

In your webhook handler:

  1. Read `X-Signature` and `X-Signature-Timestamp`.

  2. Reject the request if either header is missing.

  3. Reject stale timestamps to reduce replay risk.

  4. Read the raw request body before parsing JSON.

  5. Compute the expected signature using each active webhook secret.

  6. Compare the received signature and expected signature using a constant-time comparison.

  7. Accept the request if any active secret matches.




The following example Ruby implementation demonstrates how to verify UJET webhook signatures:
    
    
    require "base64"
    require "openssl"
    require "active_support/security_utils"
    
    def parse_ujet_signature(header)
      header.to_s.split(/\s+/).each_with_object({}) do |part, result|
        key, value = part.split("=", 2)
        result[key] = value if key && value
      end
    end
    
    def expected_signature(secret, timestamp, raw_body)
      Base64.strict_encode64(
        OpenSSL::HMAC.digest(
          OpenSSL::Digest.new("sha256"),
          secret,
          "#{timestamp}#{raw_body}"
        )
      )
    end
    
    def secure_match?(received, expected)
      return false if received.nil? || expected.nil?
      return false unless received.bytesize == expected.bytesize
    
      ActiveSupport::SecurityUtils.secure_compare(received, expected)
    end
    
    def verify_ujet_webhook!(request, primary_secret:, secondary_secret:)
      signature_header = request.headers["X-Signature"]
      timestamp = request.headers["X-Signature-Timestamp"]
    
      return false if signature_header.nil? || timestamp.nil?
    
      # Optional but recommended: reject stale requests.
      return false if (Time.now.utc - Time.at(timestamp.to_i).utc).abs > 5.minutes
    
      raw_body = request.body.read
      signatures = parse_ujet_signature(signature_header)
    
      expected = [
        expected_signature(primary_secret, timestamp, raw_body),
        expected_signature(secondary_secret, timestamp, raw_body)
      ].compact
    
      received = [
        signatures["primary"],
        signatures["secondary"]
      ].compact
    
      received.any? do |received_signature|
        expected.any? do |expected_signature_value|
          secure_match?(received_signature, expected_signature_value)
        end
      end
    end
    

If verification succeeds, return a success response quickly and process the event idempotently. Webhook delivery and API responses can arrive in different orders, so build your integration to tolerate receiving the same state change more than once without creating duplicate records.

## The integration flow

The following flow creates an end user, starts a chat, receives CCAI Platform events, exchanges messages, and ends the chat.

### Create or update the end user

**Goal:** Ensure CCAI Platform has an end-user record before you create the chat.

**Endpoint**

Use the following endpoint to create or update an end user:
    
    
    POST /apps/api/v1/end_users
    

**Example request**

The following example demonstrates a request body for creating or updating an end user:
    
    
    {
      "identifier": "customer-user-12345",
      "email": "customer.user@example.com",
      "name": "Customer User",
      "phone": "+15551234567"
    }
    

**What to store**

Store the CCAI Platform end-user ID from the response in your system. Use that ID when you create a chat.

**What to expect**

  * If the end user doesn't exist, CCAI Platform creates a new record.

  * If an end user already exists with the same identifier, CCAI Platform updates the record and returns the existing end user's information.




### Create the chat

**Goal:** Start a new CCAI Platform chat for the end user.

**Endpoint**

Use the following endpoint to start a new chat:
    
    
    POST /apps/api/v1/chats
    

**Example request**

The following example demonstrates a request body for creating a chat:
    
    
    {
      "chat": {
        "menu_id": 123,
        "end_user_id": 456,
        "lang": "en"
      }
    }
    

**Optional context for virtual-agent routing**

If your queue-selection virtual agent needs context from your application, include a context payload when you create the chat, as shown in the following example:
    
    
    {
      "chat": {
        "menu_id": 123,
        "end_user_id": 456,
        "lang": "en",
        "context": {
          "value": {
            "customer_tier": "gold",
            "issue_type": "billing"
          }
        }
      }
    }
    

A virtual agent can use values from that context to decide which queue receives the chat.

**What to expect**

  * The Apps API returns the chat resource.

  * CCAI Platform sends a `chat_created` webhook event to your configured webhook endpoint.

  * The API response and webhook event can arrive in either order. Treat both as updates to the same chat record, keyed by chat ID.




### Process chat webhook events

**Goal:** Keep the consumer application synchronized with CCAI Platform chat state.

Your webhook endpoint handles chat lifecycle and message events from CCAI Platform. At minimum, store:

  * Chat ID.

  * Event type.

  * Event timestamp.

  * Message sender, message type, and message content when the event contains a message.

  * Any escalation or deflection data when the event describes routing behavior.




**Recommended behavior**

  * Verify every webhook signature before processing the event.

  * Store processed event IDs or a deterministic event key so retries don't create duplicates.

  * Return a 2xx response after accepting the event.

  * Process downstream side effects asynchronously when possible.




**What to expect**

Your application updates its chat state when CCAI Platform sends events such as chat creation, incoming messages, agent messages, escalation changes, and chat completion.

### Send a text message

**Goal:** Send an end-user message from the consumer application into the CCAI Platform chat.

**Endpoint**

Use the following endpoint to send a text message into the chat:
    
    
    POST /apps/api/v1/chats/{chat_id}/message
    

**Example request**

The following example demonstrates a request body for sending a text message:
    
    
    {
      "from_user_id": 456,
      "message": {
        "type": "text",
        "content": "Hello, I need help with my order."
      }
    }
    

**What to expect**

  * CCAI Platform accepts the message.

  * The message appears in the agent or virtual-agent conversation.

  * Your webhook endpoint receives a message event for the message, including messages that your own application sent through the Apps API.




### Receive and display messages from CCAI Platform

**Goal:** Show agent or virtual-agent messages in the customer-owned chat experience.

When your webhook endpoint receives a message event:

  1. Verify the webhook signature.

  2. Check whether the event is new.

  3. Identify the chat by chat ID.

  4. Identify the sender and message type.

  5. Render the message in the customer-owned chat UI.

  6. Persist the event so refreshes or retries don't lose conversation history.




**What to expect**

The customer-owned chat UI shows messages sent by agents, virtual agents, and the end user in the correct order. If events arrive out of order, use event timestamps and your own persistence layer to reconcile display order.

### Escalate from a virtual agent to a human agent

**Goal:** Move the chat from virtual-agent handling to a human queue when the end user needs agent help.

If your integration uses a queue-selection virtual agent, configure the virtual agent to route chats to the target queue. If your server initiates escalation directly, use the Apps API escalation endpoint.

**Endpoint**

Use the following endpoint to escalate a chat from a virtual agent to a human agent:
    
    
    POST /apps/api/v1/chats/{chat_id}/escalations
    

**Example request**

The following example demonstrates a request body for escalating a chat:
    
    
    {
      "reason": "by_end_user_ask",
      "force_escalate": false
    }
    

**What to expect**

  * If the target queue is available, the chat moves toward agent handling.

  * If the queue is unavailable because of after-hours or over-capacity conditions, CCAI Platform can return or send deflection options through the chat flow.

  * Your integration renders the available deflection options to the end user.




### Record an escalation-deflection choice

**Goal:** Tell CCAI Platform which deflection option the end user selected.

When CCAI Platform offers escalation-deflection options, record the end user's choice with the escalation update endpoint.

**Endpoint**

Use the following endpoint to update an escalation record with a deflection choice:
    
    
    PATCH /apps/api/v1/chats/{chat_id}/escalations/{escalation_id}
    

**Supported`deflection_channel` values:**

  * `email` — the end user chooses the email deflection option.

  * `virtual_agent` — the end user chooses to continue with a virtual agent.

  * `human_agent` — the end user chooses to keep waiting for a human agent. This value applies only to over-capacity deflections.




**Example request**

The following example demonstrates a request body for recording a deflection choice:
    
    
    {
      "deflection_channel": "email"
    }
    

Send only a supported `deflection_channel` value to this endpoint. `external_link` isn't a valid value for the escalation update endpoint; when the end user follows an external deflection link, the chat ends instead.

**What to expect**

CCAI Platform updates the escalation record and transitions the chat according to the selected option.

### End the chat

**Goal:** Close the chat when the conversation is complete.

**Endpoint**

Use the following endpoint to end an active chat:
    
    
    PATCH /apps/api/v1/chats/{chat_id}/end
    

**Example request**

The following example demonstrates a request body for ending a chat:
    
    
    {
      "ended_by_user_id": 456
    }
    

**What to expect**

  * CCAI Platform ends the chat.

  * Your webhook endpoint receives the final chat-state event.

  * Your application marks the chat as complete and stops accepting new end-user messages for that chat.




## Advanced flows

The following branches are optional. Implement only the flows that apply to your integration.

### Import a pre-chat transcript

Use this flow when the end user already had a conversation in your system before you created the CCAI Platform chat, such as a chatbot conversation.

Add the transcript payload when you create the chat. The transcript gives the agent context so the end user doesn't have to repeat information.

The Apps API reference includes the exact transcript schema.

### Route chats with a queue-selection virtual agent

Use this flow when your application sends all new chats into an entry queue and lets a virtual agent decide the final target queue.

  1. Create a virtual agent for queue selection.

  2. Assign the virtual agent to the entry queue.

  3. Include context when you create the chat.

  4. Configure the virtual agent to inspect the context and escalate the chat to the correct queue.

  5. Handle deflection options if the target queue is unavailable.




### Send photo or video attachments

Use this flow when the end user sends media from the customer-owned chat UI.

The media flow has four stages.

**Stage 1 — Request a presigned upload URL**

Use the following endpoints to request a presigned URL for uploading a photo or video:
    
    
    POST /apps/api/v1/chats/{chat_id}/photos/upload
    POST /apps/api/v1/chats/{chat_id}/videos/upload
    

**Stage 2 — Upload the file to the returned storage URL**

Include the file and any fields that CCAI Platform returns in the presigned-upload response.

**Stage 3 — Add the uploaded file to the chat**

Use the following endpoints to add an uploaded photo or video to the chat:
    
    
    POST /apps/api/v1/chats/{chat_id}/photos
    POST /apps/api/v1/chats/{chat_id}/videos
    

Store the `media_id` that CCAI Platform returns. Chat message payloads refer to media by media ID.

**Stage 4 — Send the media as a message**

Use the following endpoint to send a media message into the chat:
    
    
    POST /apps/api/v1/chats/{chat_id}/message
    

**Example request**

The following example demonstrates a request body for sending a photo attachment:
    
    
    {
      "from_user_id": 456,
      "message": {
        "type": "photo",
        "content": {
          "media_id": 789
        }
      }
    }
    

Use the `video` message type and the video `media_id` for video messages.

### Send custom data during a chat

Use the following endpoint when your integration needs to attach customer-defined context to an active chat:
    
    
    POST /apps/api/v1/chats/{chat_id}/custom_data
    

The Apps API reference defines the exact payload shape and reserved-key behavior.

### Update end-user identity during a chat

Use the following endpoint when the end user's identity changes or becomes known after the chat starts:
    
    
    POST /apps/api/v1/chats/{chat_id}/end_user
    

For example, use this endpoint when an anonymous end user signs in during an active chat and your integration needs CCAI Platform to associate the chat with the updated end-user identity.

### Collect CSAT or rating data

Use the following chat CSAT and rating endpoints when your integration owns the post-chat rating experience:
    
    
    GET /apps/api/v1/chats/{chat_id}/csat
    GET /apps/api/v1/chats/{chat_id}/rating
    PATCH /apps/api/v1/chats/{chat_id}/rating
    

For the exact eligibility rules and rating payloads, see the Apps API reference.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
