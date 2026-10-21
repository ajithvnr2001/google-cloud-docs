---
url: https://docs.cloud.google.com/solutions/event-driven-architecture-pubsub/
title: Event-driven architecture with Pub/Sub \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:31.464532+00:00
---

# Event-driven architecture with Pub/Sub  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/event-driven-architecture-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Event-driven architecture with Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses the differences between on-premises message-queue-driven architectures and the cloud-based, event-driven architectures that are implemented on [Pub/Sub](https://docs.cloud.google.com/pubsub/docs). Trying to apply on-premises patterns directly to cloud-based technologies, can miss out on the unique value that makes the cloud compelling in the first place.

This document is intended for system architects who are migrating designs from on-premises architectures to cloud-based designs. This document assumes that you have an introductory understanding of messaging systems.

The following diagram shows an overview of a message-queue model and a Pub/Sub model.

![Compares the architecture of a message-queue model with an event-driven model using Pub/Sub.](https://docs.cloud.google.com/static/solutions/images/event-driven-architecture-pubsub-1-comparison-overview.svg)

In the preceding diagram, a message-queue model is compared with a Pub/Sub event-stream model. In a message-queue model, the publisher pushes messages to a queue where each subscriber can listen to a particular queue. In the event-stream model using Pub/Sub, the publisher pushes messages to a topic that multiple subscribers can listen to. The differences between these models are described in the following sections.

## Comparing event streams and queue-based messaging

If you work with on-premises systems, you are already acquainted with [enterprise service buses (ESBs)](https://wikipedia.org/wiki/Enterprise_service_bus) and [message queues](https://wikipedia.org/wiki/Message_queue). Event streams are a new pattern and there are important differences with concrete advantages for modern real-time systems.

This document discusses the key differences in the transport mechanism and in the payload data in event-driven architecture.

## Message transport

The systems that move data around in these models are called message brokers, and there are a variety of frameworks implemented within them. One of the first concepts is the underlying mechanic that transports messages from the publisher to the receiver. In on-premises message frameworks, the originating system emits an explicit, remote, decoupled message to a downstream processing system by using a message queue as the transport.

The following diagram shows a message-queue model:

![Messages from a publisher are pushed to a unique queue for each subscriber.](https://docs.cloud.google.com/static/solutions/images/event-driven-architecture-pubsub-2-message-queue-model.svg)

In the preceding diagram, the messages flow from an upstream publisher process to a downstream subscriber process by using a message queue.

System A (the publisher) sends a message to a queue on the message broker designated for System B (the subscriber). While the subscriber of the queue can consist of multiple clients, all of those clients are duplicate instances of System B that are deployed for scaling and availability. If additional downstream processes—for example, System C—need to consume the same messages from the producer (System A), a new queue is required. You need to update the producer to publish the messages to the new queue. This model is often referred to as [message passing](https://wikipedia.org/wiki/Message_passing).

The message transport layer for these queues might or might not provide message order guarantees. Frequently, message queues are expected to provide an order-guaranteed model with data sequenced in a strict first-in-first-out (FIFO) access model, similar to a task queue. This pattern is initially easy to implement, but eventually presents scaling and operational challenges. To implement ordered messages, the system needs a central process to organize the data. This process limits scaling capabilities and reduces service availability because it is a single point of failure.

The messaging brokers in these architectures tend to implement additional logic such as tracking which subscriber has received which messages, and monitoring subscriber load. The subscribers tend to be merely reactive, possessing no knowledge of the overall system and simply running a function upon message receipt. These type of architectures are called _smart pipes_ (message-queue system) and _dumb endpoints_ (subscriber).

## Pub/Sub transport

Similar to message-oriented systems, event-streaming systems also transport messages from a source system to decoupled destination systems. However, rather than sending each message to a process-targeted queue, event-based systems tend to publish messages to a shared topic, and then one or more receivers subscribe to that topic to listen for relevant messages.

The following diagram shows how various messages are emitted by an upstream publisher to a single topic, and are then routed to the relevant downstream subscriber:

![Messages from a publisher are pushed to a single topic for all subscribers.](https://docs.cloud.google.com/static/solutions/images/event-driven-architecture-pubsub-3-pubsub-model.svg)

This pattern of publish and subscribe is where the term [_pub/sub_](https://wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) comes from. This pattern is also the basis for the Google Cloud product called [Pub/Sub](https://docs.cloud.google.com/pubsub). Throughout this document, pubsub refers to the pattern and Pub/Sub refers to the product.

In the pubsub model, the messaging system doesn't need to know about any of the subscribers. It doesn't track which messages have been received and it doesn't manage the load on the consuming process. Instead, the subscribers track which messages have been received and are responsible for self-managing load levels and scaling.

One significant benefit is that as you encounter new uses for the data in the pubsub model, you don't need to update the originating system to publish to new queues or duplicate data. Instead, you attach your new consumer to a new subscription without any impact on the existing system.

The calls in event-streaming systems are almost always asynchronous, they send events and don't wait for any response. Asynchronous eventing allows for greater scaling options for both the producer and consumers. However, this asynchronous pattern can create challenges if you're expecting FIFO message-order guarantees.

## Message-queue data

The data passed between systems in message-queue systems and pubsub-based systems is generally referred to as a _message_ in both contexts. However, the model in which that data is presented is different. In message-queue systems, the messages reflect a command that is intended to change the state of the downstream data. If you look at the data for on-premises message-queue systems, the publisher might state explicitly what the consumer should do. For example, an inventory message might indicate the following:
    
    
    <m:SetInventoryLevel>
        <inventoryValue>3001</inventoryValue>
    </m: SetInventoryLevel>
    

In this example, the producer is telling the consumer that it needs to set the inventory level to 3001. This approach can be challenging because the producer needs to understand the business logic of each consumer and it needs to create separate message structures for different use cases. This message-queue system was a common practice with the large monoliths that most enterprises implemented. However, if you want to move faster, scale larger, and innovate more than before, these centralized systems can become a bottleneck because change is risky and slow.

There are operational challenges with this pattern as well. When bad data, duplicate records, or other issues occur and need to be corrected, this messaging model presents a significant challenge. For example, if you need to roll back the message used in the preceding example, you don't know what to set the corrected value to because you have no reference to the previous state. You have no insight as to whether the inventory value was 3000 or 4000 before that message was sent.

## Pubsub data

Events are another way to send message data. What's unique is that event-driven systems focus on the event that occurred rather than the result that should occur. Instead of sending data indicating what action a consumer should take, the data focuses on the details of the actual event produced. You can implement event-driven systems on a variety of platforms, but they are frequently seen on pubsub-based systems.

For example, an inventory event might look like the following:
    
    
    { "inventory":-1 }
    

The previous event data indicates that an event occurred that decreased the inventory by 1. The messages focus on the event that occurred in the past and not a state to be changed in the future. Publishers are able to send messages in an asynchronous manner, thereby making event-driven systems easier to scale than message-queue models. In the pubsub model, you can decouple the business logic so that the producer only needs to understand the actions performed on it and doesn't need to understand the downstream processes. The subscribers of that data can choose how best to deal with the data that they receive. Because these messages are not imperative commands, the order of the messages becomes less important.

With this pattern, it is easier to roll back changes. In this example, no additional information is needed because you can negate the inventory value to move it in the opposite direction. Messages that come in late or out of order are no longer a concern.

## Model comparison

In this scenario, you have four items of the same product in your inventory. One customer returns one count of the product, and the next customer purchases three counts of that same product. For this scenario, assume that the message for the returned product was delayed.

The following table, compares the inventory level of the message-queue model receiving the inventory count in the correct order with the same model receiving the inventory count out of order:

Message queue (correct order) | Message queue (out of order)  
---|---  
Initial inventory: `4` | Initial inventory: `4`  
Message 1: `setInventory(5)` | Message 2: `setInventory(2)`  
Message 2: `setInventory(2)` | Message 1: `setInventory(5)`  
Inventory level:` 2` | Inventory level: `5`  
  
In the message-queue model, the order in which the messages are received is important because the message contains the precalculated value. In this example, if the messages arrive in the correct order, the inventory level is 2. However, if the messages arrive out of order, the inventory level is 5, which is inaccurate.

The following table compares the inventory level of the pubsub-based system receiving the inventory count in the correct order with the same system receiving the inventory count out of order:

Pubsub (correct order) | Pubsub (out of order)  
---|---  
Initial inventory: 4 | Initial inventory: 4  
Message 2: `"inventory":-3` | Message 1: `"inventory":+1`  
Message 1: `"inventory":+1` | Message 2: `"inventory":-3`  
Inventory level: `2` | Inventory level: `2`  
  
In the pubsub-based system, the ordering of the messages doesn't matter because it is informed by services that produce events. No matter what order the messages arrive, the inventory level is accurate.

The following diagram shows how in the message-queue model, the queue executes commands that tell the subscriber how the state should change while in the pubsub model, the subscribers react to event data that states what occurred in the publisher:

![Checkout example that compares reacting to commands to reacting to events.](https://docs.cloud.google.com/static/solutions/images/event-driven-architecture-pubsub-4-command-compare-events.svg)

# Implementing event-driven architectures

There are a variety of concepts to consider when implementing event-driven architectures. The following sections introduce some of those topics.

## Delivery guarantees

One concept that comes up in a system discussion is the reliability of the message-delivery guarantees. Different vendors and systems might provide different levels of reliability so it's important to understand the variations.

The first type of guarantee asks a simple question: if a message is sent is it guaranteed to be delivered? This is what is referred to as an at-least-once delivery. The message is guaranteed to be delivered at least one time, but it might be sent more than once.

A different type of guarantee is the at-most-once delivery. With at-most-once delivery, the message is only delivered a maximum of one time, but there are no guarantees that it is actually delivered.

The final variation for delivery guarantees is exactly-once delivery. In this model, the system sends one and only one copy of the message that is guaranteed to be delivered.

## Order and duplicates

In on-premises architectures, messages often follow a FIFO model. To achieve this model, a centralized processing system manages the sequencing of messages to ensure accurate ordering. Ordered messaging creates challenges because for any failed message, all messages need to be re-sent in sequence. Any centralized system can become a challenge for availability and scalability. Scaling a central system that manages ordering is typically only achievable by adding more resources to an existing machine. With a single system managing the order, any reliability issues impact the entire system rather than just that machine.

Highly scalable and available messaging services often use multiple processing systems to ensure messages are delivered at least once. With many systems, managing the messages order can't be guaranteed.

Event-driven architectures don't rely on message order and can tolerate duplicate messages. If order is required, subsystems can implement aggregation and windowing techniques; however, this approach sacrifices scalability and availability in that component.

## Filtering and fanout techniques

Because an event stream can contain data that might or might not be needed by every subscriber, there is often a need to limit the data a given subscriber receives. There are two patterns for managing this requirement: event filters and event fanouts.

The following diagram shows an event-driven system with event filters filtering messages for subscribers:

![Event-driven model with event filter that filters messages to subscribers.](https://docs.cloud.google.com/static/solutions/images/event-driven-architecture-pubsub-5-event-filters.svg)

In the preceding diagram, event filters use filtering mechanisms that limit the events that reach the subscriber. In this model, a single topic contains all variations of a message. Rather than a subscriber reading each message and verifying if it's applicable, filtering logic in the messaging system evaluates the message, keeping it from the other subscribers.

The following diagram shows a variation of the event filter pattern called event fanout that uses multiple topics:

![Event-driven model with event fanout that republishes messages on topics.](https://docs.cloud.google.com/static/solutions/images/event-driven-architecture-pubsub-6-event-fanout.svg)

In the preceding diagram, the primary topic contains all variations of a message, but an event fanout mechanism republishes the messages on topics that are related to that subset of subscribers.

## Unprocessed-message queues

Even in the best systems, failures can occur. Unprocessed-message queues are a technique for dealing with such failures. In most event-driven architectures, the message system continues to provide a message to a subscriber until it is acknowledged by the subscriber.

If there is an issue with a message—for example, invalid characters in the message body—the subscriber might not be able to acknowledge the message. The system can fail to handle the scenario or can even terminate the process.

Systems typically retry unacknowledged or errored messages. If an invalid message goes unacknowledged after a predetermined amount of time, the message eventually times out and is dropped from the topic. From an operational standpoint, it is useful to review the messages instead of them disappearing. This is where unprocessed-message queues come in. Rather than removing the message from the topic, the message is moved to another topic where it can be reprocessed or reviewed to understand why it errored out.

## Stream history and replays

Event streams are ongoing flows of data. Access to this historical data is useful. You might want to know how a system achieved a certain state. You might have security-related questions that require an audit of the data. Being able to capture a historical log of the events is critical in the long-term operations of an event-driven system.

One common use of historical event data is to use it with a replay system. Replays are used for testing purposes. By replaying event data from production in other environments like stage and test, you can validate new functionalities against real data sets. You can also replay historical data to recover from a failed state. If a system goes down or loses data, teams can replay the event history from a known good point and the service can rebuild the state that it lost.

Capturing these events in log-based queues or logging streams is also useful when subscribers need access to a sequence of events at different times. Logging streams can be seen in systems with offline capabilities. By using your stream history, you can process the latest new entries by reading the stream starting at the _last-read_ pointer.

## Data views: real time and near-real time

With all data flowing through the systems, it's important that you are able to use the data. There are many techniques for accessing and using these event streams, but a common use case is to understand the overall state of data at a specific moment. These are often calculation-oriented questions, such as "how many" or "current level" that can be used either by other systems or for human consumption. There are multiple implementations that can answer these questions:

  * A real-time system can run continuously and keep track of the current state; however, with the system only having an in-memory calculation, any downtime sets the calculation to zero.
  * The system can calculate values from the history table for every request, but this can become a problem because trying to calculate values for every request while the data grows can eventually become infeasible.
  * The system can create snapshots of the calculations at specific intervals, but using only the snapshots doesn't reflect real-time data.



A useful pattern to implement is a [Lambda architecture](https://wikipedia.org/wiki/Lambda_architecture) with both near-real-time and real-time capabilities. For example, a product page on an ecommerce site can use near-real-time views of inventory data. When customers place orders, a real-time service is used to ensure up-to-the-second status updates of the inventory data. To implement this pattern, the service responds to near-real-time requests from a snapshot table that contains calculated values on a given interval. A real-time request uses both the snapshot table and the values in the history table since the last snapshot to get the exact current state. These materialized views of the event streams provide actionable data to drive real business processes.

# What's next

  * Read about [Pub/Sub or Cloud Tasks for message passing and asynchronous integration](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-cloud-tasks).
  * Try the [Pub/Sub quickstart](https://docs.cloud.google.com/pubsub/docs/quickstart-py-mac).
  * Check out the Pub/Sub [Architectural overview](https://docs.cloud.google.com/pubsub/architecture)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
