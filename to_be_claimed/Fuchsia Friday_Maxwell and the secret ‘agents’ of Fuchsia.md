
#Fuchsia Friday: Maxwell and the secret ‘agents’ of Fuchsia
![](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/fuchsia-friday-maxwell.jpg)

This week on Fuchsia Friday, we get to take a look at our most requested topic: Maxwell, the smarts behind Fuchsia.

Maxwell manages the intelligence of Fuchsia. This intelligence is actually not one large program, but, in true Fuchsia fashion, is pieced together from a variety of smaller programs. These programs, called agents (we’ve talked a little bit about agents before), can be simply be thought of as background tasks. However, I find the name “agent” very fitting: agents run in the background (secret agent!), gather information (like any good spy), and report it back to home base.

To best understand how agents work and what they do, let’s look at three agents that work in conjunction without any direct communication. The first agent is called maxwell_btl which is short for “basic text listener.” Presently, it simply scans text for email addresses, and creates an email entity (got a second for a refresher on entities?). This entity is then put into context.

Context, put simply, is Maxwell’s way of knowing what you’re currently seeing and doing, and Maxwell only knows what its agents tell it. Context is divided into different topics which helps agents listen only for changes to context that are relevant. For example, a music-related agent would only want to know about music-related changes, not email addresses.

When the context is updated, all agents are notified of the change, and respond if they need to. In this case, nothing happens yet. The next agent to look at is maxwell_entity_selector. This agent listens for changes to text selection and checks if the currently highlighted text contains an entity. If I were to highlight the email address, the agent would check context for entities contained in that selection, and put the email entity into context under a different topic.

Once that happens, the third agent, maxwell_proposal_maker, which is only listening for the highlighted entities topic, will see the context changes and make a suggestion to open Gmail and compose an email to that address.

It was my intention to show a video of this in action, but recent changes in the code have broken this example. When it’s working, I’ll update this post with the video. If anything, this is another example of the early stage Fuchsia is still in.

There’s a small handful of other agents that Maxwell uses right now:

* Module_suggester powers the search box and results that you see on the home screen of Armadillo. It does this very simply with pre-loaded results for certain searches. This will likely be replaced or greatly expanded upon down the line.
* Eddystone_agent is another simple example agent that shows how to listen for an Eddystone bluetooth beacon and suggest opening the associated URL.

![The Eddystone agent at work – Image: @g123k](https://9to5google.com/wp-content/uploads/sites/4/2018/03/eddystone-fuchsia.jpg)

* Usage_log listens for modules (modules are smaller pieces of bigger apps) being opened, and sends anonymized reports to Fuchsia’s metrics software Cobalt. Any Googlers who were looking through Cobalt logs a few weeks ago may have been confused by an unfamiliar module being opened, as we recently made our own Flutter app and ran it on Fuchsia.

Thus far, most of these agents seem like they’re placeholders or just examples of how to code bigger and more complex agents. These change when we get to Kronk. Kronk is currently Fuchsia’s only agent with voice responses. As we learned a few weeks ago, Kronk is the Fuchsia team’s code name for the Google Assistant. As of now, Kronk is one of the few components of Fuchsia that is not open source. This of course makes sense, as it surely contains code that Google wants to keep proprietary. From what we can tell from the copy we’ve obtained, it seems like business as usual for the Assistant.

These are just the agents that are included directly in the Maxwell system. Agents can be included with any app you install, but all agents report to Maxwell. With Maxwell in the middle, no two agents need to speak directly or even know about each other. A Spotify player could tell an agent what song you’re listening to, and another agent could offer you lyrics for that song without needing to talk directly to Spotify.

Oh, and in case you’re wondering (like I was), the name Maxwell seems to come from the secret agent character Maxwell Smart from the 60s TV show Get Smart. While not really a reference I can fully appreciate, my dad thought it was funny at least.

![]()
（说明：该视频届时将上传到网站服务器上）

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：（替换为译者名字和作者地址）；校对： （替换为译者名字和作者地址）       
原文链接：https://9to5google.com/2018/03/23/fuchsia-friday-maxwell/       
本文链接：https://fuchsia-china.com/×××（发布后替换）
