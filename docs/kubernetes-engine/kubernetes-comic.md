---
url: https://docs.cloud.google.com/kubernetes-engine/kubernetes-comic/
title: Deploy code faster: with CI/CD and Kubernetes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:27:48.514378+00:00
---

# Deploy code faster: with CI/CD and Kubernetes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/kubernetes-comic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/header_1x.png)

SCENE 1: The Kubernetes logo is surrounded by leaping fish and a Greek key border. NARRATOR: Smooth Sailing with Kubernetes. An online comic to learn about Kubernetes and how you can use it for continuous integration and delivery. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-1_1x.png)

SCENE 2: Jason on a beach, dressed in ancient greek armor. Sword in hand, he battles skeletal warriors and a flying harpy. NARRATOR: In ancient times, he battled gods and monsters with his mighty band of argonauts... SCENE 3: Jason in his office, stressed out about work. He is dressed like a Pacific Northwest hipster: glasses, long beard, nautical sweater, and a Greek sailor’s cap. He has pale skin and short-cut hair. NARRATOR: Now, Jason is in I.T. and his daily battles just got a lot harder. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-2_1x.png)

SCENE 4: Jason and technicians in a data center, busy at work managing server racks. NARRATOR: His company’s massively multiplayer online game is a hit, but operations is having major growing pains. TECHNICIAN: (sobbing) Looks like “Bessie” is a goner, captain! JASON: (stressed) Well quit dragging your heels and order more servers. And please don’t give them names, it’s creepy. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-3_1x.png)

SCENE 5: Jason, cradling his head worriedly, surrounded by miniature complaining people representing his problems. JASON: For Hera’s sake, who knew delivering these services would be so hard? PROBLEM 1: Sorry to call at 3:00 am, but… PROBLEM 2: We can’t scale up fast enough! PROBLEM 3: Why isn’t my code up yet? PROBLEM 4: Our update cycles are too slow! PROBLEM 5: Game’s gonna get stale, boss… PROBLEM 6: Oh crap, power’s out again! JASON: Why can’t it just work all the time?! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-4_1x.png)

SCENE 6: Jason, unexpectedly interupted by an unknown stranger. ATHENA: It can - (sentence continues) SCENE 7: Jason, startled, as a stranger in ancient greek armor comes in through the window. ATHENA: With Kubernetes! JASON: Huh? Who? 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-5_1x.png)

SCENE 8: Athena stands proudly, wearing a plumed helmet and ancient greek clothing. She carries a spear and seven-sided shield. She is a young teenager, with dark skin and long, curly, black hair. ATHENA: (announcing loudly) It’s me, Athena! Goddess of wisdom, craft, and containerized applications. JASON: I thought it was “wisdom, craft, and war.” ATHENA: Mortals have enough war. You need containers! (softly, as a side comment) Also, I’m diversifying. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-6_1x.png)

SCENE 9: Jason explaining, sincerely. JASON: Well, we’re already deploying apps in containers, but it’s hardly fixed everything ... Managing them is still slow, inefficient, and full of holes. SCENE 10: Athena poking Jason in the chest to make her point. ATHENA: Putting apps in containers is a great first step, but now you need to orchestrate those puppies. That’s where Kubernetes can help! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-7_1x.png)

SCENE 11: Athena grabs Jason by the hand as she runs towards something, pulling him off his feet. ATHENA: But first, a little history lesson, follow me! JASON: Hey, if you’re a Greek goddess, why do you look like a junior Comic-Con cosplayer? ATHENA: Shut up, that’s why! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-8_1x.png)

SCENE 12: Jason and Athena stand on mountain. A village spreads out before them. An enormous one-eyed monster is attacking the village. Inside the monsters are rotating tools that represent application functionality. Villagers are screaming and running away from the monster. JASON: Whoa, where are we?! ATHENA: Welcome to an ancient time, long long ago. When wedge sneakers were popular, Game of Thrones was, like, on season two, and monolithic applications ruled the Earth! VILLAGER 1: Aah! Help! VILLAGER 2: It’s so kludgy! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-9_1x.png)

SCENE 13: Athena prepares for battle, raising her spear and rushing forward. ATHENA: Monoliths had impressive feature sets, but too many interdependent parts, so integration and deployment were a nightmare. SCENE 14: Athena attacks the monster, cutting off its hand with a loud whack. The hand contains a single rotating tool, representing one piece of application functionality. ATHENA: By chopping them into individual processes, though, we’ve learned to bring these monsters under control. MONSTER: (screaming in pain) Aargh! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-10_1x.png)

SCENE 15: A set of six different rotating tools (hammer, saw, screwdriver, wrench, pliers, and drill) representing application functionality have been separated out. ATHENA: Each one of these “microservices” can now be debugged, updated, and deployed individually without the whole project coming to a standstill. An important step on the path to continuous integration and delivery. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-11_1x.png)

SCENE 16: Jason looks at two rotating tools, a hammer and a nail, hovering above Athena’s hands, under her control. JASON: They still have to talk to each other, right? ATHENA: Sure! They’re loosely coupled with a lightweight protocol; just enough to cooperate (sentence continues) HAMMER: (speaking to nail) Looking sharp. NAIL: (speaking to hammer) You hitting on me? SCENE 17: Jason leans forward to closely study a rotating tool. There are more tools floating above Athena’s hands now, in a top-down hierarchy where one tool depends on one or more other tools. Arrows connect the tools to represent the dependencies. ATHENA: And to preserve the network of dependencies that tied the big apps together. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-12_1x.png)

SCENE 18: An architectural diagram shows three rectangles stacked on top of each other. CPU / memory is on the bottom, kernel is in the middle, and operating system is on the top. A myriad of hands extrude from the operating system layer to grab at the spinning tools above, causing friction in the tools’ smooth rotation. ATHENA: Thing is, if you run these services on a single operating system, you might get conflicting library versions and application components (sentence continues) SCENE 19: Athena stands on top of a transparent box. Inside rotating tools float around, sometimes colliding with each other. ATHENA: If you put them all in a virtual machine, apps could still conflict with one another (sentence continues) SAW (speaking to axe): Hey, Cut it out. Pliers (speaking to wrench): Don’t pressure me! SCENE 20: Athena staggers under the weight of stack of transparent boxes, each one holding only a single rotating tool. ATHENA: And if you create a separate virtual machine for each, it’d just be top heavy, wasteful, and expensive. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-13_1x.png)

SCENE 21: Athena presenting to Jason a running process (represented by a rotating letter A) surrounded by a square of bright, sunny sky. ATHENA: But, what if each process could somehow be built to run on its own; with its libraries and settings baked in? In short, everything each process needs to run on any machine, virtual or bare metal. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-14_1x.png)

SCENE 22: The square of sunny sky is submerged in gloomy ocean depths and surrounded by curious fish. Inside the square the rotating A spins on, dry and brightly lit. SCENE 23: The square of sunny sky floats in the night sky above trees and bats. Inside the square the rotating A is still in daytime. SCENE 24: The square of sunny sky floats in the air during a hurricane. Gale-force winds and rain whip the palms trees below. Inside the square, the rotating A operates in a calm and windless day. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-15_1x.png)

SCENE 25: Text only. ATHENA: A self-contained process. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-16_1x.png)

SCENE 26: Jason is pondering what Athena just said. Athena is grinning dreamily as she thinks about the romance inherent in the concepts. JASON: Aha! Enter containers. But, did microservices really lead to containerized apps? ATHENA: Not exactly, but the ideas behind both ... Ah, they’re a match made in Olympus! SCENE 27: Athena demonstrating how a circle can be split into multiple wedge-shaped pieces. ATHENA: Because when modularity (sentence continues) SCENE 28: Athena levitating Lego pieces. ATHENA: Meets interoperability (sentence continues) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-17_1x.png)

SCENE 29: Text only ATHENA: You can start exploiting whole new levels of (sentence continues) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-18_1x.png)

SCENE 30: A process (represented by a rotating letter “A”) flying off into the sky. ATHENA: Portability (sentence continues) SCENE 31: A hand using a rubber stamp to stamp out multiple copies of a rotating letter “A”. ATHENA: Reproducibility (sentence continues) SCENE 32: A rotating letter “A” growing in size in every direction. ATHENA: and scalability (sentence continues) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-19_1x.png)

SCENE 33: Text only ATHENA: anywhere and anytime across the world! (sentence, mercifully, ends) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-20_1x.png)

SCENE 34: Jason and Athena are on opposite sides of the Earth. He stands in night time, and she in day time. They’re shouting across the distance at each other and Athena is waving her spear in emphasis. JASON: Whoa, whoa. Slow down ... My team can barely handle the containers we’ve got running now. If we ramp things up, how will we ever keep track of them all? ATHENA: You don’t! You automate all those containers with (shouting in triumph) Kubernetes! SCENE 35: A large Kubernetes logo: the word “Kubernetes” is next to a blue heptagon (seven sides). The heptagon is overlaid by a white, spoked, wheel of the type used to steer a ship. On either side of the word “Kubernetes”, Athena is making a quiet side comment. ATHENA: (cheerfully) It’s Greek for “helmsman”. ATHENA: (begrudgingly) Also... Star Trek in jokes. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-21_1x.png)

SCENE 36: Jason, pondering. JASON: Again with the logo ... Hey, this isn’t all just some big sales pitch for Google Cloud, is it? SCENE 37: Athena explaining to a skeptical Jason. His arms are folded across his chest. ATHENA: Nope. Kubernetes is open source! Free and open to anyone who wants to use it. SCENE 38: Athena getting more intense. ATHENA: It’s backed by a big community of developers. Even GitHub uses it. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-22_1x.png)

SCENE 39: Jason is still skeptical. Athena has wound down and is standing quietly, spear in hand. JASON: Is there a sales pitch later? ATHENA: (says nothing) SCENE 40: Jason holds his skeptical pose. Athena looks away from him, abashed. ATHENA: (quietly) Maybe… SCENE 41: Jason relents and uncrosses his arms. Athena is jubilant, grinning and raising her hand in triumph. JASON: Huh ... Okay, keep going. ATHENA: Yay! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-23_1x.png)

SCENE 42: Athena, the Kubernetes logo floating above her right hand, and balancing a globe of the Earth, spinning, on the forefinger of her left hand. ATHENA: So, Kubernetes has a few key goals: (sentence continues) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-24_1x.png)

SCENE 43: A drinking glass filled with containerized processes all the way up to the top. The final space is being filled with one last container. ATHENA: To distribute containers in a logical and efficient way. NARRATOR: Translation: maximize capacity. SCENE 44: A Kubernetes logo, a heptagon with an overlaid ship’s wheel, with arrows pointing out from all seven corners to demonstrate that it’s expanding in all directions. ATHENA: To scale up (or down) fast with the operations you already have. NARRATOR: Translation: Adapt to demand. SCENE 45: An anthropomorphized sun and moon, where the moon face overlays half of the sun face, indicating that the symbol represents both day and night. ATHENA: To keep processes continuously running and healthy. NARRATOR: Translation: Don’t go dark. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-25_1x.png)

SCENE 46: Athena relaxed and smiling. ATHENA: And most importantly (sentence continues) SCENE 47: A hand with an outstretched forefinger drawing a dotted through line connecting a set of points. The hand is commanding the course of events. ATHENA: To give you power over what gets done (sentence continues) SCENE 48: Emoji of a person sleeping contentedly in bed and snoring. ATHENA: Without forcing you to micro-manage how. (sentence ends) NARRATOR: Translation: OMG weekends. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-26_1x.png)

SCENE 49: Athena holds up the previous containerized process (a rotating letter “A” within a box of sky) and now a dotted line, representing a pod, surrounds the application. Jason examines the pod, interested. ATHENA: To do this, Kubernetes adds a new level of abstraction for container management: the pod. SCENE 50: An anthropomorphic dotted line, representing an pod, has an enormous eyeball attached to it that is watching a containerized process (a rotating letter “A” within a box of sky). ATHENA: Pods are the smallest building block in the Kubernetes object model. The pod “sees” the container (sentence continues) SCENE 51: An anthropomorphic Kubernetes logo, a heptagon overlaid with a ship’s wheel, has an enormous eyeball attached to it that is watching an anthropomorphized pod to the right of it. The containerized process is not shown. ATHENA: But Kubernetes only sees the pod. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-27_1x.png)

SCENE 52: An anthropomorphized Kubernetes logo watches over a set of pods. Most pods contain only one process. The last pod holds two processes of different types. Hearts are emanating from that pod. The pod nearest them, containing a single process, makes a side comment. ATHENA: Most pods hold just one container, though tightly-coupled processes will sometimes share a pod. SINGLETON POD: (quietly) Ugh. Get a room, you two. SCENE 53: Athena holds out a round platter, covered in pods, to Jason. The pods contain running processes. The overall effect is of a waiter serving the pods. Thus the platter represents a server, or node. ATHENA: Groups of pods are then co-located on a single “machine” (real or virtual), each of which we call a node. NARRATOR: (quietly) Previously known as “minions”. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-28_1x.png)

SCENE 54: Athena gestures with her hand to direct Jason’s attention to a configuration of platters in the distance. The central platter is wearing a hat, indicating that it is superior and different than the others. On the central platter is a cylinder, representing a data store, and a clipboard, representing a set of instructions. Surrounding the central node are subordinate nodes that contain only pods. Arrows point from the central node to the others, indicating that it controls them. ATHENA: And nodes are then grouped into clusters. Each of which is overseen by a master node. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-29_1x.png)

SCENE 55: A scroll magically appears in front of Jason, surprising him. Athena points at it with her spear. ATHENA: Those clusters are put in place by the deployment: a simple .yaml file declaration by you (sentence continues) SCENE 56: Athena stands behind Jason as he writes on the scroll. ATHENA: Stating the ideal battalion of processes you want up and running to do your bidding. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-30_1x.png)

SCENE 57: The magical deployment scroll hovers above the Earth giving directions to a cluster below. The cluster is represented by platters of pods and the master-node platter. Above the cluster is a cloud full of container images, represented as boxes filled with non-rotating letters. The cloud represents the container registry. Dotted arrows rain down from the cloud, indicating that container images are being pulled down to the nodes. ATHENA: Kubernetes then selects the machines and propagates the containers in each pod pulling down the container images specified in the deployment. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-31_1x.png)

SCENE 58: Athena sits with her arms resting on a deployment scroll, questioning a standing Jason. ATHENA: So do you want to pick out motherboards? JASON: Well, I, uh… ATHENA: (interrupting) Oh, and what Linux distro do you need? Ubuntu? Core OS? Debian? JASON: I hadn’t really — SCENE 59: The questioning turns into an interrogation, with Jason getting visibly flustered. ATHENA: (interrupting) I hear Utah is nice, want to put it all in Utah? JASON: What, no! I mean maybe, but — ATHENA: (interrupting again) Oh, I.P. addresses! Want to pick 198.51.100.0? 203.0.113.0? 192.0.2 — JASON: (interrupting, frustrated) I don’t care! SCENE 60: Athena leans forward and pokes her finger into Jason’s chest to emphasize her point. ATHENA: Exactly. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-32_1x.png)

SCENE 61: A group of clusters, represented by sets of pods on platter-shaped nodes. Each cluster is monitored by a different hat, which represents the master node of that cluster. Athena is off to the side with Jason. She’s pulling on his arm and pointing with her spear to direct his attention to the clusters. ATHENA: That’s the beauty of Kubernetes’ abstracted infrastructure. Who cares what “machine” your process is on. They’re all the same to you now! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-33_1x.png)

SCENE 62: A container image floats inside a cloud. The cloud is above a row of running containerized processes inside pods. An arrow points from the cloud to the row, indicating that the copies in the row have been created from the container image. ATHENA: In the same way that all containers made from a given image will be interchangeable with one another. Identical in fact, All created from the same immutable template. SCENE 63: Athena is grinning and juggling pods filled with containerized processes. Jason cowers in the background, concerned that she’ll drop something. ATHENA: So, with interchangeable container replicas and interchangeable machines (sentence continues) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-34_1x.png)

SCENE 64: The pods Athena were juggling are falling from the sky onto a node, as represented by a platter that Athena is holding up. The box-shaped pods are falling into a neat stack, with rows and columns lined up. ATHENA: Kubernetes can drop each replica into just the right place! SCENE 65: Three moving trucks are in a row. In each one, a few boxes have been tossed in haphazardly. The first truck is 75% empty, the second one is 50% empty, and the last one is 90% empty. ATHENA: Tired of wasting CPU? SCENE 66: A moving truck packed efficiently with boxes all the way up to the top. The final space is being filled with one last box. ATHENA: Kubernetes will be on the lookout for more efficient “bin packing” opportunities. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-35_1x.png)

SCENE 67: Three identical nodes, each represented as a set of pods on platter-shaped nodes. ATHENA: Risk, meanwhile, can be distributed, so that no running process (sentence continues) SCENE 68: The top node is struck by lightning and starts to die. The other two nodes are perfectly fine. ATHENA: can be taken down by a single failure point (sentence continues) SCENE 69: The top node is completely destroyed, only smoke remains. The other two nodes are perfectly fine. ATHENA: replicas can continue running smoothly, while the system (sentence continues) SCENE 70: Anthropomorphized container images, represented as rectangles with spinning letters inside, now have arms and legs and are dashing to fill a set of empty pods resting on a node. The master node, represented by a hat, is reading the deployment scroll and alarmed at the discrepancy between reality and the deployment. ATHENA: quickly restores the ideal state of your deployment. (sentence ends) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-36_1x.png)

SCENE 71: Kubernetes is shown as a meditating human with the heptagon-shaped Kubernetes logo for a head. It is experiencing enlightenment. ATHENA: Kubernetes is self-healing. SCENE 72: Kubernetes is shown as a heptagon-shaped Kubernetes logo with a giant eyeball attached. It is studying a deployment scroll. ATHENA: The system fanatically compares the ideal state, as expressed in the deployment (sentence continues) SCENE 73: Kubernetes is shown as a heptagon-shaped Kubernetes logo with a giant eyeball attached. It is studying a cluster which contains a master node and several worker nodes. Pods rest on the worker nodes. ATHENA: To the actual state of pods and clusters in real world operation. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-37_1x.png)

SCENE 74: Athena stands next to Jason, showing him a deployment scroll. ATHENA: No tolerance. No excuses. SCENE 75: Two nodes containing pods and running containerized processes are shown. On one node, one of the containerized processes is dead, as represented by a skull and crossbones. ATHENA: If any violation or inconsistency is detected—bam. Something’s going to be terminated (sentence continues) SCENE 76: A container image in a cloud is dropping down to fill an empty pod. ATHENA: and instantly reborn. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-38_1x.png)

SCENE 77: Jason and Athena stand beneath a cloud, inside of which is a container image marked “A”. A hand comes in from off screen and inserts a new container image, “A+” into the cloud. JASON: What about updates? ATHENA: Same idea. SCENE 78: A cloud with the “A+” container image inside sits at the hub of a clock. Letters sit at the rim where numbers would usually be. As the clock hand rotates, it replaces “A”s with “A+”s, representing a rolling update of the application version. ATHENA: The new container image is pulled from the registry and new containers deployed from it (sentence continues) SCENE 79: The clock hand has swung all the way around and all the “A”s have been replaced with “A+”s. ATHENA: Usually as a rolling update, for a smooth, stable transition. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-39_1x.png)

SCENE 80: Athena and Jason stand next to a stack of nodes. On each node three applications are running. The are labeled “A”, “B”, and “C”. All of the “B” applications are surrounded by a single rectangle that crosses through node boundaries. This rectangle represents a label. ATHENA: Using labels, it’s easy to treat all the replicas of a process as a single entity within a given cluster. A set of replicas that add up to a single service. SCENE 81: Kubernetes, shown as a heptagonal Kubernetes logo with a giant eyeball attached is talking to a master node (represented as a hat) which is managing a cluster of nodes. ATHENA: Kubernetes doesn’t fret over individual processes. It cares about the real world result: the aggregate services they provide. Sort of like you, I’ll bet. KUBERNETES: (to master node): Got “B”? (meaning the “B” service) MASTER NODE: (to Kubernetes) I got B like you wouldn’t believe. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-40_1x.png)

SCENE 82: Kubernetes hovers over the earth, monitoring a set of clusters. In the background the sun and moon alternate in the sky, indicating the passage of time. ATHENA: Kubernetes is dedicated to keeping those services running and healthy every minute of the day. SCENE 83: Athena and Jason look up into sunshine, representing a shiny future. ATHENA: It’s a new millennium, old boy! No one reaches into their pocket wondering if an app will be “available.” It’s up and running or you’re dead and buried. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-41_1x.png)

SCENE 84: Athena is flying through the air, spear in front of her. Jason is riding on a speeding motorcycle. He looks startled and his hat is flying off behind him. The motorcycle is labeled “Theseus” with the image of a ship underneath it. (This is a subtle reference to the ship of Theseus.) ATHENA: And with Kubernetes, you’ll be up and running for as long as you want to be! JASON: Whoa—abrupt transition! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-42_1x.png)

SCENE 85: Jason, hatless, is panicking as the motorcycle speeds off with him. Athena flies behind him smiling and having a congenial conversation. ATHENA: Just as modularity and immutability foster continuous integration, containers and Kubernetes are enabling continuous delivery. JASON: You know I’m a sailor, right?! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-43_1x.png)

SCENE 86: Athena flies down towards the speeding motorcycle and points a nut and screw that have been thrown off the spinning front wheel. ATHENA: Oh look—loose screws! No need to stop driving! JASON: No, I can pull over! ATHENA: (interrupting) All fixed! SCENE 87: Jason is still riding the speeding motorcycle, and it’s changed into a completely different model of motorcycle. Athena flies along beside him. ATHENA: Want to upgrade to a new model? JASON: (frantic) Yes, please! Let’s park at a— ATHENA: (interrupting) Voila! Whole new bike! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-44_1x.png)

SCENE 88: Text only. NARRATOR: Six hours later ... 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-45_1x.png)

SCENE 89: Jason is back in his office, slumped in his chair. He’s exhausted physically and emotionally. Athena stands near his desk, raising her spear in triumph and smiling. JASON: Okay. Enough metaphors. I’m convinced! Kubernetes really is the best way to manage containers. ATHENA: Hurray! 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-46_1x.png)

SCENE 90: An enthusiastic Athena is grinning and leaning in towards Jason. ATHENA: So, ready to harness the full power of Kubernetes using Google’s own world class infrastructure and get up and running with Google Kubernetes Engine? SCENE 91: Jason is still slumped in his chair, his expression is skeptical and world weary. JASON: Was that the sales pitch? ATHENA: (not pictured) More or less. SCENE 92: Jason, still seated behind his desk, puts his hand up to his forehead, relieved. Athena picks up his keyboard. JASON: Okay, that wasn’t so bad. 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-47_1x.png)

SCENE 93: Jason and Athena are huddled in front of his computer, working together. Athena is typing. JASON: Tell you what: I’ll get my team on it, sign them up for some training. We can try having our first nodes up and running in maybe ten weeks… ATHENA: Or… (sentence continues) 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-48_1x.png)

SCENE 94: Athena points a his desktop monitor. Jason is surprised. ATHENA: How about ten minutes? 

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-49_1x.png)

SCENE 95: Text only. NARRATOR: Now it's your turn. Type commands into the following terminal emulator and learn how to create a Kubernetes cluster on GKE. 

SCENE 96: A terminal window surrounded by a decorative Greek-key border. 

[ ![SCENE 97: Text only. NARRATOR: Art and Story by Scott McCloud.](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/credit.svg)](http://scottmccloud.com)

![](https://docs.cloud.google.com/static/kubernetes-engine/kubernetes-comic/assets/panel-51-b_1x.png)

SCENE 98: Athena stands shouting, spear in one hand and shield in the other. ATHENA: Create your first cluster! Now that you know the basics, you're ready to launch your first GKE cluster on Google Cloud. 

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
