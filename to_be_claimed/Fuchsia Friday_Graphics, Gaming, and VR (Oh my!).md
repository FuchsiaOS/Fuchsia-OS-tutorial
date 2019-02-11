
#Fuchsia Friday: Graphics, Gaming, and VR (Oh my!)
![](https://i1.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/04/fuchsia-friday-graphics.png)

Fuchsia Friday is back with your fix of Fuchsia information. This week, we’re looking at how Fuchsia handles graphics differently and what that might mean for gaming and VR.

Most operating systems have a window manager, which takes the visuals of multiple running apps and combines them into one organized view on your monitor. All of today’s traditional window managers, including those for Windows, OS X and Linux, work on the principle of composition. Usually, this means every window is rendered off-screen, and the operating system layers all of the visible windows and basic UI elements (like the taskbar and your desktop background) to create a 2D image for your monitor.

Fuchsia’s graphics engine, Scenic, instead creates a 3D scene, representing everything happening on your computer, then uses a virtual “camera” to create a 2D representation. This is very similar to how modern game engines work. Doing it this way makes a great deal of sense when you consider Material Design. The goal of Material is to feel like stacks of paper. What better way to demonstrate this than to actually stack cards in 3D?

The best part is that Flutter, Fuchsia’s primary app development tool (and subject of a previous Fuchsia Friday), specializes in Material Design and talks directly to Scenic. Thus, as a developer, you shouldn’t have to think about how everything will work in 3D.

But Material Design isn’t the only reason for this fundamental change. Soon, Scenic will have support for what it’s calling “stereo cameras.” What this means is there can be two views into the same scene. Each camera can also be independently moved or turned for a different view. The most obvious reason for this capability is virtual reality. Stereo camera support is an extremely new and experimental change, so it’s hard to say what the Fuchsia Team themselves will do, but implementing it directly in the OS should make it easier for developers to create VR experiences for Fuchsia. Needless to say I’ll be keeping an eye out for more changes on this front.

As a matter of fact, in the coming days, a stereo camera demo should be made available. When it does, I’ll update this post with a video.

To power Fuchsia’s rich 3D experience, Google could have tapped the tried and tested OpenGL, the industry standard for cross-platform 3D graphics for decades. Instead, the Fuchsia team have chosen to rely solely on Vulkan, a relative newcomer to the field and successor to OpenGL. One likely factor of this decision is that OpenGL and Vulkan are both developed by the Khronos Group, of which Google is a member. Another is that Vulkan allows more “bare metal” access to the GPU, to stretch performance. To give some perspective of the potential advantages of using Vulkan, PCGamer did some benchmark tests with the game Doom under both OpenGL and Vulkan, finding performance increases up to 35%.

Because of the choice to use Vulkan, Fuchsia has found an ally in an unlikely place. Valve (also a member of the Khronos Group) has been working with game developers to move away from a reliance on Windows. In doing so, they’ve decided to back Vulkan as the best way to drive compatibility, including investing in OS X and iOS support. With Valve’s influence on the game industry and push for Vulkan-based games, Fuchsia may find itself as a gaming platform. Google has long been rumored to be eyeing the gaming market, going so far as to hire gaming industry veteran Phil Harrison.

It’s impossible to tell now what the future holds for Fuchsia’s role in gaming. It’s clear, however, by their desire to implement it at this early stage, that VR is a first-class citizen on Fuchsia.

Finally, a note to our readers. Over the next few days, I’ll be making updates to past Fuchsia Friday articles (and this one!), to include more images and video examples. Keep an eye on Twitter for specifics. And as always, if you have any questions about how Fuchsia will work, reach out in the comments or on Twitter. You may find your answers in a future article!

Fuchsia Friday is a weekly series where we dive into the Fuchsia source code and interpret what the current state of the OS might mean for the finished product. All information in this article is speculation based on available information and is subject to change.

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：（替换为译者名字和作者地址）；校对： （替换为译者名字和作者地址）       
原文链接：https://9to5google.com/2018/04/06/fuchsia-friday-graphics-gaming-and-vr-oh-my/       
本文链接：https://fuchsia-china.com/×××（发布后替换）
