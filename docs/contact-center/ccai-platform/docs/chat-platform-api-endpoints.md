---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-endpoints/
title: Chat platform API endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:28:19.832882+00:00
---

# Chat platform API endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat platform API endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The chat platform API endpoints provide access to the chat objects. A chat object is created for every chat that is made to and from Contact Center AI Platform (CCAI Platform).

The following are the chat platform API endpoints:

  * Update a chat

  * Send a message in a chat

  * Escalate virtual agent chat

  * Update escalation

  * Add uploaded photo to the chat

  * Fetch all photos from the chat

  * Get pre-signed photo upload URL

  * Add uploaded video to the chat

  * Fetch all videos from the chat

  * Get pre-signed video upload URL

  * Create chat

  * Returns a chat ID

  * Resume chat

  * Get reserved data attributes during a chat

  * Update reserved data attributes during a chat

  * Send custom data in chat

  * Update end-user during ongoing chat session




## Chat object

A chat object is created for every mobile and web chat session on CCAI Platform. The following is the chat object:
    
    
    {
        "id": "integer",
        "status": "string",
        "status_text": "string",
        "features": [
            "string",
            "string"
        ],
        "created_at": "string",
        "ends_at": "string",
        "timeout_at": "string",
        "agent": {
            "id": "integer",
            "name": "string",
            "first_name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "virtual_agent": {
            "id": "integer",
            "name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "all_agents": [
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "all_virtual_agents": [
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "lang": "string",
        "menus": [
            {
                "id": "integer",
                "name": "string"
            },
            {
                "id": "integer",
                "name": "string"
            }
        ],
        "end_user": {
            "id": "integer",
            "identifier": "string"
        }
    }
    

## Update a chat

Parameter | Required | Data Type | Definition  
---|---|---|---  
id | TRUE | Integer | The chat ID to update  
  
**_Endpoint:_**
    
    
    Method: PATCH
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:id
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
**_Body:_**
    
    
    {
        "finished_by_user_id": "integer",
        "chat": {
            "deflection_channel": "string",
            "status": "string",
            "escalation_id": "integer"
        }
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Update a chat

This example demonstrates the successful update of an existing chat

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
id | Integer | (Required)  
  
**_Body:_**
    
    
    {
        "finished_by_user_id": "integer",
        "chat": {
            "deflection_channel": "string",
            "status": "finished",
            "escalation_id": "integer"
        }
    }
    

##### Response
    
    
    {
        "id": "integer",
        "status": "string",
        "status_text": "string",
        "features": [
            "string",
            "string"
        ],
        "created_at": "string",
        "ends_at": "string",
        "timeout_at": "string",
        "agent": {
            "id": "integer",
            "name": "string",
            "first_name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "virtual_agent": {
            "id": "integer",
            "name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "all_agents": [
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "all_virtual_agents": [
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "lang": "string",
        "menus": [
            {
                "id": "integer",
                "name": "string"
            },
            {
                "id": "integer",
                "name": "string"
            }
        ],
        "end_user": {
            "id": "integer",
            "identifier": "string"
        }
    }
    

**_Status Code:_** 200

## Send a message in a chat

This method provides the ability to send a message in an existing chat session.

Parameter | Required | Data Type | Definition  
---|---|---|---  
id | TRUE | Integer | The chat ID that the message should sent in.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:id/message
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "from_user_id": integer,
        "message": {
                "type": "string",
                "content": "string"
        }
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful message send

This example demonstrates a successful submission of a message to an existing chat session.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
id | Integer | (Required)  
  
**_Body:_**
    
    
    {
        "from_user_id": integer,
        "message": {
                "type": "string",
                "content": "string"
        }
    }
    

##### Response
    
    
    {
    }
    

**_Status Code:_** 200

## Escalate virtual agent chat

Escalate a chat from a virtual agent to a human agent.

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID to escalate.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:chat_id/escalations
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Body:_**
    
    
    {
        "reason": "string",
        "force_escalate": "boolean"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful chat escalation

This example demonstrates the request to escalate an existing chat to human agent.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
**_Body:_**
    
    
    {
        "reason": "by_end_user_ask",
        "force_escalate": true
    }
    

##### Response
    
    
    {
        "id": "integer",
        "chat_id": "integer",
        "status": "string"
    }
    

**_Status Code:_** 200

## Update escalation

Used only for selecting the deflection channel.

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID to update the deflection menu ID.  
id | TRUE | Integer | The required menu ID.  
  
**_Endpoint:_**
    
    
    Method: PATCH
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:chat_id/escalations/:id
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "deflection_channel": "string"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful escalation update

This example demonstrates a successful update of the escalation channel.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
id | Integer | (Required)  
  
**_Body:_**
    
    
    {
        "deflection_channel": "string"
    }
    

##### Response
    
    
    {
        "id": "integer",
        "chat_id": "integer",
        "status": "string"
    }
    

**_Status Code:_** 200

## Add uploaded photo to the chat

Add a photo that has been uploaded to media storage to a chat

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID to add the photo to.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}/apps/api/v1/chats/:chat_id/photos
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
**_Body:_**
    
    
    {
        "photo": [
            {
                "s3_path": "string",
                "photo_type": "string"
            },
            {
                "s3_path": "string",
                "photo_type": "string"
            }
        ]
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful addition of a photo to chat

The following example demonstrates the addition of a photo that has been uploaded to a media storage to an existing chat conversation.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
**_Body:_**
    
    
    {
        "photo": [
            {
                "s3_path": "string",
                "photo_type": "string"
            },
            {
                "s3_path": "string",
                "photo_type": "string"
            }
        ]
    }
    

##### Response
    
    
    {
        "url": "string",
        "media_id": "integer"
    }
    

**_Status Code:_** 200

## Fetch all photos from the chat

Gets media ID and storage URL for all photos attached to the chat.

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID to get the media information.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type:
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:chat_id/photos
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful retrieval of chat photo information for a chat

This example demonstrates a successful call to the API to get the photo information for an existing chat session.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
##### Response
    
    
    [
        {
            "url": "string",
            "media_id": "integer"
        },
        {
            "url": "string",
            "media_id": "integer"
        }
    ]
    

**_Status Code:_** 200

## Get pre-signed photo upload URL

Used for getting a pre-signed upload URL for photos.

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID that will be associated with the pre-signed photo URL.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:chat_id/photos/upload
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful retrieval of signed URL for upload

The following is an example of a successful request with retrieval of a signed URL for photo upload.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
##### Response
    
    
    {
        "url": "string",
        "fields": {
            "key": "string",
            "success_action_status": "string",
            "Content-Type": "string",
            "Cache-Control": "string",
            "acl": "string",
            "policy": "string",
            "x-amz-credential": "string",
            "x-amz-algorithm": "string",
            "x-amz-date": "string",
            "x-amz-security-token": "string",
            "x-amz-signature": "string",
            "x-goog-algorithm": "string",
            "x-goog-credential": "string",
            "x-goog-date": "string",
            "x-goog-signature": "string"
        }
    }
    

**_Status Code:_** 200

## Add uploaded video to the chat

Add a video that has been uploaded to media storage to a chat.

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID that the video should be associated with.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:chat_id/videos
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
**_Body:_**
    
    
    {
        "video": {
            "s3_path": "string",
            "gcs_path": "string"
        }
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful upload of a video to a chat session

This example demonstrates the successful upload of a video to a chat session.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
**_Body:_**
    
    
    {
        "photo": [
            {
                "s3_path": "string",
                "photo_type": "string"
            },
            {
                "s3_path": "string",
                "photo_type": "string"
            }
        ]
    }
    

##### Response
    
    
    Body
    {
        "url": "string",
        "media_id": "integer"
    }
    

**_Status Code:_** 200

## Fetch all videos from the chat

Gets media ID and storage URL for all videos attached to the chat.

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID for which the video URLs will be retrieved.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type:
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:chat_id/videos
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Retrieve all video URLs for a chat

This example demonstrates the retrieval of all video URLs for an existing chat.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
##### Response
    
    
    [
        {
            "url": "string",
            "media_id": "integer"
        },
        {
            "url": "string",
            "media_id": "integer"
        }
    ]
    

**_Status Code:_** 200

## Get pre-signed video upload URL

Used for getting a pre-signed upload URL for videos.

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_id | TRUE | Integer | The required chat ID that will be associated with the pre-signed video URL.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/chats/:chat_id/videos/upload
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Successful retrieval of signed URL for video upload

The following is an example of a successful request with retrieval of a signed URL for video upload.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
##### Response
    
    
    {
        "url": "string",
        "fields": {
            "key": "string",
            "success_action_status": "string",
            "Content-Type": "string",
            "Cache-Control": "string",
            "acl": "string",
            "policy": "string",
            "x-amz-credential": "string",
            "x-amz-algorithm": "string",
            "x-amz-date": "string",
            "x-amz-security-token": "string",
            "x-amz-signature": "string",
            "x-goog-algorithm": "string",
            "x-goog-credential": "string",
            "x-goog-date": "string",
            "x-goog-signature": "string"
        }
    }
    

**_Status Code:_** 200

## Create chat

Start a new chat session.

### Example request

Method: `POST`

URL: `https://{subdomain}.{domain}/apps/api/v1/chats`

#### Headers

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
#### Body
    
    
    {
        "chat": {
            "menu_id": "integer",
            "end_user_id": "integer",
            "lang": "string",
            "email": "string",
            "context": "object",
            "transcript": "object"
        },
        "end_user": {
            "phone": "string"
        }
    }
    

**Context:**

The `context` object includes the `value` object, which passes metadata to the chat conversation. You can pass the `context` object to virtual agents as an unsigned data parameter. See the following example:
    
    
    {
        "context": {
            {"value":
                {"foo": "bar",
                 "key": "value"}
            }
        }
    }
    

In this example, the unsigned data parameter value for the incoming field is `context` and the destination field could be set to `context`. This would let you use `$session.params.context.foo` or `$session.params.context.key`.

### Example response
    
    
    {
        "id": "integer",
        "status": "string",
        "status_text": "string",
        "features": [
            "string",
            "string"
        ],
        "created_at": "string",
        "ends_at": "string",
        "timeout_at": "string",
        "agent": {
            "id": "integer",
            "name": "string",
            "first_name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "virtual_agent": {
            "id": "integer",
            "name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "all_agents": [
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "all_virtual_agents": [
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "lang": "string",
        "menus": [
            {
                "id": "integer",
                "name": "string"
            },
            {
                "id": "integer",
                "name": "string"
            }
        ],
        "end_user": {
            "id": "integer",
            "identifier": "string"
        }
    }
    

## Returns a chat by ID

This method returns the chat object for a given chat ID.

**_Endpoint:_**
    
    
    Method: GET
    Type:
    URL: https://{subdomain}.​{domain}/apps/api/v1/chats/:id
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json  
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Retrieve a chat successfully

The following example demonstrates the successful request for an existing chat ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-type | application/json |   
Accept | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
chat_id | Integer | (Required)  
  
##### Response
    
    
    {
        "id": "integer",
        "status": "string",
        "status_text": "string",
        "features": [
            "string",
            "string"
        ],
        "created_at": "string",
        "ends_at": "string",
        "timeout_at": "string",
        "agent": {
            "id": "integer",
            "name": "string",
            "first_name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "virtual_agent": {
            "id": "integer",
            "name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "all_agents": [
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "all_virtual_agents": [
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            },
            {
                "id": "integer",
                "name": "string",
                "avatar_url": "string",
                "status": "string"
            }
        ],
        "lang": "string",
        "menus": [
            {
                "id": "integer",
                "name": "string"
            },
            {
                "id": "integer",
                "name": "string"
            }
        ],
        "end_user": {
            "id": "integer",
            "identifier": "string"
        }
    }
    

**_Status Code:_** 200

## Resume chat

Resumes a chat that has been dismissed for inactivity. The chat status must be `dismissed` or `va_dismissed`.

### Example request

Method: `POST`

URL: `https://{subdomain}.{domain}/apps/api/v1/chats/:id/resume`

#### Headers

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
#### URL variables

Key | Value | Description  
---|---|---  
id | integer | (Required)  
  
### Example response
    
    
    {
        "id": "integer",
        "status": "string",
        "status_text": "string",
        "features": [
            "string",
            "string"
        ],
        "created_at": "string",
        "ends_at": "string",
        "timeout_at": "string",
        "agent": {
            "id": "integer",
            "name": "string",
            "first_name": "string",
            "avatar_url": "string",
            "status": "string"
        },
        "virtual_agent": {
            "id": "integer",
            "name": "string",
            "va_alias": "string",
            "avatar_url": "string"
        },
        "all_agents": [
            {
                "id": "integer",
                "name": "string",
                "first_name": "string",
                "avatar_url": "string"
            }
        ],
        "all_virtual_agents": [
            {
                "id": "integer",
                "name": "string",
                "va_alias": "string",
                "avatar_url": "string"
            }
        ],
        "lang": "string",
        "menus": [
            {
                "id": "integer",
                "name": "string"
            }
        ],
        "end_user": {
            "id": "integer",
            "identifier": "string"
        }
    }
    

## Get reserved data attributes during a chat

**Endpoint**
    
    
    Method: GET
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/chats/:id/customer_flag
    

### Example request and responses

This section contains an example request and response for the endpoint.

#### Success

This example shows a successful call.

##### Request

**Headers**

Key | Value | Description  
---|---|---  
Accept | application/json |   
  
**URL variables**

Key | Value | Description  
---|---|---  
id | integer | (Required)  
  
##### Response
    
    
    {
        "verified_customer": "boolean",
        "bad_actor": "boolean",
        "repeat_customer": "boolean"
    }
    

## Update reserved data attributes during a chat

**Endpoint**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/chats/:id/customer_flag
    

**URL variables**

Key | Value | Description  
---|---|---  
id | integer | (Required)  
  
**Body**
    
    
    {
        "verified_customer": "boolean",
        "bad_actor": "boolean",
        "repeat_customers": "boolean"
    }
    

## Send custom data in chat

Send custom data in a chat.

### Example request

Method: `POST`

URL: `https://{subdomain}.{domain}/apps/api/v1/chats/:id/custom_data`

#### Headers

Key  | Value  | Description   
---|---|---  
Content-Type  | application/json  |   
  
#### URL variables

Key  | Value  | Description   
---|---|---  
id  | integer  | (Required)   
  
### Example response
    
    
    // Use unsecured parameter
    {
    "signed": false,
    "data": {
    // Start customer_flag fields
    "reserved_verified_customer": {
    "label": "LABEL 1",
    "value": true
    },
    "reserved_bad_actor": {
    "label": "LABEL 2",
    "value": false
    },
    "reserved_repeat_customer": {
    "label": "LABEL 3",
    "value": true
    },
    // End customer_flag fields
    "field1": {
    "label": "LABEL 4",
    "value": "dummy1"
    },
    "field2": {
    "label": "LABEL 5",
    "value": "dummy2"
    }
    }
    }
    // Use secured parameter
    // {
    // "signed": true,
    // "signed_data": "eyJhbGciOiJIUzI1NiJ9.eyJjdXN0b21fZGF0YSI6eyJyZXNlcnZlZF92ZXJpZmllZF9jdXN0b21lciI6eyJ2YWx1ZSI6ZmFsc2V9LCJyZXNlcnZlZF9iYWRfYWN0b3IiOnsidmFsdWUiOnRydWV9LCJyZXNlcnZlZF9yZXBlYXRfY3VzdG9tZXIiOnsidmFsdWUiOmZhbHNlfSwiZmllbGQxIjp7InZhbHVlIjoiZHVtbXkxMTEifSwiZmllbGQyIjp7InZhbHVlIjoiZHVtbXkyMjIifX0sImV4cCI6MTcyOTY4MzU5MywiaWF0IjoxNzI5Njc5OTkzfQ.BMskgKTM3DbgrMLWjI46ZJ1K73H25JRd16SgHK0A1Ts"
    // }
    // ======================= How to create &lt;signed_data&gt; =======================
    // payload = {
    // "custom_data": {
    // // Start customer_flag fields
    // "reserved_verified_customer": {
    // "label": "LABEL 1",
    // "value": true
    // },
    // "reserved_bad_actor": {
    // "label": "LABEL 2",
    // "value": false
    // },
    // "reserved_repeat_customer": {
    // "label": "LABEL 3",
    // "value": true
    // },
    // // End customer_flag fields
    // "field1": {
    // "label": "LABEL 4",
    // "value": "dummy1"
    // },
    // "field2": {
    // "label": "LABEL 5",
    // "value": "dummy2"
    // }
    // },
    // "exp": 1734567890, // expiration timestamp
    // "iat": 1734560000 // issue timestamp
    // }
    // signed_data = JWT.encode(payload, 'Company secret', 'HS256')
    // ======================= End how to create &lt;signed_data&gt; =======================
    

## Update end-user during ongoing chat session

Update the end-user associated with the current active chat session. Additionally, it also updates the contact information linked to the CRM ticket. `_Identifier` is required, while `name`, `email`, and `phone` are optional.

**Note:** If a phone number is already set, providing a phone parameter won't update the phone number.

### Example request

Method: `POST`

URL: `https://{subdomain}.{domain}/apps/api/v1/chats/:chat_id/end-user`

#### Headers

Key  | Value  | Description   
---|---|---  
Content-Type  | application/json  |   
  
#### URL variables

Key  | Value  | Description   
---|---|---  
chat_id  | integer  |   
  
#### Body
    
    
    {
        "identifier": "string",
        "name": "string",
        "email": "string",
        "phone": "string"
    }
    

### Example response
    
    
    {
        "message": "accepted"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
