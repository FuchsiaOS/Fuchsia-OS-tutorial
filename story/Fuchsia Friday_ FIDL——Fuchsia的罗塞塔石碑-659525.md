#Fuchsia Friday: FIDL is the Rosetta Stone of Fuchsia
#Fuchsia Friday: FIDL——Fuchsia的罗塞塔石碑
![](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/05/fuchsia-friday-fidl.png)

本周，在所有开发者对Google I/O的积极响应下，我们将继续Fuchsia Friday这一面向开发者的主题。

现代程序员通常会用不止一种编程语言，他们会根据编程语言的独特优势选择一种语言，来应对手上的挑战。但事情不总如此，一些开发人员只使用他们所熟悉的一种语言（通常是JavaScript），并用它来处理各种问题。更糟糕是，有时平台或操作系统本身对编程语言的使用作出了限制。

无论你身处编程知识的哪个领域，Fuchsia都希望能够适应你的需求，而不是支配你应该如何完成工作。为此，Fuchsia团队创造了FIDL。FIDL分为两部分，一部分是FIDL（**F**uchsia **I**nterface **D**efinition **L**anguage）本身，另一部分是一个将各种语言连接在一起的底层系统。

到目前为止，FIDL支持5种语言，未来很可能还会有更多

- Dart – 一种由谷歌创造的语言，Java和JavaScript开发者对它应该感到熟悉，Dart也是Flutter的主要开发语言。
- Go – 另一种谷歌编程语言，主要用于网络服务器
- C++ / C – 两种可信的语言，特别适用于底层编程
- Rust – Mozilla对开发C++替代品的一次成功尝试

假设你用Go语言编写了一个库，但希望在Dart（或Flutter）应用程序中使用它。你要使用FIDL语言创建一个“接口”（interface），并将其作为“实现”（implementation）连接到Go代码。然后，FIDL系统将为所有支持的语言生成“绑定”（bindings），这样就可以在Dart中使用Go代码了。

现在假设过了一段时间后，你觉得到Go语言并不是这项完成工作的最佳工具，于是你决定用Rust重写这个库。使用FIDL，也能够将你的Rust代码指定为新的实现，这样就完工了，过程十分简单。你的Dart代码无需更改，因为FIDL接口没有更改，这就是简化版的FIDL应用。

有趣的是，FIDL系统在Fuchsia开发中非常普遍，Fuchsia团队甚至为VS Code开发了一个插件，来帮助使用者编写更好的FIDL代码。

如果你有兴趣了解更多关于FIDL以及如何使用它的信息，请参阅Fuchsia文档中的官方教程。在该页面上，您可以找到简单的示例，比如如何从Dart调用C++代码，反之亦然。
***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：[659525]（https://github.com/659525）；校对：[HugoFun]（https://github.com/HugoFun）
原文链接：https://9to5google.com/2018/05/11/fuchsia-friday-fidl-is-the-rosetta-stone-of-fuchsia/       
本文链接：https://fuchsia-china.com/×××（发布后替换）
