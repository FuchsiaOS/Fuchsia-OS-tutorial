# Google Fuchsia OS 发布日期，新闻与传言
### 谷歌Android-Chrome混合操作系统的未来

![](https://cdn.mos.cms.futurecdn.net/hRqGxFF2CZZJ4rEvjC27Uk-970-80.jpg)
一直以来，我们都期待着谷歌正式发布Fuchsia，或Google Andromeda—Chrome和Android操作系统（OS）的融合系统- 早在2017年10月就进入了人们的视线，但谷歌从未正式发布过声明。

那么，Google Fuchsia将以什么样的定位发布呢？好吧，虽然Google Pixelbook和一些最好的Chromebook能够通过Google Play商店运行Android应用程序，甚至是早期版本的Fuchsia本身，但我们认为最终产品 - 如果它已经完成的话 - 可能会最终成为Google第二个跨全平台的操作系统。

事实是我们并不知道谷歌对Fuchsia的定位到底如何 - Fuchsia的信息仍然很难得到。因此，无论它或者它将运行的软件的未来是否光明，我们至少能确定Google Fuchsia的核心思想是能够使您使用的任何设备上做任何您想做的事情。这些在Google最近的一些行动中都能窥见一斑 - 比如将Android Message和VR视频编辑器移植到各种设备上——谷歌的实际行动让人们对Fuchsia抱有信心。

通过Google Pixel Slate，我们已能瞥见Fuchsia的未来—即使我们没有接触过实际发布的Fuchsia。借助这款新平板电脑，谷歌已经改变了平板电脑操作系统的UI界面，使平板电脑更加美观—使其在不同平台上的风格更加统一。它是否与Fuchsia 有关还有待观察，但它可能是朝着正确方向迈出的一步。

因此，无论最终产品会是什么样子，Google Fuchsia是否向公众发布，请务必将此页面加入书签，因为我们将随时更新它。

## 切入正题

* Fuchsia是什么？Android-meets-Chrome，跨全平台操作系统
* 什么时候发布？现在可以在Google Pixelbook上获取早期版本
* 它会收费吗？很可能不会，就像Android和Chrome一样开源免费

![](https://cdn.mos.cms.futurecdn.net/by9zV74tBzsBeoHUq8vWRF-650-80.jpg)
运行早期版本的Fuchsia OS的Google Pixelbook（图片来源：Ars Technica）

## Google Fuchsia究竟是什么？

目前，Google内部对于Fuchsia的定位还存在着分歧。虽然它的研发团队表示，他们希望Fuchsia成为倒数第二的谷歌操作系统，运行在所有手机，平板电脑，笔记本电脑和智能家居设备上—但谷歌的领导层仍称之为实验性项目。所以，我们只需静观其变，拭目以待此实验的最终结果。

那么回到标题，Google Fuchsia是一个混合操作系统，当前仍处于开发阶段。根据9to5Google的说法，整个Fuchsia OS由两个截然不同但相互关联的用户界面（UI）组成：一个以移动设备为中心的代号为“Armadillo”的用户界面和一个内部称为“ Capybara ”的传统桌面用户界面。

到目前为止，有关移动版Fuchsia的信息相较桌面版更为人所知，但最近ArsTechnica已经能够在一个非常原始的状态下使用Google Pixelbook运行Fuchsia。 

根据硬件将操作系统划分为两个独立的用户界面是一套由微软创造的的经典的移动解决方案。如今Windows 10已经扩展到多个平台，其界面呈现具体取决于它是否与台式计算机，手机，平板电脑或游戏机一起使用。实际上，Windows 10在所有硬件平台上唯一的统一程序是它的内核，它是控制OS绝大部分功能的核心部分。

对Fuchsia而言，其内核被称为“Zicron”，它被设计为始终可以升级更新。Fuchsia不仅让应用程序可以安全地持续访问内核，并且添加额外的安全层来消除应用程序与更新后的OS不兼容的情况。

无论是移动端还是桌面端，Fuchsia都充满了谷歌的Material Design风格，这种风格同时也遍布其Android和Chrome OS产品。阴影是该设计审美的一大焦点，Fuchsia使用了一种基于Vulkan的名为“Escher”的图形渲染器来完成这项工作。渲染效果结果相较传统的扁平化设计的OS产品更具深度。

> Vulkan是一种跨平台的高性能低开销的图形API,在移动设备上相较于OpenGL ES有更好的表现。 ———译注

![](https://cdn.mos.cms.futurecdn.net/HbYTJFEiZxTfzHw6cTuSyb-650-80.jpg)

Fuchsia也非常关注基于卡片的用户界面，您打开的每个应用程序都会出现在其中一张卡片中——此外，您可以将多个应用程序放入一张卡片中。这使得用户能集中精力于手头的任务而不是频繁切换应用程序。由于Google开发了一种名为Flutter的新型跨平台移动应用开发框架，因此可以预计这些应用在不同设备上的外观相同。

除此之外，Google Fuchsia围绕着Google智能助理做了进一步的适配，Google Assistant将能更深入地访问和使用您的应用和信息，以提供更多操作和建议。根据GitHub上Fuchsia开发人员页面来看，谷歌将这些应用程序和信息称为“实体”，而且这些应用程序都可以通过Fuchsia上的Google智能助理访问。我们甚至看过最近的一个demo，进一步佐证了Google智能助理在Fuchsia中的深度嵌入。

根据9to5Google的一份报告，谷歌似乎也在改变收集Fuchsia内部分析数据的方式。Fuchsia将见证一个名为“Cobalt”的新分析程序的实施，该程序将收集有关您如何在操作系统中使用应用程序的信息。据称Cobalt是谷歌对安全操作系统采取安全措施的一部分，但加密部分的工作还没有完成——但是，我们确信谷歌最终会更好地为Cobalt提供安全保障。

根据9to5谷歌的一份报告，谷歌Chrome或至少早期的Chromium版本已经能够在早期版本的Google Fuchsia上运行。虽然Fuchsia还没有做好发布的准备，但这确实意味着这个新生代操作系统越来越接近可以使用的程度了。

最后，Fuchsia有希望成为迄今为止最好的跨设备操作系统。为实现这一目标，Fuchsia使用了GitHub社区称为“Ledger”的新工具。一旦您在Fuchsia设备上登录Google帐户，Ledger将自动在所有Fuchsia设备的所有已安装应用中保存您的位置。

总而言之，Fuchsia是谷歌将Chrome和Android中的最佳产品整合到同一个操作系统中的一次尝试，它在任何时候都会比以往高效，无论你是否正在使用它，更不用说跨平台使用了。

![](https://cdn.mos.cms.futurecdn.net/fxydjj4gT6cVRrcndtYnSF-650-80.jpg)
Google I/O大会可能就是今后Fuchsia亮相的地方

## Google Fuchsia发布日期
自2016年8月以来，我们已经看到大量关于Google Fuchsia发布日期的传言——但都被证明是假的。这些谣言通常出现在谷歌在加利福尼亚举行的Google大型IO开发者活动之前，或者当我们获悉大型硬件版本发布即将来临时。

早在二月份，据透露，谷歌前安卓平台安全负责人Nick Kralevich已离开Android团队，在Fuchsia部门“定义安全”。Kralevich将其描述为“新的实验性的操作系统”，但并没有向我们展示Fuchsia任何特定的启动窗口，但这确实显示了谷歌选择将Fuchsia置于其最重要资源的位置。

现在谷歌的Pixel活动已经过去了，所以你不应期待Google Fuchsia很快就会出现。该猜测指出，Fuchsia将在未来三年内在智能家居设备上运行，并在未来五年内完全公开发布。然而，这似乎是一个不太可信的谣言——如果我们看到它在2024年之前发布（或Android系统），我们会感到非常惊讶。

无论如何，当接近可能的发布日期时，请锁定该此页面上，我们会为您提供一些关于Fuchsia的重要信息。

![](https://cdn.mos.cms.futurecdn.net/Yzh9gjppGL6MBnWbE2QTVd-650-80.jpg)

Fuchsia会是Android的终结者吗？

## Fuchsia对于Android和Chrome以及Windows和macOS有什么意义？

舆论称Google Fuchsia是谷歌对微软和苹果联合平台的回应。无论是将Android变成两大智能手机平台之一，还是后来推广Chrome操作系统——更不用说谷歌基于网络的生产力计划G-Suite，谷歌俨然已经成为所有平台上的主要参与者。

从谷歌透露出的消息来看，谷歌正着手完成微软和苹果拥有的Windows 10，iOS和macOS High Sierra的大部分内容。当然，是以非常“Google”的方式完成的。您可以轻松地获得Google无与伦比的搜索和数据跟踪功能——Google智能助理和'entities'，以及一个不断发展的用户界面，以满足访问其设备的需求。这些是Fuchsia比微软和Apple的产品更具吸引力的的宣传点。

Fuchsia最终会意味着Android和Chrome的终结吗？在名义上，这确实很有可能，但它们的设计原则几乎肯定会存在——有太多基础性的功能，无法建立在它们之上，只需看看在最近两个版本的Fuchsia的早期版本中找到的Material设计语言，就能略知一二。

最终结果可能会在今年晚些时候的预览版或2019年的可购买的设备中看到，这将是谷歌最担心的一个平台。借助Fuchsia，Google将能够同时向所有版本推送新的更新和功能，从而简化支持以及用户使用。

有了Fuchsia，谷歌将成为微软和苹果公司的一个更强大的敌人，这对Android和Chromebook用户来说是一个非常诱人的选择。谁知道呢，或许这足以让人们从微软和Apple产品阵营中投入Fuchsia的怀抱。

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Joe Osborne； 译者：[Arktische](https://github.com/Arktische) ；校对：[bootingman](https://github.com/bootingman)      
原文链接：https://www.techradar.com/news/google-fuchsia        
本文链接：https://fuchsia-china.com/google-fuchsia-os-rumors/
