
![](https://9to5google.com/wp-content/uploads/sites/4/2018/09/chromium-fuchsia-header.jpg)

Google has long been at work trying to get their Chromium web browser up and running on their upcoming, work-in-progress Fuchsia operating system. We now get to see the first fruits of that effort, with a hands-on look at Chromium for Fuchsia.

Up until now, the minimally-available web browsing experience on Fuchsia was powered by WebKit. As we demonstrated in our First 5 Minutes of Fuchsia preview back in April, this simple browser made many web pages look… extremely dated.

We’ve known that Google has been trying to get different pieces of Chromium, including the browser itself and the ‘Cast Shell’ that powers Chromecast, running on Fuchsia for quite some time now. One application in particular, ‘Web Runner’, has been seeing a great deal of work lately.

Web Runner is a specialized version of Chromium for Fuchsia that has none of the standard UI surrounding the web page itself, known as ‘browser chrome’, and it seems to rather be primarily designed for embedding web pages in other applications, or for use with progressive web apps.

(For a better understanding of what we know about Web Runner, be sure to check out our Fuchsia Friday about the web and its place in the Fuchsia ecosystem.)

Today, I was finally able to install and use Web Runner on my Pixelbook running Fuchsia and really put it to the test. And I couldn’t be more excited. Here’s a quick look:

![]()
（说明：该视频届时将上传到网站服务器上）

Does Chromium on Fuchsia really work?

Absolutely. I was able to access and use the full versions of sites like Google Search, Twitter, and even Google Docs.

chromium-fuchsia-google-search
chromium-fuchsia-twitter
chromium-fuchsia-google-docs
For all intents and purposes, websites believe this is a development build of Chrome 71

Should I use it?

This question isn’t all too relevant considering that the number of people that actually have Fuchsia up and running a Pixelbook is… small, to say the least. But still, the answer:

Not yet.

To use Web Runner on Fuchsia, you need to build Chromium from its source, a process which requires Linux and took an untold number of hours to complete on my laptop. There are signs that future Fuchsia builds may include a pre-built copy of Chromium’s Web Runner soon. But even then, once you have it all set up, you need to use the terminal to open the browser to any specific page, because Web Runner doesn’t have any browser chrome to interact with.

You may have also noticed in today’s screenshots that the user experience has been drastically simplified. This is because the UI we came to know as Armadillo is, at least for now, not the default. This means all programs need to be opened from the terminal, in the same way.

Sometimes things feel unresponsive, and the browser is very clunky for typing. Not to mention some webpages will completely crash the browser at random. I had, at first, attempted to write this entire post from Web Runner, and quickly found how unpleasant that task would be.

While things are definitely still in the early stages, getting a full-scale web browser Chromium up and running on a fledgling operating system is an incredible feat. It’s clear that getting Fuchsia ready to be usable is a priority for Google, and we’ll likely see more of its products get ported over and stabilized in the coming months.

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Joe Osborne； 译者：（替换为译者名字和作者地址）；校对： （替换为译者名字和作者地址）       
原文链接：https://9to5google.com/2018/09/17/fuchsia-os-meet-chromium-video/        
本文链接：https://fuchsia-china.com/×××（发布后替换）
