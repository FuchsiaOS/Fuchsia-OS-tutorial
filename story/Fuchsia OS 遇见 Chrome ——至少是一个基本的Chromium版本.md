# Fuchsia OS 遇见 Chrome ——至少是一个基本的Chromium版本

![](https://camo.githubusercontent.com/eaff5e7fb481d44d1129416710ef4d6ac38ba0cc/68747470733a2f2f39746f35676f6f676c652e636f6d2f77702d636f6e74656e742f75706c6f6164732f73697465732f342f323031382f30392f6368726f6d69756d2d667563687369612d6865616465722e6a7067)

谷歌长期以来一直在努力让他们的Chromium浏览器在即将推出的Fuchsia OS上运行。现在，我们可以看到这些努力的第一批成果，亲身体验为Fuchsia打造的Chromium浏览器。

到目前为止，Fuchsia上最基本的网络浏览体验是由Webkit提供支持。正如我们在四月份看到的Fuchsia 5分钟预览视频中了解的那样，这个过于简易的浏览器使得很多网页看起来——非常过时。

我们知道谷歌一直在试图将Chromium移植到各种平台上，包括浏览器本身和支持Chromecast的“Cast Shell”，它在Fuchsia已经运行了一段时间了。特别是应用程序"Web Runner"，我们可以看到最近谷歌做了不少工作。

Web Runner是用于Fuchsia的Chromium的专用版本，它不具有像我们熟知的Chrome那样的标准UI界面，它似乎主要用于在其他应用程序中嵌入网页，或者用于渐进式web应用。

今天，我终于能在运行着Fuchsia的Pixelbook上安装和使用Web Runner，并且进行了真正的测试。这使我我非常兴奋，下面是一个快速预览视频。

（说明：该视频届时将上传到网站服务器上）

 **Chromium在Fuchsia上能正常工作吗？**

绝对可以。我能够访问和使用Google搜索，Twitter，甚至Google文档等完整版本的网站。
  
![alt](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/09/chromium-fuchsia-google-search.png?zoom=1.5&w=663&h=442&quality=82&strip=all&ssl=1)
 <table>
    <tr>
        <td ><center><img src="https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/09/chromium-fuchsia-twitter2.png?zoom=1.5&w=329&h=219&quality=82&strip=all&ssl=1" ></center></td>
        <td ><center><img src="https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/09/chromium-fuchsia-google-docs2.png?zoom=1.5&w=329&h=219&quality=82&strip=all&ssl=1"  ></center></td>
    </tr>
</table>

 ![](https://i1.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/09/chromium-fuchsia-user-agent2.png?zoom=1.5&w=996&h=664&quality=82&strip=all&ssl=1)
 这些网站均认为访问来自于Chrome 71的开发版本。

**我应该用Chromium吗？**

  考虑到真正拥有Fuchsia并运行在Pixelbook上的人很少，至少可以说，这个问题并不太重要。但如果一定要给一个答案，那回答就是：还没到时候。

要在Fuchsia上使用Web Runner，您需要从其源代码构建Chromium，这个过程需要使用Linux，并且在我的笔记本电脑上花费了漫长的时间才完成。有迹象表明，未来的Fuchsia版本可能很快就会包含预置的Chromium Web Runner。但即使这样，就算你完成所有设置，你仍需要使用终端打开浏览器转到特定页面，因为Web Runner没有任何像chrome那样的UI界面来与之交互。

您可能还在今天的屏幕截图中注意到用户体验已大大简化。这是因为我们称之为Armadillo的UI目前不是默认的。这意味着所有程序都需要以相同的方式从终端打开。
![](https://9to5google.com/wp-content/uploads/sites/4/2018/09/chromium-fuchsia-terminal2.png?resize=1500,1000)
有时Web Runner反应迟钝，因而在这个浏览器上打字非常笨拙。更不用说一些网页会随机让浏览器完全崩溃。起初，我试图从Web Runner写下这篇文章，但我很快发现这个任务有多么不愉快。

虽然这项工作肯定还处于早期阶段，但在一个刚刚起步的操作系统上运行完整的Chromium Web浏览器是一项令人难以置信的壮举。很明显，准备好推出Fuchsia是Google的首要任务，我们可能会看到更多的产品在未来几个月内被移植并稳定下来。
***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Joe Osborne； 译者：[Arktische](https://github.com/Arktische)；校对： [HugoFun](https://github.com/HugoFun)       
原文链接：https://9to5google.com/2018/09/17/fuchsia-os-meet-chromium-video/        
本文链接：https://fuchsia-china.com/×××（发布后替换）