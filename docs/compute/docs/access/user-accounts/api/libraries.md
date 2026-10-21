---
url: https://docs.cloud.google.com/compute/docs/access/user-accounts/api/libraries/
title: Cloud OS Login API \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:05.968494+00:00
---

# Cloud OS Login API  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/user-accounts/api/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Cloud OS Login API Stay organized with collections  Save and categorize content based on your preferences. 

You can use OS Login to manage access to your VM instances using IAM roles.

  * REST Resource: v1beta.projects.locations
  * REST Resource: v1beta.users
  * REST Resource: v1beta.users.projects
  * REST Resource: v1beta.users.projects.locations
  * REST Resource: v1beta.users.projects.zones
  * REST Resource: v1beta.users.sshPublicKeys
  * REST Resource: v1.projects.locations
  * REST Resource: v1.users
  * REST Resource: v1.users.projects
  * REST Resource: v1.users.sshPublicKeys



## Service: oslogin.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://oslogin.googleapis.com/$discovery/rest?version=v1>
  * <https://oslogin.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://oslogin.googleapis.com`



## REST Resource: [v1beta.projects.locations](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/projects.locations)

Methods  
---  
`[signSshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/projects.locations/signSshPublicKey)` |  `POST /v1beta/{parent=projects/*/locations/*}:signSshPublicKey`   
Signs an SSH public key for a user to authenticate to a virtual machine on Google Compute Engine.  
  
## REST Resource: [v1beta.users](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users)

Methods  
---  
`[getLoginProfile](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users/getLoginProfile)` |  `GET /v1beta/{name=users/*}/loginProfile`   
Retrieves the profile information used for logging in to a virtual machine on Google Compute Engine.  
`[importSshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users/importSshPublicKey)` |  `POST /v1beta/{parent=users/*}:importSshPublicKey`   
Adds an SSH public key and returns the profile information.  
  
## REST Resource: [v1beta.users.projects](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects)

Methods  
---  
`[delete](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects/delete)` |  `DELETE /v1beta/{name=users/*/projects/*}`   
Deletes a POSIX account.  
`[provisionPosixAccount](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects/provisionPosixAccount)` |  `POST /v1beta/{name=users/*/projects/*}`   
Create a POSIX account if it doesn't exist.  
  
## REST Resource: [v1beta.users.projects.locations](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects.locations)

Methods  
---  
`[signSshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects.locations/signSshPublicKey)` |  `POST /v1beta/{parent=users/*/projects/*/locations/*}:signSshPublicKey`   
Signs an SSH public key for a user to authenticate to an instance.  
  
## REST Resource: [v1beta.users.projects.zones](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects.zones)

Methods  
---  
`[signSshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects.zones/signSshPublicKey)` |  `POST /v1beta/{parent=users/*/projects/*/zones/*}:signSshPublicKey`   
Signs an SSH public key for a user to authenticate to an instance.  
  
## REST Resource: [v1beta.users.sshPublicKeys](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.sshPublicKeys)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.sshPublicKeys/create)` |  `POST /v1beta/{parent=users/*}/sshPublicKeys`   
Create an SSH public key  
`[delete](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.sshPublicKeys/delete)` |  `DELETE /v1beta/{name=users/*/sshPublicKeys/*}`   
Deletes an SSH public key.  
`[get](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.sshPublicKeys/get)` |  `GET /v1beta/{name=users/*/sshPublicKeys/*}`   
Retrieves an SSH public key.  
`[patch](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.sshPublicKeys/patch)` |  `PATCH /v1beta/{name=users/*/sshPublicKeys/*}`   
Updates an SSH public key and returns the profile information.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/projects.locations)

Methods  
---  
`[signSshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/projects.locations/signSshPublicKey)` |  `POST /v1/{parent=projects/*/locations/*}:signSshPublicKey`   
Signs an SSH public key for a user to authenticate to a virtual machine on Google Compute Engine.  
  
## REST Resource: [v1.users](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users)

Methods  
---  
`[getLoginProfile](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users/getLoginProfile)` |  `GET /v1/{name=users/*}/loginProfile`   
Retrieves the profile information used for logging in to a virtual machine on Google Compute Engine.  
`[importSshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users/importSshPublicKey)` |  `POST /v1/{parent=users/*}:importSshPublicKey`   
Adds an SSH public key and returns the profile information.  
  
## REST Resource: [v1.users.projects](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.projects)

Methods  
---  
`[delete](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.projects/delete)` |  `DELETE /v1/{name=users/*/projects/*}`   
Deletes a POSIX account.  
`[provisionPosixAccount](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.projects/provisionPosixAccount)` |  `POST /v1/{name=users/*/projects/*}`   
Adds a POSIX account and returns the profile information.  
  
## REST Resource: [v1.users.sshPublicKeys](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKeys)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKeys/create)` |  `POST /v1/{parent=users/*}/sshPublicKeys`   
Create an SSH public key  
`[delete](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKeys/delete)` |  `DELETE /v1/{name=users/*/sshPublicKeys/*}`   
Deletes an SSH public key.  
`[get](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKeys/get)` |  `GET /v1/{name=users/*/sshPublicKeys/*}`   
Retrieves an SSH public key.  
`[patch](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKeys/patch)` |  `PATCH /v1/{name=users/*/sshPublicKeys/*}`   
Updates an SSH public key and returns the profile information.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
