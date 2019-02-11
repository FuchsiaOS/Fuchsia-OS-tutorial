
#Fuchsia Friday: Everything is an Entity
![](https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/02/entities.png)

Two weeks ago, we learned about Fuchsia’s Stories and Modules, and how they will help us better organize our time, tasks, and ideas. This week, we’re looking at the idea of ‘entities’, Fuchsia’s attempt to catalog the digital world to be read by Assistant. Entities are also part of the glue that holds disparate “modules” together into one coherent Story.

In the Fuchsia docs, an entity is described as “an identifiable person, place, thing, event, or concept […] which can be referenced, retrieved, presented, manipulated, or shared.” By this definition, almost anything can be an entity, but some more specific examples given include bands, hotels, contacts, events, photos, email threads, or just plain text. Each entity is internally labeled with its contents, so there is no mistaking a video for an email.

Entities are created and shared in JSON, a format which is designed to be human-readable and is nearly universal with parsing available in most modern programming languages. We also briefly learned last week, that Ledger is also designed to handle JSON objects well. This is certainly no coincidence. Ledger will almost certainly directly keep track of entities, among its other duties.

This is all well and good, but what does this mean for the average user? The Fuchsia team is ready with answers. One of the listed ways for entities to be used is “copy/paste via the clipboard.” It’s still relatively early in the development of Fuchsia, so there’s not a whole lot to go on, but I believe this could mean a more direct way to share things between the modules in a Story. If this is the case, a world of possibilities opens up — things like simplified contact or event sharing, copying a playlist between two unrelated music apps or your browser, and much more could become a reality.

But, for today, let’s stick with what we can prove.

One of the demo programs that used to be available in Fuchsia was called “Music.” This program (so far as I can tell at this early stage) was meant to be a demonstration of various cool things developers can do with Fuchsia. Let’s check out some examples of what it does with entities.

Say a friend of yours sends you a music video from a band you’ve never heard of. YouTube should be able to tag the video with the artist and deliver that info to Fuchsia as an entity. Alone, that wouldn’t mean much. However, the Music app (which doesn’t even have to be open at the time) recognizes the artist entity, gets more information online and gives new context-based suggestions to Assistant. Thinking you might like this new band, you pop open your Now Feed, which is always at the ready. Among your suggestions you’ll see a suggestion to open Spotify or Last.fm to learn more.

![](https://9to5google.com/wp-content/uploads/sites/4/2018/02/struts-suggestion.png)

This functionality isn’t just limited to specific apps like YouTube though. Your browser may also have the ability to pass entities from web pages to Fuchsia. From the documentation:

>This is the set of scripts used to extract entities from web pages. They are injected into web pages loaded by the web view and extract semantic information that can be used to launch modules related to the web content.

Imagine you’re planning a weekend trip to Memphis on your favorite travel booking site. Interested to see if there’s anything to do while you’re in town, you open up your Now Feed. Sitting pretty amongst your suggestions, courtesy of Music and SongKick, is a link to upcoming concerts near the specific hotel you’re looking at.

![](https://9to5google.com/wp-content/uploads/sites/4/2018/02/peabody-suggestion.png)

And this only scratches the surface of what apps will be able to do as they become more connected with the Assistant — the sky is the limit!

For some more info about how Fuchsia is able to make these experiences possible, check out our deep dive into the Maxwell system.

Let us know in the comments how entities might be useful to your workflow.

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：（替换为译者名字和作者地址）；校对： （替换为译者名字和作者地址）       
原文链接：https://9to5google.com/2018/02/09/fuchsia-friday-entities/       
本文链接：https://fuchsia-china.com/×××（发布后替换）
