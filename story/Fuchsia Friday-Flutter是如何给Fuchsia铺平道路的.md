
Fuchsia Friday：Flutter是如何给Fuchsia铺平道路的（还有我们的第一个Fuchsia app！）
Kyle Bradshaw
- 3/2/2018 17:29
![](https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/fuchsia-friday-Flutter.png)

本周早些时候，谷歌新推出的跨平台移动应用框架Flutter进入了Beta测试阶段。为了庆祝这一点，让我们仔细看看Flutter现在为应用程序开发所做出的贡献，以及它是如何为Fuchsia准备类似的开发者和用户。

Flutter 是一个开源、跨平台的移动应用开发框架。它现在支持iOS和安卓开发，并在将来有着支持桌面开发的可能性。Flutter通过它强大的跨平台性能，将自己与竞争对手（如React、Native和Xamarin）区分开来。

通过使用“材料设计”(Material Design)，Flutter应用程序在iOS上与在Android上将会看起来完全相同。此外，Flutter支持dart语言，这使得有着不同开发背景的开发人员都能熟悉Flutter。

如果你需要一点关于Flutter是什么的介绍，请看谷歌上周刚发布的新视频：
![]()
（说明：该视频届时将上传到网站服务器上）

事实上，我在业余时间使用Flutter进行开发已经有一年时间了，我感觉Flutter很好用。为了今天的演示，我花了大约半小时做了一个9to5Google演示app。这个app所做的只是提供一个电话列表以供阅读。它非常简单，而且更像是一个模型而不是一个完整的app（例如，它需要手动录入数据），但是它可以被轻易地转变成更有用的东西。

![VS Code中的Flutter工程](https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/screenshot-from-2018-03-02-12-25-36.png)
![运行在Android中的app示例](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/capture_2018-03-02-12-29-53.png)

以上便是精彩Flutter的内容, 但你可能在想“为什么标题是Fuchsia星期五？”。如果是，那你问对了。你看到的所有Fuchsia里的东西都由Flutter驱动的。我们第一次发现这个是在5月份，在Android Armadillo预览发布的时候。接下来，我会告诉你一些事情。

首先，Flutter的小组件系统是非常灵活的。除了传统的Material Design小部件和包含的“Cupertino”（iOS风格）小部件外，开发人员还可以创建自己的定制设计小部件来满足他们的需求。这种设计定制小部件的能力是许多Fuchsia用户界面的核心，比如Now feed。

![使用了Flutter的Now Feed – Image: Ars Technica](https://9to5google.com/wp-content/uploads/sites/4/2018/03/google-fuchsia-1-2018-28-1440x1080.jpg)

其次，很明显Flutter不会很快消失或被抛弃。从2017年的I/O大会Flutter的出现和2018年的I/O大会上Flutter的重大更新来看，谷歌在Flutter上下了很大的赌注。如果Fuchsia在以后会很重要的话，推出Flutter将是谷歌的明智之举--在强制开发者切换到Flutter之前让他们使用Flutter，这使得他们更能够熟悉Flutter。

不过，这项计划还有另一个目的。正如一些人所指出的，创建新的操作系统最困难的事情之一就是可能缺少第三方应用程序。大多数人不会购买没有好应用程序的设备，开发人员也不会为没有销售的设备制作应用程序。然而，他们可能没有意识到，当他们通过使用Flutter制作android&ios应用时，同时也准备好了Fuchsia的应用程序了！

本周，我可以编译Fuchsia并在Pixelbook上运行（干杯，Ben！）。还记得之前的演示应用程序吗？我只需一个简单的复制粘贴，这个应用程序就可以完美地在Fuchsia上运行。就像这个样子。

![](https://9to5google.com/wp-content/uploads/sites/4/2018/03/20180302_173431.jpg)

当然，Fuchsia还有一些可以丰富您的体验的特定功能（请参阅我们的实体细分中的一个例子），甚者，在Fuchsia发布之前，就已经有数百个兼容的应用程序以备将来使用了。这样一来，人们很容易对Flutter感兴趣。如果你想了解更多，并想赢在Fuchsia的起跑线上的话，推荐你看看Flutter的入门指南。

Fuchsia Friday是一个新的系列报道，我们将深入研究Fuchsia源代码，并解释操作系统的当前状态可能对成品意味着什么。本文中的所有信息都是基于可用信息的推测，在将来可能会发生更改。
***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：[firecckk](https://github.com/firecckk)；校对： [HugoFun](https://github.com/HugoFun)       
原文链接：https://9to5google.com/2018/03/02/fuchsia-friday-first-fuchsia-app/        
本文链接：https://fuchsia-china.com/×××（发布后替换）
