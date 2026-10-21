---
url: https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/howto-blue-green/
title: Reduce deployment risk with blue-green deployments \u00a0|\u00a0 Kf 2.9 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:01:36.016680+00:00
---

# Reduce deployment risk with blue-green deployments  |  Kf 2.9  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/howto-blue-green/

Version 2.9

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.9 ](https://docs.cloud.google.com/migrate/kf/docs/2.9)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.9/getting-started)



Send feedback 

#  Reduce deployment risk with blue-green deployments Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to deploy a new version of your application and migrate traffic over from an old to a new version.

## Push the initial App

Use the Kf CLI to push the initial version of your App with any routes:
    
    
    $ kf push app-v1 --route my-app.my-space.example.com
    

## Push the updated App

Use the Kf CLI to push a new version of your App without any routes:
    
    
    $ kf push app-v2 --no-route
    

## Add routes to the updated App

Use the Kf CLI to bind all existing routes to the updated App with a weight of 0 to ensure that they don't get any requests:
    
    
    $ kf map-route app-v2 my-space.example.com --hostname my-app --weight 0
    

## Shift traffic

Start shifting traffic from the old App to the updated App by updating the weights on the routes:
    
    
    $ kf map-route app-v1 my-space.example.com --hostname my-app --weight 80
    $ kf map-route app-v2 my-space.example.com --hostname my-app --weight 20
    

If the deployment is going well, you can shift more traffic by updating the weights again:
    
    
    $ kf map-route app-v1 my-space.example.com --hostname my-app --weight 50
    $ kf map-route app-v2 my-space.example.com --hostname my-app --weight 50
    

**Note:** Weights split traffic proportionally to the sum of the weights of all Apps mapped to the route. It's a common practice to treat weights as percentages.

## Complete traffic shifting

After you're satisfied that the new service hasn't introduced regressions, complete the rollout by shifting all traffic to the new instance:
    
    
    $ kf map-route app-v1 my-space.example.com --hostname my-app --weight 0
    $ kf map-route app-v2 my-space.example.com --hostname my-app --weight 100
    

## Turn down the original App

After you're satisfied that quick rollbacks aren't needed, remove the original route and stop the App:
    
    
    $ kf unmap-route app-v1 myspace.example.com --hostname my-app
    $ kf stop app-v1
    

Or delete the App and all associated route mappings:
    
    
    $ kf delete app-v1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
