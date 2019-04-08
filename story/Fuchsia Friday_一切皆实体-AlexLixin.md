
<!-- #Fuchsia Friday: Everything is an Entity -->
# Fuchsia Friday：一切皆实体
![](https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/02/entities.png)

<!-- Two weeks ago, we learned about Fuchsia’s Stories and Modules, and how they will help us better organize our time, tasks, and ideas. This week, we’re looking at the idea of ‘entities’, Fuchsia’s attempt to catalog the digital world to be read by Assistant. Entities are also part of the glue that holds disparate “modules” together into one coherent Story. -->
两个星期前，我们了解到Fuchsia的故事（story）和模块（module），也了解了它们是如何帮助我们更好地组织我们的时间、任务和想法。这周，我们来看看“实体”这个概念，Fuchsia试图给Assistant所理解的数字世界分类。实体也是将独立的“模块”组合成一个连贯故事的一种粘合剂。

<!-- In the Fuchsia docs, an entity is described as “an identifiable person, place, thing, event, or concept […] which can be referenced, retrieved, presented, manipulated, or shared.” By this definition, almost anything can be an entity, but some more specific examples given include bands, hotels, contacts, events, photos, email threads, or just plain text. Each entity is internally labeled with its contents, so there is no mistaking a video for an email. -->
在Fuchsia文档中, 一个实体被描述为“一个可以被引用、检索、呈现、操作或者共享的可辨识的人、地点、事物、事件或者概念[...]”，根据这个定义，几乎任何事物可以称为实体，但是以下是一些更具体的例子：包括乐队、旅馆、触点、事件、照片、电子邮件线程，或仅仅是纯文本。每个实体本质上以它的内容为标记，因此拿一封电子邮件来说，不会搞错它的视频内容。

<!-- Entities are created and shared in JSON, a format which is designed to be human-readable and is nearly universal with parsing available in most modern programming languages. We also briefly learned last week, that Ledger is also designed to handle JSON objects well. This is certainly no coincidence. Ledger will almost certainly directly keep track of entities, among its other duties. -->
实体是用JSON创建和共享的，JSON是一种被设计为方便人类阅读的数据格式，它在大多数现代编程语言中的解析几乎完全通用。上周我们还简略地学习了Ledger，它是为了很好地处理JSON对象而设计的。这当然不是巧合。在它的其他职责中，Ledger几乎理所当然地会直接地跟踪实体。

<!-- This is all well and good, but what does this mean for the average user? The Fuchsia team is ready with answers. One of the listed ways for entities to be used is “copy/paste via the clipboard.” It’s still relatively early in the development of Fuchsia, so there’s not a whole lot to go on, but I believe this could mean a more direct way to share things between the modules in a Story. If this is the case, a world of possibilities opens up — things like simplified contact or event sharing, copying a playlist between two unrelated music apps or your browser, and much more could become a reality. -->
这当然皆大欢喜，但是这对普通用户意味着什么呢?为此Fuchsia小组准备了一些答案。其中之一就是实体可以“通过剪切板复制/粘贴”。Fuchsia的开发还处于相对早期的阶段，所以还没有太多进展，但我认为这可能意味着在一个故事（Story）中可以更直接地在模块之间共享内容。在这种情况下，就会出现一个充满可能性的世界——简化的联系或事件共享、在两个不相关的音乐应用程序或浏览器之间复制播放列表，以及更多的可能性。

<!-- But, for today, let’s stick with what we can prove. -->
然而，对当下来说，让我们坚持那些我们可以证明的事物。


<!-- One of the demo programs that used to be available in Fuchsia was called “Music.” This program (so far as I can tell at this early stage) was meant to be a demonstration of various cool things developers can do with Fuchsia. Let’s check out some examples of what it does with entities. -->
在Fuchsia中有一个演示程序叫做“Music”，这个程序(就目前的早期阶段而言)旨在展示开发人员可以使用Fuchsia做的各种很酷的事情。让我们来看一些它处理实体的例子。

<!-- Say a friend of yours sends you a music video from a band you’ve never heard of. YouTube should be able to tag the video with the artist and deliver that info to Fuchsia as an entity. Alone, that wouldn’t mean much. However, the Music app (which doesn’t even have to be open at the time) recognizes the artist entity, gets more information online and gives new context-based suggestions to Assistant. Thinking you might like this new band, you pop open your Now Feed, which is always at the ready. Among your suggestions you’ll see a suggestion to open Spotify or Last.fm to learn more. -->
假设你的一个朋友给你发送了一个你从未听过的乐队的音乐视频。YouTube应该能够给视频加上艺术家的标签，并把这些信息作为一个实体传递给Fuchsia。仅仅如此，这并不意味着什么。然而，这款音乐应用(当时甚至不需要打开)可以识别艺术家实体，在线获取更多信息，并向Assistant提供基于上下文的新推荐。考虑到你可能会喜欢这个新乐队，你打开你的Now Feed，它总是随时准备着。在给你的推荐中，你会看到一个推荐建议你打开Spotify或Last.fm来了解更多。

![](https://9to5google.com/wp-content/uploads/sites/4/2018/02/struts-suggestion.png)

<!-- This functionality isn’t just limited to specific apps like YouTube though. Your browser may also have the ability to pass entities from web pages to Fuchsia. From the documentation: -->
不过，这一功能并不仅限于YouTube等特定应用。您的浏览器还可以将实体从web页面传递到Fuchsia。

请看以下文档文档:

<!-- >This is the set of scripts used to extract entities from web pages. They are injected into web pages loaded by the web view and extract semantic information that can be used to launch modules related to the web content. -->
> 这是一组用来从web页面中提取实体的脚本。它们被注入到被web view所加载的web页面中，并提取可用于启动与web内容相关的模块的语义信息。

<!-- Imagine you’re planning a weekend trip to Memphis on your favorite travel booking site. Interested to see if there’s anything to do while you’re in town, you open up your Now Feed. Sitting pretty amongst your suggestions, courtesy of Music and SongKick, is a link to upcoming concerts near the specific hotel you’re looking at. -->
想象一下，你正在你最喜欢的旅游预订网站上计划周末去孟菲斯旅行。你打开你的Now Feed，看看在那里有哪些你感兴趣的事情可以去尝试。在Music和SongKick的帮助下，在给你的推荐中有一个有趣的链接，可以链接到你正在查看的特定酒店附近即将举行的音乐会。

![](https://9to5google.com/wp-content/uploads/sites/4/2018/02/peabody-suggestion.png)

<!-- And this only scratches the surface of what apps will be able to do as they become more connected with the Assistant — the sky is the limit! -->
而这仅仅是应用程序和Assistent配合下最浅层的应用——除此之外还有无限的可能性！

<!-- For some more info about how Fuchsia is able to make these experiences possible, check out our deep dive into the Maxwell system. -->
要了解更多关于Fuchsia如何实现这种体验的信息的话，请查看我们对Maxwell系统的深入研究。

<!-- Let us know in the comments how entities might be useful to your workflow. -->
请在评论中让我们知道实体是否对您的工作流程有所帮助。

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：[AlexLixin](https://github.com/AlexLixin)；校对： [HugoFun](https://github.com/HugoFun)       
原文链接：https://9to5google.com/2018/02/09/fuchsia-friday-entities/       
本文链接：https://fuchsia-china.com/×××（发布后替换）
