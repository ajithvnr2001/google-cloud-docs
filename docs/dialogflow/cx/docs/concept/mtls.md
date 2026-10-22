---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/mtls/
title: Mutual TLS authentication \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:54.376104+00:00
---

# Mutual TLS authentication  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/mtls/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Mutual TLS authentication Stay organized with collections  Save and categorize content based on your preferences. 

The network traffic initiated by Dialogflow for webhook requests is sent on a public network. To ensure that traffic is both secure and trusted in both directions, Dialogflow optionally supports [Mutual TLS authentication (mTLS)](https://en.wikipedia.org/wiki/Mutual_authentication). During Dialogflow's standard [TLS handshake](https://hpbn.co/transport-layer-security-tls/#tls-handshake), your webhook server presents a certificate that can be validated by Dialogflow, either by following the [Certificate Authority chain](https://hpbn.co/transport-layer-security-tls/#chain-of-trust-and-certificate-authorities) or by comparing the certificate to a [Custom CA certificate](https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca). By enabling mTLS on your webhook server, it will be able to authenticate the [Google certificate](https://pki.goog/roots.pem) presented by Dialogflow to your webhook server for validation, completing the establishment of mutual trust.

## Requesting mTLS

To request mTLS:

  1. Prepare your webhook HTTPS server to request the client certificate during the TLS handshake.
  2. Your webhook server should verify the client certificate upon receiving it.
  3. Install a certificate chain for your webhook server, which can be mutually trusted by both client and server. Applications connecting to Google services should trust all the Certificate Authorities listed by [Google Trust Services](https://pki.goog/faq/#connecting-to-google). You can download root certs from: <https://pki.goog/>.



## Sample call to a webhook server using mTLS

This example uses the agent shown in the quickstart with a [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) server running [`openssl`](https://www.openssl.org/docs/manmaster/man1/openssl.html).

  1. Sample setup 
     1. A Dialogflow CX agent that takes shirt orders, and sends them to a webhook pointing to a standalone web server. 
     2. A private key for TLS communication in a file named `key.pem`. 
     3. A certificate chain signed by a [publicly-trusted CA (Certificate Authority)](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#use_a_publicly-trusted_ca) in a file named `fullchain.pem`. 
  2. Execute the [`openssl s_server`](https://www.openssl.org/docs/manmaster/man1/openssl-s_server.html) program in the server machine. 
         
         sudo openssl s_server -key key.pem -cert fullchain.pem -accept 443 -verify 1

  3. A request is sent to the agent from a client machine. For this example, the request is "I want to buy a large red shirt". This request can be sent using the Dialogflow Console, or through an API call. 
  4. Output of `openssl s_server` in the server machine. 
         
         verify depth is 1
         Using default temp DH parameters
         ACCEPT
         **depth=2 C = US, O = Google Trust Services LLC, CN = GTS Root R1
         verify return:1
         depth=1 C = US, O = Google Trust Services LLC, CN = GTS CA 1D4
         verify return:1
         depth=0 CN = *.dialogflow.com
         verify return:1**
         -----BEGIN SSL SESSION PARAMETERS-----
         MII...
         -----END SSL SESSION PARAMETERS-----
         **Client certificate
         -----BEGIN CERTIFICATE-----
         MII...
         -----END CERTIFICATE-----
         subject=CN = *.dialogflow.com
         
         issuer=C = US, O = Google Trust Services LLC, CN = GTS CA 1D4**
         
         Shared ciphers:TLS_AES_128_GCM_SHA256:...
         Signature Algorithms: ECDSA+SHA256:...
         Shared Signature Algorithms: ECDSA+SHA256:...
         Peer signing digest: SHA256
         Peer signature type: RSA-PSS
         Supported Elliptic Groups: 0xEAEA:...
         Shared Elliptic groups: X25519:...
         CIPHER is TLS_AES_128_GCM_SHA256
         Secure Renegotiation IS NOT supported
         POST /shirts-agent-webhook HTTP/1.1
         authorization: Bearer ey...
         content-type: application/json
         Host: www.example.com
         Content-Length: 1595
         Connection: keep-alive
         Accept: */*
         **User-Agent: Google-Dialogflow**
         Accept-Encoding: gzip, deflate, br
         
         {
           "detectIntentResponseId": "a7951ce2-2f00-4af5-a508-4c2cb45698b0",
           "intentInfo": {
             "lastMatchedIntent": "projects/PROJECT_ID/locations/REGION/agents/AGENT_ID/intents/0adebb70-a727-4687-b8bc-fbbc2ac0b665",
             "parameters": {
               "color": {
                 "originalValue": "red",
                 "resolvedValue": "red"
               },
               "size": {
                 "originalValue": "large",
                 "resolvedValue": "large"
               }
             },
             "displayName": "order.new",
             "confidence": 0.9978873
           },
           "pageInfo": {
             "currentPage": "projects/PROJECT_ID/locations/REGION/agents/AGENT_ID/flows/00000000-0000-0000-0000-000000000000/pages/06e6fc4d-c2f2-4830-ab57-7a318f20fd90",
             "displayName": "Order Confirmation"
           },
           "sessionInfo": {
             "session": "projects/PROJECT_ID/locations/REGION/agents/AGENT_ID/sessions/session-test-001",
             "parameters": {
               "color": "red",
               "size": "large"
             }
           },
           "fulfillmentInfo": {
             "tag": "confirm"
           },
           "messages": [{
             "text": {
               "text": ["Ok, let\u0027s start a new order."],
               "redactedText": ["Ok, let\u0027s start a new order."]
             },
             "responseType": "ENTRY_PROMPT",
             "source": "VIRTUAL_AGENT"
           }, {
             "text": {
               "text": ["You have selected a large, red shirt."],
               "redactedText": ["You have selected a large, red shirt."]
             },
             "responseType": "HANDLER_PROMPT",
             "source": "VIRTUAL_AGENT"
           }],
           "text": "I want to buy a large red shirt",
           "languageCode": "en"
         }ERROR
         shutting down SSL
         CONNECTION CLOSED
               




## Custom Client Certificate

Custom client certificates can be configured at an agent level to be used by all webhooks. At the time of webhook invocation, the configured certificates will be presented during the handshake.

The private key and passphrase are configured as a Secret Manager resource. The Dialogflow service agent will need to be given Secret Manager Secret Accessor permissions to the secret.

The client certificates need to be signed by a Certificate Authority for the handshake to be successful. 

## Best Practice

To make sure that webhook requests are initiated from your own Dialogflow agents, you should verify the Bearer [service identity token](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#id-token) from the request's Authorization header. Alternatively, you can verify a session parameter provided previously by an authentication server on your side.

## Errors

If the client certificate validation fails (for example, the webhook server does not trust the client certificate), the TLS handshake fails and the session terminates.

Common error messages:

Error message | Explanation  
---|---  
Failed to verify client's certificate: x509: certificate signed by unknown authority | Dialogflow sends its client certificate to the external webhook, but the external webhook cannot verify it. This may be because the external webhook didn't install the CA chain correctly. All root CAs from Google should be trusted.  
  
[ Previous arrow_back  Using VPC Service Controls  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/vpc-service-controls)

[ Next Regionalization and location settings  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
