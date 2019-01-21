# 谷歌新操作系统 Fuchsia，你需要知道的都在这里

> Fuchisa 最终有望取代 Android，但这需要很多年才可能达成。

Android 和 Chrome OS 是谷歌最为人熟知的两款操作系统，而现在该公司正在进行第三款操作系统的开发，这款新系统名字叫做 Fuchsia。该系统在去年第一次被人们发现时，仅仅能跳出一个简单的命令行。而现在，我们了解到了更多关于该系统的信息。

Fuchsia 看起来和包括 Android 在内的其他移动操作系统完全不同，这应该是个重要要点。而事实上，当前围绕该系统的其他的神秘要点还有非常之多。我们并不知道谷歌开发该系统的真实目的，它是否被定位为 Android 的替代品？ 又或者仅仅是谷歌的一次实验？ 我们能否像期望的那样在今年的谷歌 I/O 大会上见到这款新系统呢？

## Fuchsia 究竟是什么？

Fuchsia 与 Android 和 Chrome OS 这两款系统有点不同，它并不基于 Linux 内核，而是基于谷歌全新开发的一款名叫 Magenta 的内核（译者注： 该内核现已更名为Zircon）。根据谷歌提供的消息， Magenta 开发目标是成为同时适用于现代手机和现代个人电脑的一款系统内核，所以将来我们在智能手机中看到该系统也就不足为奇。此外，我们还不知道为什么的是，谷歌甚至已经将来自苹果公司的编程语言 Swift 添加成为 Fuchsia 的开发语言。

因为 Fuchsia 是使用能在 Android 上运行的 Flutter SDK 编写的，所以 Fuchsia 的大部分模块都可以在Android设备上运行。当前最新版本的 Fuchsia 似乎被称作为 Armadillo，它完全重新实现了一个主屏幕。根据*Ars Technica*的[测试](https://arstechnica.com/gadgets/2017/05/googles-fuchsia-smartphone-os-dumps-linux-has-a-wild-new-ui/)，该主屏幕基本上呈现为一个大的滚动列表，配置信息图片、日期、城市和电池余量图标等被放置在其中央。在该主屏幕的上边，你会看到一些“故事”卡片或者一个最近应用程序列表。而在在该主屏幕下边，你会看到一个类似于 Google Now 的建议列表。

您还可以拖动最近的应用程序，并个性化地将它们组织起来放到主屏幕你想要的位置。如果将一个应用程序放在另一个应用程序的顶部，你将进入最多可支持三个应用程序的分屏模式。

根据 [Hacker News](https://news.ycombinator.com/item?id=12271354) 的消息，曾经参与过NewOS、BeOS、Danger、Palm’s WebOS 和 iOS开发的 *Travis Geiselbrech*，以及参与过 BeOS 和 Android 开发的 *Brian Swetland*，这两个牛人都有参与进 Fuchsia 这一项目。

##　开发 Fuchsia 的目的是什么？

事实上，当前我们并不知道 Fuchsia 为什么而开发。彭博社的[最新报告](https://www.bloomberg.com/news/articles/2018-07-19/google-team-is-said-to-plot-android-successor-draw-skepticism)推测，Fuchsia 是谷歌试图使用单一操作系统去统一整个生态圈的一种尝试，Fuchsia 的目标是能够在谷歌的技术保护伞下，运行于智能手机、智能音响、笔记本电脑等任何合适的设备之上。据某消息人士透露，谷歌计划在未来三年内，先让 Fuchsia 在智能音响和其他智能家具设备上运行起来，然后再转移到笔记本电脑等更大的设备上，并最终取代 Android 成为世界上最大的移动操作系统。

Fuchsia 将取代 Android 这一说法已经出现有一段时间了，*Ars Technica*对此也持[感兴趣的的态度](https://arstechnica.com/gadgets/2017/05/googles-fuchsia-smartphone-os-dumps-linux-has-a-wild-new-ui/)。正如他指出的，Android 早在iPhone 发布之前就已经构建好了，并且其最初是被用作数码相机的操作系统。iPhone 发布后，Android 才被用于手机，而且直至今日谷歌仍然坚持多年前做出的这一选择。谷歌在 Android 上面临许多挑战，例如，它很难在为整个安卓生态系统内的设备推送更新，而 Fuchsia 也许能帮助解决这些问题。

然而，如果放弃 Android 的事情真的发生，依然还有好长一段路需要走。谷歌 CEO *Sundar Pichai* 和副董事长 *Hiroshi Lockheimer* 尚未签署任何针对 Fuchsia 的未来计划，因为这样的变更是一项艰巨的任务。三星、HTC、LG等许多大型手机制造商都还非常依赖于 Android，这使得放弃 Android 变得异常困难。如果谷歌真设法转向 Fuchsia，这对于整个智能手机世界来说都是一场巨大的变革。用于编写 Fuchsia 应用的 Flutter SDK 现已经能够为 Android 和 iOS 应用程序生成代码了，所以开发人员可以尝试通过 Flutter 构建应用，使其开发的应用能够跨所有智能手机操作系统运行。

因为 Fuchsia 的开发还处在早期阶段，我们没能够再获取到其他新的关于该操作系统信息。谷歌已经在手机上测试了这款新的操作系统，同时在 Pixelbook 和 其他笔记本电脑上的[测试](http://www.androidpolice.com/2017/12/30/pixelbook-used-test-googles-fuchsia-os/)也正在进行。如果有获取到更多的信息，我们会第一时间在这篇文章上进行更新。

##　关于 Fuchsia 的一些传闻

迁移到 Fuchsia 对谷歌有什么好处呢？ 事实证明，好处有很多。正如前文提到的，Android 最初是为数码相机而构建的，后来才被应用到带触摸屏的手机中。Android 大部分内容并不符合[谷歌对智能设备的未来期望](https://www.bloomberg.com/news/articles/2018-07-19/google-team-is-said-to-plot-android-successor-draw-skepticism)，比如语音交互方面。Fuchsia 将会为谷歌解决许多这样问题，进而为谷歌带去更多的机会。

Fuchsia有一套相较于 Android 更为健壮的安全特性，软件内置了加密的用户密钥以加强安全性。与Android相比，Fuchsia 在适应各种不同尺寸的屏幕方面也更胜一筹。在未来，或许能为从门铃到烤面包机等所有设备提供支持。通过向 Fuchsia 的转移，谷歌可以摆脱 Java 和围绕 Java 的的一些法规问题。同时这意味着谷歌可以抛弃在 Android 占据核心位置的 Linux 内核。

当然，Fuchsia 还是一个非常早期的版本，如果某些细节随着时间而改变了，不要感到惊讶。根据[彭博社的报道](https://www.bloomberg.com/news/articles/2018-07-19/google-team-is-said-to-plot-android-successor-draw-skepticism)，谷歌内部已经就 Fuchsia 的一些安全措施产生了一些争论，因为这些措施会使的谷歌的广告业务变得更加困难。

##　自己去尝试使用 Fuchsia 吧

到五月初，你就可以亲自尝试使用 Fuchsia 了。[SlashGear](https://www.slashgear.com/this-is-google-fuchsia-os-preview-apk-download-for-android-09484448/) 与 *HotFix Computer Repair* 合作推出了一个可下载的Android软件包套件（APK），你可以将它安装在自己手机上以体验 Fuchsia。这个安装包有点像是一个上文提到的被称为 Armadillo 的 alpha 版本系统的预览版启动器。Armadillo 是 Fuchsia 这一操作系统的一个版本名，类似于 Nougat 是 Android 操作系统的一个版本名。

自己去[HotFixIt](https://www.hotfixit.net/single-post/2017/05/03/How-to-build-Armadillo)下载吧，不过在此之前你需要确保明白一些事情。Fuchsia 目前还处于早期阶段，不要期望能够将其作为日常使用的操作系统。虽然在大多数 Android 手机上使用这一高度实验性的软件是相对安全的，但你也应该在清楚自己在干什么的前提下才去这么做。

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Joe Osborne； 译者：[Hzcyf](https://github.com/Hzcyf) ；校对：[bootingman](https://github.com/bootingman)  
原文链接：[DigitalTrends：Google’s Fuchsia OS: Everything you need to know](https://www.digitaltrends.com/mobile/google-fuchsia-os-news/)
本文链接：https://fuchsia-china.com/google-fuchsia-os-rumors/
