---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient
title: Class UserListServiceClient (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:35.334667+00:00
---

# Class UserListServiceClient (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UserListServiceClient (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-datamanager/data-manager/src/main/java/com/google/ads/datamanager/v1/UserListServiceClient.java)| [Product Reference](https://developers.google.com/data-manager)| [RPC Documentation](https://developers.google.com/data-manager/api/reference/rpc)  
---|---|---  
  
Service Description: Service for managing UserList resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       UserListName name = UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]");
       UserList response = userListServiceClient.getUserList(name);
     }
     

Note: close() needs to be called on the UserListServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetUserList |  Gets a UserList.  Authorization Headers:  This method supports the following optional headers to define how the API authorizes access for the request: 

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUserList(GetUserListRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUserList(UserListName name) 
  * getUserList(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUserListCallable() 

  
ListUserLists |  Lists UserLists.  Authorization Headers:  This method supports the following optional headers to define how the API authorizes access for the request: 

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUserLists(ListUserListsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUserLists(AccountName parent) 
  * listUserLists(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUserListsPagedCallable() 
  * listUserListsCallable() 

  
CreateUserList |  Creates a UserList.  Authorization Headers:  This method supports the following optional headers to define how the API authorizes access for the request: 

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUserList(CreateUserListRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUserList(AccountName parent, UserList userList) 
  * createUserList(String parent, UserList userList) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUserListCallable() 

  
UpdateUserList |  Updates a UserList.  Authorization Headers:  This method supports the following optional headers to define how the API authorizes access for the request: 

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUserList(UpdateUserListRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUserList(UserList userList, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUserListCallable() 

  
DeleteUserList |  Deletes a UserList.  Authorization Headers:  This method supports the following optional headers to define how the API authorizes access for the request: 

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUserList(DeleteUserListRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUserList(UserListName name) 
  * deleteUserList(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUserListCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of UserListServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserListServiceSettings userListServiceSettings =
         UserListServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     UserListServiceClient userListServiceClient =
         UserListServiceClient.create(userListServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserListServiceSettings userListServiceSettings =
         UserListServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     UserListServiceClient userListServiceClient =
         UserListServiceClient.create(userListServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserListServiceSettings userListServiceSettings =
         UserListServiceSettings.newHttpJsonBuilder().build();
     UserListServiceClient userListServiceClient =
         UserListServiceClient.create(userListServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UserListServiceClient

## Static Methods 

### create()
    
    
    public static final UserListServiceClient create()

Constructs an instance of UserListServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[UserListServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UserListServiceSettings settings)
    
    
    public static final UserListServiceClient create(UserListServiceSettings settings)

Constructs an instance of UserListServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UserListServiceSettings](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserListServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UserListServiceStub stub)
    
    
    public static final UserListServiceClient create(UserListServiceStub stub)

Constructs an instance of UserListServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(UserListServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UserListServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.UserListServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserListServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient)` |   
  
## Constructors 

### UserListServiceClient(UserListServiceSettings settings)
    
    
    protected UserListServiceClient(UserListServiceSettings settings)

Constructs an instance of UserListServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UserListServiceSettings](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceSettings)`  
  
  
### UserListServiceClient(UserListServiceStub stub)
    
    
    protected UserListServiceClient(UserListServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UserListServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.UserListServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### createUserList(@Nullable AccountName parent, UserList userList)
    
    
    public final UserList createUserList(@Nullable AccountName parent, UserList userList)

Creates a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       AccountName parent = AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]");
       UserList userList = UserList.newBuilder().build();
       UserList response = userListServiceClient.createUserList(parent, userList);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.datamanager.v1.AccountName`  
Required. The parent account where this user list will be created. Format: accountTypes/{account_type}/accounts/{account}  
`userList` | `[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)`  
Required. The user list to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### createUserList(CreateUserListRequest request)
    
    
    public final UserList createUserList(CreateUserListRequest request)

Creates a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       CreateUserListRequest request =
           CreateUserListRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]").toString())
               .setUserList(UserList.newBuilder().build())
               .setValidateOnly(true)
               .build();
       UserList response = userListServiceClient.createUserList(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.CreateUserListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### createUserList(String parent, UserList userList)
    
    
    public final UserList createUserList(String parent, UserList userList)

Creates a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       String parent = AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]").toString();
       UserList userList = UserList.newBuilder().build();
       UserList response = userListServiceClient.createUserList(parent, userList);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent account where this user list will be created. Format: accountTypes/{account_type}/accounts/{account}  
`userList` | `[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)`  
Required. The user list to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### createUserListCallable()
    
    
    public final UnaryCallable<CreateUserListRequest,UserList> createUserListCallable()

Creates a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       CreateUserListRequest request =
           CreateUserListRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]").toString())
               .setUserList(UserList.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<UserList> future =
           userListServiceClient.createUserListCallable().futureCall(request);
       // Do something.
       UserList response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.CreateUserListRequest),[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)>` |   
  
### deleteUserList(@Nullable UserListName name)
    
    
    public final void deleteUserList(@Nullable UserListName name)

Deletes a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       UserListName name = UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]");
       userListServiceClient.deleteUserList(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.datamanager.v1.UserListName`  
Required. The name of the user list to delete. Format: accountTypes/{account_type}/accounts/{account}/userLists/{user_list}  
  
### deleteUserList(DeleteUserListRequest request)
    
    
    public final void deleteUserList(DeleteUserListRequest request)

Deletes a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       DeleteUserListRequest request =
           DeleteUserListRequest.newBuilder()
               .setName(UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]").toString())
               .setValidateOnly(true)
               .build();
       userListServiceClient.deleteUserList(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.DeleteUserListRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUserList(String name)
    
    
    public final void deleteUserList(String name)

Deletes a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       String name = UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]").toString();
       userListServiceClient.deleteUserList(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the user list to delete. Format: accountTypes/{account_type}/accounts/{account}/userLists/{user_list}  
  
### deleteUserListCallable()
    
    
    public final UnaryCallable<DeleteUserListRequest,Empty> deleteUserListCallable()

Deletes a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       DeleteUserListRequest request =
           DeleteUserListRequest.newBuilder()
               .setName(UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]").toString())
               .setValidateOnly(true)
               .build();
       ApiFuture<Empty> future = userListServiceClient.deleteUserListCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.DeleteUserListRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getSettings()
    
    
    public final @Nullable UserListServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.datamanager.v1.UserListServiceSettings` |   
  
### getStub()
    
    
    public UserListServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[UserListServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.UserListServiceStub)` |   
  
### getUserList(@Nullable UserListName name)
    
    
    public final UserList getUserList(@Nullable UserListName name)

Gets a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       UserListName name = UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]");
       UserList response = userListServiceClient.getUserList(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.datamanager.v1.UserListName`  
Required. The resource name of the UserList to retrieve. Format: accountTypes/{account_type}/accounts/{account}/userLists/{user_list}  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### getUserList(GetUserListRequest request)
    
    
    public final UserList getUserList(GetUserListRequest request)

Gets a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       GetUserListRequest request =
           GetUserListRequest.newBuilder()
               .setName(UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]").toString())
               .build();
       UserList response = userListServiceClient.getUserList(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.GetUserListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### getUserList(String name)
    
    
    public final UserList getUserList(String name)

Gets a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       String name = UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]").toString();
       UserList response = userListServiceClient.getUserList(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the UserList to retrieve. Format: accountTypes/{account_type}/accounts/{account}/userLists/{user_list}  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### getUserListCallable()
    
    
    public final UnaryCallable<GetUserListRequest,UserList> getUserListCallable()

Gets a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       GetUserListRequest request =
           GetUserListRequest.newBuilder()
               .setName(UserListName.of("[ACCOUNT_TYPE]", "[ACCOUNT]", "[USER_LIST]").toString())
               .build();
       ApiFuture<UserList> future = userListServiceClient.getUserListCallable().futureCall(request);
       // Do something.
       UserList response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.GetUserListRequest),[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listUserLists(@Nullable AccountName parent)
    
    
    public final UserListServiceClient.ListUserListsPagedResponse listUserLists(@Nullable AccountName parent)

Lists UserLists.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       AccountName parent = AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]");
       for (UserList element : userListServiceClient.listUserLists(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.datamanager.v1.AccountName`  
Required. The parent account which owns this collection of user lists. Format: accountTypes/{account_type}/accounts/{account}  
**Returns**  
---  
**Type** | **Description**  
`[UserListServiceClient.ListUserListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient.ListUserListsPagedResponse)` |   
  
### listUserLists(ListUserListsRequest request)
    
    
    public final UserListServiceClient.ListUserListsPagedResponse listUserLists(ListUserListsRequest request)

Lists UserLists.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       ListUserListsRequest request =
           ListUserListsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (UserList element : userListServiceClient.listUserLists(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserListsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserListServiceClient.ListUserListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient.ListUserListsPagedResponse)` |   
  
### listUserLists(String parent)
    
    
    public final UserListServiceClient.ListUserListsPagedResponse listUserLists(String parent)

Lists UserLists.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       String parent = AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]").toString();
       for (UserList element : userListServiceClient.listUserLists(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent account which owns this collection of user lists. Format: accountTypes/{account_type}/accounts/{account}  
**Returns**  
---  
**Type** | **Description**  
`[UserListServiceClient.ListUserListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient.ListUserListsPagedResponse)` |   
  
### listUserListsCallable()
    
    
    public final UnaryCallable<ListUserListsRequest,ListUserListsResponse> listUserListsCallable()

Lists UserLists.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       ListUserListsRequest request =
           ListUserListsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListUserListsResponse response =
             userListServiceClient.listUserListsCallable().call(request);
         for (UserList element : response.getUserListsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserListsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListsRequest),[ListUserListsResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListsResponse)>` |   
  
### listUserListsPagedCallable()
    
    
    public final UnaryCallable<ListUserListsRequest,UserListServiceClient.ListUserListsPagedResponse> listUserListsPagedCallable()

Lists UserLists.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       ListUserListsRequest request =
           ListUserListsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT_TYPE]", "[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<UserList> future =
           userListServiceClient.listUserListsPagedCallable().futureCall(request);
       // Do something.
       for (UserList element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserListsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListsRequest),[ListUserListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListServiceClient.ListUserListsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateUserList(UpdateUserListRequest request)
    
    
    public final UserList updateUserList(UpdateUserListRequest request)

Updates a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       UpdateUserListRequest request =
           UpdateUserListRequest.newBuilder()
               .setUserList(UserList.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       UserList response = userListServiceClient.updateUserList(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UpdateUserListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### updateUserList(UserList userList, FieldMask updateMask)
    
    
    public final UserList updateUserList(UserList userList, FieldMask updateMask)

Updates a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       UserList userList = UserList.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       UserList response = userListServiceClient.updateUserList(userList, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`userList` | `[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)`  
Required. The user list to update. The user list's `name` field is used to identify the user list to update. Format: accountTypes/{account_type}/accounts/{account}/userLists/{user_list}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)` |   
  
### updateUserListCallable()
    
    
    public final UnaryCallable<UpdateUserListRequest,UserList> updateUserListCallable()

Updates a UserList.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserListServiceClient userListServiceClient = UserListServiceClient.create()) {
       UpdateUserListRequest request =
           UpdateUserListRequest.newBuilder()
               .setUserList(UserList.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<UserList> future =
           userListServiceClient.updateUserListCallable().futureCall(request);
       // Do something.
       UserList response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUserListRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UpdateUserListRequest),[UserList](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserList)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
