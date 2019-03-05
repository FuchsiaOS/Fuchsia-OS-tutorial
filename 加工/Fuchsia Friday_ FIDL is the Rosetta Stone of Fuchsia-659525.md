#Fuchsia Friday: FIDL is the Rosetta Stone of Fuchsia
#Fuchsia Friday: FIDL——Fuchsia的罗塞塔石碑
![](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/05/fuchsia-friday-fidl.png)

With all the developer excitement following Google I/O this week, we’re keeping in theme with a developer-oriented Fuchsia Friday.
在本周Google I/O之后所有开发者的积极响应下，我们将继续与一个面向开发者的Fuchsia周五主题。

The modern programmer usually has more than one programming language under their belt, with each one bringing its own unique strengths to the challenge at hand. This isn’t always the case, with some developers taking one language they know (usually Javascript) and throwing it at every problem known to man. Or worse, sometimes the platform or OS itself restricts the languages one can use.
现代程序员通常会不止一种编程语言，而每一种语言对于未来的挑战都有自己独特的优势。然而，一些开发人员使用他们所熟悉的一种语言（通常是JavaScript），并用它来处理各种问题。遗憾的是，单一的语言有时候会受到平台或操作系统本身的限制。

Wherever you may fall in the programming knowledge spectrum, Fuchsia wants to accommodate you, instead of dictating how you are supposed to get the job done. To do this, the Fuchsia Team has created FIDL. FIDL works in two parts, the Fuchsia Interface Definition Language itself, and an underlying system that connects the various languages together.
无论您身处编程知识的哪个领域，Fuchsia都希望能够适应您的需求，而不是支配您应该如何完成工作。为此，Fuchsia团队创建了FIDL。FIDL分为两部分，一部分是FIDL本身，另一部分是一个将各种语言连接在一起的底层系统。

As of now, FIDL supports 5 languages, with more likely coming in the future
到目前为止，FIDL支持5种语言，更贴近未来

- Dart – A language created by Google that should make Java and Javascript devs feel at home. Also the primary language for Flutter.
- Dart – 一种由谷歌创建的语言，它应该让Java和JavaScript开发者感到熟悉，也是Flutter的主要语言。
- Go – Another Google language, primarily used in web servers
- Go – 另一种谷歌语言，主要用于网络服务器
- C++ / C – Two trusty languages, especially useful for low-level programming
- C++ / C – 两种可信的语言，特别适用于底层编程
- Rust – Mozilla’s relatively successful attempt at a replacement for C++
- Rust – Mozilla尝试的一种C++替代品

Let’s say you write a library in Go, but want to use it in a Dart (or Flutter) application. You should be able to use the FIDL language to create an ‘interface’ and connect it to your Go code as an ‘implementation.’ The FIDL system will then generate ‘bindings’ for all supported languages, so you can use your Go code in Dart.
假设您用Go语言编写了一个库，但希望在dart（或flutter）应用程序中使用它。您应该使用FIDL语言创建一个“接口”，并将其作为“实现”连接到Go代码。然后，FIDL系统将为所有支持的语言生成“绑定”，这样您就可以在Dart中使用Go代码。

Now perhaps some time has passed, you realized that Go wasn’t really the best tool for the job, and decided to rewrite the library in Rust. With FIDL, you should be able to specify your Rust code as the new implementation. That’s it. You’re done. Your Dart code shouldn’t change, because the FIDL interface didn’t change. That’s the simplified version, anyway.
过了一阵子，你觉得到Go语言并不是这项工作的最佳工具，于是决定用Rust重写这个库。使用FIDL，您也能够将您的Rust代码指定为新的实现，过程十分简单。因为FIDL接口没有更改，您的Dart代码也无需更改。这就是简化版。

Interestingly, the FIDL system is in such common use in Fuchsia development that the Fuchsia Team has even developed an extension for VS Code to assist in writing better FIDL code.
有趣的是，FIDL系统在fuchsia开发中非常普遍，以至于fuchsia团队甚至开发了一个vs插件来帮助编写更好的FIDL代码。

If you’re interested in learning more about FIDL and how to use it, check out the official tutorial in the Fuchsia documentation. On that page, you can find simple examples of calling C++ code from Dart and vice versa.
如果您有兴趣了解更多关于FIDL以及如何使用它的信息，请参阅Fuchsia文档中的官方教程。在该页面上，您可以找到简单的示例，比如如何从Dart调用C++代码，反之亦然。
***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：（替换为译者名字和作者地址）；校对： （替换为译者名字和作者地址）       
原文链接：https://9to5google.com/2018/05/11/fuchsia-friday-fidl-is-the-rosetta-stone-of-fuchsia/       
本文链接：https://fuchsia-china.com/×××（发布后替换）
