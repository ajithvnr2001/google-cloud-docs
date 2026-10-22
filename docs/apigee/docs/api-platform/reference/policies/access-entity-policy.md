---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy/
title: AccessEntity policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:38.441183+00:00
---

# AccessEntity policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  AccessEntity policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The AccessEntity policy retrieves entity profiles you specify from the Apigee data store. The policy places the profile in a variable whose name follows the format `AccessEntity.{policy_name}`. You can use `AccessEntity` to access profiles for the following entities:

  * App
  * API product
  * Consumer key
  * Developer

**Note:** Apigee keeps the entities in cache for a minimum of 180 seconds after the entities are _accessed_.

The `AccessEntity` policy functions as a policy-based runtime database lookup. You can use the profile information returned by this policy to enable dynamic behavior, such as conditional endpoint routing, flow execution, policy enforcement.

Use the `AccessEntity` policy to get entity profile data **as XML** (or JSON in Apigee hybrid) and put it into a variable. Identify the entity to get by specifying an entity type and one or more identifiers that specify which entity of that type you want. Later, in another policy, you can retrieve the entity profile data with another policy, such as an [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) or [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** For XML examples representing entity profiles, see Example entity profile XML.

### Access AppGroups entities from `AccessEntity`

You can also use `AccessEntity` to retrieve AppGroup entities. See Supported entity types and identifiers for related entities.

For information about AppGroups and supported functionality, see [Using AppGroups to organize app ownership](https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership#using-appgroups-to-organize-app-ownership).

### Samples

The following samples show `AccessEntity` used in conjunction with the `ExtractVariables` and `AssignMessage` policies to extract a developer's email and add it to the HTTP header.

### Getting developer email for use in other policies

**Set up the`AccessEntity` policy to specify which entity profile to get from Apigee, as well as where to put the profile data.**

In the following example the policy gets a `developer` entity profile, using an API key passed as a query param to identify the developer. The profile is placed in a variable whose name follows the form `AccessEntity.{policy_name}`. So the variable set by this policy would be `AccessEntity.GetDeveloperProfile`.
    
    
    <AccessEntity name="GetDeveloperProfile">
      <!-- This is the type entity whose profile we need to pull from the Apigee datastore. -->
      <EntityType  value="developer"/>
      <!-- We tell the policy to use the API key (presented as query parameter) to identify the developer. -->
      <EntityIdentifier ref="request.queryparam.apikey" type="consumerkey"/>
    </AccessEntity>

**Use another policy to retrieve the entity profile value from the variable set by`AccessEntity`.**

In the following example, an `ExtractVariables` policy retrieves a value from the `AccessEntity.GetDeveloperProfile` variable set earlier by `AccessEntity`.

Note that the value retrieved is specified as an XPath expression in the `XMLPayload` element. The extracted value is placed in a `developer.email` variable.
    
    
    <ExtractVariables name="SetDeveloperProfile">
      <!-- The source element points to the variable populated by AccessEntity policy.
      The format is <policy-type>.<policy-name>.
      In this case, the variable contains the whole developer profile. -->
      <Source>AccessEntity.GetDeveloperProfile</Source>
      <VariablePrefix>developer</VariablePrefix>
      <XMLPayload>
        <Variable name="email" type="string">
            <!-- You parse elements from the developer profile using XPath. -->
          <XPath>/Developer/Email</XPath>
        </Variable>
      </XMLPayload>
    </ExtractVariables>

The following [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) retrieves the developer email set by the [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy).
    
    
    <!-- We'll use this policy to return the variables set in the developer profile,
    just so that we can easily see them in the response. -->
    <AssignMessage name="EchoVariables">
      <AssignTo createNew="false" type="response"></AssignTo>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <Set>
        <Headers>
          <Header name="X-Developer-email">{developer.email}</Header>
        </Headers>
      </Set>
    </AssignMessage>

* * *

## Element reference

The basic of structure of an `AccessEntity` policy is:
    
    
    <AccessEntity name="policy_name">
      <EntityType  value="entity_type"/>
      <EntityIdentifier ref="entity_identifier" type="identifier_type"/>
      <SecondaryIdentifier ref="secondary_identifier" type="identifier_type"/>
    </AccessEntity>

You can access multiple entities of the same type by grouping them in an `Identifiers` element:
    
    
    <AccessEntity name="name_of_the_policy">
      <EntityType  value="type_of_entity"/>
      <Identifiers>
        <Identifier>
          <EntityIdentifier ref="reference_to_entity_identifier" type*="identifier_type"/>
          <SecondaryIdentifier ref="reference_to_secondary_entity_identifier" type="identifier_type"/><!-- optional -->
        </Identifier >
        <Identifier>
          <EntityIdentifier ref="reference_to_entity_identifier" type*="identifier_type"/>
          <SecondaryIdentifier ref="reference_to_secondary_entity_identifier" type="identifier_type"/><!-- optional -->
        </Identifier >
      </Identifiers>
    </AccessEntity>

## <AccessEntity> attributes
    
    
    <AccessEntity async="false" continueOnError="false" enabled="true" name="policy_name">

The following table describes attributes that are common to all policy parent elements:

Attribute | Description | Default | Presence  
---|---|---|---  
`name` |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
`continueOnError` |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also:

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

| false | Optional  
`enabled` |  Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
`async` |  This attribute is deprecated. | false | Deprecated  
  
## <DisplayName> element

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, natural-language name.
    
    
    <DisplayName>Policy Display Name</DisplayName>

Default |  N/A If you omit this element, the value of the policy's `name` attribute is used.  
---|---  
Presence | Optional  
Type | String  
  
## <EntityIdentifier> element

Specifies the particular entity -- of the type given in EntityType -- to get.
    
    
    <EntityIdentifier ref="value_variable" type="identifier_type"/>

Default | N/A  
---|---  
Presence | Required  
Type | String  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
ref |  The variable that provides the source of the identifier, such as `request.queryparam.apikey`. | N/A | Required | String  
type | The type populated by the variable in the ref attribute. such as `consumerkey`. See Supported entity types and identifiers for a list of values. |  | Required | String  
  
### Example
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AccessEntity async="false" continueOnError="false" enabled="true" name="GetAPIProduct">
        <DisplayName>GetAPIProduct</DisplayName>
        <EntityType value="apiproduct"></EntityType>
        <EntityIdentifier ref="developer.app.name" type="appname"/>
        <SecondaryIdentifier ref="developer.id" type="developerid"/>
    </AccessEntity>

## <EntityType> element

Specifies the type of entity to retrieve from the data store.
    
    
    <EntityType  value="entity_type"/>

Default | N/A  
---|---  
Presence | Required  
Type | String  
  
Use an `EntityIdentifier` element to specify which entity of the given type you want. For a reference of entity types, see Supported entity types and identifiers.

### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
value | One of the supported entity types. See Supported entity types and identifiers for a list. | None | Required | String  
  
## <OutputFormat> element

**Note:** `<OutputFormat>` is available in hybrid only, beginning with hybrid v1.4. 

Specifies which format the AccessEntity policy returns: XML or JSON.
    
    
    <OutputFormat>XML</OutputFormat>

Default |  XML If you omit this element, the value defaults to XML.  
---|---  
Presence | Optional  
Type | String (XML or JSON)  
  
## <SecondaryIdentifier> element

In conjunction with `EntityIdentifier`, specifies a value to identify the desired instance of the given `EntityType`.
    
    
    <SecondaryIdentifier ref="value_variable" type="identifier_type"/>

Default | N/A  
---|---  
Presence | Optional  
Type | String  
  
Use `SecondaryIdentifier` when specifying only an `EntityIdentifier` will not guarantee that you get a single entity. See Narrowing results with secondary identifiers for more information.

Using multiple `SecondaryIdentifier` elements is not supported.

### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
ref |  The variable that provides the source of the identifier, such as `request.queryparam.apikey`. | N/A | Required | String  
type | The type populated by the variable in the ref attribute. such as `consumerkey`. See Supported entity types and identifiers for a list of values. |  | Required | String  
  
### Example
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AccessEntity async="false" continueOnError="false" enabled="true" name="GetAPIProduct">
        <DisplayName>GetAPIProduct</DisplayName>
        <EntityType value="apiproduct"></EntityType>
        <EntityIdentifier ref="developer.app.name" type="appname"/>
        <SecondaryIdentifier ref="developer.id" type="developerid"/>
    </AccessEntity>

## Usage notes

### Narrowing results with secondary identifiers

For some entities, giving one identifier might not be specific enough to get the entity you want. In those cases, you can use a secondary identifier to narrow the results.

**Note:** Where multiple matches exist for a given `EntityIdentifier` and `SecondaryIdentifier` combination, the first match will be populated in the flow. For example, consider a case in which you're wanting to get an API product profile by using an app ID.

Your first, possibly broad policy configuration might look like this:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AccessEntity async="false" continueOnError="false" enabled="true" name="GetApp">
        <DisplayName>GetAppProfile</DisplayName>
        <EntityType value="apiproduct"></EntityType>
        <EntityIdentifier ref="request.queryparam.apikey" type="consumerkey"/>
    </AccessEntity>

Because an app can be associated with multiple API products, using just the app ID might not return the API product you want (you could get just the first of multiple matched products).

Instead, to get a more exact result, you could use a `SecondaryIdentifier`. For example, you might have `appname` and `developerid` variables in the flow because these are populated by default during an OAuth 2.0 exchange. You could use the values of those variables in an `AccessEntity` policy to get profile details on the requesting app.

Your more specific policy configuration might look like this:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AccessEntity async="false" continueOnError="false" enabled="true" name="GetApp">
        <DisplayName>GetAppProfile</DisplayName>
        <EntityType value="apiproduct"></EntityType>
        <EntityIdentifier ref="developer.app.name" type="appname"/>
        <SecondaryIdentifier ref="developer.id" type="developerid"/>
    </AccessEntity>

### Supported entity types and identifiers

`AccessEntity` supports the following entity types and identifiers.

EntityType value | EntityIdentifier types | SecondaryIdentifier types  
---|---|---  
`apiproduct` | `appid` | `apiresource`  
`apiproductname` |   
`appname` | `apiresource`  
`developeremail`  
`developerid`  
`appgroupname`  
`consumerkey` | `apiresource`  
`app` | `appid` |   
`appname` | `developeremail`  
`developerid`  
`appgroupname`  
`consumerkey` |   
`authorizationcode` | `authorizationcode` |   
`appgroupname` | `appid`  
`appgroupname`  
`consumerkey` |   
`consumerkey` |   
`consumerkey` | `consumerkey` |   
`consumerkey_scope` | `consumerkey` |   
`developer` | `appid` |   
`consumerkey` |   
`developeremail` |   
`developerid` |   
`requesttoken` | `requesttoken` | `consumerkey`  
`verifier` | `verifier` |   
  
### Example entity profile XML

To retrieve the entity profile value you want with XPath, you'll need to know something about the profile XML's structure. For an example of the structure, use a Apigee API call to get XML for the entity you want. For details, refer to the [Apigee API reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).

The following sections include code for API calls, along with example XML from the call.

#### Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /apps/**$APP** \
      -X GET \
      -H "Accept:text/xml" \
      -H "Authorization: Bearer $TOKEN"
    

See also [Get app by app ID](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps/get) in the Apigee API reference.

Or:
    
    
    $ curl https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /apps/**$APP** \
      -X GET \
      -H "Accept:text/xml" \
      -H "Authorization: Bearer $TOKEN"
    

See also [Get developer app details](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/get) in the Apigee API reference.

Sample profile:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <App name="thomas-app">
        <AccessType>read</AccessType>
        <ApiProducts/>
        <Credentials>
            <Credential>
                <Attributes/>
                <ConsumerKey>wrqOOOiPArFI0WRoB1gAJMRbOguekJ5w</ConsumerKey>
                <ConsumerSecret>WvOhDrJ8m6kzz7Ni</ConsumerSecret>
                <ApiProducts>
                    <ApiProduct>
                        <Name>FreeProduct</Name>
                        <Status>approved</Status>
                    </ApiProduct>
                </ApiProducts>
                <Scopes/>
                <Status>approved</Status>
            </Credential>
        </Credentials>
        <AppFamily>default</AppFamily>
        <AppId>ab308c13-bc99-4c50-8434-0e0ed1b86075</AppId>
        <Attributes>
            <Attribute>
                <Name>DisplayName</Name>
                <Value>Tom's Weather App</Value>
            </Attribute>
        </Attributes>
        <CallbackUrl>http://tom.app/login</CallbackUrl>
        <CreatedAt>1362502872727</CreatedAt>
        <CreatedBy>admin@apigee.com</CreatedBy>
        <DeveloperId>PFK8IwOeAOW01JKA</DeveloperId>
        <LastModifiedAt>1362502872727</LastModifiedAt>
        <LastModifiedBy>admin@apigee.com</LastModifiedBy>
        <Scopes/>
        <Status>approved</Status>
    </App>

#### API product
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** \
      -X GET \
      -H "Accept:text/xml" \
      -H "Authorization: Bearer $TOKEN"
    

See also [Get API product](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/get) in the Apigee API reference.

Sample XPath, retrieves the second API resource (URI) from the API product named `weather_free`:
    
    
    /ApiProduct['@name=weather_free']/ApiResources/ApiResource[1]/text()

Sample profile returned as XML:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ApiProduct name="weather_free">
        <ApiResources>
            <ApiResource>/forecastrss, /reports</ApiResource>
        </ApiResources>
        <ApprovalType>auto</ApprovalType>
        <Attributes>
            <Attribute>
                <Name>description</Name>
                <Value>Introductory API Product</Value>
            </Attribute>
            <Attribute>
                <Name>developer.quota.interval</Name>
                <Value>1</Value>
            </Attribute>
            <Attribute>
                <Name>developer.quota.limit</Name>
                <Value>1</Value>
            </Attribute>
            <Attribute>
                <Name>developer.quota.timeunit</Name>
                <Value>minute</Value>
            </Attribute>
            <Attribute>
                <Name>servicePlan</Name>
                <Value>Introductory</Value>
            </Attribute>
        </Attributes>
        <CreatedAt>1355847839224</CreatedAt>
        <CreatedBy>andrew@apigee.com</CreatedBy>
        <Description>Free API Product</Description>
        <DisplayName>Free API Product</DisplayName>
        <Environments/>
        <LastModifiedAt>1355847839224</LastModifiedAt>
        <LastModifiedBy>andrew@apigee.com</LastModifiedBy>
        <Proxies/>
        <Scopes/>
    </ApiProduct>

#### Consumer key
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** developers/**$DEVELOPER_EMAIL** /apps/**$APP** /keys/**$KEY** \
      -X GET \
      -H "Accept:text/xml" \
      -H "Authorization: Bearer $TOKEN"
    

See also [ Get key details for a developer app](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/get) in the Apigee API reference.

Sample XPath:
    
    
    /Credential/ApiProducts/ApiProduct[Name='weather_free']/Status/text()

Sample profile:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Credential>
        <Attributes/>
        <ConsumerKey>XLotL3PRxNkUGXhGAFDPOr6fqtvAhuZe</ConsumerKey>
        <ConsumerSecret>iNUyEaOOh96KR3YL</ConsumerSecret>
        <ApiProducts>
            <ApiProduct>
                <Name>weather_free</Name>
                <Status>approved</Status>
            </ApiProduct>
        </ApiProducts>
        <Scopes/>
        <Status>approved</Status>
    </Credential>

#### Developer
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** developers/**$DEVELOPER_EMAIL** \
      -X GET \
      -H "Accept:text/xml" \
      -H "Authorization: Bearer $TOKEN"
    

See also [Get developer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/get) in the Apigee API reference.

Sample XPath:
    
    
    /Developer/Attributes/Attribute[Name='my_custom_attribute']/Value/text()
    
    
    /Developer/Email/text()

Sample profile:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Developer>
        <Apps>
            <App>weatherappx</App>
            <App>weatherapp</App>
        </Apps>
        <Email>ntesla@theramin.com</Email>
        <DeveloperId>4Y4xd0KRZ1wmHJqu</DeveloperId>
        <FirstName>Nikola</FirstName>
        <LastName>Tesla</LastName>
        <UserName>theramin</UserName>
        <OrganizationName>apigee-pm</OrganizationName>
        <Status>active</Status>
        <Attributes>
            <Attribute>
                <Name>project_type</Name>
                <Value>public</Value>
            </Attribute>
        </Attributes>
        <CreatedAt>1349797040634</CreatedAt>
        <CreatedBy>rsaha@apigee.com</CreatedBy>
        <LastModifiedAt>1349797040634</LastModifiedAt>
        <LastModifiedBy>rsaha@apigee.com</LastModifiedBy>
    </Developer>

* * *

## Flow variables

When the entity profile specified in the `AccessEntity` policy is retrieved, the profile object is added to the message context as a variable. It can be accessed like any other variable, with reference to the variable name. The user-provided name of the `AccessEntity` policy is set as the variable prefix of the variable name.

For example, if an `AccessEntity` policy with name of `GetDeveloper` is executed, then the profile is stored in the variable named `AccessEntity.GetDeveloper`. The profile can then be parsed using an XPath defined in an ExtractVariables policy that specifies `AccessEntity.GetDeveloper` as its source.

## Error reference

For related information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

None.

### Deployment errors

Error name | Fault string | HTTP status | Occurs when  
---|---|---|---  
`InvalidEntityType` | `Invalid type [entity_type] in ACCESSENTITYStepDefinition [policy_name]` | N/A | The entity type used must be one of the [supported types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy#Entities).  
  
## Related topics

  * `ExtractVariables`: [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy)
  * `AssignMessage`: [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
