---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/websocket-config/
title: Using WebSockets \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:44.598093+00:00
---

# Using WebSockets  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/websocket-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using WebSockets Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic discusses how to use [WebSockets](https://en.wikipedia.org/wiki/WebSocket) with Apigee and Apigee hybrid. 

##  Introduction 

There are many situations where web interactions need to happen in real time, such as gaming, communications, financial transactions, and other high-throughput activities.

WebSocket is a protocol that provides a full-duplex communications channel between a web client and web server over a single TCP connection. The WebSocket protocol uses the HTTP protocol to establish the connection between the client and server. Once established, the client and server then use the WebSocket protocol to send and receive data.

The [WebSockets spec](https://html.spec.whatwg.org/multipage/web-sockets.html) and protocol is maintained by the W3C.

## Support for WebSockets in Apigee

In Apigee and Apigee hybrid, environment groups provide routing to environments and define the hostnames on which API proxies are exposed. Environment groups support both the HTTP and WS protocols natively. You do not have to create a special environment group or any special configuration to use WebSockets.

**Note:** Because Apigee acts as a pass-through for WebSocket traffic, the API proxy **must connect to a backend target server** that supports the WebSocket protocol. The backend server is responsible for generating the `101 Switching Protocols` response; Apigee cannot generate this response on its own (for example, in a "No Target" proxy configuration).

It is up to the client to request a protocol upgrade from HTTP to WS by including the `Upgrade` request header. When an upgrade request is made to an API proxy connected to a valid WebSocket backend, the target returns a `101 Switching Protocols` response. Further requests and responses are made bidirectionally on the open WebSockets connection, until it is closed.

###  Policy support 

All policies will work in a web socket proxy until the handshake is completed (i.e. until the `HTTP 101` response is returned to the client). After that, no policy will execute, but OAuth tokens validated before the handshake are still honored and the connection drops when the token expires or is revoked.

###  Revoking the connection 

The WebSockets connection is closed when: 

  * The proxy endpoint receives a request without an API key or OAuth token.
  * The proxy endpoint receives a request with an expired or invalid API key or OAuth token.
  * The WebSockets connection times out.



###  Using debug and analytics 

In the Debug tool, for each WebSockets connection you'll see one request appear with a **101 Status**.

In the Apigee analytics dashboard, you will see traffic counted for each WebSockets session. Back and forth traffic that occurs during the session is not shown in the dashboard.

##  Sample WebSockets application 

To learn more, you can refer to a working [websocket-sample](https://github.com/srinandan/websocket-sample) application on GitHub. The sample demonstrates how to call an API proxy over a WebSockets connection. The proxy calls a simple backend target application that is deployed in your Kubernetes cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
