# Fuchsia Friday: Maxwell和Fuchsia的秘密“特工”
![](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/fuchsia-friday-maxwell.jpg)
本周的Fuchsia Friday，我们来看看广为大家最关心的话题：Maxwell，Fuchsia背后的智能系统组件

Maxwell管理着Fuchsia系统的智能系统，这种智能系统实际上并不是一个大型程序，而是以真正Fuchsia OS风格——从各种较小的程序拼凑而成的。这些程序被称之为代理程序（我们之前已经谈过一些代理程序），我们可以简单地将其视为后台任务。但是，我发现“代理程序”这个命名非常合适：代理在后台运行（秘密特工！），收集信息（就像间谍一样），然后将其报告回传到本地的数据库。

为了更好地理解代理程序工作的工作原理以及其功能，让我们看看三个代理程序在没有任何直接沟通的情况下如何协同工作。第一个代理程序被称为maxwell_btl，它是“基本文本监听器”的缩写。目前，它的功能仅仅是扫描文本中的电子邮件地址，并创建一个电子邮件实体，然后将该实体置于上下文中。

简单地说，上下文是让Maxwell获悉你目前所看到的文本内容和正在进行何种操作的一种途径，但Maxwell只知道它的代理程序告诉它的内容。上下文分为不同的主题，这让代理程序可以仅监听相关上下文的更改。例如，和音乐相关代理程序只希望获取与音频内容相关的用户行为，而不是电子邮件地址相关内容。

当上下文更新后，Maxwell将此次更改通知到所有代理程序，并在需要时进行响应。在这种情况下，代理程序暂时没有实质性运作。我们要关注的是下一个代理程序maxwell_entity_selector。此代理程序侦听文本选择的更改，并检查当前高亮显示的文本是否包含某种“实体”。如果我想要高亮显示电子邮件地址，代理程序将检查该选中文本中包含的实体的上下文，并将电子邮件实体置于不同主题下的上下文中。

一旦maxwell_entity_selector发挥作用，第三个代理程序maxwell_proposal_maker（仅监听突出显示的实体主题）将检测到上下文发生了变化，并为用户给出打开Gmail并撰写电子邮件发送到该地址的建议。

我打算在这个视频中展示一个这样的例子，但最近Fuchsia主仓库代码的变化中断了这个想法。一旦它能正常工作时，我会更新这篇文章，加上视频。总之，这是早期Fuchsia OS仍在开发中的另一个例证。

Maxwell目前使用的还有少数其他代理程序：

- Module_suggester为您在Armadillo主屏幕上看到的搜索框和结果提供支持。对于某些搜索选项，它可以非常简单地使用预加载的结果。这个代理程序可能会全部被替换或大幅扩展。

- Eddystone_agent是另一个简单的示例代理程序，它展示了如何监听Eddystone蓝牙信标并建议打开相关的URL。

![The Eddystone agent at work – Image: @g123k](https://9to5google.com/wp-content/uploads/sites/4/2018/03/eddystone-fuchsia.jpg)

- Usage_log侦听打开的模块（模块是较大的应用程序的一小部分），并向Fuchsia的指标软件Cobalt发送匿名报告。几周前浏览Cobalt日志的Google员工可能会因为一个不熟悉的模块被打开而感到困惑，因为我们最近制作了自己的Flutter应用并在Fuchsia上运行。

到目前为止，大多数这些代理程序似乎都是占位符，并没有实质功能，或者只是如何编写更庞大、更复杂的代理程序的示例。这种情况在我们看到Kronk时发生了改变，Kronk目前是Fuchsia唯一一个有语音回应的代理程序。正如我们几周前所了解的那样，Kronk是Fuchsia团队的Google智能助理的代号。截至目前，Kronk是没有开源的少数几个Fuchsia组件之一。这当然是有道理的，因为它肯定包含谷歌希望保留专有的代码。从我们获得的副本中可以看出，智能助理似乎和往常一样。

这些只是直接包含在Maxwell系统中的代理。代理可以包含在您安装的任何应用程序中，但所有代理都会向Maxwell报告。Maxwell在中间承担中转的工作，代理程序之间不需要交换数据，甚至不需要互相知道彼此的存在。比如Spotify播放器可以告诉座席您正在收听哪首歌，另一个代理程序可以为您提供该歌曲的歌词，而无需直接与Spotify交换数据。

对了，如果你想知道（就像我一样）为何它叫Maxwell。有一种解释是：Maxwell的名字来自60年代电视节目《糊涂侦探》里的秘密特工Maxwell Smart。虽然我并不能完全认同这种解释，但我父亲认为至少这个解释很有趣。

本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：[Arktische](https://github.com/Arktische)；校对：[HugoFun]（https://github.com/HugoFun）      
原文链接：https://9to5google.com/2018/03/23/fuchsia-friday-maxwell/       
本文链接：https://fuchsia-china.com/×××（发布后替换）