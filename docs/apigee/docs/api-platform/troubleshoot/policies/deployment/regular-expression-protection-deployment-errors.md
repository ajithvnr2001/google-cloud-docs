---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors/
title: Regular Expression Protection policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:28.903970+00:00
---

# Regular Expression Protection policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Regular Expression Protection policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors/).

## InvalidRegularExpression

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    RegularExpressionProtection policy_name: Invalid Regular Expression com.apigee.steps.regexprotection.RegularExpressionProtectionBean$RegexPattern@f4ecb23, Context Revision:revision_number;APIProxy:RegexThreat;Organization:organization;Environment:environment.

### Example Error Message
    
    
    Error Deploying Revision 1 to test
    RegularExpressionProtection Regular-Expression-Protection-1: Invalid Regular Expression com.apigee.steps.regexprotection.RegularExpressionProtectionBean$RegexPattern@f4ecb23, Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

### Example Error Screenshot

![InvalidRegularExpression error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidRegularExpression-rexp.png)

### Cause

If the regular expression in the `<Pattern>` element of the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) is not valid, then deployment of the API Proxy fails.

### Diagnosis

  1. Identify the name of the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) from the error message. For example, in the following error, the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) name is `Regular-Expression-Protection-1:`
         
         Error Deploying Revision 1 to test
         RegularExpressionProtection Regular-Expression-Protection-1: Invalid Regular Expression com.apigee.steps.regexprotection.RegularExpressionProtectionBean$RegexPattern@f4ecb23, Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

  2. Examine all the `<Pattern>` elements in the failed Regular Expression Protection policy XML. Check if any of the `<Pattern>` elements has an invalid regular expression. If any of the `<Pattern>` elements has invalid regular expression, then that's the cause of the error.

For example, the following policy specifies the value of `Pattern>` of `foo){2}`, which is considered Invalid Regular Expression: 
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
                 <DisplayName>Regular Expression Protection-1</DisplayName>
                 <Properties/>
                 <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
                 <URIPath>
                     <Pattern>foo){2}</Pattern>
                 </URIPath>
                 <Source>request</Source>
             </RegularExpressionProtection>

In the above example, the regular expression specified in the `<Pattern>` has a missing opening parentheses. Hence it is considered as an invalid regular expression. So the deployment of the API Proxy fails.




### Resolution

Ensure that each `<Pattern>` element in the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) contains a valid regular expression. You can search for different online or offline regex tools for debugging your regular expressions. To correct the example Regular Expression Protection policy shown above, add the missing parentheses:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
            <DisplayName>Regular Expression Protection-1</DisplayName>
            <Properties/>
            <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
            <URIPath>
                <Pattern>(foo){2}</Pattern>
            </URIPath>
            <Source>request</Source>
        </RegularExpressionProtection>

## XPathCompilationFailed

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    RegularExpressionProtection policy_name: Failed to compile xpath xpath_expression. Context Revision:revision_number;APIProxy:RegexThreat;Organization:organization;Environment:environment.

### Example Error Message
    
    
    Error Deploying Revision 1 to test
    RegularExpressionProtection Regular-Expression-Protection-1: Failed to compile xpath /notapigee:foo/notapigee:bar. Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

### Example Error Screenshot

![XPathCompilationFailed error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/XPathCompilationFailed-rexp.png)

### Cause

If the prefix or the value used in the `<XPath>` element is not part of any of the declared namespaces in the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection), then the deployment of the API proxy fails.

You can find more information about namespaces, XPath and prefix in [XML Namespaces and How They Affect XPath and XSLT](https://msdn.microsoft.com/en-us/library/ms950779.aspx).

### Diagnosis

  1. Identify the name of the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) where the error occurred and the XPath Expression that was used. You can find both of these items in the error message. 

For example, in the following error , the policy name is `Regular-Expression-Protection-1` and the XPath Expression is `/notapigee:foo/notapigee:bar:`
         
         Error Deploying Revision 1 to test
         RegularExpressionProtection Regular-Expression-Protection-1: Failed to compile xpath /notapigee:foo/notapigee:bar. Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

  2. In the failed Regular Expression Protection policy XML, verify that the XPath set in the `Expression` element matches the XPath identified in the error message (step #1 above). 

For example, the following policy specifies the XPath as `/notapigee:foo/notapigee:bar` which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
             <DisplayName>Regular Expression Protection-1</DisplayName>
             <Properties/>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <Source>request</Source>
              <XMLPayload>
                  <Namespaces>
                      <Namespace prefix="apigee">http://www.apigee.com</Namespace>
                  </Namespaces>
                  <XPath>
                      <Expression>/notapigee:foo/notapigee:bar</Expression>
                      <Type>nodeset</Type>
                      <Pattern>pattern</Pattern>
                      <Pattern>pattern2</Pattern>
                  </XPath>
              </XMLPayload>
         </RegularExpressionProtection>

  3. Examine the `<Namespaces>` and `<Expression>` elements in the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection). If the specific `<Expression>` indicated in the error message uses a prefix or value that is not part of the namespaces declared in the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection), then that is the cause of the error. 

Notice that the specific `<XPath>` uses the prefix `notapigee` in the example [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection):
         
         <Expression>/notapigee:foo/notapigee:bar</Expression>

However, the prefix `notapigee` is not defined in any of the `<Namespace>` elements; therefore, the compilation of `<XPath>` fails leading to deployment failure. 




### Resolution

Ensure all the namespaces that are being used in `<Expression>` elements under the `<XPath>` elements are declared in the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection). To fix the example above, you could replace `notapigee` prefix to `apigee`, which is declared in namespaces:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
        <DisplayName>Regular Expression Protection-1</DisplayName>
        <Properties/>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <Source>request</Source>
         <XMLPayload>
             <Namespaces>
                 <Namespace prefix="apigee">http://www.apigee.com</Namespace>
             </Namespaces>
             <XPath>
                 <Expression>/apigee:foo/apigee:bar</Expression>
                 <Type>nodeset</Type>
                 <Pattern>pattern</Pattern>
                 <Pattern>pattern2</Pattern>
             </XPath>
         </XMLPayload>
    </RegularExpressionProtection>

## CannotBeConvertedToNodeset

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    RegularExpressionProtection policy_name: Result of xpath xpath_expression cannot be converted to nodeset. Context Revision:revision_number;APIProxy:RegexThreat;Organization:organization;Environment:environment.

### Example Error Message
    
    
    Error Deploying Revision 1 to test
    RegularExpressionProtection Regular-Expression-Protection-1: Result of xpath count(//apigee:foo) cannot be converted to nodeset. Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

### Example Error Screenshot

![CannotBeConvertedToNodeset error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/CannotBeConvertedToNodeset-rexp.png)

### Cause

If the Regular Expression Policy has an `<XPath>` expression where the `<Type>` element is defined as [nodeset](https://docs.microsoft.com/en-us/dotnet/standard/data/xml/node-sets-in-transformations), but the expression cannot be converted to nodeset, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) where the error occurred and the XPath Expression that cannot be converted to nodeset. You can find both of these items in the error message. 

For example, in the following error , the policy name is `Regular-Expression-Protection-1` and the XPath Expression is `count(//apigee:foo):`
         
         Error Deploying Revision 1 to test
         RegularExpressionProtection Regular-Expression-Protection-1: Result of xpath count(//apigee:foo) cannot be converted to nodeset. Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

  2. In the failed Regular Expression Protection policy XML, verify that the XPath set in the `<Expression>` element of `<XPath>` element matches the XPath identified in the error message (step #1 above). 

For example, the following policy specifies the as `count(//apigee:foo)`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
                 <DisplayName>Regular Expression Protection-1</DisplayName>
                 <Properties/>
                 <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
                 <Source>request</Source>
                  <XMLPayload>
                      <Namespaces>
                          <Namespace prefix="apigee">http://www.apigee.com</Namespace>
                      </Namespaces>
                      <XPath>
                          <Expression>count(//apigee:foo)</Expression>
                          <Type>nodeset</Type>
                          <Pattern>pattern</Pattern>
                          <Pattern>pattern2</Pattern>
                      </XPath>
                  </XMLPayload>
             </RegularExpressionProtection>

  3. Examine the value set in the `<Type>` element underneath the `<XPath>` element. If the `<Type>` element is `nodeset`, then that's the cause of the error.

In this example, the XPath expression is _count()_ which doesn't return one or more nodes. So, the deployment of the API Proxy fails.




### Resolution

If the `<Type>` element is set to nodeset, ensure that the result of the `<Expression>` element set in `<XPath>` is one or more nodes. Alternatively, change the `<Type>` element to a more appropriate value based on your use-case. 

To fix the example above, you could change the `<Expression>` element to a different value that can return nodes:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
        <DisplayName>Regular Expression Protection-1</DisplayName>
        <Properties/>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <Source>request</Source>
         <XMLPayload>
             <Namespaces>
                 <Namespace prefix="apigee">http://www.apigee.com</Namespace>
             </Namespaces>
             <XPath>
                 <Expression>/apigee:foo/apigee:bar</Expression>
                 <Type>nodeset</Type>
                 <Pattern>pattern</Pattern>
                 <Pattern>pattern2</Pattern>
             </XPath>
         </XMLPayload>
    </RegularExpressionProtection>

## JSONPathCompilationFailed

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    RegularExpressionProtection policy_name: Failed to compile jsonpath jsonpath_expression Context Revision:revision_number;APIProxy:RegexThreat;Organization:organization;Environment:environment.

### Example Error Message
    
    
    Error Deploying Revision 1 to test
    RegularExpressionProtection Regular-Expression-Protection-1: Failed to compile jsonpath $.store.book[*.author. Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

### Example Error Screenshot

![JSONPathCompilationFailed error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/JSONPathCompilationFailed-rexp.png)

### Cause

If the `<Expression>` element under `<JSONPath>` element of a Regular Expression Protection policy is set to an invalid JSONPath expression, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the name of the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) where the error occurred and the invalid JSONPath Expression was used. You can find both of these items in the error message. 

For example, in the following error , the policy name is `Regular-Expression-Protection-1` and the JSONPath Expression is `$.store.book[*.author:`
         
         Error Deploying Revision 1 to test
         RegularExpressionProtection Regular-Expression-Protection-1: Failed to compile jsonpath $.store.book[*.author. Context Revision:1;APIProxy:RegexThreat;Organization:myorg;Environment:test.

  2. In the failed Regular Expression Protection policy XML, verify that the JSONPath set in the `Expression` element matches the JSONPath identified in the error message (step #1 above). 

For example, the following policy specifies the `Expression` element under `<JSONPath>` element as `$.store.book[*.author` which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
                 <DisplayName>Regular Expression Protection-1</DisplayName>
                 <Properties/>
                 <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
                 <Source>request</Source>
                 <JSONPayload>
                      <JSONPath>
                          <Expression>$.store.book[*.author</Expression>
                          <Pattern>REGEX PATTERN</Pattern>
                          <Pattern>REGEX PATTERN</Pattern>
                      </JSONPath>
                     </JSONPayload>
             </RegularExpressionProtection>

  3. Examine `<Expression>` element under `<JSONPath>` element in the policy. If it doesn't match JSONPath syntax, then this is the cause of the error. In the example above, the closing square bracket is missing, which makes the expression invalid. 

Since the JSON Path Expression is invalid, the deployment of the API Proxy fails.




### Resolution

Ensure that the value for the `<Expression>` element inside of the `<JSONPath>` element in Regular Expression Protection policy is a valid JSONPath expression. 

To correct the example shown above, you could add missing closing square bracket to `<Expression>` element value:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
        <DisplayName>Regular Expression Protection-1</DisplayName>
        <Properties/>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <Source>request</Source>
        <JSONPayload>
             <JSONPath>
                 <Expression>$.store.book[*].author</Expression>
                 <Pattern>REGEX PATTERN</Pattern>
                 <Pattern>REGEX PATTERN</Pattern>
             </JSONPath>
            </JSONPayload>
    </RegularExpressionProtection>

## NothingToEnforce

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    RegularExpressionProtection policy_name: at least one of URIPath, QueryParam, Header, FormParam, XMLPayload, JSONPayload is mandatory.

### Example Error Message
    
    
    Error Saving Revision 1
    RegularExpressionProtection Regular-Expression-Protection-1: at least one of URIPath, QueryParam, Header, FormParam, XMLPayload, JSONPayload is mandatory.

### Example Error Screenshot

![NothingToEnforce error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/NothingToEnforce-rexp.png)

### Cause

If the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) does not have any of the elements `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<XMLPayload>`, or `<JSONPayload>`, the deployment of the API Proxy fails.

As indicated in the error message, the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) must have at least one of these elements included within the policy: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<XMLPayload>`, or `<JSONPayload>`.

### Diagnosis

  1. Identify the name of the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) where the error occurred. You can find it in the error message. For example, in the following error , the policy name is `Regular-Expression-Protection-1:`
         
         RegularExpressionProtection Regular-Expression-Protection-1: at least one of URIPath, QueryParam, Header, FormParam, XMLPayload, JSONPayload is mandatory.

  2. Examine the failed Regular Expression Protection policy (identified in step #1 above). If the policy does not have even one of the following elements: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<XMLPayload>`, or `<JSONPayload>`, then that's the cause of the error. 

For example, the following Regular Expression Protection policy does not have any of the above mentioned elements:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
                 <DisplayName>Regular Expression Protection-1</DisplayName>
                 <Properties/>
                 <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
                 <Source>request</Source>
             </RegularExpressionProtection>

Since none of the mandatory elements are present in the Extract Variables policy, the deployment of the API proxy fails.




### Resolution

Ensure that the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) has at least one of these mandatory elements: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<XMLPayload>`, or `<JSONPayload>`. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
        <DisplayName>Regular Expression Protection-1</DisplayName>
        <Properties/>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <Source>request</Source>
        <JSONPayload>
            <JSONPath>
                <Expression>$.store.book[*].author</Expression>
                <Pattern>REGEX PATTERN</Pattern>
                <Pattern>REGEX PATTERN</Pattern>
            </JSONPath>
        </JSONPayload>
    </RegularExpressionProtection>

## NoPatternsToEnforce

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    RegularExpressionProtection policy_name: No patterns to enforce in payload_name.

### Example Error Message
    
    
    Error Saving Revision 1
    RegularExpressionProtection Regular-Expression-Protection-1: No patterns to enforce in XPath.

### Example Error Screenshot

![NoPatternsToEnforce error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/NoPatternsToEnforce-rexp.png)

### Cause

If any of the top level elements (`<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<XMLPayload>`, or `<JSONPayload>`) doesn't have `<Pattern>` element defined in the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection), then the deployment of the API proxy fails. 

### Diagnosis

  1. Identify the name of the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) where the error occurred and the child element which does not have the `<Pattern>` element. You can find both of these items in the error message. 

For example, in the following error, the policy name is `Regular-Expression-Protection-1` and the child element is `XPath:`
         
         RegularExpressionProtection Regular-Expression-Protection-1: No patterns to enforce in XPath.

  2. Examine the failing Regular Expression Protection policy and verify if the child element identified in step #1 does not have the `<Pattern>` element. If `<Pattern>` element doesn't exist in it, then that's the cause of the error. 

For example, the following policy doesn't have `<Pattern>` element inside of `<XPath>`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
               <DisplayName>Regular Expression Protection-1</DisplayName>
               <Properties/>
               <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
               <Source>request</Source>
               <XMLPayload>
                 <Namespaces>
                   <Namespace prefix="apigee">http://www.apigee.com</Namespace>
                 </Namespaces>
                 <XPath>
                   <Expression>/apigee:Greeting/apigee:User</Expression>
                   <Type>string</Type>
                 </XPath>
               </XMLPayload>
             </RegularExpressionProtection>

Since the `<XPath>` element does not have `<Pattern>` element, the deployment of the API Proxy fails.




### Resolution

Ensure that any of the elements `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<XMLPayload>`, or `<JSONPayload>` has at least one `<Pattern>` specified. See [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) for information on how to specify the element correctly. 

To fix example above we could just add the `<Pattern>` element to `<XPath>` element underneath `<XMLPayload>`:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
      <DisplayName>Regular Expression Protection-1</DisplayName>
      <Properties/>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
      <Source>request</Source>
      <XMLPayload>
        <Namespaces>
          <Namespace prefix="apigee">http://www.apigee.com</Namespace>
        </Namespaces>
        <XPath>
          <Expression>/apigee:Greeting/apigee:User</Expression>
          <Type>string</Type>
          <Pattern>REGEX PATTERN</Pattern>
        </XPath>
      </XMLPayload>
    </RegularExpressionProtection>

## NONEmptyPrefixMappedToEmptyURI

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    RegularExpressionProtection policy_name: Non-empty prefix prefix_name cannot be mapped to empty uri.

### Example Error Message
    
    
    Error Saving Revision 1
    RegularExpressionProtection Regular-Expression-Protection-1: Non-empty prefix apigee cannot be mapped to empty uri.

### Example Error Screenshot

![NONEmptyPrefixMappedToEmptyURI error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/NONEmptyPrefixMappedToEmptyURI-rexp.png)

### Cause

This error occurs if the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) has a prefix defined in the `<Namespace>` element under the `<XMLPayload>` element, but no URI is defined.

### Diagnosis

  1. Identify the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) where the error occurred and the name of the prefix which is not mapped to URI. You can find both of these items in the error message. 

For example, in the following error, the policy name is Regular Expression Protection-1 and the prefix is apigee:
         
         RegularExpressionProtection Regular-Expression-Protection-1: Non-empty prefix apigee cannot be mapped to empty uri.

  2. In the failed Regular Expression Protection policy XML, verify that the name of the prefix set in the `<Namespace>` element under the `<XMLPayload>` element matches the prefix name identified in the error message (step #1 above). 

For example, the following policy specifies a prefix named apigee in the `<Namespace>` element , which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
               <DisplayName>Regular Expression Protection-1</DisplayName>
               <Properties/>
               <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
               <Source>request</Source>
               <XMLPayload>
                 <Namespaces>
                   <Namespace prefix="apigee"/>
                   <Namespace prefix="gmail">http://mail.google.com</Namespace>
                 </Namespaces>
                 <XPath>
                   <Expression>/apigee:Greeting/apigee:User</Expression>
                   <Type>string</Type>
                   <Pattern>REGEX PATTERN</Pattern>
                 </XPath>
               </XMLPayload>
             </RegularExpressionProtection>

  3. Validate if the `<Namespace>` element with the specific prefix identified in step #2 has a valid URI. If the URI is missing, then that is the cause of the error.

In the example Regular Expression Protection policy shown above, notice that there's no URI corresponding to the `<Namespace>` element with the prefix apigee; therefore, you get the error:
         
         Non-empty prefix apigee cannot be mapped to empty uri.




### Resolution

Ensure that all the `<Namespace>` elements defined with a prefix have a corresponding URI in the Extract Variables policy. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
      <DisplayName>Regular Expression Protection-1</DisplayName>
      <Properties/>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
      <Source>request</Source>
      <XMLPayload>
        <Namespaces>
          <Namespace prefix="apigee">http://www.apigee.com</Namespace>
          <Namespace prefix="gmail">http://mail.google.com</Namespace>
        </Namespaces>
        <XPath>
          <Expression>/apigee:Greeting/apigee:User</Expression>
          <Type>string</Type>
          <Pattern>REGEX PATTERN</Pattern>
        </XPath>
      </XMLPayload>
    </RegularExpressionProtection>

## DuplicatePrefix

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    RegularExpressionProtection policy_name: Duplicate prefix prefix_name.

### Example Error Message
    
    
    Error Saving Revision 1
    RegularExpressionProtection Regular-Expression-Protection-1: Duplicate prefix apigee.

### Example Error Screenshot

![DuplicatePrefix error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/DuplicatePrefix-rexp.png)

### Cause

This error occurs if the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) has the same prefix defined more than once in the `<Namespace>` element under the `<XMLPayload>` element.

For example, this error occurs since the prefix apigee is defined twice as shown below: 
    
    
    <Namespace prefix="apigee">http://www.apigee.com</Namespace>
    <Namespace prefix="apigee">http://www.apigee.com</Namespace>

### Diagnosis

  1. Identify the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) where the error occurred and the name of the prefix. You can find both of these items in the error message. 

For example, in the following error, the policy name is Regular Expression Protection-1 and the prefix is apigee:
         
         RegularExpressionProtection Regular-Expression-Protection-1: Duplicate prefix apigee.

  2. In the failed Regular Expression Protection policy XML, verify that the name of the prefix set in the `<Namespace>` element under the `<XMLPayload>` element matches the prefix name identified in the error message (step #1 above). 

For example, the following policy specifies a prefix named apigee in the `<Namespace>` element , which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
               <DisplayName>Regular Expression Protection-1</DisplayName>
               <Properties/>
               <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
               <Source>request</Source>
               <XMLPayload>
                 <Namespaces>
                   <Namespace prefix="apigee">http://www.apigee.com</Namespace>
                   <Namespace prefix="apigee">http://www.apigee.com</Namespace>
                 </Namespaces>
                 <XPath>
                   <Expression>/apigee:Greeting/apigee:User</Expression>
                   <Type>string</Type>
                   <Pattern>REGEX PATTERN</Pattern>
                 </XPath>
               </XMLPayload>
             </RegularExpressionProtection>

  3. Determine if the `<Namespace>` element with the specific prefix, identified in step #2 has been defined more than once. If it is defined more than once, then that is the cause of the error.

In the example Regular Expression Protection policy shown above, notice that the `<Namespace>` element with the prefix apigee has been defined twice; therefore, you get the error:
         
         Duplicate prefix apigee.




### Resolution

Ensure that there is only one definition for each prefix in the `<Namespace>` elements in the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection). For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
          <DisplayName>Regular Expression Protection-1</DisplayName>
          <Properties/>
          <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
          <Source>request</Source>
          <XMLPayload>
            <Namespaces>
              <Namespace prefix="apigee">http://www.apigee.com</Namespace>
            </Namespaces>
            <XPath>
              <Expression>/apigee:Greeting/apigee:User</Expression>
              <Type>string</Type>
              <Pattern>REGEX PATTERN</Pattern>
            </XPath>
          </XMLPayload>
        </RegularExpressionProtection>

## EmptyXPathExpression

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    RegularExpressionProtection policy_name: Empty XPath expression.

### Example Error Message
    
    
    Error Saving Revision 1
    RegularExpressionProtection Regular-Expression-Protection-1: Empty XPath expression.

### Example Error Screenshot

![EmptyXPathExpression error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/EmptyXPathExpression-rexp.png)

### Cause

If the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) has no `<Expression>` element set within the `<XPath>` element, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the failed Regular Expression Protection policy from the error message. For example, in the following error, the policy name is Regular-Expression-Protection-1:
         
         RegularExpressionProtection Regular-Expression-Protection-1: Empty XPath expression.

  2. In the failed Regular Expression Protection policy XML, determine if there's an `<XMLPayload>` element with `<XPath>` child element that has no `<Expression>` element defined in it, or `<Expression>` element is not set to any value. If so, then that's the cause of the error.

For example, here's a Regular Expression Protection policy that has an `<XMLPayload>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
           <DisplayName>Regular Expression Protection-1</DisplayName>
           <Properties/>
           <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
           <Source>request</Source>
           <XMLPayload>
             <Namespaces>
               <Namespace prefix="apigee">http://www.apigee.com</Namespace>
             </Namespaces>
             <XPath>
               <Expression></Expression>
               <Type>string</Type>
               <Pattern>REGEX PATTERN</Pattern>
             </XPath>
           </XMLPayload>
         </RegularExpressionProtection>

Since there is an empty `<Expression>` element within the `<XPath>` element, the deployment of the API Proxy fails.




### Resolution

Ensure that the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) has a non-empty and valid `<Expression>` element defined under the `<XPath>` element. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
      <DisplayName>Regular Expression Protection-1</DisplayName>
      <Properties/>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
      <Source>request</Source>
      <XMLPayload>
        <Namespaces>
          <Namespace prefix="apigee">http://www.apigee.com</Namespace>
        </Namespaces>
        <XPath>
          <Expression>/apigee:Greeting/apigee:User</Expression>
          <Type>string</Type>
          <Pattern>REGEX PATTERN</Pattern>
        </XPath>
      </XMLPayload>
    </RegularExpressionProtection>

## EmptyJSONPathExpression

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    RegularExpressionProtection policy_name: Empty JSONPath expression.

### Example Error Message
    
    
    Error Saving Revision 1
    RegularExpressionProtection Regular-Expression-Protection-1: Empty JSONPath expression.

### Example Error Screenshot

![EmptyJSONPathExpression error text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/EmptyJSONPathExpression-rexp.png)

### Cause

If the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) has no `<Expression>` element set within the `<JSONPath>` element, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the failed Regular Expression Protection policy from the error message. For example, in the following error, the policy name is Regular-Expression-Protection-1:
         
         Error Saving Revision 1
         RegularExpressionProtection Regular-Expression-Protection-1: Empty JSONPath expression.

  2. In the failed Regular Expression Protection policy XML, determine if there's a `<JSONPayload>` element with `<JSONPath>` child element that has no `<Expression>` element defined in it, or `<Expression>` element is not set to any value. If so, then that's the cause of the error.

For example, here's a Regular Expression Protection policy that has a `<JSONPayload>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
               <DisplayName>Regular Expression Protection-1</DisplayName>
               <Properties/>
               <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
               <Source>request</Source>
               <JSONPayload>
                 <JSONPath>
                   <Expression></Expression>
                   <Pattern>REGEX PATTERN</Pattern>
                   <Pattern>REGEX PATTERN</Pattern>
                 </JSONPath>
               </JSONPayload>
             </RegularExpressionProtection>

Since there is an empty `<Expression>` element within the `<JSONPath>` element, the deployment of the API Proxy fails.




### Resolution

Ensure that the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) has a non-empty and valid `<Expression>` element defined under the `<JSONPath>` element. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name="Regular-Expression-Protection-1">
      <DisplayName>Regular Expression Protection-1</DisplayName>
      <Properties/>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
      <Source>request</Source>
      <JSONPayload>
        <JSONPath>
          <Expression>$.store.book[*].author</Expression>
          <Pattern>REGEX PATTERN</Pattern>
          <Pattern>REGEX PATTERN</Pattern>
        </JSONPath>
      </JSONPayload>
    </RegularExpressionProtection>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
