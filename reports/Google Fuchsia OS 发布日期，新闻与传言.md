# Google Fuchsia OS 发布日期，新闻与传言
### 谷歌Android-Chrome混合操作系统的未来

![](https://cdn.mos.cms.futurecdn.net/hRqGxFF2CZZJ4rEvjC27Uk-970-80.jpg)
 
一直以来，我们都期待着谷歌正式发布Fuchsia，或Google Andromeda—一款Chrome和Android操作系统（OS）的融合系统。早在2017年10月它就进入了人们的视线，但谷歌从未正式发布过声明。

那么Google Fuchsia将以什么样的定位发布呢？虽然Google Pixelbook和一些很棒的Chromebook能够通过Google Play商店运行Android应用程序，甚至是运行早期版本的Fuchsia，但我们认为成品（如果它已经完成的话）可能会最终成为Google压轴的跨全平台的操作系统。

事实上我们并不知道谷歌对Fuchsia的最终定位到底如何，有关Fuchsia的信息仍然是云里雾里。因此，无论它或者它将运行的软件的未来是否光明，我们至少能确定Google Fuchsia的核心思想是能够使用户在手上的任何设备上做任何想做的事情。这些在Google最近的一些行动中都能窥见一斑，比如将Android Message和VR视频编辑器移植到各种设备上，谷歌的实际行动让人们对Fuchsia抱有信心。

通过Google Pixel Slate，即使我们没有接触过实际发布的Fuchsia，我们已能瞥见Fuchsia的未来。借助这款新的平板电脑，谷歌已经改变了平板电脑操作系统的UI界面，使平板电脑更加美观—使其在不同平台上的风格更加统一。尽管这是否与Fuchsia有关还有待观察，但它可能是朝着正确方向迈出的一步。

因此，无论最终产品会是什么样子，又或者Google Fuchsia是否能向公众发布，请务必将此页面加入书签，因为我们将随时更新它。

## 切入正题

* Fuchsia是什么？一款集合Android和Chrome的跨全平台操作系统
* 什么时候发布？早期版本现在已经在Google Pixelbook上可用
* 它会收费吗？很可能不会，就像Android和Chrome一样开源免费

![](https://cdn.mos.cms.futurecdn.net/by9zV74tBzsBeoHUq8vWRF-650-80.jpg)
运行Fuchsia OS早期版本的Google Pixelbook（图片来源：Ars Technica）

## Google Fuchsia究竟是什么？

目前，Google内部对于Fuchsia的定位还存在着分歧。虽然研发团队表示，他们希望Fuchsia成为谷歌操作系统压轴产品，运行在所有手机、平板电脑、笔记本电脑和智能家居设备上，但谷歌的领导层仍称之为实验性项目。所以我们只需静观其变，拭目以待这项实验的最终结果。

那么回到标题，Google Fuchsia是一个混合操作系统，并且当前仍处于开发阶段。根据9to5Google的说法，整个Fuchsia OS由两个截然不同但相互关联的用户界面（UI）组成：一个以移动设备为中心的，代号为“Armadillo”的用户界面，和一个内部称为“Capybara”的传统桌面用户界面。

到目前为止，有关移动版Fuchsia的信息相较桌面版更为人所知，但在最近，ArsTechnica已经能够在非常原始粗陋的状态下使用Google Pixelbook运行Fuchsia了。 

根据硬件将操作系统划分为两个独立的用户界面是一套由微软创造的经典举措。如今Windows 10已经扩展到多个平台，其界面呈现具体取决于它是应用于台式计算机，手机，平板电脑还是游戏机上。实际上，Windows 10在所有硬件平台上只有内核是统一的，它是控制操作系统（OS）绝大部分功能的核心部分。

对Fuchsia而言，其内核被称为“Zicron”，它被设计为始终可以升级更新。Fuchsia不仅让应用程序可以安全地持续访问内核，并且添加额外的安全层来消除应用程序与更新后的操作系统（OS）不兼容的情况。

无论是移动端还是桌面端，Fuchsia都充满了谷歌的Material设计风格，这种风格同时也遍布其Android和Chrome OS产品。阴影是Fushsia设计美学的一大焦点，它使用了一种基于Vulkan的，名为“Escher”的图形渲染器来完成这项工作。渲染出的界面相较传统的扁平化OS产品更具深度。

> Vulkan是一种跨平台的高性能低开销的图形API,在移动设备上相较于OpenGL ES有更好的表现。 ———译注

![](https://cdn.mos.cms.futurecdn.net/HbYTJFEiZxTfzHw6cTuSyb-650-80.jpg)

Fuchsia也着力于使用基于卡片的用户界面设计，用户打开的应用程序都会呈现在一张张的卡片中。此外，用户还可以将多个应用程序放入同一张卡片中。这使得用户能集中精力于手头的任务，而不是频繁切换应用程序。Google开发了一种名为Flutter的新型跨平台移动应用开发框架，使得这些应用在不同设备上有着相同的外观。

除此之外，Google Fuchsia围绕着Google智能助理做了进一步的适配，Google Assistant将能更深入地访问和使用用户的应用和信息，以提供更多操作和建议。从GitHub上Fuchsia开发人员页面来看，谷歌将这些应用程序和信息称为实体（entities），而且这些应用程序都可以通过Fuchsia上的Google智能助理访问。我们甚至看过了最近的一个demo，进一步佐证了Google智能助理在Fuchsia中的深度嵌入。

根据9to5Google的一份报告，谷歌似乎也在改变收集Fuchsia内部分析数据的方式。Fuchsia上将部署一个名为“Cobalt”的新的分析程序，该程序会收集用户在操作系统中如何使用应用程序的信息。据称Cobalt是谷歌对安全操作系统采取安全措施的一部分，只是加密部分的工作还没有完成。但是，我们确信谷歌最终会更好地使用Cobalt提供安全保障。

根据9to5谷歌的一份报告，谷歌Chrome或者至少某一个早期的Chromium版本，已经能够在早期版本的Google Fuchsia上运行。虽然Fuchsia还没有做好发布的准备，但这确实表明这个新生代操作系统越来越接近可以使用的程度了。

最后，Fuchsia有希望成为迄今为止最好的跨设备操作系统。为实现这一目标，Fuchsia使用了GitHub社区称为“Ledger”的新工具。一旦用户在Fuchsia设备上登录Google帐户，Ledger将自动在所有Fuchsia设备的所有已安装应用中保存用户的进度。

总而言之，Fuchsia是谷歌将Chrome和Android中的最佳产品整合到同一个操作系统中的一次尝试，无论你是否正在使用它，它都在任何时候都会比以往高效，更不用说跨平台使用了。

![](https://cdn.mos.cms.futurecdn.net/fxydjj4gT6cVRrcndtYnSF-650-80.jpg)
Google I/O大会可能就是今后Fuchsia亮相的地方

## Google Fuchsia发布日期

自2016年8月以来，我们已经看到了不计其数的关于Google Fuchsia发布日期的传言，但都被证明是假的。这些传言通常出现在谷歌在加利福尼亚举行的Google大型IO开发者活动之前，或者大型硬件发布即将来临时。

据透露，早在二月份，谷歌前安卓平台安全负责人Nick Kralevich就已经离开Android团队，加入到Fuchsia部门的“define security”小组中。Kralevich将其描述为“新的实验性的操作系统”，但并没有向我们展示Fuchsia任何的窗口启动界面，但这确实显示了谷歌已经将Fuchsia置于其最重要资源的位置。

据现有情况推断，未来三年内，Fuchsia将仅在智能家居设备上运行，未来五年内，将公开发布全功能版本。然而，这似乎是一个不太可信的谣言，如果我们看到它在2024年之前发布（或者实际上是Android系统），我们会感到非常惊讶。

但是，最近通过Android开源项目传出的开发者消息暗示了某些动作，其中一份提交中提到了两个分支，9to5Google的人们将其理解为“并入官方Fuchsia SDK”。另一份提交中提到了华为荣耀Play智能手机，所以我们很快就能看到在实际设备上测试Fuchsia了。

无论如何，请持续关注此页面，当接近可能的发布日期时，我们会为您提供更多关于Fuchsia的重要信息。

![](https://cdn.mos.cms.futurecdn.net/Yzh9gjppGL6MBnWbE2QTVd-650-80.jpg)

Fuchsia会是Android的终结者吗？

## Fuchsia对于Android和Chrome以及Windows和macOS意味着什么？

舆论称Fuchsia是谷歌对微软和苹果统一平台的回击。无论是将Android变成两大智能手机平台之一，还是后来推广Chrome操作系统——更不用说谷歌基于网络的生产力计划G-Suite，谷歌俨然已经成为所有平台上的主要参与者。

从谷歌透露出的消息来看，谷歌正着手完成微软和苹果产品所具有的大部分功能，这些产品包括Windows 10，iOS和macOS High Sierra。当然，是以非常“Google”的方式完成的。用户可以轻松地获得Google无与伦比的搜索和数据跟踪功能——Google智能助理和“entities”，以及一个不断发展的用户界面，以满足访问其设备的需求。这些是Fuchsia比微软和Apple的产品更具吸引力的的宣传点。

Fuchsia最终会意味着Android和Chrome的终结吗？在名义上，这确实很有可能，但是后两者的设计原则几乎肯定会继续存在下去，Fushsia有很多的设计基础并不是建立在这些原则之上的。只需看看在最近两个版本的Fuchsia的早期版本中找到的Material设计语言，就能略知一二。

最终看来，大家可能会在今年晚些时候的看到Fushsia的预览版，或者在2019年上市的设备中看到它，这将是谷歌注入精力最多的一个平台。借助Fuchsia，Google将能够同时向所有版本推送新的更新和功能，从而简化技术支持以及用户对产品的使用。

有了Fuchsia，谷歌将成为微软和苹果公司的一个更强大的敌人，这对Android和Chromebook用户来说是一个非常诱人的选择。谁知道呢？或许这足以让人们从微软和Apple产品阵营中投入Fuchsia的怀抱。

***
本文原作者：Joe Osborne 译者：[Arktische](https://github.com/Arktische) ；校对：[HugoFun](https://github.com/HugoFun)
原文链接:https://www.techradar.com/sg/news/google-fuchsia 本文链接：

