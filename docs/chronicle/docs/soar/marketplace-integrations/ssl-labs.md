---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ssl-labs/
title: SSL Labs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:51:46.017737+00:00
---

# SSL Labs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ssl-labs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SSL Labs

This document provides guidance on how to integrate SSL Labs with Google SecOps.

## Configure SSL Labs integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Analyse Entity

#### Description

Analyse a host or a URL.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
status | Returns if it exists in JSON result  
protocol | Returns if it exists in JSON result  
criteriaVersion | Returns if it exists in JSON result  
isPublic | Returns if it exists in JSON result  
testTime | Returns if it exists in JSON result  
hosts | Returns if it exists in JSON result  
certs | Returns if it exists in JSON result  
ocspURIs | Returns if it exists in JSON result  
crlRevocationStatus | Returns if it exists in JSON result  
commonNames | Returns if it exists in JSON result  
altNames | Returns if it exists in JSON result  
raw | Returns if it exists in JSON result  
keySize | Returns if it exists in JSON result  
mustStaple | Returns if it exists in JSON result  
sct | Returns if it exists in JSON result  
sgc | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
issues | Returns if it exists in JSON result  
subject | Returns if it exists in JSON result  
keyAlg | Returns if it exists in JSON result  
keyStrength | Returns if it exists in JSON result  
notBefore | Returns if it exists in JSON result  
notAfter | Returns if it exists in JSON result  
keyKnownDebianInsecure | Returns if it exists in JSON result  
dnsCaa | Returns if it exists in JSON result  
ocspRevocationStatus | Returns if it exists in JSON result  
pinSha256 | Returns if it exists in JSON result  
revocationInfo | Returns if it exists in JSON result  
sha256Hash | Returns if it exists in JSON result  
revocationStatus | Returns if it exists in JSON result  
sigAlg | Returns if it exists in JSON result  
serialNumber | Returns if it exists in JSON result  
issuerSubject | Returns if it exists in JSON result  
startTime | Returns if it exists in JSON result  
engineVersion | Returns if it exists in JSON result  
endpoints | Returns if it exists in JSON result  
sims | Returns if it exists in JSON result  
results | Returns if it exists in JSON result  
lists | Returns if it exists in JSON result  
dhPrimes | Returns if it exists in JSON result  
fallbackScsv | Returns if it exists in JSON result  
hpkpRoPolicy | Returns if it exists in JSON result  
pins | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
directives | Returns if it exists in JSON result  
matchedPins | Returns if it exists in JSON result  
rc4WithModern | Returns if it exists in JSON result  
dhYsReuse | Returns if it exists in JSON result  
openSSLLuckyMinus20 | Returns if it exists in JSON result  
hasSct | Returns if it exists in JSON result  
supportsAlpn | Returns if it exists in JSON result  
dhUsesKnownPrimes | Returns if it exists in JSON result  
hpkpPolicy | Returns if it exists in JSON result  
port | Returns if it exists in JSON result  
****  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "status": "READY",
                "protocol": "http",
                "criteriaVersion": "2009p",
                "isPublic": false,
                "testTime": 1548163096137,
                "host": "https://www.siemplify.co",
                "certs": [{
                    "ocspURIs": ["http://ocsp.int-x3.letsencrypt.org"],
                    "crlRevocationStatus": 4,
                    "commonNames": ["www.siemplify.co"],
                    "altNames": ["www.siemplify.co"],
                    "raw": "-----BEGIN CERTIFICATE-----\\nMIIFWDCCBECgAwIBAgISA5qP6yPO3cbn1jut2q32WO1YMA0GCSqGSIb3DQEBCwUAMEoxCzAJBgNV\\r\\nBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQDExpMZXQncyBFbmNyeXB0IEF1\\r\\ndGhvcml0eSBYMzAeFw0xODEyMTkyMDU5MjRaFw0xOTAzMTkyMDU5MjRaMBsxGTAXBgNVBAMTEHd3\\r\\ndy5zaWVtcGxpZnkuY28wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDCVwGgI4e7VODR\\r\\nHpvnle2ACrxB4I/lu1w7UTQ+ToTH4YHf4QSphKIeIgKgTvFDO9XyDAeHHBrlQJi9gUpb4UMvqe0k\\r\\nhtusaoEtOxooyS/MriYmyb0jH6DN/+iFUz51V/TGSBiuMQOT0Xr0Pd+O1NTnScfPvZAkhA922GzN\\r\\n34A3UUrckPROod9rhyk3VVGzBiyGM0Ug/YZA/CR2KBdx44TEif5x3r5gM9Y6tVJCwpb1P8u4ih2B\\r\\nhGQfcsk9lVLhAc3CA2RuoNiJMhnSPcq0Z6Ena6HZFP50kmyC+I+nOA6maPqd2sVziLRfx/6KQ64b\\r\\nvaxmfh2JVin9HDA0s+k7FH47AgMBAAGjggJlMIICYTAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYw\\r\\nFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFBeENk9Ff8ytmywZ\\r\\nriIf/+Dxh0PhMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMG8GCCsGAQUFBwEBBGMw\\r\\nYTAuBggrBgEFBQcwAYYiaHR0cDovL29jc3AuaW50LXgzLmxldHNlbmNyeXB0Lm9yZzAvBggrBgEF\\r\\nBQcwAoYjaHR0cDovL2NlcnQuaW50LXgzLmxldHNlbmNyeXB0Lm9yZy8wGwYDVR0RBBQwEoIQd3d3\\r\\nLnNpZW1wbGlmeS5jbzBMBgNVHSAERTBDMAgGBmeBDAECATA3BgsrBgEEAYLfEwEBATAoMCYGCCsG\\r\\nAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCCAQQGCisGAQQB1nkCBAIEgfUEgfIA\\r\\n8AB2AOJpS64m6OlACeiGG7Y7g9Q+5/50iPukjyiTAZ3d8dv+AAABZ8h7B8gAAAQDAEcwRQIhALDG\\r\\nUqy3IKM5RDiC2gFQcLni9zPU0K+/emeoakaySTBQAiBKbOuHwAPc5o7K9IaQBmoBGysmSkiB2ZYS\\r\\ntN92RVmqjQB2AGPy283oO8wszwtyhCdXazOkjWF3j711pjixx2hUS9iNAAABZ8h7BdQAAAQDAEcw\\r\\nRQIhAPy8EuaFcMgeoGsrD9CK//6YoKnnnoSrBVbXDQM6DkCAAiB6iA1dre97fiuKEoeAKlmn6kha\\r\\nIbMdm4RYL9eA1EtTRDANBgkqhkiG9w0BAQsFAAOCAQEAJSzdIKyiC73v9oe9CABOz2GoZK4wUdnb\\r\\nLI5MupWv2rgZn0Co9gT/9R8mfKjq3ekdzesvhFzGGO6zIi5sHr8zxI2PyjuyLloFfI3EGsBjdDqI\\r\\nNUrpGrr/85+jk0eC2AG7ThA1ryJIApaU790f+e7uIu5ceA7WhwMpGJWF+TWhOSS5lLHhKJ3Ah4C4\\r\\nDErkeXUVpJUp+0VbE8bsigZ2jJh7eI2RsOmG8gHrTW4qPTQGeZFadR3Sfeq4mifk088Uyw3tF3eL\\r\\n9buXQWXi5o2mEsAPUpKTZFeYZqaEGQOM5RCOyO3kN/+OSJNHU+SjQn2SvyMRCCMMj7pAoMlyjvS7\\r\\nVglJKg==\\r\\n-----END CERTIFICATE-----\\n",
                    "keySize": 2048,
                    "mustStaple": false,
                    "sct": true,
                    "sgc": 0,
                    "id": "236a2b12c7f9384f5907724502b8635bc86f4281a543b9d77b7a5a87d1feed2d",
                    "issues": 0,
                    "subject": "CN=www.siemplify.co",
                    "keyAlg": "RSA",
                    "keyStrength": 2048,
                    "notBefore": 1545253164000,
                    "notAfter": 1553029164000, "sha1Hash":
                    "22a53bd913fca0bc60cd5d6e577271585019b2b4",
                    "keyKnownDebianInsecure": false,
                    "dnsCaa": false,
                    "ocspRevocationStatus": 2,
                    "pinSha256": "KBlMyqNKhogFXSV1X6/xpt62dfut1th0XspgxFAtgSY=",
                    "revocationInfo": 2,
                    "sha256Hash": "236a2b12c7f9384f5907724502b8635bc86f4281a543b9d77b7a5a87d1feed2d",
                    "revocationStatus": 2,
                    "sigAlg": "SHA256withRSA",
                    "serialNumber": "039a8feb23ceddc6e7d63baddaadf658ed58",
                    "issuerSubject": "CN=Let's Encrypt Authority X3, O=Let's Encrypt, C=US"
                }],
                "startTime": 1548162999719,
                "engineVersion": "1.32.13",
                "endpoints": [{
                    "gradeTrustIgnored": "A",
                    "grade": "A",
                    "hasWarnings": false,
                    "serverName": "1.1.1.1.bc.googleusercontent.com",
                    "delegation": 2,
                    "details": {
                        "sims": {
                            "results": [{
                                "errorCode": 1,
                                "sigAlg": "SHA256withRSA",
                                "attempts": 0,
                                "client": {
                                    "version": "2.3.7",
                                    "isReference": false,
                                    "id": 56,
                                    "name": "Android"
                                },
                                "errorMessage": "Protocol mismatch (not simulated)"
                            }]},
                        "poodleTls": 1,
                        "freak": false,
                        "sessionTickets": 1,
                        "compressionMethods": 0,
                        "suites": [{
                            "list": [{
                                "cipherStrength": 256,
                                "namedGroupName": "secp256r1",
                                "name": "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
                                "namedGroupId": 23,
                                "namedGroupBits": 256,
                                "kxStrength": 3072,
                                "kxType": "ECDH",
                                "id": 49172
                            }],
                            "protocol": 770,
                            "preference": true
                        },{
                            "protocol": 771,
                            "preference": true
                        }],
                        "dhPrimes": [                "889c6c058890bda62ced33f067eaf414568910838d4bdc23e3dbef17caf5cf117c1b48f0dd74b03b193af42d011a4b7fde725dc6ab97897a81e0ee81e1af420ce716cec48a862d4f8193709df4c59837c8a5f73006147b3c0b8d531074c83f9c94914150eb29b855d0f93b5c9b125b5eb3a21e2a638eebc50a517872af93dafbecfa137c379139272a0ecbfd5a2b3bba2f2555540a0cd2cec215b2701beaaad208c6ac3e1be79e319f39ccb2d9e1ab21d4a40e5db817bc3baa5d656bdc6764da4d4e750a5db7a0a2c724cb376f6a7a7ef1e4e58ebcdd886fdc25241c76941eaf3197ada60ca0ada91767eb0193c86eb9b9670a46511c3250f5575e04abd5e8cb"
                                    ],
                        "fallbackScsv": true,
                        "hpkpRoPolicy": {
                            "pins": [],
                            "status": "absent",
                            "directives": [],
                            "matchedPins": []
                        },
                        "rc4WithModern": false,
                        "dhYsReuse": false,
                        "openSSLLuckyMinus20": 1,
                        "hasSct": 1,
                        "supportsAlpn": true,
                        "dhUsesKnownPrimes": 0,
                        "hpkpPolicy": {
                            "pins": [],
                            "status": "absent",
                            "directives": [],
                            "matchedPins": []
                        },
                        "staticPkpPolicy": {
                            "serverSignature": "nginx",
                            "poodle": false,
                            "hstsPolicy": {
                                "status": "absent",
                                "LONG_MAX_AGE": 15552000,
                                "directives": {
                                }},
                            "ocspStapling": false,
                            "protocols": [{
                                "version": "1.1",
                                "id": 770,
                                "name": "TLS"
                            }],
                            "ticketbleed": 1,
                            "forwardSecrecy": 4,
                            "miscIntolerance": 0,
                            "hstsPreloads": [{
                                "status": "absent",
                                "source": "Chrome",
                                "hostname": "www.siemplify.co",
                                "sourceTime": 1548162600888}],
                            "drownVulnerable": false,
                            "ecdhParameterReuse": false,
                            "vulnBeast": false,
                            "drownHosts": [],
                            "certChains": [{
                                "trustPaths": [{
                                    "trust": [{
                                        "isTrusted": true,
                                        "rootStore": "Windows"
                                    }],
                                    "certIds": [                                 "236a2b12c7f9384f5907724502b8635bc86f4281a543b9d77b7a5a87d1feed2d", "25847d668eb4f04fdd40b12b6b0740c567da7d024308eb6c2c96fe41d9de218d", "0687260331a72403d909f105e69bcf0d32e1bd2493ffc6d9206d11bcd6770739"
                                               ]}],
                                "noSni": false,
                                "issues": 0
                            }],
                            "prefixDelegation": true,
                            "supportsAead": true,
                            "alpnProtocols": "h2 http/1.1",
                            "logjam": false,
                            "renegSupport": 2,
                            "heartbleed": false,
                            "heartbeat": true,
                            "sniRequired": true,
                            "sessionResumption": 2,
                            "httpStatusCode": 200,
                            "nonPrefixDelegation": false,
                            "rc4Only": false,
                            "openSslCcs": 1,
                            "bleichenbacher": 1,
                            "httpTransactions": [{
                                "requestLine": "GET / HTTP/1.1",
                                "requestHeaders": [
                                    "Host: www.siemplify.co",
                                    "User-Agent: SSL Labs (https://www.ssllabs.com/about/assessment.html); on behalf of XXX.XXX.XXX.XXX",
                                    "Accept: */*"
                                ],
                                "requestUrl": "https://www.siemplify.co/",
                                "fragileServer": false,
                                "responseLine": "HTTP/1.1 200 OK",
                                "responseHeadersRaw": [
                                    "Server: nginx",
                                    "Date: Tue, 22 Jan 2019 13:16:44 GMT",
                                    "Content-Type: text/html; charset=UTF-8"
                                ],
                                "responseHeaders": [{
                                    "name": "Server",
                                    "value": "nginx"
                                }],
                                "statusCode": 200
                            }],
                            "supportsRc4": false,
                            "drownErrors": false,
                            "hostStartTime": 1548162999719,
                            "protocolIntolerance": 0,
                            "supportsNpn": true,
                            "namedGroups": {
                                "list": [{
                                    "namedGroupType": "EC",
                                    "bits": 283,
                                    "id": 10,
                                    "name": "sect283r1"
                                }],
                                "preference": true
                            },
                            "npnProtocols": "h2 http/1.1"
                        },
                        "isExceptional": false,
                        "duration": 96329,
                        "progress": 100,
                        "ipAddress": "1.1.1.1",
                        "statusMessage": "Ready"
                    }],
                    "port": 443
                },
                              "Entity": "https://www.siemplify.co"
                              }
            ]
    

### Ping

#### Description

Test connectivity to SSL Labs.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
