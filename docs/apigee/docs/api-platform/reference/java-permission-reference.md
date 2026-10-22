---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/java-permission-reference/
title: Java permission reference \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:59.267936+00:00
---

# Java permission reference  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/java-permission-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Java permission reference Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What you need to know about Java permission policies

If you are developing a JavaCallout policy, you need to know which permission policies are in effect in the Apigee JVM and how they will affect your code. For example, your custom Java code does not have unlimited access to the file system. However, in the case of file system access, you can read certain files, such as policy resource files. But most other file system access is blocked. This topic lists all of JDK permission types and their respective targets or actions. For each target or action, we specify the permission policy and any exceptions that you need to know about.

To learn more about the JDK permission types and what each permission allows, see [Permissions in the Java Development Kit (JDK)](https://docs.oracle.com/javase/8/docs/technotes/guides/security/permissions.html).

**Permission Type** | **Target or Action Name** | **Permission Granted**  
---|---|---  
java.awt.AWTPermission |  |   
accessClipboard | NO  
accessEventQueue | NO  
accessSystemTray | NO  
createRobot | NO  
fullScreenExclusive | NO  
listenToAllAWTEvents | NO  
readDisplayPixels | NO  
replaceKeyboardFocusManager | NO  
setAppletStub | NO  
setWindowsAlwaysOnTop | NO  
showWindowWithoutWarningBanner | NO  
toolkitModality | NO  
watchMousePointer | NO  
|  |   
java.io.FilePermission  
  
A java.io.FilePermission represents access to a file or directory. A FilePermission consists of a pathname and a set of actions valid for that pathname. | read | YES but restrictions apply. See [Restrictions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy#restrictions).  
|   
write | NO  
execute | NO  
delete | NO  
readLink | YES  
|  |   
java.io.SerializablePermission  
  
A SerializablePermission contains a name (also referred to as a "target name") but no actions list; you either have the named permission or you don't. | enableSubclassImplementation | YES  
enableSubstitution | NO  
|  |   
java.lang.management.ManagementPermission  
  
Methods defined in the management interface for the Java platform | control | NO  
monitor | NO  
|  |   
java.lang.reflect.ReflectPermission  
  
For reflective operations. A ReflectPermission is a named permission and has no actions | suppressAccessChecks | NO  
| newProxyInPackage.{package name} | NO  
|  |   
java.lang.RuntimePermission  
  
Contains a name (also referred to as a "target name") but no actions list; you either have the named permission or you don't.  
| createClassLoader | NO  
getClassLoader | YES  
setContextClassLoader | YES  
enableContextClassLoaderOverride | YES  
closeClassLoader | NO  
setSecurityManager | NO  
createSecurityManager | NO  
getenv.{variable name} | NO  
exitVM.{exit status} | NO  
shutdownHooks | NO  
setFactory | NO  
setIO | NO  
modifyThread | YES  
stopThread | YES  
modifyThreadGroup | YES  
getProtectionDomain | YES  
getFileSystemAttributes | NO  
readFileDescriptor | YES  
writeFileDescriptor | NO  
loadLibrary.{library name} | NO  
accessClassInPackage. {package name} | YES  
defineClassInPackage. {package name} | NO  
accessDeclaredMembers | NO   
queuePrintJob | NO  
getStackTrace | NO  
setDefaultUncaughtExceptionHandler | NO  
preferences | NO  
usePolicy | NO  
|  |   
java.net.NetPermission  
  
A NetPermission contains a name but no actions list; you either have the named permission or you don't. | setDefaultAuthenticator | NO  
requestPasswordAuthentication | NO  
specifyStreamHandler | YES  
setProxySelector | NO  
getProxySelector | NO  
setCookieHandler | NO  
getCookieHandler | NO  
setResponseCache | NO  
getResponseCache | NO  
| getNetworkInformation | NO  
|  |   
java.net.SocketPermission  
  
Represents access to a network via sockets. A SocketPermission consists of a host specification and a set of "actions" specifying ways to connect to that host.  
host = (hostname | IPaddress)[:portrange]  
portrange = portnumber | -portnumber | portnumber-[portnumber]  
  
The possible ways to connect to the host are  
  
accept  
connect  
listen  
resolve  
  
The "listen" action is only meaningful when used with "localhost". The "resolve" (resolve host/ip name service lookups) action is implied when any of the other actions are present. | resolve | YES  
connect |  YES but restrictions apply. See [Restrictions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy#restrictions). Apigee restricts access to sitelocal, anylocal, loopback, and linklocal addresses, as well as private IPv4 ranges defined in RFC1918.  
listen,  
accept | NO  
|  |   
java.net.URLPermission  
  
Represents permission to access a resource or set of resources defined by a given url, and for a given set of user-settable request methods and request headers. The name of the permission is the url string. The actions string is a concatenation of the request methods and headers. The range of method and header names is not restricted by this class. |  | YES  
|  |   
LinkPermission  
  
The Permission class for link creation operations. | hard | NO  
symbolic | NO  
|  |   
java.security.SecurityPermission  
  
A SecurityPermission contains a name (also referred to as a "target name") but no actions list; you either have the named permission or you don't.  
The target name is the name of a security configuration parameter (see below). Currently the SecurityPermission object is used to guard access to the Policy, Security, Provider, Signer, and Identity objects. | createAccessControlContext | NO  
getDomainCombiner | NO  
getPolicy | NO  
setPolicy | NO  
createPolicy.{policy type} | NO  
getProperty.{key} | NO  
setProperty.{key} | NO  
insertProvider | NO  
removeProvider.{provider name} | NO  
clearProviderProperties.{provider name} | NO  
putProviderProperty.{provider name} | NO  
removeProviderProperty.{provider name} | NO  
SQLPermission | setLog | NO  
callAbort | NO  
setSyncFactory | NO  
setNetworkTimeout | NO  
deregisterDriver | NO  
|  |   
java.util.logging.LoggingPermission  
  
A SecurityManager will check the java.util.logging.LoggingPermission object when code running with a SecurityManager calls one of the logging control methods (such as Logger.setLevel). | control | NO  
|  |   
java.util.PropertyPermission  
The name is the name of the property ("java.home", "os.name", etc). The naming convention follows the hierarchical property naming convention. Also, an asterisk may appear at the end of the name, following a ".", or by itself, to signify a wildcard match. For example: "java.*" or "*" is valid, "*java" or "a*b" is not valid.  
  
The actions to be granted are passed to the constructor in a string containing a list of zero or more comma-separated keywords. | read | YES  
write | NO  
javax.xml.ws.WebServicePermission  
| publishEndpoint | NO  
|  |   
javax.xml.bind.JAXBPermission | setDatatypeConverter | NO  
|  |   
javax.sound.sampled.AudioPermission  
  
Access rights to the audio system resources. | play | NO  
record | NO  
|  |   
javax.security.auth.PrivateCredentialPermission  
  
Protect access to private Credentials belonging to a particular Subject. The Subject is represented by a Set of Principals. The target name of this Permission specifies a Credential class name, and a Set of Principals. The only valid value for this Permission's actions is, "read". | CredentialClass {PrincipalClass "PrincipalName"}* | NO  
|  |   
javax.security.auth.kerberos.ServicePermission  
  
Protect Kerberos services and the credentials necessary to access those services. | initiate | NO  
accept | NO  
|  |   
javax.security.auth.kerberos.DelegationPermission  
  
Used to restrict the usage of the Kerberos delegation model; ie, forwardable and proxiable tickets.  
  
The target name of this Permission specifies a pair of kerberos service principals. The first is the subordinate service principal being entrusted to use the Ticket Granting Ticket (TGT). The second service principal designates the target service the subordinate service principal is to interact with on behalf of the initiating KerberosPrincipal. | initiate | NO  
accept | NO  
|  |   
javax.security.auth.AuthPermission  
  
Currently the AuthPermission object is used to guard access to the Subject, SubjectDomainCombiner, LoginContext and Configuration objects. | doAs | NO  
doAsPrivileged | NO  
getSubject | NO  
getSubjectFromDomainCombiner | NO  
setReadOnly | NO  
modifyPrincipals | NO  
modifyPublicCredentials | NO  
modifyPrivateCredentials | NO  
refreshCredential | NO  
destroyCredential | NO  
createLoginContext.{name} | NO  
getLoginConfiguration | NO  
setLoginConfiguration | NO  
createLoginConfiguration.{configuration type} | NO  
refreshLoginConfiguration | NO  
|  |   
javax.net.ssl.SSLPermission  
| setHostnameVerifier | NO  
getSSLSessionContext | NO  
setDefaultSSLContext | NO  
javax.management.MBeanPermission  
  
Permission controlling access to MBeanServer operations. If a security manager has been set using System.setSecurityManager(java.lang.SecurityManager), most operations on the MBeanServer require that the caller's permissions imply an MBeanPermission appropriate for the operation.  
  
action className#member[objectName]  
  
If you have an MBeanPermission, it allows operations only if all four of the items match. | addNotificationListener | NO  
getAttribute | NO  
getClassLoader | NO  
getClassLoaderFor | NO  
getClassLoaderRepository | NO  
getDomains | NO  
getMBeanInfo | NO  
getObjectInstance | NO  
instantiate | NO  
invoke | NO  
isInstanceOf | NO  
queryMBeans | NO  
queryNames | NO  
registerMBean | NO  
removeNotificationListener | NO  
setAttribute | NO  
unregisterMBean | NO  
|  |   
javax.management.MBeanServerPermission  
| createMBeanServer | NO  
findMBeanServer | NO  
newMBeanServer | NO  
releaseMBeanServer | NO  
|  |   
javax.management.MBeanTrustPermission  
  
This permission represents "trust" in a signer or codebase. | register | NO  
* | NO  
|  |   
javax.management.remote.SubjectDelegationPermission  |  | NO  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
