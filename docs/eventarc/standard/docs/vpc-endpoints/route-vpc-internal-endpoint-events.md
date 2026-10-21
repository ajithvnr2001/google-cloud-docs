---
url: https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events/
title: Route events to an internal HTTP endpoint in a VPC network \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:45.673883+00:00
---

# Route events to an internal HTTP endpoint in a VPC network  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Route events to an internal HTTP endpoint in a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Eventarc lets you route events to internal HTTP endpoints hosted in a Virtual Private Cloud (VPC) network. This helps you integrate event-driven workflows with private backend services without exposing workloads to the public internet.

Eventarc delivers events to the event receiver in a [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents) through an HTTP request. You can configure triggers to capture direct events from Google Cloud sources, Cloud Audit Logs, or third-party providers.

These instructions show you how to configure event routing to an internal HTTP endpoint in a VPC network:

  * The internal HTTP endpoint can be an [internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) or [fully qualified DNS name (FQDN)](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) for any HTTP endpoint in the Virtual Private Cloud network. The following are two examples of possible event destinations:

    * A Compute Engine virtual machine (VM) instance—Compute Engine instances can run the public images for Linux and Windows Server that Google provides as well as private custom images that you can create or import from your existing systems. For more information, see [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances).
    * An internal load balancer—A Google Cloud internal Application Load Balancer is a proxy-based, regional Layer 7 load balancer that lets you run and scale your services behind an internal IP address. Internal Application Load Balancers distribute HTTP and HTTPS traffic to backends hosted on Compute Engine, Google Kubernetes Engine (GKE), and Cloud Run. For more information, see [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal).
  * A [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) is a virtual version of a physical network that is implemented inside of Google's production network. A [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks) is a VPC network defined in a _host project_ and made available as a centrally shared network for eligible resources in attached service projects.




## Before you begin

Before creating an Eventarc trigger to route events to an internal HTTP endpoint in a VPC network, you must create a network attachment that accepts connections in the same network and region containing the HTTP destination service.

A [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments) is a regional resource that lets you explicitly authorize a producer to connect to a consumer VPC network. To publish events, Eventarc uses the network attachment to establish a connection to the internal HTTP endpoint hosted in a VPC network.

These instructions assume that you have already created a VPC network and subnetwork, and that you have deployed your HTTP destination service.

**Note:** Eventarc reserves the subnet [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) IP range 240.0.0.0/20. The subnet used for the network attachment shouldn't overlap with this range.

For more information, see [Receive Pub/Sub events at an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-vpc-internal-endpoint) which demonstrates how to deploy an internal HTTP endpoint in a VPC network and route Pub/Sub events to the endpoint.

### Supported event types

The following are the supported event types when routing events to an internal HTTP endpoint in a VPC network:

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source)—Triggered by an unmediated event such as an update to an object in a Cloud Storage bucket or a message published to a Pub/Sub topic.

  * [Cloud Audit Logs events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)—Triggered when a log is produced through Cloud Audit Logs.

  * Third-party events—Triggered by the events of a non-Google provider that offers an Eventarc source.




### Known limitations

The following are known limitations when routing events to an internal HTTP endpoint in a VPC network:

  * You can't create more than one Eventarc trigger for the same DNS name.

  * There is a limit of 100 Eventarc triggers for internal HTTP endpoints per project.

  * Only the following Eventarc trigger locations are supported:

    * `asia-east1`
    * `europe-north1`
    * `europe-west1`
    * `us-central1`
    * `us-east1`



## Prepare to create a trigger

Before you create a trigger, complete these prerequisites:

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Cloud Logging and Eventarc APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com,logging.googleapis.com)

  3. If applicable, enable the API related to the direct events. For example, for Cloud Run functions events, enable `cloudfunctions.googleapis.com`.

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for your target service.

     1. In the Google Cloud console, go to the **Create service account** page.

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. Select your project.

     3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

In the **Service account description** field, enter a description. For example, `Service account for event trigger`.

     4. Click **Create and continue**.

     5. To provide appropriate access, in the **Select a role** list, select the required Identity and Access Management (IAM) roles to grant to your service account. For more information, see [Roles and permissions for an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/roles-permissions-internal).

For additional roles, click add **Add another role** and add each additional role.

     6. Click **Continue**.

     7. To finish creating the account, click **Done**.

  5. If you are creating a trigger for direct events from Cloud Storage, grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) to the Cloud Storage service agent:

     1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Select the **Include Google-provided role grants** checkbox.

     3. In the **Principal** column, find the Cloud Storage Service Agent with the form `service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`, and then click edit **Edit principal** in the corresponding row.

     4. Click either add **Add role** or add **Add another role**.

     5. In the **Select a role** list, filter for **Pub/Sub Publisher** , and then select the role.

     6. Click **Save**.

  6. If the URI of the internal HTTP endpoint in the VPC network uses the [internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) of a service resolvable by Cloud DNS, grant the [DNS Peer role](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.peer) (`roles/dns.peer`) on the VPC host project to the Eventarc service agent.

Note that depending on how you have configured the VPC network, the VPC host project might also be your Eventarc trigger project.

     1. In the Google Cloud console, on the project selector page, select the VPC host project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     3. Select the **Include Google-provided role grants** checkbox.

     4. Modify or add the Eventarc service agent as a principal:

        * If the Eventarc service agent already has other roles on the project, find the row containing the principal in the form `service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com`, click edit **Edit principal** in that row, and click add **Add another role**.

        * If the Eventarc service agent doesn't have any existing roles on the project, click person_add **Grant Access** , then enter the email address in the form `service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com`.

Replace `PROJECT_NUMBER` with the Google Cloud project number for your Eventarc trigger project. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
    
    gcloud projects describe PROJECT_ID --format='value(projectNumber)'

     5. In the **Select a role** list, filter for **DNS Peer** , and then select the role.

     6. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enable the Cloud Logging, Eventarc, and Eventarc Publishing APIs.
         
         gcloud services enable logging.googleapis.com \
           eventarc.googleapis.com \
           eventarcpublishing.googleapis.com

  3. If applicable, enable the API related to the events. For example, for Cloud Run functions events, enable `cloudfunctions.googleapis.com`.

  4. If you don't already have one, create a user-managed service account and then grant it the roles and permissions necessary so that Eventarc can manage events for your target service.

     1. Create the service account:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account. It must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. After you create a service account, you cannot change its name.

     2. Grant the required Identity and Access Management (IAM) roles or permissions. For more information, see [Roles and permissions for an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/roles-permissions-internal).

  5. If the URI of the internal HTTP endpoint in the VPC network uses the [internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) of a service resolvable by Cloud DNS, grant the [DNS Peer role](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.peer) (`roles/dns.peer`) on the VPC host project to the Eventarc service agent.

Note that depending on how you have configured the VPC network, the VPC host project might also be your Eventarc trigger project.
         
         gcloud projects add-iam-policy-binding VPC_HOST_PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com \
             --role=roles/dns.peer

Replace the following:

     * `VPC_HOST_PROJECT_ID`: the Google Cloud project ID for the VPC host project.
     * `PROJECT_NUMBER`: the Google Cloud project number for your Eventarc trigger project. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
    
    gcloud projects describe PROJECT_ID --format='value(projectNumber)'

  6. If you are creating a trigger for direct events from Cloud Storage, grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) on the project to the Cloud Storage service agent:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com \
             --role=roles/pubsub.publisher




## Create a trigger

You can create an Eventarc trigger using the Google Cloud CLI or through the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the Eventarc **Triggers** page. 

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**. 
  3. Type a **Trigger name**. 

This is the ID of the trigger and it must start with a letter. It can contain up to 63 lowercase letters, numbers, or hyphens.

  4. For the **Trigger type** , select **Google sources** or **Third-party**. 
  5. Select an **Event provider**. 

This is the service that is the source of events. For a Google source, this is either directly or through its audit logs.

  6. Depending on the event type that you are routing, do one of the following: 
     1. Direct events—In the **Event type** list, from the _Direct_ events, select an event type. 
        1. For direct Cloud Pub/Sub events, in the **Select a Cloud Pub/Sub topic** list, select a topic or accept the default of **None** so that a new topic is created for you. 
        2. For direct Cloud Storage events, specify or browse for the globally unique identifier of the Cloud Storage **Bucket**. 
     2. Audit log events—In the **Event type** list, from the _via Cloud Audit Logs_ events, select an event type, and then select one of the following: 
        * **Any resource** —This is the default and includes dynamically created resources that have identifiers generated at creation time. 
        * **Specific resource** —You must provide the full resource name. 
        * **Path pattern** —You can [filter for resources using a path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns). For example, type `projects/_/buckets/eventarc-bucket/objects/random.txt` or type `projects/_/buckets/**/r*.txt`. 
     3. Third-party events—In the **Channel** list, select a channel and then, in the **Event type** list, select an event. 

For more information, see [Create a channel and retrieve its details](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels).

  7. If applicable to the event type, in the **Event data content type** list, select **application/json** or **application/protobuf** to specify the encoding of the event payload. 

Note that an event payload formatted in JSON is larger than one formatted in Protobuf. This might impact reliability depending on your event destination and its limits on event size. For more information, see [Known issues](https://docs.cloud.google.com/eventarc/docs/issues).

  8. If applicable to the event provider, click **Add filter** and specify the following: 
     1. In the **Attribute 1** field, depending on the direct event you chose, select a [resource ID](https://docs.cloud.google.com/apis/design/resource_names) that can act as an event filter.
     2. Select an operator: 
        * **Equal**
        * **Path pattern**

For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).

     3. In the **Attribute value 1** field, depending on the operator that you chose, type the exact value or apply a path pattern.
     4. If an **Attribute 2** field is applicable, specify the appropriate values.
  9. In the **Region** list, select a location. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events.

Note that for this event destination, only the following locations are supported:

     * `asia-east1`
     * `europe-north1`
     * `europe-west1`
     * `us-east1`

For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

  10. Select the **Service account** that will invoke your service. 

Or, you can create a new service account.

This specifies the IAM service account email associated with the trigger and to which you previously granted [specific roles](https://docs.cloud.google.com/eventarc/docs/access-control) required by Eventarc.

  11. In the **Event destination** list, select **HTTP endpoint (internal)**. 
     1. Specify the **Destination URI**. This is the URI of the internal HTTP endpoint in the VPC network that receives the events for the trigger. The URI can be either a [static internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) in the VPC network addressed by the network attachment or the [internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) of a service resolvable by Cloud DNS. 

If the HTTP endpoint uses an internal DNS name, Eventarc automatically creates DNS peering zones and forwards DNS requests to the DNS zones in the target VPC network. DNS peering lets you send requests for records that come from one zone's namespace to another VPC network. For more information, see [Peering zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) and [Create a peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones).

Note that you can't create more than one trigger for the same DNS name.

     2. In the **Network attachment** list, select an identifier for the network attachment resource. This identifier is generated after you create a network attachment. For more information, see [Create network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachments). 

Network attachments let service producer VPC networks initiate connections to consumer VPC networks. Eventarc uses the network attachment to establish a connection to the internal HTTP endpoint hosted in the consumer's VPC network and publish events.

When you create a network attachment, you can explicitly authorize a connection through producer accept and reject lists; regardless, Eventarc can update the accept list of a network attachment with the appropriate project ID and without any intervention on your part.

  12. Click **Create**.

After a trigger is created, the event source filters cannot be modified. Instead, create a new trigger and delete the earlier one. For more information, see [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers).




###  gcloud 

You can create a trigger by running a `gcloud eventarc triggers create` command along with required and optional flags.

###  Direct events 
    
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-http-endpoint-uri=ENDPOINT_URI \
        --network-attachment=NETWORK_ATTACHMENT_ID \
        --event-filters="type=EVENT_FILTER_TYPE" \
        --event-filters="COLLECTION_ID=RESOURCE_ID" \
        --event-filters-path-pattern="COLLECTION_ID=PATH_PATTERN" \
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
  * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`.

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events.

Note that for this event destination, only the following locations are supported:

    * `asia-east1`
    * `europe-north1`
    * `europe-west1`
    * `us-central1`
    * `us-east1`

For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

  * `ENDPOINT_URI`: the URI of the internal HTTP endpoint in the VPC network that receives the events for the trigger. The URI can be either a [static internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) in the VPC network addressed by the network attachment or the [internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) of a service resolvable by Cloud DNS.

If the HTTP endpoint uses an internal DNS name, Eventarc automatically creates DNS peering zones and forwards DNS requests to the DNS zones in the target VPC network. DNS peering lets you send requests for records that come from one zone's namespace to another VPC network. For more information, see [Peering zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) and [Create a peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones).

Note that you can't create more than one trigger for the same DNS name.

  * `NETWORK_ATTACHMENT_ID`: unique identifier for the network attachment resource. The identifier is generated after you create a network attachment. For more information, see [Create network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachments).

Network attachments let service producer VPC networks initiate connections to consumer VPC networks. Eventarc uses the network attachment to establish a connection to the internal HTTP endpoint hosted in the consumer's VPC network and publish events.

When you create a network attachment, you can explicitly authorize a connection through producer accept and reject lists; regardless, Eventarc can update the accept list of a network attachment with the appropriate project ID and without any intervention on your part.

  * `EVENT_FILTER_TYPE`: the identifier of the event. An event is generated when an API call for the method succeeds. For long-running operations, the event is only generated at the end of the operation, and only if the action is performed successfully. See the list of [supported direct event types](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source).

  * `COLLECTION_ID` (optional): the [resource](https://docs.cloud.google.com/apis/design/resource_names) component that can act as an event filter; for example, for Cloud Run functions, this is `function`.

  * `RESOURCE_ID`: the identifier of the resource used as the filtering value for the associated collection. For more information, see [Resource ID](https://docs.cloud.google.com/apis/design/resource_names#resource_id).

  * `PATH_PATTERN`: the [path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns) to apply when filtering for the resource.

  * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account.

  * `PROJECT_ID`: your Google Cloud project ID.




Notes:

  * The `--event-filters="type=EVENT_FILTER_TYPE"` flag is required. If no other event filter is set, events for all resources are matched.
  * `EVENT_FILTER_TYPE` cannot be changed after creation. To change `EVENT_FILTER_TYPE`, create a new trigger and delete the earlier one.
  * Each trigger can have multiple event filters, comma delimited in one `--event-filters`=[`ATTRIBUTE`=`VALUE`,...] flag, or you can repeat the flag to add more filters. Only events that match all the filters are sent to the destination. Wildcards and regular expressions are not supported; however, when using the `--event-filters-path-pattern` flag, you can define a resource [path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns).
  * The `--service-account` flag is used to specify the IAM service account email associated with the trigger.



Example:
    
    
    gcloud eventarc triggers create helloworld-trigger \
        --location=us-central1 \
        --destination-http-endpoint-uri=http://my-vm.us-central1-a.c.my-project.internal \
        --network-attachment="projects/my-project/regions/us-central1/networkAttachments/my-attachment-name" \
        --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
        --service-account=my-service-account@my-project.iam.gserviceaccount.com

###  Audit log events 
    
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-http-endpoint-uri=ENDPOINT_URI \
        --network-attachment=NETWORK_ATTACHMENT_ID \
        --event-filters="type=google.cloud.audit.log.v1.written" \
        --event-filters="serviceName=SERVICE_NAME" \
        --event-filters="methodName=METHOD_NAME" \
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
  * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`.

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. The following locations are supported:

    * `asia-east1`
    * `europe-north1`
    * `europe-west1`
    * `us-central1`
    * `us-east1`

For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

  * `ENDPOINT_URI`: the URI of the internal HTTP endpoint in the VPC network that receives the events for the trigger. The URI can be either a [static internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) in the VPC network addressed by the network attachment or the [internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) of a service resolvable by Cloud DNS.

If the HTTP endpoint uses an internal DNS name, Eventarc automatically creates DNS peering zones and forwards DNS requests to the DNS zones in the target VPC network. DNS peering lets you send requests for records that come from one zone's namespace to another VPC network. For more information, see [Peering zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) and [Create a peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones).

Note that you can't create more than one trigger for the same DNS name.

  * `NETWORK_ATTACHMENT_ID`: unique identifier for the network attachment resource. The identifier is generated after you create a network attachment. For more information, see [Create network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachments).

Network attachments let service producer VPC networks initiate connections to consumer VPC networks. Eventarc uses the network attachment to establish a connection to the internal HTTP endpoint hosted in the consumer's VPC network and publish events.

When you create a network attachment, you can explicitly authorize a connection through producer accept and reject lists; regardless, Eventarc can update the accept list of a network attachment with the appropriate project ID and without any intervention on your part.

  * `SERVICE_NAME`: the identifier of the Google Cloud service. See the list of [supported audit log event types](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs).

  * `METHOD_NAME`: the identifier of the operation. See the list of [supported audit log event types](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs).

  * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account.

  * `PROJECT_ID`: your Google Cloud project ID.




Notes:

  * These flags are required: 
    * `--event-filters="type=google.cloud.audit.log.v1.written"`
    * `--event-filters="serviceName=VALUE"`
    * `--event-filters="methodName=VALUE"`
  * Optionally, filter events for a specific resource by using the `--event-filters="resourceName=VALUE"` flag and specifying the complete path to the resource. Omit the flag for dynamically created resources that have identifiers generated at creation time. Or, filter events for a set of resources by using the `--event-filters-path-pattern="resourceName=VALUE"` flag and specifying the [resource path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns).
  * Each trigger can have multiple event filters, comma delimited in one `--event-filters`=[`ATTRIBUTE`=`VALUE`,...] flag, or you can repeat the flag to add more filters. Only events that match all the filters are sent to the destination. Wildcards and regular expressions are not supported; however, when using the `--event-filters-path-pattern` flag, you can define a resource [path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns).
  * After a trigger is created, the event filter type can't be changed. For a different event type, you must create a new trigger.
  * The `--service-account` flag is used to specify the IAM service account email associated with the trigger.



Example:
    
    
    gcloud eventarc triggers create helloworld-trigger \
        --location=us-central1 \
        --destination-http-endpoint-uri=http://10.10.10.2 \
        --network-attachment="projects/my-project/regions/us-central1/networkAttachments/my-attachment" \
        --event-filters="type=google.cloud.audit.log.v1.written" \
        --event-filters="serviceName=eventarc.googleapis.com" \
        --event-filters="methodName=google.cloud.eventarc.v1.Eventarc.GetTrigger" \
        --event-filters="resourceName=projects/my-project/locations/us-central1/triggers/my-trigger" \
        --service-account=my-service-account@my-project.iam.gserviceaccount.com

###  Third-party events 
    
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-http-endpoint-uri=ENDPOINT_URI \
        --network-attachment=NETWORK_ATTACHMENT_ID \
        --event-filters="type=EVENT_FILTER_TYPE" \
        --channel=CHANNEL_NAME \
        --project=PROJECT_ID \
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
  * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`.

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events.

Note that for this event destination, only the following locations are supported:

    * `asia-east1`
    * `europe-north1`
    * `europe-west1`
    * `us-central1`
    * `us-east1`

For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

  * `ENDPOINT_URI`: the URI of the internal HTTP endpoint in the VPC network that receives the events for the trigger. The URI can be either a [static internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) in the VPC network addressed by the network attachment or the [internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) of a service resolvable by Cloud DNS.

If the HTTP endpoint uses an internal DNS name, Eventarc automatically creates DNS peering zones and forwards DNS requests to the DNS zones in the target VPC network. DNS peering lets you send requests for records that come from one zone's namespace to another VPC network. For more information, see [Peering zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) and [Create a peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones).

Note that you can't create more than one trigger for the same DNS name.

  * `NETWORK_ATTACHMENT_ID`: unique identifier for the network attachment resource. The identifier is generated after you create a network attachment. For more information, see [Create network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachments).

Network attachments let service producer VPC networks initiate connections to consumer VPC networks. Eventarc uses the network attachment to establish a connection to the internal HTTP endpoint hosted in the consumer's VPC network and publish events.

When you create a network attachment, you can explicitly authorize a connection through producer accept and reject lists; regardless, Eventarc can update the accept list of a network attachment with the appropriate project ID and without any intervention on your part.

  * `EVENT_FILTER_TYPE`: the type of event supported by the provider.

  * `CHANNEL_NAME`: a name for the channel. For more information, see [Create a channel and retrieve its details](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels).

  * `PROJECT_ID`: your Google Cloud project ID.

  * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account.




Notes:

  * The `--event-filters="type=EVENT_FILTER_TYPE"` flag is required. If no other event filter is set, events for all resources are matched.
  * `EVENT_FILTER_TYPE` cannot be changed after creation. To change `EVENT_FILTER_TYPE`, create a new trigger and delete the earlier one.
  * Each trigger can have multiple event filters, comma delimited in one `--event-filters`=[`ATTRIBUTE`=`VALUE`,...] flag, or you can repeat the flag to add more filters. Only events that match all the filters are sent to the destination. Wildcards and regular expressions are not supported.
  * The `--service-account` flag is used to specify the IAM service account email associated with the trigger.



Example:
    
    
    gcloud eventarc triggers create helloworld-trigger \
        --location=us-central1 \
        --destination-http-endpoint-uri=http://my-vm.us-central1-a.c.my-project.internal \
        --network-attachment="projects/my-project/regions/us-central1/networkAttachments/my-attachment-name" \
        --event-filters="type=third-party-event-type" \
        --channel=my-channel \
        --project=my-project-ID \
        --service-account=my-service-account@my-project.iam.gserviceaccount.com

**Note:** Although your trigger is created immediately, it can take up to two minutes for a trigger to propagate and filter events.

## List a trigger

You can confirm the creation of a trigger by listing Eventarc triggers using the Google Cloud CLI or through the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the Eventarc **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

This page lists your triggers in all locations, and includes details such as names, regions, event providers, destinations, and more.

  2. To filter your triggers:

     1. Click filter_list **Filter** or the **Filter triggers** field.
  3. In the **Properties** list, select an option to filter the triggers by.



You can select a single property or use the logical operator `OR` to add more properties.

* To sort your triggers, beside any supported column heading, click arrow_upward **Sort**.

###  gcloud 

Run the following command to list your triggers:
    
    
    gcloud eventarc triggers list --location=-

This command lists your triggers in all locations, and includes details such as names, types, destinations, and statuses.

## What's next

  * [Eventarc overview](https://docs.cloud.google.com/eventarc/standard/docs/overview)
  * [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers)
  * [Tutorial: Receive Pub/Sub events at an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-vpc-internal-endpoint)
  * [Tutorial: Receive Pub/Sub events at a private HTTP endpoint in a private GKE cluster](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-gke-private-endpoint)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
